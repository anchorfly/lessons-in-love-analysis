screen hinttracker3():

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
            if (not ev_buckettrack.hint == "") and not (ev_buckettrack.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_mothersmilk.hint == "") and not (ev_mothersmilk.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_amyevent.hint == "") and not (ev_amyevent.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"
            if (not ev_rainking.hint == "") and not (ev_rainking.hint == "Event will trigger automatically."):
                textbutton _("Happy event") action ShowMenu("secrettrackerm") style "event_button" text_style "hint_text"

        if Ami.active:
            if (not ev_amilust35.hint == "") and not (ev_amilust35.hint == "Event will trigger automatically."):
                textbutton _("[ev_amilust35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amimaid50.hint == "") and not (ev_amimaid50.hint == "Event will trigger automatically."):
                textbutton _("[ev_amimaid50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amiinvite4.hint == "") and not (ev_amiinvite4.hint == "Event will trigger automatically."):
                textbutton _("[ev_amiinvite4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amispecial50.hint == "") and not (ev_amispecial50.hint == "Event will trigger automatically."):
                textbutton _("[ev_amispecial50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"
            if (not ev_amilust50.hint == "") and not (ev_amilust50.hint == "Event will trigger automatically."):
                textbutton _("[ev_amilust50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amihint"

        if Maya.active:
            if (not ev_shrine40.hint == "") and not (ev_shrine40.hint == "Event will trigger automatically."):
                textbutton _("[ev_shrine40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayadate45.hint == "") and not (ev_mayadate45.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayadate45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"
            if (not ev_mayaspecial45.hint == "") and not (ev_mayaspecial45.hint == "Event will trigger automatically."):
                textbutton _("[ev_mayaspecial45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayahint"

        if Chika.active:
            if (not ev_chikalust25.hint == "") and not (ev_chikalust25.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikalust25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_mall45.hint == "") and not (ev_mall45.hint == "Event will trigger automatically."):
                textbutton _("[ev_mall45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikaspecial45.hint == "") and not (ev_chikaspecial45.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikaspecial45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"
            if (not ev_chikadorm45.hint == "") and not (ev_chikadorm45.hint == "Event will trigger automatically."):
                textbutton _("[ev_chikadorm45.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikahint"

        if Yumi.active:
            if (not ev_yumislumber1.hint == "") and not (ev_yumislumber1.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumislumber1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumislumber2.hint == "") and not (ev_yumislumber2.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumislumber2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"
            if (not ev_yumislumber3.hint == "") and not (ev_yumislumber3.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumislumber3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumihint"

        if Ayane.active:
            if (not ev_ayanespecial40.hint == "") and not (ev_ayanespecial40.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanespecial40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanesanabeach1.hint == "") and not (ev_ayanesanabeach1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanesanabeach1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanespecial50.hint == "") and not (ev_ayanespecial50.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanespecial50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanekirintalk.hint == "") and not (ev_ayanekirintalk.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanekirintalk.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanespecial55.hint == "") and not (ev_ayanespecial55.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanespecial55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanebonus1.hint == "") and not (ev_ayanebonus1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanebonus1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanebonus2.hint == "") and not (ev_ayanebonus2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanebonus2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"
            if (not ev_ayanepool55.hint == "") and not (ev_ayanepool55.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanepool55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanehint"

        if Sana.active:
            if (not ev_bar55.hint == "") and not (ev_bar55.hint == "Event will trigger automatically."):
                textbutton _("[ev_bar55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_ayanesanabeach2.hint == "") and not (ev_ayanesanabeach2.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanesanabeach2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_ayanesanabeach3.hint == "") and not (ev_ayanesanabeach3.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanesanabeach3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"
            if (not ev_ayanesanabeach4.hint == "") and not (ev_ayanesanabeach4.hint == "Event will trigger automatically."):
                textbutton _("[ev_ayanesanabeach4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanahint"

        if Makoto.active:
            if (not ev_sadgirls1.hint == "") and not (ev_sadgirls1.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_sadgirls7.hint == "") and not (ev_sadgirls7.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotolust30.hint == "") and not (ev_makotolust30.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotolust30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_sadgirls8.hint == "") and not (ev_sadgirls8.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotospecial50.hint == "") and not (ev_makotospecial50.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotospecial50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotopool55.hint == "") and not (ev_makotopool55.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotopool55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotodorm55p1.hint == "") and not (ev_makotodorm55p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotodorm55p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"
            if (not ev_makotodorm55p2.hint == "") and not (ev_makotodorm55p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotodorm55p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotohint"

        if Miku.active:
            if (not ev_mikuinvite1.hint == "") and not (ev_mikuinvite1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikuinvite1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikuinvite2.hint == "") and not (ev_mikuinvite2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikuinvite2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikupool55.hint == "") and not (ev_mikupool55.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikupool55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm55p1.hint == "") and not (ev_mikudorm55p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm55p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"
            if (not ev_mikudorm55p2.hint == "") and not (ev_mikudorm55p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mikudorm55p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikuhint"

        if Futaba.active:
            if (not ev_futabadorm50.hint == "") and not (ev_futabadorm50.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabadorm50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_library50.hint == "") and not (ev_library50.hint == "Event will trigger automatically."):
                textbutton _("[ev_library50.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabainvite3.hint == "") and not (ev_futabainvite3.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabainvite3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_makotofutabafuntimelustevent.hint == "") and not (ev_makotofutabafuntimelustevent.hint == "Event will trigger automatically."):
                textbutton _("[ev_makotofutabafuntimelustevent.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabaspecial60p1.hint == "") and not (ev_futabaspecial60p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabaspecial60p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabaspecial60p2.hint == "") and not (ev_futabaspecial60p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabaspecial60p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"
            if (not ev_futabaspecial60p3.hint == "") and not (ev_futabaspecial60p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_futabaspecial60p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabahint"

        if Rin.active:
            if (not ev_rindorm55.hint == "") and not (ev_rindorm55.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rindorm55p2.hint == "") and not (ev_rindorm55p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_rindorm55p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"
            if (not ev_rinspecial55.hint == "") and not (ev_rinspecial55.hint == "Event will trigger automatically."):
                textbutton _("[ev_rinspecial55.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinhint"

        if Molly.active:
            if (not ev_mollycafe30p1.hint == "") and not (ev_mollycafe30p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe30p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollycafe30p2.hint == "") and not (ev_mollycafe30p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollycafe30p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydate35p1.hint == "") and not (ev_mollydate35p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydate35p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"
            if (not ev_mollydate35p2.hint == "") and not (ev_mollydate35p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_mollydate35p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollyhint"

        if Tsuneyo.active:
            if (not ev_tsuneyoslumber1.hint == "") and not (ev_tsuneyoslumber1.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyoslumber1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyoslumber2.hint == "") and not (ev_tsuneyoslumber2.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyoslumber2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"
            if (not ev_tsuneyoslumber3.hint == "") and not (ev_tsuneyoslumber3.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsuneyoslumber3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyohint"

        if Sara.active:
            if (not ev_saraspecial30p1.hint == "") and not (ev_saraspecial30p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_saraspecial30p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
                text ("")
            if (not ev_saraspecial30p2.hint == "") and not (ev_saraspecial30p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_saraspecial30p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"
            if (not ev_sarabar30.hint == "") and not (ev_sarabar30.hint == "Event will trigger automatically."):
                textbutton _("[ev_sarabar30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "sarahint"

        if Haruka.active:
            if (not ev_sadgirls2.hint == "") and not (ev_sadgirls2.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_sadgirls4.hint == "") and not (ev_sadgirls4.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_sadgirls5.hint == "") and not (ev_sadgirls5.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukalust25.hint == "") and not (ev_harukalust25.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukalust25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_makihornytrip1.hint == "") and not (ev_makihornytrip1.hint == "Event will trigger automatically."):
                textbutton _("[ev_makihornytrip1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_makihornytrip4.hint == "") and not (ev_makihornytrip4.hint == "Event will trigger automatically."):
                textbutton _("[ev_makihornytrip4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"
            if (not ev_harukadate30.hint == "") and not (ev_harukadate30.hint == "Event will trigger automatically."):
                textbutton _("[ev_harukadate30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukahint"

        if Maki.active:
            if (not ev_sadgirls3.hint == "") and not (ev_sadgirls3.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_sadgirls6.hint == "") and not (ev_sadgirls6.hint == "Event will trigger automatically."):
                textbutton _("[ev_sadgirls6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makiinv3.hint == "") and not (ev_makiinv3.hint == "Event will trigger automatically."):
                textbutton _("[ev_makiinv3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makihornyquestintro.hint == "") and not (ev_makihornyquestintro.hint == "Event will trigger automatically."):
                textbutton _("[ev_makihornyquestintro.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makihornytrip2.hint == "") and not (ev_makihornytrip2.hint == "Event will trigger automatically."):
                textbutton _("[ev_makihornytrip2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"
            if (not ev_makihornytrip3.hint == "") and not (ev_makihornytrip3.hint == "Event will trigger automatically."):
                textbutton _("[ev_makihornytrip3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makihint"

        if Kirin.active:
            if (not ev_kirinlust30.hint == "") and not (ev_kirinlust30.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinlust30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinspecial40.hint == "") and not (ev_kirinspecial40.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinspecial40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinspecial45p1.hint == "") and not (ev_kirinspecial45p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinspecial45p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"
            if (not ev_kirinspecial45p2.hint == "") and not (ev_kirinspecial45p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_kirinspecial45p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinhint"

        if Karin.active:
            if (not ev_karindate25.hint == "") and not (ev_karindate25.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"
            if (not ev_karindate30.hint == "") and not (ev_karindate30.hint == "Event will trigger automatically."):
                textbutton _("[ev_karindate30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinhint"

        if Kaori.active:
            if (not ev_kaorispecial35.hint == "") and not (ev_kaorispecial35.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaorispecial35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaorispecial40.hint == "") and not (ev_kaorispecial40.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaorispecial40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
            if (not ev_kaoridate40.hint == "") and not (ev_kaoridate40.hint == "Event will trigger automatically."):
                textbutton _("[ev_kaoridate40.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorihint"
                text ("")

        if Imani.active:
            if (not ev_imanidate1.hint == "") and not (ev_imanidate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanidate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanihint"
            if (not ev_imanidate5.hint == "") and not (ev_imanidate5.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanidate5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanihint"
            if (not ev_imanidate15p1.hint == "") and not (ev_imanidate15p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanidate15p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanihint"
            if (not ev_imanidate15p2.hint == "") and not (ev_imanidate15p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanidate15p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanihint"
            if (not ev_imanispecial15.hint == "") and not (ev_imanispecial15.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanispecial15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanihint"

        if Rika.active:
            if (not ev_rikadate1.hint == "") and not (ev_rikadate1.hint == "Event will trigger automatically."):
                textbutton _("[ev_rikadate1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")] style "event_button" text_style "rikahint"
            if (not ev_rikaspecial2.hint == "") and not (ev_rikaspecial2.hint == "Event will trigger automatically."):
                textbutton _("[ev_rikaspecial2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")] style "event_button" text_style "rikahint"
            if (not ev_rikadive1.hint == "") and not (ev_rikadive1.hint == "Event will trigger automatically."):
                textbutton _("[ev_rikadive1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")] style "event_button" text_style "rikahint"
                text ("")

        if Nao.active:
            if (not ev_naospecial1.hint == "") and not (ev_naospecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_naospecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")] style "event_button" text_style "naohint"
            if (not ev_naospecial2.hint == "") and not (ev_naospecial2.hint == "Event will trigger automatically."):
                textbutton _("[ev_naospecial2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")] style "event_button" text_style "naohint"
            if (not ev_naospecial3.hint == "") and not (ev_naospecial3.hint == "Event will trigger automatically."):
                textbutton _("[ev_naospecial3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")] style "event_button" text_style "naohint"

        if Chinami.active:
            if (not ev_chinamidate25.hint == "") and not (ev_chinamidate25.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_chinamidate30.hint == "") and not (ev_chinamidate30.hint == "Event will trigger automatically."):
                textbutton _("[ev_chinamidate30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamihint"
            if (not ev_chapthree1.hint == "") and not (ev_chapthree1.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree2.hint == "") and not (ev_chapthree2.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree3.hint == "") and not (ev_chapthree3.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree4.hint == "") and not (ev_chapthree4.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree5.hint == "") and not (ev_chapthree5.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree6.hint == "") and not (ev_chapthree6.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_chapthree7.hint == "") and not (ev_chapthree7.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_chapthree8.hint == "") and not (ev_chapthree8.hint == "Event will trigger automatically."):
                textbutton _("[ev_chapthree8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_yumichikaspecial1.hint == "") and not (ev_yumichikaspecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumichikaspecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_yumiyukispecial1.hint == "") and not (ev_yumiyukispecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_yumiyukispecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_imanispecial1.hint == "") and not (ev_imanispecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_imanispecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_rikaspecial1.hint == "") and not (ev_rikaspecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_rikaspecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_day543.hint == "") and not (ev_day543.hint == "Event will trigger automatically."):
                textbutton _("[ev_day543.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo1.hint == "") and not (ev_dormwartwo1.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo2.hint == "") and not (ev_dormwartwo2.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo3.hint == "") and not (ev_dormwartwo3.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo4.hint == "") and not (ev_dormwartwo4.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo5.hint == "") and not (ev_dormwartwo5.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo6.hint == "") and not (ev_dormwartwo6.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo7.hint == "") and not (ev_dormwartwo7.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo8.hint == "") and not (ev_dormwartwo8.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo9.hint == "") and not (ev_dormwartwo9.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo10.hint == "") and not (ev_dormwartwo10.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo11.hint == "") and not (ev_dormwartwo11.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo12.hint == "") and not (ev_dormwartwo12.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo13.hint == "") and not (ev_dormwartwo13.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo14.hint == "") and not (ev_dormwartwo14.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo15.hint == "") and not (ev_dormwartwo15.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_dormwartwo16.hint == "") and not (ev_dormwartwo16.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo17.hint == "") and not (ev_dormwartwo17.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo18.hint == "") and not (ev_dormwartwo18.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo18.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_dormwartwo19.hint == "") and not (ev_dormwartwo19.hint == "Event will trigger automatically."):
                textbutton _("[ev_dormwartwo19.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas1.hint == "") and not (ev_beachmas1.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas2.hint == "") and not (ev_beachmas2.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas3.hint == "") and not (ev_beachmas3.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas4.hint == "") and not (ev_beachmas4.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas5.hint == "") and not (ev_beachmas5.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas6.hint == "") and not (ev_beachmas6.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas7.hint == "") and not (ev_beachmas7.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas8.hint == "") and not (ev_beachmas8.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas9.hint == "") and not (ev_beachmas9.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas10.hint == "") and not (ev_beachmas10.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas11.hint == "") and not (ev_beachmas11.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas12.hint == "") and not (ev_beachmas12.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas13.hint == "") and not (ev_beachmas13.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas14.hint == "") and not (ev_beachmas14.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas15.hint == "") and not (ev_beachmas15.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas16.hint == "") and not (ev_beachmas16.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas17.hint == "") and not (ev_beachmas17.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas18.hint == "") and not (ev_beachmas18.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas18.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachmas19.hint == "") and not (ev_beachmas19.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas19.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_beachmas20.hint == "") and not (ev_beachmas20.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachmas20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_slumberreset1.hint == "") and not (ev_slumberreset1.hint == "Event will trigger automatically."):
                textbutton _("[ev_slumberreset1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_slumberreset2.hint == "") and not (ev_slumberreset2.hint == "Event will trigger automatically."):
                textbutton _("[ev_slumberreset2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_slumberreset3.hint == "") and not (ev_slumberreset3.hint == "Event will trigger automatically."):
                textbutton _("[ev_slumberreset3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_slumberreset4.hint == "") and not (ev_slumberreset4.hint == "Event will trigger automatically."):
                textbutton _("[ev_slumberreset4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_slumberreset5.hint == "") and not (ev_slumberreset5.hint == "Event will trigger automatically."):
                textbutton _("[ev_slumberreset5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_postnodokachain1.hint == "") and not (ev_postnodokachain1.hint == "Event will trigger automatically."):
                textbutton _("[ev_postnodokachain1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_treasureisland.hint == "") and not (ev_treasureisland.hint == "Event will trigger automatically."):
                textbutton _("[ev_treasureisland.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_amispecial50mainp1.hint == "") and not (ev_amispecial50mainp1.hint == "Event will trigger automatically."):
                textbutton _("[ev_amispecial50mainp1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_amispecial50mainp2.hint == "") and not (ev_amispecial50mainp2.hint == "Event will trigger automatically."):
                textbutton _("[ev_amispecial50mainp2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_predormwars3.hint == "") and not (ev_predormwars3.hint == "Event will trigger automatically."):
                textbutton _("[ev_predormwars3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars1.hint == "") and not (ev_beachwars1.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars2.hint == "") and not (ev_beachwars2.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars3.hint == "") and not (ev_beachwars3.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars4.hint == "") and not (ev_beachwars4.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars5.hint == "") and not (ev_beachwars5.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars6.hint == "") and not (ev_beachwars6.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars7.hint == "") and not (ev_beachwars7.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars8.hint == "") and not (ev_beachwars8.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars9.hint == "") and not (ev_beachwars9.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_beachwars10.hint == "") and not (ev_beachwars10.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars11.hint == "") and not (ev_beachwars11.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars12.hint == "") and not (ev_beachwars12.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars13.hint == "") and not (ev_beachwars13.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars14.hint == "") and not (ev_beachwars14.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars15.hint == "") and not (ev_beachwars15.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars16.hint == "") and not (ev_beachwars16.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars17.hint == "") and not (ev_beachwars17.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars17.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars18.hint == "") and not (ev_beachwars18.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars18.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_beachwars19.hint == "") and not (ev_beachwars19.hint == "Event will trigger automatically."):
                textbutton _("[ev_beachwars19.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour1.hint == "") and not (ev_halloweenfour1.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour2.hint == "") and not (ev_halloweenfour2.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour3.hint == "") and not (ev_halloweenfour3.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour4.hint == "") and not (ev_halloweenfour4.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour5.hint == "") and not (ev_halloweenfour5.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour5.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour6.hint == "") and not (ev_halloweenfour6.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour6.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour7.hint == "") and not (ev_halloweenfour7.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour7.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour8.hint == "") and not (ev_halloweenfour8.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour8.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour9.hint == "") and not (ev_halloweenfour9.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour9.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour10.hint == "") and not (ev_halloweenfour10.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour10.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
                text ("")
            if (not ev_halloweenfour11.hint == "") and not (ev_halloweenfour11.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour11.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour12.hint == "") and not (ev_halloweenfour12.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour12.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour13.hint == "") and not (ev_halloweenfour13.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour13.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour14.hint == "") and not (ev_halloweenfour14.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour14.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour15.hint == "") and not (ev_halloweenfour15.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_halloweenfour16.hint == "") and not (ev_halloweenfour16.hint == "Event will trigger automatically."):
                textbutton _("[ev_halloweenfour16.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_resetsix1.hint == "") and not (ev_resetsix1.hint == "Event will trigger automatically."):
                textbutton _("[ev_resetsix1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_resetsix2.hint == "") and not (ev_resetsix2.hint == "Event will trigger automatically."):
                textbutton _("[ev_resetsix2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_resetsix3.hint == "") and not (ev_resetsix3.hint == "Event will trigger automatically."):
                textbutton _("[ev_resetsix3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"
            if (not ev_resetsix4.hint == "") and not (ev_resetsix4.hint == "Event will trigger automatically."):
                textbutton _("[ev_resetsix4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Main")] style "event_button" text_style "mainhint"

        if Yuki.active:
            if (not ev_yukidate20p1.hint == "") and not (ev_yukidate20p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate20p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"
            if (not ev_yukidate20p2.hint == "") and not (ev_yukidate20p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate20p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"
            if (not ev_yukidate25.hint == "") and not (ev_yukidate25.hint == "Event will trigger automatically."):
                textbutton _("[ev_yukidate25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukihint"

        if Wakana.active:
            if (not ev_wakanadate15.hint == "") and not (ev_wakanadate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"
            if (not ev_wakanaspecial15.hint == "") and not (ev_wakanaspecial15.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanaspecial15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"
            if (not ev_wakanadate25p1.hint == "") and not (ev_wakanadate25p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate25p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"
            if (not ev_wakanadate25p2.hint == "") and not (ev_wakanadate25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"
            if (not ev_wakanadate25p3.hint == "") and not (ev_wakanadate25p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_wakanadate25p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanahint"

        if Osako.active:
            if (not ev_osakodate15.hint == "") and not (ev_osakodate15.hint == "Event will trigger automatically."):
                textbutton _("[ev_osakodate15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")] style "event_button" text_style "osakohint"
            if (not ev_osakodate20.hint == "") and not (ev_osakodate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_osakodate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")] style "event_button" text_style "osakohint"

        if Tsubasa.active:
            if (not ev_tsubasaspecial15.hint == "") and not (ev_tsubasaspecial15.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsubasaspecial15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasahint"
            if (not ev_tsubasadate20.hint == "") and not (ev_tsubasadate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsubasadate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasahint"
            if (not ev_tsubasaspecial20.hint == "") and not (ev_tsubasaspecial20.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsubasaspecial20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasahint"

        if Tsukasa.active:
            if (not ev_tsukasaspecial1.hint == "") and not (ev_tsukasaspecial1.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsukasaspecial1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsukasa")] style "event_button" text_style "tsukasahint"
            if (not ev_tsukasaspecial1p2.hint == "") and not (ev_tsukasaspecial1p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_tsukasaspecial1p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsukasa")] style "event_button" text_style "tsukasahint"

        if Uta.active:
            if (not ev_utaarchery1.hint == "") and not (ev_utaarchery1.hint == "Event will trigger automatically."):
                textbutton _("[ev_utaarchery1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid25p1.hint == "") and not (ev_utamaid25p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid25p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utamaid25p2.hint == "") and not (ev_utamaid25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_utamaid25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm30.hint == "") and not (ev_utadorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utaspecial35.hint == "") and not (ev_utaspecial35.hint == "Event will trigger automatically."):
                textbutton _("[ev_utaspecial35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadate35.hint == "") and not (ev_utadate35.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadate35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm40p1.hint == "") and not (ev_utadorm40p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm40p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"
            if (not ev_utadorm40p2.hint == "") and not (ev_utadorm40p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_utadorm40p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utahint"

        if Io.active:
            if (not ev_ioarchery1.hint == "") and not (ev_ioarchery1.hint == "Event will trigger automatically."):
                textbutton _("[ev_ioarchery1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse25.hint == "") and not (ev_bathhouse25.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iodorm25.hint == "") and not (ev_iodorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_iodorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iospecial30.hint == "") and not (ev_iospecial30.hint == "Event will trigger automatically."):
                textbutton _("[ev_iospecial30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
                text ("")
            if (not ev_bathhouse35p1.hint == "") and not (ev_bathhouse35p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse35p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_bathhouse35p2.hint == "") and not (ev_bathhouse35p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_bathhouse35p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_iodorm35.hint == "") and not (ev_iodorm35.hint == "Event will trigger automatically."):
                textbutton _("[ev_iodorm35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"
            if (not ev_ioarchery35.hint == "") and not (ev_ioarchery35.hint == "Event will trigger automatically."):
                textbutton _("[ev_ioarchery35.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iohint"

        if Noriko.active:
            if (not ev_norikodate30.hint == "") and not (ev_norikodate30.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodate30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikodorm30.hint == "") and not (ev_norikodorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikodorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
            if (not ev_norikoinvite3.hint == "") and not (ev_norikoinvite3.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikoinvite3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"
                text ("")
            if (not ev_norikoinvite4.hint == "") and not (ev_norikoinvite4.hint == "Event will trigger automatically."):
                textbutton _("[ev_norikoinvite4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikohint"

        if Niki.active:
            if (not ev_nikilovesyou1.hint == "") and not (ev_nikilovesyou1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikilovesyou1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikilovesyou2.hint == "") and not (ev_nikilovesyou2.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikilovesyou2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
                text ("")
            if (not ev_nikilovesyou3.hint == "") and not (ev_nikilovesyou3.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikilovesyou3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"
            if (not ev_nikifirstlust.hint == "") and not (ev_nikifirstlust.hint == "Event will trigger automatically."):
                textbutton _("[ev_nikifirstlust.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikihint"

        if Nodoka.active:
            if (not ev_nodokadorm15.hint == "") and not (ev_nodokadorm15.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokadorm15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial15p1.hint == "") and not (ev_nodokaspecial15p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial15p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial15p2.hint == "") and not (ev_nodokaspecial15p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial15p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial15p3.hint == "") and not (ev_nodokaspecial15p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial15p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial20.hint == "") and not (ev_nodokaspecial20.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial30p1.hint == "") and not (ev_nodokaspecial30p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial30p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
                text ("")
            if (not ev_nodokaspecial30p2.hint == "") and not (ev_nodokaspecial30p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial30p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial30p3.hint == "") and not (ev_nodokaspecial30p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial30p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"
            if (not ev_nodokaspecial30p4.hint == "") and not (ev_nodokaspecial30p4.hint == "Event will trigger automatically."):
                textbutton _("[ev_nodokaspecial30p4.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokahint"

        if Otoha.active:
            if (not ev_otohaspecial15p1.hint == "") and not (ev_otohaspecial15p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohaspecial15p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohaspecial15p2.hint == "") and not (ev_otohaspecial15p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohaspecial15p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"
            if (not ev_otohadate20.hint == "") and not (ev_otohadate20.hint == "Event will trigger automatically."):
                textbutton _("[ev_otohadate20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohahint"

        if Touka.active:
            if (not ev_toukaarchery20.hint == "") and not (ev_toukaarchery20.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukaarchery20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm25p1.hint == "") and not (ev_toukadorm25p1.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm25p1.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm25p2.hint == "") and not (ev_toukadorm25p2.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm25p2.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"
            if (not ev_toukadorm25p3.hint == "") and not (ev_toukadorm25p3.hint == "Event will trigger automatically."):
                textbutton _("[ev_toukadorm25p3.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukahint"

        if Yasu.active:
            if (not ev_church15.hint == "") and not (ev_church15.hint == "Event will trigger automatically."):
                textbutton _("[ev_church15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasuspecial15.hint == "") and not (ev_yasuspecial15.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasuspecial15.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_church20.hint == "") and not (ev_church20.hint == "Event will trigger automatically."):
                textbutton _("[ev_church20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasudorm20.hint == "") and not (ev_yasudorm20.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasudorm20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasuspecial20.hint == "") and not (ev_yasuspecial20.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasuspecial20.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_church25.hint == "") and not (ev_church25.hint == "Event will trigger automatically."):
                textbutton _("[ev_church25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasudorm25.hint == "") and not (ev_yasudorm25.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasudorm25.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"
            if (not ev_yasudorm30.hint == "") and not (ev_yasudorm30.hint == "Event will trigger automatically."):
                textbutton _("[ev_yasudorm30.girl.colored_name]") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasuhint"

    vbox:
        xpos .33
        ypos .14
        style_prefix "hint"


        if HappyEvent.active:
            if (not ev_buckettrack.hint == "") and not (ev_buckettrack.hint == "Event will trigger automatically."):
                text ("Second Sun")
            if (not ev_mothersmilk.hint == "") and not (ev_mothersmilk.hint == "Event will trigger automatically."):
                text ("Mother's Milk")
            if (not ev_amyevent.hint == "") and not (ev_amyevent.hint == "Event will trigger automatically."):
                text ("Amy")
            if (not ev_rainking.hint == "") and not (ev_rainking.hint == "Event will trigger automatically."):
                text ("Rain King")

        if Ami.active:
            if (not ev_amilust35.hint == "") and not (ev_amilust35.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}No One Can Hear Us{/color}")
            if (not ev_amimaid50.hint == "") and not (ev_amimaid50.hint == "Event will trigger automatically."):
                text ("Not Safe For Work")
            if (not ev_amiinvite4.hint == "") and not (ev_amiinvite4.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Mama's Girl{/color}")
            if (not ev_amispecial50.hint == "") and not (ev_amispecial50.hint == "Event will trigger automatically."):
                text ("Worry Not, The Mason Jar")
            if (not ev_amilust50.hint == "") and not (ev_amilust50.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Family Matters{/color}")

        if Maya.active:
            if (not ev_shrine40.hint == "") and not (ev_shrine40.hint == "Event will trigger automatically."):
                text ("The Sun, And All Its Toxic Rays")
            if (not ev_mayadate45.hint == "") and not (ev_mayadate45.hint == "Event will trigger automatically."):
                text ("Anything & Everything")
            if (not ev_mayaspecial45.hint == "") and not (ev_mayaspecial45.hint == "Event will trigger automatically."):
                text ("A Brutal, Violent Creaming")

        if Chika.active:
            if (not ev_chikalust25.hint == "") and not (ev_chikalust25.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Mating Season{/color}")
            if (not ev_mall45.hint == "") and not (ev_mall45.hint == "Event will trigger automatically."):
                text ("Rough Cuts")
            if (not ev_chikaspecial45.hint == "") and not (ev_chikaspecial45.hint == "Event will trigger automatically."):
                text ("Curry Night")
            if (not ev_chikadorm45.hint == "") and not (ev_chikadorm45.hint == "Event will trigger automatically."):
                text ("Our Time Atop This Mattress")

        if Yumi.active:
            if (not ev_yumislumber1.hint == "") and not (ev_yumislumber1.hint == "Event will trigger automatically."):
                text ("Two Months of Nothing")
            if (not ev_yumislumber2.hint == "") and not (ev_yumislumber2.hint == "Event will trigger automatically."):
                text ("Loggerhead")
            if (not ev_yumislumber3.hint == "") and not (ev_yumislumber3.hint == "Event will trigger automatically."):
                text ("A Day in the Life")

        if Ayane.active:
            if (not ev_ayanespecial40.hint == "") and not (ev_ayanespecial40.hint == "Event will trigger automatically."):
                text ("Chronokinetics (Hell Exists)")
            if (not ev_ayanesanabeach1.hint == "") and not (ev_ayanesanabeach1.hint == "Event will trigger automatically."):
                text ("How the World Works")
            if (not ev_ayanespecial50.hint == "") and not (ev_ayanespecial50.hint == "Event will trigger automatically."):
                text ("Chiburi")
            if (not ev_ayanekirintalk.hint == "") and not (ev_ayanekirintalk.hint == "Event will trigger automatically."):
                text ("Furlough (Tell the World)")
            if (not ev_ayanespecial55.hint == "") and not (ev_ayanespecial55.hint == "Event will trigger automatically."):
                text ("Double Jeopardy")
            if (not ev_ayanebonus1.hint == "") and not (ev_ayanebonus1.hint == "Event will trigger automatically."):
                text ("The Aforementioned Light")
            if (not ev_ayanebonus2.hint == "") and not (ev_ayanebonus2.hint == "Event will trigger automatically."):
                text ("Over & Over")
            if (not ev_ayanepool55.hint == "") and not (ev_ayanepool55.hint == "Event will trigger automatically."):
                text ("Dizzy On The Comedown")

        if Sana.active:
            if (not ev_bar55.hint == "") and not (ev_bar55.hint == "Event will trigger automatically."):
                text ("Black Sandy Beaches")
            if (not ev_ayanesanabeach2.hint == "") and not (ev_ayanesanabeach2.hint == "Event will trigger automatically."):
                text ("Ad Meliora")
            if (not ev_ayanesanabeach3.hint == "") and not (ev_ayanesanabeach3.hint == "Event will trigger automatically."):
                text ("It Comes to Claim Us All")
            if (not ev_ayanesanabeach4.hint == "") and not (ev_ayanesanabeach4.hint == "Event will trigger automatically."):
                text ("Ad Infinitum")

        if Makoto.active:
            if (not ev_sadgirls1.hint == "") and not (ev_sadgirls1.hint == "Event will trigger automatically."):
                text ("Whispers of the World")
            if (not ev_sadgirls7.hint == "") and not (ev_sadgirls7.hint == "Event will trigger automatically."):
                text ("Parallelogram")
            if (not ev_makotolust30.hint == "") and not (ev_makotolust30.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}White Oak Doors{/color}")
            if (not ev_sadgirls8.hint == "") and not (ev_sadgirls8.hint == "Event will trigger automatically."):
                text ("A Beautiful Mind")
            if (not ev_makotospecial50.hint == "") and not (ev_makotospecial50.hint == "Event will trigger automatically."):
                text ("Young Cardinals")
            if (not ev_makotopool55.hint == "") and not (ev_makotopool55.hint == "Event will trigger automatically."):
                text ("Cool Sex Tips")
            if (not ev_makotodorm55p1.hint == "") and not (ev_makotodorm55p1.hint == "Event will trigger automatically."):
                text ("Bra Shopping")
            if (not ev_makotodorm55p2.hint == "") and not (ev_makotodorm55p2.hint == "Event will trigger automatically."):
                text ("Suffer the Same")

        if Miku.active:
            if (not ev_mikuinvite1.hint == "") and not (ev_mikuinvite1.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Breakaway{/color}")
            if (not ev_mikuinvite2.hint == "") and not (ev_mikuinvite2.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Fair is Fair{/color}")
            if (not ev_mikupool55.hint == "") and not (ev_mikupool55.hint == "Event will trigger automatically."):
                text ("Voice of Vibration")
            if (not ev_mikudorm55p1.hint == "") and not (ev_mikudorm55p1.hint == "Event will trigger automatically."):
                text ("Essence of Eiderdown")
            if (not ev_mikudorm55p2.hint == "") and not (ev_mikudorm55p2.hint == "Event will trigger automatically."):
                text ("Rostrum of Recollection")

        if Futaba.active:
            if (not ev_futabadorm50.hint == "") and not (ev_futabadorm50.hint == "Event will trigger automatically."):
                text ("This Infected Wound")
            if (not ev_library50.hint == "") and not (ev_library50.hint == "Event will trigger automatically."):
                text ("Bestial Vigor")
            if (not ev_futabainvite3.hint == "") and not (ev_futabainvite3.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Too Blind To See{/color}")
            if (not ev_makotofutabafuntimelustevent.hint == "") and not (ev_makotofutabafuntimelustevent.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Toys{/color}")
            if (not ev_futabaspecial60p1.hint == "") and not (ev_futabaspecial60p1.hint == "Event will trigger automatically."):
                text ("Book Burning")
            if (not ev_futabaspecial60p2.hint == "") and not (ev_futabaspecial60p2.hint == "Event will trigger automatically."):
                text ("Pg. 99")
            if (not ev_futabaspecial60p3.hint == "") and not (ev_futabaspecial60p3.hint == "Event will trigger automatically."):
                text ("Fish Eyes")

        if Rin.active:
            if (not ev_rindorm55.hint == "") and not (ev_rindorm55.hint == "Event will trigger automatically."):
                text ("Disaster Lesbian")
            if (not ev_rindorm55p2.hint == "") and not (ev_rindorm55p2.hint == "Event will trigger automatically."):
                text ("Hot Boy Summer")
            if (not ev_rinspecial55.hint == "") and not (ev_rinspecial55.hint == "Event will trigger automatically."):
                text ("Ever Fallen In Love")

        if Molly.active:
            if (not ev_mollycafe30p1.hint == "") and not (ev_mollycafe30p1.hint == "Event will trigger automatically."):
                text ("Hook")
            if (not ev_mollycafe30p2.hint == "") and not (ev_mollycafe30p2.hint == "Event will trigger automatically."):
                text ("A Night to Remember")
            if (not ev_mollydate35p1.hint == "") and not (ev_mollydate35p1.hint == "Event will trigger automatically."):
                text ("Anar'alah Belore")
            if (not ev_mollydate35p2.hint == "") and not (ev_mollydate35p2.hint == "Event will trigger automatically."):
                text ("Sardines")

        if Tsuneyo.active:
            if (not ev_tsuneyoslumber1.hint == "") and not (ev_tsuneyoslumber1.hint == "Event will trigger automatically."):
                text ("With Her")
            if (not ev_tsuneyoslumber2.hint == "") and not (ev_tsuneyoslumber2.hint == "Event will trigger automatically."):
                text ("Stripped Away")
            if (not ev_tsuneyoslumber3.hint == "") and not (ev_tsuneyoslumber3.hint == "Event will trigger automatically."):
                text ("Sudden Light")

        if Sara.active:
            if (not ev_saraspecial30p1.hint == "") and not (ev_saraspecial30p1.hint == "Event will trigger automatically."):
                text ("The Creaking of the Seventh ")
                text ("  Step ")
            if (not ev_saraspecial30p2.hint == "") and not (ev_saraspecial30p2.hint == "Event will trigger automatically."):
                text ("Halfway Down the Wishing Well")
            if (not ev_sarabar30.hint == "") and not (ev_sarabar30.hint == "Event will trigger automatically."):
                text ("Nicolas Cage")

        if Haruka.active:
            if (not ev_sadgirls2.hint == "") and not (ev_sadgirls2.hint == "Event will trigger automatically."):
                text ("The World Outside The Walls")
            if (not ev_sadgirls4.hint == "") and not (ev_sadgirls4.hint == "Event will trigger automatically."):
                text ("To Anyone Who Passes By")
            if (not ev_sadgirls5.hint == "") and not (ev_sadgirls5.hint == "Event will trigger automatically."):
                text ("Again, I Can't Recall")
            if (not ev_harukalust25.hint == "") and not (ev_harukalust25.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Secret Weapon{/color}")
            if (not ev_makihornytrip1.hint == "") and not (ev_makihornytrip1.hint == "Event will trigger automatically."):
                text ("Stress Level Midnight")
            if (not ev_makihornytrip4.hint == "") and not (ev_makihornytrip4.hint == "Event will trigger automatically."):
                text ("Conflict of Interest")
            if (not ev_harukadate30.hint == "") and not (ev_harukadate30.hint == "Event will trigger automatically."):
                text ("Scum")

        if Maki.active:
            if (not ev_sadgirls3.hint == "") and not (ev_sadgirls3.hint == "Event will trigger automatically."):
                text ("Adulting")
            if (not ev_sadgirls6.hint == "") and not (ev_sadgirls6.hint == "Event will trigger automatically."):
                text ("Rolling Stop (Turned Backwards)")
            if (not ev_makiinv3.hint == "") and not (ev_makiinv3.hint == "Event will trigger automatically."):
                text ("Baby Steps")
            if (not ev_makihornyquestintro.hint == "") and not (ev_makihornyquestintro.hint == "Event will trigger automatically."):
                text ("The Maltese Falcon")
            if (not ev_makihornytrip2.hint == "") and not (ev_makihornytrip2.hint == "Event will trigger automatically."):
                text ("Shut Up & Cum")
            if (not ev_makihornytrip3.hint == "") and not (ev_makihornytrip3.hint == "Event will trigger automatically."):
                text ("Rotting From the Inside Out")

        if Kirin.active:
            if (not ev_kirinlust30.hint == "") and not (ev_kirinlust30.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Falling Asleep Standing Up{/color}")
            if (not ev_kirinspecial40.hint == "") and not (ev_kirinspecial40.hint == "Event will trigger automatically."):
                text ("At the Edge of the Riverbank")
            if (not ev_kirinspecial45p1.hint == "") and not (ev_kirinspecial45p1.hint == "Event will trigger automatically."):
                text ("Never Enough")
            if (not ev_kirinspecial45p2.hint == "") and not (ev_kirinspecial45p2.hint == "Event will trigger automatically."):
                text ("Salmon Onigiri")

        if Karin.active:
            if (not ev_karindate25.hint == "") and not (ev_karindate25.hint == "Event will trigger automatically."):
                text ("Emerald Eyes")
            if (not ev_karindate30.hint == "") and not (ev_karindate30.hint == "Event will trigger automatically."):
                text ("Wrong Places/Wrong Times")

        if Kaori.active:
            if (not ev_kaorispecial35.hint == "") and not (ev_kaorispecial35.hint == "Event will trigger automatically."):
                text ("Where the Trees Live")
            if (not ev_kaorispecial40.hint == "") and not (ev_kaorispecial40.hint == "Event will trigger automatically."):
                text ("Human Females")
            if (not ev_kaoridate40.hint == "") and not (ev_kaoridate40.hint == "Event will trigger automatically."):
                text ("Run, Rabbit, Run (Why the ")
                text ("  Fieldmice Hide) ")

        if Imani.active:
            if (not ev_imanidate1.hint == "") and not (ev_imanidate1.hint == "Event will trigger automatically."):
                text ("Somewhere I Belong")
            if (not ev_imanidate5.hint == "") and not (ev_imanidate5.hint == "Event will trigger automatically."):
                text ("A Hairline Fracture")
            if (not ev_imanidate15p1.hint == "") and not (ev_imanidate15p1.hint == "Event will trigger automatically."):
                text ("Knotted Up")
            if (not ev_imanidate15p2.hint == "") and not (ev_imanidate15p2.hint == "Event will trigger automatically."):
                text ("Arm's Length")
            if (not ev_imanispecial15.hint == "") and not (ev_imanispecial15.hint == "Event will trigger automatically."):
                text ("Debbie Downer")

        if Rika.active:
            if (not ev_rikadate1.hint == "") and not (ev_rikadate1.hint == "Event will trigger automatically."):
                text ("Impregnation Spree")
            if (not ev_rikaspecial2.hint == "") and not (ev_rikaspecial2.hint == "Event will trigger automatically."):
                text ("Back on Track")
            if (not ev_rikadive1.hint == "") and not (ev_rikadive1.hint == "Event will trigger automatically."):
                text ("James and the Giant Peach ")
                text ("  (Together-ish) ")

        if Nao.active:
            if (not ev_naospecial1.hint == "") and not (ev_naospecial1.hint == "Event will trigger automatically."):
                text ("Silver Tongue")
            if (not ev_naospecial2.hint == "") and not (ev_naospecial2.hint == "Event will trigger automatically."):
                text ("Becoming a Kidnapper")
            if (not ev_naospecial3.hint == "") and not (ev_naospecial3.hint == "Event will trigger automatically."):
                text ("Eternity Until")

        if Chinami.active:
            if (not ev_chinamidate25.hint == "") and not (ev_chinamidate25.hint == "Event will trigger automatically."):
                text ("Death Trap")
            if (not ev_chinamidate30.hint == "") and not (ev_chinamidate30.hint == "Event will trigger automatically."):
                text ("Bad News Bears")
            if (not ev_chapthree1.hint == "") and not (ev_chapthree1.hint == "Event will trigger automatically."):
                text ("The Virgin of the Apocalypse")
            if (not ev_chapthree2.hint == "") and not (ev_chapthree2.hint == "Event will trigger automatically."):
                text ("Memories")
            if (not ev_chapthree3.hint == "") and not (ev_chapthree3.hint == "Event will trigger automatically."):
                text ("Empty Eyes")
            if (not ev_chapthree4.hint == "") and not (ev_chapthree4.hint == "Event will trigger automatically."):
                text ("The Great Migration")
            if (not ev_chapthree5.hint == "") and not (ev_chapthree5.hint == "Event will trigger automatically."):
                text ("Creatures of Habit")
            if (not ev_chapthree6.hint == "") and not (ev_chapthree6.hint == "Event will trigger automatically."):
                text ("Everything Everywhere All At ")
                text ("  Once ")
            if (not ev_chapthree7.hint == "") and not (ev_chapthree7.hint == "Event will trigger automatically."):
                text ("Normal-ish")
            if (not ev_chapthree8.hint == "") and not (ev_chapthree8.hint == "Event will trigger automatically."):
                text ("Life is Changing")
            if (not ev_yumichikaspecial1.hint == "") and not (ev_yumichikaspecial1.hint == "Event will trigger automatically."):
                text ("Dead in the Water")
            if (not ev_yumiyukispecial1.hint == "") and not (ev_yumiyukispecial1.hint == "Event will trigger automatically."):
                text ("The Road to Recovery")
            if (not ev_imanispecial1.hint == "") and not (ev_imanispecial1.hint == "Event will trigger automatically."):
                text ("No Strings Attached")
            if (not ev_rikaspecial1.hint == "") and not (ev_rikaspecial1.hint == "Event will trigger automatically."):
                text ("Metronome In Love")
            if (not ev_day543.hint == "") and not (ev_day543.hint == "Event will trigger automatically."):
                text ("Grief Seed")
            if (not ev_dormwartwo1.hint == "") and not (ev_dormwartwo1.hint == "Event will trigger automatically."):
                text ("A Walk Through Hell")
            if (not ev_dormwartwo2.hint == "") and not (ev_dormwartwo2.hint == "Event will trigger automatically."):
                text ("Dorm War II: Pre-Game Show")
            if (not ev_dormwartwo3.hint == "") and not (ev_dormwartwo3.hint == "Event will trigger automatically."):
                text ("A Frame on a Shelf in a House")
            if (not ev_dormwartwo4.hint == "") and not (ev_dormwartwo4.hint == "Event will trigger automatically."):
                text ("Gamer Girl Grindfest")
            if (not ev_dormwartwo5.hint == "") and not (ev_dormwartwo5.hint == "Event will trigger automatically."):
                text ("Hiding in Plain Sight")
            if (not ev_dormwartwo6.hint == "") and not (ev_dormwartwo6.hint == "Event will trigger automatically."):
                text ("She Is")
            if (not ev_dormwartwo7.hint == "") and not (ev_dormwartwo7.hint == "Event will trigger automatically."):
                text ("Burden to Bear")
            if (not ev_dormwartwo8.hint == "") and not (ev_dormwartwo8.hint == "Event will trigger automatically."):
                text ("Everyone")
            if (not ev_dormwartwo9.hint == "") and not (ev_dormwartwo9.hint == "Event will trigger automatically."):
                text ("Midnight Mom Mosh")
            if (not ev_dormwartwo10.hint == "") and not (ev_dormwartwo10.hint == "Event will trigger automatically."):
                text ("The Way it Scatters")
            if (not ev_dormwartwo11.hint == "") and not (ev_dormwartwo11.hint == "Event will trigger automatically."):
                text ("Misfit Maid Madness")
            if (not ev_dormwartwo12.hint == "") and not (ev_dormwartwo12.hint == "Event will trigger automatically."):
                text ("Somewhere Far From Here")
            if (not ev_dormwartwo13.hint == "") and not (ev_dormwartwo13.hint == "Event will trigger automatically."):
                text ("Swimming With Sharks")
            if (not ev_dormwartwo14.hint == "") and not (ev_dormwartwo14.hint == "Event will trigger automatically."):
                text ("Remove Curse")
            if (not ev_dormwartwo15.hint == "") and not (ev_dormwartwo15.hint == "Event will trigger automatically."):
                text ("The Cracking of the Egg ")
                text ("  (Nothing is Beautiful) ")
            if (not ev_dormwartwo16.hint == "") and not (ev_dormwartwo16.hint == "Event will trigger automatically."):
                text ("World of Lines")
            if (not ev_dormwartwo17.hint == "") and not (ev_dormwartwo17.hint == "Event will trigger automatically."):
                text ("Popping Off")
            if (not ev_dormwartwo18.hint == "") and not (ev_dormwartwo18.hint == "Event will trigger automatically."):
                text ("Tip Your Bartender")
            if (not ev_dormwartwo19.hint == "") and not (ev_dormwartwo19.hint == "Event will trigger automatically."):
                text ("Redeemer")
            if (not ev_beachmas1.hint == "") and not (ev_beachmas1.hint == "Event will trigger automatically."):
                text ("Walk Into the Water")
            if (not ev_beachmas2.hint == "") and not (ev_beachmas2.hint == "Event will trigger automatically."):
                text ("Imaginary Veins")
            if (not ev_beachmas3.hint == "") and not (ev_beachmas3.hint == "Event will trigger automatically."):
                text ("Friends (The Maya Route)")
            if (not ev_beachmas4.hint == "") and not (ev_beachmas4.hint == "Event will trigger automatically."):
                text ("Chandler's Law")
            if (not ev_beachmas5.hint == "") and not (ev_beachmas5.hint == "Event will trigger automatically."):
                text ("The Chains That Bind")
            if (not ev_beachmas6.hint == "") and not (ev_beachmas6.hint == "Event will trigger automatically."):
                text ("No Cumming on Christmas")
            if (not ev_beachmas7.hint == "") and not (ev_beachmas7.hint == "Event will trigger automatically."):
                text ("Fetch Quest")
            if (not ev_beachmas8.hint == "") and not (ev_beachmas8.hint == "Event will trigger automatically."):
                text ("A Thousand Truths")
            if (not ev_beachmas9.hint == "") and not (ev_beachmas9.hint == "Event will trigger automatically."):
                text ("The Bending of Italics")
            if (not ev_beachmas10.hint == "") and not (ev_beachmas10.hint == "Event will trigger automatically."):
                text ("Treasured")
            if (not ev_beachmas11.hint == "") and not (ev_beachmas11.hint == "Event will trigger automatically."):
                text ("いないいない。。。ばあ！")
            if (not ev_beachmas12.hint == "") and not (ev_beachmas12.hint == "Event will trigger automatically."):
                text ("Robin Hood")
            if (not ev_beachmas13.hint == "") and not (ev_beachmas13.hint == "Event will trigger automatically."):
                text ("The Legacy of Thaum Pt. IV")
            if (not ev_beachmas14.hint == "") and not (ev_beachmas14.hint == "Event will trigger automatically."):
                text ("On The Fence")
            if (not ev_beachmas15.hint == "") and not (ev_beachmas15.hint == "Event will trigger automatically."):
                text ("To the Future With a Smile")
            if (not ev_beachmas16.hint == "") and not (ev_beachmas16.hint == "Event will trigger automatically."):
                text ("Neverender")
            if (not ev_beachmas17.hint == "") and not (ev_beachmas17.hint == "Event will trigger automatically."):
                text ("Moon-Touched")
            if (not ev_beachmas18.hint == "") and not (ev_beachmas18.hint == "Event will trigger automatically."):
                text ("Smells of Summer")
            if (not ev_beachmas19.hint == "") and not (ev_beachmas19.hint == "Event will trigger automatically."):
                text ("I Will Deliver You to the ")
                text ("  Fireflies ")
            if (not ev_beachmas20.hint == "") and not (ev_beachmas20.hint == "Event will trigger automatically."):
                text ("Shelter")
            if (not ev_slumberreset1.hint == "") and not (ev_slumberreset1.hint == "Event will trigger automatically."):
                text ("To Catch Me If I Fall")
            if (not ev_slumberreset2.hint == "") and not (ev_slumberreset2.hint == "Event will trigger automatically."):
                text ("Approximation")
            if (not ev_slumberreset3.hint == "") and not (ev_slumberreset3.hint == "Event will trigger automatically."):
                text ("December 28, 2020 (Clay & ")
                text ("  Clockwork) ")
            if (not ev_slumberreset4.hint == "") and not (ev_slumberreset4.hint == "Event will trigger automatically."):
                text ("Untitled")
            if (not ev_slumberreset5.hint == "") and not (ev_slumberreset5.hint == "Event will trigger automatically."):
                text ("A Thousand Years")
            if (not ev_postnodokachain1.hint == "") and not (ev_postnodokachain1.hint == "Event will trigger automatically."):
                text ("White-Fronted Parrot")
            if (not ev_treasureisland.hint == "") and not (ev_treasureisland.hint == "Event will trigger automatically."):
                text ("First Contact")
            if (not ev_amispecial50mainp1.hint == "") and not (ev_amispecial50mainp1.hint == "Event will trigger automatically."):
                text ("All For You")
            if (not ev_amispecial50mainp2.hint == "") and not (ev_amispecial50mainp2.hint == "Event will trigger automatically."):
                text ("From the Desk of the Ninth God")
            if (not ev_predormwars3.hint == "") and not (ev_predormwars3.hint == "Event will trigger automatically."):
                text ("May the Winter Come")
            if (not ev_beachwars1.hint == "") and not (ev_beachwars1.hint == "Event will trigger automatically."):
                text ("Boner on the Bus")
            if (not ev_beachwars2.hint == "") and not (ev_beachwars2.hint == "Event will trigger automatically."):
                text ("When You Snap")
            if (not ev_beachwars3.hint == "") and not (ev_beachwars3.hint == "Event will trigger automatically."):
                text ("Until My Back is Broken")
            if (not ev_beachwars4.hint == "") and not (ev_beachwars4.hint == "Event will trigger automatically."):
                text ("The Rest of Me")
            if (not ev_beachwars5.hint == "") and not (ev_beachwars5.hint == "Event will trigger automatically."):
                text ("Hyzenthlay")
            if (not ev_beachwars6.hint == "") and not (ev_beachwars6.hint == "Event will trigger automatically."):
                text ("More Human Than Human")
            if (not ev_beachwars7.hint == "") and not (ev_beachwars7.hint == "Event will trigger automatically."):
                text ("Eyes Closed, Chin Up")
            if (not ev_beachwars8.hint == "") and not (ev_beachwars8.hint == "Event will trigger automatically."):
                text ("Sexy Swimsuit Showdown")
            if (not ev_beachwars9.hint == "") and not (ev_beachwars9.hint == "Event will trigger automatically."):
                text ("Fairytale (The End Until ")
                text ("  Tomorrow) ")
            if (not ev_beachwars10.hint == "") and not (ev_beachwars10.hint == "Event will trigger automatically."):
                text ("Monsters")
            if (not ev_beachwars11.hint == "") and not (ev_beachwars11.hint == "Event will trigger automatically."):
                text ("Pairs in Different Places")
            if (not ev_beachwars12.hint == "") and not (ev_beachwars12.hint == "Event will trigger automatically."):
                text ("Forbidden Artistry")
            if (not ev_beachwars13.hint == "") and not (ev_beachwars13.hint == "Event will trigger automatically."):
                text ("Too Many Cooks")
            if (not ev_beachwars14.hint == "") and not (ev_beachwars14.hint == "Event will trigger automatically."):
                text ("Judgement Day")
            if (not ev_beachwars15.hint == "") and not (ev_beachwars15.hint == "Event will trigger automatically."):
                text ("Mother May I")
            if (not ev_beachwars16.hint == "") and not (ev_beachwars16.hint == "Event will trigger automatically."):
                text ("Cicadian Rhythm (The Gardener)")
            if (not ev_beachwars17.hint == "") and not (ev_beachwars17.hint == "Event will trigger automatically."):
                text ("Bidder's Organs")
            if (not ev_beachwars18.hint == "") and not (ev_beachwars18.hint == "Event will trigger automatically."):
                text ("Flowerchild")
            if (not ev_beachwars19.hint == "") and not (ev_beachwars19.hint == "Event will trigger automatically."):
                text ("Danger to Society")
            if (not ev_halloweenfour1.hint == "") and not (ev_halloweenfour1.hint == "Event will trigger automatically."):
                text ("Eggside Octopus")
            if (not ev_halloweenfour2.hint == "") and not (ev_halloweenfour2.hint == "Event will trigger automatically."):
                text ("The Tenth Step")
            if (not ev_halloweenfour3.hint == "") and not (ev_halloweenfour3.hint == "Event will trigger automatically."):
                text ("BONE-TOWN")
            if (not ev_halloweenfour4.hint == "") and not (ev_halloweenfour4.hint == "Event will trigger automatically."):
                text ("Try Honesty")
            if (not ev_halloweenfour5.hint == "") and not (ev_halloweenfour5.hint == "Event will trigger automatically."):
                text ("Heartache")
            if (not ev_halloweenfour6.hint == "") and not (ev_halloweenfour6.hint == "Event will trigger automatically."):
                text ("The King of Thebes")
            if (not ev_halloweenfour7.hint == "") and not (ev_halloweenfour7.hint == "Event will trigger automatically."):
                text ("Our Fathers")
            if (not ev_halloweenfour8.hint == "") and not (ev_halloweenfour8.hint == "Event will trigger automatically."):
                text ("Eighth Eye of the Wolf Spider")
            if (not ev_halloweenfour9.hint == "") and not (ev_halloweenfour9.hint == "Event will trigger automatically."):
                text ("Childspawn")
            if (not ev_halloweenfour10.hint == "") and not (ev_halloweenfour10.hint == "Event will trigger automatically."):
                text ("An Excerpt From a Waterlogged ")
                text ("  Journal ")
            if (not ev_halloweenfour11.hint == "") and not (ev_halloweenfour11.hint == "Event will trigger automatically."):
                text ("Party Animal")
            if (not ev_halloweenfour12.hint == "") and not (ev_halloweenfour12.hint == "Event will trigger automatically."):
                text ("Girls Just Want to Have Fun")
            if (not ev_halloweenfour13.hint == "") and not (ev_halloweenfour13.hint == "Event will trigger automatically."):
                text ("Happy Memories")
            if (not ev_halloweenfour14.hint == "") and not (ev_halloweenfour14.hint == "Event will trigger automatically."):
                text ("For More Than Just Me")
            if (not ev_halloweenfour15.hint == "") and not (ev_halloweenfour15.hint == "Event will trigger automatically."):
                text ("I Won't Say I'm In Love")
            if (not ev_halloweenfour16.hint == "") and not (ev_halloweenfour16.hint == "Event will trigger automatically."):
                text ("The End of the World")
            if (not ev_resetsix1.hint == "") and not (ev_resetsix1.hint == "Event will trigger automatically."):
                text ("Times New Roman")
            if (not ev_resetsix2.hint == "") and not (ev_resetsix2.hint == "Event will trigger automatically."):
                text ("Paper City")
            if (not ev_resetsix3.hint == "") and not (ev_resetsix3.hint == "Event will trigger automatically."):
                text ("Meant to Be")
            if (not ev_resetsix4.hint == "") and not (ev_resetsix4.hint == "Event will trigger automatically."):
                text ("Remember to Smile")

        if Yuki.active:
            if (not ev_yukidate20p1.hint == "") and not (ev_yukidate20p1.hint == "Event will trigger automatically."):
                text ("Funeral Plans")
            if (not ev_yukidate20p2.hint == "") and not (ev_yukidate20p2.hint == "Event will trigger automatically."):
                text ("Douchebag McDouchefuck")
            if (not ev_yukidate25.hint == "") and not (ev_yukidate25.hint == "Event will trigger automatically."):
                text ("Pride & Joy")

        if Wakana.active:
            if (not ev_wakanadate15.hint == "") and not (ev_wakanadate15.hint == "Event will trigger automatically."):
                text ("Pseudonym")
            if (not ev_wakanaspecial15.hint == "") and not (ev_wakanaspecial15.hint == "Event will trigger automatically."):
                text ("Don't Hold Back")
            if (not ev_wakanadate25p1.hint == "") and not (ev_wakanadate25p1.hint == "Event will trigger automatically."):
                text ("The Desk Scene")
            if (not ev_wakanadate25p2.hint == "") and not (ev_wakanadate25p2.hint == "Event will trigger automatically."):
                text ("Human Error")
            if (not ev_wakanadate25p3.hint == "") and not (ev_wakanadate25p3.hint == "Event will trigger automatically."):
                text ("Follow My Lead")

        if Osako.active:
            if (not ev_osakodate15.hint == "") and not (ev_osakodate15.hint == "Event will trigger automatically."):
                text ("Young At Heart")
            if (not ev_osakodate20.hint == "") and not (ev_osakodate20.hint == "Event will trigger automatically."):
                text ("House of the Unholy")

        if Tsubasa.active:
            if (not ev_tsubasaspecial15.hint == "") and not (ev_tsubasaspecial15.hint == "Event will trigger automatically."):
                text ("Heart of Gold")
            if (not ev_tsubasadate20.hint == "") and not (ev_tsubasadate20.hint == "Event will trigger automatically."):
                text ("Playing God")
            if (not ev_tsubasaspecial20.hint == "") and not (ev_tsubasaspecial20.hint == "Event will trigger automatically."):
                text ("The Lucky Few")

        if Tsukasa.active:
            if (not ev_tsukasaspecial1.hint == "") and not (ev_tsukasaspecial1.hint == "Event will trigger automatically."):
                text ("National Tsukasa Day")
            if (not ev_tsukasaspecial1p2.hint == "") and not (ev_tsukasaspecial1p2.hint == "Event will trigger automatically."):
                text ("Jeeves Tsukioka XIII")

        if Uta.active:
            if (not ev_utaarchery1.hint == "") and not (ev_utaarchery1.hint == "Event will trigger automatically."):
                text ("Impulse")
            if (not ev_utamaid25p1.hint == "") and not (ev_utamaid25p1.hint == "Event will trigger automatically."):
                text ("Where Wishes Come True")
            if (not ev_utamaid25p2.hint == "") and not (ev_utamaid25p2.hint == "Event will trigger automatically."):
                text ("After the Rain")
            if (not ev_utadorm30.hint == "") and not (ev_utadorm30.hint == "Event will trigger automatically."):
                text ("Uta-chan")
            if (not ev_utaspecial35.hint == "") and not (ev_utaspecial35.hint == "Event will trigger automatically."):
                text ("Young & Stupid")
            if (not ev_utadate35.hint == "") and not (ev_utadate35.hint == "Event will trigger automatically."):
                text ("Enjo Kousai")
            if (not ev_utadorm40p1.hint == "") and not (ev_utadorm40p1.hint == "Event will trigger automatically."):
                text ("Whore")
            if (not ev_utadorm40p2.hint == "") and not (ev_utadorm40p2.hint == "Event will trigger automatically."):
                text ("The Girl From Nara")

        if Io.active:
            if (not ev_ioarchery1.hint == "") and not (ev_ioarchery1.hint == "Event will trigger automatically."):
                text ("Cupid's Arrow")
            if (not ev_bathhouse25.hint == "") and not (ev_bathhouse25.hint == "Event will trigger automatically."):
                text ("Work Less, Not Hard")
            if (not ev_iodorm25.hint == "") and not (ev_iodorm25.hint == "Event will trigger automatically."):
                text ("Heartbreak & Harmony")
            if (not ev_iospecial30.hint == "") and not (ev_iospecial30.hint == "Event will trigger automatically."):
                text ("1999 PC Classic, Rollercoaster ")
                text ("  Tycoon ")
            if (not ev_bathhouse35p1.hint == "") and not (ev_bathhouse35p1.hint == "Event will trigger automatically."):
                text ("Tennis Ball")
            if (not ev_bathhouse35p2.hint == "") and not (ev_bathhouse35p2.hint == "Event will trigger automatically."):
                text ("Hold You Over")
            if (not ev_iodorm35.hint == "") and not (ev_iodorm35.hint == "Event will trigger automatically."):
                text ("Yellow Cactus Flower")
            if (not ev_ioarchery35.hint == "") and not (ev_ioarchery35.hint == "Event will trigger automatically."):
                text ("Two Of Us Are Thinking")

        if Noriko.active:
            if (not ev_norikodate30.hint == "") and not (ev_norikodate30.hint == "Event will trigger automatically."):
                text ("Hotel Noriko")
            if (not ev_norikodorm30.hint == "") and not (ev_norikodorm30.hint == "Event will trigger automatically."):
                text ("Dotted Line")
            if (not ev_norikoinvite3.hint == "") and not (ev_norikoinvite3.hint == "Event will trigger automatically."):
                text ("{color=778EFF}I Really Want to Stay at Your {/color}")
                text ("{color=778EFF}  House {/color}")
            if (not ev_norikoinvite4.hint == "") and not (ev_norikoinvite4.hint == "Event will trigger automatically."):
                text ("{color=778EFF}Somewhere{/color}")

        if Niki.active:
            if (not ev_nikilovesyou1.hint == "") and not (ev_nikilovesyou1.hint == "Event will trigger automatically."):
                text ("What it Takes to Move Forward")
            if (not ev_nikilovesyou2.hint == "") and not (ev_nikilovesyou2.hint == "Event will trigger automatically."):
                text ("The End of the Tour ")
                text ("  (Glasswalker) ")
            if (not ev_nikilovesyou3.hint == "") and not (ev_nikilovesyou3.hint == "Event will trigger automatically."):
                text ("How To Make Love Stay")
            if (not ev_nikifirstlust.hint == "") and not (ev_nikifirstlust.hint == "Event will trigger automatically."):
                text ("{color=FF85FD}Non-Disclosure Agreement{/color}")

        if Nodoka.active:
            if (not ev_nodokadorm15.hint == "") and not (ev_nodokadorm15.hint == "Event will trigger automatically."):
                text ("Beyond the Reach of God")
            if (not ev_nodokaspecial15p1.hint == "") and not (ev_nodokaspecial15p1.hint == "Event will trigger automatically."):
                text ("So Far Below")
            if (not ev_nodokaspecial15p2.hint == "") and not (ev_nodokaspecial15p2.hint == "Event will trigger automatically."):
                text ("Matador")
            if (not ev_nodokaspecial15p3.hint == "") and not (ev_nodokaspecial15p3.hint == "Event will trigger automatically."):
                text ("Things That Hurt")
            if (not ev_nodokaspecial20.hint == "") and not (ev_nodokaspecial20.hint == "Event will trigger automatically."):
                text ("Twisting Ivy")
            if (not ev_nodokaspecial30p1.hint == "") and not (ev_nodokaspecial30p1.hint == "Event will trigger automatically."):
                text ("Amoeba (Incontrovertible ")
                text ("  Peculiarity) ")
            if (not ev_nodokaspecial30p2.hint == "") and not (ev_nodokaspecial30p2.hint == "Event will trigger automatically."):
                text ("This is Us")
            if (not ev_nodokaspecial30p3.hint == "") and not (ev_nodokaspecial30p3.hint == "Event will trigger automatically."):
                text ("Taco Attack")
            if (not ev_nodokaspecial30p4.hint == "") and not (ev_nodokaspecial30p4.hint == "Event will trigger automatically."):
                text ("Lavender")

        if Otoha.active:
            if (not ev_otohaspecial15p1.hint == "") and not (ev_otohaspecial15p1.hint == "Event will trigger automatically."):
                text ("King Midas")
            if (not ev_otohaspecial15p2.hint == "") and not (ev_otohaspecial15p2.hint == "Event will trigger automatically."):
                text ("White People")
            if (not ev_otohadate20.hint == "") and not (ev_otohadate20.hint == "Event will trigger automatically."):
                text ("Breaking Character")

        if Touka.active:
            if (not ev_toukaarchery20.hint == "") and not (ev_toukaarchery20.hint == "Event will trigger automatically."):
                text ("Kryptonite")
            if (not ev_toukadorm25p1.hint == "") and not (ev_toukadorm25p1.hint == "Event will trigger automatically."):
                text ("For Want Of")
            if (not ev_toukadorm25p2.hint == "") and not (ev_toukadorm25p2.hint == "Event will trigger automatically."):
                text ("To Lift This Aching Head")
            if (not ev_toukadorm25p3.hint == "") and not (ev_toukadorm25p3.hint == "Event will trigger automatically."):
                text ("Under My Wing")

        if Yasu.active:
            if (not ev_church15.hint == "") and not (ev_church15.hint == "Event will trigger automatically."):
                text ("Down The Rabbit Hole")
            if (not ev_yasuspecial15.hint == "") and not (ev_yasuspecial15.hint == "Event will trigger automatically."):
                text ("Sore Thumb")
            if (not ev_church20.hint == "") and not (ev_church20.hint == "Event will trigger automatically."):
                text ("Mother Duck")
            if (not ev_yasudorm20.hint == "") and not (ev_yasudorm20.hint == "Event will trigger automatically."):
                text ("Glossolalia")
            if (not ev_yasuspecial20.hint == "") and not (ev_yasuspecial20.hint == "Event will trigger automatically."):
                text ("The River Styx")
            if (not ev_church25.hint == "") and not (ev_church25.hint == "Event will trigger automatically."):
                text ("Frankincense & Myrrh")
            if (not ev_yasudorm25.hint == "") and not (ev_yasudorm25.hint == "Event will trigger automatically."):
                text ("Hand of God")
            if (not ev_yasudorm30.hint == "") and not (ev_yasudorm30.hint == "Event will trigger automatically."):
                text ("An Apple Each Day")

    vbox:
        xpos .53
        ypos .14
        style_prefix "hint"

        if show_hints == True:


            if HappyEvent.active:
                if (not ev_buckettrack.hint == "") and not (ev_buckettrack.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_buckettrack.hint]")
                    else:
                        text ("")
                if (not ev_mothersmilk.hint == "") and not (ev_mothersmilk.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_mothersmilk.hint]")
                    else:
                        text ("")
                if (not ev_amyevent.hint == "") and not (ev_amyevent.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_amyevent.hint]")
                    else:
                        text ("")
                if (not ev_rainking.hint == "") and not (ev_rainking.hint == "Event will trigger automatically."):
                    if show_happy_hints == True:
                        text ("[ev_rainking.hint]")
                    else:
                        text ("")

            if Ami.active:
                if (not ev_amilust35.hint == "") and not (ev_amilust35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amilust35.hint:
                        textbutton _("[ev_amilust35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amilust35.hint]")
                if (not ev_amimaid50.hint == "") and not (ev_amimaid50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amimaid50.hint:
                        textbutton _("[ev_amimaid50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amimaid50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amimaid50.hint]")
                if (not ev_amiinvite4.hint == "") and not (ev_amiinvite4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amiinvite4.hint:
                        textbutton _("[ev_amiinvite4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amiinvite4.hint]")
                if (not ev_amispecial50.hint == "") and not (ev_amispecial50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amispecial50.hint:
                        textbutton _("[ev_amispecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispecial50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amispecial50.hint]")
                if (not ev_amilust50.hint == "") and not (ev_amilust50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amilust50.hint:
                        textbutton _("[ev_amilust50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amilust50.hint]")

            if Maya.active:
                if (not ev_shrine40.hint == "") and not (ev_shrine40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_shrine40.hint:
                        textbutton _("[ev_shrine40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_shrine40.hint]")
                if (not ev_mayadate45.hint == "") and not (ev_mayadate45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayadate45.hint:
                        textbutton _("[ev_mayadate45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadate45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayadate45.hint]")
                if (not ev_mayaspecial45.hint == "") and not (ev_mayaspecial45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mayaspecial45.hint:
                        textbutton _("[ev_mayaspecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspecial45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mayaspecial45.hint]")

            if Chika.active:
                if (not ev_chikalust25.hint == "") and not (ev_chikalust25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikalust25.hint:
                        textbutton _("[ev_chikalust25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikalust25.hint]")
                if (not ev_mall45.hint == "") and not (ev_mall45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mall45.hint:
                        textbutton _("[ev_mall45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mall45.hint]")
                if (not ev_chikaspecial45.hint == "") and not (ev_chikaspecial45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikaspecial45.hint:
                        textbutton _("[ev_chikaspecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspecial45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikaspecial45.hint]")
                if (not ev_chikadorm45.hint == "") and not (ev_chikadorm45.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chikadorm45.hint:
                        textbutton _("[ev_chikadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm45), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chikadorm45.hint]")

            if Yumi.active:
                if (not ev_yumislumber1.hint == "") and not (ev_yumislumber1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumislumber1.hint:
                        textbutton _("[ev_yumislumber1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumislumber1.hint]")
                if (not ev_yumislumber2.hint == "") and not (ev_yumislumber2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumislumber2.hint:
                        textbutton _("[ev_yumislumber2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumislumber2.hint]")
                if (not ev_yumislumber3.hint == "") and not (ev_yumislumber3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumislumber3.hint:
                        textbutton _("[ev_yumislumber3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumislumber3.hint]")

            if Ayane.active:
                if (not ev_ayanespecial40.hint == "") and not (ev_ayanespecial40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanespecial40.hint:
                        textbutton _("[ev_ayanespecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanespecial40.hint]")
                if (not ev_ayanesanabeach1.hint == "") and not (ev_ayanesanabeach1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanesanabeach1.hint:
                        textbutton _("[ev_ayanesanabeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanesanabeach1.hint]")
                if (not ev_ayanespecial50.hint == "") and not (ev_ayanespecial50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanespecial50.hint:
                        textbutton _("[ev_ayanespecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanespecial50.hint]")
                if (not ev_ayanekirintalk.hint == "") and not (ev_ayanekirintalk.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanekirintalk.hint:
                        textbutton _("[ev_ayanekirintalk.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanekirintalk), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanekirintalk.hint]")
                if (not ev_ayanespecial55.hint == "") and not (ev_ayanespecial55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanespecial55.hint:
                        textbutton _("[ev_ayanespecial55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanespecial55.hint]")
                if (not ev_ayanebonus1.hint == "") and not (ev_ayanebonus1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanebonus1.hint:
                        textbutton _("[ev_ayanebonus1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanebonus1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanebonus1.hint]")
                if (not ev_ayanebonus2.hint == "") and not (ev_ayanebonus2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanebonus2.hint:
                        textbutton _("[ev_ayanebonus2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanebonus2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanebonus2.hint]")
                if (not ev_ayanepool55.hint == "") and not (ev_ayanepool55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanepool55.hint:
                        textbutton _("[ev_ayanepool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanepool55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanepool55.hint]")

            if Sana.active:
                if (not ev_bar55.hint == "") and not (ev_bar55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bar55.hint:
                        textbutton _("[ev_bar55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bar55.hint]")
                if (not ev_ayanesanabeach2.hint == "") and not (ev_ayanesanabeach2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanesanabeach2.hint:
                        textbutton _("[ev_ayanesanabeach2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanesanabeach2.hint]")
                if (not ev_ayanesanabeach3.hint == "") and not (ev_ayanesanabeach3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanesanabeach3.hint:
                        textbutton _("[ev_ayanesanabeach3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanesanabeach3.hint]")
                if (not ev_ayanesanabeach4.hint == "") and not (ev_ayanesanabeach4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ayanesanabeach4.hint:
                        textbutton _("[ev_ayanesanabeach4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ayanesanabeach4.hint]")

            if Makoto.active:
                if (not ev_sadgirls1.hint == "") and not (ev_sadgirls1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls1.hint:
                        textbutton _("[ev_sadgirls1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls1.hint]")
                if (not ev_sadgirls7.hint == "") and not (ev_sadgirls7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls7.hint:
                        textbutton _("[ev_sadgirls7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls7.hint]")
                if (not ev_makotolust30.hint == "") and not (ev_makotolust30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotolust30.hint:
                        textbutton _("[ev_makotolust30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotolust30.hint]")
                if (not ev_sadgirls8.hint == "") and not (ev_sadgirls8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls8.hint:
                        textbutton _("[ev_sadgirls8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls8.hint]")
                if (not ev_makotospecial50.hint == "") and not (ev_makotospecial50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotospecial50.hint:
                        textbutton _("[ev_makotospecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospecial50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotospecial50.hint]")
                if (not ev_makotopool55.hint == "") and not (ev_makotopool55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotopool55.hint:
                        textbutton _("[ev_makotopool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotopool55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotopool55.hint]")
                if (not ev_makotodorm55p1.hint == "") and not (ev_makotodorm55p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotodorm55p1.hint:
                        textbutton _("[ev_makotodorm55p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm55p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotodorm55p1.hint]")
                if (not ev_makotodorm55p2.hint == "") and not (ev_makotodorm55p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotodorm55p2.hint:
                        textbutton _("[ev_makotodorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm55p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotodorm55p2.hint]")

            if Miku.active:
                if (not ev_mikuinvite1.hint == "") and not (ev_mikuinvite1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikuinvite1.hint:
                        textbutton _("[ev_mikuinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuinvite1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikuinvite1.hint]")
                if (not ev_mikuinvite2.hint == "") and not (ev_mikuinvite2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikuinvite2.hint:
                        textbutton _("[ev_mikuinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuinvite2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikuinvite2.hint]")
                if (not ev_mikupool55.hint == "") and not (ev_mikupool55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikupool55.hint:
                        textbutton _("[ev_mikupool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikupool55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikupool55.hint]")
                if (not ev_mikudorm55p1.hint == "") and not (ev_mikudorm55p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm55p1.hint:
                        textbutton _("[ev_mikudorm55p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm55p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm55p1.hint]")
                if (not ev_mikudorm55p2.hint == "") and not (ev_mikudorm55p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mikudorm55p2.hint:
                        textbutton _("[ev_mikudorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm55p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mikudorm55p2.hint]")

            if Futaba.active:
                if (not ev_futabadorm50.hint == "") and not (ev_futabadorm50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabadorm50.hint:
                        textbutton _("[ev_futabadorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabadorm50.hint]")
                if (not ev_library50.hint == "") and not (ev_library50.hint == "Event will trigger automatically."):
                    if "(!)" in ev_library50.hint:
                        textbutton _("[ev_library50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library50), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_library50.hint]")
                if (not ev_futabainvite3.hint == "") and not (ev_futabainvite3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabainvite3.hint:
                        textbutton _("[ev_futabainvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabainvite3.hint]")
                if (not ev_makotofutabafuntimelustevent.hint == "") and not (ev_makotofutabafuntimelustevent.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makotofutabafuntimelustevent.hint:
                        textbutton _("[ev_makotofutabafuntimelustevent.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotofutabafuntimelustevent), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makotofutabafuntimelustevent.hint]")
                if (not ev_futabaspecial60p1.hint == "") and not (ev_futabaspecial60p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabaspecial60p1.hint:
                        textbutton _("[ev_futabaspecial60p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabaspecial60p1.hint]")
                if (not ev_futabaspecial60p2.hint == "") and not (ev_futabaspecial60p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabaspecial60p2.hint:
                        textbutton _("[ev_futabaspecial60p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabaspecial60p2.hint]")
                if (not ev_futabaspecial60p3.hint == "") and not (ev_futabaspecial60p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_futabaspecial60p3.hint:
                        textbutton _("[ev_futabaspecial60p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_futabaspecial60p3.hint]")

            if Rin.active:
                if (not ev_rindorm55.hint == "") and not (ev_rindorm55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm55.hint:
                        textbutton _("[ev_rindorm55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm55.hint]")
                if (not ev_rindorm55p2.hint == "") and not (ev_rindorm55p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rindorm55p2.hint:
                        textbutton _("[ev_rindorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm55p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rindorm55p2.hint]")
                if (not ev_rinspecial55.hint == "") and not (ev_rinspecial55.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rinspecial55.hint:
                        textbutton _("[ev_rinspecial55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspecial55), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rinspecial55.hint]")

            if Molly.active:
                if (not ev_mollycafe30p1.hint == "") and not (ev_mollycafe30p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe30p1.hint:
                        textbutton _("[ev_mollycafe30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe30p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe30p1.hint]")
                if (not ev_mollycafe30p2.hint == "") and not (ev_mollycafe30p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollycafe30p2.hint:
                        textbutton _("[ev_mollycafe30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe30p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollycafe30p2.hint]")
                if (not ev_mollydate35p1.hint == "") and not (ev_mollydate35p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydate35p1.hint:
                        textbutton _("[ev_mollydate35p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydate35p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydate35p1.hint]")
                if (not ev_mollydate35p2.hint == "") and not (ev_mollydate35p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_mollydate35p2.hint:
                        textbutton _("[ev_mollydate35p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydate35p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_mollydate35p2.hint]")

            if Tsuneyo.active:
                if (not ev_tsuneyoslumber1.hint == "") and not (ev_tsuneyoslumber1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyoslumber1.hint:
                        textbutton _("[ev_tsuneyoslumber1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyoslumber1.hint]")
                if (not ev_tsuneyoslumber2.hint == "") and not (ev_tsuneyoslumber2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyoslumber2.hint:
                        textbutton _("[ev_tsuneyoslumber2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyoslumber2.hint]")
                if (not ev_tsuneyoslumber3.hint == "") and not (ev_tsuneyoslumber3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsuneyoslumber3.hint:
                        textbutton _("[ev_tsuneyoslumber3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsuneyoslumber3.hint]")

            if Sara.active:
                if (not ev_saraspecial30p1.hint == "") and not (ev_saraspecial30p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saraspecial30p1.hint:
                        textbutton _("[ev_saraspecial30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspecial30p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saraspecial30p1.hint]")
                    text ("")
                if (not ev_saraspecial30p2.hint == "") and not (ev_saraspecial30p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_saraspecial30p2.hint:
                        textbutton _("[ev_saraspecial30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspecial30p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_saraspecial30p2.hint]")
                if (not ev_sarabar30.hint == "") and not (ev_sarabar30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sarabar30.hint:
                        textbutton _("[ev_sarabar30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sarabar30.hint]")

            if Haruka.active:
                if (not ev_sadgirls2.hint == "") and not (ev_sadgirls2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls2.hint:
                        textbutton _("[ev_sadgirls2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls2.hint]")
                if (not ev_sadgirls4.hint == "") and not (ev_sadgirls4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls4.hint:
                        textbutton _("[ev_sadgirls4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls4.hint]")
                if (not ev_sadgirls5.hint == "") and not (ev_sadgirls5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls5.hint:
                        textbutton _("[ev_sadgirls5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls5.hint]")
                if (not ev_harukalust25.hint == "") and not (ev_harukalust25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukalust25.hint:
                        textbutton _("[ev_harukalust25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukalust25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukalust25.hint]")
                if (not ev_makihornytrip1.hint == "") and not (ev_makihornytrip1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makihornytrip1.hint:
                        textbutton _("[ev_makihornytrip1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makihornytrip1.hint]")
                if (not ev_makihornytrip4.hint == "") and not (ev_makihornytrip4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makihornytrip4.hint:
                        textbutton _("[ev_makihornytrip4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makihornytrip4.hint]")
                if (not ev_harukadate30.hint == "") and not (ev_harukadate30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_harukadate30.hint:
                        textbutton _("[ev_harukadate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_harukadate30.hint]")

            if Maki.active:
                if (not ev_sadgirls3.hint == "") and not (ev_sadgirls3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls3.hint:
                        textbutton _("[ev_sadgirls3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls3.hint]")
                if (not ev_sadgirls6.hint == "") and not (ev_sadgirls6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_sadgirls6.hint:
                        textbutton _("[ev_sadgirls6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_sadgirls6.hint]")
                if (not ev_makiinv3.hint == "") and not (ev_makiinv3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makiinv3.hint:
                        textbutton _("[ev_makiinv3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinv3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makiinv3.hint]")
                if (not ev_makihornyquestintro.hint == "") and not (ev_makihornyquestintro.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makihornyquestintro.hint:
                        textbutton _("[ev_makihornyquestintro.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornyquestintro), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makihornyquestintro.hint]")
                if (not ev_makihornytrip2.hint == "") and not (ev_makihornytrip2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makihornytrip2.hint:
                        textbutton _("[ev_makihornytrip2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makihornytrip2.hint]")
                if (not ev_makihornytrip3.hint == "") and not (ev_makihornytrip3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_makihornytrip3.hint:
                        textbutton _("[ev_makihornytrip3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_makihornytrip3.hint]")

            if Kirin.active:
                if (not ev_kirinlust30.hint == "") and not (ev_kirinlust30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinlust30.hint:
                        textbutton _("[ev_kirinlust30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinlust30.hint]")
                if (not ev_kirinspecial40.hint == "") and not (ev_kirinspecial40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinspecial40.hint:
                        textbutton _("[ev_kirinspecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinspecial40.hint]")
                if (not ev_kirinspecial45p1.hint == "") and not (ev_kirinspecial45p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinspecial45p1.hint:
                        textbutton _("[ev_kirinspecial45p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial45p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinspecial45p1.hint]")
                if (not ev_kirinspecial45p2.hint == "") and not (ev_kirinspecial45p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kirinspecial45p2.hint:
                        textbutton _("[ev_kirinspecial45p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial45p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kirinspecial45p2.hint]")

            if Karin.active:
                if (not ev_karindate25.hint == "") and not (ev_karindate25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate25.hint:
                        textbutton _("[ev_karindate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate25.hint]")
                if (not ev_karindate30.hint == "") and not (ev_karindate30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_karindate30.hint:
                        textbutton _("[ev_karindate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_karindate30.hint]")

            if Kaori.active:
                if (not ev_kaorispecial35.hint == "") and not (ev_kaorispecial35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaorispecial35.hint:
                        textbutton _("[ev_kaorispecial35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispecial35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaorispecial35.hint]")
                if (not ev_kaorispecial40.hint == "") and not (ev_kaorispecial40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaorispecial40.hint:
                        textbutton _("[ev_kaorispecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispecial40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaorispecial40.hint]")
                if (not ev_kaoridate40.hint == "") and not (ev_kaoridate40.hint == "Event will trigger automatically."):
                    if "(!)" in ev_kaoridate40.hint:
                        textbutton _("[ev_kaoridate40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate40), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_kaoridate40.hint]")
                    text ("")

            if Imani.active:
                if (not ev_imanidate1.hint == "") and not (ev_imanidate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanidate1.hint:
                        textbutton _("[ev_imanidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanidate1.hint]")
                if (not ev_imanidate5.hint == "") and not (ev_imanidate5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanidate5.hint:
                        textbutton _("[ev_imanidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanidate5.hint]")
                if (not ev_imanidate15p1.hint == "") and not (ev_imanidate15p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanidate15p1.hint:
                        textbutton _("[ev_imanidate15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate15p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanidate15p1.hint]")
                if (not ev_imanidate15p2.hint == "") and not (ev_imanidate15p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanidate15p2.hint:
                        textbutton _("[ev_imanidate15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate15p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanidate15p2.hint]")
                if (not ev_imanispecial15.hint == "") and not (ev_imanispecial15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanispecial15.hint:
                        textbutton _("[ev_imanispecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispecial15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanispecial15.hint]")

            if Rika.active:
                if (not ev_rikadate1.hint == "") and not (ev_rikadate1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rikadate1.hint:
                        textbutton _("[ev_rikadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikadate1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rikadate1.hint]")
                if (not ev_rikaspecial2.hint == "") and not (ev_rikaspecial2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rikaspecial2.hint:
                        textbutton _("[ev_rikaspecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspecial2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rikaspecial2.hint]")
                if (not ev_rikadive1.hint == "") and not (ev_rikadive1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rikadive1.hint:
                        textbutton _("[ev_rikadive1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikadive1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rikadive1.hint]")
                    text ("")

            if Nao.active:
                if (not ev_naospecial1.hint == "") and not (ev_naospecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_naospecial1.hint:
                        textbutton _("[ev_naospecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_naospecial1.hint]")
                if (not ev_naospecial2.hint == "") and not (ev_naospecial2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_naospecial2.hint:
                        textbutton _("[ev_naospecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_naospecial2.hint]")
                if (not ev_naospecial3.hint == "") and not (ev_naospecial3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_naospecial3.hint:
                        textbutton _("[ev_naospecial3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_naospecial3.hint]")

            if Chinami.active:
                if (not ev_chinamidate25.hint == "") and not (ev_chinamidate25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate25.hint:
                        textbutton _("[ev_chinamidate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate25.hint]")
                if (not ev_chinamidate30.hint == "") and not (ev_chinamidate30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chinamidate30.hint:
                        textbutton _("[ev_chinamidate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chinamidate30.hint]")
                if (not ev_chapthree1.hint == "") and not (ev_chapthree1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree1.hint:
                        textbutton _("[ev_chapthree1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree1.hint]")
                if (not ev_chapthree2.hint == "") and not (ev_chapthree2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree2.hint:
                        textbutton _("[ev_chapthree2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree2.hint]")
                if (not ev_chapthree3.hint == "") and not (ev_chapthree3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree3.hint:
                        textbutton _("[ev_chapthree3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree3.hint]")
                if (not ev_chapthree4.hint == "") and not (ev_chapthree4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree4.hint:
                        textbutton _("[ev_chapthree4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree4.hint]")
                if (not ev_chapthree5.hint == "") and not (ev_chapthree5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree5.hint:
                        textbutton _("[ev_chapthree5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree5.hint]")
                if (not ev_chapthree6.hint == "") and not (ev_chapthree6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree6.hint:
                        textbutton _("[ev_chapthree6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree6.hint]")
                    text ("")
                if (not ev_chapthree7.hint == "") and not (ev_chapthree7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree7.hint:
                        textbutton _("[ev_chapthree7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree7.hint]")
                if (not ev_chapthree8.hint == "") and not (ev_chapthree8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_chapthree8.hint:
                        textbutton _("[ev_chapthree8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chapthree8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_chapthree8.hint]")
                if (not ev_yumichikaspecial1.hint == "") and not (ev_yumichikaspecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumichikaspecial1.hint:
                        textbutton _("[ev_yumichikaspecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumichikaspecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumichikaspecial1.hint]")
                if (not ev_yumiyukispecial1.hint == "") and not (ev_yumiyukispecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yumiyukispecial1.hint:
                        textbutton _("[ev_yumiyukispecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumiyukispecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yumiyukispecial1.hint]")
                if (not ev_imanispecial1.hint == "") and not (ev_imanispecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_imanispecial1.hint:
                        textbutton _("[ev_imanispecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_imanispecial1.hint]")
                if (not ev_rikaspecial1.hint == "") and not (ev_rikaspecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_rikaspecial1.hint:
                        textbutton _("[ev_rikaspecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_rikaspecial1.hint]")
                if (not ev_day543.hint == "") and not (ev_day543.hint == "Event will trigger automatically."):
                    if "(!)" in ev_day543.hint:
                        textbutton _("[ev_day543.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day543), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_day543.hint]")
                if (not ev_dormwartwo1.hint == "") and not (ev_dormwartwo1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo1.hint:
                        textbutton _("[ev_dormwartwo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo1.hint]")
                if (not ev_dormwartwo2.hint == "") and not (ev_dormwartwo2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo2.hint:
                        textbutton _("[ev_dormwartwo2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo2.hint]")
                if (not ev_dormwartwo3.hint == "") and not (ev_dormwartwo3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo3.hint:
                        textbutton _("[ev_dormwartwo3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo3.hint]")
                if (not ev_dormwartwo4.hint == "") and not (ev_dormwartwo4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo4.hint:
                        textbutton _("[ev_dormwartwo4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo4.hint]")
                if (not ev_dormwartwo5.hint == "") and not (ev_dormwartwo5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo5.hint:
                        textbutton _("[ev_dormwartwo5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo5.hint]")
                if (not ev_dormwartwo6.hint == "") and not (ev_dormwartwo6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo6.hint:
                        textbutton _("[ev_dormwartwo6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo6.hint]")
                if (not ev_dormwartwo7.hint == "") and not (ev_dormwartwo7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo7.hint:
                        textbutton _("[ev_dormwartwo7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo7.hint]")
                if (not ev_dormwartwo8.hint == "") and not (ev_dormwartwo8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo8.hint:
                        textbutton _("[ev_dormwartwo8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo8.hint]")
                if (not ev_dormwartwo9.hint == "") and not (ev_dormwartwo9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo9.hint:
                        textbutton _("[ev_dormwartwo9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo9.hint]")
                if (not ev_dormwartwo10.hint == "") and not (ev_dormwartwo10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo10.hint:
                        textbutton _("[ev_dormwartwo10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo10.hint]")
                if (not ev_dormwartwo11.hint == "") and not (ev_dormwartwo11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo11.hint:
                        textbutton _("[ev_dormwartwo11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo11.hint]")
                if (not ev_dormwartwo12.hint == "") and not (ev_dormwartwo12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo12.hint:
                        textbutton _("[ev_dormwartwo12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo12.hint]")
                if (not ev_dormwartwo13.hint == "") and not (ev_dormwartwo13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo13.hint:
                        textbutton _("[ev_dormwartwo13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo13.hint]")
                if (not ev_dormwartwo14.hint == "") and not (ev_dormwartwo14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo14.hint:
                        textbutton _("[ev_dormwartwo14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo14.hint]")
                if (not ev_dormwartwo15.hint == "") and not (ev_dormwartwo15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo15.hint:
                        textbutton _("[ev_dormwartwo15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo15.hint]")
                    text ("")
                if (not ev_dormwartwo16.hint == "") and not (ev_dormwartwo16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo16.hint:
                        textbutton _("[ev_dormwartwo16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo16.hint]")
                if (not ev_dormwartwo17.hint == "") and not (ev_dormwartwo17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo17.hint:
                        textbutton _("[ev_dormwartwo17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo17.hint]")
                if (not ev_dormwartwo18.hint == "") and not (ev_dormwartwo18.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo18.hint:
                        textbutton _("[ev_dormwartwo18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo18), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo18.hint]")
                if (not ev_dormwartwo19.hint == "") and not (ev_dormwartwo19.hint == "Event will trigger automatically."):
                    if "(!)" in ev_dormwartwo19.hint:
                        textbutton _("[ev_dormwartwo19.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwartwo19), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_dormwartwo19.hint]")
                if (not ev_beachmas1.hint == "") and not (ev_beachmas1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas1.hint:
                        textbutton _("[ev_beachmas1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas1.hint]")
                if (not ev_beachmas2.hint == "") and not (ev_beachmas2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas2.hint:
                        textbutton _("[ev_beachmas2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas2.hint]")
                if (not ev_beachmas3.hint == "") and not (ev_beachmas3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas3.hint:
                        textbutton _("[ev_beachmas3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas3.hint]")
                if (not ev_beachmas4.hint == "") and not (ev_beachmas4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas4.hint:
                        textbutton _("[ev_beachmas4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas4.hint]")
                if (not ev_beachmas5.hint == "") and not (ev_beachmas5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas5.hint:
                        textbutton _("[ev_beachmas5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas5.hint]")
                if (not ev_beachmas6.hint == "") and not (ev_beachmas6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas6.hint:
                        textbutton _("[ev_beachmas6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas6.hint]")
                if (not ev_beachmas7.hint == "") and not (ev_beachmas7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas7.hint:
                        textbutton _("[ev_beachmas7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas7.hint]")
                if (not ev_beachmas8.hint == "") and not (ev_beachmas8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas8.hint:
                        textbutton _("[ev_beachmas8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas8.hint]")
                if (not ev_beachmas9.hint == "") and not (ev_beachmas9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas9.hint:
                        textbutton _("[ev_beachmas9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas9.hint]")
                if (not ev_beachmas10.hint == "") and not (ev_beachmas10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas10.hint:
                        textbutton _("[ev_beachmas10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas10.hint]")
                if (not ev_beachmas11.hint == "") and not (ev_beachmas11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas11.hint:
                        textbutton _("[ev_beachmas11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas11.hint]")
                if (not ev_beachmas12.hint == "") and not (ev_beachmas12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas12.hint:
                        textbutton _("[ev_beachmas12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas12.hint]")
                if (not ev_beachmas13.hint == "") and not (ev_beachmas13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas13.hint:
                        textbutton _("[ev_beachmas13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas13.hint]")
                if (not ev_beachmas14.hint == "") and not (ev_beachmas14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas14.hint:
                        textbutton _("[ev_beachmas14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas14.hint]")
                if (not ev_beachmas15.hint == "") and not (ev_beachmas15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas15.hint:
                        textbutton _("[ev_beachmas15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas15.hint]")
                if (not ev_beachmas16.hint == "") and not (ev_beachmas16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas16.hint:
                        textbutton _("[ev_beachmas16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas16.hint]")
                if (not ev_beachmas17.hint == "") and not (ev_beachmas17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas17.hint:
                        textbutton _("[ev_beachmas17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas17.hint]")
                if (not ev_beachmas18.hint == "") and not (ev_beachmas18.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas18.hint:
                        textbutton _("[ev_beachmas18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas18), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas18.hint]")
                if (not ev_beachmas19.hint == "") and not (ev_beachmas19.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas19.hint:
                        textbutton _("[ev_beachmas19.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas19), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas19.hint]")
                    text ("")
                if (not ev_beachmas20.hint == "") and not (ev_beachmas20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachmas20.hint:
                        textbutton _("[ev_beachmas20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachmas20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachmas20.hint]")
                if (not ev_slumberreset1.hint == "") and not (ev_slumberreset1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_slumberreset1.hint:
                        textbutton _("[ev_slumberreset1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_slumberreset1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_slumberreset1.hint]")
                if (not ev_slumberreset2.hint == "") and not (ev_slumberreset2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_slumberreset2.hint:
                        textbutton _("[ev_slumberreset2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_slumberreset2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_slumberreset2.hint]")
                if (not ev_slumberreset3.hint == "") and not (ev_slumberreset3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_slumberreset3.hint:
                        textbutton _("[ev_slumberreset3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_slumberreset3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_slumberreset3.hint]")
                    text ("")
                if (not ev_slumberreset4.hint == "") and not (ev_slumberreset4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_slumberreset4.hint:
                        textbutton _("[ev_slumberreset4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_slumberreset4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_slumberreset4.hint]")
                if (not ev_slumberreset5.hint == "") and not (ev_slumberreset5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_slumberreset5.hint:
                        textbutton _("[ev_slumberreset5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_slumberreset5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_slumberreset5.hint]")
                if (not ev_postnodokachain1.hint == "") and not (ev_postnodokachain1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_postnodokachain1.hint:
                        textbutton _("[ev_postnodokachain1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_postnodokachain1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_postnodokachain1.hint]")
                if (not ev_treasureisland.hint == "") and not (ev_treasureisland.hint == "Event will trigger automatically."):
                    if "(!)" in ev_treasureisland.hint:
                        textbutton _("[ev_treasureisland.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_treasureisland), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_treasureisland.hint]")
                if (not ev_amispecial50mainp1.hint == "") and not (ev_amispecial50mainp1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amispecial50mainp1.hint:
                        textbutton _("[ev_amispecial50mainp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispecial50mainp1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amispecial50mainp1.hint]")
                if (not ev_amispecial50mainp2.hint == "") and not (ev_amispecial50mainp2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_amispecial50mainp2.hint:
                        textbutton _("[ev_amispecial50mainp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispecial50mainp2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_amispecial50mainp2.hint]")
                if (not ev_predormwars3.hint == "") and not (ev_predormwars3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_predormwars3.hint:
                        textbutton _("[ev_predormwars3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_predormwars3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_predormwars3.hint]")
                if (not ev_beachwars1.hint == "") and not (ev_beachwars1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars1.hint:
                        textbutton _("[ev_beachwars1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars1.hint]")
                if (not ev_beachwars2.hint == "") and not (ev_beachwars2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars2.hint:
                        textbutton _("[ev_beachwars2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars2.hint]")
                if (not ev_beachwars3.hint == "") and not (ev_beachwars3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars3.hint:
                        textbutton _("[ev_beachwars3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars3.hint]")
                if (not ev_beachwars4.hint == "") and not (ev_beachwars4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars4.hint:
                        textbutton _("[ev_beachwars4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars4.hint]")
                if (not ev_beachwars5.hint == "") and not (ev_beachwars5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars5.hint:
                        textbutton _("[ev_beachwars5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars5.hint]")
                if (not ev_beachwars6.hint == "") and not (ev_beachwars6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars6.hint:
                        textbutton _("[ev_beachwars6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars6.hint]")
                if (not ev_beachwars7.hint == "") and not (ev_beachwars7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars7.hint:
                        textbutton _("[ev_beachwars7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars7.hint]")
                if (not ev_beachwars8.hint == "") and not (ev_beachwars8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars8.hint:
                        textbutton _("[ev_beachwars8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars8.hint]")
                if (not ev_beachwars9.hint == "") and not (ev_beachwars9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars9.hint:
                        textbutton _("[ev_beachwars9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars9.hint]")
                    text ("")
                if (not ev_beachwars10.hint == "") and not (ev_beachwars10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars10.hint:
                        textbutton _("[ev_beachwars10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars10.hint]")
                if (not ev_beachwars11.hint == "") and not (ev_beachwars11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars11.hint:
                        textbutton _("[ev_beachwars11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars11.hint]")
                if (not ev_beachwars12.hint == "") and not (ev_beachwars12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars12.hint:
                        textbutton _("[ev_beachwars12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars12.hint]")
                if (not ev_beachwars13.hint == "") and not (ev_beachwars13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars13.hint:
                        textbutton _("[ev_beachwars13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars13.hint]")
                if (not ev_beachwars14.hint == "") and not (ev_beachwars14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars14.hint:
                        textbutton _("[ev_beachwars14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars14.hint]")
                if (not ev_beachwars15.hint == "") and not (ev_beachwars15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars15.hint:
                        textbutton _("[ev_beachwars15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars15.hint]")
                if (not ev_beachwars16.hint == "") and not (ev_beachwars16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars16.hint:
                        textbutton _("[ev_beachwars16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars16.hint]")
                if (not ev_beachwars17.hint == "") and not (ev_beachwars17.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars17.hint:
                        textbutton _("[ev_beachwars17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars17), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars17.hint]")
                if (not ev_beachwars18.hint == "") and not (ev_beachwars18.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars18.hint:
                        textbutton _("[ev_beachwars18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars18), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars18.hint]")
                if (not ev_beachwars19.hint == "") and not (ev_beachwars19.hint == "Event will trigger automatically."):
                    if "(!)" in ev_beachwars19.hint:
                        textbutton _("[ev_beachwars19.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachwars19), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_beachwars19.hint]")
                if (not ev_halloweenfour1.hint == "") and not (ev_halloweenfour1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour1.hint:
                        textbutton _("[ev_halloweenfour1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour1.hint]")
                if (not ev_halloweenfour2.hint == "") and not (ev_halloweenfour2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour2.hint:
                        textbutton _("[ev_halloweenfour2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour2.hint]")
                if (not ev_halloweenfour3.hint == "") and not (ev_halloweenfour3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour3.hint:
                        textbutton _("[ev_halloweenfour3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour3.hint]")
                if (not ev_halloweenfour4.hint == "") and not (ev_halloweenfour4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour4.hint:
                        textbutton _("[ev_halloweenfour4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour4.hint]")
                if (not ev_halloweenfour5.hint == "") and not (ev_halloweenfour5.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour5.hint:
                        textbutton _("[ev_halloweenfour5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour5), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour5.hint]")
                if (not ev_halloweenfour6.hint == "") and not (ev_halloweenfour6.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour6.hint:
                        textbutton _("[ev_halloweenfour6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour6), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour6.hint]")
                if (not ev_halloweenfour7.hint == "") and not (ev_halloweenfour7.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour7.hint:
                        textbutton _("[ev_halloweenfour7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour7), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour7.hint]")
                if (not ev_halloweenfour8.hint == "") and not (ev_halloweenfour8.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour8.hint:
                        textbutton _("[ev_halloweenfour8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour8), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour8.hint]")
                if (not ev_halloweenfour9.hint == "") and not (ev_halloweenfour9.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour9.hint:
                        textbutton _("[ev_halloweenfour9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour9), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour9.hint]")
                if (not ev_halloweenfour10.hint == "") and not (ev_halloweenfour10.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour10.hint:
                        textbutton _("[ev_halloweenfour10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour10), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour10.hint]")
                    text ("")
                if (not ev_halloweenfour11.hint == "") and not (ev_halloweenfour11.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour11.hint:
                        textbutton _("[ev_halloweenfour11.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour11), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour11.hint]")
                if (not ev_halloweenfour12.hint == "") and not (ev_halloweenfour12.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour12.hint:
                        textbutton _("[ev_halloweenfour12.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour12), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour12.hint]")
                if (not ev_halloweenfour13.hint == "") and not (ev_halloweenfour13.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour13.hint:
                        textbutton _("[ev_halloweenfour13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour13), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour13.hint]")
                if (not ev_halloweenfour14.hint == "") and not (ev_halloweenfour14.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour14.hint:
                        textbutton _("[ev_halloweenfour14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour14), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour14.hint]")
                if (not ev_halloweenfour15.hint == "") and not (ev_halloweenfour15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour15.hint:
                        textbutton _("[ev_halloweenfour15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour15.hint]")
                if (not ev_halloweenfour16.hint == "") and not (ev_halloweenfour16.hint == "Event will trigger automatically."):
                    if "(!)" in ev_halloweenfour16.hint:
                        textbutton _("[ev_halloweenfour16.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenfour16), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_halloweenfour16.hint]")
                if (not ev_resetsix1.hint == "") and not (ev_resetsix1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_resetsix1.hint:
                        textbutton _("[ev_resetsix1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_resetsix1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_resetsix1.hint]")
                if (not ev_resetsix2.hint == "") and not (ev_resetsix2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_resetsix2.hint:
                        textbutton _("[ev_resetsix2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_resetsix2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_resetsix2.hint]")
                if (not ev_resetsix3.hint == "") and not (ev_resetsix3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_resetsix3.hint:
                        textbutton _("[ev_resetsix3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_resetsix3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_resetsix3.hint]")
                if (not ev_resetsix4.hint == "") and not (ev_resetsix4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_resetsix4.hint:
                        textbutton _("[ev_resetsix4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_resetsix4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_resetsix4.hint]")

            if Yuki.active:
                if (not ev_yukidate20p1.hint == "") and not (ev_yukidate20p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate20p1.hint:
                        textbutton _("[ev_yukidate20p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate20p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate20p1.hint]")
                if (not ev_yukidate20p2.hint == "") and not (ev_yukidate20p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate20p2.hint:
                        textbutton _("[ev_yukidate20p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate20p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate20p2.hint]")
                if (not ev_yukidate25.hint == "") and not (ev_yukidate25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yukidate25.hint:
                        textbutton _("[ev_yukidate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yukidate25.hint]")

            if Wakana.active:
                if (not ev_wakanadate15.hint == "") and not (ev_wakanadate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate15.hint:
                        textbutton _("[ev_wakanadate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate15.hint]")
                if (not ev_wakanaspecial15.hint == "") and not (ev_wakanaspecial15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanaspecial15.hint:
                        textbutton _("[ev_wakanaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspecial15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanaspecial15.hint]")
                if (not ev_wakanadate25p1.hint == "") and not (ev_wakanadate25p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate25p1.hint:
                        textbutton _("[ev_wakanadate25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate25p1.hint]")
                if (not ev_wakanadate25p2.hint == "") and not (ev_wakanadate25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate25p2.hint:
                        textbutton _("[ev_wakanadate25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate25p2.hint]")
                if (not ev_wakanadate25p3.hint == "") and not (ev_wakanadate25p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_wakanadate25p3.hint:
                        textbutton _("[ev_wakanadate25p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_wakanadate25p3.hint]")

            if Osako.active:
                if (not ev_osakodate15.hint == "") and not (ev_osakodate15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_osakodate15.hint:
                        textbutton _("[ev_osakodate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_osakodate15.hint]")
                if (not ev_osakodate20.hint == "") and not (ev_osakodate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_osakodate20.hint:
                        textbutton _("[ev_osakodate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_osakodate20.hint]")

            if Tsubasa.active:
                if (not ev_tsubasaspecial15.hint == "") and not (ev_tsubasaspecial15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsubasaspecial15.hint:
                        textbutton _("[ev_tsubasaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspecial15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsubasaspecial15.hint]")
                if (not ev_tsubasadate20.hint == "") and not (ev_tsubasadate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsubasadate20.hint:
                        textbutton _("[ev_tsubasadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsubasadate20.hint]")
                if (not ev_tsubasaspecial20.hint == "") and not (ev_tsubasaspecial20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsubasaspecial20.hint:
                        textbutton _("[ev_tsubasaspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspecial20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsubasaspecial20.hint]")

            if Tsukasa.active:
                if (not ev_tsukasaspecial1.hint == "") and not (ev_tsukasaspecial1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsukasaspecial1.hint:
                        textbutton _("[ev_tsukasaspecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspecial1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsukasaspecial1.hint]")
                if (not ev_tsukasaspecial1p2.hint == "") and not (ev_tsukasaspecial1p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_tsukasaspecial1p2.hint:
                        textbutton _("[ev_tsukasaspecial1p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspecial1p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_tsukasaspecial1p2.hint]")

            if Uta.active:
                if (not ev_utaarchery1.hint == "") and not (ev_utaarchery1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utaarchery1.hint:
                        textbutton _("[ev_utaarchery1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaarchery1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utaarchery1.hint]")
                if (not ev_utamaid25p1.hint == "") and not (ev_utamaid25p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid25p1.hint:
                        textbutton _("[ev_utamaid25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid25p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid25p1.hint]")
                if (not ev_utamaid25p2.hint == "") and not (ev_utamaid25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utamaid25p2.hint:
                        textbutton _("[ev_utamaid25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utamaid25p2.hint]")
                if (not ev_utadorm30.hint == "") and not (ev_utadorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm30.hint:
                        textbutton _("[ev_utadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm30.hint]")
                if (not ev_utaspecial35.hint == "") and not (ev_utaspecial35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utaspecial35.hint:
                        textbutton _("[ev_utaspecial35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspecial35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utaspecial35.hint]")
                if (not ev_utadate35.hint == "") and not (ev_utadate35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadate35.hint:
                        textbutton _("[ev_utadate35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadate35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadate35.hint]")
                if (not ev_utadorm40p1.hint == "") and not (ev_utadorm40p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm40p1.hint:
                        textbutton _("[ev_utadorm40p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm40p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm40p1.hint]")
                if (not ev_utadorm40p2.hint == "") and not (ev_utadorm40p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_utadorm40p2.hint:
                        textbutton _("[ev_utadorm40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm40p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_utadorm40p2.hint]")

            if Io.active:
                if (not ev_ioarchery1.hint == "") and not (ev_ioarchery1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ioarchery1.hint:
                        textbutton _("[ev_ioarchery1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ioarchery1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ioarchery1.hint]")
                if (not ev_bathhouse25.hint == "") and not (ev_bathhouse25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse25.hint:
                        textbutton _("[ev_bathhouse25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse25.hint]")
                if (not ev_iodorm25.hint == "") and not (ev_iodorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iodorm25.hint:
                        textbutton _("[ev_iodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iodorm25.hint]")
                if (not ev_iospecial30.hint == "") and not (ev_iospecial30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iospecial30.hint:
                        textbutton _("[ev_iospecial30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospecial30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iospecial30.hint]")
                    text ("")
                if (not ev_bathhouse35p1.hint == "") and not (ev_bathhouse35p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse35p1.hint:
                        textbutton _("[ev_bathhouse35p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse35p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse35p1.hint]")
                if (not ev_bathhouse35p2.hint == "") and not (ev_bathhouse35p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_bathhouse35p2.hint:
                        textbutton _("[ev_bathhouse35p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse35p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_bathhouse35p2.hint]")
                if (not ev_iodorm35.hint == "") and not (ev_iodorm35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_iodorm35.hint:
                        textbutton _("[ev_iodorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_iodorm35.hint]")
                if (not ev_ioarchery35.hint == "") and not (ev_ioarchery35.hint == "Event will trigger automatically."):
                    if "(!)" in ev_ioarchery35.hint:
                        textbutton _("[ev_ioarchery35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ioarchery35), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_ioarchery35.hint]")

            if Noriko.active:
                if (not ev_norikodate30.hint == "") and not (ev_norikodate30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodate30.hint:
                        textbutton _("[ev_norikodate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodate30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodate30.hint]")
                if (not ev_norikodorm30.hint == "") and not (ev_norikodorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikodorm30.hint:
                        textbutton _("[ev_norikodorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikodorm30.hint]")
                if (not ev_norikoinvite3.hint == "") and not (ev_norikoinvite3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikoinvite3.hint:
                        textbutton _("[ev_norikoinvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikoinvite3.hint]")
                    text ("")
                if (not ev_norikoinvite4.hint == "") and not (ev_norikoinvite4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_norikoinvite4.hint:
                        textbutton _("[ev_norikoinvite4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_norikoinvite4.hint]")

            if Niki.active:
                if (not ev_nikilovesyou1.hint == "") and not (ev_nikilovesyou1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikilovesyou1.hint:
                        textbutton _("[ev_nikilovesyou1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikilovesyou1.hint]")
                if (not ev_nikilovesyou2.hint == "") and not (ev_nikilovesyou2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikilovesyou2.hint:
                        textbutton _("[ev_nikilovesyou2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikilovesyou2.hint]")
                    text ("")
                if (not ev_nikilovesyou3.hint == "") and not (ev_nikilovesyou3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikilovesyou3.hint:
                        textbutton _("[ev_nikilovesyou3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikilovesyou3.hint]")
                if (not ev_nikifirstlust.hint == "") and not (ev_nikifirstlust.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nikifirstlust.hint:
                        textbutton _("[ev_nikifirstlust.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikifirstlust), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nikifirstlust.hint]")

            if Nodoka.active:
                if (not ev_nodokadorm15.hint == "") and not (ev_nodokadorm15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokadorm15.hint:
                        textbutton _("[ev_nodokadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokadorm15.hint]")
                if (not ev_nodokaspecial15p1.hint == "") and not (ev_nodokaspecial15p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial15p1.hint:
                        textbutton _("[ev_nodokaspecial15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial15p1.hint]")
                if (not ev_nodokaspecial15p2.hint == "") and not (ev_nodokaspecial15p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial15p2.hint:
                        textbutton _("[ev_nodokaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial15p2.hint]")
                if (not ev_nodokaspecial15p3.hint == "") and not (ev_nodokaspecial15p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial15p3.hint:
                        textbutton _("[ev_nodokaspecial15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial15p3.hint]")
                if (not ev_nodokaspecial20.hint == "") and not (ev_nodokaspecial20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial20.hint:
                        textbutton _("[ev_nodokaspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial20.hint]")
                if (not ev_nodokaspecial30p1.hint == "") and not (ev_nodokaspecial30p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial30p1.hint:
                        textbutton _("[ev_nodokaspecial30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial30p1.hint]")
                    text ("")
                if (not ev_nodokaspecial30p2.hint == "") and not (ev_nodokaspecial30p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial30p2.hint:
                        textbutton _("[ev_nodokaspecial30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial30p2.hint]")
                if (not ev_nodokaspecial30p3.hint == "") and not (ev_nodokaspecial30p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial30p3.hint:
                        textbutton _("[ev_nodokaspecial30p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial30p3.hint]")
                if (not ev_nodokaspecial30p4.hint == "") and not (ev_nodokaspecial30p4.hint == "Event will trigger automatically."):
                    if "(!)" in ev_nodokaspecial30p4.hint:
                        textbutton _("[ev_nodokaspecial30p4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p4), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_nodokaspecial30p4.hint]")

            if Otoha.active:
                if (not ev_otohaspecial15p1.hint == "") and not (ev_otohaspecial15p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohaspecial15p1.hint:
                        textbutton _("[ev_otohaspecial15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial15p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohaspecial15p1.hint]")
                if (not ev_otohaspecial15p2.hint == "") and not (ev_otohaspecial15p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohaspecial15p2.hint:
                        textbutton _("[ev_otohaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial15p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohaspecial15p2.hint]")
                if (not ev_otohadate20.hint == "") and not (ev_otohadate20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_otohadate20.hint:
                        textbutton _("[ev_otohadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadate20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_otohadate20.hint]")

            if Touka.active:
                if (not ev_toukaarchery20.hint == "") and not (ev_toukaarchery20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukaarchery20.hint:
                        textbutton _("[ev_toukaarchery20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaarchery20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukaarchery20.hint]")
                if (not ev_toukadorm25p1.hint == "") and not (ev_toukadorm25p1.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm25p1.hint:
                        textbutton _("[ev_toukadorm25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p1), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm25p1.hint]")
                if (not ev_toukadorm25p2.hint == "") and not (ev_toukadorm25p2.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm25p2.hint:
                        textbutton _("[ev_toukadorm25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p2), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm25p2.hint]")
                if (not ev_toukadorm25p3.hint == "") and not (ev_toukadorm25p3.hint == "Event will trigger automatically."):
                    if "(!)" in ev_toukadorm25p3.hint:
                        textbutton _("[ev_toukadorm25p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p3), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_toukadorm25p3.hint]")

            if Yasu.active:
                if (not ev_church15.hint == "") and not (ev_church15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church15.hint:
                        textbutton _("[ev_church15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church15.hint]")
                if (not ev_yasuspecial15.hint == "") and not (ev_yasuspecial15.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasuspecial15.hint:
                        textbutton _("[ev_yasuspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspecial15), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasuspecial15.hint]")
                if (not ev_church20.hint == "") and not (ev_church20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church20.hint:
                        textbutton _("[ev_church20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church20.hint]")
                if (not ev_yasudorm20.hint == "") and not (ev_yasudorm20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasudorm20.hint:
                        textbutton _("[ev_yasudorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasudorm20.hint]")
                if (not ev_yasuspecial20.hint == "") and not (ev_yasuspecial20.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasuspecial20.hint:
                        textbutton _("[ev_yasuspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspecial20), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasuspecial20.hint]")
                if (not ev_church25.hint == "") and not (ev_church25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_church25.hint:
                        textbutton _("[ev_church25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_church25.hint]")
                if (not ev_yasudorm25.hint == "") and not (ev_yasudorm25.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasudorm25.hint:
                        textbutton _("[ev_yasudorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm25), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasudorm25.hint]")
                if (not ev_yasudorm30.hint == "") and not (ev_yasudorm30.hint == "Event will trigger automatically."):
                    if "(!)" in ev_yasudorm30.hint:
                        textbutton _("[ev_yasudorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm30), SetVariable("previous_screen", "hints")] style "event_button" text_style "hint_text"
                    else:
                        text ("[ev_yasudorm30.hint]")

    vbox: #box for the Back button
        xpos .25
        ypos .916
        hbox:
            textbutton _("Back") action ShowMenu("progressmod")
