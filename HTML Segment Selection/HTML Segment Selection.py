"""
Created on Mon May 13 12:42:44 2019

@author: wrichiek.kar
"""

import requests
from bs4 import BeautifulSoup as soup
from threading import Thread
import time

def read_from_txt(path):
    '''
    (None) -> list of str
    Loads up all sites from the sitelist.txt file in the root directory.
    Returns the sites as a list
    '''

    #Initialize variables
    raw_lines = []
    lines = []

    # Load data from the txt file
    try:
        f = open(path, "r")
        raw_lines = f.readlines()
        f.close()

    # Raise an error if the file couldn't be found
    except:
        print ("Couldn't locate <" + path + ">.")
        raise FileNotFoundError

    # Parse the data
    for line in raw_lines:
        lines.append(line.strip("\n"))

    # Return the data
    return lines


def link_obtainer(link):
    # try a link
    try:
        r = requests.get(link, timeout=5, verify=False, allow_redirects=True)
    except:
        print("Connection to URL <" + link + "> failed. Retrying...")
        time.sleep(5)
        try:
            r = requests.get(link, timeout=8, verify=False, allow_redirects=True)

        except:
            print("Connection to URL <" + link + "> failed.")

    page = soup(r.text, "html.parser") #parse html obtained
    raw_readmes = page.findAll("div", {"class": "Box-body"}) #serach for specific section in html

    readme =[]

    for raw_readme in raw_readmes: #search for every div that has class "box body"
        try:
            readme.append(raw_readme)
        except:
            print("No <p> found")
    print(readme)

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings() #ignore SSL warning
    # Load sites from file
    sites = read_from_txt("sites.txt")
    # Start downloading links
    Condition = True
    while (Condition):
        for site in sites:
            Thread(target=link_obtainer, args=(site,)).start() #runs link obtainer on a link
            time.sleep(2)  # 2 second delay before going to the next site (to avoid bans)
        Condition = False
