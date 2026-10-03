################################################################################
## Happy Events
################################################################################

screen secrettrackerm():

    tag menu

    use game_menu(_("HAPPY SCENES"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        xpos .25
        ypos 40
        area (0,0,1450,930)

        vbox:
            ypos 120
            vbox:
                text "{color=141414}HAPPY SCENES{/color}" style "aff"

        viewport:
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            ypos 135
            #child_size (1432,length x 29)

            vbox:
                style_prefix "tracker"
                if roomwithtrack == True:
                    textbutton _("The Room With Clocks {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("roomwithclocks", locked=False)
                else:
                    text _("???")
                if letterttrack == True:
                    textbutton _("The Letter 'T' {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("lettert", locked=False)
                else:
                    text _("???")
                if swimmingtrack == True:
                    textbutton _("Swim Trip {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("swimming", locked=False)
                elif amidorm10 == True and amifingered == False:
                    text _("{color=EF1A1A}{s}You Don't Love Me, Do You?{/s}{/color}")
                else:
                    text _("???")
                if howifeeltrack == True:
                    textbutton _("How I Feel {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("howifeel", locked=False)
                else:
                    text _("???")
                if connecttrack == True:
                    textbutton _("Everything is Connected {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("everythingisconnected", locked=False)
                elif day103 == True and connecttrack == False:
                    text _("{color=EF1A1A}{s}Nothing is Beautiful{/s}{/color}")
                else:
                    text _("???")
                if specialclassroomtrack == True:
                    textbutton _("Turn Off The Lights {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("specialclassroom", locked=False)
                elif amisroom15 == True and amifingered == False:
                    text _("{color=EF1A1A}{s}List the Things You Love{/s}{/color}")
                else:
                    text _("???")
                if ticktocktrack == True:
                    textbutton _("Tick Tock Tick Tock Tick Tock {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("ticktock", locked=False)
                else:
                    text _("???")
                if trinity1track == True:
                    textbutton _("Trinity Pt. I: Stations of the Cross {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("trinity1", locked=False)
                else:
                    text _("???")
                if trinity2track == True:
                    textbutton _("Trinity Pt. II: Hell is Empty {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("trinity2", locked=False)
                else:
                    text _("???")
                if trinity3track == True:
                    textbutton _("Trinity Pt. III: Non Est Deus {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("trinity3", locked=False)
                else:
                    text _("???")
                if babyfinches == True:
                    textbutton _("Baby Finches {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("babyfinches", locked=False)
                elif babyfinches == False and hoorayanotherreset == True:
                    text _("{color=EF1A1A}{s}A Time When Things Were Horrible{/s}{/color}")
                else:
                    text _("???")
                if lesson1 == True:
                    textbutton _("Something Everyone Knows and Ignores {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("kindergartenclass", locked=False)
                elif lesson1 == False and thirdreset1 == True:
                    text _("{color=EF1A1A}{s}LET ME OUT{/s}{/color}")
                else:
                    text _("???")
                if goodboy == True:
                    textbutton _("Good Boy {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("goodboy", locked=False)
                elif sarabar25 == True and anewkey == False and goodboy == False:
                    text _("{color=EF1A1A}{s}Bad Boy{/s}{/color}")
                else:
                    text _("???")
                if lamblegs == True:
                    textbutton _("Lamb Legs {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("specialbonusamiscene", locked=False)
                elif returntosummer2 == True and anewkey == False:
                    text _("{color=EF1A1A}{s}Ground Into Nothing{/s}{/color}")
                else:
                    text _("???")
                if buckettrack == True:
                    textbutton _("Second Sun {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("bucketscene", locked=False)
                else:
                    text _("???")
                if mothersmilk == True:
                    textbutton _("Mother's Milk {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("mothersmilk", locked=False)
                elif mothersmiss == True:
                    text _("{color=EF1A1A}{s}Overlooked{/s}{/color}")
                else:
                    text _("???")
                if amyevent == True:
                    textbutton _("Amy {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("amyevent", locked=False)
                else:
                    text _("???")
                if rainking == True:
                    textbutton _("Rain King {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("rainking", locked=False)
                elif rainkingmiss == True:
                    text _("{color=EF1A1A}{s}Drought God{/s}{/color}")
                else:
                    text _("???")
                if armsbenttrack == True:
                    textbutton _("Arms Bent Back {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("armsbentback", locked=False)
                elif rainkingmiss == True:
                    text _("{color=EF1A1A}{s}Lost in the Red Room{/s}{/color}")
                else:
                    text _("???")
                if kyotoevent == True:
                    textbutton _("Kyoto {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("kyotoevent", locked=False)
                elif rainkingmiss == True:
                    text _("{color=EF1A1A}{s}No One Leaves This City{/s}{/color}")
                else:
                    text _("???")
                if persistent.alexisevent == True:
                    textbutton _("Alexisthymia {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("alexisevent", locked=False)
                else:
                    text _("???")
                if swimtrip2 == True:
                    textbutton _("Sally Sells Seashells {b}✓{/b}"):
                        text_style "modmybutton"
                        action Replay("swimtrip2", locked=False)
                else:
                    text _("???")

################################################################################

            vbox:
                xpos .4
                style_prefix "tracker"

                if show_hints == True and show_happy_hints and not _in_replay:

                    #The Room With Clocks
                    if roomwithtrack == False and roomwithclocks:
                        text ("Visit {color=[amicolor]}Ami{/color} and {color=[mayacolor]}Maya{/color}'s dorm room.")
                    else:
                        text ("")

                    #The Letter "T"
                    if letterttrack == False and lettert:
                        text ("Visit the dorms, then choose to go home.")
                    else:
                        text ("")

                    #Swim Trip
                    if swimmingtrack == False and swimming:
                        text ("Choose =D in weekend travel menu.")
                    else:
                        text ("")

                    #How I Feel
                    if howifeeltrack == False and howifeel:
                        text ("[Maya.visit_work]")
                    else:
                        text ("")

                    #Everything is Connected
                    if connecttrack == False and soccer10:
                        text ("Visit the soccer field while the world is broken.")
                    else:
                        text ("")

                    #Turn Off The Lights
                    if specialclassroomtrack == False and specialclassroom:
                        text ("Invite {color=[mayacolor]}Maya{/color} over on the weekend.")
                    else:
                        text ("")

                    #Tick Tock Tick Tock Tick Tock
                    if ticktocktrack == False and ticktock:
                        text ("Visit {color=[amicolor]}Ami{/color} and {color=[mayacolor]}Maya{/color}'s dorm room.")
                    else:
                        text ("")

                    #Trinity Pt. I
                    if trinity1track == False and trinity:
                        text ("Visit the dorms, then choose to go home.")
                    else:
                        text ("")

                    #Trinity Pt. II
                    if trinity2track == False and trinity2:
                        text ("Visit the ramen shop (Sunday).")
                    else:
                        text ("")

                    #Trinity Pt. III
                    if trinity3track == False and trinity3:
                        text ("Invite XXXX over (Weekend night).")
                    else:
                        text ("")

                    #Baby Finches
                    if babyfinches == False and day218 and hoorayanotherreset == False:
                        text ("Use :)'s name as your username during There is Nothing.")
                    else:
                        text ("")

                    #Something Everyone Knows and Ignores (lesson1)
                    if lesson1 == False and day340 and thirdreset1 == False:
                        text ("Choose '6b 61 6f 72 69'")
                    else:
                        text ("")

                    #Good Boy
                    if sarabar25 and anewkey == True and goodboy == False:
                        text ("Choose to wait until morning in the weekend afternoon call menu.")
                    else:
                        text ("")

                    # Lamb Legs
                    if returntosummer1 and returntosummer2 == False:
                        text ("Win the lottery.")
                    else:
                        text ("")

                    # Second Son
                    if chinamidate30 and buckettrack == False:
                        text ("Visit the church (Sunday morning).")
                    else:
                        text ("")

                    # Mother's Milk
                    if slumberreset3 and mothersmilk == False:
                        text ("Answer the bonus trivia question correctly.")
                    else:
                        text ("")

                    # Amy
                    if naospecial3 and amyevent == False:
                        text ("Go to the mall on Sunday.")
                    else:
                        text ("")

                    # Rain King
                    if halloweenfour16 and rainking == False:
                        text ("Enter the correct password in Ami's computer.")
                    else:
                        text ("")

                    # Arms Bent Back
                    if beachfive16 and armsbenttrack == False:
                        text ("Go the first floor from the second floor.")
                    else:
                        text ("")

                    # Kyoto
                    if halloweenkaori2 and kyotoevent == False:
                        text ("Kill Fred.")
                    else:
                        text ("")

                    # Alexis
                    if naospecial3 and persistent.alexisevent == False:
                        text ("Play through 'Amy' after Chapter 4.")
                    else:
                        text ("")

                    # Sally Sells Seashells
                    if beachsix6 and swimtrip2 == False:
                        text ("Research on the PC after giving Makoto something.")
                    else:
                        text ("")

        vbox:
            ypos 20

            if dark_mode:
                textbutton _("Back") action ShowMenu('progressmod_dark')
            else:
                textbutton _("Back") action ShowMenu('progressmod')