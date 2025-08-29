# Get the user's file name
name = input("File name:").strip(".").lower().strip()

# Output message based on the file name
if name.endswith("gif"):
    print("image/gif")
elif name.endswith("jpeg") or name.endswith("jpg"):
    print("image/jpeg")
elif name.endswith("png"):
    print("image/png")
elif name.endswith("pdf"):
    print("application/pdf")
elif name.endswith("txt"):
    print("text/plain")
elif name.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
