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

1. **Prepare:** split your documents into small chunks (a few paragraphs each) and turn each chunk into an **embedding**: a list of numbers that represents what the text means. Chunks with similar meaning get similar numbers. Store each chunk's text, its embedding, and who's allowed to see it, often in a "vector database" (a database that finds similar embeddings).
1. **Retrieve:** when a question comes in, turn the question into an embedding too. Then find the chunks whose embeddings are closest *among the chunks this user is allowed to see*.
1. **Generate:** send the question *plus* those chunks to the LLM, with instructions to answer only from the provided text and say "I don't know" otherwise.

Those instructions *reduce* made-up answers, but they don't guarantee anything. LLMs still sometimes ignore them. That's why you show sources and test with evals (below).

**Permissions happen at retrieval, not in the prompt.** Filter chunks by the user's access *before* anything is sent to the LLM. Telling the LLM "don't reveal salary data to non-managers" is not a security control. If a restricted chunk reaches the LLM, assume it can end up in the answer.

**Do you need a special vector database?** Not always. 500 pages is only about 250,000 tokens, which is small. Postgres with the `pgvector` extension can store embeddings next to your other tables. A strong tradeoff answer: "I'd start with pgvector in our existing Postgres. I'd move to a dedicated vector database only if search got slow."

**Estimating cost: a worked example.** LLM APIs charge per **token** (roughly ¾ of a word). Teach yourself the formula, not specific prices, because prices change often:

> cost per question = (input tokens × input price) + (output tokens × output price)

For "Ask the Handbook":

| Number | Estimate |
| --- | --- |
| Questions per day | 300 employees × ~2 questions/day ≈ **600** |
| Input tokens per question | instructions (~300) + 5 chunks × ~500 tokens + question (~50) ≈ **3,000** |
| Output tokens per question | a short answer with sources ≈ **300** |
| Tokens per day | 600 × 3,300 ≈ **2 million** |
| One-time embedding cost | all 500 pages ≈ 250,000 tokens. Embedding is very cheap, so this is usually pennies |

Plug in the current per-million-token prices from your provider's pricing page to get cost per question and per month. The takeaway for an interview: at this size, the cost is small. What drives it is **how many chunks you send** and **how long the answers are**, so those are what you'd tune first. Rate limits per user stop one person (or one bug) from running up the bill.

**Estimating speed:** the embedding and search steps usually take well under a second. Most of the wait is the LLM generating the answer, often a few seconds. Streaming the answer word by word makes that wait feel much shorter.

**Design questions every LLM feature raises:**

| Concern | Questions to answer |
| --- | --- |
| Wrong answers ("hallucinations") | What happens when the answer isn't in the docs? How do you show sources so users can check? |
| Testing ("evals") | What sample questions with known answers will you test against? Do they include questions the docs *can't* answer, where the right answer is "I don't know"? When do you re-run them (for example, after changing the prompt, the model, or the chunk size)? |
| Cost | How much does each question cost in API fees (use the formula above)? What stops abuse? |
| Speed | How long will users wait? Can you stream the answer as it's generated? |
| Privacy & permissions | Can every employee see every document? Where do you filter by access (at retrieval, before the LLM)? What data leaves your servers? |
| Fallback | What happens when the AI provider is down? |

**Interview tip:** junior candidates who bring up testing, cost, and failure modes *without being asked* stand out, because many people treat the LLM as magic.

## We Do: Sketch "Ask the Handbook" (25 min)

As a group, sketch Option C from the [System Design Exercise](../Assignments/System_Design.md#option-c-ai-powered-feature):

- Requirements
- The three RAG steps as boxes in a diagram
- The data model for documents and chunks. Include an embedding column and an access field (for example, `access_group`) on each chunk
- One API endpoint
- A rough cost per question, using the formula from the overview
- Three eval questions with expected answers. **At least one must be a question the handbook can't answer**, so the expected answer is "I don't know." For extra credit, add one that a regular employee should *not* get an answer to because the information is restricted.

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
