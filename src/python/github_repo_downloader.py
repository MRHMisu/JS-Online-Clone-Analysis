"""
Web scraper for downloading repository from GitHub.
"""

import os
import sys

import requests
from bs4 import BeautifulSoup

NUMBER_OF_REPO = 10


def download_repository_each_search_result_page(url, store_dir_path):
    r = requests.get(url)
    repository_tags = BeautifulSoup(r.content, "lxml").find_all("a",
                                                                "v-align-middle")  # tailor this filter for desired tags
    master_zip_url = "https://www.github.com/{}/archive/master.zip"
    list_of_repo = store_dir_path + "/" + "downloaded_repositories.txt"

    for tag in repository_tags:
        repo = tag.string
        zip_url = master_zip_url.format(repo)
        save_file_path = (store_dir_path + "/{}.zip").format(repo.replace("/", "__"))
        global NUMBER_OF_REPO
        if NUMBER_OF_REPO > 0:
            download_and_save_a_repository(repo, zip_url, save_file_path, list_of_repo)
            NUMBER_OF_REPO -= 1
        else:
            break


def download_and_save_a_repository(repo, zip_url, save_file_path, list_of_repo):
    if not os.path.exists(save_file_path):
        print("Downloading  archive =" + repo)
        response = requests.get(zip_url)
        if response.status_code == 404:
            print("Cannot find the master branch of " + repo)
            print("Try main branch")
            zip_url = zip_url.replace("master", "main")
            response = requests.get(zip_url)
            if response.status_code == 404:
                print("Cannot find the main branch of " + repo)
                return
        with open(save_file_path, "wb+") as f:
            f.write(response.content)
        with open(list_of_repo, "a") as f:
            f.write(repo + "," + zip_url + "\n")
    else:
        print("Already downloaded the archive " + repo + ", skipping...")


def construct_url(lan, min_star):
    base = "https://github.com/search"
    query = "q=stars%3A%3E{star}+language%3A{language}"
    query_filter = "o=desc&s=forks&type=Repositories"
    pagination = "p={page_no}"
    complete_url = base + "?" + query + "&" + query_filter
    pagination_url = complete_url.format(star=min_star, language=lan) + "&" + pagination
    return pagination_url


def download_repo(url, directory_to_store):
    for i in range(30):
        if NUMBER_OF_REPO > 0:
            print("Downloading page " + str(i + 1))
            download_repository_each_search_result_page(url.format(page_no=(i + 1)), directory_to_store)


def execute():
    # Run the script with 4 cmd arguments
    # 1) language
    # 2) minimum_star
    # 3) number_of_repository_to download
    # 4) directory_to_store
    #
    # command to run the script
    # ~ python github_repo_downloader.py JavaScript 35 2 /home/mrhmisu/UCL-MS/Test-Data/SCC-Jar/

    global NUMBER_OF_REPO
    language = sys.argv[1]
    minimum_star = sys.argv[2]

    NUMBER_OF_REPO = int(sys.argv[3])
    # number_of_repo = int(sys.argv[3])
    directory_to_store = sys.argv[4]
    url = construct_url(language, minimum_star)
    download_repo(url, directory_to_store)
    sys.exit()


execute()
