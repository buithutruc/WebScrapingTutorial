# Reading a local html file using python
from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify()) to see the html code in a pretty way

    courses_html_tags = soup.find_all("h5") #find will return only the first h5 tag

    for course in courses_html_tags:
        print(course.text)
