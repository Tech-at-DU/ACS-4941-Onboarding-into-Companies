# Lesson 9: AI-Assisted Coding Interviews & Interview Integrity

**Week 5 · Monday, November 16, 2026 · 10:00 AM – 12:45 PM**

## Minute-by-Minute

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:20 | Overview: what AI-assisted rounds grade & where the lines are |
| 0:30 | 0:15 | Demo: a strong vs. weak AI-assisted interview |
| 0:45 | 0:30 | Challenge 5, round A |
| 1:15 | 0:10 | BREAK |
| 1:25 | 0:30 | Challenge 5, round B |
| 1:55 | 0:30 | Challenge 5, round C |
| 2:25 | 0:15 | Group debrief: patterns |
| 2:40 | 0:05 | Wrap up |
| TOTAL | 2:45 | |

## Why you should know this

More companies now run coding interviews where you're *expected* to use an AI assistant or coding agent, because that's how the job is done. These rounds are not easier. The AI writes code fast, so interviewers grade what's left: how well you understand the problem, direct the tool, check its work, catch its mistakes, and explain the result. At the same time, companies are cracking down hard on candidates who secretly use AI where it isn't allowed. You need to be good at the first and nowhere near the second.

## Learning Objectives

1. Describe what interviewers grade in AI-assisted coding rounds
1. Direct an AI coding assistant or agent with clear, scoped instructions
1. Verify AI-generated code by reading, running, and testing it — and catch its mistakes
1. Explain and defend AI-assisted code without the tool
1. Explain the integrity rules around AI in interviews and the consequences of breaking them

## Standup (10 min)

What I did · What I'll do · Where I'm stuck. Confirm everyone's AI tool is working.

## Overview: What AI-Assisted Rounds Grade & Where the Lines Are (20 min)

Walk through [AI in the Job Search, Section 5](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews):

| Interviewers watch for | Good looks like |
| --- | --- |
| Problem understanding | You clarify requirements *before* prompting |
| Task breakdown | Small, checkable steps — not "build the whole thing" |
| Clear direction | Prompts with context, constraints, and what "done" means |
| Verification | You read every change, run it, and test edge cases |
| Catching mistakes | You notice when the AI is wrong, overcomplicated, or insecure |
| Ownership | You can explain every line, and change it without the AI |
| Communication | You narrate the whole time, including while the AI works |

**Where the lines are** ([Sections 6–7](../Resources/AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai)):

- **AI-assisted round:** use AI openly. That's the point.
- **No-AI round:** no AI. If you're unsure which kind of round it is, ask.
- **Hidden interview "assistant" tools** — software that secretly listens to the interview or reads your screen and feeds you answers — are heavily marketed to job seekers. Interviewers are trained to spot them (eyes moving to read, delayed answers, answers that collapse under follow-up questions), platforms detect many of them, and getting caught usually means rejection and being permanently flagged by that company.
- **This is why in-person final rounds and identity checks are coming back.** Expect them.

**Discussion:** Why do you think companies are moving in both directions at once — requiring AI in some rounds and banning it in others?

## Demo: Strong vs. Weak AI-Assisted Interview (15 min)

The instructor role-plays the same 5-minute task twice, using **AI-3: Fix a failing test suite**:

1. **Weak:** pastes the whole task into the AI, accepts its changes, goes silent, can't explain why a test now passes (the AI quietly weakened the test).
1. **Strong:** reads the failing tests first, explains the plan, asks the AI to fix one test at a time, reads each diff, notices the AI tried to edit a test, rejects it, explains the real fix.

Students list the differences they noticed.

## Challenge 5: Live AI-Assisted Coding Rounds (3 × 30 min)

Each student completes one live round while the instructor interviews and the other two observe with the rubric. Each student gets a **different** problem from [Format 5 of the Problem Bank](../Resources/Problem_Bank.md#format-5-ai-assisted-coding-round-live) (AI-1, AI-2, or AI-4).

**Each 30-minute round:**

| Time | What happens |
| --- | --- |
| 0–3 min | Instructor presents the problem. Candidate asks clarifying questions. |
| 3–20 min | Candidate works with their AI tool, narrating throughout. |
| 20–27 min | Instructor's follow-up questions: "Why this approach?" "What did the AI get wrong?" "Change this function without the AI." "What would you test next?" |
| 27–30 min | Quick feedback from observers: one strength, one thing to improve. |

**Observers** score using the [challenge rubric](../Assignments/Technical_Challenges.md#rubric), including the **AI use** row, and write down one moment where the candidate showed (or missed) good judgment.

The full 1:1 instructor debrief happens in Session 10.

## Group Debrief: Patterns (15 min)

- Where did each person catch the AI making a mistake? Where did a mistake slip through?
- When did narration stop? (Usually while waiting for the AI.)
- How did the "change it without the AI" question feel?
- What will you practice before a real AI-assisted round?

## Wrap Up (5 min)

Before Session 10:

- Write down your own reflection on your round: one thing you'd do the same, two things you'd change
- Practice: take a small feature from your proof-of-work project and build it with an AI agent while narrating out loud. Then explain every change to someone else (or record yourself)
- Think about a feature in your proof-of-work project you could use for the system design exercise
- Keep up outreach

## Additional Resources

1. [AI in the Job Search — Sections 5–7](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews)
1. [Problem Bank — Format 5](../Resources/Problem_Bank.md#format-5-ai-assisted-coding-round-live)
1. [Technical challenge rubric](../Assignments/Technical_Challenges.md#rubric)
