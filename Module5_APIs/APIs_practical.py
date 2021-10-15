#%% Top upvoted
# - Look at the StackExchange API docs [here](https://api.stackexchange.com/docs)
# - Find the 10 most highly voted posts in the last day.
# - How many upvotes do they have?
# - Make sure to use the query string params defined in the documentation.

# /2.3/posts?pagesize=10&fromdate=1633996800&
# todate=1634083200&order=desc&sort=votes&site=stackoverflow

import requests
from pprint import pprint
from requests.api import request

from requests.models import Response

url = "http://api.stackexchange.com/2.3/posts"
data = {"pagesize": "10", # no of posts per page
        "fromdate" : "1633996800", 
        "todate" : "1634083200", 
        "order" : "desc", 
        "sort" : "votes",
        "site" : "stackoverflow"}
posts = requests.get(url, params=data).json()
pprint(posts)
for n in range(len(posts["items"])):
    print(posts["items"][n]["score"])

type(posts)
print(posts.keys())
#items is a list of dictionaries, one per post
print(posts['items'][0])


score = [post['score'] for post in posts['items'] ] # gets the same as the for loop above
print(score)

# %% Most recent badges awarded

# - Using the StackExchange API
# - Find the first 3 badges by alphabetical order of their name.
# - Find the most recent 3 users to be awarded each of these badges

# copied from stack exchange: /2.3/badges/name?pagesize=3&order=asc&sort=name&site=stackoverflow

import requests
from pprint import pprint

#can do in 2 ways by passing full url in with params in it as below or by passing in a dictionary of the params into get() as in example above
url = "http://api.stackexchange.com/2.3/badges/name?pagesize=3&order=asc&sort=name&site=stackoverflow"
badges = requests.get(url).json()
print(badges) 
badges.keys()
badges['items'][0] #  Take a look at the first badge awarded. The value of badges['items'] is a dictionary containing info about each badge awarded

first_3_badges_by_name = [ badge['name'] for badge in badges['items']]
print(first_3_badges_by_name)
list_badge_id = [dictionary['badge_id']  for dictionary in badges['items']]
print(list_badge_id)

list_of_dicts = []
for id in list_badge_id:
    url = f"http://api.stackexchange.com/2.3/badges/{id}?&order=asc&sort=rank&site=stackoverflow&pagesize=3"
    list_of_dicts.append(requests.get(url).json())
print(list_of_dicts)
for i in range(len(list_of_dicts)):
    print(list_of_dicts[i]['items'][0]['name'])


# %% Pagination
# - Using the StackExchange API find the first 5 pages of posts from this month
# - Keep the page size small using a query string param to avoid being restricted for making too many requests
# - Hint, what does the "page" query param do? What is on the "Paging" section of the website?
# - create a function which gets all of the responses from an endpoint by paginating through them (essentially put your solution above in a function)

# pagesize = no of posts per page
# page = page number (first 5 pages = pages 1-5)

import requests
from pprint import pprint
import time

def Pagination(url, number_of_pages, pagesize):
    list_of_dictionaries = []
    page_num = 1 
    while page_num <= number_of_pages:
        pages_and_pagesize = {'page' : str(page_num), 'pagesize' : str(pagesize)}
        list_of_dictionaries.append(requests.get(url, params=pages_and_pagesize).json())
        page_num += 1
        time.sleep(2) # implement a timeout so not to be rate-limited
    return list_of_dictionaries #return a list of dictionaries, 1 for each page 

# test the function using posts function from the stack exchange API with date, 
url = 'http://api.stackexchange.com/2.3/posts?&fromdate=1633046400&todate=1634169600&order=asc&sort=creation&site=stackoverflow'
# mylist = Pagination(url, 1, 1 ) # gets 1 page with 1 post in it
# pprint(mylist[0]['items'])

# mylist = Pagination(url, 5, 10) # gets 5 pages with 10 posts in each
# pprint(mylist[4]['items']) # look at the posts on page 5
# print(len(mylist[0]['items'])) # number of posts on page 5 ( = 10)
#%%

len(mylist[0]['items'])

# %% Most curious
#Using the StackExchange API find the 5 users with the most questions posted in the last day

import requests
import time

# first find how many questions were asked in the last day so can work out how many pages to ask for
# use a custom filter that uses 'total' instead of 'items' in the wrapper of the 'questions' API
url = 'http://api.stackexchange.com/2.3/questions?page=1&pagesize=2&fromdate=1634256000&order=desc&sort=creation&site=stackoverflow&filter=!-)3Kfj1w8kqK'
question_count = requests.get(url).json()
total_no_questions_in_last_day = question_count['total']
num_of_pages = total_no_questions_in_last_day // 100 # max is 100 (note:should round up not down really! )

# now call Pagination function with url that includes all the question 'items' from the last day to get a list of all the questions
url1 = 'http://api.stackexchange.com/2.3/questions?fromdate=1634256000&order=desc&sort=activity&site=stackoverflow'
list_of_questions = Pagination(url1, num_of_pages, 100)

# now check first and last pages have 100 questions to make sure we received the data ok
print(len(list_of_questions[0]['items']) == 100)
print(len(list_of_questions[num_of_pages-1]['items']) == 100)  

#%%
# Now find the users who asked the most questions: 
temp = {}
#for i in range(len(list_of_questions)):
for i in range(5):
    for dict in list_of_questions[i]['items']: 
        if dict['owner']['display_name'] in temp.keys():
            temp[dict['owner']['display_name']] += 1
        else:
            temp[dict['owner']['display_name']] = 1

most_curious_users = sorted(temp, key=temp.get, reverse=True)[0:6]
most_curious_users_with_score = {most_curious_users[i] : temp[most_curious_users[i]] for i in range(len(most_curious_users))}
print(most_curious_users_with_score)



