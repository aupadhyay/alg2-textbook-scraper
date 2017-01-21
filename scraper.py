import urllib
import os
import urllib.request


chapter = 1
lesson = 1
pageNumber = 1

for num in range(0,500):
    if(lesson < 10):
        lessonString = "0" + str(lesson);
    else:
        lessonString = str(lesson);

    if(chapter < 10):
        chapterString = "0" + str(chapter);
    else:
        chapterString = str(chapter);

    if(pageNumber/10 > 1):
        pageNumberString = "0" + str(pageNumber)
    elif(pageNumber/100 > 1):
        pageNumberString = str(pageNumber)
    else:
        pageNumberString = "00" + str(pageNumber)
    


    finalURL = "http://bim.easyaccessmaterials.com/protected/content/dcs_cc3/alg2/c" + chapterString + "/" + lessonString + "/alg2_" + chapterString + "_" + lessonString + "_p" + pageNumberString + ".png"
    print(finalURL)
    #https://bim.easyaccessmaterials.com/protected/content/dcs_cc3/alg2/c02/01/alg2_02_01_p001.png

    finalFileName = "mathbook/" + str(chapter) + "_" + str(lesson) + "_" + str(pageNumber) + ".png"
    try:
        urllib.request.urlretrieve(finalURL, finalFileName)
        pageNumber+=1
    except:
        print("it don't exist")
        if(lesson > 9):
            chapter+=1
            lesson = 1
            pageNumber = 1
        else:
            lesson+=1
            pageNumber = 1
