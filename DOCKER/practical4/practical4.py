
#%%
import requests
url = 'https://aicore-files.s3.amazonaws.com/Foundations/DevOps/docker_selenium.md'
response = requests.get(url)
with open('docker_selenium.md', 'wb') as f:
    f.write(response.content)

# %%
