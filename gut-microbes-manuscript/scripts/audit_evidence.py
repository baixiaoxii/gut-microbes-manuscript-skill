#!/usr/bin/env python3
"""Audit a normalized manuscript evidence manifest without filling gaps."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CRITICAL_METHODS = (
    "sample_collection",
    "extraction",
    "assay_or_sequencing",
    "bioinformatics",
    "statistics",
)


def is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, dict)):
        return not value
    return False


def audit(data: dict, mode: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    manuscript = data.get("manuscript", {})
    study = data.get("study", {})
    methods = data.get("methods", {})
    results = data.get("results", [])
    claims = data.get("claims", [])

    for field in ("study_type", "research_question"):
        if is_missing(manuscript.get(field)):
            errors.append(f"manuscript.{field} is missing")

    groups = study.get("groups", [])
    if not groups:
        errors.append("study.groups is missing")
    else:
        for index, group in enumerate(groups, start=1):
            if is_missing(group.get("name")):
                errors.append(f"study.groups[{index}].name is missing")
            n_value = group.get("n")
            if not isinstance(n_value, int) or n_value <= 0:
                errors.append(f"study.groups[{index}].n must be a positive integer")

    for field in CRITICAL_METHODS:
        if is_missing(methods.get(field)):
            errors.append(f"methods.{field} is missing")

    if not results:
        errors.append("results is empty")

    result_ids: set[str] = set()
    for index, result in enumerate(results, start=1):
        result_id = str(result.get("id", "")).strip()
        if not result_id:
            errors.append(f"results[{index}].id is missing")
            continue
        if result_id in result_ids:
            errors.append(f"duplicate result id: {result_id}")
        result_ids.add(result_id)
        for field in ("statement", "sample_size", "source"):
            if is_missing(result.get(field)):
                errors.append(f"result {result_id}.{field} is missing")
        for field in ("effect", "uncertainty", "p_value"):
            if is_missing(result.get(field)):
                warnings.append(f"result {result_id}.{field} is missing or not applicable")

    claim_ids: set[str] = set()
    allowed_strengths = {"description", "association", "prediction", "mediation", "causal"}
    for index, claim in enumerate(claims, start=1):
        claim_id = str(claim.get("id", "")).strip()
        if not claim_id:
            errors.append(f"claims[{index}].id is missing")
            continue
        if claim_id in claim_ids:
            errors.append(f"duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)
        supported_by = claim.get("supported_by", [])
        if not supported_by:
            errors.append(f"claim {claim_id} has no supporting result")
        for result_id in supported_by:
            if result_id not in result_ids:
                errors.append(f"claim {claim_id} references unknown result {result_id}")
        strength = claim.get("strength")
        if strength not in allowed_strengths:
            errors.append(f"claim {claim_id}.strength must be one of {sorted(allowed_strengths)}")

    ethics = study.get("ethics", {})
    if ethics.get("required") is True and is_missing(ethics.get("approval_id")):
        errors.append("study.ethics.approval_id is required")

    serialized = json.dumps(data, ensure_ascii=False)
    if mode == "submission-ready":
        if "AUTHOR INPUT REQUIRED" in serialized:
            errors.append("submission-ready manifest contains author-input placeholders")
        if is_missing(study.get("data_accession")):
            warnings.append("study.data_accession is missing; confirm not applicable or restricted")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to evidence JSON")
    parser.add_argument("--mode", choices=("draft", "submission-ready"), default="draft")
    args = parser.parse_args()

    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read manifest: {exc}", file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print("ERROR: manifest root must be a JSON object", file=sys.stderr)
        return 2

    errors, warnings = audit(data, args.mode)
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    print(f"SUMMARY: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
