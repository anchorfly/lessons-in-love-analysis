screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Event Tracker") action ShowMenu('eventtracker11')
            textbutton _("Girls") action ShowMenu('eventtrackercharahub')
        # AVN Mod
            # textbutton _("Progress") action ShowMenu('affection')
            if resetsix4 == False:
                textbutton _("Progress") action ShowMenu('affection_avn')
            else:
                textbutton _("Progress") action ShowMenu('affection')
        # AVN Mod    
            textbutton _("Unlockables") action ShowMenu('unlockables')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            textbutton _("Events") action ShowMenu('eventtracker11')
            textbutton _("Girls") action ShowMenu('eventtrackercharahub')
        # AVN Mod
            # textbutton _("Progress") action ShowMenu('affection')
            if resetsix4 == False:
                textbutton _("Progress") action ShowMenu('affection_avn')
            else:
                textbutton _("Progress") action ShowMenu('affection')
        # AVN Mod    
            textbutton _("Unlockables") action ShowMenu('unlockables')
            if bonus == True:
                textbutton _("Wiki") action OpenURL("https://lessonsinlove.wiki/")
            textbutton _("Hide") action HideInterface()


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    if persistent.main_menu_image is not None and renpy.loadable(persistent.main_menu_image) :
        add persistent.main_menu_image
    else :
        add gui.main_menu_background

    add gui.main_menu_overlay

    # AVN Mod
    # if len(installed_care_packages) > 0:
    #     textbutton _("Change Menu Image"):
    #         action ShowMenu("main_menu_image_picker")
    #         xpos 60 ypos 900
    textbutton _("Change Menu Image"):
        action ShowMenu("main_menu_image_picker_avn")
        xpos 60 ypos 900
    # AVN Mod

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            if bonus == True:
                text "[config.name!t]":
                    style "main_menu_title"
            else:
                text "Hug Simulator":
                    style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


