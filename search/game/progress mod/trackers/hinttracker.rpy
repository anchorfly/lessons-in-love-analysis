screen hinttracker():

    tag menu

    key "n" action Return()

    $ activate_girls()
    $ ProgressMod.update_all()
    python:
        if ProgressMod.longest_name > 34:
            hint_col = 0.53 + ((ProgressMod.longest_name - 34) * .007)
        else:
            hint_col = 0.53

    use game_menu(_("Hints"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        xpos .25
        ypos .14
        style_prefix "hint"

        $ main_chapter = "maintrackerch" + str(current_chapter) + "m"
        for current_event in MainEvent.event_list:
            if current_event.var_name in ProgressMod.current_hints.keys():
                if dark_mode:
                    textbutton _("Main event") action ShowMenu(main_chapter) style "event_button" text_style "hint_text"
                else:
                    textbutton _(MainEvent.colored_name) action ShowMenu(main_chapter) style "event_button" text_style "hint_text"
        for current_event in HappyEvent.event_list:
            if current_event.var_name in ProgressMod.current_hints.keys():
                textbutton _(HappyEvent.colored_name) action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
        for current_girl in ProgressMod.all_girls:
            if current_girl not in [MainEvent, HappyEvent]:
                if current_girl.active:
                    for current_event in current_girl.event_list:
                        if current_event.var_name in ProgressMod.current_hints.keys():
                            textbutton _(current_girl.colored_name) action [ShowMenu("amitrackerm2"), SetVariable("showgirl", current_girl.name)] style "event_button" text_style "amihint"

    vbox:
        xpos .33
        ypos .14
        style_prefix "hint"

        for current_event in MainEvent.event_list:
            if current_event.var_name in ProgressMod.current_hints.keys():
                text (current_event.name)
        for current_event in HappyEvent.event_list:
            if current_event.var_name in ProgressMod.current_hints.keys():
                text (current_event.name)
        for current_girl in ProgressMod.all_girls:
            if current_girl not in [MainEvent, HappyEvent]:
                if current_girl.active:
                    for current_event in current_girl.event_list:
                        if current_event.var_name in ProgressMod.current_hints.keys():
                            if "lust" in current_event.var_name or current_event.var_name in ["day98", "day68", "day86"]:
                                text _("{color=FF85FD}" + current_event.name + "{/color}")
                            elif "invite" in current_event.var_name:
                                text _("{color=778EFF}" + current_event.name + "{/color}")
                            else:
                                text (current_event.name)

    vbox:
        xpos hint_col
        ypos .14
        style_prefix "hint"

        if show_hints == True:

            for current_event in MainEvent.event_list:
                if current_event.var_name in ProgressMod.current_hints.keys():
                    if "(!)" in current_event.hint:
                        textbutton _("[current_event.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", current_event), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text (current_event.hint)
            for current_event in HappyEvent.event_list:
                if current_event.var_name in ProgressMod.current_hints.keys():
                    if show_happy_hints == True:
                        text (current_event.hint)
                    else:
                        text ("")
            for current_girl in ProgressMod.all_girls:
                if current_girl not in [MainEvent, HappyEvent]:
                    if current_girl.active:
                        for current_event in current_girl.event_list:
                            if current_event.var_name in ProgressMod.current_hints.keys():
                                if "(!)" in current_event.hint:
                                    textbutton _("[current_event.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", current_event), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                                else:
                                    text (current_event.hint)

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            if dark_mode:
                textbutton _("Back") action ShowMenu("progressmod_dark")
            else:
                textbutton _("Back") action ShowMenu("progressmod")
