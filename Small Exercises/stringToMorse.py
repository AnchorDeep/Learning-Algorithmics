#Author:
#Input: morse code
#Output: English
#Contributors: Master Code Online on youtube had a tutorial on this stuff



def str2Morse(text):

  morseDictionary = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "." : ".-.-.-", "," : "--..--"}

  morsecode = ""

  for a in text:
    morsecode += morseDictionary[a.upper()]

  return morsecode

text = input("Text to convert: ")
print(str2Morse(text))