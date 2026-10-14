# Lesson 10: System Design Fundamentals, Including an AI-Powered Feature

**Week 5 · Wednesday, November 18, 2026 · 10:00 AM – 12:45 PM**

## Minute-by-Minute

| **Elapsed** | **Time** | **Activity** |
| --- | --- | --- |
| 0:00 | 0:10 | Standup |
| 0:10 | 0:15 | Challenge 5 group debrief |
| 0:25 | 0:25 | Overview: a framework for junior system design |
| 0:50 | 0:25 | We do: design a feature together |
| 1:15 | 0:10 | BREAK |
| 1:25 | 0:25 | Overview: designing a feature that uses an LLM |
| 1:50 | 0:25 | We do: sketch "Ask the Handbook" |
| 2:15 | 0:25 | Work time + 1:1 Challenge 5 debriefs |
| 2:40 | 0:05 | Wrap up & Thanksgiving break plan |
| TOTAL | 2:45 | |

## Why you should know this

Junior candidates are increasingly asked lightweight system design questions — not "design Netflix," but "how would you build this feature?" Interviewers want to see that you can think about data, APIs, and tradeoffs before writing code. And more and more of those features involve AI, so knowing how to design one responsibly is a real advantage.

## Learning Objectives

1. Use a simple framework to design a small feature: requirements, data model, API, diagram, tradeoffs, and what breaks first
1. Explain basic scaling tools (caching, indexes, background jobs) in plain terms
1. Explain RAG (retrieval-augmented generation) and design a simple feature that uses it
1. Identify the risks of LLM-powered features — wrong answers, cost, speed, privacy — and how to test for them

## Standup (10 min)

What I did · What I'll do · Where I'm stuck.

## Challenge 5 Group Debrief (15 min)

The instructor shares patterns from Monday's rounds: what strong AI direction looked like, common verification gaps, and how follow-up questions went. Individual 1:1 debriefs happen during work time later today.

## Overview: A Framework for Junior System Design (25 min)

| Step | Questions to answer |
| --- | --- |
| 1. Requirements | What must it do? What's out of scope? How many users, roughly? |
| 2. Data model | What are the main things (users, groups, events)? What fields do they have? How do they relate? |
| 3. API | What endpoints does the client call? Method, path, input, output. Usually REST (the common style of web API using URLs and HTTP methods like GET and POST). |
| 4. Diagram | Boxes and arrows: client → server → database, plus any other services. |
| 5. Tradeoffs | Where did you pick one option over another, and why? |
| 6. What breaks first | As users grow, what slows down or fails? What would you do? |

**Basic scaling tools, in plain terms:**

- **Index:** like a book's index — lets the database find rows without reading every one. Add them to columns you search or filter by.
- **Cache:** keep a copy of frequently requested data somewhere fast (memory) so you don't recompute it every time.
- **Background job:** do slow work (sending emails, generating reports) later, outside the user's request, so the page stays fast.
- **Read-heavy vs. write-heavy:** most apps are read far more than written. That changes what you optimize.

**What interviewers want to hear from a junior candidate:** clear requirements, a sensible data model, and honest tradeoffs — not buzzwords. "I'd start with one Postgres database because it's simple and we have 1,000 users; I'd add caching if the dashboard got slow" is a great answer.

## We Do: Design a Feature Together (25 min)

As a group at the whiteboard, design the **study group scheduler** (Option A in the [System Design Exercise](../Assignments/System_Design.md#option-a-classic-feature)). One student drives each step; others question.

The instructor plays interviewer and asks follow-ups: "What if two people vote at the same time?" "How do reminders get sent?" "What happens with 100x more users?"

## Overview: Designing a Feature That Uses an LLM (25 min)

**RAG, explained simply.** An LLM (large language model) only knows what it was trained on, and it will confidently make things up. RAG (retrieval-augmented generation) gives it the right information at question time:

1. **Prepare:** split your documents into small chunks and store them in a way that can be searched by meaning (often a "vector database" — a database that finds text with similar meaning, not just matching words).
1. **Retrieve:** when a question comes in, search for the most relevant chunks.
1. **Generate:** send the question *plus* those chunks to the LLM, with instructions to answer only from the provided text and say "I don't know" otherwise.

**Design questions every LLM feature raises:**

| Concern | Questions to answer |
| --- | --- |
| Wrong answers ("hallucinations") | What happens when the answer isn't in the docs? How do you show sources so users can check? |
| Testing ("evals") | What set of sample questions with known answers will you test against? How often? |
| Cost | How much does each question cost in API fees? What stops abuse? |
| Speed | How long will users wait? Can you stream the answer as it's generated? |
| Privacy & permissions | Can every employee see every document? What data leaves your servers? |
| Fallback | What happens when the AI provider is down? |

**Interview tip:** junior candidates who bring up testing, cost, and failure modes *without being asked* stand out, because many people treat the LLM as magic.

## We Do: Sketch "Ask the Handbook" (25 min)

As a group, sketch Option C from the [System Design Exercise](../Assignments/System_Design.md#option-c-ai-powered-feature): requirements, the three RAG steps as boxes in a diagram, the data model for documents and chunks, one API endpoint, and three eval questions.

## Work Time + 1:1 Challenge 5 Debriefs (25 min)

- Students choose their [System Design Exercise](../Assignments/System_Design.md) option and start their design.
- Meanwhile, the instructor holds an 8-minute 1:1 debrief with each student on their Challenge 5 round: rubric scores, one key strength, and one specific thing to practice.

## Wrap Up & Thanksgiving Break Plan (5 min)

**No class Monday 11/23 or Wednesday 11/25.** Over the break:

- Finish your system design — **walkthroughs happen in Session 11 (Mon 11/30)**, 20 minutes each
- Keep your pipeline moving: the week of Thanksgiving is slow for hiring, so it's a good time for follow-ups and informational interviews with people who have free time
- Choose a target job description for your full mock loop in Session 12
- Send your final outreach and informational interview logs — due Session 11

## Additional Resources

1. [System Design Exercise](../Assignments/System_Design.md)
1. [Glossary](../README.md#glossary) (RAG, LLM, API, REST)
