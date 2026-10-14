# System Design Exercise

**Weight:** 10% · **Introduced:** Session 10 (Wed 11/18) · **Due:** Session 11 (Mon 11/30)

## Why

Junior candidates are increasingly asked lightweight system design questions: not "design Twitter for a billion users," but "how would you build this feature?" Interviewers want to see that you can think about data, APIs, and tradeoffs before writing code. More and more, that feature involves AI.

## The exercise

Choose **one** prompt. Prepare a design you can explain with a whiteboard or diagram, then walk through it in class in Session 11: a 20-minute walkthrough (about 13 minutes presenting, 7 minutes of follow-up questions from the instructor and classmates).

### Option A: Classic feature

Design a **study group scheduler** for a school. Students can create groups for a course, invite others, propose meeting times, and vote on them. Groups get reminders before meetings.

### Option B: Your own project

Pick one feature of your proof-of-work project and design how it would work if your app had 10,000 active users instead of 10.

### Option C: AI-powered feature

Design a **"Ask the Handbook" assistant** for a 300-person company. Employees type questions ("How many vacation days do I get?") and get answers based on the company's internal documents (about 500 pages of policies and how-to guides).

This is a RAG design. RAG (retrieval-augmented generation) means: when a question comes in, first **search** your documents for the most relevant passages, then send those passages along with the question to an LLM (large language model) so its answer is based on your actual documents instead of guesses.

## What your design must cover

1. **Requirements:** What must it do? What's out of scope? Roughly how many users and requests?
1. **Data model:** The main tables or collections, their fields, and how they relate.
1. **API:** The main endpoints (method, path, what goes in, what comes out). REST style is fine — REST is the common style of web API built on URLs and HTTP methods like GET and POST.
1. **Diagram:** Boxes and arrows showing the client, server, database, and any other services.
1. **Tradeoffs:** At least two decisions where you picked one option over another, and why.
1. **What breaks first** as usage grows, and what you'd do about it (caching, indexes, background jobs).

**Additional requirements for Option C:**

- How you'll split and store the documents so they can be searched
- What happens when the answer isn't in the documents (it should say "I don't know," not invent an answer)
- How you'd **test** whether answers are correct (a set of sample questions with known answers — often called "evals")
- Cost and speed: roughly how much each question costs and how long users wait
- Privacy: who's allowed to see which documents

## Using AI on this assignment

Allowed and encouraged for research and for critiquing your design ("What are the weaknesses in this design?"). Not useful for producing the design itself: in the walkthrough, you'll be asked "why?" about every box and arrow, and you need real answers. Note your AI use in one sentence at the top of your design.

## Rubric

| Criteria | Points |
| --- | --- |
| Clear requirements and scope | 15 |
| Sensible data model | 20 |
| Clear API design | 15 |
| Readable diagram | 10 |
| Tradeoffs explained with reasoning | 20 |
| Handles follow-up questions confidently (including "what breaks first?") | 20 |
