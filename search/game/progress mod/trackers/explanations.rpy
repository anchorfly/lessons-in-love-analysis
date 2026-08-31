screen explanations():

    tag menu

    key "n" action Return()

    $ explain_text = ""

    use game_menu(_("Hints"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        xpos .25
        ypos .14
        # style_prefix "hint"

        text(explain_event.girl.colored_name + '      ' + explain_event.name) style "tracker_text"

    vbox:
        xpos .25
        ypos .17
        style_prefix "hint"

        python:
            import string

            second_explain_text = ""
            if explain_event.attention_type == 1:
                explain_text = "Rejecting her will lead to missing events."
            elif explain_event.attention_type == 2:
                previous_event = eval("ev_" + explain_event.previous_event)
                if previous_event.girl == MainEvent:
                    previous_event = previous_event.var_name.rstrip(string.digits) + "1"
                    previous_event = eval("ev_" + previous_event)
                    explain_text = "You have until the " + previous_event.girl.colored_name + " " + previous_event.name + " to complete the lust requirement."
                else:
                    explain_text = "You have until the " + previous_event.girl.colored_name + " event " + previous_event.name + " to complete the lust requirement."
                if explain_event.second_attention == 9:
                    second_explain_text = "Choose " + Miku.colored_name + " as the winner of the costume contest."
                elif explain_event.second_attention == 10:
                    second_explain_text = "You will not be able to increase her lust after the " + MainEvent.colored_name + " There is Nothing."
                elif explain_event.second_attention == 15:
                    second_explain_text = "You will not be able to increase " + Makoto.colored_name + "'s lust after " + Nodoka.colored_name + "'s event Beyond the Reach of God."
            elif explain_event.attention_type == 3:
                explain_text = "Telling her the truth will cause you to miss a " + Karin.colored_name + " event."
            elif explain_event.attention_type == 4:
                explain_text = "Starting this event before you have completed the beach vacation will impact " + Rin.colored_name + "'s events."
            elif explain_event.attention_type == 5:
                explain_text = "Starting this event before you have completed the " + Yumi.colored_name + " event Abyss will impact " + Yumi.colored_name + "'s events."
            elif explain_event.attention_type == 6:
                explain_text = "Not asking for a blowjob will cause you to miss a later " + Maki.colored_name + " event."
            elif explain_event.attention_type == 7:
                explain_text = "Leaving " + Sana.colored_name + " will cause you to miss an event."
            elif explain_event.attention_type == 8:
                explain_text = "Choosing " + Ayane.colored_name + " is a requirement for future events."
            elif explain_event.attention_type == 11:
                explain_text = "Choosing " + Tsukasa.colored_name + " is a requirement for future events."
            elif explain_event.attention_type == 12:
                explain_text = "Not sending the photo will lead to missing significant content but full consequences are still unknown."
            elif explain_event.attention_type == 13:
                explain_text = "Choose to go in to avoid missing future " + Tsukasa.colored_name + " events."
            elif explain_event.attention_type == 14:
                explain_text = "Need to view the picture in Sana's profile to get her number."
            elif explain_event.attention_type == 16:
                explain_text = "Also need to read the text from Karin."
            elif explain_event.attention_type == 17:
                explain_text = 'Choosing to "Kill Kirin" will cause you to miss an event.'
            elif explain_event.attention_type == 18:
                explain_text = 'Make a save for this event to come back to during Chapter 4.'
            elif explain_event.attention_type == 19:
                explain_text = 'Must choose Maya in lingerie event for future event.'

        if not "correct choices" in explain_event.hint:
            text('     ' + explain_text)
        if not second_explain_text == "":
            text('     ' + second_explain_text)

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            if previous_screen == "hints":
                textbutton _("Back") action ShowMenu("hinttracker")
            elif previous_screen == "girls":
                textbutton _("Back") action ShowMenu("amitrackerm2")
            else:
                if dark_mode:
                    textbutton _("Back") action ShowMenu("progressmod_dark")
                else:
                    textbutton _("Back") action ShowMenu("progressmod")