#Taking arn from user and extracting it:
#python3 extract_users.py arn:aws:iam::123:user/batman - imput gives batman as output

import sys #allow script to talk with terminal

def extract_user(arn):
    return arn.split("/")[-1]

if len(sys.argv) > 1 :
    arn = sys.argv[1]
    username = extract_user(arn)
    print(f"The usename is: {username}")

#Notice the f before the quote? That stands for "format". It lets you put variables directly inside the string using {}.