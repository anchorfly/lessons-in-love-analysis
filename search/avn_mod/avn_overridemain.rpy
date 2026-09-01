
# OVERRIDED EVENTS
# main points of choices in the game - call to check the conditions and automatically start the next event
# additionally check the flag of the last known event - when it passed, disable the overriding functions (disable the mod) - the game will not break when updating

label afterschool_avn:

    $ daypart = 2
    
    call avn_stop_check

    if avndisabled == True:
        jump afterschool

    if avnmode == True:
        call avn_main_check(2, 2)

        if _return != "":
            jump expression _return    

    call newday_afterschool_avn
    
    "School passed by without anything interesting happening today."
    "It should be getting dark any minute now, but I still have a little time before I need to head home."

    jump afterschoolmenu



label afterschoolevent_avn:

    $ daypart = 2

    call avn_stop_check

    if avndisabled == True:
        jump afterschoolevent

    if avnmode == True:
        call avn_main_check(2, 3)

        if _return != "":
            jump expression _return    

    call newday_afterschool_avn
    
    "Hmm...I should still be able to fit one more activity in today."

    jump afterschoolmenu



# OVERRIDED EVENTS from script.rpy
# check when update the game

label asmenu_avn:

# AVN Mod
    # menu asmenu:

    call avn_stop_check

    if avndisabled == True:
        jump asmenu

    if avnmode == True:
        call avn_main_check(2, 2, True)

        if _return != "":
            jump expression _return

    menu:
# AVN Mod
        "Go somewhere":
            "Where should I go?"
            menu:
                "Bar":
                    if sarasex == True or saradate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Sana":
                                jump sanasbar
                            "Hang out with Sara" if saradate1 == True:
                                jump sarasbar
                            "Hang out with Yuki" if chapthreeactive == True:
                                jump yukibar
                            "Missionary Sex (Sara)" if sarasex == True and bonus == True:
                                jump saramissionaryanim
                            "Cunnilingus (Sara)" if saralust5 == True and bonus == True:
                                jump saraeatoutanim
                            "Blowjob (Sara)" if saralust10 == True and bonus == True:
                                jump sarabjreplay
                            "Hug Her Tightly (Sara)" if sarasex == True and bonus == False:
                                jump saramissionaryanim
                            "Appreciate Her (Sara)" if saralust5 == True and bonus == False:
                                jump saraeatoutanim
                            "Tightly Hug And Appreciate Her (Sara)" if saralust10 == True and bonus == False:
                                jump sarabjreplay
                    else:
                        jump sanasbar
                "Porn Shop" if bonus == True:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Sitting Doggystyle (Makoto)" if beachwars19 == True:
                                jump makotowatchpornrep
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True and makiblock == False:
                                jump makibjanim
                    else:
                        jump pornshop
                "DVD Store" if bonus == False:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True:
                                jump makibjanim
                    else:
                        jump pornshop
                "Koi Cafe" if day154 == True and mollysad == False:
                    jump mollycafe
                "Tojo Ramen" if day154 == True:
                    jump ramenshop
                "Maid Cafe" if day247 == True:
                    jump utamaid
                "Convenience Store" if norikofirsthall == True and norikoblock == False:
                    jump convenience
                "New Hope Cathedral" if yasufirsthall == True:
                    jump church
                "Dive Bar" if day == 5 and wakanaspecial15 == True and imanidate1 == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Imani":
                            jump imanidive
                        "Rika" if rikaspecial2 == True:
                            jump rikadive
                        "Wakana":
                            jump wakanadive
                "School Dorms":
                    jump dorms
                "Go Back":
                    jump asmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_night

        "Call someone" if use_new_phone_ui == False:
            jump callnight

        "Invite over" if use_new_phone_ui == False:
            jump inviteover

        "Go home and sleep":
            s "I'm feeling kind of tired today...Maybe I'll just head back to the house and go to sleep early?"

            "I decide to walk home."

            scene black
            with dissolve
            stop music fadeout 3.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            if day >= 6:
                jump endofsat



