import requests
import csv

def fetch_and_print_posts():
    link = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(link)
    print("Status Code:",response.status_code)
    if response.status_code == 200:
        response_json = response.json()
        print("Title:", response_json["title"])
        
def fetch_and_save_posts():
    link = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(link)
    if response.status_code == 200:
        response_json = response.json()
        posts = [{
            "id": response_json["id"],
            "title": response_json["title"],
            "body": response_json["body"]
        }]
        
    with open('posts.csv', 'w', encoding="UTF-8") as f:
        listy = ['id', 'title', 'body']
        add = csv.DictWriter(f, listy)
        add.writeheader()
        for post in posts:
            add.writerow(post)