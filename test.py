#!python
from __future__ import print_function
import mlbgame

month = mlbgame.games(2015, 6, home='Mets')
games = mlbgame.combine_games(month)
for game in games:
    print(game)


mlbgame.events.game_events('2018_10_09_bosmlb_nyamlb_1')['2']['top']

mlbgame.events.game_events('2018_10_08_bosmlb_nyamlb_1')

# cycle through the pitches 
mlbgame.events.game_events('2018_10_09_bosmlb_nyamlb_1')['3']['top']

# then tweet them out, have raspberry pi consume the tweets 
 
 https://statsapi.mlb.com/api/v1/game/563376/boxscore
 
"iscurrentbatter" : true
"iscurrentbatter" : true
 "pitching" : {
              "runs" : 1,
              "homeRuns" : 1,
              "strikeOuts" : 3,
              "baseOnBalls" : 0,
              "hits" : 2,
              "inningsPitched" : "1.2",
              "earnedRuns" : 1,
              "battersFaced" : 7,
              "outs" : 5,
              "pitchesThrown" : 26,
              "balls" : 9,
              "strikes" : 17
            },
 

# importing the requests library 
import requests 

URL = 'https://statsapi.mlb.com/api/v1/game/563376/boxscore'

r = requests.get(url = URL)

 x=r.json()

outs = 0
balls = 0
strikes = 0
inning = 0



y['teams']['home']['players']['ID476454']['gameStatus']

y['teams']['home']['players']['ID476454']['jerseyNumber']

y['teams']['home']['players']['ID476454']['stats']


u'status', u'stats', u'seasonStats', u'jerseyNumber', u'person', u'parentTeamId', u'position', u'gameStatus', u'allPositions']

games = 'https://statsapi.mlb.com/api/v1/schedule/postseason?hydrate=hydrations,linescore&season=2018'
g = requests.get(url = games)


games=g.json()


games['dates'][8]['games'][0]['linescore']['currentInning']

games['dates'][8]['games'][0]['linescore']['inningHalf']


balls   = games['dates'][8]['games'][0]['linescore']['balls']
strikes = games['dates'][8]['games'][0]['linescore']['strikes']
outs   = games['dates'][8]['games'][0]['linescore']['outs']

if balls == 0:
  gpio 
  
  
  
from gpiozero import LED
from time import sleep


ball1 = LED(2)
ball2 = LED(3)
ball3 = LED(4)
strike1 = LED(17)
strike2 = LED(27)
out1 = LED(22)
out2 = LED(10)
hit = LED(9)
error = LED(11)

spin1 = LED(5)
spin1 = LED(6)
spin1 = LED(13)
spin1 = LED(19)
spin1 = LED(26)
spin1 = LED(21)
spin1 = LED(20)
spin1 = LED(16)
spin1 = LED(12)
spin1 = LED(7)
spin1 = LED(8)
spin1 = LED(25)


while True:
	led01.on()
	sleep(1)
	led01.off()
	led02.on()
	sleep(1)
	led02.off()
	led03.on()
	sleep(1)

