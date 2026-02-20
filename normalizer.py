import json
import difflib

def load_counties():
    with open("data/counties.json") as f:
        return json.load(f)

def normalize_county_name(raw_name: str, counties: list) -> dict:
    names = [c["name"] for c in counties]

    match = difflib.get_close_matches(raw_name, names, n=1, cutoff=0.6)
    if not match:
        raise ValueError(f"Unknown county: {raw_name}")

    for c in counties:
        if c["name"] == match[0]:
            return c
