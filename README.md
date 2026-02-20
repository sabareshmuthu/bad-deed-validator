# Bad Deed Validator

## Overview

This project demonstrates a “trust but verify” pipeline for processing messy, OCR-scanned real estate deeds.

An LLM is used only for best-effort structure extraction from unclean text. All business, legal, and financial correctness is enforced by deterministic Python code. If any invariant is violated, the system fails closed and rejects the deed.

This is designed to prevent situations where a hallucinated or misparsed value could result in recording an invalid or fraudulent transaction.

---

## High-Level Flow

OCR Text  
→ LLM Parser (best-effort, untrusted)  
→ Deterministic Normalization + Validation  
→ ACCEPT (compute tax) or REJECT (error)

Key principle: The LLM is a parser, not a source of truth.

---

## What Is Validated (Deterministically)

- Date sanity  
  A document cannot be recorded before it is signed.

- Amount consistency  
  The numeric amount (e.g. $1,250,000.00) must match the amount written in words.

- County normalization  
  Fuzzy matching is used to map inputs like "S. Clara" to "Santa Clara" in order to look up the correct tax rate.

- Fail-closed behavior  
  Any inconsistency raises an error and the deed is rejected.

---

## Project Structure

bad-deed-validator/
- main.py              # Orchestrates the pipeline
- llm_parser.py        # LLM (or stub) → structured JSON
- validators.py        # Paranoid checks (dates, money, etc.)
- normalizer.py        # County normalization + tax lookup
- data/
  - counties.json      # Reference tax data
- tests/
  - test_validations.py
- requirements.txt
- README.md

---

## Setup

1. Create and activate a virtual environment

python3 -m venv venv  
source venv/bin/activate

2. Install dependencies

pip install -r requirements.txt

3. (Optional) LLM API Key

Create a .env file with:

OPENAI_API_KEY=sk-...

The system also supports a stub mode for local testing and demos.

---

## Running the Project

### A) Happy path (force stub, no LLM required)

source venv/bin/activate  
export USE_STUB=1  
python main.py

Expected output (example):

Using stub parser  
Deed is valid  
County: Santa Clara  
Computed tax: 15015.0

---

### B) Paranoid mode (real OCR input)

unset USE_STUB  
python main.py

With the provided sample OCR text, the system will reject the deed with errors such as:

- Recorded date before signed date
- Amount mismatch between digits and words

This demonstrates that the system does not trust the LLM or OCR and fails closed on inconsistencies.

---

## Running Tests

Always run tests using the venv Python:

python -m pytest

The tests cover:
- Date sanity validation
- Amount consistency validation

---

## Why This Design Is Safe

- The LLM is never trusted for correctness.
- All legal and financial invariants are enforced in code.
- Any inconsistency results in a hard failure.
- This prevents model hallucinations or OCR errors from corrupting critical records.

---

## Summary

This project shows how to safely combine:
- Fuzzy AI parsing for unstructured text
- With strict, deterministic validation for high-risk financial and legal data

So that no model error can silently produce an invalid or fraudulent record.

