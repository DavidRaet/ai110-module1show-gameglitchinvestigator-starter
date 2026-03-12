# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
python -m streamlit run app.py

# Run tests
pytest
```

## Project Overview

This is a Python/Streamlit number guessing game used as a learning exercise in debugging and refactoring. The project has two phases:

1. **Fix intentional bugs in `app.py`** — the app is deliberately broken for students to diagnose and repair.
2. **Refactor logic into `logic_utils.py`** and make `pytest` tests pass.

## Architecture

- `app.py` — Streamlit UI plus (currently) all game logic functions. Manages game state via `st.session_state`.
- `logic_utils.py` — Stub file where the four logic functions should be moved: `get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`. All stubs currently raise `NotImplementedError`.
- `tests/test_game_logic.py` — Pytest tests that import from `logic_utils` (not `app.py`). Tests call `check_guess(guess, secret)` and expect it to return a plain string (`"Win"`, `"Too High"`, `"Too Low"`), **not** a tuple.

## Known Intentional Bugs

- **Inverted hints**: In `app.py`, `check_guess` returns `"📈 Go HIGHER!"` when `guess > secret` (should say "Go LOWER") and `"📉 Go LOWER!"` when `guess < secret` (should say "Go HIGHER").
- **Type coercion bug**: On even-numbered attempts, the secret is cast to a string before being passed to `check_guess`, causing string vs. int comparisons that break the win condition.
- **Hard difficulty range**: `get_range_for_difficulty` returns `1–50` for "Hard" but the UI displays `1–100` (hardcoded in `st.info`).

## Refactor Contract

When moving functions to `logic_utils.py`, the tests expect `check_guess` to return **only the outcome string**, not the `(outcome, message)` tuple that `app.py` currently uses. `app.py` will need to be updated to call `logic_utils` functions after the refactor.
