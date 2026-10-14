# AI in the Job Search

AI now shows up at every stage of getting hired, on both sides of the table. Employers use it to filter resumes, run first-round interviews, and write job descriptions. Candidates use it to prepare, apply, and (sometimes) cheat. This guide covers what you need to know to use AI well, stay honest, and not get caught out.

Throughout this guide, "AI tool" means an LLM-based assistant (LLM = large language model, the technology behind ChatGPT, Claude, Gemini, and Copilot).

---

## 1. How employers use AI

Knowing what's on the other side helps you prepare for it.

| Stage | What employers use AI for | What it means for you |
| --- | --- | --- |
| Job posting | Drafting job descriptions | Postings are often generic or inflated. Focus on the core 3–4 requirements, not the whole wish list. |
| Resume screening | ATS (applicant tracking system) software ranks and filters applications; some use AI to summarize or score resumes against the job description | Clear structure and honest keyword overlap with the posting matter. Weird formatting can get your resume misread. |
| First-round screen | AI phone screens, AI chat screens, and recorded video interviews scored partly by AI | You may never talk to a human in round one. Practice speaking clearly and concisely to a machine. (See Section 4.) |
| Take-homes | Checking whether submitted code looks AI-generated, or explicitly allowing AI and grading how you used it | Read the instructions closely. Follow the AI rules exactly, and disclose when asked. |
| Live interviews | Proctoring tools, cheating detection, and AI-assisted coding rounds | Expect to either be watched closely *or* be required to use AI. Be ready for both. |
| Fraud prevention | Identity checks, often because of fake candidates using AI-generated identities and deepfake video | More in-person final rounds, ID verification, and "camera on" requirements. This is normal now, not a sign of distrust. |

---

## 2. Using AI to prepare (encouraged)

AI is an excellent, free, always-available practice partner. Use it.

**Good uses:**

- **Mock interviews.** Ask an AI tool to interview you for a specific role, one question at a time, and to give you feedback after each answer. Voice mode makes this feel close to a real phone screen.
- **Resume critique.** Paste your resume and a job description and ask: "What would a hiring manager find weak or unclear here? What's missing compared to the posting?" Then make the edits yourself.
- **Company research.** Ask for a summary of what a company does, its products, and recent news — then verify the facts on the company's own site. AI tools get company details wrong often.
- **Explaining code.** Paste unfamiliar code and ask it to walk through what happens. Great preparation for debugging interviews.
- **Algorithm practice.** After you've tried a problem yourself, ask for hints (not answers), or ask it to review your solution's time complexity.
- **Behavioral prep.** Ask it to turn your rough notes into STAR format (Situation, Task, Action, Result), then rewrite the result in your own words.
- **Negotiation role-play.** Ask it to play a recruiter making you an offer, and practice your responses out loud.

**Prompts that work well:**

```text
Act as a hiring manager interviewing me for a junior full-stack developer
role at a 50-person startup. Ask me one question at a time. After each answer,
tell me in two sentences what was strong and what was weak, then ask the next
question. Start with "Tell me about yourself."
```

```text
Here's a job posting and my resume. List the three most important
requirements in the posting, and for each one tell me whether my resume shows
clear evidence of it. Don't rewrite anything — just point out gaps.
```

```text
I'm going to paste a function. Don't tell me what's wrong. Ask me questions
that help me find the bug myself.
```

---

## 3. Where AI hurts your job search

AI makes some things *too* easy, and employers notice.

- **AI-sounding resumes.** Phrases like "spearheaded," "leveraged cutting-edge," and "passionate about driving impact" are now a red flag. Recruiters read hundreds of identical AI resumes. Use plain, specific language with real numbers.
- **AI-written outreach.** A generic, perfectly polished cold message is easy to spot and easy to ignore. The messages that get replies are short, specific, and clearly written by a person who looked at the recipient's work.
- **Mass auto-apply tools.** Tools that submit hundreds of applications for you flood the system and rarely work. Some companies flag candidates who apply to dozens of roles at once. Ten targeted applications with referrals beat 500 auto-applies.
- **Portfolio projects you can't explain.** If an AI built your project and you can't explain why it's structured the way it is, a 10-minute conversation will expose it. Interviewers *will* ask "why did you do it this way?"
- **Hallucinated facts.** AI tools confidently invent company facts, salary numbers, and technical details. Verify anything you plan to repeat in an interview.

**Rule of thumb:** use AI to get feedback and generate options, then do the final writing yourself.

---

## 4. AI-run interviews (AI screens)

Many companies now use AI to conduct first-round interviews. These come in three forms:

1. **AI phone screen** — an AI voice calls you (or you call it) and asks screening questions: background, interest in the role, availability, salary expectations, sometimes basic technical questions.
2. **AI chat screen** — the same, but by text in a chat window.
3. **Async video interview** — you're shown questions and record your answers on camera, usually with limited prep time and limited retakes. A human, AI, or both review the recordings later.

**How to do well:**

