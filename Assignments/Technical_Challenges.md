# Technical Interview Challenge Rotation

**Weight:** 20% · **Weekly, Weeks 1–5**

## Why

Real interview loops mix formats: a timed algorithm problem at one company, a take-home at another, a debugging session or an AI-assisted round at a third. This rotation gives you at least one rep of each so nothing in a real interview is your first time.

## Schedule

Each challenge is assigned in the first session of the week and debriefed in the second. Problems come from the [Problem Bank](../Resources/Problem_Bank.md).

| Week | Assigned | Debrief | Challenge | AI allowed? |
| --- | --- | --- | --- | --- |
| 1 | Mon 10/19 | Wed 10/21 | **Diagnostic:** one timed warm-up algorithm problem, done in class in Session 1 (40 min). Low stakes — this is your baseline. | No |
| 2 | Mon 10/26 | Wed 10/28 | **Take-home** (TH-1 to TH-4, 3–4 hours) | **Yes — must be disclosed in README** |
| 3 | Mon 11/2 | Wed 11/4 | **Take-home** (a different one from Week 2, 3–4 hours) | No |
| 4 | Mon 11/9 | Wed 11/11 | **Part A:** timed algorithm problem under interview conditions, done in class in Session 7 with a classmate as interviewer. **Part B:** one debugging exercise (DB-1 to DB-3) as homework | No |
| 5 | Mon 11/16 | Wed 11/18 | **Live AI-assisted coding round**, done in class in Session 9 (AI-1, AI-2, or AI-4), 30 min each, with a 1:1 instructor debrief in Session 10 | **Yes — required** |

Weeks 2 and 3 are deliberately paired: comparing the same kind of task with and without AI shows you where AI actually helps you and where you depend on it.

## How to submit

Submit a link in your tracker before the debrief session:

- **Algorithm problems:** a repo or gist with your solution, plus a short note on its time and space complexity and what you'd do differently
- **Take-homes:** a GitHub repo with a README (how to run, what you'd do with more time, AI Use section if allowed)
- **Debugging:** a short write-up: how you reproduced the bug, your hypothesis, the fix, and how you verified it
- **AI-assisted round:** no submission — the instructor scores it live

## Rubric

Each challenge is scored 1–4 on each row. A **passing** challenge averages 2.5 or higher. Pass at least 4 of the 5 challenges (over 70%) for full credit.

| Criteria | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| **Understanding** | Starts coding without clarifying | Asks some questions | Clarifies requirements and edge cases | Clarifies, restates the problem, and confirms the plan before coding |
| **Communication** | Silent or unclear | Explains only when asked | Narrates most of the process | Clear, continuous narration of reasoning and tradeoffs |
| **Correctness** | Doesn't work | Works for basic cases | Works including most edge cases | Works, handles edge cases, and has tests |
| **Code quality** | Hard to read | Readable but messy | Clean, sensible names and structure | Clean, well-organized, easy to extend |
| **Analysis** | No complexity or tradeoff discussion | Partial | Correct complexity / clear tradeoffs | Discusses alternatives and why this one wins |
| **AI use** *(AI-allowed challenges only)* | Accepted output blindly; can't explain it | Some review | Reviewed and tested AI output; explains all code | Directed the AI precisely, caught its mistakes, fully owns the result |

## Debrief format (group, ~30 minutes)

With three students, every debrief covers everyone's work:

1. Each student shows their solution in 5 minutes: approach, one thing that went well, one thing they'd change.
2. Classmates ask one question each, as an interviewer would.
3. Instructor highlights patterns and one or two techniques to practice.
4. For the Week 2 vs. Week 3 debrief: each student compares their AI and no-AI take-homes. Where was the AI genuinely faster? Where did it slow you down or introduce bugs?
