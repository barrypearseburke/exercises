__author__ = 'Barry'
#labtest1 Word cloud

#download files
#remove stop words
#add the words remaining from gettsyburg speach that are more than 3 words
#count words
#create html text file
#add each word into span element
# write html headder
#write all span elements
#write close of html
#end
#test


import httplib2
import string

def downloadfiles():
    print("Downloading files")
    speech = "http://mf2.dit.ie/gettysburg.txt"
    stopwords = "http://mf2.dit.ie/stopwords.txt"
    h = httplib2.http(".catch")
    speech_headers ,speechdownload = h.request(speech)
    stopwords_headers, stopwordsdownload =h.request(stopwords)

    for word in speechdownload:
        print(word)
if __name__ =='main':
    #main fxn

    #call download fxn and format into dict

    words = downloadfiles()

