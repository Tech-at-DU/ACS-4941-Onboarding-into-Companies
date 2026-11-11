# Lesson 8: Technical Interviews II — Take-Homes, Debugging & Reviewing AI-Written Code

**Week 4 · Wednesday, November 11, 2026 · 10:00 AM – 12:45 PM**

> **Get set up now:** download the **[Debugging Lab](../Resources/Debugging_Lab.zip)**, unzip it, and follow its README to get both projects running before the live debugging block. You'll need Node.js 18+ and Python 3.9+. Getting unfamiliar code running quickly is part of a debugging interview, so treat setup as practice. If you get stuck, say so in standup.

## Agenda

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:25 | Review: W-5 & W-6 and your AI code review |
| 0:35 | 0:15 | Overview: how take-homes are graded |
| 0:50 | 0:25 | Live debugging: I do, we do |
| 1:15 | 0:10 | BREAK |
| 1:25 | 0:15 | Overview: reviewing AI-generated code |
| 1:40 | 0:30 | Activity: code review an AI-generated pull request |
| 2:10 | 0:20 | Activity: spot the behavior change & peer review |
| 2:30 | 0:10 | Prep for Session 9 |
| 2:40 | 0:05 | Wrap up |
| TOTAL | 2:45 | |

## Why you should know this

Practical interviews look a lot like the actual job: build a small feature, fix a bug in code you didn't write, or review someone else's pull request (PR, a proposed code change submitted for review). And on the job in 2027, a lot of the code you read and review will have been written by AI. AI-generated code often *looks* correct while hiding bugs and security problems. Being the person who catches them is one of the most valuable things a junior developer can be.

## Learning Objectives

1. Judge an AI review of your own code: what to accept, what to push back on, and what it missed
1. Explain what reviewers look for in a take-home submission
1. Debug unfamiliar code using a systematic process: reproduce, hypothesize, narrow, fix, verify
1. Identify common mistakes in AI-generated code, including security problems and subtle behavior changes
1. Write clear, specific, kind code review comments ranked by severity

## Standup (10 min)

What I did · What I'll do · Where I'm stuck. AI Screen Practice reflections are due today.

## Review: W-5 & W-6 and Your AI Code Review (25 min)

