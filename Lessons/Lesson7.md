# Lesson 7: Technical Interviews I — Algorithms, Data Structures & Thinking Out Loud

**Week 4 · Monday, November 9, 2026 · 10:00 AM – 12:45 PM**

## Minute-by-Minute

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:20 | Overview: anatomy of a technical interview |
| 0:30 | 0:25 | Demo: instructor solves a problem out loud |
| 0:55 | 0:20 | Pattern drills |
| 1:15 | 0:10 | BREAK |
| 1:25 | 1:00 | Challenge 4, part A: timed mock interviews |
| 2:25 | 0:15 | Debrief & Challenge 4, part B assigned |
| 2:40 | 0:05 | Wrap up |
| TOTAL | 2:45 | |

## Why you should know this

Algorithm and data structure interviews (often called DSA — data structures and algorithms) are still common, especially at larger companies. They're rarely about getting the perfect answer. Interviewers mostly grade *how you think*: do you clarify, plan, communicate, and test? That's a learnable process, and it's the same process that makes you strong in every other interview format.

## Learning Objectives

1. Follow a repeatable sequence for solving a technical interview problem
1. Narrate your thinking clearly while solving a problem
1. Recognize common problem patterns (hash maps, two pointers, sliding window, BFS/DFS)
1. Manage your time across a 35–45 minute interview
1. Use AI tools to study algorithms in ways that build skill rather than replace it

## Standup (10 min)

What I did · What I'll do · Where I'm stuck. AI Screen Practice reflections due today.

## Overview: Anatomy of a Technical Interview (20 min)

**The sequence** (practice it until it's automatic):

| Step | What to do | Time (of 40 min) |
| --- | --- | --- |
| 1. Clarify | Restate the problem. Ask about input size, edge cases, and expected output. | 3–5 min |
| 2. Examples | Work through 1–2 examples by hand, including an edge case. | 3 min |
| 3. Brute force | Describe the simplest working approach and its Big O (how time/memory grows with input). | 3 min |
| 4. Optimize | Look for a better approach. Name the pattern. | 5 min |
| 5. Code | Write clean code, narrating as you go. | 15 min |
| 6. Test | Walk through your code with an example. Check edge cases. Fix bugs. | 5 min |
| 7. Analyze | State final time and space complexity. Mention tradeoffs. | 2 min |

**Thinking out loud:**

- Silence makes interviewers nervous. Narrate even when you're stuck: "I'm thinking about whether a hash map helps here because…"
- If you're stuck, say so, and say what you've tried. Interviewers often give hints to candidates who communicate.
- Don't announce "I've seen this problem before" and rush. Walk through it properly.

**Why these interviews persist despite AI:** they test reasoning under pressure without tools, and they're hard to fake in person. Expect them especially in in-person final rounds.

## Demo: Instructor Solves a Problem Out Loud (25 min)

The instructor solves **I-1: Bot Account Detector** from the [Problem Bank](../Resources/Problem_Bank.md#i-1-bot-account-detector) (or another interview-level problem) live, following the sequence and narrating everything — including a deliberate mistake and how to recover.

Students score the instructor on the [challenge rubric](../Assignments/Technical_Challenges.md#rubric) while watching, then discuss: What did good narration sound like? When did the instructor slow down? Did anyone recognize the problem underneath the story?

## Pattern Drills (20 min)

Interviewers rarely use a problem's textbook name. They describe it as part of their product, and you have to recognize the shape underneath. Many problems in the [Problem Bank](../Resources/Problem_Bank.md#format-1-algorithms--data-structures-timed) are ones you've solved before, in disguise.

Quick group drill: the instructor reads a Problem Bank story aloud. Students name the pattern, the signal that gave it away, and the brute-force vs. optimized complexity. No coding, and no peeking at the answer key.

| Pattern | Signal in the problem | Example |
| --- | --- | --- |
| Hash map | "Find a pair," "count occurrences," "seen before?" | W-1 Gift Card Checkout |
| Two pointers | Sorted array, pairs, reading from both ends | Checking whether a product code reads the same forwards and backwards |
| Sliding window | "Longest/shortest stretch of consecutive items with…" | I-3 Longest Fresh Streak |
| Stack | Matching open/close pairs, "most recent unfinished thing" | W-2 Config File Validator |
| BFS / DFS | Grids, connected regions, trees, rounds or levels | I-6 Wi-Fi Dead Zones |
| Sort first | Time ranges, scheduling, grouping | I-4 Calendar Busy Blocks |

## Challenge 4, Part A: Timed Mock Interviews (60 min)

Three rounds of 20 minutes, rotating roles. With 20-minute rounds, use **warm-up** problems from the [Problem Bank](../Resources/Problem_Bank.md#format-1-algorithms--data-structures-timed) that the candidate hasn't seen yet:

- **Interviewer:** presents the problem, answers clarifying questions, gives a hint only if the candidate is stuck for 3+ minutes, asks for complexity at the end.
- **Candidate:** follows the sequence, narrates, codes in a plain editor (no autocomplete, no AI).
- **Observer:** scores the candidate on the rubric and keeps time, calling out 10 and 5 minutes remaining.

2 minutes of feedback after each round, then rotate.

## Debrief & Challenge 4, Part B (15 min)

- Which step of the sequence did each person skip under pressure? (Usually: clarifying and testing.)
- **Part B assigned:** complete one debugging exercise (DB-1 to DB-3) from the [Problem Bank](../Resources/Problem_Bank.md#format-3-debug-an-unfamiliar-codebase). Submit a short write-up: how you reproduced the bug, your hypothesis, your fix, and how you verified it. No AI. Due before Session 8.

**AI in practice — studying algorithms:**

- **Do:** attempt the problem first, then ask the AI for a *hint*, not a solution. Ask it to quiz you on patterns. Ask it to review your solution's complexity.
- **Don't:** read AI solutions and believe you've learned them. Recognizing a solution is not the same as producing one under pressure.
- Try this prompt: "I'm practicing for interviews. Give me a medium array problem. Don't show the solution. When I describe my approach, tell me if it's on track and give one hint at a time."

## Wrap Up (5 min)

Before Session 8:

- Complete Challenge 4, part B (debugging write-up)
- Practice 3 problems on your own, out loud, with a timer
- Keep up outreach and log informational interviews

## Additional Resources

1. [Problem Bank](../Resources/Problem_Bank.md)
1. [Technical challenge rubric](../Assignments/Technical_Challenges.md#rubric)
