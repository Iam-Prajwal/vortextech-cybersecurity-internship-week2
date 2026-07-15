
from password_checker import evaluate_password, display_result

TEST_PASSWORDS = [
    "123456",              # Blacklisted -> Very Weak
    "qwerty",              # Blacklisted -> Very Weak
    "abcdefg",             # 7 chars, lowercase only -> Weak
    "abcdefgh",             # 8 chars, lowercase only -> Weak
    "abcdefgh1",            # 9 chars, lower + digit -> Medium
    "Abcdefgh1",            # 9 chars, upper+lower+digit -> Medium
    "Abcdefgh1!",           # 10 chars, all 4 types -> Strong
    "Abcdefghij1!",         # 12 chars, all 4 types + length bonus -> Very Strong
]

if __name__ == "__main__":
    for pwd in TEST_PASSWORDS:
        result = evaluate_password(pwd)
        print(f"\nInput Password     : {pwd}")
        display_result(result)
