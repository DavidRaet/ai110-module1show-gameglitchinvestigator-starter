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
