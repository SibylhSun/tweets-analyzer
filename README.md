# Overview

TweetsAnalyzer is a Python class designed to analyze tweet data. It provides methods to count tweets containing a specific term, analyze the number of users posting those tweets, calculate the average likes, and retrieve place information for tweets.

# Features

count_tweets_with_term_by_date(): Group and count tweets containing the search term by their posting date.

count_of_users_posted_with_term(): Count the number of unique users who posted tweets containing the search term.

count_of_likes_with_term(): Calculate the average number of likes for tweets containing the search term.

get_place(): Retrieve place information for tweets containing the search term using the Twitter API.

time_tweet_posted(): Extract the time of day when tweets containing the search term were posted.

user_posted_most_term(): Get the author_id of the user posted the most tweets containing the search term.

# Prerequisites

Before using TweetsAnalyzer, ensure you have the following installed: \
Python 3.x \
pandas \
tweepy 


# Usage
1. Prepare Your Data
Ensure your tweet data is stored in a tab-separated values (TSV) file or another format that can be loaded into a pandas DataFrame. 

2. Load Data and Initialize TweetsAnalyzer
'''
import pandas as pd
from tweets_analyzer import TweetsAnalyzer

# Load your tweet data into a DataFrame
df = pd.read_csv('path_to_your_file.tsv', sep='\t')

# Define the search term you want to analyze
search_term = 'example_term'

# Initialize the TweetsAnalyzer with the DataFrame and search term
analyzer = TweetsAnalyzer(df, search_term)

3. Analyze Data
You can now use the methods provided by TweetsAnalyzer to analyze your data:

#### Count tweets containing the term on each day
tweet_counts_by_date = analyzer.count_tweets_with_term_by_date()\
print("Number of tweets posted containing the term on each day:", tweet_counts_by_date)

# Count unique users who posted tweets with the term
user_count = analyzer.count_of_users_posted_with_term()\
print("\nCount of unique users who posted with the term:", user_count)

# Calculate the average likes for tweets with the term
average_likes = analyzer.count_of_likes_with_term()\
print("\nAverage likes per tweet with the term:", average_likes)

# Retrieve place details for tweets with the term
# Replace line 76-79 of get_place() method in tweets_analyzer.py with your own Twitter API credentials from twitter
api_key = 'your_api_key'\
api_key_secret = 'your_api_key_secret'\
access_token = 'your_access_token'\
access_token_secret = 'your_access_token_secret'\
Ensure these credentials are added to the get_place method in the TweetsAnalyzer class.

places = analyzer.get_place()\
print("\nPlace details for tweets with the term:", places)

# Extract the time each tweet was posted
times = analyzer.time_tweet_posted()\
print("\nTime each tweet was posted with the term:", times)
'''

## Example
An example of using TweetsAnalyzer can be found in the example_run.ipynb file. This example demonstrates loading data, initializing the class, and calling its methods.
