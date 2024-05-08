import requests
import os
header = ""
extension = ""

#List of the magic numbers for reference
magic_numbers = {'.png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
                 '.jpg': bytes([0xFF, 0xD8, 0xFF, 0xE0]),
                 '.gif': bytes([0x47, 0x49, 0x46, 0x38, 0x37, 0x61]),
                 
                 '.mp3': bytes([0xFF, 0xFB]),
                 '.mp4': bytes([0x66, 0x74, 0x79, 0x70, 0x69, 0x73, 0x6F, 0x6D]),

                 '.zip': bytes([0x50, 0x4B, 0x03, 0x04]),
                 '.rar': bytes([0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 00]),
                 
                 '.doc': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
                 '.xls': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
                 '.ppt': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
                 '.docx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
                 '.xlsx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
                 '.pptx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
                 '.pdf': bytes([0x25, 0x50, 0x44, 0x46, 0x2D]),

                 'exe': bytes([0x4D, 0x5A]),}


def download_file(url, name):
    global extension
    response = requests.get(url)
    
    if response.status_code == 200:

        #Downloading the file from the link by writing the bytes to a new file
        with open(name, 'wb') as file:
            
            file.write(response.content)

            #We check every magic number to find a match            
            for n in magic_numbers:
                
                file = open(name, 'rb')
                header = file.read(len(magic_numbers[n]))

                #When a match is found we test weather or not the user is satisfied 
                if header.startswith(magic_numbers[n]):
                    print("The following extension will be used: ", n)
                    #The user can choice to enter the extension manually or to accept
                    c = input("Type c to continue or anything else to enter the extension manually: ")
                    if(c != "c"):
                        extension = input("Enter the extension: ")
                    else:
                        extension = n
                file.close()
                
        #Allowing the user to enter it manually if the program failed
        if extension == "":
            
            print("Extension couldn't be found please enter it manually")
            extension = input("Enter the extension: ")

            #Adding the period in case the user forgot
            if("." not in extension):
                extension = "." + extension

        #Renaming the file with the extension
        os.rename(name, name + extension)
        
        name = name + extension
        print(f"Download successful. File saved as {name}")
        
    #If the webpage didn't respond we get the response code
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def start():
    url = input("Enter the URL: ")
    name = input("Enter the name of the file: ")
    download_file(url, name)







if __name__ == "__main__":
    start()
