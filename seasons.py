from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_str = input("Date of Birth: ").strip()
    birth_date = parse_date(birth_str)
    print(minutes_in_words(birth_date))

def parse_date(s):
    try:
        year, month, day = map(int, s.split("-"))
        return date(year, month, day)
    except (ValueError, TypeError):
        sys.exit("Invalid date")

def minutes_since(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60


def minutes_in_words(birth_date):
    minutes = minutes_since(birth_date)
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"

if __name__ == "__main__":
    main()
