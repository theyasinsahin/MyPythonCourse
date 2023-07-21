from operator import itemgetter
import requests

# Make an API Call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)

# Process Information About Each Submission
submission_ids = response.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url)
    response_dict = response.json()

    # Build  a dict for each article
    submission_dict = {
        'title': response_dict['title'],
        'author': response_dict['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'article_score': response_dict['score']
    }
    submission_dicts.append(submission_dict)

# From highest to lowest article score
submission_dicts = sorted(submission_dicts, key=itemgetter('article_score'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Author: {submission_dict['author']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Article Score: {submission_dict['article_score']}")