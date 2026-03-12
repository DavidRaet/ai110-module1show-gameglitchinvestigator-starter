# Game Glitch Investigator — Project Guidelines

## Build and Test

```bash
pip install -r requirements.txt   # install dependencies
python -m streamlit run app.py    # launch the app (localhost:8501)
pytest                            # run all tests
```

## Architecture

| File | Role |
|------|------|
| `app.py` | Streamlit UI; manages all game state via `st.session_state` |
| `logic_utils.py` | Four pure game-logic functions imported by both `app.py` and tests |
| `tests/test_game_logic.py` | Pytest tests — import only from `logic_utils`, never from `app.py` |

The four logic functions that live in `logic_utils.py`:
- `get_range_for_difficulty(difficulty)` → `(low, high)`
- `parse_guess(raw)` → `(ok, int_or_None, err_or_None)`
- `check_guess(guess, secret)` → plain outcome string only: `"Win"`, `"Too High"`, or `"Too Low"`
- `update_score(current_score, outcome, attempt_number)` → `int`

## Critical Conventions

**`check_guess` return type**: Tests expect a **plain string**, not a tuple. `app.py` calls `check_guess` and must handle the string itself to produce hint messages. Do not change the return type back to a tuple.

**Streamlit state**: All mutable game state (`secret`, `attempts`, `score`, `status`, `history`) lives in `st.session_state`. Never re-assign these outside of an explicit user action (form submit or "New Game" button) to avoid values resetting on every re-render.

**Type safety in comparisons**: Always compare `guess` and `secret` as the same type (`int`). The type-coercion bug (casting `secret` to `str` on even attempts) is an *intentional* exercise bug — do not reintroduce it.

## Known Intentional Bugs (Learning Exercise)

These bugs exist on purpose for students to find and fix:
1. **Inverted hints** — `check_guess` says "Go HIGHER" when guess > secret (should say "Go LOWER").
2. **Type coercion bug** — even-numbered attempts cast `secret` to `str`, breaking comparisons.
3. **Hard difficulty range** — `get_range_for_difficulty("Hard")` returns `1–50` but the UI label says `1–100`.
4. **Score formula** — win score uses `attempt_number + 1` instead of `attempt_number`.
5. **Attempt counter init** — `attempts` initialises to `1` but resets to `0` on new game.

## Tests

- `tests/test_game_logic.py` — unit tests for `check_guess`; pass when the function returns plain strings.
- `tests/test_ui.py` — Playwright UI tests (requires `playwright install` to run).
- `conftest.py` — currently empty; add shared fixtures here if needed.
