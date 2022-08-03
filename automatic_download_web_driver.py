import subprocess
import os
import zipfile
import wget
import requests
import tarfile
from sys import platform
import urllib.request


DOWNLOAD_PATH = "< directory location where you want to download the web driver >"


if platform == "linux" or platform == "linux2":

    try:
        google_chrome_version = subprocess.check_output(['google-chrome', '--version']).decode().replace("Google Chrome ","").replace("\n","").replace(" ","")
        google_chrome_driver_url = "https://chromedriver.storage.googleapis.com/"+google_chrome_version+"/chromedriver_linux64.zip"
        latest_driver_zip = wget.download(google_chrome_driver_url, DOWNLOAD_PATH+'chromedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_PATH)
        os.remove(latest_driver_zip)
    except Exception as e:
        print(e)
        pass


    try:
        firefox_version = subprocess.check_output(['firefox', '--version']).decode().replace("Mozilla Firefox ","").replace("\n","").replace(" ","")
        r = requests.get(url = "https://api.github.com/repos/mozilla/geckodriver/releases/latest")
        data = r.json()
        # geckodriver_linux_32_url = data['assets'][0]['browser_download_url']
        geckodriver_linux_64_url = data['assets'][2]['browser_download_url']
        latest_driver_zip = wget.download(geckodriver_linux_64_url, DOWNLOAD_PATH+'geckodriver.tar.gz')
        file = tarfile.open(latest_driver_zip)
        file.extractall(DOWNLOAD_PATH)
        file.close()
        os.remove(DOWNLOAD_PATH+'geckodriver.tar.gz')
    except:
        pass


    try:
        microsoft_edge_version = subprocess.check_output(['microsoft-edge', '--version']).decode().replace("Microsoft Edge ","").replace("\n","").replace(" ","")
        microsoft_edge_driver_url = "https://msedgedriver.azureedge.net/"+microsoft_edge_version+"/edgedriver_linux64.zip"
        latest_driver_zip = wget.download(microsoft_edge_driver_url, DOWNLOAD_PATH+'edgedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_PATH)
        os.remove(latest_driver_zip)
    except:
        pass


elif platform == "darwin":
    pass

elif platform == "win32":

    try:
        google_chrome_commands = r'''wmic datafile where 'name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"' get version'''
        google_chrome_process = subprocess.run(google_chrome_commands, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        google_chrome_output = google_chrome_process.stdout.replace("Version","").replace("\n","").replace(" ","")
        google_chrome_version = google_chrome_output
        google_chrome_version = urllib.request.urlopen("https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"+google_chrome_version.split(".")[0]).read().decode()
        google_chrome_driver_url = "https://chromedriver.storage.googleapis.com/"+google_chrome_version+"/chromedriver_win32.zip"
        latest_driver_zip = wget.download(google_chrome_driver_url, DOWNLOAD_PATH+'chromedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_PATH)
        os.remove(latest_driver_zip)
    except:
        pass

    
    try:
        firefox_commands = r'''wmic datafile where 'name="C:\\Program Files\\Mozilla Firefox\\firefox.exe"' get version'''
        firefox_process = subprocess.run(firefox_commands, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        firefox_output = firefox_process.stdout.replace("Version","").replace("\n","").replace(" ","")
        firefox_version = firefox_output
        r = requests.get(url = "https://api.github.com/repos/mozilla/geckodriver/releases/latest")
        data = r.json()
        geckodriver_win_64_url = data['assets'][7]['browser_download_url']
        latest_driver_zip = wget.download(geckodriver_win_64_url, DOWNLOAD_PATH+'geckodriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_PATH)
        os.remove(latest_driver_zip)
    except:
        pass

    
    try:
        microsoft_edge_commands = r'''wmic datafile where 'name="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"' get version'''
        microsoft_edge_process = subprocess.run(microsoft_edge_commands, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        microsoft_edge_output = microsoft_edge_process.stdout.replace("Version","").replace("\n","").replace(" ","")
        microsoft_edge_version = microsoft_edge_output
        microsoft_edge_driver_url = "https://msedgedriver.azureedge.net/"+microsoft_edge_version+"/edgedriver_win64.zip"
        latest_driver_zip = wget.download(microsoft_edge_driver_url, DOWNLOAD_PATH+'edgedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_PATH)
        os.remove(latest_driver_zip)
    except:
        pass
