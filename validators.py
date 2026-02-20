from datetime import datetime
import re
from word2number import w2n

def validate_dates(date_signed: str, date_recorded: str):
    ds = datetime.fromisoformat(date_signed)
    dr = datetime.fromisoformat(date_recorded)

    if dr < ds:
        raise ValueError(
            f"Invalid dates: recorded ({date_recorded}) before signed ({date_signed})"
        )

def parse_digits(amount_str: str) -> int:
    cleaned = re.sub(r"[^\d.]", "", amount_str)
    return int(float(cleaned))

def validate_amounts(amount_digits: str, amount_words: str):
    digits_value = parse_digits(amount_digits)
    words_value = w2n.word_to_num(amount_words.lower())

    if digits_value != words_value:
        raise ValueError(
            f"Amount mismatch: digits={digits_value}, words={words_value}"
        )
