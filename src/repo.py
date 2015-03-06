# Functions for downloading and extracting github .pretty repositories

import requests
import zipfile
import os
import shutil
import json


def mk_path_for_file(path):
    """Make path for file, for example mk_path_for_file(directory1/directory2/file1.txt) will make 
    directory \"directory1/directory2/\""""
    for i in range(len(path) - 1, 0, -1):
        if path[i] == "/": break
    if not os.path.exists(path[:i]):
        os.mkdir(path[:i])


def check_update(addr, repos_cached):
    """Check repositories for updating, addr is a string with github api adress, repos_cached is dict
    {"repository_name": "date_of_latest_push"}, for example
    check_update("https://api.github.com/users/KiCad/repos", {"Choke_SMD.pretty": "2014-11-21T21:13:48Z"})
    will return all .pretty repositories that aren't in repos_cached dict or have different date of latest
    push"""
    pages = [requests.get(addr)]
    repos2update = {}

    for i in range(2, int(pages[0].headers["Link"].split()[2][-3:-2]) + 1):
        pages.append(requests.get(pages[0].headers["Link"].split()[0][1:-3] + str(i)))

    for page in pages:
        for repo in page.json():
            # if size is not zero and repository and ".pretty" in name and doesn't exist in repos_cached
            # and/or "pushed_at" differs
            if ((repo["size"] != 0) and (".pretty" in repo["name"])) and \
               ((not (repo["full_name"] in repos_cached)) or \
                (repo["pushed_at"] != repos_cached[repo["full_name"]])):
                repos2update[repo["full_name"]] = repo["pushed_at"]

    return repos2update, pages[0].status_code


def cache_read(path_to_cache):
    """Reads .json file"""
    repos_cached_file= open(path_to_cache, "r")
    repos_cached = json.loads(repos_cached_file.read())
    repos_cached_file.close()
    return repos_cached


def cache_write(path_to_cache, repos_cached):
    """Writes .json file"""
    mk_path_for_file(path_to_cache)
    repos_cached_file = open(path_to_cache, "w")
    repos_cached_file.write(json.dumps(repos_cached, indent=4))
    repos_cached_file.close()


def download(addr, dest):
    """Downloads file from addr to dest"""

    mk_path_for_file(dest)
    remotef = requests.get(addr)        
    f = open(dest, "wb")
    f.write(remotef.content)
    f.close()

    return remotef.status_code


def extract(source, dest):
    """Extracts source to dest, designed for .pretty repositories"""
    zip = zipfile.ZipFile(source)
    
    try:
        shutil.rmtree(dest + zip.namelist()[0][:-8])
    except FileNotFoundError:
        pass
    
    zip.extractall(path=dest)
    
    os.rename(dest + zip.namelist()[0][:-1], dest + zip.namelist()[0][:-8])
    os.remove(source)


def mk_table(foot_dir, fp_lib_table):
    """Makes fp_lib_table for all .pretty directories in foot_dir"""
    mk_path_for_file(fp_lib_table)
    table = open(fp_lib_table, "w")
    
    table.write("(fp_lib_table\n")
    
    for item in os.listdir(foot_dir):
        if ".pretty" in item:
            table.write("(lib (name {})(type KiCad)".format(item[:-7]))
            table.write("(uri {})".format(foot_dir + item))
            table.write("(options \"\")(descr \"The way you like them.\"))\n")
    
    table.write(")\n")
    table.close()