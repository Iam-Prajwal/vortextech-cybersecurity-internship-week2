
import string

MIN_LENGTH = 8
STRONG_LENGTH_BONUS = 12

COMMON_PASSWORD_BLACKLIST = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "admin",
    "abc123",
    "welcome",
    "password123",
}

SPECIAL_CHARACTERS = set(string.punctuation)



def has_minimum_length(password: str, min_length: int = MIN_LENGTH) -> bool:
    """Return True if the password meets the minimum length requirement."""
    return len(password) >= min_length


def has_bonus_length(password: str, bonus_length: int = STRONG_LENGTH_BONUS) -> bool:
    """Return True if the password is long enough to earn a length bonus."""
    return len(password) >= bonus_length


def has_uppercase(password: str) -> bool:
    """Return True if the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    """Return True if the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    """Return True if the password contains at least one digit."""
    return any(char.isdigit() for char in password)


def has_special_character(password: str) -> bool:
    """Return True if the password contains at least one special symbol."""
    return any(char in SPECIAL_CHARACTERS for char in password)


def is_blacklisted(password: str, blacklist: set = COMMON_PASSWORD_BLACKLIST) -> bool:
    """Return True if the password (case-insensitive) is a known weak password."""
    return password.lower() in blacklist


# --------------------------------------------------------------------------
# Core evaluation logic
# --------------------------------------------------------------------------

def evaluate_password(password: str) -> dict:
    """
    Run every check against the password and calculate a strength score.
    """
    checks = {
        "min_length": has_minimum_length(password),
        "bonus_length": has_bonus_length(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "digit": has_digit(password),
        "special": has_special_character(password),
        "blacklisted": is_blacklisted(password),
    }

    if checks["blacklisted"]:
        score = 0
    else:
        score = sum([
            checks["min_length"],
            checks["bonus_length"],
            checks["uppercase"],
            checks["lowercase"],
            checks["digit"],
            checks["special"],
        ])

    strength = score_to_strength(score)
    feedback = generate_feedback(checks)

    return {
        "password": password,
        "checks": checks,
        "score": score,
        "strength": strength,
        "feedback": feedback,
    }


def score_to_strength(score: int) -> str:
    """Convert a numeric score (0-6) into a human-readable strength label."""
    if score == 0:
        return "Very Weak"
    elif score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:  # score == 6
        return "Very Strong"


def generate_feedback(checks: dict) -> list:
    """Build a list of personalized suggestions based on failed checks."""
    feedback = []

    if checks["blacklisted"]:
        feedback.append("✗ This is a commonly leaked/guessed password — avoid it entirely")

    if not checks["min_length"]:
        feedback.append("✓ Increase password length to at least 8 characters")
    elif not checks["bonus_length"]:
        feedback.append("✓ Consider using 12+ characters for extra strength")

    if not checks["uppercase"]:
        feedback.append("✓ Add uppercase letters")

    if not checks["lowercase"]:
        feedback.append("✓ Add lowercase letters")

    if not checks["digit"]:
        feedback.append("✓ Add numbers")

    if not checks["special"]:
        feedback.append("✓ Add special symbols (e.g. ! @ # $ %)")

    if not feedback:
        feedback.append("✓ Great job! No further improvements needed.")

    return feedback


def display_result(result: dict) -> None:
    """Print a formatted summary of the password evaluation to the terminal."""
    masked_password = mask_password(result["password"])

    print("-" * 45)
    print(f"Password Analyzed : {masked_password}")
    print(f"Strength Rating    : {result['strength']}")
    print(f"Score              : {result['score']} / 6")
    print("Feedback:")
    for line in result["feedback"]:
        print(f"  {line}")
    print("-" * 45)


def mask_password(password: str) -> str:
    """Mask a password for safe display, showing only the first character."""
    if len(password) <= 1:
        return "*" * len(password)
    return password[0] + "*" * (len(password) - 1)


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def main() -> None:
    """Prompt the user for a password and display its strength evaluation."""
    password = input("Enter a password to check its strength: ")
    result = evaluate_password(password)
    display_result(result)


if __name__ == "__main__":
    main()
