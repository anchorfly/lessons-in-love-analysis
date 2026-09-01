
# MAIN FUNCTIONS 
# check conditions and automatically move to next event
# if there is no event, go to the standard menu


label avn_stop_check:

    # reset changed variables

    if avn_ayane_love2000 == True and ayane_love > 2000:
        $ ayane_love -=2000
        $ avn_ayane_love2000 = False

    if avn_ayane_love3000 == True and ayane_love > 3000:
        $ ayane_love -=3000
        $ avn_ayane_love3000 = False

    if avn_nodoka_love200 == True and nodoka_love > 200:
        $ nodoka_love -=200
        $ avn_nodoka_love200 = False

    if halloweenfive17 == True and persistent.alexisevent <> True:
        "{i}AUTO MOD HINT:\nSecret happy scene unlocked! You can see it in Event Tracker - Happy Scenes - Alexisthymia.{/i}"
        $ persistent.alexisisreal = False
        $ persistent.alexisevent = True

    # protection from the game update without updating mod
    # check last known event - if passed, then disable overriding labels so it doesn't affect the game

    $ avndisabled = False

    if utaspring9 == True and (harukaspring6 == True or harukaspring6miss == True) and (kirinspring4 == True or kirinspring4miss == True) and (mayaspring4 == True or mayaspring4miss == True):   # ! LATEST EVENT - CHANGE WHEN UPDATE MOD ! # 060
            "{i}AUTO MOD DISABLED\nUpdate the mod when update the game{/i}"
            $ config.label_overrides = {"after_load" : "after_load_avn"}
            $ avndisabled = True
    return



label newday_saturdaymorning_avn: 

    scene bedroom_day
    with dissolve2

    "{i}[totaldays] Days have passed...{/i}"

    return


label newday_morningch4_avn: 

    scene bedroom_day
    with dissolve2

    "{i}[totaldays] Days have passed...{/i}"

    return


label newday_afterschool_avn:

    if chapthreeactive == True:
        scene street_noon
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene citysnow
        with dissolve
    else:
        scene street_noon
        with dissolve

    play music "streetnoise.mp3" fadein 2.0

    return
    

label endofday_avn(new_day, avn_daypart, avn_dayend):

    $ day_shift = new_day - day

    if avn_dayend == 4:

        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Being alive is exhausting."

        scene black
        with dissolve
        play sound "tackle.mp3"

        "I wonder how much longer I can take this for?"
        "........."
        "......"
        "..."

    elif avn_daypart == 2 and avn_dayend == 2:

        call newday_afterschool_avn

        "School passed by without anything interesting happening today."
        "I went home and went to bed early."
        "Being around teenagers is exhausting."

        scene black
        with dissolve

        "........."
        "......"
        "..."

    elif avn_daypart == 0:

        scene black
        with dissolve

    else:

        s "I'm feeling kind of tired today...Maybe I'll just head back to the house and go to sleep early?"
        "I decide to walk home."

        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Being around teenagers is exhausting."
        "I should probably get some sleep before heading out tomorrow..."

        scene black
        with dissolve

        "........."
        "......"
        "..."

    if day == 1:
        hide monday onlayer date
    if day == 2:
        hide tuesday onlayer date
    if day == 3:
        hide wednesday onlayer date
    if day == 4:
        hide thursday onlayer date
    if day == 5:
        hide friday onlayer date
    if day == 6:
        hide saturday onlayer date
    if day == 7:
        hide sunday onlayer date

    if day_shift != 1 and day_shift != -6:
        "A few days later."
    "{i}[totaldays] Days have passed...{/i}"

    $ day = new_day
    if day == 1:
        show monday onlayer date
    if day == 2:
        show tuesday onlayer date
    if day == 3:
        show wednesday onlayer date
    if day == 4:
        show thursday onlayer date
    if day == 5:
        show friday onlayer date
    if day == 6:
        show saturday onlayer date
    if day == 7:
        show sunday onlayer date
    
    if avn_dayend == 4:

        scene bedroom_day
        with dissolve2

        "I wake up again."
        "I need to keep myself busy."
        "..."

    return


label dormday_avn:

    if chap4active == True:
        scene dorm
        with fade
        play music "sweetvermouth.mp3"

        "I decide to pay a visit to the dorms."

    else:
        if day == 1:
            call dormmonday_avn
        elif day == 2:
            call dormtuesday_avn
        elif day == 3:
            call dormwednesday_avn
        elif day == 4:
            call dormthursday_avn
        elif day == 5:
            call dormfriday_avn
        else:
            call dormweekend_avn
    return


label dormmonday_avn:

    if chapthreeactive == True and yumiblock == False:
        scene summerdorm1mon
        with dissolve
    elif chapthreeactive == True and yumiblock == True:
        scene dormmonyumigone
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene monwinter
        with dissolve
    else:
        scene dorm_monday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."

    return


