----->Task 01 :
# Generate Python code using requests to fetch current weather for a city using a weather API. Include error handling for invalid city, API key errors, and network issues.
import requests

API_KEY = "your_api_key_here"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            print("Temperature:", data['main']['temp'], "°C")
            print("Humidity:", data['main']['humidity'], "%")
            print("Weather:", data['weather'][0]['description'])
        elif response.status_code == 404:
            print("❌ City not found")
        else:
            print("❌ API Error:", response.status_code)

    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.RequestException:
        print("❌ Network error")

get_weather("Hyderabad")

------> Task 02 :
# Create a Python program using requests to convert INR to USD, EUR, and GBP using an exchange rate API with input validation and error handling.
import requests

def convert_currency(amount):
    try:
        url = "https://api.exchangerate-api.com/v4/latest/INR"
        response = requests.get(url, timeout=5)

        data = response.json()

        usd = amount * data['rates']['USD']
        eur = amount * data['rates']['EUR']
        gbp = amount * data['rates']['GBP']

        print("\nConverted Values:")
        print("USD:", usd)
        print("EUR:", eur)
        print("GBP:", gbp)

    except Exception:
        print("❌ Error fetching exchange rates")

amount = float(input("Enter INR amount: "))
convert_currency(amount)

-----> Task 03 :
# Write Python code using requests to fetch GitHub repository details like stars, forks, and issues with error handling for invalid repo and rate limits.
import requests

def get_repo_info(owner, repo):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            print("Name:", data['name'])
            print("Description:", data['description'])
            print("Stars:", data['stargazers_count'])
            print("Forks:", data['forks_count'])
            print("Open Issues:", data['open_issues_count'])
        elif response.status_code == 404:
            print("❌ Repository not found")
        else:
            print("❌ API Error")

    except requests.exceptions.RequestException:
        print("❌ Network error")

get_repo_info("python", "cpython")

-----> Task 04 :
# Create a Python program using requests to fetch top 5 news headlines by category with retry mechanism and error handling.
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
