# Problem Bank

Problems for the [Technical Interview Challenge Rotation](../Assignments/Technical_Challenges.md) and in-class mock interviews, grouped by interview format.

---

## Format 1: Algorithms & Data Structures (timed)

Time limit: 35–45 minutes per problem, including talking through your approach. Practice saying your approach out loud *before* you code.

**Some of these may look new, but they aren't.** Real interviewers rarely give a problem its textbook name. They wrap it in a story about their product. Part of the skill is looking past the story to the problem underneath: *"This is really a counting problem," "this is a graph," "I've seen this shape before."* For each problem, try to name the pattern before you start coding. The answer key is at the end of this section.

### Warm-up (use for the Week 1 diagnostic)

#### W-1: Gift Card Checkout

A customer wants to pay for a purchase using exactly two gift cards. Given a list of gift card balances and the purchase total, return the positions of the two cards whose balances add up to exactly the total. Assume there is exactly one answer, and a card can't be used twice.

```text
balances = [25, 10, 40, 12, 30], total = 55   →   [0, 4]   (25 + 30)
```

#### W-2: Config File Validator

Your team's config files use three kinds of grouping symbols: `()`, `[]`, and `{}`. A file is valid only if every opening symbol is closed by the same kind of symbol, in the right order. Given a string containing only these characters, return whether it's valid.

```text
"{[()()]}"   →   true
"{[(])}"     →   false
"(("         →   false
```

#### W-3: Word Game Tile Check

In a word game, a player has a rack of letter tiles. Given the letters on the rack and a word the player wants to play, return whether the word uses **every** tile on the rack exactly once (no tiles left over, none missing).

```text
rack = "tnsiel", word = "listen"   →   true
rack = "tnsiel", word = "lists"    →   false
```

#### W-4: Concert Ticket Resale

You're tracking the resale price of a concert ticket each day for a month. You may buy one ticket on one day and sell it on a **later** day. Return the most profit you could make. If no profit is possible, return 0.

```text
prices = [90, 60, 85, 50, 70, 110, 95]   →   60   (buy at 50, sell at 110)
prices = [120, 100, 80]                  →   0
```

#### W-5: Merging Two Playlists

Two playlists are stored as linked lists, each already sorted by song length (shortest first). Merge them into one linked list sorted by song length, reusing the existing nodes instead of creating new ones.

```text
A: 2:10 → 3:05 → 4:40
B: 1:55 → 3:30
→  1:55 → 2:10 → 3:05 → 3:30 → 4:40
```

#### W-6: Chain of Command

A small company's org chart is stored as a tree where each manager has at most two direct reports. Given the CEO's node, return the number of levels in the longest chain of command, from the CEO down to an employee with no reports.

```text
        CEO
       /   \
     CTO   CFO
     /
   Lead
   /
 Junior            →   4
```

### Interview level (use for Week 4)

#### I-1: Bot Account Detector

Spam bots often sign up with usernames that are the same letters scrambled: `"mariel"`, `"mailer"`, `"realim"`. Given a list of usernames, group together the usernames that are rearrangements of each other. Return the groups in any order.

```text
["mailer", "dorm", "mariel", "rodm", "solo", "realim"]
→ [["mailer", "mariel", "realim"], ["dorm", "rodm"], ["solo"]]
```

#### I-2: Trending Tags

Given a list of every tag used in posts today, return the `k` tags used most often. Order within the result doesn't matter.

```text
tags = ["ai", "jobs", "ai", "react", "jobs", "ai", "rust"], k = 2   →   ["ai", "jobs"]
```

Follow-up: what if the list has 100 million tags but only a few thousand distinct ones?

#### I-3: Longest Fresh Streak

A music app logs your listening history as a string where each character is a song ID. Find the length of the longest stretch of **consecutive** plays in which no song repeats.

```text
"abcabcbb"   →   3   ("abc")
"bbbbb"      →   1
"pwwkew"     →   3   ("wke")
```

#### I-4: Calendar Busy Blocks

Given a list of meetings as `[start, end]` times (in minutes after 9:00 AM, not sorted), combine any meetings that overlap or touch into single busy blocks. Return the busy blocks sorted by start time.

```text
[[60, 90], [0, 30], [80, 120], [30, 45]]   →   [[0, 45], [60, 120]]
```

#### I-5: Leave-One-Out Factors

