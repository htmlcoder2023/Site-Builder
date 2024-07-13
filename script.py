import os.path
i = []
currentNum = len(i) + 1
num_str = 1
num = int(num_str)
mode = "The links will be used to give information about " + input("The links will be used to give information about ")
mode_num = 0

if mode == "The links will be used to give information about the games.":
    mode_num = 0
elif mode == "The links will be used to give information about where to buy the games.":
    mode_num = 1
else:
    raise Exception("The only answers can be [the games.] or [where to buy the games.]!")

while currentNum < num + 1:
    i.append(input("Company " + str(currentNum) + ": "))
    currentNum = len(i) + 1

s = []

for companies in range(len(i)): 
    if os.path.isfile(i[companies] + ".html"):
        print(i[companies] + ".html" + " already exists!")
        open(i[companies] + ".html", "w")
        s.append(open(i[companies] + ".html", "a+"))
    else:
        open(i[companies] + ".html", "w")
        s.append(open(i[companies] + ".html", "a+"))

for companies in range(len(s)):
    s[companies].write("<!DOCTYPE HTML>")
    s[companies].write("\n" + "<html lang='en'>")
    s[companies].write("\n" + "    <head>")
    s[companies].write("\n" + "        <title>" + input("<title>") + "</title>")
    s[companies].write("\n" + "        <link rel='icon' type='image/x-icon' href='" + input("<link rel='icon' type='image/x-icon' href='") + "'>")
    s[companies].write("\n" + "        <meta charset='UTF-8'>")
    s[companies].write("\n" + "        <meta name='description' content='" + input("<meta name='description' content='") + "'>")
    s[companies].write("\n" + "        <meta name='keywords' content='" + input("<meta name='keywords' content='") + "'>")
    s[companies].write("\n" + "        <meta name='author' content='htmlcoder2023'>")
    s[companies].write("\n" + "        <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    s[companies].write("\n" + "        <style>")
    s[companies].write("\n" + "            * {")
    s[companies].write("\n" + "                margin: 0px;")
    s[companies].write("\n" + "            }")
    s[companies].write("\n" + "            .games {")
    s[companies].write("\n" + "                display: flex;")
    s[companies].write("\n" + "                height: 50%;")
    s[companies].write("\n" + "                width: 100%;")
    s[companies].write("\n" + "            }")
    s[companies].write("\n" + "            .game {")
    s[companies].write("\n" + "                flex: 25%;")
    s[companies].write("\n" + "            }")
    s[companies].write("\n" + "            img {")
    s[companies].write("\n" + "                width: 100%;")
    s[companies].write("\n" + "                height: 100%;")
    s[companies].write("\n" + "            }")
    s[companies].write("\n" + "        </style>")
    s[companies].write("\n" + "    </head>")
    s[companies].write("\n" + "    <body>")

r = []

for companies in range(len(i)):
    currentInput = input(i[companies] + " Games: ")
    if int(currentInput) == 0:
        r.append(int(currentInput))
    elif int(currentInput) % 4 == 0 and 4 <= int(currentInput):
        r.append(int(currentInput) / 4)
    else:
        print("Your number is not divisible by 4. Please only enter numbers that are divisible by 4, and leave blank games if needed.")

numOfGames = 0
savedGames = 0
savGame = 0

sav = []
imgsav = []
altsav = []

gameFiles = []

databaseFiles = []
imgFiles = []
altFiles = []

databaseFiles_w = []
imgFiles_w = []
altFiles_w = []

try:
    for companies in range(len(i)):
        databaseFiles_w.append(open(i[companies] + ".dat", "a+"))
        imgFiles_w.append(open(i[companies] + "img.dat", "a+"))
        altFiles_w.append(open(i[companies] + "alt.dat", "a+"))
        if os.path.isfile(i[companies] + ".dat"):
            databaseFiles.append(open(i[companies] + ".dat", "r"))
            imgFiles.append(open(i[companies] + "img.dat", "r"))
            altFiles.append(open(i[companies] + "alt.dat", "r"))
            for companies in range(len(databaseFiles)):
                datFileRead = databaseFiles[companies].readlines()
                imgFileRead = imgFiles[companies].readlines()
                altFileRead = altFiles[companies].readlines()

                for images in imgFileRead:
                    if images.isspace() == False:
                        imgsav.append(images.replace("\n", ""))
        
                for descriptions in altFileRead:
                    if descriptions.isspace() == False:
                        altsav.append(descriptions.replace("\n", ""))

                for companies in range(len(s)):
                    for games in datFileRead:
                        if games.isspace() == False:
                            sav.append(games.replace("\n", ""))
                            savedGames -= 1
                    for saves in range(len(sav)):  
                        while savGame < len(sav):  
                            s[companies].write("\n" + "        <div class='games'>")
                            s[companies].write("\n" + "            <div class='game'>")
                            s[companies].write("\n" + "                <a href='" + str(sav[saves]) + "'><img src='" + str(imgsav[saves]) + "' alt='" + str(altsav[saves]) + "'></a>")
                            s[companies].write("\n" + "            </div>")
                            s[companies].write("\n" + "            <div class='game'>")
                            s[companies].write("\n" + "                <a href='" + str(sav[saves + 1]) + "'><img src='" + str(imgsav[saves + 1]) + "' alt='" + str(altsav[saves + 1]) + "'></a>")
                            s[companies].write("\n" + "            </div>")
                            s[companies].write("\n" + "            <div class='game'>")
                            s[companies].write("\n" + "                <a href='" + str(sav[saves + 2]) + "'><img src='" + str(imgsav[saves + 2]) + "' alt='" + str(altsav[saves + 2]) + "'></a>")
                            s[companies].write("\n" + "            </div>")
                            s[companies].write("\n" + "            <div class='game'>")
                            s[companies].write("\n" + "                <a href='" + str(sav[saves + 3]) + "'><img src='" + str(imgsav[saves + 3]) + "' alt='" + str(altsav[saves + 3]) + "'></a>")
                            s[companies].write("\n" + "            </div>")
                            s[companies].write("\n" + "        </div>")
                            savGame += 4

        else:
            databaseFiles_w.append(open(i[companies] + ".dat", "a+"))
            imgFiles_w.append(open(i[companies] + "img.dat", "a+"))
            altFiles_w.append(open(i[companies] + "alt.dat", "a+"))
except:
    print("Scanning files complete.")

try: 
    for companies in range(len(s)):
        for companies in range(len(r)):
            while len(sav) + savedGames < r[companies] * 4:
                if mode_num == 0:
                    sav.append(input("Game " + str(len(sav) + 1 + savedGames) + ": ") + ".html")
                elif mode_num == 1:
                    sav.append(input("Link " + str(len(sav) + 1 + savedGames) + ": "))
                imgsav.append(input("Image " + str(len(sav) + savedGames) + ": "))
                altsav.append(sav[len(sav) - 1] + " Box Art")
            for saves in range(len(sav)):
                while numOfGames < r[companies]:
                    s[companies].write("\n" + "        <div class='games'>")
                    s[companies].write("\n" + "            <div class='game'>")
                    s[companies].write("\n" + "                <a href='" + str(sav[saves - savedGames]) + "'><img src='" + str(imgsav[saves - savedGames]) + "' alt='" + str(altsav[saves - savedGames]) + "'></a>")
                    s[companies].write("\n" + "            </div>")
                    s[companies].write("\n" + "            <div class='game'>")
                    s[companies].write("\n" + "                <a href='" + str(sav[saves + 1 - savedGames]) + "'><img src='" + str(imgsav[saves + 1 - savedGames]) + "' alt='" + str(altsav[saves + 1 - savedGames]) + "'></a>")
                    s[companies].write("\n" + "            </div>")
                    s[companies].write("\n" + "            <div class='game'>")
                    s[companies].write("\n" + "                <a href='" + str(sav[saves + 2 - savedGames]) + "'><img src='" + str(imgsav[saves + 2 - savedGames]) + "' alt='" + str(altsav[saves + 2 - savedGames]) + "'></a>")
                    s[companies].write("\n" + "            </div>")
                    s[companies].write("\n" + "            <div class='game'>")
                    s[companies].write("\n" + "                <a href='" + str(sav[saves + 3 - savedGames]) + "'><img src='" + str(imgsav[saves + 3 - savedGames]) + "' alt='" + str(altsav[saves + 3 - savedGames]) + "'></a>")
                    s[companies].write("\n" + "            </div>")
                    s[companies].write("\n" + "        </div>")
                    if mode_num == 0:
                        if os.path.isfile(str(sav[saves - savedGames])):
                            print(sav[saves - savedGames] + " already exists!")
                            open(sav[saves - savedGames], "w")
                            gameFiles.append(open(sav[saves - savedGames], "a+"))
                        elif os.path.isfile(str(sav[saves + 1 - savedGames])):
                            print(sav[saves + 1 - savedGames] + " already exists!")
                            open(sav[saves + 1 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 1 - savedGames], "a+"))
                        elif os.path.isfile(str(sav[saves + 2 - savedGames])):
                            print(sav[saves + 2 - savedGames] + " already exists!")
                            open(sav[saves + 2 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 2 - savedGames], "a+"))
                        elif os.path.isfile(str(sav[saves + 3 - savedGames])):
                            print(sav[saves + 3 - savedGames] + " already exists!")
                            open(sav[saves + 3 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 3 - savedGames], "a+"))
                        else:
                            open(sav[saves - savedGames], "w")
                            gameFiles.append(open(sav[saves - savedGames], "a+"))
                            open(sav[saves + 1 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 1 - savedGames], "a+"))
                            open(sav[saves + 2 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 2 - savedGames], "a+"))
                            open(sav[saves + 3 - savedGames], "w")
                            gameFiles.append(open(sav[saves + 3 - savedGames], "a+"))
                    
                    if numOfGames + 1 >= r[companies]:
                        numOfGames = 0
                        saves = 0
                        companies += 1
                    else:
                        saves += 4
                        numOfGames += 1
                        
finally:
    print(sav)
    print(imgsav)
    print(altsav)
    try:
        for companies in range(len(s)):
            s[companies].write("\n" + "    </body>")
            s[companies].write("\n" + "</html>")
            s[companies].close()

        for files in range(len(databaseFiles_w)):
            for files in range(len(i)):
                open(i[files] + ".dat", "w")
                open(i[files] + "img.dat", "w")
                open(i[files] + "alt.dat", "w")

        for games in range(len(sav)):
            databaseFiles_w[files].write("\n" + str(sav[games]))

        for files in range(len(imgFiles_w)):
            for games in range(len(sav)):
                imgFiles_w[files].write("\n" + str(imgsav[games]))

        for files in range(len(altFiles_w)):
            for games in range(len(sav)):
                altFiles_w[files].write("\n" + str(altsav[games]))
    except:
        print("Program execution complete.")
        for files in range(len(databaseFiles_w)):
            databaseFiles_w[files].close()
        for files in range(len(imgFiles_w)):
            imgFiles_w[files].close()
        for files in range(len(altFiles_w)):
            altFiles_w[files].close()