screen main_menu_image_picker_avn:
    tag menu

    use game_menu(_("Picker"), scroll="viewport"):

        style_prefix "aff"

        vpgrid :
            cols 2
            align (0.6, 0.45)
            spacing 80

            imagebutton:
                idle im.FactorScale("gui/main_menu.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", None), Return()]

            for img in installed_menu_images:
                imagebutton:
                    idle im.FactorScale(img.file, 0.3, bilinear=True)
                    action [SetVariable("persistent.main_menu_image", img.file), Return()]

        # AVN Mod
            imagebutton:
                idle im.FactorScale("gui/main_menuold.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "gui/main_menuold.png"), Return()]
            imagebutton:
                idle im.FactorScale("gui/main_menu2.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "gui/main_menu2.png"), Return()]
            imagebutton:
                idle im.FactorScale("gui/main_menu3.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "gui/main_menu3.png"), Return()]
            imagebutton:
                idle im.FactorScale("gui/main_menu4.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "gui/main_menu4.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_24.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_24.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_25p1.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_25p1.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_25p2.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_25p2.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_26p1.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_26p1.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_26p2.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_26p2.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_26p3.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_26p3.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_27.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_27.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_28.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_28.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_29.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_29.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_30.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_30.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_31.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_31.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_32.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_32.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_33.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_33.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_34.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_34.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_35.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_35.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_36.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_36.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_37.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_37.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_38.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_38.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_39.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_39.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_40.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_40.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_41.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_41.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_42.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_42.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_43.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_43.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_44.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_44.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_45.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_45.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_46.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_46.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_47.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_47.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_48.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_48.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_49.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_49.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_50.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_50.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_51.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_51.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_52.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_52.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_53.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_53.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_54.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_54.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_55.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_55.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_56.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_56.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_57.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_57.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_58.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_58.png"), Return()]
            imagebutton:
                idle im.FactorScale("avn_mod/Images/main_menu_59.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", "avn_mod/Images/main_menu_59.png"), Return()]
        # AVN Mod


screen affection_avn():

    tag menu

    $ v11check()

    python:
        amimaxpoint = 42 if resetsix4 == True else 33 if chapthreeactive == True else 28 if hoorayanotherreset == True else 16
        ayanemaxpoint = 53 if resetsix4 == True else 34 if chapthreeactive == True else 26 if hoorayanotherreset == True else 18
        chikamaxpoint = 38 if resetsix4 == True else 28 if chapthreeactive == True else 24 if hoorayanotherreset == True else 13
        chinamimaxpoint = 15 if resetsix4 == True else 7 if chapthreeactive == True else 5 if hoorayanotherreset == True else 2
        futabamaxpoint = 42 if resetsix4 == True else 34 if chapthreeactive == True else 27 if hoorayanotherreset == True else 19
        harukamaxpoint = 26 if resetsix4 == True else 17 if chapthreeactive == True else 10 if hoorayanotherreset == True else 6
        imanimaxpoint = 13 if resetsix4 == True else 5 if chapthreeactive == True else 0 if hoorayanotherreset == True else 0
        iomaxpoint = 26 if resetsix4 == True else 17 if chapthreeactive == True else 9 if hoorayanotherreset == True else 0
        kaorimaxpoint = 20 if resetsix4 == True else 11 if chapthreeactive == True else 8 if hoorayanotherreset == True else 3
        karinmaxpoint = 16 if resetsix4 == True else 9 if chapthreeactive == True else 7 if hoorayanotherreset == True else 3
        kirinmaxpoint = 33 if resetsix4 == True else 23 if chapthreeactive == True else 19 if hoorayanotherreset == True else 3
        makimaxpoint = 21 if resetsix4 == True else 13 if chapthreeactive == True else 7 if hoorayanotherreset == True else 2
        makotomaxpoint = 41 if resetsix4 == True else 30 if chapthreeactive == True else 22 if hoorayanotherreset == True else 16
        mayamaxpoint = 38 if resetsix4 == True else 23 if chapthreeactive == True else 20 if hoorayanotherreset == True else 12
        mikumaxpoint = 34 if resetsix4 == True else 26 if chapthreeactive == True else 21 if hoorayanotherreset == True else 13
        mollymaxpoint = 27 if resetsix4 == True else 18 if chapthreeactive == True else 14 if hoorayanotherreset == True else 6
        naomaxpoint = 11 if resetsix4 == True else 3 if chapthreeactive == True else 0 if hoorayanotherreset == True else 0
        nikimaxpoint = 20 if resetsix4 == True else 10 if chapthreeactive == True else 6 if hoorayanotherreset == True else 0
        nodokamaxpoint = 28 if resetsix4 == True else 14 if chapthreeactive == True else 5 if hoorayanotherreset == True else 0
        norikomaxpoint = 24 if resetsix4 == True else 15 if chapthreeactive == True else 11 if hoorayanotherreset == True else 0
        osakomaxpoint = 13 if resetsix4 == True else 4 if chapthreeactive == True else 2 if hoorayanotherreset == True else 0
        otohamaxpoint = 21 if resetsix4 == True else 12 if chapthreeactive == True else 9 if hoorayanotherreset == True else 0
        rikamaxpoint = 11 if resetsix4 == True else 3 if chapthreeactive == True else 0 if hoorayanotherreset == True else 0
        rinmaxpoint = 37 if resetsix4 == True else 27 if chapthreeactive == True else 24 if hoorayanotherreset == True else 16
        sanamaxpoint = 35 if resetsix4 == True else 26 if chapthreeactive == True else 22 if hoorayanotherreset == True else 14
        saramaxpoint = 23 if resetsix4 == True else 13 if chapthreeactive == True else 10 if hoorayanotherreset == True else 5
        toukamaxpoint = 23 if resetsix4 == True else 13 if chapthreeactive == True else 9 if hoorayanotherreset == True else 0
        tsubasamaxpoint = 14 if resetsix4 == True else 5 if chapthreeactive == True else 2 if hoorayanotherreset == True else 0
        tsukasamaxpoint = 12 if resetsix4 == True else 2 if chapthreeactive == True else 0 if hoorayanotherreset == True else 0
        tsuneyomaxpoint = 28 if resetsix4 == True else 17 if chapthreeactive == True else 14 if hoorayanotherreset == True else 6
        utamaxpoint = 27 if resetsix4 == True else 17 if chapthreeactive == True else 9 if hoorayanotherreset == True else 0
        wakanamaxpoint = 15 if resetsix4 == True else 7 if chapthreeactive == True else 2 if hoorayanotherreset == True else 0
        yasumaxpoint = 24 if resetsix4 == True else 13 if chapthreeactive == True else 5 if hoorayanotherreset == True else 0
        yukimaxpoint = 16 if resetsix4 == True else 7 if chapthreeactive == True else 4 if hoorayanotherreset == True else 0
        yumimaxpoint = 34 if resetsix4 == True else 23 if chapthreeactive == True else 20 if hoorayanotherreset == True else 12

        rows_number = 11 + (day244 == True) + (day140 == True) + (day144 == True) + (day239 == True) + (day280 == True) + (day282 == True) + \
            (day297 == True) + (day303 == True) + (day269 == True) + (soccer20 == True) + (bar10 == True) + (cafe10 == True) + \
            (amisroom5 == True and day65 == True) + (chikadorm15 == True) + (soccer20 == True) + (pornshop15 == True) + (streets25 == True) + \
            (day271 == True) + (day237 == True) + (utamaid5 == True) + (day295 == True) + (day295 == True) + (christmastwo1 == True) + \
            (rindorm55p2 == True) + (treasureisland == True)      # total = 36

    use game_menu(_("Progress"), scroll="viewport"):

        style_prefix "profile"

        vbox:
            if ami_love >= 0:
                if resetsix4 == True:
                    if chap1point + chap2point + chap3point + chap3miss + chap4point + chap4miss != 421:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 20:
                        text "Secret Events Available!"  style "affgrid"
                elif chapthreeactive == True:
                    if chap1point + chap2point + chap3point + chap3miss != 304:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 17:
                        text "Secret Events Available!"  style "affgrid"
                elif hoorayanotherreset == True and chapthreeactive == False:
                    if chap1point + chap2point != 203:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 14:
                        text "Secret Events Available!"  style "affgrid"
                else:
                    text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss < 11:
                        text "Secret Events Available!"  style "affgrid"

                text "\n"

                grid 4 rows_number:
                    xspacing 90
                    yspacing 20

                    text "{u}Name{/u}" style "affgrid"
                    text "{u}Affection{/u}" style "affgrid"
                    text "{u}Lust{/u}" style "affgrid"
                    text "{u}Events{/u}" style "affgrid"

                    text "{color=#ff4dd2}Ami Arakawa{/color}" style "affgrid"
                    text "{color=#ff4dd2}[ami_love]{/color}" style "affgrid"
                    text "{color=#ff4dd2}[ami_lust]{/color}" style "affgrid"
                    if amitotal == amimaxpoint:
                        text "{color=#ff4dd2}[amitotal]/[amimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#ff4dd2}[amitotal]/[amimaxpoint]{/color}" style "affgrid"

                    text "{color=#00bab1}Ayane Amamiya{/color}" style "affgrid"
                    text "{color=#00bab1}[ayane_love]{/color}" style "affgrid"
                    text "{color=#00bab1}[ayane_lust]{/color}" style "affgrid"
                    if ayanetotal == ayanemaxpoint:
                        text "{color=#00bab1}[ayanetotal]/[ayanemaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#00bab1}[ayanetotal]/[ayanemaxpoint]{/color}" style "affgrid"

                    text "{color=#AF7F00}Chika Chosokabe{/color}" style "affgrid"
                    text "{color=#AF7F00}[chika_love]{/color}" style "affgrid"
                    text "{color=#AF7F00}[chika_lust]{/color}" style "affgrid"
                    if chikatotal == chikamaxpoint:
                        text "{color=#AF7F00}[chikatotal]/[chikamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#AF7F00}[chikatotal]/[chikamaxpoint]{/color}" style "affgrid"

                    if chikadorm15 == True:
                        text "{color=#FF9999}Chinami Chosokabe{/color}" style "affgrid"
                        text "{color=#FF9999}[chinami_love]{/color}" style "affgrid"
                        text "{color=#FF9999}N/A{/color}" style "affgrid"
                        if chinamitotal == chinamimaxpoint:
                            text "{color=#FF9999}[chinamitotal]/[chinamimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#FF9999}[chinamitotal]/[chinamimaxpoint]{/color}" style "affgrid"

                    text "{color=#9326ff}Futaba Fukuyama{/color}" style "affgrid"
                    text "{color=#9326ff}[futaba_love]{/color}" style "affgrid"
                    text "{color=#9326ff}[futaba_lust]{/color}" style "affgrid"
                    if futabatotal == futabamaxpoint:
                        text "{color=#9326ff}[futabatotal]/[futabamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#9326ff}[futabatotal]/[futabamaxpoint]{/color}" style "affgrid"

                    if cafe10 == True:
                        text "{color=#B02E8C}Haruka Hamasaki{/color}" style "affgrid"
                        text "{color=#B02E8C}[haruka_love]{/color}" style "affgrid"
                        text "{color=#B02E8C}[haruka_lust]{/color}" style "affgrid"
                        if harukatotal == harukamaxpoint:
                            text "{color=#B02E8C}[harukatotal]/[harukamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#B02E8C}[harukatotal]/[harukamaxpoint]{/color}" style "affgrid"

                    if christmastwo1 == True:
                        text "{color=#80C9DC}Imani Imai{/color}" style "affgrid"
                        text "{color=#80C9DC}[imani_love]{/color}" style "affgrid"
                        text "{color=#80C9DC}[imani_lust]{/color}" style "affgrid"
                        if imanitotal == imanimaxpoint:
                            text "{color=#80C9DC}[imanitotal]/[imanimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#80C9DC}[imanitotal]/[imanimaxpoint]{/color}" style "affgrid"

                    if day244 == True:
                        text "{color=#BBE3A1}Io Ichimonji{/color}" style "affgrid"
                        text "{color=#BBE3A1}[io_love]{/color}" style "affgrid"
                        text "{color=#BBE3A1}N/A{/color}" style "affgrid"
                        if iototal == iomaxpoint:
                            text "{color=#BBE3A1}[iototal]/[iomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#BBE3A1}[iototal]/[iomaxpoint]{/color}" style "affgrid"

                    if amisroom5 == True and day65 == True:
                        text "{color=#4B4B4B}Kaori Kadowaki{/color}" style "affgrid"
                        text "{color=#4B4B4B}[kaori_love]{/color}" style "affgrid"
                        text "{color=#4B4B4B}[kaori_lust]{/color}" style "affgrid"
                        if kaoritotal == kaorimaxpoint:
                            text "{color=#4B4B4B}[kaoritotal]/[kaorimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#4B4B4B}[kaoritotal]/[kaorimaxpoint]{/color}" style "affgrid"

                    if soccer20 == True:
                        text "{color=#AC9D77}Karin Kanda{/color}" style "affgrid"
                        text "{color=#AC9D77}[karin_love]{/color}" style "affgrid"
                        text "{color=#AC9D77}N/A{/color}" style "affgrid"
                        if karintotal == karinmaxpoint:
                            text "{color=#AC9D77}[karintotal]/[karinmaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#AC9D77}[karintotal]/[karinmaxpoint]{/color}" style "affgrid"

                    if soccer20 == True:
                        text "{color=#9C8080}Kirin Kanda{/color}" style "affgrid"
                        text "{color=#9C8080}[kirin_love]{/color}" style "affgrid"
                        text "{color=#9C8080}[kirin_lust]{/color}" style "affgrid"
                        if kirintotal == kirinmaxpoint:
                            text "{color=#9C8080}[kirintotal]/[kirinmaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#9C8080}[kirintotal]/[kirinmaxpoint]{/color}" style "affgrid"

                    if pornshop15 == True:
                        text "{color=#3B84A9}Maki Miyamura{/color}" style "affgrid"
                        text "{color=#3B84A9}[maki_love]{/color}" style "affgrid"
                        text "{color=#3B84A9}[maki_lust]{/color}" style "affgrid"
                        if makitotal == makimaxpoint:
                            text "{color=#3B84A9}[makitotal]/[makimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#3B84A9}[makitotal]/[makimaxpoint]{/color}" style "affgrid"

                    text "{color=#3c55fa}Makoto Miyamura{/color}" style "affgrid"
                    text "{color=#3c55fa}[makoto_love]{/color}" style "affgrid"
                    text "{color=#3c55fa}[makoto_lust]{/color}" style "affgrid"
                    if makotototal == makotomaxpoint:
                        text "{color=#3c55fa}[makotototal]/[makotomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#3c55fa}[makotototal]/[makotomaxpoint]{/color}" style "affgrid"

                    text "{color=#18b500}Maya Makinami{/color}" style "affgrid"
                    text "{color=#18b500}[maya_love]{/color}" style "affgrid"
                    text "{color=#18b500}[maya_lust]{/color}" style "affgrid"
                    if mayatotal == mayamaxpoint:
                        text "{color=#18b500}[mayatotal]/[mayamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#18b500}[mayatotal]/[mayamaxpoint]{/color}" style "affgrid"

                    text "{color=#ff8112}Miku Maruyama{/color}" style "affgrid"
                    text "{color=#ff8112}[miku_love]{/color}" style "affgrid"
                    text "{color=#ff8112}[miku_lust]{/color}" style "affgrid"
                    if mikutotal == mikumaxpoint:
                        text "{color=#ff8112}[mikutotal]/[mikumaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#ff8112}[mikutotal]/[mikumaxpoint]{/color}" style "affgrid"

                    if day140 == True:
                        text "{color=#4FCB80}Molly MacCormack{/color}" style "affgrid"
                        text "{color=#4FCB80}[molly_love]{/color}" style "affgrid"
                        text "{color=#4FCB80}[molly_lust]{/color}" style "affgrid"
                        if mollytotal == mollymaxpoint:
                            text "{color=#4FCB80}[mollytotal]/[mollymaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#4FCB80}[mollytotal]/[mollymaxpoint]{/color}" style "affgrid"

                    if treasureisland == True:
                        text "{color=#602F2B}Nao-chan{/color}" style "affgrid"
                        text "{color=#602F2B}[nao_love]{/color}" style "affgrid"
                        text "{color=#602F2B}N/A{/color}" style "affgrid"
                        if naototal == naomaxpoint:
                            text "{color=#602F2B}[naototal]/[naomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#602F2B}[naototal]/[naomaxpoint]{/color}" style "affgrid"

                    if day271 == True:
                        text "{color=#FF0074}Niki Nakayama{/color}" style "affgrid"
                        text "{color=#FF0074}[niki_love]{/color}" style "affgrid"
                        text "{color=#FF0074}[niki_lust]{/color}" style "affgrid"
                        if nikitotal == nikimaxpoint:
                            text "{color=#FF0074}[nikitotal]/[nikimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#FF0074}[nikitotal]/[nikimaxpoint]{/color}" style "affgrid"

                    if day280 == True:
                        text "{color=#AF89A2}Nodoka Nagasawa{/color}" style "affgrid"
                        text "{color=#AF89A2}[nodoka_love]{/color}" style "affgrid"
                        text "{color=#AF89A2}[nodoka_lust]{/color}" style "affgrid"
                        if nodokatotal == nodokamaxpoint:
                            text "{color=#AF89A2}[nodokatotal]/[nodokamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#AF89A2}[nodokatotal]/[nodokamaxpoint]{/color}" style "affgrid"

                    if day269 == True:
                        text "{color=#FF61A9}Noriko Nakayama{/color}" style "affgrid"
                        text "{color=#FF61A9}[noriko_love]{/color}" style "affgrid"
                        text "{color=#FF61A9}[noriko_lust]{/color}" style "affgrid"
                        if norikototal == norikomaxpoint:
                            text "{color=#FF61A9}[norikototal]/[norikomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#FF61A9}[norikototal]/[norikomaxpoint]{/color}" style "affgrid"

                    if utamaid5 == True:
                        text "{color=#9A6BA1}Osako Osaka{/color}" style "affgrid"
                        text "{color=#9A6BA1}[osako_love]{/color}" style "affgrid"
                        text "{color=#9A6BA1}N/A{/color}" style "affgrid"
                        if osakototal == osakomaxpoint:
                            text "{color=#9A6BA1}[osakototal]/[osakomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#9A6BA1}[osakototal]/[osakomaxpoint]{/color}" style "affgrid"

                    if day282 == True:
                        text "{color=#B83A6A}Otoha Okakura{/color}" style "affgrid"
                        text "{color=#B83A6A}[otoha_love]{/color}" style "affgrid"
                        text "{color=#B83A6A}N/A{/color}" style "affgrid"
                        if otohatotal == otohamaxpoint:
                            text "{color=#B83A6A}[otohatotal]/[otohamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#B83A6A}[otohatotal]/[otohamaxpoint]{/color}" style "affgrid"

                    if rindorm55p2 == True:
                        text "{color=#D18E77}Rika Rokuhara{/color}" style "affgrid"
                        text "{color=#D18E77}[rika_love]{/color}" style "affgrid"
                        text "{color=#D18E77}[rika_lust]{/color}" style "affgrid"
                        if rikatotal == rikamaxpoint:
                            text "{color=#D18E77}[rikatotal]/[rikamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#D18E77}[rikatotal]/[rikamaxpoint]{/color}" style "affgrid"

                    text "{color=#a30041}Rin Rokuhara{/color}" style "affgrid"
                    text "{color=#a30041}[rin_love]{/color}" style "affgrid"
                    text "{color=#a30041}N/A{/color}" style "affgrid"
                    if rintotal == rinmaxpoint:
                        text "{color=#a30041}[rintotal]/[rinmaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#a30041}[rintotal]/[rinmaxpoint]{/color}" style "affgrid"

                    text "{color=#005730}Sana Sakakibara{/color}" style "affgrid"
                    text "{color=#005730}[sana_love]{/color}" style "affgrid"
                    text "{color=#005730}[sana_lust]{/color}" style "affgrid"
                    if sanatotal == sanamaxpoint:
                        text "{color=#005730}[sanatotal]/[sanamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#005730}[sanatotal]/[sanamaxpoint]{/color}" style "affgrid"

                    if bar10 == True:
                        text "{color=#365D4C}Sara Sakakibara{/color}" style "affgrid"
                        text "{color=#365D4C}[sara_love]{/color}" style "affgrid"
                        text "{color=#365D4C}[sara_lust]{/color}" style "affgrid"
                        if saratotal == saramaxpoint:
                            text "{color=#365D4C}[saratotal]/[saramaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#365D4C}[saratotal]/[saramaxpoint]{/color}" style "affgrid"

                    if day297 == True:
                        text "{color=#F0E68C}Touka Tsukioka{/color}" style "affgrid"
                        text "{color=#F0E68C}[touka_love]{/color}" style "affgrid"
                        text "{color=#F0E68C}[touka_lust]{/color}" style "affgrid"
                        if toukatotal == toukamaxpoint:
                            text "{color=#F0E68C}[toukatotal]/[toukamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#F0E68C}[toukatotal]/[toukamaxpoint]{/color}" style "affgrid"

                    if day295 == True:
                        text "{color=#eae6aa}Tsubasa Tsukioka{/color}" style "affgrid"
                        text "{color=#eae6aa}[tsubasa_love]{/color}" style "affgrid"
                        text "{color=#eae6aa}N/A{/color}" style "affgrid"
                        if tsubasatotal == tsubasamaxpoint:
                            text "{color=#eae6aa}[tsubasatotal]/[tsubasamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#eae6aa}[tsubasatotal]/[tsubasamaxpoint]{/color}" style "affgrid"

                    if day295 == True:
                        text "{color=#f0ca8c}Tsukasa Tsukioka{/color}" style "affgrid"
                        text "{color=#f0ca8c}[tsukasa_love]{/color}" style "affgrid"
                        text "{color=#f0ca8c}[tsukasa_lust]{/color}" style "affgrid"
                        if tsukasatotal == tsukasamaxpoint:
                            text "{color=#f0ca8c}[tsukasatotal]/[tsukasamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#f0ca8c}[tsukasatotal]/[tsukasamaxpoint]{/color}" style "affgrid"

                    if day144 == True:
                        text "{color=#C8B330}Tsuneyo Tojo{/color}" style "affgrid"
                        text "{color=#C8B330}[tsuneyo_love]{/color}" style "affgrid"
                        text "{color=#C8B330}[tsuneyo_lust]{/color}" style "affgrid"
                        if tsuneyototal == tsuneyomaxpoint:
                            text "{color=#C8B330}[tsuneyototal]/[tsuneyomaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#C8B330}[tsuneyototal]/[tsuneyomaxpoint]{/color}" style "affgrid"

                    if day239 == True:
                        text "{color=#AA4588}Uta Ushibori{/color}" style "affgrid"
                        text "{color=#AA4588}[uta_love]{/color}" style "affgrid"
                        text "{color=#AA4588}N/A{/color}" style "affgrid"
                        if utatotal == utamaxpoint:
                            text "{color=#AA4588}[utatotal]/[utamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#AA4588}[utatotal]/[utamaxpoint]{/color}" style "affgrid"

                    if day237 == True:
                        text "{color=#540087}Wakana Watabe{/color}" style "affgrid"
                        text "{color=#540087}[wakana_love]{/color}" style "affgrid"
                        text "{color=#540087}N/A{/color}" style "affgrid"
                        if wakanatotal == wakanamaxpoint:
                            text "{color=#540087}[wakanatotal]/[wakanamaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#540087}[wakanatotal]/[wakanamaxpoint]{/color}" style "affgrid"

                    if day303 == True:
                        text "{color=#74d9e9}Yasu Yasui{/color}" style "affgrid"
                        text "{color=#74d9e9}[yasu_love]{/color}" style "affgrid"
                        text "{color=#74d9e9}[yasu_lust]{/color}" style "affgrid"
                        if yasutotal == yasumaxpoint:
                            text "{color=#74d9e9}[yasutotal]/[yasumaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#74d9e9}[yasutotal]/[yasumaxpoint]{/color}" style "affgrid"

                    if streets25 == True:
                        text "{color=#CDCDCD}Yuki Yamaguchi{/color}" style "affgrid"
                        text "{color=#CDCDCD}[yuki_love]{/color}" style "affgrid"
                        text "{color=#CDCDCD}N/A{/color}" style "affgrid"
                        if yukitotal == yukimaxpoint:
                            text "{color=#CDCDCD}[yukitotal]/[yukimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                        else:
                            text "{color=#CDCDCD}[yukitotal]/[yukimaxpoint]{/color}" style "affgrid"

                    text "{color=#d12e2e}Yumi Yamaguchi{/color}" style "affgrid"
                    text "{color=#d12e2e}[yumi_love]{/color}" style "affgrid"
                    text "{color=#d12e2e}N/A{/color}" style "affgrid"
                    if yumitotal == yumimaxpoint:
                        text "{color=#d12e2e}[yumitotal]/[yumimaxpoint] {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#d12e2e}[yumitotal]/[yumimaxpoint]{/color}" style "affgrid"
                        
                        
screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            # AVN Mod
                vbox:   
                    style_prefix "radio"
                    label _("AUTO Mod")
                    textbutton _("Off: Normal game") action SetVariable("avnmode", False)
                    textbutton _("On: Auto start event") action SetVariable("avnmode", True)
            # AVN Mod

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            

screen secrettracker_avn():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("HAPPY SCENES"), scroll="viewport"):

        style_prefix "event"

        vbox:
            label "\n{color=141414}HAPPY SCENES{/color}"
            if roomwithtrack == True:
                textbutton _("The Room With Clocks {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("roomwithclocks", locked=False)
            else:
                text _("???")
            if letterttrack == True:
                textbutton _("The Letter 'T' {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("lettert", locked=False)
            else:
                text _("???")
            if swimmingtrack == True:
                textbutton _("Swim Trip {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("swimming", locked=False)
            elif amidorm10 == True and amifingered == False:
                text _("{color=EF1A1A}{s}You Don't Love Me, Do You?{/s}{/color}")
            else:
                text _("???")
            if howifeeltrack == True:
                textbutton _("How I Feel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("howifeel", locked=False)
            else:
                text _("???")
            if connecttrack == True:
                textbutton _("Everything is Connected {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("everythingisconnected", locked=False)
            elif day103 == True and connecttrack == False:
                text _("{color=EF1A1A}{s}Nothing is Beautiful{/s}{/color}")
            else:
                text _("???")
            if specialclassroomtrack == True:
                textbutton _("Turn Off The Lights {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("specialclassroom", locked=False)
            elif amisroom15 == True and amifingered == False:
                text _("{color=EF1A1A}{s}List the Things You Love{/s}{/color}")
            else:
                text _("???")
            if ticktocktrack == True:
                textbutton _("Tick Tock Tick Tock Tick Tock {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ticktock", locked=False)
            else:
                text _("???")
            if trinity1track == True:
                textbutton _("Trinity Pt. I: Stations of the Cross {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity1", locked=False)
            else:
                text _("???")
            if trinity2track == True:
                textbutton _("Trinity Pt. II: Hell is Empty {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity2", locked=False)
            else:
                text _("???")
            if trinity3track == True:
                textbutton _("Trinity Pt. III: Non Est Deus {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity3", locked=False)
            else:
                text _("???")
            if babyfinches == True:
                textbutton _("Baby Finches {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("babyfinches", locked=False)
            elif babyfinches == False and hoorayanotherreset == True:
                text _("{color=EF1A1A}{s}A Time When Things Were Horrible{/s}{/color}")
            else:
                text _("???")
        # AVN Mod
            if hoorayanotherreset == True:
                if lesson1 == True:
                    textbutton _("Something Everyone Knows and Ignores {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kindergartenclass", locked=False)
                elif lesson1 == False and thirdreset1 == True:
                    text _("{color=EF1A1A}{s}LET ME OUT{/s}{/color}")
                else:
                    text _("???")
                if goodboy == True:
                    textbutton _("Good Boy {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("goodboy", locked=False)
                elif sarabar25 == True and anewkey == False and goodboy == False:
                    text _("{color=EF1A1A}{s}Bad Boy{/s}{/color}")
                else:
                    text _("???")
                if lamblegs == True:
                    textbutton _("Lamb Legs {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("specialbonusamiscene", locked=False)
                elif returntosummer2 == True and anewkey == False:
                    text _("{color=EF1A1A}{s}Ground Into Nothing{/s}{/color}")
                else:
                    text _("???")
            if chapthreeactive == True:
                if buckettrack == True:
                    textbutton _("Second Sun {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("bucketscene", locked=False)
                else:
                    text _("???")
                if mothersmilk == True:
                    textbutton _("Mother's Milk {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("mothersmilk", locked=False)
                elif mothersmiss == True:
                    text _("{color=EF1A1A}{s}Overlooked{/s}{/color}")
                else:
                    text _("???")
                if amyevent == True:
                    textbutton _("Amy {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("amyevent", locked=False)
                else:
                    text _("???")
                if rainking == True:
                    textbutton _("Rain King {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("rainking", locked=False)
                elif rainkingmiss == True:
                    text _("{color=EF1A1A}{s}Drought God{/s}{/color}")
                else:
                    text _("???")
            if resetsix4 == True:
                if armsbenttrack == True:
                    textbutton _("Arms Bent Back {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("armsbentback", locked=False)
                elif armsbentmiss == True:
                    text _("{color=EF1A1A}{s}Lost in the Red Room{/s}{/color}")
                else:
                    text _("???")
                if kyotoevent == True:
                    textbutton _("Kyoto {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("postfreddeathscene", locked=False)
                elif kyotomiss == True:
                    text _("{color=EF1A1A}{s}No One Leaves This City{/s}{/color}")
                else:
                    text _("???")
                if persistent.alexisevent == True:
                    textbutton _("Alexisthymia {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("alexisevent", locked=False)
                else:
                    text _("???")
                if swimtrip2 == True:
                    textbutton _("Sally Sells Seashells {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("swimtrip2", locked=False)
                elif swimtrip2miss == True:
                    text _("{color=EF1A1A}{s}Sally is Homeless{/s}{/color}")
                else:
                    text _("???")
            textbutton _("Back") action ShowMenu('eventtracker11')
            

screen eventtracker11 ():
    tag menu

    use game_menu(_("Event Tracker"), scroll="viewport"):

        style_prefix "aff"

        grid 1 3:
            #align (1, 0.45)
            spacing 20

        # AVN Mod
            if resetsix4 == False:
                imagebutton:
                    idle "mainview1.png"
                    hover "mainview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('eventtrackermainhub_avn')
                imagebutton:
                    idle "charaview1.png"
                    hover "charaview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('eventtrackercharahub')
                imagebutton:
                    idle "happyview1.png"
                    hover "happyview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('secrettracker_avn')
            else:
                imagebutton:
                    idle "mainview1.png"
                    hover "mainview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('eventtrackermainhub')
                imagebutton:
                    idle "charaview1.png"
                    hover "charaview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('eventtrackercharahub')
                imagebutton:
                    idle "happyview1.png"
                    hover "happyview2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('secrettracker')


screen eventtrackermainhub_avn ():
    tag menu

    use game_menu(_("Event Tracker"), scroll="viewport"):

        style_prefix "aff"

    # AVN Mod
        if resetsix4 == False:
            grid 3 1:
                #align (1, 0.45)
                spacing 90

                imagebutton:
                    idle "avn_mod/Images/chap1view1.png"
                    hover "avn_mod/Images/chap1view2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('maintracker')
                if hoorayanotherreset == False:
                    imagebutton:
                        idle "avn_mod/Images/chaphidden1.png"
                        hover "avn_mod/Images/chaphidden1.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        #action Replay("roomwithclocks", locked=False)
                else:
                    imagebutton:
                        idle "avn_mod/Images/chap2view1.png"
                        hover "avn_mod/Images/chap2view2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('maintrackerch2')
                if chapthreeactive == False:
                    imagebutton:
                        idle "avn_mod/Images/chaphidden1.png"
                        hover "avn_mod/Images/chaphidden1.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        #action Replay("roomwithclocks", locked=False)
                else:
                    imagebutton:
                        idle "avn_mod/Images/chap3view1.png"
                        hover "avn_mod/Images/chap3view2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('maintrackerch3')
        else:
            grid 3 2:
                #align (1, 0.45)
                spacing 40

                imagebutton:
                    idle "chap1idle.png"
                    hover "chap1hover.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('maintracker')
                if hoorayanotherreset == False:
                    imagebutton:
                        idle "chaplocked.png"
                        hover "chaplocked.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        #action Replay("roomwithclocks", locked=False)
                else:
                    imagebutton:
                        idle "chap2idle.png"
                        hover "chap2hover.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('maintrackerch2')
                if chapthreeactive == False:
                    imagebutton:
                        idle "chaplocked.png"
                        hover "chaplocked.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        #action Replay("roomwithclocks", locked=False)
                else:
                    imagebutton:
                        idle "chap3idle.png"
                        hover "chap3hover.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('maintrackerch3')
                if resetsix4 == False:
                    imagebutton:
                        idle "chaplocked.png"
                        hover "chaplocked.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        #action Replay("roomwithclocks", locked=False)
                else:
                    imagebutton:
                        idle "chap4idle.png"
                        hover "chap4hover.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('maintrackerch4')
                imagebutton:
                    idle "chaplocked.png"
                    hover "chaplocked.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Replay("roomwithclocks", locked=False)
                imagebutton:
                    idle "chaplocked.png"
                    hover "chaplocked.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Replay("roomwithclocks", locked=False)

        vbox:
            textbutton _("Back") action ShowMenu('eventtracker11')


screen eventtrackermaincharahub ():
    tag menu

    use game_menu(_("Main Characters"), scroll="viewport"):

        style_prefix "aff"

        grid 5 4:
            align (1, 1)
            xspacing 60
            yspacing 20

            if resetsix4 == True:
                imagebutton:
                    idle "chikathumb1.png" 
                    hover "chikathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuchika')
                imagebutton:
                    idle "yumithumb1.png"
                    hover "yumithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuyumi')
                imagebutton:
                    idle "ayanethumb1.png"
                    hover "ayanethumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuayane')
                imagebutton:
                    idle "sanathumb1.png"
                    hover "sanathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenusana')
                imagebutton:
                    idle "makotothumb1.png"
                    hover "makotothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumakoto')
                imagebutton:
                    idle "mikuthumb1.png"
                    hover "mikuthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumiku')
                imagebutton:
                    idle "futabathumb1.png"
                    hover "futabathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenufutaba')
                imagebutton:
                    idle "rinthumb1.png"
                    hover "rinthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenurin')
                imagebutton:
                    idle "amithumb1.png"
                    hover "amithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuami')
                imagebutton:
                    idle "mayathumb1.png"
                    hover "mayathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumaya')
                imagebutton:
                    idle "mollythumb1.png"
                    hover "mollythumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumolly')
                imagebutton:
                    idle "tsuneyothumb1.png"
                    hover "tsuneyothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenutsuneyo')
                imagebutton:
                    idle "utathumb1.png"
                    hover "utathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuuta')
                imagebutton:
                    idle "iothumb1.png"
                    hover "iothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuio')
                imagebutton:
                    idle "nodokathumb1.png"
                    hover "nodokathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenunodoka')
                imagebutton:
                    idle "otohathumb1.png"
                    hover "otohathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuotoha')
                imagebutton:
                    idle "toukathumb1.png"
                    hover "toukathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenutouka')
                imagebutton:
                    idle "yasuthumb1.png"
                    hover "yasuthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuyasu')
                imagebutton:
                    idle "norikothumb1.png"
                    hover "norikothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenunoriko')
                imagebutton:
                    idle "kirinthumb1.png"
                    hover "kirinthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenukirin')

        # AVN Mod
            else:
                imagebutton:
                    idle "avn_mod/Images/chikathumb1_37.png" 
                    hover "avn_mod/Images/chikathumb2_37.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuchika')
                imagebutton:
                    idle "avn_mod/Images/yumithumb1_37.png"
                    hover "avn_mod/Images/yumithumb2_37.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuyumi')
                imagebutton:
                    idle "ayanethumb1.png"
                    hover "ayanethumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuayane')
                imagebutton:
                    idle "sanathumb1.png"
                    hover "sanathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenusana')
                imagebutton:
                    idle "makotothumb1.png"
                    hover "makotothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumakoto')
                imagebutton:
                    idle "mikuthumb1.png"
                    hover "mikuthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumiku')
                imagebutton:
                    idle "avn_mod/Images/futabathumb1_37.png"
                    hover "avn_mod/Images/futabathumb2_37.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenufutaba')
                imagebutton:
                    idle "rinthumb1.png"
                    hover "rinthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenurin')
                imagebutton:
                    idle "amithumb1.png"
                    hover "amithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuami')
                imagebutton:
                    idle "avn_mod/Images/mayathumb1_37.png"
                    hover "avn_mod/Images/mayathumb2_37.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumaya')
                if day140 == True:
                    imagebutton:
                        idle "mollythumb1.png"
                        hover "mollythumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenumolly')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day144 == True:
                    imagebutton:
                        idle "tsuneyothumb1.png"
                        hover "tsuneyothumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenutsuneyo')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day239 == True:
                    imagebutton:
                        idle "avn_mod/Images/utathumb1_37.png"
                        hover "avn_mod/Images/utathumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuuta')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day244 == True:
                    imagebutton:
                        idle "avn_mod/Images/iothumb1_37.png"
                        hover "avn_mod/Images/iothumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuio')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day280 == True:
                    imagebutton:
                        idle "nodokathumb1.png"
                        hover "nodokathumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenunodoka')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day282 == True:
                    imagebutton:
                        idle "avn_mod/Images/otohathumb1_37.png"
                        hover "avn_mod/Images/otohathumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuotoha')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day297 == True:
                    imagebutton:
                        idle "toukathumb1.png"
                        hover "toukathumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenutouka')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day303 == True:
                    imagebutton:
                        idle "yasuthumb1.png"
                        hover "yasuthumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuyasu')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day269 == True:
                    imagebutton:
                        idle "norikothumb1.png"
                        hover "norikothumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenunoriko')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if soccer20 == True:
                    imagebutton:
                        idle "kirinthumb1.png"
                        hover "kirinthumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenukirin')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
        # AVN Mod


screen eventtrackersidecharahub ():
    tag menu

    use game_menu(_("Side Characters"), scroll="viewport"):

        style_prefix "aff"

        grid 5 3:
            align (1, 1)
            xspacing 60
            yspacing 20

            if resetsix4 == True:
                imagebutton:
                    idle "sarathumb1.png"
                    hover "sarathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenusara')
                imagebutton:
                    idle "harukathumb1.png"
                    hover "harukathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuharuka')
                imagebutton:
                    idle "kaorithumb1.png"
                    hover "kaorithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenukaori')
                imagebutton:
                    idle "chinamithumb1.png"
                    hover "chinamithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuchinami')
                imagebutton:
                    idle "karinthumb1.png"
                    hover "karinthumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenukarin')
                imagebutton:
                    idle "makithumb1.png"
                    hover "makithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenumaki')
                imagebutton:
                    idle "yukithumb1.png"
                    hover "yukithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuyuki')
                imagebutton:
                    idle "nikithumb1.png"
                    hover "nikithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuniki')
                imagebutton:
                    idle "wakanathumb1.png"
                    hover "wakanathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuwakana')
                imagebutton:
                    idle "osakothumb1.png"
                    hover "osakothumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuosako')
                imagebutton:
                    idle "tsubasathumb1.png"
                    hover "tsubasathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenutsubasa')
                imagebutton:
                    idle "tsukasathumb1.png"
                    hover "tsukasathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenutsukasa')
                imagebutton:
                    idle "imanithumb1.png"
                    hover "imanithumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenuimani')
                imagebutton:
                    idle "rikathumb1.png"
                    hover "rikathumb2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenurika')
                imagebutton:
                    idle "naothumb1.png"
                    hover "naothumb2.png"
                    xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('gamemenunao')

        # AVN Mod
            else:
                if bar10 == True:
                    imagebutton:
                        idle "avn_mod/Images/sarathumb1_37.png"
                        hover "avn_mod/Images/sarathumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenusara')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if cafe10 == True:
                    imagebutton:
                        idle "avn_mod/Images/harukathumb1_37.png"
                        hover "avn_mod/Images/harukathumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuharuka')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if amisroom5 == True and day65 == True:
                    imagebutton:
                        idle "avn_mod/Images/kaorithumb1_37.png"
                        hover "avn_mod/Images/kaorithumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenukaori')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if chikadorm15 == True:
                    imagebutton:
                        idle "avn_mod/Images/chinamithumb1_37.png"
                        hover "avn_mod/Images/chinamithumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuchinami')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if soccer20 == True:
                    imagebutton:
                        idle "avn_mod/Images/karinthumb1_37.png"
                        hover "avn_mod/Images/karinthumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenukarin')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if pornshop15 == True:
                    imagebutton:
                        idle "avn_mod/Images/makithumb1_37.png"
                        hover "avn_mod/Images/makithumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenumaki')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if streets25 == True:
                    imagebutton:
                        idle "avn_mod/Images/yukithumb1_37.png"
                        hover "avn_mod/Images/yukithumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuyuki')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day271 == True:
                    imagebutton:
                        idle "avn_mod/Images/nikithumb1_37.png"
                        hover "avn_mod/Images/nikithumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuniki')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day237 == True:
                    imagebutton:
                        idle "avn_mod/Images/wakanathumb1_37.png"
                        hover "avn_mod/Images/wakanathumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuwakana')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if utamaid5 == True:
                    imagebutton:
                        idle "avn_mod/Images/osakothumb1_37.png"
                        hover "avn_mod/Images/osakothumb2_37.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuosako')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day295 == True:
                    imagebutton:
                        idle "tsubasathumb1.png"
                        hover "tsubasathumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenutsubasa')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if day295 == True:
                    imagebutton:
                        idle "tsukasathumb1.png"
                        hover "tsukasathumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenutsukasa')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if christmastwo1 == True:
                    imagebutton:
                        idle "imanithumb1.png"
                        hover "imanithumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenuimani')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if rindorm55p2 == True:
                    imagebutton:
                        idle "rikathumb1.png"
                        hover "rikathumb2.png"
                        #xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenurika')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
                if treasureisland == True:
                    imagebutton:
                        idle "naothumb1.png"
                        hover "naothumb2.png"
                        xalign 0.2 yalign 0.5
                        focus_mask True
                        action ShowMenu('gamemenunao')
                else:
                    imagebutton:
                        idle "avn_mod/Images/hidenthumb.png"
        # AVN Mod
