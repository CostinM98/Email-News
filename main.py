
import requests

apiKey = '32ca73b20c254b22b027792b060d0dd8'
url = "https://newsapi.org/v2/everything?q=apple&from=2023-01-30&to=2023-01-30&sortBy=popularity&apiKey=32ca73b20c254b22b027792b060d0dd8"

req = requests.get(url)

content = req.json()


for article in content['articles']:

    print(article['title'])
    print(article['description'])
