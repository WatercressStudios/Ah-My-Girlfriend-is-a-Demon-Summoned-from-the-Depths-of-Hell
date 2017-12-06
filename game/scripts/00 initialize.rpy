######################### 
# Character Declaration #
#########################
define pro = Character('Makoto', color="#800000")
define bp = Character('Beepy', color="#800000")
define st = Character('S\u26E7Tan', color="#800000")
define riv = Character('Misaki', color="#800000")
define sis = Character('Yumi', color="#800000")
define mm = Character('Mami', color="#800000")
define bb = Character('Bubble', color="#800000")
define lu = Character('Lucy', color="#800000")
define co = Character('Councillor', color="#800000")
define q = Character('???', color="#800000")
define hm = Character('Hall Monitor', color="#800000")
define vs = Character('Lunch Lady', color="#800000")
define tea = Character('Teacher', color="#800000")

######################
# Sprite Declaration #
######################
#Obsolete if we use Ren'Py's image directory!

image beepy fneutral = im.Flip("beepy neutral.png", horizontal=True)
image beepy fneutraltalk = im.Flip("beepy neutraltalk.png", horizontal=True)
image beepy fdreamworks = im.Flip("beepy dreamworks.png", horizontal=True)
image beepy fangryclosed = im.Flip("beepy angryclosed.png", horizontal=True)
image misaki fshout = im.Flip("misaki shout.png", horizontal=True)
image misaki fscowl = im.Flip("misaki scowl.png", horizontal=True)
image misaki fsurprise = im.Flip("misaki surprise.png", horizontal=True)
image bubble fhappytalk = im.Flip("bubble happytalk.png", horizontal=True)
image bubble fsurprise = im.Flip("bubble surprise.png", horizontal=True)
image bubble fsadsmiletalk = im.Flip("bubble sadsmiletalk.png", horizontal=True)
image mami fstammer = im.Flip("mami stammer.png", horizontal=True)
image lucy fneutraltalk = im.Flip("lucy neutraltalk.png", horizontal=True)
image lucy ffrowntalk = im.Flip("lucy frowntalk.png", horizontal=True)
image lucy fbigfrowntalk = im.Flip("lucy bigfrowntalk.png", horizontal=True)
image lucy fneutral = im.Flip("lucy neutral.png", horizontal=True)
image lucy fsmile = im.Flip("lucy smile.png", horizontal=True)
image yumi fexasperated = im.Flip("yumi exasperated.png", horizontal=True)
image yumi fexasperatedtalk = im.Flip("yumi exasperatedtalk.png", horizontal=True)
image yumi fangry = im.Flip("yumi angry.png", horizontal=True)
image yumi fangrytalk = im.Flip("yumi angrytalk.png", horizontal=True)
image yumi fsurpriseshout = im.Flip("yumi surpriseshout.png", horizontal=True)

##################
# BG Declaration #
##################
#Potentially obsolete if we use Ren'Py's image directory!

image garage = "bgs/garage line.png"
image garage evil = "bgs/garage line.png"
image garage mess = "bgs/garage line.png"
image store interior = "bgs/storeinterior.png"
image store exterior = "bgs/superstore exterior.jpg"
image store exteriornight = "bgs/superstore exterior night.jpg"
image bedroom = "bgs/House/bedroom.png"
image bedroom night = "bgs/House/bedroom night.png"
image bedroom dark = "bgs/House/bedroom dark.png"
image hallway = "bgs/House/hallway house.png"
image house = "bgs/House/houses.png"
image house evening = "bgs/House/houses evening.png"
image house night = "bgs/House/houses night.png"
image kitchen = "bgs/House/kitchen.png"
image living room = "bgs/House/living room.png"
image movie1 = "bgs/House/Movie/movie 1.png"
image movie2 = "bgs/House/Movie/movie 2.png"
image movie3 = "bgs/House/Movie/movie 3.png"
image movie4 = "bgs/House/Movie/movie 4.png"
image movie5 = "bgs/House/Movie/movie 5.png"
image bathroom = "bgs/School/bathroom.png"
image cafeteria = "bgs/School/cafeteria.png"
image classroom1 = "bgs/School/classroom 1.jpg"
image classroom2 = "bgs/School/classroom 2.jpg"
image classroom evening1 = "bgs/School/classroom evening.jpg"
image classroom evening2 = "bgs/School/classroom evening2.jpg"
image courtyard day1 = "bgs/School/courtyard day 1.jpg"
image courtyard day2 = "bgs/School/courtyard day 2.jpg"
image courtyard evening1 = "bgs/School/courtyard evening 1.jpg"
image courtyard evening2 = "bgs/School/courtyard evening 2.jpg"
image school hallway = "bgs/School/hallway.png"
image meeting = "bgs/School/meeting.png"
image rooftop = "bgs/School/rooftop.png"
image white = "bgs/white.png"


###################
# CGs             #
###################
#Potentially obsolete if we use Ren'Py's image directory!

image intro1 = "cgs/intro/MakotoIntroCG-1.png"
image intro2 = "cgs/intro/MakotoIntroCG-2.png"
image intro3 = "cgs/intro/MakotoIntroCG-3.png"
image intro4 = "cgs/intro/MakotoIntroCG-4.png"
image satanintronormal = "cgs/stan/SatanIntroCG-Normal.png"
image satanintrotongue = "cgs/stan/SatanIntroCG-Tongue.png"
image satanintrowinktongue = "cgs/stan/SatanIntroCG-WinkTongue.png"
image satanintrowink = "cgs/stan/SatanIntroCG-Wink.png"
image beepyintro = "cgs/beepy/BeepyIntroCG-Center.png"
image beepyintroleft = "cgs/beepy/BeepyIntroCG-Left.png"
image beepyintroright = "cgs/beepy/BeepyIntroCG-Right.png"
image beepyintroroll = "cgs/beepy/BeepyIntroCG-Eyeroll.png"
image beepyintrostan = "cgs/beepy/BeepyIntroCG-Satan.png"
image misakiintroangry = "cgs/misaki/MisakiIntroCG-AngryLookingAtViewer.png"
image misakiintroclosed = "cgs/misaki/MisakiIntroCG-ClosedEyes.png"
image misakiintrolook = "cgs/misaki/MisakiIntroCG-LookingAtViewer.png"
image misakiintroopen = "cgs/misaki/MisakiIntroCG-OpenEyes.png"


#######
# VFX #
#######

###################
# SFX             #
###################


###################
# Music           #
###################


label start:
    jump scene1