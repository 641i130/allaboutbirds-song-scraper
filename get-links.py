# Downloads all songs of birds.
import requests

print("Testing all possible audio files from site! This will take a while!!!")
f = open("links.txt","w+")
counter = 0
for i in range(0,1000000,):
    perecentage = str(round((i/1000000)*100)) + "%"
    #id = "{0:06d}".format(int(i))
    id = "{0}".format(int(i))
    # link = "https://www.allaboutbirds.org/guide/assets/sound/{0}.mp3".format(id)
    link = "https://download.ams.birds.cornell.edu/api/v1/asset/{0}".format(id)
    print("Found: {0} | {1} | Testing link: {2}".format(counter,perecentage,link),end="\r")
    r = requests.get(link)
    if r.status_code == 200:
        # Valid links:
        counter+=1
        f.write(link+'\n')
f.close()

