
# AutoVN Mod

init python:

    import string

    # OVERRIDE LABELS

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
    
    # VARIABLES

    rincafegone_avn = False
    avn_ayane_love2000 = False
    avn_ayane_love3000 = False
    avn_nodoka_love200 = False
    
    avnmode = False
    avndisabled = False
    avn_events_ch1 = []
    avn_events_ch2 = []
    avn_events_ch3 = []
    avn_events_ch4 = []
    avn_event = None

    # for compatibility with old save files
    class AvnEvent:
        None

    def add_avn_event(ev_label, ev_name, ev_girl, ev_chapter, ev_type, ev_req, ev_totaldays = None, ev_days = None, ev_lovereq = {}, ev_lustreq = {}):

        # ev_label = 0, ev_name = 1, ev_girl = None, ev_chapter = 2, ev_type = 3, ev_req = 4, ev_totaldays = 6, ev_days = 5, ev_lovereq = 7, ev_lustreq = 8

        avn_event = [ev_label, ev_name, ev_chapter, ev_type, ev_req, ev_days, ev_totaldays, ev_lovereq, ev_lustreq]

        if ev_chapter == 1:
            avn_events_ch1.append(avn_event)
        if ev_chapter == 2:
            avn_events_ch2.append(avn_event)
        if ev_chapter == 3:
            avn_events_ch3.append(avn_event)
        if ev_chapter == 4:
            avn_events_ch4.append(avn_event)


    # MAIN FUNCTIONS

    def avn_check_event(daypart = 2):      # daypart = 0-morning, 1-afternoon, 2-evening

        if resetsix4 == True:
            avn_events = avn_events_ch4
        elif returntosummer3 == True:
            avn_events = avn_events_ch3
        elif hoorayanotherreset == True:
            avn_events = avn_events_ch2
        else:
            avn_events = avn_events_ch1

        i_label = 0
        i_name = 1
        i_chapter = 2
        i_type = 3
        i_req = 4
        i_days = 5
        i_totaldays = 6
        i_lovereq = 7
        i_lustreq = 8

        min_ev_label = ""
        min_ev_name = ""
        min_ev_lovereq = None
        min_ev_type = ""
        min_totaldays_shift = None
        min_totaldaypart_shift = None

        avn_vars = {}
        avn_varsl = {}
        day_vars = {}
        avn_mess = ""

        day_vars["new_totaldays"] = totaldays
        day_vars["new_day"] = day
        day_vars["new_daypart"] = daypart

        list_events = []
        list_generic = []

        for avn_event in avn_events:

            # iterate events, check main condition
            # if main condition is not met, iterate next

            if eval(avn_event[i_req]) == True:
                
                new_day = day           # day of the week 1 to 7
                new_daypart = daypart   # daypart: 0-morning, 1-afternoon, 2-evening
                totaldays_shift = 0     # how many days to add

                # check day of week and part of day

                if avn_event[i_type] in {"weekday_morning"}:
                    if new_day > 5:
                        totaldays_shift += 8 - new_day
                        new_day = 1
                        new_daypart = 2
               
                elif avn_event[i_type] in {"saturday_morning"}:
                    if new_day < 6:
                        new_daypart = 0
                        new_day = 6
                        totaldays_shift  = 6 - day
                    
                    elif new_day == 6 and new_daypart > 0:
                        new_daypart = 0
                        new_day = 6
                        totaldays_shift  = 7
                    
                    elif new_day == 7:
                        new_daypart = 0
                        new_day = 6
                        totaldays_shift  = 6

                elif avn_event[i_type] in {"weekend_morning", "work1", "date_morning"}:
                    if new_day < 6:
                        new_daypart = 0
                        new_day = 6
                        totaldays_shift  = 6 - day

                    elif new_day == 6 and new_daypart > 0:
                        new_daypart = 0
                        new_day = 7
                        totaldays_shift = 1

                    elif new_day == 7  and new_daypart > 0:
                        new_daypart = 0
                        new_day = 6
                        totaldays_shift = 6
 
                elif avn_event[i_type] in {"weekend_afternoon", "work2", "date_afternoon"}:
                    if new_day < 6:
                        new_daypart = 1
                        new_day = 6
                        totaldays_shift  = 6 - day

                    elif new_daypart == 0:
                        new_daypart = 1

                    elif new_day == 6 and new_daypart > 1:
                        new_daypart = 1
                        new_day = 7
                        totaldays_shift = 1

                    elif new_day == 7 and new_daypart > 1:
                        new_daypart = 1
                        new_day = 6
                        totaldays_shift = 6

                elif avn_event[i_type] in {"weekend_night"}:
                    if new_day < 6:
                        new_daypart = 2
                        new_day = 6
                        totaldays_shift  = 6 - day

                    elif new_daypart < 2:
                        new_daypart = 2

                elif avn_event[i_type] in {"work3", "dorm", "dorm2", "date_night", "invite"}:
                    if new_day > 5 and new_daypart < 2:
                        new_daypart = 2

                elif avn_event[i_type] in {"ch4work1", "ch4date_morning"}:
                    if new_daypart > 0:
                        new_daypart = 0
                        if new_day < 7:
                            new_day += 1
                        else:
                            new_day = 1
                        totaldays_shift = 1

                elif avn_event[i_type] in {"ch4work2", "ch4date_afternoon"}:
                    if new_daypart == 0:
                        new_daypart = 1
                    elif new_daypart > 1:
                        new_daypart = 1
                        if new_day < 7:
                            new_day += 1
                        else:
                            new_day = 1
                        totaldays_shift = 1

                elif avn_event[i_type] in {"ch4work3", "ch4date_night"}:
                    if new_daypart < 2:
                        new_daypart = 2


                # check day count

                if avn_event[i_totaldays] != None and avn_event[i_totaldays] > totaldays + totaldays_shift:
                    totaldays_shift += avn_event[i_totaldays] - totaldays - totaldays_shift
                    new_day = (day + totaldays_shift) % 7
                    if new_day == 0:
                        new_day = 7


                # check day of week

                ev_days = avn_event[i_days]
                if ev_days == None:
                    if avn_event[i_type] in {"weekday_morning"}:
                        ev_days = {1,2,3,4,5}
                    elif avn_event[i_type] in {"saturday_morning"}:
                        ev_days = {6}
                    elif avn_event[i_type] in {"weekend_morning", "saturday_morning", "work1", "date_morning", "weekend_afternoon", "work2", "date_afternoon", "weekend_night"}:
                        ev_days = {6,7}

                if ev_days != None and not new_day in ev_days:
                    newday_shift = 0
                    for correct_day in ev_days:
                        if correct_day < new_day:
                            newday_shift_ = correct_day + 7 - new_day
                        else:
                            newday_shift_ = correct_day - new_day
                        if newday_shift == 0:
                            newday_shift = newday_shift_
                        elif newday_shift > newday_shift_:
                            newday_shift = newday_shift_

                    totaldays_shift += newday_shift
                    new_day = (day + totaldays_shift) % 7
                    if new_day == 0:
                        new_day = 7

                    if avn_event[i_type] in {"work1", "weekend_morning", "date_morning", "ch4work1", "ch4date_morning"}:
                        new_daypart = 0
                    elif avn_event[i_type] in {"work2", "date_afternoon", "ch4work2", "ch4date_afternoon"}:
                        new_daypart = 1
                    elif avn_event[i_type] in {"work3", "date_night", "invite", "dorm", "dorm2", "ch4work3", "ch4date_night"}:
                        new_daypart = 2


                # if there is no shift, add to the list to choose the best one later
                
                if totaldays_shift == 0 and new_daypart == daypart:

                    min_ev_lovereq = 0

                    if avn_event[i_lovereq] != None:
                        for var_name in avn_event[i_lovereq]:
                            if min_ev_lovereq == 0 or min_ev_lovereq > avn_event[i_lovereq][var_name]:
                                min_ev_lovereq = avn_event[i_lovereq][var_name]

                    if avn_event[i_name] == "generic":
                        list_generic.append([avn_event, min_ev_lovereq])
                    else:
                        list_events.append([avn_event, min_ev_lovereq])

                else:

                    # compare with other events and choose the one where the shift is minimal
                    # if there are two identical ones, take the main event, not the generic
                    
                    if min_totaldays_shift == None or (totaldays_shift < min_totaldays_shift) or (totaldays_shift == min_totaldays_shift and new_daypart < min_new_daypart) or (min_ev_name == "generic" and min_ev_name != "generic"):

                        min_ev_label = avn_event[i_label]
                        min_ev_name = avn_event[i_name]
                        min_ev_lovereq = avn_event[i_lovereq]
                        min_ev_lustreq = avn_event[i_lustreq]
                        min_ev_type = avn_event[i_type]
                        min_totaldays_shift = totaldays_shift
                        min_new_daypart = new_daypart


        # check the found events - choose the one with the lower points requirement (this is not always correct, but so be it)

        min_ev = None
        for event in list_events:
            if min_ev == None or min_ev_lovereq > event[1]:
                min_ev = event[0]
                min_ev_lovereq = event[1]

        # if found nothing, check generics
        
        if min_ev == None and len(list_generic) > 0:
            min_ev = list_generic[0][0]
            min_ev_lovereq = list_generic[0][1]

        # if found something, return event name, type, and lists of variables to change

        if min_ev != None:
            avn_vars = min_ev[i_lovereq]
            avn_varsl = min_ev[i_lustreq]
            
            return (min_ev[i_label], min_ev[i_type], avn_mess, day_vars, avn_vars, avn_varsl)

        # didn't find an event for the current day, but found an event with a time shift

        if min_ev_label != "":
            if min_ev_lovereq != None:
                avn_vars = min_ev_lovereq
            if min_ev_lustreq != None:
                avn_varsl = min_ev_lustreq

            new_day = (day + min_totaldays_shift) % 7
            if new_day == 0:
                new_day = 7
            day_vars["new_totaldays"] = totaldays + min_totaldays_shift
            day_vars["new_day"] = new_day
            day_vars["new_daypart"] = min_new_daypart

            # if there is no date shift, there is a shift within a day - add the message text

            if min_totaldays_shift == 0:
                if daypart == 0:
                    avn_mess = avn_mess + "It's still too early to do anything...I'll just sit around for a few hours or something."
                else:
                    avn_mess = avn_mess + "I'll just...walk around until it starts to get dark, I guess."

            # return event name, type, date shift and lists of variables to change

            return (min_ev_label, min_ev_type, avn_mess, day_vars, avn_vars, avn_varsl)

        # error - no available events

        else:
            return ("", "ERROR AUTO MOD - no available events", avn_mess, day_vars, avn_vars, avn_varsl)



    # CONDITIONS

    #CH1MAIN
    add_avn_event("everyday", "Every Day I Grow Some More", "MainEvent", 1, "weekday_morning", "everyday == False")
    add_avn_event("clichebath", "A New You", "MainEvent", 1, "weekday_morning", "clichebath == False")
    add_avn_event("amiawake", "Am I Awake?", "MainEvent", 1, "weekday_morning", "amiawake == False")
    add_avn_event("firstclass", "First (?) Day of School", "MainEvent", 1, "weekday_morning", "firstclass == False")
    add_avn_event("sleepover", "Slumber Party", "MainEvent", 1, "weekday_morning", "sleepover == False")
    add_avn_event("firstdorm", "firstdorm", "MainEvent", 1, "work3", "dorm == 0")                       # added !
    add_avn_event("day20", "I Thought of You", "MainEvent", 1, "weekday_morning", "day20 == False", 20)
    add_avn_event("day5", "The Devil Incarnate", "MainEvent", 1, "weekday_morning", "day5 == False", 5)
    add_avn_event("day7", "Super Secret Sex Dungeon", "MainEvent", 1, "weekday_morning", "day7 == False", 7)
    add_avn_event("day8", "Delinquent", "MainEvent", 1, "weekday_morning", "day8 == False", 8)
    add_avn_event("day12", "Mitochondria", "MainEvent", 1, "weekday_morning", "day12 == False", 12)
    add_avn_event("day14", "Self-Esteem", "MainEvent", 1, "weekday_morning", "firsttimelibrary == True and day14 == False", 14)
    add_avn_event("day16", "Operation: Fallen Angel", "MainEvent", 1, "weekday_morning", "firsttimedojo == True and day16 == False", 16)
    add_avn_event("day20", "I Thought of You", "MainEvent", 1, "weekday_morning", "day20 == False", 20)
    add_avn_event("day21", "Not Even Me", "MainEvent", 1, "weekday_morning", "firsttimestreets and day21 == False", 21)
    add_avn_event("day24", "No Romeo", "MainEvent", 1, "weekend_morning", "day24 == False", 24)
    add_avn_event("day26", "Outside of Everything", "MainEvent", 1, "weekday_morning", "day26 == False", 26)
    add_avn_event("day28", "Ponytail", "MainEvent", 1, "weekday_morning", "day21 == True and day28 == False", 28)
    add_avn_event("day30", "Drowning", "MainEvent", 1, "weekday_morning", "cafesugar == True and day30 == False", 30)
    add_avn_event("day33", "So Many Voices", "MainEvent", 1, "weekday_morning", "day33 == False", 33)
    add_avn_event("day36", "Cleaning Duty", "MainEvent", 1, "weekday_morning", "day16 == True and bar5 == True and day36 == False", 36)
    add_avn_event("day38", "Walk in the Park", "MainEvent", 1, "weekend_afternoon", "firsttimepornshop == True and day36 == True and day38 == False", 38)
    add_avn_event("day40", "Saved by the Bell", "MainEvent", 1, "weekday_morning", "day40 == False", 40)
    add_avn_event("day44", "This Town Has Two Halves", "MainEvent", 1, "weekday_morning", "day38 == True and day44 == False", 44)
    add_avn_event("day48", "Little Girl", "MainEvent", 1, "weekday_morning", "day48 == False", 48)
    add_avn_event("day50", "Missing", "MainEvent", 1, "weekday_morning", "cafe15 == True and day50 == False", 50)
    add_avn_event("day54", "The Sakakibara Diet", "MainEvent", 1, "weekday_morning", "day54 == False", 54)
    add_avn_event("day56", "Normal Office Visit", "MainEvent", 1, "weekday_morning", "shrine5 == True and day56 == False", 56)
    # add_avn_event("day60", "O World (In Our Final Moments)", "MainEvent", 1, "chain", "aminew2")
    add_avn_event("day63", "One to Seven", "MainEvent", 1, "weekday_morning", "rindorm20 == True and day63 == False", 63)
    add_avn_event("day65", "Girl-Talk", "MainEvent", 1, "weekday_morning", "bar15 == True and cafe20 == True and day65 == False", 65)
    add_avn_event("day70", "The 'S' Word", "MainEvent", 1, "weekday_morning", "bar10 == True and day70 == False", 70)
    add_avn_event("day72", "Weight Limit", "MainEvent", 1, "weekday_morning", "day70 == True and day72 == False", 72)
    add_avn_event("day77", "Slope Intercept Form", "MainEvent", 1, "weekday_morning", "day77 == False", 77)
    add_avn_event("day79_avn", "Scientific Research", "MainEvent", 1, "weekday_morning", "chikadorm15 == True and day79 == False", 79, {5})
    add_avn_event("day80", "Secret Ingredient", "MainEvent", 1, "weekend_morning", "day72 == True and day80 == False", 80)
    add_avn_event("day83", "Parasite", "MainEvent", 1, "weekday_morning", "ayanedorm10 == True and mikudorm10 == True and day83 == False", 83)
    add_avn_event("day85", "Contractions", "MainEvent", 1, "weekday_morning", "streets10 == True and day85 == False", 85)
    add_avn_event("day89", "Milk, Eggs, and Water", "MainEvent", 1, "weekday_morning", "day65 == True and day89 == False", 89)
    add_avn_event("day91", "Stronger I Become", "MainEvent", 1, "weekday_morning", "day63 == True and day65 == True and day91 == False", 91)
    add_avn_event("day96", "Recall", "MainEvent", 1, "weekday_morning", "shrine15 == True and ayanenew1 == True and day91 == True and day96 == False", 96, {1})
    add_avn_event("day102", "Rewrite", "MainEvent", 1, "weekend_morning", "day96 == True and mayadorm15 == True and letterttrack == True and howifeeltrack == True and day102 == False", 102, {7})
    add_avn_event("day103_avn", "Reset", "MainEvent", 1, "weekday_morning", "day102 == True and day103 == False", 103)
    add_avn_event("day110", "Cursed Birds", "MainEvent", 1, "weekday_morning", "day103 == True and day110 == False", 110)
    add_avn_event("day114", "Human Trafficking", "MainEvent", 1, "weekday_morning", "day103 == True and bar20 == True and day114 == False", 114)
    add_avn_event("day120", "Girl Talk Pt. II", "MainEvent", 1, "weekday_morning", "day103 == True and day91 == True and day120 == False", 120)
    add_avn_event("day121", "A Different View", "MainEvent", 1, "weekday_morning", "day85 == True and day103 == True and day121 == False", 121)
    add_avn_event("day126", "On The Bright Side", "MainEvent", 1, "weekday_morning", "day103 == True and streets15 == True and chikadorm15 == True and day126 == False", 126)
    add_avn_event("day128", "Everything Horrible", "MainEvent", 1, "weekday_morning", "day103 == True and day126 == True and day128 == False", 128, {5})
    add_avn_event("day130", "Erotic Game Protagonist", "MainEvent", 1, "weekend_night", "day128 == True and day130 == False", 130, {6,7})
    add_avn_event("day138", "Rumors", "MainEvent", 1, "weekday_morning", "day103 == True and day130 == True and day85 == True and day138 == False", 138)
    add_avn_event("day140", "The Gem of the Emerald Isle", "MainEvent", 1, "weekday_morning", "day138 == True and day140 == False", 140)
    add_avn_event("day142", "Size Matters", "MainEvent", 1, "weekday_morning", "amidorm15 == True and day140 == True and day142 == False", 142)
    add_avn_event("day144", "Tsuneyo Tojo, Stand-up Comedian", "MainEvent", 1, "weekday_morning", "day128 == True and day142 == True and day144 == False", 144)
    add_avn_event("day150", "A Proper Introduction", "MainEvent", 1, "weekday_morning", "day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False", 150)
    add_avn_event("day153", "Supreme Overlord", "MainEvent", 1, "weekday_morning", "day150 == True and day153 == False", 153)
    add_avn_event("day154", "Lifting the Curse", "MainEvent", 1, "weekday_morning", "day153 == True and day154 == False", 154)
    add_avn_event("beachvacation1_avn", "What's Done is Done", "MainEvent", 1, "saturday_morning", "day154 == True and amidorm15 == True and futabadorm15 == True and day79 == True and makotonew3 == True and kirindate1 == True and ramen1 == True and mollydorm10 == True and rindorm25 == True and bar10 == True and beachvacation1 == False", 174, {6})
    # add_avn_event("beachvacation2", "All Along the Shoreline", "MainEvent", 1, "chain", "beachvacation1")
    # add_avn_event("beachvacation3", "My Heart is Full", "MainEvent", 1, "chain", "beachvacation2")
    # add_avn_event("beachvacation4", "Extra French Fries", "MainEvent", 1, "chain", "beachvacation3")
    # add_avn_event("beachvacation5", "Behind a Bathroom, Under the Blazing Sun", "MainEvent", 1, "chain", "beachvacation4")
    # add_avn_event("beachvacation6", "Three Girls in a Line on the Beach", "MainEvent", 1, "chain", "beachvacation5")
    # add_avn_event("beachvacation7", "The Moon is Beautiful", "MainEvent", 1, "chain", "beachvacation6")
    # add_avn_event("beachvacation8", "The Legacy of Thaum Pt. I", "MainEvent", 1, "chain", "beachvacation7")
    # add_avn_event("beachvacation9", "Summer and Winter", "MainEvent", 1, "chain", "beachvacation8")
    # add_avn_event("beachvacation10", "Where Puppies Roam Free", "MainEvent", 1, "chain", "beachvacation9")
    # add_avn_event("beachvacation11", "Die For What You Believe In", "MainEvent", 1, "chain", "beachvacation10")
    # add_avn_event("beachvacation12", "Reverse Cowgirl", "MainEvent", 1, "chain", "beachvacation11")
    # add_avn_event("beachvacation13", "Smile Guide", "MainEvent", 1, "chain", "beachvacation12")
    # add_avn_event("beachvacation14", "Prayer Position", "MainEvent", 1, "chain", "beachvacation13")
    # add_avn_event("beachvacation15", "Cry. Cry. Cry.", "MainEvent", 1, "chain", "beachvacation14")
    # add_avn_event("beachvacation16", "See You in the Morning", "MainEvent", 1, "chain", "beachvacation15")
    add_avn_event("halloween1_avn", "The Value of Sharing", "MainEvent", 1, "weekday_morning", "beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and ramen10 == True and halloween1 == False", 200, {5})
    # add_avn_event("halloween2", "Guest of Honor", "MainEvent", 1, "chain", "halloween1")
    # add_avn_event("halloween3", "The Meat has Come", "MainEvent", 1, "chain", "halloween2")
    # add_avn_event("halloween4", "Mysterious Abundance of Chickens", "MainEvent", 1, "chain", "halloween3")
    # add_avn_event("halloween5", "Sexy Land", "MainEvent", 1, "chain", "halloween4")
    # add_avn_event("halloween6", "They're Just Lights", "MainEvent", 1, "chain", "halloween5")
    # add_avn_event("halloween7", "Once, Twice, Ten Times", "MainEvent", 1, "chain", "halloween6")
    # add_avn_event("halloween8", "Mechanical Bull", "MainEvent", 1, "chain", "halloween7")
    # add_avn_event("halloween9", "At Least It's Not Christmas", "MainEvent", 1, "chain", "halloween8")
    # add_avn_event("halloween10", "Samhain", "MainEvent", 1, "chain", "halloween9")
    # add_avn_event("halloween11", "Wicked Witch of Kumon-mi", "MainEvent", 1, "chain", "halloween10")
    # add_avn_event("halloween12", "The Depressing Implication of Goosebumps", "MainEvent", 1, "chain", "halloween11")
    # add_avn_event("halloween13", "Pry With a Smile", "MainEvent", 1, "chain", "halloween12")
    # add_avn_event("halloween14", "Kadrillionbilliontrillion", "MainEvent", 1, "chain", "halloween13")
    add_avn_event("day214", "As Loud as a Whisper Can Be", "MainEvent", 1, "weekday_morning", "makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day214 == False", 214, {1})
    add_avn_event("day215", "Two Wooden Doors", "MainEvent", 1, "weekday_morning", "day214 == True and day215 == False", 215, {2})
    add_avn_event("day216", "Happy Places", "MainEvent", 1, "weekday_morning", "day215 == True and day216 == False", 216, {3})
    add_avn_event("day217", "Tradition", "MainEvent", 1, "weekday_morning", "day216 == True and day217 == False", 217, {4})
    add_avn_event("day218", "Stray Cat", "MainEvent", 1, "weekday_morning", "day217 == True and day218 == False", 218, {5})
    add_avn_event("day220", "There is Nothing", "MainEvent", 1, "saturday_morning", "((day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 16 or (amipoint + amimiss == 16)) and (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2))", 220, {6})
    # add_avn_event("hoorayanotherreset", "Changing of Seasons", "MainEvent", 1, "chain", "day220")

    #CH2MAIN
    # add_avn_event("christmas1", "Snow-Covered Footprints", "MainEvent", 2, "chain", "hoorayanotherreset")
    # add_avn_event("christmas2", "Patent-Pending", "MainEvent", 2, "chain", "christmas1")
    # add_avn_event("christmas3", "Fuck Christmas", "MainEvent", 2, "chain", "christmas2")
    # add_avn_event("christmas4", "Disappointing Everyone", "MainEvent", 2, "chain", "christmas3")
    # add_avn_event("christmas5", "Bottled Dreams", "MainEvent", 2, "chain", "christmas4")
    # add_avn_event("christmas6", "Christmas Miracle", "MainEvent", 2, "chain", "christmas5")
    # add_avn_event("christmas7", "Fireworks, Chicken, and the Innate Fear of Death", "MainEvent", 2, "chain", "christmas6")
    add_avn_event("day237", "Suicide Pact", "MainEvent", 2, "weekday_morning", "christmas7 == True and day237 == False", 237, {1})
    add_avn_event("day239", "A Door that People Move Through", "MainEvent", 2, "weekday_morning", "day237 == True and day239 == False", 239, {3})
    add_avn_event("day240", "Uta's Last Stand", "MainEvent", 2, "weekday_morning", "day239 == True and day240 == False", 240, {4})
    add_avn_event("day244", "Opposites Attract", "MainEvent", 2, "weekday_morning", "day240 == True and day244 == False", 244, {1})
    add_avn_event("day246", "All Kinds of People, All Kinds of Things", "MainEvent", 2, "weekday_morning", "day244 == True and day246 == False", 246, {3})
    add_avn_event("day247", "Caterpillar", "MainEvent", 2, "weekday_morning", "day246 == True and day247 == False", 247, {4})
    add_avn_event("day261", "Let Me Die in Spring", "MainEvent", 2, "weekday_morning", "day247 == True and kirininvite2 == True and bar35 == True and day261 == False", 261, {3})
    add_avn_event("day263", "There's Always a Chance", "MainEvent", 2, "weekday_morning", "day261 == True and day263 == False", 263, {5})
    add_avn_event("day264_avn", "Forty Degrees Below Zero", "MainEvent", 2, "weekday_morning", "day263 == True and day264 == False", 264, {1}) # weekday_morning_att03
    add_avn_event("day269", "What Could Have Been", "MainEvent", 2, "weekday_morning", "day264 == True and day269 == False", 269, {3})
    add_avn_event("day270", "What Is", "MainEvent", 2, "weekday_morning", "day269 == True and day270 == False", 270, {4})
    add_avn_event("day271", "What Was", "MainEvent", 2, "weekday_morning", "day270 == True and day271 == False", 271, {5})
    add_avn_event("day280", "Annabel Lee", "MainEvent", 2, "weekday_morning", "day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False", 280, {1})
    add_avn_event("day281", "Yuritopia", "MainEvent", 2, "weekday_morning", "day280 == True and day281 == False", 281, {2})
    add_avn_event("day282", "Birdcage", "MainEvent", 2, "weekday_morning", "day281 == True and day282 == False", 282, {3})
    add_avn_event("day283", "Survive! Grow!", "MainEvent", 2, "weekday_morning", "day282 == True and day283 == False", 283, {4})
    add_avn_event("day287", "Another Long Year", "MainEvent", 2, "weekday_morning", "day283 == True and day287 == False", 287, {1})
    add_avn_event("day288", "Adult Supervision", "MainEvent", 2, "weekday_morning", "day287 == True and day288 == False", 288, {2})
    add_avn_event("day295", "The WAP Man", "MainEvent", 2, "weekday_morning", "day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False", 295, {3})
    # add_avn_event("day295parttwo", "The Color of a Heart", "MainEvent", 2, "chain", "day295")
    add_avn_event("day297", "Call Me By Your Name", "MainEvent", 2, "weekday_morning", "day295parttwo == True and day297 == False", 297, {5})
    add_avn_event("day302", "Lives and Minds of Laymen", "MainEvent", 2, "weekday_morning", "day297 == True and day302 == False", 302, {3})
    add_avn_event("day303", "Sounds of Cicadas", "MainEvent", 2, "weekday_morning", "day302 == True and day303 == False", 303, {4})
    add_avn_event("day304", "Horses or the Whispers of the Dead", "MainEvent", 2, "weekday_morning", "day303 == True and day304 == False", 304, {5})
    add_avn_event("day318_avn", "Operation: Firestarter", "MainEvent", 2, "weekday_morning", "toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False", 318, {5})
    # add_avn_event("dormwar1", "Super Mega Ultimate Dorm War!", "MainEvent", 2, "chain", "day318")
    # add_avn_event("dormwar2", "Pre-Game Show!", "MainEvent", 2, "chain", "dormwar1")
    # add_avn_event("dormwar3", "Imouto Mode!", "MainEvent", 2, "chain", "dormwar2")
    # add_avn_event("dormwar4", "Alive & Active! All Out Athletics!", "MainEvent", 2, "chain", "dormwar3")
    # add_avn_event("dormwar5", "Friend Zone Fight!", "MainEvent", 2, "chain", "dormwar4")
    # add_avn_event("dormwar6", "Sphenopalatine Ganglioneuralgia", "MainEvent", 2, "chain", "dormwar5")
    # add_avn_event("dormwar7", "Ruthless Rhyme Rhomp! Rap Rampage!", "MainEvent", 2, "chain", "dormwar6")
    # add_avn_event("dormwar8", "Chaperone", "MainEvent", 2, "chain", "dormwar7")
    # add_avn_event("dormwar9", "Why Now?", "MainEvent", 2, "chain", "dormwar8")
    # add_avn_event("dormwar10", "In Some Cases, Love", "MainEvent", 2, "chain", "dormwar9")
    # add_avn_event("dormwar11", "The Legacy of Thaum Pt. Z: Alentha Amastacia", "MainEvent", 2, "chain", "dormwar10")
    # add_avn_event("dormwar12", "Us", "MainEvent", 2, "chain", "dormwar11")
    # add_avn_event("dormwar13", "First Last Date", "MainEvent", 2, "chain", "dormwar12")
    # add_avn_event("dormwar14", "The Scary Room", "MainEvent", 2, "chain", "dormwar13")
    # add_avn_event("dormwar15", "Fallen Angels", "MainEvent", 2, "chain", "dormwar14")
    # add_avn_event("dormwar16", "Post-Game Celebration!", "MainEvent", 2, "chain", "dormwar15")
    # add_avn_event("dormwar17", "War's End", "MainEvent", 2, "chain", "dormwar16")
    add_avn_event("day333", "Record Breaker", "MainEvent", 2, "weekday_morning", "dormwar17 == True and day333 == False", 333)
    # add_avn_event("day333part2", "Lesbian Stuff", "MainEvent", 2, "chain", "day333")
    add_avn_event("day340", "Mana Transfer", "MainEvent", 2, "weekday_morning", "utadorm20 == True and ayanedorm35 == True and day340 == False", 340, {2})
    add_avn_event("day344_avn", "The Price of Experience", "MainEvent", 2, "saturday_night", "day340 == True and amiinvite3 == True and day344 == False", 344, {6})
    # add_avn_event("thirdreset1", "Word of the Day", "MainEvent", 2, "chain", "ayanespecial1")
    # add_avn_event("thirdreset2", "Backwards Dancing", "MainEvent", 2, "chain", "thirdreset1")
    # add_avn_event("thirdreset3", "Sayonara", "MainEvent", 2, "chain", "thirdreset2")
    add_avn_event("day351", "Food Groups", "MainEvent", 2, "weekday_morning", "thirdreset3 == True and utadorm20 == True and day351 == False", 351)
    add_avn_event("day355", "Permission Slip", "MainEvent", 2, "weekday_morning", "day351 == True and day355 == False", 355)
    add_avn_event("secondbeach1_avn", "Good Morning", "MainEvent", 2, "saturday_morning", "day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False", 370, {6})
    # add_avn_event("secondbeach2", "Egg Tossing", "MainEvent", 2, "chain", "secondbeach1")
    # add_avn_event("secondbeach3", "De-Briefing the Teacher", "MainEvent", 2, "chain", "secondbeach2")
    # add_avn_event("secondbeach4", "TPK (Banana Boat)", "MainEvent", 2, "chain", "secondbeach3")
    # add_avn_event("secondbeach5", "The Next Best Thing", "MainEvent", 2, "chain", "secondbeach4")
    # add_avn_event("secondbeach6", "The Yellow Wallpaper", "MainEvent", 2, "chain", "secondbeach5")
    # add_avn_event("secondbeach7", "Everything Ephemeral (Face Forward)", "MainEvent", 2, "chain", "secondbeach6")
    # add_avn_event("secondbeach8", "The Legacy of Thaum Pt. III: Changeling", "MainEvent", 2, "chain", "secondbeach7")
    # add_avn_event("secondbeach9", "Alderaan", "MainEvent", 2, "chain", "secondbeach8")
    # add_avn_event("secondbeach10", "Torrential Downpour. Child of Man.", "MainEvent", 2, "chain", "secondbeach9")
    # add_avn_event("secondbeach11", "Getting Comfortable", "MainEvent", 2, "chain", "secondbeach10")
    # add_avn_event("secondbeach12", "Left Out in Light", "MainEvent", 2, "chain", "secondbeach11")
    # add_avn_event("secondbeach13", "We Were Angels", "MainEvent", 2, "chain", "secondbeach12")
    # add_avn_event("secondbeach14", "Lavender's Blue", "MainEvent", 2, "chain", "secondbeach13")
    # add_avn_event("secondbeach15", "Pluto Was Never Really a Planet", "MainEvent", 2, "chain", "secondbeach14")
    # add_avn_event("secondbeach16", "Try. Try. Try.", "MainEvent", 2, "chain", "secondbeach15")
    # add_avn_event("secondbeach17", "Goodnight", "MainEvent", 2, "chain", "secondbeach16")
    # add_avn_event("secondbeach18", "All is Bright. All is Beautiful.", "MainEvent", 2, "chain", "secondbeach17")
    add_avn_event("halloweentwo1_avn", "Girls in Spandex", "MainEvent", 2, "weekday_morning", "secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and halloweentwo1 == False", 400, {5})
    # add_avn_event("halloweentwo2", "Butterfly Facts", "MainEvent", 2, "chain", "halloweentwo1")
    # add_avn_event("halloweentwo3", "Immernachtreich", "MainEvent", 2, "chain", "halloweentwo2")
    # add_avn_event("halloweentwo4", "Take Me Anywhere", "MainEvent", 2, "chain", "halloweentwo3")
    # add_avn_event("halloweentwo5", "Anglerfish", "MainEvent", 2, "chain", "halloweentwo4")
    # add_avn_event("halloweentwo6", "Porcelain Labyrinth", "MainEvent", 2, "chain", "halloweentwo5")
    # add_avn_event("halloweentwo7", "The First Signs of Fraying Threads", "MainEvent", 2, "chain", "halloweentwo6")
    # add_avn_event("halloweentwo8", "Official Unofficial Double Date", "MainEvent", 2, "chain", "halloweentwo7")
    # add_avn_event("halloweentwo9", "In Circles", "MainEvent", 2, "chain", "halloweentwo8")
    # add_avn_event("halloweentwo10", "Escape Rope", "MainEvent", 2, "chain", "halloweentwo9")
    # add_avn_event("halloweentwo11", "Lavender's Green", "MainEvent", 2, "chain", "halloweentwo10")
    # add_avn_event("halloweentwo12", "Gallows Edge", "MainEvent", 2, "chain", "halloweentwo11")
    # add_avn_event("halloweentwo13", "Metal in Microwaves", "MainEvent", 2, "chain", "halloweentwo12")
    add_avn_event("christmastwo1_avn", "Three Amigos", "MainEvent", 2, "weekday_morning", "chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and christmastwo1 == False", 455, {4})
    # add_avn_event("christmastwo2", "The Reliable and Totally Legitimate Princess Imani", "MainEvent", 2, "chain", "christmastwo1")
    # add_avn_event("christmastwo3", "Room to Grow", "MainEvent", 2, "chain", "christmastwo2")
    # add_avn_event("christmastwo4", "Dodging Snowflakes", "MainEvent", 2, "chain", "christmastwo3")
    # add_avn_event("christmastwo5", "Everything Evil", "MainEvent", 2, "chain", "christmastwo4")
    # add_avn_event("christmastwo6", "Tokimeki Labyrinth", "MainEvent", 2, "chain", "christmastwo5")
    # add_avn_event("christmastwo7", "Love Set to Max (Class Warfare)", "MainEvent", 2, "chain", "christmastwo6")
    # add_avn_event("christmastwo8", "Dohoonkabhankoloos", "MainEvent", 2, "chain", "christmastwo7")
    # add_avn_event("christmastwo9", "Fear of Missing Out", "MainEvent", 2, "chain", "christmastwo8")
    # add_avn_event("christmastwo10", "Walking on Eggshells", "MainEvent", 2, "chain", "christmastwo9")
    # add_avn_event("christmastwo11", "New Age Entrepreneurs", "MainEvent", 2, "chain", "christmastwo10")
    # add_avn_event("christmastwo12", "The Smile, The Face", "MainEvent", 2, "chain", "christmastwo11")
    # add_avn_event("christmastwo13", "Shadowmeld", "MainEvent", 2, "chain", "christmastwo12")
    # add_avn_event("christmastwo14", "Chashu (A Cracked Bowl)", "MainEvent", 2, "chain", "christmastwo13")
    # add_avn_event("christmastwo15", "A Way's Away", "MainEvent", 2, "chain", "christmastwo14")
    # add_avn_event("christmastwo16", "No Escape", "MainEvent", 2, "chain", "christmastwo15")
    # add_avn_event("christmastwo17", "Spotless Mind", "MainEvent", 2, "chain", "christmastwo16")
    # add_avn_event("christmastwo18", "Me Without You", "MainEvent", 2, "chain", "christmastwo17")
    # add_avn_event("christmastwo19", "The Color White", "MainEvent", 2, "chain", "christmastwo18")
    # add_avn_event("christmastwo20", "Glued to the Sky", "MainEvent", 2, "chain", "christmastwo19")
    # add_avn_event("returntosummer1", "The Light of Last Summer", "MainEvent", 2, "chain", "amidate50p4")
    # add_avn_event("returntosummer2", "A Life of Prizes", "MainEvent", 2, "chain", "returntosummer1")
    # add_avn_event("returntosummer3", "Utinam Ne Illum Numquam Conspexissem", "MainEvent", 2, "chain", "returntosummer2")

    #CH3MAIN
    # add_avn_event("chapthree1", "The Virgin of the Apocalypse", "MainEvent", 3, "chain", "returntosummer3")
    # add_avn_event("chapthree2", "Memories", "MainEvent", 3, "chain", "chapthree1")
    # add_avn_event("chapthree3", "Empty Eyes", "MainEvent", 3, "chain", "chapthree2")
    # add_avn_event("chapthree4", "The Great Migration", "MainEvent", 3, "chain", "chapthree3")
    # add_avn_event("chapthree5", "Creatures of Habit", "MainEvent", 3, "chain", "chapthree4")
    # add_avn_event("chapthree6", "Everything Everywhere All At Once", "MainEvent", 3, "chain", "chapthree5")
    # add_avn_event("chapthree7", "Normal-ish", "MainEvent", 3, "chain", "chapthree6")
    # add_avn_event("chapthree8", "Life is Changing", "MainEvent", 3, "chain", "chapthree7")
    # add_avn_event("yumichikaspecial1", "Dead in the Water", "MainEvent", 3, "chain", "chinamidate25")
    # add_avn_event("yumiyukispecial1", "The Road to Recovery", "MainEvent", 3, "chain", "yumichikaspecial1")
    add_avn_event("imanispecial1", "No Strings Attached", "MainEvent", 3, "weekday_morning", "wakanadate15 == True and imanispecial1 == False", 535, {5})
    add_avn_event("rikaspecial1", "Metronome In Love", "MainEvent", 3, "weekday_morning", "rindorm55p2 == True and bar55 == True and rikaspecial1 == False", 541, {3})
    add_avn_event("day543", "Grief Seed", "MainEvent", 3, "weekday_morning", "rikaspecial1 == True and osakodate20 == True and day543 == False", 543, {5})
    add_avn_event("dormwartwo1_avn", "A Walk Through Hell", "MainEvent", 3, "weekday_morning", "ayanespecial50 == True and utadorm30 == True and day543 == True and chinamidate30 == True and futabainvite3 == True and imanidate5 == True and dormwartwo1 == False", 558, {5})
    # add_avn_event("dormwartwo2", "Dorm War II: Pre-Game Show", "MainEvent", 3, "chain", "dormwartwo1")
    # add_avn_event("dormwartwo3", "A Frame on a Shelf in a House", "MainEvent", 3, "chain", "dormwartwo2")
    # add_avn_event("dormwartwo4", "Gamer Girl Grindfest", "MainEvent", 3, "chain", "dormwartwo3")
    # add_avn_event("dormwartwo5", "Hiding in Plain Sight", "MainEvent", 3, "chain", "dormwartwo4")
    # add_avn_event("dormwartwo6", "She Is", "MainEvent", 3, "chain", "dormwartwo5")
    # add_avn_event("dormwartwo7", "Burden to Bear", "MainEvent", 3, "chain", "dormwartwo6")
    # add_avn_event("dormwartwo8", "Everyone", "MainEvent", 3, "chain", "dormwartwo7")
    # add_avn_event("dormwartwo9", "Midnight Mom Mosh", "MainEvent", 3, "chain", "dormwartwo8")
    # add_avn_event("dormwartwo10", "The Way it Scatters", "MainEvent", 3, "chain", "dormwartwo9")
    # add_avn_event("dormwartwo11", "Misfit Maid Madness", "MainEvent", 3, "chain", "dormwartwo10")
    # add_avn_event("dormwartwo12", "Somewhere Far From Here", "MainEvent", 3, "chain", "dormwartwo11")
    # add_avn_event("dormwartwo13", "Swimming With Sharks", "MainEvent", 3, "chain", "dormwartwo12")
    # add_avn_event("dormwartwo14", "Remove Curse", "MainEvent", 3, "chain", "dormwartwo13")
    # add_avn_event("dormwartwo15", "The Cracking of the Egg (Nothing is Beautiful)", "MainEvent", 3, "chain", "dormwartwo14")
    # add_avn_event("dormwartwo16", "World of Lines", "MainEvent", 3, "chain", "dormwartwo15")
    # add_avn_event("dormwartwo17", "Popping Off", "MainEvent", 3, "chain", "dormwartwo16")
    # add_avn_event("dormwartwo18", "Tip Your Bartender", "MainEvent", 3, "chain", "dormwartwo17")
    # add_avn_event("dormwartwo19", "Redeemer", "MainEvent", 3, "chain", "dormwartwo18")
    # add_avn_event("beachmas1", "Walk Into the Water", "MainEvent", 3, "chain", "dormwartwo19")
    # add_avn_event("beachmas2", "Imaginary Veins", "MainEvent", 3, "chain", "beachmas1")
    # add_avn_event("beachmas3", "Friends (The Maya Route)", "MainEvent", 3, "chain", "beachmas2")
    # add_avn_event("beachmas4", "Chandler's Law", "MainEvent", 3, "chain", "beachmas3")
    # add_avn_event("beachmas5", "The Chains That Bind", "MainEvent", 3, "chain", "beachmas4")
    # add_avn_event("beachmas6", "No Cumming on Christmas", "MainEvent", 3, "chain", "beachmas5")
    # add_avn_event("beachmas7", "Fetch Quest", "MainEvent", 3, "chain", "beachmas6")
    # add_avn_event("beachmas8", "A Thousand Truths", "MainEvent", 3, "chain", "beachmas7")
    # add_avn_event("beachmas9", "The Bending of Italics", "MainEvent", 3, "chain", "beachmas8")
    # add_avn_event("beachmas10", "Treasured", "MainEvent", 3, "chain", "beachmas9")
    # add_avn_event("beachmas11", "いないいない。。。ばあ！", "MainEvent", 3, "chain", "beachmas10")
    # add_avn_event("beachmas12", "Robin Hood", "MainEvent", 3, "chain", "beachmas11")
    # add_avn_event("beachmas13", "The Legacy of Thaum Pt. IV", "MainEvent", 3, "chain", "beachmas12")
    # add_avn_event("beachmas14", "On The Fence", "MainEvent", 3, "chain", "beachmas13")
    # add_avn_event("beachmas15", "To the Future With a Smile", "MainEvent", 3, "chain", "beachmas14")
    # add_avn_event("beachmas16", "Neverender", "MainEvent", 3, "chain", "beachmas15")
    # add_avn_event("beachmas17", "Moon-Touched", "MainEvent", 3, "chain", "beachmas16")
    # add_avn_event("beachmas18", "Smells of Summer", "MainEvent", 3, "chain", "beachmas17")
    # add_avn_event("beachmas19", "I Will Deliver You to the Fireflies", "MainEvent", 3, "chain", "beachmas18")
    # add_avn_event("beachmas20", "Shelter", "MainEvent", 3, "chain", "beachmas19")
    # add_avn_event("slumberreset1", "To Catch Me If I Fall", "MainEvent", 3, "chain", "beachmas20")
    # add_avn_event("slumberreset2", "Approximation", "MainEvent", 3, "chain", "slumberreset1")
    # add_avn_event("slumberreset3", "December 28, 2020 (Clay & Clockwork)", "MainEvent", 3, "chain", "slumberreset2")
    # add_avn_event("slumberreset4", "Untitled", "MainEvent", 3, "chain", "slumberreset3")
    # add_avn_event("slumberreset5", "A Thousand Years", "MainEvent", 3, "chain", "slumberreset4")
    # add_avn_event("postnodokachain1", "White-Fronted Parrot", "MainEvent", 3, "chain", "nodokaspecial30p4")
    # add_avn_event("treasureisland", "First Contact", "MainEvent", 3, "chain", "kaorispecial35")
    # add_avn_event("amispecial50mainp1", "All For You", "MainEvent", 3, "chain", "amispecial50")
    # add_avn_event("amispecial50mainp2", "From the Desk of the Ninth God", "MainEvent", 3, "chain", "amispecial50mainp1")
    add_avn_event("predormwars3", "May the Winter Come", "MainEvent", 3, "weekday_morning", "amispecial50mainp2 == True and makihornytrip4 == True and iodorm35 == True and predormwars3 == False", 620, {5})
    add_avn_event("beachwars1", "Boner on the Bus", "MainEvent", 3, "saturday_morning", "yasudorm30 == True and naospecial3 == True and tsubasaspecial20 == True and amispecial50 == True and mollydate35p2 == True and makihornytrip4 == True and ioarchery35 == True and (harukadate30 == True or harukadate30skip == True) and beachwars1 == False", None, {6}, None, {"niki_lust" : 5})
    # add_avn_event("beachwars2", "When You Snap", "MainEvent", 3, "chain", "beachwars1")
    # add_avn_event("beachwars3", "Until My Back is Broken", "MainEvent", 3, "chain", "beachwars2")
    # add_avn_event("beachwars4", "The Rest of Me", "MainEvent", 3, "chain", "beachwars3")
    # add_avn_event("beachwars5", "Hyzenthlay", "MainEvent", 3, "chain", "beachwars4")
    # add_avn_event("beachwars6", "More Human Than Human", "MainEvent", 3, "chain", "beachwars5")
    # add_avn_event("beachwars7", "Eyes Closed, Chin Up", "MainEvent", 3, "chain", "beachwars6")
    # add_avn_event("beachwars8", "Sexy Swimsuit Showdown", "MainEvent", 3, "chain", "beachwars7")
    # add_avn_event("beachwars9", "Fairytale (The End Until Tomorrow)", "MainEvent", 3, "chain", "beachwars8")
    # add_avn_event("beachwars10", "Monsters", "MainEvent", 3, "chain", "beachwars9")
    # add_avn_event("beachwars11", "Pairs in Different Places", "MainEvent", 3, "chain", "beachwars10")
    # add_avn_event("beachwars12", "Forbidden Artistry", "MainEvent", 3, "chain", "beachwars11")
    # add_avn_event("beachwars13", "Too Many Cooks", "MainEvent", 3, "chain", "beachwars12")
    # add_avn_event("beachwars14", "Judgement Day", "MainEvent", 3, "chain", "beachwars13")
    # add_avn_event("beachwars15", "Mother May I", "MainEvent", 3, "chain", "beachwars14")
    # add_avn_event("beachwars16", "Cicadian Rhythm (The Gardener)", "MainEvent", 3, "chain", "beachwars15")
    # add_avn_event("beachwars17", "Bidder's Organs", "MainEvent", 3, "chain", "beachwars16", skip_var = "beachwars17skip")
    # add_avn_event("beachwars18", "Flowerchild", "MainEvent", 3, "chain", "beachwars17")
    # add_avn_event("beachwars19", "Danger to Society", "MainEvent", 3, "chain", "beachwars18")
    add_avn_event("halloweenfour1_avn", "Eggside Octopus", "MainEvent", 3, "saturday_morning", "(amitotal == 32 and ayanetotal == 34 and chikatotal == 28 and chinamitotal == 7 and futabatotal == 34 and harukatotal == 17 and imanitotal == 5 and iototal == 17 and kaoritotal == 11 and karintotal == 9 and kirintotal == 23 and makitotal == 13 and makotototal == 30 and mayatotal == 23 and mollytotal == 18 and mikutotal == 26 and naototal == 3 and nikitotal == 10 and nodokatotal == 14 and norikototal == 15 and osakototal == 4 and otohatotal == 12 and rikatotal == 3 and rintotal == 27 and sanatotal == 26 and saratotal == 13 and toukatotal == 13 and tsubasatotal == 5 and tsukasatotal == 2 and tsuneyototal == 17 and utatotal == 17 and wakanatotal == 7 and yasutotal == 13 and yukitotal == 7 and yumitotal == 23 and (chap1point + chap2point + chap3point + chap3miss == 284))", None, {6})
    # add_avn_event("halloweenfour2", "The Tenth Step", "MainEvent", 3, "chain", "halloweenfour1")
    # add_avn_event("halloweenfour3", "BONE-TOWN", "MainEvent", 3, "chain", "halloweenfour2")
    # add_avn_event("halloweenfour4", "Try Honesty", "MainEvent", 3, "chain", "halloweenfour3")
    # add_avn_event("halloweenfour5", "Heartache", "MainEvent", 3, "chain", "halloweenfour4")
    # add_avn_event("halloweenfour6", "The King of Thebes", "MainEvent", 3, "chain", "halloweenfour5")
    # add_avn_event("halloweenfour7", "Our Fathers", "MainEvent", 3, "chain", "halloweenfour6")
    # add_avn_event("halloweenfour8", "Eighth Eye of the Wolf Spider", "MainEvent", 3, "chain", "halloweenfour7")
    # add_avn_event("halloweenfour9", "Childspawn", "MainEvent", 3, "chain", "halloweenfour8")
    # add_avn_event("halloweenfour10", "An Excerpt From a Waterlogged Journal", "MainEvent", 3, "chain", "halloweenfour9")
    # add_avn_event("halloweenfour11", "Party Animal", "MainEvent", 3, "chain", "halloweenfour10")
    # add_avn_event("halloweenfour12", "Girls Just Want to Have Fun", "MainEvent", 3, "chain", "halloweenfour11")
    # add_avn_event("halloweenfour13", "Happy Memories", "MainEvent", 3, "chain", "halloweenfour12")
    # add_avn_event("halloweenfour14", "For More Than Just Me", "MainEvent", 3, "chain", "halloweenfour13")
    # add_avn_event("halloweenfour15", "I Won't Say I'm In Love", "MainEvent", 3, "chain", "halloweenfour14")
    # add_avn_event("halloweenfour16", "The End of the World", "MainEvent", 3, "chain", "halloweenfour15")
    # add_avn_event("resetsix1", "Times New Roman", "MainEvent", 3, "chain", "halloweenfour16")
    # add_avn_event("resetsix2", "Paper City", "MainEvent", 3, "chain", "resetsix1")
    # add_avn_event("resetsix3", "Meant to Be", "MainEvent", 3, "chain", "resetsix2")
    # add_avn_event("resetsix4", "Remember to Smile", "MainEvent", 3, "chain", "resetsix3")

    #CH4MAIN
    # add_avn_event("springtime1", "The Collector", MainEvent, 4, "weekday_morning", "springtime1 == False")
    # add_avn_event("springtime2", "On the Count of Three", MainEvent, 4, "chain", "springtime1")
    # add_avn_event("springtime3", "Not the Nightingale", MainEvent, 4, "chain", "springtime2")
    # add_avn_event("springtime4", "Silver & Gold", MainEvent, 4, "chain", "springtime3")
    # add_avn_event("springtime5", "November 1st", MainEvent, 4, "chain", "springtime4")
    # add_avn_event("springtime6", "Visibly Impatient", MainEvent, 4, "chain", "springtime5")
    # add_avn_event("springtime7", "The Final Human on the Face of the Earth", MainEvent, 4, "chain", "springtime6")
    # add_avn_event("springtime8", "Actual Jesus Quotes", MainEvent, 4, "chain", "springtime7")
    # add_avn_event("springtime9", "In Regard to the Peony", MainEvent, 4, "chain", "springtime8")
    # add_avn_event("springtime10", "When the Sun Sleeps", MainEvent, 4, "chain", "springtime9")
    # add_avn_event("springtime11", "Hunger Games", MainEvent, 4, "chain", "springtime10")
    # add_avn_event("springtime12", "Shut Up & Kiss", MainEvent, 4, "chain", "springtime11")
    # add_avn_event("springtime13", "Death (And Other Sad Stuff)", MainEvent, 4, "chain", "springtime12")
    # add_avn_event("springtime14", "The Legacy of Thaum Pt. V: The Faceless Empyrean", MainEvent, 4, "chain", "springtime13")
    # add_avn_event("springtime15", "Goodnight Moon", MainEvent, 4, "chain", "springtime14")
    # add_avn_event("springtime16", "Your Blood in Spring", MainEvent, 4, "chain", "springtime15")
    # add_avn_event("springtime17", "Rhythm of a Black Heart", MainEvent, 4, "chain", "springtime16")
    # add_avn_event("springtime18", "You & Me Against the World", MainEvent, 4, "chain", "springtime17")
    # add_avn_event("springtime19", "Miserably Ever After", MainEvent, 4, "chain", "springtime18")
    # add_avn_event("springend1", "Episcopalis: Pickled Plums & Polyrhythmic Psalms", MainEvent, 4, "chain", "springtime19")
    # add_avn_event("springend2", "Okonomiyaki", MainEvent, 4, "chain", "springend1")
    # add_avn_event("springend3", "500 Channels", MainEvent, 4, "chain", "springend2")
    # add_avn_event("springend4", "Wild Boar", MainEvent, 4, "chain", "springend3")
    # add_avn_event("springend5", "All Eyes On Me", MainEvent, 4, "chain", "springend4")
    # add_avn_event("sportswars3", "War Never Changes: Egg Time Madness", MainEvent, 4, "chain", "sportswars2")
    # add_avn_event("sportswars4", "Shohei Ohtani", MainEvent, 4, "chain", "sportswars3")
    # add_avn_event("sportswars6", "Sea of Balls (Wise Turtle)", MainEvent, 4, "chain", "sportswars5")
    # add_avn_event("sportswars7", "Cock Party 2 (Better Than The First)", MainEvent, 4, "chain", "sportswars6")
    # add_avn_event("sportswars8", "Flowers & Forklifts", MainEvent, 4, "chain", "sportswars7")
    # add_avn_event("sportswars11", "David Beckham's Large Banana", MainEvent, 4, "chain", "sportswars10")
    # add_avn_event("sportswars12", "Mr. Bones' Wild Ride", MainEvent, 4, "chain", "sportswars11")
    # add_avn_event("sportswars13", "Priestess of Fallen Snow", MainEvent, 4, "chain", "sportswars12")
    # add_avn_event("sportswars15", "Trauma Bond", MainEvent, 4, "chain", "sportswars14")
    # add_avn_event("sportswars16", "Irregular Heartbeat", MainEvent, 4, "chain", "sportswars15")
    # add_avn_event("sportswars20", "Happy", MainEvent, 4, "chain", "sportswars19")
    # 042
    add_avn_event("beachfive1_avn", "From The Heart (Red Shell)", "MainEvent", 4, "weekend_morning", "imanispring2 == True and utaspring2 == True and beachfive1 == False", None, {7})
    # add_avn_event("beachfive2", "Monkey's Paw", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive4", "Operation: Sleepytime", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive5", "Sod in the Seedbed", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive7", "Recycling", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive11", "Albatross", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive12", "Pros, Cons, and Countermeasures", "MainEvent", 4, "chain", "")
    # add_avn_event("beachfive16", "Perfect Harmony", "MainEvent", 4, "chain", "")
    # 044
    add_avn_event("halloweenfive1", "Rubik’s Cube", "MainEvent", 4, "weekday_morning", "mikuspring5 == True and sanaspring4 == True  and chinamispring3 == True and wakanaspring4 == True and halloweenfive1 == False", None, {5})
    # add_avn_event("halloweenfive2", "More Than Her", "MainEvent", 4, "chain", "halloweenfive1")
    # add_avn_event("halloweenfive3", "Action/Inaction", "MainEvent", 4, "chain", "halloweenmakoto1")
    # add_avn_event("halloweenfive4", "Empty Heart Appeal", "MainEvent", 4, "chain", "halloweenami1")
    # add_avn_event("halloweenfive5", "The Art of Tribadism", "MainEvent", 4, "chain", "halloweentsuneyo1")
    # add_avn_event("halloweenfive6", "Four Walls, A Garden", "MainEvent", 4, "chain", "halloweennodoka1")
    # add_avn_event("halloweenfive7", "SENSEI-QUEST", "MainEvent", 4, "chain", "halloweenkaori2")
    # add_avn_event("halloweenfive8", "Restart", "MainEvent", 4, "chain", "endofgameworld")
    # 045
    # add_avn_event("halloweenfive9", "Recap", "MainEvent", 4, "chain", "halloweenfive8")
    # add_avn_event("halloweenfive10", "Yellow Patch (Heaven in My Hands)", "MainEvent", 4, "chain", "halloweenayane1")
    # add_avn_event("halloweenfive11", "Episcopalis: A Hymn for Him and She and Her", "MainEvent", 4, "chain", "halloweenmakoto2")
    # add_avn_event("halloweenfive12", "Sigma Grindset", "MainEvent", 4, "chain", "halloweenayane2")
    # add_avn_event("halloweenfive13", "All Around the Mulberry Bush", "MainEvent", 4, "chain", "halloweenmakoto3")
    # add_avn_event("halloweenfive14", "Pop Goes the Weasel", "MainEvent", 4, "chain", "halloweenfive13")
    # add_avn_event("halloweenfive15", "God of Light", "MainEvent", 4, "chain", "halloweenayane3")
    # add_avn_event("halloweenfive16", "Sonny Boy & The Magnificent Waiting Room", "MainEvent", 4, "chain", "halloweenfive15")
    # add_avn_event("halloweenfive17", "What We’ll See When We Get There", "MainEvent", 4, "chain", "halloweenfive16")
    # 046
    add_avn_event("christmasfive1_avn", "Aunt Niki (A Hundred Christmases)", "MainEvent", 4, "weekday_morning", "halloweenfive17 == True and christmasfive1 == False", None, {5})
    # add_avn_event("christmasfive2", "Caught in the Crossfire", "MainEvent", 4, "chain", "christmasimani2")
    # add_avn_event("christmasfive3", "The Legacy of Thaum Pt. VI: Thought Mirror", "MainEvent", 4, "chain", "christmasfive2")
    # add_avn_event("christmasfive4", "DON’T TALK TO MONKS", "MainEvent", 4, "chain", "christmasfive3")
    # add_avn_event("christmasfive5", "The One With All the Sex Toys", "MainEvent", 4, "chain", "christmastsukasa1")
    # add_avn_event("christmasfive6", "Seed of Self-Doubt", "MainEvent", 4, "chain", "christmasfutaba1intro")
    # add_avn_event("christmasfive7", "Even Heaven", "MainEvent", 4, "chain", "christmasfive6")
    # add_avn_event("christmasfive8", "Post-Nut Clarity", "MainEvent", 4, "chain", "christmasimani3")
    # 049
    add_avn_event("dormwarsfive1", "Prepare For Battle!", "MainEvent", 4, "weekday_morning", "chikaspring7 == True and rikaspring4 == True and yumispring6 == True and utaspring5 == True and toukaspring5 == True and tsuneyospring6 == True and dormwarsfive1 == False", None, {5}, None, {"imani_lust" : 5})
    # add_avn_event("dormwarsfive2", "Poetry At Best", "MainEvent", 4, "chain", "dormwarsfive1")
    # add_avn_event("dormwarsfive3", "Beach(?) Babe Breakfast Barrage!", "MainEvent", 4, "chain", "imanilust5")
    # add_avn_event("dormwarsfive4", "Dungeons & Divas! Normies Gone Nerdy!", "MainEvent", 4, "chain", "dormwarsfive3")
    # add_avn_event("dormwarsfive5", "Talentless & Talkative! Trivia Turmoil!", "MainEvent", 4, "chain", "dormwarsfive4")
    # add_avn_event("dormwarsfive6", "Sweet Joy Befall Thee! Be Nice to Sensei Battle!", "MainEvent", 4, "chain", "dormwarsfive5")
    # add_avn_event("dormwarsfive7", "Shadow Word: Death Ball", "MainEvent", 4, "chain", "dormwarsfive6")
    # add_avn_event("dormwarsfive8", "Lovely Lawyers & The Laws of...Love!", "MainEvent", 4, "chain", "dormwarsfive7")
    # add_avn_event("dormwarsfive9", "Silhouettes of Scorned Princesses", "MainEvent", 4, "chain", "dormwarsfive8")
    # add_avn_event("dormwarsfive10", "A Ghost's Guide on Haunting", "MainEvent", 4, "chain", "dormwarsfive9")
    # add_avn_event("dormwarsfive11", "Strippers? No! Swimsuits! (Pool-Toucher)", "MainEvent", 4, "chain", "dormwarsfiverin1")
    # add_avn_event("dormwarsfive12", "Goth Girl Glamour Gala!", "MainEvent", 4, "chain", "dormwarsfive11")
    # add_avn_event("dormwarsfive13", "And Then There Were Two", "MainEvent", 4, "chain", "dormwarsfive12")
    # add_avn_event("nodokathontwo1", "John 13 (From God to God)", "MainEvent", 4, "chain", "dormwarsfive13")    # nodokathontwo1miss = True
    # add_avn_event("nodokathontwo2", "Genesis 19 (Pillars of Salt)", "MainEvent", 4, "chain", "nodokathontwo1") # nodokathontwo2miss = True
    # add_avn_event("nodokathontwo3", "Thessalonians 4 (Lust Like the Pagans)", "MainEvent", 4, "chain", "nodokathontwo2")  # nodokathontwo3miss = True
    # add_avn_event("dormwarsfive14", "Partial to Jasmine", "MainEvent", 4, "chain", "nodokathontwo3")
    # 052
    add_avn_event("beachsix1", "The Legacy of Thaum", "MainEvent", 4, "saturday_morning", "(saraspring5 == True or saraspring5miss == True) and futabaspring2 == True and futabalust25 == True and chikaspring5 == True and naospring3 == True and wakanaspring6 == True and makotospring3 == True and beachsix1 == False", None, {5}, None, {"molly_lust" : 5, "sana_lust" : 5, "noriko_lust" : 5})
    # add_avn_event("beachsix2", "Natural Instinct", "MainEvent", 4, "chain", "beachsixotoha1")
    # add_avn_event("beachsix3", "Buyer's Remorse (Suicide Fund)", "MainEvent", 4, "chain", "beachsixmakoto1")
    # add_avn_event("beachsix4", "Peregrine Falcon", "MainEvent", 4, "chain", "beachsixfutaba1")
    # add_avn_event("beachsix5", "Pulling Ahead", "MainEvent", 4, "chain", "beachsix4")
    # add_avn_event("beachsix6", "Cities in Gifu", "MainEvent", 4, "chain", "beachsixtsuneyo2")
    # add_avn_event("beachsix7", "Flowers for Algernon", "MainEvent", 4, "chain", "beachsix6")
    # add_avn_event("beachsix8", "Into the Void", "MainEvent", 4, "chain", "beachsix7")
    # 053
    # add_avn_event("undeservedfuture11", "Behind the Scenes", "MainEvent", 4, "chain", "undeservedfuture10")
    # add_avn_event("undeservedfuture12", "The Web This World Has Spun", "MainEvent", 4, "chain", "undeservedfuture11")
    # add_avn_event("undeservedfuture13", "Engagement Farming", "MainEvent", 4, "chain", "undeservedfuture12")
    # add_avn_event("undeservedfuture14", "Wind Chime", "MainEvent", 4, "chain", "undeservedfuture13")
    # add_avn_event("undeservedfuture15", "F4972-B", "MainEvent", 4, "chain", "undeservedfuture14")
    # add_avn_event("undeservedfuture16", "Last Supper", "MainEvent", 4, "chain", "undeservedfuture15")
    # add_avn_event("undeservedfuture17", "All That's Left Are Stars", "MainEvent", 4, "chain", "undeservedfuture16")
    # add_avn_event("undeservedfuture18", "The First Christmalloween", "MainEvent", 4, "chain", "undeservedfuture17")
    # 054
    # add_avn_event("christmalloween1", ""Double-Bestiality", "MainEvent", 4, "chain", "undeservedfuture18")
    # add_avn_event("christmalloween2", "Pattern Recognition", "MainEvent", 4, "chain", "christmalloween1") # christmalloween2miss
    # add_avn_event("christmalloween3", "Pen & Paper", "MainEvent", 4, "chain", "yasuchristmalloween1")
    # add_avn_event("christmalloween4", "The Forest (For the Trees)", "MainEvent", 4, "chain", "christmalloween3")
    # add_avn_event("christmalloween5", "A Game of Our Own", "MainEvent", 4, "chain", "mayachristmalloween1")
    # add_avn_event("christmalloween6", "Hot Father Juice", "MainEvent", 4, "chain", "mayachristmalloween3")
    # 056
    # add_avn_event("springtimesadness1", "A Vivid Explosion of Color", "MainEvent", 4, "chain", "nikispring8")
    # add_avn_event("springtimesadness2", "The Touch of God", "MainEvent", 4, "chain", "chinamispring7")
    # 058
    add_avn_event("dormwarssix1", "One Man's Hell", "MainEvent", 4, "weekday_morning", "rinspring9 == True and iospring8 == True and toukaspring8 == True and wakanaspring8 == True and sanaspring6 == True and (chap4point + chap4miss >= 104) and (happypoint + happymiss >= 20) and dormwarssix1 == False", None, {5})
    # add_avn_event("dormwarssix2", "Athletics Abound! Keep in Shape With Karin!", "MainEvent", 4, "chain", "dormwarssix1")
    # add_avn_event("dormwarssix3", "Kaori's Chaotic Cooking Class!", "MainEvent", 4, "chain", "dormwarssix2")
    # add_avn_event("dormwarssix4", "Familial Face-Off!", "MainEvent", 4, "chain", "dormwarssix3")
    # add_avn_event("dormwarssix5", "Amplified Artistry! Drawing With Nao-chan!", "MainEvent", 4, "chain", "dormwarssix4")
    # add_avn_event("dormwarssix6", "Think Fast! Flirt Faster!", "MainEvent", 4, "chain", "dormwarssix5")
    # add_avn_event("dormwarssix7", "Trivial Trivia on Topical Topics!", "MainEvent", 4, "chain", "dormwarssixnodoka1")
    # add_avn_event("dormwarssix8", "Teenage Teacher Takedown!", "MainEvent", 4, "chain", "dormwarssix7")
    # add_avn_event("dormwarssix9", "Sea of Balls 2: Electric Boogaloo", "MainEvent", 4, "chain", "dormwarssix8")
    # add_avn_event("dormwarssix10", "Barista Beatdown: Revenge of the White People!", "MainEvent", 4, "chain", "dormwarssix9")
    # add_avn_event("dormwarssix11", "Mabby Dick (Sweetmeats for My Dolphin)", "MainEvent", 4, "chain", "dormwarssix10")
    # add_avn_event("dormwarssix12", "The Infinite Common Route", "MainEvent", 4, "chain", "dormwarssixmaya1")
    # 059
    add_avn_event("postwarsix1", "Vault of Glass", "MainEvent", 4, "weekday_morning", "dormwarssix12 == True and postwarsix1 == False", None, {4})

    # #HAPPY
    # add_avn_event("roomwithtrack", "The Room With Clocks", "HappyEvent", 1, "happy", "Visit {color=#ff4dd2}Ami{/color} and {color=#18b500}Maya{/color}'s dorm room.")
    add_avn_event("roomwithclocks", "The Room With Clocks", "HappyEvent", 1, "dorm", "roomwithclocks == True", 24)
    # add_avn_event("letterttrack", "The Letter 'T'", "HappyEvent", 1, "happy", "Visit the dorms, then choose to go home.")
    add_avn_event("lettert", "The Letter 'T'", "HappyEvent", 1, "dorm", "lettert == True")
    # add_avn_event("swimmingtrack", "Swim Trip", "HappyEvent", 1, "happy", "Choose '=D' in the weekend travel menu.", miss_preq = "amidorm10 and amifingered == False")
    add_avn_event("swimming", "Swim Trip", "HappyEvent", 1, "weekend_morning", "swimming == True", 74)   #, miss_preq = "amidorm10 and amifingered == False")
    # add_avn_event("howifeeltrack", "How I Feel", "HappyEvent", 1, "happy", "Visit the shrine.")
    add_avn_event("howifeel", "How I Feel", "HappyEvent", 1, "work2", "howifeel == True")
    # add_avn_event("connecttrack", "Everything is Connected", "HappyEvent", 1, "happy", "Visit the soccer field while the world is broken.", miss_preq = "day103 and connecttrack == False")
    # add_avn_event("specialclassroomtrack", "Turn Off The Lights", "HappyEvent", 1, "happy", "Invite {color=#18b500}Maya{/color} over during the weekend.", miss_preq = "amisroom15 and amifingered == False")
    add_avn_event("specialclassroom", "Turn Off The Lights", "HappyEvent", 1, "invite", "specialclassroom == True", None, {6,7})    #, miss_preq = "amisroom15 and amifingered == False")
    # add_avn_event("ticktocktrack", "Tick Tock Tick Tock Tick Tock", "HappyEvent", 1, "happy", "Visit {color=#ff4dd2}Ami{/color} and {color=#18b500}Maya{/color}'s dorm room.")
    add_avn_event("ticktock", "Tick Tock Tick Tock Tick Tock", "HappyEvent", 1, "dorm", "ticktock == True")
    # add_avn_event("trinity1track", "Trinity Pt. I: Stations of the Cross", "HappyEvent", 1, "happy", "Visit the dorms, then choose to go home.")
    add_avn_event("trinity1", "Trinity Pt. I: Stations of the Cross", "HappyEvent", 1, "dorm", "trinity == True")
    # add_avn_event("trinity2track", "Trinity Pt. II: Hell is Empty", "HappyEvent", 1, "happy", "Visit the ramen shop (Sunday).")
    add_avn_event("trinity2", "Trinity Pt. II: Hell is Empty", "HappyEvent", 1, "work3", "trinity2 == True", None, {7})
    # add_avn_event("trinity3track", "Trinity Pt. III: Non Est Deus", "HappyEvent", 1, "happy", "Invite XXXX over (Weekend night).")
    add_avn_event("trinity3", "Trinity Pt. III: Non Est Deus", "HappyEvent", 1, "invite", "trinity3 == True and trinity2track == True", None, {6,7})
    # add_avn_event("babyfinches", "Baby Finches", "HappyEvent", 1, "happy", "Use :)'s name as your username during There is Nothing.", miss_preq = "babyfinches == False and hoorayanotherreset")
    # add_avn_event("lesson1", "Something Everyone Knows and Ignores", "HappyEvent", 2, "happy", "Choose '6b 61 6f 72 69'", miss_preq = "lesson1 == False and thirdreset1")
    # add_avn_event("goodboy", "Good Boy", "HappyEvent", 2, "happy", "Choose to 'wait until morning' in the afternoon call menu", miss_preq = "sarabar25 and anewkey == False and goodboy == False")
    add_avn_event("goodboy", "Good Boy", "HappyEvent", 2, "work2", "anewkey == True and goodboy == False")
    # add_avn_event("lamblegs", "Lamb Legs", "HappyEvent", 2, "happy", "Win the lottery", miss_preq = "returntosummer2 and anewkey == False")
    # add_avn_event("buckettrack", "Second Sun", "HappyEvent", 3, "happy", "Visit the church (Sunday morning).")
    add_avn_event("bucketscene", "Second Sun", "HappyEvent", 3, "work1", "buckettoken == True", None, {7})
    # add_avn_event("mothersmilk", "Mother's Milk", "HappyEvent", 3, "happy", "Answer the bonus trivia question correctly.", miss_preq = "mothersmiss")
    # add_avn_event("amyevent", "Amy", "HappyEvent", 3, "happy", "Go to the mall on Sunday.")
    add_avn_event("amyevent", "Amy", "HappyEvent", 3, "work2", "letsgoexploring == True", None, {7})
    # add_avn_event("rainking", "Rain King", "HappyEvent", 3, "happy", "Enter the correct password in Ami's computer.", miss_preq = "rainkingmiss")
    # 042
    add_avn_event("armsbentback", "Arms Bent Back", "HappyEvent", 4, "dorm2", "bendyarms == True")
    # 044
    # add_avn_event("postfreddeathscene", "Kyoto", "HappyEvent", 4, "", "")
    # 045
    # add_avn_event("alexisevent", "Alexisthymia", "HappyEvent", 4, "", "")
    # 052
    # add_avn_event("swimtrip2", "Sally Sells Seashells", "HappyEvent", 4, "", "")  # swimtrip2miss

    #AMI
    add_avn_event("firsttimeamisroom", "Harem Tutorial", "Ami", 1, "work1", "firsttimeamisroom == False")
    add_avn_event("amifirsthall", "Uninvited", "Ami", 1, "dorm", "dorm > 0 and amifirsthall == False", None, {5})
    add_avn_event("amisroom5", "The Queen of Spiders", "Ami", 1, "work1", "firsttimeamisroom == True and amisroom5 == False", 30, None, {"ami_love" : 5})
    add_avn_event("amihall", "", "Ami", 1, "dorm", "amifirsthall == True and not renpy.seen_label('amihall') and amidorm5 == False and ami_love < 5", 20, {5})
    add_avn_event("amidorm5", "Home Away From Home", "Ami", 1, "dorm", "amifirsthall == True and amidorm5 == False", 25, {2,3,4,6,7}, {"ami_love" : 5})
    add_avn_event("amisroom10", "Something Darker", "Ami", 1, "work1", "amidorm5 == True and amisroom5 == True and amisroom10 == False", 35, None, {"ami_love" : 10})
    add_avn_event("aminew1", "Couple's Discount (Sea of Diamonds)", "Ami", 1, "weekday_morning", "amisroom10 == True and day24 == True and aminew1 == False", 43)
    add_avn_event("aminew2", "Ode to a Marsh Warbler", "Ami", 1, "weekend_morning", "day56 == True and aminew1 == True and aminew2 == False", 60)
    add_avn_event("amidorm10", "No One Can See Us", "Ami", 1, "dorm", "day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True", 35, {6,7}, {"ami_love" : 10})
    add_avn_event("day98", "Walking on Air", "Ami", 1, "weekday_morning", "amifingered == True and amidorm10 == True and day98 == False", 98, None, {"ami_love" : 15}, {"ami_lust" : 5})
    add_avn_event("amidorm15", "Back Out in the Heat", "Ami", 1, "dorm", "amidorm10 == True and mayadorm5 == True and amidorm15 == False", 55, {1,2,3,4,6,7}, {"ami_love" : 15})
    add_avn_event("amisroom15", "Important Things", "Ami", 1, "work1", "amidorm15 == True and amisroom15 == False", 55, None, {"ami_love" : 15})
    # add_avn_event("amilust10", "Wake Up Call", "Ami", 1, "chain_lust_adv", "ami_lust >= 20 and amifingered == True, beachvacation9", miss_preq = "beachvacation16 and amilust10 == False", None, None, {"ami_lust" : 20})
    add_avn_event("amisroom20", "Cute Girls and Stuff", "Ami", 1, "work1", "beachvacation16 == True and mayadorm25 == True and amisroom20 == False", 85, None, {"ami_love" : 20})
    add_avn_event("amidorm20", "Divergence", "Ami", 1, "dorm", "amisroom20 == True and amidorm20 == False", 85, {2,3,4,6,7}, {"ami_love" : 20})
    add_avn_event("amisroom25", "Such Small Hands", "Ami", 1, "work1", "ami_virgin == False and amidorm20 == True and amisroom25 == False", 125, None, {"ami_love" : 25})
    add_avn_event("amidorm25", "Everlasting Love", "Ami", 1, "dorm", "amidorm20 == True and amidorm25 == False", 125, {1,2,3,4,6,7}, {"ami_love" : 25})
    add_avn_event("amiinvite1", "Living", "Ami", 2, "invite", "christmas7 == True and amiinvite1 == False")
    add_avn_event("amiinvite2", "Rising to the Challenge", "Ami", 2, "invite", "amiinvite1 == True and amiinvite2 == False and amiinvite2miss == False")
    add_avn_event("amiinvite3", "Best Friends Forever", "Ami", 2, "invite", "amiinvite3 == False and shrine35 == True")
    add_avn_event("amimaid30", "Third Place", "Ami", 2, "work1", "utadorm10 == True and bar35 == True and amimaid30 == False", 185, None, {"ami_love" : 30})
    add_avn_event("amidate35", "The Big Sleep (Cute Girl Magic)", "Ami", 2, "date_afternoon", "amimaid30 == True and shrine35 == True and amidate35 == False", None, None, {"ami_love" : 35})
    add_avn_event("amidorm40", "Heaven for Human Blood", "Ami", 2, "dorm", "amidate35 == True and amidorm40miss == False and shrine35 == True and amidorm40 == False", None, {2,3,4,6,7}, {"ami_love" : 40})
    # # add_avn_event("amilust15", "As Light as Air", "Ami", 2, "chain_lust_adv", "ami_lust >= 15, ayanespecial2", skip_var = "amilust15skip")
    # # add_avn_event("amilust20", "Conscious or Not", "Ami", 2, "chain_lust_adv", "ami_lust >= 20, halloweentwo5", skip_var = "amilust20skip")
    # add_avn_event("amidate50", "Outcry of the Hunted Hare", "Ami", 2, "chain", "kaoridate25")
    # add_avn_event("amidate50p2", "Fruits of the Two Seasons", "Ami", 2, "chain", "amidate50")
    # add_avn_event("amidate50p3", "My Life With You", "Ami", 2, "chain", "amidate50p2")
    # add_avn_event("amidate50p4", "Somnambula", "Ami", 2, "chain", "amidate50p3")
    # add_avn_event("amilust35", "No One Can Hear Us", "Ami", 3, "chain_lust_adv", "ami_lust >= 50 and amifingered == True, beachmas12", skip_var = "amilust35skip")
    add_avn_event("amimaid50", "Not Safe For Work", "Ami", 3, "work1", "treasureisland == True and makotodorm55p2 == True and norikoinvite3 == True and amimaid50 == False", None, None, {"ami_love" : 50})
    add_avn_event("amiinvite4", "Mama's Girl", "Ami", 3, "invite", "kaorispecial40 == True and amimaid50 == True and amiinvite4 == False", None, None, {"ami_love" : 50})
    # add_avn_event("amispecial50", "Worry Not, The Mason Jar", "Ami", 3, "chain", "kaoridate40")
    # add_avn_event("amilust50", "Family Matters", "Ami", 3, "chain_lust_adv", "ami_lust >= 65 and amifingered == True, halloweenfour14", skip_var = "amilust50skip")
    # add_avn_event("amilust60", "The Caretaker", "Ami", 4, "chain_lust_adv", "ami_lust >= 70 and amifingered == True, springtime5", skip_var = "amilust60skip")
    # add_avn_event("amispring1", "Della", "Ami", 4, "chain", "chinamispring2")
    # add_avn_event("amicamp1", "Every Day Birds (In Nothing But Blood)", "Ami", 4, "chain", "makicamp1")
    # add_avn_event("amicamp2", "There Is A Light That Never Goes Out", "Ami", 4, "camp", 'Choose "Go back to the camp" in camp, yukicamp1')
    # 044
    # add_avn_event("halloweenami1", "Soon (Another Nightmare)", "Ami", 4, "chain", "halloweenfive3")
    # 050
    # add_avn_event("amispring2", "Faith & Sacrifice", "Ami", 4, "chain", "nikispring4")
    # add_avn_event("amispring3", "Shiritori", "Ami", 4, "chain", "nikispring6")
    # 056
    # add_avn_event("amispring4", "Nakadashi", "Ami", 4, "chain", "norikoinvite6")  # amispring4miss
    # add_avn_event("amispring5", "Victrola", "Ami", 4, "chain", "karinspring7")    # amispring5miss

    #AYANE
    add_avn_event("firsttimedojo", "The Unwavering Bravery of Ayane Amamiya", "Ayane", 1, "work2", "firsttimeshrine == True and firsttimedojo == False")
    add_avn_event("ayanefirsthall", "Spy on Me", "Ayane", 1, "dorm", "dorm > 0 and ayanefirsthall == False", None, {4})
    add_avn_event("dojo5", "The Battle for Kumon-mi", "Ayane", 1, "work2", "firsttimedojo == True and dojo5 == False", 26, None, {"ayane_love" : 5})
    add_avn_event("dojo10", "Names of Our Children", "Ayane", 1, "work2", "ayanedorm5 == True and dojo10 == False", 35, None, {"ayane_love" : 10})
    add_avn_event("ayanehall", "", "Ayane", 1, "dorm", "ayanefirsthall == True and not renpy.seen_label('ayanehall') and  ayanedorm5 == False and ayane_love < 5", 20, {4})
    add_avn_event("ayanedorm5", "Home Sweet Home", "Ayane", 1, "dorm", "ayanefirsthall == True and ayanedorm5 == False", 25, {1,2,3,5,6,7}, {"ayane_love" : 5})
    add_avn_event("ayanenew1", "Imprinting", "Ayane", 1, "date_morning", "cafesugar == True and dojo10 == True and ayanedorm5 == True and ayanenew1 == False", 35, None, {"ayane_love" : 10})
    add_avn_event("ayanenew2", "Far From Fantasy", "Ayane", 1, "work2", "ayanenew1 == True and ayanenew2 == False", 55, None, {"ayane_love" : 10})
    add_avn_event("ayanenew3", "Forever Yours (Top of the World)", "Ayane", 1, "weekday_morning", "ayanenew2 == True and ayanenew3 == False", 60)
    # add_avn_event("ayanedorm10", "Less Like the Vulture", "Ayane", 1, "chain", "ayanenew3")
    add_avn_event("ayanedorm15", "First Words", "Ayane", 1, "dorm", "ayanedorm10 == True and ayanedorm15 == False", 55, {1,2,3,5,6,7}, {"ayane_love" : 15})
    add_avn_event("day68", "Backwards Spider Crawl", "Ayane", 1, "weekday_morning", "ayanedorm10 == True and day68 == False", 68, None, {"ayane_love" : 15}, {"ayane_lust" : 5})
    add_avn_event("dojo20", "Endless Torment", "Ayane", 1, "work2", "ayanedorm15 == True and dojo20 == False", 85, None, {"ayane_love" : 20})
    add_avn_event("ayanedorm20", "Still Young", "Ayane", 1, "dorm", "dojo20 == True and ayanedorm10 == True and sanadorm15 == True and ayanedorm20 == False", 85, {6}, {"ayane_love" : 20})
    # add_avn_event("ayanelust10", "Prisoner", "Ayane", 1, "chain_lust_adv", "ayane_lust >= 20 and ayanedorm10 == True, beachvacation12", miss_preq = "beachvacation16 and ayanelust10 == False")
    add_avn_event("dojo25", "Regularly Scheduled Programming", "Ayane", 1, "work2", "halloween14 == True and ayanedorm20 == True and dojo25 == False", 125, None, {"ayane_love" : 25})
    add_avn_event("ayanedorm25", "Cold Air of an Encroaching Winter", "Ayane", 1, "dorm", "dojo25 == True and ayanedorm25 == False", 125, {1,2,3,5,6,7}, {"ayane_love" : 25})
    add_avn_event("dojo30", "First and Second", "Ayane", 1, "work2", "ayanedorm25 == True and dojo30 == False", 185, None, {"ayane_love" : 30})
    add_avn_event("ayanedorm30", "Crazier Things Have Happened", "Ayane", 1, "dorm", "dojo30 == True and ayanedorm30 == False", 185, {1,2,3,5,6,7}, {"ayane_love" : 30})
    add_avn_event("ayaneinvite1", "Hail Mary", "Ayane", 2, "invite", "christmas7 == True and ayaneinvite1 == False")
    add_avn_event("ayaneinvite2", "One of Many Rooms", "Ayane", 2, "invite", "ayaneinvite1 == True and ayaneinvite2 == False")
    # add_avn_event("ayanelust15", "What a Wonderful World", "Ayane", 2, "chain_lust_adv", "ayanelust10 == True and ayane_lust >= 35 and kirin_lust >= 25, dormwar8", skip_var = "ayanelust15skip and dormwar7")
    add_avn_event("dojo35", "Under the World Tree", "Ayane", 2, "work2", "day333part2 == True and amiinvite3 == True and dojo35 == False", None, None, {"ayane_love" : 35})
    add_avn_event("ayanedorm35", "Crash of Thunder", "Ayane", 2, "dorm", "dojo35 == True and ayanedorm35 == False", None, {1,2,3,6,7}, {"ayane_love" : 35})
    # add_avn_event("ayanespecial1", "Nevermind", "Ayane", 2, "chain", "day344")
    # add_avn_event("ayanespecial2", "Before the Sun Comes Up", "Ayane", 2, "chain", "thirdreset3")
    # add_avn_event("ayanelust20", "Out With the Old", "Ayane", 2, "chain_lust_adv", "ayane_lust >= 45, christmastwo3", skip_var = "ayanelust20skip", None, None, {"ayane_love" : 45})
    add_avn_event("ayanespecial40", "Chronokinetics (Hell Exists)", "Ayane", 3, "weekday_morning", "imanispecial1 == True and ayanespecial40 == False", 540, {2})
    add_avn_event("ayanesanabeach1", "How the World Works", "Ayane", 3, "date_morning", "ayanespecial40 == True and bar55 == True and ayanesanabeach1 == False", None, None, {"ayane_love" : 45})   #date_morning_att07
    add_avn_event("ayanespecial50", "Chiburi", "Ayane", 3, "weekday_morning", "day543 == True and ayanesanabeach1 == True and ayanespecial50 == False", 547, {1})
    add_avn_event("ayanekirintalk", "Furlough (Tell the World)", "Ayane", 3, "weekday_morning", "ayanelust15 == True and ayanespecial50 == True and ayanekirintalk == False", 550, {4})
    add_avn_event("ayanespecial55", "Double Jeopardy", "Ayane", 3, "saturday_night", "beachwars19 == True and ayanespecial55 == False", None, {6}, {"ayane_love" : 55})
    add_avn_event("ayanebonus1", "The Aforementioned Light", "Ayane", 3, "dorm", "ayanespecial55 == True and ayanecthree == True and ayanebonus1 == False", None, {1,2,3}, {"ayane_love" : 55})
    add_avn_event("ayanebonus2", "Over & Over", "Ayane", 3, "saturday_night", "ayanebonus1 == True and ayanebonus2 == False", None, {6}, {"ayane_love" : 55})
    add_avn_event("ayanepool55", "Dizzy On The Comedown", "Ayane", 3, "weekday_morning", "(ayanebonus2 == True or ayanebonus2skip == True) and ayanepool55 == False", None, {3}, {"ayane_love" : 55})
    # add_avn_event("ayanespring1", "...But Home is Nowhere", "Ayane", 4, "chain", "springend2")
    # 042
    add_avn_event("beachfive3", "Doomsayer", "Ayane", 4, "weekday_morning", "beachfive2 == True and beachfive3 == False and (rinspring3 == True or harukaspring1miss == True)", None, {5})
    # add_avn_event("beachfive15", "As You Wish", "Ayane", 4, "chain", "")
    # 045
    # add_avn_event("halloweenayane1", "Chamomile", "Ayane", 4, "chain", "halloweenfive9")
    # add_avn_event("halloweenayane2", "Time, Resets, and the Like", "Ayane", 4, "chain", "halloweenfive11")
    # add_avn_event("halloweenayane3", "Soliloquy (Wearing Someone Else's Clothes)", "Ayane", 4, "chain", "halloweenmaya3")
    # 050
    add_avn_event("ayanespring2", "In Shoes That Don't Fit", "Ayane", 4, "ch4work3", "nodokathontwo3 == True and ayanespring2 == False", None, {3})    # ayanespring2miss 
    add_avn_event("ayanespring3", "Mortal Coil", "Ayane", 4, "ch4work2", "dormwarsfive14 == True and ayanespring3 == False", None, {5})
    # 053
    # add_avn_event("undeservedfuture1", "Our Cage in Tralfamadore", "Ayane", 4, "chain", "beachsix8")
    # add_avn_event("undeservedfuture2", "Ikura", "Ayane", 4, "chain", "undeservedfuture1")
    # add_avn_event("undeservedfuture3", "A Nightmare, in Retrospect", "Ayane", 4, "chain", "undeservedfuture2")
    # add_avn_event("undeservedfuture4", "Trophy Wife Pt. I", "Ayane", 4, "chain", "undeservedfuture3")
    # add_avn_event("undeservedfuture5", "Light of My Life", "Ayane", 4, "chain", "undeservedfuture4")
    # add_avn_event("undeservedfuture6", "Infinite Joy", "Ayane", 4, "chain", "undeservedfuture5")
    # add_avn_event("undeservedfuture7", "Bitter Cherries", "Ayane", 4, "chain", "undeservedfuture6")
    # add_avn_event("undeservedfuture8", "Trophy Wife Pt. II", "Ayane", 4, "chain", "undeservedfuture7")
    # add_avn_event("undeservedfuture9", "Like Lions", "Ayane", 4, "chain", "undeservedfuture8")
    # add_avn_event("undeservedfuture10", "Aomori", "Ayane", 4, "chain", "undeservedfuture9")
    # 060
    add_avn_event("ayanespring4", "Transpacific Sadness Symposium N: CHAINSMOKER CHANGELING", "Ayane", 4, "weekday_morning", "nodokaspring3 == True and ayanespring4 == False", None, {1,2,3,4,5})

    #CHIKA
    add_avn_event("firsttimemall", "The Retail Machine", "Chika", 1, "work2", "firsttimeshrine == True and firsttimemall == False")
    add_avn_event("chikafirsthall", "A Dog that Does Math", "Chika", 1, "dorm", "dorm > 0 and chikafirsthall == False", None, {3})
    add_avn_event("mall5", "Big Shot Teacher", "Chika", 1, "work2", "firsttimemall == True and mall5 == False", 26, None, {"chika_love" : 5})
    add_avn_event("chikahall", "", "Chika", 1, "dorm", "chikafirsthall == True and not renpy.seen_label('chikahall') and chikadorm5 == False and chika_love < 5", 20, {3})
    add_avn_event("chikadorm5", "Something About Biting", "Chika", 1, "dorm", "firsttimemall == True and chikafirsthall == True and chikadorm5 == False", 25, {2,4,5,6,7}, {"chika_love" : 5})
    add_avn_event("mall10", "Behind The Curtain", "Chika", 1, "work2", "mall5 == True and mall10 == False", 55, None, {"chika_love" : 10})  #+ mall5
    add_avn_event("chikadorm10", "Side Event", "Chika", 1, "dorm", "mall10 == True and chikadorm5 == True and chikadorm10 == False", 35, {1,2,4,5,6,7}, {"chika_love" : 10})
    add_avn_event("chikadorm15", "A Castle for Everyone", "Chika", 1, "dorm", "chikadorm10 == True and chikadorm15 == False", 55, {2,4,5,6,7}, {"chika_love" : 15})
    add_avn_event("mall15", "A Dog that Doesn't Do Math", "Chika", 1, "work2", "chikadorm15 == True and day79 == True and mall15 == False", 55, None, {"chika_love" : 15})
    add_avn_event("chikadorm20", "Schadenfreude", "Chika", 1, "dorm", "beachvacation16 == True and mall15 == True and chikadorm20 == False", 85, {1,2,4,5,6,7}, {"chika_love" : 20})   # "dorm_att04"
    add_avn_event("mall20", "True Power: Unleashed", "Chika", 1, "work2", "chikadorm20 == True and mall20 == False", 85, None, {"chika_love" : 20})
    # add_avn_event("day139", "Detention", "Chika", 1, "weekday_morning", "totaldays >= 139 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_love >= 30 and day139 == False", None, None, {"chika_love" : 30})
    add_avn_event("day139", "Detention", "Chika", 1, "weekday_morning", "chikadorm20 == True and mall20 == True and day139 == False", 139, None, {"chika_love" : 30}, {"chika_lust" : 5})
    add_avn_event("chikainvite1", "A Trip to the Moon", "Chika", 1, "invite", "day139 == True and mall20 == True and chikainvite1 == False")
    add_avn_event("chikainvite2", "First Hunt", "Chika", 1, "invite", "chikainvite1 == True and chikainvite2 == False")
    # add_avn_event("chikalust10", "Baby it's Cold Outside", "Chika", 2, "chain_lust_adv_att10", "chika_lust >= 30, christmas5", miss_preq = "chikalust10miss")
    add_avn_event("chikaonsen1", "Little Miracles", "Chika", 2, "date_morning", "yumicallnight35 == True and day271 == True and streets30 == True and chikaonsen1 == False", None, {6})     #date_morning_att05
    # add_avn_event("chikaonsen2", "Bleed", "Chika", 2, "chain", "chikaonsen1")
    # add_avn_event("chikaonsen3", "Three Words", "Chika", 2, "chain", "chikaonsen2")
    # add_avn_event("chikaonsen4", "Zanzibar (Counting Cats)", "Chika", 2, "chain", "chikaonsen3")
    # add_avn_event("chikalust15", "The Princess & The Pauper", "Chika", 2, "chain_lust_adv", "chika_lust >= 35, dormwar16", skip_var = "chikalust15skip")
    # add_avn_event("chikalust20", "Into the Woods", "Chika", 2, "chain_lust_adv", "chika_lust >= 20, secondbeach10", skip_var = "chikalust20skip")
    add_avn_event("chikaspecial40", "In Search of Summer", "Chika", 2, "weekday_morning", "kirindorm25 == True and chikaspecial40 == False", 424, {1})
    add_avn_event("mall40", "Self Care", "Chika", 2, "work2", "chikaspecial40 == True and mall40 == False", None, None, {"chika_love" : 40})
    # add_avn_event("mall40p2", "The Gap in the Curtain", "Chika", 2, "chain", "mall40")
    add_avn_event("chikadate45", "The Gap in the Door", "Chika", 2, "date_morning", "mall40p2 == True and chikadate45 == False", None, None, {"chika_love" : 45})
    # add_avn_event("chikalust25", "Mating Season", "Chika", 3, "chain_lust_adv", "chika_lust >= 50, dormwartwo13", skip_var = "chikalust25skip")
    add_avn_event("mall45", "Rough Cuts", "Chika", 3, "work2", "nikilovesyou3 == True and shrine40 == True and mall45 == False", None, None, {"chika_love" : 45})
    add_avn_event("chikaspecial45", "Curry Night", "Chika", 3, "date_afternoon", "mall45 == True and chikaspecial45 == False", None, None, {"chika_love" : 45, "tsubasa_love" : 15})
    add_avn_event("chikadorm45_avn", "Our Time Atop This Mattress", "Chika", 3, "dorm", "tsubasaspecial15 == True and chikadorm45 == False", None, {1,2,4,5,6,7}, {"chika_love" : 45})    #dorm_att08
    # add_avn_event("chikaspring1", "Gold Digger", "Chika", 4, "chain", "springend5")
    # add_avn_event("chikaspring2", "Original Sin", "Chika", 4, "chain", "chikaspring1")
    add_avn_event("chikaspring3", "To Drink, To Drown", "Chika", 4, "weekday_morning", "chikaspring3 == False", None, {4})
    # 043
    # add_avn_event("chikaspring4", "Rabies", "Chika", 4, "chain", "yumispring3")
    # 047
    add_avn_event("chikaspring5", "Frogging", "Chika", 4, "weekend_afternoon", "harukaspring4 == True and futabalust25 == True and chikaspring5 == False")
    add_avn_event("chikaspring6", "Everyone I've Ever Loved", "Chika", 4, "ch4work2", "chikaspring5 == True and chikaspring6 == False", None, None, {"chika_love" : 40})
    # add_avn_event("chikaspring7", "Transpacific Sadness Symposium V: NEW BLACK PARADIGM", "Chika", 4, "chain", "chikaspring6")
    # 051
    add_avn_event("chikaspring8", "Chika-chan vs. Auto-Pilot", "Chika", 4, "ch4work2", "yumispring8 == True and chikaspring8 == False", None, {6,7})
    # 054
    # add_avn_event("chikachristmalloween1", "A Violent Sort of Sadness", "Chika", 4, "chain", "christmalloween4")
    # add_avn_event("chikachristmalloween2", "See You in School", "Chika", 4, "chain", "restofyasumallow")

    #CHINAMI
    add_avn_event("chinamidate1", "5,000 Year-Old Wizard", "Chinami", 1, "date_morning", "chinaminumber == True and chinamidate1 == False")  #+ chinaminumber == True
    add_avn_event("chinamigenmorning", "", "Chinami", 1, "date_morning", "chinaminumber == True and chinamidate1 == True and christmas7 == False and not renpy.seen_label('chinamigenmorning') and chinami_love < 5")
    # add_avn_event("chinamigenafternoon", "", "Chinami", 1, "date_afternoon", "chinaminumber == True and chinamidate1 == True and christmas7 == False and not renpy.seen_label('chinamigenafternoon') and chinami_love < 5")
    add_avn_event("chinamidate5", "Chinami-Corp", "Chinami", 1, "date_afternoon", "chinamidate1 == True and day128 == True and chinamidate5 == False", 194, None, {"chinami_love" : 5})
    add_avn_event("chinamidate10", "Giant Pool of Jell-O", "Chinami", 2, "date_morning", "christmas7 == True and chinamidate10 == False", None, None, {"chinami_love" : 10})
    add_avn_event("chinamidate15", "Pool Party (Love & Puppies)", "Chinami", 2, "date_morning", "day355 == True and chinamidate15 == False", None, None, {"chinami_love" : 15})
    add_avn_event("chinamidate20", "Happy Hour", "Chinami", 2, "date_afternoon", "chinamidate15 == True and chinamidate20 == False", None, None, {"chinami_love" : 20})
    add_avn_event("chinamidate25", "Death Trap", "Chinami", 3, "date_morning", "tsukasaspecial1p2 == True and chinamidate25 == False", None, None, {"chinami_love" : 25})
    add_avn_event("chinamidate30", "Bad News Bears", "Chinami", 3, "work2", "yumiyukispecial1 == True and chinamidate30 == False", None, None, {"chinami_love" : 30})
    # add_avn_event("chinamispring1", "Lucky (China Doll)", "Chinami", 4, "chain", "chikaspring2")
    # add_avn_event("chinamispring2", "Holden Caulfield", "Chinami", 4, "chain", "chinamispring1")
    # 043
    add_avn_event("chinamispring3_avn", "Backwards Boulevard", "Chinami", 4, "weekend_morning", "chikaspring4 == True and chinamispring3 == False", None, {6,7})
    # add_avn_event("chinamispring4", "Feed Me to the Farm", "Chinami", 4, "chain", "chinamispring3")
    # 051
    # add_avn_event("chinamispring5", "Obnoxious Sexual Rampage", "Chinami", 4, "chain", "tsukasaspring5")  # chinamispring5miss
    # add_avn_event("chinamispring6", "Five Hundred Pancakes", "Chinami", 4, "chain", "chinamispring5")     # chinamispring6miss
    # 056
    # add_avn_event("chinamispring7", "My Adventures as a Trash Compactor", "Chinami", 4, "chain", "springtimesadness1")
    # add_avn_event("chinamispring8", "Transpacific Sadness Symposium IX: HUNG HIGH IN THE HARE HOUSE", "Chinami", 4, "chain", "springtimesadness2")

    #FUTABA
    add_avn_event("firsttimelibrary", "Impossible Blossoms", "Futaba", 1, "work1", "firsttimeshrine == True and firsttimelibrary == False")
    add_avn_event("futabafall", "Fan Fiction", "Futaba", 1, "work1", "firsttimelibrary == True and futabafall == False", 30, None, {"futaba_love" : 5})
    add_avn_event("library10", "Upside Down", "Futaba", 1, "work1", "futabafall == True and library10 == False", 35, None, {"futaba_love" : 10})
    add_avn_event("futabafirsthall", "Unidentical Twins", "Futaba", 1, "dorm", "dorm > 0 and futabafirsthall == False", None, {2})
    add_avn_event("futabahall", "", "Futaba", 1, "dorm", "futabafirsthall == True and not renpy.seen_label('futabahall') and futabafirstvisit == False and futaba_love < 5", 20, {2})
    add_avn_event("futabafirstvisit", "Under the Radar", "Futaba", 1, "dorm", "futabafirsthall == True and futabafall == True and futabafirstvisit == False", 25, None, {"futaba_love" : 5})
    add_avn_event("futabadorm10", "Cutting Through Cocoons", "Futaba", 1, "dorm", "futabafirstvisit == True and futabadorm10 == False", 35, {1,3,4,5,6,7}, {"futaba_love" : 10})
    add_avn_event("library15", "Self-Insert", "Futaba", 1, "work1", "library10 == True and futabadorm10 == True and library15 == False", 55, None, {"futaba_love" : 15})
    add_avn_event("futabanew1", "Broken Flowers", "Futaba", 1, "dorm", "library15 == True and futabanew1 == False", 55, {1,3,4,5,6,7}, {"futaba_love" : 15}) 
    add_avn_event("futabanew2", "Great Burdock Leaves", "Futaba", 1, "weekday_morning", "futabanew1 == True and day72 == True and futabanew2 == False", 64)
    add_avn_event("futabanew3", "Clam's Tongue", "Futaba", 1, "dorm", "futabanew2 == True and mikudorm10 == True and futabanew3 == False", 55, {1,3,4,5,6,7}, {"futaba_love" : 15}) 
    add_avn_event("futabadorm15", "Legs of a Dying Spider", "Futaba", 1, "dorm", "futabanew3 == True and futabadorm15 == False", 55, {1,3,4,5,6,7}, {"futaba_love" : 15}) 
    add_avn_event("library20", "Only Child", "Futaba", 1, "work1", "library15 == True and library20 == False", 90, None, {"futaba_love" : 20}) #+ library15 == True and
    add_avn_event("library25", "A Book About Dragons", "Futaba", 1, "work1", "futabanew3 == True and library20 == True and library25 == False", 125, None, {"futaba_love" : 25}) 
    add_avn_event("futabadorm25", "Two Hours", "Futaba", 1, "dorm", "futabadorm15 == True and bookdate == True and futabadorm25 == False", 125, {6,7}, {"futaba_love" : 25})
    add_avn_event("day86", "Like Fucking a Cloud", "Futaba", 1, "weekday_morning", "futabadorm15 == True and day86 == False", 86, {5}, {"futaba_love" : 20}, {"futaba_lust" : 5})
    add_avn_event("library30", "Under the Table", "Futaba", 1, "work1", "futabadorm25 == True and beachvacation16 == True and library25 == True and library30 == False", 185, None, {"futaba_love" : 30}) 
    add_avn_event("futabadorm30", "A Tree Falls in the Forest", "Futaba", 1, "dorm", "library30 == True and futabadorm30 == False", 185, {1,2,4,6,7}, {"futaba_love" : 30}) 
    add_avn_event("library35", "No, You", "Futaba", 1, "work1", "rindorm35 == True and futabadorm30 == True and library35 == False", 195, None, {"futaba_love" : 35})
    add_avn_event("futabadorm35", "Overload", "Futaba", 1, "dorm", "library35 == True and futabadorm35 == False", 195, {1,3,4,5,6,7}, {"futaba_love" : 35})
    # add_avn_event("futabalust10", "Selfless", "Futaba", 2, "chain_lust_adv_att10", "futaba_lust >= 35, christmas6", miss_preq = "futabalust10miss")
    add_avn_event("futabainvite1", "Sonnet 18", "Futaba", 2, "invite", "christmas7 == True and futabainvite1 == False")
    add_avn_event("futabainvite2", "Floral Aura", "Futaba", 2, "invite", "futabainvite1 == True and futabainvite2 == False")
    # add_avn_event("futabalust15", "C'est La Vie", "Futaba", 2, "chain_lust_adv", "futaba_lust >= 40 and nodokadorm5 == True, dormwar9", skip_var = "futabalust15skip and dormwar9")
    add_avn_event("futabadorm40", "Skin (Start Somewhere)", "Futaba", 2, "dorm", "dormwar17 == True and futabadorm40 == False", None, {1,4,5,6,7}, {"futaba_love" : 40}) 
    add_avn_event("library40", "Shadowplay", "Futaba", 2, "work1", "futabadorm40 == True and yumicallnight35 == True and kaoridate15p3 == True and library40 == False", None, None, {"futaba_love" : 40}) 
    # add_avn_event("library40part2", "Without Running Away", "Futaba", 2, "chain", "library40")
    add_avn_event("futabadorm45", "Hall of Mirrors", "Futaba", 2, "dorm", "library40part2 == True and futabadorm45 == False", None, {1,4,5}, {"futaba_love" : 45}) 
    add_avn_event("futabadorm50", "This Infected Wound", "Futaba", 3, "dorm", "makiinv3 == True and futabadorm50 == False", None, {1,3,4,5,6,7}, {"futaba_love" : 50}) 
    add_avn_event("library50", "Bestial Vigor", "Futaba", 3, "work1", "futabadorm50 == True and library50 == False", None, None, {"futaba_love" : 50}) 
    add_avn_event("futabainvite3", "Too Blind To See", "Futaba", 3, "invite", "library50 == True and futabainvite3 == False")
    # add_avn_event("makotofutabafuntimelustevent", "Toys", "Futaba", 3, "chain_lust_adv", "makoto_lust >= 55 and futaba_lust >= 55, beachmas11", skip_var = "makotofutabalustskip")
    add_avn_event("futabaspecial60p1", "Book Burning", "Futaba", 3, "dorm", "beachwars19 == True and futabaspecial60p1 == False", None, {7}, {"futaba_love" : 60}) 
    # add_avn_event("futabaspecial60p2", "Pg. 99", "Futaba", 3, "chain", "futabaspecial60p1")
    # add_avn_event("futabaspecial60p3", "Fish Eyes", "Futaba", 3, "chain", "futabaspecial60p2")
    # 041
    add_avn_event("futabalust25", "Weapons of Mass Destruction", "Futaba", 4, "dorm", "yasuspring3 == True and futabalust25 == False", None, None, None, {"futaba_lust" : 25})
    # add_avn_event("futabaspring1", "My Curse", "Futaba", 4, "chain", "futabalust25")
    # 042
    # add_avn_event("beachfive9", "Transpacific Sadness Symposium II: SISTER SOFTSKIN", "Futaba", 4, "chain", "")
    # 046
    # add_avn_event("futabalust40", "The Meat in the Hole in the Wall in My Room", "Futaba", 4, "chain", "christmasfive5")
    # 051
    add_avn_event("futabaspring2", "The Taking Tree", "Futaba", 4, "ch4work1", "dormwarsfive14 == True and futabaspring2 == False", None, None, {"futaba_love" : 25})
    # 052
    # add_avn_event("beachsixfutaba1", "Spam", "Futaba", 4, "chain", "beachsix3")
    # 059
    add_avn_event("futabaspring3", "ELATION PROTOCOL 99: RE:SOLUTION (RESOLVED)", "Futaba", 4, "ch4work2", "postwarsix1 == True and futabaspring3 == False", None, {1,2,3,4,5})
    add_avn_event("futabaspring4", "New Ways to Love", "Futaba", 4, "ch4work1", "futabaspring3 == True and futabaspring4 == False", None, {6,7}, {"futaba_love" : 60})

    #HARUKA
    add_avn_event("harukadate1", "Drunk Again", "Haruka", 1, "date_night", "haruka_love >= 0 and day89 == True and harukadate1 == False")
    add_avn_event("harukacafegen", "", "Haruka", 1, "work1", "harukadate1 == True and christmas7 == False and not renpy.seen_label('harukacafegen') and haruka_love < 5", 96)
    add_avn_event("harukadate5", "Invisible Worm", "Haruka", 1, "date_night", "harukadate1 == True and harukadate5 == False", 129, None, {"haruka_love" : 5}) # date_night_att01
    add_avn_event("harukagennight", "", "Haruka", 1, "date_night", "harukadate5 == True and christmas7 == False and not renpy.seen_label('harukagennight') and haruka_love < 10")
    add_avn_event("harukafirstlust", "The Need to be Hurt", "Haruka", 1, "work1", "harukadate5 == True and harukasex == True and harukafirstlust == False", 136, None, {"haruka_love" : 10}, {"haruka_lust" : 5}) #miss_preq = "harukadate5 and harukasex == False" 
    # add_avn_event("harukalust10", "Bad Kitty", "Haruka", 1, "chain_lust_adv", "haruka_lust >= 10 and harukasex == True, halloween14", miss_preq = "halloween14 and harukalust10 == False")
    add_avn_event("harukadate10", "Performance Review", "Haruka", 1, "work1", "halloween14 == True and harukadate5 == True and rindorm35 == True and harukadate10 == False", None, None, {"haruka_love" : 10}) 
    add_avn_event("harukadate15", "Watching TV Alone", "Haruka", 1, "date_night", "harukadate10 == True and harukadate15 == False", None, None, {"haruka_love" : 15}) 
    add_avn_event("harukainvite1", "Shades of Green", "Haruka", 2, "invite", "christmas7 == True and harukainvite1 == False")
    add_avn_event("harukainvite2", "Roses", "Haruka", 2, "invite", "harukainvite1 == True and harukaskipped == False and harukainvite2 == False")
    add_avn_event("harukadate20", "Sober-ish", "Haruka", 2, "date_night", "dormwar17 == True and harukainvite1 == True and harukadate20 == False", None, None, {"haruka_love" : 20}) 
    add_avn_event("harukainvite3", "Unfiltered Tap Water", "Haruka", 2, "invite", "harukainvite3 == False and harukadate20 == True and harukasex == True")  #miss_preq = "harukadate20 and harukasex == False"
    # add_avn_event("sadgirls2", "The World Outside The Walls", "Haruka", 3, "chain", "sadgirls1", skip_var = "sadgirls2skip and sadgirls1")
    # add_avn_event("sadgirls4", "To Anyone Who Passes By", "Haruka", 3, "chain", "sadgirls3")
    # add_avn_event("sadgirls5", "Again, I Can't Recall", "Haruka", 3, "chain", "sadgirls4")
    # add_avn_event("harukalust25", "Secret Weapon", "Haruka", 3, "chain_lust_adv", "saralust20 == True and haruka_lust >= 30 and sara_lust >= 35, dormwartwo9", skip_var = "harukalust25skip")
    add_avn_event("makihornytrip1", "Stress Level Midnight", "Haruka", 3, "date_morning", "harukaresortticket == True", None, {6})
    # add_avn_event("makihornytrip4", "Conflict of Interest", "Haruka", 3, "chain", "makihornytrip1")
    add_avn_event("harukadate30", "Scum", "Haruka", 3, "date_night", "makihornytrip4 == True and harukasex == True and harukadate30 == False", None, None, {"haruka_love" : 30})  #skip_var = "harukadate30skip and makihornytrip4", 
    # add_avn_event("harukacamp1", "Small Paper Cups", "Haruka", 4, "camp", 'Choose "Bond with Haruka" in camp, amicamp2')
    add_avn_event("harukaspring1", "Subhuman", "Haruka", 4, "ch4work3", "mollyspring2 == True and harukasex == True and harukaspring1miss == False and harukaspring1 == False", None, {2})
    # 041
    add_avn_event("harukaspring2", "Limp-Dicked Loser", "Haruka", 4, "ch4work1", "yasuspring3 == True and harukaspring1 == True and harukaspring2 == False", None, {6,7}) # miss_preq = "harukaspring2miss")
    # 047
    add_avn_event("harukaspring3", "This Town, On its Knees", "Haruka", 4, "ch4work3", "sanainvite2 == True and harukasex == True and harukaspring3 == False", None, {3}) # miss_preq = "harukaspring3miss")
    add_avn_event("harukaspring4", "JR East's DC Tilting EMU E353 Series (Kaiji)", "Haruka", 4, "ch4work3", "cafeclosed == False and rinspring6 == True and harukaspring4 == False", None, {4})
    # 054
    # add_avn_event("harukachristmalloween1", "Traitor's Mark", "Haruka", 4, "chain", "chikachristmalloween1")  # harukachristmalloween1miss
    # add_avn_event("harukachristmalloween2", "Blood in the Water", "Haruka", 4, "chain", "mayachristmalloween3")  # harukachristmalloween2miss
    # 060
    add_avn_event("harukaspring5", "Ancient Dragons", "Haruka", 4, "ch4work3", "harukachristmalloween2 == True and dormwarssixsara1 == True and harukaspring5 == False", None, {3})         # harukaspring5miss
    add_avn_event("harukaspring6", "Camelopardalis (At Hoshimachi Station)", "Haruka", 4, "ch4work3", "harukaspring5 == True and harukaspring6 == False", None, None, {"haruka_love" : 40})  # harukaspring5miss

    #IMANI
    add_avn_event("imanidate1", "Somewhere I Belong", "Imani", 3, "date_night", "imani_love > 0 and wakanaspecial15 == True and imanidate1 == False")
    add_avn_event("imanidate5", "A Hairline Fracture", "Imani", 3, "date_night", "imanidate1 == True and imanidate5 == False", None, None, {"imani_love" : 5})
    add_avn_event("imanidate15p1", "Knotted Up", "Imani", 3, "weekday_morning", "rikadive1 == True and futabaspecial60p3 == True and wakanadate25p3 == True and imanidate15p1 == False", 625, None, {"imani_love" : 15})
    # add_avn_event("imanidate15p2", "Arm's Length", "Imani", 3, "chain", "imanidate15p1")
    add_avn_event("imanispecial15", "Debbie Downer", "Imani", 3, "weekend_night", "imanidate15p2 == True and imanispecial15 == False", None, None, {"imani_love" : 15})
    # 041
    # add_avn_event("imanispring1", "Antoa Suo Nyamaa", "Imani", 4, "chain", "wakanaspring2")
    # add_avn_event("imanispring2", "I Will Carry You, My Light", "Imani", 4, "chain", "imanispring1")
    # 046
    # add_avn_event("christmasimani1", "Yehoshua" "Imani", 4, "chain", "christmasfive1")
    # add_avn_event("christmasimani2", "The Truman Show", "Imani", 4, "chain", "christmasimani1")
    # add_avn_event("christmasimani3", "Now & Forever", "Imani", 4, "chain", "christmasfive7")
    # 049
    # add_avn_event("imanilust5", "The Devil's Bed", "Imani", 4, "chain", "dormwarsfive2")
    # 055
    # add_avn_event("imanispring3", "Lesbian Hand Stuff", "Imani", 4, "chain", "rikaspring5")
    # add_avn_event("imanispring4", "Lost in the Sauce (Pied Piper)", "Imani", 4, "chain", "rikaspring6")

    #IO
    add_avn_event("iofirsthall", "Viva la Revolución", "Io", 2, "dorm2", "day247 == True and iofirsthall == False", None, {2})
    add_avn_event("iohall", "", "Io", 2, "dorm2", "iofirsthall == True and not renpy.seen_label('iohall') and io_love < 4", None, {2})
    add_avn_event("bathhousegen", "", "Io", 2, "work2", "bathhouse1 == True and not renpy.seen_label('bathhousegen') and io_love < 4")
    add_avn_event("bathhouse1", "Nonetheless, I'm Here", "Io", 2, "work2", "day247 == True and bathhouse1 == False")
    add_avn_event("bathhouse5", "The Girl with the Dragon Tattoo", "Io", 2, "work2", "bathhouse1 == True and bathhouse5 == False", None, None, {"io_love" : 5})
    add_avn_event("iodorm5", "Unnamed Wooden Robots", "Io", 2, "dorm2", "iofirsthall == True  and bathhouse5 == True and iodorm5 == False", None, {1,3,4,5,6,7}, {"io_love" : 5})    #+ iofirsthall == True  and 
    add_avn_event("iodorm10", "Paperthin", "Io", 2, "dorm2", "iodorm5 == True and iofirsthall == True and iodorm10 == False", None, {1,3,4,5,6,7}, {"io_love" : 10})
    add_avn_event("bathhouse10", "Turn On The Lights", "Io", 2, "work2", "dormwar17 == True and bathhouse10 == False", None, None, {"io_love" : 10})
    add_avn_event("iodorm15", "Amongst Other Things", "Io", 2, "dorm2", "bathhouse10 == True and iodorm15 == False", None, {1,3,4,6,7}, {"io_love" : 15})
    add_avn_event("bathhouse20", "One Man's Trash", "Io", 2, "work2", "iodorm15 == True and bathhouse20 == False", None, None, {"io_love" : 20})
    # add_avn_event("bathhouse20part2", "Another Man's Treasure", "Io", 2, "chain", "bathhouse20")
    add_avn_event("ioarchery1", "Cupid's Arrow", "Io", 3, "work2", "makiinv3 == True and ioarchery1 == False", None, None, {"io_love" : 20}) # hint_girl = Uta, 
    add_avn_event("bathhouse25", "Work Less, Not Hard", "Io", 3, "work2", "ioarchery1 == True and bathhouse25 == False", None, None, {"io_love" : 25})
    add_avn_event("iodorm25", "Heartbreak & Harmony", "Io", 3, "dorm2", "bathhouse25 == True and iodorm25 == False", None, {1,3,4,6,7}, {"io_love" : 25})
    add_avn_event("iospecial30", "1999 PC Classic, Rollercoaster Tycoon", "Io", 3, "saturday_morning", "utamaid25p2 == True and iodorm25 == True and iospecial30 == False", None, {6})
    add_avn_event("bathhouse35p1", "Tennis Ball", "Io", 3, "work2", "amispecial50mainp2 == True and bathhouse35p1 == False", None, None, {"io_love" : 35})
    # add_avn_event("bathhouse35p2", "Hold You Over", "Io", 3, "chain", "bathhouse35p1")
    add_avn_event("iodorm35", "Yellow Cactus Flower", "Io", 3, "dorm2", "bathhouse35p2 == True and iodorm35 == False", None, {1,4,6,7}, {"io_love" : 35})
    add_avn_event("ioarchery35", "Two Of Us Are Thinking", "Io", 3, "date_morning", "iodorm35 == True and predormwars3 == True and ioarchery35 == False", None, None, {"io_love" : 35})
    # 041
    add_avn_event("iospring1", "My Indigo (The Blue Death)", "Io", 4, "ch4work3", "yasuspring3 == True and iospring1 == False", None, {1,2,3,4,5})
    # add_avn_event("iospring2", "Komorebi", "Io", 4, "chain", "iospring1")
    # add_avn_event("iospring3", "Stomachache", "Io", 4, "chain", "iospring2", miss_preq = "iospring3miss")
    # 047
    add_avn_event("iospring4", "1997 PC Classic, Theme Hospital", "Io", 4, "ch4work2", "sanainvite2 == True and iospring4 == False", None, {7})
    add_avn_event("iospring5", "Even Winning Feels Bad", "Io", 4, "ch4work3", "iospring4 == True and iospring5 == False", None, {7})
    # 049
    # add_avn_event("dormwarsfiveio1", "Endless Black (Sea of Nothing)", "Io", 4, "chain", "dormwarsfive10")
    # 055
    add_avn_event("iospring6", "Man-Meat", "Io", 4, "ch4work2", "christmalloween6 == True and iospring6 == False and rikaspring5 == True", None, {1,2,3}, {"io_love" : 40})
    # add_avn_event("iospring7", "Animal Cruelty", "Io", 4, "chain", "iospring6")   # iospring7miss 
    add_avn_event("iospring8", "The Hatchery", "Io", 4, "ch4work2", "iospring6 == True and rinspring9 == True and iospring8 == False", None, {5})

    #KAORI
    add_avn_event("kaoridate1", "How to Date a Human", "Kaori", 1, "date_morning", "kaorinumber == True and kaoridate1 == False")
    add_avn_event("kaorigenmorning", "", "Kaori", 1, "date_morning", "kaorinumber == True and kaoridate1 == True and not renpy.seen_label('kaorigenmorning') and kaori_love < 5", 130)
    add_avn_event("kaorigenafternoon", "", "Kaori", 1, "date_afternoon", "kaorinumber == True and kaoridate1 == True and not renpy.seen_label('kaorigenafternoon') and kaori_love < 5", 130)
    add_avn_event("kaoridate5", "The Best Ways to Rub a Cock", "Kaori", 1, "date_afternoon", "halloween14 == True and dojo25 == True and tsuneyofirsthall == True and kaoridate1 == True and kaoridate5 == False", None, None, {"kaori_love" : 5})
    add_avn_event("kaoridate10", "Objects and Appendages", "Kaori", 1, "date_morning", "kaoridate5 == True and kaoridate10 == False", None, None, {"kaori_love" : 10})
    add_avn_event("kaoridate15", "To Die, To Sleep", "Kaori", 2, "date_morning", "day271 == True and yumicallnight35 == True and kaoridate15 == False", None, None, {"kaori_love" : 15})
    # add_avn_event("kaoridate15p2", "Sad Girl Special", "Kaori", 2, "chain", "kaoridate15")
    # add_avn_event("kaoridate15p3", "Clouds", "Kaori", 2, "chain", "kaoridate15p2")
    add_avn_event("kaoridate20", "Såsom i en Spegel", "Kaori", 2, "date_night", "mayafestival4 == True and kaoridate20 == False", None, None, {"kaori_love" : 20})
    add_avn_event("kaoridate25", "Wither", "Kaori", 2, "date_night", "((chap1point + chap2point >= 200) and (happypoint + happymiss >= 13) and (chikapoint + chikamiss >= 23) and (yumipoint >= 20) and (ayanepoint + ayanemiss >= 26) and (sanapoint + sanamiss >= 22) and (makotopoint + makotomiss >= 22) and (mikupoint >= 21) and (rinpoint + rinmiss >= 24) and (futabapoint + futabamiss >= 27) and (amipoint + amimiss >= 22) and (nikipoint >= 6) and (mayapoint + mayamiss >= 20) and (mollypoint >= 14) and (tsuneyopoint >= 14) and (utapoint >= 9) and (iopoint >= 9) and (otohapoint >= 9) and (nodokapoint >= 5) and (toukapoint >= 9) and (yasupoint >= 5) and (norikopoint >= 11) and (kirinpoint + kirinmiss >= 19) and (wakanapoint >= 2) and (osakopoint >= 2) and (yukipoint >= 4) and (tsubasapoint >= 2) and (sarapoint + saramiss >= 10) and (harukapoint + harukamiss >= 10) and (karinpoint + karinmiss >= 7) and (kaoripoint >= 7) and (makipoint + makimiss >= 7) and (chinamipoint >= 5) and kaoridate25 == False)", 480, {6}) #chapter_end
    add_avn_event("kaorispecial35", "Where the Trees Live", "Kaori", 3, "date_night", "toukadorm25p3 == True and mayaspecial45 == True and nikilovesyou3 == True and nodokaspecial30p4 == True and kaorispecial35 == False", None, None, {"kaori_love" : 35})
    add_avn_event("kaorispecial40", "Human Females", "Kaori", 3, "weekday_morning", "makotodorm55p2 == True and treasureisland == True and kaorispecial40 == False", 609, {2}, {"kaori_love" : 40})
    add_avn_event("kaoridate40", "Run, Rabbit, Run (Why the Fieldmice Hide)", "Kaori", 3, "date_night", "kaorispecial40 == True and toukadorm25p3 == True and amiinvite4 == True and kaoridate40 == False", None, {6}, {"kaori_love" : 40})
    # add_avn_event("kaoricamp1", "Tree Village (The Color Machine)", "Kaori", 4, "camp", 'Choose "Treasure hunt with Kaori" in camp, yukicamp1')
    # add_avn_event("kaoricamp2", "Il Cervo", "Kaori", 4, "camp", 'Choose "Play games with Kaori" in camp, amicamp2')
    # 044
    # add_avn_event("halloweenkaori1", "Friend", "Kaori", 4, "chain", "halloweennao2")
    # add_avn_event("halloweenkaori2", "Kittens", "Kaori", 4, "chain", "halloweenkaori1")
    # 051
    add_avn_event("kaorispring1", "Seas of White (Why Not Here?)", "Kaori", 4, "ch4work3", "yumispring8 == True and kaorispring1 == False and (tsubasaspring4 == True or tsubasaspring4miss == True)", None, None, {"kaori_love" : 45})
    add_avn_event("kaorispring2", "Clearer Skies & Changing Eyes", "Kaori", 4, "ch4work3", "naospring1 == True and kaorispring2 == False", None, None, {"kaori_love" : 45})
    # add_avn_event("kaorispring3", "Breeding Material", "Kaori", 4, "chain", "kaorispring2")
    # 057
    add_avn_event("kaoriinvite1", "Borrowed Flesh", "Kaori", 4, "invite", "naospring4 == True and kaoriinvite1 == False")
    # add_avn_event("kaoriinvite2", "Scatter the Ashes", "Kaori", 4, "chain", "kaoriinvite1")

    #KARIN
    add_avn_event("karinsoccergen", "", "Karin", 1, "work1", "soccer20 == True and christmas7 == False and not renpy.seen_label('karinsoccergen') and karin_love < 5")
    add_avn_event("karindate1", "Further and Further", "Karin", 1, "date_afternoon", "karinnumber == True and karindate1 == False")
    add_avn_event("karingenafternoon", "", "Karin", 1, "date_afternoon", "karindate1 == True and not renpy.seen_label('karingenafternoon') and karin_love < 5")
    add_avn_event("karindate5", "Walking Penis Monster", "Karin", 1, "date_afternoon", "day103 == True and karindate5 == False", 129, None, {"karin_love" : 5})
    add_avn_event("karindate10", "If Only", "Karin", 1, "date_afternoon", "mollycafe1 == True and karindate10 == False", 165, None, {"karin_love" : 10})
    add_avn_event("karindate15", "Dying Alone With Ten Cats", "Karin", 2, "date_afternoon", "day264 == True and karinlied == True and karindate15 == False", None, None, {"karin_love" : 15}) # miss_preq = "day264 and karinlied == False",
    add_avn_event("karinsoccer15", "Tendrils of Flame", "Karin", 2, "work1", "day271 == True and karinsoccer15 == False", None, None, {"karin_love" : 15})
    add_avn_event("karinsoccer20", "The Adventures of Karli & Steve", "Karin", 2, "work1", "day351 == True and karinsoccer20 == False", None, None, {"karin_love" : 20})
    add_avn_event("karindate20", "Sweet Tooth", "Karin", 2, "date_afternoon", "day355 == True and karinsoccer20 == True and karindate20 == False", None, None, {"karin_love" : 20})
    add_avn_event("karindate25", "Emerald Eyes", "Karin", 3, "date_afternoon", "makiinv3 == True and karindate25 == False", None, None, {"karin_love" : 25})
    add_avn_event("karindate30", "Wrong Places/Wrong Times", "Karin", 3, "date_afternoon", "karindate25 == True and karindate30 == False", None, None, {"karin_love" : 30})
    add_avn_event("karinspring1", "Touch of Grey", "Karin", 4, "ch4work1", "yumispring2 == True and karinspring1 == False", None, {2})
    # add_avn_event("karinspring2", "Paranoid", "Karin", 4, "chain", "mikuspring2")
    add_avn_event("karinspring3", "Better Boy", "Karin", 4, "ch4work1", "karinspring2 == True and karinspring3 == False", None, {7})
    # 043
    add_avn_event("karinspring4", "Back to the Basics", "Karin", 4, "ch4work2", "beachfive16 == True and karinspring4 == False", None, {6,7})
    # 048
    add_avn_event("karinspring5", "A Trip to Uzbekistan", "Karin", 4, "ch4work2", "christmasfive8 == True and karinspring5 == False", None, {1,2,3,4,5})
    # add_avn_event("karinspring6", "Top 10 Thoughts to Think", "Karin", 4, "chain", "karinspring")
    # 056
    add_avn_event("karinspring7", "Oatmeal Raisin", "Karin", 4, "weekend_night", "kirinspring2 == True and karinspring7 == False", None, {6,7}) # karinspring7miss

    #KIRIN
    add_avn_event("kirinsoccergen", "", "Kirin", 1, "work1", "soccer20 == True and christmas7 == False and not renpy.seen_label('kirinsoccergen') and kirin_love < 5")
    add_avn_event("kirindate1", "Partners in Crime", "Kirin", 1, "date_afternoon", "kirinnumber == True and kirindate1 == False")
    add_avn_event("kiringenafternoon", "", "Kirin", 1, "date_afternoon", "kirindate1 == True and christmas7 == False and not renpy.seen_label('kiringenafternoon') and kirin_love < 5")
    add_avn_event("kirindate5", "Long and Hard", "Kirin", 1, "date_night", "kirindate1 == True and beachvacation16 == True and kirindate5 == False", 185, None, {"kirin_love" : 5})
    add_avn_event("kirindate10", "Politics! Pleasure! Ponies!", "Kirin", 1, "date_afternoon", "kirindate5 == True and kirindate10 == False", None, None, {"kirin_love" : 10})
    add_avn_event("kirinlust5", "Full Blossom", "Kirin", 2, "work1", "christmas7 == True and kirinlust5 == False", None, None, {"kirin_love" : 5}, {"kirin_lust" : 5})
    add_avn_event("kirininvite1", "Too Much, All at Once", "Kirin", 2, "invite", "christmas7 == True and kirininvite1 == False")
    add_avn_event("kirininvite2", "No Extortion Necessary", "Kirin", 2, "invite", "kirininvite1 == True and kirininvite2 == False")
    add_avn_event("kirinfirsthall", "Morals vs. Orgasms", "Kirin", 2, "dorm2", "day271 == True and kirinfirsthall == False", None, {4})    #firsthall
    add_avn_event("kirindorm10", "Love, Dorms, and Other Things", "Kirin", 2, "dorm2", "kirinfirsthall == True and day271 == True and utadorm5 == True and iodorm5 == True and kirindorm10 == False", None, {1,2,5,6,7}, {"kirin_love" : 10})
    add_avn_event("kirinsoccer15", "Flickering Spotlight", "Kirin", 2, "work1", "kirindorm10 == True and kirinsoccer15 == False", None, None, {"kirin_love" : 15})
    add_avn_event("kirinsoccer20", "Enigmatology", "Kirin", 2, "work1", "kirinsoccer15 == True and kirinsoccer20 == False", None, None, {"kirin_love" : 20})
    add_avn_event("kirindorm15", "Bye Bye, Boner", "Kirin", 2, "dorm2", "kirinsoccer20 == True and kirindorm15 == False", None, {1,2,5,6,7}, {"kirin_love" : 15})
    add_avn_event("kirindorm20", "Terms & Conditions", "Kirin", 2, "dorm2", "kirindorm15 == True and kirindorm20 == False", None, {1,2,5,6,7}, {"kirin_love" : 20})
    add_avn_event("kirindate25", "All That is Contaminated", "Kirin", 2, "date_night", "kirindorm20 == True and kirinlust5 == True and kirindate25 == False", None, None, {"kirin_love" : 25})
    # add_avn_event("kirinlust20", "Taking the Reins", "Kirin", 2, "chain_lust_adv", "kirin_lust >= 30, secondbeach6", skip_var = "kirinlust20skip")
    # add_avn_event("kirinspecial25", "Dyed Orange, Drenched in Sun", "Kirin", 2, "chain", "convenience25", skip_var = "kirinspecial25skip")
    add_avn_event("kirindorm25", "Temporary Bliss", "Kirin", 2, "dorm2", "norikodorm25 == True and kirindorm25 == False", None, {1,2,5,6,7}, {"kirin_love" : 25})
    add_avn_event("kirinsoccer25", "Four Hand Massage", "Kirin", 2, "work1", "kirindorm25 == True and kirinsoccer25 == False and dormwar17 == True", None, None, {"kirin_love" : 25})
    add_avn_event("kirinspecial30", "Made Out of Nothing", "Kirin", 2, "weekday_morning", "kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False", 410, None, {"kirin_love" : 30})   #skip_var = "kirinspecial30skip"
    # add_avn_event("kirinlust202", "The Other Half", "Kirin", 2, "chain_lust_adv", "kirin_lust >= 35, christmastwo9", skip_var = "kirinlust202skip")
    # add_avn_event("kirinlust30", "Falling Asleep Standing Up", "Kirin", 3, "chain_lust_adv_att09", "kirin_lust >= 40 and miku_lust >= 55 and mikucostumewin == True, dormwartwo18", skip_var = "kirinlust30skip")
    add_avn_event("kirinspecial40", "At the Edge of the Riverbank", "Kirin", 3, "work3", "mikuinvite2 == True and norikodate30 == True and kirinspecial40 == False", None, None, {"kirin_love" : 40})   #hint_girl = Noriko,
    add_avn_event("kirinspecial45p1", "Never Enough", "Kirin", 3, "weekday_morning", "kirinspecial40 == True and kirinspecial45p1 == False", 590, {3}, {"kirin_love" : 45})
    # add_avn_event("kirinspecial45p2", "Salmon Onigiri", "Kirin", 3, "chain", "kirinspecial45p1")
    # add_avn_event("sportswars9", "Rubber Traits", "Kirin", 4, "chain", "sportswars8")
    # add_avn_event("sportswars18", "Girls Vs. Robots", "Kirin", 4, "chain", "sportswars17")
    # 041
    add_avn_event("kirinspring1", "Clockless Watch", "Kirin", 4, "weekend_afternoon", "norikospring1 == True and kirinspring1 == False", None, {6})
    # 046
    # add_avn_event("christmaskirin1", "Solar Eclipse", "Kirin", 4, "chain", "christmasfive4")
    # add_avn_event("christmaskirin2", "Animal Control", "Kirin", 4, "chain", "christmaskirin1")
    # 054
    # add_avn_event("kirinchristmalloween1", "Perfect Days", "Kirin", 4, "chain", "harukachristmalloween2")  # kirinchristmalloween1miss
    # add_avn_event("kirinchristmalloween2", "Transpacific Sadness Symposium VII: ANTFARM ANTECHAMBER", "Kirin", 4, "chain", "kirinchristmalloween1")  # kirinchristmalloween2miss
    # 056
    add_avn_event("kirinspring2", "Love, Love, Love", "Kirin", 4, "weekday_morning", "norikoinvite5 == True and kirinchristmalloween2 == True and kirinspring2 == False", None, {1,2,3,4})  # kirinspring2miss
    # 060
    add_avn_event("kirinspring3", "In the Morning, In the Cold", "Kirin", 4, "weekday_morning", "makotospring5 == True and kirinspring3 == False", None, {1})
    add_avn_event("kirinspring4", "Failed Attempts at Arson", "Kirin", 4, "ch4work2", "mayaspring5 == True and kirinspring4miss == False and kirinspring4 == False", None, {6})    # kirinspring4miss    

    #MAKI
    add_avn_event("makidate1", "Beautiful Porn Salesman", "Maki", 1, "date_night", "maki_love >= 0 and mollycafe1 == True and pornshop15 == True and makidate1 == False")
    add_avn_event("makigennight", "", "Maki", 1, "work3", "makiblock == False and makidate1 == True and christmas7 == False and not renpy.seen_label('makigennight') and maki_love < 5") 
    add_avn_event("makigenafternoon", "", "Maki", 1, "date_afternoon", "makiblock == False and makidate1 == True and christmas7 == False and not renpy.seen_label('makigenafternoon') and maki_love < 5")
    add_avn_event("makidate5", "Maki Miyamura's Mom-Mode Mission", "Maki", 1, "work3", "makotodorm25 == True and makidate1 == True and bar30 == True and makidate5 == False", None, None, {"maki_love" : 5})
    add_avn_event("makidate10", "A Fair Trade", "Maki", 2, "work3", "christmas7 == True and makidate10 == False", None, None, {"maki_love" : 10})     #date_work_att06
    # add_avn_event("makiday351", "Three Afloat On One Raft", "Maki", 2, "chain", "day351")
    add_avn_event("makidate15", "Thank You For Your Business", "Maki", 2, "work3", "makiday351 == True and harukalust10 == True and makibj == True and makidate15 == False", None, None, {"maki_love" : 15})   #miss_preq = "makiday351 and makibj == False or makiday351 and harukalust10 == False"
    add_avn_event("makiinvite1", "Traveling Lube Dealer", "Maki", 2, "invite", "halloweentwo13 == True and makiinvite1 == False")
    add_avn_event("makiinvite2", "Special Occasions", "Maki", 2, "invite", "makiinvite1 == True and makiinvite2 == False")   # invite_att01
    # add_avn_event("sadgirls3", "Adulting", "Maki", 3, "chain", "sadgirls2")
    # add_avn_event("sadgirls6", "Rolling Stop (Turned Backwards)", "Maki", 3, "chain", "sadgirls5")
    add_avn_event("makiinv3", "Baby Steps", "Maki", 3, "invite", "sadgirls8 == True and makiinv3 == False", None , {7})
    add_avn_event("makihornyquestintro", "The Maltese Falcon", "Maki", 3, "work3", "nodokaspecial30p4 == True and amispecial50 == True and makihornyquestintro == False", None, None, {"maki_love" : 25})
    # add_avn_event("makihornytrip2", "Shut Up & Cum", "Maki", 3, "chain", "makihornytrip1", skip_var = "harumakihornyskip and makihornytrip1")
    # add_avn_event("makihornytrip3", "Rotting From the Inside Out", "Maki", 3, "chain", "makihornytrip2")
    add_avn_event("makicamp1", "Wires...and the Concept of Breathing", "Maki", 4, "saturday_night", "sportswars20 == True and makicamp1 == False", None , {6})
    #  add_avn_event("makicamp2", "A Place Between the Trees", "Maki", 4, "camp", 'Choose "Fish with Maki" in camp, yukicamp1')
    # 041
    add_avn_event("makilust5", "To Boldly Go...", "Maki", 4, "ch4work3", "yasuspring3 == True and makisex == True and makilust5 == False", None, None, None, {"maki_lust" : 5}) # miss_preq = "makilust5miss")
    # 048
    add_avn_event("makispring1", "Sex Box Memories", "Maki", 4, "ch4work3", "christmasfive8 == True and osakospring6 == True and makispring1 == False", None, None, {"maki_love" : 30})
    # add_avn_event("makispring2", "Hello Alone", "Maki", 4, "chain", "makispring1")
    # 055
    add_avn_event("makispring3", "ASS", "Maki", 4, "ch4work3", "osakospring9 == True and mikulust5 == True and makispring3 == False", None, None, {"maki_love" : 35})
    # add_avn_event("makispring4", "Budd Dwyer", "Maki", 4, "chain", "makispring3")
    # add_avn_event("makispring5", "A Million Tiny Pieces ", "Maki", 4, "chain", "makispring4")

    #MAKOTO
    add_avn_event("firsttimepornshop", "Unexpected Profession", "Makoto", 1, "work3", "firsttimeshrine == True and firsttimepornshop == False")
    add_avn_event("makotofirsthall", "Teacher's Pet", "Makoto", 1, "dorm", "dorm > 0 and makotofirsthall == False", None, {4}) 
    add_avn_event("pornshop5", "Watching Porn Alone", "Makoto", 1, "work3", "firsttimepornshop == True and pornshop5 == False", 25, None, {"makoto_love" : 5})
    add_avn_event("makotohall", "", "Makoto", 1, "dorm", "makotoblock == False and makotofirsthall == True and not renpy.seen_label('makotohall') and makotodorm5 == False and makoto_love < 5", 10, {4})
    add_avn_event("makotodorm5", "Completely Platonic", "Makoto", 1, "dorm", "firsttimepornshop == True and makotofirsthall == True and makotodorm5 == False", 25, {1,2,3,5,6,7}, {"makoto_love" : 5}) 
    add_avn_event("pornshop10", "Rising of the Tide", "Makoto", 1, "work3", "pornshop5 == True and day38 == True and pornshop10 == False", 35, None, {"makoto_love" : 10})
    add_avn_event("makotonew1", "Frogger", "Makoto", 1, "weekday_morning", "pornshop10 == True and makotonew1 == False", 55)
    add_avn_event("makotonew2", "Sowing the Seeds", "Makoto", 1, "work3", "makotonew1 == True and makotodorm5 == True and makotonew2 == False", 55, None, {"makoto_love" : 15}) 
    add_avn_event("makotonew3", "Egg Tooth", "Makoto", 1, "work3", "makotonew2 == True and makotonew3 == False", 85, {5,6}, {"makoto_love" : 20}) 
    add_avn_event("pornshop15", "Fishing For Love", "Makoto", 1, "work3", "makotonew3 == True and pornshop15 == False", 55, None, {"makoto_love" : 15}) 
    add_avn_event("makotolust5", "Quid Pro Quo", "Makoto", 1, "work3", "makotonew3 == True and makotolust5 == False", 110, None, {"makoto_love" : 25}, {"makoto_lust" : 5})
    add_avn_event("makotoinvite1", "Declaration of War", "Makoto", 1, "invite", "makotolust5 == True and day77 == True and makotoinvite1 == False")
    add_avn_event("makotoinvite2", "Studious Teen Virgin", "Makoto", 1, "invite", "makotoinvite1 == True and makotoinvite2 == False")
    add_avn_event("pornshop20", "Aftermath", "Makoto", 1, "work3", "halloween14 == True and pornshop15 == True and pornshop20 == False", 85, None, {"makoto_love" : 20}) 
    add_avn_event("makotodorm20", "Residual Sadness", "Makoto", 1, "dorm", "makidate1 == True and pornshop20 == True and makotodorm20 == False", 85, {1,3,5,6,7}, {"makoto_love" : 20}) 
    add_avn_event("pornshop25", "Service Charge", "Makoto", 1, "work3", "makotodorm20 == True and pornshop25 == False", 85, None, {"makoto_love" : 20}) 
    add_avn_event("makotodorm25", "Bluejay", "Makoto", 1, "dorm", "makotofirsthall == True and pornshop25 == True and trinity3track == True and mikudorm30 == True and makotodorm25 == False", None, {1,2,3,5,6,7}, {"makoto_love" : 25}) 
    add_avn_event("makotolust10", "Semblance of a Soul", "Makoto", 2, "weekday_morning", "christmas7 == True and makotolust10 == False", 230, None, {"makoto_love" : 30}, {"makoto_lust" : 10}) 
    add_avn_event("makotowinterbeach1", "Condoms in the Sand", "Makoto", 2, "date_afternoon", "day283 == True and soccer35 == True and mayadorm35 == True and makotowinterbeach1 == False", None, {6})
    # add_avn_event("makotowinterbeach2", "Humans With Hollow Bones", "Makoto", 2, "chain", "makotowinterbeach1")
    # add_avn_event("makotowinterbeach3", "I'm Not Here", "Makoto", 2, "chain", "makotowinterbeach2")
    # add_avn_event("makotowinterbeach4", "Something, Somewhere", "Makoto", 2, "chain", "makotowinterbeach3")
    # add_avn_event("makotolust20", "Hot Water", "Makoto", 2, "chain_lust_adv", "makoto_lust >= 40, secondbeach13", skip_var = "makotolust20skip")
    # add_avn_event("sadgirls1", "Whispers of the World", "Makoto", 3, "chain", "nodokaspecial20")
    # add_avn_event("sadgirls7", "Parallelogram", "Makoto", 3, "chain", "sadgirls6")
    # add_avn_event("makotolust30", "White Oak Doors", "Makoto", 3, "chain_lust_adv", "makoto_lust >= 50, sadgirls7", skip_var = "makotolust30skip")
    add_avn_event("sadgirls8", "A Beautiful Mind", "Makoto", 3, "weekday_morning", "sadgirls7 == True and sadgirls8 == False", None, {5})
    add_avn_event("makotospecial50", "Young Cardinals", "Makoto", 3, "weekday_morning", "slumberreset5 == True and makotospecial50 == False", 600, None, {"makoto_love" : 50})
    add_avn_event("makotopool55", "Cool Sex Tips", "Makoto", 3, "date_afternoon", "mikuinvite2 == True and makotospecial50 == True and makotopool55 == False", None, None, {"makoto_love" : 55})
    add_avn_event("makotodorm55p1", "Bra Shopping", "Makoto", 3, "dorm", "yukidate20p2 == True and shrine40 == True and makotopool55 == True and makotodorm55p1 == False", None, {1,3,4,5}, {"makoto_love" : 55})
    # add_avn_event("makotodorm55p2", "Suffer the Same", "Makoto", 3, "chain", "makotodorm55p1")
    # add_avn_event("sportswars19", "The Pit of Despair", Makoto, 4, "chain", "sportswars18")
    # 043
    add_avn_event("makotospring1", "Midnight Snack", "Makoto", 4, "ch4date_afternoon", "toukaspring3 == True and makotospring1 == False", None, None, {"makoto_love" : 55})
    # add_avn_event("makotospring2", "T Is For Time (Trees & Threes)", "Makoto", 4, "chain", "mikuspring5")
    # 044
    # add_avn_event("halloweenmakoto1", "Six Ways From Sunday", "Makoto", 4, "chain", "halloweenfive2")
    # 045
    # add_avn_event("halloweenmakoto2", "Precious Little Life", "Makoto", 4, "chain", "halloweenmaya1")
    # add_avn_event("halloweenmakoto3", "Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR", "Makoto", 4, "chain", "halloweenmaya2")
    # 051
    add_avn_event("makotospring3", "The World, Alive (Ant Farm)", "Makoto", 4, "ch4work1", "wakanaspring5 == True and makotospring3 == False", None, {6,7})
    # 052
    # add_avn_event("beachsixmakoto1", "Black Mass", "Makoto", 4, "chain", "beachsixnoriko1")
    # add_avn_event("beachsixmakoto2", "A Matter of Time", "Makoto", 4, "chain", "beachsix5")
    # 060
    add_avn_event("makotospring4", "This Penis, Eternal", "Makoto", 4, "ch4work3", "tsuneyospring8 == True and makotospring4 == False", None, {5}, {"makoto_love" : 60})
    add_avn_event("makotospring5", "Code Red", "Makoto", 4, "ch4work3", "makotospring4 == True and makotospring5 == False", None, {6})

    #MAYA
    add_avn_event("firsttimeshrine", "A New Beginning", "Maya", 1, "work2", "firsttimeshrine == False")
    add_avn_event("mayafirsthall", "Mondays", "Maya", 1, "dorm", "dorm > 0 and mayafirsthall == False and firsttimeshrine == True", None, {1}) 
    add_avn_event("shrine5", "Different Worlds", "Maya", 1, "work2", "firsttimeshrine == True and shrine5 == False", 26, None, {"maya_love" : 5})
    add_avn_event("mayahall", "", "Maya", 1, "dorm", "mayafirsthall == True and not renpy.seen_label('mayahall') and mayadorm5 == False and maya_love < 5", 20, {1})
    add_avn_event("mayadorm5", "Secrets Worth Keeping", "Maya", 1, "dorm", "mayafirsthall == True and amidorm5 == True and mayadorm5 == False", 25, {2,3,4,6,7}, {"maya_love" : 5})
    add_avn_event("shrine10", "Past/Present/Future", "Maya", 1, "work2", "shrine5 == True and shrine10 == False", 35, None, {"maya_love" : 10}) 
    add_avn_event("mayadorm10", "Rewind/Repeat/Refuse", "Maya", 1, "dorm", "shrine10 == True and mayadorm5 == True and mayadorm10 == False", 35, {2,3,4,6,7}, {"maya_love" : 10})
    add_avn_event("shrine15", "You and Me", "Maya", 1, "work2", "shrine10 == True and mayadorm10 == True and shrine15 == False", 55, None, {"maya_love" : 15})
    add_avn_event("mayadorm15", "Takoyaki", "Maya", 1, "dorm", "shrine15 == True and mayadorm15 == False", 55, {2,3,4,6,7}, {"maya_love" : 15})
    add_avn_event("shrine20", "Nothing is Real", "Maya", 1, "work2", "beachvacation16 == True and mayadorm15 == True and shrine20 == False", 85, None, {"maya_love" : 20})
    add_avn_event("mayadorm20", "Close Your Eyes", "Maya", 1, "dorm", "shrine20 == True and yumidorm10 == True and mayadorm20 == False", 85, {2,3,4,6,7}, {"maya_love" : 20})
    add_avn_event("shrine25", "Watermelons and Violin", "Maya", 1, "work2", "mayadorm20 == True and shrine25 == False", 125, None, {"maya_love" : 25})
    add_avn_event("mayadorm25", "FLAVOR BEAM!", "Maya", 1, "dorm", "shrine25 == True and mayadorm25 == False", 125, {2,3,4,6,7}, {"maya_love" : 25})
    add_avn_event("mayadorm30", "What it Means to Be Destroyed", "Maya", 2, "dorm", "mayadorm25 == True and norikoinvite2 == True and mayadorm30 == False", None, {2,3,4,6,7})
    add_avn_event("shrine30", "Now More Than Ever", "Maya", 2, "work2", "mayadorm30 == True and ami_virgin == False and shrine30 == False", 185, None, {"maya_love" : 30})   #miss_preq = "mayadorm30 and ami_virgin",
    add_avn_event("mayadorm35", "A Place That Can Only Exist in Our Minds", "Maya", 2, "dorm", "mayadorm30 == True and nikidate5 == True and mayadorm35 == False", None, {6,7}, {"maya_love" : 35})
    add_avn_event("shrine35", "Stop Looking For Answers", "Maya", 2, "work2", "mayadorm35 == True and shrine35 == False", 185, None, {"maya_love" : 30})
    add_avn_event("mayafestival1", "Somewhere Inside of a Dream", "Maya", 2, "saturday_morning", "christmastwo20 == True and mayafestival1 == False", 464, {6})
    # add_avn_event("mayafestival2", "Three Halves Make a Whole (Itadakimasu)", "Maya", 2, "chain", "mayafestival1")
    # add_avn_event("mayafestival3", "As The Sun Disappears", "Maya", 2, "chain", "mayafestival2")
    # add_avn_event("mayafestival4", "Everlasting Mercy", "Maya", 2, "chain", "mayafestival3")
    add_avn_event("shrine40", "The Sun, And All Its Toxic Rays", "Maya", 3, "work2", "nikilovesyou3 == True and shrine40 == False", None, None, {"maya_love" : 40})
    add_avn_event("mayadate45", "Anything & Everything", "Maya", 3, "date_night", "shrine40 == True and norikodorm30 == True and mayadate45 == False")
    add_avn_event("mayaspecial45", "A Brutal, Violent Creaming", "Maya", 3, "weekday_morning", "yukidate25 == True and mayadate45 == True and norikoinvite3 == True and mayaspecial45 == False", 597, {3}, {"maya_love" : 45})
    # add_avn_event("sportswars5", "The Motherland Calls!", "Maya", 4, "chain", "sportswars4")
    # add_avn_event("sportswars10", "Miraculous Human-Glue", "Maya", 4, "chain", "sportswars9")
    # add_avn_event("sportswars14", "Radio Silence", "Maya", 4, "chain", "sportswars13")
    # 045
    # add_avn_event("halloweenmaya1", "The Girl Who Leapt Through Time", "Maya", 4, "chain", "halloweenfive10")
    # add_avn_event("halloweenmaya2", "Wake Up (My Story)", "Maya", 4, "chain", "halloweenfive12")
    # add_avn_event("halloweenmaya3", "Right as Rain", "Maya", 4, "chain", "halloweenfive14")
    # 050
    add_avn_event("mayaspring1", "Billy Pilgrim", "Maya", 4, "ch4work3", "yumispring7 == True and mayaspring1 == False", None, {1,2,3,4,5})
    # add_avn_event("mayaspring2", "A Second Haunting", "Maya", 4, "chain", "mayaspring1")
    # add_avn_event("mayaspring3", "My Perfect World", "Maya", 4, "chain", "mayaspring2")
    # 054
    # add_avn_event("mayachristmalloween1", "Tying the Knot", "Maya", 4, "chain", "nodokachristmalloween3")
    # add_avn_event("mayachristmalloween2", "This Room and Everything in It", "Maya", 4, "chain", "mayachristmalloween2")
    # add_avn_event("mayachristmalloween3", "Something to Do With Love", "Maya", 4, "chain", "mayaspring2")
    # 058
    # add_avn_event("dormwarssixmaya1", "Ground Zero", "Maya", 4, "chain", "dormwarssix11")
    # 060
    add_avn_event("mayaspring4", "Ode on the Death of a Favorite Cat Drowned in a Tub of Goldfishes", "Maya", 4, "ch4work2", "makotospring5 == True and lingeriechoicemaya == True and mayaspring4miss == False and mayaspring4 == False", None, {6})     # mayaspring4miss 
    add_avn_event("mayaspring5", "The War Invalid", "Maya", 4, "ch4work2", "makotospring5 == True and mayaspring5 == False", None, {7})

    #MIKU
    add_avn_event("firsttimesoccer", "Daytime Stalking Pass", "Miku", 1, "work1", "firsttimeshrine == True and firsttimesoccerfield == False")
    add_avn_event("mikufirsthall", "Behind Closed Doors", "Miku", 1, "dorm", "dorm > 0 and mikufirsthall == False", None, {2})   
    add_avn_event("soccer5", "It's Always Sunny in Kumon-mi", "Miku", 1, "work1", "firsttimesoccerfield == True and soccer5 == False", 30, None, {"miku_love" : 5})
    add_avn_event("mikuhall", "", "Miku", 1, "dorm", "mikufirsthall == True and mikublock == False and not renpy.seen_label('mikuhall') and mikudorm5 == False and miku_love < 5", 20, {2})
    add_avn_event("mikudorm5", "Broken Bones", "Miku", 1, "dorm", "mikufirsthall == True and firsttimesoccerfield == True and mikudorm5 == False", 25, {1,3,4,5,6,7}, {"miku_love" : 5})
    add_avn_event("soccer10", "Nightvision", "Miku", 1, "work1", "soccer5 == True and soccer10 == False", 35, None, {"miku_love" : 10}) 
    add_avn_event("mikudorm10", "You and Me and the Night", "Miku", 1, "dorm", "soccer10 == True and mikudorm10 == False", 35, {1,3,4,5,6,7}, {"miku_love" : 10})
    add_avn_event("soccer15", "Hormones Running Wild", "Miku", 1, "work1", "day83 == True and mikudorm10 == True and soccer15 == False", 55, None, {"miku_love" : 15})
    add_avn_event("mikudorm15", "Moments Like This", "Miku", 1, "dorm", "mikudorm10 == True and mikudorm15 == False", 55, {1,3,4,5,6,7}, {"miku_love" : 15})
    add_avn_event("soccer20", "Coach", "Miku", 1, "work1", "soccer15 == True and soccer20 == False", 90, None, {"miku_love" : 20})
    add_avn_event("soccer25", "Thighs On-Demand", "Miku", 1, "work1", "soccer20 == True and mikudorm15 == True and halloween14 == True and soccer25 == False", 125, None, {"miku_love" : 25}) 
    add_avn_event("mikudorm25", "Scaredy Cat", "Miku", 1, "dorm", "soccer25 == True and mikudorm25 == False", 125, {1,3,4,5,6,7}, {"miku_love" : 25})
    add_avn_event("soccer30", "An Extra Set of Arms", "Miku", 1, "work1", "mikudorm25 == True and soccer30 == False", 185, None, {"miku_love" : 30})
    add_avn_event("mikudorm30", "One. Two. Three.", "Miku", 1, "dorm", "soccer30 == True and trinity3track == True and mikudorm30 == False", 185, {1,3,5,6,7}, {"miku_love" : 30})
    add_avn_event("soccer35", "Loxonin", "Miku", 2, "work1", "mikudorm30 == True and day271 == True and soccer35 == False", None, None, {"miku_love" : 35})
    # add_avn_event("mikuwinterbeach1", "To Sleep, Perchance to Dream", "Miku", 2, "chain", "makotowinterbeach3")
    add_avn_event("mikudorm35", "Triple Whammy", "Miku", 2, "dorm", "makotowinterbeach4 == True and mikudorm35 == False", None, {1,3,5,6,7}, {"miku_love" : 35})
    add_avn_event("mikudorm40", "Speed of Light", "Miku", 2, "dorm", "mikudorm35 == True and mikudorm40 == False", None, {1,3,5,6,7}, {"miku_love" : 35})
    add_avn_event("mikudorm45", "Acute Love Triangle", "Miku", 2, "dorm", "christmastwo20 == True and mikudorm45 == False", None, {1,3,5,6,7}, {"miku_love" : 45})
    # add_avn_event("mikudorm45p2", "Chrysalis", "Miku", 2, "chain", "mikudorm45")
    add_avn_event("mikuspecial50", "Someone Else's Skin", "Miku", 2, "date_afternoon", "christmastwo20 == True and mikudorm45p2 == True and mikuspecial50 == False", None, None, {"miku_love" : 50})
    # add_avn_event("mikudorm50", "The Devil & God Are Raging Inside Me", "Miku", 2, "chain", "mikuspecial50")
    add_avn_event("mikuinvite1", "Breakaway", "Miku", 3, "invite", "slumberreset5 == True and mikuinvite1 == False")
    add_avn_event("mikuinvite2", "Fair is Fair", "Miku", 3, "invite", "mikuinvite1 == True and mikuinvite2 == False")
    # add_avn_event("mikupool55", "Voice of Vibration", "Miku", 3, "chain", "ayanepool55")
    add_avn_event("mikudorm55p1", "Essence of Eiderdown", "Miku", 3, "dorm", "mikupool55 == True and mikudorm55p1 == False", None, {6}, {"miku_love" : 55})
    # add_avn_event("mikudorm55p2", "Rostrum of Recollection", "Miku", 3, "chain", "mikudorm55p1")
    add_avn_event("mikuspring1", "Captain Sorrow", "Miku", 4, "ch4work1", "karinspring1 == True and mikuspring1 == False", None, {7})
    # add_avn_event("mikuspring2", "Bonerville", "Miku", 4, "chain", "mikuspring1")
    add_avn_event("mikuspring3", "The Boys", "Miku", 4, "ch4work1", "karinspring2 == True and mikuspring3 == False", None, {3})
    # 043
    add_avn_event("mikuspring4", "Live Fast, Die Young", "Miku", 4, "ch4date_morning", "makotospring1 == True and chinamispring3 == True and mikuspring4 == False", None, {6,7}, {"miku_love" : 40})
    # add_avn_event("mikuspring5", "The Gazelle", "Miku", 4, "chain", "mikuspring4")
    # 051
    add_avn_event("mikulust5", "Practice Makes Perfect", "Miku", 4, "ch4work3", "dormwarsfive14 == True and makispring2 == True and mikulust5 == False", None, None, None, {"miku_lust" : 5})
    # 057
    add_avn_event("mikuspring6", "Bean Sprouts", "Miku", 4, "ch4work1", "iospring8 == True and nikispring8 == True and kaoriinvite2 == True and mikulust5 == True and mikuspring6 == False", None, {1,2,3,4})
    # add_avn_event("mikuspring7", "The Whale", "Miku", 4, "chain", "mikuspring6")

    #MOLLY
    add_avn_event("mollycafe1", "NTR & Pregnancy", "Molly", 1, "work3", "day154 == True and mollycafe1 == False") 
    add_avn_event("mollyfirsthall", "The Cult of Molly", "Molly", 1, "dorm2", "day154 == True and mollyfirsthall == False", None, {1}) 
    add_avn_event("mollyhall", "", "Molly", 1, "dorm2", "mollyfirsthall == True and mollysad == False and not renpy.seen_label('mollyhall') and molly_love < 5", None, {1})
    add_avn_event("mollycafegen", "", "Molly", 1, "work3", "mollycafe1 == True and christmas7 == False and mollysad == False and not renpy.seen_label('mollycafegen') and molly_love < 5")
    add_avn_event("mollycafe5", "Remnants of Forgotten Memes", "Molly", 1, "work3", "mollycafe1 == True and mollycafe5 == False", None, None, {"molly_love" : 5})
    add_avn_event("mollydorm5", "Torrent of Power", "Molly", 1, "dorm2", "mollyfirsthall == True  and mollycafe1 == True and mollydorm5 == False", None, {2,3,4,5,6,7}, {"molly_love" : 5})
    add_avn_event("mollycafe10", "Something Out of a Nukige", "Molly", 1, "work3", "mollycafe5 == True and mollydorm5 == True and mollycafe10 == False", 168, None, {"molly_love" : 10})
    add_avn_event("mollydorm10", "The Dark Entity", "Molly", 1, "dorm2", "mollydorm5 == True and mollycafe10 == True and mollydorm10 == False", 170, {2,3,4,5,6,7}, {"molly_love" : 10})
    add_avn_event("mollycafe15", "Onward to Valhalla", "Molly", 2, "work3", "christmas7 == True and mollycafe15 == False", None, None, {"molly_love" : 15})
    add_avn_event("mollydorm15", "Unpaid Promotion", "Molly", 2, "dorm2", "christmas7 == True and mollydorm15 == False", None, {2,3,4,5,6,7}, {"molly_love" : 15})
    add_avn_event("mollycafe20", "The Legacy of Thaum Pt. II", "Molly", 2, "work3", "mollycafe15 == True and mollydorm15 == True and mollycafe20 == False", None,  None, {"molly_love" : 20})
    add_avn_event("mollydorm20", "Ahead of the Curve", "Molly", 2, "dorm2", "mollycafe20 == True and mollydorm20 == False", None, {2,3,4,5,6,7}, {"molly_love" : 20})
    add_avn_event("mollycafe25", "Resurrection Sickness", "Molly", 2, "work3", "tsuneyodorm25 == True and rindorm50 == True and mollycafe25 == False", None, {6,7}, {"molly_love" : 25})
    # add_avn_event("mollycafe25p2", "Tír na nÓg", "Molly", 2, "chain", "mollycafe25")
    # add_avn_event("mollydorm25", "Transmogrification", "Molly", 2, "chain", "mollycafe25p2")
    add_avn_event("mollydorm30", "Walkthrough", "Molly", 2, "dorm2", "rindorm50special == True and mollydorm30 == False", None, {3,4,5}, {"molly_love" : 30})
    add_avn_event("mollycafe30p1", "Hook", "Molly", 3, "work3", "nikilovesyou3 == True and otohaspecial15p2 == True and mollycafe30p1 == False", None, {5}, {"molly_love" : 30})
    # add_avn_event("mollycafe30p2", "A Night to Remember", "Molly", 3, "chain", "mollycafe30p1")
    # add_avn_event("mollydate35p1", "Anar'alah Belore", "Molly", 3, "chain", "mollycafe30p2")
    # add_avn_event("mollydate35p2", "Sardines", "Molly", 3, "chain", "mollydate35p1")
    # add_avn_event("mollycamp1", "Corrupted Blood", "Molly", 4, "camp", 'Choose "Call Someone" in camp, yukicamp1')
    add_avn_event("mollyspring1", "Level One", "Molly", 4, "weekend_morning", "saracamp2 == True and mollyspring1 == False", None, {7})
    # add_avn_event("mollyspring2", "Fated to Love You", "Molly", 4, "chain", "mollyspring1")
    # 046
    # add_avn_event("mollylust10", "The Farmer’s Daughter", "Molly", 4, "chain", "futabalust40")
    # 047
    add_avn_event("mollyinvite1", "No Murder in the House", "Molly", 4, "invite", "christmasfive8 == True and mollyinvite1 == False")
    add_avn_event("mollyinvite2", "Pixels & Polygons", "Molly", 4, "invite", "mollyinvite1 == True and mollyinvite2 == False")
    # 052
    # add_avn_event("beachsixmolly1", "Power-Leveling", "Molly", 4, "chain", "beachsix2")
    # 057
    add_avn_event("mollyspring3", "Nihongo Jouzu", "Molly", 4, "ch4work2", "utaspring8 == True and mollyspring3 == False", None, {6,7}, {"molly_love" : 40})
    # add_avn_event("mollyspring4miss", "Missable Event", "Molly", 4, "chain", "mollyspring3") # mollyspring4miss 

    #NAO
    add_avn_event("naospecial1", "Silver Tongue", "Nao", 3, "saturday_morning", "predormwars3 == True and naospecial1 == False", None, {6})
    # add_avn_event("naospecial2", "Becoming a Kidnapper", "Nao", 3, "chain", "naospecial1")
    # add_avn_event("naospecial3", "Eternity Until", "Nao", 3, "chain", "naospecial2")
    # add_avn_event("naocamp1", "Flora", "Nao", 4, "chain", "kaoricamp1")
    # add_avn_event("naocamp2", "What's in the Pot?", "Nao", 4, "camp", 'Choose "See what Nao is up to" in camp, amicamp2')
    # 044
    # add_avn_event("halloweennao1", "Even Gods Get Lost", "Nao", 4, "chain", "halloweenfive6")
    # add_avn_event("halloweennao2", "A House Near a Lake", "Nao", 4, "chain", "halloweennao1")
    # 051
    # add_avn_event("naospring1", "Wings of Anhedonia", "Nao", 4, "chain", "kaorispring1")
    # add_avn_event("naospring2", "Miracle", "Nao", 4, "chain", "kaorispring3")
    add_avn_event("naospring3", "Nao More Than Ever", "Nao", 4, "ch4work3", "naospring2 == True and naospring3 == False", None, {1,2,3,4})
    # 056
    add_avn_event("naospring4", "Menma", "Nao", 4, "ch4work3", "chinamispring8 == True and naospring4 == False", None, {3})

    #NIKI
    add_avn_event("nikidate1", "Cotton Candy", "Niki", 2, "date_morning", "nikinumber == True and nikidate1 == False")
    add_avn_event("nikidate5", "Like it's Any Other Day", "Niki", 2, "date_night", "rindorm40 == True and nikidate1 == True and nikidate5 == False", None, None, {"niki_love" : 5})
    add_avn_event("nikidate10", "Thousands, If Not Millions", "Niki", 2, "date_morning", "secondbeach18 == True and nikidate10 == False", None, None, {"niki_love" : 10})
    add_avn_event("nikidate15", "Hotel Rooms", "Niki", 2, "date_night", "nikidate10 == True and nikidate15 == False", None, {6}, {"niki_love" : 15})
    add_avn_event("nikiinvite1", "Sisters", "Niki", 2, "invite", "norikodorm25 == True and nikiinvite1 == False")
    add_avn_event("nikiinvite2", "Dear You", "Niki", 2, "invite", "nikiinvite1 == True and nikiinvite2 == False")
    add_avn_event("nikilovesyou1", "What it Takes to Move Forward", "Niki", 3, "date_morning", "slumberreset5 == True and nikilovesyou1 == False", None, {6}, {"niki_love" : 20})
    # add_avn_event("nikilovesyou2", "The End of the Tour (Glasswalker)", "Niki", 3, "chain", "nikilovesyou1")
    # add_avn_event("nikilovesyou3", "How To Make Love Stay", "Niki", 3, "chain", "nikilovesyou2")
    # add_avn_event("nikifirstlust", "Non-Disclosure Agreement", "Niki", 3, "chain", "beachwars8")
    add_avn_event("nikispring1", "They Came Together", "Niki", 4, "ch4date_morning", "otohaspring2 == True and nikispring1 == False", None, {6,7}, {"niki_love" : 40})
    add_avn_event("nikispring2", "The Clod and the Pebble", "Niki", 4, "ch4work1", "karinspring3 == True and nikispring1 == True and nikispring2 == False", None, {2})
    # 042
    # add_avn_event("beachfive8", "Broken Furniture", "Niki", 4, "chain", "")
    # add_avn_event("nikispring3", "That Funny Feeling", "Niki", 4, "chain", "")
    # 050
    add_avn_event("nikispring4", "Costco (Dick Lover)", "Niki", 4, "saturday_morning", "mollyinvite2 == True and nodokainvite2 == True and mayaspring3 == True and otohaspring4 == True and nikispring4 == False", None, {6})
    # add_avn_event("nikispring5", "Beauty in What's Broken", "Niki", 4, "chain", "nikispring4")
    # add_avn_event("nikispring6", "Artificial Love", "Niki", 4, "chain", "norikospring5")
    # 056
    add_avn_event("nikispring7", "This World, So Full of Fish", "Niki", 4, "weekend_morning", "(amispring5 == True or amispring5miss == True) and nikispring7 == False", None, {7})
    # add_avn_event("nikispring8", "Say Anything", "Niki", 4, "chain", "nikispring7")
    # 058
    # add_avn_event("dormwarssixniki1", "Take it Easy (Love Nothing)", "Niki", 4, "chain", "dormwarssix6")

    #NODOKA
    add_avn_event("nodokafirsthall", "Humbert Humbert", "Nodoka", 2, "dorm2", "day288 == True and nodokafirsthall == False", None, {5})   
    add_avn_event("nodokahall", "", "Nodoka", 2, "dorm2", "nodokafirsthall == True and nodokablock == False and not renpy.seen_label('nodokahall') and nodoka_love < 5", None, {5})
    add_avn_event("nodokalibrarygen", "", "Nodoka", 2, "work2", "otohadorm1 == True and chapthreeactive == False and nodokablock == False and not renpy.seen_label('nodokalibrarygen') and nodoka_love < 5")
    add_avn_event("nodokadorm1", "The Man Who Would Be King", "Nodoka", 2, "dorm2", "day288 == True and nodokafirsthall == True and otohafirsthall == True and nodokadorm1 == False", None, {2,3,4,6,7})
    add_avn_event("nodokalibrary1", "Cracks in the Armor", "Nodoka", 2, "work2", "otohadorm1 == True and nodokalibrary1 == False")
    add_avn_event("nodokalibrary5", "Coloring Book", "Nodoka", 2, "work2", "nodokalibrary1 == True and nodokalibrary5 == False", None, {6}, {"nodoka_love" : 5})
    add_avn_event("nodokadorm5", "I See Everything", "Nodoka", 2, "dorm2", "nodokadorm1 == True and nodokalibrary5 == True and nodokadorm5 == False", None, {2,3,4,5}, {"nodoka_love" : 5}) 
    add_avn_event("nodokadorm15", "Beyond the Reach of God", "Nodoka", 3, "dorm2", "yasudorm20 == True and nodokadorm15 == False", None, None, {"nodoka_love" : 15})
    add_avn_event("nodokaspecial15p1_avn", "So Far Below", "Nodoka", 3, "weekday_morning", "yasudorm20 == True and nodokadorm15 == True and nodokaspecial15p1 == False", 514, {4})
    # add_avn_event("nodokaspecial15p2", "Matador", "Nodoka", 3, "chain", "nodokaspecial15p1")
    # add_avn_event("nodokaspecial15p3", "Things That Hurt", "Nodoka", 3, "chain", "nodokaspecial15p2", skip_var = "nodokaspecial15p3skip")
    # add_avn_event("nodokaspecial20", "Twisting Ivy", "Nodoka", 3, "chain", "yasuspecial20")
    add_avn_event("nodokaspecial30p1", "Amoeba (Incontrovertible Peculiarity)", "Nodoka", 3, "saturday_morning", "makotodorm55p2 == True and norikodorm30 == True and tsubasaspecial20 == True and nodokaspecial30p1 == False", None, {6}, {"nodoka_love" : 30})
    # add_avn_event("nodokaspecial30p2", "This is Us", "Nodoka", 3, "chain", "nodokaspecial30p1")
    # add_avn_event("nodokaspecial30p3", "Taco Attack", "Nodoka", 3, "chain", "nodokaspecial30p2")
    # add_avn_event("nodokaspecial30p4", "Lavender", "Nodoka", 3, "chain", "nodokaspecial30p3")
    # add_avn_event("sportswars17", "Meet & Fuck", "Nodoka", 4, "chain", "sportswars16")
    # 042
    # add_avn_event("beachfive6", "The Silver King", "Nodoka", 4, "chain", "")
    # add_avn_event("beachfive10", "Mille Crepe", "Nodoka", 4, "chain", "")
    # 044
    # add_avn_event("halloweennodoka1", "When the Well Runs Dry", "Nodoka", 4, "chain", "halloweenfive5")
    # 047
    add_avn_event("nodokainvite1", "Perfect Hair Forever", "Nodoka", 4, "invite", "christmasfive8 == True and nodokainvite1 == False")
    # add_avn_event("nodokainvite2", "Number One Fan", "Nodoka", 4, "chain", "nodokainvite1")
    # add_avn_event("nodokainvite3", "How to Fuck Your Father", "Nodoka", 4, "chain", "nodokainvite2")  # nodokainvite3miss
    # 054
    # add_avn_event("nodokachristmalloween1", "Hark! Now I Hear Them", "Nodoka", 4, "chain", "chikachristmalloween2")
    # add_avn_event("nodokachristmalloween2", "Beseech the Queen", "Nodoka", 4, "chain", "nodokachristmalloween1")
    # add_avn_event("nodokachristmalloween3", "The Hours of Folly (Return to Sender)", "Nodoka", 4, "chain", "nodokachristmalloween2")
    # 058
    # add_avn_event("dormwarssixnodoka1", "Rotten Wood & Rusty Nails", "Nodoka", 4, "chain", "dormwarssixniki1")
    # 060
    add_avn_event("nodokaspring1", "Number Girl", "Nodoka", 4, "dorm2", "makotospring5 == True and yasuspring8 == True and nodokaspring1 == False", None, None, {"nodoka_love" : 40})
    # add_avn_event("nodokaspring2", "Virgin Birth (Passer Montanus)", "Nodoka", 4, "chain", "nodokaspring1")
    # add_avn_event("nodokaspring3", "Worlds Unseen", "Nodoka", 4, "chain", "nodokaspring2")

    #NORIKO
    add_avn_event("norikofirsthall", "Sculpture (Dream Girl)", "Noriko", 2, "dorm2", "day271 == True and norikofirsthall == False", None, {3})
    # add_avn_event("norikohall", "", "Noriko", 3, "dorm2", "norikofirsthall == True and chapthreeactive == False and not renpy.seen_label('norikohall') and noriko_love < 5", None, {3})
    # add_avn_event("conveniencegen", "", "Noriko", 2, "work3", "convenience1 == True and norikoblock == False and chapthreeactive == False and not renpy.seen_label('conveniencegen') and noriko_love < 5")
    add_avn_event("convenience1", "Nakayarakawayama", "Noriko", 2, "work3", "norikofirsthall == True and convenience1 == False", None, None, {"noriko_love" : 5})
    add_avn_event("norikodorm5", "Semi-Constructive Criticism", "Noriko", 2, "dorm2", "kirindorm10 == True and convenience1 == True and norikodorm5 == False", None, None, {"noriko_love" : 5})
    add_avn_event("convenience5", "Mouthjob", "Noriko", 2, "work3", "norikodorm5 == True and mollydorm15 == True and convenience1 == True and convenience5 == False", None, {1,2,4,5,6,7}, {"noriko_love" : 5})
    add_avn_event("norikodorm10", "Kind Of, Yes. Kind Of, No.", "Noriko", 2, "dorm2", "convenience5 == True and kirindorm20 == True and norikodorm10 == False", None, {1,2,4,5,6,7}, {"noriko_love" : 10})
    add_avn_event("norikoinvite1", "New Shoes", "Noriko", 2, "invite", "norikodorm10 == True and norikoinvite1 == False", None, {1,2,3,4,5})
    # add_avn_event("norikoinvite2", "Beginnings. Endings. Things in Between.", "Noriko", 2, "chain", "norikoinvite1")
    add_avn_event("norikospecial20", "Fair & Square", "Noriko", 2, "weekday_morning", "halloweentwo13 == True and norikospecial20 == False", 400, {1})
    add_avn_event("norikodorm20", "Homes for the Homeless", "Noriko", 2, "dorm2", "norikospecial20 == True and norikodorm20 == False", None, {1,2,4,5,6,7}, {"noriko_love" : 20})
    add_avn_event("convenience25", "That One FMK Scene", "Noriko", 2, "work3", "norikodorm20 == True and convenience25 == False", None, None, {"noriko_love" : 25})
    add_avn_event("norikodorm25", "Loxosceles Reclusa", "Noriko", 2, "dorm2", "convenience25 == True and norikodorm25 == False", None, {1,2,4,5,6,7}, {"noriko_love" : 25})
    add_avn_event("norikodate30", "Hotel Noriko", "Noriko", 3, "date_night", "nikilovesyou3 == True and norikodate30 == False", None, None, {"noriko_love" : 30})
    add_avn_event("norikodorm30", "Dotted Line", "Noriko", 3, "dorm2", "norikodate30 == True and otohadate20 == True and norikodorm30 == False", None, {1,2,3,5,6,7}, {"noriko_love" : 30})
    add_avn_event("norikoinvite3", "I Really Want to Stay at Your House", "Noriko", 3, "invite", "norikodorm30 == True and kirinspecial45p2 == True and norikoinvite3 == False", None, None, {"noriko_love" : 40}) #skip_var = "norikoinvite3skip", 
    # add_avn_event("norikoinvite4", "Somewhere", "Noriko", 3, "chain", "norikoinvite3", skip_var = "norikoinvite4skip")
    # add_avn_event("sportswars2", "Rivals (Taco Tuesday)", "Noriko", 4, "chain", "sportswars1")
    # 041
    add_avn_event("norikospring1", "The Long Road Ahead", "Noriko", 4, "ch4work3", "yasuspring3 == True and norikospring1 == False", None, None, {"noriko_love" : 30})
    add_avn_event("norikospring2", "Transpacific Sadness Symposium I: DEN OF THE MOLE RAT", "Noriko", 4, "weekend_afternoon", "norikospring1 == True and utaspring1 == True and norikospring2 == False", None, {7})
    # 050
    # add_avn_event("norikospring3", "Hard-Off", "Noriko", 4, "chain", "amispring2")
    # add_avn_event("norikospring4", "Haiku", "Noriko", 4, "chain", "nikispring5")
    # add_avn_event("norikospring5", "At The Beach, In Every Life", "Noriko", 4, "chain", "norikospring4")
    # 052
    # add_avn_event("beachsixnoriko1", "Circling the Drain", "Noriko", 4, "chain", "beachsix2")
    # 056
    add_avn_event("norikoinvite5", "Reasons to Die", "Noriko", 4, "invite", "iospring8 == True and rinspring9 == True and toukaspring8 == True and wakanaspring8 == True and christmalloween6 == True and norikoinvite5 == False", None, None, {"noriko_love" : 50})    # if 055 
    # add_avn_event("norikoinvite6", "Love in Strange Forms", "Noriko", 4, "chain", "norikoinvite5")    # norikoinvite6miss 

    #OSAKO
    # add_avn_event("osakodate1", "Pressure Point", "Osako", 2, "chain", "wakanadate5")
    add_avn_event("osakodojo1", "Floating Forever, Unfulfilled", "Osako", 2, "work2", "osakodate1 == True and osakodojo1 == False")
    # add_avn_event("osakodojogen", "", "Osako", 2, "work2", "osakodate1 == True and chapthreeactive == False and not renpy.seen_label('osakodojogen') and osako_love < 5")
    add_avn_event("osakodate15", "Young At Heart", "Osako", 3, "work2", "wakanaspecial15 == True and osakodate15 == False", None, None, {"osako_love" : 15}) # hint_girl = Uta,
    add_avn_event("osakodate20", "House of the Unholy", "Osako", 3, "work2", "osakodate15 == True and osakodate20 == False", None, None, {"osako_love" : 20})  #hint_girl = Maki, 
    add_avn_event("osakospring1", "Chaos Spiral (Heterosexual Sex)", "Osako", 4, "weekend_morning", "rinspring2 == True and osakospring1 == False", None, {7})
    # add_avn_event("osakospring2", "Meat-Pocket", "Osako", 4, "chain", "osakospring1")
    add_avn_event("osakospring3", "Indecent Proposal", "Osako", 4, "weekday_morning", "osakospring2 == True and osakospring3 == False", None, {5})
    # 043
    # add_avn_event("osakospring4", "MILF of the Month Club", "Osako", 4, "chain", "karinspring4")
    # 047
    add_avn_event("osakospring5", "Girl C", "Osako", 4, "ch4work3", "sanainvite2 == True and osakospring5 == False", None, {6})
    # add_avn_event("osakospring6", "All Good Things", "Osako", 4, "chain", "osakospring5")
    # 055
    # add_avn_event("osakospring7", "When Harry Met Gandalf", "Osako", 4, "chain", "rikaspring7")
    add_avn_event("osakospring8", "Troubles, Trials, and Tribadism", "Osako", 4, "ch4work3", "osakospring7 == True and osakospring8 == False")
    # add_avn_event("osakospring9", "Pica", "Osako", 4, "chain", "osakospring8")

    #OTOHA
    add_avn_event("otohafirsthall", "Everybody Loves Otoha", "Otoha", 2, "dorm2", "day288 == True and otohafirsthall == False", None, {1}) 
    add_avn_event("otohahallgen", "", "Otoha", 2, "dorm2", "otohafirsthall == True and not renpy.seen_label('otohahallgen') and otoha_love < 5", None , {1})
    # add_avn_event("otohadorm1", "Conversations Outside of a Girls’ Dorm", Otoha, 2, "chain", "nodokadorm1")
    add_avn_event("otohapark1", "Japanese Summer (Double Suicide)", "Otoha", 2, "work1", "otohadorm1 == True and saradate10 == True and otohapark1 == False")  #otoha_love >= 0
    add_avn_event("otohaparkgen", "", "Otoha", 2, "work1", "otohapark1 == True and chapthreeactive == False and not renpy.seen_label('otohaparkgen') and otoha_love < 5")
    add_avn_event("otohapark5", "Locked In", "Otoha", 2, "work1", "otohapark1 == True and otohapark5 == False") #otoha_love >= 0
    add_avn_event("otohadorm5", "Highly Pornographic", "Otoha", 2, "dorm2", "otohapark5 == True and otohadorm5 == False", None, {6,7}, {"otoha_love" : 5})
    add_avn_event("otohapark10", "Pull the Plug", "Otoha", 2, "work1", "christmastwo20 == True and otohapark10 == False", None, None, {"otoha_love" : 10})
    # add_avn_event("otohaspecial10", "Two-Octave Pitch Glide", "Otoha", 2, "chain", "otohapark10")
    # add_avn_event("otohadorm10", "Breathing in Unison", "Otoha", 2, "chain", "otohaspecial10")
    # add_avn_event("otohadorm10p2", "Vanilla Bean", "Otoha", 2, "chain", "otohadorm10")
    add_avn_event("otohaspecial15p1", "King Midas", "Otoha", 3, "dorm2", "nikilovesyou3 == True and otohaspecial15p1 == False", None, {7}, {"otoha_love" : 15})
    # add_avn_event("otohaspecial15p2", "White People", "Otoha", 3, "chain", "otohaspecial15p1")
    add_avn_event("otohadate20", "Breaking Character", "Otoha", 3, "work1", "otohaspecial15p2 == True and otohadate20 == False", None, None, {"otoha_love" : 20})    #hint_girl = Rin, 
    add_avn_event("otohaspring1", "This Curse Called Youth", "Otoha", 4, "ch4work2", "tsuneyospring1 == True and otohaspring1 == False", None, {2})
    add_avn_event("otohaspring2", "Taint the Sapling", "Otoha", 4, "ch4work2", "yumispring2 == True and otohaspring1 == True and otohaspring2 == False")
    # add_avn_event("otohaspring3", "Something Wonderful", "Otoha", 4, "chain", "nikispring1")
    # 046
    # add_avn_event("christmasotoha1", "Sisterly Love", "Otoha", 4, "chain", "christmaskirin2")
    add_avn_event("otohaspring4", "Becoming Closer to Closure", "Otoha", 4, "dorm2", "christmasfive8 == True and day < 6 and otohaspring4 == False", None, {1,2,3,4,5}, {"otoha_love" : 20})
    # 052
    # add_avn_event("beachsixotoha1", "Something in the Water", "Otoha", 4, "chain", "beachsix1")
    # 059
    add_avn_event("otohaspring5", "Five Star Review", "Otoha", 4, "ch4work2", "tsubasaspring7 == True and otohaspring5 == False", None, {6,7})
    # add_avn_event("otohaspring6", "Billboard Hot 100", "Otoha", 4, "chain", "otohaspring5")
    add_avn_event("otohaspring7", "Pet Sounds", "Otoha", 4, "ch4work3", "otohaspring6 == True and otohaspring7 == False", None, None, {"otoha_love" : 25})

    #RIKA
    add_avn_event("rikadate1", "Impregnation Spree", "Rika", 3, "date_night", "nodokaspecial30p4 == True and rikadate1 == False")  
    add_avn_event("rikaspecial2", "Back on Track", "Rika", 3, "weekday_morning", "nodokaspecial30p4 == True and rikadate1 == True and rikaspecial2 == False", 605)
    add_avn_event("rikadive1", "James and the Giant Peach (Together-ish)", "Rika", 3, "work3", "rikaspecial2 == True and rikadive1 == False", None, {5}) 
    add_avn_event("sportswars1", "Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You", "Rika", 4, "weekday_morning", "nikispring2 == True and tsuneyospring3 == True and sportswars1 == False", None, {5})
    # 042
    add_avn_event("rikaspring1", "Rat College", "Rika", 4, "ch4work3", "beachfive16 == True and rikaspring1 == False", None, {6})
    # add_avn_event("rikaspring2", "Sixty-Minute Mark", "Rika", 4, "chain", "")
    # 048
    add_avn_event("rikaspring3", "Sins of Thy Beloved", "Rika", 4, "ch4work3", "chikaspring5 == True and osakospring6 == True and rikaspring3 == False")
    # add_avn_event("rikaspring4", "Four Hours, Thirteen Minutes, Eleven Seconds", "Rika", 4, "chain", "rikaspring3")
    # 055
    add_avn_event("rikaspring5", "A Horse Rides an Elephant", "Rika", 4, "ch4work2", "christmalloween6 == True and rikaspring5 == False", None, {1,2,3,4,5})
    # add_avn_event("rikaspring6", "Solidarity (Hag Scene)", "Rika", 4, "chain", "imanispring3")
    # add_avn_event("rikaspring7", "How to Escape a Quagmire", "Rika", 4, "chain", "imanispring4")

    #RIN
    add_avn_event("firsttimecafe", "Guinea Pig", "Rin", 1, "work1", "firsttimeshrine == True and firsttimecafe == False")  
    add_avn_event("rinfirsthall", "Locked Out", "Rin", 1, "dorm", "dorm > 0 and rinfirsthall == False", None, {3})  
    add_avn_event("cafesugar", "The Flavor of Love", "Rin", 1, "work1", "firsttimecafe == True and cafesugar == False", 30, None, {"rin_love" : 5})
    add_avn_event("cafe10", "Haruka", "Rin", 1, "work1", "cafesugar == True and cafe10 == False", 35, None, {"rin_love" : 10}) 
    add_avn_event("rinhall", "", "Rin", 1, "dorm", "rinsad == False and rinfirsthall == True and not renpy.seen_label('rinhall') and rinfirstvisit == False and rin_love < 5", 15, {3})
    add_avn_event("rinfirstvisit", "Skulls", "Rin", 1, "dorm", "cafesugar == True and rinfirstvisit == False", 25, None, {"rin_love" : 5})
    add_avn_event("rindorm10", "Rin's Secret", "Rin", 1, "dorm", "cafe10 == True and rindorm10 == False", 35,  {1,2,4,5,6,7}, {"rin_love" : 10})
    add_avn_event("cafe15", "Window of the Waking Mind", "Rin", 1, "work1", "rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False", 55, None, {"rin_love" : 15})
    add_avn_event("rindorm15", "Boundaries", "Rin", 1, "dorm", "rindorm10 == True and rindorm15 == False", 55,  {1,2,4,5,6,7}, {"rin_love" : 15})
    add_avn_event("rincafegone", "", "Rin", 1, "work1", "cafe15 == True and day63 == False and rincafegone_avn == False and cafe20 == False")    # sad Rin
    add_avn_event("cafe20", "Nothing Was Missing, Except Me", "Rin", 1, "work1", "ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False and rincafegone_avn == True", 85, None, {"rin_love" : 20}) 
    add_avn_event("rindorm20", "Delirium", "Rin", 1, "dorm", "cafe20 == True and day50 == True and rindorm20 == False", 85,  {1,4,5,6,7}, {"rin_love" : 20})
    add_avn_event("cafe25", "Good Day, Humans", "Rin", 1, "work1", "rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False", 125, None, {"rin_love" : 25})
    add_avn_event("rindorm25", "Sock Fetish", "Rin", 1, "dorm", "rindorm20 == True and rindorm25 == False", 125,  {1,2,4,5,6,7}, {"rin_love" : 25})
    add_avn_event("cafe30", "Nothing Was Different", "Rin", 1, "work1", "beachvacation16 == True and cafe30 == False", 185, None, {"rin_love" : 30})
    add_avn_event("rindorm30", "Two Steps Back", "Rin", 1, "dorm", "cafe30 == True and rindorm30 == False", 185, {1,2,4,5,6,7}, {"rin_love" : 30})
    add_avn_event("rindorm35", "Ten Steps Forward", "Rin", 1, "dorm", "rindorm30 == True and rindorm35 == False", 195,  {1,2,4,5,6,7}, {"rin_love" : 35})
    add_avn_event("cafe35", "I Died With You", "Rin", 1, "work1", "library30 == True and rindorm35 == True and rininvite == True and cafe35 == False", 195, None, {"rin_love" : 35}) #miss_preq = "rindorm35 and rininvite == False",
    add_avn_event("cafe40", "Sketchy Basement", "Rin", 2, "work1", "christmas7 == True and cafe40 == False", None, None, {"rin_love" : 40})
    add_avn_event("rindorm40", "Semantics", "Rin", 2, "dorm", "cafe40 == True and rindorm40 == False", None, {1,4,5}, {"rin_love" : 40})
    add_avn_event("cafe45", "Debatably Bisexual Musicians", "Rin", 2, "work1", "rindorm40 == True and cafe45 == False", None, None, {"rin_love" : 45})
    # add_avn_event("rindorm45", "The Art of Never Knowing", "Rin", 2, "chain", "cafe45")
    add_avn_event("cafe50", "The Paragon of Not Worrying About Stuff", "Rin", 2, "work1", "secondbeach18 == True and cafe50 == False", None, None, {"rin_love" : 50})
    add_avn_event("rindorm50", "Technicolored Happiness Explosion", "Rin", 2, "dorm", "cafe50 == True and rindorm50 == False", None, {2,4,5,6,7}, {"rin_love" : 50})
    # add_avn_event("rindorm50special", "Lifejacket", "Rin", 2, "chain", "mollydorm25")
    add_avn_event("rindate50", "The Happiest Girl in the World", "Rin", 2, "date_night", "rinbetrayed == False and rindorm50special == True and rindate50 == False") #  miss_preq = "rindorm50special and rinbetrayed"
    add_avn_event("rindorm55", "Disaster Lesbian", "Rin", 3, "dorm", "imanispecial1 == True and futabainvite3 == True and rindorm55 == False", None, {1,4,5,6,7}, {"rin_love" : 55})
    # add_avn_event("rindorm55p2", "Hot Boy Summer", "Rin", 3, "chain", "rindorm55")
    # add_avn_event("rinspecial55", "Ever Fallen In Love", "Rin", 3, "chain", "rikaspecial1")
    # add_avn_event("rinspring1", "Anthem of the Heart", "Rin", 4, "chain", "chikaspring1")
    # add_avn_event("rinspring2", "Voices of a Distant Star", "Rin", 4, "chain", "chikaspring3")
    # 041
    # add_avn_event("rinspring3", "Sex Dreams", "Rin", 4, "chain", "harukaspring2", miss_preq = "harukaspring1miss")
    # 047
    add_avn_event("rinspring4", "Voice of Reason", "Rin", 4, "ch4work3", "christmasfive8 == True and rinspring4 == False", None, {6})
    # add_avn_event("rinspring5", "Dear Sensei (Red Sea)", "Rin", 4, "chain", "rinspring4")
    # add_avn_event("rinspring6", "Love Long Overdue", "Rin", 4, "chain", "rinspring5")
    # 049
    # add_avn_event("dormwarsfiverin1", "The First Time Since the Last Time", "Rin", 4, "chain", "dormwarsfiveio1")
    # 055
    add_avn_event("rinspring7", "Days to Waste", "Rin", 4, "weekend_morning", "makispring5 == True and rinspring7 == False", None, {6,7})
    # add_avn_event("rinspring8", "Table for Two", "Rin", 4, "chain", "rinspring7")
    # add_avn_event("rinspring9", "Transpacific Sadness Symposium VIII: AN ATOM (ME) AND ADAM (YOU)", "Rin", 4, "chain", "rinspring8")

    #SANA
    add_avn_event("firsttimebar", "Family Business", "Sana", 1, "work3", "firsttimeshrine == True and firsttimebar == False")
    add_avn_event("sanafirsthall", "Nothing to Do", "Sana", 1, "dorm", "dorm > 0 and sanafirsthall == False and firsttimebar == True", None, {5}) 
    add_avn_event("bar5", "The Bare Minimum", "Sana", 1, "work3", "firsttimebar == True and bar5 == False", 25, None, {"sana_love" : 5})   
    add_avn_event("sanahall", "", "Sana", 1, "dorm", "sanafirsthall == True and not renpy.seen_label('sanahall') and sanadorm5 == False and sana_love < 5", 10, {5})
    add_avn_event("sanadorm5", "Recluse", "Sana", 1, "dorm", "sanafirsthall == True and sanadorm5 == False", 25,  {1,2,3,4,6,7}, {"sana_love" : 5})
    add_avn_event("bar10", "Supermom", "Sana", 1, "work3", "bar5 == True and sanafirsthall == True and bar10 == False", 35, None, {"sana_love" : 10})
    add_avn_event("sanadorm10", "Anywhere At All", "Sana", 1, "dorm", "bar10 == True and sanadorm10 == False", 35, {1,2,3,4,6,7}, {"sana_love" : 10})
    add_avn_event("bar15", "Carry Me Home", "Sana", 1, "work3", "bar10 == True and bar15 == False", 55, None, {"sana_love" : 15})    # work_att01
    add_avn_event("sanadorm15", "Shaking The Tree", "Sana", 1, "dorm", "sanadorm10 == True and sanadorm15 == False", 55, {1,2,3,4,6,7}, {"sana_love" : 15})
    add_avn_event("bar20", "Scouting Mission", "Sana", 1, "work3", "day65 == True and bar15 == True and amisroom5 == True and bar20 == False", 85, None, {"sana_love" : 20})
    add_avn_event("sanadorm20", "Nice Weather We're Having", "Sana", 1, "dorm", "bar20 == True and sanadorm20 == False", 85, {1,2,3,4,6,7}, {"sana_love" : 20})
    add_avn_event("bar25", "Life is a Tomato", "Sana", 1, "work3", "sanadorm20 == True and makidate1 == True and bar25 == False", 125, None, {"sana_love" : 25})
    add_avn_event("sanadorm25", "The Girl in the Black Dress", "Sana", 1, "dorm", "bar25 == True and beachvacation16 == True and sanadorm25 == False", 125, {1,2,3,4,6,7}, {"sana_love" : 25})
    add_avn_event("bar30", "Self-Medication", "Sana", 1, "work3", "sanadorm25 == True and day120 == True and bar30 == False", 185, None, {"sana_love" : 30})
    add_avn_event("sanadorm30", "Tortoises and the Concept of Friendship", "Sana", 1, "dorm", "bar30 == True and sanadorm30 == False", 185, {1,2,3,6,7}, {"sana_love" : 30})
    add_avn_event("bar35", "Purest Intentions", "Sana", 2, "work3", "utamaid5 == True and christmas7 == True and bar35 == False", None, None, {"sana_love" : 35})
    add_avn_event("sanadorm35", "Waiting for Anything", "Sana", 2, "dorm", "bar35 == True and sanadorm35 == False", None, {1,2,3,6,7}, {"sana_love" : 35})
    add_avn_event("bar40", "Closer to Me", "Sana", 2, "work3", "sanadorm35 == True and bar40 == False", None, None, {"sana_love" : 40})
    # add_avn_event("sanadorm40", "The Inside of a Triangle", "Sana", 2, "chain", "bar40")
    add_avn_event("bar45", "Sweet Vermouth", "Sana", 2, "work3", "thirdreset3 == True and futabadorm45 == True and bar45 == False", None, None, {"sana_love" : 45})
    add_avn_event("sanadorm45", "The Complete Absence of Everything", "Sana", 2, "dorm", "thirdreset3 == True and sanadorm45 == False", None, {1,2,3,6,7}, {"sana_love" : 45})
    add_avn_event("sanadorm50", "Mine (Yours)", "Sana", 2, "dorm", "sanadorm45 == True and bar45 == True and sanadorm50 == False", None, {1,2,3,4,6,7}, {"sana_love" : 50})
    add_avn_event("bar50", "Melatonin", "Sana", 2, "work3", "day351 == True and sarasex == True and sanadorm50 == True and bar50miss == False and bar50 == False",  None, None, {"sana_love" : 50}) #miss_preq = "bar50miss"
    add_avn_event("bar55", "Black Sandy Beaches", "Sana", 3, "work3", "imanispecial1 == True and bar55 == False", None, {1,2,3,4}, {"sana_love" : 55})
    # add_avn_event("ayanesanabeach2", "Ad Meliora", "Sana", 3, "chain", "ayanesanabeach1", skip_var = "ayanesanabeach2skip")
    # add_avn_event("ayanesanabeach3", "It Comes to Claim Us All", "Sana", 3, "chain", "ayanesanabeach2")
    # add_avn_event("ayanesanabeach4", "Ad Infinitum", "Sana", 3, "chain", "ayanesanabeach3", skip_var = "ayanesanabeach4skip")
    # add_avn_event("sanaspring1", "Taller", "Sana", 4, "chain", "rinspring1")
    # add_avn_event("sanaspring2", "Stutter-Step", "Sana", 4, "chain", "sanaspring1")
    # add_avn_event("sanaspring3", "Weak Man, Weak Boy", "Sana", 4, "chain", "sanaspring2")
    # 043
    add_avn_event("sanaspring4", "Transpacific Sadness Symposium III: TWO-HEADED HORSE", "Sana", 4, "ch4work3", "yukispring2 == True and sanaspring4 == False", None, {5})
    # 047
    add_avn_event("sanainvite1_avn", "Piggy & The Boulder", "Sana", 4, "invite", "christmasfive8 == True and sanainvite1 == False")
    # add_avn_event("sanainvite2", "Four Letter Words", "Sana", 4, "chain", "sanainvite1")
    # 052
    # add_avn_event("beachsixsana1", "Despicable Meat Toilet", "Sana", 4, "chain", "beachsix2")
    # 057
    # add_avn_event("sanaspring5", "Addict in Training", "Sana", 4, "chain", "yukispring6") # sanaspring5miss 
    add_avn_event("sanaspring6", "Counting Down From Four", "Sana", 4, "dorm", "saraspring7 == True and sanaspring6 == False", None, None, {"sana_love" : 55})

    #SARA
    add_avn_event("saradate1", "A Woman's Heart", "Sara", 1, "date_afternoon", "bar15 == True and saradate1 == False", 74)
    add_avn_event("sarabargen", "", "Sara", 1, "work3", "saradate1 == True and christmas7 == False and not renpy.seen_label('sarabargen') and sara_lust < 5")
    add_avn_event("saragenafternoon", "", "Sara", 1, "date_afternoon", "saradate1 == True and christmas7 == False and not renpy.seen_label('saragenafternoon') and sara_love < 5")
    add_avn_event("saralust5", "Zero Friction", "Sara", 1, "work3", "saradate1 == True and sarasex == True and saralust5 == False", 75, None, {"sara_love" : 5}, {"sara_lust" : 5})  #miss_preq = "bar15 and sarasex == False", 
    add_avn_event("sarainvite1", "Third Wheel", "Sara", 1, "invite", "saradate1 == True and sarainvite1 == False")
    add_avn_event("sarainvite2", "A Mostly Empty Home", "Sara", 1, "invite", "sarainvite1 == True and sarainvite2 == False")
    # add_avn_event("saralust10", "Medical Assistance", "Sara", 1, "chain_lust_adv", "sara_lust >= 10, halloween7", miss_preq = "halloween8 and saralust10 == False")
    add_avn_event("saradate10", "Uptown Girl", "Sara", 2, "date_afternoon", "nikidate5 == True and sanadorm35 == True and saradate10 == False", None, None, {"sara_love" : 15})
    add_avn_event("sarabar20", "She's Always a Woman", "Sara", 2, "work3", "sarasex == True and day271 == True and sanadorm40 == True and sarabar20 == False", None, None, {"sara_love" : 20})  #miss_preq = "saradate10 and sarasex == False", 
    add_avn_event("sarabar25", "Tell Me When", "Sara", 2, "work3", "yukidate10p2 == True and sarabar25 == False", None, None, {"sara_love" : 25})
    # add_avn_event("sarabar25p2", "The Place She Falls Asleep At Night", "Sara", 2, "chain", "sarabar25")
    # add_avn_event("saralust20", "Engulfed", "Sara", 2, "chain_lust_adv", "sara_lust >= 30 and haruka_lust >= 25 and sarasex == True and harukasex == True, christmastwo6", skip_var = "saralust20skip")
    # add_avn_event("saraspecial30p1", "The Creaking of the Seventh Step", "Sara", 3, "chain", "yukidate25")
    # add_avn_event("saraspecial30p2", "Halfway Down the Wishing Well", "Sara", 3, "chain", "saraspecial30p1", skip_var = "saraspecial30p2skip")
    add_avn_event("sarabar30", "Nicolas Cage", "Sara", 3, "work3", "saraspecial30p1 == True and sarabar30 == False", None, None, {"sara_love" : 30})
    # add_avn_event("saracamp1", "The One With A Happy Ending", "Sara", 4, "chain", "amicamp1")
    # add_avn_event("saracamp2", "I've Been Thinking About Leaving This Place", "Sara", 4, "camp", 'Choose "Call it a night" in camp, amicamp2')
    # 043
    add_avn_event("saraspring1", "Details in the Fabric", "Sara", 4, "ch4work3", "rikaspring1 == True and saraspring1 == False", None, None, {"sara_love" : 35})
    add_avn_event("saraspring2", "Silent Night (Onee-san)", "Sara", 4, "ch4work3", "sarasex == True and yukispring2 == True and saraspring2 == False", None, None, {"sara_love" : 40})
    # 050
    # add_avn_event("saraspring3", "Worthless Me", "Sara", 4, "chain", "ayanespring2")     #saraspring3miss
    add_avn_event("saraspring4", "Two for the Price of One", "Sara", 4, "ch4work3", "saraspring3 == True and saraspring4 == False")     #saraspring4miss
    add_avn_event("saraspring5", "The Puppeteer", "Sara", 4, "ch4work3", "saraspring4 == True and saraspring5 == False", None, {1,2,3,4,5})     #saraspring5miss
    # 057
    # add_avn_event("saraspring6", "The Most Beautiful Bitter Fruit", "Sara", 4, "chain", "yukispring7")     #saraspring6miss
    add_avn_event("saraspring7", "You and I in Unison", "Sara", 4, "ch4work2", "yukispring7 == True and saraspring7 == False", None, None, {"sara_love" : 45})
    # 058
    # add_avn_event("dormwarssixsara1", "Ring of Fire", "Sara", 4, "chain", "yukispring7")     #dormwarssixmaya1

    #TOUKA
    add_avn_event("toukafirsthall", "Spontaneous Sentimentality", "Touka", 2, "dorm2", "day304 == True and toukafirsthall == False", None, {2})
    add_avn_event("toukahallgen", "", "Touka", 2, "dorm2", "toukafirsthall == True and not renpy.seen_label('toukahallgen') and touka_love < 5", None, {2})
    add_avn_event("toukastreets1", "Trial Period", "Touka", 2, "work1", "day304 == True and toukastreets1 == False")    #touka_love >= 0
    add_avn_event("toukastreetsgen", "", "Touka", 2, "work1", "toukastreets1 == True and chapthreeactive == False and not renpy.seen_label('toukastreetsgen') and touka_love < 5")
    add_avn_event("toukadorm1", "Fish Out of Water", "Touka", 2, "dorm2", "toukafirsthall == True and toukadorm1 == False", None, {1,3,5,6,7}) 
    add_avn_event("toukastreets5", "A Brief Moment in Time", "Touka", 2, "work1", "ramen20 == True and convenience5 == True and toukadorm1 == True and toukastreets5 == False", None, None, {"touka_love" : 5})
    add_avn_event("toukadorm5", "Loser", "Touka", 2, "dorm2", "toukastreets5 == True and toukadorm5 == False", None, {1,3,5,6,7}, {"touka_love" : 5})
    add_avn_event("toukadorm10", "House Call", "Touka", 2, "dorm2", "christmastwo20 == True and toukadorm10 == False", None, {1,3,5,6,7}, {"touka_love" : 10})
    add_avn_event("toukaspecial15", "A Commoner's Tour of Summer", "Touka", 2, "work1", "toukadorm10 == True and toukaspecial15 == False", None, None, {"touka_love" : 15})
    # add_avn_event("toukaspecial15p2", "Red-ish Light District", "Touka", 2, "chain", "toukaspecial15")
    # add_avn_event("toukaspecial15p3", "Something Less Lonely", "Touka", 2, "chain", "toukaspecial15p2")
    add_avn_event("toukaarchery20", "Kryptonite", "Touka", 3, "work2", "tsubasaspecial20 == True and toukaarchery20 == False", None, None, {"touka_love" : 20})
    add_avn_event("toukadorm25p1", "For Want Of", "Touka", 3, "dorm2", "toukaarchery20 == True and toukadorm25p1 == False", None, {1,3,4,5,6,7}, {"touka_love" : 25})
    # add_avn_event("toukadorm25p2", "To Lift This Aching Head", "Touka", 3, "chain", "toukadorm25p1")
    # add_avn_event("toukadorm25p3", "Under My Wing", "Touka", 3, "chain", "toukadorm25p2")
    # add_avn_event("toukacamp1", "Salt in the Wound", "Touka", 4, "camp", 'Choose "Call Someone" in camp, amicamp2')
    add_avn_event("toukaspring1", "Blankets & Ball-Gags", "Touka", 4, "weekend_morning", "saracamp2 == True and toukaspring1 == False",  None, {6})
    # add_avn_event("toukaspring2", "Artisan Hands", "Touka", 4, "chain", "toukaspring1")
    # 043
    add_avn_event("toukaspring3", "One Thousand Penises", "Touka", 4, "ch4work3", "chinamispring3 == True and toukaspring3 == False",  None, {3})
    # 048
    # add_avn_event("toukaspring4", "Come For Me", "Touka", 4, "chain", "yasuspring5")
    add_avn_event("toukaspring5", "One of the Girls", "Touka", 4, "ch4work3", "toukaspring4 == True and toukaspring5 == False",  None, {7})
    # 055
    add_avn_event("toukaspring6", "Spermicide", "Touka", 4, "weekend_afternoon", "christmalloween6 == True and toukaspring6 == False")
    # add_avn_event("toukaspring7", "The Corpse of Seth Rogen", "Touka", 4, "chain", "toukaspring6")
    # add_avn_event("toukaspring8", "One Step Closer", "Touka", 4, "chain", "toukaspring7")

    #TSUBASA
    add_avn_event("tsubasadate1", "Everbloom (Pride of the Sinful Sort)", "Tsubasa", 2, "date_morning", "toukaspecial15p3 == True and tsubasadate1 == False")
    # add_avn_event("tsubasadate1p2", "The Deep End", "Tsubasa", 2, "chain", "tsubasadate1")
    # add_avn_event("tsubasaspecial15", "Heart of Gold", "Tsubasa", 3, "chain", "chikaspecial45")
    add_avn_event("tsubasadate20", "Playing God", "Tsubasa", 3, "work2", "tsubasaspecial15 == True and tsubasadate20 == False", None, None, {"tsubasa_love" : 20})    # hint_girl = Touka,
    add_avn_event("tsubasaspecial20", "The Lucky Few", "Tsubasa", 3, "date_afternoon", "tsubasadate20 == True and chikadorm45 == True and otohadate20 == True and norikoinvite3 == True and tsubasaspecial20 == False", None, None, {"tsubasa_love" : 20})
    add_avn_event("tsubasaspring1", "The Bird & The Worm", "Tsubasa", 4, "ch4work1", "chinamispring2 == True and tsubasaspring1 == False", None, {3}, {"tsubasa_love" : 5})
    # 043
    # add_avn_event("tsubasaspring2", "Petite Sirah", "Tsubasa", 4, "chain", "saraspring2")
    # add_avn_event("tsubasaspring3", "The Pleasures of the Flesh", "Tsubasa", 4, "chain", "tsubasaspring2")
    # 046
    # add_avn_event("christmastsubasa1", "Yes, Mother", "Tsubasa", 4, "chain", "mollylust10")
    # 051
    add_avn_event("tsubasaspring4", "Hands-On Learning", "Tsubasa", 4, "ch4date_afternoon", "chinamispring6 == True and yumispring8 == True and tsubasaspring4 == False")    # tsubasaspring4miss 
    # add_avn_event("tsubasaspring5", "For the Sake of Brevity", "Tsubasa", 4, "chain", "tsukasaspring6")    # tsubasaspring5miss 
    add_avn_event("tsubasaspring6", "When We Dead Awaken", "Tsubasa", 4, "ch4work3", "yumispring8 == True and (tsubasaspring4 == True or tsubasaspring4miss == True) and tsubasaspring6 == False", None, {5})
    # 059
    add_avn_event("tsubasaspring7", "Climbing Up the Ladder", "Tsubasa", 4, "weekend_morning", "futabaspring4 == True and tsubasaspring7 == False")
    # add_avn_event("tsubasaspring8", "Human Veal", "Tsubasa", 4, "chain", "tsubasaspring7")    # tsubasaspring8miss 

    #TSUKASA
    add_avn_event("tsukasaspecial1", "National Tsukasa Day", "Tsukasa", 3, "weekday_morning", "iospecial30 == True and karindate25 == True and tsukasaspecial1 == False", 530, {1})
    # add_avn_event("tsukasaspecial1p2", "Jeeves Tsukioka XIII", "Tsukasa", 3, "chain", "tsukasaspecial1")
    add_avn_event("tsukasaspring1intro", "Vow of Silence (Pole Position)", "Tsukasa", 4, "ch4date_morning", "tsubasaspring1 == True and tsukasaspring1skip == False and tsukasaspring1 == False")
    # add_avn_event("tsukasaspring2", "Blood & Sunset", "Tsukasa", 4, "chain", "tsukasaspring1", skip_var = "tsukasaspring2skip")
    add_avn_event("tsukasaspring3_avn", "Failsafe", "Tsukasa", 4, "ch4date_afternoon", "tsukasaspring2 == True and tsukasaspring3 == False")
    # 046
    # add_avn_event("christmastsukasa1", "A Part of Your World", "Tsukasa", 4, "chain", "christmasotoha1")
    add_avn_event("tsukasaspring4", "The Talk", "Tsukasa", 4, "weekend_afternoon", "christmasfive8 == True and tsukasacurious == True and tsukasaspring4 == False", None, {7})
    # 051
    # add_avn_event("tsukasaspring5", "Six Inches of Suffering", "Tsukasa", 4, "chain", "chikaspring8")     # tsukasaspring5miss
    # add_avn_event("tsukasaspring6", "Useless, Flightless Fledgling", "Tsukasa", 4, "chain", "tsubasaspring4")     # tsukasaspring6miss
    # 059
    add_avn_event("tsukasaspring7", "The Gays", "Tsukasa", 4, "ch4work3", "tsubasaspring8 == True and tsukasaspring7 == False", None, {1,2,3,4,5}, {"tsukasa_love" : 25})   # tsukasaspring7miss
    add_avn_event("tsukasaspring8", "To Bury a Body", "Tsukasa", 4, "weekend_morning", "tsukasaspring7 == True and tsukasaspring8 == False", None, {6})   # tsukasaspring8miss
    # add_avn_event("tsukasaspring9", "Simple Moving Average", "Tsukasa", 4, "chain", "tsukasaspring8")   # tsukasaspring9miss

    #TSUNEYO
    add_avn_event("ramen1", "Snake Venom", "Tsuneyo", 1, "work3", "day154 == True and ramen1 == False") 
    add_avn_event("tsuneyofirsthall", "The Life of a Blue Whale", "Tsuneyo", 1, "dorm2", "day154 == True and tsuneyofirsthall == False", None, {3})
    add_avn_event("tsuneyohall", "", "Tsuneyo", 1, "dorm2", "tsuneyofirsthall == True and not renpy.seen_label('tsuneyohall') and tsuneyo_love < 5", None, {3})
    add_avn_event("tsuneyodorm5", "Drug Use & Jump-Rope", "Tsuneyo", 1, "dorm2", "ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False", None, {1,2,4,5,6,7}, {"tsuneyo_love" : 5})
    add_avn_event("ramengen", "", "Tsuneyo", 1, "work3", "ramen1 == True and christmas7 == False and not renpy.seen_label('ramengen') and tsuneyo_love < 5")
    add_avn_event("ramen5", "Between the Slurps of Pork Broth", "Tsuneyo", 1, "work3", "ramen1 == True and ramen5 == False", None, None, {"tsuneyo_love" : 5})
    add_avn_event("ramen10", "A Short List", "Tsuneyo", 1, "work3", "ramen5 == True and tsuneyodorm5 == True and ramen10 == False", 168, None, {"tsuneyo_love" : 10})
    add_avn_event("tsuneyodorm10", "The Man Who Loves Nothing", "Tsuneyo", 1, "dorm2", "ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False", 170, {1,2,4,5,6,7}, {"tsuneyo_love" : 10})
    add_avn_event("ramen15", "Seeds", "Tsuneyo", 2, "work3", "christmas7 == True and ramen15 == False", None, None, {"tsuneyo_love" : 15})
    add_avn_event("tsuneyodorm15", "Moe Fan Service", "Tsuneyo", 2, "dorm2", "ramen15 == True and tsuneyodorm15 == False", None, {1,2,4,5,6,7}, {"tsuneyo_love" : 15})
    add_avn_event("tsuneyodorm20", "Fucking...Or What it Means to Live (Shio & Shoyu)", "Tsuneyo", 2, "dorm2", "tsuneyodorm15 == True and day247 == True and tsuneyodorm20 == False", None, {1,2,4,5,6,7}, {"tsuneyo_love" : 20})
    add_avn_event("ramen20", "Blackout", "Tsuneyo", 2, "work3", "tsuneyodorm20 == True and ramen20 == False", None, None, {"tsuneyo_love" : 20})
    add_avn_event("ramen25", "Like Noodles in the Wind", "Tsuneyo", 2, "work3", "secondbeach18 == True and ramen25 == False", None, None, {"tsuneyo_love" : 25})
    # add_avn_event("ramen25p2", "Green Onions and Contraceptives", "Tsuneyo", 2, "chain", "ramen25")
    add_avn_event("tsuneyodorm25", "Unsleeping Aegis", "Tsuneyo", 2, "dorm2", "secondbeach18 == True and tsuneyodorm25 == False", None, {1,2,4,5,6,7}, {"tsuneyo_love" : 25})
    add_avn_event("ramen30", "Things Like Stairs", "Tsuneyo", 2, "work3", "ramen25p2 == True and tsuneyodorm25 == True and ramen30 == False", None, None, {"tsuneyo_love" : 30})
    # add_avn_event("tsuneyoslumber1", "With Her", "Tsuneyo", 3, "chain", "slumberreset2")
    # add_avn_event("tsuneyoslumber2", "Stripped Away", "Tsuneyo", 3, "chain", "tsuneyoslumber1")
    # add_avn_event("tsuneyoslumber3", "Sudden Light", "Tsuneyo", 3, "chain", "tsuneyoslumber2")
    add_avn_event("tsuneyospring1", "Ramen Girl", "Tsuneyo", 4, "ch4work3", "osakospring3 == True and tsuneyospring1 == False", None, {6})
    add_avn_event("tsuneyospring2", "Soothsayer", "Tsuneyo", 4, "ch4work2", "nikispring2 == True and tsuneyospring2 == False", None, {6})
    # add_avn_event("tsuneyospring3", "TH15 15NT M3", "Tsuneyo", 4, "chain", "tsuneyospring2")
    # 044
    # add_avn_event("halloweentsuneyo1", "ELATION PROTOCOL 99: NOODLEFOOT DISCO", "Tsuneyo", 4, "chain", "halloweenyasu1")
    # 047
    add_avn_event("tsuneyospring4", "Thomas Mato, M.D.", "Tsuneyo", 4, "ch4work3", "christmasfive8 == True and tsuneyospring4 == False", None, {5})
    # 048
    add_avn_event("tsuneyospring5", "Yamato Nadeshiko", "Tsuneyo", 4, "ch4work3", "yumispring6 == True and tsuneyospring5 == False", None, None, {"tsuneyo_love" : 35})
    # add_avn_event("tsuneyospring6", "WORMGOD54", "Tsuneyo", 4, "chain", "tsuneyospring5")
    # 052
    # add_avn_event("beachsixtsuneyo1", "Defilement of a Temple", "Tsuneyo", 4, "chain", "beachsixmakoto2")
    # add_avn_event("beachsixtsuneyo2", "Denouement", "Tsuneyo", 4, "chain", "beachsixtsuneyo1")
    # 059
    add_avn_event("tsuneyospring7", "Shaka-Shaka-HEY", "Tsuneyo", 4, "dorm2", "otohaspring7 == True and tsuneyospring7 == False", None, {6,7}, {"tsuneyo_love" : 40})
    add_avn_event("tsuneyospring8", "Anyone for Any Reason", "Tsuneyo", 4, "weekday_morning", "tsuneyospring7 == True and futabaspring4 == True and tsuneyospring8 == False", None, {5})

    #UTA
    add_avn_event("utafirsthall", "Far From Home", "Uta", 2, "dorm2", "day247 == True and utafirsthall == False", None, {5}) 
    add_avn_event("utahallgen", "", "Uta", 2, "dorm2", "utafirsthall == True and not renpy.seen_label('utahallgen') and uta_love < 4", None, {5})
    add_avn_event("utamaid1", "Abuse of Power", "Uta", 2, "work3", "day247 == True and utamaid1 == False") 
    add_avn_event("utamaidgen", "", "Uta", 2, "work3", "utamaid1 == True and chapthreeactive == False and not renpy.seen_label('utamaidgen') and uta_love < 4")
    add_avn_event("utamaid5", "Love Me to Pieces", "Uta", 2, "work3", "utamaid1 == True and utamaid5 == False", None, {6,7}, {"uta_love" : 5})
    add_avn_event("utadorm5", "The VIP Treatment", "Uta", 2, "dorm2", "utamaid5 == True and utadorm5 == False", None, {1,2,3,4,6,7}, {"uta_love" : 5})
    add_avn_event("utadorm10", "Shawshank Redemption", "Uta", 2, "dorm2", "utadorm5 == True and utadorm10 == False", None, {1,3,4,6,7}, {"uta_love" : 10})
    add_avn_event("utamaid10", "Happier Things", "Uta", 2, "work3", "dormwar17 == True and utamaid10 == False", None, None, {"uta_love" : 10})
    add_avn_event("utadorm15", "Facetime With My Mom (Tonight)", "Uta", 2, "dorm2", "utamaid10 == True and utadorm15 == False", None, {1,3,4,6,7}, {"uta_love" : 15})
    add_avn_event("utamaid20", "Veins and the Circulatory System", "Uta", 2, "work3", "bathhouse20part2 == True and utadorm15 == True and utamaid20 == False", None, None, {"uta_love" : 20})
    # add_avn_event("utadorm20", "Blood Everywhere", "Uta", 2, "chain", "utamaid20")
    # add_avn_event("utaarchery1", "Impulse", "Uta", 3, "chain", "ioarchery1")
    add_avn_event("utamaid25p1", "Where Wishes Come True", "Uta", 3, "work1", "utaarchery1 == True and utamaid25p1 == False", None, None, {"uta_love" : 25})
    # add_avn_event("utamaid25p2", "After the Rain", "Uta", 3, "chain", "utamaid25p1")
    add_avn_event("utadorm30", "Uta-chan", "Uta", 3, "dorm2", "utamaid25p2 == True and utadorm30 == False", None, {1,2,3,4,6,7}, {"uta_love" : 30})
    add_avn_event("utaspecial35", "Young & Stupid", "Uta", 3, "weekday_morning", "beachwars19 == True and utaspecial35 == False", 622, {2}, {"uta_love" : 35})
    add_avn_event("utadate35", "Enjo Kousai", "Uta", 3, "date_morning", "utaspecial35 == True and utadate35 == False", None, None, {"uta_love" : 35})
    add_avn_event("utadorm40p1", "Whore", "Uta", 3, "dorm2", "utadate35 == True and wakanadate25p3 == True and utadorm40p1 == False", None, {1,3,4,6,7}, {"uta_love" : 40})
    # add_avn_event("utadorm40p2", "The Girl From Nara", "Uta", 3, "chain", "utadorm40p1")
    # 041
    add_avn_event("utaspring1", "To Be Wanted", "Uta", 4, "ch4work1", "yasuspring3 == True and utaspring1 == False", None, {6})
    add_avn_event("utaspring2", "Meet Me At Our Spot", "Uta", 4, "ch4work3", "yasuspring3 == True and utaspring1 == True and iospring2 == True and utaspring2 == False", None, {3})
    # 042
    # add_avn_event("beachfive14", "Reasons For Rain", "Uta", 4, "chain", "")
    # 048
    add_avn_event("utaspring3", "Songs of Autumn", "Uta", 4, "ch4work3", "iospring1 == True and iospring5 == True and utaspring3 == False", None, {1,2,3,4})
    # add_avn_event("utaspring4", "Heebie-Jeebies", "Uta", 4, "chain", "utaspring3")
    # add_avn_event("utaspring5", "A Thousand Times, Yes", "Uta", 4, "chain", "utaspring4")
    # 057
    add_avn_event("utaspring6", "Stolen Valor", "Uta", 4, "ch4work1", "iospring7 == True and mikuspring7 == True and utaspring6 == False and utaspring6miss == False", None, {1,2,3,4}) # utaspring6miss
    add_avn_event("utaspring7", "ASL", "Uta", 4, "ch4work3", "(utaspring6 == True or utaspring6miss == True) and utaspring7 == False", None, None, {"uta_love" : 30})
    # add_avn_event("utaspring8", "ELATION PROTOCOL 99: DEFINE INTERVENTION", "Uta", 4, "chain", "utaspring7")
    # 060
    # add_avn_event("utaspring9", "Secret Admirer", "Uta", 4, "chain", "ayanespring4")

    #WAKANA
    add_avn_event("wakanadate1", "To the River", "Wakana", 2, "date_morning", "wakananumber == True and wakanadate1 == False")
    add_avn_event("wakananightgen", "", "Wakana", 2, "date_night", "wakanadate1 == True and not renpy.seen_label('wakananightgen') and wakana_love < 5")
    add_avn_event("wakanadate5", "Soup, or Another Year With You", "Wakana", 2, "date_night", "wakanadate1 == True and kaoridate15p3 == True and wakanadate5 == False", None, None, {"wakana_love" : 5})
    add_avn_event("wakanadate15", "Pseudonym", "Wakana", 3, "date_morning", "yumiyukispecial1 == True and wakanadate15 == False", None, None, {"wakana_love" : 15})
    # add_avn_event("wakanaspecial15", "Don't Hold Back", "Wakana", 3, "chain", "imanispecial1")
    add_avn_event("wakanadate25p1", "The Desk Scene", "Wakana", 3, "weekday_morning", "beachwars19 == True and rikadive1 == True and wakanadate25p1 == False", 622, {2}, {"wakana_love" : 25})
    # add_avn_event("wakanadate25p2", "Human Error", "Wakana", 3, "chain", "wakanadate25p1")
    # add_avn_event("wakanadate25p3", "Follow My Lead", "Wakana", 3, "chain", "wakanadate25p2")
    # 041
    add_avn_event("wakanaspring1", "Enough is Not Enough", "Wakana", 4, "weekend_morning", "yasuspring3 == True and utaspring2 == True and norikospring2 == True and kirinspring1 == True and iospring2 == True and wakanaspring1 == False", None, {6})
    # add_avn_event("wakanaspring2", "In the Morning, I'll Forget", "Wakana", 4, "chain", "wakanaspring1")
    # 043
    add_avn_event("wakanaspring3", "I'm Wide Awake, It's Morning", "Wakana", 4, "weekend_morning", "osakospring4 == True and wakanaspring3 == False", None, {6})
    # add_avn_event("wakanaspring4", "Dark White (Pretty Joy)", "Wakana", 4, "chain", "wakanaspring3")
    # 051
    add_avn_event("wakanaspring5", "Connect the Dots", "Wakana", 4, "weekend_morning", "amispring3 == True and wakanaspring5 == False", None, {6,7})
    add_avn_event("wakanaspring6", "From the Horse’s Mouth", "Wakana", 4, "ch4work2", "wakanaspring5 == True and wakanaspring6 == False", None, {3})
    # 056
    add_avn_event("wakanaspring7", "Road to Nowhere", "Wakana", 4, "ch4work3", "iospring8 == True and rinspring9 == True and toukaspring8 == True and osakospring9 == True and makispring3 == True and wakanaspring7 == False", None, None, {"wakana_love" : 40})   # if 055 
    add_avn_event("wakanaspring8", "Dick Wizard", "Wakana", 4, "weekday_morning", "wakanaspring7 == True and wakanaspring8 == False", None, {1,2,3,4,5})

    #YASU
    add_avn_event("yasufirsthall", "The Hole That Swallowed Everything", "Yasu", 2, "dorm2", "day304 == True and yasufirsthall == False", None, {4})
    add_avn_event("yasuhallgen", "", "Yasu", 2, "dorm2", "yasufirsthall == True and not renpy.seen_label('yasuhallgen') and yasu_love < 5", None, {4})
    add_avn_event("church1", "Transference", "Yasu", 2, "work3", "yasufirsthall == True and ramen20 == True and church1 == False")
    add_avn_event("churchgen", "", "Yasu", 2, "work3", "church1 == True and chapthreeactive == False and not renpy.seen_label('churchgen') and yasu_love < 5")
    add_avn_event("church5", "Armor of Older Gods", "Yasu", 2, "work3", "church1 == True and church5 == False", None, None, {"yasu_love" : 5})
    add_avn_event("yasudorm10", "Repentance", "Yasu", 2, "dorm2", "yasufirsthall == True and toukadorm5 == True and makotowinterbeach4 == True and yasudorm10 == False", None, {1,2,3,5,6,7}, {"yasu_love" : 10})
    add_avn_event("church10", "Sakura Season", "Yasu", 2, "work3", "yasudorm10 == True and church10 == False", None, {7}, {"yasu_love" : 10})
    add_avn_event("church15", "Down The Rabbit Hole", "Yasu", 3, "work3", "chapthree8 == True and church15 == False", None, None, {"yasu_love" : 15})
    add_avn_event("yasuspecial15", "Sore Thumb", "Yasu", 3, "weekday_morning", "chapthree8 == True and church15 == True and yasuspecial15 == False", 500)
    add_avn_event("church20", "Mother Duck", "Yasu", 3, "work3", "yasuspecial15 == True and church20 == False", None, None, {"yasu_love" : 20})
    add_avn_event("yasudorm20", "Glossolalia", "Yasu", 3, "dorm2", "church20 == True and yasudorm20 == False", None, {1,3,5,6,7}, {"yasu_love" : 20})
    # add_avn_event("yasuspecial20", "The River Styx", "Yasu", 3, "chain", "nodokaspecial15p2")
    add_avn_event("church25", "Frankincense & Myrrh", "Yasu", 3, "work3", "predormwars3 == True and church25 == False", None, None, {"yasu_love" : 25})
    add_avn_event("yasudorm25", "Hand of God", "Yasu", 3, "dorm2", "church25 == True and yasudorm25 == False", None, {4}, {"yasu_love" : 25})
    add_avn_event("yasudorm30", "An Apple Each Day", "Yasu", 3, "dorm2", "yasudorm25 == True and yasudorm30 == False", None, {1,3,5,6,7}, {"yasu_love" : 25})
    # 041
    add_avn_event("yasuspring1", "Throne of Flesh", "Yasu", 4, "weekend_morning", "toukaspring2 == True and yasuspring1 == False", None, {7})
    add_avn_event("yasuspring2", "Fruits of Torment", "Yasu", 4, "ch4work3", "yasuspring1 == True and yasuspring2 == False", None, {6})
    # add_avn_event("yasuspring3", "The Art of Drowning", "Yasu", 4, "chain", "yasuspring2")
    # 044
    # add_avn_event("halloweenyasu1", "Infinity House", "Yasu", 4, "chain", "halloweenfive4")
    # 048
    add_avn_event("yasuspring4", "False Chameleon", "Yasu", 4, "ch4work2", "karinspring5 == True and yasuspring4 == False", None, {6,7})
    # add_avn_event("yasuspring5", "Etinsib Ziwa & The Book of Colors", "Yasu", 4, "chain", "yasuspring4")
    # 054
    # add_avn_event("yasuchristmalloween1", "Etinsi", "Yasu", 4, "chain", "christmalloween1")
    # add_avn_event("yasuchristmalloween2", "Etinsi", "Yasu", 4, "chain", "chikachristmalloween1")
    60
    add_avn_event("yasuspring6", "Child of Light", "Yasu", 4, "ch4work3", "tsuneyospring8 == True and yasuspring6 == False", None, {1}, {"yasu_love" : 30})
    add_avn_event("yasuspring7", "Ichigo Daifuku", "Yasu", 4, "ch4work3", "yasuspring6 == True and yasuspring7 == False", None, {5}, {"yasu_love" : 30})
    # add_avn_event("yasuspring8", "Heretic", "Yasu", 4, "chain", "yasuspring7")

    #YUKI
    add_avn_event("yukidate1", "Rule #1", "Yuki", 2, "date_night", "streets30 == True and ramen20 == True and yukidate1 == False")
    add_avn_event("yukigennight", "", "Yuki", 2, "date_night", "yukidate1 == True and chapthreeactive == False and not renpy.seen_label('yukigennight') and yuki_love < 5")
    add_avn_event("yukidate5", "Better Off Alone", "Yuki", 2, "date_night", "yumidorm30 == True and yukidate1 == True and yukidate5 == False", None, None, {"yuki_love" : 5})
    add_avn_event("yukidate10", "Opposite Directions", "Yuki", 2, "date_night", "yukidate5 == True and kirindorm25 == True and yukidate10 == False", None, None, {"yuki_love" : 10})
    # add_avn_event("yukidate10p2", "A Thing of the Past", "Yuki", 2, "chain", "yukidate10")
    add_avn_event("yukidate20p1", "Funeral Plans", "Yuki", 3, "date_night", "nikilovesyou3 == True and yukidate20p1 == False", None, {5}, {"yuki_love" : 20})
    # add_avn_event("yukidate20p2", "Douchebag McDouchefuck", "Yuki", 3, "chain", "yukidate20p1")
    add_avn_event("yukidate25", "Pride & Joy", "Yuki", 3, "work3", "yukidate20p2 == True and yukidate25 == False", None, {5,6}, {"yuki_love" : 25}) # hint_girl = Yuki
    # add_avn_event("yukicamp1", "Big Dog", "Yuki", 4, "chain", "saracamp1")
    # add_avn_event("yukicamp2", "My Heart is in Rotenburg", "Yuki", 4, "camp", 'Choose "Drink with Yuki" in camp, yukicamp1')
    # 043
    # add_avn_event("yukispring1", "Small Plastic Baggies", "Yuki", 4, "chain", "saraspring1")
    # add_avn_event("yukispring2", "Better Than Sex", "Yuki", 4, "chain", "yukispring1")
    # 050
    # add_avn_event("yukispring3", "As the Footsteps Die Out Forever", "Yuki", 4, "chain", "yumispring7")
    # add_avn_event("yukispring4", "Heart of Fear", "Yuki", 4, "chain", "yukispring3")
    # add_avn_event("yukispring5", "When I Say “Jump”", "Yuki", 4, "chain", "amispring3")
    # 057
    add_avn_event("yukispring6", "When", "Bridge Burner", 4, "ch4work3", "(mollyspring4 == True or mollyspring4miss == True) and yukispring6 == False", None, {1,2,3,4,5}, {"yuki_love" : 30})
    # add_avn_event("yukispring7", "When", "Yuki-onna", 4, "chain", "sanaspring5")

    #YUMI
    add_avn_event("firsttimestreets", "Five Million Dollars", "Yumi", 1, "work2", "firsttimeshrine == True and firsttimestreets == False") 
    add_avn_event("yumifirsthall", "Micropenis", "Yumi", 1, "dorm", "dorm > 0 and yumifirsthall == False", None, {1})
    add_avn_event("streets5", "Three Second Smile", "Yumi", 1, "work2", "firsttimestreets == True and streets5 == False", 26, None, {"yumi_love" : 5})
    add_avn_event("streets10", "I See You", "Yumi", 1, "work2", "day44 == True and streets10 == False", 35, None, {"yumi_love" : 10})
    add_avn_event("yumihall", "", "Yumi", 1, "dorm", "yumiblock == False and yumifirsthall == True and not renpy.seen_label('yumihall') and yumidorm5 == False and yumi_love < 5", 10, {1})
    add_avn_event("yumidorm5", "Fuck The Police", "Yumi", 1, "dorm", "streets10 == True and yumidorm5 == False", 25, {2,3,4,5,6,7}, {"yumi_love" : 5})
    add_avn_event("yumidorm10", "Yumi Revitalization Project", "Yumi", 1, "dorm", "yumidorm5 == True and yumidorm10 == False", 35, {2,3,4,5,6,7}, {"yumi_love" : 10})
    add_avn_event("yumidorm15", "Worse Comes to Worst", "Yumi", 1, "dorm", "yumidorm10 == True and cafe20 == True and yumidorm15 == False", 55, {2,3,4,5,6,7}, {"yumi_love" : 15})
    add_avn_event("streets15", "Apples to Apples", "Yumi", 1, "work2", "yumidorm15 == True and streets15 == False", 55, None, {"yumi_love" : 15})
    add_avn_event("streets20", "Token Tsundere", "Yumi", 1, "work2", "streets15 == True and ramen1 == True and streets20 == False", 85, None, {"yumi_love" : 20})
    add_avn_event("yumidorm20", "Great Expectations", "Yumi", 1, "dorm", "streets20 == True and yumidorm20 == False", 85, {2,3,4,5,6,7}, {"yumi_love" : 20})
    add_avn_event("streets25", "A Place Like This", "Yumi", 1, "work2", "yumidorm20 == True and streets25 == False", 125, None, {"yumi_love" : 25})
    add_avn_event("yumidorm25", "Caught in the Vortex", "Yumi", 1, "dorm", "streets25 == True and yumidorm25 == False", 125, {2,3,4,5,6,7}, {"yumi_love" : 25})
    add_avn_event("streets30", "Where the Sidewalk Ends", "Yumi", 2, "work2", "day271 == True and streets30 == False", 185, None, {"yumi_love" : 30})
    add_avn_event("yumidorm30", "Walls Too Thick to Hear Through", "Yumi", 2, "dorm", "streets30 == True and yukidate1 == True and yumidorm30 == False", 185, {2,3,4,5,6,7}, {"yumi_love" : 30})
    add_avn_event("yumidorm35", "Tech Support", "Yumi", 2, "dorm", "yumidorm30 == True and yumidorm35 == False", None, {2,3,4,5,6,7}, {"yumi_love" : 35})
    add_avn_event("yumicallnight35", "Abyss", "Yumi", 2, "date_night", "yumidorm35 == True and yumicallnight35 == False", None, {1,2,3,4,5,7}, {"yumi_love" : 35})
    # add_avn_event("yumispecial40", "Reconciliation", "Yumi", 2, "chain", "yukidate10p2")
    # add_avn_event("yumispecial40p2", "Neon Heart (If I Close My Eyes)", "Yumi", 2, "chain", "yumispecial40")
    add_avn_event("streets40", "Unsung Heroes", "Yumi", 2, "work2", "yumispecial40p2 == True and streets40 == False", None, None, {"yumi_love" : 40})
    add_avn_event("yumispecial45", "See You Around", "Yumi", 2, "weekday_morning", "streets40 == True and yumispecial45 == False", 417, {5})
    # add_avn_event("yumislumber1", "Two Months of Nothing", "Yumi", 3, "chain", "slumberreset2")
    # add_avn_event("yumislumber2", "Loggerhead", "Yumi", 3, "chain", "yumislumber1")
    # add_avn_event("yumislumber3", "A Day in the Life", "Yumi", 3, "chain", "yumislumber2")
    # add_avn_event("yumispring1", "Kid of the Month", "Yumi", 4, "chain", "tsuneyospring1")
    add_avn_event("yumispring2", "Frog Boy", "Yumi", 4, "ch4work2", "tsuneyospring1 == True and yumispring2 == False", None, {7})
    # 042
    # add_avn_event("beachfive13", "Wake Me Up When It's Over", "Yumi", 4, "chain", "")
    # 043
    add_avn_event("yumispring3", "A Life I Never Wanted", "Yumi", 4, "weekend_morning", "beachfive16 == True and yumispring3 == False", None, {6})
    # 048
    add_avn_event("yumispring4", "Pogonomyrmex Occidentalis Owyheei", "Yumi", 4, "ch4work2", "rikaspring4 == True and yumispring4 == False", None, {1,2,3,4}, {"yumi_love" : 45})
    # add_avn_event("yumispring5", "The Dragon", "Yumi", 4, "chain", "yumispring4")
    # add_avn_event("yumispring6", "Ittekimasu", "Yumi", 4, "chain", "yumispring5")
    # 050
    add_avn_event("yumispring7", "Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS", "Yumi", 4, "ch4work3", "ayanespring3 == True and yumispring7 == False", None, {7})
    # 051
    add_avn_event("yumispring8", "Death With Dignity", "Yumi", 4, "ch4work2", "yukispring5 == True and yumispring8 == False", None, {1,2,3,4,5})
    # 059
    add_avn_event("yumispring9", "Scar Tissue", "Yumi", 4, "ch4work3", "postwarsix1 == True and yumispring9 == False", None, {1,2,3,4}, {"yumi_love" : 50})
    # add_avn_event("yumispring10", "Chabudai (Plastic Corpses)", "Yumi", 4, "chain", "yumispring9")





    # GENERICS - common repeatable events (a check has been added to the condition that the event has not yet been viewed, i.e. each event is played only once)
    # note: christmas7 - ch2, chapthreeactive - ch3, chap4active - ch4

    #AMI
    add_avn_event("amisroom3to4", "generic", "Ami", 1, "work1", "firsttimeamisroom == True and not renpy.seen_label('amisroom3to4')", 30)
    add_avn_event("amimaidgen", "generic", "Ami", 3, "work1", "chapthreeactive == True and not renpy.seen_label('amimaidgen')")
    add_avn_event("amisummer2maidgen", "generic", "Ami", 2, "work1", "amimaid30 == True and chapthreeactive == False and not renpy.seen_label('amisummer2maidgen')")
    add_avn_event("amigenafternoon", "generic", "Ami", 1, "date_afternoon", "chapthreeactive == False and not renpy.seen_label('amigenafternoon')", 30)
    add_avn_event("amisummer2noongen", "generic", "Ami", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('amisummer2noongen')")
    add_avn_event("amigennight", "generic", "Ami", 1, "date_night", "christmas7 == False and chapthreeactive == False and not renpy.seen_label('amigennight')", 30)
    add_avn_event("amigennight2", "generic", "Ami", 2, "date_night", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('amigennight2')")
    add_avn_event("amisummer2nightgen", "generic", "Ami", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('amisummer2nightgen')")
    add_avn_event("amihall", "generic", "Ami", 1, "dorm", "amifirsthall == True and not renpy.seen_label('amihall')", 20, {5})
    add_avn_event("amidormgen_avn", "generic", "Ami", 1, "dorm", "amisroom5 == True and not renpy.seen_label('amidormgen_avn')", 20, {1,2,3,4,6,7})
    add_avn_event("amiinviteaff", "generic", "Ami", 1, "invite", "amiblock == False and (amiinvite2 == True or amiinvite2miss == True) and not renpy.seen_label('amiinviteaff')")
    add_avn_event("amispringmaidgen", "generic", "Ami", 4, "ch4work1", "senseisad == False and amiblock == False and not renpy.seen_label('amispringmaidgen')")
    add_avn_event("amispringnoongen", "generic", "Ami", 4, "ch4date_afternoon", "amiblock == False and not renpy.seen_label('amispringnoongen')")
    add_avn_event("amispringnightgen", "generic", "Ami", 4, "ch4date_night", "amiblock == False and not renpy.seen_label('amispringnightgen')")

    #AYANE
    add_avn_event("dojo3to4", "generic", "Ayane", 1, "work2", "firsttimedojo == True and christmas7 == False and not renpy.seen_label('dojo3to4')", 20)
    add_avn_event("dojogen2", "generic", "Ayane", 2, "work2", "chapthreeactive == False and christmas7 == True and not renpy.seen_label('dojogen2')")
    add_avn_event("ayanesummer2dojogen", "generic", "Ayane", 3, "work2", "chapthreeactive == True and not renpy.seen_label('ayanesummer2dojogen')")
    add_avn_event("callayanemorning", "generic", "Ayane", 1, "date_morning", "amisroom5 == True and ayanedorm10 == True and not renpy.seen_label('callayanemorning')", 20)
    add_avn_event("callayanemorning", "generic", "Ayane", 2, "date_morning", "christmas7 == True and not renpy.seen_label('ayanemorninggen2')")  # one entry - callayanemorning
    add_avn_event("ayanesummer2morninggen", "generic", "Ayane", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('ayanesummer2morninggen')")
    add_avn_event("ayanesummer2nightgen", "generic", "Ayane", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('ayanesummer2nightgen')")
    add_avn_event("ayanehall", "generic", "Ayane", 1, "dorm", "ayanefirsthall == True and not renpy.seen_label('ayanehall')", 20, {4})
    add_avn_event("ayanedormgen_avn", "generic", "Ayane", 1, "dorm", "ayanedorm5 == True and not renpy.seen_label('ayanedormgen_avn')", 20, {1,2,3,5,6,7})
    add_avn_event("ayaneinviteaff", "generic", "Ayane", 1, "invite", "ayaneinvite2 == True and not renpy.seen_label('ayaneinviteaff')")
    add_avn_event("ayanespringpoolgen", "generic", "Ayane", 4, "ch4work2", "not renpy.seen_label('ayanespringpoolgen')")
    add_avn_event("ayanespringmorninggen", "generic", "Ayane", 4, "ch4date_morning", "not renpy.seen_label('ayanespringmorninggen')")
    add_avn_event("ayanespringnightgen", "generic", "Ayane", 4, "ch4date_night", "not renpy.seen_label('ayanespringnightgen')")
    add_avn_event("ayanedormgen_avn", "generic", "Ayane", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('ayanedormgen_avn')")

    #CHIKA
    add_avn_event("mall2to4", "generic", "Chika", 1, "work2", "firsttimemall == True and not renpy.seen_label('mall2to4')", 20)
    add_avn_event("mallgen2", "generic", "Chika", 2, "work2", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('mallgen2')")
    add_avn_event("chikasummer2mallgen", "generic", "Chika", 3, "work2", "chapthreeactive == True and not renpy.seen_label('chikasummer2mallgen')")
    add_avn_event("callchikamorning", "generic", "Chika", 1, "date_morning", "chikanumber == True and not renpy.seen_label('callchikamorning')")
    add_avn_event("chikasummer2morninggen", "generic", "Chika", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('chikasummer2morninggen')")
    add_avn_event("callchikanight", "generic", "Chika", 1, "date_night", "chikanumber == True and not renpy.seen_label('callchikanight')")
    add_avn_event("callchikanight", "generic", "Chika", 2, "date_night", "christmas7 == True and not renpy.seen_label('chikanightgen2')")    # one entry - callchikanight
    add_avn_event("callchikanight", "generic", "Chika", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('chikasummer2nightgen')")    # one entry - callchikanight
    add_avn_event("chikahall", "generic", "Chika", 1, "dorm", "chikafirsthall == True and not renpy.seen_label('chikahall')", 20, {3})
    add_avn_event("chikadormgen_avn", "generic", "Chika", 1, "dorm", "chikadorm5 == True and not renpy.seen_label('chikadormgen_avn')", 20, {1,2,4,5,6,7})
    add_avn_event("chikainviteaff", "generic", "Chika", 1, "invite", "chikainvite2 == True and not renpy.seen_label('chikainviteaff')")
    add_avn_event("chikaspringmaidgen", "generic", "Chika", 4, "ch4work2", "senseisad == False and chikablock == False and not renpy.seen_label('chikaspringmaidgen')")
    add_avn_event("chikadormgen_avn", "generic", "Chika", 4, "dorm", "(senseisad == False or mollyspring2 == True) and chikablock == False and escapeshampoo == False and not renpy.seen_label('chikadormgen_avn')")
    # 045
    add_avn_event("callchikanight", "generic", "Chika", 4, "date_night", "chap4active == True and senseisad == False and chikablock == True and not renpy.seen_label('chikaspringnightgen')")    # one entry - callchikanight

    #CHINAMI
    add_avn_event("chinamigenmorning", "generic", "Chinami", 1, "date_morning", "chinaminumber == True and chinamidate1 == True and christmas7 == False and not renpy.seen_label('chinamigenmorning')")
    add_avn_event("chinamimorninggen2", "generic", "Chinami", 2, "date_morning", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('chinamimorninggen2')")
    add_avn_event("chinamisummer2morninggen", "generic", "Chinami", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('chinamisummer2morninggen')")
    add_avn_event("chinamigenafternoon", "generic", "Chinami", 1, "date_afternoon", "chinaminumber == True and chinamidate1 == True and christmas7 == False and not renpy.seen_label('chinamigenafternoon')")
    add_avn_event("chinaminoongen2", "generic", "Chinami", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('chinaminoongen2')")
    add_avn_event("chinamisummer2noongen", "generic", "Chinami", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('chinamisummer2noongen')")
    add_avn_event("chinamispringmorninggen", "generic", "Chinami", 4, "ch4date_morning", "senseisad == False and not renpy.seen_label('chinamispringmorninggen')")
    add_avn_event("chinamispringnoongen", "generic", "Chinami", 4, "ch4date_afternoon", "senseisad == False and not renpy.seen_label('chinamispringnoongen')")

    #FUTABA
    add_avn_event("library2to4", "generic", "Futaba", 1, "work1", "firsttimelibrary == True and not renpy.seen_label('library2to4')", 15)
    add_avn_event("futabamorninggen2", "generic", "Futaba", 2, "work1", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('futabamorninggen2')")
    add_avn_event("futabasummer2librarygen", "generic", "Futaba", 3, "work1", "chapthreeactive == True and not renpy.seen_label('futabasummer2librarygen')")
    add_avn_event("callfutabaafternoon", "generic", "Futaba", 1, "date_afternoon", "futabanumber == True and futabadorm35 == True and not renpy.seen_label('callfutabaafternoon')")
    add_avn_event("futabanoongen2", "generic", "Futaba", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('futabanoongen2')")
    add_avn_event("futabasummer2noongen", "generic", "Futaba", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('futabasummer2noongen')")
    add_avn_event("futabadorm6to9_avn", "generic", "Futaba", 1, "dorm", "futabafirstvisit == True and not renpy.seen_label('futabadorm6to9_avn')", 20, {1,3,4,5,6,7})
    add_avn_event("futabahall", "generic", "Futaba", 1, "dorm", "futabafirsthall == True and not renpy.seen_label('futabahall')", 20, {2})
    add_avn_event("futabainviteaff", "generic", "Futaba", 1, "invite", "futabainvite2 == True and not renpy.seen_label('futabainviteaff')")
    add_avn_event("futabaspringlibrarygen", "generic", "Futaba", 4, "ch4work1", "senseisad == False and not renpy.seen_label('futabaspringlibrarygen')")
    add_avn_event("futabaspringnoongen", "generic", "Futaba", 4, "ch4date_morning", "senseisad == False and not renpy.seen_label('futabaspringnoongen')")
    add_avn_event("futabadorm6to9_avn", "generic", "Futaba", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('futabadorm6to9_avn')")

    #HARUKA
    add_avn_event("harukacafegen", "generic", "Haruka", 1, "work1", "harukadate1 == True and christmas7 == False and not renpy.seen_label('harukacafegen')")
    add_avn_event("harukamorninggen2", "generic", "Haruka", 2, "work1", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('harukamorninggen2')")
    add_avn_event("harukasummer2cafegen", "generic", "Haruka", 3, "work1", "chapthreeactive == True and not renpy.seen_label('harukasummer2cafegen')")
    # add_avn_event("callharukaafternoon", "generic", "Haruka", 1, "date_afternoon", "harukadate5 == True and not renpy.seen_label('callharukaafternoon')")
    add_avn_event("harukagennight", "generic", "Haruka", 1, "date_night", "harukadate5 == True and christmas7 == False and not renpy.seen_label('harukagennight')")
    add_avn_event("harukanightgen2", "generic", "Haruka", 2, "date_night", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('harukanightgen2')")
    add_avn_event("harukasummer2nightgen", "generic", "Haruka", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('harukasummer2nightgen')")
    add_avn_event("harukainviteaff", "generic", "Haruka", 1, "invite", "harukainvite2 == True and not renpy.seen_label('harukainviteaff')")
    add_avn_event("harukaspringcafegen", "generic", "Haruka", 4, "ch4work1", "(senseisad == False or saracamp2 == True) and cafeclosed == False and not renpy.seen_label('harukaspringcafegen')")
    add_avn_event("harukaspringnightgen", "generic", "Haruka", 4, "ch4date_night", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('harukaspringnightgen')")

    #IMANI
    add_avn_event("imanidive", "generic", "Imani", 3, "work3", "wakanaspecial15 == True and imanidate1 == True and not renpy.seen_label('imanidive')", None, {5})
    add_avn_event("imanimorninggen", "generic", "Imani", 3, "date_morning", "imanidate1 == True and not renpy.seen_label('imanimorninggen')")
    add_avn_event("imanispringdivegen", "generic", "Imani", 4, "work3", "(senseisad == False or imanispring2 == True) and not renpy.seen_label('imanispringdivegen')", None, {5})
    add_avn_event("imanispringnoongen", "generic", "Imani", 4, "ch4date_afternoon", "senseisad == False and cafeclosed == False and not renpy.seen_label('imanispringnoongen')")
    add_avn_event("imanispringnightgen", "generic", "Imani", 4, "ch4date_night", "senseisad == False and not renpy.seen_label('imanispringnightgen')")

    #IO
    add_avn_event("bathhousegen", "generic", "Io", 2, "work2", "bathhouse1 == True and not renpy.seen_label('bathhousegen')")
    add_avn_event("iosummer2bathgen", "generic", "Io", 3, "work2", "chapthreeactive == True and not renpy.seen_label('iosummer2bathgen')")
    add_avn_event("calliomorning", "generic", "Io", 2, "date_morning", "ionumber == True and not renpy.seen_label('calliomorning')")
    add_avn_event("iosummer2morninggen", "generic", "Io", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('iosummer2morninggen')")
    add_avn_event("callionight", "generic", "Io", 2, "date_night", "ionumber == True and not renpy.seen_label('callionight')")
    add_avn_event("iohall", "generic", "Io", 2, "dorm2", "iofirsthall == True and not renpy.seen_label('iohall')", None, {2})
    add_avn_event("iodormgen", "generic", "Io", 2, "dorm2", "iodorm5 == True and not renpy.seen_label('iodormgen')", None, {1,3,4,5,6,7})
    add_avn_event("iospringbathhousegen", "generic", "Io", 4, "ch4work2", "senseisad == False and ioblock == False and not renpy.seen_label('iospringbathhousegen')")
    add_avn_event("iospringmorninggen", "generic", "Io", 4, "ch4date_morning", "senseisad == False and not renpy.seen_label('iospringmorninggen')")
    add_avn_event("iospringnightgen", "generic", "Io", 4, "ch4date_night", "senseisad == False and not renpy.seen_label('iospringnightgen')")
    add_avn_event("iodormgen", "generic", "Io", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and ioblock == False and escapeshampoo == False and not renpy.seen_label('iodormgen')")

    #KAORI
    add_avn_event("kaorigenmorning", "generic", "Kaori", 1, "date_morning", "kaorinumber == True and kaoridate1 == True and not renpy.seen_label('kaorigenmorning')")
    add_avn_event("kaorimorninggen2", "generic", "Kaori", 2, "date_morning", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('kaorimorninggen2')")
    add_avn_event("kaorisummer2morninggen", "generic", "Kaori", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('kaorisummer2morninggen')")
    add_avn_event("kaorigenafternoon", "generic", "Kaori", 1, "date_afternoon", "kaorinumber == True and kaoridate1 == True and not renpy.seen_label('kaorigenafternoon')")
    add_avn_event("kaorinoongen2", "generic", "Kaori", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('kaorinoongen2')")
    add_avn_event("kaorisummer2noongen", "generic", "Kaori", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('kaorisummer2noongen')")
    add_avn_event("kaorispringmorninggen", "generic", "Kaori", 4, "ch4date_morning", "not renpy.seen_label('kaorispringmorninggen')")
    add_avn_event("kaorispringnightgen", "generic", "Kaori", 4, "ch4date_night", "not renpy.seen_label('kaorispringnightgen')")
    # 057
    add_avn_event("kaoriinviteaff", "generic", "Kaori", 4, "invite", "kaoriinvite2 == True and not renpy.seen_label('kaoriinviteaff')")

    #KARIN
    add_avn_event("karinsoccergen", "generic", "Karin", 1, "work1", "soccer20 == True and christmas7 == False and not renpy.seen_label('karinsoccergen')")
    add_avn_event("karinsoccergen2", "generic", "Karin", 2, "work1", "christmas7 == True and not renpy.seen_label('karinsoccergen2')")
    add_avn_event("karinsummer2morninggen", "generic", "Karin", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('karinsummer2morninggen')")
    add_avn_event("karingenafternoon", "generic", "Karin", 1, "date_afternoon", "karindate1 == True and not renpy.seen_label('karingenafternoon')")
    add_avn_event("karinnoongen2", "generic", "Karin", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('karinnoongen2')")
    add_avn_event("karinsummer2poolgen", "generic", "Karin", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('karinsummer2poolgen')")
    add_avn_event("karinspringpoolgen", "generic", "Karin", 4, "ch4work2", "senseisad == False and not renpy.seen_label('karinspringpoolgen')")
    add_avn_event("karinspringmorninggen", "generic", "Karin", 4, "ch4date_morning", "senseisad == False and karinbetter == False and not renpy.seen_label('karinspringmorninggen')")

    #KIRIN
    add_avn_event("kirinsoccergen", "generic", "Kirin", 1, "work1", "soccer20 == True and christmas7 == False and not renpy.seen_label('kirinsoccergen')")
    add_avn_event("kirinsoccergen2", "generic", "Kirin", 2, "work1", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('kirinsoccergen2')")
    add_avn_event("kirinsummer2archerygen", "generic", "Kirin", 3, "work1", "chapthreeactive == True and not renpy.seen_label('kirinsummer2archerygen')")
    add_avn_event("kiringenafternoon", "generic", "Kirin", 1, "date_afternoon", "kirindate1 == True and christmas7 == False and not renpy.seen_label('kiringenafternoon')")
    add_avn_event("kirinnoongen2", "generic", "Kirin", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('kirinnoongen2')")
    add_avn_event("kirinsummer2noongen", "generic", "Kirin", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('kirinsummer2noongen')")
    add_avn_event("kiringennight", "generic", "Kirin", 1, "date_night", "kirindate1 == True and christmas7 == False and not renpy.seen_label('kiringennight')")
    add_avn_event("kirinnightgen2", "generic", "Kirin", 2, "date_night", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('kirinnightgen2')")
    add_avn_event("kirinsummer2nightgen", "generic", "Kirin", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('kirinsummer2nightgen')")
    add_avn_event("kirinhall", "generic", "Kirin", 1, "dorm2", "kirinfirsthall == True and not renpy.seen_label('kirinhall')", None, {4})
    add_avn_event("kirindormgen", "generic", "Kirin", 1, "dorm2", "kirindorm10 == True and not renpy.seen_label('kirindormgen')", None, {1,2,3,5,6,7})
    add_avn_event("kirininviteaff", "generic", "Kirin", 2, "invite", "kirininvite2 == True and not renpy.seen_label('kirininviteaff')")
    add_avn_event("kirinspringnoongen", "generic", "Kirin", 4, "ch4date_afternoon", "senseisad == False and not renpy.seen_label('kirinspringnoongen')")
    add_avn_event("kirinspringnightgen", "generic", "Kirin", 4, "ch4date_night", "senseisad == False and not renpy.seen_label('kirinspringnightgen')")
    add_avn_event("kirindormgen", "generic", "Kirin", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('kirindormgen')")

    #MAKI
    add_avn_event("makigennight", "generic", "Maki", 1, "work3", "makiblock == False and makidate1 == True and christmas7 == False and not renpy.seen_label('makigennight')")
    add_avn_event("makinightgen2", "generic", "Maki", 2, "work3", "makiblock == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('makinightgen2')")
    add_avn_event("makisummer2porngen", "generic", "Maki", 3, "work3", "makiblock == False and chapthreeactive == True and not renpy.seen_label('makisummer2porngen')")
    add_avn_event("makisummer2morninggen", "generic", "Maki", 3, "date_morning", "makiblock == False and chapthreeactive == True and not renpy.seen_label('makisummer2morninggen')")
    add_avn_event("makigenafternoon", "generic", "Maki", 1, "date_afternoon", "makiblock == False and makidate1 == True and christmas7 == False and not renpy.seen_label('makigenafternoon')")
    add_avn_event("makinoongen2", "generic", "Maki", 2, "date_afternoon", "makiblock == False and christmas7 == True and not renpy.seen_label('makinoongen2')")
    add_avn_event("makiinviteaff", "generic", "Maki", 1, "invite", "makiblock == False and makiinvite2 == True and not renpy.seen_label('makiinviteaff')")
    add_avn_event("makispringporngen", "generic", "Maki", 4, "ch4work3", "makiblock == False and (senseisad == False or saracamp2 == True) and not renpy.seen_label('makispringporngen')")
    add_avn_event("makispringmorninggen", "generic", "Maki", 4, "ch4date_morning", "makiblock == False and (senseisad == False or saracamp2 == True) and not renpy.seen_label('makispringmorninggen')")

    #MAKOTO
    add_avn_event("porn3to4", "generic", "Makoto", 1, "work3", "makotoblock == False and firsttimepornshop == True and not renpy.seen_label('porn3to4')", 15)
    add_avn_event("makotoporngen2", "generic", "Makoto", 2, "work3", "makotoblock == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('makotoporngen2')")
    add_avn_event("makotosummer2porngen", "generic", "Makoto", 3, "work3", "makotoblock == False and chapthreeactive == True and not renpy.seen_label('makotosummer2porngen')")
    add_avn_event("callmakotomorning", "generic", "Makoto", 2, "date_morning", "makotoblock == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('callmakotomorning')")
    add_avn_event("makotosummer2morninggen", "generic", "Makoto", 3, "date_morning", "makotoblock == False and chapthreeactive == True and not renpy.seen_label('makotosummer2morninggen')")
    add_avn_event("callmakotoafternoon", "generic", "Makoto", 2, "date_afternoon", "makotoblock == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('callmakotoafternoon')")
    add_avn_event("makotosummer2poolgen", "generic", "Makoto", 3, "date_afternoon", "makotoblock == False and chapthreeactive == True and not renpy.seen_label('makotosummer2poolgen')")
    add_avn_event("makotohall", "generic", "Makoto", 1, "dorm", "makotoblock == False and makotofirsthall == True and not renpy.seen_label('makotohall')", 10, {4})
    add_avn_event("makotodormgen", "generic", "Makoto", 1, "dorm", "makotoblock == False and makotodorm5 == True and not renpy.seen_label('makotodormgen')", 20, {1,2,3,5,6,7})
    add_avn_event("makotoinviteaff", "generic", "Makoto", 1, "invite", "makotoblock == False and makotoinvite2 == True and not renpy.seen_label('makotoinviteaff')")
    add_avn_event("makotospringporngen", "generic", "Makoto", 4, "ch4work3", "senseisad == False and not renpy.seen_label('makotospringporngen')")
    add_avn_event("makotospringnoongen", "generic", "Makoto", 4, "ch4date_afternoon", "senseisad == False and not renpy.seen_label('makotospringnoongen')")
    add_avn_event("makotodormgen", "generic", "Makoto", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('makotodormgen')")

    #MAYA
    add_avn_event("shrine2to4", "generic", "Maya", 1, "work2", "firsttimeshrine == True and not renpy.seen_label('shrine2to4')", 15)
    add_avn_event("mayanoongen2", "generic", "Maya", 2, "work2", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('mayanoongen2')")
    add_avn_event("mayasummer2shrinegen", "generic", "Maya", 3, "work2", "chapthreeactive == True and not renpy.seen_label('mayasummer2shrinegen')")
    add_avn_event("mayanightgen", "generic", "Maya", 3, "date_night", "mayadate45 == True and not renpy.seen_label('mayanightgen')")
    add_avn_event("mayahall", "generic", "Maya", 1, "dorm", "mayafirsthall == True and not renpy.seen_label('mayahall')", 20, {1})
    add_avn_event("mayadormgen", "generic", "Maya", 1, "dorm", "mayadorm5 == True and not renpy.seen_label('mayadormgen')", 20, {2,3,4,5,6,7})
    add_avn_event("mayaspringshrinegen", "generic", "Maya", 4, "ch4work2", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('mayaspringshrinegen')")
    add_avn_event("mayaspringshrinegen2", "generic", "Maya", 4, "ch4work2", "(senseisad == False or saracamp2 == True) and dormwarssix12 == True and not renpy.seen_label('mayaspringshrinegen2')")

    #MIKU
    add_avn_event("soccer2to4", "generic", "Miku", 1, "work1", "firsttimesoccerfield == True and christmas7 == False and not renpy.seen_label('soccer2to4')", 20)
    add_avn_event("mikusoccergen2", "generic", "Miku", 2, "work1", "mikublock == False and firsttimesoccerfield == True and christmas7 == True and chapthreeactive == False and not renpy.seen_label('mikusoccergen2')")
    add_avn_event("mikusummer2poolgen", "generic", "Miku", 3, "work1", "mikublock == False and chapthreeactive == True and not renpy.seen_label('mikusummer2poolgen')")
    add_avn_event("callmikuafternoon", "generic", "Miku", 2, "date_afternoon", "mikublock == False and mikuspecial50 == True and chapthreeactive  == False and not renpy.seen_label('callmikuafternoon')")
    add_avn_event("mikusummer2nightgen", "generic", "Miku", 3, "date_night", "mikublock == False and chapthreeactive == True and christmas7 == False and not renpy.seen_label('mikusummer2nightgen')")
    add_avn_event("mikuhall", "generic", "Miku", 1, "dorm", "mikufirsthall == True and mikublock == False and not renpy.seen_label('mikuhall')", 20, {2})
    add_avn_event("mikudormgen_avn", "generic", "Miku", 1, "dorm", "mikudorm5 == True and mikublock == False and not renpy.seen_label('mikudormgen_avn')", 20, {1,3,4,5,6,7})
    add_avn_event("mikuinviteaff", "generic", "Miku", 3, "invite", "mikublock == False and mikuinvite2 == True and not renpy.seen_label('mikuinviteaff')")
    add_avn_event("mikuspringpoolgen", "generic", "Miku", 4, "ch4work1", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('mikuspringpoolgen')")
    add_avn_event("mikuspringnightgen", "generic", "Miku", 4, "ch4date_night", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('mikuspringnightgen')")
    add_avn_event("mikudormgen_avn", "generic", "Miku", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('mikudormgen_avn')")
    add_avn_event("mikuinviteaff", "generic", "Miku", 4, "invite", "mikuinvite2 == True and not renpy.seen_label('mikuinviteaff')")

    #MOLLY
    add_avn_event("mollycafegen", "generic", "Molly", 1, "work3", "mollycafe1 == True and christmas7 == False and mollysad == False and not renpy.seen_label('mollycafegen')")
    add_avn_event("mollynightgen2", "generic", "Molly", 2, "work3", "christmas7 == True and chapthreeactive == False and mollysad == False and not renpy.seen_label('mollynightgen2')")
    add_avn_event("mollysummer2cafegen", "generic", "Molly", 3, "work3", "chapthreeactive == True and mollysad == False and not renpy.seen_label('mollysummer2cafegen')")
    add_avn_event("mollydormgen_avn", "generic", "Molly", 1, "dorm2", "mollydorm5 == True and mollysad == False and not renpy.seen_label('mollydormgen_avn')", None, {2,3,4,5,6,7})
    add_avn_event("mollyhall", "generic", "Molly", 1, "dorm2", "mollyfirsthall == True and mollysad == False and not renpy.seen_label('mollyhall')", None, {1})
    add_avn_event("mollyspringcafegen", "generic", "Molly", 4, "ch4work3", "cafeclosed == False and (senseisad == False or mollycamp1 == True) and not renpy.seen_label('mollyspringcafegen')")
    add_avn_event("mollyspringmorninggen", "generic", "Molly", 4, "ch4date_morning", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('mollyspringmorninggen')")
    add_avn_event("mollydormgen_avn", "generic", "Molly", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('mollydormgen_avn')")
    # 047
    add_avn_event("mollyinviteaff", "generic", "Molly", 4, "invite", "mollyinvite2 == True and not renpy.seen_label('mollyinviteaff')")

    #NAO

    #NIKI
    add_avn_event("nikigenmorning", "generic", "Niki", 2, "date_morning", "nikidate1 == True and chapthreeactive == False and not renpy.seen_label('nikigenmorning')")
    add_avn_event("nikisummer2morninggen", "generic", "Niki", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('nikisummer2morninggen')")
    add_avn_event("nikisummer2nightgen", "generic", "Niki", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('nikisummer2nightgen')")
    add_avn_event("nikiinviteaff", "generic", "Niki", 2, "invite", "nikiinvite2 == True and not renpy.seen_label('nikiinviteaff')")
    add_avn_event("nikispringnightgen", "generic", "Niki", 4, "ch4date_night", "nikiblock == False and not renpy.seen_label('nikispringnightgen')")

    #NODOKA
    add_avn_event("nodokalibrarygen", "generic", "Nodoka", 2, "work2", "otohadorm1 == True and chapthreeactive == False and nodokablock == False and not renpy.seen_label('nodokalibrarygen')")
    add_avn_event("nodokasummer2librarygen", "generic", "Nodoka", 3, "work2", "chapthreeactive == True and nodokablock == False and not renpy.seen_label('nodokasummer2librarygen')")
    add_avn_event("callnodokanight", "generic", "Nodoka", 2, "date_night", "nodokalibrary1 == True and nodokablock == False and not renpy.seen_label('callnodokanight')")
    add_avn_event("nodokasummer2nightgen", "generic", "Nodoka", 3, "date_night", "chapthreeactive == True and nodokablock == False and not renpy.seen_label('nodokasummer2nightgen')")
    add_avn_event("nodokahall", "generic", "Nodoka", 2, "dorm2", "nodokafirsthall == True and nodokablock == False and not renpy.seen_label('nodokahall')", None, {5})
    add_avn_event("nodokadormgen_avn", "generic", "Nodoka", 2, "dorm2", "nodokadorm1 == True and nodokablock == False and not renpy.seen_label('nodokadormgen_avn')", None, {1,2,3,4,6,7})
    add_avn_event("nodokaspringlibrarygen", "generic", "Nodoka", 4, "ch4work2", "not renpy.seen_label('nodokaspringlibrarygen')")
    add_avn_event("nodokaspringnightgen", "generic", "Nodoka", 4, "ch4date_night", "not renpy.seen_label('nodokaspringnightgen')")
    add_avn_event("nodokadormgen_avn", "generic", "Nodoka", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('nodokadormgen_avn')")
    # 047
    add_avn_event("nodokainviteaff", "generic", "Nodoka", 4, "invite", "nodokainvite2 == True and not renpy.seen_label('nodokainviteaff')")

    #NORIKO
    add_avn_event("norikodormgen", "generic", "Noriko", 2, "dorm2", "norikodorm5 == True and not renpy.seen_label('norikodormgen')", None, {1,2,4,5,6,7})
    add_avn_event("norikohall", "generic", "Noriko", 3, "dorm2", "norikofirsthall == True and chapthreeactive == False and not renpy.seen_label('norikohall')", None, {3})
    add_avn_event("conveniencegen", "generic", "Noriko", 2, "work3", "convenience1 == True and norikoblock == False and chapthreeactive == False and not renpy.seen_label('conveniencegen')")
    add_avn_event("norikosummer2conveniencegen", "generic", "Noriko", 3, "work3", "norikoblock == False and chapthreeactive == True and not renpy.seen_label('norikosummer2conveniencegen')")
    add_avn_event("norikomorninggen", "generic", "Noriko", 2, "date_morning", "norikoblock == False and norikonumber == True and chapthreeactive == False and not renpy.seen_label('norikomorninggen')")
    add_avn_event("norikosummer2morninggen", "generic", "Noriko", 3, "date_morning", "norikoblock == False and chapthreeactive == True and not renpy.seen_label('norikosummer2morninggen')")
    add_avn_event("norikospringconveniencegen", "generic", "Noriko", 4, "ch4work3", "senseisad == False and not renpy.seen_label('norikospringconveniencegen')")
    add_avn_event("norikospringmorninggen", "generic", "Noriko", 4, "ch4date_morning", "senseisad == False and not renpy.seen_label('norikospringmorninggen')")
    add_avn_event("norikodormgen", "generic", "Noriko", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('norikodormgen')")
    # 057
    add_avn_event("norikoinviteaff", "generic", "Noriko", 4, "invite", "norikoinvite6 == True and not renpy.seen_label('norikoinviteaff')")

    #OSAKO
    add_avn_event("osakodojogen", "generic", "Osako", 2, "work2", "osakodate1 == True and chapthreeactive == False and not renpy.seen_label('osakodojogen')")
    add_avn_event("osakosummer2dojogen", "generic", "Osako", 3, "work2", "chapthreeactive == True and not renpy.seen_label('osakosummer2dojogen')")
    add_avn_event("osakospringdojogen", "generic", "Osako", 4, "ch4work2", "senseisad == False and not renpy.seen_label('osakospringdojogen')")
    add_avn_event("osakospringdivegen", "generic", "Osako", 4, "work3", "(senseisad == False or imanispring2 == True) and not renpy.seen_label('osakospringdivegen')", None, {5})

    #OTOHA
    add_avn_event("otohaparkgen", "generic", "Otoha", 2, "work1", "otohapark1 == True and chapthreeactive == False and not renpy.seen_label('otohaparkgen')")
    add_avn_event("otohasummer2streetsgen", "generic", "Otoha", 3, "work1", "chapthreeactive == True and not renpy.seen_label('otohasummer2streetsgen')")
    add_avn_event("otohahallgen", "generic", "Otoha", 2, "dorm2", "otohafirsthall == True and not renpy.seen_label('otohahallgen')", None , {1})
    add_avn_event("otohadormgen_avn", "generic", "Otoha", 2, "dorm2", "nodokadorm1 == True and not renpy.seen_label('otohadormgen_avn')", None , {2,3,4,5,6,7})
    add_avn_event("otohaspringparkgen", "generic", "Otoha", 4, "ch4work1", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('otohaspringparkgen')")
    add_avn_event("otohadormgen_avn", "generic", "Otoha", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('otohadormgen_avn')")

    #RIKA
    add_avn_event("rikadivegen", "generic", "Rika", 3, "work3", "rikadive1 == True and not renpy.seen_label('rikadivegen')", None, {5})
    add_avn_event("rikaspringdivegen", "generic", "Rika", 4, "work3", "(senseisad == False or imanispring2 == True) and not renpy.seen_label('rikaspringdivegen')", None, {5})

    #RIN
    add_avn_event("cafe6to9", "generic", "Rin", 1, "work1", "rinsad == False and firsttimecafe == True and christmas7 == False and not renpy.seen_label('cafe6to9')", 10)
    add_avn_event("rincafegone", "generic", "Rin", 1, "work1", "cafe15 == True and day63 == False and rincafegone_avn == False and cafe20 == False")    # sad Rin 
    add_avn_event("rinmorninggen2", "generic", "Rin", 2, "work1", "rinsad == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('rinmorninggen2')")
    add_avn_event("rinsummer2cafegen", "generic", "Rin", 3, "work1", "rinsad == False and chapthreeactive == True and not renpy.seen_label('rinsummer2cafegen')")
    add_avn_event("callrinafternoon", "generic", "Rin", 2, "date_afternoon", "rinsad == False and dormwar17 == True and chapthreeactive == False and not renpy.seen_label('callrinafternoon')")
    add_avn_event("rinsummer2nightgen", "generic", "Rin", 3, "date_night", "rinsad == False and chapthreeactive == True and not renpy.seen_label('rinsummer2nightgen')")
    add_avn_event("rinhall", "generic", "Rin", 1, "dorm", "rinsad == False and rinfirsthall == True and not renpy.seen_label('rinhall')", 15, {3})
    add_avn_event("rindorm6to9_avn", "generic", "Rin", 1, "dorm", "rinsad == False and rinfirstvisit == True and not renpy.seen_label('rindorm6to9_avn')", 20, {1,2,4,5,6,7})
    add_avn_event("rinspringcafegen", "generic", "Rin", 4, "ch4work1", "not renpy.seen_label('rinspringcafegen')")
    add_avn_event("rinspringnightgen", "generic", "Rin", 4, "ch4date_night", "not renpy.seen_label('rinspringnightgen')")
    add_avn_event("rindorm6to9_avn", "generic", "Rin", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('rindorm6to9_avn')")

    #SANA
    add_avn_event("sanahall", "generic", "Sana", 1, "dorm", "sanafirsthall == True and not renpy.seen_label('sanahall')", 10, {5})
    add_avn_event("sanadormgen_avn", "generic", "Sana", 1, "dorm", "sanadorm5 == True and not renpy.seen_label('sanadormgen_avn')", 20, {1,2,3,4,6,7})
    add_avn_event("bar2to4", "generic", "Sana", 1, "work3", "firsttimebar == True and christmas7 == False and not renpy.seen_label('bar2to4')", 10)
    add_avn_event("bargen2", "generic", "Sana", 2, "work3", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('bargen2')")
    add_avn_event("sanasummer2bargen", "generic", "Sana", 3, "work3", "chapthreeactive == True and not renpy.seen_label('sanasummer2bargen')")
    add_avn_event("sanaspringbargen", "generic", "Sana", 4, "ch4work3", "not renpy.seen_label('sanaspringbargen')")
    add_avn_event("sanadormgen_avn", "generic", "Sana", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('sanadormgen_avn')")
    # 047
    add_avn_event("sanainviteaff", "generic", "Sana", 4, "invite", "sanainvite2 == True and not renpy.seen_label('sanainviteaff')")

    #SARA
    add_avn_event("sarabargen", "generic", "Sara", 1, "work3", "saradate1 == True and christmas7 == False and not renpy.seen_label('sarabargen')")
    add_avn_event("sarabargen2", "generic", "Sara", 2, "work3", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('sarabargen2')")
    add_avn_event("sarasummer2bargen", "generic", "Sara", 3, "work3", "chapthreeactive == True and not renpy.seen_label('sarasummer2bargen')")
    add_avn_event("saragenafternoon", "generic", "Sara", 1, "date_afternoon", "saradate1 == True and christmas7 == False and not renpy.seen_label('saragenafternoon')")
    add_avn_event("saranoongen2", "generic", "Sara", 2, "date_afternoon", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('saranoongen2')")
    add_avn_event("sarasummer2noongen", "generic", "Sara", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('sarasummer2noongen')")
    add_avn_event("sarainviteaff", "generic", "Sara", 1, "invite", "sarainvite2 == True and not renpy.seen_label('sarainviteaff')")
    add_avn_event("saraspringbargen", "generic", "Sara", 4, "ch4work3", "((senseisad == False and sarablock == False) or (saracamp2 == True and sarablock == False)) and not renpy.seen_label('saraspringbargen')")
    add_avn_event("saraspringnoongen", "generic", "Sara", 4, "ch4date_afternoon", "((senseisad == False and sarablock == False) or (saracamp2 == True and sarablock == False)) and not renpy.seen_label('saraspringnoongen')")

    #TOUKA
    add_avn_event("toukasummer2archerygen", "generic", "Touka", 3, "work1", "chapthreeactive == True and not renpy.seen_label('toukasummer2archerygen')")
    add_avn_event("toukastreetsgen", "generic", "Touka", 2, "work1", "toukastreets1 == True and chapthreeactive == False and not renpy.seen_label('toukastreetsgen')")
    add_avn_event("toukahallgen", "generic", "Touka", 2, "dorm2", "toukafirsthall == True and not renpy.seen_label('toukahallgen')", None, {2})
    add_avn_event("toukadormgen_avn", "generic", "Touka", 2, "dorm2", "toukadorm1 == True and not renpy.seen_label('toukadormgen_avn')", None, {1,3,4,5,6,7})
    add_avn_event("toukaspringarcherygen", "generic", "Touka", 4, "ch4work1", "toukablock == False and not renpy.seen_label('toukaspringarcherygen')")
    add_avn_event("toukadormgen_avn", "generic", "Touka", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and toukablock == False and not renpy.seen_label('toukadormgen_avn')")

    #TSUBASA
    add_avn_event("tsubasasummer2noongen", "generic", "Tsubasa", 3, "date_afternoon", "chapthreeactive == True and not renpy.seen_label('tsubasasummer2noongen')")
    add_avn_event("tsubasaspringnightgen", "generic", "Tsubasa", 4, "ch4date_night", "not renpy.seen_label('tsubasaspringnightgen')")

    #TSUKASA
    # calltsukasamorning
    # calltsukasaafternoon
    # calltsukasanight

    #TSUNEYO
    add_avn_event("ramengen", "generic", "Tsuneyo", 1, "work3", "ramen1 == True and christmas7 == False and not renpy.seen_label('ramengen')")
    add_avn_event("tsuneyohall", "generic", "Tsuneyo", 1, "dorm2", "tsuneyofirsthall == True and not renpy.seen_label('tsuneyohall')", None, {3})
    add_avn_event("tsuneyodormgen", "generic", "Tsuneyo", 1, "dorm2", "tsuneyodorm5 == True and not renpy.seen_label('tsuneyodormgen')", None, {1,2,4,5,6,7})
    add_avn_event("tsuneyonightgen2", "generic", "Tsuneyo", 2, "work3", "christmas7 == True and chapthreeactive == False and not renpy.seen_label('tsuneyonightgen2')")
    add_avn_event("tsuneyosummer2ramengen", "generic", "Tsuneyo", 3, "work3", "chapthreeactive == True and not renpy.seen_label('tsuneyosummer2ramengen')")
    add_avn_event("tsuneyosummer2archerygen", "generic", "Tsuneyo", 3, "work1", "chapthreeactive == True and not renpy.seen_label('tsuneyosummer2archerygen')")
    add_avn_event("tsuneyospringarcherygen", "generic", "Tsuneyo", 4, "ch4work1", "senseisad == False and not renpy.seen_label('tsuneyospringarcherygen')")
    add_avn_event("tsuneyospringramengen", "generic", "Tsuneyo", 4, "ch4work3", "senseisad == False and not renpy.seen_label('tsuneyospringramengen')")
    add_avn_event("tsuneyodormgen", "generic", "Tsuneyo", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('tsuneyodormgen')")

    #UTA
    add_avn_event("utaarchery", "generic", "Uta", 3, "work1", "chapthreeactive == True and not renpy.seen_label('utaarchery')")
    add_avn_event("utamaidgen", "generic", "Uta", 2, "work3", "utamaid1 == True and chapthreeactive == False and not renpy.seen_label('utamaidgen')")
    add_avn_event("utasummer2maidgen", "generic", "Uta", 3, "work3", "chapthreeactive == True and not renpy.seen_label('utasummer2maidgen')")
    add_avn_event("callutamorning", "generic", "Uta", 2, "date_morning", "utanumber == True and chapthreeactive == False and not renpy.seen_label('callutamorning')")
    add_avn_event("callutaafternoon", "generic", "Uta", 2, "date_afternoon", "utanumber == True and chapthreeactive == False and not renpy.seen_label('callutaafternoon')")
    add_avn_event("utadormgen", "generic", "Uta", 2, "dorm2", "utadorm5 == True and not renpy.seen_label('utadormgen')", None, {1,2,3,4,6,7})
    add_avn_event("utahallgen", "generic", "Uta", 2, "dorm2", "utafirsthall == True and not renpy.seen_label('utahallgen')", None, {5})
    add_avn_event("utaspringarcherygen", "generic", "Uta", 4, "ch4work1", "senseisad == False and utablock == False and not renpy.seen_label('utaspringarcherygen')")
    add_avn_event("utaspringmaidgen", "generic", "Uta", 4, "ch4work3", "senseisad == False and amiblock == False and utablock == False and not renpy.seen_label('utaspringmaidgen')")
    add_avn_event("utaspringnightgen", "generic", "Uta", 4, "ch4date_night", "senseisad == False and utablock == False and not renpy.seen_label('utaspringnightgen')")
    add_avn_event("utadormgen", "generic", "Uta", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and utablock == False and not renpy.seen_label('utadormgen')")

    #WAKANA
    add_avn_event("wakanadive", "generic", "Wakana", 3, "work3", "wakanaspecial15 == True and imanidate1 == True and not renpy.seen_label('wakanadive')", None, {5})
    add_avn_event("wakanasummer2morninggen", "generic", "Wakana", 3, "date_morning", "chapthreeactive == True and not renpy.seen_label('wakanasummer2morninggen')")
    add_avn_event("wakananightgen", "generic", "Wakana", 2, "date_night", "wakanadate1 == True and not renpy.seen_label('wakananightgen')")
    add_avn_event("wakanasummer2nightgen", "generic", "Wakana", 3, "date_night", "chapthreeactive == True and not renpy.seen_label('wakanasummer2nightgen')")
    add_avn_event("wakanaspringdivegen", "generic", "Wakana", 4, "work3", "(senseisad == False or imanispring2 == True) and not renpy.seen_label('wakanaspringdivegen')", None, {5})
    add_avn_event("wakanaspringmorninggen", "generic", "Wakana", 4, "ch4date_morning", "senseisad == False and not renpy.seen_label('wakanaspringmorninggen')")
    add_avn_event("wakanaspringnoongen", "generic", "Wakana", 4, "ch4date_afternoon", "senseisad == False and not renpy.seen_label('wakanaspringnoongen')")

    #YASU
    add_avn_event("yasuhallgen", "generic", "Yasu", 2, "dorm2", "yasufirsthall == True and not renpy.seen_label('yasuhallgen')", None, {4})
    add_avn_event("yasudormgen_avn", "generic", "Yasu", 2, "dorm2", "yasudorm10 == True and not renpy.seen_label('yasudormgen_avn')", None, {1,2,3,5,6,7})
    add_avn_event("churchgen", "generic", "Yasu", 2, "work3", "church1 == True and chapthreeactive == False and not renpy.seen_label('churchgen')")
    add_avn_event("yasusummer2chapelgen", "generic", "Yasu", 3, "work3", "chapthreeactive == True and not renpy.seen_label('yasusummer2chapelgen')")
    add_avn_event("yasuspringchurchgen", "generic", "Yasu", 4, "ch4work3", "not renpy.seen_label('yasuspringchurchgen')")
    add_avn_event("yasudormgen_avn", "generic", "Yasu", 4, "dorm2", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('yasudormgen_avn')")

    #YUKI
    add_avn_event("yukisummer2bargen", "generic", "Yuki", 3, "work3", "chapthreeactive == True and not renpy.seen_label('yukisummer2bargen')")
    add_avn_event("yukigennight", "generic", "Yuki", 2, "date_night", "yukidate1 == True and chapthreeactive == False and not renpy.seen_label('yukigennight')")
    add_avn_event("yukispringbargen", "generic", "Yuki", 4, "ch4work3", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('yukispringbargen')")
    add_avn_event("yukispringnoongen", "generic", "Yuki", 4, "ch4date_afternoon", "(senseisad == False or saracamp2 == True) and not renpy.seen_label('yukispringnoongen')")

    #YUMI
    add_avn_event("streets2to4", "generic", "Yumi", 1, "work2", "firsttimestreets == True and chapthreeactive == False and not renpy.seen_label('streets2to4')", 10)
    add_avn_event("yuminoongen2", "generic", "Yumi", 2, "work2", "yumiblock == False and christmas7 == True and chapthreeactive == False and not renpy.seen_label('yuminoongen2')")
    add_avn_event("yumisummer2streetsgen", "generic", "Yumi", 3, "work2", "yumiblock == False and chapthreeactive == True and not renpy.seen_label('yumisummer2streetsgen')")
    add_avn_event("yumigennight", "generic", "Yumi", 2, "date_night", "yumiblock == False and yumicallnight35 == True and chapthreeactive == False and not renpy.seen_label('yumigennight')")
    add_avn_event("yumisummer2nightgen", "generic", "Yumi", 3, "date_night", "yumiblock == False and chapthreeactive == True and not renpy.seen_label('yumisummer2nightgen')")
    add_avn_event("yumihall", "generic", "Yumi", 1, "dorm", "yumiblock == False and yumifirsthall == True and not renpy.seen_label('yumihall')", 10, {1})
    add_avn_event("yumidormgen", "generic", "Yumi", 1, "dorm", "yumiblock == False and yumidorm10 == True and not renpy.seen_label('yumidormgen')", 20, {2,3,4,5,6,7})
    add_avn_event("yumispringstreetsgen", "generic", "Yumi", 4, "ch4work2", "senseisad == False and not renpy.seen_label('yumispringstreetsgen')")
    add_avn_event("yumispringnightgen", "generic", "Yumi", 4, "ch4date_night", "senseisad == False and not renpy.seen_label('yumispringnightgen')")
    add_avn_event("yumidormgen", "generic", "Yumi", 4, "dorm", "(senseisad == False or mollyspring2 == True) and escapeshampoo == False and not renpy.seen_label('yumidormgen')")
