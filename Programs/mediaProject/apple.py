#https://music.apple.com/us/artist/twice/1203816887/see-all?section=singles
#https://music.apple.com/us/artist/twice/1203816887/see-all?section=full-albums
import sys
import requests
import re

toFindAlbums = '<a href="https://music.apple.com/us/album/'

link = sys.argv[1]
nameArtist = sys.argv[2]

url = link

r = requests.get(url)
html = r.text
htmlLines = html.split("\n")

albumsList = []

for line in htmlLines:
	if toFindAlbums in line:
		splitA = line.split("\"")
		albumsList.append(splitA[1])

f = open("toDownload.sh", "w")
for album in albumsList:
	continueA = True
	page = requests.get(album)
	htmlA = page.text
	splitAlbum = htmlA.split("\n")
	for linesA in splitAlbum:
		if "h1 class" in linesA:
			titleA = linesA.split(">")
			titleFinal = titleA[1][0:len(titleA[1])-4]
			titleFinal = titleFinal.replace("&amp;", "&")
			titleFinal = titleFinal.replace("&lt;", "<")
			titleFinal = re.sub("<.*", "", titleFinal)
		elif "picture class" in linesA:
			pictureA = linesA.split(",")

			pictureB = pictureA[4][0:(len(pictureA[4])-5)]
			pictureB = pictureB.replace("592x592bb", "1500x1500")
			print(pictureB)
			break
	toWrite = "aria2c -o \"" + titleFinal + ".webp\" " + pictureB + "\n"
	f.write(toWrite)
	
f.close()