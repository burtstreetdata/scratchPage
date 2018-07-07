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
    
    try:
        response = requests.get(
            url=url,
            params={
                "gameid": "20180630-MIN-CHC",
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
       # go thru the  batter ups, list all  the players
       players = {} # the players we've seen so far
       matchups = []
       thismatchup, lastmatchup = ({}, {'Batter':'', 'Pitcher':''})
       
       atbats = pbpjson['gameplaybyplay']['atBats']['atBat']
       for  atbat in atbats:
              for atbatplay in atbat['atBatPlay']:
                     if 'pitch' in atbatplay :
                            pitcherId = atbatplay['pitch']['pitchingPlayer']['ID']
                            batterId = atbatplay['pitch']['battingPlayer']['ID']
                            thismatchup={'Batter': batterId, 'Pitcher': pitcherId}
                            if (thismatchup['Batter'] != lastmatchup['Batter'] or
                                thismatchup['Pitcher'] != lastmatchup['Pitcher'] ):
                                   matchups.append(thismatchup)
                            lastmatchup=thismatchup;
#       print(matchups)
       return matchups





    
