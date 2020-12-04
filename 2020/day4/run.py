import re
import sys

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

def validate_passport(passport):
    for field in REQUIRED_FIELDS:
        try:
            if not passport[field]:
                return False
        except:
            return False
    return True

def valid_field(field, value):
    if field == "byr":
        year = int(value)
        return year >= 1920 and year <= 2002
    elif field == "iyr":
        year = int(value)
        return year >= 2010 and year <= 2020
    elif field == "eyr":
        year = int(value)
        return year >= 2020 and year <= 2030
    elif field == "hgt":
        amount = int(value[:-2])
        unit = value[-2:]
        if unit == "cm":
            return amount >= 150 and amount <= 193
        elif unit == "in":
            return amount >= 59 and amount <= 76
    elif field == "hcl":
        return bool(re.match("^#[a-f0-9]{6}", value))
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        # Gotcha 2. We have to check the length of the pid
        # since the regex will match values longer than 9 characters.
        return len(value) == 9 and bool(re.match("^[0-9]{9}", value))

    return False


def validate_passport_and_fields(passport):
    for field in REQUIRED_FIELDS:
        try:
            value = passport[field]
            if not valid_field(field, value):
                return False
        except:
            return False
    return True

def main():
    # allow the map to be indexable
    passports = []
    current_passport = None
    for line in sys.stdin:
        l = line.strip()
        if l:
            # Instantiate the dict
            if current_passport is None:
                current_passport = {}
            parts = l.split(" ")
            for p in parts:
                [key, val] = p.split(":")
                current_passport[key] = val
        else:
            # Passport ended
            if current_passport is not None:
                passports.append(current_passport)
                current_passport = None

    # Gotcha 1. There's no newline character at the end
    # of the file so we have to manually add it.
    if current_passport is not None:
        # print("we still have a passport")
        # print(current_passport)
        passports.append(current_passport)

    print("part 1")
    valid_count = 0
    for p in passports:
        if validate_passport(p):
            valid_count += 1
    print(valid_count)

    print("part 2")
    valid_count_2 = 0
    for p in passports:
        if validate_passport_and_fields(p):
            valid_count_2 += 1
    print(valid_count_2)


if __name__ == "__main__":
    main()
