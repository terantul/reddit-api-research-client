from reddit_client import RedditClient
from filters import apply_filters

if __name__ == "__main__":
    client = RedditClient()
    posts = client.fetch_posts("programming", limit=10)
    filtered_posts = apply_filters(posts)

    for post in filtered_posts:
        print(post)