# Lesson 8: Technical Interviews II — Take-Homes, Debugging & Reviewing AI-Written Code

**Week 4 · Wednesday, November 11, 2026 · 10:00 AM – 12:45 PM**

> **Instructor note:** November 11 is Veterans Day. Confirm this is a class day on the academic calendar.

## Minute-by-Minute

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:25 | Challenge 4 debrief |
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

Practical interviews look a lot like the actual job: build a small feature, fix a bug in code you didn't write, or review someone else's pull request (PR — a proposed code change submitted for review). And on the job in 2027, a lot of the code you'll read and review was written by AI. AI-generated code often *looks* correct while hiding bugs and security problems. Being the person who catches them is one of the most valuable things a junior developer can be.

## Learning Objectives

1. Explain what reviewers look for in a take-home submission
1. Debug unfamiliar code using a systematic process: reproduce, hypothesize, narrow, fix, verify
1. Identify common mistakes in AI-generated code, including security problems and subtle behavior changes
1. Write clear, specific, kind code review comments ranked by severity

## Standup (10 min)

What I did · What I'll do · Where I'm stuck.

## Challenge 4 Debrief (25 min)

1. Quick review of Monday's timed mocks: what improved from the Week 1 diagnostic?
1. Each student walks through their debugging write-up (about 6 minutes each). Focus on *process*: How did you reproduce it? What was your first hypothesis? Was it right?

## Overview: How Take-Homes Are Graded (15 min)

- **Reviewers check, roughly in this order:** Does it run from the README instructions? Does it meet the requirements? Is it readable? Are there tests? Does the README explain decisions and what you'd do next?
- **Scope:** do the core requirements well before adding extras. Say what you'd do with more time.
- **Follow-up interviews are common:** "Walk us through your code" or "Add this feature live." If you can't extend your own submission, it raises flags — especially if AI wrote it.
- **AI rules:** follow them exactly. If unclear, ask. If allowed, disclose. (Review the [disclosure table](../Resources/AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai).)
- **Safety:** never run a "take-home" from an unverified recruiter that asks you to install unknown packages or run scripts you haven't read. Fake take-homes are a known way to spread malware.

## Live Debugging: I Do, We Do (25 min)

Using **DB-3: The slow dashboard** from the [Problem Bank](../Resources/Problem_Bank.md#db-3-the-slow-dashboard):

1. **I do (10 min):** the instructor narrates the process: reproduce → read the code → form a hypothesis → measure → fix → verify.
1. **We do (15 min):** the group tackles **DB-2** together, with one student driving and the others directing. Rotate the driver every 5 minutes.

**Debugging process to practice:**

1. Reproduce the bug reliably
1. Read the code path involved — don't guess yet
1. Form one hypothesis and test it (print statements, debugger, a failing test)
1. Fix the smallest thing that resolves it
1. Verify the fix and check you didn't break anything else
1. Explain the root cause in one sentence

## Overview: Reviewing AI-Generated Code (15 min)

Common problems in AI-written code:

| Problem | Example |
| --- | --- |
| Security holes | SQL injection, logging passwords, weak password hashing, secrets in code |
| Plausible but wrong logic | Off-by-one errors, wrong edge cases, silently changed behavior in "refactors" |
| Invented APIs | Calling functions or library options that don't exist |
| Changing the tests instead of the code | Making tests pass by weakening them |
| Overcomplication | Extra layers, abstractions, or dependencies nobody asked for |
| Missing error handling | Happy path only |
| "Tested locally" with no tests | Claims that aren't backed by evidence |

**How to write a good review comment:** what's wrong, why it matters, and a suggested fix. Label severity (blocking / should fix / nitpick). Be kind and specific — "This query is vulnerable to SQL injection because user input goes straight into the string; a parameterized query would fix it" beats "this is insecure."

## Activity: Code Review an AI-Generated PR (30 min)

1. Individually, review **CR-1** from the [Problem Bank](../Resources/Problem_Bank.md#cr-1-ai-generated-signup-endpoint) as if it were a real PR (15 min). Write comments, ranked by severity.
1. Compare findings as a group (10 min). Who found what? Which issues did nobody find?
1. **AI twist (5 min):** paste the code into an AI tool and ask it to review the PR. Did it catch everything? Did it flag anything that wasn't actually a problem? Lesson: AI review is a useful second pass, not a replacement for yours.

## Activity: Spot the Behavior Change & Peer Review (20 min)

1. **CR-2** (5 min): an AI "readability refactor." Did it change behavior? How would a test have caught it?
1. **CR-3** (15 min): swap your Week 2 take-home with a classmate and leave 3–5 review comments as if it were a PR. Share your top comment with the author.

## Prep for Session 9 (10 min)

Session 9 is the **live AI-assisted coding round** (Challenge 5). Before Monday:

- Choose your AI tool: an AI chat assistant, or a coding agent (a tool that can read files, run commands, and edit code on its own, like Claude Code, Cursor, or GitHub Copilot in agent mode). Free tiers or student plans are fine.
- Install it and make sure it works with your editor and a sample project.
- Read [AI in the Job Search, Sections 5–7](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews).

## Wrap Up (5 min)

Before Session 9:

- Set up and test your AI coding tool
- Read Sections 5–7 of the AI guide
- Practice once: give the AI a small task in one of your projects, and narrate out loud as you review every change it makes
- Keep up outreach

## Additional Resources

1. [Problem Bank — Debugging & Code Review](../Resources/Problem_Bank.md#format-3-debug-an-unfamiliar-codebase)
1. [AI-assisted coding interviews](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews)
