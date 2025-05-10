# Lab 17: Refactor code in ‘hn_submissions.py’
# Name: Justin Tang
# Date: 5/9/2025
# Relevant Comments: A lot easier than I thought.

from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    """

    for submission_id in submission_ids[:30] (input): This function processes all information via a try-except
    function and sees if any KeyErrors exist here.

    """
    try:
    # Make a new API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

    # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)

        submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)
    
    except KeyError:
       print("{response_dict} cannot be implemented here!")

for submission_dict in submission_dicts:

    """
    
    for submission_dict in submission_dicts (print): This function prints out results for the output that
    in turn, are determined by the inputs-outputs from the submission_dict dictionary.

    """

    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")