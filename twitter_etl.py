import tweepy
import json
from pathlib import Path
import os

import pandas as pd


DEFAULT_USERNAME = "elonmusk"
DEFAULT_OUTPUT_PATH = "refined_tweets.csv"
TEXT_FIELDS = ("text", "full_text", "content", "tweet_text")
DATE_FIELDS = ("created_at", "createdAt", "date", "timestamp")
LIKE_FIELDS = ("favorite_count", "like_count", "likes", "favorites")
RETWEET_FIELDS = ("retweet_count", "reposts", "retweets", "shares")
WRAPPED_FIELDS = ("tweets", "data", "results", "items")


def first_value(row, fields):
    for field in fields:
        value = row.get(field)
        if value not in (None, ""):
            return value
    return None


def coerce_count(value):
    if value in (None, ""):
        return 0
    try:
        if pd.isna(value):
            return 0
    except (TypeError, ValueError):
        pass
    try:
        return int(float(str(value).replace(",", "")))
    except (TypeError, ValueError):
        return 0


def read_xquik_export(path):
    export_path = Path(path)
    suffix = export_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(export_path).to_dict("records")

    text = export_path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if suffix == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    payload = json.loads(text)
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for field in WRAPPED_FIELDS:
            rows = payload.get(field)
            if isinstance(rows, list):
                return rows
    return []


def normalize_xquik_rows(rows):
    refined_tweets = []
    for row in rows:
        text = first_value(row, TEXT_FIELDS)
        if text is None or not str(text).strip():
            continue
        refined_tweets.append(
            {
                "user": row.get("username") or row.get("user") or "xquik",
                "text": str(text).strip(),
                "favorite_count": coerce_count(first_value(row, LIKE_FIELDS)),
                "retweet_count": coerce_count(first_value(row, RETWEET_FIELDS)),
                "created_at": first_value(row, DATE_FIELDS) or "",
            }
        )
    return refined_tweets


def write_tweets(refined_tweets):
    output_path = os.getenv("TWITTER_OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    df = pd.DataFrame(refined_tweets)
    df.to_csv(output_path, index=False)
    return output_path


def run_twitter_etl():
    xquik_export_path = os.getenv("XQUIK_EXPORT_PATH")
    if xquik_export_path:
        refined_tweets = normalize_xquik_rows(read_xquik_export(xquik_export_path))
        output_path = write_tweets(refined_tweets)
        print(f"Imported {len(refined_tweets)} Xquik rows to {output_path}.")
        return refined_tweets

    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_key = os.getenv("TWITTER_ACCESS_TOKEN")
    access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    required_values = [consumer_key, consumer_secret, access_key, access_secret]
    if any(value in (None, "") for value in required_values):
        raise ValueError(
            "Set TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, "
            "TWITTER_ACCESS_TOKEN, and TWITTER_ACCESS_TOKEN_SECRET."
        )

    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # # # Creating an API object 
    api = tweepy.API(auth)
    username = os.getenv("TWITTER_USERNAME", DEFAULT_USERNAME)
    count = int(os.getenv("TWITTER_MAX_RESULTS", "200"))
    tweets = api.user_timeline(
        screen_name=username,
        count=count,
        include_rts=False,
        tweet_mode="extended",
    )

    refined_tweets = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        refined_tweets.append(refined_tweet)

    output_path = write_tweets(refined_tweets)
    print(f"Wrote {len(refined_tweets)} rows to {output_path}.")
    return refined_tweets


if __name__ == "__main__":
    run_twitter_etl()
