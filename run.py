import os
from time import sleep

class legends:
    def __init__(self):
           self.copy="cp"
           self.storage="/sdcard"
           self.android="/Android"
           self.data="/data"
           self.ml="/com.mobile.legends"
           self.fl="/files"
           self.dr="/dragon2017"
           self.ass="/assets"
           self.doca="/Document/android"

    def logos(self):
           os.system('clear')
           logo="""
                 █████████
                 █▄█████▄█
                 █▼▼▼▼▼
                 █ MOBILE LEGENDS ENEMYS HACK
                 █▲▲▲▲▲
                 █████████ LEARNCODE
                  ██ ██\n"""
           return logo

    def hacks(self):
           self.logos()
           os.system(self.copy+' src/AIHeroPerRoundLimit_MC.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/AIRoundLevelUp_MC.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/BattleConfig.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/CloneModeExtra.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/Document.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/GameMode_mc.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/GuideModeExtra.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/LoadResSimple.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)
           os.system(self.copy+' src/SpecialDPSValue_MC.unity3d '+self.storage+self.android+self.data+self.ml+self.fl+self.dr+self.ass+self.doca)

buapak_ko=legends()
if buapak_ko.hacks() == None:
   sleep(2)
   print('Sukses bosque, selamat bermain ML')
     
