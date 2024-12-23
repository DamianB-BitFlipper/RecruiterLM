import os

from github import Github

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin")

    # Print the login of each user found and their top 5 most recent repositories
    filtered_users = []
    for user in users[:50]:
        if not user.hireable:
            continue
        print(f"User: {user.login}")

        # Get repositories sorted by last push date
        repos = user.get_repos(sort='pushed', direction='desc')
        
        # Fetch the 10 latest active repositories and record the ones that are Python repos
        python_repos = []
        for i, repo in enumerate(repos[:10], start=1):
            if repo.language != "Python":
                continue

            python_repos.append(repo)

        # Filter people who have less then 3 recent Python repositories
        if len(python_repos) < 3:
            continue



if __name__ == '__main__':
    main()
