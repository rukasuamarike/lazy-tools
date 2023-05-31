#open chrome tabs
import webbrowser
import sys,os
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

#precondition: txt file with lines of urls
f=open(f'{sys.path[0]}/{sys.argv[1]}',"r")
data=f.readlines()
for url in data:
    webbrowser.get(chrome_path).open(url.strip())