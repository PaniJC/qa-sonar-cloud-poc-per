import requests

def searchFiles(token: str):
    try:    
        response = requests.get(
            f"https://www.googleapis.com/drive/v3/files",
            headers={"Authorization": f"Bearer {token}"}
        )
    
        json = response.json()
        
        files = json["files"]

        newfiles = []

        for file in files:
            if file["mimeType"] == "application/vnd.google-apps.spreadsheet":
                newfiles.append(file)

        return newfiles
    except ValueError:
        print("Invalid token.")