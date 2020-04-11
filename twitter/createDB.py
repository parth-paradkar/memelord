from config import db

cursor = db.cursor()

try:
    tweetTable = "CREATE TABLE `fetched_tweets` (`ID` INT NOT NULL AUTO_INCREMENT, `tweet_ID` VARCHAR(255) NOT NULL, `tweet_screen_name` VARCHAR(255) NOT NULL, `tweet_fetched_time` VARCHAR(255) NOT NULL, `tweet_text` VARCHAR(255) NOT NULL, `tweet_media_url` VARCHAR(255) NOT NULL, `posted_on_slack` VARCHAR(1) NOT NULL DEFAULT 'N', UNIQUE(`tweet_ID`), PRIMARY KEY(`ID`))"
    

    topTweets = "CREATE TABLE `top_tweets` (`ID` INT NOT NULL AUTO_INCREMENT, `tweet_ID` VARCHAR(255) NOT NULL, `tweet_screen_name` VARCHAR(255) NOT NULL, `tweet_fetched_time` VARCHAR(255) NOT NULL, `tweet_text` VARCHAR(255) NOT NULL, `tweet_media_url` VARCHAR(255) NOT NULL, `posted_on_slack` VARCHAR(1) NOT NULL DEFAULT 'N', UNIQUE(`tweet_ID`), PRIMARY KEY(`ID`))"

    cursor.execute(tweetTable)
    cursor.execute(topTweets)
    db.commit()

except Exception as e:
    print(e)



