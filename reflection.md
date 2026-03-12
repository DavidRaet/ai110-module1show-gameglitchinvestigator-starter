# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Pressing enter after submitting your guess does not work 
- the hint contradicts itself; tells you to go lower, when you should be going higher and vice versa
- changing between difficulties does not change the description of which range of numbers to guess on 
e.g (picking Easy should change the description "Guess a number between 1 and 20. Attempts left: 6" but stays "Guess a number between 1 and 100. Attempts left: 6")
- I don't know if this should be considered a bug but having a negative score
- guessing the secret does not result in successfully guessing the number
(the secret is not being saved) 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project, I used both Github Copilot and Claude Code to refactor two changes:

- Github Copilot to move the necessary util functions that were in the app file into logic_utils. The LLM 
was able to correctly move the necessary util functions into the logic_utils and removed them from the app.
I added guardrails into the instructions of the prompt by telling the LLM to not tamper or refactor the 
logic the functions in any way and only focus on moving them into the logic_utils file. 
- Claude Code was used to fix a bug where the enter key wouldn't allow the user to submit the guess. 
This was accomplished by putting Claude Code on planning mode by explaining what the bug was, the 
requirements for the implementation, and including test cases using Playwright that verify the bug 
was fixed. Because I put Claude Code on planning mode, I was able to thoroughly articulate what the goal
was for solving the bug before asking it to add its implementations. Additionally, I ran the tests 
and verified the implementation worked on the webpage. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
When a bugged was really fixed, a subsequent test targetting the bug should either pass or fail depending on the type of test
write. For example, a conventional test for expected behavior or a "counter-test" that passes if the bug no longer exists (!bug)
On one bug that did not let users submit their guess using enter, I explained the bug to Claude Code in plan mode and helped devise a multi-step plan
that involved understanding the bug, implementing the fix, and writing a test that verified the fix. The model helped me better visualize what happens at
each step (from the client to the server) and with methodical steps, made the tests that it generated easier to understand and intuitive. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
