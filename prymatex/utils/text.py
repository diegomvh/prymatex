# -*- coding: utf-8 -*-
#!/usr/bin/env python

import string

upperCase = string.upper
    
lowerCase = string.lower

def titleCase(text):
    return text.title()
    
def oppositeCase(text):
    newText = ""
    for char in text:
        uindex = string.uppercase.find(char)
        lindex = string.lowercase.find(char)
        if uindex != -1:
            newText += string.lowercase[uindex]
        elif lindex != -1:
            newText += string.uppercase[lindex]
        else:
            newText += char
    return newText
    
def spacesToTabs(text, spaceLength = 4):
    return text
    
def tabToSpaces(text, spaceLength = 4):
    return text
    
def transpose(text):
    return text[::-1]

convert_functions = [ upperCase, lowerCase, titleCase, oppositeCase, spacesToTabs, tabToSpaces, transpose ]

if __name__ == '__main__':
    print oppositeCase("holaMunDSos 452 3jhds f as12315sdf")
    print transpose("hola mundo")