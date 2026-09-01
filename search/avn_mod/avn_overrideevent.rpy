# OVERRIDED EVENTS
# used to preset the necessary variables when auto mod is enabled and some additional transitions


label start_avn:

    python:
        i_label = 0
        i_name = 1
        for avn_event in avn_events_ch1:
            if avn_event[i_name] == "generic":
                renpy.game.persistent._seen_ever.pop(avn_event[i_label], None)
        for avn_event in avn_events_ch2:
            if avn_event[i_name] == "generic":
                renpy.game.persistent._seen_ever.pop(avn_event[i_label], None)
        for avn_event in avn_events_ch3:
            if avn_event[i_name] == "generic":
                renpy.game.persistent._seen_ever.pop(avn_event[i_label], None)
        for avn_event in avn_events_ch4:
            if avn_event[i_name] == "generic":
                renpy.game.persistent._seen_ever.pop(avn_event[i_label], None)

    $ if "start" in config.label_overrides: del config.label_overrides["start"]
    jump start



label day79_avn:

    if not _in_replay and avnmode == True and ayane_love <= 2000:
        $ ayane_love +=2000
        $ avn_ayane_love2000 = True

    $ if "day79" in config.label_overrides: del config.label_overrides["day79"]
    jump day79



label day103_avn:

    if not _in_replay and avnmode == True and connecttrack == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!{/i}"
        "..."
        jump everythingisconnected

    $ if "day103" in config.label_overrides: del config.label_overrides["day103"]
    jump day103



label beachvacation1_avn:

    if not _in_replay and avnmode == True:
        if futaba_lust < 10:
            $ futaba_lust = 10
        if ayanedorm10 == True and ayane_lust < 10:
            $ ayane_lust = 10
        if amifingered == True and ami_lust < 10:
            $ ami_lust = 10

    $ if "beachvacation1" in config.label_overrides: del config.label_overrides["beachvacation1"]
    jump beachvacation1



label beachvacation6_avn:

    if not _in_replay and avnmode == True:
        if ayanedorm10 == True and ayane_lust < 10:
            $ ayane_lust = 10
        if amifingered == True and ami_lust < 10:
            $ ami_lust = 10

    $ if "beachvacation6" in config.label_overrides: del config.label_overrides["beachvacation6"]
    jump beachvacation6



label beachvacation10_avn:

    if not _in_replay and avnmode == True:
        if ayanedorm10 == True and ayane_lust < 10:
            $ ayane_lust = 10

    $ if "beachvacation10" in config.label_overrides: del config.label_overrides["beachvacation10"]
    jump beachvacation10



label halloween1_avn:

    if not _in_replay and avnmode == True:
        if sarasex == True and sara_lust < 10:
            $ sara_lust = 10
        if harukasex == True and haruka_lust < 10:
            $ haruka_lust = 10

    $ if "halloween1" in config.label_overrides: del config.label_overrides["halloween1"]
    jump halloween1



label saralust10skip_avn:

    $ if "saralust10skip" in config.label_overrides: del config.label_overrides["saralust10skip"]

    if not _in_replay and avnmode == True:
        if sarasex == True and sara_lust < 10:
            $ sara_lust = 10
            jump saralust10

    jump saralust10skip



label harukalust10skip_avn:

    $ if "harukalust10skip" in config.label_overrides: del config.label_overrides["harukalust10skip"]

    if not _in_replay and avnmode == True:
        if harukasex == True and haruka_lust < 10:
            $ haruka_lust = 10
            jump harukalust10

    jump harukalust10skip



label hoorayanotherreset_avn:

    if not _in_replay and avnmode == True and babyfinches == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!\nHOPE was the right user name.{/i}"
        "..."
        jump babyfinches

    if not _in_replay and avnmode == True:
        if chika_lust < 10:
            $ chika_lust = 10
        if futaba_lust < 10:
            $ futaba_lust = 10

    $ if "hoorayanotherreset" in config.label_overrides: del config.label_overrides["hoorayanotherreset"]
    jump hoorayanotherreset



label chikalust10intro_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 10:
            $ chika_lust = 10
        if futaba_lust < 10:
            $ futaba_lust = 10

    $ if "chikalust10intro" in config.label_overrides: del config.label_overrides["chikalust10intro"]
    jump chikalust10intro



