import praw
import datetime

reddit = praw.Reddit("bot")
print("I'm alive\n-----------------------------------------------------")
subreddit = reddit.subreddit("")
print("I'm in r/" + subreddit.display_name + "\n-----------------------------------------------------")
keyphrase = [""]
for submission in subreddit.stream.submissions():
    for word in keyphrase:
        if word in submission.title.lower():
            print("title: " + submission.title)
            print("time: " + datetime.datetime.fromtimestamp(
            int(submission.created_utc)
            ).strftime('%Y-%m-%d %H:%M:%S') +"\n-----------------------------------------------------")
            replyto = reddit.submission(submission.id)
            replyto.reply("Please donate to [insert charity]\n\n*I'm a bot! If you have any comments, concerns, or improvement suggestions; shoot me a message!*")
            replyto.hide()
