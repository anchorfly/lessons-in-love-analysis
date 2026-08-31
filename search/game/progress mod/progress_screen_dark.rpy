################################################################################
## Progress Mod v0.60.0 2026-08-15
################################################################################

# Add at line 379 of screens.rpy:

# adds "Progress" button to menu sidebar
#
#        textbutton _("Progress") action ShowMenu("progressmod")
#

################################################################################
## Progress Screen
################################################################################

init python:
    def save_playtime(d):
        d["playtime"] = renpy.get_game_runtime()
    config.save_json_callbacks = [save_playtime]

screen progressmod_dark ():

    tag menu

    key "p" action Return()

    $ v11check()                                                        # refreshes the number of each girl's points (method written by Selebus)
    $ update_chapter_values()                                           # updates the count of how many events each girl has in each chapter
    $ ProgressMod.update_all()                                          # updates the hints for all events
    $ activate_girls()                                                  # determines which girls are to be shown (depends on player progress)

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    $ y_col = .15 - ((count_girls_shown() - 10) * .0032)                # determines y position for columns
    $ main_col = .19 - ((count_girls_shown() - 10) * .0032)             # determines y position for side column with main event information
    $ op_col = .19 - ((count_girls_shown() - 10) * .0032)               # determines y position for options button

    use game_menu(_("Progress"), scroll="viewport"):

        style_prefix "aff"

    vbox:
        xpos .25
        ypos main_col

        text ("{color=#FFFFFF}Chap. [current_chapter]{/color}") style "mod"
        text ("{color=#FFFFFF}Day [totaldays]{/color}") style "mod"
        text ("") style "mod"

        textbutton _("{color=#FFFFFF}Main:{/color}") action ShowMenu("maintrackerch" + str(current_chapter) + "m") style "event_button" text_style "mod"
        text ("{color=#FFFFFF}[MainEvent.points]/[MainEvent.current_max]{/color}") style "mod"
        text ("") style "mod"

        textbutton _("{color=#FFFFFF}Happy:{/color}") action ShowMenu("secrettrackerm") style "event_button" text_style "mod"
        if happymiss < 1:
            text ("{color=#FFFFFF}[HappyEvent.points]/[HappyEvent.current_max]{/color}") style "mod"
        else:
            text ("{color=#FFFFFF}[HappyEvent.points]/[HappyEvent.current_max]{/color} {color=#FF0000}([happymiss]){/color}") style "mod"
        text ("") style "mod"

        text ("{color=#FFFFFF}Playtime{/color}") style "mod"
        $ pt_minutes, pt_seconds = divmod(int(renpy.get_game_runtime()), 60)
        $ pt_hours, pt_minutes = divmod(pt_minutes, 60)
        $ pt_minutes = str(pt_minutes)
        $ if len(pt_minutes) == 1: pt_minutes = "0" + pt_minutes
        text "{color=#FFFFFF}[pt_hours]:[pt_minutes]{/color}" style "mod"

        $ pt_hours = renpy.get_game_runtime()

    vbox:
        xpos .25
        ypos 990

        if show_hints:
            textbutton _("Hints") action ShowMenu("hinttracker")