label christmas6_avn:

    if not _in_replay and avnmode == True:
        if futaba_lust < 10:
            $ futaba_lust = 10

    $ if "christmas6" in config.label_overrides: del config.label_overrides["christmas6"]
    jump christmas6



label endofreset3loop_avn:

    if not _in_replay and avnmode == True and lesson1 == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!{/i}"
        "..."
        jump kindergartenclass

    scene bedroom_day

    s "Time to go to work!"

    $ renpy.end_replay()
    $ thirdreset1 = True

    jump thirdreset2



label day264_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nChoosen \"I’m already involved with her\" will miss events later.{/i}"

    $ if "day264" in config.label_overrides: del config.label_overrides["day264"]
    jump day264



label day318_avn:

    if not _in_replay and avnmode == True:
        if ayane_lust < 15:
            $ ayane_lust = 15
        if chika_lust < 15:
            $ chika_lust = 15
        if futaba_lust < 15:
            $ futaba_lust = 15
        if kirin_lust < 15:
            $ kirin_lust = 15

    $ if "day318" in config.label_overrides: del config.label_overrides["day318"]
    jump day318



label dormwar4_avn:

    if not _in_replay and avnmode == True:
        if ayane_lust < 15:
            $ ayane_lust = 15
        if chika_lust < 15:
            $ chika_lust = 15
        if futaba_lust < 15:
            $ futaba_lust = 15
        if kirin_lust < 15:
            $ kirin_lust = 15

    $ if "dormwar4" in config.label_overrides: del config.label_overrides["dormwar4"]
    jump dormwar4



label dormwar9_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 15:
            $ chika_lust = 15
        if futaba_lust < 15:
            $ futaba_lust = 15
    
    $ if "dormwar9" in config.label_overrides: del config.label_overrides["dormwar9"]
    jump dormwar9


label dormwar16_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 15:
            $ chika_lust = 15
    
    $ if "dormwar16" in config.label_overrides: del config.label_overrides["dormwar16"]
    jump dormwar16




label secondbeach1_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 20:
            $ chika_lust = 20
        if kirin_lust < 20:
            $ kirin_lust = 20
        if makoto_lust < 20:
            $ makoto_lust = 20

    $ if "secondbeach1" in config.label_overrides: del config.label_overrides["secondbeach1"]
    jump secondbeach1



label kirinlust20intro_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 20:
            $ chika_lust = 20
        if kirin_lust < 20:
            $ kirin_lust = 20
        if makoto_lust < 20:
            $ makoto_lust = 20

    $ if "kirinlust20intro" in config.label_overrides: del config.label_overrides["kirinlust20intro"]
    jump kirinlust20intro



label chikalust20intro_avn:

    if not _in_replay and avnmode == True:
        if chika_lust < 20:
            $ chika_lust = 20
        if makoto_lust < 20:
            $ makoto_lust = 20

    $ if "chikalust20intro" in config.label_overrides: del config.label_overrides["chikalust20intro"]
    jump chikalust20intro



label makotolust20intro_avn:

    if not _in_replay and avnmode == True:
        if makoto_lust < 20:
            $ makoto_lust = 20

    $ if "makotolust20intro" in config.label_overrides: del config.label_overrides["makotolust20intro"]
    jump makotolust20intro



label fmkx_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nChoosen \"Kill Kirin\" will miss events later.{/i}"

    $ if "fmkx" in config.label_overrides: del config.label_overrides["fmkx"]
    jump fmkx  



label chinamibrx_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nChoosen \"Wait outside\" will miss events later.{/i}"

    $ if "chinamibrx" in config.label_overrides: del config.label_overrides["chinamibrx"]
    jump chinamibrx  



label halloweentwo1_avn:

    if not _in_replay and avnmode == True and amifingered == True and ami_lust < 20:
        $ ami_lust = 20

    $ if "halloweentwo1" in config.label_overrides: del config.label_overrides["halloweentwo1"]
    jump halloweentwo1



label amilust20intro_avn:

    if not _in_replay and avnmode == True and amifingered == True and ami_lust < 20:
        $ ami_lust = 20

    $ if "amilust20intro" in config.label_overrides: del config.label_overrides["amilust20intro"]
    jump amilust20intro
    
        

