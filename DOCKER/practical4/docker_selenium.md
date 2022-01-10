# Run Selenium in a Docker Container

These are the steps you have to follow to create the Dockerfile. For each of the steps, you have to figure out what Dockerfile instructions you have to use for each step


1. Pull a Python image. For example, python:3.8-slim-buster will do the job

2. Adding trusting keys to apt for repositories, you can download and add them using the following command:
`wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -`
3. Add Google Chrome. Use the following command for that
`sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'`
4. Update apt:
`apt-get -y update`
5. And install google chrome:
`apt-get install -y google-chrome-stable`

6. Now you need to download chromedriver. First you are going to download the zipfile containing the latest chromedriver release:
apt-get install -yqq unzip

```
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
```
7. You downloaded the zip file, so you need to unzip it:
```
apt-get install -yqq unzip

unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
```
8. Set an environment variable to set a display port:

`DISPLAY=:99`

9. Copy your application in a Docker image

10. Install your requirements

11. Run your application