# Column showing ! indicator for available events/hints

    vbox:
        xpos .33
        ypos y_col
        style_prefix "exclam"

        text ("")

        if amipoint + amimiss != Ami.current_max and Ami.active:
            if Ami.has_hint and show_hints:
                text ("!") style "amimod"
            else:
                text ("") style "amimod"
        elif Ami.active:
                text ("") style "amimod"
        if ayanepoint + ayanemiss != Ayane.current_max and Ayane.active:
            if Ayane.has_hint and show_hints:
                text ("!") style "ayanemod"
            else:
                text ("") style "ayanemod"
        elif Ayane.active:
                text ("") style "ayanemod"
        if chikapoint + chikamiss != Chika.current_max and Chika.active:
            if Chika.has_hint and show_hints:
                text ("!") style "chikamod"
            else:
                text ("") style "chikamod"
        elif Chika.active:
                text ("") style "chikamod"
        if chinamipoint + chinamimiss != Chinami.current_max and Chinami.active:
            if Chinami.has_hint and show_hints:
                text ("!") style "chinamimod"
            else:
                text ("") style "chinamimod"
        elif Chinami.active:
                text ("") style "chinamimod"
        if futabapoint + futabamiss != Futaba.current_max and Futaba.active:
            if Futaba.has_hint and show_hints:
                text ("!") style "futabamod"
            else:
                text ("") style "futabamod"
        elif Futaba.active:
                text ("") style "futabamod"
        if harukapoint + harukamiss != Haruka.current_max and Haruka.active:
            if Haruka.has_hint and show_hints:
                text ("!") style "harukamod"
            else:
                text ("") style "harukamod"
        elif Haruka.active:
                text ("") style "harukamod"
        if imanipoint + imanimiss != Imani.current_max and Imani.active:
            if Imani.has_hint and show_hints:
                text ("!") style "imanimod"
            else:
                text ("") style "imanimod"
        elif Imani.active:
                text ("") style "imanimod"
        if iopoint + iomiss != Io.current_max and Io.active:
            if Io.has_hint and show_hints:
                text ("!") style "iomod_dark"
            else:
                text ("") style "iomod_dark"
        elif Io.active:
                text ("") style "iomod_dark"
        if kaoripoint + kaorimiss != Kaori.current_max and Kaori.active:
            if Kaori.has_hint and show_hints:
                text ("!") style "kaorimod"
            else:
                text ("") style "kaorimod"
        elif Kaori.active:
                text ("") style "kaorimod"
        if karinpoint + karinmiss != Karin.current_max and Karin.active:
            if Karin.has_hint and show_hints:
                text ("!") style "karinmod"
            else:
                text ("") style "karinmod"
        elif Karin.active:
                text ("") style "karinmod"
        if kirinpoint + kirinmiss != Kirin.current_max and Kirin.active:
            if Kirin.has_hint and show_hints:
                text ("!") style "kirinmod"
            else:
                text ("") style "kirinmod"
        elif Kirin.active:
                text ("") style "kirinmod"
        if makipoint + makimiss != Maki.current_max and Maki.active:
            if Maki.has_hint and show_hints:
                text ("!") style "makimod"
            else:
                text ("") style "makimod"
        elif Maki.active:
                text ("") style "makimod"
        if makotopoint + makotomiss != Makoto.current_max and Makoto.active:
            if Makoto.has_hint and show_hints:
                text ("!") style "makotomod"
            else:
                text ("") style "makotomod"
        elif Makoto.active:
                text ("") style "makotomod"
        if mayapoint + mayamiss != Maya.current_max and Maya.active:
            if Maya.has_hint and show_hints:
                text ("!") style "mayamod"
            else:
                text ("") style "mayamod"
        elif Maya.active:
                text ("") style "mayamod"
        if mikupoint + mikumiss != Miku.current_max and Miku.active:
            if Miku.has_hint and show_hints:
                text ("!") style "mikumod"
            else:
                text ("") style "mikumod"
        elif Miku.active:
                text ("") style "mikumod"
        if mollypoint + mollymiss != Molly.current_max and Molly.active:
            if Molly.has_hint and show_hints:
                text ("!") style "mollymod"
            else:
                text ("") style "mollymod"
        elif Molly.active:
                text ("") style "mollymod"
        if naopoint + naomiss != Nao.current_max and Nao.active:
            if Nao.has_hint and show_hints:
                text ("!") style "naomod"
            else:
                text ("") style "naomod"
        elif Nao.active:
                text ("") style "naomod"
        if nikipoint + nikimiss != Niki.current_max and Niki.active:
            if Niki.has_hint and show_hints:
                text ("!") style "nikimod"
            else:
                text ("") style "nikimod"
        elif Niki.active:
                text ("") style "nikimod"
        if nodokapoint + nodokamiss != Nodoka.current_max and Nodoka.active:
            if Nodoka.has_hint and show_hints:
                text ("!") style "nodokamod"
            else:
                text ("") style "nodokamod"
        elif Nodoka.active:
                text ("") style "nodokamod"
        if norikopoint + norikomiss != Noriko.current_max and Noriko.active:
            if Noriko.has_hint and show_hints:
                text ("!") style "norikomod"
            else:
                text ("") style "norikomod"
        elif Noriko.active:
                text ("") style "norikomod"
        if osakopoint + osakomiss != Osako.current_max and Osako.active:
            if Osako.has_hint and show_hints:
                text ("!") style "osakomod"
            else:
                text ("") style "osakomod"
        elif Osako.active:
                text ("") style "osakomod"
        if otohapoint + otohamiss != Otoha.current_max and Otoha.active:
            if Otoha.has_hint and show_hints:
                text ("!") style "otohamod"
            else:
                text ("") style "otohamod"
        elif Otoha.active:
                text ("") style "otohamod"
        if rikapoint + rikamiss != Rika.current_max and Rika.active:
            if Rika.has_hint and show_hints:
                text ("!") style "rikamod"
            else:
                text ("") style "rikamod"
        elif Rika.active:
                text ("") style "rikamod"
        if rinpoint + rinmiss != Rin.current_max and Rin.active:
            if Rin.has_hint and show_hints:
                text ("!") style "rinmod"
            else:
                text ("") style "rinmod"
        elif Rin.active:
                text ("") style "rinmod"
        if sanapoint + sanamiss != Sana.current_max and Sana.active:
            if Sana.has_hint and show_hints:
                text ("!") style "sanamod"
            else:
                text ("") style "sanamod"
        elif Sana.active:
                text ("") style "sanamod"
        if sarapoint + saramiss != Sara.current_max and Sara.active:
            if Sara.has_hint and show_hints:
                text ("!") style "saramod"
            else:
                text ("") style "saramod"
        elif Sara.active:
                text ("") style "saramod"
        if toukapoint + toukamiss != Touka.current_max and Touka.active:
            if Touka.has_hint and show_hints:
                text ("!") style "toukamod_dark"
            else:
                text ("") style "toukamod_dark"
        elif Touka.active:
                text ("") style "toukamod_dark"
        if tsubasapoint + tsubasamiss != Tsubasa.current_max and Tsubasa.active:
            if Tsubasa.has_hint and show_hints:
                text ("!") style "tsubasamod_dark"
            else:
                text ("") style "tsubasamod_dark"
        elif Tsubasa.active:
                text ("") style "tsubasamod_dark"
        if tsukasapoint + tsukasamiss != Tsukasa.current_max and Tsukasa.active:
            if Tsukasa.has_hint and show_hints:
                text ("!") style "tsukasamod"
            else:
                text ("") style "tsukasamod"
        elif Tsukasa.active:
                text ("") style "tsukasamod"
        if tsuneyopoint + tsuneyomiss != Tsuneyo.current_max and Tsuneyo.active:
            if Tsuneyo.has_hint and show_hints:
                text ("!") style "tsuneyomod"
            else:
                text ("") style "tsuneyomod"
        elif Tsuneyo.active:
                text ("") style "tsuneyomod"
        if utapoint + utamiss != Uta.current_max and Uta.active:
            if Uta.has_hint and show_hints:
                text ("!") style "utamod"
            else:
                text ("") style "utamod"
        elif Uta.active:
                text ("") style "utamod"
        if wakanapoint + wakanamiss != Wakana.current_max and Wakana.active:
            if Wakana.has_hint and show_hints:
                text ("!") style "wakanamod"
            else:
                text ("") style "wakanamod"
        elif Wakana.active:
                text ("") style "wakanamod"
        if yasupoint + yasumiss != Yasu.current_max and Yasu.active:
            if Yasu.has_hint and show_hints:
                text ("!") style "yasumod"
            else:
                text ("") style "yasumod"
        elif Yasu.active:
                text ("") style "yasumod"
        if yukipoint + yukimiss != Yuki.current_max and Yuki.active:
            if Yuki.has_hint and show_hints:
                text ("!") style "yukimod_dark"
            else:
                text ("") style "yukimod_dark"
        elif Yuki.active:
                text ("") style "yukimod_dark"
        if yumipoint + yumimiss != Yumi.current_max and Yumi.active:
            if Yumi.has_hint and show_hints:
                text ("!") style "yumimod"
            else:
                text ("") style "yumimod"
        elif Yumi.active:
                text ("") style "yumimod"