label dormtuesday_avn:

    if chapthreeactive == True and mikublock == False:
        scene summerdorm1tues
        with dissolve
    elif chapthreeactive == True and mikublock == True:
        scene dormtuesmikugone
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene tueswinter
        with dissolve
    else:
        scene dorm_tuesday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."

    return


label dormwednesday_avn:

    if chapthreeactive == True:
        scene summerdorm1wed
        with dissolve
    elif rinsad == True and chapthreeactive == False:
        scene wedwinterringone
        with dissolve
    elif cafe15 == True and rindorm20 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif beachvacation16 == True and rindorm35 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene wedwinter
        with dissolve
    else:
        scene dorm_wednesday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."

    return


label dormthursday_avn:

    if chapthreeactive == True and makotoblock == False:
        scene summerdorm1thurs
        with dissolve
    elif chapthreeactive == True and makotoblock == True:
        scene dormthursmakotogone
        with dissolve
    elif makotodorm25 == True and hoorayanotherreset == False and chapthreeactive == False:
        scene dorm_thursday2
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene thurswinter
        with dissolve
    else:
        scene dorm_thursday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."

    return


label dormfriday_avn:

    if chapthreeactive == True:
        scene summerdorm1fri
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene friwinter
        with dissolve
    else:
        scene dorm_friday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."

    return


label dormweekend_avn:

    scene dorm
    with dissolve
    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "Maybe it would be a good time to spend some time with one of the girls."
    "It doesn't look like anyone is hanging out in the halls today."

    return


label dorm2day_avn:

    if chap4active == True:
        scene dorm2
        with fade
        play music "sweetvermouth.mp3"
        
        "I walk up the stairs to the second floor of the dorms."

    else:
        if day == 1:
            call dorm2monday_avn
        elif day == 2:
            call dorm2tuesday_avn
        elif day == 3:
            call dorm2wednesday_avn
        elif day == 4:
            call dorm2thursday_avn
        elif day == 5:
            call dorm2friday_avn
        else:
            call dorm2weekend_avn

    return


label dorm2monday_avn:

    if otohaspecial15p2 == True:
        scene summerdorm2monsecond
        with dissolve
    elif chapthreeactive == True and otohaspecial15p2 == False:
        scene summerdorm2mon
        with dissolve
    elif mollysad == True and chapthreeactive == False:
        scene monwinter2nomolly
        with dissolve
    elif day288 == True and mollysad == False and chapthreeactive == False:
        scene monwinter2otoha
        with dissolve
    elif christmas7 == True and day288 == False and chapthreeactive == False:
        scene monwinter2
        with dissolve
    else:
        scene dorm2_monday
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return


label dorm2tuesday_avn:

    if chapthreeactive == True:
        scene summerdorm2tues
        with dissolve
    elif day304 == True and chapthreeactive == False:
        scene tueswinter2
        with dissolve
    elif day304 == False and day247 == True and chapthreeactive == False:
        scene dorm2_tuesday
        with dissolve
    else:
        scene dorm2
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return


label dorm2wednesday_avn:

    if chapthreeactive == True and norikoblock == False:
        scene summerdorm2wed
        with dissolve
    elif chapthreeactive == True and norikoblock == True:
        scene summerdorm2wednorikogone
        with dissolve
    elif christmas7 == True and day271 == True and chapthreeactive == False:
        scene wedwinter2noriko
        with dissolve
    elif christmas7 == True and day271 == False and chapthreeactive == False:
        scene wedwinter2
        with dissolve
    elif christmas7 == False and chapthreeactive == False:
        scene dorm2_wednesday
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return


label dorm2thursday_avn:

    if yasu_love >= 25 and church25 == True and yasudorm25 == False:
        jump yasudorm25
    elif chapthreeactive == True:
        scene summerdorm2thurs
        with dissolve
    elif day304 == True and chapthreeactive == False:
        scene thurswinter2yasu
        with dissolve
    elif day304 == False and day271 == True and chapthreeactive == False:
        scene thurswinter2
        with dissolve
    else:
        scene dorm2
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return


label dorm2friday_avn:

    if chapthreeactive == True and nodokablock == False:
        scene summerdorm2fri
        with dissolve
    elif chapthreeactive == True and nodokablock == True:
        scene dorm2frinodokagone
        with dissolve
    elif day288 == True and chapthreeactive == False:
        scene friwinter2nodoka
        with dissolve
    elif day247 == True and day288 == False and chapthreeactive == False:
        scene dorm2_friday
        with dissolve
    else:
        scene dorm2
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return


