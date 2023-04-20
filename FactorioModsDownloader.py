#CREATED BY CKANZ#
import requests
from bs4 import BeautifulSoup
import wget
import os

download_hosts = "https://official-factorio-mirror.re146.dev"
mods_portal = "https://mods.factorio.com"
download_host = ""

path = r""

menu_options = {
    1: 'Only One Mod',
    2: 'Only Dependecies',
    3: 'Mods with dependecies',
    4: 'Change Path',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    if path == "":
        real_path = os.path.dirname(os.path.realpath(__file__))
        createFolder(real_path + '/mods')
    download_file_one_mod()

def option2():
    if path == "":
        real_path = os.path.dirname(os.path.realpath(__file__))
        createFolder(real_path + '/mods')

    download_file_dependencies_only()

    count = 0
    for track in tracks:
        download_file(track["href"])
        count += 1
    print(len(tracks))

def option3():
    if path == "":
        real_path = os.path.dirname(os.path.realpath(__file__))
        createFolder(real_path + '/mods')

    download_file_one_mod()
    download_file_dependencies_only()

    count = 0
    for track in tracks:
        download_file(track["href"])
        count += 1
    print(len(tracks))

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
    
    path =  os.chdir(directory)

def find_version(mods_name):
    mods_portal_url = mods_portal + mods_name + "/downloads"
    html_text_version = requests.get(mods_portal_url).text
    soup_version = BeautifulSoup(html_text_version, 'html.parser')

    file_version = soup_version.find("dl", {"class" : "panel-hole ddw80p"}).findAll("dd", recursive=False)
    return file_version[0].text.strip()

def download_file_one_mod():
    file_name_replace = download_host.replace("https://mods.factorio.com/mod/", "")
    file_name = file_name_replace.replace("/downloads", "").strip()
    mods_portal_url = "/mod/" + file_name
    download_url = download_hosts + "/" + file_name + "/" + find_version(mods_portal_url) + ".zip"
    wget.download(download_url, out = path)
    print('Downloaded: {}'.format(file_name, download_url))


def download_file_dependencies_only(mods_name):
    file_name = mods_name.strip().replace("/mod/", "")
    download_url = download_hosts + "/" + file_name + "/" + find_version(mods_name) + ".zip"
    wget.download(download_url, out = path)
    print('Downloaded: {}'.format(file_name, download_url))

if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Choose Option: '))
        except:
            print('Option Wrong!')
        if option == 1:
            download_host = input("Copy link(https://mods.factorio.com/mod/mods-name/downloads): ")
            option1()
        elif option == 2:
            download_host = input("Copy link(https://mods.factorio.com/mod/mods-name/downloads): ")
            option2()
        elif option == 3:
            download_host = input("Copy link(https://mods.factorio.com/mod/mods-name/downloads): ")
            option3()
        elif option == 4:
            path = input("Choose Path(C:\Path1): ")
        elif option == 5:
            print('Exit..')
            exit()
        else:
            print('Input Between 1-5')
#CREATED BY CKANZ#