# Names Column (linking to their event trackers)

    vbox:
        xpos .35
        ypos y_col

        text ("") style "mod"

        if Ami.active:
            textbutton _("Ami") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")] style "event_button" text_style "amimod"
        if Ayane.active:
            textbutton _("Ayane") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")] style "event_button" text_style "ayanemod"
        if Chika.active:
            textbutton _("Chika") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")] style "event_button" text_style "chikamod"
        if Chinami.active:
            textbutton _("Chinami") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")] style "event_button" text_style "chinamimod"
        if Futaba.active:
            textbutton _("Futaba") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")] style "event_button" text_style "futabamod"
        if Haruka.active:
            textbutton _("Haruka") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")] style "event_button" text_style "harukamod"
        if Imani.active:
            textbutton _("Imani") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")] style "event_button" text_style "imanimod"
        if Io.active:
            textbutton _("Io") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")] style "event_button" text_style "iomod_dark"
        if Kaori.active:
            textbutton _("Kaori") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")] style "event_button" text_style "kaorimod"
        if Karin.active:
            textbutton _("Karin") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")] style "event_button" text_style "karinmod"
        if Kirin.active:
            textbutton _("Kirin") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")] style "event_button" text_style "kirinmod"
        if Maki.active:
            textbutton _("Maki") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")] style "event_button" text_style "makimod"
        if Makoto.active:
            textbutton _("Makoto") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")] style "event_button" text_style "makotomod"
        if Maya.active:
            textbutton _("Maya") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")] style "event_button" text_style "mayamod"
        if Miku.active:
            textbutton _("Miku") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")] style "event_button" text_style "mikumod"
        if Molly.active:
            textbutton _("Molly") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")] style "event_button" text_style "mollymod"
        if Nao.active:
            textbutton _("Nao") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")] style "event_button" text_style "naomod"
        if Niki.active:
            textbutton _("Niki") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")] style "event_button" text_style "nikimod"
        if Nodoka.active:
            textbutton _("Nodoka") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")] style "event_button" text_style "nodokamod"
        if Noriko.active:
            textbutton _("Noriko") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")] style "event_button" text_style "norikomod"
        if Osako.active:
            textbutton _("Osako") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")] style "event_button" text_style "osakomod"
        if Otoha.active:
            textbutton _("Otoha") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")] style "event_button" text_style "otohamod"
        if Rika.active:
            textbutton _("Rika") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")] style "event_button" text_style "rikamod"
        if Rin.active:
            textbutton _("Rin") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")] style "event_button" text_style "rinmod"
        if Sana.active:
            textbutton _("Sana") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")] style "event_button" text_style "sanamod"
        if Sara.active:
            textbutton _("Sara") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")] style "event_button" text_style "saramod"
        if Touka.active:
            textbutton _("Touka") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")] style "event_button" text_style "toukamod_dark"
        if Tsubasa.active:
            textbutton _("Tsubasa") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")] style "event_button" text_style "tsubasamod_dark"
        if Tsukasa.active:
            textbutton _("Tsukasa") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsukasa")] style "event_button" text_style "tsukasamod"
        if Tsuneyo.active:
            textbutton _("Tsuneyo") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")] style "event_button" text_style "tsuneyomod"
        if Uta.active:
            textbutton _("Uta") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")] style "event_button" text_style "utamod"
        if Wakana.active:
            textbutton _("Wakana") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")] style "event_button" text_style "wakanamod"
        if Yasu.active:
            textbutton _("Yasu") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")] style "event_button" text_style "yasumod"
        if Yuki.active:
            textbutton _("Yuki") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")] style "event_button" text_style "yukimod_dark"
        if Yumi.active:
            textbutton _("Yumi") action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")] style "event_button" text_style "yumimod"

# Affection Column

    vbox: # (to allow for centering of "Affection" at the top)
        xpos .45
        ypos y_col

        text ("Affection") style "mod"

