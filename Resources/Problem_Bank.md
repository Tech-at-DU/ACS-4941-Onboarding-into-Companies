# Problem Bank

Problems for the [Technical Interview Challenge Rotation](../Assignments/Technical_Challenges.md) and in-class mock interviews, grouped by interview format. Problem names in the algorithm section match common practice sites (LeetCode, NeetCode, HackerRank), so you can find extra test cases there.

---

## Format 1: Algorithms & Data Structures (timed)

Time limit: 35–45 minutes per problem, including talking through your approach. Practice saying your approach out loud *before* you code.

### Warm-up (use for the Week 1 diagnostic)

| Problem | Core idea |
| --- | --- |
| Two Sum | Hash map for O(n) lookup |
| Valid Parentheses | Stack |
| Valid Anagram | Counting characters with a hash map |
| Best Time to Buy and Sell Stock | Track a running minimum |
| Merge Two Sorted Lists | Linked list pointers |
| Maximum Depth of Binary Tree | Recursion on trees |

### Interview level (use for Week 4)

| Problem | Core idea |
| --- | --- |
| Group Anagrams | Hash map with a computed key |
| Top K Frequent Elements | Hash map + heap or bucket sort |
| Longest Substring Without Repeating Characters | Sliding window |
| Merge Intervals | Sort, then sweep |
| Product of Array Except Self | Prefix and suffix products |
| Number of Islands | Graph traversal (BFS or DFS — breadth-first or depth-first search) |
| Binary Tree Level Order Traversal | BFS with a queue |
| LRU Cache | Hash map + doubly linked list (good for discussing design) |
| Climbing Stairs / House Robber | Introductory dynamic programming |

---

## Format 2: Take-Home Challenges

Time budget: 3–4 hours. Submit a GitHub repo with a README that explains how to run it, what you'd do with more time, and (if AI was allowed) an AI-use note. See the [disclosure guidance](AI_In_The_Job_Search.md#6-disclosure-when-and-how-to-tell-employers-you-used-ai).

Pick any language or framework you're comfortable with unless the prompt says otherwise.

### TH-1: Link Shortener API

Build a small API with two endpoints: `POST /links` takes a long URL and returns a short code; `GET /:code` redirects to the original URL. Track how many times each link was visited and expose it at `GET /links/:code/stats`. Validate input, handle unknown codes, and include tests.

### TH-2: Event RSVP App

Build a web page where someone can view an event and RSVP with name and email. Prevent duplicate RSVPs by email, cap attendance at a limit, and show a waitlist once full. Include a simple admin view listing attendees.

### TH-3: CSV Expense Report

Write a command-line tool that reads a CSV of expenses (date, category, amount, description), and prints totals by category and by month. Handle malformed rows gracefully and report them at the end. Include tests for the parsing logic.

### TH-4: Rate Limiter

Implement a rate limiter that allows at most N requests per user per minute. Expose it as middleware in a small web server. In your README, explain the tradeoffs of your approach and what would change if you ran multiple servers.

### TH-5: Extend an Existing Codebase

Take one of your classmates' take-home submissions from an earlier week (with permission) and add a feature the instructor assigns. This is how many companies run follow-up interviews: "extend the code you (or someone) wrote."

---

## Format 3: Debug an Unfamiliar Codebase

Time limit: 30–45 minutes. The goal is not just to fix the bug but to show *how* you find it: reproduce it, form a hypothesis, narrow it down, fix it, and verify the fix.

### DB-1: The off-by-something pagination

Users report that every page of search results shows one fewer item than it should, and some results never appear on any page.

```python
def paginate(items, page, page_size):
    """Return the items for a 1-indexed page number."""
    start = (page - 1) * page_size
    end = start + page_size - 1
    return items[start:end]
```

### DB-2: The disappearing cart items

Adding the same product twice sometimes resets the quantity instead of increasing it.

```javascript
function addToCart(cart, productId, qty) {
  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.qty = qty;
  } else {
    cart.push({ id: productId, qty });
  }
  return cart;
}
```

### DB-3: The slow dashboard

A dashboard takes 20 seconds to load for users with many projects. Find the performance problem.

