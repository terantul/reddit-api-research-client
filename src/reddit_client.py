import requests
import os
from dotenv import load_dotenv

load_dotenv()

class RedditClient:
    def __init__(self):
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")
        self.base_url = "https://www.reddit.com/api/v1"
        self.token = self.get_access_token()

    def get_access_token(self):
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {"grant_type": "client_credentials"}
        headers = {"User-Agent": self.user_agent}

        response = requests.post(f"{self.base_url}/access_token", auth=auth, data=data, headers=headers)
        response.raise_for_status()
        return response.json()["access_token"]

    def fetch_posts(self, subreddit, limit=10):
        headers = {"Authorization": f"bearer {self.token}", "User-Agent": self.user_agent}
        url = f"https://oauth.reddit.com/r/{subreddit}/hot?limit={limit}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["data"]["children"]