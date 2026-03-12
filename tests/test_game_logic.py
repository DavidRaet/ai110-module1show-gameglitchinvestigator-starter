from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    userGuessResult, message = check_guess(50, 50)
    assert userGuessResult == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    userGuessResult, message = check_guess(60, 50)
    assert userGuessResult == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    userGuessResult, message = check_guess(40, 50)
    assert userGuessResult == "Too Low"