# (actual column)
    vbox:
        xpos .47
        ypos y_col

        text ("") style "mod"

        if Ami.active:
            if Ami.next_love > 0 and show_next:
                text ("[ami_love] ([Ami.next_love])") style "amimod"
            else:
                text ("[ami_love]") style "amimod"
        if Ayane.active:
            if Ayane.next_love > 0 and show_next:
                text ("[ayane_love] ([Ayane.next_love])") style "ayanemod"
            else:
                text ("[ayane_love]") style "ayanemod"
        if Chika.active:
            if Chika.next_love > 0 and show_next:
                text ("[chika_love] ([Chika.next_love])") style "chikamod"
            else:
                text ("[chika_love]") style "chikamod"
        if Chinami.active:
            if Chinami.next_love > 0 and show_next:
                text ("[chinami_love] ([Chinami.next_love])") style "chinamimod"
            else:
                text ("[chinami_love]") style "chinamimod"
        if Futaba.active:
            if Futaba.next_love > 0 and show_next:
                text ("[futaba_love] ([Futaba.next_love])") style "futabamod"
            else:
                text ("[futaba_love]") style "futabamod"
        if Haruka.active:
            if Haruka.next_love > 0 and show_next:
                text ("[haruka_love] ([Haruka.next_love])") style "harukamod"
            else:
                text ("[haruka_love]") style "harukamod"
        if Imani.active:
            if Imani.next_love > 0 and show_next:
                text ("[imani_love] ([Imani.next_love])") style "imanimod"
            else:
                text ("[imani_love]") style "imanimod"
        if Io.active:
            if Io.next_love > 0 and show_next:
                text ("[io_love] ([Io.next_love])") style "iomod_dark"
            else:
                text ("[io_love]") style "iomod_dark"
        if Kaori.active:
            if Kaori.next_love > 0 and show_next:
                text ("[kaori_love] ([Kaori.next_love])") style "kaorimod"
            else:
                text ("[kaori_love]") style "kaorimod"
        if Karin.active:
            if Karin.next_love > 0 and show_next:
                text ("[karin_love] ([Karin.next_love])") style "karinmod"
            else:
                text ("[karin_love]") style "karinmod"
        if Kirin.active:
            if Kirin.next_love > 0 and show_next:
                text ("[kirin_love] ([Kirin.next_love])") style "kirinmod"
            else:
                text ("[kirin_love]") style "kirinmod"
        if Maki.active:
            if Maki.next_love > 0 and show_next:
                text ("[maki_love] ([Maki.next_love])") style "makimod"
            else:
                text ("[maki_love]") style "makimod"
        if Makoto.active:
            if Makoto.next_love > 0 and show_next:
                text ("[makoto_love] ([Makoto.next_love])") style "makotomod"
            else:
                text ("[makoto_love]") style "makotomod"
        if Maya.active:
            if Maya.next_love > 0 and show_next:
                text ("[maya_love] ([Maya.next_love])") style "mayamod"
            else:
                text ("[maya_love]") style "mayamod"
        if Miku.active:
            if Miku.next_love > 0 and show_next:
                text ("[miku_love] ([Miku.next_love])") style "mikumod"
            else:
                text ("[miku_love]") style "mikumod"
        if Molly.active:
            if Molly.next_love > 0 and show_next:
                text ("[molly_love] ([Molly.next_love])") style "mollymod"
            else:
                text ("[molly_love]") style "mollymod"
        if Nao.active:
            if Nao.next_love > 0 and show_next:
                text ("[nao_love] ([Nao.next_love])") style "naomod"
            else:
                text ("[nao_love]") style "naomod"
        if Niki.active:
            if Niki.next_love > 0 and show_next:
                text ("[niki_love] ([Niki.next_love])") style "nikimod"
            else:
                text ("[niki_love]") style "nikimod"
        if Nodoka.active:
            if Nodoka.next_love > 0 and show_next:
                text ("[nodoka_love] ([Nodoka.next_love])") style "nodokamod"
            else:
                text ("[nodoka_love]") style "nodokamod"
        if Noriko.active:
            if Noriko.next_love > 0 and show_next:
                text ("[noriko_love] ([Noriko.next_love])") style "norikomod"
            else:
                text ("[noriko_love]") style "norikomod"
        if Osako.active:
            if Osako.next_love > 0 and show_next:
                text ("[osako_love] ([Osako.next_love])") style "osakomod"
            else:
                text ("[osako_love]") style "osakomod"
        if Otoha.active:
            if Otoha.next_love > 0 and show_next:
                text ("[otoha_love] ([Otoha.next_love])") style "otohamod"
            else:
                text ("[otoha_love]") style "otohamod"
        if Rika.active:
            if Rika.next_love > 0 and show_next:
                text ("[rika_love] ([Rika.next_love])") style "rikamod"
            else:
                text ("[rika_love]") style "rikamod"
        if Rin.active:
            if Rin.next_love > 0 and show_next:
                text ("[rin_love] ([Rin.next_love])") style "rinmod"
            else:
                text ("[rin_love]") style "rinmod"
        if Sana.active:
            if Sana.next_love > 0 and show_next:
                text ("[sana_love] ([Sana.next_love])") style "sanamod"
            else:
                text ("[sana_love]") style "sanamod"
        if Sara.active:
            if Sara.next_love > 0 and show_next:
                text ("[sara_love] ([Sara.next_love])") style "saramod"
            else:
                text ("[sara_love]") style "saramod"
        if Touka.active:
            if Touka.next_love > 0 and show_next:
                text ("[touka_love] ([Touka.next_love])") style "toukamod_dark"
            else:
                text ("[touka_love]") style "toukamod_dark"
        if Tsubasa.active:
            if Tsubasa.next_love > 0 and show_next:
                text ("[tsubasa_love] ([Tsubasa.next_love])") style "tsubasamod_dark"
            else:
                text ("[tsubasa_love]") style "tsubasamod_dark"
        if Tsukasa.active:
            if Tsukasa.next_love > 0 and show_next:
                text ("[tsukasa_love] ([Tsukasa.next_love])") style "tsukasamod"
            else:
                text ("[tsukasa_love]") style "tsukasamod"
        if Tsuneyo.active:
            if Tsuneyo.next_love > 0 and show_next:
                text ("[tsuneyo_love] ([Tsuneyo.next_love])") style "tsuneyomod"
            else:
                text ("[tsuneyo_love]") style "tsuneyomod"
        if Uta.active:
            if Uta.next_love > 0 and show_next:
                text ("[uta_love] ([Uta.next_love])") style "utamod"
            else:
                text ("[uta_love]") style "utamod"
        if Wakana.active:
            if Wakana.next_love > 0 and show_next:
                text ("[wakana_love] ([Wakana.next_love])") style "wakanamod"
            else:
                text ("[wakana_love]") style "wakanamod"
        if Yasu.active:
            if Yasu.next_love > 0 and show_next:
                text ("[yasu_love] ([Yasu.next_love])") style "yasumod"
            else:
                text ("[yasu_love]") style "yasumod"
        if Yuki.active:
            if Yuki.next_love > 0 and show_next:
                text ("[yuki_love] ([Yuki.next_love])") style "yukimod_dark"
            else:
                text ("[yuki_love]") style "yukimod_dark"
        if Yumi.active:
            if Yumi.next_love > 0 and show_next:
                text ("[yumi_love] ([Yumi.next_love])") style "yumimod"
            else:
                text ("[yumi_love]") style "yumimod"