label saturdaymorning_avn:

    $ daypart = 0

    call avn_stop_check

    if avndisabled == True:
        jump saturdaymorning

    #if totaldays > 24:
    #    $ everyday = True
    #    $ clichebath = True
    #    $ amiawake = True
    #    $ firstclass = True
    #    $ sleepover = True
    #    $ day5 = True
    #    $ day7 = True
    #    $ day8 = True
    #    $ day12 = True
    #    $ day14 = True
    #    $ day16 = True
    #    $ day20 = True
    #    $ day21 = True
    #    $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if ((totaldays >= 220) and (day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and
        (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and
        (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 16 or (amipoint + amimiss == 16)) and
        (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and
        (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2) and (day == 6)):
            jump day220
    if day == 6 and totaldays >= 370 and day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False:
        jump secondbeach1
    if totaldays >= 464 and christmastwo20 == True and day == 6 and mayafestival1 == False:
        jump mayafestival1
    if utamaid25p2 == True and day == 6 and iodorm25 == True and iospecial30 == False:
        jump iospecial30
    if makotodorm55p2 == True and nodoka_love >= 30 and norikodorm30 == True and tsubasaspecial20 == True and day == 6 and nodokaspecial30p1 == False:
        jump nodokaspecial30p1
    if predormwars3 == True and day == 6 and naospecial1 == False:
        jump naospecial1
    if yasudorm30 == True and naospecial3 == True and tsubasaspecial20 == True and niki_lust >= 5 and amispecial50 == True and mollydate35p2 == True and makihornytrip4 == True and ioarchery35 == True and (harukadate30 == True or harukadate30skip == True) and day == 6 and beachwars1 == False:
        jump beachwars1
    if (amitotal == 32 and ayanetotal == 34 and chikatotal == 28 and chinamitotal == 7 and futabatotal == 34 and harukatotal == 17 and imanitotal == 5 and iototal == 17 and kaoritotal == 11 and
        karintotal == 9 and kirintotal == 23 and makitotal == 13 and makotototal == 30 and mayatotal == 23 and mollytotal == 18 and mikutotal == 26 and naototal == 3 and nikitotal == 10 and nodokatotal == 14 and
        norikototal == 15 and osakototal == 4 and otohatotal == 12 and rikatotal == 3 and rintotal == 27 and sanatotal == 26 and saratotal == 13 and toukatotal == 13 and tsubasatotal == 5 and tsukasatotal == 2 and
        tsuneyototal == 17 and utatotal == 17 and wakanatotal == 7 and yasutotal == 13 and yukitotal == 7 and yumitotal == 23 and (chap1point + chap2point + chap3point + chap3miss == 284) and (happypoint + happymiss == 16) and day == 6):
            jump halloweenfour1

    # scene bedroom_day
    # with dissolve2

    # "{i}[totaldays] Days have passed...{/i}"

    if totaldays >= 24 and day24 == False:
        call newday_saturdaymorning_avn #AVN Mod
        jump day24
    if totaldays >= 60 and day56 == True and aminew1 == True and aminew2 == False:
        call newday_saturdaymorning_avn #AVN Mod
        jump aminew2
    if totaldays >= 80 and day72 == True and day80 == False:
        call newday_saturdaymorning_avn #AVN Mod
        jump day80
    if totaldays >= 102 and day == 7 and day96 == True and mayadorm15 == True and letterttrack == True and howifeeltrack == True and day102 == False:
        call newday_saturdaymorning_avn #AVN Mod
        jump day102
    if totaldays >= 174 and day154 == True and amidorm15 == True and futabadorm15 == True and day79 == True and makotonew3 == True and kirindate1 == True and ramen1 == True and mollydorm10 == True and rindorm25 == True and bar10 == True and day == 6 and beachvacation1 == False:
        call newday_saturdaymorning_avn #AVN Mod
        jump beachvacation1
    # else:
    #     "I wake up to sunlight pouring in through the window."

    call avn_stop_check

    if avndisabled == True:
        jump saturdaymorning

    if avnmode == True:
        call avn_main_check(0)

        if _return != "":
            jump expression _return    

    call newday_saturdaymorning_avn
   
    "I wake up to sunlight pouring in through the window."
    "What should I do today?"

    jump satmorningmenu



label satmorningmenu_avn:

# AVN Mod
    # menu satmorningmenu:

    call avn_stop_check

    if avndisabled == True:
        jump satmorningmenu

    if avnmode == True:
        call avn_main_check(0, 0, True)

        if _return != "":
            jump expression _return

    menu:
# AVN Mod
        "Go somewhere":
            "Where should I go?"
            menu:
                "Archery Range" if chapthreeactive == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Kirin":
                            jump kirinarchery
                        "Touka":
                            jump toukaarchery
                        "Uta":
                            jump utaarchery
                "Koi Cafe" if firsttimeamisroom == True:
                    if harukadate1 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Rin":
                                jump cafe
                            "Haruka":
                                if harukafirstlust == True:
                                    "What do I want to do?"
                                    menu:
                                        "Hang out":
                                            jump harukacafe
                                        "Quickie (Doggystyle)" if bonus == True:
                                            jump harukacafedogrep
                                        "Hug Really Quickly" if bonus == False:
                                            jump harukacafedogrep
                                else:
                                    jump harukacafe
                    else:
                        jump cafe
                "Library" if firsttimeamisroom == True:
                    jump library
                "Pool" if chapthreeactive == True:
                    jump mikupool
                "Soccer field" if firsttimeamisroom == True and chapthreeactive == False:
                    if soccer20 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Miku":
                                jump soccerfield
                            "Karin":
                                jump soccerfieldkarin
                            "Kirin":
                                jump soccerfieldkirin
                    else:
                        jump soccerfield
                "Ami's Room" if christmas7 == False:
                    jump amisroom
                "Maid Cafe" if christmas7 == True:
                    jump amimaidhub
                "Park" if day288 == True:
                    if otohadorm1 == False:
                        "I should make sure Otoha is settled into the dorm first before visiting her at the park."
                        jump satmorningmenu
                    else:
                        jump otohapark
                "Streets" if day304 == True and chapthreeactive == False:
                    jump toukastreets
                "New Hope Cathedral" if buckettoken == True and day == 7:
                    jump bucketscene
                "=D" if swimming == True:
                    jump swimming
                "Go Back":
                    jump satmorningmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_morning

        "Call someone" if use_new_phone_ui == False:
            jump callmorning

        "Use the computer":
            jump computer

        "Wait until afternoon" if firsttimeshrine == True:
            s "It's still too early to do anything...I'll just sit around for a few hours or something."

            scene black
            with dissolve
            stop music fadeout 3.0

            "........."
            "......"
            "..."

            jump saturdayafternoon



label saturdayafternoon_avn:

    $ daypart = 1

    call avn_stop_check

    if avndisabled == True:
        jump saturdayafternoon

if totaldays >= 38 and firsttimepornshop == True and day36 == True and day38 == False:
    jump day38
else:
    
    if avnmode == True:
        call avn_main_check(1)

        if _return != "":
            jump expression _return    

    "Now what should I do?"

    jump satafternoonmenu



label saturdaynight_avn:

    $ daypart = 2

    call avn_stop_check

    if avndisabled == True:
        jump saturdaynight

if totaldays >= 130 and day128 == True and day > 5 and day130 == False:
    jump day130
if totaldays >= 344 and day340 == True and amiinvite3 == True and day == 6 and day344 == False:
    jump day344
if ayane_love >= 55 and beachwars19 == True and day == 6 and ayanespecial55 == False:
    jump ayanespecial55
if ayane_love >= 55 and ayanebonus1 == True and day == 6 and ayanebonus2 == False:
    jump ayanebonus2
if imani_love >= 15 and imanidate15p2 == True and imanispecial15 == False:
    jump imanispecial15
else:

    if avnmode == True:
        call avn_main_check(2, 1)

        if _return != "":
            jump expression _return    

    "It's late, but I should be able to fit one more thing in today..."
    "What should I do now?"

    jump satnightmenu





# OVERRIDED EVENTS from senseiquest.rpy
# check when update the game

label gameworldmainhub_avn:

# AVN Mod
    # menu gameworldmainhub:
    menu:
# AVN Mod
        "Fields of Despair":
            jump fieldsofdespair
        "Sea of Stairs" if stairmap == True and plantorb == False:
            jump seaofstairs
        "Bedlehem" if bedmap == True and wormorb == False:
            jump bedlehem
        "Palace of the Fist" if fistmap == True and fistorb == False:
            jump palaceofthefist
        "Unholy Cathedral" if clockmap == True and redorb == False:
            jump unholycathedral
        "Developer Island" if ancmap1 == True and ancmap2 == True and fredisdead == False:
            jump developerisland
        "Traveler’s Tavern":
            jump travelerstavern
        "Roadside Merchant":
            jump roadsidemerchant
        "Meowri’s House" if fistorb and redorb and wormorb and plantorb == True:
            "{i}This is the point of no return. Do you still wish to proceed?{/i}"

            s "Wow, an actual helpful tip for once."

            "{i}Do you wish to proceed or not?{/i}"

            menu:
                "Summon the final boss":
                    $ renpy.end_replay()
                    $ halloweenfive7 = True

                    jump endofgameworld
                "Continue exploring":
                    s "I have a few loose ends to tie up first..."

                    jump gameworldmainhub

# AVN Mod
        "AUTO MOD HINT: Buy all items" if not _in_replay and avnmode == True:
            menu:
                "Buy all items":
                    jump avn_buy_all_items
                "Continue exploring":
                    jump gameworldmainhub
# AVN Mod




label avn_buy_all_items:
    
    if stairmap == False:
        play sound "winner.mp3"
        "{i}Quest accepted — Sea of Stairs!{/i}"
        $ stairmap = True
    
    if bedmap == False:
        play sound "winner.mp3"
        "{i}Quest accepted — Bedlehem!{/i}"
        $ bedmap = True

    if fistmap == False:
        play sound "winner.mp3"
        "{i}Quest accepted — Palace of the Fist!{/i}"
        $ fistmap = True

    if clockmap == False:
        play sound "winner.mp3"
        "{i}Quest accepted — Unholy Cathedral!{/i}"
        $ clockmap = True

    if venomspit == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Venom Spit!{/b}{/i}"
        $ venomspit = True

    if bananablast == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Banana Blast!{/b}{/i}"
        $ bananablast = True

    if bubblebeam == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Bubble Beam!{/b}{/i}"
        $ bubblebeam = True

    if sanitize == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Sanitize!{/b}{/i}"
        $ sanitize = True

    if fertilize == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Fertilize!{/b}{/i}"
        $ fertilize = True

    if saltspray == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Salt Spray!{/b}{/i}"
        $ saltspray = True

    if fireball == False:
        play sound "winner.mp3"
        "{i}Sensei has learned {b}Fire Ball!{/b}{/i}"
        $ fireball = True

    if ancmap1 == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained the first piece of an ancient map!{/i}"
        $ ancmap1 = True

    if swordofhope == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained the {b}Sword of Hope!{/b}{/i}"
        $ swordofhope = True

    if shieldofresistance == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained the {b}Shield of Resistance!{/b}{/i}"
        $ shieldofresistance = True

    if bootsofforgiveness == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained the {b}Boots of Forgiveness!{/b}{/i}"
        $ bootsofforgiveness = True

    if steelbucket == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained a {b}Steel Bucket!{/b}{/i}"
        $ steelbucket = True

    if blowtorch == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained a {b}Blowtorch!{/b}{/i}"
        $ blowtorch = True

    if massageoil == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained some {b}Massage Oil!{/b}{/i}"
        $ massageoil = True

    if ancmap2 == False:
        play sound "winner.mp3"
        "{i}Sensei has obtained the second piece of an ancient map!{/i}"
        $ ancmap2 = True

    if nyaorifit == False:
        play sound "winner.mp3"
        "{i}A new profile outfit for Kaori has been unlocked!{/i}"
        $ nyaorifit = True

    if nyaofit == False:
        play sound "winner.mp3"
        "{i}A new profile outfit for Nao-chan has been unlocked!{/i}"
        $ nyaofit = True

    "Continue exploring ..."
    jump gameworldmainhub





# OVERRIDED EVENTS from DormEvents.rpy
# check when update the game

label amidormgen_avn:
    play sound "knock.mp3"

    s "Hey, Ami. Are you in there?"
    a "Mhm! Come in, Sensei!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

# AVN Mod
    # scene amidormgen
    # with dissolve
    if springtime19 == True:    # 0.37 
        scene amidormgen with dissolve
    elif chapthree1 == True:    # 0.25
        image amidormgen_avn35 = "avn_mod/Images/amidormgen_035.webp"
        scene amidormgen_avn35 with dissolve
    else:
        image amidormgen_avn24 = "avn_mod/Images/amidormgen_024.webp"
        scene amidormgen_avn24 with dissolve
# AVN Mod

    "Ami lets me in and the two of us hang out in her room for a few hours."
    "She coerces me into watching some girly anime with her and gets mad whenever I ask a question."

    if day < 4:
        "After a while, she tells me that she has plans with Maya tonight and that we can't hang out for much longer."
        "Despite that, we wind up watching a few more episodes until Ami's phone blows up with 'Where are you?' texts."

        scene black
        with dissolve

        "Being the exceptional legal guardian I am, I walk her to the park to meet up with Maya and company and begin a very boring trek home..."

        $ ami_love += 1
        stop music fadeout 3.0

        "{i}Ami's affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if chap4active == True:
            if day >= 6:
                jump endofsatch4
            else:
                jump endofweekdaych4
        else:
            if day < 6:
                jump endofweekday
            else:
                jump endofsat


    else:
        "After a while, the two of us begin to get hungry and decide that we should probably continue this at home."
        "Since Ami isn't staying at the dorm tonight, we walk back together and stop at a convenience store along the way."
        "I get talked into buying her a disgusting amount of candy and, before I know it, we are skipping dinner and eating junk food."

        scene black
        with dissolve

        "But hey...At least I got to spend some quality time with my [niece]."
        "I can't ask for much more than that..."

        $ ami_love += 1
        stop music fadeout 3.0

        "{i}Ami's affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if chap4active == True:
            if day >= 6:
                jump endofsatch4
            else:
                jump endofweekdaych4
        else:
            if day < 6:
                jump endofweekday
            else:
                jump endofsat



label ayanedormgen_avn:
    play sound "knock.mp3"

    "..."

    ay "Come in!"

    scene black
    with dissolve
# AVN Mod
    # scene ayanedormgen
    # with dissolve
    if halloweenfive17 == True:    # 0.45 
        scene ayanedormgen with dissolve
    else:
        image ayanedormgen_avn44 = "avn_mod/Images/ayanedormgen_044.webp"
        scene ayanedormgen_avn44 with dissolve
# AVN Mod

    "Ayane and I spend the night hanging out in her dorm."
    "She proceeds to tell me all about the 'master plan' she's made for our lives together and I decide to
    go along with it for the sake of conversation."
    "To be honest, there's no way I'm ready to start seriously talking about the future right now."
    "But she looks so happy whenever {i}she{/i} does that it would be borderline painful to stop her..."

    $ ayane_love += 1
    stop music fadeout 5.0

    scene black
    with dissolve

    "{i}Ayane's affection has increased to [ayane_love]!{/i}"

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label chikadormgen_avn:

    play sound "knock.mp3"

    "..."
    c "Come in!"

# AVN Mod
    # scene chikadormgen
    # with fade
    if springtime1 == True:     # 0.36
        scene chikadormgen with fade
    elif chapthree1 == True:    # 0.25
        image chikadormgen_avn35 = "avn_mod/Images/chikadormgen_035.webp"
        scene chikadormgen_avn35 with fade
    else:
        image chikadormgen_avn24 = "avn_mod/Images/chikadormgen_024.webp"
        scene chikadormgen_avn24 with fade
# AVN Mod

    "Chika and I spend our free time hanging out in her room."
    "We watch a few TV shows and I listen to her ramble on about how she's tired of working at the mall and
    wants to start a business or something."
    "But in order to start a business, you need money. And Chika seems to be using the money she earns on
    something else."
    "It gets late pretty quickly and the two of us decide that it would be best if I head back before Yumi gets home."

    scene black
    with dissolve
    $ chika_love += 1
    stop music fadeout 5.0

    "I can't help but feel a bit upset that we didn't get to spend more time together..."
    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label futabadorm6to9_avn:
    play sound "knock.mp3"

    "..."

    f "Come in!"

    play sound "dooropen.mp3"

# AVN Mod
    # scene futabadormgen
    # with fade
    if chapthree1 == True:    # 0.25
        scene futabadormgen with fade
    else:
        image futabadormgen_avn24 = "avn_mod/Images/futabadormgen_024.webp"
        scene futabadormgen_avn24 with fade
# AVN Mod

    "Futaba lets me in and the two of us spend some time together."
    "Apparently, she was planning on spending the night studying."
    "I feel kind of bad for interrupting her, so I decide to help her out to the best of my ability."
    "It never ceases to amaze me how diligent and dedicated she is when it comes to[school]."
    "I’m glad that she's able to stay motivated despite her lack of confidence in herself..."

    scene black
    with dissolve

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label makotodormgen_avn:
    play sound "knock.mp3"

    s "Hey, Makoto. Are you free right now?"
    mak "Sensei? Of course. Come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

# AVN Mod
    # scene makotodormgen
    # with dissolve
    if tsuneyospring8 == True:    # 0.60
        scene makotodormgen with dissolve
    else:
        image makotodormgen_avn24 = "avn_mod/Images/makotodormgen_059.webp"
        scene makotodormgen_avn24 with dissolve

# AVN Mod

    "Makoto invites me in and tries to lecture me on the importance of whatever weird subject she's studying tonight."

    if bonus == True:
        "I get fed up after several minutes and wind up telling her that I won't recommend her to a good[school] unless she chills out."
        "She obliges and we get on to talking about work and how stressed she is having to balance[school] with...porn."
        "It sounds weird to say it like that, but it's clear to see that she actually is getting a little run-down as the days go by."
    else:
        "I swear, sometimes it's like this girl doesn't realize {i}I{/i} am the teacher. I should be lecturing {i}her.{/i}"

    scene black
    with dissolve

    "Eventually, it comes time for me to go as she has yet another late shift at her parents' shop."
    "I walk her to the bus stop and the two of us say our goodbyes."
    "I really do hope that she's able to find time to relax soon..."

    $ makoto_love += 1
    stop music fadeout 3.0

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label mikudormgen_avn:
    play sound "knock.mp3"

    s "Hey, Miku. What are you doing right now?"
    mi "A whole lotta nothin'! Come talk to me about stuff!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

# AVN Mod
    # scene mikudormgen
    # with dissolve
    if christmalloween6 == True:    # 0.54
        scene mikudormgen with dissolve
    elif chapthree1 == True:        # 0.25
        image mikudormgen_avn53 = "avn_mod/Images/mikudormgen_053.webp"
        scene mikudormgen_avn53 with dissolve
    else:
        image mikudormgen_avn24 = "avn_mod/Images/mikudormgen_024.webp"
        scene mikudormgen_avn24 with dissolve
# AVN Mod

    "Miku lets me into the room and the two of us proceed to 'talk about stuff.'"
    if chapthree8 == False:
        "We go through the usual routine of her rambling on about soccer and other drama that has been going on with the team while I..."
    else:
        "We go through the usual routine of her rambling on about swimming and other drama that has been going on with the team while I..."

    "Well, I just do my best to keep up...which is a lot harder than you might expect."
    "Miku is like a ball of lightning constantly ricocheting off of everything in its path."
    "And don't get me wrong, I like being a lightning rod just as much as any guy would, but-"
    "Well, let's just say I wouldn't mind if she slowed down every once in a while."

    scene black
    with dissolve

    "We wind up playing some card game that Miku made up for a couple hours until Makoto tells her she's on the way home."
    "Strange...it feels like I just got here. It's crazy how quickly time flies when I'm with Miku."
    "But, yet again, it might just be that time is trying to catch up to her..."

    $ miku_love += 1
    stop music fadeout 3.0

    "{i}Miku's affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat
            


label rindorm6to9_avn:
    play sound "knock.mp3"

    "..."

    r "Come in!"

    play sound "dooropen.mp3"

# AVN Mod
    # scene rindormgen
    # with fade
    if christmalloween6 == True:    # 0.54
        scene rindormgen with fade
    elif springtime1 == True:       # 0.36
        image rindormgen_avn52 = "avn_mod/Images/rindormgen_052.webp"
        scene rindormgen_avn52 with fade
    elif chapthree1 == True:        # 0.25
        image rindormgen_avn35 = "avn_mod/Images/rindormgen_035.webp"
        scene rindormgen_avn35 with fade
    elif christmastwo20 == True:    # 0.23
        image rindormgen_avn24 = "avn_mod/Images/rindormgen_024.webp"
        scene rindormgen_avn24 with fade
    else:
        image rindormgen_avn22 = "avn_mod/Images/rindormgen_022.webp"
        scene rindormgen_avn22 with fade
# AVN Mod

    "Rin invites me in again and the two of us kill time together in her room."
    "She shows me some of the music she’s been into lately and a lot of it seems eerily depressing."
    "I’m surprised that someone as cheerful as her listens to things like this, but
    I guess it’s never good to judge a book by its cover."
    "Plus, she collects human skulls so it’s not like she’s exactly “normal.”"
    "Eventually, Futaba sends her a text that she’s on her way back and
    the two of us decide it’s best for me to head out."

    scene black
    with dissolve

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 2.0

    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label sanadormgen_avn:
    play sound "knock.mp3"

    "..."

    sa "Umm...You can come in..."

    scene black
    with dissolve

# AVN Mod
    # scene sanadormgen
    # with dissolve
    if tsuneyospring8 == True:    # 0.60
        scene sanadormgen with dissolve
    if springtime19 == True:    # 0.37 
        image sanadormgen_avn59 = "avn_mod/Images/sanadormgen_059.webp"
        scene sanadormgen_avn59 with dissolve
    else:
        image sanadormgen_avn35 = "avn_mod/Images/sanadormgen_035.webp"
        scene sanadormgen_avn35 with dissolve
# AVN Mod

    "Sana and I spend the night hanging out in her dorm."
    "She seems a little more comfortable in here than she does in the bar."
    "The two of us wind up browsing through a bunch of indie games she has on her Xbox to kill some time with."
    "She eventually decides to load up a multiplayer one and proceeds to mop the floor with me in it."
    "I don't mind losing, though, as long as it means she's having a good time..."

    scene black
    with dissolve

    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana's affection has increased to [sana_love]!{/i}"

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat
            


# OVERRIDED EVENTS from Dorm2Events.rpy
# check when update the game

label mollydormgen_avn:
    play sound "knock.mp3"

    mo "Enter, mortal!"

# AVN Mod
    # scene mollydormgen
    # with dissolve
    if springtime19 == True:    # 0.37 
        scene mollydormgen with dissolve
    else:
        image mollydormgen_avn35 = "avn_mod/Images/mollydormgen_035.webp"
        scene mollydormgen_avn35 with dissolve
# AVN Mod

    "I decide to spend the night hanging out with Molly in her dorm."
    "She spends the entirety of our time together trying to convince me to get into some video game that she likes and will not allow me to change the topic no matter how hard I try."
    "Normally, I'm fine with girls taking the lead in conversations so I don't need to divulge any information about myself-"
    "But I'd at least prefer to understand what it is that my partner is talking about."
    "Regardless, I pretend to be interested because it makes Molly happy. And even if she's exhausting to be around, her mischievous smile always seems to strike energy back into me."

    scene black
    with dissolve

    "Eventually, it begins to get late and I decide to head home before Tsuneyo gets back from the ramen shop."
    "Molly awkwardly lunges forward as if she wants to hug me but then backs off and gives me a military-style salute instead."
    "What a strange girl..."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label nodokadormgen_avn:
    play sound "knock.mp3"

    no "Come in!"

# AVN Mod
    # scene nodokadormgen
    # with fade
    if chapthree1 == True:    # 0.25
        scene nodokadormgen with fade
    else:
        image nodokadormgen_avn22 = "avn_mod/Images/nodokadormgen_022.webp"
        scene nodokadormgen_avn22 with fade
# AVN Mod

    "I decide to spend the night hanging out with Nodoka in her dorm."
    "She makes coffee for the two of us to share and we proceed to sit on her bed, making idle chit chat while listening to melancholic indie rock bleeding out of her smartphone."
    "She says that Otoha would be fine with us borrowing one of her speakers or amps and playing it through there-"
    "But then states that there's something magical about the tinge of distortion that accompanies music when streamed through the same devices we use to speak to our loved ones."
    "For those of us that have any loved ones, I mean."
    "I can't help but feel like this won't change much for her or myself."
    "Nonetheless, it changes nothing."
    "The music drags on."

    scene black
    with dissolve

    "Despite Nodoka showing no signs of growing tired, I realize I'm unable to stick around any longer without the fear of passing out."
    "And if I pass out in here, I strongly believe that she might conduct experiments on me for the purpose of her own personal {i}research{/i}."
    "I am not a lab rat. And I can get home without having to traverse a maze."
    "So I do just that and leave her behind."
    "I don't know what she does after that."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label otohadormgen_avn:
    play sound "knock.mp3"

    o "Come in!"

# AVN Mod
    # scene otohadormgen
    # with fade
    if springtime19 == True:    # 0.37 
        scene otohadormgen with fade
    elif slumberreset5 == True:  # 0.30
        image otohadormgen_avn35 = "avn_mod/Images/otohadormgen_035.webp"
        scene otohadormgen_avn35 with fade
    else:
        image otohadormgen_avn27 = "avn_mod/Images/otohadormgen_027.webp"
        scene otohadormgen_avn27 with fade
# AVN Mod

    "I decide to spend the night hanging out with Otoha in her room."
    "Without much for the two of us to do around here, I manage to coerce her into playing a few songs for me."
    "She's a bit bashful about it at first since it's apparently weird to just play and sing for one guy in her room."
    "I get that. It definitely is weird."
    "But we manage to counteract the discomfort by eighty-sixing the vocals and just maintaining different sorts of conversations while she strums away."
    "We talk about all sorts of things, none of them being noteworthy, as the sun is slowly overtaken by the moon."
    "Before we know it, it's almost midnight."

    scene black
    with dissolve

    "I try to get Otoha to play an encore for me, {i}with{/i} vocals this time-"
    "But she promptly kicks me out of the room and tells me I'll need to come see her perform elsewhere if I want a real show."
    "It's fine, though."
    "I'm perfectly content for what I {i}did{/i} get to see."
    "Because I realize that no one else will ever see it."
    "And exclusivity is one of my favorite things in the world when I am the one benefiting from it."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label toukadormgen_avn:
    play sound "knock.mp3"

    to "Come in!"

# AVN Mod
    # scene toukadormgen
    # with fade
    if springtime19 == True:    # 0.37 
        scene toukadormgen with fade
    else:
        image toukadormgen_avn35 = "avn_mod/Images/toukadormgen_035.webp"
        scene toukadormgen_avn35 with fade
# AVN Mod

    "I decide to spend the night hanging out in the dorm with Touka."
    "Despite the place being light years beneath her standards, she doesn't particularly seem to {i}hate{/i} things here."
    "Granted, she spends most of her time either alone or on video calls with different instructors to make up for my inadequacy as a teacher-"
    "But she hasn't asked for a transfer or gotten me fired yet, so that is a clear plus."

    scene black
    with dissolve

    "Eventually, she moves on to talking about her family's business and I can't help but begin to lose interest."
    "Her cuteness may get her far in life, and her great wealth may get her even further-"
    "But it will not get her to the point where she can talk about boring stuff without risking my interest."
    "And, obviously, I need to be the center of her affinities because this is a world made for me."

    if bonus == True:
        "I convince Touka to leave her family and become my sex slave. She obliges and, within moments, we are naked."
    else:
        "I convince Touka to leave her family and open up an Arby's with me."

    "Just kidding."
    "I never convince her to do any of that and, instead, decide to just head home."
    "But at least the two of us managed to get a little closer."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat



label yasudormgen_avn:
    play sound "knock.mp3"

    ya "Come in!"

# AVN Mod
    # scene yasudormgen
    # with fade
    if christmasfive1 == True:    # 0.46
        scene yasudormgen with fade
    elif springtime19 == True:    # 0.37 
        image yasudormgen_avn45 = "avn_mod/Images/yasudormgen_037.webp"
        scene yasudormgen_avn45 with fade
    else:
        image yasudormgen_avn35 = "avn_mod/Images/yasudormgen_035.webp"
        scene yasudormgen_avn35 with fade
# AVN Mod

    "I decide to spend the night hanging out in the dark with Yasu."
    "I ask her to turn the lights on because I feel incredibly uncomfortable just watching her stand there smiling, but she refuses."
    "Apparently, even artificial light stings her eyes and it isn't just the sun that manages to do that."
    "My discomfort grows, but is quelled by the fact that, unlike some of the other residents of this dorm, she does not possess any weapons."
    "That being said, I absolutely would not be surprised if there were some weird religious ritual tools tucked away under her bed or something like that."

    scene black
    with dissolve

    "I make it through the night without dying, which is a thing a lot of unfortunate people out there aren't able to say."
    "Yasu probably makes it through the night without dying as well, but I can't say that definitively as I'm not there to watch her fall asleep."
    "For all I know, she could be sacrificing herself right now in the name of her god."
    "But I'm just going to assume that doesn't happen and hopefully run into her again tomorrow."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat




# OVERRIDED EVENTS from chap4hub.rpy
# check when update the game

label morningch4_avn:
    
    call avn_stop_check

    if avndisabled == True:
        jump morningch4

    if chap4active == True:
        if day == 4 and chikaspring3 == False:
            jump chikaspring3
        if day == 7 and rinspring2 == True and osakospring1 == False:
            jump osakospring1
        if day == 5 and osakospring2 == True and osakospring3 == False:
            jump osakospring3
        if day == 3 and tsubasa_love >= 5 and chinamispring2 == True and tsubasaspring1 == False:
            jump tsubasaspring1
        if day == 2 and yumispring2 == True and karinspring1 == False:
            jump karinspring1
        if day == 7 and karinspring1 == True and mikuspring1 == False:
            jump mikuspring1
        if day == 3 and karinspring2 == True and mikuspring3 == False:
            jump mikuspring3
        if day == 7 and karinspring2 == True and karinspring3 == False:
            jump karinspring3
        if day == 2 and karinspring3 == True and nikispring1 == True and nikispring2 == False:
            jump nikispring2
        if day == 5 and nikispring2 == True and tsuneyospring3 == True and sportswars1 == False:
            jump sportswars1
        if day == 6 and saracamp2 == True and toukaspring1 == False:
            jump toukaspring1
        if day == 7 and saracamp2 == True and mollyspring1 == False:
            jump mollyspring1
        if day == 7 and toukaspring2 == True and yasuspring1 == False:
            jump yasuspring1
        if day == 6 and yasuspring3 == True and utaspring1 == False:
            jump utaspring1
        if day == 6 and yasuspring3 == True and utaspring2 == True and norikospring2 == True and kirinspring1 == True and iospring2 == True and wakanaspring1 == False:
            jump wakanaspring1
        if day == 7 and imanispring2 == True and utaspring2 == True and beachfive1 == False:
            jump beachfive1
        if (day == 5 and beachfive2 == True and beachfive3 == False and rinspring3 == True) or (day == 5 and beachfive2 == True and beachfive3 == False and harukaspring1miss == True):
            jump beachfive3
        if day == 6 and osakospring4 == True and wakanaspring3 == False:
            jump wakanaspring3
        if day == 6 and beachfive16 == True and yumispring3 == False:
            jump yumispring3
        if day > 5 and chikaspring4 == True and chinamispring3 == False:
            jump chinamispring3
        if day == 5 and mikuspring5 == True and sanaspring4 == True and chinamispring3 == True and wakanaspring4 == True and halloweenfive1 == False:
            jump halloweenfive1
        if day == 5 and halloweenfive17 == True and christmasfive1 == False:
            jump christmasfive1
        if day == 5 and imani_lust >= 5 and chikaspring7 == True and rikaspring4 == True and yumispring6 == True and utaspring5 == True and toukaspring5 == True and tsuneyospring6 == True and dormwarsfive1 == False:
            jump dormwarsfive1
        if day == 6 and mollyinvite2 == True and nodokainvite2 == True and mayaspring3 == True and otohaspring4 == True and nikispring4 == False:
            jump nikispring4
        if day > 5 and amispring3 == True and wakanaspring5 == False:
            jump wakanaspring5
        if day > 5 and wakanaspring5 == True and makotospring3 == False:
            jump makotospring3
        if day == 6 and (saraspring5 == True or saraspring5miss == True) and karinpic1read == True and molly_lust >= 5 and sana_lust >= 5 and noriko_lust >= 5 and futabaspring2 == True and futabalust25 == True and chikaspring5 == True and naospring3 == True and wakanaspring6 == True and makotospring3 == True and beachsix1 == False:
            jump beachsix1
        if day > 5 and makispring5 == True and rinspring7 == False:
            jump rinspring7
        if day < 6 and wakanaspring7 == True and wakanaspring8 == False:
            jump wakanaspring8
        if day < 5 and norikoinvite5 == True and kirinchristmalloween2 == True and kirinspring2 == False:
            jump kirinspring2
        if day == 7 and (amispring5 == True or amispring5miss == True) and nikispring7 == False:
            jump nikispring7
        if day < 5 and iospring8 == True and nikispring8 == True and kaoriinvite2 == True and mikulust5 == True and mikuspring6 == False:
            jump mikuspring6
        if day < 5 and iospring7 == True and mikuspring7 == True and utaspring6 == False:
            jump utaspring6
        if (day == 5 and (chap4point + chap4miss >= 104) and (happypoint + happymiss >= 20) and (yumipoint + yumimiss >= 32) and (chikapoint + chikamiss >= 38) and (ayanepoint + ayanemiss >= 52) and (sanapoint + sanamiss >= 35) and
            (makotopoint + makotomiss >= 39) and (mikupoint + mikumiss >= 34) and (rinpoint + rinmiss >= 37) and (futabapoint + futabamiss >= 40) and (amipoint + amimiss >= 42) and (mayapoint + mayamiss >= 35) and (mollypoint + mollymiss >= 27) and
            (tsuneyopoint + tsuneyomiss >= 26) and  (utapoint + utamiss >= 26) and (iopoint + iomiss >= 26) and (nodokapoint + nodokamiss >= 24) and (otohapoint + otohamiss >= 18) and (toukapoint + toukamiss >= 22) and (yasupoint + yasumiss >= 21) and
            (kirinpoint + kirinmiss >= 31) and (norikopoint + norikomiss >= 24) and (sarapoint + saramiss >= 22) and (harukapoint + harukamiss >= 24) and (kaoripoint + kaorimiss >= 20) and (chinamipoint + chinamimiss >= 15) and
            (karinpoint + karinmiss >= 16) and (makipoint + makimiss >= 21) and (yukipoint + yukimiss >= 16) and (nikipoint + nikimiss >= 19) and (wakanapoint + wakanamiss >= 15) and (osakopoint + osakomiss >= 13) and (tsubasapoint + tsubasamiss >= 12) and
            (tsukasapoint + tsukasamiss >= 9) and (imanipoint + imanimiss >= 13) and (rikapoint + rikamiss >= 11) and (naopoint + naomiss >= 11) and dormwarssix1 == False):
                jump dormwarssix1
        if day == 4 and dormwarssix12 == True and postwarsix1 == False:
            jump postwarsix1
        if day > 5 and futabaspring4 == True and tsubasaspring7 == False:
            jump tsubasaspring7
        if day == 6 and tsukasaspring7 == True and tsukasaspring8 == False:
            jump tsukasaspring8
        if day == 5 and tsuneyospring7 == True and futabaspring4 == True and tsuneyospring8 == False:
            jump tsuneyospring8
        if day == 1 and makotospring5 == True and kirinspring3 == False:
            jump kirinspring3
        if day < 6 and nodokaspring3 == True and ayanespring4 == False:
            jump ayanespring4
        else:

        # AVN Mod
            if avnmode == True:
                call avn_main_check(0, 4)

                if _return != "":
                    jump expression _return
        # AVN Mod

            "{i}[totaldays] Days have passed...{/i}"

            $ v11check()

            scene bedroom_day
            with dissolve2

            "I wake up again."

            s "..."

            scene black
            with dissolve

            "I need to keep myself busy."
            "........."
            "......"
            "..."

            jump ch4morningmenu



label ch4morningmenu_avn:

# AVN Mod
# menu ch4morningmenu:

    call avn_stop_check

    if avndisabled == True:
        jump ch4morningmenu

    if avnmode == True:
        call avn_main_check(0, 4, True)

        if _return != "":
            jump expression _return

menu:
# AVN Mod
    "Go somewhere":
        "Where should I go?"
        menu:
            "Archery Range":
                "Who do I want to spend time with?"
                menu:
                    "Touka" if toukablock == False:
                        jump toukaarchery
                    "Tsuneyo" if senseisad == False:
                        jump tsuneyoarchery
                    "Uta" if senseisad == False and utablock == False:
                        jump utaarchery
            "Koi Cafe" if cafeclosed == False:
                "Who do I want to spend time with?"
                menu:
                    "Rin":
                        jump cafe
                    "Haruka" if senseisad == False or saracamp2 == True:
                        if harukafirstlust == True:
                            "What do I want to do?"
                            menu:
                                "Hang out":
                                    jump harukacafe
                                "Quickie (Doggystyle)" if bonus == True:
                                    jump harukacafedogrep
                        else:
                            jump harukacafe
            "Dojo" if beachfive16 == True and osakospring4 == False and day > 5:
                jump osakodojo
            "Library" if senseisad == False:
                jump library
            "Pool" if senseisad == False or saracamp2 == True:
                jump mikupool
            "Maid Cafe" if senseisad == False and amiblock == False:
                jump amimaidhub
            "Park" if senseisad == False or saracamp2 == True:
                jump otohapark
            "Go Back":
                jump ch4morningmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_morning

    "Call someone" if use_new_phone_ui == False:
        jump callmorning

    "Use the computer":
        jump computer

    "Wait until afternoon":
        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        jump noonch4




label noonch4_avn:
    
    call avn_stop_check

    if avndisabled == True:
        jump noonch4

    if day == 2 and tsuneyospring1 == True and otohaspring1 == False:
        jump otohaspring1
    if day == 6 and nikispring2 == True and tsuneyospring2 == False:
        jump tsuneyospring2
    if day == 6 and norikospring1 == True and kirinspring1 == False:
        jump kirinspring1
    if day == 7 and norikospring1 == True and utaspring1 == True and norikospring2 == False:
        jump norikospring2
    if day == 7 and christmasfive8 == True and tsukasacurious == True and tsukasaspring4 == False:
        jump tsukasaspring4
    if day == 7 and sanainvite2 == True and iospring4 == False:
        jump iospring4
    if day > 5 and harukaspring4 == True and chikaspring5 == False:
        jump chikaspring5
    if day < 6 and christmasfive8 == True and karinspring5 == False:
        jump karinspring5
    if day > 5 and karinspring5 == True and yasuspring4 == False:
        jump yasuspring4
    if day == 5 and dormwarsfive14 == True and ayanespring3 == False:
        jump ayanespring3
    if day < 6 and yukispring5 == True and yumispring8 == False:
        jump yumispring8
    if day > 5 and yumispring8 == True and chikaspring8 == False:
        jump chikaspring8
    if day == 3 and wakanaspring5 == True and wakanaspring6 == False:
        jump wakanaspring6
    if day < 6 and christmalloween6 == True and rikaspring5 == False:
        jump rikaspring5
    if day > 5 and christmalloween6 == True and toukaspring6 == False:
        jump toukaspring6
    if day == 5 and iospring6 == True and rinspring9 == True and iospring8 == False:
        jump iospring8
    if day > 5 and kirinspring2 == True and karinspring7 == False:
        jump karinspring7
    if day > 5 and molly_love >= 40 and utaspring8 == True and mollyspring3 == False:
        jump mollyspring3
    if day < 6 and postwarsix1 == True and futabaspring3 == False:
        jump futabaspring3
    if day > 5 and tsubasaspring7 == True and otohaspring5 == False:
        jump otohaspring5
    if day == 6 and makotospring5 == True and lingeriechoicemaya == True and mayaspring4miss == False and mayaspring4 == False:
        jump mayaspring4
    if day == 7 and makotospring5 == True and mayaspring5 == False:
        jump mayaspring5
    if day == 6 and mayaspring5 == True and kirinspring4miss == False and kirinspring4 == False:
        jump kirinspring4
    else:
    
    # AVN Mod
        if avnmode == True:
            call avn_main_check(1, 4)

            if _return != "":
                jump expression _return  
    # AVN Mod
    
        "What do I want to do?"

        jump ch4noonmenu



label ch4noonmenu_avn:

# AVN Mod
# menu ch4noonmenu:

    call avn_stop_check

    if avndisabled == True:
        jump ch4noonmenu

    if avnmode == True:
        call avn_main_check(0, 4, True)

        if _return != "":
            jump expression _return

menu:
# AVN Mod
    "Go somewhere":
        "Where should I go?"
        menu:
            "City Streets" if senseisad == False:
                jump streets
            "Shrine" if senseisad == False or saracamp2 == True:
                jump shrine
            "Dojo" if senseisad == False:
                jump osakodojo
            "Pond" if tsuneyospring1 == True and yumispring2 == False and day == 7:
                jump yumispring2
            "Bathhouse" if senseisad == False and ioblock == False:
                jump bathhouse
            "Library":
                jump nodokalibrary
            "Maid Cafe" if senseisad == False and chikablock == False:
                jump chikamaid
            "Pool":
                menu:
                    "Ayane":
                        jump ayanepool
                    "Karin" if karinbetter == True:
                        jump karinpool
            "Go Back":
                jump ch4noonmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_afternoon

    "Call someone" if use_new_phone_ui == False:
        jump callafternoon

    "Wait until night" if firsttimeshrine == True:
        s "I'll just...walk around until it starts to get dark, I guess."

        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        jump nightch4




label nightch4_avn:
    
    call avn_stop_check

    if avndisabled == True:
        jump nightch4

    if day == 6 and osakospring3 == True and tsuneyospring1 == False:
        jump tsuneyospring1
    if day == 6 and sportswars20 == True and makicamp1 == False:
        jump makicamp1
    if day == 6 and yasuspring1 == True and yasuspring2 == False:
        jump yasuspring2
    if day == 3 and yasuspring3 == True and utaspring1 == True and iospring2 == True and utaspring2 == False:
        jump utaspring2
    if day == 6 and beachfive16 == True and rikaspring1 == False:
        jump rikaspring1
    if day == 3 and chinamispring3 == True and toukaspring3 == False:
        jump toukaspring3
    if day == 5 and yukispring2 == True and sanaspring4 == False:
        jump sanaspring4
    if day == 6 and sanainvite2 == True and osakospring5 == False:
        jump osakospring5
    if day == 7 and iospring4 == True and iospring5 == False:
        jump iospring5
    if day == 3 and sanainvite2 == True and harukasex == True and harukaspring3 == False:
        jump harukaspring3
    if day == 5 and christmasfive8 == True and tsuneyospring4 == False:
        jump tsuneyospring4
    if day == 6 and christmasfive8 == True and rinspring4 == False:
        jump rinspring4
    if day == 4 and cafeclosed == False and rinspring6 == True and harukaspring4 == False:
        jump harukaspring4
    if chikaspring5 == True and osakospring6 == True and rikaspring3 == False:
        jump rikaspring3
    if day == 7 and toukaspring4 == True and toukaspring5 == False:
        jump toukaspring5
    if day == 3 and nodokathontwo3 == True and ayanespring2 == False:
        jump ayanespring2
    if day == 7 and ayanespring3 == True and yumispring7 == False:
        jump yumispring7
    if day < 6 and saraspring4 == True and saraspring5 == False:
        jump saraspring5
    if (day == 5 and yumispring8 == True and tsubasaspring4 == True and tsubasaspring6 == False) or (day == 5 and yumispring8 == True and tsubasaspring4miss == True and tsubasaspring6 == False):
        jump tsubasaspring6
    if day < 5 and naospring2 == True and naospring3 == False:
        jump naospring3
    if wakana_love >= 40 and osakospring9 == True and makispring3 == True and wakanaspring7 == False:
        jump wakanaspring7
    if day < 6 and yuki_love >= 30 and (mollyspring4 == True or mollyspring4miss == True) and yukispring6 == False:
        jump yukispring6
    if tsukasa_love >= 25 and tsubasaspring8 == True and day < 6 and tsukasaspring7 == False:
        jump tsukasaspring7
    if otoha_love >= 25 and otohaspring6 == True and otohaspring7 == False:
        jump otohaspring7
    if yasu_love >= 30 and day == 1 and tsuneyospring8 == True and yasuspring6 == False:
        jump yasuspring6
    if yasu_love >= 40 and day == 5 and yasuspring6 == True and yasuspring7 == False:
        jump yasuspring7
    if makoto_love >= 60 and day == 5 and tsuneyospring8 == True and makotospring4 == False:
        jump makotospring4
    if day == 6 and makotospring4 == True and makotospring5 == False:
        jump makotospring5
    if day == 3 and harukachristmalloween2 == True and dormwarssixsara1 == True and harukaspring5 == False:
        jump harukaspring5
    else:

    # AVN Mod
        if avnmode == True:
            call avn_main_check(2, 4)

            if _return != "":
                jump expression _return  
    # AVN Mod
    
        "What do I want to do?"

        jump ch4nightmenu



label ch4nightmenu_avn:

# AVN Mod
# menu ch4nightmenu:

    call avn_stop_check

    if avndisabled == True:
        jump ch4nightmenu

    if avnmode == True:
        call avn_main_check(0, 4, True)

        if _return != "":
            jump expression _return

menu:
# AVN Mod
    "Go somewhere":
        "Where should I go?"
        menu:
            "Bar":
                if sarasex == True or saradate1 == True:
                    "What do I want to do?"
                    menu:
                        "Hang out with Sana":
                            jump sanasbar
                        "Hang out with Sara" if (senseisad == False and sarablock == False) or (saracamp2 == True and sarablock == False):
                            jump sarasbar
                        "Hang out with Yuki" if yukiblock == False and senseisad == False or saracamp2 == True and yukiblock == False:
                            jump yukibar
                        "Missionary Sex (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump saramissionaryanim
                        "Cunnilingus (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump saraeatoutanim
                        "Blowjob (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump sarabjreplay
            "Porn Shop" if senseisad == False or saracamp2 == True:
                "What do I want to do?"
                menu:
                    "Hang out with Makoto" if senseisad == False:
                        jump pornshop
                    "Sitting Doggystyle (Makoto)" if beachwars19 == True and senseisad == False:
                        jump makotowatchpornrep
                    "Hang out with Maki":
                        jump pornshopmaki
                    "Blowjob (Maki)" if makibj == True and makiblock == False:
                        jump makibjanim
            "Koi Cafe" if cafeclosed == False and (senseisad == False or mollycamp1 == True):
                jump mollycafe
            "Tojo Ramen" if senseisad == False:
                jump ramenshop
            "Bathhouse" if yasuspring3 == True and day < 6 and iospring1 == False:
                jump iospring1
            "Bathhouse" if iospring1 == True and iospring5 == True and day < 5 and utaspring3 == False:
                jump utaspring3
            "Maid Cafe" if senseisad == False and amiblock == False and utablock == False:
                jump utamaid
            "Convenience Store" if senseisad == False or yasuspring3 == True and norikospring1 == False:
                jump convenience
            "New Hope Cathedral":
                jump church
            "Dive Bar" if (day == 5 and senseisad == False) or (day == 5 and imanispring2 == True):
                "Who do I want to spend time with?"
                menu:
                    "Imani":
                        jump imanidive
                    "Imani but, like...sexually" if christmasimani3 == True:
                        jump imanidivedoggyanim
                    "Osako":
                        jump osakodive
                    "Rika":
                        jump rikadive
                    "Wakana":
                        jump wakanadive
            "Streets" if (yumispring8 == True and kaori_love >= 45 and tsubasaspring4 == True and kaorispring1 == False) or (yumispring8 == True and kaori_love >= 45 and tsubasaspring4miss == True and kaorispring1 == False):
                jump kaorispring1
            "School Dorms" if senseisad == False or mollyspring2 == True:
                jump dormsch4
            "Go Back":
                jump ch4nightmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_night

    "Call someone" if use_new_phone_ui == False:
        jump callnight

    "Invite over" if use_new_phone_ui == False and senseisad == False:
        jump inviteover

    "Go home and sleep":
        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekdaych4
        if day >= 6:
            jump endofsatch4
