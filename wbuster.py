try:
    import requests
except ModuleNotFoundError as e:
    print("requests in not install run $pip3 install requests and try again.Thanks!")
import _thread
import threading
import random
import string
import math
sucPaths = []

exitFlag = 0

# variables used by buster
buster = "soph"
wild = False
host = "http://localhost"
wildLength = 0

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

def bust(paths):
    global sucPaths
    global buster
    global wild
    global wildLength
    global host
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
            if(status==200 and tLength != wildLength):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")

    if(buster == "unsoph" and wild == True):
        for i in range(len(paths)):
            status,tLength = wildUnSophBuster(host,paths[i])
            if(status==200 and tLength != wildLength):#200ish
                sucPaths.append(paths[i])
                print("/"+paths[i]+"\n")


class BusterThreads (threading.Thread):
   def __init__(self, threadID, name, paths):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.paths = paths
   def run(self):
      print ("Starting " + self.name)
      bust(self.paths)
      print ("Exiting " + self.name)

### divide lists for multithreading
def slice_list(input, size):
    input_size = len(input)
    slice_size = input_size // size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result


def divide_list(input,size):
    list_of_lists = []
    item_per_list = len(input) // size
    temp_list = []
    for i in range(len(input)):
        if(len(temp_list)<=item_per_list):
            temp_list.append(input[i])
        else:
            list_of_lists.append(temp_list)
            temp_list = []
    return list_of_lists
            
def main():
    print("Wbuster v0.1 \n")
    print("this will test for paths .html,folder,.php,.py,.jsp,.asp files primarily")
    dictfile = "directory-list-1.0.txt"

    threadCount = 10
    
    # path = "/"
    paths = []
    # paths = []
    global sucPaths
    global buster
    global wild
    global wildLength
    global host

    with open(dictfile) as file:
        # line=file.readline()
        for line in file:
            if(line.startswith("#")):
                continue
            else:
                paths.append(line.rstrip("\n"))


    rand = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
    # rand = "wrwqfsifasf"
    paths = divide_list(paths,threadCount)

    #inital tests
    status = sophBuster(host,"")
    if(status==501):
        buster = "unsoph"

    if(buster == "soph"):
        status,tLength = wildSophBuster(host,rand)
        if(status==200):#200ish
            wild = True
            wildLength = tLength
            print("wild card support detected using advenced method")
    else:
        status,tLength = wildUnSophBuster(host,rand)
        if(status==200):#200ish
            wild = True
            wildLength = tLength
            print("wild card support detected using advenced method")

    threadList = []
    for t in range(0,len(paths)):
        try:
            #print("starting thread ",t)
            #_thread.start_new_thread(bust,(buster,wild,wildLength,host,paths[t]))
            threadname = "T"+str(t)
            thread = BusterThreads(1, threadname, paths[t])
            threadList.append(thread)
        except:
            print("Unable to Create threads")

    for i in range(len(threadList)):
        threadList[i].start()
    for i in range(len(threadList)):
        threadList[i].join()
    print("exiting Main Function")

try:
    main()
except:
    print("error occured")           