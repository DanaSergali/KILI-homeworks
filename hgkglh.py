import re

def readfile():
    with open("/Users/Max/Desktop/mystem.xml", "r", encoding="utf-8") as f:
        text = f.read()
        text = text.split("\n")
        return text

def writefile(tekst):
    with open("/Users/Max/Desktop/mystemout.txt", "a", encoding="utf-8") as f:
        f.write(tekst)
    if not f.writable:
        print("Unable to get access to the end file.")

def fun1(a):
    flag = 1
    c = 0
    for line in a:
        if re.search("</se>", line):
            flag *= -1
        if flag == -1:
            c += 1
        if re.search("<se>", line):
            flag *= -1
    return c

def fun2(b):
    dict = {}
    for line in b:
        if re.search("gr",line):
            c = 0
            for lineinline in b:
                if lineinline == line:
                    c += 1
            line = line.split()
            dict[line[2]] = c
    return dict

def fun3(c):
    stroka = ""
    for line in c:
        if re.search("A",line) and re.search("жен",line):
            tmp = re.findall("[а-я]+",line)
            stroka += tmp[len(tmp)-1]+(", ")
    return stroka

writefile(str(fun1(readfile())))
writefile(str(fun2(readfile())))
writefile(str(fun3(readfile())))