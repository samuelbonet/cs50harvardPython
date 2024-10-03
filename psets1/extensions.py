def main():
    file = input("File Name: ").strip().lower()
    
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    for extension, media_type in media_types.items():
        if file.endswith(extension):
            print(media_type)
            return
    
    print("application/octet-stream")

if __name__ == "__main__":
    main()

