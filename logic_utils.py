def get_range_for_difficulty(difficulty: str):
    """
    Returns the low and high bounds of the difficulty based on the
    selected difficulty level.

    Args:
        difficulty (str): The difficulty level selected by the user.
            Expected values are "Easy", "Normal", or "Hard".

    Returns:
        tuple: A tuple containing the low and high bounds

    Example:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500


def parse_guess(raw: str):
    """
    Parses the user's guess and validates it.

    Args:
        raw (str): The raw input from the user.

    Returns:
        tuple: A tuple containing a boolean indicating if the guess is
            valid, the parsed integer guess (or None if invalid), and
            an error message (or None if valid).

    Raises:
        ValueError: If the input cannot be parsed as a non-negative integer.

    Example:
        >>> parse_guess("5")
        (True, 5, None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
            if value < 0:
                return False, None, "Guess must be a non-negative number."
        else:
            value = int(raw)
            if value < 0:
                return False, None, "Guess must be a non-negative number."
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Checks the user's guess against the secret number. Returns whether
    the guess is correct, too high, or too low, along with an
    appropriate message.

    Args:
        guess (int): The user's guess.
        secret (int): The secret number.

    Returns:
        tuple: A tuple containing the outcome ("Win", "Too High", or
            "Too Low") and a message.

    Example:
        >>> check_guess(5, 10)
        ("Too Low", "📈 Go HIGHER!")
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Updates the player's score based on the outcome of their guess.

    Args:
        current_score (int): The player's current score before this guess.
        outcome (str): The outcome of the guess, which can be "Win",
            "Too High", or "Too Low".
        attempt_number (int): The number of attempts the player has
            made so far (starting from 1).

    Returns:
        int: The updated player score.

    Example:
        >>> update_score(100, "Win", 1)
        90
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
