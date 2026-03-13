import subprocess
import time
import pytest
from playwright.sync_api import Page, expect

PORT = 8502


@pytest.fixture(scope="session", autouse=True)
def streamlit_server():
    proc = subprocess.Popen(
        [
            "python", "-m", "streamlit", "run", "app.py",
            "--server.headless=true",
            f"--server.port={PORT}",
        ]
    )
    time.sleep(4)  # wait for Streamlit to start
    yield
    proc.terminate()
    proc.wait()


def test_enter_key_submits_guess(page: Page):
    page.goto(f"http://localhost:{PORT}")
    page.get_by_label("Enter your guess:").fill("50")
    page.keyboard.press("Enter")
    # After submission a hint (warning), win (success), or loss (error) appears
    expect(page.locator(".stAlert").first).to_be_visible(timeout=6000)


def test_submit_button_submits_guess(page: Page):
    page.goto(f"http://localhost:{PORT}")
    page.get_by_label("Enter your guess:").fill("50")
    page.get_by_role("button", name="Submit Guess 🚀").click()
    expect(page.locator(".stAlert").first).to_be_visible(timeout=6000)


def test_high_guess_shows_go_lower_hint(page: Page):
    page.goto(f"http://localhost:{PORT}")
    page.get_by_label("Enter your guess:").fill("999")
    page.get_by_role("button", name="Submit Guess 🚀").click()
    expect(page.locator(".stAlert", has_text="Go LOWER!")).to_be_visible(timeout=6000)


def test_low_guess_shows_go_higher_hint(page: Page):
    page.goto(f"http://localhost:{PORT}")
    page.get_by_label("Enter your guess:").fill("0")
    page.get_by_role("button", name="Submit Guess 🚀").click()
    expect(page.locator(".stAlert", has_text="Go HIGHER!")).to_be_visible(timeout=6000)


def _get_secret(page: Page) -> int:
    """Returns the current secret number from the Developer Debug Info expander.

    Closes and reopens the expander to ensure fresh DOM state after reruns.
    Initially, there was a testing issue being investigated on test_secret_changes_on_new_game
    where the secret value was stagnant even after clicking New Game. This was due to 
    
    """
    expander = page.locator("details").filter(has_text="Developer Debug Info")
    # Close the expander if it's open to reset state
    if expander.evaluate("el => el.open"):
        expander.locator("summary").click()
    # Reopen the expander to guarantee fresh DOM elements
    expander.locator("summary").click()
    
    secret_locator = page.get_by_text("Secret:").first
    expect(secret_locator).to_be_visible(timeout=3000)

    raw = secret_locator.text_content()
    return int(raw.split("Secret:")[-1].strip())


def test_secret_does_not_change_on_submit(page: Page):
    page.goto(f"http://localhost:{PORT}")

    secret_before = _get_secret(page)

    # Submit a guess guaranteed not to win (0 is below every difficulty range)
    page.get_by_label("Enter your guess:").fill("0")
    page.get_by_role("button", name="Submit Guess 🚀").click()
    # Wait for the rerun to complete — an alert appears after every valid submission
    expect(page.locator(".stAlert").first).to_be_visible(timeout=6000)

    secret_after = _get_secret(page)

    assert secret_before == secret_after, (
        f"Secret changed from {secret_before} to {secret_after} after submitting a guess."
    )


def test_secret_changes_on_new_game(page: Page):
    page.goto(f"http://localhost:{PORT}")
    
    # Submit one guess first so we are mid-game when New Game is clicked
    page.get_by_label("Enter your guess:").fill("0")
    page.get_by_role("button", name="Submit Guess 🚀").click()
    expect(page.locator(".stAlert").first).to_be_visible(timeout=6000)

    secret_before = _get_secret(page)

    page.get_by_role("button", name="New Game 🔁").click()
    # After New Game, attempts resets to 1 so the banner returns to "Attempts left: 7".
    # Waiting for this specific text is a reliable signal the st.rerun() has completed.
    expect(page.get_by_text("Attempts left: 7")).to_be_visible(timeout=6000)

    secret_after = _get_secret(page)

    # There is a 1-in-100 chance of a false negative if the same number is redrawn.
    assert secret_before != secret_after, (
        f"Secret did not change after clicking New Game "
        f"(was {secret_before}, still {secret_after})."
    )
    