label christmastwo1_avn:

    if not _in_replay and avnmode == True:
        if ayane_lust < 20:
            $ ayane_lust = 20
        if sarasex == True and sara_lust < 20:
            $ sara_lust = 20
        if harukasex == True and haruka_lust < 20:
            $ haruka_lust = 20
        if kirin_lust < 20:
            $ kirin_lust = 20

    $ if "christmastwo1" in config.label_overrides: del config.label_overrides["christmastwo1"]
    jump christmastwo1


label christmastwo3_avn:

    if not _in_replay and avnmode == True:
        if ayane_lust < 20:
            $ ayane_lust = 20
        if sarasex == True and sara_lust < 20:
            $ sara_lust = 20
        if harukasex == True and haruka_lust < 20:
            $ haruka_lust = 20
        if kirin_lust < 20:
            $ kirin_lust = 20

    $ if "christmastwo3" in config.label_overrides: del config.label_overrides["christmastwo3"]
    jump christmastwo3


label saralust20intro_avn:

    if not _in_replay and avnmode == True:
        if sarasex == True and sara_lust < 20:
            $ sara_lust = 20
        if harukasex == True and haruka_lust < 20:
            $ haruka_lust = 20
        if kirin_lust < 20:
            $ kirin_lust = 20

    $ if "saralust20intro" in config.label_overrides: del config.label_overrides["saralust20intro"]
    jump saralust20intro


label kirinlust202_avn:

    if not _in_replay and avnmode == True:
        if kirin_lust < 20:
            $ kirin_lust = 20

    $ if "kirinlust202" in config.label_overrides: del config.label_overrides["kirinlust202"]
    jump kirinlust202        


label returntosummer3_avn:

    if not _in_replay and avnmode == True and goodboy == True and lamblegs == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!{/i}"
        "..."
        jump specialbonusamiscene

    $ if "returntosummer3" in config.label_overrides: del config.label_overrides["returntosummer3"]
    jump returntosummer3

            

label nodokaspecial15p1_avn:

    if not _in_replay and avnmode == True and makoto_lust < 30:
        $ makoto_lust = 30

    $ if "nodokaspecial15p1" in config.label_overrides: del config.label_overrides["nodokaspecial15p1"]
    jump nodokaspecial15p1
    


label sadgirls1_avn:

    if not _in_replay and avnmode == True and makoto_lust < 30:
        $ makoto_lust = 30

    $ if "sadgirls1" in config.label_overrides: del config.label_overrides["sadgirls1"]
    jump sadgirls1



label sadgirls7_avn:

    if not _in_replay and avnmode == True and makoto_lust < 30:
        $ makoto_lust = 30

    $ if "sadgirls7" in config.label_overrides: del config.label_overrides["sadgirls7"]
    jump sadgirls7



label day344_avn:

    if not _in_replay and avnmode == True and amifingered == True and ami_lust < 15:
        $ ami_lust = 15

    $ if "day344" in config.label_overrides: del config.label_overrides["day344"]
    jump day344



label ayanespecial2_avn:

    if not _in_replay and avnmode == True and amifingered == True and ami_lust < 15:
        $ ami_lust = 15

    $ if "ayanespecial2" in config.label_overrides: del config.label_overrides["ayanespecial2"]
    jump ayanespecial2



label ayanesanabeach3_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nChoosen \"DON’T DO IT\" will miss events later.{/i}"

    $ if "ayanesanabeach3" in config.label_overrides: del config.label_overrides["ayanesanabeach3"]
    jump ayanesanabeach3



label dormwartwo1_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if chika_lust < 25:
            $ chika_lust = 25
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49
        if kirin_lust < 30:
            $ kirin_lust = 30
        if miku_lust < 10:
            $ miku_lust = 10
        if sarasex == True and sara_lust < 25:
            $ sara_lust = 25
        if harukasex == True and haruka_lust < 25:
            $ haruka_lust = 25

    $ if "dormwartwo1" in config.label_overrides: del config.label_overrides["dormwartwo1"]
    jump dormwartwo1



