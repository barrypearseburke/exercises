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
    #file urls
    speech = "http://mf2.dit.ie/gettysburg.txt"
    stopwords = "http://mf2.dit.ie/stopwords.txt"

    h = httplib2.Http(".catch")
    speech_headers, speechdownload = h.request(speech)
    stopwords_headers, stopwordsdownload =h.request(stopwords)

    #split on space
    speechdownload =speechdownload.decode()
    speechdownload =speechdownload.split(' ')

    #split on conma
    stopwordsdownload =stopwordsdownload.decode()
    stopwordsdownload =stopwordsdownload.split(',')

    #put words in dict
    keywords = {}
    for word in speechdownload:
        word =word.strip()
        size = len(word)
        if size > 3: #ignores words of <=3
            if word in keywords:
                keywords[word] += 1
            else:
                keywords[word] = 1

    for word2 in stopwordsdownload:
        word2 = word2.strip()
        if word2 in keywords:
            keywords[word2] = 0 #if words in stopwords,take them out
#add works to dict
    #print(keywords) #test
    return (keywords) #return


def writeto(wordspassed):
    #going to create and write file here

    #create file
    try:
        fileopen =open("wordcloud.html","w") #open file called wordcloud
    except IOError as erroronfile:
        print(erroronfile)

    #file is now created and we need to add span element and the headers to the file

    #firstly add header

    html_headders = "<!DOCTYPE html> <html> <head lang=\"en\"> <meta charset=\"UTF-8\"> <title>Tag Cloud Generator</title> </head> <body> <div style=\"text-align: center; vertical-align: middle; font-family: arial; color: green background-color:blue; border:1px solid blue\">"
    html_end = "</div> </body> </html>"
    fileopen.write(html_headders)

    #the bit that changes
    minvalue =20
    maxvalue =200
    multiplier =10
    for k1,v1 in wordspassed.items():
        #min and max value for words setting

        if v1 <minvalue:
            v1 = ( minvalue + (v1*multiplier))
            if v1 > maxvalue:
                v1 =maxvalue
        if v1 > maxvalue:
            v1 =maxvalue

        span = ( "<span style=\"font-size: {}px\"> {} </span>" .format(v1,k1) )
        fileopen.write(span)
        fileopen.write("\n")

    fileopen.write(html_end)







#main fxn

#call download fxn and format into dict

wordsfinal = downloadfiles()
writeto(wordsfinal)