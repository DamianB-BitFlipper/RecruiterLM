import os

from github import Github

def main():
    g = Github(os.getenv('GITHUB_ACCESS_TOKEN'), per_page=30)

    # Search for users with location set to Berlin
    users = g.search_users("", location="Berlin", followers="<2000")

    # Print the login of each user found and their top 5 most recent repositories
    filtered_users = []
    for user_idx, user in enumerate(users[:500]):
        # user = g.get_user("aliev")
        print(f"{user_idx} User: {user.login}")

        #if not user.hireable:
        #    print("\tUser is not hireable")
        #    continue

        # Filter high-ball followers
        n_followers = user.get_followers().totalCount
        print(f"\tFollowers: {n_followers}")
        # if n_followers > 200:
        #     print(f"\tHigh-ball followers {n_followers}")
        #     continue

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
            continue

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
            continue

        # Save the filtered user
        filtered_users.append(user)
        print("\t+++ User is a hit! +++")

    # Print all of the `filtered_users`
    for user in filtered_users:
        print(f"User: {user.login}")

if __name__ == '__main__':
    main()
