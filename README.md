# Cursor IDE Setup - Task Log

## Tools Installed
- **Cursor IDE** - AI-powered code editor (https://cursor.com/)
- **Claude Code extension** - Official Anthropic extension, installed via Cursor Extensions panel
- **Codex extension** - OpenAI's coding agent, installed via Cursor Extensions panel

## Steps Completed
1. Downloaded and installed Cursor IDE from cursor.com
2. Opened Extensions panel (Ctrl+Shift+X) and searched "Claude Code" - installed the official Anthropic extension
3. Searched "Codex" in Extensions - installed OpenAI's Codex coding agent
4. Created a GitHub account at github.com
5. Created a new public repository named `cursor-setup-task`
6. Added this README.md to document the process

## Issues Encountered and How I Solved Them
- No major issues encountered during installation
- The Cursor docs page opened in browser instead of the app - solved by launching Cursor directly from desktop
## Experts Selected

# Research Project-- AI-Powered SEO Content Production

## Why I Chose This Topic
AI-powered SEO content production is one of the fastest-moving areas in digital marketing. 
Traditional SEO is being disrupted by LLMs, AI Overviews, and generative search engines like 
ChatGPT and Perplexity. Understanding how content needs to evolve to rank in this new landscape 
is critical for any modern marketer or business.

---

## Experts Selected

I selected 10 experts based on:
- Proven hands-on experience in SEO, AI content and SaaS marketing
- Active content sharing across LinkedIn, YouTube and podcasts
- Unique, future-facing perspectives on AI search and LLM optimization
- Focus on data-backed insights rather than generic SEO advice

### LinkedIn Connections
1. **Peter Rota** -Senior Technical SEO Manager at HUB International, Top 1% LinkedIn 
   creator in the US with 70,000+ followers. Posts daily on technical SEO, AI search
   and LLM optimization. https://www.linkedin.com/in/peterrota/

2. **Daniel Ndege** - Kenya-based SEO specialist, founder of OnMedia agency and SEO Tab tool. 
   Leads Search 254, Kenya's SEO community. Posts practical AI-powered content strategies. 
   https://www.linkedin.com/in/danielndege/

3. **Mohammed Fakhruddin** -Posts regularly on AI-powered SEO covering SEO vs AEO vs GEO, 
   and how to optimize for generative search engines like ChatGPT and Perplexity. 
   https://www.linkedin.com/in/fakhruddiin/

4. **Bengu Sarica Dincer** -LinkedIn SEO and AI content practitioner sharing insights on 
   search optimization and AI-powered marketing. 
   https://www.linkedin.com/in/bengu-sarica-dincer/

### YouTube Creators
5. **Webhive Digital (Kate Smoothy)** -UK SEO agency founder known for viral bite-sized 
   SEO audit content. Covers on-page SEO, technical audits and AI content strategy. 
   https://www.youtube.com/@webhivedigital

6. **Neil Patel** -Co-founder of NP Digital and Ubersuggest. 2.2M+ YouTube subscribers. 
   Has advised Amazon, Google and Microsoft on SEO and content strategy. 
   https://www.youtube.com/@neilpatel

7. **Matt Diggity** -SEO practitioner since 2009 with 172K+ subscribers. Known for 
   test-based, data-driven SEO strategies. Founder of The Search Initiative and Affiliate Lab. 
   https://www.youtube.com/@MattDiggity

8. **Surfer SEO** -Official channel of leading AI content optimization platform. Covers 
   AI-powered content workflows, NLP-based SEO, topical authority, and ranking in AI search. 
   https://www.youtube.com/@SurferSEO

### Podcast Hosts
9. **Matthew Bertram -The Best SEO Podcast** -Creator of LLM Visibility™, Lead Strategist 
   at EWR Digital. 5M+ downloads. Covers AI-era discoverability and the future of search. 
   https://open.spotify.com/show/4nvjY61QJE93ZCIXWg6wZd

10. **SEO Rockstars -Guillermo Bravo & Eduardo Silva** -Nearfront founders covering AI 
    revolution in SEO, automation and strategies that move the needle. 
    https://open.spotify.com/show/2t9YeoF3nL0fqNQgsrOgvg

---

## Research Structure
research/
├── sources.md              # Full list of all experts with links and annotations
├── linkedin-posts/         # Posts collected from LinkedIn experts
│   ├── peter-rota.md
│   ├── daniel-ndege.md
│   ├── mohammed-fakhruddin.md
│   └── bengu-sarica-dincer.md
├── youtube-transcripts/    # Transcripts extracted via Supadata API
│   ├── neil-patel.md
│   ├── matt-diggity.md
│   ├── surfer-seo.md
│   └── webhive-digital.md
├── podcasts/               # Episode notes from Spotify podcasts
│   ├── best-seo-podcast.md
│   └── seo-rockstars.md
└── other/                  # Additional articles and materials

---

## Key Themes Being Studied
-AI replacing traditional keyword-based search
-LLM optimization vs classic SEO — what changes and what stays
-Content authority and entity-based search
-Data-driven SEO decision making using tools like Surfer SEO
-Zero-click search and SERP evolution
-How brands get cited by ChatGPT, Perplexity, and Google AI Overviews

---

## How Content Was Collected

### YouTube Transcripts
Transcripts were collected using the **Supadata API** with a Python script run inside 
Cursor IDE. The script automatically fetched transcripts from 4 YouTube channels and 
saved them as markdown files in `/research/youtube-transcripts/`.

Tools used:
- Python 3.14
- Supadata SDK (`pip install supadata`)
- Cursor IDE terminal

### LinkedIn Posts
LinkedIn posts were manually collected by visiting each expert's profile and copying 
their most recent posts about AI SEO and content strategy.

### Podcast Notes
Episode summaries and key insights were manually collected from Spotify podcast pages 
and saved in `/research/podcasts/`.

---

## Challenges Faced and How I Resolved Them

### 1. Python not installed
When trying to run the transcript script, the terminal returned `pip is not recognized`. 
Solved by downloading and installing Python 3.14 from python.org and using `py` instead 
of `python` on Windows.

### 2. Git not installed
After collecting transcripts, `git` was not recognized in the Cursor terminal. 
Solved by downloading and installing Git 2.53 from git-scm.com.

### 3. YouTube transcripts pushed to master branch instead of main
After pushing the transcript files, they ended up on the `master` branch instead of 
`main` because the local repo was initialized without specifying the branch name. 
This took significant time to resolve. The fix involved:
-Running `git checkout -b main` to create the main branch locally
-Running `git merge master` to bring all files from master into main
-Running `git pull origin main --allow-unrelated-histories` to sync with GitHub
-Finally running `git push origin main` to push everything to the correct branch

### 4. Vim editor opened unexpectedly
During the merge process, Git opened the Vim text editor in the terminal for a commit 
message. This was unfamiliar and took time to figure out. Solved by pressing `Escape` 
then typing `:wq` and pressing Enter to save and exit.

---

## Outcome
This research will be used to:
-Build modern AI-powered SEO content strategies
-Create high-authority content that ranks in both Google and AI search engines
-Understand how to optimize for LLMs like ChatGPT and Perplexity
-Develop a practical playbook for AI-powered SEO content production
