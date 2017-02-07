# compiler from .tlg to .html

import sys


thetext = 'Saya ingin buat halaman web. Judul halaman adalah "Website contoh". Halaman web tersebut berisikan "div". Div tersebut berisikan "Hello world di dalam div". Selanjutnya, halaman berisikan "Tulisan di luar div". Di level yang sama, terdapat sebuah "div". Di dalamnya terdapat "gambar" dengan src=http://cdn.pcwallart.com/images/ball-python-cute-wallpaper-2.jpg, height=100px. '

filename = 'hasil.html'

args = sys.argv

if len(args) > 1:
    filename = args[1]
    f = open(filename,'r')
    thetext = f.read()
    filename = filename.split('.')[0] + '.html'
    f.close

lineArr = thetext.replace("\n"," ").split(". ")

result = ["<!doctype html>"]
pointer = 1

# reserved words
reserved = ["div","span","header","footer","section","article","aside","main"]

# process all command
for line in lineArr:
    
    # clean the syntax
    syntax = line.strip().lower()
    
    # detect if first line
    if( syntax.find("saya ingin buat halaman web") >= 0):
        result.insert(1, "<html>")
        result.insert(2, "<head>")
        result.insert(3, "</head>")
        result.insert(4, "<body>")
        result.insert(5, "</body>")
        result.insert(6,"</html>")
        pointer = 5
        
    # detect title
    if( syntax.find("judul halaman adalah") >=0):
        content = syntax.split('"')[1]
        result.insert(3,"<title>" + content + "</title>")
        pointer += 1
        
    # detect if contains "selanjutnya"
    if(syntax.find("selanjutnya,") >= 0 or syntax.find("kemudian,") >= 0):
        if result[pointer][1] == "/":
            pointer += 1
        
    # detect if says berisikan
    if(syntax.find("berisikan") >= 0 or syntax.find("terdapat") >= 0):
        command = syntax.split('"')[1]
        
        try:
            index = reserved.index(command)
            result.insert(pointer, "<" + command + ">")
            result.insert(pointer+1, "</" + command + ">")
            pointer += 1
        
        except ValueError:
            #img tag
            if command == "gambar":
                result.insert(pointer,"<img>")
                
            else:
                result.insert(pointer, command)
                
            pointer += 1
            
    # detect if says dengan (atribut)
    if(syntax.find("dengan") >= 0 ):
        pointer -= 1
        pos = syntax.find("dengan")
        attributes = syntax[pos+6:].split(",")
        
        for attribute in attributes:
            firstSD = attribute.find("=")
            attrName = attribute[:firstSD]
            attrVal = attribute[firstSD+1:]
            
            element = result[pointer]
            closingTag = element.find(">")
            element = element[:closingTag]
            element += " " + attrName + "=" + "\"" + attrVal + "\" >"
            
            result[pointer] = element
            
        pointer += 1
    
    
#print(result)

# write to file
f = open(filename,'w')
for line in result:
    f.write(line)
    print(line)
    
f.close()
