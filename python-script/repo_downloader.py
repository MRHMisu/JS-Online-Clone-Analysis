"""
Web scraper for downloading repository from GitHub.
"""

import os

import requests
from bs4 import BeautifulSoup


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
        download_and_save_a_repository(repo, zip_url, save_file_path, list_of_repo)


def download_and_save_a_repository(repo, zip_url, save_file_path, list_of_repo):
    if not os.path.exists(save_file_path):
        print("Downloading  archive =" + repo)
        r = requests.get(zip_url)
        with open(save_file_path, "wb+") as f:
            f.write(r.content)
        with open(list_of_repo, "a") as f:
            f.write(repo + "," + zip_url + "\n")
    else:
        print("Already downloaded the archive " + repo + ", skipping...")


def construct_url(lan, min_star):
    base = "https://github.com/search"
    query = "q=stars%3A%3E{star}+language%3A{language}"
    query_filter = "o=desc&s=forks&type=Repositories"
    pagination = "p{}"
    complete_url = base + "?" + query + "&" + query_filter
    pagination_rul = complete_url.format(star=min_star, language=lan) + "&" + pagination
    return pagination_rul


def download_repo(url, num_of_repo):
    number_of_page = (num_of_repo / 10) + 1
    for i in range(number_of_page):
        if (num_of_repo > 0):
            print("Downloading page " + str(i + 1))
            download_repository_each_search_result_page(url.format(i + 1), dir_path_to_store_downloaded_repo)
            num_of_repo -= 1


if __name__ == "__main__":
    language = "JavaScript"  # sys.argv[1]
    minimum_star = 35  # sys.argv[2]
    dir_path_to_store_downloaded_repo = "/home/mrhmisu/UCL-MS/Test-Data/Download-JS-Reop"  # "#sys.argv[3]
    number_of_repo = 100  # sys.argv[4]
    url = construct_url(language, minimum_star);
    download_repo(url, number_of_repo)
