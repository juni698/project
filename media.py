import os

FILENAME = "social.txt"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file: 

            pass  

def analyze_sentiment(post_text):
    sentiment_score = int(input("enter a score :"))
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"


def add_post(posts):
    post_id = int(input("Enter a unique post ID: "))
    if post_id in posts:
        print("Error: A post with this ID already exists.")
        return

    post_text = input("Enter the post content: ")
    sentiment = analyze_sentiment(post_text)
    posts[post_id] = (post_text, sentiment)
    print(f"Success! Post added with ID '{post_id}' and sentiment: {sentiment}")


def edit_post(posts):
    post_id = int(input("Enter the ID of the post you want to edit: "))
    if post_id not in posts:
        print("Error: Post not found.")
        return

    new_post_text = input("Enter the new post content: ")
    sentiment = analyze_sentiment(new_post_text)
    posts[post_id] = (new_post_text, sentiment)
    print(f"Post with ID '{post_id}' updated. New sentiment: {sentiment}")


def delete_post(posts):
    post_id = int(input("Enter the ID of the post you want to delete: "))
    if post_id not in posts:
        print("Error: Post not found.")
        return

    del posts[post_id]
    print(f"Post with ID '{post_id}' has been deleted.")


def search_post(posts):
    keyword = input("Enter the keyword to search for: ")
    found_posts = {id_: (text, sentiment) for id_, (text, sentiment) in posts.items() if keyword.lower() in text.lower()}

    if not found_posts:
        print("No posts found with the given keyword.")
        return

    print("\nFound Posts:")
    for post_id, (post_text, sentiment) in found_posts.items():
        print(f"Post ID: {post_id}\nText: {post_text}\nSentiment: {sentiment}\n")


def display_all_posts(posts):
    if not posts:
        print("No posts available.")
        return

    print("\nAll Posts:")
    for post_id, (post_text, sentiment) in posts.items():
        print(f"Post ID: {post_id}\nText: {post_text}\nSentiment: {sentiment}\n")


def main():
    posts = {}
    initialize_file()

    while True:
        print("\n--- Social Media Sentiment Analysis ---")
        print("1. Add a new post")
        print("2. Edit an existing post")
        print("3. Delete a post")
        print("4. Search for posts by keyword")
        print("5. Display all posts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_post(posts)
        elif choice == '2':
            edit_post(posts)
        elif choice == '3':
            delete_post(posts)
        elif choice == '4':
            search_post(posts)
        elif choice == '5':
            display_all_posts(posts)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

initialize_file ()
main()
