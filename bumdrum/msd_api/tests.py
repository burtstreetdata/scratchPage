import unittest
import json
import msf_mlb_api as SUT


class MiscTests(unittest.TestCase):

    pbp = None

    def setUp(self):
        with open("pbp.json.big", "r") as f:
            self.pbp = json.load(f)

    def test_talkback(self):
        self.assertEqual(SUT.talkback(), "hi")

    def test_expected_json(self):
        self.assertEqual(self.pbp["gameplaybyplay"]['game']['id'], "44659")

    def test_pitcher_batter_list_first_batter_spotcheck(self):
        matchupData = SUT.pitcherBatterMatchups(self.pbp)
        self.assertEqual(matchupData['Matchups'][0]["Batter"], '10668')

    def test_pitcher_batter_list_last_pitcher_spotcheck(self):
        matchupData = SUT.pitcherBatterMatchups(self.pbp)
        self.assertEqual(matchupData['Matchups'][-1]["Pitcher"], '10322')

    def test_pitcher_batter_list(self):
        matchupData = SUT.pitcherBatterMatchups(self.pbp)
        Roster = [ '10322', '10324', '10325', '10327', '10328',
'10329', '10330', '10331', '10393', '10464', '10657', '10668',
'10671', '10672', '10686', '10915', '10953', '10961', '11135',
'11136', '11139', '11221', '11223', '11264', '11304', '11465',
'11586', '12333', '12361', '12484', '13122', '13999', '14143', '14594'
        ]
        ids = list(map(lambda plyr: plyr['ID'],  matchupData['Roster']))
        for p in Roster:
            if not p in ids :
                print (p + " is missing from  roster")
            self.assertTrue(p in ids)
        


    
