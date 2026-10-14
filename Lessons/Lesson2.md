# Lesson 2: Proof-of-Work Portfolio & Deployment Workshop

**Week 1 · Wednesday, October 21, 2026 · 10:00 AM – 12:45 PM**

## Minute-by-Minute

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:25 | Challenge 1 debrief |
| 0:35 | 0:20 | Overview: what a hiring manager looks at |
| 0:55 | 0:20 | Activity: 30-second GitHub teardown |
| 1:15 | 0:10 | BREAK |
| 1:25 | 0:50 | Deployment workshop |
| 2:15 | 0:25 | Activity: start your decisions write-up |
| 2:40 | 0:05 | Wrap up |
| TOTAL | 2:45 | |

## Why you should know this

A hiring manager might spend 30 seconds on your GitHub before deciding whether to read further. Since AI can generate a decent-looking project in an afternoon, what stands out now is a project that's **live**, **tested**, and **explained** — evidence that you made real decisions. By the end of today, your proof-of-work project should be deployed or very close.

## Learning Objectives

1. Evaluate a GitHub profile and project the way a hiring manager does
1. Deploy a project to a public URL using a free hosting service
1. Explain the difference between a project that shows proof of work and one that doesn't
1. Begin a decisions write-up that explains the tradeoffs in your project

## Standup (10 min)

What I did · What I'll do · Where I'm stuck. Job search plans are due today — confirm everyone has submitted.

## Challenge 1 Debrief (25 min)

Each student (about 7 minutes each):

1. Show your solution and explain your approach in 2 minutes.
1. Share your complexity analysis.
1. One thing that went well, one thing you'd change.

Instructor notes patterns across the group: Did people clarify the problem first? Test with examples? Talk through their thinking?

## Overview: What a Hiring Manager Looks At (20 min)

- **The 30-second scan:** profile photo and bio → pinned repos → top of a README → is there a live link? → do commits look like real work?
- **Signals of proof of work:**
  - A live URL that works on a phone
  - A README that says what it does, who it's for, and how to run it
  - Tests and sensible error handling
  - A record of decisions and tradeoffs
  - An honest AI Use section
- **Signals that hurt:** empty READMEs, "final-project-v2" repo names, pinned tutorial clones, a single giant commit, secrets committed to the repo.
- **AI-era reality:** interviewers increasingly assume AI helped build your project. That's fine — what they test is whether *you* understand it. Expect "why did you structure it this way?" and "add this feature right now."

## Activity: 30-Second GitHub Teardown (20 min)

1. Rotate laptops. Each student gets 30 seconds (timed) on a classmate's GitHub profile.
1. Write down: What does this person do? What's their best project? Would you click further?
1. Share findings with the owner (3 minutes each). Compare what the owner *wanted* someone to notice vs. what was actually noticed.
1. Each student writes down their top 3 fixes from the [Portfolio checklist](../Assignments/Portfolio_Proof_of_Work.md#4-github-profile).

## Deployment Workshop (50 min)

Goal: your proof-of-work project live at a public URL, or a clear plan and a working deploy of at least part of it by Session 4.

1. Pick a host using the [Deployment Guide](../Resources/Deployment_Guide.md) (5 min).
1. Deploy (40 min). The instructor circulates and helps debug. Classmates who finish first help others.
1. Run the [deployment checklist](../Resources/Deployment_Guide.md#deployment-checklist) (5 min).

**AI in practice:** It's fine to use an AI assistant to write a deployment config or explain an error log. But:

- Read the actual error before asking the AI about it.
- Never paste secret keys into an AI chat.
- Be ready to answer "How did you deploy this?" in an interview without notes.

## Activity: Start Your Decisions Write-Up (25 min)

1. In pairs (instructor joins as the third partner), interview each other for 5 minutes each about your project, asking "why?" at least five times:
   - Why this framework? Why this database? Why is this file structured this way? What would break first with more users?
1. Write down the 3–5 decisions that came up. These become your `DECISIONS.md` (see the [assignment](../Assignments/Portfolio_Proof_of_Work.md#3-a-decisions-write-up-decisionsmd)).
1. Flag any decision you *couldn't* explain — especially code an AI wrote. That's what to study before an interview.

## Wrap Up (5 min)

Before Session 3:

- Finish deploying — **live URL due Session 4**
- Fix the top 3 issues from your GitHub teardown
- Bring your current resume (PDF) and one job posting you're interested in for a live resume review
- Hit your standup commitments

## Additional Resources

1. [Proof-of-Work Portfolio assignment](../Assignments/Portfolio_Proof_of_Work.md)
1. [Free Deployment Options](../Resources/Deployment_Guide.md)
1. [AI disclosure guidance](../Resources/AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai)
