# Google drive backup

# Upload files to google drive
# List files in google drive
# Download files from google drive

# pip install pydrive

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '12ab7_xYLeTnMzAIf8SBSuM1b75J_nO-O'

# Upload files
# directory = "C:\Users\BAVISKAR\Desktop\College"
# for f in os.listdir(directory):
# 	filename = os.path.join(directory, f)
# 	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
# 	gfile.SetContentFile(filename)
# 	gfile.Upload()

# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])