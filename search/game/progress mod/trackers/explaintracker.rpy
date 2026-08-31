screen explaintracker():

    tag menu

    key "n" action Return()

    $ activate_girls()
    $ ProgressMod.update_all()
    python:
        if ProgressMod.longest_name > 34:
            hint_col = 0.53 + ((ProgressMod.longest_name - 34) * .007)
        else:
            hint_col = 0.53

    use game_menu(_("Explanations " + str(current_chapter)), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        xpos .25
        ypos .14
        style_prefix "hint"

        $ main_chapter = "maintrackerch" + str(current_chapter) + "m"
        for current_event in MainEvent.event_list:
            if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                if dark_mode:
                    textbutton _("Main event") action ShowMenu(main_chapter) style "event_button" text_style "hint_text"
                else:
                    textbutton _(MainEvent.colored_name) action ShowMenu(main_chapter) style "event_button" text_style "hint_text"
        for current_event in HappyEvent.event_list:
            if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                textbutton _(HappyEvent.colored_name) action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
        for current_girl in ProgressMod.all_girls:
            if current_girl not in [MainEvent, HappyEvent]:
                if current_girl.active:
                    for current_event in current_girl.event_list:
                        if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                            textbutton _(current_girl.colored_name) action [ShowMenu("amitrackerm2"), SetVariable("showgirl", current_girl.name)] style "event_button" text_style "amihint"
                            if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                text ("")
                        elif current_chapter == 1 and current_event.var_name in ProgressMod.explain_list.keys() and current_event.var_name in ["chikalust10","futabalust10"]:
                            textbutton _(current_girl.colored_name) action [ShowMenu("amitrackerm2"), SetVariable("showgirl", current_girl.name)] style "event_button" text_style "amihint"
                            if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                text ("")

    vbox:
        xpos .33
        ypos .14
        style_prefix "hint"

        for current_event in MainEvent.event_list:
            if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                text (current_event.name)
        for current_event in HappyEvent.event_list:
            if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                text (current_event.name)
        for current_girl in ProgressMod.all_girls:
            if current_girl not in [MainEvent, HappyEvent]:
                if current_girl.active:
                    for current_event in current_girl.event_list:
                        if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                            if "lust" in current_event.var_name or current_event.var_name in ["day98", "day68", "day86"]:
                                text _("{color=FF85FD}" + current_event.name + "{/color}")
                                if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                    text ("")
                            elif "invite" in current_event.var_name:
                                text _("{color=778EFF}" + current_event.name + "{/color}")
                            else:
                                text (current_event.name)
                        elif current_chapter == 1 and current_event.var_name in ProgressMod.explain_list.keys() and current_event.var_name in ["chikalust10","futabalust10"]:
                            if "lust" in current_event.var_name or current_event.var_name in ["day98", "day68", "day86"]:
                                text _("{color=FF85FD}" + current_event.name + "{/color}")
                            if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                text ("")

    vbox:
        xpos hint_col
        ypos .14
        style_prefix "hint"
        if show_hints == True:
            for current_event in MainEvent.event_list:
                if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():                
                    
                    python:

                        import string

                        second_explain_text = ""
                        if current_event.attention_type == 1:
                            current_event.explain_text = "Rejecting her will lead to missing events."
                        elif current_event.attention_type == 2:
                            previous_event = eval("ev_" + current_event.previous_event)
                            if previous_event.girl == MainEvent:
                                previous_event = previous_event.var_name.rstrip(string.digits) + "1"
                                previous_event = eval("ev_" + previous_event)
                                current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " " + previous_event.name + " to complete the lust requirement."
                            else:
                                current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " event " + previous_event.name + " to complete the lust requirement."
                            if current_event.second_attention == 9:
                                current_event.second_explain_text = "Choose " + Miku.colored_name + " as the winner of the costume contest."
                            elif current_event.second_attention == 10:
                                current_event.second_explain_text = "You will not be able to increase her lust after the " + MainEvent.colored_name + " There is Nothing."
                            elif current_event.second_attention == 15:
                                current_event.second_explain_text = "You will not be able to increase " + Makoto.colored_name + "'s lust after " + Nodoka.colored_name + "'s event Beyond the Reach of God."
                        elif current_event.attention_type == 3:
                            current_event.explain_text = "Telling her the truth will cause you to miss a " + Karin.colored_name + " event."
                        elif current_event.attention_type == 4:
                            current_event.explain_text = "Starting this event before you have completed the beach vacation will impact " + Rin.colored_name + "'s events."
                        elif current_event.attention_type == 5:
                            current_event.explain_text = "Starting this event before you have completed the " + Yumi.colored_name + " event Abyss will impact " + Yumi.colored_name + "'s events."
                        elif current_event.attention_type == 6:
                            current_event.explain_text = "Not asking for a blowjob will cause you to miss a later " + Maki.colored_name + " event."
                        elif current_event.attention_type == 7:
                            current_event.explain_text = "Leaving " + Sana.colored_name + " will cause you to miss an event."
                        elif current_event.attention_type == 8:
                            current_event.explain_text = "Choosing " + Ayane.colored_name + " is a requirement for future events."
                        elif current_event.attention_type == 11:
                            current_event.explain_text = "Choosing " + Tsukasa.colored_name + " is a requirement for future events."
                        elif current_event.attention_type == 12:
                            current_event.explain_text = "Not sending the photo will lead to missing significant content but full consequences are still unknown."
                        elif current_event.attention_type == 13:
                            current_event.explain_text = "Choose to go in to avoid missing future " + Tsukasa.colored_name + " events."
                        elif current_event.attention_type == 14:
                            current_event.explain_text = "Need to view the picture in Sana's profile to get her number."
                        elif current_event.attention_type == 16:
                            current_event.explain_text = "Also need to read the text from Karin."
                        elif current_event.attention_type == 17:
                            current_event.explain_text = 'Choosing to "Kill Kirin" will cause you to miss an event.'

                    text (current_event.explain_text)

            for current_event in HappyEvent.event_list:
                if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():               
                    
                    python:

                        import string

                        second_explain_text = ""
                        if current_event.attention_type == 1:
                            current_event.explain_text = "Rejecting her will lead to missing events."
                        elif current_event.attention_type == 2:
                            previous_event = eval("ev_" + current_event.previous_event)
                            if previous_event.girl == MainEvent:
                                previous_event = previous_event.var_name.rstrip(string.digits) + "1"
                                previous_event = eval("ev_" + previous_event)
                                current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " " + previous_event.name + " to complete the lust requirement."
                            else:
                                current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " event " + previous_event.name + " to complete the lust requirement."
                            if current_event.second_attention == 9:
                                current_event.second_explain_text = "Choose " + Miku.colored_name + " as the winner of the costume contest."
                            elif current_event.second_attention == 10:
                                current_event.second_explain_text = "You will not be able to increase her lust after the " + MainEvent.colored_name + " There is Nothing."
                            elif current_event.second_attention == 15:
                                current_event.second_explain_text = "You will not be able to increase " + Makoto.colored_name + "'s lust after " + Nodoka.colored_name + "'s event Beyond the Reach of God."
                        elif current_event.attention_type == 3:
                            current_event.explain_text = "Telling her the truth will cause you to miss a " + Karin.colored_name + " event."
                        elif current_event.attention_type == 4:
                            current_event.explain_text = "Starting this event before you have completed the beach vacation will impact " + Rin.colored_name + "'s events."
                        elif current_event.attention_type == 5:
                            current_event.explain_text = "Starting this event before you have completed the " + Yumi.colored_name + " event Abyss will impact " + Yumi.colored_name + "'s events."
                        elif current_event.attention_type == 6:
                            current_event.explain_text = "Not asking for a blowjob will cause you to miss a later " + Maki.colored_name + " event."
                        elif current_event.attention_type == 7:
                            current_event.explain_text = "Leaving " + Sana.colored_name + " will cause you to miss an event."
                        elif current_event.attention_type == 8:
                            current_event.explain_text = "Choosing " + Ayane.colored_name + " is a requirement for future events."
                        elif current_event.attention_type == 11:
                            current_event.explain_text = "Choosing " + Tsukasa.colored_name + " is a requirement for future events."
                        elif current_event.attention_type == 12:
                            current_event.explain_text = "Not sending the photo will lead to missing significant content but full consequences are still unknown."
                        elif current_event.attention_type == 13:
                            current_event.explain_text = "Choose to go in to avoid missing future " + Tsukasa.colored_name + " events."
                        elif current_event.attention_type == 14:
                            current_event.explain_text = "Need to view the picture in Sana's profile to get her number."
                        elif current_event.attention_type == 16:
                            current_event.explain_text = "Also need to read the text from Karin."
                        elif current_event.attention_type == 17:
                            current_event.explain_text = 'Choosing to "Kill Kirin" will cause you to miss an event.'

                    text (current_event.explain_text)
            for current_girl in ProgressMod.all_girls:
                if current_girl not in [MainEvent, HappyEvent]:
                    if current_girl.active:
                        for current_event in current_girl.event_list:
                            if current_event.chapter == current_chapter and current_event.var_name in ProgressMod.explain_list.keys():
                                
                                python:

                                    import string

                                    second_explain_text = ""
                                    if current_event.attention_type == 1:
                                        current_event.explain_text = "Rejecting her will lead to missing events."
                                    elif current_event.attention_type == 2:
                                        previous_event = eval("ev_" + current_event.previous_event)
                                        if previous_event.girl == MainEvent:
                                            previous_event = previous_event.var_name.rstrip(string.digits) + "1"
                                            previous_event = eval("ev_" + previous_event)
                                            current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " " + previous_event.name + " to complete the lust requirement."
                                        else:
                                            current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " event " + previous_event.name + " to complete the lust requirement."
                                        if current_event.second_attention == 9:
                                            current_event.second_explain_text = "Choose " + Miku.colored_name + " as the winner of the costume contest."
                                        elif current_event.second_attention == 10:
                                            current_event.second_explain_text = "You will not be able to increase her lust after the " + MainEvent.colored_name + " There is Nothing."
                                        elif current_event.second_attention == 15:
                                            current_event.second_explain_text = "You will not be able to increase " + Makoto.colored_name + "'s lust after " + Nodoka.colored_name + "'s event Beyond the Reach of God."
                                    elif current_event.attention_type == 3:
                                        current_event.explain_text = "Telling her the truth will cause you to miss a " + Karin.colored_name + " event."
                                    elif current_event.attention_type == 4:
                                        current_event.explain_text = "Starting this event before you have completed the beach vacation will impact " + Rin.colored_name + "'s events."
                                    elif current_event.attention_type == 5:
                                        current_event.explain_text = "Starting this event before you have completed the " + Yumi.colored_name + " event Abyss will impact " + Yumi.colored_name + "'s events."
                                    elif current_event.attention_type == 6:
                                        current_event.explain_text = "Not asking for a blowjob will cause you to miss a later " + Maki.colored_name + " event."
                                    elif current_event.attention_type == 7:
                                        current_event.explain_text = "Leaving " + Sana.colored_name + " will cause you to miss an event."
                                    elif current_event.attention_type == 8:
                                        current_event.explain_text = "Choosing " + Ayane.colored_name + " is a requirement for future events."
                                    elif current_event.attention_type == 11:
                                        current_event.explain_text = "Choosing " + Tsukasa.colored_name + " is a requirement for future events."
                                    elif current_event.attention_type == 12:
                                        current_event.explain_text = "Not sending the photo will lead to missing significant content but full consequences are still unknown."
                                    elif current_event.attention_type == 13:
                                        current_event.explain_text = "Choose to go in to avoid missing future " + Tsukasa.colored_name + " events."
                                    elif current_event.attention_type == 14:
                                        current_event.explain_text = "Need to view the picture in Sana's profile to get her number."
                                    elif current_event.attention_type == 16:
                                        current_event.explain_text = "Also need to read the text from Karin."
                                    elif current_event.attention_type == 17:
                                        current_event.explain_text = 'Choosing to "Kill Kirin" will cause you to miss an event.'

                                text (current_event.explain_text)
                                if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                    text (current_event.second_explain_text)
                            elif current_chapter == 1 and current_event.var_name in ProgressMod.explain_list.keys() and current_event.var_name in ["chikalust10","futabalust10"]:

                                python:

                                    import string

                                    second_explain_text = ""
                                    if current_event.attention_type == 1:
                                        current_event.explain_text = "Rejecting her will lead to missing events."
                                    elif current_event.attention_type == 2:
                                        previous_event = eval("ev_" + current_event.previous_event)
                                        if previous_event.girl == MainEvent:
                                            previous_event = previous_event.var_name.rstrip(string.digits) + "1"
                                            previous_event = eval("ev_" + previous_event)
                                            current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " " + previous_event.name + " to complete the lust requirement."
                                        else:
                                            current_event.explain_text = "You have until the " + previous_event.girl.colored_name + " event " + previous_event.name + " to complete the lust requirement."
                                        if current_event.second_attention == 9:
                                            current_event.second_explain_text = "Choose " + Miku.colored_name + " as the winner of the costume contest."
                                        elif current_event.second_attention == 10:
                                            current_event.second_explain_text = "You will not be able to increase her lust after the " + MainEvent.colored_name + " There is Nothing."
                                        elif current_event.second_attention == 15:
                                            current_event.second_explain_text = "You will not be able to increase " + Makoto.colored_name + "'s lust after " + Nodoka.colored_name + "'s event Beyond the Reach of God."
                                    elif current_event.attention_type == 3:
                                        current_event.explain_text = "Telling her the truth will cause you to miss a " + Karin.colored_name + " event."
                                    elif current_event.attention_type == 4:
                                        current_event.explain_text = "Starting this event before you have completed the beach vacation will impact " + Rin.colored_name + "'s events."
                                    elif current_event.attention_type == 5:
                                        current_event.explain_text = "Starting this event before you have completed the " + Yumi.colored_name + " event Abyss will impact " + Yumi.colored_name + "'s events."
                                    elif current_event.attention_type == 6:
                                        current_event.explain_text = "Not asking for a blowjob will cause you to miss a later " + Maki.colored_name + " event."
                                    elif current_event.attention_type == 7:
                                        current_event.explain_text = "Leaving " + Sana.colored_name + " will cause you to miss an event."
                                    elif current_event.attention_type == 8:
                                        current_event.explain_text = "Choosing " + Ayane.colored_name + " is a requirement for future events."
                                    elif current_event.attention_type == 11:
                                        current_event.explain_text = "Choosing " + Tsukasa.colored_name + " is a requirement for future events."
                                    elif current_event.attention_type == 12:
                                        current_event.explain_text = "Not sending the photo will lead to missing significant content but full consequences are still unknown."
                                    elif current_event.attention_type == 13:
                                        current_event.explain_text = "Choose to go in to avoid missing future " + Tsukasa.colored_name + " events."
                                    elif current_event.attention_type == 14:
                                        current_event.explain_text = "Need to view the picture in Sana's profile to get her number."
                                    elif current_event.attention_type == 16:
                                        current_event.explain_text = "Also need to read the text from Karin."
                                    elif current_event.attention_type == 17:
                                        current_event.explain_text = 'Choosing to "Kill Kirin" will cause you to miss an event.'

                                text (current_event.explain_text)
                                if current_event.var_name in ["chikalust10", "futabalust10", "makotofutabafuntimelustevent", "kirinlust30", "makotolust30"]:
                                    text (current_event.second_explain_text)

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            if dark_mode:
                textbutton _("Back") action ShowMenu("progressmod_dark")
            else:
                textbutton _("Back") action ShowMenu("progressmod")