A factory line has several machines in a row, each with a quality factor. For each machine, engineers want to know the combined factor of **all the other machines** (multiply them together). Return a list with that value for each position. You may not use division — a broken machine can have a factor of 0.

```text
[2, 3, 4, 5]   →   [60, 40, 30, 24]
[1, 0, 3]      →   [0, 3, 0]
```

#### I-6: Wi-Fi Dead Zones

A building's Wi-Fi survey is a grid where `1` means a weak-signal spot and `0` means good signal. Weak spots that touch up, down, left, or right are part of the same dead zone. Count how many separate dead zones there are.

```text
1 1 0 0 0
1 1 0 0 1
0 0 0 1 1
0 0 0 0 0
1 0 0 0 0      →   3
```

#### I-7: Emergency Phone Tree

A school's emergency phone tree is a tree where each person calls at most two others. The principal calls first, then everyone they called makes calls at the same time, and so on. Return a list of rounds, where each round lists the people who receive a call in that round (the principal is round 0).

```text
        Principal
        /       \
     Ana        Ben
     /  \          \
   Cal  Dee        Eve

→ [["Principal"], ["Ana", "Ben"], ["Cal", "Dee", "Eve"]]
```

#### I-8: Recently Viewed Products

An online store shows each shopper their recently viewed products, but only has room to remember `capacity` products. Design a class with two operations, both running in O(1) time:

- `view(product_id, details)` — record that the product was viewed (adding it, or refreshing it if already there). If this goes over capacity, forget the product that was viewed longest ago.
- `get(product_id)` — return the product's details if it's remembered (this counts as a view), or `null` if not.

```text
capacity = 2
view(1, "mug"); view(2, "hat"); get(1) → "mug"
view(3, "pen")      // forgets product 2, the least recently viewed
get(2) → null
```

#### I-9: Parking Garage Ramps

You're walking up a parking garage with `n` levels. Each ramp takes you up either 1 level or 2 levels. How many different sequences of ramps get you from the ground to level `n`?

```text
n = 3   →   3   (1+1+1, 1+2, 2+1)
n = 5   →   8
```

#### I-10: Delivery Tips

A delivery driver has a street of houses, each with a known tip amount. Company policy says the driver can't deliver to two houses right next to each other on the same shift. Return the largest total tip the driver can collect.

```text
tips = [5, 1, 2, 9, 3]   →   14   (houses 0 and 3 → 5 + 9)
tips = [2, 7, 9, 3, 1]   →   12   (2 + 9 + 1)
```

<details>
<summary>Answer key: patterns & classic names (try to spot them yourself first)</summary>

| Problem | Pattern | Classic name you may have seen |
| --- | --- | --- |
| W-1 Gift Card Checkout | Hash map: store what you've seen, look up the complement | Two Sum |
| W-2 Config File Validator | Stack | Valid Parentheses |
| W-3 Word Game Tile Check | Count characters with a hash map | Valid Anagram |
| W-4 Concert Ticket Resale | Track a running minimum | Best Time to Buy and Sell Stock |
| W-5 Merging Two Playlists | Linked list pointers | Merge Two Sorted Lists |
| W-6 Chain of Command | Recursion on trees | Maximum Depth of Binary Tree |
| I-1 Bot Account Detector | Hash map with a computed key (sorted letters or letter counts) | Group Anagrams |
| I-2 Trending Tags | Hash map + heap or bucket sort | Top K Frequent Elements |
| I-3 Longest Fresh Streak | Sliding window | Longest Substring Without Repeating Characters |
| I-4 Calendar Busy Blocks | Sort, then sweep | Merge Intervals |
| I-5 Leave-One-Out Factors | Prefix and suffix products | Product of Array Except Self |
| I-6 Wi-Fi Dead Zones | Graph traversal (BFS or DFS — breadth-first or depth-first search) | Number of Islands |
| I-7 Emergency Phone Tree | BFS with a queue | Binary Tree Level Order Traversal |
| I-8 Recently Viewed Products | Hash map + doubly linked list | LRU Cache |
| I-9 Parking Garage Ramps | Introductory dynamic programming (Fibonacci-shaped) | Climbing Stairs |
| I-10 Delivery Tips | Dynamic programming: take it or skip it | House Robber |

Once you've solved one, search the classic name to find more test cases and practice problems with the same pattern.

</details>

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
