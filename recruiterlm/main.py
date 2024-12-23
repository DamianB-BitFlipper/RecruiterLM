import os

from github import Github

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin")

    breakpoint()
    # Print the login of each user found
    for user in users:
        print(user.login)

if __name__ == '__main__':
    main()
