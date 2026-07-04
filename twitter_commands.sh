sudo apt-get update
sudo apt install python3-pip
python3 -m pip install -r requirements.txt

export TWITTER_USERNAME='elonmusk'
export TWITTER_MAX_RESULTS='200'
export TWITTER_OUTPUT_PATH='refined_tweets.csv'

# For live Twitter API extraction, set these credentials:
export TWITTER_CONSUMER_KEY='your_consumer_key'
export TWITTER_CONSUMER_SECRET='your_consumer_secret'
export TWITTER_ACCESS_TOKEN='your_access_token'
export TWITTER_ACCESS_TOKEN_SECRET='your_access_token_secret'

# For Xquik export replay, set this instead of live credentials:
export XQUIK_EXPORT_PATH='data/xquik-export.jsonl'
