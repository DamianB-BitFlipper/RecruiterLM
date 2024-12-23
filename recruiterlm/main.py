from github import Github

def main():
    # Replace 'your_access_token' with your actual GitHub access token
    g = Github("your_access_token")
    
    # Search for users with location set to Berlin
    users = g.search_users(query='location:Berlin', per_page=100)
    
    # Print the login of each user found
    for user in users:
        print(user.login)

if __name__ == '__main__':
    main()
