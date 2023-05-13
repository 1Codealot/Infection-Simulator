import requests, os
from zipfile import ZipFile

versions = ["V1.4","V1.5","V1.6"]
version = ''

while version.upper() not in versions:
	version = input('What version do you want to install? "V1.4", "V1.5", "V1.6"')


link_template = f"https://github.com/1Codealot/Infection-Simulator/releases/download/{version}/Infection.{version}.zip"

#Gets Path
thePath = os.getcwd()

# Define the remote file to retrieve
remote_url = link_template

# Define the local filename to save data
local_file = 'Infection_Temp.zip'

# Make http request for remote file data
print("Downloading folder...")
data = requests.get(remote_url)
print("Folder downloaded")

# Save file data to local copy
with open(local_file, 'wb')as file:
	file.write(data.content)

print("Extracting")
## Extract
with ZipFile(thePath+"\\Infection_Temp.zip", 'r') as zObject:
	zObject.extractall(path=thePath+"\\Infection")

print("Clean up")
os.remove("Infection_Temp.zip")

print("Finished!")
