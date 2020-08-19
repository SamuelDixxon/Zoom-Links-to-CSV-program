# -*- coding: utf-8 -*-
"""
Writing Zoomlinks to chat
"""


def writeZoomLinks(course, classification, day, time_frame, link):
    with open("C:/Users/15123/Desktop/ZoomZoom.csv", "a") as myFile:
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
        

