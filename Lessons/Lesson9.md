# Lesson 9: AI-Assisted Coding Interviews & Interview Integrity

**Week 5 · Monday, November 16, 2026 · 10:00 AM – 12:45 PM**

> **Before your round:** make sure your AI tool works with your editor, and that you can share your **whole screen** (editor, terminal, and AI tool) in our video call. If you're the AI-1 candidate, download the [To-Do API starter](../Resources/Todo_API_Starter.zip) when your round starts and follow its README.

## Agenda

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:15 | Take-home review |
| 0:25 | 0:15 | Overview: what AI-assisted rounds grade & where the lines are |
| 0:40 | 0:15 | Demo: a strong vs. weak AI-assisted interview |
| 0:55 | 0:30 | Challenge 5, round A |
| 1:25 | 0:10 | BREAK |
| 1:35 | 0:30 | Challenge 5, round B |
| 2:05 | 0:30 | Challenge 5, round C |
| 2:35 | 0:05 | Quick debrief |
| 2:40 | 0:05 | Wrap up |
| TOTAL | 2:45 | |

## Why you should know this

More companies now run coding interviews where you're *expected* to use an AI assistant or coding agent, because that's how the job is done. These rounds are not easier. The AI writes code fast, so interviewers grade what's left: how well you understand the problem, direct the tool, check its work, catch its mistakes, and explain the result. At the same time, companies are cracking down hard on candidates who secretly use AI where it isn't allowed. You need to be good at the first and nowhere near the second.

## Learning Objectives

1. Describe what interviewers grade in AI-assisted coding rounds
1. Direct an AI coding assistant or agent with clear, scoped instructions
1. Verify AI-generated code by reading, running, and testing it, and catch its mistakes
1. Explain and defend AI-assisted code without the tool
1. Explain the integrity rules around AI in interviews and the consequences of breaking them

## Standup (10 min)

What I did · What I'll do · Where I'm stuck. Quick check: is everyone's AI tool working, and can you share your screen?

## Take-Home Review (15 min)

Have your take-home solution open and ready to share.

1. **Walkthrough (about 3 minutes each):** share your screen and walk through your solution the way you would in a take-home follow-up interview. Start with how to run it, then your approach, then one decision you'd defend.
1. **One question from the group** for each person. Good questions: "Why this approach?" "What happens if the input is empty or huge?" "What would you do with another hour?"
1. **Compare:** where did solutions differ? Which differences actually matter, and which are just style?

Notice how it feels to explain your own code on the spot. That's exactly what the follow-up questions in today's rounds will ask of you.

## Overview: What AI-Assisted Rounds Grade & Where the Lines Are (15 min)

From [AI in the Job Search, Section 5](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews):

| Interviewers watch for | Good looks like |
| --- | --- |
| Problem understanding | You clarify requirements *before* prompting |
| Task breakdown | Small, checkable steps, not "build the whole thing" |
| Clear direction | Prompts with context, constraints, and what "done" means |
| Verification | You read every change, run it, and test edge cases |
| Catching mistakes | You notice when the AI is wrong, overcomplicated, or insecure |
| Ownership | You can explain every line, and change it without the AI |
| Communication | You narrate the whole time, including while the AI works |

**Where the lines are** ([Sections 6–7](../Resources/AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai)):

- **AI-assisted round:** use AI openly. That's the point.
- **No-AI round:** no AI. If you're unsure which kind of round it is, ask.
- **Hidden interview "assistant" tools** are software that secretly listens to the interview or reads your screen and feeds you answers. They're heavily marketed to job seekers. Interviewers are trained to spot them (eyes moving to read, delayed answers, answers that collapse under follow-up questions), platforms detect many of them, and getting caught usually means rejection and being permanently flagged by that company.
- **This is why in-person final rounds and identity checks are coming back.** Expect them.

**Discussion:** Why do you think companies are moving in both directions at once, requiring AI in some rounds and banning it in others?

## Demo: Strong vs. Weak AI-Assisted Interview (15 min)

Watch the same 5-minute task done twice, using **AI-3: Fix a failing test suite**. The code is the [Checkout Demo](../Resources/Checkout_Demo.zip): a store's pricing code with five failing tests.

1. **Weak:** pastes the whole task into the AI, accepts every change, goes silent, and can't explain why a test now passes.
1. **Strong:** reads the failing tests and the pricing rules first, explains a plan, fixes one thing at a time, reads every change, and pushes back when the AI suggests something wrong.

As you watch, write down every difference you notice. We'll list them together. Want to try it yourself later? Download the Checkout Demo and see whether your AI tool tries to change a test instead of the code.

## Challenge 5: Live AI-Assisted Coding Rounds (3 × 30 min)

Each student does one live round. The instructor is the interviewer, and the other two students observe. Each student gets a **different** problem from [Format 5 of the Problem Bank](../Resources/Problem_Bank.md#format-5-ai-assisted-coding-round-live): AI-1, AI-2, or AI-4.

**Each 30-minute round:**

| Time | What happens |
| --- | --- |
| 0–3 min | The interviewer presents the problem. The candidate asks clarifying questions. |
| 3–20 min | The candidate works with their AI tool, narrating throughout. |
| 20–27 min | Follow-up questions: "Why this approach?" "What did the AI get wrong?" "Change this function without the AI." "What would you test next?" |
| 27–30 min | Quick feedback from observers: one strength, one thing to improve. |

**Candidate:**

- Share your **whole screen**, not just one window, so we can see the editor, terminal, and AI tool.
- Ask clarifying questions *before* you prompt. Then narrate everything, especially while the AI is working.

**Observers:**

- Stay muted with cameras on.
- Score the candidate using the [challenge rubric](../Assignments/Technical_Challenges.md#rubric), including the **AI use** row.
- Write down one moment where the candidate showed (or missed) good judgment.

Your full 1:1 debrief with the instructor happens in Session 10.

## Quick Debrief (5 min)

One sentence each: where did you catch the AI making a mistake, or where did one slip past you? We'll dig into patterns in Session 10.

## Wrap Up (5 min)

Before Session 10:

- Write a short reflection on your round: one thing you'd do the same, two things you'd change
- Practice: take a small feature from your proof-of-work project and build it with an AI agent while narrating out loud. Then explain every change to someone else (or record yourself)
- Think about a feature in your proof-of-work project you could use for the system design exercise
- Keep up outreach

## Additional Resources

1. [AI in the Job Search, Sections 5–7](../Resources/AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews)
1. [Problem Bank, Format 5](../Resources/Problem_Bank.md#format-5-ai-assisted-coding-round-live)
1. [Technical challenge rubric](../Assignments/Technical_Challenges.md#rubric)
1. [Checkout Demo](../Resources/Checkout_Demo.zip): practice catching an AI that edits tests instead of code
