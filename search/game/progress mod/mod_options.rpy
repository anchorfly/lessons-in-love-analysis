screen mod_options ():

    tag menu

    use game_menu(_("Event Tracker Options"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        
        style_prefix "tracker"

        xpos .25
        ypos .20

        hbox:
            vbox:
                textbutton _("Show completed events") action SetVariable("show_complete", not show_complete) text_style "optionbutton"
                text ("(Should already completed events be shown in the trackers?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Show completed girl portraits") action SetVariable("show_completed_girls", not show_completed_girls) text_style "optionbutton"
                text ("(Do you want to see the portraits for girls with no events remaining?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Desaturate portraits") action SetVariable("desaturate_girls", not desaturate_girls) text_style "optionbutton"
                text ("(Should the portraits of girls without any active hints be in black and white?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Show hints") action SetVariable("show_hints", not show_hints) text_style "optionbutton"
                text ("(Do you want to see event hints?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Show happy event hints") action SetVariable("show_happy_hints", not show_happy_hints) text_style "optionbutton"
                text ("(Do you want to see happy event hints on the hint screen?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Show next values") action SetVariable("show_next", not show_next) text_style "optionbutton"
                text ("(Do you want to see required values for a girl's next event on the progress screen?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Show DLC") action SetVariable("show_dlc", not show_dlc) text_style "optionbutton"
                text ("(Do you want to see the DLC option in the menu screen?)") style "explanation"
                text ("") style "explanation"
                textbutton _("Dark Mode") action SetVariable("dark_mode", not dark_mode) text_style "optionbutton"
                text ("(Are you using the dark mode mod?)") style "explanation"
                text ("") style "explanation"
            vbox:
                xpos 50

                if show_complete == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if show_completed_girls == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                text ("") style "explanation"
                if desaturate_girls == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if show_hints == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if show_happy_hints == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if show_next == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if show_dlc == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
                text ("") style "explanation"
                if dark_mode == True:
                    text ("On") style "mod"
                else:
                    text ("Off") style "mod"
                text ("") style "explanation"
        vbox:
            ypos 317

            if dark_mode:
                textbutton _("Back") action ShowMenu("progressmod_dark")
            else:
                textbutton _("Back") action ShowMenu('progressmod')