label dormwartwo8_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if chika_lust < 25:
            $ chika_lust = 25
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49
        if kirin_lust < 30:
            $ kirin_lust = 30
        if miku_lust < 10:
            $ miku_lust = 10
        if sarasex == True and sara_lust < 25:
            $ sara_lust = 25
        if harukasex == True and haruka_lust < 25:
            $ haruka_lust = 25

    $ if "dormwartwo8" in config.label_overrides: del config.label_overrides["dormwartwo8"]
    jump dormwartwo8



label harukalust25intro_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if chika_lust < 25:
            $ chika_lust = 25
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49
        if kirin_lust < 30:
            $ kirin_lust = 30
        if miku_lust < 10:
            $ miku_lust = 10
        if sarasex == True and sara_lust < 25:
            $ sara_lust = 25
        if harukasex == True and haruka_lust < 25:
            $ haruka_lust = 25

    $ if "harukalust25intro" in config.label_overrides: del config.label_overrides["harukalust25intro"]
    jump harukalust25intro



label dormwartwo13_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if chika_lust < 25:
            $ chika_lust = 25
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49
        if kirin_lust < 30:
            $ kirin_lust = 30
        if miku_lust < 10:
            $ miku_lust = 10

    $ if "dormwartwo13" in config.label_overrides: del config.label_overrides["dormwartwo13"]
    jump dormwartwo13



label dormwartwo18_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD HINT:\nNot choosen Miku winner will miss events later.{/i}"

    $ if "dormwartwo18" in config.label_overrides: del config.label_overrides["dormwartwo18"]
    jump dormwartwo18



label kirinlust30intro_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49
        if kirin_lust < 30:
            $ kirin_lust = 30
        if miku_lust < 10:
            $ miku_lust = 10

    $ if "kirinlust30intro" in config.label_overrides: del config.label_overrides["kirinlust30intro"]
    jump kirinlust30intro



label beachmas11_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35
        if futaba_lust < 49:
            $ futaba_lust = 49
        if makoto_lust < 49:
            $ makoto_lust = 49

    $ if "beachmas11" in config.label_overrides: del config.label_overrides["beachmas11"]
    jump beachmas11



label amilust35intro_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 35:
            $ ami_lust = 35

    $ if "amilust35intro" in config.label_overrides: del config.label_overrides["amilust35intro"]
    jump amilust35intro



label chikadorm45_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nNot choosen Ayane will miss events later.{/i}"

    $ if "chikadorm45" in config.label_overrides: del config.label_overrides["chikadorm45"]
    jump chikadorm45



label gstriviaround2_avn:

    if not _in_replay and avnmode == True and mothersmilk == False:
        scene black
        "..."
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!\nThe correct answer was a cute puppy.{/i}"
        "..."
        jump mothersmilk

    $ if "gstriviaround2" in config.label_overrides: del config.label_overrides["gstriviaround2"]
    jump gstriviaround2    



label halloweenfour1_avn:
    
    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 60:
            $ ami_lust = 60
        if makoto_lust < 55:
            $ makoto_lust = 55

    $ if "halloweenfour1" in config.label_overrides: del config.label_overrides["halloweenfour1"]
    jump halloweenfour1    



label amilust50intro_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 60:
            $ ami_lust = 60
        if makoto_lust < 55:
            $ makoto_lust = 55

    $ if "amilust50intro" in config.label_overrides: del config.label_overrides["amilust50intro"]
    jump amilust50intro    



label escaperoomfridge_avn:

    if not _in_replay and avnmode == True and escapeshampoo == False:
        "{i}AUTO MOD WARNING:\nTaking the shampoo will miss events later.{/i}"

    $ if "escaperoomfridge" in config.label_overrides: del config.label_overrides["escaperoomfridge"]
    jump escaperoomfridge    



label resetsix2_avn:

    if not _in_replay and avnmode == True and rainking == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!{/i}"
        "..."
        $ rainkingmiss = False
        jump rainking

    $ if "resetsix2" in config.label_overrides: del config.label_overrides["resetsix2"]
    jump resetsix2    



label amilust60intro_avn:

    if not _in_replay and avnmode == True:
        if amifingered == True and ami_lust < 60:
            $ ami_lust = 60
        if makoto_lust < 55:
            $ makoto_lust = 55

    $ if "amilust60intro" in config.label_overrides: del config.label_overrides["amilust60intro"]
    jump amilust60intro



