import praw
import datetime
import time

reddit = praw.Reddit("bot") # Make sure that the praw.ini file has the bot's information listed under the [bot] tag. https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
keyPhrase = [] # Enter the keyPhrase that will trigger the bot to comment on the post.
startTime = time.time()

# Confirms that the user has entered the correct information.
## If the information is incorrect, the program terminates.
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
    subreddit = reddit.subreddit("") # Enter your preferred subreddit here.
    
    # Uses the confirm() method listed above.
    print("I'm alive\n-----------------------------------------------------")
    print("I'm in r/" + subreddit.display_name + "\n-----------------------------------------------------")
    confirm()
    
    # Monitors recent submissions for the keyPhrase.
    for submission in subreddit.stream.submissions():
        if submission.created_utc > startTime:
            for word in keyPhrase:
                if word in submission.title.lower():
                    print("title: " + submission.title)
                    print("time: " + datetime.datetime.fromtimestamp(
                    int(submission.created_utc)
                    ).strftime('%Y-%m-%d %H:%M:%S') +"\n-----------------------------------------------------")
                    replyto = reddit.submission(submission.id)
                    replyto.reply("Please donate to [charity name](charity url)\n\n*I'm a bot! If you have any comments, concerns, or improvement suggestions; shoot me a message!*") # Enter the charity's name and url in their respective boxes and modify the message if you'd like.
                    break

main()