# Lust Column
    vbox:
        xpos .57
        ypos y_col

        text ("Lust") style "mod"
        if Ami.active:
            if Ami.next_lust > 0 and show_next:
                text ("[ami_lust] ([Ami.next_lust])") style "amimod"
            elif Ami.lust_active:
                text ("[ami_lust]") style "amimod"
            else:
                text ("N/A") style "mod"
        if Ayane.active:
            if Ayane.next_lust > 0 and show_next:
                text ("[ayane_lust] ([Ayane.next_lust])") style "ayanemod"
            elif Ayane.lust_active:
                text ("[ayane_lust]") style "ayanemod"
            else:
                text ("N/A") style "mod"
        if Chika.active:
            if Chika.next_lust > 0 and show_next:
                text ("[chika_lust] ([Chika.next_lust])") style "chikamod"
            elif Chika.lust_active:
                text ("[chika_lust]") style "chikamod"
            else:
                text ("N/A") style "mod"
        if Chinami.active:
            if Chinami.next_lust > 0 and show_next:
                text ("[chinami_lust] ([Chinami.next_lust])") style "chinamimod"
            elif Chinami.lust_active:
                text ("[chinami_lust]") style "chinamimod"
            else:
                text ("N/A") style "mod"
        if Futaba.active:
            if Futaba.next_lust > 0 and show_next:
                text ("[futaba_lust] ([Futaba.next_lust])") style "futabamod"
            elif Futaba.lust_active:
                text ("[futaba_lust]") style "futabamod"
            else:
                text ("N/A") style "mod"
        if Haruka.active:
            if Haruka.next_lust > 0 and show_next:
                text ("[haruka_lust] ([Haruka.next_lust])") style "harukamod"
            elif Haruka.lust_active:
                text ("[haruka_lust]") style "harukamod"
            else:
                text ("N/A") style "mod"
        if Imani.active:
            if Imani.next_lust > 0 and show_next:
                text ("[imani_lust] ([Imani.next_lust])") style "imanimod"
            elif Imani.lust_active:
                text ("[imani_lust]") style "imanimod"
            else:
                text ("N/A") style "mod"
        if Io.active:
            if Io.next_lust > 0 and show_next:
                text ("[io_lust] ([Io.next_lust])") style "iomod_dark"
            elif Io.lust_active:
                text ("[io_lust]") style "iomod_dark"
            else:
                text ("N/A") style "mod"
        if Kaori.active:
            if Kaori.next_lust > 0 and show_next:
                text ("[kaori_lust] ([Kaori.next_lust])") style "kaorimod"
            elif Kaori.lust_active:
                text ("[kaori_lust]") style "kaorimod"
            else:
                text ("N/A") style "mod"
        if Karin.active:
            if Karin.next_lust > 0 and show_next:
                text ("[karin_lust] ([Karin.next_lust])") style "karinmod"
            elif Karin.lust_active:
                text ("[karin_lust]") style "karinmod"
            else:
                text ("N/A") style "mod"
        if Kirin.active:
            if Kirin.next_lust > 0 and show_next:
                text ("[kirin_lust] ([Kirin.next_lust])") style "kirinmod"
            elif Kirin.lust_active:
                text ("[kirin_lust]") style "kirinmod"
            else:
                text ("N/A") style "mod"
        if Maki.active:
            if Maki.next_lust > 0 and show_next:
                text ("[maki_lust] ([Maki.next_lust])") style "makimod"
            elif Maki.lust_active:
                text ("[maki_lust]") style "makimod"
            else:
                text ("N/A") style "mod"
        if Makoto.active:
            if Makoto.next_lust > 0 and show_next:
                text ("[makoto_lust] ([Makoto.next_lust])") style "makotomod"
            elif Makoto.lust_active:
                text ("[makoto_lust]") style "makotomod"
            else:
                text ("N/A") style "mod"
        if Maya.active:
            if Maya.next_lust > 0 and show_next:
                text ("[maya_lust] ([Maya.next_lust])") style "mayamod"
            elif Maya.lust_active:
                text ("[maya_lust]") style "mayamod"
            else:
                text ("N/A") style "mod"
        if Miku.active:
            if Miku.next_lust > 0 and show_next:
                text ("[miku_lust] ([Miku.next_lust])") style "mikumod"
            elif Miku.lust_active:
                text ("[miku_lust]") style "mikumod"
            else:
                text ("N/A") style "mod"
        if Molly.active:
            if Molly.next_lust > 0 and show_next:
                text ("[molly_lust] ([Molly.next_lust])") style "mollymod"
            elif Molly.lust_active:
                text ("[molly_lust]") style "mollymod"
            else:
                text ("N/A") style "mod"
        if Nao.active:
            if Nao.next_lust > 0 and show_next:
                text ("[nao_lust] ([Nao.next_lust])") style "naomod"
            elif Nao.lust_active:
                text ("[nao_lust]") style "naomod"
            else:
                text ("N/A") style "mod"
        if Niki.active:
            if Niki.next_lust > 0 and show_next:
                text ("[niki_lust] ([Niki.next_lust])") style "nikimod"
            elif Niki.lust_active:
                text ("[niki_lust]") style "nikimod"
            else:
                text ("N/A") style "mod"
        if Nodoka.active:
            if Nodoka.next_lust > 0 and show_next:
                text ("[nodoka_lust] ([Nodoka.next_lust])") style "nodokamod"
            elif Nodoka.lust_active:
                text ("[nodoka_lust]") style "nodokamod"
            else:
                text ("N/A") style "mod"
        if Noriko.active:
            if Noriko.next_lust > 0 and show_next:
                text ("[noriko_lust] ([Noriko.next_lust])") style "norikomod"
            elif Noriko.lust_active:
                text ("[noriko_lust]") style "norikomod"
            else:
                text ("N/A") style "mod"
        if Osako.active:
            if Osako.next_lust > 0 and show_next:
                text ("[osako_lust] ([Osako.next_lust])") style "osakomod"
            elif Osako.lust_active:
                text ("[osako_lust]") style "osakomod"
            else:
                text ("N/A") style "mod"
        if Otoha.active:
            if Otoha.next_lust > 0 and show_next:
                text ("[otoha_lust] ([Otoha.next_lust])") style "otohamod"
            elif Otoha.lust_active:
                text ("[otoha_lust]") style "otohamod"
            else:
                text ("N/A") style "mod"
        if Rika.active:
            if Rika.next_lust > 0 and show_next:
                text ("[rika_lust] ([Rika.next_lust])") style "rikamod"
            elif Rika.lust_active:
                text ("[rika_lust]") style "rikamod"
            else:
                text ("N/A") style "mod"
        if Rin.active:
            if Rin.next_lust > 0 and show_next:
                text ("[rin_lust] ([Rin.next_lust])") style "rinmod"
            elif Rin.lust_active:
                text ("[rin_lust]") style "rinmod"
            else:
                text ("N/A") style "mod"
        if Sana.active:
            if Sana.next_lust > 0 and show_next:
                text ("[sana_lust] ([Sana.next_lust])") style "sanamod"
            elif Sana.lust_active:
                text ("[sana_lust]") style "sanamod"
            else:
                text ("N/A") style "mod"
        if Sara.active:
            if Sara.next_lust > 0 and show_next:
                text ("[sara_lust] ([Sara.next_lust])") style "saramod"
            elif Sara.lust_active:
                text ("[sara_lust]") style "saramod"
            else:
                text ("N/A") style "mod"
        if Touka.active:
            if Touka.next_lust > 0 and show_next:
                text ("[touka_lust] ([Touka.next_lust])") style "toukamod_dark"
            elif Touka.lust_active:
                text ("[touka_lust]") style "toukamod_dark"
            else:
                text ("N/A") style "mod"
        if Tsubasa.active:
            if Tsubasa.next_lust > 0 and show_next:
                text ("[tsubasa_lust] ([Tsubasa.next_lust])") style "tsubasamod_dark"
            elif Tsubasa.lust_active:
                text ("[tsubasa_lust]") style "tsubasamod_dark"
            else:
                text ("N/A") style "mod"
        if Tsukasa.active:
            if Tsukasa.next_lust > 0 and show_next:
                text ("[tsukasa_lust] ([Tsukasa.next_lust])") style "tsukasamod"
            elif Tsukasa.lust_active:
                text ("[tsukasa_lust]") style "tsukasamod"
            else:
                text ("N/A") style "mod"
        if Tsuneyo.active:
            if Tsuneyo.next_lust > 0 and show_next:
                text ("[tsuneyo_lust] ([Tsuneyo.next_lust])") style "tsuneyomod"
            elif Tsuneyo.lust_active:
                text ("[tsuneyo_lust]") style "tsuneyomod"
            else:
                text ("N/A") style "mod"
        if Uta.active:
            if Uta.next_lust > 0 and show_next:
                text ("[uta_lust] ([Uta.next_lust])") style "utamod"
            elif Uta.lust_active:
                text ("[uta_lust]") style "utamod"
            else:
                text ("N/A") style "mod"
        if Wakana.active:
            if Wakana.next_lust > 0 and show_next:
                text ("[wakana_lust] ([Wakana.next_lust])") style "wakanamod"
            elif Wakana.lust_active:
                text ("[wakana_lust]") style "wakanamod"
            else:
                text ("N/A") style "mod"
        if Yasu.active:
            if Yasu.next_lust > 0 and show_next:
                text ("[yasu_lust] ([Yasu.next_lust])") style "yasumod"
            elif Yasu.lust_active:
                text ("[yasu_lust]") style "yasumod"
            else:
                text ("N/A") style "mod"
        if Yuki.active:
            if Yuki.next_lust > 0 and show_next:
                text ("[yuki_lust] ([Yuki.next_lust])") style "yukimod_dark"
            elif Yuki.lust_active:
                text ("[yuki_lust]") style "yukimod_dark"
            else:
                text ("N/A") style "mod"
        if Yumi.active:
            if Yumi.next_lust > 0 and show_next:
                text ("[yumi_lust] ([Yumi.next_lust])") style "yumimod"
            elif Yumi.lust_active:
                text ("[yumi_lust]") style "yumimod"
            else:
                text ("N/A") style "mod"

