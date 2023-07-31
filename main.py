import wikipedia

def generate_random_article():
    while True:
        try:
            random_article = wikipedia.random()
            page = wikipedia.page(random_article)
            return page
        except wikipedia.exceptions.DisambiguationError as e:
            # If a disambiguation error occurs, try fetching another random article.
            continue
        except wikipedia.exceptions.HTTPTimeoutError:
            print("Failed to fetch the article. Please try again later.")
            return None

def main():
    while True:
        user_input = input("Would you like to read a random Wikipedia article? (y/n): ").strip().lower()
        if user_input == "y":
            article = generate_random_article()
            if article:
                print(f"Title: {article.title}")
                print(f"Summary:\n{article.summary}")
            else:
                print("Failed to generate the article. Please try again later...")
        elif user_input == "n":
            print("Thank you for using. Have a great day!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
