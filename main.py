import requests
from send_email import sendEmail

apiKey = '32ca73b20c254b22b027792b060d0dd8'
url = "https://newsapi.org/v2/everything?q=apple&from=2023-01-30&to=2023-01-30&sortBy=popularity&apiKey=32ca73b20c254b22b027792b060d0dd8"

req = requests.get(url)

content = req.json()

body = ''
for article in content['articles']:
    if article['title'] is not None:

        body = body + article['title'] + '\n' + article['description'] + 2 * '\n'

body = body.encode('utf-8')
sendEmail(message=body)