# Events Column
    vbox:
        xpos .67
        ypos y_col

        text ("Events") style "mod"

        if Ami.active and amimiss < 1:
            text ("[amipoint]/[Ami.current_max]") style "amimod"
        elif Ami.active and amimiss >= 1:
            text ("{color=[amicolor]}[amipoint]/[Ami.current_max]{/color} {color=#FF0000}([amimiss]){/color}") style "mod"

        if Ayane.active and ayanemiss < 1:
            text ("[ayanepoint]/[Ayane.current_max]") style "ayanemod"
        elif Ayane.active and ayanemiss >= 1:
            text ("{color=[ayanecolor]}[ayanepoint]/[Ayane.current_max]{/color} {color=#FF0000}([ayanemiss]){/color}") style "mod"

        if Chika.active and chikamiss < 1:
            text ("[chikapoint]/[Chika.current_max]") style "chikamod"
        elif Chika.active and chikamiss >= 1:
            text ("{color=[chikacolor]}[chikapoint]/[Chika.current_max]{/color} {color=#FF0000}([chikamiss]){/color}") style "mod"

        if Chinami.active and chinamimiss < 1:
            text ("[chinamipoint]/[Chinami.current_max]") style "chinamimod"
        elif Chinami.active and chinamimiss >= 1:
            text ("{color=[chinamicolor]}[chinamipoint]/[Chinami.current_max]{/color} {color=#FF0000}([chinamimiss]){/color}") style "mod"

        if Futaba.active and futabamiss < 1:
            text ("[futabapoint]/[Futaba.current_max]") style "futabamod"
        elif Futaba.active and futabamiss >= 1:
            text ("{color=[futabacolor]}[futabapoint]/[Futaba.current_max]{/color} {color=#FF0000}([futabamiss]){/color}") style "mod"

        if Haruka.active and harukamiss < 1:
            text ("[harukapoint]/[Haruka.current_max]") style "harukamod"
        elif Haruka.active and harukamiss >= 1:
            text ("{color=[harukacolor]}[harukapoint]/[Haruka.current_max]{/color} {color=#FF0000}([harukamiss]){/color}") style "mod"

        if Imani.active and imanimiss < 1:
            text ("[imanipoint]/[Imani.current_max]") style "imanimod"
        elif Imani.active and imanimiss >= 1:
            text ("{color=[imanicolor]}[imanipoint]/[Imani.current_max]{/color} {color=#FF0000}([imanimiss]){/color}") style "mod"

        if Io.active and iomiss < 1:
            text ("[iopoint]/[Io.current_max]") style "iomod_dark"
        elif Io.active and iomiss >= 1:
            text ("{color=[iocolor]}[iopoint]/[Io.current_max]{/color} {color=#FF0000}([iomiss]){/color}") style "mod"

        if Kaori.active and kaorimiss < 1:
            text ("[kaoripoint]/[Kaori.current_max]") style "kaorimod"
        elif Kaori.active and kaorimiss >= 1:
            text ("{color=[kaoricolor]}[kaoripoint]/[Kaori.current_max]{/color} {color=#FF0000}([kaorimiss]){/color}") style "mod"

        if Karin.active and karinmiss < 1:
            text ("[karinpoint]/[Karin.current_max]") style "karinmod"
        elif Karin.active and karinmiss >= 1:
            text ("{color=[karincolor]}[karinpoint]/[Karin.current_max]{/color} {color=#FF0000}([karinmiss]){/color}") style "mod"

        if Kirin.active and kirinmiss < 1:
            text ("[kirinpoint]/[Kirin.current_max]") style "kirinmod"
        elif Kirin.active and kirinmiss >= 1:
            text ("{color=[kirincolor]}[kirinpoint]/[Kirin.current_max]{/color} {color=#FF0000}([kirinmiss]){/color}") style "mod"

        if Maki.active and makimiss < 1:
            text ("[makipoint]/[Maki.current_max]") style "makimod"
        elif Maki.active and makimiss >= 1:
            text ("{color=[makicolor]}[makipoint]/[Maki.current_max]{/color} {color=#FF0000}([makimiss]){/color}") style "mod"

        if Makoto.active and makotomiss < 1:
            text ("[makotopoint]/[Makoto.current_max]") style "makotomod"
        elif Makoto.active and makotomiss >= 1:
            text ("{color=[makotocolor]}[makotopoint]/[Makoto.current_max]{/color} {color=#FF0000}([makotomiss]){/color}") style "mod"

        if Maya.active and mayamiss < 1:
            text ("[mayapoint]/[Maya.current_max]") style "mayamod"
        elif Maya.active and mayamiss >= 1:
            text ("{color=[mayacolor]}[mayapoint]/[Maya.current_max]{/color} {color=#FF0000}([mayamiss]){/color}") style "mod"

        if Miku.active and mikumiss < 1:
            text ("[mikupoint]/[Miku.current_max]") style "mikumod"
        elif Miku.active and mikumiss >= 1:
            text ("{color=[mikucolor]}[mikupoint]/[Miku.current_max]{/color} {color=#FF0000}([mikumiss]){/color}") style "mod"

        if Molly.active and mollymiss < 1:
            text ("[mollypoint]/[Molly.current_max]") style "mollymod"
        elif Molly.active and mollymiss >= 1:
            text ("{color=[mollycolor]}[mollypoint]/[Molly.current_max]{/color} {color=#FF0000}([mollymiss]){/color}") style "mod"

        if Nao.active and naomiss < 1:
            text ("[naopoint]/[Nao.current_max]") style "naomod"
        elif Nao.active and naomiss >= 1:
            text ("{color=[naocolor]}[naopoint]/[Nao.current_max]{/color} {color=#FF0000}([naomiss]){/color}") style "mod"

        if Niki.active and nikimiss < 1:
            text ("[nikipoint]/[Niki.current_max]") style "nikimod"
        elif Niki.active and nikimiss >= 1:
            text ("{color=[nikicolor]}[nikipoint]/[Niki.current_max]{/color} {color=#FF0000}([nikimiss]){/color}") style "mod"

        if Nodoka.active and nodokamiss < 1:
            text ("[nodokapoint]/[Nodoka.current_max]") style "nodokamod"
        elif Nodoka.active and nodokamiss >= 1:
            text ("{color=[nodokacolor]}[nodokapoint]/[Nodoka.current_max]{/color} {color=#FF0000}([nodokamiss]){/color}") style "mod"

        if Noriko.active and norikomiss < 1:
            text ("[norikopoint]/[Noriko.current_max]") style "norikomod"
        elif Noriko.active and norikomiss >= 1:
            text ("{color=[norikocolor]}[norikopoint]/[Noriko.current_max]{/color} {color=#FF0000}([norikomiss]){/color}") style "mod"

        if Osako.active and osakomiss < 1:
            text ("[osakopoint]/[Osako.current_max]") style "osakomod"
        elif Osako.active and osakomiss >= 1:
            text ("{color=[osakocolor]}[osakopoint]/[Osako.current_max]{/color} {color=#FF0000}([osakomiss]){/color}") style "mod"

        if Otoha.active and otohamiss < 1:
            text ("[otohapoint]/[Otoha.current_max]") style "otohamod"
        elif Otoha.active and otohamiss >= 1:
            text ("{color=[otohacolor]}[otohapoint]/[Otoha.current_max]{/color} {color=#FF0000}([otohamiss]){/color}") style "mod"

        if Rika.active and rikamiss < 1:
            text ("[rikapoint]/[Rika.current_max]") style "rikamod"
        elif Rika.active and rikamiss >= 1:
            text ("{color=[rikacolor]}[rikapoint]/[Rika.current_max]{/color} {color=#FF0000}([rikamiss]){/color}") style "mod"

        if Rin.active and rinmiss < 1:
            text ("[rinpoint]/[Rin.current_max]") style "rinmod"
        elif Rin.active and rinmiss >= 1:
            text ("{color=[rincolor]}[rinpoint]/[Rin.current_max]{/color} {color=#FF0000}([rinmiss]){/color}") style "mod"

        if Sana.active and sanamiss < 1:
            text ("[sanapoint]/[Sana.current_max]") style "sanamod"
        elif Sana.active and sanamiss >= 1:
            text ("{color=[sanacolor]}[sanapoint]/[Sana.current_max]{/color} {color=#FF0000}([sanamiss]){/color}") style "mod"

        if Sara.active and saramiss < 1:
            text ("[sarapoint]/[Sara.current_max]") style "saramod"
        elif Sara.active and saramiss >= 1:
            text ("{color=[saracolor]}[sarapoint]/[Sara.current_max]{/color} {color=#FF0000}([saramiss]){/color}") style "mod"

        if Touka.active and toukamiss < 1:
            text ("[toukapoint]/[Touka.current_max]") style "toukamod_dark"
        elif Touka.active and toukamiss >= 1:
            text ("{color=[toukacolor]}[toukapoint]/[Touka.current_max]{/color} {color=#FF0000}([toukamiss]){/color}") style "mod"

        if Tsubasa.active and tsubasamiss < 1:
            text ("[tsubasapoint]/[Tsubasa.current_max]") style "tsubasamod_dark"
        elif Tsubasa.active and tsubasamiss >= 1:
            text ("{color=[tsubasacolor]}[tsubasapoint]/[Tsubasa.current_max]{/color} {color=#FF0000}([tsubasamiss]){/color}") style "mod"

        if Tsukasa.active and tsukasamiss < 1:
            text ("[tsukasapoint]/[Tsukasa.current_max]") style "tsukasamod"
        elif Tsukasa.active and tsukasamiss >= 1:
            text ("{color=[tsukasacolor]}[tsukasapoint]/[Tsukasa.current_max]{/color} {color=#FF0000}([tsukasamiss]){/color}") style "mod"

        if Tsuneyo.active and tsuneyomiss < 1:
            text ("[tsuneyopoint]/[Tsuneyo.current_max]") style "tsuneyomod"
        elif Tsuneyo.active and tsuneyomiss >= 1:
            text ("{color=[tsuneyocolor]}[tsuneyopoint]/[Tsuneyo.current_max]{/color} {color=#FF0000}([tsuneyomiss]){/color}") style "mod"

        if Uta.active and utamiss < 1:
            text ("[utapoint]/[Uta.current_max]") style "utamod"
        elif Uta.active and utamiss >= 1:
            text ("{color=[utacolor]}[utapoint]/[Uta.current_max]{/color} {color=#FF0000}([utamiss]){/color}") style "mod"

        if Wakana.active and wakanamiss < 1:
            text ("[wakanapoint]/[Wakana.current_max]") style "wakanamod"
        elif Wakana.active and wakanamiss >= 1:
            text ("{color=[wakanacolor]}[wakanapoint]/[Wakana.current_max]{/color} {color=#FF0000}([wakanamiss]){/color}") style "mod"

        if Yasu.active and yasumiss < 1:
            text ("[yasupoint]/[Yasu.current_max]") style "yasumod"
        elif Yasu.active and yasumiss >= 1:
            text ("{color=[yasucolor]}[yasupoint]/[Yasu.current_max]{/color} {color=#FF0000}([yasumiss]){/color}") style "mod"

        if Yuki.active and yukimiss < 1:
            text ("[yukipoint]/[Yuki.current_max]") style "yukimod_dark"
        elif Yuki.active and yukimiss >= 1:
            text ("{color=[yukicolor]}[yukipoint]/[Yuki.current_max]{/color} {color=#FF0000}([yukimiss]){/color}") style "mod"

        if Yumi.active and yumimiss < 1:
            text ("[yumipoint]/[Yumi.current_max]") style "yumimod"
        elif Yumi.active and yumimiss >= 1:
            text ("{color=[yumicolor]}[yumipoint]/[Yumi.current_max]{/color} {color=#FF0000}([yumimiss]){/color}") style "mod"

# Options Column
    vbox:
        xpos .8
        ypos op_col

        textbutton _("{color=#FFFFFF}Options{/color}") action ShowMenu("mod_options") text_style "mod"
