label after_load_avn:
    
    if christmastwo19 and not christmastwo18:
        $ christmastwo18 = True
    if secondbeach5 and not secondbeach4:
        $ secondbeach4 = True
    if christmastwo19 and mollysad:
        $ mollysad = False
    if sadgirls8 == True and makotolust30 == False:
        $ makotolust30skip = True
    if sanapic1read == True:
        $ sananumber = True
    if tsukasarefused and tsukasacurious:
        $ tsukasacurious = False
        $ tsukasaspring4 = False
        $ tsukasaspring4skip = True
    if mayablock and christmasfive8:
        $ mayablock = False
    if dormwarsfive14 == True and nodokathontwo3 == False:
            $ ayanespring2miss = True
            $ saraspring3miss = True
            $ saraspring4miss = True
            $ saraspring5miss = True
    if saraspring2 == True and saraspring2miss == True:
            $ saraspring2miss = False
    if chikaspring8 == True and tsukasaspring5miss == True:
        $ tsubasaspring4miss = True
        $ tsubasaspring5miss = True
        $ tsukasaspring6miss = True
    if undeservedfuture18 == True and armsbenttrack == False:
        $ armsbentmiss = True 


    # AVN Mod
    # restore overrided labels

    python:
        
        # to fix errors in old saves
        renpy.store.avn_event = None

        config.label_overrides = {
            "after_load" : "after_load_avn",
            "start" : "start_avn",
            
            "afterschool" : "afterschool_avn",
            "afterschoolevent" : "afterschoolevent_avn",
            "asmenu" : "asmenu_avn",
            "saturdaymorning" : "saturdaymorning_avn",
            "satmorningmenu" : "satmorningmenu_avn",
            "saturdayafternoon" : "saturdayafternoon_avn",
            "saturdaynight" : "saturdaynight_avn",

            "morningch4" : "morningch4_avn",
            "ch4morningmenu" : "ch4morningmenu_avn",
            "noonch4" : "noonch4_avn",
            "ch4noonmenu" : "ch4noonmenu_avn",
            "nightch4" : "nightch4_avn",
            "ch4nightmenu" : "ch4nightmenu_avn",

            "amidormgen" : "amidormgen_avn",
            "ayanedormgen" : "ayanedormgen_avn",
            "chikadormgen" : "chikadormgen_avn",
            "futabadorm6to9" : "futabadorm6to9_avn",
            "mikudormgen" : "mikudormgen_avn",
            "rindorm6to9" : "rindorm6to9_avn",
            "sanadormgen" : "sanadormgen_avn",
            "mollydormgen" : "mollydormgen_avn",
            "nodokadormgen" : "nodokadormgen_avn",
            "otohadormgen" : "otohadormgen_avn",
            "toukadormgen" : "toukadormgen_avn",
            "yasudormgen" : "yasudormgen_avn",
            "makotodormgen" : "makotodormgen_avn",

            "ayanedorm20" : "ayanedorm20_avn",

            "day79": "day79_avn",
            "day103" : "day103_avn",
            "beachvacation1" : "beachvacation1_avn",
            "beachvacation6" : "beachvacation6_avn",
            "beachvacation10" : "beachvacation10_avn",
            "halloween1" : "halloween1_avn",
            "saralust10skip" : "saralust10skip_avn",
            "harukalust10skip" : "harukalust10skip_avn",
            "hoorayanotherreset" : "hoorayanotherreset_avn",
            
            "chikalust10intro" : "chikalust10intro_avn",
            "christmas6" : "christmas6_avn",
            "endofreset3loop" : "endofreset3loop_avn",
            "day264" : "day264_avn",
            "day318" : "day318_avn",
            "dormwar4" : "dormwar4_avn",
            "dormwar9" : "dormwar9_avn",
            "dormwar16" : "dormwar16_avn",
            "secondbeach1" : "secondbeach1_avn",
            "kirinlust20intro" : "kirinlust20intro_avn",
            "chikalust20intro" : "chikalust20intro_avn",
            "makotolust20intro" : "makotolust20intro_avn",
            "fmkx" : "fmkx_avn",
            "chinamibrx" : "chinamibrx_avn",
            "halloweentwo1" : "halloweentwo1_avn",
            "amilust20intro" : "amilust20intro_avn",
            "christmastwo1" : "christmastwo1_avn",
            "christmastwo3" : "christmastwo3_avn",
            "saralust20intro" : "saralust20intro_avn",
            "kirinlust202" : "kirinlust202_avn",
            "returntosummer3" : "returntosummer3_avn",
            "nodokaspecial15p1" : "nodokaspecial15p1_avn",
            "sadgirls1" : "sadgirls1_avn",
            "sadgirls7" : "sadgirls7_avn",
            "day344" : "day344_avn",
            "ayanespecial2" : "ayanespecial2_avn",

            "ayanesanabeach3" : "ayanesanabeach3_avn",
            "dormwartwo1" : "dormwartwo1_avn",
            "dormwartwo8" : "dormwartwo8_avn",
            "harukalust25intro" : "harukalust25intro_avn",
            "dormwartwo13" : "dormwartwo13_avn",
            "dormwartwo18" : "dormwartwo18_avn",
            "kirinlust30intro" : "kirinlust30intro_avn",
            "beachmas11" : "beachmas11_avn",
            "amilust35intro" : "amilust35intro_avn",
            "chikadorm45" : "chikadorm45_avn",
            "gstriviaround2" : "gstriviaround2_avn",
            "halloweenfour1" : "halloweenfour1_avn",
            "amilust50intro" : "amilust50intro_avn",
            "escaperoomfridge" : "escaperoomfridge_avn",
            "resetsix2" : "resetsix2_avn",

            "amilust60intro" : "amilust60intro_avn",
            "chinamispring2" : "chinamispring2_avn",
            "sportswars19" : "sportswars19_avn",
            "beachfive1" : "beachfive1_avn",
            "beachfive15" : "beachfive15_avn",
            "tsukasaspring3" : "tsukasaspring3_avn",
            "chinamispring3" : "chinamispring3_avn",
            "gameworldmainhub" : "gameworldmainhub_avn",
            "christmasfive1" : "christmasfive1_avn",
            "christmasfutaba1intro" : "christmasfutaba1intro_avn",
            "christmasfive8" : "christmasfive8_avn",
            "iospring3" : "iospring3_avn",
            "endofbuildamaya" : "endofbuildamaya_avn",
            "dormwarssix1" : "dormwarssix1_avn",
            "dormwarssixnodoka1" : "dormwarssixnodoka1_avn"
        }
