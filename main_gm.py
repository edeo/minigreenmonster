from gpiozero import LED
from time import sleep
import requests

# here I am assigning the pins from the raspberry pi to the different parts of the count:

ball1 = LED(2)
ball2 = LED(3)
ball3 = LED(4)
strike1 = LED(17)
strike2 = LED(27)
out1 = LED(22)
out2 = LED(10)


# these functions are to take the information from the api json returned, and turn it into
# instructions for turning on and turning off lights.
# you have to have the instructions to turn on and off lights, so that when you go from one 
# batter to the next, the lights don't stay on.


def game_balls(balls):
  if balls == 1:
    ball1.on()
    ball2.off()
    ball3.off()
    print('1 ball')
  elif balls == 2:  
    print('2 balls')
    ball1.on()
    ball2.on()
    ball3.off()
  elif balls == 3:
    print('3 balls')
    ball1.on()
    ball2.on()
    ball3.on()
  elif balls == 0:
    print('0 balls')
    ball1.off()
    ball2.off()
    ball3.off()  
  else:
    print('code error')
    
def game_strikes(strikes):
  if strikes == 1:
    print('1 strikes')
    strike1.on()
    strike2.off()
  elif strikes == 2:
    print('2 strikes')
    strike1.on()
    strike2.on()
  elif strikes == 0:
    print('0 strikes')
    strike1.off()
    strike2.off()
  else:
    print('code error')

def game_outs(outs):
  if outs == 1:
    print('1 outs')
    out1.on()
    out2.off()
  elif outs == 2:
    print('2 outs')
    out1.on()
    out2.on()
  elif outs == 0:
    print('0 outs')
    out1.off()
    out2.off()
  else:
    print('code error')

count = 0


while(count < 30000):
    games = 'https://statsapi.mlb.com/api/v1/schedule/postseason?hydrate=hydrations,linescore&season=2018'
    g = requests.get(url = games)
    games=g.json()
    # for each game, you have to change the numbers after dates and games to makes sure you have the 
    #right game 
    balls   = games['dates'][11]['games'][0]['linescore']['balls']
    strikes = games['dates'][11]['games'][0]['linescore']['strikes']
    outs   = games['dates'][11]['games'][0]['linescore']['outs']
    game_balls(balls)
    game_strikes(strikes)
    game_outs(outs)
    count = count+1
    #  the score board will get ahead of the tv broadcast, you can play with the sleep to try and keep
    # them together
    sleep(3)


