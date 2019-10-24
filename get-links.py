# Downloads all songs of birds.
import requests

print("Testing all possible audio files from site! This will take a while!!!")

f = open("links.txt","w+")
counter = 0
for i in range(548,999999):
    perecentage = str(round((i/999999)*100)) + "%"
    id = "{:06d}".format(int(i))
    link = "https://www.allaboutbirds.org/guide/assets/sound/{0}.mp3".format(id)
    print("Found: {0} | {1} | Testing link: {2}".format(counter,perecentage,link),end="\r")
    r = requests.get(link)
    if r.status_code == 200:
        # Valid links:
        counter+=1
        text = (link, "/n")
        f.write(text)
f.close()

