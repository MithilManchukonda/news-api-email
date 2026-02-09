import requests
from send_email import send_email

topic = "tesla"

api_key = "enter your api key"

url = (
    "https://newsapi.org/v2/everything?q=tesla&from=2025-11-20&sortBy=publishedAt&apiKey=your api key"

)

request = requests.get(url)
content = request.json()

body = "Subject: Tesla News Updates\n\n"

for article in content["articles"][:20]:
    if article["title"]:
        body += (
            article["title"] + "\n"
            + (article["description"] or "") + "\n"
            + article["url"] + "\n\n"
        )

send_email(body.encode("utf-8"))
