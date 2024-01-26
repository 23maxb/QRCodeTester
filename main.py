def makeQRCode(s, fileName="basic_qrcode.png"):
    import segno
    if not fileName.endswith(".png"):
        fileName = fileName[0:len(fileName) - 4]
    segno.make(s).save(fileName)


def fileToQRCode(pathToFiles):
    import segno
    import os
    os.listdir(path=pathToFiles)
    for k in os.listdir(path=pathToFiles):
        with open(pathToFiles + "/" + k) as content:
            makeQRCode(content.read(), k[0:len(k) - 4] + ".png")


if __name__ == '__main__':
    import re

    print("Welcome to QRCode Generator")
    print("Enter 'files' to convert all files in 'ToQrCode' folder to QRCode")
    print("Otherwise just type a url to convert it to QRCode")
    pattern = re.compile(
        r"/(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?/g")
    inp = input("Enter your value: ")
    while not (pattern.match(inp) or inp == "files"):
        print("Invalid URL")
        inp = input("Enter your value: ")
    if inp == "files":
        fileToQRCode("ToQrCode")
    else:
        makeQRCode(inp)
