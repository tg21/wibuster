try:
    import requests
except ModuleNotFoundError as e:
    print("requests in not install run $pip3 install requests and try again.Thanks!")


def sophBuster(h, p):#buster for sophisticated servers that accept head requests
    try:
        # print("requesting",h+"/"+p)
        r = requests.head(h+"/"+p)
        return r.status_code    
    except requests.ConnectionError as e:
        return e

def unSophBuster(h,p):
    try:
        r = requests.get(h+"/"+p)
        # print("requesting",h+"/"+p)
        return r.status_code
    except requests.ConnectionError as e:
        return e

def wildSophBuster(h, p):#buster for sophisticated servers that accept head requests
    try:
        # print("requesting",h+"/"+p)
        r = requests.head(h+"/"+p)
        return r.status_code,len(r.text)    
    except requests.ConnectionError as e:
        return e

def wildUnSophBuster(h,p):
    try:
        r = requests.get(h+"/"+p)
        # print("requesting",h+"/"+p)
        return r.status_code,len(r.text)
    except requests.ConnectionError as e:
        return e



def main():
    print("Wbuster v0.1 \n")
    print("this will test for express paths .html,folder,.php,.py,.jsp,.asp files primarily")
    dictfile = "directory-list-1.0.txt"
    buster = "soph"
    wild = False
    host = "http://localhost"
    # path = "/"
    paths = []
    sucPaths = []
    wildLenght = 0
    with open(dictfile) as file:
        # line=file.readline()
        for line in file:
            if(line.startswith("#")):
                continue
            else:
                paths.append(line.rstrip("\n"))

    # rand = input("enter a completely random unexpected word consisting of more than 8 letters eg- otqtjgpaf ::=> ")
    rand = "wrwqfsifasf"


    #inital tests
    status = sophBuster(host,"")
    if(status==501):
        buster = "unsoph"

    if(buster == "soph"):
        status,tLength = wildSophBuster(host,rand)
        if(status==200):#200ish
            wild = True
            wildLenght = tLength
            print("wild card support detected using advenced method")
    else:
        status,tLength = wildUnSophBuster(host,rand)
        if(status==200):#200ish
            wild = True
            wildLenght = tLength
            print("wild card support detected using advenced method")

    if(buster == "soph" and wild == False):
        for i in range(len(paths)):
            status = sophBuster(host,paths[i])
            if(status==200):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")

    if(buster == "unsoph" and wild == False):
        for i in range(len(paths)):
            status = unSophBuster(host,paths[i])
            if(status==200):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")

    if(buster == "soph" and wild == True):
        for i in range(len(paths)):
            status,tLength = wildSophBuster(host,paths[i])
            if(status==200 and tLength != wildLenght):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")

    if(buster == "unsoph" and wild == True):
        for i in range(len(paths)):
            status,tLength = wildUnSophBuster(host,paths[i])
            if(status==200 and tLength != wildLenght):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")

try:
    main()
except:
    print("error occured")           