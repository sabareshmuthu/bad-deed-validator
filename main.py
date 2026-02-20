from llm_parser import parse_deed_with_llm
from normalizer import load_counties, normalize_county_name
from validators import validate_dates, validate_amounts, parse_digits

RAW_TEXT = """*** RECORDING REQ ***
Doc: DEED-TRUST-0042
County: S. Clara  |  State: CA
Date Signed: 2024-01-15
Date Recorded: 2024-01-10
Grantor:  T.E.S.L.A. Holdings LLC
Grantee:  John  &  Sarah  Connor
Amount: $1,250,000.00 (One Million Two Hundred Thousand Dollars)
APN: 992-001-XA
Status: PRELIMINARY
*** END ***"""

def main():
    deed = parse_deed_with_llm(RAW_TEXT)

    counties = load_counties()
    county_info = normalize_county_name(deed["county"], counties)

    # Paranoid checks
    validate_dates(deed["date_signed"], deed["date_recorded"])
    validate_amounts(deed["amount_digits"], deed["amount_words"])

    amount = parse_digits(deed["amount_digits"])
    tax = amount * county_info["tax_rate"]

    print("Deed is valid ")
    print("County:", county_info["name"])
    print("Computed tax:", tax)

if __name__ == "__main__":
    main()
