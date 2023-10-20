# python scrapper to extra stats
# testUrl = 'https://news.ycombinator.com/'

import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt 
# Request docs: https://requests.readthedocs.io/en/latest/
# beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
# matplotlib docs: https://matplotlib.org/stable/index.html

def main():
    # print("Hello World")
    # request url and connect it to BS
    testUrl = 'https://news.ycombinator.com/item?id=37739028'
    response = requests.get(testUrl)

    # Beautiful soup object
    # inspect page and look for div class of what we want
    soup = bs(response.content, "html.parser")

    # gives list of elements containing 
    # find where class ind = 0 so it doesn't look at child comments
    elements = soup.find_all(class_="ind", indent=0)

    # after class ind = 0 the comment class exists with the content
    # elements is a list so this iterates all items in elements
    comments = [e.find_next(class_="comment") for e in elements]
    text = [e.get_text() for e in comments]


    # print basics
    print(f"Scraping: {testUrl}")
    print("response get code:", response)

    print("Num of comments:",len(comments))
    print()

    # wanted keywords (coding languages)
    keywords = {
        "python": 0,
        "javascript":0, 
        "typescript":0, 
        "ruby":0, 
        "java":0, 
        "c++":0
    }


    # iterates all comments, get readable human text and then counts for a specific word
    for comment in comments:
        # gets readabable text in lowercase for case sensitivity
        comment_text = comment.get_text().lower()
        # creates an array of each word split by whitespace
        words = comment_text.split(" ")
        # creates a new set for words that removes duplicate words
        words = {w.strip(".,/:;!@") for w in words}

        # iterates the words set and if keyword k is in set, iterate the keyword
        for k in keywords:
            if k in words:
                keywords[k] += 1
        # print(words)
        # print()
        # print(comment_text)
    print(keywords)

    # plt.bar(x-axis, y-axis) | keywords.keys = left side of dictionary | keyword.values = right side 
    # plt.bar(keywords.keys(), keywords.values() )
    # plt.xlabel("Language")
    # plt.ylabel("# of mentions")
    # plt.show()

if __name__ == "__main__":
    main()
