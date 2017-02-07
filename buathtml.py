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
    
# clear dot between quotes
quote = 0
for i, c in enumerate(thetext):
    if c == '"' and quote == 0:
        quote = 1
    elif c == '"' and quote == 1:
        quote = 0
    
    if c == "." and quote == 1:
        thetext = thetext[:i] + '`' + thetext[i+1:]

#print(thetext)

lineArr = thetext.replace("\n"," ").split(". ")

result = ["<!doctype html>"]
pointer = 1

# reserved words
reserved = ["div","span","header","footer","section","article","aside","main","form","iframe"]

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
        
    # detect dependency
    if( syntax.find("memakai") >= 0):
        dependencies = syntax.split('"')[1].split(",")
        
        # bootstrap
        for dependency in dependencies:
            if dependency == "bootstrap":
                result.insert(4,'<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>')

            pointer += 1
        
        
    # detect if contains "selanjutnya"
    if(syntax.find("selanjutnya,") >= 0 or syntax.find("kemudian,") >= 0 or syntax.find("setelah itu,") >= 0):
        
        if result[pointer] == "</li>":
            pointer += 1
        if result[pointer][1] == "/":
            pointer += 1
            
    # detect isi list
    if(syntax.find("(*)") >= 0 ):
        
        if result[pointer] != "</ol>" and result[pointer] != "</ul>":
            pointer += 1
            
        result.insert(pointer,"<li>")
        result.insert(pointer+1, "</li>")
            
        syntax = syntax[3:].strip()
        pointer += 1
        
    # detect if says berisikan
    if(syntax.find("berisikan") >= 0 or syntax.find("terdapat") >= 0):
        command = syntax.split('"')[1].replace("`",".")
        
        try:
            index = reserved.index(command)
            result.insert(pointer, "<" + command + ">")
            result.insert(pointer+1, "</" + command + ">")
            pointer += 1
        
        except ValueError:
            #img tag
            if command == "gambar":
                result.insert(pointer,"<img>")
            elif command == "pembungkus":
                result.insert(pointer,"<div class='container'>")
                result.insert(pointer+1, "</div>")
            elif command == "paragraf":
                result.insert(pointer,"<p>")
                result.insert(pointer+1, "</p>")
            elif command.find("heading") >= 0:
                angka = command.split("heading")[1]
                result.insert(pointer,"<h" + angka + ">")
                result.insert(pointer+1, "</h" + angka + ">")
            elif command == "tebal":
                result.insert(pointer,"<strong>")
                result.insert(pointer+1, "</strong>")
            elif command == "miring":
                result.insert(pointer,"<em>")
                result.insert(pointer+1, "</em>")
            elif command == "daftar":
                result.insert(pointer,"<ul>")
                result.insert(pointer+1, "</ul>")
            elif command == "daftar bernomor":
                result.insert(pointer,"<ol>")
                result.insert(pointer+1, "</ol>")
            elif command == "tombol":
                result.insert(pointer,"<button>")
                result.insert(pointer+1, "</button>")
            elif command == "grid":
                result.insert(pointer,"<div class='row'>")
                result.insert(pointer+1, "</div>")
            elif command.find("kolom grid") >= 0:
                fraction = command.split("kolom grid")[1]
                pembilang = int(fraction.split("/")[0])
                
                penyebut = 1
                if len(fraction.split("/")) > 1:
                    penyebut = int(fraction.split("/")[1])
                    
                width = int((pembilang/penyebut) * 12)
                print(width)
                
                result.insert(pointer,"<div class='col-md-" + str(width) + "'>")
                result.insert(pointer+1, "</div>")
                
            else:
                result.insert(pointer, command)
                
            pointer += 1
            
    # detect if says dengan (atribut)
    if(syntax.find("dengan atribut") >= 0 ):
        pointer -= 1
        pos = syntax.find("dengan atribut")
        attributes = syntax[pos+14:].split(",")
        
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
