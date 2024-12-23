import os

from github import Github

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin")

    breakpoint()
    # Print the login of each user found and their top 5 most recent Python repositories
    for user in users:
        print(f"User: {user.login}")
        
        # Get the user object to access repositories
        user_obj = g.get_user(user.login)
        
        # Get Python repositories sorted by last push date
        repos = user_obj.get_repos(sort='pushed', direction='desc', language='Python')
        
        # Print the top 5 most recent Python repositories
        for i, repo in enumerate(repos[:5], start=1):
            print(f"  {i}. {repo.name}")

if __name__ == '__main__':
    main()
