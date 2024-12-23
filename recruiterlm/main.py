import os
import multiprocessing
from github import Github

def process_user(user):
    user_idx = user.id  # or any unique identifier for the user
    print(f"{user_idx} User: {user.login}")

    # Filter high-ball followers
    n_followers = user.get_followers().totalCount
    print(f"\tFollowers: {n_followers}")

    # Get repositories sorted by last push date
    repos = user.get_repos(sort='pushed', direction='desc')
    
    # Fetch the 10 latest active repositories and record
    # the ones that are Python repos which are not forks
    python_repos = []
    for i, repo in enumerate(repos):
        # Stop the loop after 10 iterations
        if i >= 10:
            break

        if repo.language != "Python" or repo.fork:
            continue

        python_repos.append(repo)

    # Filter people who have less than 3 recent Python repositories
    if len(python_repos) < 3:
        print("\tNot enough Python")
        return None

    # Search for Emacs Lisp and Vim Script in the user's top 100 repositories
    found_emacs_vim = False
    for i, repo in enumerate(repos):
        # Stop the loop after 100 iterations
        if i >= 100:
            break

        if not repo.language:
            continue

        if repo.language.lower() == "emacs lisp" or repo.language.lower() == "vim script":
            found_emacs_vim = True
            break

    if not found_emacs_vim:
        print("\tNo Emacs or Vim")
        return None

    # Save the filtered user
    print("\t+++ User is a hit! +++")
    return user

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'), per_page=30)

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin", followers="<2000")

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the process_user function over the users
        filtered_users = pool.map(process_user, users[:500])

    # Filter out None values (users that did not meet the criteria)
    filtered_users = [user for user in filtered_users if user]

    # Print all of the `filtered_users`
    for user in filtered_users:
        print(f"User: {user.login}")

if __name__ == '__main__':
    main()
