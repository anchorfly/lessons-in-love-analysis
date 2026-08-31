screen hinttracker2():

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


        if HappyEvent.active:
            if (not ev_lesson1.hint == "") and not (ev_lesson1.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
                text ("")
            if (not ev_goodboy.hint == "") and not (ev_goodboy.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_lamblegs.hint == "") and not (ev_lamblegs.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"

        if Ami.active:
            if (not ev_amiinvite1.hint == "") and not (ev_amiinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_amiinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amiinvite2.hint == "") and not (ev_amiinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_amiinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amiinvite3.hint == "") and not (ev_amiinvite3.hint == "Event will trigger automatically."):
                textbutton _("[ev_amiinvite3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amimaid30.hint == "") and not (ev_amimaid30.hint == "Event will trigger automatically."):
                textbutton _("[ev_amimaid30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidate35.hint == "") and not (ev_amidate35.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidate35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidorm40.hint == "") and not (ev_amidorm40.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidorm40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amilust15.hint == "") and not (ev_amilust15.hint == "Event will trigger automatically."):
                textbutton _("[ev_amilust15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amilust20.hint == "") and not (ev_amilust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_amilust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidate50.hint == "") and not (ev_amidate50.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidate50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidate50p2.hint == "") and not (ev_amidate50p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidate50p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidate50p3.hint == "") and not (ev_amidate50p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidate50p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amidate50p4.hint == "") and not (ev_amidate50p4.hint == "Event will trigger automatically."):
                textbutton _("[ev_amidate50p4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"

        if Maya.active:
            if (not ev_mayadorm30.hint == "") and not (ev_mayadorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_shrine30.hint == "") and not (ev_shrine30.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadorm35.hint == "") and not (ev_mayadorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
                text ("")
            if (not ev_shrine35.hint == "") and not (ev_shrine35.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayafestival1.hint == "") and not (ev_mayafestival1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayafestival1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayafestival2.hint == "") and not (ev_mayafestival2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayafestival2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
                text ("")
            if (not ev_mayafestival3.hint == "") and not (ev_mayafestival3.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayafestival3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayafestival4.hint == "") and not (ev_mayafestival4.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayafestival4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"

        if Chika.active:
            if (not ev_chikalust10.hint == "") and not (ev_chikalust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikalust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaonsen1.hint == "") and not (ev_chikaonsen1.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaonsen1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaonsen2.hint == "") and not (ev_chikaonsen2.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaonsen2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaonsen3.hint == "") and not (ev_chikaonsen3.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaonsen3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaonsen4.hint == "") and not (ev_chikaonsen4.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaonsen4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikalust15.hint == "") and not (ev_chikalust15.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikalust15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikalust20.hint == "") and not (ev_chikalust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikalust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaspecial40.hint == "") and not (ev_chikaspecial40.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaspecial40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall40.hint == "") and not (ev_mall40.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall40p2.hint == "") and not (ev_mall40p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall40p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadate45.hint == "") and not (ev_chikadate45.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadate45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"

        if Yumi.active:
            if (not ev_streets30.hint == "") and not (ev_streets30.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm30.hint == "") and not (ev_yumidorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumidorm35.hint == "") and not (ev_yumidorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumidorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumicallnight35.hint == "") and not (ev_yumicallnight35.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumicallnight35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumispecial40.hint == "") and not (ev_yumispecial40.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumispecial40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumispecial40p2.hint == "") and not (ev_yumispecial40p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumispecial40p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_streets40.hint == "") and not (ev_streets40.hint == "Event will trigger automatically."):
                textbutton _("[ev_streets40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumispecial45.hint == "") and not (ev_yumispecial45.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumispecial45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"

        if Ayane.active:
            if (not ev_ayaneinvite1.hint == "") and not (ev_ayaneinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayaneinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayaneinvite2.hint == "") and not (ev_ayaneinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayaneinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanelust15.hint == "") and not (ev_ayanelust15.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanelust15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_dojo35.hint == "") and not (ev_dojo35.hint == "Event will trigger automatically."):
                textbutton _("[ev_dojo35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanedorm35.hint == "") and not (ev_ayanedorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanedorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanespecial1.hint == "") and not (ev_ayanespecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanespecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanespecial2.hint == "") and not (ev_ayanespecial2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanespecial2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanelust20.hint == "") and not (ev_ayanelust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanelust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"

        if Sana.active:
            if (not ev_bar35.hint == "") and not (ev_bar35.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm35.hint == "") and not (ev_sanadorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar40.hint == "") and not (ev_bar40.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm40.hint == "") and not (ev_sanadorm40.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar45.hint == "") and not (ev_bar45.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_sanadorm45.hint == "") and not (ev_sanadorm45.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
                text ("")
            if (not ev_sanadorm50.hint == "") and not (ev_sanadorm50.hint == "Event will trigger automatically."):
                textbutton _("[ev_sanadorm50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_bar50.hint == "") and not (ev_bar50.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"

        if Makoto.active:
            if (not ev_makotolust10.hint == "") and not (ev_makotolust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotolust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotowinterbeach1.hint == "") and not (ev_makotowinterbeach1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotowinterbeach1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotowinterbeach2.hint == "") and not (ev_makotowinterbeach2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotowinterbeach2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotowinterbeach3.hint == "") and not (ev_makotowinterbeach3.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotowinterbeach3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotowinterbeach4.hint == "") and not (ev_makotowinterbeach4.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotowinterbeach4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotolust20.hint == "") and not (ev_makotolust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotolust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"

        if Miku.active:
            if (not ev_soccer35.hint == "") and not (ev_soccer35.hint == "Event will trigger automatically."):
                textbutton _("[ev_soccer35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikuwinterbeach1.hint == "") and not (ev_mikuwinterbeach1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikuwinterbeach1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm35.hint == "") and not (ev_mikudorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm40.hint == "") and not (ev_mikudorm40.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm45.hint == "") and not (ev_mikudorm45.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm45p2.hint == "") and not (ev_mikudorm45p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm45p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikuspecial50.hint == "") and not (ev_mikuspecial50.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikuspecial50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm50.hint == "") and not (ev_mikudorm50.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
                text ("")

        if Futaba.active:
            if (not ev_futabalust10.hint == "") and not (ev_futabalust10.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabalust10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabainvite1.hint == "") and not (ev_futabainvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabainvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabainvite2.hint == "") and not (ev_futabainvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabainvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabalust15.hint == "") and not (ev_futabalust15.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabalust15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm40.hint == "") and not (ev_futabadorm40.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library40.hint == "") and not (ev_library40.hint == "Event will trigger automatically."):
                textbutton _("[ev_library40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library40part2.hint == "") and not (ev_library40part2.hint == "Event will trigger automatically."):
                textbutton _("[ev_library40part2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabadorm45.hint == "") and not (ev_futabadorm45.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"

        if Rin.active:
            if (not ev_cafe40.hint == "") and not (ev_cafe40.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm40.hint == "") and not (ev_rindorm40.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe45.hint == "") and not (ev_cafe45.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm45.hint == "") and not (ev_rindorm45.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_cafe50.hint == "") and not (ev_cafe50.hint == "Event will trigger automatically."):
                textbutton _("[ev_cafe50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
                text ("")
            if (not ev_rindorm50.hint == "") and not (ev_rindorm50.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
                text ("")
            if (not ev_rindorm50special.hint == "") and not (ev_rindorm50special.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm50special.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindate50.hint == "") and not (ev_rindate50.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindate50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"

        if Molly.active:
            if (not ev_mollycafe15.hint == "") and not (ev_mollycafe15.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm15.hint == "") and not (ev_mollydorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe20.hint == "") and not (ev_mollycafe20.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm20.hint == "") and not (ev_mollydorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe25.hint == "") and not (ev_mollycafe25.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe25p2.hint == "") and not (ev_mollycafe25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm25.hint == "") and not (ev_mollydorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydorm30.hint == "") and not (ev_mollydorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"

        if Tsuneyo.active:
            if (not ev_ramen15.hint == "") and not (ev_ramen15.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyodorm15.hint == "") and not (ev_tsuneyodorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyodorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyodorm20.hint == "") and not (ev_tsuneyodorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyodorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
                text ("")
            if (not ev_ramen20.hint == "") and not (ev_ramen20.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_ramen25.hint == "") and not (ev_ramen25.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_ramen25p2.hint == "") and not (ev_ramen25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyodorm25.hint == "") and not (ev_tsuneyodorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyodorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_ramen30.hint == "") and not (ev_ramen30.hint == "Event will trigger automatically."):
                textbutton _("[ev_ramen30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"

        if Sara.active:
            if (not ev_saradate10.hint == "") and not (ev_saradate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_saradate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarabar20.hint == "") and not (ev_sarabar20.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarabar20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarabar25.hint == "") and not (ev_sarabar25.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarabar25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarabar25p2.hint == "") and not (ev_sarabar25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarabar25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
                text ("")
            if (not ev_saralust20.hint == "") and not (ev_saralust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_saralust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"

        if Haruka.active:
            if (not ev_harukainvite1.hint == "") and not (ev_harukainvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukainvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukainvite2.hint == "") and not (ev_harukainvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukainvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukadate20.hint == "") and not (ev_harukadate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukainvite3.hint == "") and not (ev_harukainvite3.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukainvite3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"

        if Maki.active:
            if (not ev_makidate10.hint == "") and not (ev_makidate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_makidate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makiday351.hint == "") and not (ev_makiday351.hint == "Event will trigger automatically."):
                textbutton _("[ev_makiday351.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makidate15.hint == "") and not (ev_makidate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_makidate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makiinvite1.hint == "") and not (ev_makiinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makiinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makiinvite2.hint == "") and not (ev_makiinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makiinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"

        if Kirin.active:
            if (not ev_kirinlust5.hint == "") and not (ev_kirinlust5.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinlust5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirininvite1.hint == "") and not (ev_kirininvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirininvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirininvite2.hint == "") and not (ev_kirininvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirininvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinfirsthall.hint == "") and not (ev_kirinfirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinfirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindorm10.hint == "") and not (ev_kirindorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinsoccer15.hint == "") and not (ev_kirinsoccer15.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinsoccer15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinsoccer20.hint == "") and not (ev_kirinsoccer20.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinsoccer20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindorm15.hint == "") and not (ev_kirindorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindorm20.hint == "") and not (ev_kirindorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindate25.hint == "") and not (ev_kirindate25.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindate25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinlust20.hint == "") and not (ev_kirinlust20.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinlust20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinspecial25.hint == "") and not (ev_kirinspecial25.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinspecial25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirindorm25.hint == "") and not (ev_kirindorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirindorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinsoccer25.hint == "") and not (ev_kirinsoccer25.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinsoccer25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinspecial30.hint == "") and not (ev_kirinspecial30.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinspecial30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinlust202.hint == "") and not (ev_kirinlust202.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinlust202.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"

        if Karin.active:
            if (not ev_karindate15.hint == "") and not (ev_karindate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karinsoccer15.hint == "") and not (ev_karinsoccer15.hint == "Event will trigger automatically."):
                textbutton _("[ev_karinsoccer15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karinsoccer20.hint == "") and not (ev_karinsoccer20.hint == "Event will trigger automatically."):
                textbutton _("[ev_karinsoccer20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karindate20.hint == "") and not (ev_karindate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"

        if Kaori.active:
            if (not ev_kaoridate15.hint == "") and not (ev_kaoridate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate15p2.hint == "") and not (ev_kaoridate15p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate15p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate15p3.hint == "") and not (ev_kaoridate15p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate15p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate20.hint == "") and not (ev_kaoridate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate25.hint == "") and not (ev_kaoridate25.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"

        if Chinami.active:
            if (not ev_chinamidate10.hint == "") and not (ev_chinamidate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_chinamidate15.hint == "") and not (ev_chinamidate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_chinamidate20.hint == "") and not (ev_chinamidate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_christmas1.hint == "") and not (ev_christmas1.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas2.hint == "") and not (ev_christmas2.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas3.hint == "") and not (ev_christmas3.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas4.hint == "") and not (ev_christmas4.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas5.hint == "") and not (ev_christmas5.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas6.hint == "") and not (ev_christmas6.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmas7.hint == "") and not (ev_christmas7.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmas7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_day237.hint == "") and not (ev_day237.hint == "Event will trigger automatically."):
                textbutton _("[ev_day237.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day239.hint == "") and not (ev_day239.hint == "Event will trigger automatically."):
                textbutton _("[ev_day239.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day240.hint == "") and not (ev_day240.hint == "Event will trigger automatically."):
                textbutton _("[ev_day240.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day244.hint == "") and not (ev_day244.hint == "Event will trigger automatically."):
                textbutton _("[ev_day244.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day246.hint == "") and not (ev_day246.hint == "Event will trigger automatically."):
                textbutton _("[ev_day246.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_day247.hint == "") and not (ev_day247.hint == "Event will trigger automatically."):
                textbutton _("[ev_day247.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day261.hint == "") and not (ev_day261.hint == "Event will trigger automatically."):
                textbutton _("[ev_day261.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day263.hint == "") and not (ev_day263.hint == "Event will trigger automatically."):
                textbutton _("[ev_day263.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day264.hint == "") and not (ev_day264.hint == "Event will trigger automatically."):
                textbutton _("[ev_day264.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day269.hint == "") and not (ev_day269.hint == "Event will trigger automatically."):
                textbutton _("[ev_day269.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day270.hint == "") and not (ev_day270.hint == "Event will trigger automatically."):
                textbutton _("[ev_day270.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day271.hint == "") and not (ev_day271.hint == "Event will trigger automatically."):
                textbutton _("[ev_day271.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day280.hint == "") and not (ev_day280.hint == "Event will trigger automatically."):
                textbutton _("[ev_day280.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day281.hint == "") and not (ev_day281.hint == "Event will trigger automatically."):
                textbutton _("[ev_day281.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day282.hint == "") and not (ev_day282.hint == "Event will trigger automatically."):
                textbutton _("[ev_day282.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day283.hint == "") and not (ev_day283.hint == "Event will trigger automatically."):
                textbutton _("[ev_day283.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day287.hint == "") and not (ev_day287.hint == "Event will trigger automatically."):
                textbutton _("[ev_day287.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day288.hint == "") and not (ev_day288.hint == "Event will trigger automatically."):
                textbutton _("[ev_day288.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day295.hint == "") and not (ev_day295.hint == "Event will trigger automatically."):
                textbutton _("[ev_day295.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day295parttwo.hint == "") and not (ev_day295parttwo.hint == "Event will trigger automatically."):
                textbutton _("[ev_day295parttwo.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day297.hint == "") and not (ev_day297.hint == "Event will trigger automatically."):
                textbutton _("[ev_day297.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day302.hint == "") and not (ev_day302.hint == "Event will trigger automatically."):
                textbutton _("[ev_day302.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day303.hint == "") and not (ev_day303.hint == "Event will trigger automatically."):
                textbutton _("[ev_day303.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day304.hint == "") and not (ev_day304.hint == "Event will trigger automatically."):
                textbutton _("[ev_day304.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_day318.hint == "") and not (ev_day318.hint == "Event will trigger automatically."):
                textbutton _("[ev_day318.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar1.hint == "") and not (ev_dormwar1.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar2.hint == "") and not (ev_dormwar2.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar3.hint == "") and not (ev_dormwar3.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar4.hint == "") and not (ev_dormwar4.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_dormwar5.hint == "") and not (ev_dormwar5.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar6.hint == "") and not (ev_dormwar6.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar7.hint == "") and not (ev_dormwar7.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_dormwar8.hint == "") and not (ev_dormwar8.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar9.hint == "") and not (ev_dormwar9.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar10.hint == "") and not (ev_dormwar10.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar11.hint == "") and not (ev_dormwar11.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_dormwar12.hint == "") and not (ev_dormwar12.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar13.hint == "") and not (ev_dormwar13.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar14.hint == "") and not (ev_dormwar14.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar15.hint == "") and not (ev_dormwar15.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar16.hint == "") and not (ev_dormwar16.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwar17.hint == "") and not (ev_dormwar17.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwar17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day333.hint == "") and not (ev_day333.hint == "Event will trigger automatically."):
                textbutton _("[ev_day333.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day333part2.hint == "") and not (ev_day333part2.hint == "Event will trigger automatically."):
                textbutton _("[ev_day333part2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day340.hint == "") and not (ev_day340.hint == "Event will trigger automatically."):
                textbutton _("[ev_day340.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day344.hint == "") and not (ev_day344.hint == "Event will trigger automatically."):
                textbutton _("[ev_day344.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_thirdreset1.hint == "") and not (ev_thirdreset1.hint == "Event will trigger automatically."):
                textbutton _("[ev_thirdreset1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_thirdreset2.hint == "") and not (ev_thirdreset2.hint == "Event will trigger automatically."):
                textbutton _("[ev_thirdreset2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_thirdreset3.hint == "") and not (ev_thirdreset3.hint == "Event will trigger automatically."):
                textbutton _("[ev_thirdreset3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day351.hint == "") and not (ev_day351.hint == "Event will trigger automatically."):
                textbutton _("[ev_day351.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day355.hint == "") and not (ev_day355.hint == "Event will trigger automatically."):
                textbutton _("[ev_day355.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach1.hint == "") and not (ev_secondbeach1.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach2.hint == "") and not (ev_secondbeach2.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach3.hint == "") and not (ev_secondbeach3.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach4.hint == "") and not (ev_secondbeach4.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach5.hint == "") and not (ev_secondbeach5.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach6.hint == "") and not (ev_secondbeach6.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach7.hint == "") and not (ev_secondbeach7.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_secondbeach8.hint == "") and not (ev_secondbeach8.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_secondbeach9.hint == "") and not (ev_secondbeach9.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach10.hint == "") and not (ev_secondbeach10.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_secondbeach11.hint == "") and not (ev_secondbeach11.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach12.hint == "") and not (ev_secondbeach12.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach13.hint == "") and not (ev_secondbeach13.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach14.hint == "") and not (ev_secondbeach14.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach15.hint == "") and not (ev_secondbeach15.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach16.hint == "") and not (ev_secondbeach16.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach17.hint == "") and not (ev_secondbeach17.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_secondbeach18.hint == "") and not (ev_secondbeach18.hint == "Event will trigger automatically."):
                textbutton _("[ev_secondbeach18.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_halloweentwo1.hint == "") and not (ev_halloweentwo1.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo2.hint == "") and not (ev_halloweentwo2.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo3.hint == "") and not (ev_halloweentwo3.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo4.hint == "") and not (ev_halloweentwo4.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo5.hint == "") and not (ev_halloweentwo5.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo6.hint == "") and not (ev_halloweentwo6.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo7.hint == "") and not (ev_halloweentwo7.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_halloweentwo8.hint == "") and not (ev_halloweentwo8.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo9.hint == "") and not (ev_halloweentwo9.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo10.hint == "") and not (ev_halloweentwo10.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo11.hint == "") and not (ev_halloweentwo11.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo12.hint == "") and not (ev_halloweentwo12.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweentwo13.hint == "") and not (ev_halloweentwo13.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweentwo13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo1.hint == "") and not (ev_christmastwo1.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo2.hint == "") and not (ev_christmastwo2.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_christmastwo3.hint == "") and not (ev_christmastwo3.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo4.hint == "") and not (ev_christmastwo4.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo5.hint == "") and not (ev_christmastwo5.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo6.hint == "") and not (ev_christmastwo6.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo7.hint == "") and not (ev_christmastwo7.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo8.hint == "") and not (ev_christmastwo8.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo9.hint == "") and not (ev_christmastwo9.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo10.hint == "") and not (ev_christmastwo10.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo11.hint == "") and not (ev_christmastwo11.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo12.hint == "") and not (ev_christmastwo12.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo13.hint == "") and not (ev_christmastwo13.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo14.hint == "") and not (ev_christmastwo14.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo15.hint == "") and not (ev_christmastwo15.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo16.hint == "") and not (ev_christmastwo16.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo17.hint == "") and not (ev_christmastwo17.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo18.hint == "") and not (ev_christmastwo18.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo18.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo19.hint == "") and not (ev_christmastwo19.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo19.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_christmastwo20.hint == "") and not (ev_christmastwo20.hint == "Event will trigger automatically."):
                textbutton _("[ev_christmastwo20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_returntosummer1.hint == "") and not (ev_returntosummer1.hint == "Event will trigger automatically."):
                textbutton _("[ev_returntosummer1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_returntosummer2.hint == "") and not (ev_returntosummer2.hint == "Event will trigger automatically."):
                textbutton _("[ev_returntosummer2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_returntosummer3.hint == "") and not (ev_returntosummer3.hint == "Event will trigger automatically."):
                textbutton _("[ev_returntosummer3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")

        if Yuki.active:
            if (not ev_yukidate1.hint == "") and not (ev_yukidate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"
            if (not ev_yukidate5.hint == "") and not (ev_yukidate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"
            if (not ev_yukidate10.hint == "") and not (ev_yukidate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"
            if (not ev_yukidate10p2.hint == "") and not (ev_yukidate10p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate10p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"

        if Wakana.active:
            if (not ev_wakanadate1.hint == "") and not (ev_wakanadate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"
            if (not ev_wakanadate5.hint == "") and not (ev_wakanadate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"

        if Osako.active:
            if (not ev_osakodate1.hint == "") and not (ev_osakodate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_osakodate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")] style "event_button" text_style "osakohint"
            if (not ev_osakodojo1.hint == "") and not (ev_osakodojo1.hint == "Event will trigger automatically."):
                textbutton _("[ev_osakodojo1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")] style "event_button" text_style "osakohint"

        if Tsubasa.active:
            if (not ev_tsubasadate1.hint == "") and not (ev_tsubasadate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsubasadate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasahint"
                text ("")
            if (not ev_tsubasadate1p2.hint == "") and not (ev_tsubasadate1p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsubasadate1p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasahint"

        if Uta.active:
            if (not ev_utafirsthall.hint == "") and not (ev_utafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_utafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid1.hint == "") and not (ev_utamaid1.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid5.hint == "") and not (ev_utamaid5.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm5.hint == "") and not (ev_utadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm10.hint == "") and not (ev_utadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid10.hint == "") and not (ev_utamaid10.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm15.hint == "") and not (ev_utadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid20.hint == "") and not (ev_utamaid20.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
                text ("")
            if (not ev_utadorm20.hint == "") and not (ev_utadorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"

        if Io.active:
            if (not ev_iofirsthall.hint == "") and not (ev_iofirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_iofirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse1.hint == "") and not (ev_bathhouse1.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse5.hint == "") and not (ev_bathhouse5.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iodorm5.hint == "") and not (ev_iodorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_iodorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iodorm10.hint == "") and not (ev_iodorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_iodorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse10.hint == "") and not (ev_bathhouse10.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iodorm15.hint == "") and not (ev_iodorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_iodorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse20.hint == "") and not (ev_bathhouse20.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse20part2.hint == "") and not (ev_bathhouse20part2.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse20part2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"

        if Noriko.active:
            if (not ev_norikofirsthall.hint == "") and not (ev_norikofirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikofirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_convenience1.hint == "") and not (ev_convenience1.hint == "Event will trigger automatically."):
                textbutton _("[ev_convenience1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikodorm5.hint == "") and not (ev_norikodorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_convenience5.hint == "") and not (ev_convenience5.hint == "Event will trigger automatically."):
                textbutton _("[ev_convenience5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikodorm10.hint == "") and not (ev_norikodorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikoinvite1.hint == "") and not (ev_norikoinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikoinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikoinvite2.hint == "") and not (ev_norikoinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikoinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
                text ("")
            if (not ev_norikospecial20.hint == "") and not (ev_norikospecial20.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikospecial20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikodorm20.hint == "") and not (ev_norikodorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_convenience25.hint == "") and not (ev_convenience25.hint == "Event will trigger automatically."):
                textbutton _("[ev_convenience25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikodorm25.hint == "") and not (ev_norikodorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"

        if Niki.active:
            if (not ev_nikidate1.hint == "") and not (ev_nikidate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikidate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikidate5.hint == "") and not (ev_nikidate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikidate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikidate10.hint == "") and not (ev_nikidate10.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikidate10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikidate15.hint == "") and not (ev_nikidate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikidate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikiinvite1.hint == "") and not (ev_nikiinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikiinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikiinvite2.hint == "") and not (ev_nikiinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikiinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"

        if Nodoka.active:
            if (not ev_nodokafirsthall.hint == "") and not (ev_nodokafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokadorm1.hint == "") and not (ev_nodokadorm1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokadorm1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokalibrary1.hint == "") and not (ev_nodokalibrary1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokalibrary1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokalibrary5.hint == "") and not (ev_nodokalibrary5.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokalibrary5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokadorm5.hint == "") and not (ev_nodokadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"

        if Otoha.active:
            if (not ev_otohafirsthall.hint == "") and not (ev_otohafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohadorm1.hint == "") and not (ev_otohadorm1.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohadorm1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
                text ("")
            if (not ev_otohapark1.hint == "") and not (ev_otohapark1.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohapark1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
                text ("")
            if (not ev_otohapark5.hint == "") and not (ev_otohapark5.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohapark5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohadorm5.hint == "") and not (ev_otohadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohapark10.hint == "") and not (ev_otohapark10.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohapark10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohaspecial10.hint == "") and not (ev_otohaspecial10.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohaspecial10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohadorm10.hint == "") and not (ev_otohadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohadorm10p2.hint == "") and not (ev_otohadorm10p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohadorm10p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"

        if Touka.active:
            if (not ev_toukafirsthall.hint == "") and not (ev_toukafirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukafirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukastreets1.hint == "") and not (ev_toukastreets1.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukastreets1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm1.hint == "") and not (ev_toukadorm1.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukastreets5.hint == "") and not (ev_toukastreets5.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukastreets5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm5.hint == "") and not (ev_toukadorm5.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm10.hint == "") and not (ev_toukadorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukaspecial15.hint == "") and not (ev_toukaspecial15.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukaspecial15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukaspecial15p2.hint == "") and not (ev_toukaspecial15p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukaspecial15p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukaspecial15p3.hint == "") and not (ev_toukaspecial15p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukaspecial15p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"

        if Yasu.active:
            if (not ev_yasufirsthall.hint == "") and not (ev_yasufirsthall.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasufirsthall.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
                text ("")
            if (not ev_church1.hint == "") and not (ev_church1.hint == "Event will trigger automatically."):
                textbutton _("[ev_church1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_church5.hint == "") and not (ev_church5.hint == "Event will trigger automatically."):
                textbutton _("[ev_church5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasudorm10.hint == "") and not (ev_yasudorm10.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasudorm10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_church10.hint == "") and not (ev_church10.hint == "Event will trigger automatically."):
                textbutton _("[ev_church10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"

    vbox:
        xpos .33
        ypos .14
        style_prefix "hint"


        if HappyEvent.active:
            if (not ev_lesson1.hint == "") and not (ev_lesson1.hint == "Event will trigger automatically."):
                text ("Something Everyone Knows and ")
                text ("  Ignores ")
            if (not ev_goodboy.hint == "") and not (ev_goodboy.hint == "Event will trigger automatically."):
                text ("Good Boy")
            if (not ev_lamblegs.hint == "") and not (ev_lamblegs.hint == "Event will trigger automatically."):
                text ("Lamb Legs")

        if Ami.active:
            if (not ev_amiinvite1.hint == "") and not (ev_amiinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Living{/color}")
            if (not ev_amiinvite2.hint == "") and not (ev_amiinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Rising to the Challenge{/color}")
            if (not ev_amiinvite3.hint == "") and not (ev_amiinvite3.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Best Friends Forever{/color}")
            if (not ev_amimaid30.hint == "") and not (ev_amimaid30.hint == "Event will trigger automatically."):
                text ("Third Place")
            if (not ev_amidate35.hint == "") and not (ev_amidate35.hint == "Event will trigger automatically."):
                text ("The Big Sleep (Cute Girl Magic)")
            if (not ev_amidorm40.hint == "") and not (ev_amidorm40.hint == "Event will trigger automatically."):
                text ("Heaven for Human Blood")
            if (not ev_amilust15.hint == "") and not (ev_amilust15.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}As Light as Air{/color}")
            if (not ev_amilust20.hint == "") and not (ev_amilust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Conscious or Not{/color}")
            if (not ev_amidate50.hint == "") and not (ev_amidate50.hint == "Event will trigger automatically."):
                text ("Outcry of the Hunted Hare")
            if (not ev_amidate50p2.hint == "") and not (ev_amidate50p2.hint == "Event will trigger automatically."):
                text ("Fruits of the Two Seasons")
            if (not ev_amidate50p3.hint == "") and not (ev_amidate50p3.hint == "Event will trigger automatically."):
                text ("My Life With You")
            if (not ev_amidate50p4.hint == "") and not (ev_amidate50p4.hint == "Event will trigger automatically."):
                text ("Somnambula")

        if Maya.active:
            if (not ev_mayadorm30.hint == "") and not (ev_mayadorm30.hint == "Event will trigger automatically."):
                text ("What it Means to Be Destroyed")
            if (not ev_shrine30.hint == "") and not (ev_shrine30.hint == "Event will trigger automatically."):
                text ("Now More Than Ever")
            if (not ev_mayadorm35.hint == "") and not (ev_mayadorm35.hint == "Event will trigger automatically."):
                text ("A Place That Can Only Exist in ")
                text ("  Our Minds ")
            if (not ev_shrine35.hint == "") and not (ev_shrine35.hint == "Event will trigger automatically."):
                text ("Stop Looking For Answers")
            if (not ev_mayafestival1.hint == "") and not (ev_mayafestival1.hint == "Event will trigger automatically."):
                text ("Somewhere Inside of a Dream")
            if (not ev_mayafestival2.hint == "") and not (ev_mayafestival2.hint == "Event will trigger automatically."):
                text ("Three Halves Make a Whole ")
                text ("  (Itadakimasu) ")
            if (not ev_mayafestival3.hint == "") and not (ev_mayafestival3.hint == "Event will trigger automatically."):
                text ("As The Sun Disappears")
            if (not ev_mayafestival4.hint == "") and not (ev_mayafestival4.hint == "Event will trigger automatically."):
                text ("Everlasting Mercy")

        if Chika.active:
            if (not ev_chikalust10.hint == "") and not (ev_chikalust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Baby it's Cold Outside{/color}")
            if (not ev_chikaonsen1.hint == "") and not (ev_chikaonsen1.hint == "Event will trigger automatically."):
                text ("Little Miracles")
            if (not ev_chikaonsen2.hint == "") and not (ev_chikaonsen2.hint == "Event will trigger automatically."):
                text ("Bleed")
            if (not ev_chikaonsen3.hint == "") and not (ev_chikaonsen3.hint == "Event will trigger automatically."):
                text ("Three Words")
            if (not ev_chikaonsen4.hint == "") and not (ev_chikaonsen4.hint == "Event will trigger automatically."):
                text ("Zanzibar (Counting Cats)")
            if (not ev_chikalust15.hint == "") and not (ev_chikalust15.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}The Princess & The Pauper{/color}")
            if (not ev_chikalust20.hint == "") and not (ev_chikalust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Into the Woods{/color}")
            if (not ev_chikaspecial40.hint == "") and not (ev_chikaspecial40.hint == "Event will trigger automatically."):
                text ("In Search of Summer")
            if (not ev_mall40.hint == "") and not (ev_mall40.hint == "Event will trigger automatically."):
                text ("Self Care")
            if (not ev_mall40p2.hint == "") and not (ev_mall40p2.hint == "Event will trigger automatically."):
                text ("The Gap in the Curtain")
            if (not ev_chikadate45.hint == "") and not (ev_chikadate45.hint == "Event will trigger automatically."):
                text ("The Gap in the Door")

        if Yumi.active:
            if (not ev_streets30.hint == "") and not (ev_streets30.hint == "Event will trigger automatically."):
                text ("Where the Sidewalk Ends")
            if (not ev_yumidorm30.hint == "") and not (ev_yumidorm30.hint == "Event will trigger automatically."):
                text ("Walls Too Thick to Hear Through")
            if (not ev_yumidorm35.hint == "") and not (ev_yumidorm35.hint == "Event will trigger automatically."):
                text ("Tech Support")
            if (not ev_yumicallnight35.hint == "") and not (ev_yumicallnight35.hint == "Event will trigger automatically."):
                text ("Abyss")
            if (not ev_yumispecial40.hint == "") and not (ev_yumispecial40.hint == "Event will trigger automatically."):
                text ("Reconciliation")
            if (not ev_yumispecial40p2.hint == "") and not (ev_yumispecial40p2.hint == "Event will trigger automatically."):
                text ("Neon Heart (If I Close My Eyes)")
            if (not ev_streets40.hint == "") and not (ev_streets40.hint == "Event will trigger automatically."):
                text ("Unsung Heroes")
            if (not ev_yumispecial45.hint == "") and not (ev_yumispecial45.hint == "Event will trigger automatically."):
                text ("See You Around")

        if Ayane.active:
            if (not ev_ayaneinvite1.hint == "") and not (ev_ayaneinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Hail Mary{/color}")
            if (not ev_ayaneinvite2.hint == "") and not (ev_ayaneinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}One of Many Rooms{/color}")
            if (not ev_ayanelust15.hint == "") and not (ev_ayanelust15.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}What a Wonderful World{/color}")
            if (not ev_dojo35.hint == "") and not (ev_dojo35.hint == "Event will trigger automatically."):
                text ("Under the World Tree")
            if (not ev_ayanedorm35.hint == "") and not (ev_ayanedorm35.hint == "Event will trigger automatically."):
                text ("Crash of Thunder")
            if (not ev_ayanespecial1.hint == "") and not (ev_ayanespecial1.hint == "Event will trigger automatically."):
                text ("Nevermind")
            if (not ev_ayanespecial2.hint == "") and not (ev_ayanespecial2.hint == "Event will trigger automatically."):
                text ("Before the Sun Comes Up")
            if (not ev_ayanelust20.hint == "") and not (ev_ayanelust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Out With the Old{/color}")

        if Sana.active:
            if (not ev_bar35.hint == "") and not (ev_bar35.hint == "Event will trigger automatically."):
                text ("Purest Intentions")
            if (not ev_sanadorm35.hint == "") and not (ev_sanadorm35.hint == "Event will trigger automatically."):
                text ("Waiting for Anything")
            if (not ev_bar40.hint == "") and not (ev_bar40.hint == "Event will trigger automatically."):
                text ("Closer to Me")
            if (not ev_sanadorm40.hint == "") and not (ev_sanadorm40.hint == "Event will trigger automatically."):
                text ("The Inside of a Triangle")
            if (not ev_bar45.hint == "") and not (ev_bar45.hint == "Event will trigger automatically."):
                text ("Sweet Vermouth")
            if (not ev_sanadorm45.hint == "") and not (ev_sanadorm45.hint == "Event will trigger automatically."):
                text ("The Complete Absence of ")
                text ("  Everything ")
            if (not ev_sanadorm50.hint == "") and not (ev_sanadorm50.hint == "Event will trigger automatically."):
                text ("Mine (Yours)")
            if (not ev_bar50.hint == "") and not (ev_bar50.hint == "Event will trigger automatically."):
                text ("Melatonin")

        if Makoto.active:
            if (not ev_makotolust10.hint == "") and not (ev_makotolust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Semblance of a Soul{/color}")
            if (not ev_makotowinterbeach1.hint == "") and not (ev_makotowinterbeach1.hint == "Event will trigger automatically."):
                text ("Condoms in the Sand")
            if (not ev_makotowinterbeach2.hint == "") and not (ev_makotowinterbeach2.hint == "Event will trigger automatically."):
                text ("Humans With Hollow Bones")
            if (not ev_makotowinterbeach3.hint == "") and not (ev_makotowinterbeach3.hint == "Event will trigger automatically."):
                text ("I'm Not Here")
            if (not ev_makotowinterbeach4.hint == "") and not (ev_makotowinterbeach4.hint == "Event will trigger automatically."):
                text ("Something, Somewhere")
            if (not ev_makotolust20.hint == "") and not (ev_makotolust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Hot Water{/color}")

        if Miku.active:
            if (not ev_soccer35.hint == "") and not (ev_soccer35.hint == "Event will trigger automatically."):
                text ("Loxonin")
            if (not ev_mikuwinterbeach1.hint == "") and not (ev_mikuwinterbeach1.hint == "Event will trigger automatically."):
                text ("To Sleep, Perchance to Dream")
            if (not ev_mikudorm35.hint == "") and not (ev_mikudorm35.hint == "Event will trigger automatically."):
                text ("Triple Whammy")
            if (not ev_mikudorm40.hint == "") and not (ev_mikudorm40.hint == "Event will trigger automatically."):
                text ("Speed of Light")
            if (not ev_mikudorm45.hint == "") and not (ev_mikudorm45.hint == "Event will trigger automatically."):
                text ("Acute Love Triangle")
            if (not ev_mikudorm45p2.hint == "") and not (ev_mikudorm45p2.hint == "Event will trigger automatically."):
                text ("Chrysalis")
            if (not ev_mikuspecial50.hint == "") and not (ev_mikuspecial50.hint == "Event will trigger automatically."):
                text ("Someone Else's Skin")
            if (not ev_mikudorm50.hint == "") and not (ev_mikudorm50.hint == "Event will trigger automatically."):
                text ("The Devil & God Are Raging ")
                text ("  Inside Me ")

        if Futaba.active:
            if (not ev_futabalust10.hint == "") and not (ev_futabalust10.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Selfless{/color}")
            if (not ev_futabainvite1.hint == "") and not (ev_futabainvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Sonnet 18{/color}")
            if (not ev_futabainvite2.hint == "") and not (ev_futabainvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Floral Aura{/color}")
            if (not ev_futabalust15.hint == "") and not (ev_futabalust15.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}C'est La Vie{/color}")
            if (not ev_futabadorm40.hint == "") and not (ev_futabadorm40.hint == "Event will trigger automatically."):
                text ("Skin (Start Somewhere)")
            if (not ev_library40.hint == "") and not (ev_library40.hint == "Event will trigger automatically."):
                text ("Shadowplay")
            if (not ev_library40part2.hint == "") and not (ev_library40part2.hint == "Event will trigger automatically."):
                text ("Without Running Away")
            if (not ev_futabadorm45.hint == "") and not (ev_futabadorm45.hint == "Event will trigger automatically."):
                text ("Hall of Mirrors")

        if Rin.active:
            if (not ev_cafe40.hint == "") and not (ev_cafe40.hint == "Event will trigger automatically."):
                text ("Sketchy Basement")
            if (not ev_rindorm40.hint == "") and not (ev_rindorm40.hint == "Event will trigger automatically."):
                text ("Semantics")
            if (not ev_cafe45.hint == "") and not (ev_cafe45.hint == "Event will trigger automatically."):
                text ("Debatably Bisexual Musicians")
            if (not ev_rindorm45.hint == "") and not (ev_rindorm45.hint == "Event will trigger automatically."):
                text ("The Art of Never Knowing")
            if (not ev_cafe50.hint == "") and not (ev_cafe50.hint == "Event will trigger automatically."):
                text ("The Paragon of Not Worrying ")
                text ("  About Stuff ")
            if (not ev_rindorm50.hint == "") and not (ev_rindorm50.hint == "Event will trigger automatically."):
                text ("Technicolored Happiness ")
                text ("  Explosion ")
            if (not ev_rindorm50special.hint == "") and not (ev_rindorm50special.hint == "Event will trigger automatically."):
                text ("Lifejacket")
            if (not ev_rindate50.hint == "") and not (ev_rindate50.hint == "Event will trigger automatically."):
                text ("The Happiest Girl in the World")

        if Molly.active:
            if (not ev_mollycafe15.hint == "") and not (ev_mollycafe15.hint == "Event will trigger automatically."):
                text ("Onward to Valhalla")
            if (not ev_mollydorm15.hint == "") and not (ev_mollydorm15.hint == "Event will trigger automatically."):
                text ("Unpaid Promotion")
            if (not ev_mollycafe20.hint == "") and not (ev_mollycafe20.hint == "Event will trigger automatically."):
                text ("The Legacy of Thaum Pt. II")
            if (not ev_mollydorm20.hint == "") and not (ev_mollydorm20.hint == "Event will trigger automatically."):
                text ("Ahead of the Curve")
            if (not ev_mollycafe25.hint == "") and not (ev_mollycafe25.hint == "Event will trigger automatically."):
                text ("Resurrection Sickness")
            if (not ev_mollycafe25p2.hint == "") and not (ev_mollycafe25p2.hint == "Event will trigger automatically."):
                text ("Tír na nÓg")
            if (not ev_mollydorm25.hint == "") and not (ev_mollydorm25.hint == "Event will trigger automatically."):
                text ("Transmogrification")
            if (not ev_mollydorm30.hint == "") and not (ev_mollydorm30.hint == "Event will trigger automatically."):
                text ("Walkthrough")

        if Tsuneyo.active:
            if (not ev_ramen15.hint == "") and not (ev_ramen15.hint == "Event will trigger automatically."):
                text ("Seeds")
            if (not ev_tsuneyodorm15.hint == "") and not (ev_tsuneyodorm15.hint == "Event will trigger automatically."):
                text ("Moe Fan Service")
            if (not ev_tsuneyodorm20.hint == "") and not (ev_tsuneyodorm20.hint == "Event will trigger automatically."):
                text ("Fucking...Or What it Means to ")
                text ("  Live (Shio & Shoyu) ")
            if (not ev_ramen20.hint == "") and not (ev_ramen20.hint == "Event will trigger automatically."):
                text ("Blackout")
            if (not ev_ramen25.hint == "") and not (ev_ramen25.hint == "Event will trigger automatically."):
                text ("Like Noodles in the Wind")
            if (not ev_ramen25p2.hint == "") and not (ev_ramen25p2.hint == "Event will trigger automatically."):
                text ("Green Onions and Contraceptives")
            if (not ev_tsuneyodorm25.hint == "") and not (ev_tsuneyodorm25.hint == "Event will trigger automatically."):
                text ("Unsleeping Aegis")
            if (not ev_ramen30.hint == "") and not (ev_ramen30.hint == "Event will trigger automatically."):
                text ("Things Like Stairs")

        if Sara.active:
            if (not ev_saradate10.hint == "") and not (ev_saradate10.hint == "Event will trigger automatically."):
                text ("Uptown Girl")
            if (not ev_sarabar20.hint == "") and not (ev_sarabar20.hint == "Event will trigger automatically."):
                text ("She's Always a Woman")
            if (not ev_sarabar25.hint == "") and not (ev_sarabar25.hint == "Event will trigger automatically."):
                text ("Tell Me When")
            if (not ev_sarabar25p2.hint == "") and not (ev_sarabar25p2.hint == "Event will trigger automatically."):
                text ("The Place She Falls Asleep At ")
                text ("  Night ")
            if (not ev_saralust20.hint == "") and not (ev_saralust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Engulfed{/color}")

        if Haruka.active:
            if (not ev_harukainvite1.hint == "") and not (ev_harukainvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Shades of Green{/color}")
            if (not ev_harukainvite2.hint == "") and not (ev_harukainvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Roses{/color}")
            if (not ev_harukadate20.hint == "") and not (ev_harukadate20.hint == "Event will trigger automatically."):
                text ("Sober-ish")
            if (not ev_harukainvite3.hint == "") and not (ev_harukainvite3.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Unfiltered Tap Water{/color}")

        if Maki.active:
            if (not ev_makidate10.hint == "") and not (ev_makidate10.hint == "Event will trigger automatically."):
                text ("A Fair Trade")
            if (not ev_makiday351.hint == "") and not (ev_makiday351.hint == "Event will trigger automatically."):
                text ("Three Afloat On One Raft")
            if (not ev_makidate15.hint == "") and not (ev_makidate15.hint == "Event will trigger automatically."):
                text ("Thank You For Your Business")
            if (not ev_makiinvite1.hint == "") and not (ev_makiinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Traveling Lube Dealer{/color}")
            if (not ev_makiinvite2.hint == "") and not (ev_makiinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Special Occasions{/color}")

        if Kirin.active:
            if (not ev_kirinlust5.hint == "") and not (ev_kirinlust5.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Full Blossom{/color}")
            if (not ev_kirininvite1.hint == "") and not (ev_kirininvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Too Much, All at Once{/color}")
            if (not ev_kirininvite2.hint == "") and not (ev_kirininvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}No Extortion Necessary{/color}")
            if (not ev_kirinfirsthall.hint == "") and not (ev_kirinfirsthall.hint == "Event will trigger automatically."):
                text ("Morals vs. Orgasms")
            if (not ev_kirindorm10.hint == "") and not (ev_kirindorm10.hint == "Event will trigger automatically."):
                text ("Love, Dorms, and Other Things")
            if (not ev_kirinsoccer15.hint == "") and not (ev_kirinsoccer15.hint == "Event will trigger automatically."):
                text ("Flickering Spotlight")
            if (not ev_kirinsoccer20.hint == "") and not (ev_kirinsoccer20.hint == "Event will trigger automatically."):
                text ("Enigmatology")
            if (not ev_kirindorm15.hint == "") and not (ev_kirindorm15.hint == "Event will trigger automatically."):
                text ("Bye Bye, Boner")
            if (not ev_kirindorm20.hint == "") and not (ev_kirindorm20.hint == "Event will trigger automatically."):
                text ("Terms & Conditions")
            if (not ev_kirindate25.hint == "") and not (ev_kirindate25.hint == "Event will trigger automatically."):
                text ("All That is Contaminated")
            if (not ev_kirinlust20.hint == "") and not (ev_kirinlust20.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Taking the Reins{/color}")
            if (not ev_kirinspecial25.hint == "") and not (ev_kirinspecial25.hint == "Event will trigger automatically."):
                text ("Dyed Orange, Drenched in Sun")
            if (not ev_kirindorm25.hint == "") and not (ev_kirindorm25.hint == "Event will trigger automatically."):
                text ("Temporary Bliss")
            if (not ev_kirinsoccer25.hint == "") and not (ev_kirinsoccer25.hint == "Event will trigger automatically."):
                text ("Four Hand Massage")
            if (not ev_kirinspecial30.hint == "") and not (ev_kirinspecial30.hint == "Event will trigger automatically."):
                text ("Made Out of Nothing")
            if (not ev_kirinlust202.hint == "") and not (ev_kirinlust202.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}The Other Half{/color}")

        if Karin.active:
            if (not ev_karindate15.hint == "") and not (ev_karindate15.hint == "Event will trigger automatically."):
                text ("Dying Alone With Ten Cats")
            if (not ev_karinsoccer15.hint == "") and not (ev_karinsoccer15.hint == "Event will trigger automatically."):
                text ("Tendrils of Flame")
            if (not ev_karinsoccer20.hint == "") and not (ev_karinsoccer20.hint == "Event will trigger automatically."):
                text ("The Adventures of Karli & Steve")
            if (not ev_karindate20.hint == "") and not (ev_karindate20.hint == "Event will trigger automatically."):
                text ("Sweet Tooth")

        if Kaori.active:
            if (not ev_kaoridate15.hint == "") and not (ev_kaoridate15.hint == "Event will trigger automatically."):
                text ("To Die, To Sleep")
            if (not ev_kaoridate15p2.hint == "") and not (ev_kaoridate15p2.hint == "Event will trigger automatically."):
                text ("Sad Girl Special")
            if (not ev_kaoridate15p3.hint == "") and not (ev_kaoridate15p3.hint == "Event will trigger automatically."):
                text ("Clouds")
            if (not ev_kaoridate20.hint == "") and not (ev_kaoridate20.hint == "Event will trigger automatically."):
                text ("Såsom i en Spegel")
            if (not ev_kaoridate25.hint == "") and not (ev_kaoridate25.hint == "Event will trigger automatically."):
                text ("Wither")

        if Chinami.active:
            if (not ev_chinamidate10.hint == "") and not (ev_chinamidate10.hint == "Event will trigger automatically."):
                text ("Giant Pool of Jell-O")
            if (not ev_chinamidate15.hint == "") and not (ev_chinamidate15.hint == "Event will trigger automatically."):
                text ("Pool Party (Love & Puppies)")
            if (not ev_chinamidate20.hint == "") and not (ev_chinamidate20.hint == "Event will trigger automatically."):
                text ("Happy Hour")
            if (not ev_christmas1.hint == "") and not (ev_christmas1.hint == "Event will trigger automatically."):
                text ("Snow-Covered Footprints")
            if (not ev_christmas2.hint == "") and not (ev_christmas2.hint == "Event will trigger automatically."):
                text ("Patent-Pending")
            if (not ev_christmas3.hint == "") and not (ev_christmas3.hint == "Event will trigger automatically."):
                text ("Fuck Christmas")
            if (not ev_christmas4.hint == "") and not (ev_christmas4.hint == "Event will trigger automatically."):
                text ("Disappointing Everyone")
            if (not ev_christmas5.hint == "") and not (ev_christmas5.hint == "Event will trigger automatically."):
                text ("Bottled Dreams")
            if (not ev_christmas6.hint == "") and not (ev_christmas6.hint == "Event will trigger automatically."):
                text ("Christmas Miracle")
            if (not ev_christmas7.hint == "") and not (ev_christmas7.hint == "Event will trigger automatically."):
                text ("Fireworks, Chicken, and the ")
                text ("  Innate Fear of Death ")
            if (not ev_day237.hint == "") and not (ev_day237.hint == "Event will trigger automatically."):
                text ("Suicide Pact")
            if (not ev_day239.hint == "") and not (ev_day239.hint == "Event will trigger automatically."):
                text ("A Door that People Move Through")
            if (not ev_day240.hint == "") and not (ev_day240.hint == "Event will trigger automatically."):
                text ("Uta's Last Stand")
            if (not ev_day244.hint == "") and not (ev_day244.hint == "Event will trigger automatically."):
                text ("Opposites Attract")
            if (not ev_day246.hint == "") and not (ev_day246.hint == "Event will trigger automatically."):
                text ("All Kinds of People, All Kinds ")
                text ("  of Things ")
            if (not ev_day247.hint == "") and not (ev_day247.hint == "Event will trigger automatically."):
                text ("Caterpillar")
            if (not ev_day261.hint == "") and not (ev_day261.hint == "Event will trigger automatically."):
                text ("Let Me Die in Spring")
            if (not ev_day263.hint == "") and not (ev_day263.hint == "Event will trigger automatically."):
                text ("There's Always a Chance")
            if (not ev_day264.hint == "") and not (ev_day264.hint == "Event will trigger automatically."):
                text ("Forty Degrees Below Zero")
            if (not ev_day269.hint == "") and not (ev_day269.hint == "Event will trigger automatically."):
                text ("What Could Have Been")
            if (not ev_day270.hint == "") and not (ev_day270.hint == "Event will trigger automatically."):
                text ("What Is")
            if (not ev_day271.hint == "") and not (ev_day271.hint == "Event will trigger automatically."):
                text ("What Was")
            if (not ev_day280.hint == "") and not (ev_day280.hint == "Event will trigger automatically."):
                text ("Annabel Lee")
            if (not ev_day281.hint == "") and not (ev_day281.hint == "Event will trigger automatically."):
                text ("Yuritopia")
            if (not ev_day282.hint == "") and not (ev_day282.hint == "Event will trigger automatically."):
                text ("Birdcage")
            if (not ev_day283.hint == "") and not (ev_day283.hint == "Event will trigger automatically."):
                text ("Survive! Grow!")
            if (not ev_day287.hint == "") and not (ev_day287.hint == "Event will trigger automatically."):
                text ("Another Long Year")
            if (not ev_day288.hint == "") and not (ev_day288.hint == "Event will trigger automatically."):
                text ("Adult Supervision")
            if (not ev_day295.hint == "") and not (ev_day295.hint == "Event will trigger automatically."):
                text ("The WAP Man")
            if (not ev_day295parttwo.hint == "") and not (ev_day295parttwo.hint == "Event will trigger automatically."):
                text ("The Color of a Heart")
            if (not ev_day297.hint == "") and not (ev_day297.hint == "Event will trigger automatically."):
                text ("Call Me By Your Name")
            if (not ev_day302.hint == "") and not (ev_day302.hint == "Event will trigger automatically."):
                text ("Lives and Minds of Laymen")
            if (not ev_day303.hint == "") and not (ev_day303.hint == "Event will trigger automatically."):
                text ("Sounds of Cicadas")
            if (not ev_day304.hint == "") and not (ev_day304.hint == "Event will trigger automatically."):
                text ("Horses or the Whispers of the ")
                text ("  Dead ")
            if (not ev_day318.hint == "") and not (ev_day318.hint == "Event will trigger automatically."):
                text ("Operation: Firestarter")
            if (not ev_dormwar1.hint == "") and not (ev_dormwar1.hint == "Event will trigger automatically."):
                text ("Super Mega Ultimate Dorm War!")
            if (not ev_dormwar2.hint == "") and not (ev_dormwar2.hint == "Event will trigger automatically."):
                text ("Pre-Game Show!")
            if (not ev_dormwar3.hint == "") and not (ev_dormwar3.hint == "Event will trigger automatically."):
                text ("Imouto Mode!")
            if (not ev_dormwar4.hint == "") and not (ev_dormwar4.hint == "Event will trigger automatically."):
                text ("Alive & Active! All Out ")
                text ("  Athletics! ")
            if (not ev_dormwar5.hint == "") and not (ev_dormwar5.hint == "Event will trigger automatically."):
                text ("Friend Zone Fight!")
            if (not ev_dormwar6.hint == "") and not (ev_dormwar6.hint == "Event will trigger automatically."):
                text ("Sphenopalatine Ganglioneuralgia")
            if (not ev_dormwar7.hint == "") and not (ev_dormwar7.hint == "Event will trigger automatically."):
                text ("Ruthless Rhyme Rhomp! Rap ")
                text ("  Rampage! ")
            if (not ev_dormwar8.hint == "") and not (ev_dormwar8.hint == "Event will trigger automatically."):
                text ("Chaperone")
            if (not ev_dormwar9.hint == "") and not (ev_dormwar9.hint == "Event will trigger automatically."):
                text ("Why Now?")
            if (not ev_dormwar10.hint == "") and not (ev_dormwar10.hint == "Event will trigger automatically."):
                text ("In Some Cases, Love")
            if (not ev_dormwar11.hint == "") and not (ev_dormwar11.hint == "Event will trigger automatically."):
                text ("The Legacy of Thaum Pt. Z: ")
                text ("  Alentha Amastacia ")
            if (not ev_dormwar12.hint == "") and not (ev_dormwar12.hint == "Event will trigger automatically."):
                text ("Us")
            if (not ev_dormwar13.hint == "") and not (ev_dormwar13.hint == "Event will trigger automatically."):
                text ("First Last Date")
            if (not ev_dormwar14.hint == "") and not (ev_dormwar14.hint == "Event will trigger automatically."):
                text ("The Scary Room")
            if (not ev_dormwar15.hint == "") and not (ev_dormwar15.hint == "Event will trigger automatically."):
                text ("Fallen Angels")
            if (not ev_dormwar16.hint == "") and not (ev_dormwar16.hint == "Event will trigger automatically."):
                text ("Post-Game Celebration!")
            if (not ev_dormwar17.hint == "") and not (ev_dormwar17.hint == "Event will trigger automatically."):
                text ("War's End")
            if (not ev_day333.hint == "") and not (ev_day333.hint == "Event will trigger automatically."):
                text ("Record Breaker")
            if (not ev_day333part2.hint == "") and not (ev_day333part2.hint == "Event will trigger automatically."):
                text ("Lesbian Stuff")
            if (not ev_day340.hint == "") and not (ev_day340.hint == "Event will trigger automatically."):
                text ("Mana Transfer")
            if (not ev_day344.hint == "") and not (ev_day344.hint == "Event will trigger automatically."):
                text ("The Price of Experience")
            if (not ev_thirdreset1.hint == "") and not (ev_thirdreset1.hint == "Event will trigger automatically."):
                text ("Word of the Day")
            if (not ev_thirdreset2.hint == "") and not (ev_thirdreset2.hint == "Event will trigger automatically."):
                text ("Backwards Dancing")
            if (not ev_thirdreset3.hint == "") and not (ev_thirdreset3.hint == "Event will trigger automatically."):
                text ("Sayonara")
            if (not ev_day351.hint == "") and not (ev_day351.hint == "Event will trigger automatically."):
                text ("Food Groups")
            if (not ev_day355.hint == "") and not (ev_day355.hint == "Event will trigger automatically."):
                text ("Permission Slip")
            if (not ev_secondbeach1.hint == "") and not (ev_secondbeach1.hint == "Event will trigger automatically."):
                text ("Good Morning")
            if (not ev_secondbeach2.hint == "") and not (ev_secondbeach2.hint == "Event will trigger automatically."):
                text ("Egg Tossing")
            if (not ev_secondbeach3.hint == "") and not (ev_secondbeach3.hint == "Event will trigger automatically."):
                text ("De-Briefing the Teacher")
            if (not ev_secondbeach4.hint == "") and not (ev_secondbeach4.hint == "Event will trigger automatically."):
                text ("TPK (Banana Boat)")
            if (not ev_secondbeach5.hint == "") and not (ev_secondbeach5.hint == "Event will trigger automatically."):
                text ("The Next Best Thing")
            if (not ev_secondbeach6.hint == "") and not (ev_secondbeach6.hint == "Event will trigger automatically."):
                text ("The Yellow Wallpaper")
            if (not ev_secondbeach7.hint == "") and not (ev_secondbeach7.hint == "Event will trigger automatically."):
                text ("Everything Ephemeral (Face ")
                text ("  Forward) ")
            if (not ev_secondbeach8.hint == "") and not (ev_secondbeach8.hint == "Event will trigger automatically."):
                text ("The Legacy of Thaum Pt. III: ")
                text ("  Changeling ")
            if (not ev_secondbeach9.hint == "") and not (ev_secondbeach9.hint == "Event will trigger automatically."):
                text ("Alderaan")
            if (not ev_secondbeach10.hint == "") and not (ev_secondbeach10.hint == "Event will trigger automatically."):
                text ("Torrential Downpour. Child of ")
                text ("  Man. ")
            if (not ev_secondbeach11.hint == "") and not (ev_secondbeach11.hint == "Event will trigger automatically."):
                text ("Getting Comfortable")
            if (not ev_secondbeach12.hint == "") and not (ev_secondbeach12.hint == "Event will trigger automatically."):
                text ("Left Out in Light")
            if (not ev_secondbeach13.hint == "") and not (ev_secondbeach13.hint == "Event will trigger automatically."):
                text ("We Were Angels")
            if (not ev_secondbeach14.hint == "") and not (ev_secondbeach14.hint == "Event will trigger automatically."):
                text ("Lavender's Blue")
            if (not ev_secondbeach15.hint == "") and not (ev_secondbeach15.hint == "Event will trigger automatically."):
                text ("Pluto Was Never Really a Planet")
            if (not ev_secondbeach16.hint == "") and not (ev_secondbeach16.hint == "Event will trigger automatically."):
                text ("Try. Try. Try.")
            if (not ev_secondbeach17.hint == "") and not (ev_secondbeach17.hint == "Event will trigger automatically."):
                text ("Goodnight")
            if (not ev_secondbeach18.hint == "") and not (ev_secondbeach18.hint == "Event will trigger automatically."):
                text ("All is Bright. All is ")
                text ("  Beautiful. ")
            if (not ev_halloweentwo1.hint == "") and not (ev_halloweentwo1.hint == "Event will trigger automatically."):
                text ("Girls in Spandex")
            if (not ev_halloweentwo2.hint == "") and not (ev_halloweentwo2.hint == "Event will trigger automatically."):
                text ("Butterfly Facts")
            if (not ev_halloweentwo3.hint == "") and not (ev_halloweentwo3.hint == "Event will trigger automatically."):
                text ("Immernachtreich")
            if (not ev_halloweentwo4.hint == "") and not (ev_halloweentwo4.hint == "Event will trigger automatically."):
                text ("Take Me Anywhere")
            if (not ev_halloweentwo5.hint == "") and not (ev_halloweentwo5.hint == "Event will trigger automatically."):
                text ("Anglerfish")
            if (not ev_halloweentwo6.hint == "") and not (ev_halloweentwo6.hint == "Event will trigger automatically."):
                text ("Porcelain Labyrinth")
            if (not ev_halloweentwo7.hint == "") and not (ev_halloweentwo7.hint == "Event will trigger automatically."):
                text ("The First Signs of Fraying ")
                text ("  Threads ")
            if (not ev_halloweentwo8.hint == "") and not (ev_halloweentwo8.hint == "Event will trigger automatically."):
                text ("Official Unofficial Double Date")
            if (not ev_halloweentwo9.hint == "") and not (ev_halloweentwo9.hint == "Event will trigger automatically."):
                text ("In Circles")
            if (not ev_halloweentwo10.hint == "") and not (ev_halloweentwo10.hint == "Event will trigger automatically."):
                text ("Escape Rope")
            if (not ev_halloweentwo11.hint == "") and not (ev_halloweentwo11.hint == "Event will trigger automatically."):
                text ("Lavender's Green")
            if (not ev_halloweentwo12.hint == "") and not (ev_halloweentwo12.hint == "Event will trigger automatically."):
                text ("Gallows Edge")
            if (not ev_halloweentwo13.hint == "") and not (ev_halloweentwo13.hint == "Event will trigger automatically."):
                text ("Metal in Microwaves")
            if (not ev_christmastwo1.hint == "") and not (ev_christmastwo1.hint == "Event will trigger automatically."):
                text ("Three Amigos")
            if (not ev_christmastwo2.hint == "") and not (ev_christmastwo2.hint == "Event will trigger automatically."):
                text ("The Reliable and Totally ")
                text ("  Legitimate Princess Imani ")
            if (not ev_christmastwo3.hint == "") and not (ev_christmastwo3.hint == "Event will trigger automatically."):
                text ("Room to Grow")
            if (not ev_christmastwo4.hint == "") and not (ev_christmastwo4.hint == "Event will trigger automatically."):
                text ("Dodging Snowflakes")
            if (not ev_christmastwo5.hint == "") and not (ev_christmastwo5.hint == "Event will trigger automatically."):
                text ("Everything Evil")
            if (not ev_christmastwo6.hint == "") and not (ev_christmastwo6.hint == "Event will trigger automatically."):
                text ("Tokimeki Labyrinth")
            if (not ev_christmastwo7.hint == "") and not (ev_christmastwo7.hint == "Event will trigger automatically."):
                text ("Love Set to Max (Class Warfare)")
            if (not ev_christmastwo8.hint == "") and not (ev_christmastwo8.hint == "Event will trigger automatically."):
                text ("Dohoonkabhankoloos")
            if (not ev_christmastwo9.hint == "") and not (ev_christmastwo9.hint == "Event will trigger automatically."):
                text ("Fear of Missing Out")
            if (not ev_christmastwo10.hint == "") and not (ev_christmastwo10.hint == "Event will trigger automatically."):
                text ("Walking on Eggshells")
            if (not ev_christmastwo11.hint == "") and not (ev_christmastwo11.hint == "Event will trigger automatically."):
                text ("New Age Entrepreneurs")
            if (not ev_christmastwo12.hint == "") and not (ev_christmastwo12.hint == "Event will trigger automatically."):
                text ("The Smile, The Face")
            if (not ev_christmastwo13.hint == "") and not (ev_christmastwo13.hint == "Event will trigger automatically."):
                text ("Shadowmeld")
            if (not ev_christmastwo14.hint == "") and not (ev_christmastwo14.hint == "Event will trigger automatically."):
                text ("Chashu (A Cracked Bowl)")
            if (not ev_christmastwo15.hint == "") and not (ev_christmastwo15.hint == "Event will trigger automatically."):
                text ("A Way's Away")
            if (not ev_christmastwo16.hint == "") and not (ev_christmastwo16.hint == "Event will trigger automatically."):
                text ("No Escape")
            if (not ev_christmastwo17.hint == "") and not (ev_christmastwo17.hint == "Event will trigger automatically."):
                text ("Spotless Mind")
            if (not ev_christmastwo18.hint == "") and not (ev_christmastwo18.hint == "Event will trigger automatically."):
                text ("Me Without You")
            if (not ev_christmastwo19.hint == "") and not (ev_christmastwo19.hint == "Event will trigger automatically."):
                text ("The Color White")
            if (not ev_christmastwo20.hint == "") and not (ev_christmastwo20.hint == "Event will trigger automatically."):
                text ("Glued to the Sky")
            if (not ev_returntosummer1.hint == "") and not (ev_returntosummer1.hint == "Event will trigger automatically."):
                text ("The Light of Last Summer")
            if (not ev_returntosummer2.hint == "") and not (ev_returntosummer2.hint == "Event will trigger automatically."):
                text ("A Life of Prizes")
            if (not ev_returntosummer3.hint == "") and not (ev_returntosummer3.hint == "Event will trigger automatically."):
                text ("Utinam Ne Illum Numquam ")
                text ("  Conspexissem ")

        if Yuki.active:
            if (not ev_yukidate1.hint == "") and not (ev_yukidate1.hint == "Event will trigger automatically."):
                text ("Rule #1")
            if (not ev_yukidate5.hint == "") and not (ev_yukidate5.hint == "Event will trigger automatically."):
                text ("Better Off Alone")
            if (not ev_yukidate10.hint == "") and not (ev_yukidate10.hint == "Event will trigger automatically."):
                text ("Opposite Directions")
            if (not ev_yukidate10p2.hint == "") and not (ev_yukidate10p2.hint == "Event will trigger automatically."):
                text ("A Thing of the Past")

        if Wakana.active:
            if (not ev_wakanadate1.hint == "") and not (ev_wakanadate1.hint == "Event will trigger automatically."):
                text ("To the River")
            if (not ev_wakanadate5.hint == "") and not (ev_wakanadate5.hint == "Event will trigger automatically."):
                text ("Soup, or Another Year With You")

        if Osako.active:
            if (not ev_osakodate1.hint == "") and not (ev_osakodate1.hint == "Event will trigger automatically."):
                text ("Pressure Point")
            if (not ev_osakodojo1.hint == "") and not (ev_osakodojo1.hint == "Event will trigger automatically."):
                text ("Floating Forever, Unfulfilled")

        if Tsubasa.active:
            if (not ev_tsubasadate1.hint == "") and not (ev_tsubasadate1.hint == "Event will trigger automatically."):
                text ("Everbloom (Pride of the Sinful ")
                text ("  Sort) ")
            if (not ev_tsubasadate1p2.hint == "") and not (ev_tsubasadate1p2.hint == "Event will trigger automatically."):
                text ("The Deep End")

        if Uta.active:
            if (not ev_utafirsthall.hint == "") and not (ev_utafirsthall.hint == "Event will trigger automatically."):
                text ("Far From Home")
            if (not ev_utamaid1.hint == "") and not (ev_utamaid1.hint == "Event will trigger automatically."):
                text ("Abuse of Power")
            if (not ev_utamaid5.hint == "") and not (ev_utamaid5.hint == "Event will trigger automatically."):
                text ("Love Me to Pieces")
            if (not ev_utadorm5.hint == "") and not (ev_utadorm5.hint == "Event will trigger automatically."):
                text ("The VIP Treatment")
            if (not ev_utadorm10.hint == "") and not (ev_utadorm10.hint == "Event will trigger automatically."):
                text ("Shawshank Redemption")
            if (not ev_utamaid10.hint == "") and not (ev_utamaid10.hint == "Event will trigger automatically."):
                text ("Happier Things")
            if (not ev_utadorm15.hint == "") and not (ev_utadorm15.hint == "Event will trigger automatically."):
                text ("Facetime With My Mom (Tonight)")
            if (not ev_utamaid20.hint == "") and not (ev_utamaid20.hint == "Event will trigger automatically."):
                text ("Veins and the Circulatory ")
                text ("  System ")
            if (not ev_utadorm20.hint == "") and not (ev_utadorm20.hint == "Event will trigger automatically."):
                text ("Blood Everywhere")

        if Io.active:
            if (not ev_iofirsthall.hint == "") and not (ev_iofirsthall.hint == "Event will trigger automatically."):
                text ("Viva la Revolución")
            if (not ev_bathhouse1.hint == "") and not (ev_bathhouse1.hint == "Event will trigger automatically."):
                text ("Nonetheless, I'm Here")
            if (not ev_bathhouse5.hint == "") and not (ev_bathhouse5.hint == "Event will trigger automatically."):
                text ("The Girl with the Dragon Tattoo")
            if (not ev_iodorm5.hint == "") and not (ev_iodorm5.hint == "Event will trigger automatically."):
                text ("Unnamed Wooden Robots")
            if (not ev_iodorm10.hint == "") and not (ev_iodorm10.hint == "Event will trigger automatically."):
                text ("Paperthin")
            if (not ev_bathhouse10.hint == "") and not (ev_bathhouse10.hint == "Event will trigger automatically."):
                text ("Turn On The Lights")
            if (not ev_iodorm15.hint == "") and not (ev_iodorm15.hint == "Event will trigger automatically."):
                text ("Amongst Other Things")
            if (not ev_bathhouse20.hint == "") and not (ev_bathhouse20.hint == "Event will trigger automatically."):
                text ("One Man's Trash")
            if (not ev_bathhouse20part2.hint == "") and not (ev_bathhouse20part2.hint == "Event will trigger automatically."):
                text ("Another Man's Treasure")

        if Noriko.active:
            if (not ev_norikofirsthall.hint == "") and not (ev_norikofirsthall.hint == "Event will trigger automatically."):
                text ("Sculpture (Dream Girl)")
            if (not ev_convenience1.hint == "") and not (ev_convenience1.hint == "Event will trigger automatically."):
                text ("Nakayarakawayama")
            if (not ev_norikodorm5.hint == "") and not (ev_norikodorm5.hint == "Event will trigger automatically."):
                text ("Semi-Constructive Criticism")
            if (not ev_convenience5.hint == "") and not (ev_convenience5.hint == "Event will trigger automatically."):
                text ("Mouthjob")
            if (not ev_norikodorm10.hint == "") and not (ev_norikodorm10.hint == "Event will trigger automatically."):
                text ("Kind Of, Yes. Kind Of, No.")
            if (not ev_norikoinvite1.hint == "") and not (ev_norikoinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}New Shoes{/color}")
            if (not ev_norikoinvite2.hint == "") and not (ev_norikoinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Beginnings. Endings. Things in {/color}")
                text ("{color=778EFF}  Between. {/color}")
            if (not ev_norikospecial20.hint == "") and not (ev_norikospecial20.hint == "Event will trigger automatically."):
                text ("Fair & Square")
            if (not ev_norikodorm20.hint == "") and not (ev_norikodorm20.hint == "Event will trigger automatically."):
                text ("Homes for the Homeless")
            if (not ev_convenience25.hint == "") and not (ev_convenience25.hint == "Event will trigger automatically."):
                text ("That One FMK Scene")
            if (not ev_norikodorm25.hint == "") and not (ev_norikodorm25.hint == "Event will trigger automatically."):
                text ("Loxosceles Reclusa")

        if Niki.active:
            if (not ev_nikidate1.hint == "") and not (ev_nikidate1.hint == "Event will trigger automatically."):
                text ("Cotton Candy")
            if (not ev_nikidate5.hint == "") and not (ev_nikidate5.hint == "Event will trigger automatically."):
                text ("Like it's Any Other Day")
            if (not ev_nikidate10.hint == "") and not (ev_nikidate10.hint == "Event will trigger automatically."):
                text ("Thousands, If Not Millions")
            if (not ev_nikidate15.hint == "") and not (ev_nikidate15.hint == "Event will trigger automatically."):
                text ("Hotel Rooms")
            if (not ev_nikiinvite1.hint == "") and not (ev_nikiinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Sisters{/color}")
            if (not ev_nikiinvite2.hint == "") and not (ev_nikiinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Dear You{/color}")

        if Nodoka.active:
            if (not ev_nodokafirsthall.hint == "") and not (ev_nodokafirsthall.hint == "Event will trigger automatically."):
                text ("Humbert Humbert")
            if (not ev_nodokadorm1.hint == "") and not (ev_nodokadorm1.hint == "Event will trigger automatically."):
                text ("The Man Who Would Be King")
            if (not ev_nodokalibrary1.hint == "") and not (ev_nodokalibrary1.hint == "Event will trigger automatically."):
                text ("Cracks in the Armor")
            if (not ev_nodokalibrary5.hint == "") and not (ev_nodokalibrary5.hint == "Event will trigger automatically."):
                text ("Coloring Book")
            if (not ev_nodokadorm5.hint == "") and not (ev_nodokadorm5.hint == "Event will trigger automatically."):
                text ("I See Everything")

        if Otoha.active:
            if (not ev_otohafirsthall.hint == "") and not (ev_otohafirsthall.hint == "Event will trigger automatically."):
                text ("Everybody Loves Otoha")
            if (not ev_otohadorm1.hint == "") and not (ev_otohadorm1.hint == "Event will trigger automatically."):
                text ("Conversations Outside of a ")
                text ("  Girls’ Dorm ")
            if (not ev_otohapark1.hint == "") and not (ev_otohapark1.hint == "Event will trigger automatically."):
                text ("Japanese Summer (Double ")
                text ("  Suicide) ")
            if (not ev_otohapark5.hint == "") and not (ev_otohapark5.hint == "Event will trigger automatically."):
                text ("Locked In")
            if (not ev_otohadorm5.hint == "") and not (ev_otohadorm5.hint == "Event will trigger automatically."):
                text ("Highly Pornographic")
            if (not ev_otohapark10.hint == "") and not (ev_otohapark10.hint == "Event will trigger automatically."):
                text ("Pull the Plug")
            if (not ev_otohaspecial10.hint == "") and not (ev_otohaspecial10.hint == "Event will trigger automatically."):
                text ("Two-Octave Pitch Glide")
            if (not ev_otohadorm10.hint == "") and not (ev_otohadorm10.hint == "Event will trigger automatically."):
                text ("Breathing in Unison")
            if (not ev_otohadorm10p2.hint == "") and not (ev_otohadorm10p2.hint == "Event will trigger automatically."):
                text ("Vanilla Bean")

        if Touka.active:
            if (not ev_toukafirsthall.hint == "") and not (ev_toukafirsthall.hint == "Event will trigger automatically."):
                text ("Spontaneous Sentimentality")
            if (not ev_toukastreets1.hint == "") and not (ev_toukastreets1.hint == "Event will trigger automatically."):
                text ("Trial Period")
            if (not ev_toukadorm1.hint == "") and not (ev_toukadorm1.hint == "Event will trigger automatically."):
                text ("Fish Out of Water")
            if (not ev_toukastreets5.hint == "") and not (ev_toukastreets5.hint == "Event will trigger automatically."):
                text ("A Brief Moment in Time")
            if (not ev_toukadorm5.hint == "") and not (ev_toukadorm5.hint == "Event will trigger automatically."):
                text ("Loser")
            if (not ev_toukadorm10.hint == "") and not (ev_toukadorm10.hint == "Event will trigger automatically."):
                text ("House Call")
            if (not ev_toukaspecial15.hint == "") and not (ev_toukaspecial15.hint == "Event will trigger automatically."):
                text ("A Commoner's Tour of Summer")
            if (not ev_toukaspecial15p2.hint == "") and not (ev_toukaspecial15p2.hint == "Event will trigger automatically."):
                text ("Red-ish Light District")
            if (not ev_toukaspecial15p3.hint == "") and not (ev_toukaspecial15p3.hint == "Event will trigger automatically."):
                text ("Something Less Lonely")

        if Yasu.active:
            if (not ev_yasufirsthall.hint == "") and not (ev_yasufirsthall.hint == "Event will trigger automatically."):
                text ("The Hole That Swallowed ")
                text ("  Everything ")
            if (not ev_church1.hint == "") and not (ev_church1.hint == "Event will trigger automatically."):
                text ("Transference")
            if (not ev_church5.hint == "") and not (ev_church5.hint == "Event will trigger automatically."):
                text ("Armor of Older Gods")
            if (not ev_yasudorm10.hint == "") and not (ev_yasudorm10.hint == "Event will trigger automatically."):
                text ("Repentance")
            if (not ev_church10.hint == "") and not (ev_church10.hint == "Event will trigger automatically."):
                text ("Sakura Season")

    vbox:
        xpos .53
        ypos .14
        style_prefix "hint"

        if show_hints == True:


            if HappyEvent.active:
                if (not ev_lesson1.hint == "") and not (ev_lesson1.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_lesson1.hint]")
                        text ("")
                    else:
                        text ("")
                        text ("")
                if (not ev_goodboy.hint == "") and not (ev_goodboy.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_goodboy.hint]")
                    else:
                        text ("")
                if (not ev_lamblegs.hint == "") and not (ev_lamblegs.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_lamblegs.hint]")
                    else:
                        text ("")

            if Ami.active:
                if (not ev_amiinvite1.hint == "") and not (ev_amiinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amiinvite1.hint:
                        textbutton _("[ev_amiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amiinvite1.hint]")
                if (not ev_amiinvite2.hint == "") and not (ev_amiinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amiinvite2.hint:
                        textbutton _("[ev_amiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amiinvite2.hint]")
                if (not ev_amiinvite3.hint == "") and not (ev_amiinvite3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amiinvite3.hint:
                        textbutton _("[ev_amiinvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amiinvite3.hint]")
                if (not ev_amimaid30.hint == "") and not (ev_amimaid30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amimaid30.hint:
                        textbutton _("[ev_amimaid30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amimaid30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amimaid30.hint]")
                if (not ev_amidate35.hint == "") and not (ev_amidate35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidate35.hint:
                        textbutton _("[ev_amidate35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidate35.hint]")
                if (not ev_amidorm40.hint == "") and not (ev_amidorm40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidorm40.hint:
                        textbutton _("[ev_amidorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidorm40.hint]")
                if (not ev_amilust15.hint == "") and not (ev_amilust15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amilust15.hint:
                        textbutton _("[ev_amilust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amilust15.hint]")
                if (not ev_amilust20.hint == "") and not (ev_amilust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amilust20.hint:
                        textbutton _("[ev_amilust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amilust20.hint]")
                if (not ev_amidate50.hint == "") and not (ev_amidate50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidate50.hint:
                        textbutton _("[ev_amidate50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidate50.hint]")
                if (not ev_amidate50p2.hint == "") and not (ev_amidate50p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidate50p2.hint:
                        textbutton _("[ev_amidate50p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidate50p2.hint]")
                if (not ev_amidate50p3.hint == "") and not (ev_amidate50p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidate50p3.hint:
                        textbutton _("[ev_amidate50p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidate50p3.hint]")
                if (not ev_amidate50p4.hint == "") and not (ev_amidate50p4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amidate50p4.hint:
                        textbutton _("[ev_amidate50p4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amidate50p4.hint]")

            if Maya.active:
                if (not ev_mayadorm30.hint == "") and not (ev_mayadorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm30.hint:
                        textbutton _("[ev_mayadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm30.hint]")
                if (not ev_shrine30.hint == "") and not (ev_shrine30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine30.hint:
                        textbutton _("[ev_shrine30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine30.hint]")
                if (not ev_mayadorm35.hint == "") and not (ev_mayadorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadorm35.hint:
                        textbutton _("[ev_mayadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadorm35.hint]")
                    text ("")
                if (not ev_shrine35.hint == "") and not (ev_shrine35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine35.hint:
                        textbutton _("[ev_shrine35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine35.hint]")
                if (not ev_mayafestival1.hint == "") and not (ev_mayafestival1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayafestival1.hint:
                        textbutton _("[ev_mayafestival1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayafestival1.hint]")
                if (not ev_mayafestival2.hint == "") and not (ev_mayafestival2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayafestival2.hint:
                        textbutton _("[ev_mayafestival2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayafestival2.hint]")
                    text ("")
                if (not ev_mayafestival3.hint == "") and not (ev_mayafestival3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayafestival3.hint:
                        textbutton _("[ev_mayafestival3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayafestival3.hint]")
                if (not ev_mayafestival4.hint == "") and not (ev_mayafestival4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayafestival4.hint:
                        textbutton _("[ev_mayafestival4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayafestival4.hint]")

            if Chika.active:
                if (not ev_chikalust10.hint == "") and not (ev_chikalust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikalust10.hint:
                        textbutton _("[ev_chikalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikalust10.hint]")
                if (not ev_chikaonsen1.hint == "") and not (ev_chikaonsen1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaonsen1.hint:
                        textbutton _("[ev_chikaonsen1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaonsen1.hint]")
                if (not ev_chikaonsen2.hint == "") and not (ev_chikaonsen2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaonsen2.hint:
                        textbutton _("[ev_chikaonsen2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaonsen2.hint]")
                if (not ev_chikaonsen3.hint == "") and not (ev_chikaonsen3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaonsen3.hint:
                        textbutton _("[ev_chikaonsen3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaonsen3.hint]")
                if (not ev_chikaonsen4.hint == "") and not (ev_chikaonsen4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaonsen4.hint:
                        textbutton _("[ev_chikaonsen4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaonsen4.hint]")
                if (not ev_chikalust15.hint == "") and not (ev_chikalust15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikalust15.hint:
                        textbutton _("[ev_chikalust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikalust15.hint]")
                if (not ev_chikalust20.hint == "") and not (ev_chikalust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikalust20.hint:
                        textbutton _("[ev_chikalust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikalust20.hint]")
                if (not ev_chikaspecial40.hint == "") and not (ev_chikaspecial40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaspecial40.hint:
                        textbutton _("[ev_chikaspecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspecial40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaspecial40.hint]")
                if (not ev_mall40.hint == "") and not (ev_mall40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall40.hint:
                        textbutton _("[ev_mall40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall40.hint]")
                if (not ev_mall40p2.hint == "") and not (ev_mall40p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall40p2.hint:
                        textbutton _("[ev_mall40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall40p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall40p2.hint]")
                if (not ev_chikadate45.hint == "") and not (ev_chikadate45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadate45.hint:
                        textbutton _("[ev_chikadate45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadate45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadate45.hint]")

            if Yumi.active:
                if (not ev_streets30.hint == "") and not (ev_streets30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets30.hint:
                        textbutton _("[ev_streets30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets30.hint]")
                if (not ev_yumidorm30.hint == "") and not (ev_yumidorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm30.hint:
                        textbutton _("[ev_yumidorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm30.hint]")
                if (not ev_yumidorm35.hint == "") and not (ev_yumidorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumidorm35.hint:
                        textbutton _("[ev_yumidorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumidorm35.hint]")
                if (not ev_yumicallnight35.hint == "") and not (ev_yumicallnight35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumicallnight35.hint:
                        textbutton _("[ev_yumicallnight35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumicallnight35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumicallnight35.hint]")
                if (not ev_yumispecial40.hint == "") and not (ev_yumispecial40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumispecial40.hint:
                        textbutton _("[ev_yumispecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumispecial40.hint]")
                if (not ev_yumispecial40p2.hint == "") and not (ev_yumispecial40p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumispecial40p2.hint:
                        textbutton _("[ev_yumispecial40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial40p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumispecial40p2.hint]")
                if (not ev_streets40.hint == "") and not (ev_streets40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_streets40.hint:
                        textbutton _("[ev_streets40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_streets40.hint]")
                if (not ev_yumispecial45.hint == "") and not (ev_yumispecial45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumispecial45.hint:
                        textbutton _("[ev_yumispecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumispecial45.hint]")

            if Ayane.active:
                if (not ev_ayaneinvite1.hint == "") and not (ev_ayaneinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayaneinvite1.hint:
                        textbutton _("[ev_ayaneinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayaneinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayaneinvite1.hint]")
                if (not ev_ayaneinvite2.hint == "") and not (ev_ayaneinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayaneinvite2.hint:
                        textbutton _("[ev_ayaneinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayaneinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayaneinvite2.hint]")
                if (not ev_ayanelust15.hint == "") and not (ev_ayanelust15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanelust15.hint:
                        textbutton _("[ev_ayanelust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanelust15.hint]")
                if (not ev_dojo35.hint == "") and not (ev_dojo35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dojo35.hint:
                        textbutton _("[ev_dojo35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dojo35.hint]")
                if (not ev_ayanedorm35.hint == "") and not (ev_ayanedorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanedorm35.hint:
                        textbutton _("[ev_ayanedorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanedorm35.hint]")
                if (not ev_ayanespecial1.hint == "") and not (ev_ayanespecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanespecial1.hint:
                        textbutton _("[ev_ayanespecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanespecial1.hint]")
                if (not ev_ayanespecial2.hint == "") and not (ev_ayanespecial2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanespecial2.hint:
                        textbutton _("[ev_ayanespecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanespecial2.hint]")
                if (not ev_ayanelust20.hint == "") and not (ev_ayanelust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanelust20.hint:
                        textbutton _("[ev_ayanelust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanelust20.hint]")

            if Sana.active:
                if (not ev_bar35.hint == "") and not (ev_bar35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar35.hint:
                        textbutton _("[ev_bar35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar35.hint]")
                if (not ev_sanadorm35.hint == "") and not (ev_sanadorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm35.hint:
                        textbutton _("[ev_sanadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm35.hint]")
                if (not ev_bar40.hint == "") and not (ev_bar40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar40.hint:
                        textbutton _("[ev_bar40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar40.hint]")
                if (not ev_sanadorm40.hint == "") and not (ev_sanadorm40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm40.hint:
                        textbutton _("[ev_sanadorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm40.hint]")
                if (not ev_bar45.hint == "") and not (ev_bar45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar45.hint:
                        textbutton _("[ev_bar45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar45.hint]")
                if (not ev_sanadorm45.hint == "") and not (ev_sanadorm45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm45.hint:
                        textbutton _("[ev_sanadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm45.hint]")
                    text ("")
                if (not ev_sanadorm50.hint == "") and not (ev_sanadorm50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sanadorm50.hint:
                        textbutton _("[ev_sanadorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sanadorm50.hint]")
                if (not ev_bar50.hint == "") and not (ev_bar50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar50.hint:
                        textbutton _("[ev_bar50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar50.hint]")

            if Makoto.active:
                if (not ev_makotolust10.hint == "") and not (ev_makotolust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotolust10.hint:
                        textbutton _("[ev_makotolust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotolust10.hint]")
                if (not ev_makotowinterbeach1.hint == "") and not (ev_makotowinterbeach1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotowinterbeach1.hint:
                        textbutton _("[ev_makotowinterbeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotowinterbeach1.hint]")
                if (not ev_makotowinterbeach2.hint == "") and not (ev_makotowinterbeach2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotowinterbeach2.hint:
                        textbutton _("[ev_makotowinterbeach2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotowinterbeach2.hint]")
                if (not ev_makotowinterbeach3.hint == "") and not (ev_makotowinterbeach3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotowinterbeach3.hint:
                        textbutton _("[ev_makotowinterbeach3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotowinterbeach3.hint]")
                if (not ev_makotowinterbeach4.hint == "") and not (ev_makotowinterbeach4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotowinterbeach4.hint:
                        textbutton _("[ev_makotowinterbeach4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotowinterbeach4.hint]")
                if (not ev_makotolust20.hint == "") and not (ev_makotolust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotolust20.hint:
                        textbutton _("[ev_makotolust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotolust20.hint]")

            if Miku.active:
                if (not ev_soccer35.hint == "") and not (ev_soccer35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_soccer35.hint:
                        textbutton _("[ev_soccer35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_soccer35.hint]")
                if (not ev_mikuwinterbeach1.hint == "") and not (ev_mikuwinterbeach1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikuwinterbeach1.hint:
                        textbutton _("[ev_mikuwinterbeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuwinterbeach1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikuwinterbeach1.hint]")
                if (not ev_mikudorm35.hint == "") and not (ev_mikudorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm35.hint:
                        textbutton _("[ev_mikudorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm35.hint]")
                if (not ev_mikudorm40.hint == "") and not (ev_mikudorm40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm40.hint:
                        textbutton _("[ev_mikudorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm40.hint]")
                if (not ev_mikudorm45.hint == "") and not (ev_mikudorm45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm45.hint:
                        textbutton _("[ev_mikudorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm45.hint]")
                if (not ev_mikudorm45p2.hint == "") and not (ev_mikudorm45p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm45p2.hint:
                        textbutton _("[ev_mikudorm45p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm45p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm45p2.hint]")
                if (not ev_mikuspecial50.hint == "") and not (ev_mikuspecial50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikuspecial50.hint:
                        textbutton _("[ev_mikuspecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspecial50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikuspecial50.hint]")
                if (not ev_mikudorm50.hint == "") and not (ev_mikudorm50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm50.hint:
                        textbutton _("[ev_mikudorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm50.hint]")
                    text ("")

            if Futaba.active:
                if (not ev_futabalust10.hint == "") and not (ev_futabalust10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabalust10.hint:
                        textbutton _("[ev_futabalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabalust10.hint]")
                if (not ev_futabainvite1.hint == "") and not (ev_futabainvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabainvite1.hint:
                        textbutton _("[ev_futabainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabainvite1.hint]")
                if (not ev_futabainvite2.hint == "") and not (ev_futabainvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabainvite2.hint:
                        textbutton _("[ev_futabainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabainvite2.hint]")
                if (not ev_futabalust15.hint == "") and not (ev_futabalust15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabalust15.hint:
                        textbutton _("[ev_futabalust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabalust15.hint]")
                if (not ev_futabadorm40.hint == "") and not (ev_futabadorm40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm40.hint:
                        textbutton _("[ev_futabadorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm40.hint]")
                if (not ev_library40.hint == "") and not (ev_library40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library40.hint:
                        textbutton _("[ev_library40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library40.hint]")
                if (not ev_library40part2.hint == "") and not (ev_library40part2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library40part2.hint:
                        textbutton _("[ev_library40part2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library40part2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library40part2.hint]")
                if (not ev_futabadorm45.hint == "") and not (ev_futabadorm45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm45.hint:
                        textbutton _("[ev_futabadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm45.hint]")

            if Rin.active:
                if (not ev_cafe40.hint == "") and not (ev_cafe40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe40.hint:
                        textbutton _("[ev_cafe40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe40.hint]")
                if (not ev_rindorm40.hint == "") and not (ev_rindorm40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm40.hint:
                        textbutton _("[ev_rindorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm40.hint]")
                if (not ev_cafe45.hint == "") and not (ev_cafe45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe45.hint:
                        textbutton _("[ev_cafe45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe45.hint]")
                if (not ev_rindorm45.hint == "") and not (ev_rindorm45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm45.hint:
                        textbutton _("[ev_rindorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm45.hint]")
                if (not ev_cafe50.hint == "") and not (ev_cafe50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_cafe50.hint:
                        textbutton _("[ev_cafe50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_cafe50.hint]")
                    text ("")
                if (not ev_rindorm50.hint == "") and not (ev_rindorm50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm50.hint:
                        textbutton _("[ev_rindorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm50.hint]")
                    text ("")
                if (not ev_rindorm50special.hint == "") and not (ev_rindorm50special.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm50special.hint:
                        textbutton _("[ev_rindorm50special.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm50special), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm50special.hint]")
                if (not ev_rindate50.hint == "") and not (ev_rindate50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindate50.hint:
                        textbutton _("[ev_rindate50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindate50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindate50.hint]")

            if Molly.active:
                if (not ev_mollycafe15.hint == "") and not (ev_mollycafe15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe15.hint:
                        textbutton _("[ev_mollycafe15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe15.hint]")
                if (not ev_mollydorm15.hint == "") and not (ev_mollydorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm15.hint:
                        textbutton _("[ev_mollydorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm15.hint]")
                if (not ev_mollycafe20.hint == "") and not (ev_mollycafe20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe20.hint:
                        textbutton _("[ev_mollycafe20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe20.hint]")
                if (not ev_mollydorm20.hint == "") and not (ev_mollydorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm20.hint:
                        textbutton _("[ev_mollydorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm20.hint]")
                if (not ev_mollycafe25.hint == "") and not (ev_mollycafe25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe25.hint:
                        textbutton _("[ev_mollycafe25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe25.hint]")
                if (not ev_mollycafe25p2.hint == "") and not (ev_mollycafe25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe25p2.hint:
                        textbutton _("[ev_mollycafe25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe25p2.hint]")
                if (not ev_mollydorm25.hint == "") and not (ev_mollydorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm25.hint:
                        textbutton _("[ev_mollydorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm25.hint]")
                if (not ev_mollydorm30.hint == "") and not (ev_mollydorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydorm30.hint:
                        textbutton _("[ev_mollydorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydorm30.hint]")

            if Tsuneyo.active:
                if (not ev_ramen15.hint == "") and not (ev_ramen15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen15.hint:
                        textbutton _("[ev_ramen15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen15.hint]")
                if (not ev_tsuneyodorm15.hint == "") and not (ev_tsuneyodorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyodorm15.hint:
                        textbutton _("[ev_tsuneyodorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyodorm15.hint]")
                if (not ev_tsuneyodorm20.hint == "") and not (ev_tsuneyodorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyodorm20.hint:
                        textbutton _("[ev_tsuneyodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyodorm20.hint]")
                    text ("")
                if (not ev_ramen20.hint == "") and not (ev_ramen20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen20.hint:
                        textbutton _("[ev_ramen20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen20.hint]")
                if (not ev_ramen25.hint == "") and not (ev_ramen25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen25.hint:
                        textbutton _("[ev_ramen25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen25.hint]")
                if (not ev_ramen25p2.hint == "") and not (ev_ramen25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen25p2.hint:
                        textbutton _("[ev_ramen25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen25p2.hint]")
                if (not ev_tsuneyodorm25.hint == "") and not (ev_tsuneyodorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyodorm25.hint:
                        textbutton _("[ev_tsuneyodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyodorm25.hint]")
                if (not ev_ramen30.hint == "") and not (ev_ramen30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ramen30.hint:
                        textbutton _("[ev_ramen30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ramen30.hint]")

            if Sara.active:
                if (not ev_saradate10.hint == "") and not (ev_saradate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saradate10.hint:
                        textbutton _("[ev_saradate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saradate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saradate10.hint]")
                if (not ev_sarabar20.hint == "") and not (ev_sarabar20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarabar20.hint:
                        textbutton _("[ev_sarabar20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarabar20.hint]")
                if (not ev_sarabar25.hint == "") and not (ev_sarabar25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarabar25.hint:
                        textbutton _("[ev_sarabar25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarabar25.hint]")
                if (not ev_sarabar25p2.hint == "") and not (ev_sarabar25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarabar25p2.hint:
                        textbutton _("[ev_sarabar25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarabar25p2.hint]")
                    text ("")
                if (not ev_saralust20.hint == "") and not (ev_saralust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saralust20.hint:
                        textbutton _("[ev_saralust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saralust20.hint]")

            if Haruka.active:
                if (not ev_harukainvite1.hint == "") and not (ev_harukainvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukainvite1.hint:
                        textbutton _("[ev_harukainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukainvite1.hint]")
                if (not ev_harukainvite2.hint == "") and not (ev_harukainvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukainvite2.hint:
                        textbutton _("[ev_harukainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukainvite2.hint]")
                if (not ev_harukadate20.hint == "") and not (ev_harukadate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate20.hint:
                        textbutton _("[ev_harukadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate20.hint]")
                if (not ev_harukainvite3.hint == "") and not (ev_harukainvite3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukainvite3.hint:
                        textbutton _("[ev_harukainvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukainvite3.hint]")

            if Maki.active:
                if (not ev_makidate10.hint == "") and not (ev_makidate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makidate10.hint:
                        textbutton _("[ev_makidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makidate10.hint]")
                if (not ev_makiday351.hint == "") and not (ev_makiday351.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makiday351.hint:
                        textbutton _("[ev_makiday351.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiday351), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makiday351.hint]")
                if (not ev_makidate15.hint == "") and not (ev_makidate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makidate15.hint:
                        textbutton _("[ev_makidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makidate15.hint]")
                if (not ev_makiinvite1.hint == "") and not (ev_makiinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makiinvite1.hint:
                        textbutton _("[ev_makiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makiinvite1.hint]")
                if (not ev_makiinvite2.hint == "") and not (ev_makiinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makiinvite2.hint:
                        textbutton _("[ev_makiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makiinvite2.hint]")

            if Kirin.active:
                if (not ev_kirinlust5.hint == "") and not (ev_kirinlust5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinlust5.hint:
                        textbutton _("[ev_kirinlust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinlust5.hint]")
                if (not ev_kirininvite1.hint == "") and not (ev_kirininvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirininvite1.hint:
                        textbutton _("[ev_kirininvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirininvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirininvite1.hint]")
                if (not ev_kirininvite2.hint == "") and not (ev_kirininvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirininvite2.hint:
                        textbutton _("[ev_kirininvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirininvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirininvite2.hint]")
                if (not ev_kirinfirsthall.hint == "") and not (ev_kirinfirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinfirsthall.hint:
                        textbutton _("[ev_kirinfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinfirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinfirsthall.hint]")
                if (not ev_kirindorm10.hint == "") and not (ev_kirindorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindorm10.hint:
                        textbutton _("[ev_kirindorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindorm10.hint]")
                if (not ev_kirinsoccer15.hint == "") and not (ev_kirinsoccer15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinsoccer15.hint:
                        textbutton _("[ev_kirinsoccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinsoccer15.hint]")
                if (not ev_kirinsoccer20.hint == "") and not (ev_kirinsoccer20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinsoccer20.hint:
                        textbutton _("[ev_kirinsoccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinsoccer20.hint]")
                if (not ev_kirindorm15.hint == "") and not (ev_kirindorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindorm15.hint:
                        textbutton _("[ev_kirindorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindorm15.hint]")
                if (not ev_kirindorm20.hint == "") and not (ev_kirindorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindorm20.hint:
                        textbutton _("[ev_kirindorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindorm20.hint]")
                if (not ev_kirindate25.hint == "") and not (ev_kirindate25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindate25.hint:
                        textbutton _("[ev_kirindate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindate25.hint]")
                if (not ev_kirinlust20.hint == "") and not (ev_kirinlust20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinlust20.hint:
                        textbutton _("[ev_kirinlust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinlust20.hint]")
                if (not ev_kirinspecial25.hint == "") and not (ev_kirinspecial25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinspecial25.hint:
                        textbutton _("[ev_kirinspecial25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinspecial25.hint]")
                if (not ev_kirindorm25.hint == "") and not (ev_kirindorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirindorm25.hint:
                        textbutton _("[ev_kirindorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirindorm25.hint]")
                if (not ev_kirinsoccer25.hint == "") and not (ev_kirinsoccer25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinsoccer25.hint:
                        textbutton _("[ev_kirinsoccer25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinsoccer25.hint]")
                if (not ev_kirinspecial30.hint == "") and not (ev_kirinspecial30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinspecial30.hint:
                        textbutton _("[ev_kirinspecial30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinspecial30.hint]")
                if (not ev_kirinlust202.hint == "") and not (ev_kirinlust202.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinlust202.hint:
                        textbutton _("[ev_kirinlust202.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust202), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinlust202.hint]")

            if Karin.active:
                if (not ev_karindate15.hint == "") and not (ev_karindate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate15.hint:
                        textbutton _("[ev_karindate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate15.hint]")
                if (not ev_karinsoccer15.hint == "") and not (ev_karinsoccer15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karinsoccer15.hint:
                        textbutton _("[ev_karinsoccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinsoccer15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karinsoccer15.hint]")
                if (not ev_karinsoccer20.hint == "") and not (ev_karinsoccer20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karinsoccer20.hint:
                        textbutton _("[ev_karinsoccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinsoccer20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karinsoccer20.hint]")
                if (not ev_karindate20.hint == "") and not (ev_karindate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate20.hint:
                        textbutton _("[ev_karindate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate20.hint]")

            if Kaori.active:
                if (not ev_kaoridate15.hint == "") and not (ev_kaoridate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate15.hint:
                        textbutton _("[ev_kaoridate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate15.hint]")
                if (not ev_kaoridate15p2.hint == "") and not (ev_kaoridate15p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate15p2.hint:
                        textbutton _("[ev_kaoridate15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate15p2.hint]")
                if (not ev_kaoridate15p3.hint == "") and not (ev_kaoridate15p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate15p3.hint:
                        textbutton _("[ev_kaoridate15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate15p3.hint]")
                if (not ev_kaoridate20.hint == "") and not (ev_kaoridate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate20.hint:
                        textbutton _("[ev_kaoridate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate20.hint]")
                if (not ev_kaoridate25.hint == "") and not (ev_kaoridate25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate25.hint:
                        textbutton _("[ev_kaoridate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate25.hint]")

            if Chinami.active:
                if (not ev_chinamidate10.hint == "") and not (ev_chinamidate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate10.hint:
                        textbutton _("[ev_chinamidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate10.hint]")
                if (not ev_chinamidate15.hint == "") and not (ev_chinamidate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate15.hint:
                        textbutton _("[ev_chinamidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate15.hint]")
                if (not ev_chinamidate20.hint == "") and not (ev_chinamidate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate20.hint:
                        textbutton _("[ev_chinamidate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate20.hint]")
                if (not ev_christmas1.hint == "") and not (ev_christmas1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas1.hint:
                        textbutton _("[ev_christmas1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas1.hint]")
                if (not ev_christmas2.hint == "") and not (ev_christmas2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas2.hint:
                        textbutton _("[ev_christmas2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas2.hint]")
                if (not ev_christmas3.hint == "") and not (ev_christmas3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas3.hint:
                        textbutton _("[ev_christmas3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas3.hint]")
                if (not ev_christmas4.hint == "") and not (ev_christmas4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas4.hint:
                        textbutton _("[ev_christmas4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas4.hint]")
                if (not ev_christmas5.hint == "") and not (ev_christmas5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas5.hint:
                        textbutton _("[ev_christmas5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas5.hint]")
                if (not ev_christmas6.hint == "") and not (ev_christmas6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas6.hint:
                        textbutton _("[ev_christmas6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas6.hint]")
                if (not ev_christmas7.hint == "") and not (ev_christmas7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmas7.hint:
                        textbutton _("[ev_christmas7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmas7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmas7.hint]")
                    text ("")
                if (not ev_day237.hint == "") and not (ev_day237.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day237.hint:
                        textbutton _("[ev_day237.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day237), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day237.hint]")
                if (not ev_day239.hint == "") and not (ev_day239.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day239.hint:
                        textbutton _("[ev_day239.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day239), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day239.hint]")
                if (not ev_day240.hint == "") and not (ev_day240.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day240.hint:
                        textbutton _("[ev_day240.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day240), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day240.hint]")
                if (not ev_day244.hint == "") and not (ev_day244.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day244.hint:
                        textbutton _("[ev_day244.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day244), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day244.hint]")
                if (not ev_day246.hint == "") and not (ev_day246.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day246.hint:
                        textbutton _("[ev_day246.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day246), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day246.hint]")
                    text ("")
                if (not ev_day247.hint == "") and not (ev_day247.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day247.hint:
                        textbutton _("[ev_day247.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day247), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day247.hint]")
                if (not ev_day261.hint == "") and not (ev_day261.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day261.hint:
                        textbutton _("[ev_day261.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day261), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day261.hint]")
                if (not ev_day263.hint == "") and not (ev_day263.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day263.hint:
                        textbutton _("[ev_day263.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day263), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day263.hint]")
                if (not ev_day264.hint == "") and not (ev_day264.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day264.hint:
                        textbutton _("[ev_day264.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day264), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day264.hint]")
                if (not ev_day269.hint == "") and not (ev_day269.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day269.hint:
                        textbutton _("[ev_day269.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day269), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day269.hint]")
                if (not ev_day270.hint == "") and not (ev_day270.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day270.hint:
                        textbutton _("[ev_day270.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day270), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day270.hint]")
                if (not ev_day271.hint == "") and not (ev_day271.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day271.hint:
                        textbutton _("[ev_day271.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day271), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day271.hint]")
                if (not ev_day280.hint == "") and not (ev_day280.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day280.hint:
                        textbutton _("[ev_day280.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day280), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day280.hint]")
                if (not ev_day281.hint == "") and not (ev_day281.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day281.hint:
                        textbutton _("[ev_day281.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day281), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day281.hint]")
                if (not ev_day282.hint == "") and not (ev_day282.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day282.hint:
                        textbutton _("[ev_day282.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day282), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day282.hint]")
                if (not ev_day283.hint == "") and not (ev_day283.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day283.hint:
                        textbutton _("[ev_day283.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day283), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day283.hint]")
                if (not ev_day287.hint == "") and not (ev_day287.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day287.hint:
                        textbutton _("[ev_day287.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day287), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day287.hint]")
                if (not ev_day288.hint == "") and not (ev_day288.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day288.hint:
                        textbutton _("[ev_day288.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day288), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day288.hint]")
                if (not ev_day295.hint == "") and not (ev_day295.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day295.hint:
                        textbutton _("[ev_day295.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day295), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day295.hint]")
                if (not ev_day295parttwo.hint == "") and not (ev_day295parttwo.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day295parttwo.hint:
                        textbutton _("[ev_day295parttwo.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day295parttwo), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day295parttwo.hint]")
                if (not ev_day297.hint == "") and not (ev_day297.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day297.hint:
                        textbutton _("[ev_day297.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day297), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day297.hint]")
                if (not ev_day302.hint == "") and not (ev_day302.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day302.hint:
                        textbutton _("[ev_day302.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day302), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day302.hint]")
                if (not ev_day303.hint == "") and not (ev_day303.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day303.hint:
                        textbutton _("[ev_day303.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day303), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day303.hint]")
                if (not ev_day304.hint == "") and not (ev_day304.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day304.hint:
                        textbutton _("[ev_day304.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day304), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day304.hint]")
                    text ("")
                if (not ev_day318.hint == "") and not (ev_day318.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day318.hint:
                        textbutton _("[ev_day318.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day318), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day318.hint]")
                if (not ev_dormwar1.hint == "") and not (ev_dormwar1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar1.hint:
                        textbutton _("[ev_dormwar1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar1.hint]")
                if (not ev_dormwar2.hint == "") and not (ev_dormwar2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar2.hint:
                        textbutton _("[ev_dormwar2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar2.hint]")
                if (not ev_dormwar3.hint == "") and not (ev_dormwar3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar3.hint:
                        textbutton _("[ev_dormwar3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar3.hint]")
                if (not ev_dormwar4.hint == "") and not (ev_dormwar4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar4.hint:
                        textbutton _("[ev_dormwar4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar4.hint]")
                    text ("")
                if (not ev_dormwar5.hint == "") and not (ev_dormwar5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar5.hint:
                        textbutton _("[ev_dormwar5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar5.hint]")
                if (not ev_dormwar6.hint == "") and not (ev_dormwar6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar6.hint:
                        textbutton _("[ev_dormwar6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar6.hint]")
                if (not ev_dormwar7.hint == "") and not (ev_dormwar7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar7.hint:
                        textbutton _("[ev_dormwar7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar7.hint]")
                    text ("")
                if (not ev_dormwar8.hint == "") and not (ev_dormwar8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar8.hint:
                        textbutton _("[ev_dormwar8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar8.hint]")
                if (not ev_dormwar9.hint == "") and not (ev_dormwar9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar9.hint:
                        textbutton _("[ev_dormwar9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar9.hint]")
                if (not ev_dormwar10.hint == "") and not (ev_dormwar10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar10.hint:
                        textbutton _("[ev_dormwar10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar10.hint]")
                if (not ev_dormwar11.hint == "") and not (ev_dormwar11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar11.hint:
                        textbutton _("[ev_dormwar11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar11.hint]")
                    text ("")
                if (not ev_dormwar12.hint == "") and not (ev_dormwar12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar12.hint:
                        textbutton _("[ev_dormwar12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar12.hint]")
                if (not ev_dormwar13.hint == "") and not (ev_dormwar13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar13.hint:
                        textbutton _("[ev_dormwar13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar13.hint]")
                if (not ev_dormwar14.hint == "") and not (ev_dormwar14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar14.hint:
                        textbutton _("[ev_dormwar14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar14.hint]")
                if (not ev_dormwar15.hint == "") and not (ev_dormwar15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar15.hint:
                        textbutton _("[ev_dormwar15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar15.hint]")
                if (not ev_dormwar16.hint == "") and not (ev_dormwar16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar16.hint:
                        textbutton _("[ev_dormwar16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar16.hint]")
                if (not ev_dormwar17.hint == "") and not (ev_dormwar17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwar17.hint:
                        textbutton _("[ev_dormwar17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwar17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwar17.hint]")
                if (not ev_day333.hint == "") and not (ev_day333.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day333.hint:
                        textbutton _("[ev_day333.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day333), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day333.hint]")
                if (not ev_day333part2.hint == "") and not (ev_day333part2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day333part2.hint:
                        textbutton _("[ev_day333part2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day333part2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day333part2.hint]")
                if (not ev_day340.hint == "") and not (ev_day340.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day340.hint:
                        textbutton _("[ev_day340.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day340), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day340.hint]")
                if (not ev_day344.hint == "") and not (ev_day344.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day344.hint:
                        textbutton _("[ev_day344.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day344), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day344.hint]")
                if (not ev_thirdreset1.hint == "") and not (ev_thirdreset1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_thirdreset1.hint:
                        textbutton _("[ev_thirdreset1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_thirdreset1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_thirdreset1.hint]")
                if (not ev_thirdreset2.hint == "") and not (ev_thirdreset2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_thirdreset2.hint:
                        textbutton _("[ev_thirdreset2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_thirdreset2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_thirdreset2.hint]")
                if (not ev_thirdreset3.hint == "") and not (ev_thirdreset3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_thirdreset3.hint:
                        textbutton _("[ev_thirdreset3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_thirdreset3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_thirdreset3.hint]")
                if (not ev_day351.hint == "") and not (ev_day351.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day351.hint:
                        textbutton _("[ev_day351.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day351), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day351.hint]")
                if (not ev_day355.hint == "") and not (ev_day355.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day355.hint:
                        textbutton _("[ev_day355.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day355), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day355.hint]")
                if (not ev_secondbeach1.hint == "") and not (ev_secondbeach1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach1.hint:
                        textbutton _("[ev_secondbeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach1.hint]")
                if (not ev_secondbeach2.hint == "") and not (ev_secondbeach2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach2.hint:
                        textbutton _("[ev_secondbeach2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach2.hint]")
                if (not ev_secondbeach3.hint == "") and not (ev_secondbeach3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach3.hint:
                        textbutton _("[ev_secondbeach3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach3.hint]")
                if (not ev_secondbeach4.hint == "") and not (ev_secondbeach4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach4.hint:
                        textbutton _("[ev_secondbeach4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach4.hint]")
                if (not ev_secondbeach5.hint == "") and not (ev_secondbeach5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach5.hint:
                        textbutton _("[ev_secondbeach5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach5.hint]")
                if (not ev_secondbeach6.hint == "") and not (ev_secondbeach6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach6.hint:
                        textbutton _("[ev_secondbeach6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach6.hint]")
                if (not ev_secondbeach7.hint == "") and not (ev_secondbeach7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach7.hint:
                        textbutton _("[ev_secondbeach7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach7.hint]")
                    text ("")
                if (not ev_secondbeach8.hint == "") and not (ev_secondbeach8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach8.hint:
                        textbutton _("[ev_secondbeach8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach8.hint]")
                    text ("")
                if (not ev_secondbeach9.hint == "") and not (ev_secondbeach9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach9.hint:
                        textbutton _("[ev_secondbeach9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach9.hint]")
                if (not ev_secondbeach10.hint == "") and not (ev_secondbeach10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach10.hint:
                        textbutton _("[ev_secondbeach10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach10.hint]")
                    text ("")
                if (not ev_secondbeach11.hint == "") and not (ev_secondbeach11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach11.hint:
                        textbutton _("[ev_secondbeach11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach11.hint]")
                if (not ev_secondbeach12.hint == "") and not (ev_secondbeach12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach12.hint:
                        textbutton _("[ev_secondbeach12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach12.hint]")
                if (not ev_secondbeach13.hint == "") and not (ev_secondbeach13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach13.hint:
                        textbutton _("[ev_secondbeach13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach13.hint]")
                if (not ev_secondbeach14.hint == "") and not (ev_secondbeach14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach14.hint:
                        textbutton _("[ev_secondbeach14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach14.hint]")
                if (not ev_secondbeach15.hint == "") and not (ev_secondbeach15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach15.hint:
                        textbutton _("[ev_secondbeach15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach15.hint]")
                if (not ev_secondbeach16.hint == "") and not (ev_secondbeach16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach16.hint:
                        textbutton _("[ev_secondbeach16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach16.hint]")
                if (not ev_secondbeach17.hint == "") and not (ev_secondbeach17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach17.hint:
                        textbutton _("[ev_secondbeach17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach17.hint]")
                if (not ev_secondbeach18.hint == "") and not (ev_secondbeach18.hint == "Event will trigger automatically."):
                    if "(!)" in ev_secondbeach18.hint:
                        textbutton _("[ev_secondbeach18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_secondbeach18), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_secondbeach18.hint]")
                    text ("")
                if (not ev_halloweentwo1.hint == "") and not (ev_halloweentwo1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo1.hint:
                        textbutton _("[ev_halloweentwo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo1.hint]")
                if (not ev_halloweentwo2.hint == "") and not (ev_halloweentwo2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo2.hint:
                        textbutton _("[ev_halloweentwo2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo2.hint]")
                if (not ev_halloweentwo3.hint == "") and not (ev_halloweentwo3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo3.hint:
                        textbutton _("[ev_halloweentwo3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo3.hint]")
                if (not ev_halloweentwo4.hint == "") and not (ev_halloweentwo4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo4.hint:
                        textbutton _("[ev_halloweentwo4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo4.hint]")
                if (not ev_halloweentwo5.hint == "") and not (ev_halloweentwo5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo5.hint:
                        textbutton _("[ev_halloweentwo5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo5.hint]")
                if (not ev_halloweentwo6.hint == "") and not (ev_halloweentwo6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo6.hint:
                        textbutton _("[ev_halloweentwo6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo6.hint]")
                if (not ev_halloweentwo7.hint == "") and not (ev_halloweentwo7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo7.hint:
                        textbutton _("[ev_halloweentwo7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo7.hint]")
                    text ("")
                if (not ev_halloweentwo8.hint == "") and not (ev_halloweentwo8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo8.hint:
                        textbutton _("[ev_halloweentwo8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo8.hint]")
                if (not ev_halloweentwo9.hint == "") and not (ev_halloweentwo9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo9.hint:
                        textbutton _("[ev_halloweentwo9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo9.hint]")
                if (not ev_halloweentwo10.hint == "") and not (ev_halloweentwo10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo10.hint:
                        textbutton _("[ev_halloweentwo10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo10.hint]")
                if (not ev_halloweentwo11.hint == "") and not (ev_halloweentwo11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo11.hint:
                        textbutton _("[ev_halloweentwo11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo11.hint]")
                if (not ev_halloweentwo12.hint == "") and not (ev_halloweentwo12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo12.hint:
                        textbutton _("[ev_halloweentwo12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo12.hint]")
                if (not ev_halloweentwo13.hint == "") and not (ev_halloweentwo13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweentwo13.hint:
                        textbutton _("[ev_halloweentwo13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentwo13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweentwo13.hint]")
                if (not ev_christmastwo1.hint == "") and not (ev_christmastwo1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo1.hint:
                        textbutton _("[ev_christmastwo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo1.hint]")
                if (not ev_christmastwo2.hint == "") and not (ev_christmastwo2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo2.hint:
                        textbutton _("[ev_christmastwo2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo2.hint]")
                    text ("")
                if (not ev_christmastwo3.hint == "") and not (ev_christmastwo3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo3.hint:
                        textbutton _("[ev_christmastwo3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo3.hint]")
                if (not ev_christmastwo4.hint == "") and not (ev_christmastwo4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo4.hint:
                        textbutton _("[ev_christmastwo4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo4.hint]")
                if (not ev_christmastwo5.hint == "") and not (ev_christmastwo5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo5.hint:
                        textbutton _("[ev_christmastwo5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo5.hint]")
                if (not ev_christmastwo6.hint == "") and not (ev_christmastwo6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo6.hint:
                        textbutton _("[ev_christmastwo6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo6.hint]")
                if (not ev_christmastwo7.hint == "") and not (ev_christmastwo7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo7.hint:
                        textbutton _("[ev_christmastwo7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo7.hint]")
                if (not ev_christmastwo8.hint == "") and not (ev_christmastwo8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo8.hint:
                        textbutton _("[ev_christmastwo8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo8.hint]")
                if (not ev_christmastwo9.hint == "") and not (ev_christmastwo9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo9.hint:
                        textbutton _("[ev_christmastwo9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo9.hint]")
                if (not ev_christmastwo10.hint == "") and not (ev_christmastwo10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo10.hint:
                        textbutton _("[ev_christmastwo10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo10.hint]")
                if (not ev_christmastwo11.hint == "") and not (ev_christmastwo11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo11.hint:
                        textbutton _("[ev_christmastwo11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo11.hint]")
                if (not ev_christmastwo12.hint == "") and not (ev_christmastwo12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo12.hint:
                        textbutton _("[ev_christmastwo12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo12.hint]")
                if (not ev_christmastwo13.hint == "") and not (ev_christmastwo13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo13.hint:
                        textbutton _("[ev_christmastwo13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo13.hint]")
                if (not ev_christmastwo14.hint == "") and not (ev_christmastwo14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo14.hint:
                        textbutton _("[ev_christmastwo14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo14.hint]")
                if (not ev_christmastwo15.hint == "") and not (ev_christmastwo15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo15.hint:
                        textbutton _("[ev_christmastwo15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo15.hint]")
                if (not ev_christmastwo16.hint == "") and not (ev_christmastwo16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo16.hint:
                        textbutton _("[ev_christmastwo16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo16.hint]")
                if (not ev_christmastwo17.hint == "") and not (ev_christmastwo17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo17.hint:
                        textbutton _("[ev_christmastwo17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo17.hint]")
                if (not ev_christmastwo18.hint == "") and not (ev_christmastwo18.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo18.hint:
                        textbutton _("[ev_christmastwo18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo18), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo18.hint]")
                if (not ev_christmastwo19.hint == "") and not (ev_christmastwo19.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo19.hint:
                        textbutton _("[ev_christmastwo19.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo19), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo19.hint]")
                if (not ev_christmastwo20.hint == "") and not (ev_christmastwo20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_christmastwo20.hint:
                        textbutton _("[ev_christmastwo20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastwo20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_christmastwo20.hint]")
                if (not ev_returntosummer1.hint == "") and not (ev_returntosummer1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_returntosummer1.hint:
                        textbutton _("[ev_returntosummer1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_returntosummer1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_returntosummer1.hint]")
                if (not ev_returntosummer2.hint == "") and not (ev_returntosummer2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_returntosummer2.hint:
                        textbutton _("[ev_returntosummer2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_returntosummer2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_returntosummer2.hint]")
                if (not ev_returntosummer3.hint == "") and not (ev_returntosummer3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_returntosummer3.hint:
                        textbutton _("[ev_returntosummer3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_returntosummer3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_returntosummer3.hint]")
                    text ("")

            if Yuki.active:
                if (not ev_yukidate1.hint == "") and not (ev_yukidate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate1.hint:
                        textbutton _("[ev_yukidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate1.hint]")
                if (not ev_yukidate5.hint == "") and not (ev_yukidate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate5.hint:
                        textbutton _("[ev_yukidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate5.hint]")
                if (not ev_yukidate10.hint == "") and not (ev_yukidate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate10.hint:
                        textbutton _("[ev_yukidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate10.hint]")
                if (not ev_yukidate10p2.hint == "") and not (ev_yukidate10p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate10p2.hint:
                        textbutton _("[ev_yukidate10p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate10p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate10p2.hint]")

            if Wakana.active:
                if (not ev_wakanadate1.hint == "") and not (ev_wakanadate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate1.hint:
                        textbutton _("[ev_wakanadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate1.hint]")
                if (not ev_wakanadate5.hint == "") and not (ev_wakanadate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate5.hint:
                        textbutton _("[ev_wakanadate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate5.hint]")

            if Osako.active:
                if (not ev_osakodate1.hint == "") and not (ev_osakodate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_osakodate1.hint:
                        textbutton _("[ev_osakodate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_osakodate1.hint]")
                if (not ev_osakodojo1.hint == "") and not (ev_osakodojo1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_osakodojo1.hint:
                        textbutton _("[ev_osakodojo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodojo1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_osakodojo1.hint]")

            if Tsubasa.active:
                if (not ev_tsubasadate1.hint == "") and not (ev_tsubasadate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsubasadate1.hint:
                        textbutton _("[ev_tsubasadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsubasadate1.hint]")
                    text ("")
                if (not ev_tsubasadate1p2.hint == "") and not (ev_tsubasadate1p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsubasadate1p2.hint:
                        textbutton _("[ev_tsubasadate1p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate1p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsubasadate1p2.hint]")

            if Uta.active:
                if (not ev_utafirsthall.hint == "") and not (ev_utafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utafirsthall.hint:
                        textbutton _("[ev_utafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utafirsthall.hint]")
                if (not ev_utamaid1.hint == "") and not (ev_utamaid1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid1.hint:
                        textbutton _("[ev_utamaid1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid1.hint]")
                if (not ev_utamaid5.hint == "") and not (ev_utamaid5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid5.hint:
                        textbutton _("[ev_utamaid5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid5.hint]")
                if (not ev_utadorm5.hint == "") and not (ev_utadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm5.hint:
                        textbutton _("[ev_utadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm5.hint]")
                if (not ev_utadorm10.hint == "") and not (ev_utadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm10.hint:
                        textbutton _("[ev_utadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm10.hint]")
                if (not ev_utamaid10.hint == "") and not (ev_utamaid10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid10.hint:
                        textbutton _("[ev_utamaid10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid10.hint]")
                if (not ev_utadorm15.hint == "") and not (ev_utadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm15.hint:
                        textbutton _("[ev_utadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm15.hint]")
                if (not ev_utamaid20.hint == "") and not (ev_utamaid20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid20.hint:
                        textbutton _("[ev_utamaid20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid20.hint]")
                    text ("")
                if (not ev_utadorm20.hint == "") and not (ev_utadorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm20.hint:
                        textbutton _("[ev_utadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm20.hint]")

            if Io.active:
                if (not ev_iofirsthall.hint == "") and not (ev_iofirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iofirsthall.hint:
                        textbutton _("[ev_iofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iofirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iofirsthall.hint]")
                if (not ev_bathhouse1.hint == "") and not (ev_bathhouse1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse1.hint:
                        textbutton _("[ev_bathhouse1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse1.hint]")
                if (not ev_bathhouse5.hint == "") and not (ev_bathhouse5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse5.hint:
                        textbutton _("[ev_bathhouse5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse5.hint]")
                if (not ev_iodorm5.hint == "") and not (ev_iodorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iodorm5.hint:
                        textbutton _("[ev_iodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iodorm5.hint]")
                if (not ev_iodorm10.hint == "") and not (ev_iodorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iodorm10.hint:
                        textbutton _("[ev_iodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iodorm10.hint]")
                if (not ev_bathhouse10.hint == "") and not (ev_bathhouse10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse10.hint:
                        textbutton _("[ev_bathhouse10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse10.hint]")
                if (not ev_iodorm15.hint == "") and not (ev_iodorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iodorm15.hint:
                        textbutton _("[ev_iodorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iodorm15.hint]")
                if (not ev_bathhouse20.hint == "") and not (ev_bathhouse20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse20.hint:
                        textbutton _("[ev_bathhouse20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse20.hint]")
                if (not ev_bathhouse20part2.hint == "") and not (ev_bathhouse20part2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse20part2.hint:
                        textbutton _("[ev_bathhouse20part2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse20part2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse20part2.hint]")

            if Noriko.active:
                if (not ev_norikofirsthall.hint == "") and not (ev_norikofirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikofirsthall.hint:
                        textbutton _("[ev_norikofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikofirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikofirsthall.hint]")
                if (not ev_convenience1.hint == "") and not (ev_convenience1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_convenience1.hint:
                        textbutton _("[ev_convenience1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_convenience1.hint]")
                if (not ev_norikodorm5.hint == "") and not (ev_norikodorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodorm5.hint:
                        textbutton _("[ev_norikodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodorm5.hint]")
                if (not ev_convenience5.hint == "") and not (ev_convenience5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_convenience5.hint:
                        textbutton _("[ev_convenience5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_convenience5.hint]")
                if (not ev_norikodorm10.hint == "") and not (ev_norikodorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodorm10.hint:
                        textbutton _("[ev_norikodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodorm10.hint]")
                if (not ev_norikoinvite1.hint == "") and not (ev_norikoinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikoinvite1.hint:
                        textbutton _("[ev_norikoinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikoinvite1.hint]")
                if (not ev_norikoinvite2.hint == "") and not (ev_norikoinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikoinvite2.hint:
                        textbutton _("[ev_norikoinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikoinvite2.hint]")
                    text ("")
                if (not ev_norikospecial20.hint == "") and not (ev_norikospecial20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikospecial20.hint:
                        textbutton _("[ev_norikospecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospecial20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikospecial20.hint]")
                if (not ev_norikodorm20.hint == "") and not (ev_norikodorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodorm20.hint:
                        textbutton _("[ev_norikodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodorm20.hint]")
                if (not ev_convenience25.hint == "") and not (ev_convenience25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_convenience25.hint:
                        textbutton _("[ev_convenience25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_convenience25.hint]")
                if (not ev_norikodorm25.hint == "") and not (ev_norikodorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodorm25.hint:
                        textbutton _("[ev_norikodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodorm25.hint]")

            if Niki.active:
                if (not ev_nikidate1.hint == "") and not (ev_nikidate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikidate1.hint:
                        textbutton _("[ev_nikidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikidate1.hint]")
                if (not ev_nikidate5.hint == "") and not (ev_nikidate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikidate5.hint:
                        textbutton _("[ev_nikidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikidate5.hint]")
                if (not ev_nikidate10.hint == "") and not (ev_nikidate10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikidate10.hint:
                        textbutton _("[ev_nikidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikidate10.hint]")
                if (not ev_nikidate15.hint == "") and not (ev_nikidate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikidate15.hint:
                        textbutton _("[ev_nikidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikidate15.hint]")
                if (not ev_nikiinvite1.hint == "") and not (ev_nikiinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikiinvite1.hint:
                        textbutton _("[ev_nikiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikiinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikiinvite1.hint]")
                if (not ev_nikiinvite2.hint == "") and not (ev_nikiinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikiinvite2.hint:
                        textbutton _("[ev_nikiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikiinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikiinvite2.hint]")

            if Nodoka.active:
                if (not ev_nodokafirsthall.hint == "") and not (ev_nodokafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokafirsthall.hint:
                        textbutton _("[ev_nodokafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokafirsthall.hint]")
                if (not ev_nodokadorm1.hint == "") and not (ev_nodokadorm1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokadorm1.hint:
                        textbutton _("[ev_nodokadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokadorm1.hint]")
                if (not ev_nodokalibrary1.hint == "") and not (ev_nodokalibrary1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokalibrary1.hint:
                        textbutton _("[ev_nodokalibrary1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokalibrary1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokalibrary1.hint]")
                if (not ev_nodokalibrary5.hint == "") and not (ev_nodokalibrary5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokalibrary5.hint:
                        textbutton _("[ev_nodokalibrary5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokalibrary5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokalibrary5.hint]")
                if (not ev_nodokadorm5.hint == "") and not (ev_nodokadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokadorm5.hint:
                        textbutton _("[ev_nodokadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokadorm5.hint]")

            if Otoha.active:
                if (not ev_otohafirsthall.hint == "") and not (ev_otohafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohafirsthall.hint:
                        textbutton _("[ev_otohafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohafirsthall.hint]")
                if (not ev_otohadorm1.hint == "") and not (ev_otohadorm1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohadorm1.hint:
                        textbutton _("[ev_otohadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohadorm1.hint]")
                    text ("")
                if (not ev_otohapark1.hint == "") and not (ev_otohapark1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohapark1.hint:
                        textbutton _("[ev_otohapark1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohapark1.hint]")
                    text ("")
                if (not ev_otohapark5.hint == "") and not (ev_otohapark5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohapark5.hint:
                        textbutton _("[ev_otohapark5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohapark5.hint]")
                if (not ev_otohadorm5.hint == "") and not (ev_otohadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohadorm5.hint:
                        textbutton _("[ev_otohadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohadorm5.hint]")
                if (not ev_otohapark10.hint == "") and not (ev_otohapark10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohapark10.hint:
                        textbutton _("[ev_otohapark10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohapark10.hint]")
                if (not ev_otohaspecial10.hint == "") and not (ev_otohaspecial10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohaspecial10.hint:
                        textbutton _("[ev_otohaspecial10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohaspecial10.hint]")
                if (not ev_otohadorm10.hint == "") and not (ev_otohadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohadorm10.hint:
                        textbutton _("[ev_otohadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohadorm10.hint]")
                if (not ev_otohadorm10p2.hint == "") and not (ev_otohadorm10p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohadorm10p2.hint:
                        textbutton _("[ev_otohadorm10p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm10p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohadorm10p2.hint]")

            if Touka.active:
                if (not ev_toukafirsthall.hint == "") and not (ev_toukafirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukafirsthall.hint:
                        textbutton _("[ev_toukafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukafirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukafirsthall.hint]")
                if (not ev_toukastreets1.hint == "") and not (ev_toukastreets1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukastreets1.hint:
                        textbutton _("[ev_toukastreets1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukastreets1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukastreets1.hint]")
                if (not ev_toukadorm1.hint == "") and not (ev_toukadorm1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm1.hint:
                        textbutton _("[ev_toukadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm1.hint]")
                if (not ev_toukastreets5.hint == "") and not (ev_toukastreets5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukastreets5.hint:
                        textbutton _("[ev_toukastreets5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukastreets5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukastreets5.hint]")
                if (not ev_toukadorm5.hint == "") and not (ev_toukadorm5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm5.hint:
                        textbutton _("[ev_toukadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm5.hint]")
                if (not ev_toukadorm10.hint == "") and not (ev_toukadorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm10.hint:
                        textbutton _("[ev_toukadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm10.hint]")
                if (not ev_toukaspecial15.hint == "") and not (ev_toukaspecial15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukaspecial15.hint:
                        textbutton _("[ev_toukaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukaspecial15.hint]")
                if (not ev_toukaspecial15p2.hint == "") and not (ev_toukaspecial15p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukaspecial15p2.hint:
                        textbutton _("[ev_toukaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukaspecial15p2.hint]")
                if (not ev_toukaspecial15p3.hint == "") and not (ev_toukaspecial15p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukaspecial15p3.hint:
                        textbutton _("[ev_toukaspecial15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukaspecial15p3.hint]")

            if Yasu.active:
                if (not ev_yasufirsthall.hint == "") and not (ev_yasufirsthall.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasufirsthall.hint:
                        textbutton _("[ev_yasufirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasufirsthall), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasufirsthall.hint]")
                    text ("")
                if (not ev_church1.hint == "") and not (ev_church1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church1.hint:
                        textbutton _("[ev_church1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church1.hint]")
                if (not ev_church5.hint == "") and not (ev_church5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church5.hint:
                        textbutton _("[ev_church5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church5.hint]")
                if (not ev_yasudorm10.hint == "") and not (ev_yasudorm10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasudorm10.hint:
                        textbutton _("[ev_yasudorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasudorm10.hint]")
                if (not ev_church10.hint == "") and not (ev_church10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church10.hint:
                        textbutton _("[ev_church10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church10.hint]")

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            textbutton _("Back") action ShowMenu("progressmod")
