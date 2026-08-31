screen hinttracker1():

    tag menu

    key "n" action Return()

    $ activate_girls()
    $ ProgressMod.update_all()

    use game_menu(_("Hints"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    vbox:
        xpos .25
        ypos .14
        style_prefix "hint"

        if (not ev_everyday.hint == "") and not (ev_everyday.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_clichebath.hint == "") and not (ev_clichebath.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_amiawake.hint == "") and not (ev_amiawake.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_firstclass.hint == "") and not (ev_firstclass.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_sleepover.hint == "") and not (ev_sleepover.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day5.hint == "") and not (ev_day5.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day7.hint == "") and not (ev_day7.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day8.hint == "") and not (ev_day8.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day12.hint == "") and not (ev_day12.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day14.hint == "") and not (ev_day14.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day16.hint == "") and not (ev_day16.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day20.hint == "") and not (ev_day20.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day21.hint == "") and not (ev_day21.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day24.hint == "") and not (ev_day24.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day26.hint == "") and not (ev_day26.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day28.hint == "") and not (ev_day28.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day30.hint == "") and not (ev_day30.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day33.hint == "") and not (ev_day33.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day36.hint == "") and not (ev_day36.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day38.hint == "") and not (ev_day38.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day40.hint == "") and not (ev_day40.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day44.hint == "") and not (ev_day44.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day48.hint == "") and not (ev_day48.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day50.hint == "") and not (ev_day50.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day54.hint == "") and not (ev_day54.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day56.hint == "") and not (ev_day56.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day60.hint == "") and not (ev_day60.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day63.hint == "") and not (ev_day63.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day65.hint == "") and not (ev_day65.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day70.hint == "") and not (ev_day70.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day72.hint == "") and not (ev_day72.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day77.hint == "") and not (ev_day77.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day79.hint == "") and not (ev_day79.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day80.hint == "") and not (ev_day80.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day83.hint == "") and not (ev_day83.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day85.hint == "") and not (ev_day85.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day89.hint == "") and not (ev_day89.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day91.hint == "") and not (ev_day91.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day96.hint == "") and not (ev_day96.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day102.hint == "") and not (ev_day102.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day103.hint == "") and not (ev_day103.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day110.hint == "") and not (ev_day110.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day114.hint == "") and not (ev_day114.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day120.hint == "") and not (ev_day120.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day121.hint == "") and not (ev_day121.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day126.hint == "") and not (ev_day126.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day128.hint == "") and not (ev_day128.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day130.hint == "") and not (ev_day130.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day138.hint == "") and not (ev_day138.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day140.hint == "") and not (ev_day140.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day142.hint == "") and not (ev_day142.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day144.hint == "") and not (ev_day144.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day150.hint == "") and not (ev_day150.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day153.hint == "") and not (ev_day153.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day154.hint == "") and not (ev_day154.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation1.hint == "") and not (ev_beachvacation1.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation2.hint == "") and not (ev_beachvacation2.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation3.hint == "") and not (ev_beachvacation3.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation4.hint == "") and not (ev_beachvacation4.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation5.hint == "") and not (ev_beachvacation5.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
            text ("")
        if (not ev_beachvacation6.hint == "") and not (ev_beachvacation6.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
            text ("")
        if (not ev_beachvacation7.hint == "") and not (ev_beachvacation7.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation8.hint == "") and not (ev_beachvacation8.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation9.hint == "") and not (ev_beachvacation9.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation10.hint == "") and not (ev_beachvacation10.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation11.hint == "") and not (ev_beachvacation11.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation12.hint == "") and not (ev_beachvacation12.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation13.hint == "") and not (ev_beachvacation13.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation14.hint == "") and not (ev_beachvacation14.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation15.hint == "") and not (ev_beachvacation15.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_beachvacation16.hint == "") and not (ev_beachvacation16.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween1.hint == "") and not (ev_halloween1.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween2.hint == "") and not (ev_halloween2.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween3.hint == "") and not (ev_halloween3.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween4.hint == "") and not (ev_halloween4.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
            text ("")
        if (not ev_halloween5.hint == "") and not (ev_halloween5.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween6.hint == "") and not (ev_halloween6.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween7.hint == "") and not (ev_halloween7.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween8.hint == "") and not (ev_halloween8.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween9.hint == "") and not (ev_halloween9.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween10.hint == "") and not (ev_halloween10.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween11.hint == "") and not (ev_halloween11.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween12.hint == "") and not (ev_halloween12.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
            text ("")
        if (not ev_halloween13.hint == "") and not (ev_halloween13.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_halloween14.hint == "") and not (ev_halloween14.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day214.hint == "") and not (ev_day214.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day215.hint == "") and not (ev_day215.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day216.hint == "") and not (ev_day216.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day217.hint == "") and not (ev_day217.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day218.hint == "") and not (ev_day218.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_day220.hint == "") and not (ev_day220.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"
        if (not ev_hoorayanotherreset.hint == "") and not (ev_hoorayanotherreset.hint == "Event will trigger automatically."):
            textbutton _("Main event") action ShowMenu("maintrackerch1m") style "event_button" text_style "hint_text"

        if HappyEvent.active:
            if (not ev_roomwithtrack.hint == "") and not (ev_roomwithtrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_letterttrack.hint == "") and not (ev_letterttrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_swimmingtrack.hint == "") and not (ev_swimmingtrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_howifeeltrack.hint == "") and not (ev_howifeeltrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_connecttrack.hint == "") and not (ev_connecttrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_specialclassroomtrack.hint == "") and not (ev_specialclassroomtrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_ticktocktrack.hint == "") and not (ev_ticktocktrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_trinity1track.hint == "") and not (ev_trinity1track.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
                text ("")
            if (not ev_trinity2track.hint == "") and not (ev_trinity2track.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_trinity3track.hint == "") and not (ev_trinity3track.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_babyfinches.hint == "") and not (ev_babyfinches.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"

        if Ami.active:
            if (not ev_firsttimeamisroom.hint == "") and not (ev_firsttimeamisroom.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimeamisroom.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amifirsthall.hint == "") and not (ev_amifirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_amifirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amisroom5.hint == "") and not (ev_amisroom5.hint == "Event will trigger automatically."):
                textbutton _("[ev_amisroom5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm5.hint == "") and not (ev_amidorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amisroom10.hint == "") and not (ev_amisroom10.hint == "Event will trigger automatically."):
                textbutton _("[ev_amisroom10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_aminew1.hint == "") and not (ev_aminew1.hint == "Event will trigger automatically."):
                textbutton _("[ev_aminew1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
                text ("")
            if (not ev_aminew2.hint == "") and not (ev_aminew2.hint == "Event will trigger automatically."):
                textbutton _("[ev_aminew2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm10.hint == "") and not (ev_amidorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_day98.hint == "") and not (ev_day98.hint == "Event will trigger automatically."):
                textbutton _("[ev_day98.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm15.hint == "") and not (ev_amidorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amisroom15.hint == "") and not (ev_amisroom15.hint == "Event will trigger automatically."):
                textbutton _("[ev_amisroom15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amilust10.hint == "") and not (ev_amilust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_amilust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amisroom20.hint == "") and not (ev_amisroom20.hint == "Event will trigger automatically."):
                textbutton _("[ev_amisroom20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm20.hint == "") and not (ev_amidorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amisroom25.hint == "") and not (ev_amisroom25.hint == "Event will trigger automatically."):
                textbutton _("[ev_amisroom25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm25.hint == "") and not (ev_amidorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"

        if Maya.active:
            if (not ev_firsttimeshrine.hint == "") and not (ev_firsttimeshrine.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimeshrine.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayafirsthall.hint == "") and not (ev_mayafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine5.hint == "") and not (ev_shrine5.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm5.hint == "") and not (ev_mayadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine10.hint == "") and not (ev_shrine10.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm10.hint == "") and not (ev_mayadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine15.hint == "") and not (ev_shrine15.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm15.hint == "") and not (ev_mayadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine20.hint == "") and not (ev_shrine20.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm20.hint == "") and not (ev_mayadorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine25.hint == "") and not (ev_shrine25.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm25.hint == "") and not (ev_mayadorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"

        if Chika.active:
            if (not ev_firsttimemall.hint == "") and not (ev_firsttimemall.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimemall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikafirsthall.hint == "") and not (ev_chikafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall5.hint == "") and not (ev_mall5.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadorm5.hint == "") and not (ev_chikadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall10.hint == "") and not (ev_mall10.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadorm10.hint == "") and not (ev_chikadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadorm15.hint == "") and not (ev_chikadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall15.hint == "") and not (ev_mall15.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadorm20.hint == "") and not (ev_chikadorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall20.hint == "") and not (ev_mall20.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_day139.hint == "") and not (ev_day139.hint == "Event will trigger automatically."):
                textbutton _("[ev_day139.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikainvite1.hint == "") and not (ev_chikainvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikainvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikainvite2.hint == "") and not (ev_chikainvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikainvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"

        if Yumi.active:
            if (not ev_firsttimestreets.hint == "") and not (ev_firsttimestreets.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimestreets.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumifirsthall.hint == "") and not (ev_yumifirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumifirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets5.hint == "") and not (ev_streets5.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets10.hint == "") and not (ev_streets10.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm5.hint == "") and not (ev_yumidorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm10.hint == "") and not (ev_yumidorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm15.hint == "") and not (ev_yumidorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets15.hint == "") and not (ev_streets15.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets20.hint == "") and not (ev_streets20.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm20.hint == "") and not (ev_yumidorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets25.hint == "") and not (ev_streets25.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm25.hint == "") and not (ev_yumidorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"

        if Ayane.active:
            if (not ev_firsttimedojo.hint == "") and not (ev_firsttimedojo.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimedojo.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
                text ("")
            if (not ev_ayanefirsthall.hint == "") and not (ev_ayanefirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanefirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_dojo5.hint == "") and not (ev_dojo5.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_dojo10.hint == "") and not (ev_dojo10.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm5.hint == "") and not (ev_ayanedorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanenew1.hint == "") and not (ev_ayanenew1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanenew1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanenew2.hint == "") and not (ev_ayanenew2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanenew2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanenew3.hint == "") and not (ev_ayanenew3.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanenew3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
                text ("")
            if (not ev_ayanedorm10.hint == "") and not (ev_ayanedorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm15.hint == "") and not (ev_ayanedorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_day68.hint == "") and not (ev_day68.hint == "Event will trigger automatically."):
                textbutton _("[ev_day68.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_dojo20.hint == "") and not (ev_dojo20.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm20.hint == "") and not (ev_ayanedorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanelust10.hint == "") and not (ev_ayanelust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanelust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_dojo25.hint == "") and not (ev_dojo25.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm25.hint == "") and not (ev_ayanedorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
                text ("")
            if (not ev_dojo30.hint == "") and not (ev_dojo30.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm30.hint == "") and not (ev_ayanedorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"

        if Sana.active:
            if (not ev_firsttimebar.hint == "") and not (ev_firsttimebar.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimebar.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanafirsthall.hint == "") and not (ev_sanafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar5.hint == "") and not (ev_bar5.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm5.hint == "") and not (ev_sanadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar10.hint == "") and not (ev_bar10.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm10.hint == "") and not (ev_sanadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar15.hint == "") and not (ev_bar15.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm15.hint == "") and not (ev_sanadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar20.hint == "") and not (ev_bar20.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm20.hint == "") and not (ev_sanadorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar25.hint == "") and not (ev_bar25.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm25.hint == "") and not (ev_sanadorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar30.hint == "") and not (ev_bar30.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm30.hint == "") and not (ev_sanadorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
                text ("")

        if Makoto.active:
            if (not ev_firsttimepornshop.hint == "") and not (ev_firsttimepornshop.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimepornshop.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotofirsthall.hint == "") and not (ev_makotofirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotofirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_pornshop5.hint == "") and not (ev_pornshop5.hint == "Event will trigger automatically."):
                textbutton _("[ev_pornshop5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotodorm5.hint == "") and not (ev_makotodorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotodorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_pornshop10.hint == "") and not (ev_pornshop10.hint == "Event will trigger automatically."):
                textbutton _("[ev_pornshop10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotonew1.hint == "") and not (ev_makotonew1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotonew1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotonew2.hint == "") and not (ev_makotonew2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotonew2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotonew3.hint == "") and not (ev_makotonew3.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotonew3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_pornshop15.hint == "") and not (ev_pornshop15.hint == "Event will trigger automatically."):
                textbutton _("[ev_pornshop15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotolust5.hint == "") and not (ev_makotolust5.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotolust5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotoinvite1.hint == "") and not (ev_makotoinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotoinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotoinvite2.hint == "") and not (ev_makotoinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotoinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_pornshop20.hint == "") and not (ev_pornshop20.hint == "Event will trigger automatically."):
                textbutton _("[ev_pornshop20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotodorm20.hint == "") and not (ev_makotodorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotodorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_pornshop25.hint == "") and not (ev_pornshop25.hint == "Event will trigger automatically."):
                textbutton _("[ev_pornshop25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotodorm25.hint == "") and not (ev_makotodorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotodorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"

        if Miku.active:
            if (not ev_firsttimesoccerfield.hint == "") and not (ev_firsttimesoccerfield.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimesoccerfield.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikufirsthall.hint == "") and not (ev_mikufirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikufirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer5.hint == "") and not (ev_soccer5.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm5.hint == "") and not (ev_mikudorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer10.hint == "") and not (ev_soccer10.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm10.hint == "") and not (ev_mikudorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer15.hint == "") and not (ev_soccer15.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm15.hint == "") and not (ev_mikudorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer20.hint == "") and not (ev_soccer20.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer25.hint == "") and not (ev_soccer25.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm25.hint == "") and not (ev_mikudorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_soccer30.hint == "") and not (ev_soccer30.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm30.hint == "") and not (ev_mikudorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"

        if Futaba.active:
            if (not ev_firsttimelibrary.hint == "") and not (ev_firsttimelibrary.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimelibrary.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabafall.hint == "") and not (ev_futabafall.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabafall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library10.hint == "") and not (ev_library10.hint == "Event will trigger automatically."):
                textbutton _("[ev_library10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabafirsthall.hint == "") and not (ev_futabafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabafirstvisit.hint == "") and not (ev_futabafirstvisit.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabafirstvisit.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm10.hint == "") and not (ev_futabadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library15.hint == "") and not (ev_library15.hint == "Event will trigger automatically."):
                textbutton _("[ev_library15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabanew1.hint == "") and not (ev_futabanew1.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabanew1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabanew2.hint == "") and not (ev_futabanew2.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabanew2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabanew3.hint == "") and not (ev_futabanew3.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabanew3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm15.hint == "") and not (ev_futabadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library20.hint == "") and not (ev_library20.hint == "Event will trigger automatically."):
                textbutton _("[ev_library20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library25.hint == "") and not (ev_library25.hint == "Event will trigger automatically."):
                textbutton _("[ev_library25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm25.hint == "") and not (ev_futabadorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_day86.hint == "") and not (ev_day86.hint == "Event will trigger automatically."):
                textbutton _("[ev_day86.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library30.hint == "") and not (ev_library30.hint == "Event will trigger automatically."):
                textbutton _("[ev_library30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm30.hint == "") and not (ev_futabadorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library35.hint == "") and not (ev_library35.hint == "Event will trigger automatically."):
                textbutton _("[ev_library35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm35.hint == "") and not (ev_futabadorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"

        if Rin.active:
            if (not ev_firsttimecafe.hint == "") and not (ev_firsttimecafe.hint == "Event will trigger automatically."):
                textbutton _("[ev_firsttimecafe.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafesugar.hint == "") and not (ev_cafesugar.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafesugar.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe10.hint == "") and not (ev_cafe10.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rinfirsthall.hint == "") and not (ev_rinfirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_rinfirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rinfirstvisit.hint == "") and not (ev_rinfirstvisit.hint == "Event will trigger automatically."):
                textbutton _("[ev_rinfirstvisit.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm10.hint == "") and not (ev_rindorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe15.hint == "") and not (ev_cafe15.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm15.hint == "") and not (ev_rindorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe20.hint == "") and not (ev_cafe20.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm20.hint == "") and not (ev_rindorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe25.hint == "") and not (ev_cafe25.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm25.hint == "") and not (ev_rindorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe30.hint == "") and not (ev_cafe30.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm30.hint == "") and not (ev_rindorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm35.hint == "") and not (ev_rindorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe35.hint == "") and not (ev_cafe35.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"

        if Molly.active:
            if (not ev_mollycafe1.hint == "") and not (ev_mollycafe1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollyfirsthall.hint == "") and not (ev_mollyfirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollyfirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe5.hint == "") and not (ev_mollycafe5.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm5.hint == "") and not (ev_mollydorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe10.hint == "") and not (ev_mollycafe10.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm10.hint == "") and not (ev_mollydorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"

        if Tsuneyo.active:
            if (not ev_ramen1.hint == "") and not (ev_ramen1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyofirsthall.hint == "") and not (ev_tsuneyofirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyofirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_ramen5.hint == "") and not (ev_ramen5.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
                text ("")
            if (not ev_tsuneyodorm5.hint == "") and not (ev_tsuneyodorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyodorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_ramen10.hint == "") and not (ev_ramen10.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyodorm10.hint == "") and not (ev_tsuneyodorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyodorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"

        if Sara.active:
            if (not ev_saradate1.hint == "") and not (ev_saradate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_saradate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_saralust5.hint == "") and not (ev_saralust5.hint == "Event will trigger automatically."):
                textbutton _("[ev_saralust5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarainvite1.hint == "") and not (ev_sarainvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarainvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarainvite2.hint == "") and not (ev_sarainvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarainvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_saralust10.hint == "") and not (ev_saralust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_saralust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"

        if Haruka.active:
            if (not ev_harukadate1.hint == "") and not (ev_harukadate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukadate5.hint == "") and not (ev_harukadate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukafirstlust.hint == "") and not (ev_harukafirstlust.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukafirstlust.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukalust10.hint == "") and not (ev_harukalust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukalust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukadate10.hint == "") and not (ev_harukadate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukadate15.hint == "") and not (ev_harukadate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"

        if Maki.active:
            if (not ev_makidate1.hint == "") and not (ev_makidate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makidate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makidate5.hint == "") and not (ev_makidate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_makidate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
                text ("")

        if Kirin.active:
            if (not ev_kirindate1.hint == "") and not (ev_kirindate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindate5.hint == "") and not (ev_kirindate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindate10.hint == "") and not (ev_kirindate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"

        if Karin.active:
            if (not ev_karindate1.hint == "") and not (ev_karindate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karindate5.hint == "") and not (ev_karindate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karindate10.hint == "") and not (ev_karindate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"

        if Kaori.active:
            if (not ev_kaoridate1.hint == "") and not (ev_kaoridate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate5.hint == "") and not (ev_kaoridate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate10.hint == "") and not (ev_kaoridate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"

        if Chinami.active:
            if (not ev_chinamidate1.hint == "") and not (ev_chinamidate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_chinamidate5.hint == "") and not (ev_chinamidate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"

    vbox:
        xpos .33
        ypos .14
        style_prefix "hint"

        if (not ev_everyday.hint == "") and not (ev_everyday.hint == "Event will trigger automatically."):
                text ("Every Day I Grow Some More")
        if (not ev_clichebath.hint == "") and not (ev_clichebath.hint == "Event will trigger automatically."):
                text ("A New You")
        if (not ev_amiawake.hint == "") and not (ev_amiawake.hint == "Event will trigger automatically."):
                text ("Am I Awake?")
        if (not ev_firstclass.hint == "") and not (ev_firstclass.hint == "Event will trigger automatically."):
                text ("First (?) Day of School")
        if (not ev_sleepover.hint == "") and not (ev_sleepover.hint == "Event will trigger automatically."):
                text ("Slumber Party")
        if (not ev_day5.hint == "") and not (ev_day5.hint == "Event will trigger automatically."):
                text ("The Devil Incarnate")
        if (not ev_day7.hint == "") and not (ev_day7.hint == "Event will trigger automatically."):
                text ("Super Secret Sex Dungeon")
        if (not ev_day8.hint == "") and not (ev_day8.hint == "Event will trigger automatically."):
                text ("Delinquent")
        if (not ev_day12.hint == "") and not (ev_day12.hint == "Event will trigger automatically."):
                text ("Mitochondria")
        if (not ev_day14.hint == "") and not (ev_day14.hint == "Event will trigger automatically."):
                text ("Self-Esteem")
        if (not ev_day16.hint == "") and not (ev_day16.hint == "Event will trigger automatically."):
                text ("Operation: Fallen Angel")
        if (not ev_day20.hint == "") and not (ev_day20.hint == "Event will trigger automatically."):
                text ("I Thought of You")
        if (not ev_day21.hint == "") and not (ev_day21.hint == "Event will trigger automatically."):
                text ("Not Even Me")
        if (not ev_day24.hint == "") and not (ev_day24.hint == "Event will trigger automatically."):
                text ("No Romeo")
        if (not ev_day26.hint == "") and not (ev_day26.hint == "Event will trigger automatically."):
                text ("Outside of Everything")
        if (not ev_day28.hint == "") and not (ev_day28.hint == "Event will trigger automatically."):
                text ("Ponytail")
        if (not ev_day30.hint == "") and not (ev_day30.hint == "Event will trigger automatically."):
                text ("Drowning")
        if (not ev_day33.hint == "") and not (ev_day33.hint == "Event will trigger automatically."):
                text ("So Many Voices")
        if (not ev_day36.hint == "") and not (ev_day36.hint == "Event will trigger automatically."):
                text ("Cleaning Duty")
        if (not ev_day38.hint == "") and not (ev_day38.hint == "Event will trigger automatically."):
                text ("Walk in the Park")
        if (not ev_day40.hint == "") and not (ev_day40.hint == "Event will trigger automatically."):
                text ("Saved by the Bell")
        if (not ev_day44.hint == "") and not (ev_day44.hint == "Event will trigger automatically."):
                text ("This Town Has Two Halves")
        if (not ev_day48.hint == "") and not (ev_day48.hint == "Event will trigger automatically."):
                text ("Little Girl")
        if (not ev_day50.hint == "") and not (ev_day50.hint == "Event will trigger automatically."):
                text ("Missing")
        if (not ev_day54.hint == "") and not (ev_day54.hint == "Event will trigger automatically."):
                text ("The Sakakibara Diet")
        if (not ev_day56.hint == "") and not (ev_day56.hint == "Event will trigger automatically."):
                text ("Normal Office Visit")
        if (not ev_day60.hint == "") and not (ev_day60.hint == "Event will trigger automatically."):
                text ("O World (In Our Final Moments)")
        if (not ev_day63.hint == "") and not (ev_day63.hint == "Event will trigger automatically."):
                text ("One to Seven")
        if (not ev_day65.hint == "") and not (ev_day65.hint == "Event will trigger automatically."):
                text ("Girl-Talk")
        if (not ev_day70.hint == "") and not (ev_day70.hint == "Event will trigger automatically."):
                text ("The 'S' Word")
        if (not ev_day72.hint == "") and not (ev_day72.hint == "Event will trigger automatically."):
                text ("Weight Limit")
        if (not ev_day77.hint == "") and not (ev_day77.hint == "Event will trigger automatically."):
                text ("Slope Intercept Form")
        if (not ev_day79.hint == "") and not (ev_day79.hint == "Event will trigger automatically."):
                text ("Scientific Research")
        if (not ev_day80.hint == "") and not (ev_day80.hint == "Event will trigger automatically."):
                text ("Secret Ingredient")
        if (not ev_day83.hint == "") and not (ev_day83.hint == "Event will trigger automatically."):
                text ("Parasite")
        if (not ev_day85.hint == "") and not (ev_day85.hint == "Event will trigger automatically."):
                text ("Contractions")
        if (not ev_day89.hint == "") and not (ev_day89.hint == "Event will trigger automatically."):
                text ("Milk, Eggs, and Water")
        if (not ev_day91.hint == "") and not (ev_day91.hint == "Event will trigger automatically."):
                text ("Stronger I Become")
        if (not ev_day96.hint == "") and not (ev_day96.hint == "Event will trigger automatically."):
                text ("Recall")
        if (not ev_day102.hint == "") and not (ev_day102.hint == "Event will trigger automatically."):
                text ("Rewrite")
        if (not ev_day103.hint == "") and not (ev_day103.hint == "Event will trigger automatically."):
                text ("Reset")
        if (not ev_day110.hint == "") and not (ev_day110.hint == "Event will trigger automatically."):
                text ("Cursed Birds")
        if (not ev_day114.hint == "") and not (ev_day114.hint == "Event will trigger automatically."):
                text ("Human Trafficking")
        if (not ev_day120.hint == "") and not (ev_day120.hint == "Event will trigger automatically."):
                text ("Girl Talk Pt. II")
        if (not ev_day121.hint == "") and not (ev_day121.hint == "Event will trigger automatically."):
                text ("A Different View")
        if (not ev_day126.hint == "") and not (ev_day126.hint == "Event will trigger automatically."):
                text ("On The Bright Side")
        if (not ev_day128.hint == "") and not (ev_day128.hint == "Event will trigger automatically."):
                text ("Everything Horrible")
        if (not ev_day130.hint == "") and not (ev_day130.hint == "Event will trigger automatically."):
                text ("Erotic Game Protagonist")
        if (not ev_day138.hint == "") and not (ev_day138.hint == "Event will trigger automatically."):
                text ("Rumors")
        if (not ev_day140.hint == "") and not (ev_day140.hint == "Event will trigger automatically."):
                text ("The Gem of the Emerald Isle")
        if (not ev_day142.hint == "") and not (ev_day142.hint == "Event will trigger automatically."):
                text ("Size Matters")
        if (not ev_day144.hint == "") and not (ev_day144.hint == "Event will trigger automatically."):
                text ("Tsuneyo Tojo, Stand-up Comedian")
        if (not ev_day150.hint == "") and not (ev_day150.hint == "Event will trigger automatically."):
                text ("A Proper Introduction")
        if (not ev_day153.hint == "") and not (ev_day153.hint == "Event will trigger automatically."):
                text ("Supreme Overlord")
        if (not ev_day154.hint == "") and not (ev_day154.hint == "Event will trigger automatically."):
                text ("Lifting the Curse")
        if (not ev_beachvacation1.hint == "") and not (ev_beachvacation1.hint == "Event will trigger automatically."):
                text ("What's Done is Done")
        if (not ev_beachvacation2.hint == "") and not (ev_beachvacation2.hint == "Event will trigger automatically."):
                text ("All Along the Shoreline")
        if (not ev_beachvacation3.hint == "") and not (ev_beachvacation3.hint == "Event will trigger automatically."):
                text ("My Heart is Full")
        if (not ev_beachvacation4.hint == "") and not (ev_beachvacation4.hint == "Event will trigger automatically."):
                text ("Extra French Fries")
        if (not ev_beachvacation5.hint == "") and not (ev_beachvacation5.hint == "Event will trigger automatically."):
                text ("Behind a Bathroom, Under the ")
                text ("  Blazing Sun ")
        if (not ev_beachvacation6.hint == "") and not (ev_beachvacation6.hint == "Event will trigger automatically."):
                text ("Three Girls in a Line on the ")
                text ("  Beach ")
        if (not ev_beachvacation7.hint == "") and not (ev_beachvacation7.hint == "Event will trigger automatically."):
                text ("The Moon is Beautiful")
        if (not ev_beachvacation8.hint == "") and not (ev_beachvacation8.hint == "Event will trigger automatically."):
                text ("The Legacy of Thaum Pt. I")
        if (not ev_beachvacation9.hint == "") and not (ev_beachvacation9.hint == "Event will trigger automatically."):
                text ("Summer and Winter")
        if (not ev_beachvacation10.hint == "") and not (ev_beachvacation10.hint == "Event will trigger automatically."):
                text ("Where Puppies Roam Free")
        if (not ev_beachvacation11.hint == "") and not (ev_beachvacation11.hint == "Event will trigger automatically."):
                text ("Die For What You Believe In")
        if (not ev_beachvacation12.hint == "") and not (ev_beachvacation12.hint == "Event will trigger automatically."):
                text ("Reverse Cowgirl")
        if (not ev_beachvacation13.hint == "") and not (ev_beachvacation13.hint == "Event will trigger automatically."):
                text ("Smile Guide")
        if (not ev_beachvacation14.hint == "") and not (ev_beachvacation14.hint == "Event will trigger automatically."):
                text ("Prayer Position")
        if (not ev_beachvacation15.hint == "") and not (ev_beachvacation15.hint == "Event will trigger automatically."):
                text ("Cry. Cry. Cry.")
        if (not ev_beachvacation16.hint == "") and not (ev_beachvacation16.hint == "Event will trigger automatically."):
                text ("See You in the Morning")
        if (not ev_halloween1.hint == "") and not (ev_halloween1.hint == "Event will trigger automatically."):
                text ("The Value of Sharing")
        if (not ev_halloween2.hint == "") and not (ev_halloween2.hint == "Event will trigger automatically."):
                text ("Guest of Honor")
        if (not ev_halloween3.hint == "") and not (ev_halloween3.hint == "Event will trigger automatically."):
                text ("The Meat has Come")
        if (not ev_halloween4.hint == "") and not (ev_halloween4.hint == "Event will trigger automatically."):
                text ("Mysterious Abundance of ")
                text ("  Chickens ")
        if (not ev_halloween5.hint == "") and not (ev_halloween5.hint == "Event will trigger automatically."):
                text ("Sexy Land")
        if (not ev_halloween6.hint == "") and not (ev_halloween6.hint == "Event will trigger automatically."):
                text ("They're Just Lights")
        if (not ev_halloween7.hint == "") and not (ev_halloween7.hint == "Event will trigger automatically."):
                text ("Once, Twice, Ten Times")
        if (not ev_halloween8.hint == "") and not (ev_halloween8.hint == "Event will trigger automatically."):
                text ("Mechanical Bull")
        if (not ev_halloween9.hint == "") and not (ev_halloween9.hint == "Event will trigger automatically."):
                text ("At Least It's Not Christmas")
        if (not ev_halloween10.hint == "") and not (ev_halloween10.hint == "Event will trigger automatically."):
                text ("Samhain")
        if (not ev_halloween11.hint == "") and not (ev_halloween11.hint == "Event will trigger automatically."):
                text ("Wicked Witch of Kumon-mi")
        if (not ev_halloween12.hint == "") and not (ev_halloween12.hint == "Event will trigger automatically."):
                text ("The Depressing Implication of ")
                text ("  Goosebumps ")
        if (not ev_halloween13.hint == "") and not (ev_halloween13.hint == "Event will trigger automatically."):
                text ("Pry With a Smile")
        if (not ev_halloween14.hint == "") and not (ev_halloween14.hint == "Event will trigger automatically."):
                text ("Kadrillionbilliontrillion")
        if (not ev_day214.hint == "") and not (ev_day214.hint == "Event will trigger automatically."):
                text ("As Loud as a Whisper Can Be")
        if (not ev_day215.hint == "") and not (ev_day215.hint == "Event will trigger automatically."):
                text ("Two Wooden Doors")
        if (not ev_day216.hint == "") and not (ev_day216.hint == "Event will trigger automatically."):
                text ("Happy Places")
        if (not ev_day217.hint == "") and not (ev_day217.hint == "Event will trigger automatically."):
                text ("Tradition")
        if (not ev_day218.hint == "") and not (ev_day218.hint == "Event will trigger automatically."):
                text ("Stray Cat")
        if (not ev_day220.hint == "") and not (ev_day220.hint == "Event will trigger automatically."):
                text ("There is Nothing")
        if (not ev_hoorayanotherreset.hint == "") and not (ev_hoorayanotherreset.hint == "Event will trigger automatically."):
                text ("Changing of Seasons")

        if HappyEvent.active:
            if (not ev_roomwithtrack.hint == "") and not (ev_roomwithtrack.hint == "Event will trigger automatically."):
                text ("The Room With Clocks")
            if (not ev_letterttrack.hint == "") and not (ev_letterttrack.hint == "Event will trigger automatically."):
                text ("The Letter 'T'")
            if (not ev_swimmingtrack.hint == "") and not (ev_swimmingtrack.hint == "Event will trigger automatically."):
                text ("Swim Trip")
            if (not ev_howifeeltrack.hint == "") and not (ev_howifeeltrack.hint == "Event will trigger automatically."):
                text ("How I Feel")
            if (not ev_connecttrack.hint == "") and not (ev_connecttrack.hint == "Event will trigger automatically."):
                text ("Everything is Connected")
            if (not ev_specialclassroomtrack.hint == "") and not (ev_specialclassroomtrack.hint == "Event will trigger automatically."):
                text ("Turn Off The Lights")
            if (not ev_ticktocktrack.hint == "") and not (ev_ticktocktrack.hint == "Event will trigger automatically."):
                text ("Tick Tock Tick Tock Tick Tock")
            if (not ev_trinity1track.hint == "") and not (ev_trinity1track.hint == "Event will trigger automatically."):
                text ("Trinity Pt. I: Stations of the ")
                text ("  Cross ")
            if (not ev_trinity2track.hint == "") and not (ev_trinity2track.hint == "Event will trigger automatically."):
                text ("Trinity Pt. II: Hell is Empty")
            if (not ev_trinity3track.hint == "") and not (ev_trinity3track.hint == "Event will trigger automatically."):
                text ("Trinity Pt. III: Non Est Deus")
            if (not ev_babyfinches.hint == "") and not (ev_babyfinches.hint == "Event will trigger automatically."):
                text ("Baby Finches")

        if Ami.active:
            if (not ev_firsttimeamisroom.hint == "") and not (ev_firsttimeamisroom.hint == "Event will trigger automatically."):
                text ("Harem Tutorial")
            if (not ev_amifirsthall.hint == "") and not (ev_amifirsthall.hint == "Event will trigger automatically."):
                text ("Uninvited")
            if (not ev_amisroom5.hint == "") and not (ev_amisroom5.hint == "Event will trigger automatically."):
                text ("The Queen of Spiders")
            if (not ev_amidorm5.hint == "") and not (ev_amidorm5.hint == "Event will trigger automatically."):
                text ("Home Away From Home")
            if (not ev_amisroom10.hint == "") and not (ev_amisroom10.hint == "Event will trigger automatically."):
                text ("Something Darker")
            if (not ev_aminew1.hint == "") and not (ev_aminew1.hint == "Event will trigger automatically."):
                text ("Couple's Discount (Sea of ")
                text ("  Diamonds) ")
            if (not ev_aminew2.hint == "") and not (ev_aminew2.hint == "Event will trigger automatically."):
                text ("Ode to a Marsh Warbler")
            if (not ev_amidorm10.hint == "") and not (ev_amidorm10.hint == "Event will trigger automatically."):
                text ("No One Can See Us")
            if (not ev_day98.hint == "") and not (ev_day98.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Walking on Air{/color}")
            if (not ev_amidorm15.hint == "") and not (ev_amidorm15.hint == "Event will trigger automatically."):
                text ("Back Out in the Heat")
            if (not ev_amisroom15.hint == "") and not (ev_amisroom15.hint == "Event will trigger automatically."):
                text ("Important Things")
            if (not ev_amilust10.hint == "") and not (ev_amilust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Wake Up Call{/color}")
            if (not ev_amisroom20.hint == "") and not (ev_amisroom20.hint == "Event will trigger automatically."):
                text ("Cute Girls and Stuff")
            if (not ev_amidorm20.hint == "") and not (ev_amidorm20.hint == "Event will trigger automatically."):
                text ("Divergence")
            if (not ev_amisroom25.hint == "") and not (ev_amisroom25.hint == "Event will trigger automatically."):
                text ("Such Small Hands")
            if (not ev_amidorm25.hint == "") and not (ev_amidorm25.hint == "Event will trigger automatically."):
                text ("Everlasting Love")

        if Maya.active:
            if (not ev_firsttimeshrine.hint == "") and not (ev_firsttimeshrine.hint == "Event will trigger automatically."):
                text ("A New Beginning")
            if (not ev_mayafirsthall.hint == "") and not (ev_mayafirsthall.hint == "Event will trigger automatically."):
                text ("Mondays")
            if (not ev_shrine5.hint == "") and not (ev_shrine5.hint == "Event will trigger automatically."):
                text ("Different Worlds")
            if (not ev_mayadorm5.hint == "") and not (ev_mayadorm5.hint == "Event will trigger automatically."):
                text ("Secrets Worth Keeping")
            if (not ev_shrine10.hint == "") and not (ev_shrine10.hint == "Event will trigger automatically."):
                text ("Past/Present/Future")
            if (not ev_mayadorm10.hint == "") and not (ev_mayadorm10.hint == "Event will trigger automatically."):
                text ("Rewind/Repeat/Refuse")
            if (not ev_shrine15.hint == "") and not (ev_shrine15.hint == "Event will trigger automatically."):
                text ("You and Me")
            if (not ev_mayadorm15.hint == "") and not (ev_mayadorm15.hint == "Event will trigger automatically."):
                text ("Takoyaki")
            if (not ev_shrine20.hint == "") and not (ev_shrine20.hint == "Event will trigger automatically."):
                text ("Nothing is Real")
            if (not ev_mayadorm20.hint == "") and not (ev_mayadorm20.hint == "Event will trigger automatically."):
                text ("Close Your Eyes")
            if (not ev_shrine25.hint == "") and not (ev_shrine25.hint == "Event will trigger automatically."):
                text ("Watermelons and Violin")
            if (not ev_mayadorm25.hint == "") and not (ev_mayadorm25.hint == "Event will trigger automatically."):
                text ("FLAVOR BEAM!")

        if Chika.active:
            if (not ev_firsttimemall.hint == "") and not (ev_firsttimemall.hint == "Event will trigger automatically."):
                text ("The Retail Machine")
            if (not ev_chikafirsthall.hint == "") and not (ev_chikafirsthall.hint == "Event will trigger automatically."):
                text ("A Dog that Does Math")
            if (not ev_mall5.hint == "") and not (ev_mall5.hint == "Event will trigger automatically."):
                text ("Big Shot Teacher")
            if (not ev_chikadorm5.hint == "") and not (ev_chikadorm5.hint == "Event will trigger automatically."):
                text ("Something About Biting")
            if (not ev_mall10.hint == "") and not (ev_mall10.hint == "Event will trigger automatically."):
                text ("Behind The Curtain")
            if (not ev_chikadorm10.hint == "") and not (ev_chikadorm10.hint == "Event will trigger automatically."):
                text ("Side Event")
            if (not ev_chikadorm15.hint == "") and not (ev_chikadorm15.hint == "Event will trigger automatically."):
                text ("A Castle for Everyone")
            if (not ev_mall15.hint == "") and not (ev_mall15.hint == "Event will trigger automatically."):
                text ("A Dog that Doesn't Do Math")
            if (not ev_chikadorm20.hint == "") and not (ev_chikadorm20.hint == "Event will trigger automatically."):
                text ("Schadenfreude")
            if (not ev_mall20.hint == "") and not (ev_mall20.hint == "Event will trigger automatically."):
                text ("True Power: Unleashed")
            if (not ev_day139.hint == "") and not (ev_day139.hint == "Event will trigger automatically."):
                text ("Detention")
            if (not ev_chikainvite1.hint == "") and not (ev_chikainvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}A Trip to the Moon{/color}")
            if (not ev_chikainvite2.hint == "") and not (ev_chikainvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}First Hunt{/color}")

        if Yumi.active:
            if (not ev_firsttimestreets.hint == "") and not (ev_firsttimestreets.hint == "Event will trigger automatically."):
                text ("Five Million Dollars")
            if (not ev_yumifirsthall.hint == "") and not (ev_yumifirsthall.hint == "Event will trigger automatically."):
                text ("Micropenis")
            if (not ev_streets5.hint == "") and not (ev_streets5.hint == "Event will trigger automatically."):
                text ("Three Second Smile")
            if (not ev_streets10.hint == "") and not (ev_streets10.hint == "Event will trigger automatically."):
                text ("I See You")
            if (not ev_yumidorm5.hint == "") and not (ev_yumidorm5.hint == "Event will trigger automatically."):
                text ("Fuck The Police")
            if (not ev_yumidorm10.hint == "") and not (ev_yumidorm10.hint == "Event will trigger automatically."):
                text ("Yumi Revitalization Project")
            if (not ev_yumidorm15.hint == "") and not (ev_yumidorm15.hint == "Event will trigger automatically."):
                text ("Worse Comes to Worst")
            if (not ev_streets15.hint == "") and not (ev_streets15.hint == "Event will trigger automatically."):
                text ("Apples to Apples")
            if (not ev_streets20.hint == "") and not (ev_streets20.hint == "Event will trigger automatically."):
                text ("Token Tsundere")
            if (not ev_yumidorm20.hint == "") and not (ev_yumidorm20.hint == "Event will trigger automatically."):
                text ("Great Expectations")
            if (not ev_streets25.hint == "") and not (ev_streets25.hint == "Event will trigger automatically."):
                text ("A Place Like This")
            if (not ev_yumidorm25.hint == "") and not (ev_yumidorm25.hint == "Event will trigger automatically."):
                text ("Caught in the Vortex")

        if Ayane.active:
            if (not ev_firsttimedojo.hint == "") and not (ev_firsttimedojo.hint == "Event will trigger automatically."):
                text ("The Unwavering Bravery of ")
                text ("  Ayane Amamiya ")
            if (not ev_ayanefirsthall.hint == "") and not (ev_ayanefirsthall.hint == "Event will trigger automatically."):
                text ("Spy on Me")
            if (not ev_dojo5.hint == "") and not (ev_dojo5.hint == "Event will trigger automatically."):
                text ("The Battle for Kumon-mi")
            if (not ev_dojo10.hint == "") and not (ev_dojo10.hint == "Event will trigger automatically."):
                text ("Names of Our Children")
            if (not ev_ayanedorm5.hint == "") and not (ev_ayanedorm5.hint == "Event will trigger automatically."):
                text ("Home Sweet Home")
            if (not ev_ayanenew1.hint == "") and not (ev_ayanenew1.hint == "Event will trigger automatically."):
                text ("Imprinting")
            if (not ev_ayanenew2.hint == "") and not (ev_ayanenew2.hint == "Event will trigger automatically."):
                text ("Far From Fantasy")
            if (not ev_ayanenew3.hint == "") and not (ev_ayanenew3.hint == "Event will trigger automatically."):
                text ("Forever Yours (Top of the ")
                text ("  World) ")
            if (not ev_ayanedorm10.hint == "") and not (ev_ayanedorm10.hint == "Event will trigger automatically."):
                text ("Less Like the Vulture")
            if (not ev_ayanedorm15.hint == "") and not (ev_ayanedorm15.hint == "Event will trigger automatically."):
                text ("First Words")
            if (not ev_day68.hint == "") and not (ev_day68.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Backwards Spider Crawl{/color}")
            if (not ev_dojo20.hint == "") and not (ev_dojo20.hint == "Event will trigger automatically."):
                text ("Endless Torment")
            if (not ev_ayanedorm20.hint == "") and not (ev_ayanedorm20.hint == "Event will trigger automatically."):
                text ("Still Young")
            if (not ev_ayanelust10.hint == "") and not (ev_ayanelust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Prisoner{/color}")
            if (not ev_dojo25.hint == "") and not (ev_dojo25.hint == "Event will trigger automatically."):
                text ("Regularly Scheduled Programming")
            if (not ev_ayanedorm25.hint == "") and not (ev_ayanedorm25.hint == "Event will trigger automatically."):
                text ("Cold Air of an Encroaching ")
                text ("  Winter ")
            if (not ev_dojo30.hint == "") and not (ev_dojo30.hint == "Event will trigger automatically."):
                text ("First and Second")
            if (not ev_ayanedorm30.hint == "") and not (ev_ayanedorm30.hint == "Event will trigger automatically."):
                text ("Crazier Things Have Happened")

        if Sana.active:
            if (not ev_firsttimebar.hint == "") and not (ev_firsttimebar.hint == "Event will trigger automatically."):
                text ("Family Business")
            if (not ev_sanafirsthall.hint == "") and not (ev_sanafirsthall.hint == "Event will trigger automatically."):
                text ("Nothing to Do")
            if (not ev_bar5.hint == "") and not (ev_bar5.hint == "Event will trigger automatically."):
                text ("The Bare Minimum")
            if (not ev_sanadorm5.hint == "") and not (ev_sanadorm5.hint == "Event will trigger automatically."):
                text ("Recluse")
            if (not ev_bar10.hint == "") and not (ev_bar10.hint == "Event will trigger automatically."):
                text ("Supermom")
            if (not ev_sanadorm10.hint == "") and not (ev_sanadorm10.hint == "Event will trigger automatically."):
                text ("Anywhere At All")
            if (not ev_bar15.hint == "") and not (ev_bar15.hint == "Event will trigger automatically."):
                text ("Carry Me Home")
            if (not ev_sanadorm15.hint == "") and not (ev_sanadorm15.hint == "Event will trigger automatically."):
                text ("Shaking The Tree")
            if (not ev_bar20.hint == "") and not (ev_bar20.hint == "Event will trigger automatically."):
                text ("Scouting Mission")
            if (not ev_sanadorm20.hint == "") and not (ev_sanadorm20.hint == "Event will trigger automatically."):
                text ("Nice Weather We're Having")
            if (not ev_bar25.hint == "") and not (ev_bar25.hint == "Event will trigger automatically."):
                text ("Life is a Tomato")
            if (not ev_sanadorm25.hint == "") and not (ev_sanadorm25.hint == "Event will trigger automatically."):
                text ("The Girl in the Black Dress")
            if (not ev_bar30.hint == "") and not (ev_bar30.hint == "Event will trigger automatically."):
                text ("Self-Medication")
            if (not ev_sanadorm30.hint == "") and not (ev_sanadorm30.hint == "Event will trigger automatically."):
                text ("Tortoises and the Concept of ")
                text ("  Friendship ")

        if Makoto.active:
            if (not ev_firsttimepornshop.hint == "") and not (ev_firsttimepornshop.hint == "Event will trigger automatically."):
                text ("Unexpected Profession")
            if (not ev_makotofirsthall.hint == "") and not (ev_makotofirsthall.hint == "Event will trigger automatically."):
                text ("Teacher's Pet")
            if (not ev_pornshop5.hint == "") and not (ev_pornshop5.hint == "Event will trigger automatically."):
                text ("Watching Porn Alone")
            if (not ev_makotodorm5.hint == "") and not (ev_makotodorm5.hint == "Event will trigger automatically."):
                text ("Completely Platonic")
            if (not ev_pornshop10.hint == "") and not (ev_pornshop10.hint == "Event will trigger automatically."):
                text ("Rising of the Tide")
            if (not ev_makotonew1.hint == "") and not (ev_makotonew1.hint == "Event will trigger automatically."):
                text ("Frogger")
            if (not ev_makotonew2.hint == "") and not (ev_makotonew2.hint == "Event will trigger automatically."):
                text ("Sowing the Seeds")
            if (not ev_makotonew3.hint == "") and not (ev_makotonew3.hint == "Event will trigger automatically."):
                text ("Egg Tooth")
            if (not ev_pornshop15.hint == "") and not (ev_pornshop15.hint == "Event will trigger automatically."):
                text ("Fishing For Love")
            if (not ev_makotolust5.hint == "") and not (ev_makotolust5.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Quid Pro Quo{/color}")
            if (not ev_makotoinvite1.hint == "") and not (ev_makotoinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Declaration of War{/color}")
            if (not ev_makotoinvite2.hint == "") and not (ev_makotoinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Studious Teen Virgin{/color}")
            if (not ev_pornshop20.hint == "") and not (ev_pornshop20.hint == "Event will trigger automatically."):
                text ("Aftermath")
            if (not ev_makotodorm20.hint == "") and not (ev_makotodorm20.hint == "Event will trigger automatically."):
                text ("Residual Sadness")
            if (not ev_pornshop25.hint == "") and not (ev_pornshop25.hint == "Event will trigger automatically."):
                text ("Service Charge")
            if (not ev_makotodorm25.hint == "") and not (ev_makotodorm25.hint == "Event will trigger automatically."):
                text ("Bluejay")

        if Miku.active:
            if (not ev_firsttimesoccerfield.hint == "") and not (ev_firsttimesoccerfield.hint == "Event will trigger automatically."):
                text ("Daytime Stalking Pass")
            if (not ev_mikufirsthall.hint == "") and not (ev_mikufirsthall.hint == "Event will trigger automatically."):
                text ("Behind Closed Doors")
            if (not ev_soccer5.hint == "") and not (ev_soccer5.hint == "Event will trigger automatically."):
                text ("It's Always Sunny in Kumon-mi")
            if (not ev_mikudorm5.hint == "") and not (ev_mikudorm5.hint == "Event will trigger automatically."):
                text ("Broken Bones")
            if (not ev_soccer10.hint == "") and not (ev_soccer10.hint == "Event will trigger automatically."):
                text ("Nightvision")
            if (not ev_mikudorm10.hint == "") and not (ev_mikudorm10.hint == "Event will trigger automatically."):
                text ("You and Me and the Night")
            if (not ev_soccer15.hint == "") and not (ev_soccer15.hint == "Event will trigger automatically."):
                text ("Hormones Running Wild")
            if (not ev_mikudorm15.hint == "") and not (ev_mikudorm15.hint == "Event will trigger automatically."):
                text ("Moments Like This")
            if (not ev_soccer20.hint == "") and not (ev_soccer20.hint == "Event will trigger automatically."):
                text ("Coach")
            if (not ev_soccer25.hint == "") and not (ev_soccer25.hint == "Event will trigger automatically."):
                text ("Thighs On-Demand")
            if (not ev_mikudorm25.hint == "") and not (ev_mikudorm25.hint == "Event will trigger automatically."):
                text ("Scaredy Cat")
            if (not ev_soccer30.hint == "") and not (ev_soccer30.hint == "Event will trigger automatically."):
                text ("An Extra Set of Arms")
            if (not ev_mikudorm30.hint == "") and not (ev_mikudorm30.hint == "Event will trigger automatically."):
                text ("One. Two. Three.")

        if Futaba.active:
            if (not ev_firsttimelibrary.hint == "") and not (ev_firsttimelibrary.hint == "Event will trigger automatically."):
                text ("Impossible Blossoms")
            if (not ev_futabafall.hint == "") and not (ev_futabafall.hint == "Event will trigger automatically."):
                text ("Fan Fiction")
            if (not ev_library10.hint == "") and not (ev_library10.hint == "Event will trigger automatically."):
                text ("Upside Down")
            if (not ev_futabafirsthall.hint == "") and not (ev_futabafirsthall.hint == "Event will trigger automatically."):
                text ("Unidentical Twins")
            if (not ev_futabafirstvisit.hint == "") and not (ev_futabafirstvisit.hint == "Event will trigger automatically."):
                text ("Under the Radar")
            if (not ev_futabadorm10.hint == "") and not (ev_futabadorm10.hint == "Event will trigger automatically."):
                text ("Cutting Through Cocoons")
            if (not ev_library15.hint == "") and not (ev_library15.hint == "Event will trigger automatically."):
                text ("Self-Insert")
            if (not ev_futabanew1.hint == "") and not (ev_futabanew1.hint == "Event will trigger automatically."):
                text ("Broken Flowers")
            if (not ev_futabanew2.hint == "") and not (ev_futabanew2.hint == "Event will trigger automatically."):
                text ("Great Burdock Leaves")
            if (not ev_futabanew3.hint == "") and not (ev_futabanew3.hint == "Event will trigger automatically."):
                text ("Clam's Tongue")
            if (not ev_futabadorm15.hint == "") and not (ev_futabadorm15.hint == "Event will trigger automatically."):
                text ("Legs of a Dying Spider")
            if (not ev_library20.hint == "") and not (ev_library20.hint == "Event will trigger automatically."):
                text ("Only Child")
            if (not ev_library25.hint == "") and not (ev_library25.hint == "Event will trigger automatically."):
                text ("A Book About Dragons")
            if (not ev_futabadorm25.hint == "") and not (ev_futabadorm25.hint == "Event will trigger automatically."):
                text ("Two Hours")
            if (not ev_day86.hint == "") and not (ev_day86.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Like Fucking a Cloud{/color}")
            if (not ev_library30.hint == "") and not (ev_library30.hint == "Event will trigger automatically."):
                text ("Under the Table")
            if (not ev_futabadorm30.hint == "") and not (ev_futabadorm30.hint == "Event will trigger automatically."):
                text ("A Tree Falls in the Forest")
            if (not ev_library35.hint == "") and not (ev_library35.hint == "Event will trigger automatically."):
                text ("No, You")
            if (not ev_futabadorm35.hint == "") and not (ev_futabadorm35.hint == "Event will trigger automatically."):
                text ("Overload")

        if Rin.active:
            if (not ev_firsttimecafe.hint == "") and not (ev_firsttimecafe.hint == "Event will trigger automatically."):
                text ("Guinea Pig")
            if (not ev_cafesugar.hint == "") and not (ev_cafesugar.hint == "Event will trigger automatically."):
                text ("The Flavor of Love")
            if (not ev_cafe10.hint == "") and not (ev_cafe10.hint == "Event will trigger automatically."):
                text ("Haruka")
            if (not ev_rinfirsthall.hint == "") and not (ev_rinfirsthall.hint == "Event will trigger automatically."):
                text ("Locked Out")
            if (not ev_rinfirstvisit.hint == "") and not (ev_rinfirstvisit.hint == "Event will trigger automatically."):
                text ("Skulls")
            if (not ev_rindorm10.hint == "") and not (ev_rindorm10.hint == "Event will trigger automatically."):
                text ("Rin's Secret")
            if (not ev_cafe15.hint == "") and not (ev_cafe15.hint == "Event will trigger automatically."):
                text ("Window of the Waking Mind")
            if (not ev_rindorm15.hint == "") and not (ev_rindorm15.hint == "Event will trigger automatically."):
                text ("Boundaries")
            if (not ev_cafe20.hint == "") and not (ev_cafe20.hint == "Event will trigger automatically."):
                text ("Nothing Was Missing, Except Me")
            if (not ev_rindorm20.hint == "") and not (ev_rindorm20.hint == "Event will trigger automatically."):
                text ("Delirium")
            if (not ev_cafe25.hint == "") and not (ev_cafe25.hint == "Event will trigger automatically."):
                text ("Good Day, Humans")
            if (not ev_rindorm25.hint == "") and not (ev_rindorm25.hint == "Event will trigger automatically."):
                text ("Sock Fetish")
            if (not ev_cafe30.hint == "") and not (ev_cafe30.hint == "Event will trigger automatically."):
                text ("Nothing Was Different")
            if (not ev_rindorm30.hint == "") and not (ev_rindorm30.hint == "Event will trigger automatically."):
                text ("Two Steps Back")
            if (not ev_rindorm35.hint == "") and not (ev_rindorm35.hint == "Event will trigger automatically."):
                text ("Ten Steps Forward")
            if (not ev_cafe35.hint == "") and not (ev_cafe35.hint == "Event will trigger automatically."):
                text ("I Died With You")

        if Molly.active:
            if (not ev_mollycafe1.hint == "") and not (ev_mollycafe1.hint == "Event will trigger automatically."):
                text ("NTR & Pregnancy")
            if (not ev_mollyfirsthall.hint == "") and not (ev_mollyfirsthall.hint == "Event will trigger automatically."):
                text ("The Cult of Molly")
            if (not ev_mollycafe5.hint == "") and not (ev_mollycafe5.hint == "Event will trigger automatically."):
                text ("Remnants of Forgotten Memes")
            if (not ev_mollydorm5.hint == "") and not (ev_mollydorm5.hint == "Event will trigger automatically."):
                text ("Torrent of Power")
            if (not ev_mollycafe10.hint == "") and not (ev_mollycafe10.hint == "Event will trigger automatically."):
                text ("Something Out of a Nukige")
            if (not ev_mollydorm10.hint == "") and not (ev_mollydorm10.hint == "Event will trigger automatically."):
                text ("The Dark Entity")

        if Tsuneyo.active:
            if (not ev_ramen1.hint == "") and not (ev_ramen1.hint == "Event will trigger automatically."):
                text ("Snake Venom")
            if (not ev_tsuneyofirsthall.hint == "") and not (ev_tsuneyofirsthall.hint == "Event will trigger automatically."):
                text ("The Life of a Blue Whale")
            if (not ev_ramen5.hint == "") and not (ev_ramen5.hint == "Event will trigger automatically."):
                text ("Between the Slurps of Pork ")
                text ("  Broth ")
            if (not ev_tsuneyodorm5.hint == "") and not (ev_tsuneyodorm5.hint == "Event will trigger automatically."):
                text ("Drug Use & Jump-Rope")
            if (not ev_ramen10.hint == "") and not (ev_ramen10.hint == "Event will trigger automatically."):
                text ("A Short List")
            if (not ev_tsuneyodorm10.hint == "") and not (ev_tsuneyodorm10.hint == "Event will trigger automatically."):
                text ("The Man Who Loves Nothing")

        if Sara.active:
            if (not ev_saradate1.hint == "") and not (ev_saradate1.hint == "Event will trigger automatically."):
                text ("A Woman's Heart")
            if (not ev_saralust5.hint == "") and not (ev_saralust5.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Zero Friction{/color}")
            if (not ev_sarainvite1.hint == "") and not (ev_sarainvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Third Wheel{/color}")
            if (not ev_sarainvite2.hint == "") and not (ev_sarainvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}A Mostly Empty Home{/color}")
            if (not ev_saralust10.hint == "") and not (ev_saralust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Medical Assistance{/color}")

        if Haruka.active:
            if (not ev_harukadate1.hint == "") and not (ev_harukadate1.hint == "Event will trigger automatically."):
                text ("Drunk Again")
            if (not ev_harukadate5.hint == "") and not (ev_harukadate5.hint == "Event will trigger automatically."):
                text ("Invisible Worm")
            if (not ev_harukafirstlust.hint == "") and not (ev_harukafirstlust.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}The Need to be Hurt{/color}")
            if (not ev_harukalust10.hint == "") and not (ev_harukalust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Bad Kitty{/color}")
            if (not ev_harukadate10.hint == "") and not (ev_harukadate10.hint == "Event will trigger automatically."):
                text ("Performance Review")
            if (not ev_harukadate15.hint == "") and not (ev_harukadate15.hint == "Event will trigger automatically."):
                text ("Watching TV Alone")

        if Maki.active:
            if (not ev_makidate1.hint == "") and not (ev_makidate1.hint == "Event will trigger automatically."):
                text ("Beautiful Porn Salesman")
            if (not ev_makidate5.hint == "") and not (ev_makidate5.hint == "Event will trigger automatically."):
                text ("Maki Miyamura's Mom-Mode ")
                text ("  Mission ")

        if Kirin.active:
            if (not ev_kirindate1.hint == "") and not (ev_kirindate1.hint == "Event will trigger automatically."):
                text ("Partners in Crime")
            if (not ev_kirindate5.hint == "") and not (ev_kirindate5.hint == "Event will trigger automatically."):
                text ("Long and Hard")
            if (not ev_kirindate10.hint == "") and not (ev_kirindate10.hint == "Event will trigger automatically."):
                text ("Politics! Pleasure! Ponies!")

        if Karin.active:
            if (not ev_karindate1.hint == "") and not (ev_karindate1.hint == "Event will trigger automatically."):
                text ("Further and Further")
            if (not ev_karindate5.hint == "") and not (ev_karindate5.hint == "Event will trigger automatically."):
                text ("Walking Penis Monster")
            if (not ev_karindate10.hint == "") and not (ev_karindate10.hint == "Event will trigger automatically."):
                text ("If Only")

        if Kaori.active:
            if (not ev_kaoridate1.hint == "") and not (ev_kaoridate1.hint == "Event will trigger automatically."):
                text ("How to Date a Human")
            if (not ev_kaoridate5.hint == "") and not (ev_kaoridate5.hint == "Event will trigger automatically."):
                text ("The Best Ways to Rub a Cock")
            if (not ev_kaoridate10.hint == "") and not (ev_kaoridate10.hint == "Event will trigger automatically."):
                text ("Objects and Appendages")

        if Chinami.active:
            if (not ev_chinamidate1.hint == "") and not (ev_chinamidate1.hint == "Event will trigger automatically."):
                text ("5,000 Year-Old Wizard")
            if (not ev_chinamidate5.hint == "") and not (ev_chinamidate5.hint == "Event will trigger automatically."):
                text ("Chinami-Corp")

    vbox:
        xpos .53
        ypos .14
        style_prefix "hint"

        if show_hints == True:

            if (not ev_everyday.hint == "") and not (ev_everyday.hint == "Event will trigger automatically."):
                text ("[ev_everyday.hint]")
            if (not ev_clichebath.hint == "") and not (ev_clichebath.hint == "Event will trigger automatically."):
                text ("[ev_clichebath.hint]")
            if (not ev_amiawake.hint == "") and not (ev_amiawake.hint == "Event will trigger automatically."):
                text ("[ev_amiawake.hint]")
            if (not ev_firstclass.hint == "") and not (ev_firstclass.hint == "Event will trigger automatically."):
                text ("[ev_firstclass.hint]")
            if (not ev_sleepover.hint == "") and not (ev_sleepover.hint == "Event will trigger automatically."):
                text ("[ev_sleepover.hint]")
            if (not ev_day5.hint == "") and not (ev_day5.hint == "Event will trigger automatically."):
                text ("[ev_day5.hint]")
            if (not ev_day7.hint == "") and not (ev_day7.hint == "Event will trigger automatically."):
                text ("[ev_day7.hint]")
            if (not ev_day8.hint == "") and not (ev_day8.hint == "Event will trigger automatically."):
                text ("[ev_day8.hint]")
            if (not ev_day12.hint == "") and not (ev_day12.hint == "Event will trigger automatically."):
                text ("[ev_day12.hint]")
            if (not ev_day14.hint == "") and not (ev_day14.hint == "Event will trigger automatically."):
                text ("[ev_day14.hint]")
            if (not ev_day16.hint == "") and not (ev_day16.hint == "Event will trigger automatically."):
                text ("[ev_day16.hint]")
            if (not ev_day20.hint == "") and not (ev_day20.hint == "Event will trigger automatically."):
                text ("[ev_day20.hint]")
            if (not ev_day21.hint == "") and not (ev_day21.hint == "Event will trigger automatically."):
                text ("[ev_day21.hint]")
            if (not ev_day24.hint == "") and not (ev_day24.hint == "Event will trigger automatically."):
                text ("[ev_day24.hint]")
            if (not ev_day26.hint == "") and not (ev_day26.hint == "Event will trigger automatically."):
                text ("[ev_day26.hint]")
            if (not ev_day28.hint == "") and not (ev_day28.hint == "Event will trigger automatically."):
                text ("[ev_day28.hint]")
            if (not ev_day30.hint == "") and not (ev_day30.hint == "Event will trigger automatically."):
                text ("[ev_day30.hint]")
            if (not ev_day33.hint == "") and not (ev_day33.hint == "Event will trigger automatically."):
                text ("[ev_day33.hint]")
            if (not ev_day36.hint == "") and not (ev_day36.hint == "Event will trigger automatically."):
                text ("[ev_day36.hint]")
            if (not ev_day38.hint == "") and not (ev_day38.hint == "Event will trigger automatically."):
                text ("[ev_day38.hint]")
            if (not ev_day40.hint == "") and not (ev_day40.hint == "Event will trigger automatically."):
                text ("[ev_day40.hint]")
            if (not ev_day44.hint == "") and not (ev_day44.hint == "Event will trigger automatically."):
                text ("[ev_day44.hint]")
            if (not ev_day48.hint == "") and not (ev_day48.hint == "Event will trigger automatically."):
                text ("[ev_day48.hint]")
            if (not ev_day50.hint == "") and not (ev_day50.hint == "Event will trigger automatically."):
                text ("[ev_day50.hint]")
            if (not ev_day54.hint == "") and not (ev_day54.hint == "Event will trigger automatically."):
                text ("[ev_day54.hint]")
            if (not ev_day56.hint == "") and not (ev_day56.hint == "Event will trigger automatically."):
                text ("[ev_day56.hint]")
            if (not ev_day60.hint == "") and not (ev_day60.hint == "Event will trigger automatically."):
                text ("[ev_day60.hint]")
            if (not ev_day63.hint == "") and not (ev_day63.hint == "Event will trigger automatically."):
                text ("[ev_day63.hint]")
            if (not ev_day65.hint == "") and not (ev_day65.hint == "Event will trigger automatically."):
                text ("[ev_day65.hint]")
            if (not ev_day70.hint == "") and not (ev_day70.hint == "Event will trigger automatically."):
                text ("[ev_day70.hint]")
            if (not ev_day72.hint == "") and not (ev_day72.hint == "Event will trigger automatically."):
                text ("[ev_day72.hint]")
            if (not ev_day77.hint == "") and not (ev_day77.hint == "Event will trigger automatically."):
                text ("[ev_day77.hint]")
            if (not ev_day79.hint == "") and not (ev_day79.hint == "Event will trigger automatically."):
                text ("[ev_day79.hint]")
            if (not ev_day80.hint == "") and not (ev_day80.hint == "Event will trigger automatically."):
                text ("[ev_day80.hint]")
            if (not ev_day83.hint == "") and not (ev_day83.hint == "Event will trigger automatically."):
                text ("[ev_day83.hint]")
            if (not ev_day85.hint == "") and not (ev_day85.hint == "Event will trigger automatically."):
                text ("[ev_day85.hint]")
            if (not ev_day89.hint == "") and not (ev_day89.hint == "Event will trigger automatically."):
                text ("[ev_day89.hint]")
            if (not ev_day91.hint == "") and not (ev_day91.hint == "Event will trigger automatically."):
                text ("[ev_day91.hint]")
            if (not ev_day96.hint == "") and not (ev_day96.hint == "Event will trigger automatically."):
                text ("[ev_day96.hint]")
            if (not ev_day102.hint == "") and not (ev_day102.hint == "Event will trigger automatically."):
                text ("[ev_day102.hint]")
            if (not ev_day103.hint == "") and not (ev_day103.hint == "Event will trigger automatically."):
                text ("[ev_day103.hint]")
            if (not ev_day110.hint == "") and not (ev_day110.hint == "Event will trigger automatically."):
                text ("[ev_day110.hint]")
            if (not ev_day114.hint == "") and not (ev_day114.hint == "Event will trigger automatically."):
                text ("[ev_day114.hint]")
            if (not ev_day120.hint == "") and not (ev_day120.hint == "Event will trigger automatically."):
                text ("[ev_day120.hint]")
            if (not ev_day121.hint == "") and not (ev_day121.hint == "Event will trigger automatically."):
                text ("[ev_day121.hint]")
            if (not ev_day126.hint == "") and not (ev_day126.hint == "Event will trigger automatically."):
                text ("[ev_day126.hint]")
            if (not ev_day128.hint == "") and not (ev_day128.hint == "Event will trigger automatically."):
                text ("[ev_day128.hint]")
            if (not ev_day130.hint == "") and not (ev_day130.hint == "Event will trigger automatically."):
                text ("[ev_day130.hint]")
            if (not ev_day138.hint == "") and not (ev_day138.hint == "Event will trigger automatically."):
                text ("[ev_day138.hint]")
            if (not ev_day140.hint == "") and not (ev_day140.hint == "Event will trigger automatically."):
                text ("[ev_day140.hint]")
            if (not ev_day142.hint == "") and not (ev_day142.hint == "Event will trigger automatically."):
                text ("[ev_day142.hint]")
            if (not ev_day144.hint == "") and not (ev_day144.hint == "Event will trigger automatically."):
                text ("[ev_day144.hint]")
            if (not ev_day150.hint == "") and not (ev_day150.hint == "Event will trigger automatically."):
                text ("[ev_day150.hint]")
            if (not ev_day153.hint == "") and not (ev_day153.hint == "Event will trigger automatically."):
                text ("[ev_day153.hint]")
            if (not ev_day154.hint == "") and not (ev_day154.hint == "Event will trigger automatically."):
                text ("[ev_day154.hint]")
            if (not ev_beachvacation1.hint == "") and not (ev_beachvacation1.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation1.hint]")
            if (not ev_beachvacation2.hint == "") and not (ev_beachvacation2.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation2.hint]")
            if (not ev_beachvacation3.hint == "") and not (ev_beachvacation3.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation3.hint]")
            if (not ev_beachvacation4.hint == "") and not (ev_beachvacation4.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation4.hint]")
            if (not ev_beachvacation5.hint == "") and not (ev_beachvacation5.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation5.hint]")
                text ("")
            if (not ev_beachvacation6.hint == "") and not (ev_beachvacation6.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation6.hint]")
                text ("")
            if (not ev_beachvacation7.hint == "") and not (ev_beachvacation7.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation7.hint]")
            if (not ev_beachvacation8.hint == "") and not (ev_beachvacation8.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation8.hint]")
            if (not ev_beachvacation9.hint == "") and not (ev_beachvacation9.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation9.hint]")
            if (not ev_beachvacation10.hint == "") and not (ev_beachvacation10.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation10.hint]")
            if (not ev_beachvacation11.hint == "") and not (ev_beachvacation11.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation11.hint]")
            if (not ev_beachvacation12.hint == "") and not (ev_beachvacation12.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation12.hint]")
            if (not ev_beachvacation13.hint == "") and not (ev_beachvacation13.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation13.hint]")
            if (not ev_beachvacation14.hint == "") and not (ev_beachvacation14.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation14.hint]")
            if (not ev_beachvacation15.hint == "") and not (ev_beachvacation15.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation15.hint]")
            if (not ev_beachvacation16.hint == "") and not (ev_beachvacation16.hint == "Event will trigger automatically."):
                text ("[ev_beachvacation16.hint]")
            if (not ev_halloween1.hint == "") and not (ev_halloween1.hint == "Event will trigger automatically."):
                text ("[ev_halloween1.hint]")
            if (not ev_halloween2.hint == "") and not (ev_halloween2.hint == "Event will trigger automatically."):
                text ("[ev_halloween2.hint]")
            if (not ev_halloween3.hint == "") and not (ev_halloween3.hint == "Event will trigger automatically."):
                text ("[ev_halloween3.hint]")
            if (not ev_halloween4.hint == "") and not (ev_halloween4.hint == "Event will trigger automatically."):
                text ("[ev_halloween4.hint]")
                text ("")
            if (not ev_halloween5.hint == "") and not (ev_halloween5.hint == "Event will trigger automatically."):
                text ("[ev_halloween5.hint]")
            if (not ev_halloween6.hint == "") and not (ev_halloween6.hint == "Event will trigger automatically."):
                text ("[ev_halloween6.hint]")
            if (not ev_halloween7.hint == "") and not (ev_halloween7.hint == "Event will trigger automatically."):
                text ("[ev_halloween7.hint]")
            if (not ev_halloween8.hint == "") and not (ev_halloween8.hint == "Event will trigger automatically."):
                text ("[ev_halloween8.hint]")
            if (not ev_halloween9.hint == "") and not (ev_halloween9.hint == "Event will trigger automatically."):
                text ("[ev_halloween9.hint]")
            if (not ev_halloween10.hint == "") and not (ev_halloween10.hint == "Event will trigger automatically."):
                text ("[ev_halloween10.hint]")
            if (not ev_halloween11.hint == "") and not (ev_halloween11.hint == "Event will trigger automatically."):
                text ("[ev_halloween11.hint]")
            if (not ev_halloween12.hint == "") and not (ev_halloween12.hint == "Event will trigger automatically."):
                text ("[ev_halloween12.hint]")
                text ("")
            if (not ev_halloween13.hint == "") and not (ev_halloween13.hint == "Event will trigger automatically."):
                text ("[ev_halloween13.hint]")
            if (not ev_halloween14.hint == "") and not (ev_halloween14.hint == "Event will trigger automatically."):
                text ("[ev_halloween14.hint]")
            if (not ev_day214.hint == "") and not (ev_day214.hint == "Event will trigger automatically."):
                text ("[ev_day214.hint]")
            if (not ev_day215.hint == "") and not (ev_day215.hint == "Event will trigger automatically."):
                text ("[ev_day215.hint]")
            if (not ev_day216.hint == "") and not (ev_day216.hint == "Event will trigger automatically."):
                text ("[ev_day216.hint]")
            if (not ev_day217.hint == "") and not (ev_day217.hint == "Event will trigger automatically."):
                text ("[ev_day217.hint]")
            if (not ev_day218.hint == "") and not (ev_day218.hint == "Event will trigger automatically."):
                text ("[ev_day218.hint]")
            if (not ev_day220.hint == "") and not (ev_day220.hint == "Event will trigger automatically."):
                text ("[ev_day220.hint]")
            if (not ev_hoorayanotherreset.hint == "") and not (ev_hoorayanotherreset.hint == "Event will trigger automatically."):
                text ("[ev_hoorayanotherreset.hint]")

            if HappyEvent.active:
                if (not ev_roomwithtrack.hint == "") and not (ev_roomwithtrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_roomwithtrack.hint]")
                    else:
                        text ("")
                if (not ev_letterttrack.hint == "") and not (ev_letterttrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_letterttrack.hint]")
                    else:
                        text ("")
                if (not ev_swimmingtrack.hint == "") and not (ev_swimmingtrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_swimmingtrack.hint]")
                    else:
                        text ("")
                if (not ev_howifeeltrack.hint == "") and not (ev_howifeeltrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_howifeeltrack.hint]")
                    else:
                        text ("")
                if (not ev_connecttrack.hint == "") and not (ev_connecttrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_connecttrack.hint]")
                    else:
                        text ("")
                if (not ev_specialclassroomtrack.hint == "") and not (ev_specialclassroomtrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_specialclassroomtrack.hint]")
                    else:
                        text ("")
                if (not ev_ticktocktrack.hint == "") and not (ev_ticktocktrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_ticktocktrack.hint]")
                    else:
                        text ("")
                if (not ev_trinity1track.hint == "") and not (ev_trinity1track.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_trinity1track.hint]")
                        text ("")
                    else:
                        text ("")
                        text ("")
                if (not ev_trinity2track.hint == "") and not (ev_trinity2track.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_trinity2track.hint]")
                    else:
                        text ("")
                if (not ev_trinity3track.hint == "") and not (ev_trinity3track.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_trinity3track.hint]")
                    else:
                        text ("")
                if (not ev_babyfinches.hint == "") and not (ev_babyfinches.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_babyfinches.hint]")
                    else:
                        text ("")

            if Ami.active:
                if (not ev_firsttimeamisroom.hint == "") and not (ev_firsttimeamisroom.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimeamisroom.hint:
                        textbutton _("[ev_firsttimeamisroom.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimeamisroom), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimeamisroom.hint]")
                if (not ev_amifirsthall.hint == "") and not (ev_amifirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amifirsthall.hint:
                        textbutton _("[ev_amifirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amifirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amifirsthall.hint]")
                if (not ev_amisroom5.hint == "") and not (ev_amisroom5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amisroom5.hint:
                        textbutton _("[ev_amisroom5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amisroom5.hint]")
                if (not ev_amidorm5.hint == "") and not (ev_amidorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm5.hint:
                        textbutton _("[ev_amidorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm5.hint]")
                if (not ev_amisroom10.hint == "") and not (ev_amisroom10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amisroom10.hint:
                        textbutton _("[ev_amisroom10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amisroom10.hint]")
                if (not ev_aminew1.hint == "") and not (ev_aminew1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_aminew1.hint:
                        textbutton _("[ev_aminew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_aminew1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_aminew1.hint]")
                    text ("")
                if (not ev_aminew2.hint == "") and not (ev_aminew2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_aminew2.hint:
                        textbutton _("[ev_aminew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_aminew2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_aminew2.hint]")
                if (not ev_amidorm10.hint == "") and not (ev_amidorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm10.hint:
                        textbutton _("[ev_amidorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm10.hint]")
                if (not ev_day98.hint == "") and not (ev_day98.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day98.hint:
                        textbutton _("[ev_day98.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day98), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day98.hint]")
                if (not ev_amidorm15.hint == "") and not (ev_amidorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm15.hint:
                        textbutton _("[ev_amidorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm15.hint]")
                if (not ev_amisroom15.hint == "") and not (ev_amisroom15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amisroom15.hint:
                        textbutton _("[ev_amisroom15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amisroom15.hint]")
                if (not ev_amilust10.hint == "") and not (ev_amilust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amilust10.hint:
                        textbutton _("[ev_amilust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amilust10.hint]")
                if (not ev_amisroom20.hint == "") and not (ev_amisroom20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amisroom20.hint:
                        textbutton _("[ev_amisroom20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amisroom20.hint]")
                if (not ev_amidorm20.hint == "") and not (ev_amidorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm20.hint:
                        textbutton _("[ev_amidorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm20.hint]")
                if (not ev_amisroom25.hint == "") and not (ev_amisroom25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amisroom25.hint:
                        textbutton _("[ev_amisroom25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amisroom25.hint]")
                if (not ev_amidorm25.hint == "") and not (ev_amidorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm25.hint:
                        textbutton _("[ev_amidorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm25.hint]")

            if Maya.active:
                if (not ev_firsttimeshrine.hint == "") and not (ev_firsttimeshrine.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimeshrine.hint:
                        textbutton _("[ev_firsttimeshrine.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimeshrine), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimeshrine.hint]")
                if (not ev_mayafirsthall.hint == "") and not (ev_mayafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayafirsthall.hint:
                        textbutton _("[ev_mayafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayafirsthall.hint]")
                if (not ev_shrine5.hint == "") and not (ev_shrine5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine5.hint:
                        textbutton _("[ev_shrine5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine5.hint]")
                if (not ev_mayadorm5.hint == "") and not (ev_mayadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm5.hint:
                        textbutton _("[ev_mayadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm5.hint]")
                if (not ev_shrine10.hint == "") and not (ev_shrine10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine10.hint:
                        textbutton _("[ev_shrine10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine10.hint]")
                if (not ev_mayadorm10.hint == "") and not (ev_mayadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm10.hint:
                        textbutton _("[ev_mayadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm10.hint]")
                if (not ev_shrine15.hint == "") and not (ev_shrine15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine15.hint:
                        textbutton _("[ev_shrine15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine15.hint]")
                if (not ev_mayadorm15.hint == "") and not (ev_mayadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm15.hint:
                        textbutton _("[ev_mayadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm15.hint]")
                if (not ev_shrine20.hint == "") and not (ev_shrine20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine20.hint:
                        textbutton _("[ev_shrine20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine20.hint]")
                if (not ev_mayadorm20.hint == "") and not (ev_mayadorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm20.hint:
                        textbutton _("[ev_mayadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm20.hint]")
                if (not ev_shrine25.hint == "") and not (ev_shrine25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine25.hint:
                        textbutton _("[ev_shrine25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine25.hint]")
                if (not ev_mayadorm25.hint == "") and not (ev_mayadorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm25.hint:
                        textbutton _("[ev_mayadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm25.hint]")

            if Chika.active:
                if (not ev_firsttimemall.hint == "") and not (ev_firsttimemall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimemall.hint:
                        textbutton _("[ev_firsttimemall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimemall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimemall.hint]")
                if (not ev_chikafirsthall.hint == "") and not (ev_chikafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikafirsthall.hint:
                        textbutton _("[ev_chikafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikafirsthall.hint]")
                if (not ev_mall5.hint == "") and not (ev_mall5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall5.hint:
                        textbutton _("[ev_mall5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall5.hint]")
                if (not ev_chikadorm5.hint == "") and not (ev_chikadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadorm5.hint:
                        textbutton _("[ev_chikadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadorm5.hint]")
                if (not ev_mall10.hint == "") and not (ev_mall10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall10.hint:
                        textbutton _("[ev_mall10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall10.hint]")
                if (not ev_chikadorm10.hint == "") and not (ev_chikadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadorm10.hint:
                        textbutton _("[ev_chikadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadorm10.hint]")
                if (not ev_chikadorm15.hint == "") and not (ev_chikadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadorm15.hint:
                        textbutton _("[ev_chikadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadorm15.hint]")
                if (not ev_mall15.hint == "") and not (ev_mall15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall15.hint:
                        textbutton _("[ev_mall15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall15.hint]")
                if (not ev_chikadorm20.hint == "") and not (ev_chikadorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadorm20.hint:
                        textbutton _("[ev_chikadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadorm20.hint]")
                if (not ev_mall20.hint == "") and not (ev_mall20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall20.hint:
                        textbutton _("[ev_mall20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall20.hint]")
                if (not ev_day139.hint == "") and not (ev_day139.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day139.hint:
                        textbutton _("[ev_day139.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day139), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day139.hint]")
                if (not ev_chikainvite1.hint == "") and not (ev_chikainvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikainvite1.hint:
                        textbutton _("[ev_chikainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikainvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikainvite1.hint]")
                if (not ev_chikainvite2.hint == "") and not (ev_chikainvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikainvite2.hint:
                        textbutton _("[ev_chikainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikainvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikainvite2.hint]")

            if Yumi.active:
                if (not ev_firsttimestreets.hint == "") and not (ev_firsttimestreets.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimestreets.hint:
                        textbutton _("[ev_firsttimestreets.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimestreets), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimestreets.hint]")
                if (not ev_yumifirsthall.hint == "") and not (ev_yumifirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumifirsthall.hint:
                        textbutton _("[ev_yumifirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumifirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumifirsthall.hint]")
                if (not ev_streets5.hint == "") and not (ev_streets5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets5.hint:
                        textbutton _("[ev_streets5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets5.hint]")
                if (not ev_streets10.hint == "") and not (ev_streets10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets10.hint:
                        textbutton _("[ev_streets10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets10.hint]")
                if (not ev_yumidorm5.hint == "") and not (ev_yumidorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm5.hint:
                        textbutton _("[ev_yumidorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm5.hint]")
                if (not ev_yumidorm10.hint == "") and not (ev_yumidorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm10.hint:
                        textbutton _("[ev_yumidorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm10.hint]")
                if (not ev_yumidorm15.hint == "") and not (ev_yumidorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm15.hint:
                        textbutton _("[ev_yumidorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm15.hint]")
                if (not ev_streets15.hint == "") and not (ev_streets15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets15.hint:
                        textbutton _("[ev_streets15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets15.hint]")
                if (not ev_streets20.hint == "") and not (ev_streets20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets20.hint:
                        textbutton _("[ev_streets20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets20.hint]")
                if (not ev_yumidorm20.hint == "") and not (ev_yumidorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm20.hint:
                        textbutton _("[ev_yumidorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm20.hint]")
                if (not ev_streets25.hint == "") and not (ev_streets25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets25.hint:
                        textbutton _("[ev_streets25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets25.hint]")
                if (not ev_yumidorm25.hint == "") and not (ev_yumidorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm25.hint:
                        textbutton _("[ev_yumidorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm25.hint]")

            if Ayane.active:
                if (not ev_firsttimedojo.hint == "") and not (ev_firsttimedojo.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimedojo.hint:
                        textbutton _("[ev_firsttimedojo.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimedojo), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimedojo.hint]")
                    text ("")
                if (not ev_ayanefirsthall.hint == "") and not (ev_ayanefirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanefirsthall.hint:
                        textbutton _("[ev_ayanefirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanefirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanefirsthall.hint]")
                if (not ev_dojo5.hint == "") and not (ev_dojo5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo5.hint:
                        textbutton _("[ev_dojo5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo5.hint]")
                if (not ev_dojo10.hint == "") and not (ev_dojo10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo10.hint:
                        textbutton _("[ev_dojo10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo10.hint]")
                if (not ev_ayanedorm5.hint == "") and not (ev_ayanedorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm5.hint:
                        textbutton _("[ev_ayanedorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm5.hint]")
                if (not ev_ayanenew1.hint == "") and not (ev_ayanenew1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanenew1.hint:
                        textbutton _("[ev_ayanenew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanenew1.hint]")
                if (not ev_ayanenew2.hint == "") and not (ev_ayanenew2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanenew2.hint:
                        textbutton _("[ev_ayanenew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanenew2.hint]")
                if (not ev_ayanenew3.hint == "") and not (ev_ayanenew3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanenew3.hint:
                        textbutton _("[ev_ayanenew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanenew3.hint]")
                    text ("")
                if (not ev_ayanedorm10.hint == "") and not (ev_ayanedorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm10.hint:
                        textbutton _("[ev_ayanedorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm10.hint]")
                if (not ev_ayanedorm15.hint == "") and not (ev_ayanedorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm15.hint:
                        textbutton _("[ev_ayanedorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm15.hint]")
                if (not ev_day68.hint == "") and not (ev_day68.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day68.hint:
                        textbutton _("[ev_day68.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day68), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day68.hint]")
                if (not ev_dojo20.hint == "") and not (ev_dojo20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo20.hint:
                        textbutton _("[ev_dojo20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo20.hint]")
                if (not ev_ayanedorm20.hint == "") and not (ev_ayanedorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm20.hint:
                        textbutton _("[ev_ayanedorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm20.hint]")
                if (not ev_ayanelust10.hint == "") and not (ev_ayanelust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanelust10.hint:
                        textbutton _("[ev_ayanelust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanelust10.hint]")
                if (not ev_dojo25.hint == "") and not (ev_dojo25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo25.hint:
                        textbutton _("[ev_dojo25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo25.hint]")
                if (not ev_ayanedorm25.hint == "") and not (ev_ayanedorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm25.hint:
                        textbutton _("[ev_ayanedorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm25.hint]")
                    text ("")
                if (not ev_dojo30.hint == "") and not (ev_dojo30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo30.hint:
                        textbutton _("[ev_dojo30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo30.hint]")
                if (not ev_ayanedorm30.hint == "") and not (ev_ayanedorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm30.hint:
                        textbutton _("[ev_ayanedorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm30.hint]")

            if Sana.active:
                if (not ev_firsttimebar.hint == "") and not (ev_firsttimebar.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimebar.hint:
                        textbutton _("[ev_firsttimebar.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimebar), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimebar.hint]")
                if (not ev_sanafirsthall.hint == "") and not (ev_sanafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanafirsthall.hint:
                        textbutton _("[ev_sanafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanafirsthall.hint]")
                if (not ev_bar5.hint == "") and not (ev_bar5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar5.hint:
                        textbutton _("[ev_bar5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar5.hint]")
                if (not ev_sanadorm5.hint == "") and not (ev_sanadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm5.hint:
                        textbutton _("[ev_sanadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm5.hint]")
                if (not ev_bar10.hint == "") and not (ev_bar10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar10.hint:
                        textbutton _("[ev_bar10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar10.hint]")
                if (not ev_sanadorm10.hint == "") and not (ev_sanadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm10.hint:
                        textbutton _("[ev_sanadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm10.hint]")
                if (not ev_bar15.hint == "") and not (ev_bar15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar15.hint:
                        textbutton _("[ev_bar15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar15.hint]")
                if (not ev_sanadorm15.hint == "") and not (ev_sanadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm15.hint:
                        textbutton _("[ev_sanadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm15.hint]")
                if (not ev_bar20.hint == "") and not (ev_bar20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar20.hint:
                        textbutton _("[ev_bar20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar20.hint]")
                if (not ev_sanadorm20.hint == "") and not (ev_sanadorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm20.hint:
                        textbutton _("[ev_sanadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm20.hint]")
                if (not ev_bar25.hint == "") and not (ev_bar25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar25.hint:
                        textbutton _("[ev_bar25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar25.hint]")
                if (not ev_sanadorm25.hint == "") and not (ev_sanadorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm25.hint:
                        textbutton _("[ev_sanadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm25.hint]")
                if (not ev_bar30.hint == "") and not (ev_bar30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar30.hint:
                        textbutton _("[ev_bar30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar30.hint]")
                if (not ev_sanadorm30.hint == "") and not (ev_sanadorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm30.hint:
                        textbutton _("[ev_sanadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm30.hint]")
                    text ("")

            if Makoto.active:
                if (not ev_firsttimepornshop.hint == "") and not (ev_firsttimepornshop.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimepornshop.hint:
                        textbutton _("[ev_firsttimepornshop.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimepornshop), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimepornshop.hint]")
                if (not ev_makotofirsthall.hint == "") and not (ev_makotofirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotofirsthall.hint:
                        textbutton _("[ev_makotofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotofirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotofirsthall.hint]")
                if (not ev_pornshop5.hint == "") and not (ev_pornshop5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_pornshop5.hint:
                        textbutton _("[ev_pornshop5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_pornshop5.hint]")
                if (not ev_makotodorm5.hint == "") and not (ev_makotodorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotodorm5.hint:
                        textbutton _("[ev_makotodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotodorm5.hint]")
                if (not ev_pornshop10.hint == "") and not (ev_pornshop10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_pornshop10.hint:
                        textbutton _("[ev_pornshop10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_pornshop10.hint]")
                if (not ev_makotonew1.hint == "") and not (ev_makotonew1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotonew1.hint:
                        textbutton _("[ev_makotonew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotonew1.hint]")
                if (not ev_makotonew2.hint == "") and not (ev_makotonew2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotonew2.hint:
                        textbutton _("[ev_makotonew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotonew2.hint]")
                if (not ev_makotonew3.hint == "") and not (ev_makotonew3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotonew3.hint:
                        textbutton _("[ev_makotonew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotonew3.hint]")
                if (not ev_pornshop15.hint == "") and not (ev_pornshop15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_pornshop15.hint:
                        textbutton _("[ev_pornshop15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_pornshop15.hint]")
                if (not ev_makotolust5.hint == "") and not (ev_makotolust5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotolust5.hint:
                        textbutton _("[ev_makotolust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotolust5.hint]")
                if (not ev_makotoinvite1.hint == "") and not (ev_makotoinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotoinvite1.hint:
                        textbutton _("[ev_makotoinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotoinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotoinvite1.hint]")
                if (not ev_makotoinvite2.hint == "") and not (ev_makotoinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotoinvite2.hint:
                        textbutton _("[ev_makotoinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotoinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotoinvite2.hint]")
                if (not ev_pornshop20.hint == "") and not (ev_pornshop20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_pornshop20.hint:
                        textbutton _("[ev_pornshop20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_pornshop20.hint]")
                if (not ev_makotodorm20.hint == "") and not (ev_makotodorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotodorm20.hint:
                        textbutton _("[ev_makotodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotodorm20.hint]")
                if (not ev_pornshop25.hint == "") and not (ev_pornshop25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_pornshop25.hint:
                        textbutton _("[ev_pornshop25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_pornshop25.hint]")
                if (not ev_makotodorm25.hint == "") and not (ev_makotodorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotodorm25.hint:
                        textbutton _("[ev_makotodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotodorm25.hint]")

            if Miku.active:
                if (not ev_firsttimesoccerfield.hint == "") and not (ev_firsttimesoccerfield.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimesoccerfield.hint:
                        textbutton _("[ev_firsttimesoccerfield.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimesoccerfield), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimesoccerfield.hint]")
                if (not ev_mikufirsthall.hint == "") and not (ev_mikufirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikufirsthall.hint:
                        textbutton _("[ev_mikufirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikufirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikufirsthall.hint]")
                if (not ev_soccer5.hint == "") and not (ev_soccer5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer5.hint:
                        textbutton _("[ev_soccer5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer5.hint]")
                if (not ev_mikudorm5.hint == "") and not (ev_mikudorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm5.hint:
                        textbutton _("[ev_mikudorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm5.hint]")
                if (not ev_soccer10.hint == "") and not (ev_soccer10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer10.hint:
                        textbutton _("[ev_soccer10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer10.hint]")
                if (not ev_mikudorm10.hint == "") and not (ev_mikudorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm10.hint:
                        textbutton _("[ev_mikudorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm10.hint]")
                if (not ev_soccer15.hint == "") and not (ev_soccer15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer15.hint:
                        textbutton _("[ev_soccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer15.hint]")
                if (not ev_mikudorm15.hint == "") and not (ev_mikudorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm15.hint:
                        textbutton _("[ev_mikudorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm15.hint]")
                if (not ev_soccer20.hint == "") and not (ev_soccer20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer20.hint:
                        textbutton _("[ev_soccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer20.hint]")
                if (not ev_soccer25.hint == "") and not (ev_soccer25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer25.hint:
                        textbutton _("[ev_soccer25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer25.hint]")
                if (not ev_mikudorm25.hint == "") and not (ev_mikudorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm25.hint:
                        textbutton _("[ev_mikudorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm25.hint]")
                if (not ev_soccer30.hint == "") and not (ev_soccer30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer30.hint:
                        textbutton _("[ev_soccer30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer30.hint]")
                if (not ev_mikudorm30.hint == "") and not (ev_mikudorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm30.hint:
                        textbutton _("[ev_mikudorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm30.hint]")

            if Futaba.active:
                if (not ev_firsttimelibrary.hint == "") and not (ev_firsttimelibrary.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimelibrary.hint:
                        textbutton _("[ev_firsttimelibrary.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimelibrary), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimelibrary.hint]")
                if (not ev_futabafall.hint == "") and not (ev_futabafall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabafall.hint:
                        textbutton _("[ev_futabafall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabafall.hint]")
                if (not ev_library10.hint == "") and not (ev_library10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library10.hint:
                        textbutton _("[ev_library10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library10.hint]")
                if (not ev_futabafirsthall.hint == "") and not (ev_futabafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabafirsthall.hint:
                        textbutton _("[ev_futabafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabafirsthall.hint]")
                if (not ev_futabafirstvisit.hint == "") and not (ev_futabafirstvisit.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabafirstvisit.hint:
                        textbutton _("[ev_futabafirstvisit.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafirstvisit), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabafirstvisit.hint]")
                if (not ev_futabadorm10.hint == "") and not (ev_futabadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm10.hint:
                        textbutton _("[ev_futabadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm10.hint]")
                if (not ev_library15.hint == "") and not (ev_library15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library15.hint:
                        textbutton _("[ev_library15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library15.hint]")
                if (not ev_futabanew1.hint == "") and not (ev_futabanew1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabanew1.hint:
                        textbutton _("[ev_futabanew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabanew1.hint]")
                if (not ev_futabanew2.hint == "") and not (ev_futabanew2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabanew2.hint:
                        textbutton _("[ev_futabanew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabanew2.hint]")
                if (not ev_futabanew3.hint == "") and not (ev_futabanew3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabanew3.hint:
                        textbutton _("[ev_futabanew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabanew3.hint]")
                if (not ev_futabadorm15.hint == "") and not (ev_futabadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm15.hint:
                        textbutton _("[ev_futabadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm15.hint]")
                if (not ev_library20.hint == "") and not (ev_library20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library20.hint:
                        textbutton _("[ev_library20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library20.hint]")
                if (not ev_library25.hint == "") and not (ev_library25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library25.hint:
                        textbutton _("[ev_library25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library25.hint]")
                if (not ev_futabadorm25.hint == "") and not (ev_futabadorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm25.hint:
                        textbutton _("[ev_futabadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm25.hint]")
                if (not ev_day86.hint == "") and not (ev_day86.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day86.hint:
                        textbutton _("[ev_day86.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day86), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day86.hint]")
                if (not ev_library30.hint == "") and not (ev_library30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library30.hint:
                        textbutton _("[ev_library30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library30.hint]")
                if (not ev_futabadorm30.hint == "") and not (ev_futabadorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm30.hint:
                        textbutton _("[ev_futabadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm30.hint]")
                if (not ev_library35.hint == "") and not (ev_library35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library35.hint:
                        textbutton _("[ev_library35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library35.hint]")
                if (not ev_futabadorm35.hint == "") and not (ev_futabadorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm35.hint:
                        textbutton _("[ev_futabadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm35.hint]")

            if Rin.active:
                if (not ev_firsttimecafe.hint == "") and not (ev_firsttimecafe.hint == "Event will trigger automatically."):
                    if "(!)" in ev_firsttimecafe.hint:
                        textbutton _("[ev_firsttimecafe.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimecafe), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_firsttimecafe.hint]")
                if (not ev_cafesugar.hint == "") and not (ev_cafesugar.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafesugar.hint:
                        textbutton _("[ev_cafesugar.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafesugar), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafesugar.hint]")
                if (not ev_cafe10.hint == "") and not (ev_cafe10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe10.hint:
                        textbutton _("[ev_cafe10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe10.hint]")
                if (not ev_rinfirsthall.hint == "") and not (ev_rinfirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rinfirsthall.hint:
                        textbutton _("[ev_rinfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinfirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rinfirsthall.hint]")
                if (not ev_rinfirstvisit.hint == "") and not (ev_rinfirstvisit.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rinfirstvisit.hint:
                        textbutton _("[ev_rinfirstvisit.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinfirstvisit), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rinfirstvisit.hint]")
                if (not ev_rindorm10.hint == "") and not (ev_rindorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm10.hint:
                        textbutton _("[ev_rindorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm10.hint]")
                if (not ev_cafe15.hint == "") and not (ev_cafe15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe15.hint:
                        textbutton _("[ev_cafe15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe15.hint]")
                if (not ev_rindorm15.hint == "") and not (ev_rindorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm15.hint:
                        textbutton _("[ev_rindorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm15.hint]")
                if (not ev_cafe20.hint == "") and not (ev_cafe20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe20.hint:
                        textbutton _("[ev_cafe20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe20.hint]")
                if (not ev_rindorm20.hint == "") and not (ev_rindorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm20.hint:
                        textbutton _("[ev_rindorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm20.hint]")
                if (not ev_cafe25.hint == "") and not (ev_cafe25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe25.hint:
                        textbutton _("[ev_cafe25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe25.hint]")
                if (not ev_rindorm25.hint == "") and not (ev_rindorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm25.hint:
                        textbutton _("[ev_rindorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm25.hint]")
                if (not ev_cafe30.hint == "") and not (ev_cafe30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe30.hint:
                        textbutton _("[ev_cafe30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe30.hint]")
                if (not ev_rindorm30.hint == "") and not (ev_rindorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm30.hint:
                        textbutton _("[ev_rindorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm30.hint]")
                if (not ev_rindorm35.hint == "") and not (ev_rindorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm35.hint:
                        textbutton _("[ev_rindorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm35.hint]")
                if (not ev_cafe35.hint == "") and not (ev_cafe35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe35.hint:
                        textbutton _("[ev_cafe35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe35.hint]")

            if Molly.active:
                if (not ev_mollycafe1.hint == "") and not (ev_mollycafe1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe1.hint:
                        textbutton _("[ev_mollycafe1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe1.hint]")
                if (not ev_mollyfirsthall.hint == "") and not (ev_mollyfirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollyfirsthall.hint:
                        textbutton _("[ev_mollyfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyfirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollyfirsthall.hint]")
                if (not ev_mollycafe5.hint == "") and not (ev_mollycafe5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe5.hint:
                        textbutton _("[ev_mollycafe5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe5.hint]")
                if (not ev_mollydorm5.hint == "") and not (ev_mollydorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm5.hint:
                        textbutton _("[ev_mollydorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm5.hint]")
                if (not ev_mollycafe10.hint == "") and not (ev_mollycafe10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe10.hint:
                        textbutton _("[ev_mollycafe10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe10.hint]")
                if (not ev_mollydorm10.hint == "") and not (ev_mollydorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm10.hint:
                        textbutton _("[ev_mollydorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm10.hint]")

            if Tsuneyo.active:
                if (not ev_ramen1.hint == "") and not (ev_ramen1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen1.hint:
                        textbutton _("[ev_ramen1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen1.hint]")
                if (not ev_tsuneyofirsthall.hint == "") and not (ev_tsuneyofirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyofirsthall.hint:
                        textbutton _("[ev_tsuneyofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyofirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyofirsthall.hint]")
                if (not ev_ramen5.hint == "") and not (ev_ramen5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen5.hint:
                        textbutton _("[ev_ramen5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen5.hint]")
                    text ("")
                if (not ev_tsuneyodorm5.hint == "") and not (ev_tsuneyodorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyodorm5.hint:
                        textbutton _("[ev_tsuneyodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyodorm5.hint]")
                if (not ev_ramen10.hint == "") and not (ev_ramen10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen10.hint:
                        textbutton _("[ev_ramen10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen10.hint]")
                if (not ev_tsuneyodorm10.hint == "") and not (ev_tsuneyodorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyodorm10.hint:
                        textbutton _("[ev_tsuneyodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyodorm10.hint]")

            if Sara.active:
                if (not ev_saradate1.hint == "") and not (ev_saradate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saradate1.hint:
                        textbutton _("[ev_saradate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saradate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saradate1.hint]")
                if (not ev_saralust5.hint == "") and not (ev_saralust5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saralust5.hint:
                        textbutton _("[ev_saralust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saralust5.hint]")
                if (not ev_sarainvite1.hint == "") and not (ev_sarainvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarainvite1.hint:
                        textbutton _("[ev_sarainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarainvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarainvite1.hint]")
                if (not ev_sarainvite2.hint == "") and not (ev_sarainvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarainvite2.hint:
                        textbutton _("[ev_sarainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarainvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarainvite2.hint]")
                if (not ev_saralust10.hint == "") and not (ev_saralust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saralust10.hint:
                        textbutton _("[ev_saralust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saralust10.hint]")

            if Haruka.active:
                if (not ev_harukadate1.hint == "") and not (ev_harukadate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate1.hint:
                        textbutton _("[ev_harukadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate1.hint]")
                if (not ev_harukadate5.hint == "") and not (ev_harukadate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate5.hint:
                        textbutton _("[ev_harukadate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate5.hint]")
                if (not ev_harukafirstlust.hint == "") and not (ev_harukafirstlust.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukafirstlust.hint:
                        textbutton _("[ev_harukafirstlust.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukafirstlust), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukafirstlust.hint]")
                if (not ev_harukalust10.hint == "") and not (ev_harukalust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukalust10.hint:
                        textbutton _("[ev_harukalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukalust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukalust10.hint]")
                if (not ev_harukadate10.hint == "") and not (ev_harukadate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate10.hint:
                        textbutton _("[ev_harukadate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate10.hint]")
                if (not ev_harukadate15.hint == "") and not (ev_harukadate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate15.hint:
                        textbutton _("[ev_harukadate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate15.hint]")

            if Maki.active:
                if (not ev_makidate1.hint == "") and not (ev_makidate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makidate1.hint:
                        textbutton _("[ev_makidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makidate1.hint]")
                if (not ev_makidate5.hint == "") and not (ev_makidate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makidate5.hint:
                        textbutton _("[ev_makidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makidate5.hint]")
                    text ("")

            if Kirin.active:
                if (not ev_kirindate1.hint == "") and not (ev_kirindate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindate1.hint:
                        textbutton _("[ev_kirindate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindate1.hint]")
                if (not ev_kirindate5.hint == "") and not (ev_kirindate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindate5.hint:
                        textbutton _("[ev_kirindate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindate5.hint]")
                if (not ev_kirindate10.hint == "") and not (ev_kirindate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindate10.hint:
                        textbutton _("[ev_kirindate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindate10.hint]")

            if Karin.active:
                if (not ev_karindate1.hint == "") and not (ev_karindate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate1.hint:
                        textbutton _("[ev_karindate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate1.hint]")
                if (not ev_karindate5.hint == "") and not (ev_karindate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate5.hint:
                        textbutton _("[ev_karindate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate5.hint]")
                if (not ev_karindate10.hint == "") and not (ev_karindate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate10.hint:
                        textbutton _("[ev_karindate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate10.hint]")

            if Kaori.active:
                if (not ev_kaoridate1.hint == "") and not (ev_kaoridate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate1.hint:
                        textbutton _("[ev_kaoridate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate1.hint]")
                if (not ev_kaoridate5.hint == "") and not (ev_kaoridate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate5.hint:
                        textbutton _("[ev_kaoridate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate5.hint]")
                if (not ev_kaoridate10.hint == "") and not (ev_kaoridate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate10.hint:
                        textbutton _("[ev_kaoridate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate10.hint]")

            if Chinami.active:
                if (not ev_chinamidate1.hint == "") and not (ev_chinamidate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate1.hint:
                        textbutton _("[ev_chinamidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate1.hint]")
                if (not ev_chinamidate5.hint == "") and not (ev_chinamidate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate5.hint:
                        textbutton _("[ev_chinamidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate5.hint]")

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            textbutton _("Back") action ShowMenu("progressmod")
