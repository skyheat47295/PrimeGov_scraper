from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

local_path = './data'  # Path to local files to be uploaded.
g_path = 'PrimeGov/data'  # Path to remote G-Drive directory to upload files

# Initiation
gauth = GoogleAuth()
gauth.LoadCredentialsFile('mycreds.txt')
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#folder = drive.CreateFile({'title': 'PrimeGov', "mimeType": "application/vnd.google-apps.folder"})
#folder.Upload()
#gauth.SaveCredentialsFile("mycreds.txt")
print('what comes next')