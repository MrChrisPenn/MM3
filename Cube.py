"""
Taken from the original idea by Craig Richardson in his 'Learning to program with Minecraft'
book. 
"""

import microbit
from mcpi import minecraft as minecraft
from mcpi import block as block
from datetime import datetime
import time
import serial
import random
 
mc = minecraft.Minecraft.create()

def bigBlock(Increase,block):
    pos = mc.player.getTilePos()
    mc.postToChat("Build")
    mc.setBlocks(pos.x, pos.y, pos.z,pos.x+Increase, pos.y+Increase, pos.z+Increase, block)
    mc.postToChat("Wait")
    time.sleep(5)
    mc.postToChat("Clear")
    mc.setBlocks(pos.x, pos.y, pos.z,pos.x+Increase, pos.y+Increase, pos.z+Increase, 0)
    
    
Increase = 0
pos = mc.player.getTilePos()
while True:

    if microbit.button_a.was_pressed():
        Increase = Increase+1
        msg = "Size = 1 block+"+str(Increase)
        mc.postToChat(msg)

    if microbit.button_b.was_pressed():
        bigBlock(Increase,46)
    
    time.sleep(1)
    
    



