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

    def test_pitcher_batter_list(self):
        matchups = SUT.pitcherBatterMatchups(self.pbp)
        self.assertEqual(matchups[0]["Batter"], '10668')
    
