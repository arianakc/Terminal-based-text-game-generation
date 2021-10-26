import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import re
if __name__ == '__main__':
    session = requests.Session()
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "en-US,en;q=0.5",
               "Connection": "keep-alive",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0"}
    r = session.get("https://blog.reedsy.com/short-stories/", headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    genre_list = []
    for option in soup.find_all("option"):
        value = option.get('value')
        if value != "":
            genre_list.append(str(value))
            print(value)
    genre = input("Please input one of genres above:")
    while genre not in genre_list:
        genre = input("Your input is wrong, please input one of genres above, input q to quit:")
        if genre == "q":
            exit(0)
    r = session.get("https://blog.reedsy.com/short-stories/" + genre, headers=headers)
    soup2 = BeautifulSoup(r.text, 'html.parser')
    pages_num = soup2.find(name="span", attrs={"class": "last"}).find("a").get("href").split("/")[-2]
    print(f"There are total {pages_num} pages."
          f"Downloading and Generating per line text data file...")
    wanted_pages = input("How many pages do you want to download?")
    text_data = []
    story_links = []
    with open(f"{genre}.txt", "a+") as f:
        for num in tqdm(range(int(wanted_pages)), total=int(wanted_pages)):
            r = session.get("https://blog.reedsy.com/short-stories/" + genre + "/page/" + str(num + 1), headers=headers)
            soup3 = BeautifulSoup(r.text, 'html.parser')
            stories_in_cur_page = soup3.find_all(name="a", attrs={"class": "no-decoration"})
            for story_link in stories_in_cur_page:
                if len(story_link.get("class")) == 1 and story_link.get("class")[0] == "no-decoration":
                    link = str(story_link.get("href"))
                    if "short-story" in link and link not in story_links:
                        story_links.append(link)
                        story_text = ""
                        s = session.get("https://blog.reedsy.com" + link, headers=headers)
                        while "Retry later" in s.text:
                            print(link)
                            print(s.text)
                            time.sleep(10)
                            s = session.get("https://blog.reedsy.com" + link, headers=headers)
                        soup4 = BeautifulSoup(s.text, 'html.parser')
                        print(link)
                        sps = soup4.find("article").find_all("p")
                        for sp in sps:
                            story_text = story_text + re.sub("</?[a-z]+>", "", " ".join(str(c) for c in sp.contents))
                            # if sp.string is not None and str(sp.string).rstrip("\n\r\t "):
                            #     story_text += str(sp.string).replace("&nbsp", "").rstrip("\n\r") + " "
                        text_data.append(story_text)
                        clean_text = BeautifulSoup(story_text.encode("ascii", "ignore").decode(), "lxml").get_text(strip=True)
                        f.write(clean_text.replace("\n", "").replace("\r", "") + "\n")
    print(f"There are total {len(text_data)} stories downloaded")
    # print(f"Write to {genre}.txt...")
    # with open(f"{genre}.txt", "w") as f:
    #     for text in tqdm(text_data, total=len(text_data)):
    #         f.write(text + "\n")
