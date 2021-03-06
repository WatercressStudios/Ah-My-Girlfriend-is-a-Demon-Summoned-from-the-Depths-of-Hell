label scene12:
    scene house with dissolve

    "At last, another tedious and tiresome school day draws to a close."
    "I feel drained and weary all at once, like Samson without his flowing mane of hair."
    "Each monotonous day threatens to end my reign of terror before it ever truly begins."
    "But now… it {i}has{/i} ended, and I have returned to my humble abode."
    "I am not expecting much of a welcome; my progenitors are still away, and my sister is at odds with me after my summoning ritual."
    "I’m not even sure if Beepy managed to make it back home. She might be napping somewhere on a street corner for all I know."
    "Oh well; there’s not much I can do about that."
    "Better for me to head inside and relax than worry about things beyond my control."
    
    scene hallway with dissolve

    play sound "sfx/Door Open.mp3"
    "I open the door to my house and exchange my usual greeting."
    

    voice "C-12-1.mp3" #Makoto (Reece Bridger)
    pro "I'm home."

    "But as soon as I say that, something completely unexpected happens."

    show bubble bigsmiletalk with easeinleft:
            align (0.35, 1.0)

    #music hijinks
    play music shenanigansthemeintro fadein 1.0
    queue music shenaniganstheme
    voice "C-12-2.mp3" #Bubble 
    bb "Yay~! Welcome home, Makoto~!"
            
    "A girl who I've never seen before suddenly latches onto me in fervent excitement."
    "Or, wait, {i}is{/i} she just a girl? Her skin is a dark shade of blue…"

    voice "C-12-3.mp3" #Makoto (Reece Bridger)
    pro "What the--!? Who are you?"

    show mami shout with easeinright:
            align (0.65, 1.0)

    voice "C-12-4.mp3" #Mami 
    mm "{b}Hey!{/b} What do you think you're doing!?"
    
    play sound "sfx/Yoink.mp3"

    "Before I know it, the strange girl is violently pulled away…"
    "...by another, almost identical-looking girl. Only, her skin is a lighter shade of blue…"

    show bubble sadsmiletalk

    voice "C-12-5.mp3" #Bubble 
    bb "What are you getting mad at me for!? I was just greeting Makoto like we were supposed to!"
    
    show mami lecture
    show bubble frown
    voice "C-12-6.mp3" #Mami 
    mm "You were supposed to wait until {i}after{/i} Beepy told us to introduce ourselves! You weren't paying attention at all, were you!?"
    
    show bubble scowltalk
    show mami scowl
    voice "C-12-7.mp3" #Bubble 
    bb "Well, why didn't you remind me about it instead of yelling!?"
    
    show mami shoutvein
    show bubble scowl
    voice "C-12-8.mp3" #Mami 
    mm "Like I'm gonna spend all my time being your friggin' babysitter!"
    
    show bubble xdshout
    voice "C-12-9.mp3" #Bubble 
    bb "Who're you calling a baby, you big baby!?"

    "While the twins bicker among themselves, I stand there… I'm not sure what to do."
    "My bewilderment eventually reaches a critical peak in what could only be described as a moment of existential horror."
    "Just when things can't get any crazier, yet another mysterious girl enters the picture."

    show lucy frowntalk with easeinright
    show bubble surprise
    show mami scowl

    voice "C-12-10.mp3" #Lucy (Vivi)
    lu "P-please, stop fighting you two! Y-you're making a scene!"

    show bubble sadblush with easeinleft:
        align (0.30, 1.0)
    show mami scowlclosed with easeinright:
        align (0.70, 1.0)
    show lucy angst
    "She seems to have the situation under control, but once she notices me, she flies into another panic."

    #show Lucy frightened

    show lucy bigfrowntalk
    voice "C-12-11.mp3" #Lucy (Vivi)
    lu "{b}Ah!{/b} Wait! Y-Y-You're not supposed to see me either!"
    
    play sound "sfx/Sweatdrop.mp3"
    
    show lucy frowntalk
    voice "C-12-12.mp3" #Lucy (Vivi)
    lu "I-I, um… j-just pretend you didn't see anything, okay!?"
    
    voice "C-12-13.mp3" #Makoto (Reece Bridger)
    pro "Wait, what!? {i}Who's{/i} not supposed to see you?"

    "Between this flustered girl and the arguing twins, I'm not sure what to make of this situation."
    "Who are these people? How did they get in my house!?"

    #q line here voiced by Beepy

    show lucy bigfrowntalk
    show bubble surprisetalk
    show mami neutral
    
    voice "C-12-14.mp3" #??? 
    q "...Jeez, you guys…"

    show beepy fneutral with easeinright:
            align (1.0, 1.0)
    "As if to answer my question, Beepy rises from the sofa, groggy as usual, and saunters over to the front door."

    #enter Beepy stage right

    show beepy fdreamworks
    voice "C-12-15.mp3" #Beepy (Hikari)
    bp "The least you could do is behave yourselves..."
    
    show lucy frowntalk
    voice "C-12-16.mp3" #Lucy (Vivi)
    lu "I-I'm sorry, Beepy! I t-tried my best to keep things under control!"
    
    show mami angrysmiletalk
    voice "C-12-17.mp3" #Mami 
    mm "If you wanna blame anyone, blame that little troublemaker over there!"
    
    show bubble angrysmiletalk
    show beepy fneutral
    show lucy neutral
    voice "C-12-18.mp3" #Bubble 
    bb "You're more of a troublemaker than I am! You tried to steal that big TV in the living room!"
    
    show mami closedtalk
    voice "C-12-19.mp3" #Mami 
    mm "Yeah, but who was the one about to raid the entire fridge until Beepy stopped them!? Oh, right, it's you!"
    
    show beepy fangryclosed
    voice "C-12-20.mp3" #Beepy (Hikari)
    bp "I mean, I only did that because I raided it last night… There isn't much there anyways."
    
    #music cut
    stop music fadeout 1.0
    show beepy fneutral
    show lucy frowntalk
    show mami scowl
    show bubble surprise
    voice "C-12-21.mp3" #Makoto (Reece Bridger)
    pro "Hold up, wait wait {b}wait!{/b}"

    "I hold my hands up and raise my voice, desperate to have everyone calm down even for a little bit."
    "It seems to work, but my head is still abuzz with questions."
    "And right now, my familiar is the only one who can answer them."

    #exit Lucy and twins stage left
    hide mami with easeoutright
    hide lucy with easeoutright
    hide bubble with easeoutright
    show beepy fneutral with easeinright:
            align(0.5, 1.0)

    #music lighthearted
    play music lightheartedtheme fadein 1.0
    voice "C-12-22.mp3" #Makoto (Reece Bridger)
    pro "Beepy, what is going on here?"
    
    show beepy neutraltalk
    voice "C-12-23.mp3" #Beepy (Hikari)
    bp "Huh? Oh, well…"
    
    show beepy neutralclosedtalk
    voice "C-12-24.mp3" #Beepy (Hikari)
    bp "I found my way home, as you see. It was actually pretty easy once I picked up the house's scent…"
    
    show beepy eyebrowtalk
    voice "C-12-25.mp3" #Beepy (Hikari)
    bp "It smelled a little bit like that cape of yours… You know, you really should wash that thing sometime."
    
    show beepy eyebrow
    voice "C-12-26.mp3" #Makoto (Reece Bridger)
    pro "H-How did you associate that with…"
    
    voice "C-12-27.mp3" #Makoto (Reece Bridger)
    pro "*Sigh*... Nevermind. That's beside the point."
    
    show beepy neutralclosedtalk
    voice "C-12-28.mp3" #Beepy (Hikari)
    bp "Right, anyways…"

    #show Beepy sad

    show beepy neutraltalk
    voice "C-12-29.mp3" #Beepy (Hikari)
    bp "Once I made it back here, I realized there wasn't anyone for you to hang out with."
    
    show beepy dreamworks
    voice "C-12-30.mp3" #Beepy (Hikari)
    bp "I mean, your sister's an option - but with that lame schtick of yours, I dunno how she can even tolerate you."
    
    show beepy neutraltalk
    voice "C-12-31.mp3" #Beepy (Hikari)
    bp "I felt there wasn't much of a point in having you be lonely and miserable the whole time..."

    #show Beepy smiling

    show beepy smileclosed
    voice "C-12-32.mp3" #Beepy (Hikari)
    bp "So I brought a couple of my friends over."
    
    voice "C-12-33.mp3" #Makoto (Reece Bridger)
    pro "Huh? Y-You can do that?"
    
    show beepy neutraltalk
    voice "C-12-34.mp3" #Beepy (Hikari)
    bp "Why not? You're only bound to me, so having other demons around shouldn't be a problem."
    
    show beepy smile
    voice "C-12-35.mp3" #Beepy (Hikari)
    bp "If Satan has issue with it, well… she can stuff it."

    "...Did she really do all that for me?"
    "The last time I saw her, she didn't seem to concern herself over who I was or how much of the dark arts I've mastered."
    "But… she does care, doesn't she?"

    voice "C-12-36.mp3" #Makoto (Reece Bridger)
    pro "Wow… I-I didn't expect you to go this far, Beepy."
    
    show beepy dreamworks
    voice "C-12-37.mp3" #Beepy (Hikari)
    bp "Pretty great, huh? I bet you never knew what I was planning~"
    
    voice "C-12-38.mp3" #Beepy (Hikari)
    bp "My poker face is unbeatable."
    
    voice "C-12-39.mp3" #Makoto (Reece Bridger)
    pro "...I can't tell if it's {i}really{/i} a poker face or if you're just tired all the time."

    show beepy neutraltalk

    voice "C-12-40.mp3" #Beepy (Hikari)
    bp "Anyways, I should probably introduce you, so…"
    
    show beepy eyebrowtalk
    voice "C-12-41.mp3" #Beepy (Hikari)
    bp "Who wants to go first?"

    #enter twins, stage left
    #show Bubble happy, show Mami angry

    show beepy neutral
    show bubble fhappytalk with easeinright:
            align (0.75, 1.0)
    
    voice "C-12-42.mp3" #Bubble 
    bb "Ooh, ooh, me me me me! I wanna go first!"
    
    show mami shout with easeinright:
            align (0.9, 1.0)
    
    voice "C-12-43.mp3" #Mami 
    mm "No way! We gotta do our intro together, remember?"

    show bubble scowl

    voice "C-12-44.mp3" #Bubble 
    bb "Yeah, right! There's no way I'm doing an intro with {i}you!{/i} You'll just mess everything up like you always do!"
    
    show mami shoutvein
    voice "C-12-45.mp3" #Mami 
    mm "At least my intro is better than that dumb baby crap you came up with!"
    
    show bubble xdshout
    voice "C-12-46.mp3" #Bubble 
    bb "{b}What did you say!?{/b}"

    show beepy angryclosed
    "Good God, do these two do anything besides quarrel with each other?"

    show beepy angryclosedtalk
    voice "C-12-47.mp3" #Beepy (Hikari)
    bp "...Alright, this is getting nowhere."
    
    show beepy angrytalk with easeinright:
            align(0.10, 1.0)
    voice "C-12-48.mp3" #Beepy (Hikari)
    bp "Lucy, you go."

    #enter Lucy stage left

    show beepy neutral
    show lucy fneutraltalk with easeinright:
            align (0.55, 1.0)
    show bubble fsurprise
    show mami neutral
    voice "C-12-49.mp3" #Lucy (Vivi)
    lu "Huh? M-M-Me!?"
    
    voice "C-12-50.mp3" #Lucy (Vivi)
    show lucy ffrowntalk
    lu "I-I couldn't! I mean, I'm not ready..."
    
    show beepy eyebrowtalk
    voice "C-12-51.mp3" #Beepy (Hikari)
    bp "You don't have to do a flashy introduction, just say your name."

    #show Lucy determined

    show beepy eyebrow
    show lucy fneutral
    voice "C-12-52.mp3" #Lucy (Vivi)
    lu "N-No, I can't let everyone else down like that!"
    
    show beepy neutral
    show lucy fsmile
    voice "C-12-53.mp3" #Lucy (Vivi)
    lu "Besides, h-he deserves a proper introduction from all of us!"
    
    show beepy smile
    voice "C-12-54.mp3" #Beepy (Hikari)
    bp "...Suit yourself."

    #exit Beepy stage right

    show lucy smile with easeinright:
            align (0.5,1.0)
    "Lucy takes a deep breath, as if to steady herself."

    show lucydetermined with dissolve
    
    voice "C-12-55.mp3" #Lucy (Vivi)
    lu "Um… I-I am Lucifer of Pride…"

    show lucyfrightened
    hide lucydetermined

    play sound "sfx/Sweatdrop.mp3"
    
    voice "C-12-56.mp3" #Lucy (Vivi)
    lu "No, wait! I wasn't supposed to start like that! L-L-Lemme try again!"
    
    voice "C-12-57.mp3" #Lucy (Vivi)
    lu "I, um… I-I-I'm the one who, uh, m-makes you… p-proud of…"
    
    voice "C-12-58.mp3" #Lucy (Vivi)
    lu "Of… of… of…"

    show lucycrying
    hide lucyfrightened

    voice "C-12-59.mp3" #Lucy (Vivi)
    lu "{b}{i}Uwaaaaaaaah!{/i}{/b}"
    
    voice "C-12-60.mp3" #Lucy (Vivi)
    lu "I'm so sorry! I forgot all of my lines!"
    
    voice "C-12-61.mp3" #Lucy (Vivi)
    lu "*Sniff* J-Just call me Lucy, okay…?"
    
    show lucy bigcry
    show beepy neutral
    show bubble fsadsmiletalk
    show mami scowlclosed
    
    hide lucycrying with dissolve
    
    "Well… that could have gone better."
    "She had a burst of confidence just a second ago, but it fell apart as soon as started talking."
    "I never expected a demon of pride to falter so easily; then again, I've been blindsided at every turn since the day began."

    hide lucy with easeoutright
    show bubble pitytalk
    voice "C-12-62.mp3" #Bubble 
    bb "What's wrong, Lucy? Why are you crying?"
    
    show mami shout
    voice "C-12-63.mp3" #Mami 
    mm "Obviously it was because you wouldn't do your intro!"

    #show Bubble angry

    show bubble scowltalk
    voice "C-12-64.mp3" #Bubble 
    bb "What are you talking about!? {i}You{/i} were the one who wouldn't do {i}your{/i} intro!"
    
    show mami closedtalk
    voice "C-12-65.mp3" #Mami 
    mm "Oh yeah!? Just watch! I'll pull off an intro so good that he'll be head-over-heels for me!"
    
    show bubble xdshout with easeinright:
            align (0.6, 1.0)
            
    voice "C-12-66.mp3" #Bubble 
    bb "Nu-uh~! My intro's gonna be bigger and better than yours!"

    show bubble smiletalk
    show mami angrysmiletalk with easeinright:
            align (0.4, 1.0)
    #music cut
    stop music fadeout 1.0
    show beepy angry
    "Before I know it, both of them are assaulting me."

    #show Bubble happy, show Mami pumped up
    #dual audio both Bubble and Mami's lines play at the same time

    show twinssmug with dissolve
    #music magical girl
    play music satansthemeintro fadein 1.0
    queue music satanstheme
    show mami neutraltalk
    voice "C-12-67.mp3" #Mami 
    mm "Who makes you steal from the cookie jar!? It's me!"
    
    show bubble bigsmiletalk
    voice "C-12-68.mp3" #Bubble 
    bb "Gimme your food~! Gimme your food~! {i}Gobble, gobble, munch~!{/i}"
    
    show twinsirritated
    hide twinssmug
    show mami smugtalk
    voice "C-12-69.mp3" #Mami 
    mm "Who makes you miserly with money!? It's me!"
    
    show bubble pitytalk
    voice "C-12-70.mp3" #Bubble 
    bb "I'm the one who makes you eat~! {i}Crunch, crunch, crunch~!{/i}"
    
    show twinsright
    hide twinsirritated
    show mami neutraltalk
    voice "C-12-71.mp3" #Mami 
    mm "Who makes you say ‘charities suck!?' Yep, that's me too!"
    
    show twinsleft
    hide twinsright
    show bubble happytalk
    voice "C-12-72.mp3" #Bubble 
    bb "I'm here for every meal, be it dinner or lunch~!"
    
    show twinsright
    hide twinsleft
    show mami xdtalk
    voice "C-12-73.mp3" #Mami 
    mm "Hell yeah, Mammon of Greed! That's meeee~!"
    
    show twinsleft
    hide twinsright
    show bubble xdbigshout
    voice "C-12-74.mp3" #Bubble 
    bb "I'm Beelzebub of Gluttony, the cutest of the bunch~!"
    
    show beepy eyebrow
    show twinsright
    hide twinsleft
    "The information overload threatens to overtake me!"
    show mami fscowl
    show bubble fscowl
    show twinsleft
    hide twinsright
    "They make no effort to coordinate their introductions at all, resulting in an unbearable cacophony."
    #music cut
    stop music fadeout 1.0
    hide twinsleft with dissolve

    "And while I'm trying to prevent a headache from breaking out, the twins start arguing again."

    #show Bubble and Mami angry

    #music hijinks
    play music shenanigansthemeintro fadein 1.0
    queue music shenaniganstheme
    show mami fshout
    voice "C-12-75.mp3" #Mami 
    mm "What the hell was that!? Your stupid intro messed everything up!"
    
    show bubble fscowltalk
    voice "C-12-76.mp3" #Bubble 
    bb "No it didn't! {i}Your{/i} intro got in the way of {i}mine{/i}! What is your problem, you ultra jerkface!?"
    
    show mami fshoutvein
    voice "C-12-77.mp3" #Mami 
    mm "I'll tell you what my problem is! She's short, looks like an idiot, and talks just like one!"
    
    show bubble fxdshout
    voice "C-12-78.mp3" #Bubble 
    bb "You just described yourself, you big dummy!"

    show mami fxdangry
    voice "C-12-79.mp3" #Mami 
    mm "{b}What was that!?{/b}"

    #exit twins stage right

    show beepy angry
    "The chaos in the atmosphere climbs toward its peak."
    "I have to do something before it erupts like Mt. Pompeii on that fateful day in--"

    #q line here voiced by Yumi

    show bubble fsurprise
    show mami fstammer
    show beepy eyebrow
    #music cut
    stop music fadeout 1.0
    voice "C-12-80.mp3" #??? 
    q "{b}MAKOTO!!!{/b}"

    "{i}Shit.{/i}"
    "Too late. My soul is forfeit now."
    play sound "sfx/Door Open.mp3"
    
    "Yumi bursts into the room."

    #enter Yumi stage right, annoyed
    show mami fstammer
    show bubble surprise
    show yumi angrywideshout with easeinright:
        align (1.0, 1.0)


    voice "C-12-81.mp3" #Yumi (Kaito)
    sis "{b}What{/b} is going {i}on{/i} down here!? I've been calling you all this time, how have you still..."

    #show Yumi surprised

    show yumi surpriseshout
    voice "C-12-82.mp3" #Yumi (Kaito)
    sis "not… heard... me...?"

    "As soon as Yumi surveys the scene, her rage subsides."
    show yumi surprise
    "I can see her face growing as pale as a ghost, being constrained by half a dozen conflicting emotions all at once."
    "I want to tell her what's going on, but… I don't think I can properly explain this either."
    show yumi exasperated
    "Then, as if possessed, she breathlessly speaks to me."

    show yumi fexasperatedtalk
    voice "C-12-83.mp3" #Yumi (Kaito)
    sis "I'm just gonna… leave you alone…"

    #exit Yumi stage right

    hide yumi with easeoutright
    "Yumi creeps her way back upstairs."
    
    show black with dissolve
    
    #music lighthearted
    play music lightheartedtheme fadein 1.0
    "It takes a long, painful while for Beepy to get the twins to settle down - but soon enough, the excitement dies."
    show beepy neutral:
        align (0.05, 1.0)
    hide bubble
    hide mami

    
    "Honestly, all that energy has me worn out to the point of exhaustion."
    "Still, Beepy {i}did{/i} put in all that effort to bring her friends over, so…"
    "The least I can do is get to know them."
    hide black with dissolve


    voice "C-12-84.mp3" #Makoto (Reece Bridger)
    pro "Alright… lemme see if I can get this straight."

    #enter Lucy stage left, show Lucy pensive
    show lucy neutral with easeinright:
            align (0.4, 1.0)
            
    voice "C-12-85.mp3" #Makoto (Reece Bridger)
    pro "You're Lucifer, a demon associated with Pride, otherwise known as Lucy."

    show lucy smile

    voice "C-12-86.mp3" #Lucy (Vivi)
    lu "Y-Yes, that's right… It's nice to meet you."

    "I had thought a demon of pride would have been more arrogant, but she's awfully nice for some reason."
    "I guess you have to be when your self-confidence is as low as her's."

    show bubble smile with easeinright:
            align (0.7, 1.0)
    show mami scowl with easeinright:
            align (0.95, 1.0)

    voice "C-12-87.mp3" #Makoto (Reece Bridger)
    pro "And you two are identical twins."
    
    show mami stoic
    "My eyes survey the light-blue demon."
    
    voice "C-12-88.mp3" #Makoto (Reece Bridger)
    pro "Let's see, you are… Beelzebub?"

    #show Mami angry

    show mami shoutvein
    voice "C-12-89.mp3" #Mami 
    mm "I'm {b}Mammon,{/b} you idiot!"
    
    show lucy neutral
    show bubble smileclosed
    show mami scowlclosed
    show beepy smile
    voice "C-12-90.mp3" #Makoto (Reece Bridger)
    pro "R-Right, right, sorry… I'll try to remember next time"

    #show Mami pouting

    show mami shout
    voice "C-12-91.mp3" #Mami 
    mm "Humph! You'd better!"
    
    show beepy neutral
    show mami lecture
    voice "C-12-92.mp3" #Mami 
    mm "In fact, don't even bother with Mammon. Just call me Mami, got it?"
    
    show mami scowl
    voice "C-12-93.mp3" #Makoto (Reece Bridger)
    pro "Whatever you say…"

    "She's awfully pushy - completely spoiled, by the sound of it."
    "I guess it's to be expected from a demon of greed."

    show bubble smile
    voice "C-12-94.mp3" #Makoto (Reece Bridger)
    pro "So then, that makes {i}you{/i} Beelzebub, right?"
    
    show bubble bigsmileclosedtalk
    voice "C-12-95.mp3" #Bubble 
    bb "Yup yup, that's me, Beelzebub of Gluttony~! But you can just call me Bubble! *Giggle*"

    #show Bubble smiling
    play sound "sfx/Flourish.mp3"

    show bubble bigsmiletalk
    voice "C-12-96.mp3" #Bubble 
    bb "Nice to meetcha!"
    
    voice "C-12-97.mp3" #Makoto (Reece Bridger)
    pro "Ah… likewise."

    "Her cheerfulness is extremely infectious… Perhaps even more-so than the Bubonic Plague."
    "It's hard to believe the two of them are even identical - especially when they squabble all the time."

    show bubble happytalk
    voice "C-12-98.mp3" #Bubble 
    bb "And you're Makoto, riiiight~?"
    
    #music cut
    stop music fadeout 1.0
    voice "C-12-99.mp3" #Makoto (Reece Bridger)
    pro "I-I am {i}not{/i} Makoto, I…"

    show bubble surprise
    show mami neutral
    show lucy neutraltalk
    show beepy eyebrow
    #music dark chuuni
    play music darkchuunitheme fadein 1.0
    "Who does this little girl think she is, ignoring my demonic heritage!?"
    "Such an outrage will not stand… I must tell her who I really am to strike some fear into her heart!"
    "Feeling my willpower return, I strike a pose and begin my Satanic monologue."

    voice "C-12-100.mp3" #Makoto (Reece Bridger)
    pro "I am Sebastian Wolfgang IV, supreme leader of evil and all-powerful commander of the dark arts!"
    
    voice "C-12-101.mp3" #Makoto (Reece Bridger)
    pro "Hear me, o demons from the underworld, you shall serve as my vassals and grant me the power I need to begin my conquest!"

    #enter Lucy stage left, enter Beepy stage right
    #show Lucy concerned, show Mami confused

    "I unleash my inner persona onto the unsuspecting masses, hoping to exude my dominance over them."
    
    play sound "sfx/Downer.mp3"
    
    #music cut
    stop music fadeout 1.0
    show lucy angst
    show mami smugclosed
    show beepy angry
    show bubble xd
    "...They are not impressed in the slightest."

    #music hijinks
    play music shenanigansthemeintro fadein 1.0
    queue music shenaniganstheme
    voice "C-12-102.mp3" #Mami 
    show mami smugcomment
    mm "...Oh my God."
    
    show mami smugclosed
    show lucy frowntalk
    voice "C-12-103.mp3" #Lucy (Vivi)
    lu "I-It's worse than I thought…"
    
    show bubble xdlaugh
    show lucy angst
    voice "C-12-104.mp3" #Bubble 
    bb "Nyahahaha~! You sure are funny, Makoto!"
    
    show beepy angryclosed
    #voice "C-12-105.mp3" #Beepy (Hikari)
    bp "Not this again…"
    
    voice "C-12-106.mp3" #Makoto (Reece Bridger)
    pro "Wh-What's with that reaction!? This is who I really am!"
    
    voice "C-12-107.mp3" #Makoto (Reece Bridger)
    pro "I'm a dark overlord sent from the furthest reaches of Hell to rule over all the worthless maggots in this realm!"

    #show Mami annoyed

    show mami angrysmiletalk
    voice "C-12-108.mp3" #Mami 
    mm "You're a real loser is what you are."
    
    show mami smirk
    show bubble sadsmile
    
    voice "C-12-109.mp3" #Makoto (Reece Bridger)
    pro "God, lay off already! Do you even know what I'm dealing with right now!?"

    show beepy angry
    show lucy serioustalk
    #music cut
    stop music fadeout 1.0

    voice "C-12-110.mp3" #Lucy (Vivi)
    lu "Actually… we do."
    
    voice "C-12-111.mp3" #Lucy (Vivi)
    lu "You see, Beepy told us everything that happened this morning…"
    
    show beepy neutral
    
    #music calm
    play music calmtrack fadein 1.0
    show lucy neutraltalk
    voice "C-12-112.mp3" #Lucy (Vivi)
    lu "You were challenged to… a-a \"duel\" by that other girl, Misaki."
    
    show lucy frowntalk
    voice "C-12-113.mp3" #Lucy (Vivi)
    lu "A-And our leader is with her, too…"
    
    show lucy neutral
    voice "C-12-114.mp3" #Makoto (Reece Bridger)
    pro "That stupid Satan… I go to all the trouble to summon her and she ends up helping my rival instead! It's unforgivable!"
    
    show beepy neutraltalk
    voice "C-12-115.mp3" #Beepy (Hikari)
    bp "That's kinda her thing, dude. Making other people mad is what she lives for…"

    #show Beepy annoyed

    show beepy neutralclosedtalk
    voice "C-12-116.mp3" #Beepy (Hikari)
    bp "I wouldn't be surprised if that stupid \"idol troupe\" thing was meant to annoy me specifically."

    #show Lucy nervous

    show lucy neutraltalk
    show beepy neutralclosed
    voice "C-12-117.mp3" #Lucy (Vivi)
    lu "Y-Yes, well… When we heard about all that, we thought you needed some help against her."

    #show Lucy smiling

    show lucy smile
    voice "C-12-118.mp3" #Lucy (Vivi)
    lu "S-So you can count on us! We'll help you in any way we can!"
    
    show bubble smileclosed
    voice "C-12-119.mp3" #Makoto (Reece Bridger)
    pro "Wait… for real?"

    #show Mami confident

    show mami angrysmiletalk
    voice "C-12-120.mp3" #Mami 
    mm "Of course! We wouldn't call ourselves Beepy's friends if we couldn't help her out with a pathetic sad-sack like you!"

    #show Mami mischievous

    show mami smugtalk
    voice "C-12-121.mp3" #Mami 
    mm "Though if you ask me, it'd be funnier to watch you squirm."
    
    show mami smug
    voice "C-12-122.mp3" #Makoto (Reece Bridger)
    pro "...I'm not sure how much confidence that's supposed to fill me with."

    "Despite my misgivings, they seem eager to help..."
    "Wait… Could this be what I needed all along?"
    "A legion of demons ready to teach me all the spells and magic that I'll need for my fated showdown… That must be why they're here!"
    "They can impart all the magical knowledge they have onto me, and then I'll be ready to destroy my rival as if crushing an ant underfoot!"
    "This is incredible! I can't possibly think of a better situation to be in right now!"

    #show Lucy nervous

    show lucy neutraltalk
    #music cut
    stop music fadeout 1.0
    voice "C-12-123.mp3" #Lucy (Vivi)
    lu "S-So, um… will you let us help you?"
    
    voice "C-12-124.mp3" #Makoto (Reece Bridger)
    pro "Heheheh… what an absurd question. Of course I will."
    
    show lucy smile
    #music lighthearted
    play music lightheartedtheme fadein 1.0
    voice "C-12-125.mp3" #Makoto (Reece Bridger)
    pro "Your help will be invaluable; I'm confident that this is just what I'll need to show my rival the error of her ways."
    
    show beepy eyebrow
    show lucy angst
    show mami scowl
    show bubble smile
    voice "C-12-126.mp3" #Makoto (Reece Bridger)
    pro "So let's get started! This world has just become ripe for the taking!"

    #show Mami confused

    show mami stammer
    voice "C-12-127.mp3" #Mami 
    mm "Uh… yeah. Whatever you say."
    
    show bubble xdbigshout
    voice "C-12-128.mp3" #Bubble 
    bb "Yayyyy~! Big Bro Makoto's gonna let us help!"
    
    show bubble bigsmileclosedtalk
    voice "C-12-129.mp3" #Bubble 
    bb "We have all sorts of neato ideas to try, too~! Let's get started right away~!"

    #show Mami annoyed

    show mami shout
    voice "C-12-130.mp3" #Mami 
    mm "Not so fast! Aren't you forgetting something?"

    #show Bubble confused

    show bubble frown
    show lucy neutral
    show beepy neutral
    voice "C-12-131.mp3" #Bubble 
    bb "Huh? I'm not forgetting anything… I think."
    
    show mami lecture
    voice "C-12-132.mp3" #Mami 
    mm "We're supposed to go get supplies first, remember?"
    
    voice "C-12-133.mp3" #Makoto (Reece Bridger)
    pro "'S-Supplies…?'"

    #show Bubble smiling

    show mami scowl
    show bubble happytalk
    voice "C-12-134.mp3" #Bubble 
    bb "Oh, yeah, now I remember! We need to go get stuff!"

    #show Bubble drooling

    show bubble angrysmiletalk
    voice "C-12-135.mp3" #Bubble 
    bb "Including food! Lots and lots and {b}lots{/b} of food~!"
    
    voice "C-12-136.mp3" #Makoto (Reece Bridger)
    pro "H-Hold on a minute, what supplies?"
    
    show lucy frowntalk
    voice "C-12-137.mp3" #Lucy (Vivi)
    lu "O-Oh, um… we need lots of things before we can start helping you out…"
    
    show lucy lilcry
    voice "C-12-138.mp3" #Lucy (Vivi)
    lu "Beepy dragged us away so suddenly, we didn't bring a whole lot with us… S-Sorry about that."
    
    show beepy neutraltalk
    voice "C-12-139.mp3" #Beepy (Hikari)
    bp "I had to act fast, so… I ended up overlooking a few details."
    
    show beepy neutral
    voice "C-12-140.mp3" #Makoto (Reece Bridger)
    pro "...With all due respect, you are the last person I'd expect to be anywhere near ‘fast.'"
    
    show beepy dreamworks
    show mami smugcomment
    voice "C-12-141.mp3" #Mami 
    mm "But anyways, that's the situation we're in right now. We can't actually help you unless we have all we need, so…"
    
    show mami smug
    voice "C-12-142.mp3" #Mami 
    mm "You're gonna have to drive us out to the supermarket. Right now."
    
    show mami smirk
    show bubble smileclosed
    voice "C-12-143.mp3" #Makoto (Reece Bridger)
    pro "Wait, {b}what!?{/b}"
    
    show lucy cry
    voice "C-12-144.mp3" #Lucy (Vivi)
    lu "I-I'm sorry about this! It's just… you're the only one who'd know this place better than anyone."
    
    voice "C-12-145.mp3" #Makoto (Reece Bridger)
    pro "Th-That doesn't mean I can take you now!"
    
    show beepy neutral
    voice "C-12-146.mp3" #Makoto (Reece Bridger)
    pro "I don't even have a driver's license! I couldn't drive a car even if I wanted to!"

    #show Bubble angry

    show bubble scowltalk
    voice "C-12-147.mp3" #Bubble 
    bb "But I wanna go get food!"
    
    show bubble xdshout
    voice "C-12-148.mp3" #Bubble 
    bb "Food food food! {b}Gimme foooooooood!{/b}"
    
    voice "C-12-149.mp3" #Makoto (Reece Bridger)
    pro "Gah! Alright, already! We'll go!"
    
    show lucy neutral
    show bubble smileclosed
    voice "C-12-150.mp3" #Makoto (Reece Bridger)
    pro "I just… need to negotiate with my sister about driving us there."

    scene black with dissolve
    #exit all stage left

    #music cut
    stop music fadeout 1.0
    "Managing to wrestle myself away from the crowd, I head up the stairs to talk with Yumi."
    "Never in my millenia-spanning existence did I think I would deign to take my demon servants out to the supermarket, but… so be it."
    "If it will get me one step closer to realizing my dreams of world domination, then I'll try anything."
    "I can only hope my sister is willing to take all of us…"

    jump scene13
