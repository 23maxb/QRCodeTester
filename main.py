def makeQRCode(s):
    import segno
    segno.make(s).save("basic_qrcode.png")


def fileToQRCode():
    import segno
    os.listdir(path='.')
    with open("geeks.txt") as file:
        data = file.read()
    segno.make(data).save("basic_qrcode.png")


if __name__ == '__main__':
    with open("ToQRCode/google.txt") as file:
        data = file.read()
    print(data)
    import re

    pattern = re.compile(
        "/(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?/g")
    inp = input("Enter your value: ")
    if input == "files":
        fileToQRCode()
    else:
        while not pattern.match(inp):
            print("Invalid URL")
            inp = input("Enter your value: ")
        makeQRCode(input)
