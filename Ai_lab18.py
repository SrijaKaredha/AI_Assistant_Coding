#Create a Python program using requests to fetch top 5 news headlines by category with retry mechanism and error handling.
import requests

API_KEY = "your_api_key_here"

def get_news(category):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"

    for attempt in range(2):  # retry
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                articles = data['articles'][:5]

                print("\nTop Headlines:")
                for i, article in enumerate(articles, 1):
                    print(f"{i}. {article['title']}")
                return
            else:
                print("❌ API Error")

        except requests.exceptions.RequestException:
            print("Retrying...")

    print("❌ Failed after retry")

get_news("technology")