On Monday we solved [W-5: Merging Two Playlists](../Resources/Problem_Bank.md#w-5-merging-two-playlists) and [W-6: Chain of Command](../Resources/Problem_Bank.md#w-6-chain-of-command) in class, and you asked an AI tool to review your solutions. Have your code and the AI's review open.

**For each problem (about 10 minutes each):**

1. One volunteer shares their solution and walks through it in 2 minutes, the way they would in an interview.
1. Name the pattern underneath the story. What gave it away?
1. Check edge cases as a group. Does your code handle them?
   - **W-5:** one or both playlists empty; one playlist much longer than the other; two songs with the same length
   - **W-6:** no CEO (an empty tree); a CEO with no reports; a "tree" that's really one long chain
1. State the time and space complexity. For W-6, what does recursion cost in space? What happens if the chain of command is 100,000 levels deep?

**Then discuss the AI review (5 minutes):**

- What did the AI flag? Was it right?
- Did it flag anything that wasn't actually a problem, or "fix" something that was already correct?
- Did it suggest a different approach (recursive vs. iterative, a placeholder "dummy" node for W-5)? Could you explain *why* that approach is better or worse, without the AI?
- What did the AI miss that the group found?
- Did you accept any change you couldn't explain? If an interviewer asked "why?", could you answer?

This is a preview of the second half of today: reviewing AI output is a skill, and the AI is not always right about your code *or* its own.

## Overview: How Take-Homes Are Graded (15 min)

- **Reviewers check, roughly in this order:** Does it run from the README instructions? Does it meet the requirements? Is it readable? Are there tests? Does the README explain your decisions and what you'd do next?
- **Scope:** do the core requirements well before adding extras. Say what you'd do with more time.
- **Follow-up interviews are common:** "Walk us through your code" or "Add this feature live." If you can't extend your own submission, it raises flags, especially if AI wrote it.
- **AI rules:** follow them exactly. If they're unclear, ask. If AI is allowed, disclose how you used it. (Review the [disclosure table](../Resources/AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai).)
- **Safety:** never run a "take-home" from an unverified recruiter that asks you to install unknown packages or run scripts you haven't read. Fake take-homes are a known way to spread malware. Practice the habit today: read `package.json` and `requirements.txt` in the Debugging Lab before you install anything.

## Live Debugging: I Do, We Do (25 min)

Use the **[Debugging Lab](../Resources/Debugging_Lab.zip)**. Its README has the bug reports, setup steps, and tasks.

1. **I do (10 min): DB-3, the slow dashboard** (`dashboard/` folder). The instructor talks through the process out loud: reproduce → read the code → form a hypothesis → measure → fix → verify. Follow along on your own machine.
1. **We do (15 min): DB-2, the disappearing cart items** (`cart/` folder). One student shares their screen and drives while everyone else directs. The driver rotates every 5 minutes. Notice that all the tests pass even though the bug is real. Write a failing test *before* you fix anything.

**Debugging process to practice:**

1. Reproduce the bug reliably
1. Read the code path involved. Don't guess yet.
1. Form one hypothesis and test it (print statements, a debugger, a failing test)
1. Fix the smallest thing that resolves it
1. Verify the fix, and check that you didn't break anything else
1. Explain the root cause in one sentence

## BREAK (10 min)

## Overview: Reviewing AI-Generated Code (15 min)

Common problems in AI-written code:

| Problem | Example |
| --- | --- |
| Security holes | SQL injection, logging passwords, weak password hashing, secrets in code |
| Plausible but wrong logic | Off-by-one errors, wrong edge cases, behavior silently changed in "refactors" |
| Invented APIs | Calling functions or library options that don't exist |
| Changing the tests instead of the code | Making tests pass by weakening them |
| Overcomplication | Extra layers, abstractions, or dependencies nobody asked for |
| Missing error handling | Only the "happy path" (everything goes right) is handled |
| "Tested locally" with no tests | Claims that aren't backed by evidence |

**How to write a good review comment:** say what's wrong, why it matters, and how to fix it. Label the severity (blocking / should fix / nitpick). Be kind and specific: "This query is vulnerable to SQL injection because user input goes straight into the string; a parameterized query would fix it" beats "this is insecure."

## Activity: Code Review an AI-Generated PR (30 min)

1. On your own, review **[CR-1](../Resources/Problem_Bank.md#cr-1-ai-generated-signup-endpoint)** as if it were a real PR (15 min). Write your comments and rank them by severity. No peeking at the answer key.
1. Compare findings as a group (10 min). Who found what? Which issues did nobody find?
1. **AI twist (5 min):** paste the code into an AI tool and ask it to review the PR. Did it catch everything? Did it flag anything that wasn't actually a problem? AI review is a useful second pass, not a replacement for your own.

## Activity: Spot the Behavior Change & Peer Review (20 min)

1. **[CR-2](../Resources/Problem_Bank.md#cr-2-ai-refactored-utility)** (5 min): an AI "readability refactor." Did it change behavior? What test would have caught it?
1. **[CR-3](../Resources/Problem_Bank.md#cr-3-review-a-classmates-take-home)** (15 min): swap your Week 2 take-home with a classmate and leave 3–5 review comments as if it were a PR. Share your top comment with the author.

## Prep for Session 9 (10 min)

Session 9 is the **live AI-assisted coding round** (Challenge 5). Before Monday:

- Choose your AI tool: an AI chat assistant, or a coding agent (a tool that can read files, run commands, and edit code on its own, like Claude Code, Cursor, or GitHub Copilot in agent mode). Free tiers or student plans are fine.
- Install it and make sure it works with your editor and a sample project.
- Read [AI in the Job Search, Sections 5–7](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews).

## Wrap Up (5 min)

Before Session 9:

- Set up and test your AI coding tool
- Read Sections 5–7 of the AI guide
- Practice once: give the AI a small task in one of your projects, and narrate out loud as you review every change it makes. The Debugging Lab is a good place to try this.
- Keep up outreach

## Additional Resources

1. [Debugging Lab](../Resources/Debugging_Lab.zip): runnable code for DB-2 and DB-3
1. [Problem Bank: Debugging & Code Review](../Resources/Problem_Bank.md#format-3-debug-an-unfamiliar-codebase)
1. [AI-assisted coding interviews](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews)
