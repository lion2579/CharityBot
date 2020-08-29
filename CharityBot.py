import praw
import datetime
import time

reddit = praw.Reddit("bot")
keyPhrase = []
startTime = time.time()

def confirm():
    affirmation = ""
    def displayAnswer():
        print("You answered: " + affirmation + "\n-----------------------------------------------------")
    while affirmation != 'y' and affirmation != 'n':
        affirmation = input("Is this correct? Y/n\n")
        affirmation = affirmation.lower()
        if affirmation == 'y':
            displayAnswer()
        elif affirmation == 'n':
            displayAnswer()
            print("Terminating program execution.")
            quit()
        else:
            print("Invalid input.")
            displayAnswer()

def main():
    subreddit = reddit.subreddit("")
    print("I'm alive\n-----------------------------------------------------")
    print("I'm in r/" + subreddit.display_name + "\n-----------------------------------------------------")
    confirm()
    for submission in subreddit.stream.submissions():
        if submission.created_utc > startTime:
            for word in keyPhrase:
                if word in submission.title.lower():
                    print("title: " + submission.title)
                    print("time: " + datetime.datetime.fromtimestamp(
                    int(submission.created_utc)
                    ).strftime('%Y-%m-%d %H:%M:%S') +"\n-----------------------------------------------------")
                    replyto = reddit.submission(submission.id)
                    replyto.reply("Please donate to [charity name](charity url)\n\n*I'm a bot! If you have any comments, concerns, or improvement suggestions; shoot me a message!*")
                    break

main()
