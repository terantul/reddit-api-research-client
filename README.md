# Reddit API Research Client

## Project Description

This project is a lightweight Reddit research client designed for public discussion trend analysis and software feedback aggregation. It is intended for internal research and experimentation purposes only.

## Features
- Read-only Reddit API usage
- Public subreddit content ingestion
- Basic filtering of spam/bot content
- Rate limiting
- No voting/commenting/posting
- No user profiling
- No resale of Reddit data
- No automated engagement

## API Usage Policy
- The client intentionally uses conservative request pacing and respects Reddit API rate limits.
- Only accesses public content
- Respects Reddit rate limits
- Does not store private user information
- Does not perform behavioral profiling
- Does not repost Reddit content
- No spam automation
- No account automation

## Example Workflow
1. Fetch posts from selected subreddits
2. Filter obvious spam/bot/promotional content
3. Store lightweight metadata for internal analysis
4. Aggregate trends at topic level

## Setup

1. Create a `.env` file based on `.env.example`:

```
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the demo:

```
python src/main.py
```

## Disclaimer

This repository is a minimal public compliance example and does not represent the full internal research infrastructure.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**This project is not intended for commercial redistribution of Reddit content.**