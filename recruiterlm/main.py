import os

from github import Github

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin")

    breakpoint()
    # Print the login of each user found and their top 5 most recent repositories
    for user in users:
        # Get repositories sorted by last push date
        repos = user.get_repos(sort='pushed', direction='desc')
        
        # Print the top 5 most recent repositories
        for i, repo in enumerate(repos[:5], start=1):
            print(f"  {i}. {repo.name}")

if __name__ == '__main__':
    main()
