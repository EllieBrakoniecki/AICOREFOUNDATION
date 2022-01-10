#%%
import boto3 
s3_client = boto3.client('s3')
# %%
response = s3_client.upload_file('cat.jpg', 'awsbucketellieb', 'cat.jpg')
# %%

s3 = boto3.resource('s3')

my_bucket = s3.Bucket('awsbucketellieb')

for file in my_bucket.objects.all():
    print(file.key)
# %%
s3 = boto3.client('s3')

s3.download_file('awsbucketellieb', 'cat.jpg', 'cat_download.jpg')

boto3.client('s3').download_file
# %%

import requests

url = 'https://awsbucketellieb.s3.amazonaws.com/cat.jpg'

response = requests.get(url)
with open('cat1.jpg', 'wb') as f:
    f.write(response.content)
# %%
####################
#ocado scraper
response = s3_client.upload_file('cat_0.jpg', 'cat-scraper', 'cat.jpg')