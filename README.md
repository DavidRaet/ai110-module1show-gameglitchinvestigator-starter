# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
The once "Impossible Guesser" after fixing the bugs is a game that prompts the user to guess a secret number. If you decide to show hints, 
you will be prompted to guess higher since your guess was lower than the secret and vice versa. 
- [X] Detail which bugs you found.
Some of the most significant bugs that were found in this game were the secret always being changed after the user submitted the guess, clicking new game
making the game unplayable, and the hint initially contradicting itself (go higher when your guess was too high and vice versa)
- [ ] Explain what fixes you applied.
I applied all fixes to the bugs above through rigorous refactoring and testing with the assistance of AI. Additionally, I fixed
client facing bugs such as the difficulty ranges being hardcoded and the attempts-left-number not being changed after the first click. 
## 📸 Demo

- [X] [Insert a screenshot of your fixed, winning game here]
![Fixed Game](https://image2url.com/r2/default/images/1773446589932-aaac845b-5575-4b7a-871c-ea52b4b68fa2.png)
## 🚀 Stretch Features
- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
