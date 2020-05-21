# -*- coding: utf-8 -*-

# This script reads all of the output from WikiExtractor.py and cleans/reorganizes it by:
# - removing the <doc></doc> tags (and their contents) at the beginning and end of each article
# - lowercasing each word
# - removing punctuation, digits, and <br> tags from the edges of each word
# - omitting words altogether if they still contain any of the above
# - omitting any duplicate words
# - writing the remaining/cleaned words, one per line, to the file "cleanedwikiwords.txt"

# This is intended to be run from within the text/ directory
# that is created by WikiExtractor.py
# (text/ should contain a series of directories AA, AB, AC, ...,
# each of which contains a series of text files wiki_00, wiki_01, ...)



import io
import os
from datetime import datetime



# read wiki text from file srcpath and append cleaned, unique words one per line to file destpath
def cleanandsplit(srcpath, destpath):
    with io.open(srcpath,"r",encoding="utf-8") as src:
        with io.open(destpath,"a",encoding="utf-8") as dest:
            sline = src.readline() 
            while len(sline) > 0:
                if not sline.startswith("<doc") and not sline.startswith("</doc"):
                    wds = sline.split()
                    #numwdstotal += len(wds)
                    for w in wds:
                        cleaned = clean(w.lower())
                        if len(cleaned)>0 and cleaned not in uniquewds:
                            uniquewds.append(cleaned)
                            dest.write(cleaned+"\n")
                    
                sline = src.readline()
                
     
# remove punctuation, numerals, and <br> tags from word edges
# return cleaned word, or empty string if the word still contains above chars word-internally
def clean(word):
    donotwant = ["-","–","—","(","+","=","_","*",",",".",")","[","]",'"',"'","1","2","3","4","5","6","7","8","9","0","/",";",":","„","”","<",">"]
    if word.startswith("<br>"):
        word = word[4:]
    while len(word)>0 and word[0] in donotwant:
        word = word[1:]
    while len(word)>0 and word[-1] in donotwant:
        word = word[:-1]
    for punc in donotwant:
        if punc in word:
            word = ""
    return word
                
# iterate through AA, AB, AC, ... directories and clean each of their wiki_00, wiki_01, wiki_02 files
contents = os.listdir()
#numwdstotal = 0
uniquewds = []
for item in contents: #eg AB
    if os.path.isdir(item):
        texts = os.listdir(item)
        for txt in texts: #eg wiki_05
            cleanandsplit(item+"/"+txt,"cleanedwikiwords"+datetime.now().strftime("_%Y%m%d_%H%M%S")+".txt")
print(str(len(uniquewds))+" unique clean words written")#, of "+str(numwdstotal)+" words total")
