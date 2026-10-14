# Free Deployment Options

Your proof-of-work project needs a live URL by Session 4. "Deploy" means putting your app on the internet at a public URL so anyone — including a recruiter on their phone — can use it.

A hiring manager is far more likely to click a working link than to clone a repo and run it locally. A live URL is the cheapest credibility boost you can get.

> Free tiers change often. Check each provider's current limits before you pick one. None of these should require a credit card for a basic hobby project, but some may ask for one to verify your identity.

## Pick a host by project type

| Project type | Good free options | Notes |
| --- | --- | --- |
| Static site (HTML/CSS/JS, React/Vue/Svelte build) | GitHub Pages, Netlify, Vercel, Cloudflare Pages | Easiest. Connect your GitHub repo and it deploys on every push. |
| Next.js or other full-stack JavaScript framework | Vercel, Netlify | Serverless functions included on free tiers. |
| Backend API or server app (Node, Python/Flask/FastAPI, Go) | Render, Koyeb, Fly.io (check current free allowance) | Free servers often "sleep" when idle and take 30–60 seconds to wake up. Mention this in your README. |
| Database | Supabase (Postgres), Neon (Postgres), MongoDB Atlas free tier, Turso (SQLite) | Use environment variables for connection strings — never commit them. |
| Mobile app | Expo (for React Native) preview links, TestFlight for iOS, or a recorded demo video plus a web version | If you can't deploy, a 2-minute demo video linked at the top of your README is the next best thing. |

## Deployment checklist

- [ ] The app loads at a public URL on a phone and a laptop
- [ ] No secrets (API keys, database passwords) are committed to the repo — use environment variables
- [ ] If the app needs login, there's a demo account or a "try as guest" option, listed in the README
- [ ] The live URL is at the top of the README and in the GitHub repo's "About" section
- [ ] If the server sleeps when idle, the README says so ("first load may take 30 seconds")
- [ ] If the app calls a paid AI API, it has a usage limit so a stranger can't run up a bill

## Using AI tools to deploy

AI coding assistants are good at writing deployment configs and explaining error logs. Use them — but:

- Read every config file it writes and know what it does. "How did you deploy this?" is a common interview question.
- Never paste secret keys into an AI chat.
- If a deploy fails, read the actual error log first, then ask the AI about the specific error.
