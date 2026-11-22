
"""
Reddit research collector prototype.

Requires approved Reddit Data API access.
Read-only: does not post, vote, or message users.
"""

import os
import requests

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

SUBREDDITS = ["webdev", "selfhosted", "nextjs", "SaaS"]

KEYWORDS = [
    "deployment failed",
    "hosting problems",
    "railway alternative",
    "render cold start",
    "vercel deployment",
]


def collect():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Reddit API credentials not configured.")
        print("API access approval is required before collection.")
        return []

    # API authentication and collection will be
    # implemented after Reddit grants access.
    print("Reddit collector is awaiting API integration.")
    return []


if __name__ == "__main__":
    collect()