- **Be concise and structured.** AI scoring often rewards clear, relevant answers. Aim for 60–90 seconds per answer. Lead with the answer, then give one example.
- **Use the language of the job description** where it honestly fits — the AI is often comparing your answers to it.
- **Speak clearly and at a steady pace.** Pauses are fine. Talking over the AI is not.
- **Have notes nearby** for facts (your projects, your availability, your salary range) — but don't read a script; it sounds flat.
- **Treat it like a real interview.** Recordings and transcripts are often passed to a human reviewer.
- **Test your setup:** camera, microphone, lighting, quiet room, stable internet.
- **Know your rights.** Some places (for example, Illinois and New York City) require employers to tell you when AI is used in hiring decisions. You can ask the recruiter how the screen is evaluated and whether a human reviews the results.

**What you'll practice in this course:** In Session 6, you'll run AI phone screens in class using free AI voice tools. See [AI Screen Practice](../Assignments/AI_Screen_Practice.md).

---

## 5. AI-assisted coding interviews

A growing number of companies now *require* you to use an AI tool in a coding interview. They want to see how you'll actually work on the job. You may be given:

- An AI chat assistant alongside a coding environment, or
- An AI coding agent (a tool like Claude Code, Cursor, or GitHub Copilot's agent mode that can read files, run commands, and edit code on its own) inside a real codebase.

**What interviewers are grading:**

| They watch for | Good looks like |
| --- | --- |
| Problem understanding | You clarify requirements *before* prompting. You don't hand the AI a vague task. |
| Task breakdown | You split the work into small, checkable steps instead of asking for everything at once. |
| Clear direction | Your prompts give context, constraints, and what "done" means. |
| Verification | You read every change, run the code, write or run tests, and check edge cases. |
| Catching mistakes | You notice when the AI is wrong, overcomplicated, or insecure — and fix it. |
| Ownership | You can explain every line in the final solution and why it's there. |
| Communication | You narrate what you're doing and why, just like a regular coding interview. |

**Common ways candidates fail:**

- Accepting the first output without reading it
- Prompting in circles when the AI gets stuck, instead of debugging themselves
- Being unable to explain the code once the interviewer asks "why?"
- Going silent while the AI works

You'll practice this in Sessions 8 and 9.

---

## 6. Disclosure: when and how to tell employers you used AI

**Default rule: follow the employer's instructions exactly.** If instructions are unclear, ask: *"What's your policy on using AI tools for this take-home?"* Asking is a good signal, not a bad one.

| Situation | What to do |
| --- | --- |
| Take-home says AI allowed | Use it, and include a short note in your README: which tool, what you used it for, and what you changed or verified yourself. |
| Take-home says no AI | Don't use it. Many companies follow up with a live session where you extend your own code — it shows quickly. |
| Take-home says nothing | Ask. If you can't ask, disclose any meaningful AI use in your README. |
| Live interview, no AI mentioned | Assume no AI unless told otherwise. Ask if unsure. |
| Portfolio projects | It's fine to say "I used Claude Code / Copilot for parts of this" — then show what *you* decided, tested, and fixed. |
| Resume and cover letter | No disclosure needed for editing help, but every claim must be true and in your own voice. |

**Sample README disclosure:**

```markdown
## AI Use
I used Claude to generate the initial test scaffolding and to suggest the
SQL query in `reports.py`. I rewrote the query to fix an N+1 problem it
introduced, added the input validation myself, and wrote the error-handling
tests by hand.
```

---

## 7. What crosses the line

**Do not use hidden "interview assistant" tools** — software that listens to a live interview or reads your screen and secretly feeds you answers. They are widely marketed to job seekers, and:

- Interviewers are trained to spot them (eye movement, reading cadence, pauses, answers that don't match follow-up questions).
- Interview platforms detect many of them.
- Getting caught usually means immediate rejection and, at many companies, being permanently flagged.
- Even if it works, you'll be hired for a job you can't do yet — and fail on the job.

Also off-limits:

- Having someone else (or an AI voice/video) interview for you
- Claiming AI-generated work as entirely your own when asked directly
- Inventing experience, metrics, or skills on your resume, even if an AI suggested them

---

## 8. Privacy and safety

- Never paste your Social Security number, passport details, bank information, home address, or passwords into an AI tool.
- Don't paste a company's confidential take-home materials into tools that may train on your data unless the company allows AI use. Check your tool's data/training settings and turn off training where possible.
- **Watch for AI-powered job scams.** Fake recruiters (sometimes using AI voices or video), fake "take-homes" that ask you to download and run suspicious code, and fake job offers that ask for bank details or payment for equipment. Red flags: interviews only over text chat, offers with no real interview, requests for money or personal financial info before a signed offer, and email domains that don't match the company.

---

## 9. AI at work (after you're hired)

Every company has different rules about AI tools. In your first week, find out:

- Which AI tools are approved, and which are banned
- Whether you can paste company code into external AI tools (often: no, or only approved ones)
- What the team's norms are for AI-generated code in pull requests (PRs — proposed code changes submitted for review)
- Whether AI-generated code needs to be labeled

The engineers who do best treat AI output like code from a fast but unreliable new teammate: useful, but always reviewed. See [Lesson 14](../Lessons/Lesson14.md).
