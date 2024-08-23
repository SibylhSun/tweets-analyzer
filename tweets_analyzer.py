import pandas as pd
import tweepy

class TweetsAnalyzer:
    def __init__(self, df, term):
        """
        Initialize the TweetsAnalyzer with a DataFrame and a search term.

        :param df: Pandas DataFrame containing tweet data.
        :param term: The search term to filter tweets by.
        """
        self.df = self.preprocess_dataframe(df)
        self.term = term

    def preprocess_dataframe(self, df):
        """
        Preprocess the DataFrame before analysis.
        """
        df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
        df['year'] = df['created_at'].dt.year
        df['month'] = df['created_at'].dt.month
        df['day'] = df['created_at'].dt.day
        df['created_at_date'] = pd.to_datetime(df[['year', 'month', 'day']])
        return df


    def count_tweets_with_term_by_date(self):
        """
        Count the number of tweets containing the specified term, grouped by the date of creation.

        :return: A Series with dates as index and the count of tweets as values.
        """
        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Group the filtered tweets by 'created_at_date' and count the number of tweets each day
        return df_term.groupby('created_at_date').count()['text']

    def count_of_users_posted_with_term(self):
        """
        Count the number of unique users who posted tweets containing the specified term.

        :return: An integer count of unique users.
        """
        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Count the number of unique users who posted these tweets
        count_of_users = df_term['author_id'].nunique()
        return count_of_users

    def count_of_likes_with_term(self):
        """
        Calculate the average number of likes for tweets containing the specified term.

        :return: A float representing the average number of likes per tweet.
        """
        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Avoid division by zero if no tweets with the term are found
        if len(df_term) == 0:
            return 0.0
        
        # Calculate the average number of likes for these tweets
        count_of_likes = df_term['like_count'].mean()
        return count_of_likes

    def get_place(self):
        """
        Retrieve the place details for tweets containing the specified term using Tweepy.

        :return: A DataFrame with tweet ID, place ID, and place name.
        """
        # TODO: Set up your credentials
        api_key = 'your_api_key'
        api_key_secret = 'your_api_key_secret'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        
        # Authenticate with Twitter API using Tweepy
        auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        api = tweepy.API(auth)

        # Verify API credentials
        try:
            api.verify_credentials()
            print("Authentication OK")
        except tweepy.TweepError as e:
            print(f"Error during authentication: {e}")

        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Retrieve place details based on 'place_id' from the tweets
        # Ensure 'place_id' exists and is valid before querying
        if 'place_id' in df_term.columns and not df_term['place_id'].isna().all():
            df_term['place'] = df_term['place_id'].apply(lambda id: api.place(id).full_name if id else None)
        else:
            df_term['place'] = None
        
        return df_term[['id', 'place_id', 'place']]

    def time_tweet_posted(self):
        """
        Extract the time each tweet was posted for tweets containing the specified term.

        :return: A DataFrame with tweet ID and the time it was posted.
        """
        
        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Extract the time from 'created_at' and add it to a new 'time' column
        df_term = df_term['created_at'].dt.time

        return df_term[['id', 'time']]

    def user_posted_most_term(self):
        """
        Identifies the user who posted the most tweets containing a specific term.

        :returns: dict: A dictionary containing the 'author_id' of the user who posted the most tweets with the specified term.
        """
        # Filter tweets containing the term
        df_term = self.df[self.df["text"].str.contains(self.term, na=False)]
        
        # Group by 'author_id' and count the number of tweets per user, then sort in descending order
        user = df_term.groupby('author_id').count().sort_values('id', ascending=False)[:1].index.values[0]
        
        # Return the 'author_id' of the user with the most tweets containing the term
        return {'author_id': user}


# Example usage
if __name__ == "__main__":
    # Assuming 'path_to_file.tsv' is a path to your data file
    df = pd.read_csv('path_to_file.tsv', sep='\t')
    # Convert the 'created_at' column to datetime format
    df = self.df.copy()
    analyzer = TweetsAnalyzer(df, 'your_search_term')
    # Example method calls
    print(analyzer.count_tweets_with_term_by_date())
    print(analyzer.count_of_users_posted_with_term())
    print(analyzer.count_of_likes_with_term())
    print(analyzer.get_place())
    print(analyzer.time_tweet_posted())
    print(analyzer.user_posted_most_term())
