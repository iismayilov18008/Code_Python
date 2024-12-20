import requests

url=input("Enter the URL: ")
# worldlist=input("Enter the WordList: ")
extension=input("Enter the Extension: '.html etc' ")

f=open("dirbuster.txt", "r")

for i in f:
    
    fullurl=url+i+extension
    response=requests.get(fullurl)
    if response.status_code == 200:
        print(f"URL exists: {fullurl.strip()} --> {response.status_code}")
    else :
        print(f"URL does not exists: {fullurl}")
        

    
