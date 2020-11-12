import urllib.request
import json
import time

#Your steam API key here
apiKey = ''
#Path where you want FriendsList.json to save
filePath = ''
#SteamID for first account to seed search
seedID = ''
#Depth to search. 1: Friends of Seed, 2: Friends of friends, 3: Friends of friends of friends (recommend no number higher than 3)
searchDepth = 1
#Hard-limit number of API requests in case searchDepth is entered incorrectly
queryLimit = 2

def apiPull(steamID):
    return urllib.request.urlopen('https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key='+apiKey+'&steamid='+steamID).read().decode('utf8')

def Spider(seed, depth):
    #fList = [] 
    holdA = [seed]
    holdB = []
    count = 0
    for i in range(depth):
        for j in holdA:
            time.sleep(0.1)
            count += 1
            #print(j)
            print(count)
            try:
                page = apiPull(j)
                obj = json.loads(page)
                for k in (obj['friendslist']['friends']):
                    holdB.append(k['steamid'])
            except Exception as ex:
                print(ex)
                pass
            finally:
                if count >= queryLimit:
                    break
        #fList += holdB #obsolete
        with open(filePath+r'FriendsList_Depth_'+str(depth)+r'.json', 'a') as file:
            file.write(str(holdB))
        holdA = holdB
        holdB = []
    #return count,fList #obsolete

if __name__ == '__main__':
    Spider(seedID,searchDepth)