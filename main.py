import requests

BASE_URL_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines"
BASE_URL_EVERYTHING = "https://newsapi.org/v2/everything"


def get_top_news(api_key):
    """
    Get current top headlines and print them.
    """
    params = {
        "country": "us",  # you can change this if you want
        "pageSize": 10,
        "apiKey": api_key
    }

    try:
        response = requests.get(BASE_URL_TOP_HEADLINES, params=params)
    except Exception as e:
        print("Error when trying to connect to News API:", e)
        return

    if response.status_code != 200:
        print("News API returned an error:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()

    articles = data.get("articles", [])
    if not articles:
        print("No news articles found.")
        return

    print("\n=== Top Headlines ===\n")
    for index, article in enumerate(articles, start=1):
        title = article.get("title") or "No title"
        source = article.get("source", {}).get("name") or "Unknown source"
        url = article.get("url") or "-"

        print(f"{index}. {title}")
        print(f"   Source: {source}")
        print(f"   Link: {url}\n")


def search_news(api_key):
    """
    Ask user for a search keyword and print matching news.
    """
    keyword = input("Enter search keyword: ").strip()

    if keyword == "":
        print("You must enter something to search.")
        return

    params = {
        "q": keyword,
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": api_key
    }

    try:
        response = requests.get(BASE_URL_EVERYTHING, params=params)
    except Exception as e:
        print("Error when trying to connect to News API:", e)
        return

    if response.status_code != 200:
        print("News API returned an error:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()

    articles = data.get("articles", [])
    if not articles:
        print("No news found for that keyword.")
        return

    print(f"\n=== Search results for '{keyword}' ===\n")
    for index, article in enumerate(articles, start=1):
        title = article.get("title") or "No title"
        source = article.get("source", {}).get("name") or "Unknown source"
        url = article.get("url") or "-"

        print(f"{index}. {title}")
        print(f"   Source: {source}")
        print(f"   Link: {url}\n")


def main():
    print("News API Demo Program")
    print("---------------------")
    api_key = input("Enter your NewsAPI.org API key: ").strip()

    if api_key == "":
        print("API key cannot be empty. Exiting.")
        return

    while True:
        print("\nMenu:")
        print("1. Show current top news")
        print("2. Search news by keyword")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            get_top_news(api_key)
        elif choice == "2":
            search_news(api_key)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