label dorm2weekend_avn:

    scene dorm2
    with dissolve

    "I walk up the stairs to the second floor of the dorms."

    return



# main check function
# avn_daypart = 0-mornig, 1-afternoon, 2-evening
# avn_dayend  = 1-weekend, 2-weekday after school, 3-weekday after event, 4-ch4

label avn_main_check(avn_daypart, avn_dayend = None, skipintro = False):

    python:

        v11check()
        avn_label, avn_type, avn_mess, day_vars, avn_vars, avn_varsl = avn_check_event(avn_daypart)

        # change variables if required

        new_totaldays =  None
        new_day = None
        new_daypart = None

        # day_vars - force update

        for avn_var_name in day_vars:
            locals()[avn_var_name] = day_vars[avn_var_name]

        # avn_vars - update only if we need to increase the value

        if avn_vars != None:
            for avn_var_name in avn_vars:
                if avn_vars[avn_var_name] > locals()[avn_var_name]:
                    locals()[avn_var_name] = avn_vars[avn_var_name]

        if avn_varsl != None:
            for avn_var_name in avn_varsl:
                if avn_varsl[avn_var_name] > locals()[avn_var_name]:
                    locals()[avn_var_name] = avn_varsl[avn_var_name]

    if totaldays != new_totaldays:
        $ totaldays = new_totaldays

    # check the event type and change the scene if required

    if day != new_day:
        call endofday_avn(new_day, avn_daypart, avn_dayend)

    elif skipintro == False:
        if avn_dayend == 0:
            "..."

        elif avn_dayend == 4:
            if avn_daypart == 0:
                call newday_morningch4_avn
                "I wake up again."
                "I need to keep myself busy."

        elif avn_daypart == 0:
            call newday_saturdaymorning_avn
            "I wake up to sunlight pouring in through the window."
            "What should I do today?"
        
        elif avn_daypart == 1:
            "Now what should I do?"

        elif avn_dayend == 1:
            "It's late, but I should be able to fit one more thing in today..."
            "What should I do now?"

        elif avn_dayend == 2:
            call newday_afterschool_avn
            "School passed by without anything interesting happening today."
            "It should be getting dark any minute now, but I still have a little time before I need to head home."

        elif avn_dayend == 3:
            call newday_afterschool_avn
            "Hmm...I should still be able to fit one more activity in today."
    
    # display a message if required

    if avn_mess != "":
        "[avn_mess]"
        "..."

    # scene change before some events

    if avn_type == "dorm":
        call dormday_avn

    if avn_type == "dorm2":
        call dorm2day_avn

    # messages before some events

    if avn_label == "roomwithclocks":
        "I knock on Ami and Maya's door."
        "..."

    if avn_label == "lettert":
        "..."
        "I decide to go back home."

    if avn_label == "howifeel":
        "I'm heading to the Shrine to see if Maya is there."

    if avn_label == "specialclassroom":
        "I tap on {s} Maya's {/s} name in my phone."
        "There is something buried underneath your feet."

    if avn_label == "ticktock":
        "I knock on Ami and Maya's door."
        "..."

    if avn_label == "trinity1":
        "..."
        "I decide to go back home."

    if avn_label == "trinity3":
        "I tap on xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx in my phone."

    if avn_label == "goodboy":
        "I decide to wait until the morning."
        "..."
    
    if avn_label == "bucketscene":
        "I'm going to New Hope Cathedral." 
        "..."

    if avn_label == "rincafegone":
        $ rincafegone_avn = True

    # invites

    if avn_label == "amiinviteaff":
        call amiinvitegen_avn

    if avn_label == "ayaneinviteaff":
        call ayaneinvitegen_avn

    if avn_label == "chikainviteaff":
        call chikainvitegen_avn

    if avn_label == "futabainviteaff":
        call futabainvitegen_avn

    if avn_label == "harukainviteaff":
        call harukainvitegen_avn

    if avn_label == "kirininviteaff":
        call kirininvitegen_avn

    if avn_label == "makiinviteaff":
        call makiinvitegen_avn

    if avn_label == "makotoinviteaff":
        call makotoinvitegen_avn

    if avn_label == "mikuinviteaff":
        call mikuinvitegen_avn

    if avn_label == "nikiinviteaff":
        call nikiinvitegen_avn

    if avn_label == "sarainviteaff":
        call sarainvitegen_avn

    if avn_label == "mollyinviteaff":
        call mollyinvitegen_avn

    if avn_label == "nodokainviteaff":
        call nodokainvitegen_avn

    if avn_label == "sanainviteaff":
        call sanainvitegen_avn

    if avn_label == "kaoriinviteaff":
        call kaoriinvitegen_avn

    if avn_label == "norikoinviteaff":
        call norikoinvitegen_avn

    # label of event

    return avn_label