label chinamispring2_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nChoosen Chinami will miss events later.{/i}"

    $ if "chinamispring2" in config.label_overrides: del config.label_overrides["chinamispring2"]
    jump chinamispring2



label sportswars19_avn:

    if not _in_replay and avnmode == True and makoto_lust < 55:
        $ makoto_lust = 55

    $ if "sportswars19" in config.label_overrides: del config.label_overrides["sportswars19"]
    jump sportswars19



label beachfive1_avn:
    
    if not _in_replay and avnmode == True and ayane_lust < 40:
        $ ayane_lust = 40

    $ if "beachfive1" in config.label_overrides: del config.label_overrides["beachfive1"]
    jump beachfive1



label beachfive15_avn:
    
    if not _in_replay and avnmode == True and ayane_lust < 40:
        $ ayane_lust = 40

    $ if "beachfive15" in config.label_overrides: del config.label_overrides["beachfive15"]
    jump beachfive15



label tsukasaspring3_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nNot choosen \"Take it\" will miss events later.{/i}"

    $ if "tsukasaspring3" in config.label_overrides: del config.label_overrides["tsukasaspring3"]
    jump tsukasaspring3



label chinamispring3_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nNot choosen \"Endanger her\" will miss events later.{/i}"

    $ if "chinamispring3" in config.label_overrides: del config.label_overrides["chinamispring3"]
    jump chinamispring3



label christmasfive1_avn:

    if not _in_replay and avnmode == True:
        if futaba_lust < 40:
            $ futaba_lust = 40
        if molly_lust < 10:
            $ molly_lust = 10
        if ayane_love <= 3000:
            $ ayane_love +=3000
            $ avn_ayane_love3000 = True

    $ if "christmasfive1" in config.label_overrides: del config.label_overrides["christmasfive1"]
    jump christmasfive1



label christmasfutaba1intro_avn:

    if not _in_replay and avnmode == True:
        if futaba_lust < 40:
            $ futaba_lust = 40
        if molly_lust < 10:
            $ molly_lust = 10
        if ayane_love <= 3000:
            $ ayane_love +=3000
            $ avn_ayane_love3000 = True

    $ if "christmasfutaba1intro" in config.label_overrides: del config.label_overrides["christmasfutaba1intro"]
    jump christmasfutaba1intro



label christmasfive8_avn:

    if not _in_replay and avnmode == True and ayane_love <= 3000:
        $ ayane_love +=3000
        $ avn_ayane_love3000 = True

    $ if "christmasfive8" in config.label_overrides: del config.label_overrides["christmasfive8"]
    jump christmasfive8



label sanainvite1_avn:

    $ sananumber = True
    jump sanainvite1



label endofbuildamaya_avn:

    if not _in_replay and avnmode == True and swimtrip2 == False:
        "{i}AUTO MOD WARNING:\nOops... Looks like you missed the happy scene!{/i}"
        "..."
        $ buildamayakoi = True
        $ buildamayamakoto = True
        $ buildamayakoitip = True
        jump buildamayaprehappy

    $ if "endofbuildamaya" in config.label_overrides: del config.label_overrides["endofbuildamaya"]
    jump endofbuildamaya



label iospring3_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nNot choosen \"Destroy her\" will miss events later.{/i}"

    $ if "iospring3" in config.label_overrides: del config.label_overrides["iospring3"]
    jump iospring3



label dormwarssix1_avn:

    if not _in_replay and avnmode == True and nodoka_love <= 200:
        $ nodoka_love +=200
        $ avn_nodoka_love200 = True

    $ if "dormwarssix1" in config.label_overrides: del config.label_overrides["dormwarssix1"]
    jump dormwarssix1



label dormwarssixnodoka1_avn:

    if not _in_replay and avnmode == True:
        "{i}AUTO MOD WARNING:\nNot choosen Maya will miss events later.{/i}"

    if not _in_replay and avnmode == True and nodoka_love <= 200:
        $ nodoka_love +=200
        $ avn_nodoka_love200 = True

    $ if "dormwarssixnodoka1" in config.label_overrides: del config.label_overrides["dormwarssixnodoka1"]
    jump dormwarssixnodoka1