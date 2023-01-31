import requests
from send_email import sendEmail


topic='apple'
apiKey = '32ca73b20c254b22b027792b060d0dd8'
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-01-30&to=2023-01-30&sortBy=popularity&apiKey=32ca73b20c254b22b027792b060d0dd8&language=en"

req = requests.get(url)

content = req.json()

body = ''
for article in content['articles'][0:20]:
    if article['title'] is not None:
        body ='Subject:News for Today'+'\n'+ body + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2 * '\n'

body = body.encode('utf-8')
sendEmail(message=body)
