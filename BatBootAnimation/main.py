import os


if __name__ == "__main__":
    print("vvvvvv")
    begin = 452
    fp = r"C:\Users\Administrator\Desktop\BatBootAnimation\part4"
    li = os.listdir(fp) 
    for p in li: 
        pathname = os.path.join(fp, p)
        index = str(begin).zfill(4) #p[18:23]
        begin = begin + 1
        newpathname = os.path.join(fp, index + ".png")
        print("move " + pathname + " to " + newpathname)
        os.rename(pathname, newpathname)
    