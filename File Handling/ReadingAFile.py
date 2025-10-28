with open("/workspaces/gcse-24-27-laya04/File Handling/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)

with open("/workspaces/gcse-24-27-laya04/File Handling/practiceRead.txt", "a") as file:
    file.write("\nthis is a new line added later")