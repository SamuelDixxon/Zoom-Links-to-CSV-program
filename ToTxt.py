# -*- coding: utf-8 -*-
"""
Writing Zoomlinks to chat
"""


def writeZoomLinks(course, classification, day, time_frame, link):
    with open("C:/Users/#####/Desktop/ZoomZoom.csv", "w") as myFile:   #specify User address for writing file to the desktop, first use write to create the file, then change to append in order to avoid over writing the file everytime
        #myFile.write("Course, Meeting Type, Day, Time, Link\n") ### initial header 
        myFile.write("%s,%s,%s,%s,%s" % (course, classification, day, time_frame, link))
        
def getdata():
    course = input("Course: ")
    classification = input("Classification: ")
    day = input("Day: ")
    time = input("Time: ")
    link = input("Link: ")
    
    return course, classification, day, time, link
       
a = getdata()


writeZoomLinks(a[0], a[1], a[2], a[3], a[4])
        