```python
def dashboard(user):
    projects = db.query("SELECT * FROM projects WHERE owner_id = ?", user.id)
    result = []
    for p in projects:
        tasks = db.query("SELECT * FROM tasks WHERE project_id = ?", p.id)
        result.append({"project": p.name, "open_tasks": len([t for t in tasks if not t.done])})
    return result
```

*(Hint for debrief: this is the "N+1 query" problem — one query for the list, then one more query per item.)*

### DB-4: Bring your own

The instructor provides a small open source repo with a known bug and an issue description. Clone it, reproduce the bug, and fix it. This is closest to what a real debugging interview looks like.

---

## Format 4: Code Review (including AI-generated code)

Time limit: 20–30 minutes. You're given a pull request (PR — a proposed code change). Leave review comments as you would on GitHub: what's wrong, why it matters, and what to do instead. Rank issues by severity.

AI tools write a lot of code that *looks* correct. Reviewing it critically is one of the most important skills for a junior developer in 2027.

### CR-1: AI-generated signup endpoint

The PR description says: "Added user signup endpoint (generated with AI assistant, tested locally)." Find every problem you can. There are at least six.

```javascript
app.post('/signup', async (req, res) => {
  const { email, password } = req.body;
  const user = await db.query(
    `SELECT * FROM users WHERE email = '${email}'`
  );
  if (user.length > 0) {
    return res.status(200).send('User already exists: ' + JSON.stringify(user[0]));
  }
  const hashed = md5(password);
  await db.query(
    `INSERT INTO users (email, password) VALUES ('${email}', '${hashed}')`
  );
  console.log('New signup', email, password);
  res.send({ success: true });
});
```

<details>
<summary>Instructor answer key</summary>

1. SQL injection — user input is pasted directly into the query string; use parameterized queries.
2. Leaks the existing user's full record (including password hash) in the response.
3. Wrong status code for a duplicate (200 instead of 409 Conflict).
4. Reveals whether an email is registered (account enumeration) — discuss the tradeoff.
5. MD5 is not a password hashing algorithm; use bcrypt, scrypt, or Argon2.
6. Logs the plaintext password.
7. No input validation (email format, password length).
8. No error handling if the database call fails.
9. Race condition: two simultaneous signups with the same email can both pass the check — needs a unique constraint in the database.
10. "Tested locally" with no tests in the PR.

</details>

### CR-2: AI-refactored utility

The PR says: "Refactored date helpers for readability (AI-assisted)." Compare before and after. Did the refactor change behavior?

```javascript
// Before
function isWeekend(date) {
  const day = date.getDay();
  return day === 0 || day === 6;
}

// After
const isWeekend = (date) => [5, 6].includes(date.getDay());
```

*(Debrief: `getDay()` returns 0 for Sunday, so the "readability" refactor silently changed the logic. AI refactors often introduce small behavior changes — always check with tests.)*

### CR-3: Review a classmate's take-home

Swap take-home submissions from Week 2 and review each other's code as a PR. Practice giving feedback that is specific, kind, and actionable.

---

## Format 5: AI-Assisted Coding Round (live)

Time limit: 30 minutes in class (45 minutes for longer practice on your own). You use an AI assistant or coding agent of your choice while the interviewer watches. You're graded on the criteria in [AI in the Job Search, Section 5](AI_In_The_Job_Search.md#5-ai-assisted-coding-interviews), not just whether the code works.

Rules:

- Narrate what you're doing. Silence while the AI works is a red flag.
- Read and explain every change before accepting it.
- The interviewer will ask "why?" about the final code, and may ask you to change something *without* the AI.

### AI-1: Add a feature to a starter app

Given a small to-do API (instructor provides), add due dates and an endpoint that returns overdue tasks, with tests. The starter code has one pre-existing bug the AI is likely to miss.

### AI-2: Build from a vague spec

"We want a way for users to export their data." That's the whole spec. Ask clarifying questions first, then decide on scope, then build it with the AI. Graded heavily on the questions you ask and how you scope the work.

### AI-3: Fix a failing test suite

Given a repo with five failing tests, get them passing. The AI will be tempted to change the tests instead of the code — catching that is part of the challenge.

### AI-4: Speed + judgment

Build a small web page that fetches data from a public API and displays it with search and sorting. Should take about 20 minutes with AI help. The remaining time is spent on the interviewer's follow-up questions: error handling, accessibility, performance, and what you'd test.
