from gpiozero import LED
from time import sleep
import requests

ball1 = LED(2)
ball2 = LED(3)
ball3 = LED(4)
strike1 = LED(17)
strike2 = LED(27)
out1 = LED(22)
out2 = LED(10)
hit = LED(9)
error = LED(11)

spin01 = LED(5)
spin02 = LED(6)
spin03 = LED(13)
spin04 = LED(19)
spin05 = LED(26)
spin06 = LED(21)
spin07 = LED(20)
spin08 = LED(16)
spin09 = LED(12)
spin10 = LED(7)
spin11 = LED(8)
spin12 = LED(25)

def game_balls(balls):
  if balls == 1:
    print('1 ball')
    ball1.on
    ball2.off()
    ball3.off()
  elif balls == 2:  
    print('2 balls')
    ball1.on()
    ball2.on()
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
    print('2 strikes')
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

games = 'https://statsapi.mlb.com/api/v1/schedule/postseason?hydrate=hydrations,linescore&season=2018'

while(count < 10000):
    g = requests.get(url = games)
    games=g.json()
  
    balls   = games['dates'][10]['games'][1]['linescore']['balls']
    strikes = games['dates'][10]['games'][1]['linescore']['strikes']
    outs   = games['dates'][10]['games'][1]['linescore']['outs']

    game_balls(balls)
    game_strikes(strikes)
    game_outs(outs)
    
    count = count+1
    sleep(2)


