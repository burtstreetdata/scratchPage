# My sports feeds  MLB api

import base64
import requests
import json

def getpwd():
       with open("/mnt/c/tmp/bbpwd.txt") as secretfile:
              p=secretfile.readline().strip()
              return  p

def playbyplay(away, home, date):
    url='https://api.mysportsfeeds.com/v1.2/pull/mlb/2018-regular/game_playbyplay.json'
    username="burtstreetdata"
    password=getpwd()
    authstring="Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
    gameid = f"{date}-{away}-{home}"
    
    try:
        response = requests.get(
            url=url,
            params={
                "gameid": gameid
            },
            headers={
                "Authorization": authstring
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        if not response.ok :
            print('\nThe submitted headers were ' + authstring)
            # return None
            print ('fail')
        else:
            pass
    except requests.exceptions.RequestException:
        print('HTTP Request failed and said: ' + response.content)
        print('The headers were ' + headers)

    parsed = json.loads(response.content.decode('utf-8'))
    return parsed

def talkback():
    return "hi"

def pitcherBatterMatchups(pbpjson):
       # go thru the  batter ups, list all  the combinations of pitchers and
       # batters. Normally this is found  in 'pitch' element, but a matchup
       # can also come when there is  an intentional walk
       players = [] # the players we've seen so far
       matchups = []
       thismatchup, lastmatchup = ({'Batter':'', 'Pitcher':''}, {'Batter':'', 'Pitcher':''})
       pitcherId, batterId = (None,  None)
       
       atbats = pbpjson['gameplaybyplay']['atBats']['atBat']
       for  atbat in atbats:
              
              for atbatplay in atbat['atBatPlay']:
                     if 'baseRunAttempt' in atbatplay and atbatplay['baseRunAttempt']['isWalkIntentional']=="true" :
                            # on an intentional walk, there may be no pitches, so matchup
                            # won't be present.
                            batter = atbatplay['baseRunAttempt']['runningPlayer']
                            batterId = batter['ID']
                            batterName = f"{batter['FirstName']} {batter['LastName']}"
                            pitcherId = lastmatchup['Pitcher']

                     else : 
                            if 'pitch' in atbatplay :
                                   pitcher= atbatplay['pitch']['pitchingPlayer']
                                   pitcherId = pitcher['ID']
                                   pitcherName = f"{pitcher['FirstName']} {pitcher['LastName']}"
                                   batter = atbatplay['pitch']['battingPlayer']
                                   batterName = f"{batter['FirstName']} {batter['LastName']}"
                                   batterId = batter['ID']
                     if (pitcherId != None ) and (not pitcherId in list(map(lambda x: x['ID'], players))) :
                            players.append({
                                   "ID" : pitcherId,
                                   "Name" :pitcherName
                                   })
                     if (batterId != None) and not (batterId in  list(map (lambda x: x['ID'], players))) :
                            players.append({
                                   "ID" : batterId,
                                   "Name" :batterName
                                   })
                     thismatchup={'Batter': batterId, 'Pitcher': pitcherId}
                     if (thismatchup['Batter'] != lastmatchup['Batter'] or
                         thismatchup['Pitcher'] != lastmatchup['Pitcher'] ):
                            matchups.append(thismatchup)
                            lastmatchup=thismatchup;
#       print(matchups)
       return {'Matchups' : matchups,
               'Roster' : players}





    
