import requests


def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Download successful. File saved as {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def start():
    # Example usage:
    url = input("Enter the URL: ")
    name = input("Enter the name of the file: ")
    extenstion = ""

extenstion = ".exe"

destination_path = name + extenstion
download_file(url, destination_path)



if __name__ == "__main__":
    start()
