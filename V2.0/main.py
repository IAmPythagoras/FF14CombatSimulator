from Fight import *
from Spell import *
from Player import *
from Enemy import *


Dummy = Enemy()

Action = [F3, Eno, T3, F4, F4]
PrePull = []

BLMPlayer = BlackMage(2.17, Action, PrePull, [AstralFire, UmbralIce])

Event = Fight([BLMPlayer], Dummy)
Event.SimulateFight(0.01, 15)



