
################################################################################
## Girls
################################################################################

init:
    transform customzoom:
        zoom 0.33

screen amitrackerm2():

    key "g" action Return()

    tag menu

    use game_menu(_("Girls"), scroll="viewport"):

        null

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    # calculate lengh of viewport window
    $ if show_complete: girl_scroll = ((eval(showgirl).max[max_chapter] + max_chapter - 1) * 26) + 5
    $ if not show_complete: girl_scroll = ((eval(showgirl).current_max - eval(showgirl.lower() + "point") + max_chapter - 1) * 26) + 5

    vbox: #box to stack the headers on the event stuff
        xpos .25
        ypos 40
        area (0,0,1450,930)

        vbox: #box for the navigations buttons
            hbox: #box to hold the navigations buttons side by side
                vbox:
                    hbox:
                        if Ami.active and ((amipoint + amimiss != Ami.max[current_chapter]) or show_completed_girls == True):
                            if Ami.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/amithumb1.png"
                                    hover "images/amithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/amithumb1.png")
                                    hover "images/amithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ami")]
                                    at customzoom
                            text(" ")
                        if Ayane.active and ((ayanepoint + ayanemiss != Ayane.max[current_chapter]) or show_completed_girls == True):
                            if Ayane.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/ayanethumb1.png"
                                    hover "images/ayanethumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/ayanethumb1.png")
                                    hover "images/ayanethumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Ayane")]
                                    at customzoom
                            text(" ")
                        if Chika.active and ((chikapoint + chikamiss != Chika.max[current_chapter]) or show_completed_girls == True):
                            if Chika.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/chikathumb1.png"
                                    hover "images/chikathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/chikathumb1.png")
                                    hover "images/chikathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chika")]
                                    at customzoom
                            text(" ")
                        if Chinami.active and ((chinamipoint + chinamimiss != Chinami.max[current_chapter]) or show_completed_girls == True):
                            if Chinami.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/chinamithumb1.png"
                                    hover "images/chinamithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/chinamithumb1.png")
                                    hover "images/chinamithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Chinami")]
                                    at customzoom
                            text(" ")
                        if Futaba.active and ((futabapoint + futabamiss != Futaba.max[current_chapter]) or show_completed_girls == True):
                            if Futaba.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/futabathumb1.png"
                                    hover "images/futabathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/futabathumb1.png")
                                    hover "images/futabathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Futaba")]
                                    at customzoom
                            text(" ")
                        if Haruka.active and ((harukapoint + harukamiss != Haruka.max[current_chapter]) or show_completed_girls == True):
                            if Haruka.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/harukathumb1.png"
                                    hover "images/harukathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/harukathumb1.png")
                                    hover "images/harukathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Haruka")]
                                    at customzoom
                            text(" ")
                        if Imani.active and ((imanipoint + imanimiss != Imani.max[current_chapter]) or show_completed_girls == True):
                            if Imani.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/imanithumb1.png"
                                    hover "images/imanithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/imanithumb1.png")
                                    hover "images/imanithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Imani")]
                                    at customzoom
                            text(" ")
                        if Io.active and ((iopoint + iomiss != Io.max[current_chapter]) or show_completed_girls == True):
                            if Io.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/iothumb1.png"
                                    hover "images/iothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/iothumb1.png")
                                    hover "images/iothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Io")]
                                    at customzoom
                            text(" ")
                        if Kaori.active and ((kaoripoint + kaorimiss != Kaori.max[current_chapter]) or show_completed_girls == True):
                            if Kaori.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/kaorithumb1.png"
                                    hover "images/kaorithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/kaorithumb1.png")
                                    hover "images/kaorithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kaori")]
                                    at customzoom
                            text(" ")
                        if Karin.active and ((karinpoint + karinmiss != Karin.max[current_chapter]) or show_completed_girls == True):
                            if Karin.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/karinthumb1.png"
                                    hover "images/karinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/karinthumb1.png")
                                    hover "images/karinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Karin")]
                                    at customzoom
                            text(" ")
                        if Kirin.active and ((kirinpoint + kirinmiss != Kirin.max[current_chapter]) or show_completed_girls == True):
                            if Kirin.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/kirinthumb1.png"
                                    hover "images/kirinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/kirinthumb1.png")
                                    hover "images/kirinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Kirin")]
                                    at customzoom
                            text(" ")
                        if Maki.active and ((makipoint + makimiss != Maki.max[current_chapter]) or show_completed_girls == True):
                            if Maki.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/makithumb1.png"
                                    hover "images/makithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/makithumb1.png")
                                    hover "images/makithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maki")]
                                    at customzoom
                            text(" ")
                        if Makoto.active and ((makotopoint + makotomiss != Makoto.max[current_chapter]) or show_completed_girls == True):
                            if Makoto.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/makotothumb1.png"
                                    hover "images/makotothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/makotothumb1.png")
                                    hover "images/makotothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Makoto")]
                                    at customzoom
                            text(" ")
                        if Maya.active and ((mayapoint + mayamiss != Maya.max[current_chapter]) or show_completed_girls == True):
                            if Maya.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/mayathumb1.png"
                                    hover "images/mayathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/mayathumb1.png")
                                    hover "images/mayathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Maya")]
                                    at customzoom
                            text(" ")
                        if Miku.active and ((mikupoint + mikumiss != Miku.max[current_chapter]) or show_completed_girls == True):
                            if Miku.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/mikuthumb1.png"
                                    hover "images/mikuthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/mikuthumb1.png")
                                    hover "images/mikuthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Miku")]
                                    at customzoom
                            text(" ")
                        if Molly.active and ((mollypoint + mollymiss != Molly.max[current_chapter]) or show_completed_girls == True):
                            if Molly.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/mollythumb1.png"
                                    hover "images/mollythumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/mollythumb1.png")
                                    hover "images/mollythumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Molly")]
                                    at customzoom
                            text(" ")
                        if Nao.active and ((naopoint + naomiss != Nao.max[current_chapter]) or show_completed_girls == True):
                            if Nao.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/naothumb1.png"
                                    hover "images/naothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/naothumb1.png")
                                    hover "images/naothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nao")]
                                    at customzoom
                            text(" ")
                        if Niki.active and ((nikipoint + nikimiss != Niki.max[current_chapter]) or show_completed_girls == True):
                            if Niki.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/nikithumb1.png"
                                    hover "images/nikithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/nikithumb1.png")
                                    hover "images/nikithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Niki")]
                                    at customzoom
                            text(" ")
                    hbox:
                        ypos 10
                        if Nodoka.active and ((nodokapoint + nodokamiss != Nodoka.max[current_chapter]) or show_completed_girls == True):
                            if Nodoka.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/nodokathumb1.png"
                                    hover "images/nodokathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/nodokathumb1.png")
                                    hover "images/nodokathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Nodoka")]
                                    at customzoom
                            text(" ")
                        if Noriko.active and ((norikopoint + norikomiss != Noriko.max[current_chapter]) or show_completed_girls == True):
                            if Noriko.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/norikothumb1.png"
                                    hover "images/norikothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/norikothumb1.png")
                                    hover "images/norikothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Noriko")]
                                    at customzoom
                            text(" ")
                        if Osako.active and ((osakopoint + osakomiss != Osako.max[current_chapter]) or show_completed_girls == True):
                            if Osako.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/osakothumb1.png"
                                    hover "images/osakothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/osakothumb1.png")
                                    hover "images/osakothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Osako")]
                                    at customzoom
                            text(" ")
                        if Otoha.active and ((otohapoint + otohamiss != Otoha.max[current_chapter]) or show_completed_girls == True):
                            if Otoha.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/otohathumb1.png"
                                    hover "images/otohathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/otohathumb1.png")
                                    hover "images/otohathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Otoha")]
                                    at customzoom
                            text(" ")
                        if Rika.active and ((rikapoint + rikamiss != Rika.max[current_chapter]) or show_completed_girls == True):
                            if Rika.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/rikathumb1.png"
                                    hover "images/rikathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/rikathumb1.png")
                                    hover "images/rikathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rika")]
                                    at customzoom
                            text(" ")
                        if Rin.active and ((rinpoint + rinmiss != Rin.max[current_chapter]) or show_completed_girls == True):
                            if Rin.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/rinthumb1.png"
                                    hover "images/rinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/rinthumb1.png")
                                    hover "images/rinthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Rin")]
                                    at customzoom
                            text(" ")
                        if Sana.active and ((sanapoint + sanamiss != Sana.max[current_chapter]) or show_completed_girls == True):
                            if Sana.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/sanathumb1.png"
                                    hover "images/sanathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/sanathumb1.png")
                                    hover "images/sanathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sana")]
                                    at customzoom
                            text(" ")
                        if Sara.active and ((sarapoint + saramiss != Sara.max[current_chapter]) or show_completed_girls == True):
                            if Sara.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/sarathumb1.png"
                                    hover "images/sarathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/sarathumb1.png")
                                    hover "images/sarathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Sara")]
                                    at customzoom
                            text(" ")
                        if Touka.active and ((toukapoint + toukamiss != Touka.max[current_chapter]) or show_completed_girls == True):
                            if Touka.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/toukathumb1.png"
                                    hover "images/toukathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/toukathumb1.png")
                                    hover "images/toukathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Touka")]
                                    at customzoom
                            text(" ")
                        if Tsubasa.active and ((tsubasapoint + tsubasamiss != Tsubasa.max[current_chapter]) or show_completed_girls == True):
                            if Tsubasa.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/tsubasathumb1.png"
                                    hover "images/tsubasathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/tsubasathumb1.png")
                                    hover "images/tsubasathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsubasa")]
                                    at customzoom
                            text(" ")
                        if Tsukasa.active and ((tsukasapoint + tsukasamiss != Tsukasa.max[current_chapter]) or show_completed_girls == True):
                            if Tsukasa.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/tsukasathumb1.png"
                                    hover "images/tsukasathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsukasa")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/tsukasathumb1.png")
                                    hover "images/tsukasathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsukasa")]
                                    at customzoom
                            text(" ")
                        if Tsuneyo.active and ((tsuneyopoint + tsuneyomiss != Tsuneyo.max[current_chapter]) or show_completed_girls == True):
                            if Tsuneyo.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/tsuneyothumb1.png"
                                    hover "images/tsuneyothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/tsuneyothumb1.png")
                                    hover "images/tsuneyothumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Tsuneyo")]
                                    at customzoom
                            text(" ")
                        if Uta.active and ((utapoint + utamiss != Uta.max[current_chapter]) or show_completed_girls == True):
                            if Uta.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/utathumb1.png"
                                    hover "images/utathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/utathumb1.png")
                                    hover "images/utathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Uta")]
                                    at customzoom
                            text(" ")
                        if Wakana.active and ((wakanapoint + wakanamiss != Wakana.max[current_chapter]) or show_completed_girls == True):
                            if Wakana.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/wakanathumb1.png"
                                    hover "images/wakanathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/wakanathumb1.png")
                                    hover "images/wakanathumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Wakana")]
                                    at customzoom
                            text(" ")
                        if Yasu.active and ((yasupoint + yasumiss != Yasu.max[current_chapter]) or show_completed_girls == True):
                            if Yasu.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/yasuthumb1.png"
                                    hover "images/yasuthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/yasuthumb1.png")
                                    hover "images/yasuthumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yasu")]
                                    at customzoom
                            text(" ")
                        if Yuki.active and ((yukipoint + yukimiss != Yuki.max[current_chapter]) or show_completed_girls == True):
                            if Yuki.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/yukithumb1.png"
                                    hover "images/yukithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/yukithumb1.png")
                                    hover "images/yukithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yuki")]
                                    at customzoom
                            text(" ")
                        if Yumi.active and ((yumipoint + yumimiss != Yumi.max[current_chapter]) or show_completed_girls == True):
                            if Yumi.has_hint or not desaturate_girls:
                                imagebutton:
                                    idle "images/yumithumb1.png"
                                    hover "images/yumithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")]
                                    at customzoom
                            else:
                                imagebutton:
                                    idle im.Grayscale("images/yumithumb1.png")
                                    hover "images/yumithumb1.png"
                                    focus_mask True
                                    action [ShowMenu("amitrackerm2"), SetVariable("showgirl", "Yumi")]
                                    at customzoom
                            text(" ")

        vbox: #box for the character name
            ypos 25
            if showgirl == "Ami":
                if ami_lust == "N/A":
                    text "{color=[amicolor]}Ami Arakawa ([ami_love] Affection){/color}" style "aff"
                else:
                    text "{color=[amicolor]}Ami Arakawa ([ami_love] Affection/[ami_lust] Lust){/color}" style "aff"
            if showgirl == "Ayane":
                if ayane_lust == "N/A":
                    text "{color=[ayanecolor]}Ayane Amamiya ([ayane_love] Affection){/color}" style "aff"
                else:
                    text "{color=[ayanecolor]}Ayane Amamiya ([ayane_love] Affection/[ayane_lust] Lust){/color}" style "aff"
            if showgirl == "Chika":
                if chika_lust == "N/A":
                    text "{color=[chikacolor]}Chika Chosokabe ([chika_love] Affection){/color}" style "aff"
                else:
                    text "{color=[chikacolor]}Chika Chosokabe ([chika_love] Affection/[chika_lust] Lust){/color}" style "aff"
            if showgirl == "Chinami":
                if chinami_lust == "N/A":
                    text "{color=[chinamicolor]}Chinami Chosokabe ([chinami_love] Affection){/color}" style "aff"
                else:
                    text "{color=[chinamicolor]}Chinami Chosokabe ([chinami_love] Affection/[chinami_lust] Lust){/color}" style "aff"
            if showgirl == "Futaba":
                if futaba_lust == "N/A":
                    text "{color=[futabacolor]}Futaba Fukuyama ([futaba_love] Affection){/color}" style "aff"
                else:
                    text "{color=[futabacolor]}Futaba Fukuyama ([futaba_love] Affection/[futaba_lust] Lust){/color}" style "aff"
            if showgirl == "Haruka":
                if haruka_lust == "N/A":
                    text "{color=[harukacolor]}Haruka Hamasaki ([haruka_love] Affection){/color}" style "aff"
                else:
                    text "{color=[harukacolor]}Haruka Hamasaki ([haruka_love] Affection/[haruka_lust] Lust){/color}" style "aff"
            if showgirl == "Imani":
                if imani_lust == "N/A":
                    text "{color=[imanicolor]}Imani Imai ([imani_love] Affection){/color}" style "aff"
                else:
                    text "{color=[imanicolor]}Imani Imai ([imani_love] Affection/[imani_lust] Lust){/color}" style "aff"
            if showgirl == "Io":
                if io_lust == "N/A":
                    text "{color=[iocolor]}Io Ichimonji ([io_love] Affection){/color}" style "aff"
                else:
                    text "{color=[iocolor]}Io Ichimonji ([io_love] Affection/[io_lust] Lust){/color}" style "aff"
            if showgirl == "Kaori":
                if kaori_lust == "N/A":
                    text "{color=[kaoricolor]}Kaori Kadowaki ([kaori_love] Affection){/color}" style "aff"
                else:
                    text "{color=[kaoricolor]}Kaori Kadowaki ([kaori_love] Affection/[kaori_lust] Lust){/color}" style "aff"
            if showgirl == "Karin":
                if karin_lust == "N/A":
                    text "{color=[karincolor]}Karin Kanda ([karin_love] Affection){/color}" style "aff"
                else:
                    text "{color=[karincolor]}Karin Kanda ([karin_love] Affection/[karin_lust] Lust){/color}" style "aff"
            if showgirl == "Kirin":
                if kirin_lust == "N/A":
                    text "{color=[kirincolor]}Kirin Kanda ([kirin_love] Affection){/color}" style "aff"
                else:
                    text "{color=[kirincolor]}Kirin Kanda ([kirin_love] Affection/[kirin_lust] Lust){/color}" style "aff"
            if showgirl == "Maki":
                if maki_lust == "N/A":
                    text "{color=[makicolor]}Maki Miyamura ([maki_love] Affection){/color}" style "aff"
                else:
                    text "{color=[makicolor]}Maki Miyamura ([maki_love] Affection/[maki_lust] Lust){/color}" style "aff"
            if showgirl == "Makoto":
                if makoto_lust == "N/A":
                    text "{color=[makotocolor]}Makoto Miyamura ([makoto_love] Affection){/color}" style "aff"
                else:
                    text "{color=[makotocolor]}Makoto Miyamura ([makoto_love] Affection/[makoto_lust] Lust){/color}" style "aff"
            if showgirl == "Maya":
                if maya_lust == "N/A":
                    text "{color=[mayacolor]}Maya Makinami ([maya_love] Affection){/color}" style "aff"
                else:
                    text "{color=[mayacolor]}Maya Makinami ([maya_love] Affection/[maya_lust] Lust){/color}" style "aff"
            if showgirl == "Miku":
                if miku_lust == "N/A":
                    text "{color=[mikucolor]}Miku Maruyama ([miku_love] Affection){/color}" style "aff"
                else:
                    text "{color=[mikucolor]}Miku Maruyama ([miku_love] Affection/[miku_lust] Lust){/color}" style "aff"
            if showgirl == "Molly":
                if molly_lust == "N/A":
                    text "{color=[mollycolor]}Molly MacCormack ([molly_love] Affection){/color}" style "aff"
                else:
                    text "{color=[mollycolor]}Molly MacCormack ([molly_love] Affection/[molly_lust] Lust){/color}" style "aff"
            if showgirl == "Nao":
                if nao_lust == "N/A":
                    text "{color=[naocolor]}Nao ([nao_love] Affection){/color}" style "aff"
                else:
                    text "{color=[naocolor]}Nao ([nao_love] Affection/[nao_lust] Lust){/color}" style "aff"
            if showgirl == "Niki":
                if niki_lust == "N/A":
                    text "{color=[nikicolor]}Niki Nakayama ([niki_love] Affection){/color}" style "aff"
                else:
                    text "{color=[nikicolor]}Niki Nakayama ([niki_love] Affection/[niki_lust] Lust){/color}" style "aff"
            if showgirl == "Nodoka":
                if nodoka_lust == "N/A":
                    text "{color=[nodokacolor]}Nodoka Nagasawa ([nodoka_love] Affection){/color}" style "aff"
                else:
                    text "{color=[nodokacolor]}Nodoka Nagasawa ([nodoka_love] Affection/[nodoka_lust] Lust){/color}" style "aff"
            if showgirl == "Noriko":
                if noriko_lust == "N/A":
                    text "{color=[norikocolor]}Noriko Nakayama ([noriko_love] Affection){/color}" style "aff"
                else:
                    text "{color=[norikocolor]}Noriko Nakayama ([noriko_love] Affection/[noriko_lust] Lust){/color}" style "aff"
            if showgirl == "Osako":
                if osako_lust == "N/A":
                    text "{color=[osakocolor]}Osako Osaka ([osako_love] Affection){/color}" style "aff"
                else:
                    text "{color=[osakocolor]}Osako Osaka ([osako_love] Affection/[osako_lust] Lust){/color}" style "aff"
            if showgirl == "Otoha":
                if otoha_lust == "N/A":
                    text "{color=[otohacolor]}Otoha Okakura ([otoha_love] Affection){/color}" style "aff"
                else:
                    text "{color=[otohacolor]}Otoha Okakura ([otoha_love] Affection/[otoha_lust] Lust){/color}" style "aff"
            if showgirl == "Rika":
                if rika_lust == "N/A":
                    text "{color=[rikacolor]}Rika Rokuhara ([rika_love] Affection){/color}" style "aff"
                else:
                    text "{color=[rikacolor]}Rika Rokuhara ([rika_love] Affection/[rika_lust] Lust){/color}" style "aff"
            if showgirl == "Rin":
                if rin_lust == "N/A":
                    text "{color=[rincolor]}Rin Rokuhara ([rin_love] Affection){/color}" style "aff"
                else:
                    text "{color=[rincolor]}Rin Rokuhara ([rin_love] Affection/[rin_lust] Lust){/color}" style "aff"
            if showgirl == "Sana":
                if sana_lust == "N/A":
                    text "{color=[sanacolor]}Sana Sakakibara ([sana_love] Affection){/color}" style "aff"
                else:
                    text "{color=[sanacolor]}Sana Sakakibara ([sana_love] Affection/[sana_lust] Lust){/color}" style "aff"
            if showgirl == "Sara":
                if sara_lust == "N/A":
                    text "{color=[saracolor]}Sara Sakakibara ([sara_love] Affection){/color}" style "aff"
                else:
                    text "{color=[saracolor]}Sara Sakakibara ([sara_love] Affection/[sara_lust] Lust){/color}" style "aff"
            if showgirl == "Touka":
                if touka_lust == "N/A":
                    text "{color=[toukacolor]}Touka Tsukioka ([touka_love] Affection){/color}" style "aff"
                else:
                    text "{color=[toukacolor]}Touka Tsukioka ([touka_love] Affection/[touka_lust] Lust){/color}" style "aff"
            if showgirl == "Tsubasa":
                if tsubasa_lust == "N/A":
                    text "{color=[tsubasacolor]}Tsubasa Tsukioka ([tsubasa_love] Affection){/color}" style "aff"
                else:
                    text "{color=[tsubasacolor]}Tsubasa Tsukioka ([tsubasa_love] Affection/[tsubasa_lust] Lust){/color}" style "aff"
            if showgirl == "Tsukasa":
                if tsukasa_lust == "N/A":
                    text "{color=[tsukasacolor]}Tsukasa Tsukioka ([tsukasa_love] Affection){/color}" style "aff"
                else:
                    text "{color=[tsukasacolor]}Tsukasa Tsukioka ([tsukasa_love] Affection/[tsukasa_lust] Lust){/color}" style "aff"
            if showgirl == "Tsuneyo":
                if tsuneyo_lust == "N/A":
                    text "{color=[tsuneyocolor]}Tsuneyo Tojo ([tsuneyo_love] Affection){/color}" style "aff"
                else:
                    text "{color=[tsuneyocolor]}Tsuneyo Tojo ([tsuneyo_love] Affection/[tsuneyo_lust] Lust){/color}" style "aff"
            if showgirl == "Uta":
                if uta_lust == "N/A":
                    text "{color=[utacolor]}Uta Ushibori ([uta_love] Affection){/color}" style "aff"
                else:
                    text "{color=[utacolor]}Uta Ushibori ([uta_love] Affection/[uta_lust] Lust){/color}" style "aff"
            if showgirl == "Wakana":
                if wakana_lust == "N/A":
                    text "{color=[wakanacolor]}Wakana Watabe ([wakana_love] Affection){/color}" style "aff"
                else:
                    text "{color=[wakanacolor]}Wakana Watabe ([wakana_love] Affection/[wakana_lust] Lust){/color}" style "aff"
            if showgirl == "Yasu":
                if yasu_lust == "N/A":
                    text "{color=[yasucolor]}Yasu Yasui ([yasu_love] Affection){/color}" style "aff"
                else:
                    text "{color=[yasucolor]}Yasu Yasui ([yasu_love] Affection/[yasu_lust] Lust){/color}" style "aff"
            if showgirl == "Yuki":
                if yuki_lust == "N/A":
                    text "{color=[yukicolor]}Yuki Yamaguchi ([yuki_love] Affection){/color}" style "aff"
                else:
                    text "{color=[yukicolor]}Yuki Yamaguchi ([yuki_love] Affection/[yuki_lust] Lust){/color}" style "aff"
            if showgirl == "Yumi":
                if yumi_lust == "N/A":
                    text "{color=[yumicolor]}Yumi Yamaguchi ([yumi_love] Affection){/color}" style "aff"
                else:
                    text "{color=[yumicolor]}Yumi Yamaguchi ([yumi_love] Affection/[yumi_lust] Lust){/color}" style "aff"

        viewport: #viewport to hold the event list and hints side by side
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            ypos 35
            child_size (1432,girl_scroll)

            vbox: #box for the event list

                style_prefix "tracker"

                #AMIEVENT

                if showgirl == "Ami":

                    if firsttimeamisroom and show_complete:
                        textbutton _("Harem Tutorial {b}✓{/b}") action Replay("firsttimeamisroom", locked=False) text_style "modmybutton"
                    elif not firsttimeamisroom and not ev_firsttimeamisroom.missed:
                        text _("Harem Tutorial")

                    if amifirsthall and show_complete:
                        textbutton _("Uninvited {b}✓{/b}") action Replay("amifirsthall", locked=False) text_style "modmybutton"
                    elif not amifirsthall and not ev_amifirsthall.missed:
                        text _("Uninvited")

                    if amisroom5 and show_complete:
                        textbutton _("The Queen of Spiders {b}✓{/b}") action Replay("amisroom5", locked=False) text_style "modmybutton"
                    elif not amisroom5 and not ev_amisroom5.missed:
                        text _("The Queen of Spiders")

                    if amidorm5 and show_complete:
                        textbutton _("Home Away From Home {b}✓{/b}") action Replay("amidorm5", locked=False) text_style "modmybutton"
                    elif not amidorm5 and not ev_amidorm5.missed:
                        text _("Home Away From Home")

                    if amisroom10 and show_complete:
                        textbutton _("Something Darker {b}✓{/b}") action Replay("amisroom10", locked=False) text_style "modmybutton"
                    elif not amisroom10 and not ev_amisroom10.missed:
                        text _("Something Darker")

                    if aminew1 and show_complete:
                        textbutton _("Couple's Discount (Sea of Diamonds) {b}✓{/b}") action Replay("aminew1", locked=False) text_style "modmybutton"
                    elif not aminew1 and not ev_aminew1.missed:
                        text _("Couple's Discount (Sea of Diamonds)")

                    if aminew2 and show_complete:
                        textbutton _("Ode to a Marsh Warbler {b}✓{/b}") action Replay("aminew2", locked=False) text_style "modmybutton"
                    elif not aminew2 and not ev_aminew2.missed:
                        text _("Ode to a Marsh Warbler")

                    if amidorm10 and show_complete:
                        textbutton _("No One Can See Us {b}✓{/b}") action Replay("amidorm10", locked=False) text_style "modmybutton"
                    elif not amidorm10 and not ev_amidorm10.missed:
                        text _("No One Can See Us")

                    if day98 and show_complete:
                        textbutton _("Walking on Air {b}✓{/b}") action Replay("day98", locked=False) text_style "modmybutton"
                    elif ev_day98.missed and show_complete:
                        text _("{color=EF1A1A}{s}Falling, Falling, Falling{/s}{/color}")
                    elif not day98 and not ev_day98.missed:
                        text _("{color=FF85FD}Walking on Air{/color}")

                    if amidorm15 and show_complete:
                        textbutton _("Back Out in the Heat {b}✓{/b}") action Replay("amidorm15", locked=False) text_style "modmybutton"
                    elif not amidorm15 and not ev_amidorm15.missed:
                        text _("Back Out in the Heat")

                    if amisroom15 and show_complete:
                        textbutton _("Important Things {b}✓{/b}") action Replay("amisroom15", locked=False) text_style "modmybutton"
                    elif not amisroom15 and not ev_amisroom15.missed:
                        text _("Important Things")

                    if amilust10 and show_complete:
                        textbutton _("Wake Up Call {b}✓{/b}") action Replay("amilust10", locked=False) text_style "modmybutton"
                    elif ev_amilust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Sleep Forever{/s}{/color}")
                    elif not amilust10 and not ev_amilust10.missed:
                        text _("{color=FF85FD}Wake Up Call{/color}")

                    if amisroom20 and show_complete:
                        textbutton _("Cute Girls and Stuff {b}✓{/b}") action Replay("amisroom20", locked=False) text_style "modmybutton"
                    elif not amisroom20 and not ev_amisroom20.missed:
                        text _("Cute Girls and Stuff")

                    if amidorm20 and show_complete:
                        textbutton _("Divergence {b}✓{/b}") action Replay("amidorm20", locked=False) text_style "modmybutton"
                    elif not amidorm20 and not ev_amidorm20.missed:
                        text _("Divergence")

                    if amisroom25 and show_complete:
                        textbutton _("Such Small Hands {b}✓{/b}") action Replay("amisroom25", locked=False) text_style "modmybutton"
                    elif ev_amisroom25.missed and show_complete:
                        text _("{color=EF1A1A}{s}Ghosts in the Walls{/s}{/color}")
                    elif not amisroom25 and not ev_amisroom25.missed:
                        text _("Such Small Hands")

                    if amidorm25 and show_complete:
                        textbutton _("Everlasting Love {b}✓{/b}") action Replay("amidorm25", locked=False) text_style "modmybutton"
                    elif not amidorm25 and not ev_amidorm25.missed:
                        text _("Everlasting Love")

                    text _("---------------------------------------------")

                    if amiinvite1 and show_complete:
                        textbutton _("Living {b}✓{/b}") action Replay("amiinvite1", locked=False) text_style "modmybutton"
                    elif not amiinvite1 and not ev_amiinvite1.missed:
                        text _("{color=778EFF}Living{/color}")

                    if amiinvite2 and show_complete:
                        textbutton _("Rising to the Challenge {b}✓{/b}") action Replay("amiinvite2", locked=False) text_style "modmybutton"
                    elif ev_amiinvite2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Failing at Everything{/s}{/color}")
                    elif not amiinvite2 and not ev_amiinvite2.missed:
                        text _("{color=778EFF}Rising to the Challenge{/color}")

                    if amiinvite3 and show_complete:
                        textbutton _("Best Friends Forever {b}✓{/b}") action Replay("amiinvite3", locked=False) text_style "modmybutton"
                    elif not amiinvite3 and not ev_amiinvite3.missed:
                        text _("{color=778EFF}Best Friends Forever{/color}")

                    if amimaid30 and show_complete:
                        textbutton _("Third Place {b}✓{/b}") action Replay("amimaid30", locked=False) text_style "modmybutton"
                    elif not amimaid30 and not ev_amimaid30.missed:
                        text _("Third Place")

                    if amidate35 and show_complete:
                        textbutton _("The Big Sleep (Cute Girl Magic) {b}✓{/b}") action Replay("amidate35", locked=False) text_style "modmybutton"
                    elif not amidate35 and not ev_amidate35.missed:
                        text _("The Big Sleep (Cute Girl Magic)")

                    if amidorm40 and show_complete:
                        textbutton _("Heaven for Human Blood {b}✓{/b}") action Replay("amidorm40", locked=False) text_style "modmybutton"
                    elif ev_amidorm40.missed and show_complete:
                        text _("{color=EF1A1A}{s}A Horse Misused{/s}{/color}")
                    elif not amidorm40 and not ev_amidorm40.missed:
                        text _("Heaven for Human Blood")

                    if amilust15 and show_complete:
                        textbutton _("As Light as Air {b}✓{/b}") action Replay("amilust15", locked=False) text_style "modmybutton"
                    elif ev_amilust15.missed and show_complete:
                        text _("{color=EF1A1A}{s}Does She Remind You?{/s}{/color}")
                    elif not amilust15 and not ev_amilust15.missed:
                        text _("{color=FF85FD}As Light as Air{/color}")

                    if amilust20 and show_complete:
                        textbutton _("Conscious or Not {b}✓{/b}") action Replay("amilust20", locked=False) text_style "modmybutton"
                    elif ev_amilust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}A Hallway Full of Eyes{/s}{/color}")
                    elif not amilust20 and not ev_amilust20.missed:
                        text _("{color=FF85FD}Conscious or Not{/color}")

                    if amidate50 and show_complete:
                        textbutton _("Outcry of the Hunted Hare {b}✓{/b}") action Replay("amidate50", locked=False) text_style "modmybutton"
                    elif not amidate50 and not ev_amidate50.missed:
                        text _("Outcry of the Hunted Hare")

                    if amidate50p2 and show_complete:
                        textbutton _("Fruits of the Two Seasons {b}✓{/b}") action Replay("amidate50p2", locked=False) text_style "modmybutton"
                    elif not amidate50p2 and not ev_amidate50p2.missed:
                        text _("Fruits of the Two Seasons")

                    if amidate50p3 and show_complete:
                        textbutton _("My Life With You {b}✓{/b}") action Replay("amidate50p3", locked=False) text_style "modmybutton"
                    elif not amidate50p3 and not ev_amidate50p3.missed:
                        text _("My Life With You")

                    if amidate50p4 and show_complete:
                        textbutton _("Somnambula {b}✓{/b}") action Replay("amidate50p4", locked=False) text_style "modmybutton"
                    elif not amidate50p4 and not ev_amidate50p4.missed:
                        text _("Somnambula")

                    text _("---------------------------------------------")

                    if amilust35 and show_complete:
                        textbutton _("No One Can Hear Us {b}✓{/b}") action Replay("amilust35", locked=False) text_style "modmybutton"
                    elif ev_amilust35.missed and show_complete:
                        text _("{color=EF1A1A}{s}Splat{/s}{/color}")
                    elif not amilust35 and not ev_amilust35.missed:
                        text _("{color=FF85FD}No One Can Hear Us{/color}")

                    if amimaid50 and show_complete:
                        textbutton _("Not Safe For Work {b}✓{/b}") action Replay("amimaid50", locked=False) text_style "modmybutton"
                    elif not amimaid50 and not ev_amimaid50.missed:
                        text _("Not Safe For Work")

                    if amiinvite4 and show_complete:
                        textbutton _("Mama's Girl {b}✓{/b}") action Replay("amiinvite4", locked=False) text_style "modmybutton"
                    elif not amiinvite4 and not ev_amiinvite4.missed:
                        text _("{color=778EFF}Mama's Girl{/color}")

                    if amispecial50 and show_complete:
                        textbutton _("Worry Not, The Mason Jar {b}✓{/b}") action Replay("amispecial50", locked=False) text_style "modmybutton"
                    elif not amispecial50 and not ev_amispecial50.missed:
                        text _("Worry Not, The Mason Jar")

                    if amilust50 and show_complete:
                        textbutton _("Family Matters {b}✓{/b}") action Replay("amilust50", locked=False) text_style "modmybutton"
                    elif ev_amilust50.missed and show_complete:
                        text _("{color=EF1A1A}{s}Fucking Die You Piece of Shit{/s}{/color}")
                    elif not amilust50 and not ev_amilust50.missed:
                        text _("{color=FF85FD}Family Matters{/color}")

                    text _("---------------------------------------------")

                    if amilust60 and show_complete:
                        textbutton _("The Caretaker {b}✓{/b}") action Replay("amilust60", locked=False) text_style "modmybutton"
                    elif ev_amilust60.missed and show_complete:
                        text _("{color=EF1A1A}{s}Bucket, Bucket, Lovely Old Bucket{/s}{/color}")
                    elif not amilust60 and not ev_amilust60.missed:
                        text _("{color=FF85FD}The Caretaker{/color}")

                    if amispring1 and show_complete:
                        textbutton _("Della {b}✓{/b}") action Replay("amispring1", locked=False) text_style "modmybutton"
                    elif not amispring1 and not ev_amispring1.missed:
                        text _("Della")

                    if amicamp1 and show_complete:
                        textbutton _("Every Day Birds (In Nothing But Blood) {b}✓{/b}") action Replay("amicamp1", locked=False) text_style "modmybutton"
                    elif not amicamp1 and not ev_amicamp1.missed:
                        text _("Every Day Birds (In Nothing But Blood)")

                    if amicamp2 and show_complete:
                        textbutton _("There Is A Light That Never Goes Out {b}✓{/b}") action Replay("amicamp2", locked=False) text_style "modmybutton"
                    elif not amicamp2 and not ev_amicamp2.missed:
                        text _("There Is A Light That Never Goes Out")

                    if halloweenami1 and show_complete:
                        textbutton _("Soon (Another Nightmare) {b}✓{/b}") action Replay("halloweenami1", locked=False) text_style "modmybutton"
                    elif not halloweenami1 and not ev_halloweenami1.missed:
                        text _("Soon (Another Nightmare)")

                    if amispring2 and show_complete:
                        textbutton _("Faith & Sacrifice {b}✓{/b}") action Replay("amispring2", locked=False) text_style "modmybutton"
                    elif not amispring2 and not ev_amispring2.missed:
                        text _("Faith & Sacrifice")

                    if amispring3 and show_complete:
                        textbutton _("Shiritori {b}✓{/b}") action Replay("amispring3", locked=False) text_style "modmybutton"
                    elif not amispring3 and not ev_amispring3.missed:
                        text _("Shiritori")

                    if amispring4 and show_complete:
                        textbutton _("Nakadashi {b}✓{/b}") action Replay("amispring4", locked=False) text_style "modmybutton"
                    elif ev_amispring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}SPRAY AND PRAY{/s}{/color}")
                    elif not amispring4 and not ev_amispring4.missed:
                        text _("Nakadashi")

                    if amispring5 and show_complete:
                        textbutton _("Victrola {b}✓{/b}") action Replay("amispring5", locked=False) text_style "modmybutton"
                    elif ev_amispring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}INESCAPABLE WHITE NOISE{/s}{/color}")
                    elif not amispring5 and not ev_amispring5.missed:
                        text _("Victrola")

                #AYANEEVENT

                if showgirl == "Ayane":

                    if firsttimedojo and show_complete:
                        textbutton _("The Unwavering Bravery of Ayane Amamiya {b}✓{/b}") action Replay("firsttimedojo", locked=False) text_style "modmybutton"
                    elif not firsttimedojo and not ev_firsttimedojo.missed:
                        text _("The Unwavering Bravery of Ayane Amamiya")

                    if ayanefirsthall and show_complete:
                        textbutton _("Spy on Me {b}✓{/b}") action Replay("ayanefirsthall", locked=False) text_style "modmybutton"
                    elif not ayanefirsthall and not ev_ayanefirsthall.missed:
                        text _("Spy on Me")

                    if dojo5 and show_complete:
                        textbutton _("The Battle for Kumon-mi {b}✓{/b}") action Replay("dojo5", locked=False) text_style "modmybutton"
                    elif not dojo5 and not ev_dojo5.missed:
                        text _("The Battle for Kumon-mi")

                    if dojo10 and show_complete:
                        textbutton _("Names of Our Children {b}✓{/b}") action Replay("dojo10", locked=False) text_style "modmybutton"
                    elif not dojo10 and not ev_dojo10.missed:
                        text _("Names of Our Children")

                    if ayanedorm5 and show_complete:
                        textbutton _("Home Sweet Home {b}✓{/b}") action Replay("ayanedorm5", locked=False) text_style "modmybutton"
                    elif not ayanedorm5 and not ev_ayanedorm5.missed:
                        text _("Home Sweet Home")

                    if ayanenew1 and show_complete:
                        textbutton _("Imprinting {b}✓{/b}") action Replay("ayanenew1", locked=False) text_style "modmybutton"
                    elif not ayanenew1 and not ev_ayanenew1.missed:
                        text _("Imprinting")

                    if ayanenew2 and show_complete:
                        textbutton _("Far From Fantasy {b}✓{/b}") action Replay("ayanenew2", locked=False) text_style "modmybutton"
                    elif not ayanenew2 and not ev_ayanenew2.missed:
                        text _("Far From Fantasy")

                    if ayanenew3 and show_complete:
                        textbutton _("Forever Yours (Top of the World) {b}✓{/b}") action Replay("ayanenew3", locked=False) text_style "modmybutton"
                    elif not ayanenew3 and not ev_ayanenew3.missed:
                        text _("Forever Yours (Top of the World)")

                    if ayanedorm10 and show_complete:
                        textbutton _("Less Like the Vulture {b}✓{/b}") action Replay("ayanedorm10", locked=False) text_style "modmybutton"
                    elif not ayanedorm10 and not ev_ayanedorm10.missed:
                        text _("Less Like the Vulture")

                    if ayanedorm15 and show_complete:
                        textbutton _("First Words {b}✓{/b}") action Replay("ayanedorm15", locked=False) text_style "modmybutton"
                    elif not ayanedorm15 and not ev_ayanedorm15.missed:
                        text _("First Words")

                    if day68 and show_complete:
                        textbutton _("Backwards Spider Crawl {b}✓{/b}") action Replay("day68", locked=False) text_style "modmybutton"
                    elif not day68 and not ev_day68.missed:
                        text _("{color=FF85FD}Backwards Spider Crawl{/color}")

                    if dojo20 and show_complete:
                        textbutton _("Endless Torment {b}✓{/b}") action Replay("dojo20", locked=False) text_style "modmybutton"
                    elif not dojo20 and not ev_dojo20.missed:
                        text _("Endless Torment")

                    if ayanedorm20 and show_complete:
                        textbutton _("Still Young {b}✓{/b}") action Replay("ayanedorm20", locked=False) text_style "modmybutton"
                    elif not ayanedorm20 and not ev_ayanedorm20.missed:
                        text _("Still Young")

                    if ayanelust10 and show_complete:
                        textbutton _("Prisoner {b}✓{/b}") action Replay("ayanelust10", locked=False) text_style "modmybutton"
                    elif ev_ayanelust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Back to Normal{/s}{/color}")
                    elif not ayanelust10 and not ev_ayanelust10.missed:
                        text _("{color=FF85FD}Prisoner{/color}")

                    if dojo25 and show_complete:
                        textbutton _("Regularly Scheduled Programming {b}✓{/b}") action Replay("dojo25", locked=False) text_style "modmybutton"
                    elif not dojo25 and not ev_dojo25.missed:
                        text _("Regularly Scheduled Programming")

                    if ayanedorm25 and show_complete:
                        textbutton _("Cold Air of an Encroaching Winter {b}✓{/b}") action Replay("ayanedorm25", locked=False) text_style "modmybutton"
                    elif not ayanedorm25 and not ev_ayanedorm25.missed:
                        text _("Cold Air of an Encroaching Winter")

                    if dojo30 and show_complete:
                        textbutton _("First and Second {b}✓{/b}") action Replay("dojo30", locked=False) text_style "modmybutton"
                    elif not dojo30 and not ev_dojo30.missed:
                        text _("First and Second")

                    if ayanedorm30 and show_complete:
                        textbutton _("Crazier Things Have Happened {b}✓{/b}") action Replay("ayanedorm30", locked=False) text_style "modmybutton"
                    elif not ayanedorm30 and not ev_ayanedorm30.missed:
                        text _("Crazier Things Have Happened")

                    text _("---------------------------------------------")

                    if ayaneinvite1 and show_complete:
                        textbutton _("Hail Mary {b}✓{/b}") action Replay("ayaneinvite1", locked=False) text_style "modmybutton"
                    elif not ayaneinvite1 and not ev_ayaneinvite1.missed:
                        text _("{color=778EFF}Hail Mary{/color}")

                    if ayaneinvite2 and show_complete:
                        textbutton _("One of Many Rooms {b}✓{/b}") action Replay("ayaneinvite2", locked=False) text_style "modmybutton"
                    elif not ayaneinvite2 and not ev_ayaneinvite2.missed:
                        text _("{color=778EFF}One of Many Rooms{/color}")

                    if ayanelust15 and show_complete:
                        textbutton _("What a Wonderful World {b}✓{/b}") action Replay("ayanelust15", locked=False) text_style "modmybutton"
                    elif ev_ayanelust15.missed and show_complete:
                        text _("{color=EF1A1A}{s}The World is Bad!{/s}{/color}")
                    elif not ayanelust15 and not ev_ayanelust15.missed:
                        text _("{color=FF85FD}What a Wonderful World{/color}")

                    if dojo35 and show_complete:
                        textbutton _("Under the World Tree {b}✓{/b}") action Replay("dojo35", locked=False) text_style "modmybutton"
                    elif not dojo35 and not ev_dojo35.missed:
                        text _("Under the World Tree")

                    if ayanedorm35 and show_complete:
                        textbutton _("Crash of Thunder {b}✓{/b}") action Replay("ayanedorm35", locked=False) text_style "modmybutton"
                    elif not ayanedorm35 and not ev_ayanedorm35.missed:
                        text _("Crash of Thunder")

                    if ayanespecial1 and show_complete:
                        textbutton _("Nevermind {b}✓{/b}") action Replay("ayanespecial1", locked=False) text_style "modmybutton"
                    elif not ayanespecial1 and not ev_ayanespecial1.missed:
                        text _("Nevermind")

                    if ayanespecial2 and show_complete:
                        textbutton _("Before the Sun Comes Up {b}✓{/b}") action Replay("ayanespecial2", locked=False) text_style "modmybutton"
                    elif not ayanespecial2 and not ev_ayanespecial2.missed:
                        text _("Before the Sun Comes Up")

                    if ayanelust20 and show_complete:
                        textbutton _("Out With the Old {b}✓{/b}") action Replay("ayanelust20", locked=False) text_style "modmybutton"
                    elif ev_ayanelust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}In With the New{/s}{/color}")
                    elif not ayanelust20 and not ev_ayanelust20.missed:
                        text _("{color=FF85FD}Out With the Old{/color}")

                    text _("---------------------------------------------")

                    if ayanespecial40 and show_complete:
                        textbutton _("Chronokinetics (Hell Exists) {b}✓{/b}") action Replay("ayanespecial40", locked=False) text_style "modmybutton"
                    elif not ayanespecial40 and not ev_ayanespecial40.missed:
                        text _("Chronokinetics (Hell Exists)")

                    if ayanesanabeach1 and show_complete:
                        textbutton _("How the World Works {b}✓{/b}") action Replay("ayanesanabeach1", locked=False) text_style "modmybutton"
                    elif not ayanesanabeach1 and not ev_ayanesanabeach1.missed:
                        text _("How the World Works")

                    if ayanespecial50 and show_complete:
                        textbutton _("Chiburi {b}✓{/b}") action Replay("ayanespecial50", locked=False) text_style "modmybutton"
                    elif not ayanespecial50 and not ev_ayanespecial50.missed:
                        text _("Chiburi")

                    if ayanekirintalk and show_complete:
                        textbutton _("Furlough (Tell the World) {b}✓{/b}") action Replay("ayanekirintalk", locked=False) text_style "modmybutton"
                    elif ev_ayanekirintalk.missed and show_complete:
                        text _("{color=EF1A1A}{s}Indefinite Parole{/s}{/color}")
                    elif not ayanekirintalk and not ev_ayanekirintalk.missed:
                        text _("Furlough (Tell the World)")

                    if ayanespecial55 and show_complete:
                        textbutton _("Double Jeopardy {b}✓{/b}") action Replay("ayanespecial55", locked=False) text_style "modmybutton"
                    elif not ayanespecial55 and not ev_ayanespecial55.missed:
                        text _("Double Jeopardy")

                    if ayanebonus1 and show_complete:
                        textbutton _("The Aforementioned Light {b}✓{/b}") action Replay("ayanebonus1", locked=False) text_style "modmybutton"
                    elif ev_ayanebonus1.missed and show_complete:
                        text _("{color=EF1A1A}{s}Dark Side of the Room{/s}{/color}")
                    elif not ayanebonus1 and not ev_ayanebonus1.missed:
                        text _("The Aforementioned Light")

                    if ayanebonus2 and show_complete:
                        textbutton _("Over & Over {b}✓{/b}") action Replay("ayanebonus2", locked=False) text_style "modmybutton"
                    elif ev_ayanebonus2.missed and show_complete:
                        text _("{color=EF1A1A}{s}A Failed Attempt at Being Good{/s}{/color}")
                    elif not ayanebonus2 and not ev_ayanebonus2.missed:
                        text _("Over & Over")

                    if ayanepool55 and show_complete:
                        textbutton _("Dizzy On The Comedown {b}✓{/b}") action Replay("ayanepool55", locked=False) text_style "modmybutton"
                    elif not ayanepool55 and not ev_ayanepool55.missed:
                        text _("Dizzy On The Comedown")

                    text _("---------------------------------------------")

                    if ayanespring1 and show_complete:
                        textbutton _("...But Home is Nowhere {b}✓{/b}") action Replay("ayanespring1", locked=False) text_style "modmybutton"
                    elif not ayanespring1 and not ev_ayanespring1.missed:
                        text _("...But Home is Nowhere")

                    if beachfive3 and show_complete:
                        textbutton _("Doomsayer {b}✓{/b}") action Replay("beachfive3", locked=False) text_style "modmybutton"
                    elif not beachfive3 and not ev_beachfive3.missed:
                        text _("Doomsayer")

                    if beachfive15 and show_complete:
                        textbutton _("As You Wish {b}✓{/b}") action Replay("beachfive15", locked=False) text_style "modmybutton"
                    elif ev_beachfive15.missed and show_complete:
                        text _("{color=EF1A1A}{s}As You Wash{/s}{/color}")
                    elif not beachfive15 and not ev_beachfive15.missed:
                        text _("As You Wish")

                    if halloweenayane1 and show_complete:
                        textbutton _("Chamomile {b}✓{/b}") action Replay("halloweenayane1", locked=False) text_style "modmybutton"
                    elif not halloweenayane1 and not ev_halloweenayane1.missed:
                        text _("Chamomile")

                    if halloweenayane2 and show_complete:
                        textbutton _("Time, Resets, and the Like {b}✓{/b}") action Replay("halloweenayane2", locked=False) text_style "modmybutton"
                    elif not halloweenayane2 and not ev_halloweenayane2.missed:
                        text _("Time, Resets, and the Like")

                    if halloweenayane3 and show_complete:
                        textbutton _("Soliloquy (Wearing Someone Else's Clothes) {b}✓{/b}") action Replay("halloweenayane3", locked=False) text_style "modmybutton"
                    elif not halloweenayane3 and not ev_halloweenayane3.missed:
                        text _("Soliloquy (Wearing Someone Else's Clothes)")

                    if ayanespring2 and show_complete:
                        textbutton _("In Shoes That Don't Fit {b}✓{/b}") action Replay("ayanespring2", locked=False) text_style "modmybutton"
                    elif ev_ayanespring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Bipedal Deformation{/s}{/color}")
                    elif not ayanespring2 and not ev_ayanespring2.missed:
                        text _("In Shoes That Don't Fit")

                    if ayanespring3 and show_complete:
                        textbutton _("Mortal Coil (Gay Stuff) {b}✓{/b}") action Replay("ayanespring3", locked=False) text_style "modmybutton"
                    elif not ayanespring3 and not ev_ayanespring3.missed:
                        text _("Mortal Coil (Gay Stuff)")

                    if undeservedfuture1 and show_complete:
                        textbutton _("Our Cage in Tralfamadore {b}✓{/b}") action Replay("undeservedfuture1", locked=False) text_style "modmybutton"
                    elif not undeservedfuture1 and not ev_undeservedfuture1.missed:
                        text _("Our Cage in Tralfamadore")

                    if undeservedfuture2 and show_complete:
                        textbutton _("Ikura {b}✓{/b}") action Replay("undeservedfuture2", locked=False) text_style "modmybutton"
                    elif not undeservedfuture2 and not ev_undeservedfuture2.missed:
                        text _("Ikura")

                    if undeservedfuture3 and show_complete:
                        textbutton _("A Nightmare, in Retrospect {b}✓{/b}") action Replay("undeservedfuture3", locked=False) text_style "modmybutton"
                    elif not undeservedfuture3 and not ev_undeservedfuture3.missed:
                        text _("A Nightmare, in Retrospect")

                    if undeservedfuture4 and show_complete:
                        textbutton _("Trophy Wife Pt. I {b}✓{/b}") action Replay("undeservedfuture4", locked=False) text_style "modmybutton"
                    elif not undeservedfuture4 and not ev_undeservedfuture4.missed:
                        text _("Trophy Wife Pt. I")

                    if undeservedfuture5 and show_complete:
                        textbutton _("Light of My Life {b}✓{/b}") action Replay("undeservedfuture5", locked=False) text_style "modmybutton"
                    elif not undeservedfuture5 and not ev_undeservedfuture5.missed:
                        text _("Light of My Life")

                    if undeservedfuture6 and show_complete:
                        textbutton _("Infinite Joy {b}✓{/b}") action Replay("undeservedfuture6", locked=False) text_style "modmybutton"
                    elif not undeservedfuture6 and not ev_undeservedfuture6.missed:
                        text _("Infinite Joy")

                    if undeservedfuture7 and show_complete:
                        textbutton _("Bitter Cherries {b}✓{/b}") action Replay("undeservedfuture7", locked=False) text_style "modmybutton"
                    elif not undeservedfuture7 and not ev_undeservedfuture7.missed:
                        text _("Bitter Cherries")

                    if undeservedfuture8 and show_complete:
                        textbutton _("Trophy Wife Pt. II {b}✓{/b}") action Replay("undeservedfuture8", locked=False) text_style "modmybutton"
                    elif not undeservedfuture8 and not ev_undeservedfuture8.missed:
                        text _("Trophy Wife Pt. II")

                    if undeservedfuture9 and show_complete:
                        textbutton _("Like Lions {b}✓{/b}") action Replay("undeservedfuture9", locked=False) text_style "modmybutton"
                    elif not undeservedfuture9 and not ev_undeservedfuture9.missed:
                        text _("Like Lions")

                    if undeservedfuture10 and show_complete:
                        textbutton _("Aomori {b}✓{/b}") action Replay("undeservedfuture10", locked=False) text_style "modmybutton"
                    elif not undeservedfuture10 and not ev_undeservedfuture10.missed:
                        text _("Aomori")

                    if ayanespring4 and show_complete:
                        textbutton _("Transpacific Sadness Symposium N: CHAINSMOKER CHANGELING {b}✓{/b}") action Replay("ayanespring4", locked=False) text_style "modmybutton"
                    elif not ayanespring4 and not ev_ayanespring4.missed:
                        text _("Transpacific Sadness Symposium N: CHAINSMOKER CHANGELING")

                #CHIKAEVENT

                if showgirl == "Chika":

                    if firsttimemall and show_complete:
                        textbutton _("The Retail Machine {b}✓{/b}") action Replay("firsttimemall", locked=False) text_style "modmybutton"
                    elif not firsttimemall and not ev_firsttimemall.missed:
                        text _("The Retail Machine")

                    if chikafirsthall and show_complete:
                        textbutton _("A Dog that Does Math {b}✓{/b}") action Replay("chikafirsthall", locked=False) text_style "modmybutton"
                    elif not chikafirsthall and not ev_chikafirsthall.missed:
                        text _("A Dog that Does Math")

                    if mall5 and show_complete:
                        textbutton _("Big Shot Teacher {b}✓{/b}") action Replay("mall5", locked=False) text_style "modmybutton"
                    elif not mall5 and not ev_mall5.missed:
                        text _("Big Shot Teacher")

                    if chikadorm5 and show_complete:
                        textbutton _("Something About Biting {b}✓{/b}") action Replay("chikadorm5", locked=False) text_style "modmybutton"
                    elif not chikadorm5 and not ev_chikadorm5.missed:
                        text _("Something About Biting")

                    if mall10 and show_complete:
                        textbutton _("Behind The Curtain {b}✓{/b}") action Replay("mall10", locked=False) text_style "modmybutton"
                    elif not mall10 and not ev_mall10.missed:
                        text _("Behind The Curtain")

                    if chikadorm10 and show_complete:
                        textbutton _("Side Event {b}✓{/b}") action Replay("chikadorm10", locked=False) text_style "modmybutton"
                    elif not chikadorm10 and not ev_chikadorm10.missed:
                        text _("Side Event")

                    if chikadorm15 and show_complete:
                        textbutton _("A Castle for Everyone {b}✓{/b}") action Replay("chikadorm15", locked=False) text_style "modmybutton"
                    elif not chikadorm15 and not ev_chikadorm15.missed:
                        text _("A Castle for Everyone")

                    if mall15 and show_complete:
                        textbutton _("A Dog that Doesn't Do Math {b}✓{/b}") action Replay("mall15", locked=False) text_style "modmybutton"
                    elif not mall15 and not ev_mall15.missed:
                        text _("A Dog that Doesn't Do Math")

                    if chikadorm20 and show_complete:
                        textbutton _("Schadenfreude {b}✓{/b}") action Replay("chikadorm20", locked=False) text_style "modmybutton"
                    elif not chikadorm20 and not ev_chikadorm20.missed:
                        text _("Schadenfreude")

                    if mall20 and show_complete:
                        textbutton _("True Power: Unleashed {b}✓{/b}") action Replay("mall20", locked=False) text_style "modmybutton"
                    elif not mall20 and not ev_mall20.missed:
                        text _("True Power: Unleashed")

                    if day139 and show_complete:
                        textbutton _("Detention {b}✓{/b}") action Replay("day139", locked=False) text_style "modmybutton"
                    elif not day139 and not ev_day139.missed:
                        text _("Detention")

                    if chikainvite1 and show_complete:
                        textbutton _("A Trip to the Moon {b}✓{/b}") action Replay("chikainvite1", locked=False) text_style "modmybutton"
                    elif not chikainvite1 and not ev_chikainvite1.missed:
                        text _("{color=778EFF}A Trip to the Moon{/color}")

                    if chikainvite2 and show_complete:
                        textbutton _("First Hunt {b}✓{/b}") action Replay("chikainvite2", locked=False) text_style "modmybutton"
                    elif not chikainvite2 and not ev_chikainvite2.missed:
                        text _("{color=778EFF}First Hunt{/color}")

                    text _("---------------------------------------------")

                    if chikalust10 and show_complete:
                        textbutton _("Baby it's Cold Outside {b}✓{/b}") action Replay("chikalust10", locked=False) text_style "modmybutton"
                    elif ev_chikalust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Freezing to Death{/s}{/color}")
                    elif not chikalust10 and not ev_chikalust10.missed:
                        text _("{color=FF85FD}Baby it's Cold Outside{/color}")

                    if chikaonsen1 and show_complete:
                        textbutton _("Little Miracles {b}✓{/b}") action Replay("chikaonsen1", locked=False) text_style "modmybutton"
                    elif not chikaonsen1 and not ev_chikaonsen1.missed:
                        text _("Little Miracles")

                    if chikaonsen2 and show_complete:
                        textbutton _("Bleed {b}✓{/b}") action Replay("chikaonsen2", locked=False) text_style "modmybutton"
                    elif not chikaonsen2 and not ev_chikaonsen2.missed:
                        text _("Bleed")

                    if chikaonsen3 and show_complete:
                        textbutton _("Three Words {b}✓{/b}") action Replay("chikaonsen3", locked=False) text_style "modmybutton"
                    elif not chikaonsen3 and not ev_chikaonsen3.missed:
                        text _("Three Words")

                    if chikaonsen4 and show_complete:
                        textbutton _("Zanzibar (Counting Cats) {b}✓{/b}") action Replay("chikaonsen4", locked=False) text_style "modmybutton"
                    elif not chikaonsen4 and not ev_chikaonsen4.missed:
                        text _("Zanzibar (Counting Cats)")

                    if chikalust15 and show_complete:
                        textbutton _("The Princess & The Pauper {b}✓{/b}") action Replay("chikalust15", locked=False) text_style "modmybutton"
                    elif ev_chikalust15.missed and show_complete:
                        text _("{color=EF1A1A}{s}Them{/s}{/color}")
                    elif not chikalust15 and not ev_chikalust15.missed:
                        text _("{color=FF85FD}The Princess & The Pauper{/color}")

                    if chikalust20 and show_complete:
                        textbutton _("Into the Woods {b}✓{/b}") action Replay("chikalust20", locked=False) text_style "modmybutton"
                    elif ev_chikalust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}Out of the Woods{/s}{/color}")
                    elif not chikalust20 and not ev_chikalust20.missed:
                        text _("{color=FF85FD}Into the Woods{/color}")

                    if chikaspecial40 and show_complete:
                        textbutton _("In Search of Summer {b}✓{/b}") action Replay("chikaspecial40", locked=False) text_style "modmybutton"
                    elif not chikaspecial40 and not ev_chikaspecial40.missed:
                        text _("In Search of Summer")

                    if mall40 and show_complete:
                        textbutton _("Self Care {b}✓{/b}") action Replay("mall40", locked=False) text_style "modmybutton"
                    elif not mall40 and not ev_mall40.missed:
                        text _("Self Care")

                    if mall40p2 and show_complete:
                        textbutton _("The Gap in the Curtain {b}✓{/b}") action Replay("mall40p2", locked=False) text_style "modmybutton"
                    elif not mall40p2 and not ev_mall40p2.missed:
                        text _("The Gap in the Curtain")

                    if chikadate45 and show_complete:
                        textbutton _("The Gap in the Door {b}✓{/b}") action Replay("chikadate45", locked=False) text_style "modmybutton"
                    elif not chikadate45 and not ev_chikadate45.missed:
                        text _("The Gap in the Door")

                    text _("---------------------------------------------")

                    if chikalust25 and show_complete:
                        textbutton _("Mating Season {b}✓{/b}") action Replay("chikalust25", locked=False) text_style "modmybutton"
                    elif ev_chikalust25.missed and show_complete:
                        text _("{color=EF1A1A}{s}Hibernation{/s}{/color}")
                    elif not chikalust25 and not ev_chikalust25.missed:
                        text _("{color=FF85FD}Mating Season{/color}")

                    if mall45 and show_complete:
                        textbutton _("Rough Cuts {b}✓{/b}") action Replay("mall45", locked=False) text_style "modmybutton"
                    elif not mall45 and not ev_mall45.missed:
                        text _("Rough Cuts")

                    if chikaspecial45 and show_complete:
                        textbutton _("Curry Night {b}✓{/b}") action Replay("chikaspecial45", locked=False) text_style "modmybutton"
                    elif not chikaspecial45 and not ev_chikaspecial45.missed:
                        text _("Curry Night")

                    if chikadorm45 and show_complete:
                        textbutton _("Our Time Atop This Mattress {b}✓{/b}") action Replay("chikadorm45", locked=False) text_style "modmybutton"
                    elif not chikadorm45 and not ev_chikadorm45.missed:
                        text _("Our Time Atop This Mattress")

                    text _("---------------------------------------------")

                    if chikaspring1 and show_complete:
                        textbutton _("Gold Digger {b}✓{/b}") action Replay("chikaspring1", locked=False) text_style "modmybutton"
                    elif not chikaspring1 and not ev_chikaspring1.missed:
                        text _("Gold Digger")

                    if chikaspring2 and show_complete:
                        textbutton _("Original Sin {b}✓{/b}") action Replay("chikaspring2", locked=False) text_style "modmybutton"
                    elif not chikaspring2 and not ev_chikaspring2.missed:
                        text _("Original Sin")

                    if chikaspring3 and show_complete:
                        textbutton _("To Drink, To Drown {b}✓{/b}") action Replay("chikaspring3", locked=False) text_style "modmybutton"
                    elif not chikaspring3 and not ev_chikaspring3.missed:
                        text _("To Drink, To Drown")

                    if chikaspring4 and show_complete:
                        textbutton _("Rabies {b}✓{/b}") action Replay("chikaspring4", locked=False) text_style "modmybutton"
                    elif not chikaspring4 and not ev_chikaspring4.missed:
                        text _("Rabies")

                    if chikaspring5 and show_complete:
                        textbutton _("Frogging {b}✓{/b}") action Replay("chikaspring5", locked=False) text_style "modmybutton"
                    elif not chikaspring5 and not ev_chikaspring5.missed:
                        text _("Frogging")

                    if chikaspring6 and show_complete:
                        textbutton _("Everyone I've Ever Loved {b}✓{/b}") action Replay("chikaspring6", locked=False) text_style "modmybutton"
                    elif not chikaspring6 and not ev_chikaspring6.missed:
                        text _("Everyone I've Ever Loved")

                    if chikaspring7 and show_complete:
                        textbutton _("Transpacific Sadness Symposium V: NEW BLACK PARADIGM {b}✓{/b}") action Replay("chikaspring7", locked=False) text_style "modmybutton"
                    elif not chikaspring7 and not ev_chikaspring7.missed:
                        text _("Transpacific Sadness Symposium V: NEW BLACK PARADIGM")

                    if chikaspring8 and show_complete:
                        textbutton _("Chika-chan vs. Auto-Pilot {b}✓{/b}") action Replay("chikaspring8", locked=False) text_style "modmybutton"
                    elif not chikaspring8 and not ev_chikaspring8.missed:
                        text _("Chika-chan vs. Auto-Pilot")

                    if chikachristmalloween1 and show_complete:
                        textbutton _("A Violent Sort of Sadness {b}✓{/b}") action Replay("chikachristmalloween1", locked=False) text_style "modmybutton"
                    elif not chikachristmalloween1 and not ev_chikachristmalloween1.missed:
                        text _("A Violent Sort of Sadness")

                    if chikachristmalloween2 and show_complete:
                        textbutton _("See You in School {b}✓{/b}") action Replay("chikachristmalloween2", locked=False) text_style "modmybutton"
                    elif not chikachristmalloween2 and not ev_chikachristmalloween2.missed:
                        text _("See You in School")

                #CHINAMIEVENT

                if showgirl == "Chinami":

                    if chinamidate1 and show_complete:
                        textbutton _("5,000 Year-Old Wizard {b}✓{/b}") action Replay("chinamidate1", locked=False) text_style "modmybutton"
                    elif not chinamidate1 and not ev_chinamidate1.missed:
                        text _("5,000 Year-Old Wizard")

                    if chinamidate5 and show_complete:
                        textbutton _("Chinami-Corp {b}✓{/b}") action Replay("chinamidate5", locked=False) text_style "modmybutton"
                    elif not chinamidate5 and not ev_chinamidate5.missed:
                        text _("Chinami-Corp")

                    text _("---------------------------------------------")

                    if chinamidate10 and show_complete:
                        textbutton _("Giant Pool of Jell-O {b}✓{/b}") action Replay("chinamidate10", locked=False) text_style "modmybutton"
                    elif not chinamidate10 and not ev_chinamidate10.missed:
                        text _("Giant Pool of Jell-O")

                    if chinamidate15 and show_complete:
                        textbutton _("Pool Party (Love & Puppies) {b}✓{/b}") action Replay("chinamidate15", locked=False) text_style "modmybutton"
                    elif not chinamidate15 and not ev_chinamidate15.missed:
                        text _("Pool Party (Love & Puppies)")

                    if chinamidate20 and show_complete:
                        textbutton _("Happy Hour {b}✓{/b}") action Replay("chinamidate20", locked=False) text_style "modmybutton"
                    elif not chinamidate20 and not ev_chinamidate20.missed:
                        text _("Happy Hour")

                    text _("---------------------------------------------")

                    if chinamidate25 and show_complete:
                        textbutton _("Death Trap {b}✓{/b}") action Replay("chinamidate25", locked=False) text_style "modmybutton"
                    elif not chinamidate25 and not ev_chinamidate25.missed:
                        text _("Death Trap")

                    if chinamidate30 and show_complete:
                        textbutton _("Bad News Bears {b}✓{/b}") action Replay("chinamidate30", locked=False) text_style "modmybutton"
                    elif not chinamidate30 and not ev_chinamidate30.missed:
                        text _("Bad News Bears")

                    text _("---------------------------------------------")

                    if chinamispring1 and show_complete:
                        textbutton _("Lucky (China Doll) {b}✓{/b}") action Replay("chinamispring1", locked=False) text_style "modmybutton"
                    elif not chinamispring1 and not ev_chinamispring1.missed:
                        text _("Lucky (China Doll)")

                    if chinamispring2 and show_complete:
                        textbutton _("Holden Caulfield {b}✓{/b}") action Replay("chinamispring2", locked=False) text_style "modmybutton"
                    elif not chinamispring2 and not ev_chinamispring2.missed:
                        text _("Holden Caulfield")

                    if chinamispring3 and show_complete:
                        textbutton _("Backwards Boulevard {b}✓{/b}") action Replay("chinamispring3", locked=False) text_style "modmybutton"
                    elif not chinamispring3 and not ev_chinamispring3.missed:
                        text _("Backwards Boulevard")

                    if chinamispring4 and show_complete:
                        textbutton _("Feed Me to the Farm {b}✓{/b}") action Replay("chinamispring4", locked=False) text_style "modmybutton"
                    elif ev_chinamispring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}Mad Cow Disease{/s}{/color}")
                    elif not chinamispring4 and not ev_chinamispring4.missed:
                        text _("Feed Me to the Farm")

                    if chinamispring5 and show_complete:
                        textbutton _("Obnoxious Sexual Rampage {b}✓{/b}") action Replay("chinamispring5", locked=False) text_style "modmybutton"
                    elif ev_chinamispring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}Even More Obnoxious Abstinence{/s}{/color}")
                    elif not chinamispring5 and not ev_chinamispring5.missed:
                        text _("Obnoxious Sexual Rampage")

                    if chinamispring6 and show_complete:
                        textbutton _("Five Hundred Pancakes {b}✓{/b}") action Replay("chinamispring6", locked=False) text_style "modmybutton"
                    elif ev_chinamispring6.missed and show_complete:
                        text _("{color=EF1A1A}{s}Zero Pancakes{/s}{/color}")
                    elif not chinamispring6 and not ev_chinamispring6.missed:
                        text _("Five Hundred Pancakes")

                    if chinamispring7 and show_complete:
                        textbutton _("My Adventures as a Trash Compactor {b}✓{/b}") action Replay("chinamispring7", locked=False) text_style "modmybutton"
                    elif not chinamispring7 and not ev_chinamispring7.missed:
                        text _("My Adventures as a Trash Compactor")

                    if chinamispring8 and show_complete:
                        textbutton _("Transpacific Sadness Symposium IX: HUNG HIGH IN THE HARE HOUSE {b}✓{/b}") action Replay("chinamispring8", locked=False) text_style "modmybutton"
                    elif not chinamispring8 and not ev_chinamispring8.missed:
                        text _("Transpacific Sadness Symposium IX: HUNG HIGH IN THE HARE HOUSE")

                #FUTABAEVENT

                if showgirl == "Futaba":

                    if firsttimelibrary and show_complete:
                        textbutton _("Impossible Blossoms {b}✓{/b}") action Replay("firsttimelibrary", locked=False) text_style "modmybutton"
                    elif not firsttimelibrary and not ev_firsttimelibrary.missed:
                        text _("Impossible Blossoms")

                    if futabafall and show_complete:
                        textbutton _("Fan Fiction {b}✓{/b}") action Replay("futabafall", locked=False) text_style "modmybutton"
                    elif not futabafall and not ev_futabafall.missed:
                        text _("Fan Fiction")

                    if library10 and show_complete:
                        textbutton _("Upside Down {b}✓{/b}") action Replay("library10", locked=False) text_style "modmybutton"
                    elif not library10 and not ev_library10.missed:
                        text _("Upside Down")

                    if futabafirsthall and show_complete:
                        textbutton _("Unidentical Twins {b}✓{/b}") action Replay("futabafirsthall", locked=False) text_style "modmybutton"
                    elif not futabafirsthall and not ev_futabafirsthall.missed:
                        text _("Unidentical Twins")

                    if futabafirstvisit and show_complete:
                        textbutton _("Under the Radar {b}✓{/b}") action Replay("futabafirstvisit", locked=False) text_style "modmybutton"
                    elif not futabafirstvisit and not ev_futabafirstvisit.missed:
                        text _("Under the Radar")

                    if futabadorm10 and show_complete:
                        textbutton _("Cutting Through Cocoons {b}✓{/b}") action Replay("futabadorm10", locked=False) text_style "modmybutton"
                    elif not futabadorm10 and not ev_futabadorm10.missed:
                        text _("Cutting Through Cocoons")

                    if library15 and show_complete:
                        textbutton _("Self-Insert {b}✓{/b}") action Replay("library15", locked=False) text_style "modmybutton"
                    elif not library15 and not ev_library15.missed:
                        text _("Self-Insert")

                    if futabanew1 and show_complete:
                        textbutton _("Broken Flowers {b}✓{/b}") action Replay("futabanew1", locked=False) text_style "modmybutton"
                    elif not futabanew1 and not ev_futabanew1.missed:
                        text _("Broken Flowers")

                    if futabanew2 and show_complete:
                        textbutton _("Great Burdock Leaves {b}✓{/b}") action Replay("futabanew2", locked=False) text_style "modmybutton"
                    elif not futabanew2 and not ev_futabanew2.missed:
                        text _("Great Burdock Leaves")

                    if futabanew3 and show_complete:
                        textbutton _("Clam's Tongue {b}✓{/b}") action Replay("futabanew3", locked=False) text_style "modmybutton"
                    elif not futabanew3 and not ev_futabanew3.missed:
                        text _("Clam's Tongue")

                    if futabadorm15 and show_complete:
                        textbutton _("Legs of a Dying Spider {b}✓{/b}") action Replay("futabadorm15", locked=False) text_style "modmybutton"
                    elif not futabadorm15 and not ev_futabadorm15.missed:
                        text _("Legs of a Dying Spider")

                    if library20 and show_complete:
                        textbutton _("Only Child {b}✓{/b}") action Replay("library20", locked=False) text_style "modmybutton"
                    elif not library20 and not ev_library20.missed:
                        text _("Only Child")

                    if library25 and show_complete:
                        textbutton _("A Book About Dragons {b}✓{/b}") action Replay("library25", locked=False) text_style "modmybutton"
                    elif not library25 and not ev_library25.missed:
                        text _("A Book About Dragons")

                    if futabadorm25 and show_complete:
                        textbutton _("Two Hours {b}✓{/b}") action Replay("futabadorm25", locked=False) text_style "modmybutton"
                    elif ev_futabadorm25.missed and show_complete:
                        text _("{color=EF1A1A}{s}I Just Want to Be Loved{/s}{/color}")
                    elif not futabadorm25 and not ev_futabadorm25.missed:
                        text _("Two Hours")

                    if day86 and show_complete:
                        textbutton _("Like Fucking a Cloud {b}✓{/b}") action Replay("day86", locked=False) text_style "modmybutton"
                    elif not day86 and not ev_day86.missed:
                        text _("{color=FF85FD}Like Fucking a Cloud{/color}")

                    if library30 and show_complete:
                        textbutton _("Under the Table {b}✓{/b}") action Replay("library30", locked=False) text_style "modmybutton"
                    elif not library30 and not ev_library30.missed:
                        text _("Under the Table")

                    if futabadorm30 and show_complete:
                        textbutton _("A Tree Falls in the Forest {b}✓{/b}") action Replay("futabadorm30", locked=False) text_style "modmybutton"
                    elif not futabadorm30 and not ev_futabadorm30.missed:
                        text _("A Tree Falls in the Forest")

                    if library35 and show_complete:
                        textbutton _("No, You {b}✓{/b}") action Replay("library35", locked=False) text_style "modmybutton"
                    elif not library35 and not ev_library35.missed:
                        text _("No, You")

                    if futabadorm35 and show_complete:
                        textbutton _("Overload {b}✓{/b}") action Replay("futabadorm35", locked=False) text_style "modmybutton"
                    elif not futabadorm35 and not ev_futabadorm35.missed:
                        text _("Overload")

                    text _("---------------------------------------------")

                    if futabalust10 and show_complete:
                        textbutton _("Selfless {b}✓{/b}") action Replay("futabalust10", locked=False) text_style "modmybutton"
                    elif ev_futabalust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Loveless{/s}{/color}")
                    elif not futabalust10 and not ev_futabalust10.missed:
                        text _("{color=FF85FD}Selfless{/color}")

                    if futabainvite1 and show_complete:
                        textbutton _("Sonnet 18 {b}✓{/b}") action Replay("futabainvite1", locked=False) text_style "modmybutton"
                    elif not futabainvite1 and not ev_futabainvite1.missed:
                        text _("{color=778EFF}Sonnet 18{/color}")

                    if futabainvite2 and show_complete:
                        textbutton _("Floral Aura {b}✓{/b}") action Replay("futabainvite2", locked=False) text_style "modmybutton"
                    elif not futabainvite2 and not ev_futabainvite2.missed:
                        text _("{color=778EFF}Floral Aura{/color}")

                    if futabalust15 and show_complete:
                        textbutton _("C'est La Vie {b}✓{/b}") action Replay("futabalust15", locked=False) text_style "modmybutton"
                    elif ev_futabalust15.missed and show_complete:
                        text _("{color=EF1A1A}{s}Mourir. Dormir.{/s}{/color}")
                    elif not futabalust15 and not ev_futabalust15.missed:
                        text _("{color=FF85FD}C'est La Vie{/color}")

                    if futabadorm40 and show_complete:
                        textbutton _("Skin (Start Somewhere) {b}✓{/b}") action Replay("futabadorm40", locked=False) text_style "modmybutton"
                    elif not futabadorm40 and not ev_futabadorm40.missed:
                        text _("Skin (Start Somewhere)")

                    if library40 and show_complete:
                        textbutton _("Shadowplay {b}✓{/b}") action Replay("library40", locked=False) text_style "modmybutton"
                    elif not library40 and not ev_library40.missed:
                        text _("Shadowplay")

                    if library40part2 and show_complete:
                        textbutton _("Without Running Away {b}✓{/b}") action Replay("library40part2", locked=False) text_style "modmybutton"
                    elif not library40part2 and not ev_library40part2.missed:
                        text _("Without Running Away")

                    if futabadorm45 and show_complete:
                        textbutton _("Hall of Mirrors {b}✓{/b}") action Replay("futabadorm45", locked=False) text_style "modmybutton"
                    elif not futabadorm45 and not ev_futabadorm45.missed:
                        text _("Hall of Mirrors")

                    text _("---------------------------------------------")

                    if futabadorm50 and show_complete:
                        textbutton _("This Infected Wound {b}✓{/b}") action Replay("futabadorm50", locked=False) text_style "modmybutton"
                    elif not futabadorm50 and not ev_futabadorm50.missed:
                        text _("This Infected Wound")

                    if library50 and show_complete:
                        textbutton _("Bestial Vigor {b}✓{/b}") action Replay("library50", locked=False) text_style "modmybutton"
                    elif not library50 and not ev_library50.missed:
                        text _("Bestial Vigor")

                    if futabainvite3 and show_complete:
                        textbutton _("Too Blind To See {b}✓{/b}") action Replay("futabainvite3", locked=False) text_style "modmybutton"
                    elif not futabainvite3 and not ev_futabainvite3.missed:
                        text _("{color=778EFF}Too Blind To See{/color}")

                    if makotofutabafuntimelustevent and show_complete:
                        textbutton _("Toys {b}✓{/b}") action Replay("makotofutabafuntimelustevent", locked=False) text_style "modmybutton"
                    elif ev_makotofutabafuntimelustevent.missed and show_complete:
                        text _("{color=EF1A1A}{s}Grounded{/s}{/color}")
                    elif not makotofutabafuntimelustevent and not ev_makotofutabafuntimelustevent.missed:
                        text _("{color=FF85FD}Toys{/color}")

                    if futabaspecial60p1 and show_complete:
                        textbutton _("Book Burning {b}✓{/b}") action Replay("futabaspecial60p1", locked=False) text_style "modmybutton"
                    elif not futabaspecial60p1 and not ev_futabaspecial60p1.missed:
                        text _("Book Burning")

                    if futabaspecial60p2 and show_complete:
                        textbutton _("Pg. 99 {b}✓{/b}") action Replay("futabaspecial60p2", locked=False) text_style "modmybutton"
                    elif not futabaspecial60p2 and not ev_futabaspecial60p2.missed:
                        text _("Pg. 99")

                    if futabaspecial60p3 and show_complete:
                        textbutton _("Fish Eyes {b}✓{/b}") action Replay("futabaspecial60p3", locked=False) text_style "modmybutton"
                    elif not futabaspecial60p3 and not ev_futabaspecial60p3.missed:
                        text _("Fish Eyes")

                    text _("---------------------------------------------")

                    if futabalust25 and show_complete:
                        textbutton _("Weapons of Mass Destruction {b}✓{/b}") action Replay("futabalust25", locked=False) text_style "modmybutton"
                    elif not futabalust25 and not ev_futabalust25.missed:
                        text _("{color=FF85FD}Weapons of Mass Destruction{/color}")

                    if futabaspring1 and show_complete:
                        textbutton _("My Curse {b}✓{/b}") action Replay("futabaspring1", locked=False) text_style "modmybutton"
                    elif not futabaspring1 and not ev_futabaspring1.missed:
                        text _("My Curse")

                    if beachfive9 and show_complete:
                        textbutton _("Transpacific Sadness Symposium II: SISTER SOFTSKIN {b}✓{/b}") action Replay("beachfive9", locked=False) text_style "modmybutton"
                    elif not beachfive9 and not ev_beachfive9.missed:
                        text _("Transpacific Sadness Symposium II: SISTER SOFTSKIN")

                    if futabalust40 and show_complete:
                        textbutton _("The Meat in the Hole in the Wall in My Room {b}✓{/b}") action Replay("futabalust40", locked=False) text_style "modmybutton"
                    elif ev_futabalust40.missed and show_complete:
                        text _("{color=EF1A1A}{s}Maisie Belle{/s}{/color}")
                    elif not futabalust40 and not ev_futabalust40.missed:
                        text _("{color=FF85FD}The Meat in the Hole in the Wall in My Room{/color}")

                    if futabaspring2 and show_complete:
                        textbutton _("The Taking Tree {b}✓{/b}") action Replay("futabaspring2", locked=False) text_style "modmybutton"
                    elif not futabaspring2 and not ev_futabaspring2.missed:
                        text _("The Taking Tree")

                    if beachsixfutaba1 and show_complete:
                        textbutton _("Spam {b}✓{/b}") action Replay("beachsixfutaba1", locked=False) text_style "modmybutton"
                    elif not beachsixfutaba1 and not ev_beachsixfutaba1.missed:
                        text _("Spam")

                    if futabaspring3 and show_complete:
                        textbutton _("ELATION PROTOCOL 99: RE:SOLUTION (RESOLVED) {b}✓{/b}") action Replay("futabaspring3", locked=False) text_style "modmybutton"
                    elif not futabaspring3 and not ev_futabaspring3.missed:
                        text _("ELATION PROTOCOL 99: RE:SOLUTION (RESOLVED)")

                    if futabaspring4 and show_complete:
                        textbutton _("New Ways to Love {b}✓{/b}") action Replay("futabaspring4", locked=False) text_style "modmybutton"
                    elif not futabaspring4 and not ev_futabaspring4.missed:
                        text _("New Ways to Love")

                #HARUKAEVENT

                if showgirl == "Haruka":

                    if harukadate1 and show_complete:
                        textbutton _("Drunk Again {b}✓{/b}") action Replay("harukadate1", locked=False) text_style "modmybutton"
                    elif not harukadate1 and not ev_harukadate1.missed:
                        text _("Drunk Again")

                    if harukadate5 and show_complete:
                        textbutton _("Invisible Worm {b}✓{/b}") action Replay("harukadate5", locked=False) text_style "modmybutton"
                    elif not harukadate5 and not ev_harukadate5.missed:
                        text _("Invisible Worm")

                    if harukafirstlust and show_complete:
                        textbutton _("The Need to be Hurt {b}✓{/b}") action Replay("harukafirstlust", locked=False) text_style "modmybutton"
                    elif ev_harukafirstlust.missed and show_complete:
                        text _("{color=EF1A1A}{s}Hurt Me{/s}{/color}")
                    elif not harukafirstlust and not ev_harukafirstlust.missed:
                        text _("{color=FF85FD}The Need to be Hurt{/color}")

                    if harukalust10 and show_complete:
                        textbutton _("Bad Kitty {b}✓{/b}") action Replay("harukalust10", locked=False) text_style "modmybutton"
                    elif ev_harukalust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Fixing Pipes{/s}{/color}")
                    elif not harukalust10 and not ev_harukalust10.missed:
                        text _("{color=FF85FD}Bad Kitty{/color}")

                    if harukadate10 and show_complete:
                        textbutton _("Performance Review {b}✓{/b}") action Replay("harukadate10", locked=False) text_style "modmybutton"
                    elif not harukadate10 and not ev_harukadate10.missed:
                        text _("Performance Review")

                    if harukadate15 and show_complete:
                        textbutton _("Watching TV Alone {b}✓{/b}") action Replay("harukadate15", locked=False) text_style "modmybutton"
                    elif not harukadate15 and not ev_harukadate15.missed:
                        text _("Watching TV Alone")

                    text _("---------------------------------------------")

                    if harukainvite1 and show_complete:
                        textbutton _("Shades of Green {b}✓{/b}") action Replay("harukainvite1", locked=False) text_style "modmybutton"
                    elif not harukainvite1 and not ev_harukainvite1.missed:
                        text _("{color=778EFF}Shades of Green{/color}")

                    if harukainvite2 and show_complete:
                        textbutton _("Roses {b}✓{/b}") action Replay("harukainvite2", locked=False) text_style "modmybutton"
                    elif not harukainvite2 and not ev_harukainvite2.missed:
                        text _("{color=778EFF}Roses{/color}")

                    if harukadate20 and show_complete:
                        textbutton _("Sober-ish {b}✓{/b}") action Replay("harukadate20", locked=False) text_style "modmybutton"
                    elif not harukadate20 and not ev_harukadate20.missed:
                        text _("Sober-ish")

                    if harukainvite3 and show_complete:
                        textbutton _("Unfiltered Tap Water {b}✓{/b}") action Replay("harukainvite3", locked=False) text_style "modmybutton"
                    elif ev_harukainvite3.missed and show_complete:
                        text _("{color=EF1A1A}{s}Worms{/s}{/color}")
                    elif not harukainvite3 and not ev_harukainvite3.missed:
                        text _("{color=778EFF}Unfiltered Tap Water{/color}")

                    text _("---------------------------------------------")

                    if sadgirls2 and show_complete:
                        textbutton _("The World Outside The Walls {b}✓{/b}") action Replay("sadgirls2", locked=False) text_style "modmybutton"
                    elif ev_sadgirls2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Personal Hell{/s}{/color}")
                    elif not sadgirls2 and not ev_sadgirls2.missed:
                        text _("The World Outside The Walls")

                    if sadgirls4 and show_complete:
                        textbutton _("To Anyone Who Passes By {b}✓{/b}") action Replay("sadgirls4", locked=False) text_style "modmybutton"
                    elif not sadgirls4 and not ev_sadgirls4.missed:
                        text _("To Anyone Who Passes By")

                    if sadgirls5 and show_complete:
                        textbutton _("Again, I Can't Recall {b}✓{/b}") action Replay("sadgirls5", locked=False) text_style "modmybutton"
                    elif not sadgirls5 and not ev_sadgirls5.missed:
                        text _("Again, I Can't Recall")

                    if harukalust25 and show_complete:
                        textbutton _("Secret Weapon {b}✓{/b}") action Replay("harukalust25", locked=False) text_style "modmybutton"
                    elif ev_harukalust25.missed and show_complete:
                        text _("{color=EF1A1A}{s}Fatal Misfire{/s}{/color}")
                    elif not harukalust25 and not ev_harukalust25.missed:
                        text _("{color=FF85FD}Secret Weapon{/color}")

                    if makihornytrip1 and show_complete:
                        textbutton _("Stress Level Midnight {b}✓{/b}") action Replay("makihornytrip1", locked=False) text_style "modmybutton"
                    elif not makihornytrip1 and not ev_makihornytrip1.missed:
                        text _("Stress Level Midnight")

                    if makihornytrip4 and show_complete:
                        textbutton _("Conflict of Interest {b}✓{/b}") action Replay("makihornytrip4", locked=False) text_style "modmybutton"
                    elif not makihornytrip4 and not ev_makihornytrip4.missed:
                        text _("Conflict of Interest")

                    if harukadate30 and show_complete:
                        textbutton _("Scum {b}✓{/b}") action Replay("harukadate30", locked=False) text_style "modmybutton"
                    elif ev_harukadate30.missed and show_complete:
                        text _("{color=EF1A1A}{s}Soap{/s}{/color}")
                    elif not harukadate30 and not ev_harukadate30.missed:
                        text _("Scum")

                    text _("---------------------------------------------")

                    if harukacamp1 and show_complete:
                        textbutton _("Small Paper Cups {b}✓{/b}") action Replay("harukacamp1", locked=False) text_style "modmybutton"
                    elif not harukacamp1 and not ev_harukacamp1.missed:
                        text _("Small Paper Cups")

                    if harukaspring1 and show_complete:
                        textbutton _("Subhuman {b}✓{/b}") action Replay("harukaspring1", locked=False) text_style "modmybutton"
                    elif ev_harukaspring1.missed and show_complete:
                        text _("{color=EF1A1A}{s}Crisis Averted!{/s}{/color}")
                    elif not harukaspring1 and not ev_harukaspring1.missed:
                        text _("Subhuman")

                    if harukaspring2 and show_complete:
                        textbutton _("Limp-Dicked Loser {b}✓{/b}") action Replay("harukaspring2", locked=False) text_style "modmybutton"
                    elif ev_harukaspring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Open For Business!{/s}{/color}")
                    elif not harukaspring2 and not ev_harukaspring2.missed:
                        text _("Limp-Dicked Loser")

                    if harukaspring3 and show_complete:
                        textbutton _("This Town, On its Knees {b}✓{/b}") action Replay("harukaspring3", locked=False) text_style "modmybutton"
                    elif ev_harukaspring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Ballad of Tebiso{/s}{/color}")
                    elif not harukaspring3 and not ev_harukaspring3.missed:
                        text _("This Town, On its Knees")

                    if harukaspring4 and show_complete:
                        textbutton _("JR East's DC Tilting EMU E353 Series (Kaiji) {b}✓{/b}") action Replay("harukaspring4", locked=False) text_style "modmybutton"
                    elif not harukaspring4 and not ev_harukaspring4.missed:
                        text _("JR East's DC Tilting EMU E353 Series (Kaiji)")

                    if harukachristmalloween1 and show_complete:
                        textbutton _("Traitor's Mark {b}✓{/b}") action Replay("harukachristmalloween1", locked=False) text_style "modmybutton"
                    elif ev_harukachristmalloween1.missed and show_complete:
                        text _("{color=EF1A1A}{s}Cattlebrand{/s}{/color}")
                    elif not harukachristmalloween1 and not ev_harukachristmalloween1.missed:
                        text _("Traitor's Mark")

                    if harukachristmalloween2 and show_complete:
                        textbutton _("Blood in the Water {b}✓{/b}") action Replay("harukachristmalloween2", locked=False) text_style "modmybutton"
                    elif ev_harukachristmalloween2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Mola Mola{/s}{/color}")
                    elif not harukachristmalloween2 and not ev_harukachristmalloween2.missed:
                        text _("Blood in the Water")

                    if harukaspring5 and show_complete:
                        textbutton _("Ancient Dragons {b}✓{/b}") action Replay("harukaspring5", locked=False) text_style "modmybutton"
                    elif ev_harukaspring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}Crumbled Golem{/s}{/color}")
                    elif not harukaspring5 and not ev_harukaspring5.missed:
                        text _("Ancient Dragons")

                    if harukaspring6 and show_complete:
                        textbutton _("Camelopardalis (At Hoshimachi Station) {b}✓{/b}") action Replay("harukaspring6", locked=False) text_style "modmybutton"
                    elif ev_harukaspring6.missed and show_complete:
                        text _("{color=EF1A1A}{s}Caelum’s Cancer{/s}{/color}")
                    elif not harukaspring6 and not ev_harukaspring6.missed:
                        text _("Camelopardalis (At Hoshimachi Station)")

                #IMANIEVENT

                if showgirl == "Imani":

                    if imanidate1 and show_complete:
                        textbutton _("Somewhere I Belong {b}✓{/b}") action Replay("imanidate1", locked=False) text_style "modmybutton"
                    elif not imanidate1 and not ev_imanidate1.missed:
                        text _("Somewhere I Belong")

                    if imanidate5 and show_complete:
                        textbutton _("A Hairline Fracture {b}✓{/b}") action Replay("imanidate5", locked=False) text_style "modmybutton"
                    elif not imanidate5 and not ev_imanidate5.missed:
                        text _("A Hairline Fracture")

                    if imanidate15p1 and show_complete:
                        textbutton _("Knotted Up {b}✓{/b}") action Replay("imanidate15p1", locked=False) text_style "modmybutton"
                    elif not imanidate15p1 and not ev_imanidate15p1.missed:
                        text _("Knotted Up")

                    if imanidate15p2 and show_complete:
                        textbutton _("Arm's Length {b}✓{/b}") action Replay("imanidate15p2", locked=False) text_style "modmybutton"
                    elif not imanidate15p2 and not ev_imanidate15p2.missed:
                        text _("Arm's Length")

                    if imanispecial15 and show_complete:
                        textbutton _("Debbie Downer {b}✓{/b}") action Replay("imanispecial15", locked=False) text_style "modmybutton"
                    elif not imanispecial15 and not ev_imanispecial15.missed:
                        text _("Debbie Downer")

                    text _("---------------------------------------------")

                    if imanispring1 and show_complete:
                        textbutton _("Antoa Suo Nyamaa {b}✓{/b}") action Replay("imanispring1", locked=False) text_style "modmybutton"
                    elif not imanispring1 and not ev_imanispring1.missed:
                        text _("Antoa Suo Nyamaa")

                    if imanispring2 and show_complete:
                        textbutton _("I Will Carry You, My Light {b}✓{/b}") action Replay("imanispring2", locked=False) text_style "modmybutton"
                    elif not imanispring2 and not ev_imanispring2.missed:
                        text _("I Will Carry You, My Light")

                    if christmasimani1 and show_complete:
                        textbutton _("Yehoshua {b}✓{/b}") action Replay("christmasimani1", locked=False) text_style "modmybutton"
                    elif not christmasimani1 and not ev_christmasimani1.missed:
                        text _("Yehoshua")

                    if christmasimani2 and show_complete:
                        textbutton _("The Truman Show {b}✓{/b}") action Replay("christmasimani2", locked=False) text_style "modmybutton"
                    elif not christmasimani2 and not ev_christmasimani2.missed:
                        text _("The Truman Show")

                    if christmasimani3 and show_complete:
                        textbutton _("Now & Forever {b}✓{/b}") action Replay("christmasimani3", locked=False) text_style "modmybutton"
                    elif not christmasimani3 and not ev_christmasimani3.missed:
                        text _("Now & Forever")

                    if imanilust5 and show_complete:
                        textbutton _("The Devil's Bed {b}✓{/b}") action Replay("imanilust5", locked=False) text_style "modmybutton"
                    elif not imanilust5 and not ev_imanilust5.missed:
                        text _("{color=FF85FD}The Devil's Bed{/color}")

                    if imanispring3 and show_complete:
                        textbutton _("Lesbian Hand Stuff {b}✓{/b}") action Replay("imanispring3", locked=False) text_style "modmybutton"
                    elif not imanispring3 and not ev_imanispring3.missed:
                        text _("Lesbian Hand Stuff")

                    if imanispring4 and show_complete:
                        textbutton _("Lost in the Sauce (Pied Piper) {b}✓{/b}") action Replay("imanispring4", locked=False) text_style "modmybutton"
                    elif not imanispring4 and not ev_imanispring4.missed:
                        text _("Lost in the Sauce (Pied Piper)")

                #IOEVENT

                if showgirl == "Io":

                    if iofirsthall and show_complete:
                        textbutton _("Viva la Revolución {b}✓{/b}") action Replay("iofirsthall", locked=False) text_style "modmybutton"
                    elif not iofirsthall and not ev_iofirsthall.missed:
                        text _("Viva la Revolución")

                    if bathhouse1 and show_complete:
                        textbutton _("Nonetheless, I'm Here {b}✓{/b}") action Replay("bathhouse1", locked=False) text_style "modmybutton"
                    elif not bathhouse1 and not ev_bathhouse1.missed:
                        text _("Nonetheless, I'm Here")

                    if bathhouse5 and show_complete:
                        textbutton _("The Girl with the Dragon Tattoo {b}✓{/b}") action Replay("bathhouse5", locked=False) text_style "modmybutton"
                    elif not bathhouse5 and not ev_bathhouse5.missed:
                        text _("The Girl with the Dragon Tattoo")

                    if iodorm5 and show_complete:
                        textbutton _("Unnamed Wooden Robots {b}✓{/b}") action Replay("iodorm5", locked=False) text_style "modmybutton"
                    elif not iodorm5 and not ev_iodorm5.missed:
                        text _("Unnamed Wooden Robots")

                    if iodorm10 and show_complete:
                        textbutton _("Paperthin {b}✓{/b}") action Replay("iodorm10", locked=False) text_style "modmybutton"
                    elif not iodorm10 and not ev_iodorm10.missed:
                        text _("Paperthin")

                    if bathhouse10 and show_complete:
                        textbutton _("Turn On The Lights {b}✓{/b}") action Replay("bathhouse10", locked=False) text_style "modmybutton"
                    elif not bathhouse10 and not ev_bathhouse10.missed:
                        text _("Turn On The Lights")

                    if iodorm15 and show_complete:
                        textbutton _("Amongst Other Things {b}✓{/b}") action Replay("iodorm15", locked=False) text_style "modmybutton"
                    elif not iodorm15 and not ev_iodorm15.missed:
                        text _("Amongst Other Things")

                    if bathhouse20 and show_complete:
                        textbutton _("One Man's Trash {b}✓{/b}") action Replay("bathhouse20", locked=False) text_style "modmybutton"
                    elif not bathhouse20 and not ev_bathhouse20.missed:
                        text _("One Man's Trash")

                    if bathhouse20part2 and show_complete:
                        textbutton _("Another Man's Treasure {b}✓{/b}") action Replay("bathhouse20part2", locked=False) text_style "modmybutton"
                    elif not bathhouse20part2 and not ev_bathhouse20part2.missed:
                        text _("Another Man's Treasure")

                    text _("---------------------------------------------")

                    if ioarchery1 and show_complete:
                        textbutton _("Cupid's Arrow {b}✓{/b}") action Replay("ioarchery1", locked=False) text_style "modmybutton"
                    elif not ioarchery1 and not ev_ioarchery1.missed:
                        text _("Cupid's Arrow")

                    if bathhouse25 and show_complete:
                        textbutton _("Work Less, Not Hard {b}✓{/b}") action Replay("bathhouse25", locked=False) text_style "modmybutton"
                    elif not bathhouse25 and not ev_bathhouse25.missed:
                        text _("Work Less, Not Hard")

                    if iodorm25 and show_complete:
                        textbutton _("Heartbreak & Harmony {b}✓{/b}") action Replay("iodorm25", locked=False) text_style "modmybutton"
                    elif not iodorm25 and not ev_iodorm25.missed:
                        text _("Heartbreak & Harmony")

                    if iospecial30 and show_complete:
                        textbutton _("1999 PC Classic, Rollercoaster Tycoon {b}✓{/b}") action Replay("iospecial30", locked=False) text_style "modmybutton"
                    elif not iospecial30 and not ev_iospecial30.missed:
                        text _("1999 PC Classic, Rollercoaster Tycoon")

                    if bathhouse35p1 and show_complete:
                        textbutton _("Tennis Ball {b}✓{/b}") action Replay("bathhouse35p1", locked=False) text_style "modmybutton"
                    elif not bathhouse35p1 and not ev_bathhouse35p1.missed:
                        text _("Tennis Ball")

                    if bathhouse35p2 and show_complete:
                        textbutton _("Hold You Over {b}✓{/b}") action Replay("bathhouse35p2", locked=False) text_style "modmybutton"
                    elif not bathhouse35p2 and not ev_bathhouse35p2.missed:
                        text _("Hold You Over")

                    if iodorm35 and show_complete:
                        textbutton _("Yellow Cactus Flower {b}✓{/b}") action Replay("iodorm35", locked=False) text_style "modmybutton"
                    elif not iodorm35 and not ev_iodorm35.missed:
                        text _("Yellow Cactus Flower")

                    if ioarchery35 and show_complete:
                        textbutton _("Two Of Us Are Thinking {b}✓{/b}") action Replay("ioarchery35", locked=False) text_style "modmybutton"
                    elif not ioarchery35 and not ev_ioarchery35.missed:
                        text _("Two Of Us Are Thinking")

                    text _("---------------------------------------------")

                    if iospring1 and show_complete:
                        textbutton _("My Indigo (The Blue Death) {b}✓{/b}") action Replay("iospring1", locked=False) text_style "modmybutton"
                    elif not iospring1 and not ev_iospring1.missed:
                        text _("My Indigo (The Blue Death)")

                    if iospring2 and show_complete:
                        textbutton _("Komorebi {b}✓{/b}") action Replay("iospring2", locked=False) text_style "modmybutton"
                    elif not iospring2 and not ev_iospring2.missed:
                        text _("Komorebi")

                    if iospring3 and show_complete:
                        textbutton _("Stomachache {b}✓{/b}") action Replay("iospring3", locked=False) text_style "modmybutton"
                    elif ev_iospring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}Dress-Up{/s}{/color}")
                    elif not iospring3 and not ev_iospring3.missed:
                        text _("Stomachache")

                    if iospring4 and show_complete:
                        textbutton _("1997 PC Classic, Theme Hospital {b}✓{/b}") action Replay("iospring4", locked=False) text_style "modmybutton"
                    elif not iospring4 and not ev_iospring4.missed:
                        text _("1997 PC Classic, Theme Hospital")

                    if iospring5 and show_complete:
                        textbutton _("Even Winning Feels Bad {b}✓{/b}") action Replay("iospring5", locked=False) text_style "modmybutton"
                    elif not iospring5 and not ev_iospring5.missed:
                        text _("Even Winning Feels Bad")

                    if dormwarsfiveio1 and show_complete:
                        textbutton _("Endless Black (Sea of Nothing) {b}✓{/b}") action Replay("dormwarsfiveio1", locked=False) text_style "modmybutton"
                    elif not dormwarsfiveio1 and not ev_dormwarsfiveio1.missed:
                        text _("Endless Black (Sea of Nothing)")

                    if iospring6 and show_complete:
                        textbutton _("Man-Meat {b}✓{/b}") action Replay("iospring6", locked=False) text_style "modmybutton"
                    elif not iospring6 and not ev_iospring6.missed:
                        text _("Man-Meat")

                    if iospring7 and show_complete:
                        textbutton _("Animal Cruelty {b}✓{/b}") action Replay("iospring7", locked=False) text_style "modmybutton"
                    elif ev_iospring7.missed and show_complete:
                        text _("{color=EF1A1A}{s}Joining PETA{/s}{/color}")
                    elif not iospring7 and not ev_iospring7.missed:
                        text _("Animal Cruelty")

                    if iospring8 and show_complete:
                        textbutton _("The Hatchery {b}✓{/b}") action Replay("iospring8", locked=False) text_style "modmybutton"
                    elif not iospring8 and not ev_iospring8.missed:
                        text _("The Hatchery")

                #KAORIEVENT

                if showgirl == "Kaori":

                    if kaoridate1 and show_complete:
                        textbutton _("How to Date a Human {b}✓{/b}") action Replay("kaoridate1", locked=False) text_style "modmybutton"
                    elif not kaoridate1 and not ev_kaoridate1.missed:
                        text _("How to Date a Human")

                    if kaoridate5 and show_complete:
                        textbutton _("The Best Ways to Rub a Cock {b}✓{/b}") action Replay("kaoridate5", locked=False) text_style "modmybutton"
                    elif not kaoridate5 and not ev_kaoridate5.missed:
                        text _("The Best Ways to Rub a Cock")

                    if kaoridate10 and show_complete:
                        textbutton _("Objects and Appendages {b}✓{/b}") action Replay("kaoridate10", locked=False) text_style "modmybutton"
                    elif not kaoridate10 and not ev_kaoridate10.missed:
                        text _("Objects and Appendages")

                    text _("---------------------------------------------")

                    if kaoridate15 and show_complete:
                        textbutton _("To Die, To Sleep {b}✓{/b}") action Replay("kaoridate15", locked=False) text_style "modmybutton"
                    elif not kaoridate15 and not ev_kaoridate15.missed:
                        text _("To Die, To Sleep")

                    if kaoridate15p2 and show_complete:
                        textbutton _("Sad Girl Special {b}✓{/b}") action Replay("kaoridate15p2", locked=False) text_style "modmybutton"
                    elif not kaoridate15p2 and not ev_kaoridate15p2.missed:
                        text _("Sad Girl Special")

                    if kaoridate15p3 and show_complete:
                        textbutton _("Clouds {b}✓{/b}") action Replay("kaoridate15p3", locked=False) text_style "modmybutton"
                    elif not kaoridate15p3 and not ev_kaoridate15p3.missed:
                        text _("Clouds")

                    if kaoridate20 and show_complete:
                        textbutton _("Såsom i en Spegel {b}✓{/b}") action Replay("kaoridate20", locked=False) text_style "modmybutton"
                    elif not kaoridate20 and not ev_kaoridate20.missed:
                        text _("Såsom i en Spegel")

                    if kaoridate25 and show_complete:
                        textbutton _("Wither {b}✓{/b}") action Replay("kaoridate25", locked=False) text_style "modmybutton"
                    elif not kaoridate25 and not ev_kaoridate25.missed:
                        text _("Wither")

                    text _("---------------------------------------------")

                    if kaorispecial35 and show_complete:
                        textbutton _("Where the Trees Live {b}✓{/b}") action Replay("kaorispecial35", locked=False) text_style "modmybutton"
                    elif not kaorispecial35 and not ev_kaorispecial35.missed:
                        text _("Where the Trees Live")

                    if kaorispecial40 and show_complete:
                        textbutton _("Human Females {b}✓{/b}") action Replay("kaorispecial40", locked=False) text_style "modmybutton"
                    elif not kaorispecial40 and not ev_kaorispecial40.missed:
                        text _("Human Females")

                    if kaoridate40 and show_complete:
                        textbutton _("Run, Rabbit, Run (Why the Fieldmice Hide) {b}✓{/b}") action Replay("kaoridate40", locked=False) text_style "modmybutton"
                    elif not kaoridate40 and not ev_kaoridate40.missed:
                        text _("Run, Rabbit, Run (Why the Fieldmice Hide)")

                    text _("---------------------------------------------")

                    if kaoricamp1 and show_complete:
                        textbutton _("Tree Village (The Color Machine) {b}✓{/b}") action Replay("kaoricamp1", locked=False) text_style "modmybutton"
                    elif not kaoricamp1 and not ev_kaoricamp1.missed:
                        text _("Tree Village (The Color Machine)")

                    if kaoricamp2 and show_complete:
                        textbutton _("Il Cervo {b}✓{/b}") action Replay("kaoricamp2", locked=False) text_style "modmybutton"
                    elif not kaoricamp2 and not ev_kaoricamp2.missed:
                        text _("Il Cervo")

                    if halloweenkaori1 and show_complete:
                        textbutton _("Friend {b}✓{/b}") action Replay("halloweenkaori1", locked=False) text_style "modmybutton"
                    elif not halloweenkaori1 and not ev_halloweenkaori1.missed:
                        text _("Friend")

                    if halloweenkaori2 and show_complete:
                        textbutton _("Kittens {b}✓{/b}") action Replay("halloweenkaori2", locked=False) text_style "modmybutton"
                    elif not halloweenkaori2 and not ev_halloweenkaori2.missed:
                        text _("Kittens")

                    if kaorispring1 and show_complete:
                        textbutton _("Seas of White (Why Not Here?) {b}✓{/b}") action Replay("kaorispring1", locked=False) text_style "modmybutton"
                    elif not kaorispring1 and not ev_kaorispring1.missed:
                        text _("Seas of White (Why Not Here?)")

                    if kaorispring2 and show_complete:
                        textbutton _("Clearer Skies & Changing Eyes {b}✓{/b}") action Replay("kaorispring2", locked=False) text_style "modmybutton"
                    elif not kaorispring2 and not ev_kaorispring2.missed:
                        text _("Clearer Skies & Changing Eyes")

                    if kaorispring3 and show_complete:
                        textbutton _("Breeding Material {b}✓{/b}") action Replay("kaorispring3", locked=False) text_style "modmybutton"
                    elif not kaorispring3 and not ev_kaorispring3.missed:
                        text _("Breeding Material")

                    if kaoriinvite1 and show_complete:
                        textbutton _("Borrowed Flesh {b}✓{/b}") action Replay("kaoriinvite1", locked=False) text_style "modmybutton"
                    elif not kaoriinvite1 and not ev_kaoriinvite1.missed:
                        text _("{color=778EFF}Borrowed Flesh{/color}")

                    if kaoriinvite2 and show_complete:
                        textbutton _("Scatter the Ashes {b}✓{/b}") action Replay("kaoriinvite2", locked=False) text_style "modmybutton"
                    elif not kaoriinvite2 and not ev_kaoriinvite2.missed:
                        text _("{color=778EFF}Scatter the Ashes{/color}")

                #KARINEVENT

                if showgirl == "Karin":

                    if karindate1 and show_complete:
                        textbutton _("Further and Further {b}✓{/b}") action Replay("karindate1", locked=False) text_style "modmybutton"
                    elif not karindate1 and not ev_karindate1.missed:
                        text _("Further and Further")

                    if karindate5 and show_complete:
                        textbutton _("Walking Penis Monster {b}✓{/b}") action Replay("karindate5", locked=False) text_style "modmybutton"
                    elif not karindate5 and not ev_karindate5.missed:
                        text _("Walking Penis Monster")

                    if karindate10 and show_complete:
                        textbutton _("If Only {b}✓{/b}") action Replay("karindate10", locked=False) text_style "modmybutton"
                    elif not karindate10 and not ev_karindate10.missed:
                        text _("If Only")

                    text _("---------------------------------------------")

                    if karindate15 and show_complete:
                        textbutton _("Dying Alone With Ten Cats {b}✓{/b}") action Replay("karindate15", locked=False) text_style "modmybutton"
                    elif ev_karindate15.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Price of Honesty{/s}{/color}")
                    elif not karindate15 and not ev_karindate15.missed:
                        text _("Dying Alone With Ten Cats")

                    if karinsoccer15 and show_complete:
                        textbutton _("Tendrils of Flame {b}✓{/b}") action Replay("karinsoccer15", locked=False) text_style "modmybutton"
                    elif not karinsoccer15 and not ev_karinsoccer15.missed:
                        text _("Tendrils of Flame")

                    if karinsoccer20 and show_complete:
                        textbutton _("The Adventures of Karli & Steve {b}✓{/b}") action Replay("karinsoccer20", locked=False) text_style "modmybutton"
                    elif not karinsoccer20 and not ev_karinsoccer20.missed:
                        text _("The Adventures of Karli & Steve")

                    if karindate20 and show_complete:
                        textbutton _("Sweet Tooth {b}✓{/b}") action Replay("karindate20", locked=False) text_style "modmybutton"
                    elif not karindate20 and not ev_karindate20.missed:
                        text _("Sweet Tooth")

                    text _("---------------------------------------------")

                    if karindate25 and show_complete:
                        textbutton _("Emerald Eyes {b}✓{/b}") action Replay("karindate25", locked=False) text_style "modmybutton"
                    elif not karindate25 and not ev_karindate25.missed:
                        text _("Emerald Eyes")

                    if karindate30 and show_complete:
                        textbutton _("Wrong Places/Wrong Times {b}✓{/b}") action Replay("karindate30", locked=False) text_style "modmybutton"
                    elif not karindate30 and not ev_karindate30.missed:
                        text _("Wrong Places/Wrong Times")

                    text _("---------------------------------------------")

                    if karinspring1 and show_complete:
                        textbutton _("Touch of Grey {b}✓{/b}") action Replay("karinspring1", locked=False) text_style "modmybutton"
                    elif not karinspring1 and not ev_karinspring1.missed:
                        text _("Touch of Grey")

                    if karinspring2 and show_complete:
                        textbutton _("Paranoid {b}✓{/b}") action Replay("karinspring2", locked=False) text_style "modmybutton"
                    elif not karinspring2 and not ev_karinspring2.missed:
                        text _("Paranoid")

                    if karinspring3 and show_complete:
                        textbutton _("Better Boy {b}✓{/b}") action Replay("karinspring3", locked=False) text_style "modmybutton"
                    elif not karinspring3 and not ev_karinspring3.missed:
                        text _("Better Boy")

                    if karinspring4 and show_complete:
                        textbutton _("Back to the Basics {b}✓{/b}") action Replay("karinspring4", locked=False) text_style "modmybutton"
                    elif not karinspring4 and not ev_karinspring4.missed:
                        text _("Back to the Basics")

                    if karinspring5 and show_complete:
                        textbutton _("A Trip to Uzbekistan {b}✓{/b}") action Replay("karinspring5", locked=False) text_style "modmybutton"
                    elif not karinspring5 and not ev_karinspring5.missed:
                        text _("A Trip to Uzbekistan")

                    if karinspring6 and show_complete:
                        textbutton _("Top 10 Thoughts to Think {b}✓{/b}") action Replay("karinspring6", locked=False) text_style "modmybutton"
                    elif not karinspring6 and not ev_karinspring6.missed:
                        text _("Top 10 Thoughts to Think")

                    if karinspring7 and show_complete:
                        textbutton _("Oatmeal Raisin {b}✓{/b}") action Replay("karinspring7", locked=False) text_style "modmybutton"
                    elif ev_karinspring7.missed and show_complete:
                        text _("{color=EF1A1A}{s}Burnt Chocolate{/s}{/color}")
                    elif not karinspring7 and not ev_karinspring7.missed:
                        text _("Oatmeal Raisin")

                #KIRINEVENT

                if showgirl == "Kirin":

                    if kirindate1 and show_complete:
                        textbutton _("Partners in Crime {b}✓{/b}") action Replay("kirindate1", locked=False) text_style "modmybutton"
                    elif not kirindate1 and not ev_kirindate1.missed:
                        text _("Partners in Crime")

                    if kirindate5 and show_complete:
                        textbutton _("Long and Hard {b}✓{/b}") action Replay("kirindate5", locked=False) text_style "modmybutton"
                    elif not kirindate5 and not ev_kirindate5.missed:
                        text _("Long and Hard")

                    if kirindate10 and show_complete:
                        textbutton _("Politics! Pleasure! Ponies! {b}✓{/b}") action Replay("kirindate10", locked=False) text_style "modmybutton"
                    elif not kirindate10 and not ev_kirindate10.missed:
                        text _("Politics! Pleasure! Ponies!")

                    text _("---------------------------------------------")

                    if kirinlust5 and show_complete:
                        textbutton _("Full Blossom {b}✓{/b}") action Replay("kirinlust5", locked=False) text_style "modmybutton"
                    elif not kirinlust5 and not ev_kirinlust5.missed:
                        text _("{color=FF85FD}Full Blossom{/color}")

                    if kirininvite1 and show_complete:
                        textbutton _("Too Much, All at Once {b}✓{/b}") action Replay("kirininvite1", locked=False) text_style "modmybutton"
                    elif not kirininvite1 and not ev_kirininvite1.missed:
                        text _("{color=778EFF}Too Much, All at Once{/color}")

                    if kirininvite2 and show_complete:
                        textbutton _("No Extortion Necessary {b}✓{/b}") action Replay("kirininvite2", locked=False) text_style "modmybutton"
                    elif not kirininvite2 and not ev_kirininvite2.missed:
                        text _("{color=778EFF}No Extortion Necessary{/color}")

                    if kirinfirsthall and show_complete:
                        textbutton _("Morals vs. Orgasms {b}✓{/b}") action Replay("kirinfirsthall", locked=False) text_style "modmybutton"
                    elif not kirinfirsthall and not ev_kirinfirsthall.missed:
                        text _("Morals vs. Orgasms")

                    if kirindorm10 and show_complete:
                        textbutton _("Love, Dorms, and Other Things {b}✓{/b}") action Replay("kirindorm10", locked=False) text_style "modmybutton"
                    elif not kirindorm10 and not ev_kirindorm10.missed:
                        text _("Love, Dorms, and Other Things")

                    if kirinsoccer15 and show_complete:
                        textbutton _("Flickering Spotlight {b}✓{/b}") action Replay("kirinsoccer15", locked=False) text_style "modmybutton"
                    elif not kirinsoccer15 and not ev_kirinsoccer15.missed:
                        text _("Flickering Spotlight")

                    if kirinsoccer20 and show_complete:
                        textbutton _("Enigmatology {b}✓{/b}") action Replay("kirinsoccer20", locked=False) text_style "modmybutton"
                    elif not kirinsoccer20 and not ev_kirinsoccer20.missed:
                        text _("Enigmatology")

                    if kirindorm15 and show_complete:
                        textbutton _("Bye Bye, Boner {b}✓{/b}") action Replay("kirindorm15", locked=False) text_style "modmybutton"
                    elif not kirindorm15 and not ev_kirindorm15.missed:
                        text _("Bye Bye, Boner")

                    if kirindorm20 and show_complete:
                        textbutton _("Terms & Conditions {b}✓{/b}") action Replay("kirindorm20", locked=False) text_style "modmybutton"
                    elif not kirindorm20 and not ev_kirindorm20.missed:
                        text _("Terms & Conditions")

                    if kirindate25 and show_complete:
                        textbutton _("All That is Contaminated {b}✓{/b}") action Replay("kirindate25", locked=False) text_style "modmybutton"
                    elif not kirindate25 and not ev_kirindate25.missed:
                        text _("All That is Contaminated")

                    if kirinlust20 and show_complete:
                        textbutton _("Taking the Reins {b}✓{/b}") action Replay("kirinlust20", locked=False) text_style "modmybutton"
                    elif ev_kirinlust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}Falling Off the Tracks{/s}{/color}")
                    elif not kirinlust20 and not ev_kirinlust20.missed:
                        text _("{color=FF85FD}Taking the Reins{/color}")

                    if kirinspecial25 and show_complete:
                        textbutton _("Dyed Orange, Drenched in Sun {b}✓{/b}") action Replay("kirinspecial25", locked=False) text_style "modmybutton"
                    elif ev_kirinspecial25.missed and show_complete:
                        text _("{color=EF1A1A}{s}Drowned in Blue{/s}{/color}")
                    elif not kirinspecial25 and not ev_kirinspecial25.missed:
                        text _("Dyed Orange, Drenched in Sun")

                    if kirindorm25 and show_complete:
                        textbutton _("Temporary Bliss {b}✓{/b}") action Replay("kirindorm25", locked=False) text_style "modmybutton"
                    elif not kirindorm25 and not ev_kirindorm25.missed:
                        text _("Temporary Bliss")

                    if kirinsoccer25 and show_complete:
                        textbutton _("Four Hand Massage {b}✓{/b}") action Replay("kirinsoccer25", locked=False) text_style "modmybutton"
                    elif not kirinsoccer25 and not ev_kirinsoccer25.missed:
                        text _("Four Hand Massage")

                    if kirinspecial30 and show_complete:
                        textbutton _("Made Out of Nothing {b}✓{/b}") action Replay("kirinspecial30", locked=False) text_style "modmybutton"
                    elif ev_kirinspecial30.missed and show_complete:
                        text _("{color=EF1A1A}{s}At Least Someone Smiles{/s}{/color}")
                    elif not kirinspecial30 and not ev_kirinspecial30.missed:
                        text _("Made Out of Nothing")

                    if kirinlust202 and show_complete:
                        textbutton _("The Other Half {b}✓{/b}") action Replay("kirinlust202", locked=False) text_style "modmybutton"
                    elif ev_kirinlust202.missed and show_complete:
                        text _("{color=EF1A1A}{s}Eternally Empty{/s}{/color}")
                    elif not kirinlust202 and not ev_kirinlust202.missed:
                        text _("{color=FF85FD}The Other Half{/color}")

                    text _("---------------------------------------------")

                    if kirinlust30 and show_complete:
                        textbutton _("Falling Asleep Standing Up {b}✓{/b}") action Replay("kirinlust30", locked=False) text_style "modmybutton"
                    elif ev_kirinlust30.missed and show_complete:
                        text _("{color=EF1A1A}{s}Drugs Are Bad{/s}{/color}")
                    elif not kirinlust30 and not ev_kirinlust30.missed:
                        text _("{color=FF85FD}Falling Asleep Standing Up{/color}")

                    if kirinspecial40 and show_complete:
                        textbutton _("At the Edge of the Riverbank {b}✓{/b}") action Replay("kirinspecial40", locked=False) text_style "modmybutton"
                    elif not kirinspecial40 and not ev_kirinspecial40.missed:
                        text _("At the Edge of the Riverbank")

                    if kirinspecial45p1 and show_complete:
                        textbutton _("Never Enough {b}✓{/b}") action Replay("kirinspecial45p1", locked=False) text_style "modmybutton"
                    elif not kirinspecial45p1 and not ev_kirinspecial45p1.missed:
                        text _("Never Enough")

                    if kirinspecial45p2 and show_complete:
                        textbutton _("Salmon Onigiri {b}✓{/b}") action Replay("kirinspecial45p2", locked=False) text_style "modmybutton"
                    elif not kirinspecial45p2 and not ev_kirinspecial45p2.missed:
                        text _("Salmon Onigiri")

                    text _("---------------------------------------------")

                    if sportswars9 and show_complete:
                        textbutton _("Rubber Traits {b}✓{/b}") action Replay("sportswars9", locked=False) text_style "modmybutton"
                    elif not sportswars9 and not ev_sportswars9.missed:
                        text _("Rubber Traits")

                    if sportswars18 and show_complete:
                        textbutton _("Girls Vs. Robots {b}✓{/b}") action Replay("sportswars18", locked=False) text_style "modmybutton"
                    elif not sportswars18 and not ev_sportswars18.missed:
                        text _("Girls Vs. Robots")

                    if kirinspring1 and show_complete:
                        textbutton _("Clockless Watch {b}✓{/b}") action Replay("kirinspring1", locked=False) text_style "modmybutton"
                    elif not kirinspring1 and not ev_kirinspring1.missed:
                        text _("Clockless Watch")

                    if christmaskirin1 and show_complete:
                        textbutton _("Solar Eclipse {b}✓{/b}") action Replay("christmaskirin1", locked=False) text_style "modmybutton"
                    elif not christmaskirin1 and not ev_christmaskirin1.missed:
                        text _("Solar Eclipse")

                    if christmaskirin2 and show_complete:
                        textbutton _("Animal Control {b}✓{/b}") action Replay("christmaskirin2", locked=False) text_style "modmybutton"
                    elif not christmaskirin2 and not ev_christmaskirin2.missed:
                        text _("Animal Control")

                    if kirinchristmalloween1 and show_complete:
                        textbutton _("Perfect Days {b}✓{/b}") action Replay("kirinchristmalloween1", locked=False) text_style "modmybutton"
                    elif ev_kirinchristmalloween1.missed and show_complete:
                        text _("{color=EF1A1A}{s}SEPTIC SEPSIS{/s}{/color}")
                    elif not kirinchristmalloween1 and not ev_kirinchristmalloween1.missed:
                        text _("Perfect Days")

                    if kirinchristmalloween2 and show_complete:
                        textbutton _("Transpacific Sadness Symposium VII: ANTFARM ANTECHAMBER {b}✓{/b}") action Replay("kirinchristmalloween2", locked=False) text_style "modmybutton"
                    elif ev_kirinchristmalloween2.missed and show_complete:
                        text _("{color=EF1A1A}{s}THE CANCELLATION OF ACT V{/s}{/color}")
                    elif not kirinchristmalloween2 and not ev_kirinchristmalloween2.missed:
                        text _("Transpacific Sadness Symposium VII: ANTFARM ANTECHAMBER")

                    if kirinspring2 and show_complete:
                        textbutton _("Love, Love, Love {b}✓{/b}") action Replay("kirinspring2", locked=False) text_style "modmybutton"
                    elif ev_kirinspring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}SQUIRM, SQUIRM, SQUIRM{/s}{/color}")
                    elif not kirinspring2 and not ev_kirinspring2.missed:
                        text _("Love, Love, Love")

                    if kirinspring3 and show_complete:
                        textbutton _("In the Morning, In the Cold {b}✓{/b}") action Replay("kirinspring3", locked=False) text_style "modmybutton"
                    elif not kirinspring3 and not ev_kirinspring3.missed:
                        text _("In the Morning, In the Cold")

                    if kirinspring4 and show_complete:
                        textbutton _("Failed Attempts at Arson {b}✓{/b}") action Replay("kirinspring4", locked=False) text_style "modmybutton"
                    elif ev_kirinspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}Firestopper{/s}{/color}")
                    elif not kirinspring4 and not ev_kirinspring4.missed:
                        text _("Failed Attempts at Arson")

                #MAKIEVENT

                if showgirl == "Maki":

                    if makidate1 and show_complete:
                        textbutton _("Beautiful Porn Salesman {b}✓{/b}") action Replay("makidate1", locked=False) text_style "modmybutton"
                    elif not makidate1 and not ev_makidate1.missed:
                        text _("Beautiful Porn Salesman")

                    if makidate5 and show_complete:
                        textbutton _("Maki Miyamura's Mom-Mode Mission {b}✓{/b}") action Replay("makidate5", locked=False) text_style "modmybutton"
                    elif not makidate5 and not ev_makidate5.missed:
                        text _("Maki Miyamura's Mom-Mode Mission")

                    text _("---------------------------------------------")

                    if makidate10 and show_complete:
                        textbutton _("A Fair Trade {b}✓{/b}") action Replay("makidate10", locked=False) text_style "modmybutton"
                    elif not makidate10 and not ev_makidate10.missed:
                        text _("A Fair Trade")

                    if makiday351 and show_complete:
                        textbutton _("Three Afloat On One Raft {b}✓{/b}") action Replay("makiday351", locked=False) text_style "modmybutton"
                    elif not makiday351 and not ev_makiday351.missed:
                        text _("Three Afloat On One Raft")

                    if makidate15 and show_complete:
                        textbutton _("Thank You For Your Business {b}✓{/b}") action Replay("makidate15", locked=False) text_style "modmybutton"
                    elif ev_makidate15.missed and show_complete:
                        text _("{color=EF1A1A}{s}Closed for Renovation{/s}{/color}")
                    elif not makidate15 and not ev_makidate15.missed:
                        text _("Thank You For Your Business")

                    if makiinvite1 and show_complete:
                        textbutton _("Traveling Lube Dealer {b}✓{/b}") action Replay("makiinvite1", locked=False) text_style "modmybutton"
                    elif not makiinvite1 and not ev_makiinvite1.missed:
                        text _("{color=778EFF}Traveling Lube Dealer{/color}")

                    if makiinvite2 and show_complete:
                        textbutton _("Special Occasions {b}✓{/b}") action Replay("makiinvite2", locked=False) text_style "modmybutton"
                    elif not makiinvite2 and not ev_makiinvite2.missed:
                        text _("{color=778EFF}Special Occasions{/color}")

                    text _("---------------------------------------------")

                    if sadgirls3 and show_complete:
                        textbutton _("Adulting {b}✓{/b}") action Replay("sadgirls3", locked=False) text_style "modmybutton"
                    elif not sadgirls3 and not ev_sadgirls3.missed:
                        text _("Adulting")

                    if sadgirls6 and show_complete:
                        textbutton _("Rolling Stop (Turned Backwards) {b}✓{/b}") action Replay("sadgirls6", locked=False) text_style "modmybutton"
                    elif not sadgirls6 and not ev_sadgirls6.missed:
                        text _("Rolling Stop (Turned Backwards)")

                    if makiinv3 and show_complete:
                        textbutton _("Baby Steps {b}✓{/b}") action Replay("makiinv3", locked=False) text_style "modmybutton"
                    elif not makiinv3 and not ev_makiinv3.missed:
                        text _("Baby Steps")

                    if makihornyquestintro and show_complete:
                        textbutton _("The Maltese Falcon {b}✓{/b}") action Replay("makihornyquestintro", locked=False) text_style "modmybutton"
                    elif not makihornyquestintro and not ev_makihornyquestintro.missed:
                        text _("The Maltese Falcon")

                    if makihornytrip2 and show_complete:
                        textbutton _("Shut Up & Cum {b}✓{/b}") action Replay("makihornytrip2", locked=False) text_style "modmybutton"
                    elif ev_makihornytrip2.missed and show_complete:
                        text _("{color=EF1A1A}{s}You Missed Something Again{/s}{/color}")
                    elif not makihornytrip2 and not ev_makihornytrip2.missed:
                        text _("Shut Up & Cum")

                    if makihornytrip3 and show_complete:
                        textbutton _("Rotting From the Inside Out {b}✓{/b}") action Replay("makihornytrip3", locked=False) text_style "modmybutton"
                    elif not makihornytrip3 and not ev_makihornytrip3.missed:
                        text _("Rotting From the Inside Out")

                    text _("---------------------------------------------")

                    if makicamp1 and show_complete:
                        textbutton _("Wires...and the Concept of Breathing {b}✓{/b}") action Replay("makicamp1", locked=False) text_style "modmybutton"
                    elif not makicamp1 and not ev_makicamp1.missed:
                        text _("Wires...and the Concept of Breathing")

                    if makicamp2 and show_complete:
                        textbutton _("A Place Between the Trees {b}✓{/b}") action Replay("makicamp2", locked=False) text_style "modmybutton"
                    elif not makicamp2 and not ev_makicamp2.missed:
                        text _("A Place Between the Trees")

                    if makilust5 and show_complete:
                        textbutton _("To Boldly Go... {b}✓{/b}") action Replay("makilust5", locked=False) text_style "modmybutton"
                    elif ev_makilust5.missed and show_complete:
                        text _("{color=EF1A1A}{s}Humble ABITCH{/s}{/color}")
                    elif not makilust5 and not ev_makilust5.missed:
                        text _("{color=FF85FD}To Boldly Go...{/color}")

                    if makispring1 and show_complete:
                        textbutton _("Sex Box Memories {b}✓{/b}") action Replay("makispring1", locked=False) text_style "modmybutton"
                    elif not makispring1 and not ev_makispring1.missed:
                        text _("Sex Box Memories")

                    if makispring2 and show_complete:
                        textbutton _("Hello Alone {b}✓{/b}") action Replay("makispring2", locked=False) text_style "modmybutton"
                    elif not makispring2 and not ev_makispring2.missed:
                        text _("Hello Alone")

                    if makispring3 and show_complete:
                        textbutton _("ASS {b}✓{/b}") action Replay("makispring3", locked=False) text_style "modmybutton"
                    elif not makispring3 and not ev_makispring3.missed:
                        text _("ASS")

                    if makispring4 and show_complete:
                        textbutton _("Budd Dwyer {b}✓{/b}") action Replay("makispring4", locked=False) text_style "modmybutton"
                    elif not makispring4 and not ev_makispring4.missed:
                        text _("Budd Dwyer")

                    if makispring5 and show_complete:
                        textbutton _("A Million Tiny Pieces {b}✓{/b}") action Replay("makispring5", locked=False) text_style "modmybutton"
                    elif not makispring5 and not ev_makispring5.missed:
                        text _("A Million Tiny Pieces")

                #MAKOTOEVENT

                if showgirl == "Makoto":

                    if firsttimepornshop and show_complete:
                        textbutton _("Unexpected Profession {b}✓{/b}") action Replay("firsttimepornshop", locked=False) text_style "modmybutton"
                    elif not firsttimepornshop and not ev_firsttimepornshop.missed:
                        text _("Unexpected Profession")

                    if makotofirsthall and show_complete:
                        textbutton _("Teacher's Pet {b}✓{/b}") action Replay("makotofirsthall", locked=False) text_style "modmybutton"
                    elif not makotofirsthall and not ev_makotofirsthall.missed:
                        text _("Teacher's Pet")

                    if pornshop5 and show_complete:
                        textbutton _("Watching Porn Alone {b}✓{/b}") action Replay("pornshop5", locked=False) text_style "modmybutton"
                    elif not pornshop5 and not ev_pornshop5.missed:
                        text _("Watching Porn Alone")

                    if makotodorm5 and show_complete:
                        textbutton _("Completely Platonic {b}✓{/b}") action Replay("makotodorm5", locked=False) text_style "modmybutton"
                    elif not makotodorm5 and not ev_makotodorm5.missed:
                        text _("Completely Platonic")

                    if pornshop10 and show_complete:
                        textbutton _("Rising of the Tide {b}✓{/b}") action Replay("pornshop10", locked=False) text_style "modmybutton"
                    elif not pornshop10 and not ev_pornshop10.missed:
                        text _("Rising of the Tide")

                    if makotonew1 and show_complete:
                        textbutton _("Frogger {b}✓{/b}") action Replay("makotonew1", locked=False) text_style "modmybutton"
                    elif not makotonew1 and not ev_makotonew1.missed:
                        text _("Frogger")

                    if makotonew2 and show_complete:
                        textbutton _("Sowing the Seeds {b}✓{/b}") action Replay("makotonew2", locked=False) text_style "modmybutton"
                    elif not makotonew2 and not ev_makotonew2.missed:
                        text _("Sowing the Seeds")

                    if makotonew3 and show_complete:
                        textbutton _("Egg Tooth {b}✓{/b}") action Replay("makotonew3", locked=False) text_style "modmybutton"
                    elif not makotonew3 and not ev_makotonew3.missed:
                        text _("Egg Tooth")

                    if pornshop15 and show_complete:
                        textbutton _("Fishing For Love {b}✓{/b}") action Replay("pornshop15", locked=False) text_style "modmybutton"
                    elif not pornshop15 and not ev_pornshop15.missed:
                        text _("Fishing For Love")

                    if makotolust5 and show_complete:
                        textbutton _("Quid Pro Quo {b}✓{/b}") action Replay("makotolust5", locked=False) text_style "modmybutton"
                    elif not makotolust5 and not ev_makotolust5.missed:
                        text _("{color=FF85FD}Quid Pro Quo{/color}")

                    if makotoinvite1 and show_complete:
                        textbutton _("Declaration of War {b}✓{/b}") action Replay("makotoinvite1", locked=False) text_style "modmybutton"
                    elif not makotoinvite1 and not ev_makotoinvite1.missed:
                        text _("{color=778EFF}Declaration of War{/color}")

                    if makotoinvite2 and show_complete:
                        textbutton _("Studious Teen Virgin {b}✓{/b}") action Replay("makotoinvite2", locked=False) text_style "modmybutton"
                    elif not makotoinvite2 and not ev_makotoinvite2.missed:
                        text _("{color=778EFF}Studious Teen Virgin{/color}")

                    if pornshop20 and show_complete:
                        textbutton _("Aftermath {b}✓{/b}") action Replay("pornshop20", locked=False) text_style "modmybutton"
                    elif not pornshop20 and not ev_pornshop20.missed:
                        text _("Aftermath")

                    if makotodorm20 and show_complete:
                        textbutton _("Residual Sadness {b}✓{/b}") action Replay("makotodorm20", locked=False) text_style "modmybutton"
                    elif not makotodorm20 and not ev_makotodorm20.missed:
                        text _("Residual Sadness")

                    if pornshop25 and show_complete:
                        textbutton _("Service Charge {b}✓{/b}") action Replay("pornshop25", locked=False) text_style "modmybutton"
                    elif not pornshop25 and not ev_pornshop25.missed:
                        text _("Service Charge")

                    if makotodorm25 and show_complete:
                        textbutton _("Bluejay {b}✓{/b}") action Replay("makotodorm25", locked=False) text_style "modmybutton"
                    elif not makotodorm25 and not ev_makotodorm25.missed:
                        text _("Bluejay")

                    text _("---------------------------------------------")

                    if makotolust10 and show_complete:
                        textbutton _("Semblance of a Soul {b}✓{/b}") action Replay("makotolust10", locked=False) text_style "modmybutton"
                    elif not makotolust10 and not ev_makotolust10.missed:
                        text _("{color=FF85FD}Semblance of a Soul{/color}")

                    if makotowinterbeach1 and show_complete:
                        textbutton _("Condoms in the Sand {b}✓{/b}") action Replay("makotowinterbeach1", locked=False) text_style "modmybutton"
                    elif not makotowinterbeach1 and not ev_makotowinterbeach1.missed:
                        text _("Condoms in the Sand")

                    if makotowinterbeach2 and show_complete:
                        textbutton _("Humans With Hollow Bones {b}✓{/b}") action Replay("makotowinterbeach2", locked=False) text_style "modmybutton"
                    elif not makotowinterbeach2 and not ev_makotowinterbeach2.missed:
                        text _("Humans With Hollow Bones")

                    if makotowinterbeach3 and show_complete:
                        textbutton _("I'm Not Here {b}✓{/b}") action Replay("makotowinterbeach3", locked=False) text_style "modmybutton"
                    elif not makotowinterbeach3 and not ev_makotowinterbeach3.missed:
                        text _("I'm Not Here")

                    if makotowinterbeach4 and show_complete:
                        textbutton _("Something, Somewhere {b}✓{/b}") action Replay("makotowinterbeach4", locked=False) text_style "modmybutton"
                    elif not makotowinterbeach4 and not ev_makotowinterbeach4.missed:
                        text _("Something, Somewhere")

                    if makotolust20 and show_complete:
                        textbutton _("Hot Water {b}✓{/b}") action Replay("makotolust20", locked=False) text_style "modmybutton"
                    elif ev_makotolust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}Cold Water{/s}{/color}")
                    elif not makotolust20 and not ev_makotolust20.missed:
                        text _("{color=FF85FD}Hot Water{/color}")

                    text _("---------------------------------------------")

                    if sadgirls1 and show_complete:
                        textbutton _("Whispers of the World {b}✓{/b}") action Replay("sadgirls1", locked=False) text_style "modmybutton"
                    elif not sadgirls1 and not ev_sadgirls1.missed:
                        text _("Whispers of the World")

                    if sadgirls7 and show_complete:
                        textbutton _("Parallelogram {b}✓{/b}") action Replay("sadgirls7", locked=False) text_style "modmybutton"
                    elif not sadgirls7 and not ev_sadgirls7.missed:
                        text _("Parallelogram")

                    if makotolust30 and show_complete:
                        textbutton _("White Oak Doors {b}✓{/b}") action Replay("makotolust30", locked=False) text_style "modmybutton"
                    elif ev_makotolust30.missed and show_complete:
                        text _("{color=EF1A1A}{s}Daddy's Girl{/s}{/color}")
                    elif not makotolust30 and not ev_makotolust30.missed:
                        text _("{color=FF85FD}White Oak Doors{/color}")

                    if sadgirls8 and show_complete:
                        textbutton _("A Beautiful Mind {b}✓{/b}") action Replay("sadgirls8", locked=False) text_style "modmybutton"
                    elif not sadgirls8 and not ev_sadgirls8.missed:
                        text _("A Beautiful Mind")

                    if makotospecial50 and show_complete:
                        textbutton _("Young Cardinals {b}✓{/b}") action Replay("makotospecial50", locked=False) text_style "modmybutton"
                    elif not makotospecial50 and not ev_makotospecial50.missed:
                        text _("Young Cardinals")

                    if makotopool55 and show_complete:
                        textbutton _("Cool Sex Tips {b}✓{/b}") action Replay("makotopool55", locked=False) text_style "modmybutton"
                    elif not makotopool55 and not ev_makotopool55.missed:
                        text _("Cool Sex Tips")

                    if makotodorm55p1 and show_complete:
                        textbutton _("Bra Shopping {b}✓{/b}") action Replay("makotodorm55p1", locked=False) text_style "modmybutton"
                    elif not makotodorm55p1 and not ev_makotodorm55p1.missed:
                        text _("Bra Shopping")

                    if makotodorm55p2 and show_complete:
                        textbutton _("Suffer the Same {b}✓{/b}") action Replay("makotodorm55p2", locked=False) text_style "modmybutton"
                    elif not makotodorm55p2 and not ev_makotodorm55p2.missed:
                        text _("Suffer the Same")

                    text _("---------------------------------------------")

                    if sportswars19 and show_complete:
                        textbutton _("The Pit of Despair {b}✓{/b}") action Replay("sportswars19", locked=False) text_style "modmybutton"
                    elif not sportswars19 and not ev_sportswars19.missed:
                        text _("The Pit of Despair")

                    if makotospring1 and show_complete:
                        textbutton _("Midnight Snack {b}✓{/b}") action Replay("makotospring1", locked=False) text_style "modmybutton"
                    elif not makotospring1 and not ev_makotospring1.missed:
                        text _("Midnight Snack")

                    if makotospring2 and show_complete:
                        textbutton _("T Is For Time (Trees & Threes) {b}✓{/b}") action Replay("makotospring2", locked=False) text_style "modmybutton"
                    elif not makotospring2 and not ev_makotospring2.missed:
                        text _("T Is For Time (Trees & Threes)")

                    if halloweenmakoto1 and show_complete:
                        textbutton _("Six Ways From Sunday {b}✓{/b}") action Replay("halloweenmakoto1", locked=False) text_style "modmybutton"
                    elif not halloweenmakoto1 and not ev_halloweenmakoto1.missed:
                        text _("Six Ways From Sunday")

                    if halloweenmakoto2 and show_complete:
                        textbutton _("Precious Little Life {b}✓{/b}") action Replay("halloweenmakoto2", locked=False) text_style "modmybutton"
                    elif not halloweenmakoto2 and not ev_halloweenmakoto2.missed:
                        text _("Precious Little Life")

                    if halloweenmakoto3 and show_complete:
                        textbutton _("Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR {b}✓{/b}") action Replay("halloweenmakoto3", locked=False) text_style "modmybutton"
                    elif not halloweenmakoto3 and not ev_halloweenmakoto3.missed:
                        text _("Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR")

                    if makotospring3 and show_complete:
                        textbutton _("The World, Alive (Ant Farm) {b}✓{/b}") action Replay("makotospring3", locked=False) text_style "modmybutton"
                    elif not makotospring3 and not ev_makotospring3.missed:
                        text _("The World, Alive (Ant Farm)")

                    if beachsixmakoto1 and show_complete:
                        textbutton _("Black Mass {b}✓{/b}") action Replay("beachsixmakoto1", locked=False) text_style "modmybutton"
                    elif not beachsixmakoto1 and not ev_beachsixmakoto1.missed:
                        text _("Black Mass")

                    if beachsixmakoto2 and show_complete:
                        textbutton _("A Matter of Time {b}✓{/b}") action Replay("beachsixmakoto2", locked=False) text_style "modmybutton"
                    elif not beachsixmakoto2 and not ev_beachsixmakoto2.missed:
                        text _("A Matter of Time")

                    if makotospring4 and show_complete:
                        textbutton _("This Penis, Eternal {b}✓{/b}") action Replay("makotospring4", locked=False) text_style "modmybutton"
                    elif not makotospring4 and not ev_makotospring4.missed:
                        text _("This Penis, Eternal")

                    if makotospring5 and show_complete:
                        textbutton _("Code Red {b}✓{/b}") action Replay("makotospring5", locked=False) text_style "modmybutton"
                    elif not makotospring5 and not ev_makotospring5.missed:
                        text _("Code Red")

                #MAYAEVENT

                if showgirl == "Maya":

                    if firsttimeshrine and show_complete:
                        textbutton _("A New Beginning {b}✓{/b}") action Replay("firsttimeshrine", locked=False) text_style "modmybutton"
                    elif not firsttimeshrine and not ev_firsttimeshrine.missed:
                        text _("A New Beginning")

                    if mayafirsthall and show_complete:
                        textbutton _("Mondays {b}✓{/b}") action Replay("mayafirsthall", locked=False) text_style "modmybutton"
                    elif not mayafirsthall and not ev_mayafirsthall.missed:
                        text _("Mondays")

                    if shrine5 and show_complete:
                        textbutton _("Different Worlds {b}✓{/b}") action Replay("shrine5", locked=False) text_style "modmybutton"
                    elif not shrine5 and not ev_shrine5.missed:
                        text _("Different Worlds")

                    if mayadorm5 and show_complete:
                        textbutton _("Secrets Worth Keeping {b}✓{/b}") action Replay("mayadorm5", locked=False) text_style "modmybutton"
                    elif not mayadorm5 and not ev_mayadorm5.missed:
                        text _("Secrets Worth Keeping")

                    if shrine10 and show_complete:
                        textbutton _("Past/Present/Future {b}✓{/b}") action Replay("shrine10", locked=False) text_style "modmybutton"
                    elif not shrine10 and not ev_shrine10.missed:
                        text _("Past/Present/Future")

                    if mayadorm10 and show_complete:
                        textbutton _("Rewind/Repeat/Refuse {b}✓{/b}") action Replay("mayadorm10", locked=False) text_style "modmybutton"
                    elif not mayadorm10 and not ev_mayadorm10.missed:
                        text _("Rewind/Repeat/Refuse")

                    if shrine15 and show_complete:
                        textbutton _("You and Me {b}✓{/b}") action Replay("shrine15", locked=False) text_style "modmybutton"
                    elif not shrine15 and not ev_shrine15.missed:
                        text _("You and Me")

                    if mayadorm15 and show_complete:
                        textbutton _("Takoyaki {b}✓{/b}") action Replay("mayadorm15", locked=False) text_style "modmybutton"
                    elif not mayadorm15 and not ev_mayadorm15.missed:
                        text _("Takoyaki")

                    if shrine20 and show_complete:
                        textbutton _("Nothing is Real {b}✓{/b}") action Replay("shrine20", locked=False) text_style "modmybutton"
                    elif not shrine20 and not ev_shrine20.missed:
                        text _("Nothing is Real")

                    if mayadorm20 and show_complete:
                        textbutton _("Close Your Eyes {b}✓{/b}") action Replay("mayadorm20", locked=False) text_style "modmybutton"
                    elif not mayadorm20 and not ev_mayadorm20.missed:
                        text _("Close Your Eyes")

                    if shrine25 and show_complete:
                        textbutton _("Watermelons and Violin {b}✓{/b}") action Replay("shrine25", locked=False) text_style "modmybutton"
                    elif not shrine25 and not ev_shrine25.missed:
                        text _("Watermelons and Violin")

                    if mayadorm25 and show_complete:
                        textbutton _("FLAVOR BEAM! {b}✓{/b}") action Replay("mayadorm25", locked=False) text_style "modmybutton"
                    elif not mayadorm25 and not ev_mayadorm25.missed:
                        text _("FLAVOR BEAM!")

                    text _("---------------------------------------------")

                    if mayadorm30 and show_complete:
                        textbutton _("What it Means to Be Destroyed {b}✓{/b}") action Replay("mayadorm30", locked=False) text_style "modmybutton"
                    elif not mayadorm30 and not ev_mayadorm30.missed:
                        text _("What it Means to Be Destroyed")

                    if shrine30 and show_complete:
                        textbutton _("Now More Than Ever {b}✓{/b}") action Replay("shrine30", locked=False) text_style "modmybutton"
                    elif ev_shrine30.missed and show_complete:
                        text _("{color=EF1A1A}{s}Breaking, the Best Way{/s}{/color}")
                    elif not shrine30 and not ev_shrine30.missed:
                        text _("Now More Than Ever")

                    if mayadorm35 and show_complete:
                        textbutton _("A Place That Can Only Exist in Our Minds {b}✓{/b}") action Replay("mayadorm35", locked=False) text_style "modmybutton"
                    elif not mayadorm35 and not ev_mayadorm35.missed:
                        text _("A Place That Can Only Exist in Our Minds")

                    if shrine35 and show_complete:
                        textbutton _("Stop Looking For Answers {b}✓{/b}") action Replay("shrine35", locked=False) text_style "modmybutton"
                    elif not shrine35 and not ev_shrine35.missed:
                        text _("Stop Looking For Answers")

                    if mayafestival1 and show_complete:
                        textbutton _("Somewhere Inside of a Dream {b}✓{/b}") action Replay("mayafestival1", locked=False) text_style "modmybutton"
                    elif not mayafestival1 and not ev_mayafestival1.missed:
                        text _("Somewhere Inside of a Dream")

                    if mayafestival2 and show_complete:
                        textbutton _("Three Halves Make a Whole (Itadakimasu) {b}✓{/b}") action Replay("mayafestival2", locked=False) text_style "modmybutton"
                    elif not mayafestival2 and not ev_mayafestival2.missed:
                        text _("Three Halves Make a Whole (Itadakimasu)")

                    if mayafestival3 and show_complete:
                        textbutton _("As The Sun Disappears {b}✓{/b}") action Replay("mayafestival3", locked=False) text_style "modmybutton"
                    elif not mayafestival3 and not ev_mayafestival3.missed:
                        text _("As The Sun Disappears")

                    if mayafestival4 and show_complete:
                        textbutton _("Everlasting Mercy {b}✓{/b}") action Replay("mayafestival4", locked=False) text_style "modmybutton"
                    elif not mayafestival4 and not ev_mayafestival4.missed:
                        text _("Everlasting Mercy")

                    text _("---------------------------------------------")

                    if shrine40 and show_complete:
                        textbutton _("The Sun, And All Its Toxic Rays {b}✓{/b}") action Replay("shrine40", locked=False) text_style "modmybutton"
                    elif not shrine40 and not ev_shrine40.missed:
                        text _("The Sun, And All Its Toxic Rays")

                    if mayadate45 and show_complete:
                        textbutton _("Anything & Everything {b}✓{/b}") action Replay("mayadate45", locked=False) text_style "modmybutton"
                    elif not mayadate45 and not ev_mayadate45.missed:
                        text _("Anything & Everything")

                    if mayaspecial45 and show_complete:
                        textbutton _("A Brutal, Violent Creaming {b}✓{/b}") action Replay("mayaspecial45", locked=False) text_style "modmybutton"
                    elif not mayaspecial45 and not ev_mayaspecial45.missed:
                        text _("A Brutal, Violent Creaming")

                    text _("---------------------------------------------")

                    if sportswars5 and show_complete:
                        textbutton _("The Motherland Calls! {b}✓{/b}") action Replay("sportswars5", locked=False) text_style "modmybutton"
                    elif not sportswars5 and not ev_sportswars5.missed:
                        text _("The Motherland Calls!")

                    if sportswars10 and show_complete:
                        textbutton _("Miraculous Human-Glue {b}✓{/b}") action Replay("sportswars10", locked=False) text_style "modmybutton"
                    elif not sportswars10 and not ev_sportswars10.missed:
                        text _("Miraculous Human-Glue")

                    if sportswars14 and show_complete:
                        textbutton _("Radio Silence {b}✓{/b}") action Replay("sportswars14", locked=False) text_style "modmybutton"
                    elif not sportswars14 and not ev_sportswars14.missed:
                        text _("Radio Silence")

                    if halloweenmaya1 and show_complete:
                        textbutton _("The Girl Who Leapt Through Time {b}✓{/b}") action Replay("halloweenmaya1", locked=False) text_style "modmybutton"
                    elif not halloweenmaya1 and not ev_halloweenmaya1.missed:
                        text _("The Girl Who Leapt Through Time")

                    if halloweenmaya2 and show_complete:
                        textbutton _("Wake Up (My Story) {b}✓{/b}") action Replay("halloweenmaya2", locked=False) text_style "modmybutton"
                    elif not halloweenmaya2 and not ev_halloweenmaya2.missed:
                        text _("Wake Up (My Story)")

                    if halloweenmaya3 and show_complete:
                        textbutton _("Right as Rain {b}✓{/b}") action Replay("halloweenmaya3", locked=False) text_style "modmybutton"
                    elif not halloweenmaya3 and not ev_halloweenmaya3.missed:
                        text _("Right as Rain")

                    if mayaspring1 and show_complete:
                        textbutton _("Billy Pilgrim {b}✓{/b}") action Replay("mayaspring1", locked=False) text_style "modmybutton"
                    elif not mayaspring1 and not ev_mayaspring1.missed:
                        text _("Billy Pilgrim")

                    if mayaspring2 and show_complete:
                        textbutton _("A Second Haunting {b}✓{/b}") action Replay("mayaspring2", locked=False) text_style "modmybutton"
                    elif not mayaspring2 and not ev_mayaspring2.missed:
                        text _("A Second Haunting")

                    if mayaspring3 and show_complete:
                        textbutton _("My Perfect World {b}✓{/b}") action Replay("mayaspring3", locked=False) text_style "modmybutton"
                    elif not mayaspring3 and not ev_mayaspring3.missed:
                        text _("My Perfect World")

                    if mayachristmalloween1 and show_complete:
                        textbutton _("Tying the Knot {b}✓{/b}") action Replay("mayachristmalloween1", locked=False) text_style "modmybutton"
                    elif not mayachristmalloween1 and not ev_mayachristmalloween1.missed:
                        text _("Tying the Knot")

                    if mayachristmalloween2 and show_complete:
                        textbutton _("This Room and Everything in It {b}✓{/b}") action Replay("mayachristmalloween2", locked=False) text_style "modmybutton"
                    elif not mayachristmalloween2 and not ev_mayachristmalloween2.missed:
                        text _("This Room and Everything in It")

                    if mayachristmalloween3 and show_complete:
                        textbutton _("Something to Do With Love {b}✓{/b}") action Replay("mayachristmalloween3", locked=False) text_style "modmybutton"
                    elif not mayachristmalloween3 and not ev_mayachristmalloween3.missed:
                        text _("Something to Do With Love")

                    if dormwarssixmaya1 and show_complete:
                        textbutton _("Ground Zero {b}✓{/b}") action Replay("dormwarssixmaya1", locked=False) text_style "modmybutton"
                    elif not dormwarssixmaya1 and not ev_dormwarssixmaya1.missed:
                        text _("Ground Zero")

                    if mayaspring4 and show_complete:
                        textbutton _("Ode on the Death of a Favorite Cat Drowned in a Tub of Goldfishes {b}✓{/b}") action Replay("mayaspring4", locked=False) text_style "modmybutton"
                    elif ev_mayaspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}Ode on a Thing That Did a Thing or Something{/s}{/color}")
                    elif not mayaspring4 and not ev_mayaspring4.missed:
                        text _("Ode on the Death of a Favorite Cat Drowned in a Tub of Goldfishes")

                    if mayaspring5 and show_complete:
                        textbutton _("The War Invalid {b}✓{/b}") action Replay("mayaspring5", locked=False) text_style "modmybutton"
                    elif not mayaspring5 and not ev_mayaspring5.missed:
                        text _("The War Invalid")

                #MIKUEVENT

                if showgirl == "Miku":

                    if firsttimesoccerfield and show_complete:
                        textbutton _("Daytime Stalking Pass {b}✓{/b}") action Replay("firsttimesoccerfield", locked=False) text_style "modmybutton"
                    elif not firsttimesoccerfield and not ev_firsttimesoccerfield.missed:
                        text _("Daytime Stalking Pass")

                    if mikufirsthall and show_complete:
                        textbutton _("Behind Closed Doors {b}✓{/b}") action Replay("mikufirsthall", locked=False) text_style "modmybutton"
                    elif not mikufirsthall and not ev_mikufirsthall.missed:
                        text _("Behind Closed Doors")

                    if soccer5 and show_complete:
                        textbutton _("It's Always Sunny in Kumon-mi {b}✓{/b}") action Replay("soccer5", locked=False) text_style "modmybutton"
                    elif not soccer5 and not ev_soccer5.missed:
                        text _("It's Always Sunny in Kumon-mi")

                    if mikudorm5 and show_complete:
                        textbutton _("Broken Bones {b}✓{/b}") action Replay("mikudorm5", locked=False) text_style "modmybutton"
                    elif not mikudorm5 and not ev_mikudorm5.missed:
                        text _("Broken Bones")

                    if soccer10 and show_complete:
                        textbutton _("Nightvision {b}✓{/b}") action Replay("soccer10", locked=False) text_style "modmybutton"
                    elif not soccer10 and not ev_soccer10.missed:
                        text _("Nightvision")

                    if mikudorm10 and show_complete:
                        textbutton _("You and Me and the Night {b}✓{/b}") action Replay("mikudorm10", locked=False) text_style "modmybutton"
                    elif not mikudorm10 and not ev_mikudorm10.missed:
                        text _("You and Me and the Night")

                    if soccer15 and show_complete:
                        textbutton _("Hormones Running Wild {b}✓{/b}") action Replay("soccer15", locked=False) text_style "modmybutton"
                    elif not soccer15 and not ev_soccer15.missed:
                        text _("Hormones Running Wild")

                    if mikudorm15 and show_complete:
                        textbutton _("Moments Like This {b}✓{/b}") action Replay("mikudorm15", locked=False) text_style "modmybutton"
                    elif not mikudorm15 and not ev_mikudorm15.missed:
                        text _("Moments Like This")

                    if soccer20 and show_complete:
                        textbutton _("Coach {b}✓{/b}") action Replay("soccer20", locked=False) text_style "modmybutton"
                    elif not soccer20 and not ev_soccer20.missed:
                        text _("Coach")

                    if soccer25 and show_complete:
                        textbutton _("Thighs On-Demand {b}✓{/b}") action Replay("soccer25", locked=False) text_style "modmybutton"
                    elif not soccer25 and not ev_soccer25.missed:
                        text _("Thighs On-Demand")

                    if mikudorm25 and show_complete:
                        textbutton _("Scaredy Cat {b}✓{/b}") action Replay("mikudorm25", locked=False) text_style "modmybutton"
                    elif not mikudorm25 and not ev_mikudorm25.missed:
                        text _("Scaredy Cat")

                    if soccer30 and show_complete:
                        textbutton _("An Extra Set of Arms {b}✓{/b}") action Replay("soccer30", locked=False) text_style "modmybutton"
                    elif not soccer30 and not ev_soccer30.missed:
                        text _("An Extra Set of Arms")

                    if mikudorm30 and show_complete:
                        textbutton _("One. Two. Three. {b}✓{/b}") action Replay("mikudorm30", locked=False) text_style "modmybutton"
                    elif not mikudorm30 and not ev_mikudorm30.missed:
                        text _("One. Two. Three.")

                    text _("---------------------------------------------")

                    if soccer35 and show_complete:
                        textbutton _("Loxonin {b}✓{/b}") action Replay("soccer35", locked=False) text_style "modmybutton"
                    elif not soccer35 and not ev_soccer35.missed:
                        text _("Loxonin")

                    if mikuwinterbeach1 and show_complete:
                        textbutton _("To Sleep, Perchance to Dream {b}✓{/b}") action Replay("mikuwinterbeach1", locked=False) text_style "modmybutton"
                    elif not mikuwinterbeach1 and not ev_mikuwinterbeach1.missed:
                        text _("To Sleep, Perchance to Dream")

                    if mikudorm35 and show_complete:
                        textbutton _("Triple Whammy {b}✓{/b}") action Replay("mikudorm35", locked=False) text_style "modmybutton"
                    elif not mikudorm35 and not ev_mikudorm35.missed:
                        text _("Triple Whammy")

                    if mikudorm40 and show_complete:
                        textbutton _("Speed of Light {b}✓{/b}") action Replay("mikudorm40", locked=False) text_style "modmybutton"
                    elif not mikudorm40 and not ev_mikudorm40.missed:
                        text _("Speed of Light")

                    if mikudorm45 and show_complete:
                        textbutton _("Acute Love Triangle {b}✓{/b}") action Replay("mikudorm45", locked=False) text_style "modmybutton"
                    elif not mikudorm45 and not ev_mikudorm45.missed:
                        text _("Acute Love Triangle")

                    if mikudorm45p2 and show_complete:
                        textbutton _("Chrysalis {b}✓{/b}") action Replay("mikudorm45p2", locked=False) text_style "modmybutton"
                    elif not mikudorm45p2 and not ev_mikudorm45p2.missed:
                        text _("Chrysalis")

                    if mikuspecial50 and show_complete:
                        textbutton _("Someone Else's Skin {b}✓{/b}") action Replay("mikuspecial50", locked=False) text_style "modmybutton"
                    elif not mikuspecial50 and not ev_mikuspecial50.missed:
                        text _("Someone Else's Skin")

                    if mikudorm50 and show_complete:
                        textbutton _("The Devil & God Are Raging Inside Me {b}✓{/b}") action Replay("mikudorm50", locked=False) text_style "modmybutton"
                    elif not mikudorm50 and not ev_mikudorm50.missed:
                        text _("The Devil & God Are Raging Inside Me")

                    text _("---------------------------------------------")

                    if mikuinvite1 and show_complete:
                        textbutton _("Breakaway {b}✓{/b}") action Replay("mikuinvite1", locked=False) text_style "modmybutton"
                    elif not mikuinvite1 and not ev_mikuinvite1.missed:
                        text _("{color=778EFF}Breakaway{/color}")

                    if mikuinvite2 and show_complete:
                        textbutton _("Fair is Fair {b}✓{/b}") action Replay("mikuinvite2", locked=False) text_style "modmybutton"
                    elif not mikuinvite2 and not ev_mikuinvite2.missed:
                        text _("{color=778EFF}Fair is Fair{/color}")

                    if mikupool55 and show_complete:
                        textbutton _("Voice of Vibration {b}✓{/b}") action Replay("mikupool55", locked=False) text_style "modmybutton"
                    elif not mikupool55 and not ev_mikupool55.missed:
                        text _("Voice of Vibration")

                    if mikudorm55p1 and show_complete:
                        textbutton _("Essence of Eiderdown {b}✓{/b}") action Replay("mikudorm55p1", locked=False) text_style "modmybutton"
                    elif not mikudorm55p1 and not ev_mikudorm55p1.missed:
                        text _("Essence of Eiderdown")

                    if mikudorm55p2 and show_complete:
                        textbutton _("Rostrum of Recollection {b}✓{/b}") action Replay("mikudorm55p2", locked=False) text_style "modmybutton"
                    elif not mikudorm55p2 and not ev_mikudorm55p2.missed:
                        text _("Rostrum of Recollection")

                    text _("---------------------------------------------")

                    if mikuspring1 and show_complete:
                        textbutton _("Captain Sorrow {b}✓{/b}") action Replay("mikuspring1", locked=False) text_style "modmybutton"
                    elif not mikuspring1 and not ev_mikuspring1.missed:
                        text _("Captain Sorrow")

                    if mikuspring2 and show_complete:
                        textbutton _("Bonerville {b}✓{/b}") action Replay("mikuspring2", locked=False) text_style "modmybutton"
                    elif not mikuspring2 and not ev_mikuspring2.missed:
                        text _("Bonerville")

                    if mikuspring3 and show_complete:
                        textbutton _("The Boys {b}✓{/b}") action Replay("mikuspring3", locked=False) text_style "modmybutton"
                    elif not mikuspring3 and not ev_mikuspring3.missed:
                        text _("The Boys")

                    if mikuspring4 and show_complete:
                        textbutton _("Live Fast, Die Young {b}✓{/b}") action Replay("mikuspring4", locked=False) text_style "modmybutton"
                    elif not mikuspring4 and not ev_mikuspring4.missed:
                        text _("Live Fast, Die Young")

                    if mikuspring5 and show_complete:
                        textbutton _("The Gazelle {b}✓{/b}") action Replay("mikuspring5", locked=False) text_style "modmybutton"
                    elif not mikuspring5 and not ev_mikuspring5.missed:
                        text _("The Gazelle")

                    if mikulust5 and show_complete:
                        textbutton _("Practice Makes Perfect {b}✓{/b}") action Replay("mikulust5", locked=False) text_style "modmybutton"
                    elif not mikulust5 and not ev_mikulust5.missed:
                        text _("{color=FF85FD}Practice Makes Perfect{/color}")

                    if mikuspring6 and show_complete:
                        textbutton _("Bean Sprouts {b}✓{/b}") action Replay("mikuspring6", locked=False) text_style "modmybutton"
                    elif not mikuspring6 and not ev_mikuspring6.missed:
                        text _("Bean Sprouts")

                    if mikuspring7 and show_complete:
                        textbutton _("The Whale {b}✓{/b}") action Replay("mikuspring7", locked=False) text_style "modmybutton"
                    elif not mikuspring7 and not ev_mikuspring7.missed:
                        text _("The Whale")

                #MOLLYEVENT

                if showgirl == "Molly":

                    if mollycafe1 and show_complete:
                        textbutton _("NTR & Pregnancy {b}✓{/b}") action Replay("mollycafe1", locked=False) text_style "modmybutton"
                    elif not mollycafe1 and not ev_mollycafe1.missed:
                        text _("NTR & Pregnancy")

                    if mollyfirsthall and show_complete:
                        textbutton _("The Cult of Molly {b}✓{/b}") action Replay("mollyfirsthall", locked=False) text_style "modmybutton"
                    elif not mollyfirsthall and not ev_mollyfirsthall.missed:
                        text _("The Cult of Molly")

                    if mollycafe5 and show_complete:
                        textbutton _("Remnants of Forgotten Memes {b}✓{/b}") action Replay("mollycafe5", locked=False) text_style "modmybutton"
                    elif not mollycafe5 and not ev_mollycafe5.missed:
                        text _("Remnants of Forgotten Memes")

                    if mollydorm5 and show_complete:
                        textbutton _("Torrent of Power {b}✓{/b}") action Replay("mollydorm5", locked=False) text_style "modmybutton"
                    elif not mollydorm5 and not ev_mollydorm5.missed:
                        text _("Torrent of Power")

                    if mollycafe10 and show_complete:
                        textbutton _("Something Out of a Nukige {b}✓{/b}") action Replay("mollycafe10", locked=False) text_style "modmybutton"
                    elif not mollycafe10 and not ev_mollycafe10.missed:
                        text _("Something Out of a Nukige")

                    if mollydorm10 and show_complete:
                        textbutton _("The Dark Entity {b}✓{/b}") action Replay("mollydorm10", locked=False) text_style "modmybutton"
                    elif not mollydorm10 and not ev_mollydorm10.missed:
                        text _("The Dark Entity")

                    text _("---------------------------------------------")

                    if mollycafe15 and show_complete:
                        textbutton _("Onward to Valhalla {b}✓{/b}") action Replay("mollycafe15", locked=False) text_style "modmybutton"
                    elif not mollycafe15 and not ev_mollycafe15.missed:
                        text _("Onward to Valhalla")

                    if mollydorm15 and show_complete:
                        textbutton _("Unpaid Promotion {b}✓{/b}") action Replay("mollydorm15", locked=False) text_style "modmybutton"
                    elif not mollydorm15 and not ev_mollydorm15.missed:
                        text _("Unpaid Promotion")

                    if mollycafe20 and show_complete:
                        textbutton _("The Legacy of Thaum Pt. II {b}✓{/b}") action Replay("mollycafe20", locked=False) text_style "modmybutton"
                    elif not mollycafe20 and not ev_mollycafe20.missed:
                        text _("The Legacy of Thaum Pt. II")

                    if mollydorm20 and show_complete:
                        textbutton _("Ahead of the Curve {b}✓{/b}") action Replay("mollydorm20", locked=False) text_style "modmybutton"
                    elif not mollydorm20 and not ev_mollydorm20.missed:
                        text _("Ahead of the Curve")

                    if mollycafe25 and show_complete:
                        textbutton _("Resurrection Sickness {b}✓{/b}") action Replay("mollycafe25", locked=False) text_style "modmybutton"
                    elif not mollycafe25 and not ev_mollycafe25.missed:
                        text _("Resurrection Sickness")

                    if mollycafe25p2 and show_complete:
                        textbutton _("Tír na nÓg {b}✓{/b}") action Replay("mollycafe25p2", locked=False) text_style "modmybutton"
                    elif not mollycafe25p2 and not ev_mollycafe25p2.missed:
                        text _("Tír na nÓg")

                    if mollydorm25 and show_complete:
                        textbutton _("Transmogrification {b}✓{/b}") action Replay("mollydorm25", locked=False) text_style "modmybutton"
                    elif not mollydorm25 and not ev_mollydorm25.missed:
                        text _("Transmogrification")

                    if mollydorm30 and show_complete:
                        textbutton _("Walkthrough {b}✓{/b}") action Replay("mollydorm30", locked=False) text_style "modmybutton"
                    elif not mollydorm30 and not ev_mollydorm30.missed:
                        text _("Walkthrough")

                    text _("---------------------------------------------")

                    if mollycafe30p1 and show_complete:
                        textbutton _("Hook {b}✓{/b}") action Replay("mollycafe30p1", locked=False) text_style "modmybutton"
                    elif not mollycafe30p1 and not ev_mollycafe30p1.missed:
                        text _("Hook")

                    if mollycafe30p2 and show_complete:
                        textbutton _("A Night to Remember {b}✓{/b}") action Replay("mollycafe30p2", locked=False) text_style "modmybutton"
                    elif not mollycafe30p2 and not ev_mollycafe30p2.missed:
                        text _("A Night to Remember")

                    if mollydate35p1 and show_complete:
                        textbutton _("Anar'alah Belore {b}✓{/b}") action Replay("mollydate35p1", locked=False) text_style "modmybutton"
                    elif not mollydate35p1 and not ev_mollydate35p1.missed:
                        text _("Anar'alah Belore")

                    if mollydate35p2 and show_complete:
                        textbutton _("Sardines {b}✓{/b}") action Replay("mollydate35p2", locked=False) text_style "modmybutton"
                    elif not mollydate35p2 and not ev_mollydate35p2.missed:
                        text _("Sardines")

                    text _("---------------------------------------------")

                    if mollycamp1 and show_complete:
                        textbutton _("Corrupted Blood {b}✓{/b}") action Replay("mollycamp1", locked=False) text_style "modmybutton"
                    elif not mollycamp1 and not ev_mollycamp1.missed:
                        text _("Corrupted Blood")

                    if mollyspring1 and show_complete:
                        textbutton _("Level One {b}✓{/b}") action Replay("mollyspring1", locked=False) text_style "modmybutton"
                    elif not mollyspring1 and not ev_mollyspring1.missed:
                        text _("Level One")

                    if mollyspring2 and show_complete:
                        textbutton _("Fated to Love You {b}✓{/b}") action Replay("mollyspring2", locked=False) text_style "modmybutton"
                    elif not mollyspring2 and not ev_mollyspring2.missed:
                        text _("Fated to Love You")

                    if mollylust10 and show_complete:
                        textbutton _("The Farmer’s Daughter {b}✓{/b}") action Replay("mollylust10", locked=False) text_style "modmybutton"
                    elif ev_mollylust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Goblin Queen{/s}{/color}")
                    elif not mollylust10 and not ev_mollylust10.missed:
                        text _("{color=FF85FD}The Farmer’s Daughter{/color}")

                    if mollyinvite1 and show_complete:
                        textbutton _("No Murder in the House {b}✓{/b}") action Replay("mollyinvite1", locked=False) text_style "modmybutton"
                    elif not mollyinvite1 and not ev_mollyinvite1.missed:
                        text _("{color=778EFF}No Murder in the House{/color}")

                    if mollyinvite2 and show_complete:
                        textbutton _("Pixels & Polygons {b}✓{/b}") action Replay("mollyinvite2", locked=False) text_style "modmybutton"
                    elif not mollyinvite2 and not ev_mollyinvite2.missed:
                        text _("{color=778EFF}Pixels & Polygons{/color}")

                    if beachsixmolly1 and show_complete:
                        textbutton _("Power-Leveling {b}✓{/b}") action Replay("beachsixmolly1", locked=False) text_style "modmybutton"
                    elif not beachsixmolly1 and not ev_beachsixmolly1.missed:
                        text _("Power-Leveling")

                    if mollyspring3 and show_complete:
                        textbutton _("Nihongo Jouzu {b}✓{/b}") action Replay("mollyspring3", locked=False) text_style "modmybutton"
                    elif not mollyspring3 and not ev_mollyspring3.missed:
                        text _("Nihongo Jouzu")

                    if mollyspring4 and show_complete:
                        textbutton _("Missable Event {b}✓{/b}") action Replay("mollyspring4", locked=False) text_style "modmybutton"
                    elif ev_mollyspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}Missed Event{/s}{/color}")
                    elif not mollyspring4 and not ev_mollyspring4.missed:
                        text _("Missable Event")

                #NAOEVENT

                if showgirl == "Nao":

                    if naospecial1 and show_complete:
                        textbutton _("Silver Tongue {b}✓{/b}") action Replay("naospecial1", locked=False) text_style "modmybutton"
                    elif not naospecial1 and not ev_naospecial1.missed:
                        text _("Silver Tongue")

                    if naospecial2 and show_complete:
                        textbutton _("Becoming a Kidnapper {b}✓{/b}") action Replay("naospecial2", locked=False) text_style "modmybutton"
                    elif not naospecial2 and not ev_naospecial2.missed:
                        text _("Becoming a Kidnapper")

                    if naospecial3 and show_complete:
                        textbutton _("Eternity Until {b}✓{/b}") action Replay("naospecial3", locked=False) text_style "modmybutton"
                    elif not naospecial3 and not ev_naospecial3.missed:
                        text _("Eternity Until")

                    text _("---------------------------------------------")

                    if naocamp1 and show_complete:
                        textbutton _("Flora {b}✓{/b}") action Replay("naocamp1", locked=False) text_style "modmybutton"
                    elif not naocamp1 and not ev_naocamp1.missed:
                        text _("Flora")

                    if naocamp2 and show_complete:
                        textbutton _("What's in the Pot? {b}✓{/b}") action Replay("naocamp2", locked=False) text_style "modmybutton"
                    elif not naocamp2 and not ev_naocamp2.missed:
                        text _("What's in the Pot?")

                    if halloweennao1 and show_complete:
                        textbutton _("Even Gods Get Lost {b}✓{/b}") action Replay("halloweennao1", locked=False) text_style "modmybutton"
                    elif not halloweennao1 and not ev_halloweennao1.missed:
                        text _("Even Gods Get Lost")

                    if halloweennao2 and show_complete:
                        textbutton _("A House Near a Lake (The Same Place as Always) {b}✓{/b}") action Replay("halloweennao2", locked=False) text_style "modmybutton"
                    elif not halloweennao2 and not ev_halloweennao2.missed:
                        text _("A House Near a Lake (The Same Place as Always)")

                    if naospring1 and show_complete:
                        textbutton _("Wings of Anhedonia {b}✓{/b}") action Replay("naospring1", locked=False) text_style "modmybutton"
                    elif not naospring1 and not ev_naospring1.missed:
                        text _("Wings of Anhedonia")

                    if naospring2 and show_complete:
                        textbutton _("Miracle {b}✓{/b}") action Replay("naospring2", locked=False) text_style "modmybutton"
                    elif not naospring2 and not ev_naospring2.missed:
                        text _("Miracle")

                    if naospring3 and show_complete:
                        textbutton _("Nao More Than Ever {b}✓{/b}") action Replay("naospring3", locked=False) text_style "modmybutton"
                    elif not naospring3 and not ev_naospring3.missed:
                        text _("Nao More Than Ever")

                    if naospring4 and show_complete:
                        textbutton _("Menma {b}✓{/b}") action Replay("naospring4", locked=False) text_style "modmybutton"
                    elif not naospring4 and not ev_naospring4.missed:
                        text _("Menma")

                #NIKIEVENT

                if showgirl == "Niki":

                    if nikidate1 and show_complete:
                        textbutton _("Cotton Candy {b}✓{/b}") action Replay("nikidate1", locked=False) text_style "modmybutton"
                    elif not nikidate1 and not ev_nikidate1.missed:
                        text _("Cotton Candy")

                    if nikidate5 and show_complete:
                        textbutton _("Like it's Any Other Day {b}✓{/b}") action Replay("nikidate5", locked=False) text_style "modmybutton"
                    elif not nikidate5 and not ev_nikidate5.missed:
                        text _("Like it's Any Other Day")

                    if nikidate10 and show_complete:
                        textbutton _("Thousands, If Not Millions {b}✓{/b}") action Replay("nikidate10", locked=False) text_style "modmybutton"
                    elif not nikidate10 and not ev_nikidate10.missed:
                        text _("Thousands, If Not Millions")

                    if nikidate15 and show_complete:
                        textbutton _("Hotel Rooms {b}✓{/b}") action Replay("nikidate15", locked=False) text_style "modmybutton"
                    elif not nikidate15 and not ev_nikidate15.missed:
                        text _("Hotel Rooms")

                    if nikiinvite1 and show_complete:
                        textbutton _("Sisters {b}✓{/b}") action Replay("nikiinvite1", locked=False) text_style "modmybutton"
                    elif not nikiinvite1 and not ev_nikiinvite1.missed:
                        text _("{color=778EFF}Sisters{/color}")

                    if nikiinvite2 and show_complete:
                        textbutton _("Dear You {b}✓{/b}") action Replay("nikiinvite2", locked=False) text_style "modmybutton"
                    elif not nikiinvite2 and not ev_nikiinvite2.missed:
                        text _("{color=778EFF}Dear You{/color}")

                    text _("---------------------------------------------")

                    if nikilovesyou1 and show_complete:
                        textbutton _("What it Takes to Move Forward {b}✓{/b}") action Replay("nikilovesyou1", locked=False) text_style "modmybutton"
                    elif not nikilovesyou1 and not ev_nikilovesyou1.missed:
                        text _("What it Takes to Move Forward")

                    if nikilovesyou2 and show_complete:
                        textbutton _("The End of the Tour (Glasswalker) {b}✓{/b}") action Replay("nikilovesyou2", locked=False) text_style "modmybutton"
                    elif not nikilovesyou2 and not ev_nikilovesyou2.missed:
                        text _("The End of the Tour (Glasswalker)")

                    if nikilovesyou3 and show_complete:
                        textbutton _("How To Make Love Stay {b}✓{/b}") action Replay("nikilovesyou3", locked=False) text_style "modmybutton"
                    elif not nikilovesyou3 and not ev_nikilovesyou3.missed:
                        text _("How To Make Love Stay")

                    if nikifirstlust and show_complete:
                        textbutton _("Non-Disclosure Agreement {b}✓{/b}") action Replay("nikifirstlust", locked=False) text_style "modmybutton"
                    elif not nikifirstlust and not ev_nikifirstlust.missed:
                        text _("{color=FF85FD}Non-Disclosure Agreement{/color}")

                    text _("---------------------------------------------")

                    if nikispring1 and show_complete:
                        textbutton _("They Came Together {b}✓{/b}") action Replay("nikispring1", locked=False) text_style "modmybutton"
                    elif not nikispring1 and not ev_nikispring1.missed:
                        text _("They Came Together")

                    if nikispring2 and show_complete:
                        textbutton _("The Clod and the Pebble {b}✓{/b}") action Replay("nikispring2", locked=False) text_style "modmybutton"
                    elif not nikispring2 and not ev_nikispring2.missed:
                        text _("The Clod and the Pebble")

                    if beachfive8 and show_complete:
                        textbutton _("Broken Furniture {b}✓{/b}") action Replay("beachfive8", locked=False) text_style "modmybutton"
                    elif not beachfive8 and not ev_beachfive8.missed:
                        text _("Broken Furniture")

                    if nikispring3 and show_complete:
                        textbutton _("That Funny Feeling {b}✓{/b}") action Replay("nikispring3", locked=False) text_style "modmybutton"
                    elif not nikispring3 and not ev_nikispring3.missed:
                        text _("That Funny Feeling")

                    if nikispring4 and show_complete:
                        textbutton _("Costco (Dick Lover) {b}✓{/b}") action Replay("nikispring4", locked=False) text_style "modmybutton"
                    elif not nikispring4 and not ev_nikispring4.missed:
                        text _("Costco (Dick Lover)")

                    if nikispring5 and show_complete:
                        textbutton _("Beauty in What's Broken {b}✓{/b}") action Replay("nikispring5", locked=False) text_style "modmybutton"
                    elif not nikispring5 and not ev_nikispring5.missed:
                        text _("Beauty in What's Broken")

                    if nikispring6 and show_complete:
                        textbutton _("Artificial Love {b}✓{/b}") action Replay("nikispring6", locked=False) text_style "modmybutton"
                    elif not nikispring6 and not ev_nikispring6.missed:
                        text _("Artificial Love")

                    if nikispring7 and show_complete:
                        textbutton _("This World, So Full of Fish {b}✓{/b}") action Replay("nikispring7", locked=False) text_style "modmybutton"
                    elif not nikispring7 and not ev_nikispring7.missed:
                        text _("This World, So Full of Fish")

                    if nikispring8 and show_complete:
                        textbutton _("Say Anything {b}✓{/b}") action Replay("nikispring8", locked=False) text_style "modmybutton"
                    elif not nikispring8 and not ev_nikispring8.missed:
                        text _("Say Anything")

                    if dormwarssixniki1 and show_complete:
                        textbutton _("Take it Easy (Love Nothing) {b}✓{/b}") action Replay("dormwarssixniki1", locked=False) text_style "modmybutton"
                    elif not dormwarssixniki1 and not ev_dormwarssixniki1.missed:
                        text _("Take it Easy (Love Nothing)")

                #NODOKAEVENT

                if showgirl == "Nodoka":

                    if nodokafirsthall and show_complete:
                        textbutton _("Humbert Humbert {b}✓{/b}") action Replay("nodokafirsthall", locked=False) text_style "modmybutton"
                    elif not nodokafirsthall and not ev_nodokafirsthall.missed:
                        text _("Humbert Humbert")

                    if nodokadorm1 and show_complete:
                        textbutton _("The Man Who Would Be King {b}✓{/b}") action Replay("nodokadorm1", locked=False) text_style "modmybutton"
                    elif not nodokadorm1 and not ev_nodokadorm1.missed:
                        text _("The Man Who Would Be King")

                    if nodokalibrary1 and show_complete:
                        textbutton _("Cracks in the Armor {b}✓{/b}") action Replay("nodokalibrary1", locked=False) text_style "modmybutton"
                    elif not nodokalibrary1 and not ev_nodokalibrary1.missed:
                        text _("Cracks in the Armor")

                    if nodokalibrary5 and show_complete:
                        textbutton _("Coloring Book {b}✓{/b}") action Replay("nodokalibrary5", locked=False) text_style "modmybutton"
                    elif not nodokalibrary5 and not ev_nodokalibrary5.missed:
                        text _("Coloring Book")

                    if nodokadorm5 and show_complete:
                        textbutton _("I See Everything {b}✓{/b}") action Replay("nodokadorm5", locked=False) text_style "modmybutton"
                    elif not nodokadorm5 and not ev_nodokadorm5.missed:
                        text _("I See Everything")

                    text _("---------------------------------------------")

                    if nodokadorm15 and show_complete:
                        textbutton _("Beyond the Reach of God {b}✓{/b}") action Replay("nodokadorm15", locked=False) text_style "modmybutton"
                    elif not nodokadorm15 and not ev_nodokadorm15.missed:
                        text _("Beyond the Reach of God")

                    if nodokaspecial15p1 and show_complete:
                        textbutton _("So Far Below {b}✓{/b}") action Replay("nodokaspecial15p1", locked=False) text_style "modmybutton"
                    elif not nodokaspecial15p1 and not ev_nodokaspecial15p1.missed:
                        text _("So Far Below")

                    if nodokaspecial15p2 and show_complete:
                        textbutton _("Matador {b}✓{/b}") action Replay("nodokaspecial15p2", locked=False) text_style "modmybutton"
                    elif not nodokaspecial15p2 and not ev_nodokaspecial15p2.missed:
                        text _("Matador")

                    if nodokaspecial15p3 and show_complete:
                        textbutton _("Things That Hurt {b}✓{/b}") action Replay("nodokaspecial15p3", locked=False) text_style "modmybutton"
                    elif ev_nodokaspecial15p3.missed and show_complete:
                        text _("{color=EF1A1A}{s}Seeing Red{/s}{/color}")
                    elif not nodokaspecial15p3 and not ev_nodokaspecial15p3.missed:
                        text _("Things That Hurt")

                    if nodokaspecial20 and show_complete:
                        textbutton _("Twisting Ivy {b}✓{/b}") action Replay("nodokaspecial20", locked=False) text_style "modmybutton"
                    elif not nodokaspecial20 and not ev_nodokaspecial20.missed:
                        text _("Twisting Ivy")

                    if nodokaspecial30p1 and show_complete:
                        textbutton _("Amoeba (Incontrovertible Peculiarity) {b}✓{/b}") action Replay("nodokaspecial30p1", locked=False) text_style "modmybutton"
                    elif not nodokaspecial30p1 and not ev_nodokaspecial30p1.missed:
                        text _("Amoeba (Incontrovertible Peculiarity)")

                    if nodokaspecial30p2 and show_complete:
                        textbutton _("This is Us {b}✓{/b}") action Replay("nodokaspecial30p2", locked=False) text_style "modmybutton"
                    elif not nodokaspecial30p2 and not ev_nodokaspecial30p2.missed:
                        text _("This is Us")

                    if nodokaspecial30p3 and show_complete:
                        textbutton _("Taco Attack {b}✓{/b}") action Replay("nodokaspecial30p3", locked=False) text_style "modmybutton"
                    elif not nodokaspecial30p3 and not ev_nodokaspecial30p3.missed:
                        text _("Taco Attack")

                    if nodokaspecial30p4 and show_complete:
                        textbutton _("Lavender {b}✓{/b}") action Replay("nodokaspecial30p4", locked=False) text_style "modmybutton"
                    elif not nodokaspecial30p4 and not ev_nodokaspecial30p4.missed:
                        text _("Lavender")

                    text _("---------------------------------------------")

                    if sportswars17 and show_complete:
                        textbutton _("Meet & Fuck {b}✓{/b}") action Replay("sportswars17", locked=False) text_style "modmybutton"
                    elif not sportswars17 and not ev_sportswars17.missed:
                        text _("Meet & Fuck")

                    if beachfive6 and show_complete:
                        textbutton _("The Silver King {b}✓{/b}") action Replay("beachfive6", locked=False) text_style "modmybutton"
                    elif not beachfive6 and not ev_beachfive6.missed:
                        text _("The Silver King")

                    if beachfive10 and show_complete:
                        textbutton _("Mille Crepe {b}✓{/b}") action Replay("beachfive10", locked=False) text_style "modmybutton"
                    elif not beachfive10 and not ev_beachfive10.missed:
                        text _("Mille Crepe")

                    if halloweennodoka1 and show_complete:
                        textbutton _("When the Well Runs Dry {b}✓{/b}") action Replay("halloweennodoka1", locked=False) text_style "modmybutton"
                    elif not halloweennodoka1 and not ev_halloweennodoka1.missed:
                        text _("When the Well Runs Dry")

                    if nodokainvite1 and show_complete:
                        textbutton _("Perfect Hair Forever {b}✓{/b}") action Replay("nodokainvite1", locked=False) text_style "modmybutton"
                    elif not nodokainvite1 and not ev_nodokainvite1.missed:
                        text _("{color=778EFF}Perfect Hair Forever{/color}")

                    if nodokainvite2 and show_complete:
                        textbutton _("Number One Fan {b}✓{/b}") action Replay("nodokainvite2", locked=False) text_style "modmybutton"
                    elif not nodokainvite2 and not ev_nodokainvite2.missed:
                        text _("{color=778EFF}Number One Fan{/color}")

                    if nodokainvite3 and show_complete:
                        textbutton _("How to Fuck Your Father {b}✓{/b}") action Replay("nodokainvite3", locked=False) text_style "modmybutton"
                    elif ev_nodokainvite3.missed and show_complete:
                        text _("{color=EF1A1A}{s}How to Cuck Your Daughter{/s}{/color}")
                    elif not nodokainvite3 and not ev_nodokainvite3.missed:
                        text _("{color=778EFF}How to Fuck Your Father{/color}")

                    if nodokachristmalloween1 and show_complete:
                        textbutton _("Hark! Now I Hear Them. {b}✓{/b}") action Replay("nodokachristmalloween1", locked=False) text_style "modmybutton"
                    elif not nodokachristmalloween1 and not ev_nodokachristmalloween1.missed:
                        text _("Hark! Now I Hear Them.")

                    if nodokachristmalloween2 and show_complete:
                        textbutton _("Beseech the Queen {b}✓{/b}") action Replay("nodokachristmalloween2", locked=False) text_style "modmybutton"
                    elif not nodokachristmalloween2 and not ev_nodokachristmalloween2.missed:
                        text _("Beseech the Queen")

                    if nodokachristmalloween3 and show_complete:
                        textbutton _("The Hours of Folly (Return to Sender) {b}✓{/b}") action Replay("nodokachristmalloween3", locked=False) text_style "modmybutton"
                    elif not nodokachristmalloween3 and not ev_nodokachristmalloween3.missed:
                        text _("The Hours of Folly (Return to Sender)")

                    if dormwarssixnodoka1 and show_complete:
                        textbutton _("Rotten Wood & Rusty Nails {b}✓{/b}") action Replay("dormwarssixnodoka1", locked=False) text_style "modmybutton"
                    elif not dormwarssixnodoka1 and not ev_dormwarssixnodoka1.missed:
                        text _("Rotten Wood & Rusty Nails")

                    if nodokaspring1 and show_complete:
                        textbutton _("Number Girl {b}✓{/b}") action Replay("nodokaspring1", locked=False) text_style "modmybutton"
                    elif not nodokaspring1 and not ev_nodokaspring1.missed:
                        text _("Number Girl")

                    if nodokaspring2 and show_complete:
                        textbutton _("Virgin Birth (Passer Montanus) {b}✓{/b}") action Replay("nodokaspring2", locked=False) text_style "modmybutton"
                    elif not nodokaspring2 and not ev_nodokaspring2.missed:
                        text _("Virgin Birth (Passer Montanus)")

                    if nodokaspring3 and show_complete:
                        textbutton _("Worlds Unseen {b}✓{/b}") action Replay("nodokaspring3", locked=False) text_style "modmybutton"
                    elif not nodokaspring3 and not ev_nodokaspring3.missed:
                        text _("Worlds Unseen")

                #NORIKOEVENT

                if showgirl == "Noriko":

                    if norikofirsthall and show_complete:
                        textbutton _("Sculpture (Dream Girl) {b}✓{/b}") action Replay("norikofirsthall", locked=False) text_style "modmybutton"
                    elif not norikofirsthall and not ev_norikofirsthall.missed:
                        text _("Sculpture (Dream Girl)")

                    if convenience1 and show_complete:
                        textbutton _("Nakayarakawayama {b}✓{/b}") action Replay("convenience1", locked=False) text_style "modmybutton"
                    elif not convenience1 and not ev_convenience1.missed:
                        text _("Nakayarakawayama")

                    if norikodorm5 and show_complete:
                        textbutton _("Semi-Constructive Criticism {b}✓{/b}") action Replay("norikodorm5", locked=False) text_style "modmybutton"
                    elif not norikodorm5 and not ev_norikodorm5.missed:
                        text _("Semi-Constructive Criticism")

                    if convenience5 and show_complete:
                        textbutton _("Mouthjob {b}✓{/b}") action Replay("convenience5", locked=False) text_style "modmybutton"
                    elif not convenience5 and not ev_convenience5.missed:
                        text _("Mouthjob")

                    if norikodorm10 and show_complete:
                        textbutton _("Kind Of, Yes. Kind Of, No. {b}✓{/b}") action Replay("norikodorm10", locked=False) text_style "modmybutton"
                    elif not norikodorm10 and not ev_norikodorm10.missed:
                        text _("Kind Of, Yes. Kind Of, No.")

                    if norikoinvite1 and show_complete:
                        textbutton _("New Shoes {b}✓{/b}") action Replay("norikoinvite1", locked=False) text_style "modmybutton"
                    elif not norikoinvite1 and not ev_norikoinvite1.missed:
                        text _("{color=778EFF}New Shoes{/color}")

                    if norikoinvite2 and show_complete:
                        textbutton _("Beginnings. Endings. Things in Between. {b}✓{/b}") action Replay("norikoinvite2", locked=False) text_style "modmybutton"
                    elif not norikoinvite2 and not ev_norikoinvite2.missed:
                        text _("{color=778EFF}Beginnings. Endings. Things in Between.{/color}")

                    if norikospecial20 and show_complete:
                        textbutton _("Fair & Square {b}✓{/b}") action Replay("norikospecial20", locked=False) text_style "modmybutton"
                    elif not norikospecial20 and not ev_norikospecial20.missed:
                        text _("Fair & Square")

                    if norikodorm20 and show_complete:
                        textbutton _("Homes for the Homeless {b}✓{/b}") action Replay("norikodorm20", locked=False) text_style "modmybutton"
                    elif not norikodorm20 and not ev_norikodorm20.missed:
                        text _("Homes for the Homeless")

                    if convenience25 and show_complete:
                        textbutton _("That One FMK Scene {b}✓{/b}") action Replay("convenience25", locked=False) text_style "modmybutton"
                    elif not convenience25 and not ev_convenience25.missed:
                        text _("That One FMK Scene")

                    if norikodorm25 and show_complete:
                        textbutton _("Loxosceles Reclusa {b}✓{/b}") action Replay("norikodorm25", locked=False) text_style "modmybutton"
                    elif not norikodorm25 and not ev_norikodorm25.missed:
                        text _("Loxosceles Reclusa")

                    text _("---------------------------------------------")

                    if norikodate30 and show_complete:
                        textbutton _("Hotel Noriko {b}✓{/b}") action Replay("norikodate30", locked=False) text_style "modmybutton"
                    elif not norikodate30 and not ev_norikodate30.missed:
                        text _("Hotel Noriko")

                    if norikodorm30 and show_complete:
                        textbutton _("Dotted Line {b}✓{/b}") action Replay("norikodorm30", locked=False) text_style "modmybutton"
                    elif not norikodorm30 and not ev_norikodorm30.missed:
                        text _("Dotted Line")

                    if norikoinvite3 and show_complete:
                        textbutton _("I Really Want to Stay at Your House {b}✓{/b}") action Replay("norikoinvite3", locked=False) text_style "modmybutton"
                    elif ev_norikoinvite3.missed and show_complete:
                        text _("{color=EF1A1A}{s}CONSUMED BY THE OLD ONE{/s}{/color}")
                    elif not norikoinvite3 and not ev_norikoinvite3.missed:
                        text _("{color=778EFF}I Really Want to Stay at Your House{/color}")

                    if norikoinvite4 and show_complete:
                        textbutton _("Somewhere {b}✓{/b}") action Replay("norikoinvite4", locked=False) text_style "modmybutton"
                    elif ev_norikoinvite4.missed and show_complete:
                        text _("{color=EF1A1A}{s}NOWHERE{/s}{/color}")
                    elif not norikoinvite4 and not ev_norikoinvite4.missed:
                        text _("{color=778EFF}Somewhere{/color}")

                    text _("---------------------------------------------")

                    if sportswars2 and show_complete:
                        textbutton _("Rivals (Taco Tuesday) {b}✓{/b}") action Replay("sportswars2", locked=False) text_style "modmybutton"
                    elif not sportswars2 and not ev_sportswars2.missed:
                        text _("Rivals (Taco Tuesday)")

                    if norikospring1 and show_complete:
                        textbutton _("The Long Road Ahead {b}✓{/b}") action Replay("norikospring1", locked=False) text_style "modmybutton"
                    elif not norikospring1 and not ev_norikospring1.missed:
                        text _("The Long Road Ahead")

                    if norikospring2 and show_complete:
                        textbutton _("Transpacific Sadness Symposium I: DEN OF THE MOLE RAT {b}✓{/b}") action Replay("norikospring2", locked=False) text_style "modmybutton"
                    elif not norikospring2 and not ev_norikospring2.missed:
                        text _("Transpacific Sadness Symposium I: DEN OF THE MOLE RAT")

                    if norikospring3 and show_complete:
                        textbutton _("Hard-Off {b}✓{/b}") action Replay("norikospring3", locked=False) text_style "modmybutton"
                    elif not norikospring3 and not ev_norikospring3.missed:
                        text _("Hard-Off")

                    if norikospring4 and show_complete:
                        textbutton _("Haiku {b}✓{/b}") action Replay("norikospring4", locked=False) text_style "modmybutton"
                    elif not norikospring4 and not ev_norikospring4.missed:
                        text _("Haiku")

                    if norikospring5 and show_complete:
                        textbutton _("At The Beach, In Every Life {b}✓{/b}") action Replay("norikospring5", locked=False) text_style "modmybutton"
                    elif not norikospring5 and not ev_norikospring5.missed:
                        text _("At The Beach, In Every Life")

                    if beachsixnoriko1 and show_complete:
                        textbutton _("Circling the Drain {b}✓{/b}") action Replay("beachsixnoriko1", locked=False) text_style "modmybutton"
                    elif not beachsixnoriko1 and not ev_beachsixnoriko1.missed:
                        text _("Circling the Drain")

                    if norikoinvite5 and show_complete:
                        textbutton _("Reasons to Die {b}✓{/b}") action Replay("norikoinvite5", locked=False) text_style "modmybutton"
                    elif not norikoinvite5 and not ev_norikoinvite5.missed:
                        text _("{color=778EFF}Reasons to Die{/color}")

                    if norikoinvite6 and show_complete:
                        textbutton _("Love in Strange Forms {b}✓{/b}") action Replay("norikoinvite6", locked=False) text_style "modmybutton"
                    elif ev_norikoinvite6.missed and show_complete:
                        text _("{color=EF1A1A}{s}PYRAMID OF HATE{/s}{/color}")
                    elif not norikoinvite6 and not ev_norikoinvite6.missed:
                        text _("{color=778EFF}Love in Strange Forms{/color}")

                #OSAKOEVENT

                if showgirl == "Osako":

                    if osakodate1 and show_complete:
                        textbutton _("Pressure Point {b}✓{/b}") action Replay("osakodate1", locked=False) text_style "modmybutton"
                    elif not osakodate1 and not ev_osakodate1.missed:
                        text _("Pressure Point")

                    if osakodojo1 and show_complete:
                        textbutton _("Floating Forever, Unfulfilled {b}✓{/b}") action Replay("osakodojo1", locked=False) text_style "modmybutton"
                    elif not osakodojo1 and not ev_osakodojo1.missed:
                        text _("Floating Forever, Unfulfilled")

                    text _("---------------------------------------------")

                    if osakodate15 and show_complete:
                        textbutton _("Young At Heart {b}✓{/b}") action Replay("osakodate15", locked=False) text_style "modmybutton"
                    elif not osakodate15 and not ev_osakodate15.missed:
                        text _("Young At Heart")

                    if osakodate20 and show_complete:
                        textbutton _("House of the Unholy {b}✓{/b}") action Replay("osakodate20", locked=False) text_style "modmybutton"
                    elif not osakodate20 and not ev_osakodate20.missed:
                        text _("House of the Unholy")

                    text _("---------------------------------------------")

                    if osakospring1 and show_complete:
                        textbutton _("Chaos Spiral (Heterosexual Sex) {b}✓{/b}") action Replay("osakospring1", locked=False) text_style "modmybutton"
                    elif not osakospring1 and not ev_osakospring1.missed:
                        text _("Chaos Spiral (Heterosexual Sex)")

                    if osakospring2 and show_complete:
                        textbutton _("Meat-Pocket {b}✓{/b}") action Replay("osakospring2", locked=False) text_style "modmybutton"
                    elif not osakospring2 and not ev_osakospring2.missed:
                        text _("Meat-Pocket")

                    if osakospring3 and show_complete:
                        textbutton _("Indecent Proposal {b}✓{/b}") action Replay("osakospring3", locked=False) text_style "modmybutton"
                    elif not osakospring3 and not ev_osakospring3.missed:
                        text _("Indecent Proposal")

                    if osakospring4 and show_complete:
                        textbutton _("MILF of the Month Club {b}✓{/b}") action Replay("osakospring4", locked=False) text_style "modmybutton"
                    elif not osakospring4 and not ev_osakospring4.missed:
                        text _("MILF of the Month Club")

                    if osakospring5 and show_complete:
                        textbutton _("Girl C {b}✓{/b}") action Replay("osakospring5", locked=False) text_style "modmybutton"
                    elif not osakospring5 and not ev_osakospring5.missed:
                        text _("Girl C")

                    if osakospring6 and show_complete:
                        textbutton _("All Good Things {b}✓{/b}") action Replay("osakospring6", locked=False) text_style "modmybutton"
                    elif not osakospring6 and not ev_osakospring6.missed:
                        text _("All Good Things")

                    if osakospring7 and show_complete:
                        textbutton _("When Harry Met Gandalf {b}✓{/b}") action Replay("osakospring7", locked=False) text_style "modmybutton"
                    elif not osakospring7 and not ev_osakospring7.missed:
                        text _("When Harry Met Gandalf")

                    if osakospring8 and show_complete:
                        textbutton _("Troubles, Trials, and Tribadism {b}✓{/b}") action Replay("osakospring8", locked=False) text_style "modmybutton"
                    elif not osakospring8 and not ev_osakospring8.missed:
                        text _("Troubles, Trials, and Tribadism")

                    if osakospring9 and show_complete:
                        textbutton _("Pica {b}✓{/b}") action Replay("osakospring9", locked=False) text_style "modmybutton"
                    elif not osakospring9 and not ev_osakospring9.missed:
                        text _("Pica")

                #OTOHAEVENT

                if showgirl == "Otoha":

                    if otohafirsthall and show_complete:
                        textbutton _("Everybody Loves Otoha {b}✓{/b}") action Replay("otohafirsthall", locked=False) text_style "modmybutton"
                    elif not otohafirsthall and not ev_otohafirsthall.missed:
                        text _("Everybody Loves Otoha")

                    if otohadorm1 and show_complete:
                        textbutton _("Conversations Outside of a Girls’ Dorm {b}✓{/b}") action Replay("otohadorm1", locked=False) text_style "modmybutton"
                    elif not otohadorm1 and not ev_otohadorm1.missed:
                        text _("Conversations Outside of a Girls’ Dorm")

                    if otohapark1 and show_complete:
                        textbutton _("Japanese Summer (Double Suicide) {b}✓{/b}") action Replay("otohapark1", locked=False) text_style "modmybutton"
                    elif not otohapark1 and not ev_otohapark1.missed:
                        text _("Japanese Summer (Double Suicide)")

                    if otohapark5 and show_complete:
                        textbutton _("Locked In {b}✓{/b}") action Replay("otohapark5", locked=False) text_style "modmybutton"
                    elif not otohapark5 and not ev_otohapark5.missed:
                        text _("Locked In")

                    if otohadorm5 and show_complete:
                        textbutton _("Highly Pornographic {b}✓{/b}") action Replay("otohadorm5", locked=False) text_style "modmybutton"
                    elif not otohadorm5 and not ev_otohadorm5.missed:
                        text _("Highly Pornographic")

                    if otohapark10 and show_complete:
                        textbutton _("Pull the Plug {b}✓{/b}") action Replay("otohapark10", locked=False) text_style "modmybutton"
                    elif not otohapark10 and not ev_otohapark10.missed:
                        text _("Pull the Plug")

                    if otohaspecial10 and show_complete:
                        textbutton _("Two-Octave Pitch Glide {b}✓{/b}") action Replay("otohaspecial10", locked=False) text_style "modmybutton"
                    elif not otohaspecial10 and not ev_otohaspecial10.missed:
                        text _("Two-Octave Pitch Glide")

                    if otohadorm10 and show_complete:
                        textbutton _("Breathing in Unison {b}✓{/b}") action Replay("otohadorm10", locked=False) text_style "modmybutton"
                    elif not otohadorm10 and not ev_otohadorm10.missed:
                        text _("Breathing in Unison")

                    if otohadorm10p2 and show_complete:
                        textbutton _("Vanilla Bean {b}✓{/b}") action Replay("otohadorm10p2", locked=False) text_style "modmybutton"
                    elif not otohadorm10p2 and not ev_otohadorm10p2.missed:
                        text _("Vanilla Bean")

                    text _("---------------------------------------------")

                    if otohaspecial15p1 and show_complete:
                        textbutton _("King Midas {b}✓{/b}") action Replay("otohaspecial15p1", locked=False) text_style "modmybutton"
                    elif not otohaspecial15p1 and not ev_otohaspecial15p1.missed:
                        text _("King Midas")

                    if otohaspecial15p2 and show_complete:
                        textbutton _("White People {b}✓{/b}") action Replay("otohaspecial15p2", locked=False) text_style "modmybutton"
                    elif not otohaspecial15p2 and not ev_otohaspecial15p2.missed:
                        text _("White People")

                    if otohadate20 and show_complete:
                        textbutton _("Breaking Character {b}✓{/b}") action Replay("otohadate20", locked=False) text_style "modmybutton"
                    elif not otohadate20 and not ev_otohadate20.missed:
                        text _("Breaking Character")

                    text _("---------------------------------------------")

                    if otohaspring1 and show_complete:
                        textbutton _("This Curse Called Youth {b}✓{/b}") action Replay("otohaspring1", locked=False) text_style "modmybutton"
                    elif not otohaspring1 and not ev_otohaspring1.missed:
                        text _("This Curse Called Youth")

                    if otohaspring2 and show_complete:
                        textbutton _("Taint the Sapling {b}✓{/b}") action Replay("otohaspring2", locked=False) text_style "modmybutton"
                    elif not otohaspring2 and not ev_otohaspring2.missed:
                        text _("Taint the Sapling")

                    if otohaspring3 and show_complete:
                        textbutton _("Something Wonderful {b}✓{/b}") action Replay("otohaspring3", locked=False) text_style "modmybutton"
                    elif not otohaspring3 and not ev_otohaspring3.missed:
                        text _("Something Wonderful")

                    if christmasotoha1 and show_complete:
                        textbutton _("Sisterly Love {b}✓{/b}") action Replay("christmasotoha1", locked=False) text_style "modmybutton"
                    elif not christmasotoha1 and not ev_christmasotoha1.missed:
                        text _("Sisterly Love")

                    if otohaspring4 and show_complete:
                        textbutton _("Becoming Closer to Closure {b}✓{/b}") action Replay("otohaspring4", locked=False) text_style "modmybutton"
                    elif not otohaspring4 and not ev_otohaspring4.missed:
                        text _("Becoming Closer to Closure")

                    if beachsixotoha1 and show_complete:
                        textbutton _("Something in the Water {b}✓{/b}") action Replay("beachsixotoha1", locked=False) text_style "modmybutton"
                    elif not beachsixotoha1 and not ev_beachsixotoha1.missed:
                        text _("Something in the Water")

                    if otohaspring5 and show_complete:
                        textbutton _("Five Star Review {b}✓{/b}") action Replay("otohaspring5", locked=False) text_style "modmybutton"
                    elif not otohaspring5 and not ev_otohaspring5.missed:
                        text _("Five Star Review")

                    if otohaspring6 and show_complete:
                        textbutton _("Billboard Hot 100 {b}✓{/b}") action Replay("otohaspring6", locked=False) text_style "modmybutton"
                    elif not otohaspring6 and not ev_otohaspring6.missed:
                        text _("Billboard Hot 100")

                    if otohaspring7 and show_complete:
                        textbutton _("Pet Sounds {b}✓{/b}") action Replay("otohaspring7", locked=False) text_style "modmybutton"
                    elif not otohaspring7 and not ev_otohaspring7.missed:
                        text _("Pet Sounds")

                #RIKAEVENT

                if showgirl == "Rika":

                    if rikadate1 and show_complete:
                        textbutton _("Impregnation Spree {b}✓{/b}") action Replay("rikadate1", locked=False) text_style "modmybutton"
                    elif not rikadate1 and not ev_rikadate1.missed:
                        text _("Impregnation Spree")

                    if rikaspecial2 and show_complete:
                        textbutton _("Back on Track {b}✓{/b}") action Replay("rikaspecial2", locked=False) text_style "modmybutton"
                    elif not rikaspecial2 and not ev_rikaspecial2.missed:
                        text _("Back on Track")

                    if rikadive1 and show_complete:
                        textbutton _("James and the Giant Peach (Together-ish) {b}✓{/b}") action Replay("rikadive1", locked=False) text_style "modmybutton"
                    elif not rikadive1 and not ev_rikadive1.missed:
                        text _("James and the Giant Peach (Together-ish)")

                    text _("---------------------------------------------")

                    if sportswars1 and show_complete:
                        textbutton _("Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You {b}✓{/b}") action Replay("sportswars1", locked=False) text_style "modmybutton"
                    elif not sportswars1 and not ev_sportswars1.missed:
                        text _("Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You")

                    if rikaspring1 and show_complete:
                        textbutton _("Rat College {b}✓{/b}") action Replay("rikaspring1", locked=False) text_style "modmybutton"
                    elif not rikaspring1 and not ev_rikaspring1.missed:
                        text _("Rat College")

                    if rikaspring2 and show_complete:
                        textbutton _("Sixty-Minute Mark {b}✓{/b}") action Replay("rikaspring2", locked=False) text_style "modmybutton"
                    elif not rikaspring2 and not ev_rikaspring2.missed:
                        text _("Sixty-Minute Mark")

                    if rikaspring3 and show_complete:
                        textbutton _("Sins of Thy Beloved {b}✓{/b}") action Replay("rikaspring3", locked=False) text_style "modmybutton"
                    elif not rikaspring3 and not ev_rikaspring3.missed:
                        text _("Sins of Thy Beloved")

                    if rikaspring4 and show_complete:
                        textbutton _("Four Hours, Thirteen Minutes, Eleven Seconds {b}✓{/b}") action Replay("rikaspring4", locked=False) text_style "modmybutton"
                    elif not rikaspring4 and not ev_rikaspring4.missed:
                        text _("Four Hours, Thirteen Minutes, Eleven Seconds")

                    if rikaspring5 and show_complete:
                        textbutton _("A Horse Rides an Elephant {b}✓{/b}") action Replay("rikaspring5", locked=False) text_style "modmybutton"
                    elif not rikaspring5 and not ev_rikaspring5.missed:
                        text _("A Horse Rides an Elephant")

                    if rikaspring6 and show_complete:
                        textbutton _("Solidarity (Hag Scene) {b}✓{/b}") action Replay("rikaspring6", locked=False) text_style "modmybutton"
                    elif not rikaspring6 and not ev_rikaspring6.missed:
                        text _("Solidarity (Hag Scene)")

                    if rikaspring7 and show_complete:
                        textbutton _("How to Escape a Quagmire {b}✓{/b}") action Replay("rikaspring7", locked=False) text_style "modmybutton"
                    elif not rikaspring7 and not ev_rikaspring7.missed:
                        text _("How to Escape a Quagmire")

                #RINEVENT

                if showgirl == "Rin":

                    if firsttimecafe and show_complete:
                        textbutton _("Guinea Pig {b}✓{/b}") action Replay("firsttimecafe", locked=False) text_style "modmybutton"
                    elif not firsttimecafe and not ev_firsttimecafe.missed:
                        text _("Guinea Pig")

                    if cafesugar and show_complete:
                        textbutton _("The Flavor of Love {b}✓{/b}") action Replay("cafesugar", locked=False) text_style "modmybutton"
                    elif not cafesugar and not ev_cafesugar.missed:
                        text _("The Flavor of Love")

                    if cafe10 and show_complete:
                        textbutton _("Haruka {b}✓{/b}") action Replay("cafe10", locked=False) text_style "modmybutton"
                    elif not cafe10 and not ev_cafe10.missed:
                        text _("Haruka")

                    if rinfirsthall and show_complete:
                        textbutton _("Locked Out {b}✓{/b}") action Replay("rinfirsthall", locked=False) text_style "modmybutton"
                    elif not rinfirsthall and not ev_rinfirsthall.missed:
                        text _("Locked Out")

                    if rinfirstvisit and show_complete:
                        textbutton _("Skulls {b}✓{/b}") action Replay("rinfirstvisit", locked=False) text_style "modmybutton"
                    elif not rinfirstvisit and not ev_rinfirstvisit.missed:
                        text _("Skulls")

                    if rindorm10 and show_complete:
                        textbutton _("Rin's Secret {b}✓{/b}") action Replay("rindorm10", locked=False) text_style "modmybutton"
                    elif not rindorm10 and not ev_rindorm10.missed:
                        text _("Rin's Secret")

                    if cafe15 and show_complete:
                        textbutton _("Window of the Waking Mind {b}✓{/b}") action Replay("cafe15", locked=False) text_style "modmybutton"
                    elif not cafe15 and not ev_cafe15.missed:
                        text _("Window of the Waking Mind")

                    if rindorm15 and show_complete:
                        textbutton _("Boundaries {b}✓{/b}") action Replay("rindorm15", locked=False) text_style "modmybutton"
                    elif not rindorm15 and not ev_rindorm15.missed:
                        text _("Boundaries")

                    if cafe20 and show_complete:
                        textbutton _("Nothing Was Missing, Except Me {b}✓{/b}") action Replay("cafe20", locked=False) text_style "modmybutton"
                    elif not cafe20 and not ev_cafe20.missed:
                        text _("Nothing Was Missing, Except Me")

                    if rindorm20 and show_complete:
                        textbutton _("Delirium {b}✓{/b}") action Replay("rindorm20", locked=False) text_style "modmybutton"
                    elif not rindorm20 and not ev_rindorm20.missed:
                        text _("Delirium")

                    if cafe25 and show_complete:
                        textbutton _("Good Day, Humans {b}✓{/b}") action Replay("cafe25", locked=False) text_style "modmybutton"
                    elif not cafe25 and not ev_cafe25.missed:
                        text _("Good Day, Humans")

                    if rindorm25 and show_complete:
                        textbutton _("Sock Fetish {b}✓{/b}") action Replay("rindorm25", locked=False) text_style "modmybutton"
                    elif not rindorm25 and not ev_rindorm25.missed:
                        text _("Sock Fetish")

                    if cafe30 and show_complete:
                        textbutton _("Nothing Was Different {b}✓{/b}") action Replay("cafe30", locked=False) text_style "modmybutton"
                    elif not cafe30 and not ev_cafe30.missed:
                        text _("Nothing Was Different")

                    if rindorm30 and show_complete:
                        textbutton _("Two Steps Back {b}✓{/b}") action Replay("rindorm30", locked=False) text_style "modmybutton"
                    elif not rindorm30 and not ev_rindorm30.missed:
                        text _("Two Steps Back")

                    if rindorm35 and show_complete:
                        textbutton _("Ten Steps Forward {b}✓{/b}") action Replay("rindorm35", locked=False) text_style "modmybutton"
                    elif not rindorm35 and not ev_rindorm35.missed:
                        text _("Ten Steps Forward")

                    if cafe35 and show_complete:
                        textbutton _("I Died With You {b}✓{/b}") action Replay("cafe35", locked=False) text_style "modmybutton"
                    elif ev_cafe35.missed and show_complete:
                        text _("{color=EF1A1A}{s}Love Life, Let Go{/s}{/color}")
                    elif not cafe35 and not ev_cafe35.missed:
                        text _("I Died With You")

                    text _("---------------------------------------------")

                    if cafe40 and show_complete:
                        textbutton _("Sketchy Basement {b}✓{/b}") action Replay("cafe40", locked=False) text_style "modmybutton"
                    elif not cafe40 and not ev_cafe40.missed:
                        text _("Sketchy Basement")

                    if rindorm40 and show_complete:
                        textbutton _("Semantics {b}✓{/b}") action Replay("rindorm40", locked=False) text_style "modmybutton"
                    elif not rindorm40 and not ev_rindorm40.missed:
                        text _("Semantics")

                    if cafe45 and show_complete:
                        textbutton _("Debatably Bisexual Musicians {b}✓{/b}") action Replay("cafe45", locked=False) text_style "modmybutton"
                    elif not cafe45 and not ev_cafe45.missed:
                        text _("Debatably Bisexual Musicians")

                    if rindorm45 and show_complete:
                        textbutton _("The Art of Never Knowing {b}✓{/b}") action Replay("rindorm45", locked=False) text_style "modmybutton"
                    elif not rindorm45 and not ev_rindorm45.missed:
                        text _("The Art of Never Knowing")

                    if cafe50 and show_complete:
                        textbutton _("The Paragon of Not Worrying About Stuff {b}✓{/b}") action Replay("cafe50", locked=False) text_style "modmybutton"
                    elif not cafe50 and not ev_cafe50.missed:
                        text _("The Paragon of Not Worrying About Stuff")

                    if rindorm50 and show_complete:
                        textbutton _("Technicolored Happiness Explosion {b}✓{/b}") action Replay("rindorm50", locked=False) text_style "modmybutton"
                    elif not rindorm50 and not ev_rindorm50.missed:
                        text _("Technicolored Happiness Explosion")

                    if rindorm50special and show_complete:
                        textbutton _("Lifejacket {b}✓{/b}") action Replay("rindorm50special", locked=False) text_style "modmybutton"
                    elif not rindorm50special and not ev_rindorm50special.missed:
                        text _("Lifejacket")

                    if rindate50 and show_complete:
                        textbutton _("The Happiest Girl in the World {b}✓{/b}") action Replay("rindate50", locked=False) text_style "modmybutton"
                    elif ev_rindate50.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Raw Sting of Lacerated Skin{/s}{/color}")
                    elif not rindate50 and not ev_rindate50.missed:
                        text _("The Happiest Girl in the World")

                    text _("---------------------------------------------")

                    if rindorm55 and show_complete:
                        textbutton _("Disaster Lesbian {b}✓{/b}") action Replay("rindorm55", locked=False) text_style "modmybutton"
                    elif not rindorm55 and not ev_rindorm55.missed:
                        text _("Disaster Lesbian")

                    if rindorm55p2 and show_complete:
                        textbutton _("Hot Boy Summer {b}✓{/b}") action Replay("rindorm55p2", locked=False) text_style "modmybutton"
                    elif not rindorm55p2 and not ev_rindorm55p2.missed:
                        text _("Hot Boy Summer")

                    if rinspecial55 and show_complete:
                        textbutton _("Ever Fallen In Love {b}✓{/b}") action Replay("rinspecial55", locked=False) text_style "modmybutton"
                    elif not rinspecial55 and not ev_rinspecial55.missed:
                        text _("Ever Fallen In Love")

                    text _("---------------------------------------------")

                    if rinspring1 and show_complete:
                        textbutton _("Anthem of the Heart {b}✓{/b}") action Replay("rinspring1", locked=False) text_style "modmybutton"
                    elif not rinspring1 and not ev_rinspring1.missed:
                        text _("Anthem of the Heart")

                    if rinspring2 and show_complete:
                        textbutton _("Voices of a Distant Star {b}✓{/b}") action Replay("rinspring2", locked=False) text_style "modmybutton"
                    elif not rinspring2 and not ev_rinspring2.missed:
                        text _("Voices of a Distant Star")

                    if rinspring3 and show_complete:
                        textbutton _("Sex Dreams {b}✓{/b}") action Replay("rinspring3", locked=False) text_style "modmybutton"
                    elif ev_rinspring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}Virgin Nightmares{/s}{/color}")
                    elif not rinspring3 and not ev_rinspring3.missed:
                        text _("Sex Dreams")

                    if rinspring4 and show_complete:
                        textbutton _("Voice of Reason {b}✓{/b}") action Replay("rinspring4", locked=False) text_style "modmybutton"
                    elif not rinspring4 and not ev_rinspring4.missed:
                        text _("Voice of Reason")

                    if rinspring5 and show_complete:
                        textbutton _("Dear Sensei (Red Sea) {b}✓{/b}") action Replay("rinspring5", locked=False) text_style "modmybutton"
                    elif not rinspring5 and not ev_rinspring5.missed:
                        text _("Dear Sensei (Red Sea)")

                    if rinspring6 and show_complete:
                        textbutton _("Love Long Overdue {b}✓{/b}") action Replay("rinspring6", locked=False) text_style "modmybutton"
                    elif not rinspring6 and not ev_rinspring6.missed:
                        text _("Love Long Overdue")

                    if dormwarsfiverin1 and show_complete:
                        textbutton _("The First Time Since the Last Time {b}✓{/b}") action Replay("dormwarsfiverin1", locked=False) text_style "modmybutton"
                    elif not dormwarsfiverin1 and not ev_dormwarsfiverin1.missed:
                        text _("The First Time Since the Last Time")

                    if rinspring7 and show_complete:
                        textbutton _("Days to Waste {b}✓{/b}") action Replay("rinspring7", locked=False) text_style "modmybutton"
                    elif not rinspring7 and not ev_rinspring7.missed:
                        text _("Days to Waste")

                    if rinspring8 and show_complete:
                        textbutton _("Table for Two {b}✓{/b}") action Replay("rinspring8", locked=False) text_style "modmybutton"
                    elif not rinspring8 and not ev_rinspring8.missed:
                        text _("Table for Two")

                    if rinspring9 and show_complete:
                        textbutton _("Transpacific Sadness Symposium VIII: AN ATOM (ME) AND ADAM (YOU) {b}✓{/b}") action Replay("rinspring9", locked=False) text_style "modmybutton"
                    elif not rinspring9 and not ev_rinspring9.missed:
                        text _("Transpacific Sadness Symposium VIII: AN ATOM (ME) AND ADAM (YOU)")

                #SANAEVENT

                if showgirl == "Sana":

                    if firsttimebar and show_complete:
                        textbutton _("Family Business {b}✓{/b}") action Replay("firsttimebar", locked=False) text_style "modmybutton"
                    elif not firsttimebar and not ev_firsttimebar.missed:
                        text _("Family Business")

                    if sanafirsthall and show_complete:
                        textbutton _("Nothing to Do {b}✓{/b}") action Replay("sanafirsthall", locked=False) text_style "modmybutton"
                    elif not sanafirsthall and not ev_sanafirsthall.missed:
                        text _("Nothing to Do")

                    if bar5 and show_complete:
                        textbutton _("The Bare Minimum {b}✓{/b}") action Replay("bar5", locked=False) text_style "modmybutton"
                    elif not bar5 and not ev_bar5.missed:
                        text _("The Bare Minimum")

                    if sanadorm5 and show_complete:
                        textbutton _("Recluse {b}✓{/b}") action Replay("sanadorm5", locked=False) text_style "modmybutton"
                    elif not sanadorm5 and not ev_sanadorm5.missed:
                        text _("Recluse")

                    if bar10 and show_complete:
                        textbutton _("Supermom {b}✓{/b}") action Replay("bar10", locked=False) text_style "modmybutton"
                    elif not bar10 and not ev_bar10.missed:
                        text _("Supermom")

                    if sanadorm10 and show_complete:
                        textbutton _("Anywhere At All {b}✓{/b}") action Replay("sanadorm10", locked=False) text_style "modmybutton"
                    elif not sanadorm10 and not ev_sanadorm10.missed:
                        text _("Anywhere At All")

                    if bar15 and show_complete:
                        textbutton _("Carry Me Home {b}✓{/b}") action Replay("bar15", locked=False) text_style "modmybutton"
                    elif not bar15 and not ev_bar15.missed:
                        text _("Carry Me Home")

                    if sanadorm15 and show_complete:
                        textbutton _("Shaking The Tree {b}✓{/b}") action Replay("sanadorm15", locked=False) text_style "modmybutton"
                    elif not sanadorm15 and not ev_sanadorm15.missed:
                        text _("Shaking The Tree")

                    if bar20 and show_complete:
                        textbutton _("Scouting Mission {b}✓{/b}") action Replay("bar20", locked=False) text_style "modmybutton"
                    elif not bar20 and not ev_bar20.missed:
                        text _("Scouting Mission")

                    if sanadorm20 and show_complete:
                        textbutton _("Nice Weather We're Having {b}✓{/b}") action Replay("sanadorm20", locked=False) text_style "modmybutton"
                    elif not sanadorm20 and not ev_sanadorm20.missed:
                        text _("Nice Weather We're Having")

                    if bar25 and show_complete:
                        textbutton _("Life is a Tomato {b}✓{/b}") action Replay("bar25", locked=False) text_style "modmybutton"
                    elif not bar25 and not ev_bar25.missed:
                        text _("Life is a Tomato")

                    if sanadorm25 and show_complete:
                        textbutton _("The Girl in the Black Dress {b}✓{/b}") action Replay("sanadorm25", locked=False) text_style "modmybutton"
                    elif not sanadorm25 and not ev_sanadorm25.missed:
                        text _("The Girl in the Black Dress")

                    if bar30 and show_complete:
                        textbutton _("Self-Medication {b}✓{/b}") action Replay("bar30", locked=False) text_style "modmybutton"
                    elif not bar30 and not ev_bar30.missed:
                        text _("Self-Medication")

                    if sanadorm30 and show_complete:
                        textbutton _("Tortoises and the Concept of Friendship {b}✓{/b}") action Replay("sanadorm30", locked=False) text_style "modmybutton"
                    elif not sanadorm30 and not ev_sanadorm30.missed:
                        text _("Tortoises and the Concept of Friendship")

                    text _("---------------------------------------------")

                    if bar35 and show_complete:
                        textbutton _("Purest Intentions {b}✓{/b}") action Replay("bar35", locked=False) text_style "modmybutton"
                    elif not bar35 and not ev_bar35.missed:
                        text _("Purest Intentions")

                    if sanadorm35 and show_complete:
                        textbutton _("Waiting for Anything {b}✓{/b}") action Replay("sanadorm35", locked=False) text_style "modmybutton"
                    elif not sanadorm35 and not ev_sanadorm35.missed:
                        text _("Waiting for Anything")

                    if bar40 and show_complete:
                        textbutton _("Closer to Me {b}✓{/b}") action Replay("bar40", locked=False) text_style "modmybutton"
                    elif not bar40 and not ev_bar40.missed:
                        text _("Closer to Me")

                    if sanadorm40 and show_complete:
                        textbutton _("The Inside of a Triangle {b}✓{/b}") action Replay("sanadorm40", locked=False) text_style "modmybutton"
                    elif not sanadorm40 and not ev_sanadorm40.missed:
                        text _("The Inside of a Triangle")

                    if bar45 and show_complete:
                        textbutton _("Sweet Vermouth {b}✓{/b}") action Replay("bar45", locked=False) text_style "modmybutton"
                    elif not bar45 and not ev_bar45.missed:
                        text _("Sweet Vermouth")

                    if sanadorm45 and show_complete:
                        textbutton _("The Complete Absence of Everything {b}✓{/b}") action Replay("sanadorm45", locked=False) text_style "modmybutton"
                    elif not sanadorm45 and not ev_sanadorm45.missed:
                        text _("The Complete Absence of Everything")

                    if sanadorm50 and show_complete:
                        textbutton _("Mine (Yours) {b}✓{/b}") action Replay("sanadorm50", locked=False) text_style "modmybutton"
                    elif not sanadorm50 and not ev_sanadorm50.missed:
                        text _("Mine (Yours)")

                    if bar50 and show_complete:
                        textbutton _("Melatonin {b}✓{/b}") action Replay("bar50", locked=False) text_style "modmybutton"
                    elif ev_bar50.missed and show_complete:
                        text _("{color=EF1A1A}{s}Why Don't You Ever Lock the Door?{/s}{/color}")
                    elif not bar50 and not ev_bar50.missed:
                        text _("Melatonin")

                    text _("---------------------------------------------")

                    if bar55 and show_complete:
                        textbutton _("Black Sandy Beaches {b}✓{/b}") action Replay("bar55", locked=False) text_style "modmybutton"
                    elif not bar55 and not ev_bar55.missed:
                        text _("Black Sandy Beaches")

                    if ayanesanabeach2 and show_complete:
                        textbutton _("Ad Meliora {b}✓{/b}") action Replay("ayanesanabeach2", locked=False) text_style "modmybutton"
                    elif ev_ayanesanabeach2.missed and show_complete:
                        text _("{color=EF1A1A}{s}It's All Wrong{/s}{/color}")
                    elif not ayanesanabeach2 and not ev_ayanesanabeach2.missed:
                        text _("Ad Meliora")

                    if ayanesanabeach3 and show_complete:
                        textbutton _("It Comes to Claim Us All {b}✓{/b}") action Replay("ayanesanabeach3", locked=False) text_style "modmybutton"
                    elif not ayanesanabeach3 and not ev_ayanesanabeach3.missed:
                        text _("It Comes to Claim Us All")

                    if ayanesanabeach4 and show_complete:
                        textbutton _("Ad Infinitum {b}✓{/b}") action Replay("ayanesanabeach4", locked=False) text_style "modmybutton"
                    elif ev_ayanesanabeach4.missed and show_complete:
                        text _("{color=EF1A1A}{s}Gods Don't Smile Down{/s}{/color}")
                    elif not ayanesanabeach4 and not ev_ayanesanabeach4.missed:
                        text _("Ad Infinitum")

                    text _("---------------------------------------------")

                    if sanaspring1 and show_complete:
                        textbutton _("Taller {b}✓{/b}") action Replay("sanaspring1", locked=False) text_style "modmybutton"
                    elif not sanaspring1 and not ev_sanaspring1.missed:
                        text _("Taller")

                    if sanaspring2 and show_complete:
                        textbutton _("Stutter-Step {b}✓{/b}") action Replay("sanaspring2", locked=False) text_style "modmybutton"
                    elif not sanaspring2 and not ev_sanaspring2.missed:
                        text _("Stutter-Step")

                    if sanaspring3 and show_complete:
                        textbutton _("Weak Man, Weak Boy {b}✓{/b}") action Replay("sanaspring3", locked=False) text_style "modmybutton"
                    elif not sanaspring3 and not ev_sanaspring3.missed:
                        text _("Weak Man, Weak Boy")

                    if sanaspring4 and show_complete:
                        textbutton _("Transpacific Sadness Symposium III: TWO-HEADED HORSE {b}✓{/b}") action Replay("sanaspring4", locked=False) text_style "modmybutton"
                    elif not sanaspring4 and not ev_sanaspring4.missed:
                        text _("Transpacific Sadness Symposium III: TWO-HEADED HORSE")

                    if sanainvite1 and show_complete:
                        textbutton _("Piggy & The Boulder {b}✓{/b}") action Replay("sanainvite1", locked=False) text_style "modmybutton"
                    elif not sanainvite1 and not ev_sanainvite1.missed:
                        text _("{color=778EFF}Piggy & The Boulder{/color}")

                    if sanainvite2 and show_complete:
                        textbutton _("Four Letter Words {b}✓{/b}") action Replay("sanainvite2", locked=False) text_style "modmybutton"
                    elif not sanainvite2 and not ev_sanainvite2.missed:
                        text _("{color=778EFF}Four Letter Words{/color}")

                    if beachsixsana1 and show_complete:
                        textbutton _("Despicable Meat Toilet {b}✓{/b}") action Replay("beachsixsana1", locked=False) text_style "modmybutton"
                    elif not beachsixsana1 and not ev_beachsixsana1.missed:
                        text _("Despicable Meat Toilet")

                    if sanaspring5 and show_complete:
                        textbutton _("Addict in Training {b}✓{/b}") action Replay("sanaspring5", locked=False) text_style "modmybutton"
                    elif ev_sanaspring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}Failing the Sex Exam{/s}{/color}")
                    elif not sanaspring5 and not ev_sanaspring5.missed:
                        text _("Addict in Training")

                    if sanaspring6 and show_complete:
                        textbutton _("Counting Down From Four {b}✓{/b}") action Replay("sanaspring6", locked=False) text_style "modmybutton"
                    elif not sanaspring6 and not ev_sanaspring6.missed:
                        text _("Counting Down From Four")

                #SARAEVENT

                if showgirl == "Sara":

                    if saradate1 and show_complete:
                        textbutton _("A Woman's Heart {b}✓{/b}") action Replay("saradate1", locked=False) text_style "modmybutton"
                    elif not saradate1 and not ev_saradate1.missed:
                        text _("A Woman's Heart")

                    if saralust5 and show_complete:
                        textbutton _("Zero Friction {b}✓{/b}") action Replay("saralust5", locked=False) text_style "modmybutton"
                    elif ev_saralust5.missed and show_complete:
                        text _("{color=EF1A1A}{s}The World Moves too Quickly{/s}{/color}")
                    elif not saralust5 and not ev_saralust5.missed:
                        text _("{color=FF85FD}Zero Friction{/color}")

                    if sarainvite1 and show_complete:
                        textbutton _("Third Wheel {b}✓{/b}") action Replay("sarainvite1", locked=False) text_style "modmybutton"
                    elif not sarainvite1 and not ev_sarainvite1.missed:
                        text _("{color=778EFF}Third Wheel{/color}")

                    if sarainvite2 and show_complete:
                        textbutton _("A Mostly Empty Home {b}✓{/b}") action Replay("sarainvite2", locked=False) text_style "modmybutton"
                    elif not sarainvite2 and not ev_sarainvite2.missed:
                        text _("{color=778EFF}A Mostly Empty Home{/color}")

                    if saralust10 and show_complete:
                        textbutton _("Medical Assistance {b}✓{/b}") action Replay("saralust10", locked=False) text_style "modmybutton"
                    elif ev_saralust10.missed and show_complete:
                        text _("{color=EF1A1A}{s}Almost Burning{/s}{/color}")
                    elif not saralust10 and not ev_saralust10.missed:
                        text _("{color=FF85FD}Medical Assistance{/color}")

                    text _("---------------------------------------------")

                    if saradate10 and show_complete:
                        textbutton _("Uptown Girl {b}✓{/b}") action Replay("saradate10", locked=False) text_style "modmybutton"
                    elif not saradate10 and not ev_saradate10.missed:
                        text _("Uptown Girl")

                    if sarabar20 and show_complete:
                        textbutton _("She's Always a Woman {b}✓{/b}") action Replay("sarabar20", locked=False) text_style "modmybutton"
                    elif ev_sarabar20.missed and show_complete:
                        text _("{color=EF1A1A}{s}I've Loved These Days{/s}{/color}")
                    elif not sarabar20 and not ev_sarabar20.missed:
                        text _("She's Always a Woman")

                    if sarabar25 and show_complete:
                        textbutton _("Tell Me When {b}✓{/b}") action Replay("sarabar25", locked=False) text_style "modmybutton"
                    elif not sarabar25 and not ev_sarabar25.missed:
                        text _("Tell Me When")

                    if sarabar25p2 and show_complete:
                        textbutton _("The Place She Falls Asleep At Night {b}✓{/b}") action Replay("sarabar25p2", locked=False) text_style "modmybutton"
                    elif not sarabar25p2 and not ev_sarabar25p2.missed:
                        text _("The Place She Falls Asleep At Night")

                    if saralust20 and show_complete:
                        textbutton _("Engulfed {b}✓{/b}") action Replay("saralust20", locked=False) text_style "modmybutton"
                    elif ev_saralust20.missed and show_complete:
                        text _("{color=EF1A1A}{s}Swallowed Whole{/s}{/color}")
                    elif not saralust20 and not ev_saralust20.missed:
                        text _("{color=FF85FD}Engulfed{/color}")

                    text _("---------------------------------------------")

                    if saraspecial30p1 and show_complete:
                        textbutton _("The Creaking of the Seventh Step {b}✓{/b}") action Replay("saraspecial30p1", locked=False) text_style "modmybutton"
                    elif not saraspecial30p1 and not ev_saraspecial30p1.missed:
                        text _("The Creaking of the Seventh Step")

                    if saraspecial30p2 and show_complete:
                        textbutton _("Halfway Down the Wishing Well {b}✓{/b}") action Replay("saraspecial30p2", locked=False) text_style "modmybutton"
                    elif ev_saraspecial30p2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Zoopledoop{/s}{/color}")
                    elif not saraspecial30p2 and not ev_saraspecial30p2.missed:
                        text _("Halfway Down the Wishing Well")

                    if sarabar30 and show_complete:
                        textbutton _("Nicolas Cage {b}✓{/b}") action Replay("sarabar30", locked=False) text_style "modmybutton"
                    elif not sarabar30 and not ev_sarabar30.missed:
                        text _("Nicolas Cage")

                    text _("---------------------------------------------")

                    if saracamp1 and show_complete:
                        textbutton _("The One With A Happy Ending {b}✓{/b}") action Replay("saracamp1", locked=False) text_style "modmybutton"
                    elif not saracamp1 and not ev_saracamp1.missed:
                        text _("The One With A Happy Ending")

                    if saracamp2 and show_complete:
                        textbutton _("I've Been Thinking About Leaving This Place {b}✓{/b}") action Replay("saracamp2", locked=False) text_style "modmybutton"
                    elif not saracamp2 and not ev_saracamp2.missed:
                        text _("I've Been Thinking About Leaving This Place")

                    if saraspring1 and show_complete:
                        textbutton _("Details in the Fabric {b}✓{/b}") action Replay("saraspring1", locked=False) text_style "modmybutton"
                    elif not saraspring1 and not ev_saraspring1.missed:
                        text _("Details in the Fabric")

                    if saraspring2 and show_complete:
                        textbutton _("Silent Night (Onee-san) {b}✓{/b}") action Replay("saraspring2", locked=False) text_style "modmybutton"
                    elif ev_saraspring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Sister Says No{/s}{/color}")
                    elif not saraspring2 and not ev_saraspring2.missed:
                        text _("Silent Night (Onee-san)")

                    if saraspring3 and show_complete:
                        textbutton _("Worthless Me {b}✓{/b}") action Replay("saraspring3", locked=False) text_style "modmybutton"
                    elif ev_saraspring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}Worthless You{/s}{/color}")
                    elif not saraspring3 and not ev_saraspring3.missed:
                        text _("Worthless Me")

                    if saraspring4 and show_complete:
                        textbutton _("Two for the Price of One {b}✓{/b}") action Replay("saraspring4", locked=False) text_style "modmybutton"
                    elif ev_saraspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}One for the Price of Two{/s}{/color}")
                    elif not saraspring4 and not ev_saraspring4.missed:
                        text _("Two for the Price of One")

                    if saraspring5 and show_complete:
                        textbutton _("The Puppeteer {b}✓{/b}") action Replay("saraspring5", locked=False) text_style "modmybutton"
                    elif ev_saraspring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Puppet{/s}{/color}")
                    elif not saraspring5 and not ev_saraspring5.missed:
                        text _("The Puppeteer")

                    if saraspring6 and show_complete:
                        textbutton _("The Most Beautiful Bitter Fruit {b}✓{/b}") action Replay("saraspring6", locked=False) text_style "modmybutton"
                    elif ev_saraspring6.missed and show_complete:
                        text _("{color=EF1A1A}{s}Sister Says No{/s}{/color}")
                    elif not saraspring6 and not ev_saraspring6.missed:
                        text _("The Most Beautiful Bitter Fruit")

                    if saraspring7 and show_complete:
                        textbutton _("You and I in Unison {b}✓{/b}") action Replay("saraspring7", locked=False) text_style "modmybutton"
                    elif not saraspring7 and not ev_saraspring7.missed:
                        text _("You and I in Unison")

                    if dormwarssixsara1 and show_complete:
                        textbutton _("Ring of Fire {b}✓{/b}") action Replay("dormwarssixsara1", locked=False) text_style "modmybutton"
                    elif ev_dormwarssixsara1.missed and show_complete:
                        text _("{color=EF1A1A}{s}Empire of Dirt{/s}{/color}")
                    elif not dormwarssixsara1 and not ev_dormwarssixsara1.missed:
                        text _("Ring of Fire")

                #TOUKAEVENT

                if showgirl == "Touka":

                    if toukafirsthall and show_complete:
                        textbutton _("Spontaneous Sentimentality {b}✓{/b}") action Replay("toukafirsthall", locked=False) text_style "modmybutton"
                    elif not toukafirsthall and not ev_toukafirsthall.missed:
                        text _("Spontaneous Sentimentality")

                    if toukastreets1 and show_complete:
                        textbutton _("Trial Period {b}✓{/b}") action Replay("toukastreets1", locked=False) text_style "modmybutton"
                    elif not toukastreets1 and not ev_toukastreets1.missed:
                        text _("Trial Period")

                    if toukadorm1 and show_complete:
                        textbutton _("Fish Out of Water {b}✓{/b}") action Replay("toukadorm1", locked=False) text_style "modmybutton"
                    elif not toukadorm1 and not ev_toukadorm1.missed:
                        text _("Fish Out of Water")

                    if toukastreets5 and show_complete:
                        textbutton _("A Brief Moment in Time {b}✓{/b}") action Replay("toukastreets5", locked=False) text_style "modmybutton"
                    elif not toukastreets5 and not ev_toukastreets5.missed:
                        text _("A Brief Moment in Time")

                    if toukadorm5 and show_complete:
                        textbutton _("Loser {b}✓{/b}") action Replay("toukadorm5", locked=False) text_style "modmybutton"
                    elif not toukadorm5 and not ev_toukadorm5.missed:
                        text _("Loser")

                    if toukadorm10 and show_complete:
                        textbutton _("House Call {b}✓{/b}") action Replay("toukadorm10", locked=False) text_style "modmybutton"
                    elif not toukadorm10 and not ev_toukadorm10.missed:
                        text _("House Call")

                    if toukaspecial15 and show_complete:
                        textbutton _("A Commoner's Tour of Summer {b}✓{/b}") action Replay("toukaspecial15", locked=False) text_style "modmybutton"
                    elif not toukaspecial15 and not ev_toukaspecial15.missed:
                        text _("A Commoner's Tour of Summer")

                    if toukaspecial15p2 and show_complete:
                        textbutton _("Red-ish Light District {b}✓{/b}") action Replay("toukaspecial15p2", locked=False) text_style "modmybutton"
                    elif not toukaspecial15p2 and not ev_toukaspecial15p2.missed:
                        text _("Red-ish Light District")

                    if toukaspecial15p3 and show_complete:
                        textbutton _("Something Less Lonely {b}✓{/b}") action Replay("toukaspecial15p3", locked=False) text_style "modmybutton"
                    elif not toukaspecial15p3 and not ev_toukaspecial15p3.missed:
                        text _("Something Less Lonely")

                    text _("---------------------------------------------")

                    if toukaarchery20 and show_complete:
                        textbutton _("Kryptonite {b}✓{/b}") action Replay("toukaarchery20", locked=False) text_style "modmybutton"
                    elif not toukaarchery20 and not ev_toukaarchery20.missed:
                        text _("Kryptonite")

                    if toukadorm25p1 and show_complete:
                        textbutton _("For Want Of {b}✓{/b}") action Replay("toukadorm25p1", locked=False) text_style "modmybutton"
                    elif not toukadorm25p1 and not ev_toukadorm25p1.missed:
                        text _("For Want Of")

                    if toukadorm25p2 and show_complete:
                        textbutton _("To Lift This Aching Head {b}✓{/b}") action Replay("toukadorm25p2", locked=False) text_style "modmybutton"
                    elif not toukadorm25p2 and not ev_toukadorm25p2.missed:
                        text _("To Lift This Aching Head")

                    if toukadorm25p3 and show_complete:
                        textbutton _("Under My Wing {b}✓{/b}") action Replay("toukadorm25p3", locked=False) text_style "modmybutton"
                    elif not toukadorm25p3 and not ev_toukadorm25p3.missed:
                        text _("Under My Wing")

                    text _("---------------------------------------------")

                    if toukacamp1 and show_complete:
                        textbutton _("Salt in the Wound {b}✓{/b}") action Replay("toukacamp1", locked=False) text_style "modmybutton"
                    elif not toukacamp1 and not ev_toukacamp1.missed:
                        text _("Salt in the Wound")

                    if toukaspring1 and show_complete:
                        textbutton _("Blankets & Ball-Gags {b}✓{/b}") action Replay("toukaspring1", locked=False) text_style "modmybutton"
                    elif not toukaspring1 and not ev_toukaspring1.missed:
                        text _("Blankets & Ball-Gags")

                    if toukaspring2 and show_complete:
                        textbutton _("Artisan Hands {b}✓{/b}") action Replay("toukaspring2", locked=False) text_style "modmybutton"
                    elif not toukaspring2 and not ev_toukaspring2.missed:
                        text _("Artisan Hands")

                    if toukaspring3 and show_complete:
                        textbutton _("One Thousand Penises {b}✓{/b}") action Replay("toukaspring3", locked=False) text_style "modmybutton"
                    elif not toukaspring3 and not ev_toukaspring3.missed:
                        text _("One Thousand Penises")

                    if toukaspring4 and show_complete:
                        textbutton _("Come For Me {b}✓{/b}") action Replay("toukaspring4", locked=False) text_style "modmybutton"
                    elif not toukaspring4 and not ev_toukaspring4.missed:
                        text _("Come For Me")

                    if toukaspring5 and show_complete:
                        textbutton _("One of the Girls {b}✓{/b}") action Replay("toukaspring5", locked=False) text_style "modmybutton"
                    elif not toukaspring5 and not ev_toukaspring5.missed:
                        text _("One of the Girls")

                    if toukaspring6 and show_complete:
                        textbutton _("Spermicide {b}✓{/b}") action Replay("toukaspring6", locked=False) text_style "modmybutton"
                    elif not toukaspring6 and not ev_toukaspring6.missed:
                        text _("Spermicide")

                    if toukaspring7 and show_complete:
                        textbutton _("The Corpse of Seth Rogen {b}✓{/b}") action Replay("toukaspring7", locked=False) text_style "modmybutton"
                    elif not toukaspring7 and not ev_toukaspring7.missed:
                        text _("The Corpse of Seth Rogen")

                    if toukaspring8 and show_complete:
                        textbutton _("One Step Closer {b}✓{/b}") action Replay("toukaspring8", locked=False) text_style "modmybutton"
                    elif not toukaspring8 and not ev_toukaspring8.missed:
                        text _("One Step Closer")

                #TSUBASAEVENT

                if showgirl == "Tsubasa":

                    if tsubasadate1 and show_complete:
                        textbutton _("Everbloom (Pride of the Sinful Sort) {b}✓{/b}") action Replay("tsubasadate1", locked=False) text_style "modmybutton"
                    elif not tsubasadate1 and not ev_tsubasadate1.missed:
                        text _("Everbloom (Pride of the Sinful Sort)")

                    if tsubasadate1p2 and show_complete:
                        textbutton _("The Deep End {b}✓{/b}") action Replay("tsubasadate1p2", locked=False) text_style "modmybutton"
                    elif not tsubasadate1p2 and not ev_tsubasadate1p2.missed:
                        text _("The Deep End")

                    text _("---------------------------------------------")

                    if tsubasaspecial15 and show_complete:
                        textbutton _("Heart of Gold {b}✓{/b}") action Replay("tsubasaspecial15", locked=False) text_style "modmybutton"
                    elif not tsubasaspecial15 and not ev_tsubasaspecial15.missed:
                        text _("Heart of Gold")

                    if tsubasadate20 and show_complete:
                        textbutton _("Playing God {b}✓{/b}") action Replay("tsubasadate20", locked=False) text_style "modmybutton"
                    elif not tsubasadate20 and not ev_tsubasadate20.missed:
                        text _("Playing God")

                    if tsubasaspecial20 and show_complete:
                        textbutton _("The Lucky Few {b}✓{/b}") action Replay("tsubasaspecial20", locked=False) text_style "modmybutton"
                    elif not tsubasaspecial20 and not ev_tsubasaspecial20.missed:
                        text _("The Lucky Few")

                    text _("---------------------------------------------")

                    if tsubasaspring1 and show_complete:
                        textbutton _("The Bird & The Worm {b}✓{/b}") action Replay("tsubasaspring1", locked=False) text_style "modmybutton"
                    elif not tsubasaspring1 and not ev_tsubasaspring1.missed:
                        text _("The Bird & The Worm")

                    if tsubasaspring2 and show_complete:
                        textbutton _("Petite Sirah {b}✓{/b}") action Replay("tsubasaspring2", locked=False) text_style "modmybutton"
                    elif ev_tsubasaspring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}Bum Wine{/s}{/color}")
                    elif not tsubasaspring2 and not ev_tsubasaspring2.missed:
                        text _("Petite Sirah")

                    if tsubasaspring3 and show_complete:
                        textbutton _("The Pleasures of the Flesh {b}✓{/b}") action Replay("tsubasaspring3", locked=False) text_style "modmybutton"
                    elif ev_tsubasaspring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}It Changes With The Light{/s}{/color}")
                    elif not tsubasaspring3 and not ev_tsubasaspring3.missed:
                        text _("The Pleasures of the Flesh")

                    if christmastsubasa1 and show_complete:
                        textbutton _("Yes, Mother {b}✓{/b}") action Replay("christmastsubasa1", locked=False) text_style "modmybutton"
                    elif ev_christmastsubasa1.missed and show_complete:
                        text _("{color=EF1A1A}{s}You Are a Very Bad Boy{/s}{/color}")
                    elif not christmastsubasa1 and not ev_christmastsubasa1.missed:
                        text _("Yes, Mother")

                    if tsubasaspring4 and show_complete:
                        textbutton _("Hands-On Learning {b}✓{/b}") action Replay("tsubasaspring4", locked=False) text_style "modmybutton"
                    elif ev_tsubasaspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Good Guy Approach{/s}{/color}")
                    elif not tsubasaspring4 and not ev_tsubasaspring4.missed:
                        text _("Hands-On Learning")

                    if tsubasaspring5 and show_complete:
                        textbutton _("For the Sake of Brevity {b}✓{/b}") action Replay("tsubasaspring5", locked=False) text_style "modmybutton"
                    elif ev_tsubasaspring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}Solitary Bath Time{/s}{/color}")
                    elif not tsubasaspring5 and not ev_tsubasaspring5.missed:
                        text _("For the Sake of Brevity")

                    if tsubasaspring6 and show_complete:
                        textbutton _("When We Dead Awaken {b}✓{/b}") action Replay("tsubasaspring6", locked=False) text_style "modmybutton"
                    elif not tsubasaspring6 and not ev_tsubasaspring6.missed:
                        text _("When We Dead Awaken")

                    if tsubasaspring7 and show_complete:
                        textbutton _("Climbing Up the Ladder {b}✓{/b}") action Replay("tsubasaspring7", locked=False) text_style "modmybutton"
                    elif not tsubasaspring7 and not ev_tsubasaspring7.missed:
                        text _("Climbing Up the Ladder")

                    if tsubasaspring8 and show_complete:
                        textbutton _("Human Veal {b}✓{/b}") action Replay("tsubasaspring8", locked=False) text_style "modmybutton"
                    elif ev_tsubasaspring8.missed and show_complete:
                        text _("{color=EF1A1A}{s}Cage Legs{/s}{/color}")
                    elif not tsubasaspring8 and not ev_tsubasaspring8.missed:
                        text _("Human Veal")

                #TSUKASAEVENT

                if showgirl == "Tsukasa":

                    if tsukasaspecial1 and show_complete:
                        textbutton _("National Tsukasa Day {b}✓{/b}") action Replay("tsukasaspecial1", locked=False) text_style "modmybutton"
                    elif not tsukasaspecial1 and not ev_tsukasaspecial1.missed:
                        text _("National Tsukasa Day")

                    if tsukasaspecial1p2 and show_complete:
                        textbutton _("Jeeves Tsukioka XIII {b}✓{/b}") action Replay("tsukasaspecial1p2", locked=False) text_style "modmybutton"
                    elif not tsukasaspecial1p2 and not ev_tsukasaspecial1p2.missed:
                        text _("Jeeves Tsukioka XIII")

                    text _("---------------------------------------------")

                    if tsukasaspring1 and show_complete:
                        textbutton _("Vow of Silence (Pole Position) {b}✓{/b}") action Replay("tsukasaspring1", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring1.missed and show_complete:
                        text _("{color=EF1A1A}{s}YOU{/s}{/color}")
                    elif not tsukasaspring1 and not ev_tsukasaspring1.missed:
                        text _("Vow of Silence (Pole Position)")

                    if tsukasaspring2 and show_complete:
                        textbutton _("Blood & Sunset {b}✓{/b}") action Replay("tsukasaspring2", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring2.missed and show_complete:
                        text _("{color=EF1A1A}{s}ARE{/s}{/color}")
                    elif not tsukasaspring2 and not ev_tsukasaspring2.missed:
                        text _("Blood & Sunset")

                    if tsukasaspring3 and show_complete:
                        textbutton _("Failsafe {b}✓{/b}") action Replay("tsukasaspring3", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring3.missed and show_complete:
                        text _("{color=EF1A1A}{s}WEAK{/s}{/color}")
                    elif not tsukasaspring3 and not ev_tsukasaspring3.missed:
                        text _("Failsafe")

                    if christmastsukasa1 and show_complete:
                        textbutton _("A Part of Your World {b}✓{/b}") action Replay("christmastsukasa1", locked=False) text_style "modmybutton"
                    elif not christmastsukasa1 and not ev_christmastsukasa1.missed:
                        text _("A Part of Your World")

                    if tsukasaspring4 and show_complete:
                        textbutton _("The Talk {b}✓{/b}") action Replay("tsukasaspring4", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring4.missed and show_complete:
                        text _("{color=EF1A1A}{s}WEAK{/s}{/color}")
                    elif not tsukasaspring4 and not ev_tsukasaspring4.missed:
                        text _("The Talk")

                    if tsukasaspring5 and show_complete:
                        textbutton _("Six Inches of Suffering {b}✓{/b}") action Replay("tsukasaspring5", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring5.missed and show_complete:
                        text _("{color=EF1A1A}{s}No Penis, No Gain{/s}{/color}")
                    elif not tsukasaspring5 and not ev_tsukasaspring5.missed:
                        text _("Six Inches of Suffering")

                    if tsukasaspring6 and show_complete:
                        textbutton _("Useless, Flightless Fledgling {b}✓{/b}") action Replay("tsukasaspring6", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring6.missed and show_complete:
                        text _("{color=EF1A1A}{s}Leaving the Nest{/s}{/color}")
                    elif not tsukasaspring6 and not ev_tsukasaspring6.missed:
                        text _("Useless, Flightless Fledgling")

                    if tsukasaspring7 and show_complete:
                        textbutton _("The Gays {b}✓{/b}") action Replay("tsukasaspring7", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring7.missed and show_complete:
                        text _("{color=EF1A1A}{s}The Gaze{/s}{/color}")
                    elif not tsukasaspring7 and not ev_tsukasaspring7.missed:
                        text _("The Gays")

                    if tsukasaspring8 and show_complete:
                        textbutton _("To Bury a Body {b}✓{/b}") action Replay("tsukasaspring8", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring8.missed and show_complete:
                        text _("{color=EF1A1A}{s}To Rise From the Dead{/s}{/color}")
                    elif not tsukasaspring8 and not ev_tsukasaspring8.missed:
                        text _("To Bury a Body")

                    if tsukasaspring9 and show_complete:
                        textbutton _("Simple Moving Average {b}✓{/b}") action Replay("tsukasaspring9", locked=False) text_style "modmybutton"
                    elif ev_tsukasaspring9.missed and show_complete:
                        text _("{color=EF1A1A}{s}Overbought{/s}{/color}")
                    elif not tsukasaspring9 and not ev_tsukasaspring9.missed:
                        text _("Simple Moving Average")

                #TSUNEYOEVENT

                if showgirl == "Tsuneyo":

                    if ramen1 and show_complete:
                        textbutton _("Snake Venom {b}✓{/b}") action Replay("ramen1", locked=False) text_style "modmybutton"
                    elif not ramen1 and not ev_ramen1.missed:
                        text _("Snake Venom")

                    if tsuneyofirsthall and show_complete:
                        textbutton _("The Life of a Blue Whale {b}✓{/b}") action Replay("tsuneyofirsthall", locked=False) text_style "modmybutton"
                    elif not tsuneyofirsthall and not ev_tsuneyofirsthall.missed:
                        text _("The Life of a Blue Whale")

                    if ramen5 and show_complete:
                        textbutton _("Between the Slurps of Pork Broth {b}✓{/b}") action Replay("ramen5", locked=False) text_style "modmybutton"
                    elif not ramen5 and not ev_ramen5.missed:
                        text _("Between the Slurps of Pork Broth")

                    if tsuneyodorm5 and show_complete:
                        textbutton _("Drug Use & Jump-Rope {b}✓{/b}") action Replay("tsuneyodorm5", locked=False) text_style "modmybutton"
                    elif not tsuneyodorm5 and not ev_tsuneyodorm5.missed:
                        text _("Drug Use & Jump-Rope")

                    if ramen10 and show_complete:
                        textbutton _("A Short List {b}✓{/b}") action Replay("ramen10", locked=False) text_style "modmybutton"
                    elif not ramen10 and not ev_ramen10.missed:
                        text _("A Short List")

                    if tsuneyodorm10 and show_complete:
                        textbutton _("The Man Who Loves Nothing {b}✓{/b}") action Replay("tsuneyodorm10", locked=False) text_style "modmybutton"
                    elif not tsuneyodorm10 and not ev_tsuneyodorm10.missed:
                        text _("The Man Who Loves Nothing")

                    text _("---------------------------------------------")

                    if ramen15 and show_complete:
                        textbutton _("Seeds {b}✓{/b}") action Replay("ramen15", locked=False) text_style "modmybutton"
                    elif not ramen15 and not ev_ramen15.missed:
                        text _("Seeds")

                    if tsuneyodorm15 and show_complete:
                        textbutton _("Moe Fan Service {b}✓{/b}") action Replay("tsuneyodorm15", locked=False) text_style "modmybutton"
                    elif not tsuneyodorm15 and not ev_tsuneyodorm15.missed:
                        text _("Moe Fan Service")

                    if tsuneyodorm20 and show_complete:
                        textbutton _("Fucking...Or What it Means to Live (Shio & Shoyu) {b}✓{/b}") action Replay("tsuneyodorm20", locked=False) text_style "modmybutton"
                    elif not tsuneyodorm20 and not ev_tsuneyodorm20.missed:
                        text _("Fucking...Or What it Means to Live (Shio & Shoyu)")

                    if ramen20 and show_complete:
                        textbutton _("Blackout {b}✓{/b}") action Replay("ramen20", locked=False) text_style "modmybutton"
                    elif not ramen20 and not ev_ramen20.missed:
                        text _("Blackout")

                    if ramen25 and show_complete:
                        textbutton _("Like Noodles in the Wind {b}✓{/b}") action Replay("ramen25", locked=False) text_style "modmybutton"
                    elif not ramen25 and not ev_ramen25.missed:
                        text _("Like Noodles in the Wind")

                    if ramen25p2 and show_complete:
                        textbutton _("Green Onions and Contraceptives {b}✓{/b}") action Replay("ramen25p2", locked=False) text_style "modmybutton"
                    elif not ramen25p2 and not ev_ramen25p2.missed:
                        text _("Green Onions and Contraceptives")

                    if tsuneyodorm25 and show_complete:
                        textbutton _("Unsleeping Aegis {b}✓{/b}") action Replay("tsuneyodorm25", locked=False) text_style "modmybutton"
                    elif not tsuneyodorm25 and not ev_tsuneyodorm25.missed:
                        text _("Unsleeping Aegis")

                    if ramen30 and show_complete:
                        textbutton _("Things Like Stairs {b}✓{/b}") action Replay("ramen30", locked=False) text_style "modmybutton"
                    elif not ramen30 and not ev_ramen30.missed:
                        text _("Things Like Stairs")

                    text _("---------------------------------------------")

                    if tsuneyoslumber1 and show_complete:
                        textbutton _("With Her {b}✓{/b}") action Replay("tsuneyoslumber1", locked=False) text_style "modmybutton"
                    elif not tsuneyoslumber1 and not ev_tsuneyoslumber1.missed:
                        text _("With Her")

                    if tsuneyoslumber2 and show_complete:
                        textbutton _("Stripped Away {b}✓{/b}") action Replay("tsuneyoslumber2", locked=False) text_style "modmybutton"
                    elif not tsuneyoslumber2 and not ev_tsuneyoslumber2.missed:
                        text _("Stripped Away")

                    if tsuneyoslumber3 and show_complete:
                        textbutton _("Sudden Light {b}✓{/b}") action Replay("tsuneyoslumber3", locked=False) text_style "modmybutton"
                    elif not tsuneyoslumber3 and not ev_tsuneyoslumber3.missed:
                        text _("Sudden Light")

                    text _("---------------------------------------------")

                    if tsuneyospring1 and show_complete:
                        textbutton _("Ramen Girl {b}✓{/b}") action Replay("tsuneyospring1", locked=False) text_style "modmybutton"
                    elif not tsuneyospring1 and not ev_tsuneyospring1.missed:
                        text _("Ramen Girl")

                    if tsuneyospring2 and show_complete:
                        textbutton _("Soothsayer {b}✓{/b}") action Replay("tsuneyospring2", locked=False) text_style "modmybutton"
                    elif not tsuneyospring2 and not ev_tsuneyospring2.missed:
                        text _("Soothsayer")

                    if tsuneyospring3 and show_complete:
                        textbutton _("TH15 15NT M3 {b}✓{/b}") action Replay("tsuneyospring3", locked=False) text_style "modmybutton"
                    elif not tsuneyospring3 and not ev_tsuneyospring3.missed:
                        text _("TH15 15NT M3")

                    if halloweentsuneyo1 and show_complete:
                        textbutton _("ELATION PROTOCOL 99: NOODLEFOOT DISCO {b}✓{/b}") action Replay("halloweentsuneyo1", locked=False) text_style "modmybutton"
                    elif not halloweentsuneyo1 and not ev_halloweentsuneyo1.missed:
                        text _("ELATION PROTOCOL 99: NOODLEFOOT DISCO")

                    if tsuneyospring4 and show_complete:
                        textbutton _("Thomas Mato, M.D. {b}✓{/b}") action Replay("tsuneyospring4", locked=False) text_style "modmybutton"
                    elif not tsuneyospring4 and not ev_tsuneyospring4.missed:
                        text _("Thomas Mato, M.D.")

                    if tsuneyospring5 and show_complete:
                        textbutton _("Yamato Nadeshiko {b}✓{/b}") action Replay("tsuneyospring5", locked=False) text_style "modmybutton"
                    elif not tsuneyospring5 and not ev_tsuneyospring5.missed:
                        text _("Yamato Nadeshiko")

                    if tsuneyospring6 and show_complete:
                        textbutton _("WORMGOD54 {b}✓{/b}") action Replay("tsuneyospring6", locked=False) text_style "modmybutton"
                    elif not tsuneyospring6 and not ev_tsuneyospring6.missed:
                        text _("WORMGOD54")

                    if beachsixtsuneyo1 and show_complete:
                        textbutton _("Defilement of a Temple {b}✓{/b}") action Replay("beachsixtsuneyo1", locked=False) text_style "modmybutton"
                    elif not beachsixtsuneyo1 and not ev_beachsixtsuneyo1.missed:
                        text _("Defilement of a Temple")

                    if beachsixtsuneyo2 and show_complete:
                        textbutton _("Denouement {b}✓{/b}") action Replay("beachsixtsuneyo2", locked=False) text_style "modmybutton"
                    elif not beachsixtsuneyo2 and not ev_beachsixtsuneyo2.missed:
                        text _("Denouement")

                    if tsuneyospring7 and show_complete:
                        textbutton _("Shaka-Shaka-HEY {b}✓{/b}") action Replay("tsuneyospring7", locked=False) text_style "modmybutton"
                    elif not tsuneyospring7 and not ev_tsuneyospring7.missed:
                        text _("Shaka-Shaka-HEY")

                    if tsuneyospring8 and show_complete:
                        textbutton _("Anyone for Any Reason {b}✓{/b}") action Replay("tsuneyospring8", locked=False) text_style "modmybutton"
                    elif not tsuneyospring8 and not ev_tsuneyospring8.missed:
                        text _("Anyone for Any Reason")

                #UTAEVENT

                if showgirl == "Uta":

                    if utafirsthall and show_complete:
                        textbutton _("Far From Home {b}✓{/b}") action Replay("utafirsthall", locked=False) text_style "modmybutton"
                    elif not utafirsthall and not ev_utafirsthall.missed:
                        text _("Far From Home")

                    if utamaid1 and show_complete:
                        textbutton _("Abuse of Power {b}✓{/b}") action Replay("utamaid1", locked=False) text_style "modmybutton"
                    elif not utamaid1 and not ev_utamaid1.missed:
                        text _("Abuse of Power")

                    if utamaid5 and show_complete:
                        textbutton _("Love Me to Pieces {b}✓{/b}") action Replay("utamaid5", locked=False) text_style "modmybutton"
                    elif not utamaid5 and not ev_utamaid5.missed:
                        text _("Love Me to Pieces")

                    if utadorm5 and show_complete:
                        textbutton _("The VIP Treatment {b}✓{/b}") action Replay("utadorm5", locked=False) text_style "modmybutton"
                    elif not utadorm5 and not ev_utadorm5.missed:
                        text _("The VIP Treatment")

                    if utadorm10 and show_complete:
                        textbutton _("Shawshank Redemption {b}✓{/b}") action Replay("utadorm10", locked=False) text_style "modmybutton"
                    elif not utadorm10 and not ev_utadorm10.missed:
                        text _("Shawshank Redemption")

                    if utamaid10 and show_complete:
                        textbutton _("Happier Things {b}✓{/b}") action Replay("utamaid10", locked=False) text_style "modmybutton"
                    elif not utamaid10 and not ev_utamaid10.missed:
                        text _("Happier Things")

                    if utadorm15 and show_complete:
                        textbutton _("Facetime With My Mom (Tonight) {b}✓{/b}") action Replay("utadorm15", locked=False) text_style "modmybutton"
                    elif not utadorm15 and not ev_utadorm15.missed:
                        text _("Facetime With My Mom (Tonight)")

                    if utamaid20 and show_complete:
                        textbutton _("Veins and the Circulatory System {b}✓{/b}") action Replay("utamaid20", locked=False) text_style "modmybutton"
                    elif not utamaid20 and not ev_utamaid20.missed:
                        text _("Veins and the Circulatory System")

                    if utadorm20 and show_complete:
                        textbutton _("Blood Everywhere {b}✓{/b}") action Replay("utadorm20", locked=False) text_style "modmybutton"
                    elif not utadorm20 and not ev_utadorm20.missed:
                        text _("Blood Everywhere")

                    text _("---------------------------------------------")

                    if utaarchery1 and show_complete:
                        textbutton _("Impulse {b}✓{/b}") action Replay("utaarchery1", locked=False) text_style "modmybutton"
                    elif not utaarchery1 and not ev_utaarchery1.missed:
                        text _("Impulse")

                    if utamaid25p1 and show_complete:
                        textbutton _("Where Wishes Come True {b}✓{/b}") action Replay("utamaid25p1", locked=False) text_style "modmybutton"
                    elif not utamaid25p1 and not ev_utamaid25p1.missed:
                        text _("Where Wishes Come True")

                    if utamaid25p2 and show_complete:
                        textbutton _("After the Rain {b}✓{/b}") action Replay("utamaid25p2", locked=False) text_style "modmybutton"
                    elif not utamaid25p2 and not ev_utamaid25p2.missed:
                        text _("After the Rain")

                    if utadorm30 and show_complete:
                        textbutton _("Uta-chan {b}✓{/b}") action Replay("utadorm30", locked=False) text_style "modmybutton"
                    elif not utadorm30 and not ev_utadorm30.missed:
                        text _("Uta-chan")

                    if utaspecial35 and show_complete:
                        textbutton _("Young & Stupid {b}✓{/b}") action Replay("utaspecial35", locked=False) text_style "modmybutton"
                    elif not utaspecial35 and not ev_utaspecial35.missed:
                        text _("Young & Stupid")

                    if utadate35 and show_complete:
                        textbutton _("Enjo Kousai {b}✓{/b}") action Replay("utadate35", locked=False) text_style "modmybutton"
                    elif not utadate35 and not ev_utadate35.missed:
                        text _("Enjo Kousai")

                    if utadorm40p1 and show_complete:
                        textbutton _("Whore {b}✓{/b}") action Replay("utadorm40p1", locked=False) text_style "modmybutton"
                    elif not utadorm40p1 and not ev_utadorm40p1.missed:
                        text _("Whore")

                    if utadorm40p2 and show_complete:
                        textbutton _("The Girl From Nara {b}✓{/b}") action Replay("utadorm40p2", locked=False) text_style "modmybutton"
                    elif not utadorm40p2 and not ev_utadorm40p2.missed:
                        text _("The Girl From Nara")

                    text _("---------------------------------------------")

                    if utaspring1 and show_complete:
                        textbutton _("To Be Wanted {b}✓{/b}") action Replay("utaspring1", locked=False) text_style "modmybutton"
                    elif not utaspring1 and not ev_utaspring1.missed:
                        text _("To Be Wanted")

                    if utaspring2 and show_complete:
                        textbutton _("Meet Me At Our Spot {b}✓{/b}") action Replay("utaspring2", locked=False) text_style "modmybutton"
                    elif not utaspring2 and not ev_utaspring2.missed:
                        text _("Meet Me At Our Spot")

                    if beachfive14 and show_complete:
                        textbutton _("Reasons For Rain {b}✓{/b}") action Replay("beachfive14", locked=False) text_style "modmybutton"
                    elif not beachfive14 and not ev_beachfive14.missed:
                        text _("Reasons For Rain")

                    if utaspring3 and show_complete:
                        textbutton _("Songs of Autumn {b}✓{/b}") action Replay("utaspring3", locked=False) text_style "modmybutton"
                    elif not utaspring3 and not ev_utaspring3.missed:
                        text _("Songs of Autumn")

                    if utaspring4 and show_complete:
                        textbutton _("Heebie-Jeebies {b}✓{/b}") action Replay("utaspring4", locked=False) text_style "modmybutton"
                    elif not utaspring4 and not ev_utaspring4.missed:
                        text _("Heebie-Jeebies")

                    if utaspring5 and show_complete:
                        textbutton _("A Thousand Times, Yes {b}✓{/b}") action Replay("utaspring5", locked=False) text_style "modmybutton"
                    elif not utaspring5 and not ev_utaspring5.missed:
                        text _("A Thousand Times, Yes")

                    if utaspring6 and show_complete:
                        textbutton _("Stolen Valor {b}✓{/b}") action Replay("utaspring6", locked=False) text_style "modmybutton"
                    elif ev_utaspring6.missed and show_complete:
                        text _("{color=EF1A1A}{s}One Year in Prison{/s}{/color}")
                    elif not utaspring6 and not ev_utaspring6.missed:
                        text _("Stolen Valor")

                    if utaspring7 and show_complete:
                        textbutton _("ASL {b}✓{/b}") action Replay("utaspring7", locked=False) text_style "modmybutton"
                    elif not utaspring7 and not ev_utaspring7.missed:
                        text _("ASL")

                    if utaspring8 and show_complete:
                        textbutton _("ELATION PROTOCOL 99: DEFINE INTERVENTION {b}✓{/b}") action Replay("utaspring8", locked=False) text_style "modmybutton"
                    elif not utaspring8 and not ev_utaspring8.missed:
                        text _("ELATION PROTOCOL 99: DEFINE INTERVENTION")

                    if utaspring9 and show_complete:
                        textbutton _("Secret Admirer {b}✓{/b}") action Replay("utaspring9", locked=False) text_style "modmybutton"
                    elif not utaspring9 and not ev_utaspring9.missed:
                        text _("Secret Admirer")

                #WAKANAEVENT

                if showgirl == "Wakana":

                    if wakanadate1 and show_complete:
                        textbutton _("To the River {b}✓{/b}") action Replay("wakanadate1", locked=False) text_style "modmybutton"
                    elif not wakanadate1 and not ev_wakanadate1.missed:
                        text _("To the River")

                    if wakanadate5 and show_complete:
                        textbutton _("Soup, or Another Year With You {b}✓{/b}") action Replay("wakanadate5", locked=False) text_style "modmybutton"
                    elif not wakanadate5 and not ev_wakanadate5.missed:
                        text _("Soup, or Another Year With You")

                    text _("---------------------------------------------")

                    if wakanadate15 and show_complete:
                        textbutton _("Pseudonym {b}✓{/b}") action Replay("wakanadate15", locked=False) text_style "modmybutton"
                    elif not wakanadate15 and not ev_wakanadate15.missed:
                        text _("Pseudonym")

                    if wakanaspecial15 and show_complete:
                        textbutton _("Don't Hold Back {b}✓{/b}") action Replay("wakanaspecial15", locked=False) text_style "modmybutton"
                    elif not wakanaspecial15 and not ev_wakanaspecial15.missed:
                        text _("Don't Hold Back")

                    if wakanadate25p1 and show_complete:
                        textbutton _("The Desk Scene {b}✓{/b}") action Replay("wakanadate25p1", locked=False) text_style "modmybutton"
                    elif not wakanadate25p1 and not ev_wakanadate25p1.missed:
                        text _("The Desk Scene")

                    if wakanadate25p2 and show_complete:
                        textbutton _("Human Error {b}✓{/b}") action Replay("wakanadate25p2", locked=False) text_style "modmybutton"
                    elif not wakanadate25p2 and not ev_wakanadate25p2.missed:
                        text _("Human Error")

                    if wakanadate25p3 and show_complete:
                        textbutton _("Follow My Lead {b}✓{/b}") action Replay("wakanadate25p3", locked=False) text_style "modmybutton"
                    elif not wakanadate25p3 and not ev_wakanadate25p3.missed:
                        text _("Follow My Lead")

                    text _("---------------------------------------------")

                    if wakanaspring1 and show_complete:
                        textbutton _("Enough is Not Enough {b}✓{/b}") action Replay("wakanaspring1", locked=False) text_style "modmybutton"
                    elif not wakanaspring1 and not ev_wakanaspring1.missed:
                        text _("Enough is Not Enough")

                    if wakanaspring2 and show_complete:
                        textbutton _("In the Morning, I'll Forget {b}✓{/b}") action Replay("wakanaspring2", locked=False) text_style "modmybutton"
                    elif not wakanaspring2 and not ev_wakanaspring2.missed:
                        text _("In the Morning, I'll Forget")

                    if wakanaspring3 and show_complete:
                        textbutton _("I'm Wide Awake, It's Morning {b}✓{/b}") action Replay("wakanaspring3", locked=False) text_style "modmybutton"
                    elif not wakanaspring3 and not ev_wakanaspring3.missed:
                        text _("I'm Wide Awake, It's Morning")

                    if wakanaspring4 and show_complete:
                        textbutton _("Dark White (Pretty Joy) {b}✓{/b}") action Replay("wakanaspring4", locked=False) text_style "modmybutton"
                    elif not wakanaspring4 and not ev_wakanaspring4.missed:
                        text _("Dark White (Pretty Joy)")

                    if wakanaspring5 and show_complete:
                        textbutton _("Connect the Dots {b}✓{/b}") action Replay("wakanaspring5", locked=False) text_style "modmybutton"
                    elif not wakanaspring5 and not ev_wakanaspring5.missed:
                        text _("Connect the Dots")

                    if wakanaspring6 and show_complete:
                        textbutton _("From the Horse’s Mouth {b}✓{/b}") action Replay("wakanaspring6", locked=False) text_style "modmybutton"
                    elif not wakanaspring6 and not ev_wakanaspring6.missed:
                        text _("From the Horse’s Mouth")

                    if wakanaspring7 and show_complete:
                        textbutton _("Road to Nowhere {b}✓{/b}") action Replay("wakanaspring7", locked=False) text_style "modmybutton"
                    elif not wakanaspring7 and not ev_wakanaspring7.missed:
                        text _("Road to Nowhere")

                    if wakanaspring8 and show_complete:
                        textbutton _("Dick Wizard {b}✓{/b}") action Replay("wakanaspring8", locked=False) text_style "modmybutton"
                    elif not wakanaspring8 and not ev_wakanaspring8.missed:
                        text _("Dick Wizard")

                #YASUEVENT

                if showgirl == "Yasu":

                    if yasufirsthall and show_complete:
                        textbutton _("The Hole That Swallowed Everything {b}✓{/b}") action Replay("yasufirsthall", locked=False) text_style "modmybutton"
                    elif not yasufirsthall and not ev_yasufirsthall.missed:
                        text _("The Hole That Swallowed Everything")

                    if church1 and show_complete:
                        textbutton _("Transference {b}✓{/b}") action Replay("church1", locked=False) text_style "modmybutton"
                    elif not church1 and not ev_church1.missed:
                        text _("Transference")

                    if church5 and show_complete:
                        textbutton _("Armor of Older Gods {b}✓{/b}") action Replay("church5", locked=False) text_style "modmybutton"
                    elif not church5 and not ev_church5.missed:
                        text _("Armor of Older Gods")

                    if yasudorm10 and show_complete:
                        textbutton _("Repentance {b}✓{/b}") action Replay("yasudorm10", locked=False) text_style "modmybutton"
                    elif not yasudorm10 and not ev_yasudorm10.missed:
                        text _("Repentance")

                    if church10 and show_complete:
                        textbutton _("Sakura Season {b}✓{/b}") action Replay("church10", locked=False) text_style "modmybutton"
                    elif not church10 and not ev_church10.missed:
                        text _("Sakura Season")

                    text _("---------------------------------------------")

                    if church15 and show_complete:
                        textbutton _("Down The Rabbit Hole {b}✓{/b}") action Replay("church15", locked=False) text_style "modmybutton"
                    elif not church15 and not ev_church15.missed:
                        text _("Down The Rabbit Hole")

                    if yasuspecial15 and show_complete:
                        textbutton _("Sore Thumb {b}✓{/b}") action Replay("yasuspecial15", locked=False) text_style "modmybutton"
                    elif not yasuspecial15 and not ev_yasuspecial15.missed:
                        text _("Sore Thumb")

                    if church20 and show_complete:
                        textbutton _("Mother Duck {b}✓{/b}") action Replay("church20", locked=False) text_style "modmybutton"
                    elif not church20 and not ev_church20.missed:
                        text _("Mother Duck")

                    if yasudorm20 and show_complete:
                        textbutton _("Glossolalia {b}✓{/b}") action Replay("yasudorm20", locked=False) text_style "modmybutton"
                    elif not yasudorm20 and not ev_yasudorm20.missed:
                        text _("Glossolalia")

                    if yasuspecial20 and show_complete:
                        textbutton _("The River Styx {b}✓{/b}") action Replay("yasuspecial20", locked=False) text_style "modmybutton"
                    elif not yasuspecial20 and not ev_yasuspecial20.missed:
                        text _("The River Styx")

                    if church25 and show_complete:
                        textbutton _("Frankincense & Myrrh {b}✓{/b}") action Replay("church25", locked=False) text_style "modmybutton"
                    elif not church25 and not ev_church25.missed:
                        text _("Frankincense & Myrrh")

                    if yasudorm25 and show_complete:
                        textbutton _("Hand of God {b}✓{/b}") action Replay("yasudorm25", locked=False) text_style "modmybutton"
                    elif not yasudorm25 and not ev_yasudorm25.missed:
                        text _("Hand of God")

                    if yasudorm30 and show_complete:
                        textbutton _("An Apple Each Day {b}✓{/b}") action Replay("yasudorm30", locked=False) text_style "modmybutton"
                    elif not yasudorm30 and not ev_yasudorm30.missed:
                        text _("An Apple Each Day")

                    text _("---------------------------------------------")

                    if yasuspring1 and show_complete:
                        textbutton _("Throne of Flesh {b}✓{/b}") action Replay("yasuspring1", locked=False) text_style "modmybutton"
                    elif not yasuspring1 and not ev_yasuspring1.missed:
                        text _("Throne of Flesh")

                    if yasuspring2 and show_complete:
                        textbutton _("Fruits of Torment {b}✓{/b}") action Replay("yasuspring2", locked=False) text_style "modmybutton"
                    elif not yasuspring2 and not ev_yasuspring2.missed:
                        text _("Fruits of Torment")

                    if yasuspring3 and show_complete:
                        textbutton _("The Art of Drowning {b}✓{/b}") action Replay("yasuspring3", locked=False) text_style "modmybutton"
                    elif not yasuspring3 and not ev_yasuspring3.missed:
                        text _("The Art of Drowning")

                    if halloweenyasu1 and show_complete:
                        textbutton _("Infinity House {b}✓{/b}") action Replay("halloweenyasu1", locked=False) text_style "modmybutton"
                    elif not halloweenyasu1 and not ev_halloweenyasu1.missed:
                        text _("Infinity House")

                    if yasuspring4 and show_complete:
                        textbutton _("False Chameleon {b}✓{/b}") action Replay("yasuspring4", locked=False) text_style "modmybutton"
                    elif not yasuspring4 and not ev_yasuspring4.missed:
                        text _("False Chameleon")

                    if yasuspring5 and show_complete:
                        textbutton _("Etinsib Ziwa & The Book of Colors {b}✓{/b}") action Replay("yasuspring5", locked=False) text_style "modmybutton"
                    elif not yasuspring5 and not ev_yasuspring5.missed:
                        text _("Etinsib Ziwa & The Book of Colors")

                    if yasuchristmalloween1 and show_complete:
                        textbutton _("Before the Sun Sets {b}✓{/b}") action Replay("yasuchristmalloween1", locked=False) text_style "modmybutton"
                    elif not yasuchristmalloween1 and not ev_yasuchristmalloween1.missed:
                        text _("Before the Sun Sets")

                    if yasuchristmalloween2 and show_complete:
                        textbutton _("His Eternal Diary {b}✓{/b}") action Replay("yasuchristmalloween2", locked=False) text_style "modmybutton"
                    elif not yasuchristmalloween2 and not ev_yasuchristmalloween2.missed:
                        text _("His Eternal Diary")

                    if yasuspring6 and show_complete:
                        textbutton _("Child of Light {b}✓{/b}") action Replay("yasuspring6", locked=False) text_style "modmybutton"
                    elif not yasuspring6 and not ev_yasuspring6.missed:
                        text _("Child of Light")

                    if yasuspring7 and show_complete:
                        textbutton _("Ichigo Daifuku {b}✓{/b}") action Replay("yasuspring7", locked=False) text_style "modmybutton"
                    elif not yasuspring7 and not ev_yasuspring7.missed:
                        text _("Ichigo Daifuku")

                    if yasuspring8 and show_complete:
                        textbutton _("Heretic {b}✓{/b}") action Replay("yasuspring8", locked=False) text_style "modmybutton"
                    elif not yasuspring8 and not ev_yasuspring8.missed:
                        text _("Heretic")

                #YUKIEVENT

                if showgirl == "Yuki":

                    if yukidate1 and show_complete:
                        textbutton _("Rule #1 {b}✓{/b}") action Replay("yukidate1", locked=False) text_style "modmybutton"
                    elif not yukidate1 and not ev_yukidate1.missed:
                        text _("Rule #1")

                    if yukidate5 and show_complete:
                        textbutton _("Better Off Alone {b}✓{/b}") action Replay("yukidate5", locked=False) text_style "modmybutton"
                    elif not yukidate5 and not ev_yukidate5.missed:
                        text _("Better Off Alone")

                    if yukidate10 and show_complete:
                        textbutton _("Opposite Directions {b}✓{/b}") action Replay("yukidate10", locked=False) text_style "modmybutton"
                    elif not yukidate10 and not ev_yukidate10.missed:
                        text _("Opposite Directions")

                    if yukidate10p2 and show_complete:
                        textbutton _("A Thing of the Past {b}✓{/b}") action Replay("yukidate10p2", locked=False) text_style "modmybutton"
                    elif not yukidate10p2 and not ev_yukidate10p2.missed:
                        text _("A Thing of the Past")

                    text _("---------------------------------------------")

                    if yukidate20p1 and show_complete:
                        textbutton _("Funeral Plans {b}✓{/b}") action Replay("yukidate20p1", locked=False) text_style "modmybutton"
                    elif not yukidate20p1 and not ev_yukidate20p1.missed:
                        text _("Funeral Plans")

                    if yukidate20p2 and show_complete:
                        textbutton _("Douchebag McDouchefuck {b}✓{/b}") action Replay("yukidate20p2", locked=False) text_style "modmybutton"
                    elif not yukidate20p2 and not ev_yukidate20p2.missed:
                        text _("Douchebag McDouchefuck")

                    if yukidate25 and show_complete:
                        textbutton _("Pride & Joy {b}✓{/b}") action Replay("yukidate25", locked=False) text_style "modmybutton"
                    elif not yukidate25 and not ev_yukidate25.missed:
                        text _("Pride & Joy")

                    text _("---------------------------------------------")

                    if yukicamp1 and show_complete:
                        textbutton _("Big Dog {b}✓{/b}") action Replay("yukicamp1", locked=False) text_style "modmybutton"
                    elif not yukicamp1 and not ev_yukicamp1.missed:
                        text _("Big Dog")

                    if yukicamp2 and show_complete:
                        textbutton _("My Heart is in Rotenburg {b}✓{/b}") action Replay("yukicamp2", locked=False) text_style "modmybutton"
                    elif not yukicamp2 and not ev_yukicamp2.missed:
                        text _("My Heart is in Rotenburg")

                    if yukispring1 and show_complete:
                        textbutton _("Small Plastic Baggies {b}✓{/b}") action Replay("yukispring1", locked=False) text_style "modmybutton"
                    elif not yukispring1 and not ev_yukispring1.missed:
                        text _("Small Plastic Baggies")

                    if yukispring2 and show_complete:
                        textbutton _("Better Than Sex {b}✓{/b}") action Replay("yukispring2", locked=False) text_style "modmybutton"
                    elif not yukispring2 and not ev_yukispring2.missed:
                        text _("Better Than Sex")

                    if yukispring3 and show_complete:
                        textbutton _("As the Footsteps Die Out Forever {b}✓{/b}") action Replay("yukispring3", locked=False) text_style "modmybutton"
                    elif not yukispring3 and not ev_yukispring3.missed:
                        text _("As the Footsteps Die Out Forever")

                    if yukispring4 and show_complete:
                        textbutton _("Heart of Fear {b}✓{/b}") action Replay("yukispring4", locked=False) text_style "modmybutton"
                    elif not yukispring4 and not ev_yukispring4.missed:
                        text _("Heart of Fear")

                    if yukispring5 and show_complete:
                        textbutton _("When I Say “Jump” {b}✓{/b}") action Replay("yukispring5", locked=False) text_style "modmybutton"
                    elif not yukispring5 and not ev_yukispring5.missed:
                        text _("When I Say “Jump”")

                    if yukispring6 and show_complete:
                        textbutton _("Bridge Burner {b}✓{/b}") action Replay("yukispring6", locked=False) text_style "modmybutton"
                    elif not yukispring6 and not ev_yukispring6.missed:
                        text _("Bridge Burner")

                    if yukispring7 and show_complete:
                        textbutton _("Yuki-onna {b}✓{/b}") action Replay("yukispring7", locked=False) text_style "modmybutton"
                    elif not yukispring7 and not ev_yukispring7.missed:
                        text _("Yuki-onna")

                #YUMIEVENT

                if showgirl == "Yumi":

                    if firsttimestreets and show_complete:
                        textbutton _("Five Million Dollars {b}✓{/b}") action Replay("firsttimestreets", locked=False) text_style "modmybutton"
                    elif not firsttimestreets and not ev_firsttimestreets.missed:
                        text _("Five Million Dollars")

                    if yumifirsthall and show_complete:
                        textbutton _("Micropenis {b}✓{/b}") action Replay("yumifirsthall", locked=False) text_style "modmybutton"
                    elif not yumifirsthall and not ev_yumifirsthall.missed:
                        text _("Micropenis")

                    if streets5 and show_complete:
                        textbutton _("Three Second Smile {b}✓{/b}") action Replay("streets5", locked=False) text_style "modmybutton"
                    elif not streets5 and not ev_streets5.missed:
                        text _("Three Second Smile")

                    if streets10 and show_complete:
                        textbutton _("I See You {b}✓{/b}") action Replay("streets10", locked=False) text_style "modmybutton"
                    elif not streets10 and not ev_streets10.missed:
                        text _("I See You")

                    if yumidorm5 and show_complete:
                        textbutton _("Fuck The Police {b}✓{/b}") action Replay("yumidorm5", locked=False) text_style "modmybutton"
                    elif not yumidorm5 and not ev_yumidorm5.missed:
                        text _("Fuck The Police")

                    if yumidorm10 and show_complete:
                        textbutton _("Yumi Revitalization Project {b}✓{/b}") action Replay("yumidorm10", locked=False) text_style "modmybutton"
                    elif not yumidorm10 and not ev_yumidorm10.missed:
                        text _("Yumi Revitalization Project")

                    if yumidorm15 and show_complete:
                        textbutton _("Worse Comes to Worst {b}✓{/b}") action Replay("yumidorm15", locked=False) text_style "modmybutton"
                    elif not yumidorm15 and not ev_yumidorm15.missed:
                        text _("Worse Comes to Worst")

                    if streets15 and show_complete:
                        textbutton _("Apples to Apples {b}✓{/b}") action Replay("streets15", locked=False) text_style "modmybutton"
                    elif not streets15 and not ev_streets15.missed:
                        text _("Apples to Apples")

                    if streets20 and show_complete:
                        textbutton _("Token Tsundere {b}✓{/b}") action Replay("streets20", locked=False) text_style "modmybutton"
                    elif not streets20 and not ev_streets20.missed:
                        text _("Token Tsundere")

                    if yumidorm20 and show_complete:
                        textbutton _("Great Expectations {b}✓{/b}") action Replay("yumidorm20", locked=False) text_style "modmybutton"
                    elif not yumidorm20 and not ev_yumidorm20.missed:
                        text _("Great Expectations")

                    if streets25 and show_complete:
                        textbutton _("A Place Like This {b}✓{/b}") action Replay("streets25", locked=False) text_style "modmybutton"
                    elif not streets25 and not ev_streets25.missed:
                        text _("A Place Like This")

                    if yumidorm25 and show_complete:
                        textbutton _("Caught in the Vortex {b}✓{/b}") action Replay("yumidorm25", locked=False) text_style "modmybutton"
                    elif not yumidorm25 and not ev_yumidorm25.missed:
                        text _("Caught in the Vortex")

                    text _("---------------------------------------------")

                    if streets30 and show_complete:
                        textbutton _("Where the Sidewalk Ends {b}✓{/b}") action Replay("streets30", locked=False) text_style "modmybutton"
                    elif not streets30 and not ev_streets30.missed:
                        text _("Where the Sidewalk Ends")

                    if yumidorm30 and show_complete:
                        textbutton _("Walls Too Thick to Hear Through {b}✓{/b}") action Replay("yumidorm30", locked=False) text_style "modmybutton"
                    elif not yumidorm30 and not ev_yumidorm30.missed:
                        text _("Walls Too Thick to Hear Through")

                    if yumidorm35 and show_complete:
                        textbutton _("Tech Support {b}✓{/b}") action Replay("yumidorm35", locked=False) text_style "modmybutton"
                    elif not yumidorm35 and not ev_yumidorm35.missed:
                        text _("Tech Support")

                    if yumicallnight35 and show_complete:
                        textbutton _("Abyss {b}✓{/b}") action Replay("yumicallnight35", locked=False) text_style "modmybutton"
                    elif not yumicallnight35 and not ev_yumicallnight35.missed:
                        text _("Abyss")

                    if yumispecial40 and show_complete:
                        textbutton _("Reconciliation {b}✓{/b}") action Replay("yumispecial40", locked=False) text_style "modmybutton"
                    elif not yumispecial40 and not ev_yumispecial40.missed:
                        text _("Reconciliation")

                    if yumispecial40p2 and show_complete:
                        textbutton _("Neon Heart (If I Close My Eyes) {b}✓{/b}") action Replay("yumispecial40p2", locked=False) text_style "modmybutton"
                    elif not yumispecial40p2 and not ev_yumispecial40p2.missed:
                        text _("Neon Heart (If I Close My Eyes)")

                    if streets40 and show_complete:
                        textbutton _("Unsung Heroes {b}✓{/b}") action Replay("streets40", locked=False) text_style "modmybutton"
                    elif not streets40 and not ev_streets40.missed:
                        text _("Unsung Heroes")

                    if yumispecial45 and show_complete:
                        textbutton _("See You Around {b}✓{/b}") action Replay("yumispecial45", locked=False) text_style "modmybutton"
                    elif not yumispecial45 and not ev_yumispecial45.missed:
                        text _("See You Around")

                    text _("---------------------------------------------")

                    if yumislumber1 and show_complete:
                        textbutton _("Two Months of Nothing {b}✓{/b}") action Replay("yumislumber1", locked=False) text_style "modmybutton"
                    elif not yumislumber1 and not ev_yumislumber1.missed:
                        text _("Two Months of Nothing")

                    if yumislumber2 and show_complete:
                        textbutton _("Loggerhead {b}✓{/b}") action Replay("yumislumber2", locked=False) text_style "modmybutton"
                    elif not yumislumber2 and not ev_yumislumber2.missed:
                        text _("Loggerhead")

                    if yumislumber3 and show_complete:
                        textbutton _("A Day in the Life {b}✓{/b}") action Replay("yumislumber3", locked=False) text_style "modmybutton"
                    elif not yumislumber3 and not ev_yumislumber3.missed:
                        text _("A Day in the Life")

                    text _("---------------------------------------------")

                    if yumispring1 and show_complete:
                        textbutton _("Kid of the Month {b}✓{/b}") action Replay("yumispring1", locked=False) text_style "modmybutton"
                    elif not yumispring1 and not ev_yumispring1.missed:
                        text _("Kid of the Month")

                    if yumispring2 and show_complete:
                        textbutton _("Frog Boy {b}✓{/b}") action Replay("yumispring2", locked=False) text_style "modmybutton"
                    elif not yumispring2 and not ev_yumispring2.missed:
                        text _("Frog Boy")

                    if beachfive13 and show_complete:
                        textbutton _("Wake Me Up When It's Over {b}✓{/b}") action Replay("beachfive13", locked=False) text_style "modmybutton"
                    elif not beachfive13 and not ev_beachfive13.missed:
                        text _("Wake Me Up When It's Over")

                    if yumispring3 and show_complete:
                        textbutton _("A Life I Never Wanted {b}✓{/b}") action Replay("yumispring3", locked=False) text_style "modmybutton"
                    elif not yumispring3 and not ev_yumispring3.missed:
                        text _("A Life I Never Wanted")

                    if yumispring4 and show_complete:
                        textbutton _("Pogonomyrmex Occidentalis Owyheei {b}✓{/b}") action Replay("yumispring4", locked=False) text_style "modmybutton"
                    elif not yumispring4 and not ev_yumispring4.missed:
                        text _("Pogonomyrmex Occidentalis Owyheei")

                    if yumispring5 and show_complete:
                        textbutton _("The Dragon {b}✓{/b}") action Replay("yumispring5", locked=False) text_style "modmybutton"
                    elif not yumispring5 and not ev_yumispring5.missed:
                        text _("The Dragon")

                    if yumispring6 and show_complete:
                        textbutton _("Ittekimasu {b}✓{/b}") action Replay("yumispring6", locked=False) text_style "modmybutton"
                    elif not yumispring6 and not ev_yumispring6.missed:
                        text _("Ittekimasu")

                    if yumispring7 and show_complete:
                        textbutton _("Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS {b}✓{/b}") action Replay("yumispring7", locked=False) text_style "modmybutton"
                    elif not yumispring7 and not ev_yumispring7.missed:
                        text _("Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS")

                    if yumispring8 and show_complete:
                        textbutton _("Death With Dignity {b}✓{/b}") action Replay("yumispring8", locked=False) text_style "modmybutton"
                    elif not yumispring8 and not ev_yumispring8.missed:
                        text _("Death With Dignity")

                    if yumispring9 and show_complete:
                        textbutton _("Scar Tissue {b}✓{/b}") action Replay("yumispring9", locked=False) text_style "modmybutton"
                    elif not yumispring9 and not ev_yumispring9.missed:
                        text _("Scar Tissue")

                    if yumispring10 and show_complete:
                        textbutton _("Chabudai (Plastic Corpses) {b}✓{/b}") action Replay("yumispring10", locked=False) text_style "modmybutton"
                    elif not yumispring10 and not ev_yumispring10.missed:
                        text _("Chabudai (Plastic Corpses)")

    ################################################################################

            vbox: #box for the hints
                xpos .4
                style_prefix "tracker"

                if show_hints == True:

                    #AMIHINT

                    if showgirl == "Ami":

                        if not _in_replay:

                            #Harem Tutorial (firsttimeamisroom)
                            if (not ev_firsttimeamisroom.completed and not ev_firsttimeamisroom.missed) or show_complete:
                                if "(!)" in ev_firsttimeamisroom.hint:
                                    textbutton _("[ev_firsttimeamisroom.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimeamisroom), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimeamisroom.hint]")

                            #Uninvited (amifirsthall)
                            if (not ev_amifirsthall.completed and not ev_amifirsthall.missed) or show_complete:
                                if "(!)" in ev_amifirsthall.hint:
                                    textbutton _("[ev_amifirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amifirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amifirsthall.hint]")

                            #The Queen of Spiders (amisroom5)
                            if (not ev_amisroom5.completed and not ev_amisroom5.missed) or show_complete:
                                if "(!)" in ev_amisroom5.hint:
                                    textbutton _("[ev_amisroom5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amisroom5.hint]")

                            #Home Away From Home (amidorm5)
                            if (not ev_amidorm5.completed and not ev_amidorm5.missed) or show_complete:
                                if "(!)" in ev_amidorm5.hint:
                                    textbutton _("[ev_amidorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm5.hint]")

                            #Something Darker (amisroom10)
                            if (not ev_amisroom10.completed and not ev_amisroom10.missed) or show_complete:
                                if "(!)" in ev_amisroom10.hint:
                                    textbutton _("[ev_amisroom10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amisroom10.hint]")

                            #Couple's Discount (Sea of Diamonds) (aminew1)
                            if (not ev_aminew1.completed and not ev_aminew1.missed) or show_complete:
                                if "(!)" in ev_aminew1.hint:
                                    textbutton _("[ev_aminew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_aminew1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_aminew1.hint]")

                            #Ode to a Marsh Warbler (aminew2)
                            if (not ev_aminew2.completed and not ev_aminew2.missed) or show_complete:
                                if "(!)" in ev_aminew2.hint:
                                    textbutton _("[ev_aminew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_aminew2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_aminew2.hint]")

                            #No One Can See Us (amidorm10)
                            if (not ev_amidorm10.completed and not ev_amidorm10.missed) or show_complete:
                                if "(!)" in ev_amidorm10.hint:
                                    textbutton _("[ev_amidorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm10.hint]")

                            #Walking on Air (day98)
                            if (not ev_day98.completed and not ev_day98.missed) or show_complete:
                                if "(!)" in ev_day98.hint:
                                    textbutton _("[ev_day98.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day98), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_day98.hint]")

                            #Back Out in the Heat (amidorm15)
                            if (not ev_amidorm15.completed and not ev_amidorm15.missed) or show_complete:
                                if "(!)" in ev_amidorm15.hint:
                                    textbutton _("[ev_amidorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm15.hint]")

                            #Important Things (amisroom15)
                            if (not ev_amisroom15.completed and not ev_amisroom15.missed) or show_complete:
                                if "(!)" in ev_amisroom15.hint:
                                    textbutton _("[ev_amisroom15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amisroom15.hint]")

                            #Wake Up Call (amilust10)
                            if (not ev_amilust10.completed and not ev_amilust10.missed) or show_complete:
                                if "(!)" in ev_amilust10.hint:
                                    textbutton _("[ev_amilust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust10.hint]")

                            #Cute Girls and Stuff (amisroom20)
                            if (not ev_amisroom20.completed and not ev_amisroom20.missed) or show_complete:
                                if "(!)" in ev_amisroom20.hint:
                                    textbutton _("[ev_amisroom20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amisroom20.hint]")

                            #Divergence (amidorm20)
                            if (not ev_amidorm20.completed and not ev_amidorm20.missed) or show_complete:
                                if "(!)" in ev_amidorm20.hint:
                                    textbutton _("[ev_amidorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm20.hint]")

                            #Such Small Hands (amisroom25)
                            if (not ev_amisroom25.completed and not ev_amisroom25.missed) or show_complete:
                                if "(!)" in ev_amisroom25.hint:
                                    textbutton _("[ev_amisroom25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amisroom25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amisroom25.hint]")

                            #Everlasting Love (amidorm25)
                            if (not ev_amidorm25.completed and not ev_amidorm25.missed) or show_complete:
                                if "(!)" in ev_amidorm25.hint:
                                    textbutton _("[ev_amidorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm25.hint]")

                            text ("")

                            #Living (amiinvite1)
                            if (not ev_amiinvite1.completed and not ev_amiinvite1.missed) or show_complete:
                                if "(!)" in ev_amiinvite1.hint:
                                    textbutton _("[ev_amiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amiinvite1.hint]")

                            #Rising to the Challenge (amiinvite2)
                            if (not ev_amiinvite2.completed and not ev_amiinvite2.missed) or show_complete:
                                if "(!)" in ev_amiinvite2.hint:
                                    textbutton _("[ev_amiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amiinvite2.hint]")

                            #Best Friends Forever (amiinvite3)
                            if (not ev_amiinvite3.completed and not ev_amiinvite3.missed) or show_complete:
                                if "(!)" in ev_amiinvite3.hint:
                                    textbutton _("[ev_amiinvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amiinvite3.hint]")

                            #Third Place (amimaid30)
                            if (not ev_amimaid30.completed and not ev_amimaid30.missed) or show_complete:
                                if "(!)" in ev_amimaid30.hint:
                                    textbutton _("[ev_amimaid30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amimaid30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amimaid30.hint]")

                            #The Big Sleep (Cute Girl Magic) (amidate35)
                            if (not ev_amidate35.completed and not ev_amidate35.missed) or show_complete:
                                if "(!)" in ev_amidate35.hint:
                                    textbutton _("[ev_amidate35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidate35.hint]")

                            #Heaven for Human Blood (amidorm40)
                            if (not ev_amidorm40.completed and not ev_amidorm40.missed) or show_complete:
                                if "(!)" in ev_amidorm40.hint:
                                    textbutton _("[ev_amidorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidorm40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidorm40.hint]")

                            #As Light as Air (amilust15)
                            if (not ev_amilust15.completed and not ev_amilust15.missed) or show_complete:
                                if "(!)" in ev_amilust15.hint:
                                    textbutton _("[ev_amilust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust15.hint]")

                            #Conscious or Not (amilust20)
                            if (not ev_amilust20.completed and not ev_amilust20.missed) or show_complete:
                                if "(!)" in ev_amilust20.hint:
                                    textbutton _("[ev_amilust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust20.hint]")

                            #Outcry of the Hunted Hare (amidate50)
                            if (not ev_amidate50.completed and not ev_amidate50.missed) or show_complete:
                                if "(!)" in ev_amidate50.hint:
                                    textbutton _("[ev_amidate50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidate50.hint]")

                            #Fruits of the Two Seasons (amidate50p2)
                            if (not ev_amidate50p2.completed and not ev_amidate50p2.missed) or show_complete:
                                if "(!)" in ev_amidate50p2.hint:
                                    textbutton _("[ev_amidate50p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidate50p2.hint]")

                            #My Life With You (amidate50p3)
                            if (not ev_amidate50p3.completed and not ev_amidate50p3.missed) or show_complete:
                                if "(!)" in ev_amidate50p3.hint:
                                    textbutton _("[ev_amidate50p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidate50p3.hint]")

                            #Somnambula (amidate50p4)
                            if (not ev_amidate50p4.completed and not ev_amidate50p4.missed) or show_complete:
                                if "(!)" in ev_amidate50p4.hint:
                                    textbutton _("[ev_amidate50p4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amidate50p4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amidate50p4.hint]")

                            text ("")

                            #No One Can Hear Us (amilust35)
                            if (not ev_amilust35.completed and not ev_amilust35.missed) or show_complete:
                                if "(!)" in ev_amilust35.hint:
                                    textbutton _("[ev_amilust35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust35.hint]")

                            #Not Safe For Work (amimaid50)
                            if (not ev_amimaid50.completed and not ev_amimaid50.missed) or show_complete:
                                if "(!)" in ev_amimaid50.hint:
                                    textbutton _("[ev_amimaid50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amimaid50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amimaid50.hint]")

                            #Mama's Girl (amiinvite4)
                            if (not ev_amiinvite4.completed and not ev_amiinvite4.missed) or show_complete:
                                if "(!)" in ev_amiinvite4.hint:
                                    textbutton _("[ev_amiinvite4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amiinvite4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amiinvite4.hint]")

                            #Worry Not, The Mason Jar (amispecial50)
                            if (not ev_amispecial50.completed and not ev_amispecial50.missed) or show_complete:
                                if "(!)" in ev_amispecial50.hint:
                                    textbutton _("[ev_amispecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispecial50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispecial50.hint]")

                            #Family Matters (amilust50)
                            if (not ev_amilust50.completed and not ev_amilust50.missed) or show_complete:
                                if "(!)" in ev_amilust50.hint:
                                    textbutton _("[ev_amilust50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust50.hint]")

                            text ("")

                            #The Caretaker (amilust60)
                            if (not ev_amilust60.completed and not ev_amilust60.missed) or show_complete:
                                if "(!)" in ev_amilust60.hint:
                                    textbutton _("[ev_amilust60.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amilust60), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amilust60.hint]")

                            #Della (amispring1)
                            if (not ev_amispring1.completed and not ev_amispring1.missed) or show_complete:
                                if "(!)" in ev_amispring1.hint:
                                    textbutton _("[ev_amispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispring1.hint]")

                            #Every Day Birds (In Nothing But Blood) (amicamp1)
                            if (not ev_amicamp1.completed and not ev_amicamp1.missed) or show_complete:
                                if "(!)" in ev_amicamp1.hint:
                                    textbutton _("[ev_amicamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amicamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amicamp1.hint]")

                            #There Is A Light That Never Goes Out (amicamp2)
                            if (not ev_amicamp2.completed and not ev_amicamp2.missed) or show_complete:
                                if "(!)" in ev_amicamp2.hint:
                                    textbutton _("[ev_amicamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amicamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amicamp2.hint]")

                            #Soon (Another Nightmare) (halloweenami1)
                            if (not ev_halloweenami1.completed and not ev_halloweenami1.missed) or show_complete:
                                if "(!)" in ev_halloweenami1.hint:
                                    textbutton _("[ev_halloweenami1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenami1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenami1.hint]")

                            #Faith & Sacrifice (amispring2)
                            if (not ev_amispring2.completed and not ev_amispring2.missed) or show_complete:
                                if "(!)" in ev_amispring2.hint:
                                    textbutton _("[ev_amispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispring2.hint]")

                            #Shiritori (amispring3)
                            if (not ev_amispring3.completed and not ev_amispring3.missed) or show_complete:
                                if "(!)" in ev_amispring3.hint:
                                    textbutton _("[ev_amispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispring3.hint]")

                            #Nakadashi (amispring4)
                            if (not ev_amispring4.completed and not ev_amispring4.missed) or show_complete:
                                if "(!)" in ev_amispring4.hint:
                                    textbutton _("[ev_amispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispring4.hint]")

                            #Victrola (amispring5)
                            if (not ev_amispring5.completed and not ev_amispring5.missed) or show_complete:
                                if "(!)" in ev_amispring5.hint:
                                    textbutton _("[ev_amispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_amispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_amispring5.hint]")

                    #AYANEHINT

                    if showgirl == "Ayane":

                        if not _in_replay:

                            #The Unwavering Bravery of Ayane Amamiya (firsttimedojo)
                            if (not ev_firsttimedojo.completed and not ev_firsttimedojo.missed) or show_complete:
                                if "(!)" in ev_firsttimedojo.hint:
                                    textbutton _("[ev_firsttimedojo.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimedojo), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimedojo.hint]")

                            #Spy on Me (ayanefirsthall)
                            if (not ev_ayanefirsthall.completed and not ev_ayanefirsthall.missed) or show_complete:
                                if "(!)" in ev_ayanefirsthall.hint:
                                    textbutton _("[ev_ayanefirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanefirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanefirsthall.hint]")

                            #The Battle for Kumon-mi (dojo5)
                            if (not ev_dojo5.completed and not ev_dojo5.missed) or show_complete:
                                if "(!)" in ev_dojo5.hint:
                                    textbutton _("[ev_dojo5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo5.hint]")

                            #Names of Our Children (dojo10)
                            if (not ev_dojo10.completed and not ev_dojo10.missed) or show_complete:
                                if "(!)" in ev_dojo10.hint:
                                    textbutton _("[ev_dojo10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo10.hint]")

                            #Home Sweet Home (ayanedorm5)
                            if (not ev_ayanedorm5.completed and not ev_ayanedorm5.missed) or show_complete:
                                if "(!)" in ev_ayanedorm5.hint:
                                    textbutton _("[ev_ayanedorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm5.hint]")

                            #Imprinting (ayanenew1)
                            if (not ev_ayanenew1.completed and not ev_ayanenew1.missed) or show_complete:
                                if "(!)" in ev_ayanenew1.hint:
                                    textbutton _("[ev_ayanenew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanenew1.hint]")

                            #Far From Fantasy (ayanenew2)
                            if (not ev_ayanenew2.completed and not ev_ayanenew2.missed) or show_complete:
                                if "(!)" in ev_ayanenew2.hint:
                                    textbutton _("[ev_ayanenew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanenew2.hint]")

                            #Forever Yours (Top of the World) (ayanenew3)
                            if (not ev_ayanenew3.completed and not ev_ayanenew3.missed) or show_complete:
                                if "(!)" in ev_ayanenew3.hint:
                                    textbutton _("[ev_ayanenew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanenew3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanenew3.hint]")

                            #Less Like the Vulture (ayanedorm10)
                            if (not ev_ayanedorm10.completed and not ev_ayanedorm10.missed) or show_complete:
                                if "(!)" in ev_ayanedorm10.hint:
                                    textbutton _("[ev_ayanedorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm10.hint]")

                            #First Words (ayanedorm15)
                            if (not ev_ayanedorm15.completed and not ev_ayanedorm15.missed) or show_complete:
                                if "(!)" in ev_ayanedorm15.hint:
                                    textbutton _("[ev_ayanedorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm15.hint]")

                            #Backwards Spider Crawl (day68)
                            if (not ev_day68.completed and not ev_day68.missed) or show_complete:
                                if "(!)" in ev_day68.hint:
                                    textbutton _("[ev_day68.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day68), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_day68.hint]")

                            #Endless Torment (dojo20)
                            if (not ev_dojo20.completed and not ev_dojo20.missed) or show_complete:
                                if "(!)" in ev_dojo20.hint:
                                    textbutton _("[ev_dojo20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo20.hint]")

                            #Still Young (ayanedorm20)
                            if (not ev_ayanedorm20.completed and not ev_ayanedorm20.missed) or show_complete:
                                if "(!)" in ev_ayanedorm20.hint:
                                    textbutton _("[ev_ayanedorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm20.hint]")

                            #Prisoner (ayanelust10)
                            if (not ev_ayanelust10.completed and not ev_ayanelust10.missed) or show_complete:
                                if "(!)" in ev_ayanelust10.hint:
                                    textbutton _("[ev_ayanelust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanelust10.hint]")

                            #Regularly Scheduled Programming (dojo25)
                            if (not ev_dojo25.completed and not ev_dojo25.missed) or show_complete:
                                if "(!)" in ev_dojo25.hint:
                                    textbutton _("[ev_dojo25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo25.hint]")

                            #Cold Air of an Encroaching Winter (ayanedorm25)
                            if (not ev_ayanedorm25.completed and not ev_ayanedorm25.missed) or show_complete:
                                if "(!)" in ev_ayanedorm25.hint:
                                    textbutton _("[ev_ayanedorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm25.hint]")

                            #First and Second (dojo30)
                            if (not ev_dojo30.completed and not ev_dojo30.missed) or show_complete:
                                if "(!)" in ev_dojo30.hint:
                                    textbutton _("[ev_dojo30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo30.hint]")

                            #Crazier Things Have Happened (ayanedorm30)
                            if (not ev_ayanedorm30.completed and not ev_ayanedorm30.missed) or show_complete:
                                if "(!)" in ev_ayanedorm30.hint:
                                    textbutton _("[ev_ayanedorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm30.hint]")

                            text ("")

                            #Hail Mary (ayaneinvite1)
                            if (not ev_ayaneinvite1.completed and not ev_ayaneinvite1.missed) or show_complete:
                                if "(!)" in ev_ayaneinvite1.hint:
                                    textbutton _("[ev_ayaneinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayaneinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayaneinvite1.hint]")

                            #One of Many Rooms (ayaneinvite2)
                            if (not ev_ayaneinvite2.completed and not ev_ayaneinvite2.missed) or show_complete:
                                if "(!)" in ev_ayaneinvite2.hint:
                                    textbutton _("[ev_ayaneinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayaneinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayaneinvite2.hint]")

                            #What a Wonderful World (ayanelust15)
                            if (not ev_ayanelust15.completed and not ev_ayanelust15.missed) or show_complete:
                                if "(!)" in ev_ayanelust15.hint:
                                    textbutton _("[ev_ayanelust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanelust15.hint]")

                            #Under the World Tree (dojo35)
                            if (not ev_dojo35.completed and not ev_dojo35.missed) or show_complete:
                                if "(!)" in ev_dojo35.hint:
                                    textbutton _("[ev_dojo35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dojo35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dojo35.hint]")

                            #Crash of Thunder (ayanedorm35)
                            if (not ev_ayanedorm35.completed and not ev_ayanedorm35.missed) or show_complete:
                                if "(!)" in ev_ayanedorm35.hint:
                                    textbutton _("[ev_ayanedorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanedorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanedorm35.hint]")

                            #Nevermind (ayanespecial1)
                            if (not ev_ayanespecial1.completed and not ev_ayanespecial1.missed) or show_complete:
                                if "(!)" in ev_ayanespecial1.hint:
                                    textbutton _("[ev_ayanespecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespecial1.hint]")

                            #Before the Sun Comes Up (ayanespecial2)
                            if (not ev_ayanespecial2.completed and not ev_ayanespecial2.missed) or show_complete:
                                if "(!)" in ev_ayanespecial2.hint:
                                    textbutton _("[ev_ayanespecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespecial2.hint]")

                            #Out With the Old (ayanelust20)
                            if (not ev_ayanelust20.completed and not ev_ayanelust20.missed) or show_complete:
                                if "(!)" in ev_ayanelust20.hint:
                                    textbutton _("[ev_ayanelust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanelust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanelust20.hint]")

                            text ("")

                            #Chronokinetics (Hell Exists) (ayanespecial40)
                            if (not ev_ayanespecial40.completed and not ev_ayanespecial40.missed) or show_complete:
                                if "(!)" in ev_ayanespecial40.hint:
                                    textbutton _("[ev_ayanespecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespecial40.hint]")

                            #How the World Works (ayanesanabeach1)
                            if (not ev_ayanesanabeach1.completed and not ev_ayanesanabeach1.missed) or show_complete:
                                if "(!)" in ev_ayanesanabeach1.hint:
                                    textbutton _("[ev_ayanesanabeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanesanabeach1.hint]")

                            #Chiburi (ayanespecial50)
                            if (not ev_ayanespecial50.completed and not ev_ayanespecial50.missed) or show_complete:
                                if "(!)" in ev_ayanespecial50.hint:
                                    textbutton _("[ev_ayanespecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespecial50.hint]")

                            #Furlough (Tell the World) (ayanekirintalk)
                            if (not ev_ayanekirintalk.completed and not ev_ayanekirintalk.missed) or show_complete:
                                if "(!)" in ev_ayanekirintalk.hint:
                                    textbutton _("[ev_ayanekirintalk.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanekirintalk), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanekirintalk.hint]")

                            #Double Jeopardy (ayanespecial55)
                            if (not ev_ayanespecial55.completed and not ev_ayanespecial55.missed) or show_complete:
                                if "(!)" in ev_ayanespecial55.hint:
                                    textbutton _("[ev_ayanespecial55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespecial55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespecial55.hint]")

                            #The Aforementioned Light (ayanebonus1)
                            if (not ev_ayanebonus1.completed and not ev_ayanebonus1.missed) or show_complete:
                                if "(!)" in ev_ayanebonus1.hint:
                                    textbutton _("[ev_ayanebonus1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanebonus1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanebonus1.hint]")

                            #Over & Over (ayanebonus2)
                            if (not ev_ayanebonus2.completed and not ev_ayanebonus2.missed) or show_complete:
                                if "(!)" in ev_ayanebonus2.hint:
                                    textbutton _("[ev_ayanebonus2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanebonus2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanebonus2.hint]")

                            #Dizzy On The Comedown (ayanepool55)
                            if (not ev_ayanepool55.completed and not ev_ayanepool55.missed) or show_complete:
                                if "(!)" in ev_ayanepool55.hint:
                                    textbutton _("[ev_ayanepool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanepool55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanepool55.hint]")

                            text ("")

                            #...But Home is Nowhere (ayanespring1)
                            if (not ev_ayanespring1.completed and not ev_ayanespring1.missed) or show_complete:
                                if "(!)" in ev_ayanespring1.hint:
                                    textbutton _("[ev_ayanespring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespring1.hint]")

                            #Doomsayer (beachfive3)
                            if (not ev_beachfive3.completed and not ev_beachfive3.missed) or show_complete:
                                if "(!)" in ev_beachfive3.hint:
                                    textbutton _("[ev_beachfive3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive3.hint]")

                            #As You Wish (beachfive15)
                            if (not ev_beachfive15.completed and not ev_beachfive15.missed) or show_complete:
                                if "(!)" in ev_beachfive15.hint:
                                    textbutton _("[ev_beachfive15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive15.hint]")

                            #Chamomile (halloweenayane1)
                            if (not ev_halloweenayane1.completed and not ev_halloweenayane1.missed) or show_complete:
                                if "(!)" in ev_halloweenayane1.hint:
                                    textbutton _("[ev_halloweenayane1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenayane1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenayane1.hint]")

                            #Time, Resets, and the Like (halloweenayane2)
                            if (not ev_halloweenayane2.completed and not ev_halloweenayane2.missed) or show_complete:
                                if "(!)" in ev_halloweenayane2.hint:
                                    textbutton _("[ev_halloweenayane2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenayane2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenayane2.hint]")

                            #Soliloquy (Wearing Someone Else's Clothes) (halloweenayane3)
                            if (not ev_halloweenayane3.completed and not ev_halloweenayane3.missed) or show_complete:
                                if "(!)" in ev_halloweenayane3.hint:
                                    textbutton _("[ev_halloweenayane3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenayane3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenayane3.hint]")

                            #In Shoes That Don't Fit (ayanespring2)
                            if (not ev_ayanespring2.completed and not ev_ayanespring2.missed) or show_complete:
                                if "(!)" in ev_ayanespring2.hint:
                                    textbutton _("[ev_ayanespring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespring2.hint]")

                            #Mortal Coil (Gay Stuff) (ayanespring3)
                            if (not ev_ayanespring3.completed and not ev_ayanespring3.missed) or show_complete:
                                if "(!)" in ev_ayanespring3.hint:
                                    textbutton _("[ev_ayanespring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespring3.hint]")

                            #Our Cage in Tralfamadore (undeservedfuture1)
                            if (not ev_undeservedfuture1.completed and not ev_undeservedfuture1.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture1.hint:
                                    textbutton _("[ev_undeservedfuture1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture1.hint]")

                            #Ikura (undeservedfuture2)
                            if (not ev_undeservedfuture2.completed and not ev_undeservedfuture2.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture2.hint:
                                    textbutton _("[ev_undeservedfuture2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture2.hint]")

                            #A Nightmare, in Retrospect (undeservedfuture3)
                            if (not ev_undeservedfuture3.completed and not ev_undeservedfuture3.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture3.hint:
                                    textbutton _("[ev_undeservedfuture3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture3.hint]")

                            #Trophy Wife Pt. I (undeservedfuture4)
                            if (not ev_undeservedfuture4.completed and not ev_undeservedfuture4.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture4.hint:
                                    textbutton _("[ev_undeservedfuture4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture4.hint]")

                            #Light of My Life (undeservedfuture5)
                            if (not ev_undeservedfuture5.completed and not ev_undeservedfuture5.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture5.hint:
                                    textbutton _("[ev_undeservedfuture5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture5.hint]")

                            #Infinite Joy (undeservedfuture6)
                            if (not ev_undeservedfuture6.completed and not ev_undeservedfuture6.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture6.hint:
                                    textbutton _("[ev_undeservedfuture6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture6.hint]")

                            #Bitter Cherries (undeservedfuture7)
                            if (not ev_undeservedfuture7.completed and not ev_undeservedfuture7.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture7.hint:
                                    textbutton _("[ev_undeservedfuture7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture7.hint]")

                            #Trophy Wife Pt. II (undeservedfuture8)
                            if (not ev_undeservedfuture8.completed and not ev_undeservedfuture8.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture8.hint:
                                    textbutton _("[ev_undeservedfuture8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture8.hint]")

                            #Like Lions (undeservedfuture9)
                            if (not ev_undeservedfuture9.completed and not ev_undeservedfuture9.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture9.hint:
                                    textbutton _("[ev_undeservedfuture9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture9.hint]")

                            #Aomori (undeservedfuture10)
                            if (not ev_undeservedfuture10.completed and not ev_undeservedfuture10.missed) or show_complete:
                                if "(!)" in ev_undeservedfuture10.hint:
                                    textbutton _("[ev_undeservedfuture10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_undeservedfuture10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_undeservedfuture10.hint]")

                            #Transpacific Sadness Symposium N: CHAINSMOKER CHANGELING (ayanespring4)
                            if (not ev_ayanespring4.completed and not ev_ayanespring4.missed) or show_complete:
                                if "(!)" in ev_ayanespring4.hint:
                                    textbutton _("[ev_ayanespring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanespring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanespring4.hint]")

                    #CHIKAHINT

                    if showgirl == "Chika":

                        if not _in_replay:

                            #The Retail Machine (firsttimemall)
                            if (not ev_firsttimemall.completed and not ev_firsttimemall.missed) or show_complete:
                                if "(!)" in ev_firsttimemall.hint:
                                    textbutton _("[ev_firsttimemall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimemall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimemall.hint]")

                            #A Dog that Does Math (chikafirsthall)
                            if (not ev_chikafirsthall.completed and not ev_chikafirsthall.missed) or show_complete:
                                if "(!)" in ev_chikafirsthall.hint:
                                    textbutton _("[ev_chikafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikafirsthall.hint]")

                            #Big Shot Teacher (mall5)
                            if (not ev_mall5.completed and not ev_mall5.missed) or show_complete:
                                if "(!)" in ev_mall5.hint:
                                    textbutton _("[ev_mall5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall5.hint]")

                            #Something About Biting (chikadorm5)
                            if (not ev_chikadorm5.completed and not ev_chikadorm5.missed) or show_complete:
                                if "(!)" in ev_chikadorm5.hint:
                                    textbutton _("[ev_chikadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadorm5.hint]")

                            #Behind The Curtain (mall10)
                            if (not ev_mall10.completed and not ev_mall10.missed) or show_complete:
                                if "(!)" in ev_mall10.hint:
                                    textbutton _("[ev_mall10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall10.hint]")

                            #Side Event (chikadorm10)
                            if (not ev_chikadorm10.completed and not ev_chikadorm10.missed) or show_complete:
                                if "(!)" in ev_chikadorm10.hint:
                                    textbutton _("[ev_chikadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadorm10.hint]")

                            #A Castle for Everyone (chikadorm15)
                            if (not ev_chikadorm15.completed and not ev_chikadorm15.missed) or show_complete:
                                if "(!)" in ev_chikadorm15.hint:
                                    textbutton _("[ev_chikadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadorm15.hint]")

                            #A Dog that Doesn't Do Math (mall15)
                            if (not ev_mall15.completed and not ev_mall15.missed) or show_complete:
                                if "(!)" in ev_mall15.hint:
                                    textbutton _("[ev_mall15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall15.hint]")

                            #Schadenfreude (chikadorm20)
                            if (not ev_chikadorm20.completed and not ev_chikadorm20.missed) or show_complete:
                                if "(!)" in ev_chikadorm20.hint:
                                    textbutton _("[ev_chikadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadorm20.hint]")

                            #True Power: Unleashed (mall20)
                            if (not ev_mall20.completed and not ev_mall20.missed) or show_complete:
                                if "(!)" in ev_mall20.hint:
                                    textbutton _("[ev_mall20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall20.hint]")

                            #Detention (day139)
                            if (not ev_day139.completed and not ev_day139.missed) or show_complete:
                                if "(!)" in ev_day139.hint:
                                    textbutton _("[ev_day139.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day139), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_day139.hint]")

                            #A Trip to the Moon (chikainvite1)
                            if (not ev_chikainvite1.completed and not ev_chikainvite1.missed) or show_complete:
                                if "(!)" in ev_chikainvite1.hint:
                                    textbutton _("[ev_chikainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikainvite1.hint]")

                            #First Hunt (chikainvite2)
                            if (not ev_chikainvite2.completed and not ev_chikainvite2.missed) or show_complete:
                                if "(!)" in ev_chikainvite2.hint:
                                    textbutton _("[ev_chikainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikainvite2.hint]")

                            text ("")

                            #Baby it's Cold Outside (chikalust10)
                            if (not ev_chikalust10.completed and not ev_chikalust10.missed) or show_complete:
                                if "(!)" in ev_chikalust10.hint:
                                    textbutton _("[ev_chikalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikalust10.hint]")

                            #Little Miracles (chikaonsen1)
                            if (not ev_chikaonsen1.completed and not ev_chikaonsen1.missed) or show_complete:
                                if "(!)" in ev_chikaonsen1.hint:
                                    textbutton _("[ev_chikaonsen1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaonsen1.hint]")

                            #Bleed (chikaonsen2)
                            if (not ev_chikaonsen2.completed and not ev_chikaonsen2.missed) or show_complete:
                                if "(!)" in ev_chikaonsen2.hint:
                                    textbutton _("[ev_chikaonsen2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaonsen2.hint]")

                            #Three Words (chikaonsen3)
                            if (not ev_chikaonsen3.completed and not ev_chikaonsen3.missed) or show_complete:
                                if "(!)" in ev_chikaonsen3.hint:
                                    textbutton _("[ev_chikaonsen3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaonsen3.hint]")

                            #Zanzibar (Counting Cats) (chikaonsen4)
                            if (not ev_chikaonsen4.completed and not ev_chikaonsen4.missed) or show_complete:
                                if "(!)" in ev_chikaonsen4.hint:
                                    textbutton _("[ev_chikaonsen4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaonsen4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaonsen4.hint]")

                            #The Princess & The Pauper (chikalust15)
                            if (not ev_chikalust15.completed and not ev_chikalust15.missed) or show_complete:
                                if "(!)" in ev_chikalust15.hint:
                                    textbutton _("[ev_chikalust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikalust15.hint]")

                            #Into the Woods (chikalust20)
                            if (not ev_chikalust20.completed and not ev_chikalust20.missed) or show_complete:
                                if "(!)" in ev_chikalust20.hint:
                                    textbutton _("[ev_chikalust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikalust20.hint]")

                            #In Search of Summer (chikaspecial40)
                            if (not ev_chikaspecial40.completed and not ev_chikaspecial40.missed) or show_complete:
                                if "(!)" in ev_chikaspecial40.hint:
                                    textbutton _("[ev_chikaspecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspecial40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspecial40.hint]")

                            #Self Care (mall40)
                            if (not ev_mall40.completed and not ev_mall40.missed) or show_complete:
                                if "(!)" in ev_mall40.hint:
                                    textbutton _("[ev_mall40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall40.hint]")

                            #The Gap in the Curtain (mall40p2)
                            if (not ev_mall40p2.completed and not ev_mall40p2.missed) or show_complete:
                                if "(!)" in ev_mall40p2.hint:
                                    textbutton _("[ev_mall40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall40p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall40p2.hint]")

                            #The Gap in the Door (chikadate45)
                            if (not ev_chikadate45.completed and not ev_chikadate45.missed) or show_complete:
                                if "(!)" in ev_chikadate45.hint:
                                    textbutton _("[ev_chikadate45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadate45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadate45.hint]")

                            text ("")

                            #Mating Season (chikalust25)
                            if (not ev_chikalust25.completed and not ev_chikalust25.missed) or show_complete:
                                if "(!)" in ev_chikalust25.hint:
                                    textbutton _("[ev_chikalust25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikalust25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikalust25.hint]")

                            #Rough Cuts (mall45)
                            if (not ev_mall45.completed and not ev_mall45.missed) or show_complete:
                                if "(!)" in ev_mall45.hint:
                                    textbutton _("[ev_mall45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mall45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mall45.hint]")

                            #Curry Night (chikaspecial45)
                            if (not ev_chikaspecial45.completed and not ev_chikaspecial45.missed) or show_complete:
                                if "(!)" in ev_chikaspecial45.hint:
                                    textbutton _("[ev_chikaspecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspecial45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspecial45.hint]")

                            #Our Time Atop This Mattress (chikadorm45)
                            if (not ev_chikadorm45.completed and not ev_chikadorm45.missed) or show_complete:
                                if "(!)" in ev_chikadorm45.hint:
                                    textbutton _("[ev_chikadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikadorm45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikadorm45.hint]")

                            text ("")

                            #Gold Digger (chikaspring1)
                            if (not ev_chikaspring1.completed and not ev_chikaspring1.missed) or show_complete:
                                if "(!)" in ev_chikaspring1.hint:
                                    textbutton _("[ev_chikaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring1.hint]")

                            #Original Sin (chikaspring2)
                            if (not ev_chikaspring2.completed and not ev_chikaspring2.missed) or show_complete:
                                if "(!)" in ev_chikaspring2.hint:
                                    textbutton _("[ev_chikaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring2.hint]")

                            #To Drink, To Drown (chikaspring3)
                            if (not ev_chikaspring3.completed and not ev_chikaspring3.missed) or show_complete:
                                if "(!)" in ev_chikaspring3.hint:
                                    textbutton _("[ev_chikaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring3.hint]")

                            #Rabies (chikaspring4)
                            if (not ev_chikaspring4.completed and not ev_chikaspring4.missed) or show_complete:
                                if "(!)" in ev_chikaspring4.hint:
                                    textbutton _("[ev_chikaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring4.hint]")

                            #Frogging (chikaspring5)
                            if (not ev_chikaspring5.completed and not ev_chikaspring5.missed) or show_complete:
                                if "(!)" in ev_chikaspring5.hint:
                                    textbutton _("[ev_chikaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring5.hint]")

                            #Everyone I've Ever Loved (chikaspring6)
                            if (not ev_chikaspring6.completed and not ev_chikaspring6.missed) or show_complete:
                                if "(!)" in ev_chikaspring6.hint:
                                    textbutton _("[ev_chikaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring6.hint]")

                            #Transpacific Sadness Symposium V: NEW BLACK PARADIGM (chikaspring7)
                            if (not ev_chikaspring7.completed and not ev_chikaspring7.missed) or show_complete:
                                if "(!)" in ev_chikaspring7.hint:
                                    textbutton _("[ev_chikaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring7.hint]")

                            #Chika-chan vs. Auto-Pilot (chikaspring8)
                            if (not ev_chikaspring8.completed and not ev_chikaspring8.missed) or show_complete:
                                if "(!)" in ev_chikaspring8.hint:
                                    textbutton _("[ev_chikaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikaspring8.hint]")

                            #A Violent Sort of Sadness (chikachristmalloween1)
                            if (not ev_chikachristmalloween1.completed and not ev_chikachristmalloween1.missed) or show_complete:
                                if "(!)" in ev_chikachristmalloween1.hint:
                                    textbutton _("[ev_chikachristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikachristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikachristmalloween1.hint]")

                            #See You in School (chikachristmalloween2)
                            if (not ev_chikachristmalloween2.completed and not ev_chikachristmalloween2.missed) or show_complete:
                                if "(!)" in ev_chikachristmalloween2.hint:
                                    textbutton _("[ev_chikachristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chikachristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chikachristmalloween2.hint]")

                    #CHINAMIHINT

                    if showgirl == "Chinami":

                        if not _in_replay:

                            #5,000 Year-Old Wizard (chinamidate1)
                            if (not ev_chinamidate1.completed and not ev_chinamidate1.missed) or show_complete:
                                if "(!)" in ev_chinamidate1.hint:
                                    textbutton _("[ev_chinamidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate1.hint]")

                            #Chinami-Corp (chinamidate5)
                            if (not ev_chinamidate5.completed and not ev_chinamidate5.missed) or show_complete:
                                if "(!)" in ev_chinamidate5.hint:
                                    textbutton _("[ev_chinamidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate5.hint]")

                            text ("")

                            #Giant Pool of Jell-O (chinamidate10)
                            if (not ev_chinamidate10.completed and not ev_chinamidate10.missed) or show_complete:
                                if "(!)" in ev_chinamidate10.hint:
                                    textbutton _("[ev_chinamidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate10.hint]")

                            #Pool Party (Love & Puppies) (chinamidate15)
                            if (not ev_chinamidate15.completed and not ev_chinamidate15.missed) or show_complete:
                                if "(!)" in ev_chinamidate15.hint:
                                    textbutton _("[ev_chinamidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate15.hint]")

                            #Happy Hour (chinamidate20)
                            if (not ev_chinamidate20.completed and not ev_chinamidate20.missed) or show_complete:
                                if "(!)" in ev_chinamidate20.hint:
                                    textbutton _("[ev_chinamidate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate20.hint]")

                            text ("")

                            #Death Trap (chinamidate25)
                            if (not ev_chinamidate25.completed and not ev_chinamidate25.missed) or show_complete:
                                if "(!)" in ev_chinamidate25.hint:
                                    textbutton _("[ev_chinamidate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate25.hint]")

                            #Bad News Bears (chinamidate30)
                            if (not ev_chinamidate30.completed and not ev_chinamidate30.missed) or show_complete:
                                if "(!)" in ev_chinamidate30.hint:
                                    textbutton _("[ev_chinamidate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamidate30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamidate30.hint]")

                            text ("")

                            #Lucky (China Doll) (chinamispring1)
                            if (not ev_chinamispring1.completed and not ev_chinamispring1.missed) or show_complete:
                                if "(!)" in ev_chinamispring1.hint:
                                    textbutton _("[ev_chinamispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring1.hint]")

                            #Holden Caulfield (chinamispring2)
                            if (not ev_chinamispring2.completed and not ev_chinamispring2.missed) or show_complete:
                                if "(!)" in ev_chinamispring2.hint:
                                    textbutton _("[ev_chinamispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring2.hint]")

                            #Backwards Boulevard (chinamispring3)
                            if (not ev_chinamispring3.completed and not ev_chinamispring3.missed) or show_complete:
                                if "(!)" in ev_chinamispring3.hint:
                                    textbutton _("[ev_chinamispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring3.hint]")

                            #Feed Me to the Farm (chinamispring4)
                            if (not ev_chinamispring4.completed and not ev_chinamispring4.missed) or show_complete:
                                if "(!)" in ev_chinamispring4.hint:
                                    textbutton _("[ev_chinamispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring4.hint]")

                            #Obnoxious Sexual Rampage (chinamispring5)
                            if (not ev_chinamispring5.completed and not ev_chinamispring5.missed) or show_complete:
                                if "(!)" in ev_chinamispring5.hint:
                                    textbutton _("[ev_chinamispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring5.hint]")

                            #Five Hundred Pancakes (chinamispring6)
                            if (not ev_chinamispring6.completed and not ev_chinamispring6.missed) or show_complete:
                                if "(!)" in ev_chinamispring6.hint:
                                    textbutton _("[ev_chinamispring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring6.hint]")

                            #My Adventures as a Trash Compactor (chinamispring7)
                            if (not ev_chinamispring7.completed and not ev_chinamispring7.missed) or show_complete:
                                if "(!)" in ev_chinamispring7.hint:
                                    textbutton _("[ev_chinamispring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring7.hint]")

                            #Transpacific Sadness Symposium IX: HUNG HIGH IN THE HARE HOUSE (chinamispring8)
                            if (not ev_chinamispring8.completed and not ev_chinamispring8.missed) or show_complete:
                                if "(!)" in ev_chinamispring8.hint:
                                    textbutton _("[ev_chinamispring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_chinamispring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_chinamispring8.hint]")

                    #FUTABAHINT

                    if showgirl == "Futaba":

                        if not _in_replay:

                            #Impossible Blossoms (firsttimelibrary)
                            if (not ev_firsttimelibrary.completed and not ev_firsttimelibrary.missed) or show_complete:
                                if "(!)" in ev_firsttimelibrary.hint:
                                    textbutton _("[ev_firsttimelibrary.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimelibrary), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimelibrary.hint]")

                            #Fan Fiction (futabafall)
                            if (not ev_futabafall.completed and not ev_futabafall.missed) or show_complete:
                                if "(!)" in ev_futabafall.hint:
                                    textbutton _("[ev_futabafall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabafall.hint]")

                            #Upside Down (library10)
                            if (not ev_library10.completed and not ev_library10.missed) or show_complete:
                                if "(!)" in ev_library10.hint:
                                    textbutton _("[ev_library10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library10.hint]")

                            #Unidentical Twins (futabafirsthall)
                            if (not ev_futabafirsthall.completed and not ev_futabafirsthall.missed) or show_complete:
                                if "(!)" in ev_futabafirsthall.hint:
                                    textbutton _("[ev_futabafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabafirsthall.hint]")

                            #Under the Radar (futabafirstvisit)
                            if (not ev_futabafirstvisit.completed and not ev_futabafirstvisit.missed) or show_complete:
                                if "(!)" in ev_futabafirstvisit.hint:
                                    textbutton _("[ev_futabafirstvisit.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabafirstvisit), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabafirstvisit.hint]")

                            #Cutting Through Cocoons (futabadorm10)
                            if (not ev_futabadorm10.completed and not ev_futabadorm10.missed) or show_complete:
                                if "(!)" in ev_futabadorm10.hint:
                                    textbutton _("[ev_futabadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm10.hint]")

                            #Self-Insert (library15)
                            if (not ev_library15.completed and not ev_library15.missed) or show_complete:
                                if "(!)" in ev_library15.hint:
                                    textbutton _("[ev_library15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library15.hint]")

                            #Broken Flowers (futabanew1)
                            if (not ev_futabanew1.completed and not ev_futabanew1.missed) or show_complete:
                                if "(!)" in ev_futabanew1.hint:
                                    textbutton _("[ev_futabanew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabanew1.hint]")

                            #Great Burdock Leaves (futabanew2)
                            if (not ev_futabanew2.completed and not ev_futabanew2.missed) or show_complete:
                                if "(!)" in ev_futabanew2.hint:
                                    textbutton _("[ev_futabanew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabanew2.hint]")

                            #Clam's Tongue (futabanew3)
                            if (not ev_futabanew3.completed and not ev_futabanew3.missed) or show_complete:
                                if "(!)" in ev_futabanew3.hint:
                                    textbutton _("[ev_futabanew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabanew3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabanew3.hint]")

                            #Legs of a Dying Spider (futabadorm15)
                            if (not ev_futabadorm15.completed and not ev_futabadorm15.missed) or show_complete:
                                if "(!)" in ev_futabadorm15.hint:
                                    textbutton _("[ev_futabadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm15.hint]")

                            #Only Child (library20)
                            if (not ev_library20.completed and not ev_library20.missed) or show_complete:
                                if "(!)" in ev_library20.hint:
                                    textbutton _("[ev_library20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library20.hint]")

                            #A Book About Dragons (library25)
                            if (not ev_library25.completed and not ev_library25.missed) or show_complete:
                                if "(!)" in ev_library25.hint:
                                    textbutton _("[ev_library25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library25.hint]")

                            #Two Hours (futabadorm25)
                            if (not ev_futabadorm25.completed and not ev_futabadorm25.missed) or show_complete:
                                if "(!)" in ev_futabadorm25.hint:
                                    textbutton _("[ev_futabadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm25.hint]")

                            #Like Fucking a Cloud (day86)
                            if (not ev_day86.completed and not ev_day86.missed) or show_complete:
                                if "(!)" in ev_day86.hint:
                                    textbutton _("[ev_day86.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_day86), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_day86.hint]")

                            #Under the Table (library30)
                            if (not ev_library30.completed and not ev_library30.missed) or show_complete:
                                if "(!)" in ev_library30.hint:
                                    textbutton _("[ev_library30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library30.hint]")

                            #A Tree Falls in the Forest (futabadorm30)
                            if (not ev_futabadorm30.completed and not ev_futabadorm30.missed) or show_complete:
                                if "(!)" in ev_futabadorm30.hint:
                                    textbutton _("[ev_futabadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm30.hint]")

                            #No, You (library35)
                            if (not ev_library35.completed and not ev_library35.missed) or show_complete:
                                if "(!)" in ev_library35.hint:
                                    textbutton _("[ev_library35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library35.hint]")

                            #Overload (futabadorm35)
                            if (not ev_futabadorm35.completed and not ev_futabadorm35.missed) or show_complete:
                                if "(!)" in ev_futabadorm35.hint:
                                    textbutton _("[ev_futabadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm35.hint]")

                            text ("")

                            #Selfless (futabalust10)
                            if (not ev_futabalust10.completed and not ev_futabalust10.missed) or show_complete:
                                if "(!)" in ev_futabalust10.hint:
                                    textbutton _("[ev_futabalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabalust10.hint]")

                            #Sonnet 18 (futabainvite1)
                            if (not ev_futabainvite1.completed and not ev_futabainvite1.missed) or show_complete:
                                if "(!)" in ev_futabainvite1.hint:
                                    textbutton _("[ev_futabainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabainvite1.hint]")

                            #Floral Aura (futabainvite2)
                            if (not ev_futabainvite2.completed and not ev_futabainvite2.missed) or show_complete:
                                if "(!)" in ev_futabainvite2.hint:
                                    textbutton _("[ev_futabainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabainvite2.hint]")

                            #C'est La Vie (futabalust15)
                            if (not ev_futabalust15.completed and not ev_futabalust15.missed) or show_complete:
                                if "(!)" in ev_futabalust15.hint:
                                    textbutton _("[ev_futabalust15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabalust15.hint]")

                            #Skin (Start Somewhere) (futabadorm40)
                            if (not ev_futabadorm40.completed and not ev_futabadorm40.missed) or show_complete:
                                if "(!)" in ev_futabadorm40.hint:
                                    textbutton _("[ev_futabadorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm40.hint]")

                            #Shadowplay (library40)
                            if (not ev_library40.completed and not ev_library40.missed) or show_complete:
                                if "(!)" in ev_library40.hint:
                                    textbutton _("[ev_library40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library40.hint]")

                            #Without Running Away (library40part2)
                            if (not ev_library40part2.completed and not ev_library40part2.missed) or show_complete:
                                if "(!)" in ev_library40part2.hint:
                                    textbutton _("[ev_library40part2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library40part2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library40part2.hint]")

                            #Hall of Mirrors (futabadorm45)
                            if (not ev_futabadorm45.completed and not ev_futabadorm45.missed) or show_complete:
                                if "(!)" in ev_futabadorm45.hint:
                                    textbutton _("[ev_futabadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm45.hint]")

                            text ("")

                            #This Infected Wound (futabadorm50)
                            if (not ev_futabadorm50.completed and not ev_futabadorm50.missed) or show_complete:
                                if "(!)" in ev_futabadorm50.hint:
                                    textbutton _("[ev_futabadorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabadorm50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabadorm50.hint]")

                            #Bestial Vigor (library50)
                            if (not ev_library50.completed and not ev_library50.missed) or show_complete:
                                if "(!)" in ev_library50.hint:
                                    textbutton _("[ev_library50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_library50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_library50.hint]")

                            #Too Blind To See (futabainvite3)
                            if (not ev_futabainvite3.completed and not ev_futabainvite3.missed) or show_complete:
                                if "(!)" in ev_futabainvite3.hint:
                                    textbutton _("[ev_futabainvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabainvite3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabainvite3.hint]")

                            #Toys (makotofutabafuntimelustevent)
                            if (not ev_makotofutabafuntimelustevent.completed and not ev_makotofutabafuntimelustevent.missed) or show_complete:
                                if "(!)" in ev_makotofutabafuntimelustevent.hint:
                                    textbutton _("[ev_makotofutabafuntimelustevent.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotofutabafuntimelustevent), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotofutabafuntimelustevent.hint]")

                            #Book Burning (futabaspecial60p1)
                            if (not ev_futabaspecial60p1.completed and not ev_futabaspecial60p1.missed) or show_complete:
                                if "(!)" in ev_futabaspecial60p1.hint:
                                    textbutton _("[ev_futabaspecial60p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspecial60p1.hint]")

                            #Pg. 99 (futabaspecial60p2)
                            if (not ev_futabaspecial60p2.completed and not ev_futabaspecial60p2.missed) or show_complete:
                                if "(!)" in ev_futabaspecial60p2.hint:
                                    textbutton _("[ev_futabaspecial60p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspecial60p2.hint]")

                            #Fish Eyes (futabaspecial60p3)
                            if (not ev_futabaspecial60p3.completed and not ev_futabaspecial60p3.missed) or show_complete:
                                if "(!)" in ev_futabaspecial60p3.hint:
                                    textbutton _("[ev_futabaspecial60p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspecial60p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspecial60p3.hint]")

                            text ("")

                            #Weapons of Mass Destruction (futabalust25)
                            if (not ev_futabalust25.completed and not ev_futabalust25.missed) or show_complete:
                                if "(!)" in ev_futabalust25.hint:
                                    textbutton _("[ev_futabalust25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabalust25.hint]")

                            #My Curse (futabaspring1)
                            if (not ev_futabaspring1.completed and not ev_futabaspring1.missed) or show_complete:
                                if "(!)" in ev_futabaspring1.hint:
                                    textbutton _("[ev_futabaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspring1.hint]")

                            #Transpacific Sadness Symposium II: SISTER SOFTSKIN (beachfive9)
                            if (not ev_beachfive9.completed and not ev_beachfive9.missed) or show_complete:
                                if "(!)" in ev_beachfive9.hint:
                                    textbutton _("[ev_beachfive9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive9.hint]")

                            #The Meat in the Hole in the Wall in My Room (futabalust40)
                            if (not ev_futabalust40.completed and not ev_futabalust40.missed) or show_complete:
                                if "(!)" in ev_futabalust40.hint:
                                    textbutton _("[ev_futabalust40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabalust40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabalust40.hint]")

                            #The Taking Tree (futabaspring2)
                            if (not ev_futabaspring2.completed and not ev_futabaspring2.missed) or show_complete:
                                if "(!)" in ev_futabaspring2.hint:
                                    textbutton _("[ev_futabaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspring2.hint]")

                            #Spam (beachsixfutaba1)
                            if (not ev_beachsixfutaba1.completed and not ev_beachsixfutaba1.missed) or show_complete:
                                if "(!)" in ev_beachsixfutaba1.hint:
                                    textbutton _("[ev_beachsixfutaba1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixfutaba1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixfutaba1.hint]")

                            #ELATION PROTOCOL 99: RE:SOLUTION (RESOLVED) (futabaspring3)
                            if (not ev_futabaspring3.completed and not ev_futabaspring3.missed) or show_complete:
                                if "(!)" in ev_futabaspring3.hint:
                                    textbutton _("[ev_futabaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspring3.hint]")

                            #New Ways to Love (futabaspring4)
                            if (not ev_futabaspring4.completed and not ev_futabaspring4.missed) or show_complete:
                                if "(!)" in ev_futabaspring4.hint:
                                    textbutton _("[ev_futabaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_futabaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_futabaspring4.hint]")

                    #HARUKAHINT

                    if showgirl == "Haruka":

                        if not _in_replay:

                            #Drunk Again (harukadate1)
                            if (not ev_harukadate1.completed and not ev_harukadate1.missed) or show_complete:
                                if "(!)" in ev_harukadate1.hint:
                                    textbutton _("[ev_harukadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate1.hint]")

                            #Invisible Worm (harukadate5)
                            if (not ev_harukadate5.completed and not ev_harukadate5.missed) or show_complete:
                                if "(!)" in ev_harukadate5.hint:
                                    textbutton _("[ev_harukadate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate5.hint]")

                            #The Need to be Hurt (harukafirstlust)
                            if (not ev_harukafirstlust.completed and not ev_harukafirstlust.missed) or show_complete:
                                if "(!)" in ev_harukafirstlust.hint:
                                    textbutton _("[ev_harukafirstlust.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukafirstlust), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukafirstlust.hint]")

                            #Bad Kitty (harukalust10)
                            if (not ev_harukalust10.completed and not ev_harukalust10.missed) or show_complete:
                                if "(!)" in ev_harukalust10.hint:
                                    textbutton _("[ev_harukalust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukalust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukalust10.hint]")

                            #Performance Review (harukadate10)
                            if (not ev_harukadate10.completed and not ev_harukadate10.missed) or show_complete:
                                if "(!)" in ev_harukadate10.hint:
                                    textbutton _("[ev_harukadate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate10.hint]")

                            #Watching TV Alone (harukadate15)
                            if (not ev_harukadate15.completed and not ev_harukadate15.missed) or show_complete:
                                if "(!)" in ev_harukadate15.hint:
                                    textbutton _("[ev_harukadate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate15.hint]")

                            text ("")

                            #Shades of Green (harukainvite1)
                            if (not ev_harukainvite1.completed and not ev_harukainvite1.missed) or show_complete:
                                if "(!)" in ev_harukainvite1.hint:
                                    textbutton _("[ev_harukainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukainvite1.hint]")

                            #Roses (harukainvite2)
                            if (not ev_harukainvite2.completed and not ev_harukainvite2.missed) or show_complete:
                                if "(!)" in ev_harukainvite2.hint:
                                    textbutton _("[ev_harukainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukainvite2.hint]")

                            #Sober-ish (harukadate20)
                            if (not ev_harukadate20.completed and not ev_harukadate20.missed) or show_complete:
                                if "(!)" in ev_harukadate20.hint:
                                    textbutton _("[ev_harukadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate20.hint]")

                            #Unfiltered Tap Water (harukainvite3)
                            if (not ev_harukainvite3.completed and not ev_harukainvite3.missed) or show_complete:
                                if "(!)" in ev_harukainvite3.hint:
                                    textbutton _("[ev_harukainvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukainvite3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukainvite3.hint]")

                            text ("")

                            #The World Outside The Walls (sadgirls2)
                            if (not ev_sadgirls2.completed and not ev_sadgirls2.missed) or show_complete:
                                if "(!)" in ev_sadgirls2.hint:
                                    textbutton _("[ev_sadgirls2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls2.hint]")

                            #To Anyone Who Passes By (sadgirls4)
                            if (not ev_sadgirls4.completed and not ev_sadgirls4.missed) or show_complete:
                                if "(!)" in ev_sadgirls4.hint:
                                    textbutton _("[ev_sadgirls4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls4.hint]")

                            #Again, I Can't Recall (sadgirls5)
                            if (not ev_sadgirls5.completed and not ev_sadgirls5.missed) or show_complete:
                                if "(!)" in ev_sadgirls5.hint:
                                    textbutton _("[ev_sadgirls5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls5.hint]")

                            #Secret Weapon (harukalust25)
                            if (not ev_harukalust25.completed and not ev_harukalust25.missed) or show_complete:
                                if "(!)" in ev_harukalust25.hint:
                                    textbutton _("[ev_harukalust25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukalust25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukalust25.hint]")

                            #Stress Level Midnight (makihornytrip1)
                            if (not ev_makihornytrip1.completed and not ev_makihornytrip1.missed) or show_complete:
                                if "(!)" in ev_makihornytrip1.hint:
                                    textbutton _("[ev_makihornytrip1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makihornytrip1.hint]")

                            #Conflict of Interest (makihornytrip4)
                            if (not ev_makihornytrip4.completed and not ev_makihornytrip4.missed) or show_complete:
                                if "(!)" in ev_makihornytrip4.hint:
                                    textbutton _("[ev_makihornytrip4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makihornytrip4.hint]")

                            #Scum (harukadate30)
                            if (not ev_harukadate30.completed and not ev_harukadate30.missed) or show_complete:
                                if "(!)" in ev_harukadate30.hint:
                                    textbutton _("[ev_harukadate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukadate30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukadate30.hint]")

                            text ("")

                            #Small Paper Cups (harukacamp1)
                            if (not ev_harukacamp1.completed and not ev_harukacamp1.missed) or show_complete:
                                if "(!)" in ev_harukacamp1.hint:
                                    textbutton _("[ev_harukacamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukacamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukacamp1.hint]")

                            #Subhuman (harukaspring1)
                            if (not ev_harukaspring1.completed and not ev_harukaspring1.missed) or show_complete:
                                if "(!)" in ev_harukaspring1.hint:
                                    textbutton _("[ev_harukaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring1.hint]")

                            #Limp-Dicked Loser (harukaspring2)
                            if (not ev_harukaspring2.completed and not ev_harukaspring2.missed) or show_complete:
                                if "(!)" in ev_harukaspring2.hint:
                                    textbutton _("[ev_harukaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring2.hint]")

                            #This Town, On its Knees (harukaspring3)
                            if (not ev_harukaspring3.completed and not ev_harukaspring3.missed) or show_complete:
                                if "(!)" in ev_harukaspring3.hint:
                                    textbutton _("[ev_harukaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring3.hint]")

                            #JR East's DC Tilting EMU E353 Series (Kaiji) (harukaspring4)
                            if (not ev_harukaspring4.completed and not ev_harukaspring4.missed) or show_complete:
                                if "(!)" in ev_harukaspring4.hint:
                                    textbutton _("[ev_harukaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring4.hint]")

                            #Traitor's Mark (harukachristmalloween1)
                            if (not ev_harukachristmalloween1.completed and not ev_harukachristmalloween1.missed) or show_complete:
                                if "(!)" in ev_harukachristmalloween1.hint:
                                    textbutton _("[ev_harukachristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukachristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukachristmalloween1.hint]")

                            #Blood in the Water (harukachristmalloween2)
                            if (not ev_harukachristmalloween2.completed and not ev_harukachristmalloween2.missed) or show_complete:
                                if "(!)" in ev_harukachristmalloween2.hint:
                                    textbutton _("[ev_harukachristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukachristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukachristmalloween2.hint]")

                            #Ancient Dragons (harukaspring5)
                            if (not ev_harukaspring5.completed and not ev_harukaspring5.missed) or show_complete:
                                if "(!)" in ev_harukaspring5.hint:
                                    textbutton _("[ev_harukaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring5.hint]")

                            #Camelopardalis (At Hoshimachi Station) (harukaspring6)
                            if (not ev_harukaspring6.completed and not ev_harukaspring6.missed) or show_complete:
                                if "(!)" in ev_harukaspring6.hint:
                                    textbutton _("[ev_harukaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_harukaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_harukaspring6.hint]")

                    #IMANIHINT

                    if showgirl == "Imani":

                        if not _in_replay:

                            #Somewhere I Belong (imanidate1)
                            if (not ev_imanidate1.completed and not ev_imanidate1.missed) or show_complete:
                                if "(!)" in ev_imanidate1.hint:
                                    textbutton _("[ev_imanidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanidate1.hint]")

                            #A Hairline Fracture (imanidate5)
                            if (not ev_imanidate5.completed and not ev_imanidate5.missed) or show_complete:
                                if "(!)" in ev_imanidate5.hint:
                                    textbutton _("[ev_imanidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanidate5.hint]")

                            #Knotted Up (imanidate15p1)
                            if (not ev_imanidate15p1.completed and not ev_imanidate15p1.missed) or show_complete:
                                if "(!)" in ev_imanidate15p1.hint:
                                    textbutton _("[ev_imanidate15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate15p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanidate15p1.hint]")

                            #Arm's Length (imanidate15p2)
                            if (not ev_imanidate15p2.completed and not ev_imanidate15p2.missed) or show_complete:
                                if "(!)" in ev_imanidate15p2.hint:
                                    textbutton _("[ev_imanidate15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanidate15p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanidate15p2.hint]")

                            #Debbie Downer (imanispecial15)
                            if (not ev_imanispecial15.completed and not ev_imanispecial15.missed) or show_complete:
                                if "(!)" in ev_imanispecial15.hint:
                                    textbutton _("[ev_imanispecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispecial15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanispecial15.hint]")

                            text ("")

                            #Antoa Suo Nyamaa (imanispring1)
                            if (not ev_imanispring1.completed and not ev_imanispring1.missed) or show_complete:
                                if "(!)" in ev_imanispring1.hint:
                                    textbutton _("[ev_imanispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanispring1.hint]")

                            #I Will Carry You, My Light (imanispring2)
                            if (not ev_imanispring2.completed and not ev_imanispring2.missed) or show_complete:
                                if "(!)" in ev_imanispring2.hint:
                                    textbutton _("[ev_imanispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanispring2.hint]")

                            #Yehoshua (christmasimani1)
                            if (not ev_christmasimani1.completed and not ev_christmasimani1.missed) or show_complete:
                                if "(!)" in ev_christmasimani1.hint:
                                    textbutton _("[ev_christmasimani1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmasimani1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmasimani1.hint]")

                            #The Truman Show (christmasimani2)
                            if (not ev_christmasimani2.completed and not ev_christmasimani2.missed) or show_complete:
                                if "(!)" in ev_christmasimani2.hint:
                                    textbutton _("[ev_christmasimani2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmasimani2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmasimani2.hint]")

                            #Now & Forever (christmasimani3)
                            if (not ev_christmasimani3.completed and not ev_christmasimani3.missed) or show_complete:
                                if "(!)" in ev_christmasimani3.hint:
                                    textbutton _("[ev_christmasimani3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmasimani3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmasimani3.hint]")

                            #The Devil's Bed (imanilust5)
                            if (not ev_imanilust5.completed and not ev_imanilust5.missed) or show_complete:
                                if "(!)" in ev_imanilust5.hint:
                                    textbutton _("[ev_imanilust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanilust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanilust5.hint]")

                            #Lesbian Hand Stuff (imanispring3)
                            if (not ev_imanispring3.completed and not ev_imanispring3.missed) or show_complete:
                                if "(!)" in ev_imanispring3.hint:
                                    textbutton _("[ev_imanispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanispring3.hint]")

                            #Lost in the Sauce (Pied Piper) (imanispring4)
                            if (not ev_imanispring4.completed and not ev_imanispring4.missed) or show_complete:
                                if "(!)" in ev_imanispring4.hint:
                                    textbutton _("[ev_imanispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_imanispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_imanispring4.hint]")

                    #IOHINT

                    if showgirl == "Io":

                        if not _in_replay:

                            #Viva la Revolución (iofirsthall)
                            if (not ev_iofirsthall.completed and not ev_iofirsthall.missed) or show_complete:
                                if "(!)" in ev_iofirsthall.hint:
                                    textbutton _("[ev_iofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iofirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iofirsthall.hint]")

                            #Nonetheless, I'm Here (bathhouse1)
                            if (not ev_bathhouse1.completed and not ev_bathhouse1.missed) or show_complete:
                                if "(!)" in ev_bathhouse1.hint:
                                    textbutton _("[ev_bathhouse1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse1.hint]")

                            #The Girl with the Dragon Tattoo (bathhouse5)
                            if (not ev_bathhouse5.completed and not ev_bathhouse5.missed) or show_complete:
                                if "(!)" in ev_bathhouse5.hint:
                                    textbutton _("[ev_bathhouse5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse5.hint]")

                            #Unnamed Wooden Robots (iodorm5)
                            if (not ev_iodorm5.completed and not ev_iodorm5.missed) or show_complete:
                                if "(!)" in ev_iodorm5.hint:
                                    textbutton _("[ev_iodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iodorm5.hint]")

                            #Paperthin (iodorm10)
                            if (not ev_iodorm10.completed and not ev_iodorm10.missed) or show_complete:
                                if "(!)" in ev_iodorm10.hint:
                                    textbutton _("[ev_iodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iodorm10.hint]")

                            #Turn On The Lights (bathhouse10)
                            if (not ev_bathhouse10.completed and not ev_bathhouse10.missed) or show_complete:
                                if "(!)" in ev_bathhouse10.hint:
                                    textbutton _("[ev_bathhouse10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse10.hint]")

                            #Amongst Other Things (iodorm15)
                            if (not ev_iodorm15.completed and not ev_iodorm15.missed) or show_complete:
                                if "(!)" in ev_iodorm15.hint:
                                    textbutton _("[ev_iodorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iodorm15.hint]")

                            #One Man's Trash (bathhouse20)
                            if (not ev_bathhouse20.completed and not ev_bathhouse20.missed) or show_complete:
                                if "(!)" in ev_bathhouse20.hint:
                                    textbutton _("[ev_bathhouse20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse20.hint]")

                            #Another Man's Treasure (bathhouse20part2)
                            if (not ev_bathhouse20part2.completed and not ev_bathhouse20part2.missed) or show_complete:
                                if "(!)" in ev_bathhouse20part2.hint:
                                    textbutton _("[ev_bathhouse20part2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse20part2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse20part2.hint]")

                            text ("")

                            #Cupid's Arrow (ioarchery1)
                            if (not ev_ioarchery1.completed and not ev_ioarchery1.missed) or show_complete:
                                if "(!)" in ev_ioarchery1.hint:
                                    textbutton _("[ev_ioarchery1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ioarchery1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ioarchery1.hint]")

                            #Work Less, Not Hard (bathhouse25)
                            if (not ev_bathhouse25.completed and not ev_bathhouse25.missed) or show_complete:
                                if "(!)" in ev_bathhouse25.hint:
                                    textbutton _("[ev_bathhouse25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse25.hint]")

                            #Heartbreak & Harmony (iodorm25)
                            if (not ev_iodorm25.completed and not ev_iodorm25.missed) or show_complete:
                                if "(!)" in ev_iodorm25.hint:
                                    textbutton _("[ev_iodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iodorm25.hint]")

                            #1999 PC Classic, Rollercoaster Tycoon (iospecial30)
                            if (not ev_iospecial30.completed and not ev_iospecial30.missed) or show_complete:
                                if "(!)" in ev_iospecial30.hint:
                                    textbutton _("[ev_iospecial30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospecial30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospecial30.hint]")

                            #Tennis Ball (bathhouse35p1)
                            if (not ev_bathhouse35p1.completed and not ev_bathhouse35p1.missed) or show_complete:
                                if "(!)" in ev_bathhouse35p1.hint:
                                    textbutton _("[ev_bathhouse35p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse35p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse35p1.hint]")

                            #Hold You Over (bathhouse35p2)
                            if (not ev_bathhouse35p2.completed and not ev_bathhouse35p2.missed) or show_complete:
                                if "(!)" in ev_bathhouse35p2.hint:
                                    textbutton _("[ev_bathhouse35p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bathhouse35p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bathhouse35p2.hint]")

                            #Yellow Cactus Flower (iodorm35)
                            if (not ev_iodorm35.completed and not ev_iodorm35.missed) or show_complete:
                                if "(!)" in ev_iodorm35.hint:
                                    textbutton _("[ev_iodorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iodorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iodorm35.hint]")

                            #Two Of Us Are Thinking (ioarchery35)
                            if (not ev_ioarchery35.completed and not ev_ioarchery35.missed) or show_complete:
                                if "(!)" in ev_ioarchery35.hint:
                                    textbutton _("[ev_ioarchery35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ioarchery35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ioarchery35.hint]")

                            text ("")

                            #My Indigo (The Blue Death) (iospring1)
                            if (not ev_iospring1.completed and not ev_iospring1.missed) or show_complete:
                                if "(!)" in ev_iospring1.hint:
                                    textbutton _("[ev_iospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring1.hint]")

                            #Komorebi (iospring2)
                            if (not ev_iospring2.completed and not ev_iospring2.missed) or show_complete:
                                if "(!)" in ev_iospring2.hint:
                                    textbutton _("[ev_iospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring2.hint]")

                            #Stomachache (iospring3)
                            if (not ev_iospring3.completed and not ev_iospring3.missed) or show_complete:
                                if "(!)" in ev_iospring3.hint:
                                    textbutton _("[ev_iospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring3.hint]")

                            #1997 PC Classic, Theme Hospital (iospring4)
                            if (not ev_iospring4.completed and not ev_iospring4.missed) or show_complete:
                                if "(!)" in ev_iospring4.hint:
                                    textbutton _("[ev_iospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring4.hint]")

                            #Even Winning Feels Bad (iospring5)
                            if (not ev_iospring5.completed and not ev_iospring5.missed) or show_complete:
                                if "(!)" in ev_iospring5.hint:
                                    textbutton _("[ev_iospring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring5.hint]")

                            #Endless Black (Sea of Nothing) (dormwarsfiveio1)
                            if (not ev_dormwarsfiveio1.completed and not ev_dormwarsfiveio1.missed) or show_complete:
                                if "(!)" in ev_dormwarsfiveio1.hint:
                                    textbutton _("[ev_dormwarsfiveio1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarsfiveio1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarsfiveio1.hint]")

                            #Man-Meat (iospring6)
                            if (not ev_iospring6.completed and not ev_iospring6.missed) or show_complete:
                                if "(!)" in ev_iospring6.hint:
                                    textbutton _("[ev_iospring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring6.hint]")

                            #Animal Cruelty (iospring7)
                            if (not ev_iospring7.completed and not ev_iospring7.missed) or show_complete:
                                if "(!)" in ev_iospring7.hint:
                                    textbutton _("[ev_iospring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring7.hint]")

                            #The Hatchery (iospring8)
                            if (not ev_iospring8.completed and not ev_iospring8.missed) or show_complete:
                                if "(!)" in ev_iospring8.hint:
                                    textbutton _("[ev_iospring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_iospring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_iospring8.hint]")

                    #KAORIHINT

                    if showgirl == "Kaori":

                        if not _in_replay:

                            #How to Date a Human (kaoridate1)
                            if (not ev_kaoridate1.completed and not ev_kaoridate1.missed) or show_complete:
                                if "(!)" in ev_kaoridate1.hint:
                                    textbutton _("[ev_kaoridate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate1.hint]")

                            #The Best Ways to Rub a Cock (kaoridate5)
                            if (not ev_kaoridate5.completed and not ev_kaoridate5.missed) or show_complete:
                                if "(!)" in ev_kaoridate5.hint:
                                    textbutton _("[ev_kaoridate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate5.hint]")

                            #Objects and Appendages (kaoridate10)
                            if (not ev_kaoridate10.completed and not ev_kaoridate10.missed) or show_complete:
                                if "(!)" in ev_kaoridate10.hint:
                                    textbutton _("[ev_kaoridate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate10.hint]")

                            text ("")

                            #To Die, To Sleep (kaoridate15)
                            if (not ev_kaoridate15.completed and not ev_kaoridate15.missed) or show_complete:
                                if "(!)" in ev_kaoridate15.hint:
                                    textbutton _("[ev_kaoridate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate15.hint]")

                            #Sad Girl Special (kaoridate15p2)
                            if (not ev_kaoridate15p2.completed and not ev_kaoridate15p2.missed) or show_complete:
                                if "(!)" in ev_kaoridate15p2.hint:
                                    textbutton _("[ev_kaoridate15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate15p2.hint]")

                            #Clouds (kaoridate15p3)
                            if (not ev_kaoridate15p3.completed and not ev_kaoridate15p3.missed) or show_complete:
                                if "(!)" in ev_kaoridate15p3.hint:
                                    textbutton _("[ev_kaoridate15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate15p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate15p3.hint]")

                            #Såsom i en Spegel (kaoridate20)
                            if (not ev_kaoridate20.completed and not ev_kaoridate20.missed) or show_complete:
                                if "(!)" in ev_kaoridate20.hint:
                                    textbutton _("[ev_kaoridate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate20.hint]")

                            #Wither (kaoridate25)
                            if (not ev_kaoridate25.completed and not ev_kaoridate25.missed) or show_complete:
                                if "(!)" in ev_kaoridate25.hint:
                                    textbutton _("[ev_kaoridate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate25.hint]")

                            text ("")

                            #Where the Trees Live (kaorispecial35)
                            if (not ev_kaorispecial35.completed and not ev_kaorispecial35.missed) or show_complete:
                                if "(!)" in ev_kaorispecial35.hint:
                                    textbutton _("[ev_kaorispecial35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispecial35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaorispecial35.hint]")

                            #Human Females (kaorispecial40)
                            if (not ev_kaorispecial40.completed and not ev_kaorispecial40.missed) or show_complete:
                                if "(!)" in ev_kaorispecial40.hint:
                                    textbutton _("[ev_kaorispecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispecial40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaorispecial40.hint]")

                            #Run, Rabbit, Run (Why the Fieldmice Hide) (kaoridate40)
                            if (not ev_kaoridate40.completed and not ev_kaoridate40.missed) or show_complete:
                                if "(!)" in ev_kaoridate40.hint:
                                    textbutton _("[ev_kaoridate40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoridate40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoridate40.hint]")

                            text ("")

                            #Tree Village (The Color Machine) (kaoricamp1)
                            if (not ev_kaoricamp1.completed and not ev_kaoricamp1.missed) or show_complete:
                                if "(!)" in ev_kaoricamp1.hint:
                                    textbutton _("[ev_kaoricamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoricamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoricamp1.hint]")

                            #Il Cervo (kaoricamp2)
                            if (not ev_kaoricamp2.completed and not ev_kaoricamp2.missed) or show_complete:
                                if "(!)" in ev_kaoricamp2.hint:
                                    textbutton _("[ev_kaoricamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoricamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoricamp2.hint]")

                            #Friend (halloweenkaori1)
                            if (not ev_halloweenkaori1.completed and not ev_halloweenkaori1.missed) or show_complete:
                                if "(!)" in ev_halloweenkaori1.hint:
                                    textbutton _("[ev_halloweenkaori1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenkaori1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenkaori1.hint]")

                            #Kittens (halloweenkaori2)
                            if (not ev_halloweenkaori2.completed and not ev_halloweenkaori2.missed) or show_complete:
                                if "(!)" in ev_halloweenkaori2.hint:
                                    textbutton _("[ev_halloweenkaori2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenkaori2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenkaori2.hint]")

                            #Seas of White (Why Not Here?) (kaorispring1)
                            if (not ev_kaorispring1.completed and not ev_kaorispring1.missed) or show_complete:
                                if "(!)" in ev_kaorispring1.hint:
                                    textbutton _("[ev_kaorispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaorispring1.hint]")

                            #Clearer Skies & Changing Eyes (kaorispring2)
                            if (not ev_kaorispring2.completed and not ev_kaorispring2.missed) or show_complete:
                                if "(!)" in ev_kaorispring2.hint:
                                    textbutton _("[ev_kaorispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaorispring2.hint]")

                            #Breeding Material (kaorispring3)
                            if (not ev_kaorispring3.completed and not ev_kaorispring3.missed) or show_complete:
                                if "(!)" in ev_kaorispring3.hint:
                                    textbutton _("[ev_kaorispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaorispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaorispring3.hint]")

                            #Borrowed Flesh (kaoriinvite1)
                            if (not ev_kaoriinvite1.completed and not ev_kaoriinvite1.missed) or show_complete:
                                if "(!)" in ev_kaoriinvite1.hint:
                                    textbutton _("[ev_kaoriinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoriinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoriinvite1.hint]")

                            #Scatter the Ashes (kaoriinvite2)
                            if (not ev_kaoriinvite2.completed and not ev_kaoriinvite2.missed) or show_complete:
                                if "(!)" in ev_kaoriinvite2.hint:
                                    textbutton _("[ev_kaoriinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kaoriinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kaoriinvite2.hint]")

                    #KARINHINT

                    if showgirl == "Karin":

                        if not _in_replay:

                            #Further and Further (karindate1)
                            if (not ev_karindate1.completed and not ev_karindate1.missed) or show_complete:
                                if "(!)" in ev_karindate1.hint:
                                    textbutton _("[ev_karindate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate1.hint]")

                            #Walking Penis Monster (karindate5)
                            if (not ev_karindate5.completed and not ev_karindate5.missed) or show_complete:
                                if "(!)" in ev_karindate5.hint:
                                    textbutton _("[ev_karindate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate5.hint]")

                            #If Only (karindate10)
                            if (not ev_karindate10.completed and not ev_karindate10.missed) or show_complete:
                                if "(!)" in ev_karindate10.hint:
                                    textbutton _("[ev_karindate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate10.hint]")

                            text ("")

                            #Dying Alone With Ten Cats (karindate15)
                            if (not ev_karindate15.completed and not ev_karindate15.missed) or show_complete:
                                if "(!)" in ev_karindate15.hint:
                                    textbutton _("[ev_karindate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate15.hint]")

                            #Tendrils of Flame (karinsoccer15)
                            if (not ev_karinsoccer15.completed and not ev_karinsoccer15.missed) or show_complete:
                                if "(!)" in ev_karinsoccer15.hint:
                                    textbutton _("[ev_karinsoccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinsoccer15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinsoccer15.hint]")

                            #The Adventures of Karli & Steve (karinsoccer20)
                            if (not ev_karinsoccer20.completed and not ev_karinsoccer20.missed) or show_complete:
                                if "(!)" in ev_karinsoccer20.hint:
                                    textbutton _("[ev_karinsoccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinsoccer20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinsoccer20.hint]")

                            #Sweet Tooth (karindate20)
                            if (not ev_karindate20.completed and not ev_karindate20.missed) or show_complete:
                                if "(!)" in ev_karindate20.hint:
                                    textbutton _("[ev_karindate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate20.hint]")

                            text ("")

                            #Emerald Eyes (karindate25)
                            if (not ev_karindate25.completed and not ev_karindate25.missed) or show_complete:
                                if "(!)" in ev_karindate25.hint:
                                    textbutton _("[ev_karindate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate25.hint]")

                            #Wrong Places/Wrong Times (karindate30)
                            if (not ev_karindate30.completed and not ev_karindate30.missed) or show_complete:
                                if "(!)" in ev_karindate30.hint:
                                    textbutton _("[ev_karindate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karindate30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karindate30.hint]")

                            text ("")

                            #Touch of Grey (karinspring1)
                            if (not ev_karinspring1.completed and not ev_karinspring1.missed) or show_complete:
                                if "(!)" in ev_karinspring1.hint:
                                    textbutton _("[ev_karinspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring1.hint]")

                            #Paranoid (karinspring2)
                            if (not ev_karinspring2.completed and not ev_karinspring2.missed) or show_complete:
                                if "(!)" in ev_karinspring2.hint:
                                    textbutton _("[ev_karinspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring2.hint]")

                            #Better Boy (karinspring3)
                            if (not ev_karinspring3.completed and not ev_karinspring3.missed) or show_complete:
                                if "(!)" in ev_karinspring3.hint:
                                    textbutton _("[ev_karinspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring3.hint]")

                            #Back to the Basics (karinspring4)
                            if (not ev_karinspring4.completed and not ev_karinspring4.missed) or show_complete:
                                if "(!)" in ev_karinspring4.hint:
                                    textbutton _("[ev_karinspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring4.hint]")

                            #A Trip to Uzbekistan (karinspring5)
                            if (not ev_karinspring5.completed and not ev_karinspring5.missed) or show_complete:
                                if "(!)" in ev_karinspring5.hint:
                                    textbutton _("[ev_karinspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring5.hint]")

                            #Top 10 Thoughts to Think (karinspring6)
                            if (not ev_karinspring6.completed and not ev_karinspring6.missed) or show_complete:
                                if "(!)" in ev_karinspring6.hint:
                                    textbutton _("[ev_karinspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring6.hint]")

                            #Oatmeal Raisin (karinspring7)
                            if (not ev_karinspring7.completed and not ev_karinspring7.missed) or show_complete:
                                if "(!)" in ev_karinspring7.hint:
                                    textbutton _("[ev_karinspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_karinspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_karinspring7.hint]")

                    #KIRINHINT

                    if showgirl == "Kirin":

                        if not _in_replay:

                            #Partners in Crime (kirindate1)
                            if (not ev_kirindate1.completed and not ev_kirindate1.missed) or show_complete:
                                if "(!)" in ev_kirindate1.hint:
                                    textbutton _("[ev_kirindate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindate1.hint]")

                            #Long and Hard (kirindate5)
                            if (not ev_kirindate5.completed and not ev_kirindate5.missed) or show_complete:
                                if "(!)" in ev_kirindate5.hint:
                                    textbutton _("[ev_kirindate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindate5.hint]")

                            #Politics! Pleasure! Ponies! (kirindate10)
                            if (not ev_kirindate10.completed and not ev_kirindate10.missed) or show_complete:
                                if "(!)" in ev_kirindate10.hint:
                                    textbutton _("[ev_kirindate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindate10.hint]")

                            text ("")

                            #Full Blossom (kirinlust5)
                            if (not ev_kirinlust5.completed and not ev_kirinlust5.missed) or show_complete:
                                if "(!)" in ev_kirinlust5.hint:
                                    textbutton _("[ev_kirinlust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinlust5.hint]")

                            #Too Much, All at Once (kirininvite1)
                            if (not ev_kirininvite1.completed and not ev_kirininvite1.missed) or show_complete:
                                if "(!)" in ev_kirininvite1.hint:
                                    textbutton _("[ev_kirininvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirininvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirininvite1.hint]")

                            #No Extortion Necessary (kirininvite2)
                            if (not ev_kirininvite2.completed and not ev_kirininvite2.missed) or show_complete:
                                if "(!)" in ev_kirininvite2.hint:
                                    textbutton _("[ev_kirininvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirininvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirininvite2.hint]")

                            #Morals vs. Orgasms (kirinfirsthall)
                            if (not ev_kirinfirsthall.completed and not ev_kirinfirsthall.missed) or show_complete:
                                if "(!)" in ev_kirinfirsthall.hint:
                                    textbutton _("[ev_kirinfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinfirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinfirsthall.hint]")

                            #Love, Dorms, and Other Things (kirindorm10)
                            if (not ev_kirindorm10.completed and not ev_kirindorm10.missed) or show_complete:
                                if "(!)" in ev_kirindorm10.hint:
                                    textbutton _("[ev_kirindorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindorm10.hint]")

                            #Flickering Spotlight (kirinsoccer15)
                            if (not ev_kirinsoccer15.completed and not ev_kirinsoccer15.missed) or show_complete:
                                if "(!)" in ev_kirinsoccer15.hint:
                                    textbutton _("[ev_kirinsoccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinsoccer15.hint]")

                            #Enigmatology (kirinsoccer20)
                            if (not ev_kirinsoccer20.completed and not ev_kirinsoccer20.missed) or show_complete:
                                if "(!)" in ev_kirinsoccer20.hint:
                                    textbutton _("[ev_kirinsoccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinsoccer20.hint]")

                            #Bye Bye, Boner (kirindorm15)
                            if (not ev_kirindorm15.completed and not ev_kirindorm15.missed) or show_complete:
                                if "(!)" in ev_kirindorm15.hint:
                                    textbutton _("[ev_kirindorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindorm15.hint]")

                            #Terms & Conditions (kirindorm20)
                            if (not ev_kirindorm20.completed and not ev_kirindorm20.missed) or show_complete:
                                if "(!)" in ev_kirindorm20.hint:
                                    textbutton _("[ev_kirindorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindorm20.hint]")

                            #All That is Contaminated (kirindate25)
                            if (not ev_kirindate25.completed and not ev_kirindate25.missed) or show_complete:
                                if "(!)" in ev_kirindate25.hint:
                                    textbutton _("[ev_kirindate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindate25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindate25.hint]")

                            #Taking the Reins (kirinlust20)
                            if (not ev_kirinlust20.completed and not ev_kirinlust20.missed) or show_complete:
                                if "(!)" in ev_kirinlust20.hint:
                                    textbutton _("[ev_kirinlust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinlust20.hint]")

                            #Dyed Orange, Drenched in Sun (kirinspecial25)
                            if (not ev_kirinspecial25.completed and not ev_kirinspecial25.missed) or show_complete:
                                if "(!)" in ev_kirinspecial25.hint:
                                    textbutton _("[ev_kirinspecial25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspecial25.hint]")

                            #Temporary Bliss (kirindorm25)
                            if (not ev_kirindorm25.completed and not ev_kirindorm25.missed) or show_complete:
                                if "(!)" in ev_kirindorm25.hint:
                                    textbutton _("[ev_kirindorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirindorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirindorm25.hint]")

                            #Four Hand Massage (kirinsoccer25)
                            if (not ev_kirinsoccer25.completed and not ev_kirinsoccer25.missed) or show_complete:
                                if "(!)" in ev_kirinsoccer25.hint:
                                    textbutton _("[ev_kirinsoccer25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinsoccer25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinsoccer25.hint]")

                            #Made Out of Nothing (kirinspecial30)
                            if (not ev_kirinspecial30.completed and not ev_kirinspecial30.missed) or show_complete:
                                if "(!)" in ev_kirinspecial30.hint:
                                    textbutton _("[ev_kirinspecial30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspecial30.hint]")

                            #The Other Half (kirinlust202)
                            if (not ev_kirinlust202.completed and not ev_kirinlust202.missed) or show_complete:
                                if "(!)" in ev_kirinlust202.hint:
                                    textbutton _("[ev_kirinlust202.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust202), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinlust202.hint]")

                            text ("")

                            #Falling Asleep Standing Up (kirinlust30)
                            if (not ev_kirinlust30.completed and not ev_kirinlust30.missed) or show_complete:
                                if "(!)" in ev_kirinlust30.hint:
                                    textbutton _("[ev_kirinlust30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinlust30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinlust30.hint]")

                            #At the Edge of the Riverbank (kirinspecial40)
                            if (not ev_kirinspecial40.completed and not ev_kirinspecial40.missed) or show_complete:
                                if "(!)" in ev_kirinspecial40.hint:
                                    textbutton _("[ev_kirinspecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspecial40.hint]")

                            #Never Enough (kirinspecial45p1)
                            if (not ev_kirinspecial45p1.completed and not ev_kirinspecial45p1.missed) or show_complete:
                                if "(!)" in ev_kirinspecial45p1.hint:
                                    textbutton _("[ev_kirinspecial45p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial45p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspecial45p1.hint]")

                            #Salmon Onigiri (kirinspecial45p2)
                            if (not ev_kirinspecial45p2.completed and not ev_kirinspecial45p2.missed) or show_complete:
                                if "(!)" in ev_kirinspecial45p2.hint:
                                    textbutton _("[ev_kirinspecial45p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspecial45p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspecial45p2.hint]")

                            text ("")

                            #Rubber Traits (sportswars9)
                            if (not ev_sportswars9.completed and not ev_sportswars9.missed) or show_complete:
                                if "(!)" in ev_sportswars9.hint:
                                    textbutton _("[ev_sportswars9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars9.hint]")

                            #Girls Vs. Robots (sportswars18)
                            if (not ev_sportswars18.completed and not ev_sportswars18.missed) or show_complete:
                                if "(!)" in ev_sportswars18.hint:
                                    textbutton _("[ev_sportswars18.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars18), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars18.hint]")

                            #Clockless Watch (kirinspring1)
                            if (not ev_kirinspring1.completed and not ev_kirinspring1.missed) or show_complete:
                                if "(!)" in ev_kirinspring1.hint:
                                    textbutton _("[ev_kirinspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspring1.hint]")

                            #Solar Eclipse (christmaskirin1)
                            if (not ev_christmaskirin1.completed and not ev_christmaskirin1.missed) or show_complete:
                                if "(!)" in ev_christmaskirin1.hint:
                                    textbutton _("[ev_christmaskirin1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmaskirin1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmaskirin1.hint]")

                            #Animal Control (christmaskirin2)
                            if (not ev_christmaskirin2.completed and not ev_christmaskirin2.missed) or show_complete:
                                if "(!)" in ev_christmaskirin2.hint:
                                    textbutton _("[ev_christmaskirin2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmaskirin2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmaskirin2.hint]")

                            #Perfect Days (kirinchristmalloween1)
                            if (not ev_kirinchristmalloween1.completed and not ev_kirinchristmalloween1.missed) or show_complete:
                                if "(!)" in ev_kirinchristmalloween1.hint:
                                    textbutton _("[ev_kirinchristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinchristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinchristmalloween1.hint]")

                            #Transpacific Sadness Symposium VII: ANTFARM ANTECHAMBER (kirinchristmalloween2)
                            if (not ev_kirinchristmalloween2.completed and not ev_kirinchristmalloween2.missed) or show_complete:
                                if "(!)" in ev_kirinchristmalloween2.hint:
                                    textbutton _("[ev_kirinchristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinchristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinchristmalloween2.hint]")

                            #Love, Love, Love (kirinspring2)
                            if (not ev_kirinspring2.completed and not ev_kirinspring2.missed) or show_complete:
                                if "(!)" in ev_kirinspring2.hint:
                                    textbutton _("[ev_kirinspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspring2.hint]")

                            #In the Morning, In the Cold (kirinspring3)
                            if (not ev_kirinspring3.completed and not ev_kirinspring3.missed) or show_complete:
                                if "(!)" in ev_kirinspring3.hint:
                                    textbutton _("[ev_kirinspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspring3.hint]")

                            #Failed Attempts at Arson (kirinspring4)
                            if (not ev_kirinspring4.completed and not ev_kirinspring4.missed) or show_complete:
                                if "(!)" in ev_kirinspring4.hint:
                                    textbutton _("[ev_kirinspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_kirinspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_kirinspring4.hint]")

                    #MAKIHINT

                    if showgirl == "Maki":

                        if not _in_replay:

                            #Beautiful Porn Salesman (makidate1)
                            if (not ev_makidate1.completed and not ev_makidate1.missed) or show_complete:
                                if "(!)" in ev_makidate1.hint:
                                    textbutton _("[ev_makidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makidate1.hint]")

                            #Maki Miyamura's Mom-Mode Mission (makidate5)
                            if (not ev_makidate5.completed and not ev_makidate5.missed) or show_complete:
                                if "(!)" in ev_makidate5.hint:
                                    textbutton _("[ev_makidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makidate5.hint]")

                            text ("")

                            #A Fair Trade (makidate10)
                            if (not ev_makidate10.completed and not ev_makidate10.missed) or show_complete:
                                if "(!)" in ev_makidate10.hint:
                                    textbutton _("[ev_makidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makidate10.hint]")

                            #Three Afloat On One Raft (makiday351)
                            if (not ev_makiday351.completed and not ev_makiday351.missed) or show_complete:
                                if "(!)" in ev_makiday351.hint:
                                    textbutton _("[ev_makiday351.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiday351), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makiday351.hint]")

                            #Thank You For Your Business (makidate15)
                            if (not ev_makidate15.completed and not ev_makidate15.missed) or show_complete:
                                if "(!)" in ev_makidate15.hint:
                                    textbutton _("[ev_makidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makidate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makidate15.hint]")

                            #Traveling Lube Dealer (makiinvite1)
                            if (not ev_makiinvite1.completed and not ev_makiinvite1.missed) or show_complete:
                                if "(!)" in ev_makiinvite1.hint:
                                    textbutton _("[ev_makiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makiinvite1.hint]")

                            #Special Occasions (makiinvite2)
                            if (not ev_makiinvite2.completed and not ev_makiinvite2.missed) or show_complete:
                                if "(!)" in ev_makiinvite2.hint:
                                    textbutton _("[ev_makiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makiinvite2.hint]")

                            text ("")

                            #Adulting (sadgirls3)
                            if (not ev_sadgirls3.completed and not ev_sadgirls3.missed) or show_complete:
                                if "(!)" in ev_sadgirls3.hint:
                                    textbutton _("[ev_sadgirls3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls3.hint]")

                            #Rolling Stop (Turned Backwards) (sadgirls6)
                            if (not ev_sadgirls6.completed and not ev_sadgirls6.missed) or show_complete:
                                if "(!)" in ev_sadgirls6.hint:
                                    textbutton _("[ev_sadgirls6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls6.hint]")

                            #Baby Steps (makiinv3)
                            if (not ev_makiinv3.completed and not ev_makiinv3.missed) or show_complete:
                                if "(!)" in ev_makiinv3.hint:
                                    textbutton _("[ev_makiinv3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makiinv3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makiinv3.hint]")

                            #The Maltese Falcon (makihornyquestintro)
                            if (not ev_makihornyquestintro.completed and not ev_makihornyquestintro.missed) or show_complete:
                                if "(!)" in ev_makihornyquestintro.hint:
                                    textbutton _("[ev_makihornyquestintro.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornyquestintro), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makihornyquestintro.hint]")

                            #Shut Up & Cum (makihornytrip2)
                            if (not ev_makihornytrip2.completed and not ev_makihornytrip2.missed) or show_complete:
                                if "(!)" in ev_makihornytrip2.hint:
                                    textbutton _("[ev_makihornytrip2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makihornytrip2.hint]")

                            #Rotting From the Inside Out (makihornytrip3)
                            if (not ev_makihornytrip3.completed and not ev_makihornytrip3.missed) or show_complete:
                                if "(!)" in ev_makihornytrip3.hint:
                                    textbutton _("[ev_makihornytrip3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makihornytrip3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makihornytrip3.hint]")

                            text ("")

                            #Wires...and the Concept of Breathing (makicamp1)
                            if (not ev_makicamp1.completed and not ev_makicamp1.missed) or show_complete:
                                if "(!)" in ev_makicamp1.hint:
                                    textbutton _("[ev_makicamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makicamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makicamp1.hint]")

                            #A Place Between the Trees (makicamp2)
                            if (not ev_makicamp2.completed and not ev_makicamp2.missed) or show_complete:
                                if "(!)" in ev_makicamp2.hint:
                                    textbutton _("[ev_makicamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makicamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makicamp2.hint]")

                            #To Boldly Go... (makilust5)
                            if (not ev_makilust5.completed and not ev_makilust5.missed) or show_complete:
                                if "(!)" in ev_makilust5.hint:
                                    textbutton _("[ev_makilust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makilust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makilust5.hint]")

                            #Sex Box Memories (makispring1)
                            if (not ev_makispring1.completed and not ev_makispring1.missed) or show_complete:
                                if "(!)" in ev_makispring1.hint:
                                    textbutton _("[ev_makispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makispring1.hint]")

                            #Hello Alone (makispring2)
                            if (not ev_makispring2.completed and not ev_makispring2.missed) or show_complete:
                                if "(!)" in ev_makispring2.hint:
                                    textbutton _("[ev_makispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makispring2.hint]")

                            #ASS (makispring3)
                            if (not ev_makispring3.completed and not ev_makispring3.missed) or show_complete:
                                if "(!)" in ev_makispring3.hint:
                                    textbutton _("[ev_makispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makispring3.hint]")

                            #Budd Dwyer (makispring4)
                            if (not ev_makispring4.completed and not ev_makispring4.missed) or show_complete:
                                if "(!)" in ev_makispring4.hint:
                                    textbutton _("[ev_makispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makispring4.hint]")

                            #A Million Tiny Pieces (makispring5)
                            if (not ev_makispring5.completed and not ev_makispring5.missed) or show_complete:
                                if "(!)" in ev_makispring5.hint:
                                    textbutton _("[ev_makispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makispring5.hint]")

                    #MAKOTOHINT

                    if showgirl == "Makoto":

                        if not _in_replay:

                            #Unexpected Profession (firsttimepornshop)
                            if (not ev_firsttimepornshop.completed and not ev_firsttimepornshop.missed) or show_complete:
                                if "(!)" in ev_firsttimepornshop.hint:
                                    textbutton _("[ev_firsttimepornshop.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimepornshop), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimepornshop.hint]")

                            #Teacher's Pet (makotofirsthall)
                            if (not ev_makotofirsthall.completed and not ev_makotofirsthall.missed) or show_complete:
                                if "(!)" in ev_makotofirsthall.hint:
                                    textbutton _("[ev_makotofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotofirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotofirsthall.hint]")

                            #Watching Porn Alone (pornshop5)
                            if (not ev_pornshop5.completed and not ev_pornshop5.missed) or show_complete:
                                if "(!)" in ev_pornshop5.hint:
                                    textbutton _("[ev_pornshop5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_pornshop5.hint]")

                            #Completely Platonic (makotodorm5)
                            if (not ev_makotodorm5.completed and not ev_makotodorm5.missed) or show_complete:
                                if "(!)" in ev_makotodorm5.hint:
                                    textbutton _("[ev_makotodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotodorm5.hint]")

                            #Rising of the Tide (pornshop10)
                            if (not ev_pornshop10.completed and not ev_pornshop10.missed) or show_complete:
                                if "(!)" in ev_pornshop10.hint:
                                    textbutton _("[ev_pornshop10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_pornshop10.hint]")

                            #Frogger (makotonew1)
                            if (not ev_makotonew1.completed and not ev_makotonew1.missed) or show_complete:
                                if "(!)" in ev_makotonew1.hint:
                                    textbutton _("[ev_makotonew1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotonew1.hint]")

                            #Sowing the Seeds (makotonew2)
                            if (not ev_makotonew2.completed and not ev_makotonew2.missed) or show_complete:
                                if "(!)" in ev_makotonew2.hint:
                                    textbutton _("[ev_makotonew2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotonew2.hint]")

                            #Egg Tooth (makotonew3)
                            if (not ev_makotonew3.completed and not ev_makotonew3.missed) or show_complete:
                                if "(!)" in ev_makotonew3.hint:
                                    textbutton _("[ev_makotonew3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotonew3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotonew3.hint]")

                            #Fishing For Love (pornshop15)
                            if (not ev_pornshop15.completed and not ev_pornshop15.missed) or show_complete:
                                if "(!)" in ev_pornshop15.hint:
                                    textbutton _("[ev_pornshop15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_pornshop15.hint]")

                            #Quid Pro Quo (makotolust5)
                            if (not ev_makotolust5.completed and not ev_makotolust5.missed) or show_complete:
                                if "(!)" in ev_makotolust5.hint:
                                    textbutton _("[ev_makotolust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotolust5.hint]")

                            #Declaration of War (makotoinvite1)
                            if (not ev_makotoinvite1.completed and not ev_makotoinvite1.missed) or show_complete:
                                if "(!)" in ev_makotoinvite1.hint:
                                    textbutton _("[ev_makotoinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotoinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotoinvite1.hint]")

                            #Studious Teen Virgin (makotoinvite2)
                            if (not ev_makotoinvite2.completed and not ev_makotoinvite2.missed) or show_complete:
                                if "(!)" in ev_makotoinvite2.hint:
                                    textbutton _("[ev_makotoinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotoinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotoinvite2.hint]")

                            #Aftermath (pornshop20)
                            if (not ev_pornshop20.completed and not ev_pornshop20.missed) or show_complete:
                                if "(!)" in ev_pornshop20.hint:
                                    textbutton _("[ev_pornshop20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_pornshop20.hint]")

                            #Residual Sadness (makotodorm20)
                            if (not ev_makotodorm20.completed and not ev_makotodorm20.missed) or show_complete:
                                if "(!)" in ev_makotodorm20.hint:
                                    textbutton _("[ev_makotodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotodorm20.hint]")

                            #Service Charge (pornshop25)
                            if (not ev_pornshop25.completed and not ev_pornshop25.missed) or show_complete:
                                if "(!)" in ev_pornshop25.hint:
                                    textbutton _("[ev_pornshop25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_pornshop25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_pornshop25.hint]")

                            #Bluejay (makotodorm25)
                            if (not ev_makotodorm25.completed and not ev_makotodorm25.missed) or show_complete:
                                if "(!)" in ev_makotodorm25.hint:
                                    textbutton _("[ev_makotodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotodorm25.hint]")

                            text ("")

                            #Semblance of a Soul (makotolust10)
                            if (not ev_makotolust10.completed and not ev_makotolust10.missed) or show_complete:
                                if "(!)" in ev_makotolust10.hint:
                                    textbutton _("[ev_makotolust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotolust10.hint]")

                            #Condoms in the Sand (makotowinterbeach1)
                            if (not ev_makotowinterbeach1.completed and not ev_makotowinterbeach1.missed) or show_complete:
                                if "(!)" in ev_makotowinterbeach1.hint:
                                    textbutton _("[ev_makotowinterbeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotowinterbeach1.hint]")

                            #Humans With Hollow Bones (makotowinterbeach2)
                            if (not ev_makotowinterbeach2.completed and not ev_makotowinterbeach2.missed) or show_complete:
                                if "(!)" in ev_makotowinterbeach2.hint:
                                    textbutton _("[ev_makotowinterbeach2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotowinterbeach2.hint]")

                            #I'm Not Here (makotowinterbeach3)
                            if (not ev_makotowinterbeach3.completed and not ev_makotowinterbeach3.missed) or show_complete:
                                if "(!)" in ev_makotowinterbeach3.hint:
                                    textbutton _("[ev_makotowinterbeach3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotowinterbeach3.hint]")

                            #Something, Somewhere (makotowinterbeach4)
                            if (not ev_makotowinterbeach4.completed and not ev_makotowinterbeach4.missed) or show_complete:
                                if "(!)" in ev_makotowinterbeach4.hint:
                                    textbutton _("[ev_makotowinterbeach4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotowinterbeach4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotowinterbeach4.hint]")

                            #Hot Water (makotolust20)
                            if (not ev_makotolust20.completed and not ev_makotolust20.missed) or show_complete:
                                if "(!)" in ev_makotolust20.hint:
                                    textbutton _("[ev_makotolust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotolust20.hint]")

                            text ("")

                            #Whispers of the World (sadgirls1)
                            if (not ev_sadgirls1.completed and not ev_sadgirls1.missed) or show_complete:
                                if "(!)" in ev_sadgirls1.hint:
                                    textbutton _("[ev_sadgirls1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls1.hint]")

                            #Parallelogram (sadgirls7)
                            if (not ev_sadgirls7.completed and not ev_sadgirls7.missed) or show_complete:
                                if "(!)" in ev_sadgirls7.hint:
                                    textbutton _("[ev_sadgirls7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls7.hint]")

                            #White Oak Doors (makotolust30)
                            if (not ev_makotolust30.completed and not ev_makotolust30.missed) or show_complete:
                                if "(!)" in ev_makotolust30.hint:
                                    textbutton _("[ev_makotolust30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotolust30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotolust30.hint]")

                            #A Beautiful Mind (sadgirls8)
                            if (not ev_sadgirls8.completed and not ev_sadgirls8.missed) or show_complete:
                                if "(!)" in ev_sadgirls8.hint:
                                    textbutton _("[ev_sadgirls8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sadgirls8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sadgirls8.hint]")

                            #Young Cardinals (makotospecial50)
                            if (not ev_makotospecial50.completed and not ev_makotospecial50.missed) or show_complete:
                                if "(!)" in ev_makotospecial50.hint:
                                    textbutton _("[ev_makotospecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospecial50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospecial50.hint]")

                            #Cool Sex Tips (makotopool55)
                            if (not ev_makotopool55.completed and not ev_makotopool55.missed) or show_complete:
                                if "(!)" in ev_makotopool55.hint:
                                    textbutton _("[ev_makotopool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotopool55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotopool55.hint]")

                            #Bra Shopping (makotodorm55p1)
                            if (not ev_makotodorm55p1.completed and not ev_makotodorm55p1.missed) or show_complete:
                                if "(!)" in ev_makotodorm55p1.hint:
                                    textbutton _("[ev_makotodorm55p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm55p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotodorm55p1.hint]")

                            #Suffer the Same (makotodorm55p2)
                            if (not ev_makotodorm55p2.completed and not ev_makotodorm55p2.missed) or show_complete:
                                if "(!)" in ev_makotodorm55p2.hint:
                                    textbutton _("[ev_makotodorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotodorm55p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotodorm55p2.hint]")

                            text ("")

                            #The Pit of Despair (sportswars19)
                            if (not ev_sportswars19.completed and not ev_sportswars19.missed) or show_complete:
                                if "(!)" in ev_sportswars19.hint:
                                    textbutton _("[ev_sportswars19.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars19), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars19.hint]")

                            #Midnight Snack (makotospring1)
                            if (not ev_makotospring1.completed and not ev_makotospring1.missed) or show_complete:
                                if "(!)" in ev_makotospring1.hint:
                                    textbutton _("[ev_makotospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospring1.hint]")

                            #T Is For Time (Trees & Threes) (makotospring2)
                            if (not ev_makotospring2.completed and not ev_makotospring2.missed) or show_complete:
                                if "(!)" in ev_makotospring2.hint:
                                    textbutton _("[ev_makotospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospring2.hint]")

                            #Six Ways From Sunday (halloweenmakoto1)
                            if (not ev_halloweenmakoto1.completed and not ev_halloweenmakoto1.missed) or show_complete:
                                if "(!)" in ev_halloweenmakoto1.hint:
                                    textbutton _("[ev_halloweenmakoto1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmakoto1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmakoto1.hint]")

                            #Precious Little Life (halloweenmakoto2)
                            if (not ev_halloweenmakoto2.completed and not ev_halloweenmakoto2.missed) or show_complete:
                                if "(!)" in ev_halloweenmakoto2.hint:
                                    textbutton _("[ev_halloweenmakoto2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmakoto2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmakoto2.hint]")

                            #Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR (halloweenmakoto3)
                            if (not ev_halloweenmakoto3.completed and not ev_halloweenmakoto3.missed) or show_complete:
                                if "(!)" in ev_halloweenmakoto3.hint:
                                    textbutton _("[ev_halloweenmakoto3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmakoto3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmakoto3.hint]")

                            #The World, Alive (Ant Farm) (makotospring3)
                            if (not ev_makotospring3.completed and not ev_makotospring3.missed) or show_complete:
                                if "(!)" in ev_makotospring3.hint:
                                    textbutton _("[ev_makotospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospring3.hint]")

                            #Black Mass (beachsixmakoto1)
                            if (not ev_beachsixmakoto1.completed and not ev_beachsixmakoto1.missed) or show_complete:
                                if "(!)" in ev_beachsixmakoto1.hint:
                                    textbutton _("[ev_beachsixmakoto1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixmakoto1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixmakoto1.hint]")

                            #A Matter of Time (beachsixmakoto2)
                            if (not ev_beachsixmakoto2.completed and not ev_beachsixmakoto2.missed) or show_complete:
                                if "(!)" in ev_beachsixmakoto2.hint:
                                    textbutton _("[ev_beachsixmakoto2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixmakoto2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixmakoto2.hint]")

                            #This Penis, Eternal (makotospring4)
                            if (not ev_makotospring4.completed and not ev_makotospring4.missed) or show_complete:
                                if "(!)" in ev_makotospring4.hint:
                                    textbutton _("[ev_makotospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospring4.hint]")

                            #Code Red (makotospring5)
                            if (not ev_makotospring5.completed and not ev_makotospring5.missed) or show_complete:
                                if "(!)" in ev_makotospring5.hint:
                                    textbutton _("[ev_makotospring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_makotospring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_makotospring5.hint]")

                    #MAYAHINT

                    if showgirl == "Maya":

                        if not _in_replay:

                            #A New Beginning (firsttimeshrine)
                            if (not ev_firsttimeshrine.completed and not ev_firsttimeshrine.missed) or show_complete:
                                if "(!)" in ev_firsttimeshrine.hint:
                                    textbutton _("[ev_firsttimeshrine.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimeshrine), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimeshrine.hint]")

                            #Mondays (mayafirsthall)
                            if (not ev_mayafirsthall.completed and not ev_mayafirsthall.missed) or show_complete:
                                if "(!)" in ev_mayafirsthall.hint:
                                    textbutton _("[ev_mayafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayafirsthall.hint]")

                            #Different Worlds (shrine5)
                            if (not ev_shrine5.completed and not ev_shrine5.missed) or show_complete:
                                if "(!)" in ev_shrine5.hint:
                                    textbutton _("[ev_shrine5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine5.hint]")

                            #Secrets Worth Keeping (mayadorm5)
                            if (not ev_mayadorm5.completed and not ev_mayadorm5.missed) or show_complete:
                                if "(!)" in ev_mayadorm5.hint:
                                    textbutton _("[ev_mayadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm5.hint]")

                            #Past/Present/Future (shrine10)
                            if (not ev_shrine10.completed and not ev_shrine10.missed) or show_complete:
                                if "(!)" in ev_shrine10.hint:
                                    textbutton _("[ev_shrine10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine10.hint]")

                            #Rewind/Repeat/Refuse (mayadorm10)
                            if (not ev_mayadorm10.completed and not ev_mayadorm10.missed) or show_complete:
                                if "(!)" in ev_mayadorm10.hint:
                                    textbutton _("[ev_mayadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm10.hint]")

                            #You and Me (shrine15)
                            if (not ev_shrine15.completed and not ev_shrine15.missed) or show_complete:
                                if "(!)" in ev_shrine15.hint:
                                    textbutton _("[ev_shrine15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine15.hint]")

                            #Takoyaki (mayadorm15)
                            if (not ev_mayadorm15.completed and not ev_mayadorm15.missed) or show_complete:
                                if "(!)" in ev_mayadorm15.hint:
                                    textbutton _("[ev_mayadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm15.hint]")

                            #Nothing is Real (shrine20)
                            if (not ev_shrine20.completed and not ev_shrine20.missed) or show_complete:
                                if "(!)" in ev_shrine20.hint:
                                    textbutton _("[ev_shrine20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine20.hint]")

                            #Close Your Eyes (mayadorm20)
                            if (not ev_mayadorm20.completed and not ev_mayadorm20.missed) or show_complete:
                                if "(!)" in ev_mayadorm20.hint:
                                    textbutton _("[ev_mayadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm20.hint]")

                            #Watermelons and Violin (shrine25)
                            if (not ev_shrine25.completed and not ev_shrine25.missed) or show_complete:
                                if "(!)" in ev_shrine25.hint:
                                    textbutton _("[ev_shrine25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine25.hint]")

                            #FLAVOR BEAM! (mayadorm25)
                            if (not ev_mayadorm25.completed and not ev_mayadorm25.missed) or show_complete:
                                if "(!)" in ev_mayadorm25.hint:
                                    textbutton _("[ev_mayadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm25.hint]")

                            text ("")

                            #What it Means to Be Destroyed (mayadorm30)
                            if (not ev_mayadorm30.completed and not ev_mayadorm30.missed) or show_complete:
                                if "(!)" in ev_mayadorm30.hint:
                                    textbutton _("[ev_mayadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm30.hint]")

                            #Now More Than Ever (shrine30)
                            if (not ev_shrine30.completed and not ev_shrine30.missed) or show_complete:
                                if "(!)" in ev_shrine30.hint:
                                    textbutton _("[ev_shrine30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine30.hint]")

                            #A Place That Can Only Exist in Our Minds (mayadorm35)
                            if (not ev_mayadorm35.completed and not ev_mayadorm35.missed) or show_complete:
                                if "(!)" in ev_mayadorm35.hint:
                                    textbutton _("[ev_mayadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadorm35.hint]")

                            #Stop Looking For Answers (shrine35)
                            if (not ev_shrine35.completed and not ev_shrine35.missed) or show_complete:
                                if "(!)" in ev_shrine35.hint:
                                    textbutton _("[ev_shrine35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine35.hint]")

                            #Somewhere Inside of a Dream (mayafestival1)
                            if (not ev_mayafestival1.completed and not ev_mayafestival1.missed) or show_complete:
                                if "(!)" in ev_mayafestival1.hint:
                                    textbutton _("[ev_mayafestival1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayafestival1.hint]")

                            #Three Halves Make a Whole (Itadakimasu) (mayafestival2)
                            if (not ev_mayafestival2.completed and not ev_mayafestival2.missed) or show_complete:
                                if "(!)" in ev_mayafestival2.hint:
                                    textbutton _("[ev_mayafestival2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayafestival2.hint]")

                            #As The Sun Disappears (mayafestival3)
                            if (not ev_mayafestival3.completed and not ev_mayafestival3.missed) or show_complete:
                                if "(!)" in ev_mayafestival3.hint:
                                    textbutton _("[ev_mayafestival3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayafestival3.hint]")

                            #Everlasting Mercy (mayafestival4)
                            if (not ev_mayafestival4.completed and not ev_mayafestival4.missed) or show_complete:
                                if "(!)" in ev_mayafestival4.hint:
                                    textbutton _("[ev_mayafestival4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayafestival4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayafestival4.hint]")

                            text ("")

                            #The Sun, And All Its Toxic Rays (shrine40)
                            if (not ev_shrine40.completed and not ev_shrine40.missed) or show_complete:
                                if "(!)" in ev_shrine40.hint:
                                    textbutton _("[ev_shrine40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_shrine40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_shrine40.hint]")

                            #Anything & Everything (mayadate45)
                            if (not ev_mayadate45.completed and not ev_mayadate45.missed) or show_complete:
                                if "(!)" in ev_mayadate45.hint:
                                    textbutton _("[ev_mayadate45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayadate45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayadate45.hint]")

                            #A Brutal, Violent Creaming (mayaspecial45)
                            if (not ev_mayaspecial45.completed and not ev_mayaspecial45.missed) or show_complete:
                                if "(!)" in ev_mayaspecial45.hint:
                                    textbutton _("[ev_mayaspecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspecial45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspecial45.hint]")

                            text ("")

                            #The Motherland Calls! (sportswars5)
                            if (not ev_sportswars5.completed and not ev_sportswars5.missed) or show_complete:
                                if "(!)" in ev_sportswars5.hint:
                                    textbutton _("[ev_sportswars5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars5.hint]")

                            #Miraculous Human-Glue (sportswars10)
                            if (not ev_sportswars10.completed and not ev_sportswars10.missed) or show_complete:
                                if "(!)" in ev_sportswars10.hint:
                                    textbutton _("[ev_sportswars10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars10.hint]")

                            #Radio Silence (sportswars14)
                            if (not ev_sportswars14.completed and not ev_sportswars14.missed) or show_complete:
                                if "(!)" in ev_sportswars14.hint:
                                    textbutton _("[ev_sportswars14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars14), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars14.hint]")

                            #The Girl Who Leapt Through Time (halloweenmaya1)
                            if (not ev_halloweenmaya1.completed and not ev_halloweenmaya1.missed) or show_complete:
                                if "(!)" in ev_halloweenmaya1.hint:
                                    textbutton _("[ev_halloweenmaya1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmaya1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmaya1.hint]")

                            #Wake Up (My Story) (halloweenmaya2)
                            if (not ev_halloweenmaya2.completed and not ev_halloweenmaya2.missed) or show_complete:
                                if "(!)" in ev_halloweenmaya2.hint:
                                    textbutton _("[ev_halloweenmaya2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmaya2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmaya2.hint]")

                            #Right as Rain (halloweenmaya3)
                            if (not ev_halloweenmaya3.completed and not ev_halloweenmaya3.missed) or show_complete:
                                if "(!)" in ev_halloweenmaya3.hint:
                                    textbutton _("[ev_halloweenmaya3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenmaya3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenmaya3.hint]")

                            #Billy Pilgrim (mayaspring1)
                            if (not ev_mayaspring1.completed and not ev_mayaspring1.missed) or show_complete:
                                if "(!)" in ev_mayaspring1.hint:
                                    textbutton _("[ev_mayaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspring1.hint]")

                            #A Second Haunting (mayaspring2)
                            if (not ev_mayaspring2.completed and not ev_mayaspring2.missed) or show_complete:
                                if "(!)" in ev_mayaspring2.hint:
                                    textbutton _("[ev_mayaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspring2.hint]")

                            #My Perfect World (mayaspring3)
                            if (not ev_mayaspring3.completed and not ev_mayaspring3.missed) or show_complete:
                                if "(!)" in ev_mayaspring3.hint:
                                    textbutton _("[ev_mayaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspring3.hint]")

                            #Tying the Knot (mayachristmalloween1)
                            if (not ev_mayachristmalloween1.completed and not ev_mayachristmalloween1.missed) or show_complete:
                                if "(!)" in ev_mayachristmalloween1.hint:
                                    textbutton _("[ev_mayachristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayachristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayachristmalloween1.hint]")

                            #This Room and Everything in It (mayachristmalloween2)
                            if (not ev_mayachristmalloween2.completed and not ev_mayachristmalloween2.missed) or show_complete:
                                if "(!)" in ev_mayachristmalloween2.hint:
                                    textbutton _("[ev_mayachristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayachristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayachristmalloween2.hint]")

                            #Something to Do With Love (mayachristmalloween3)
                            if (not ev_mayachristmalloween3.completed and not ev_mayachristmalloween3.missed) or show_complete:
                                if "(!)" in ev_mayachristmalloween3.hint:
                                    textbutton _("[ev_mayachristmalloween3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayachristmalloween3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayachristmalloween3.hint]")

                            #Ground Zero (dormwarssixmaya1)
                            if (not ev_dormwarssixmaya1.completed and not ev_dormwarssixmaya1.missed) or show_complete:
                                if "(!)" in ev_dormwarssixmaya1.hint:
                                    textbutton _("[ev_dormwarssixmaya1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarssixmaya1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarssixmaya1.hint]")

                            #Ode on the Death of a Favorite Cat Drowned in a Tub of Goldfishes (mayaspring4)
                            if (not ev_mayaspring4.completed and not ev_mayaspring4.missed) or show_complete:
                                if "(!)" in ev_mayaspring4.hint:
                                    textbutton _("[ev_mayaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspring4.hint]")

                            #The War Invalid (mayaspring5)
                            if (not ev_mayaspring5.completed and not ev_mayaspring5.missed) or show_complete:
                                if "(!)" in ev_mayaspring5.hint:
                                    textbutton _("[ev_mayaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mayaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mayaspring5.hint]")

                    #MIKUHINT

                    if showgirl == "Miku":

                        if not _in_replay:

                            #Daytime Stalking Pass (firsttimesoccerfield)
                            if (not ev_firsttimesoccerfield.completed and not ev_firsttimesoccerfield.missed) or show_complete:
                                if "(!)" in ev_firsttimesoccerfield.hint:
                                    textbutton _("[ev_firsttimesoccerfield.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimesoccerfield), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimesoccerfield.hint]")

                            #Behind Closed Doors (mikufirsthall)
                            if (not ev_mikufirsthall.completed and not ev_mikufirsthall.missed) or show_complete:
                                if "(!)" in ev_mikufirsthall.hint:
                                    textbutton _("[ev_mikufirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikufirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikufirsthall.hint]")

                            #It's Always Sunny in Kumon-mi (soccer5)
                            if (not ev_soccer5.completed and not ev_soccer5.missed) or show_complete:
                                if "(!)" in ev_soccer5.hint:
                                    textbutton _("[ev_soccer5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer5.hint]")

                            #Broken Bones (mikudorm5)
                            if (not ev_mikudorm5.completed and not ev_mikudorm5.missed) or show_complete:
                                if "(!)" in ev_mikudorm5.hint:
                                    textbutton _("[ev_mikudorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm5.hint]")

                            #Nightvision (soccer10)
                            if (not ev_soccer10.completed and not ev_soccer10.missed) or show_complete:
                                if "(!)" in ev_soccer10.hint:
                                    textbutton _("[ev_soccer10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer10.hint]")

                            #You and Me and the Night (mikudorm10)
                            if (not ev_mikudorm10.completed and not ev_mikudorm10.missed) or show_complete:
                                if "(!)" in ev_mikudorm10.hint:
                                    textbutton _("[ev_mikudorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm10.hint]")

                            #Hormones Running Wild (soccer15)
                            if (not ev_soccer15.completed and not ev_soccer15.missed) or show_complete:
                                if "(!)" in ev_soccer15.hint:
                                    textbutton _("[ev_soccer15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer15.hint]")

                            #Moments Like This (mikudorm15)
                            if (not ev_mikudorm15.completed and not ev_mikudorm15.missed) or show_complete:
                                if "(!)" in ev_mikudorm15.hint:
                                    textbutton _("[ev_mikudorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm15.hint]")

                            #Coach (soccer20)
                            if (not ev_soccer20.completed and not ev_soccer20.missed) or show_complete:
                                if "(!)" in ev_soccer20.hint:
                                    textbutton _("[ev_soccer20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer20.hint]")

                            #Thighs On-Demand (soccer25)
                            if (not ev_soccer25.completed and not ev_soccer25.missed) or show_complete:
                                if "(!)" in ev_soccer25.hint:
                                    textbutton _("[ev_soccer25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer25.hint]")

                            #Scaredy Cat (mikudorm25)
                            if (not ev_mikudorm25.completed and not ev_mikudorm25.missed) or show_complete:
                                if "(!)" in ev_mikudorm25.hint:
                                    textbutton _("[ev_mikudorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm25.hint]")

                            #An Extra Set of Arms (soccer30)
                            if (not ev_soccer30.completed and not ev_soccer30.missed) or show_complete:
                                if "(!)" in ev_soccer30.hint:
                                    textbutton _("[ev_soccer30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer30.hint]")

                            #One. Two. Three. (mikudorm30)
                            if (not ev_mikudorm30.completed and not ev_mikudorm30.missed) or show_complete:
                                if "(!)" in ev_mikudorm30.hint:
                                    textbutton _("[ev_mikudorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm30.hint]")

                            text ("")

                            #Loxonin (soccer35)
                            if (not ev_soccer35.completed and not ev_soccer35.missed) or show_complete:
                                if "(!)" in ev_soccer35.hint:
                                    textbutton _("[ev_soccer35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_soccer35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_soccer35.hint]")

                            #To Sleep, Perchance to Dream (mikuwinterbeach1)
                            if (not ev_mikuwinterbeach1.completed and not ev_mikuwinterbeach1.missed) or show_complete:
                                if "(!)" in ev_mikuwinterbeach1.hint:
                                    textbutton _("[ev_mikuwinterbeach1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuwinterbeach1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuwinterbeach1.hint]")

                            #Triple Whammy (mikudorm35)
                            if (not ev_mikudorm35.completed and not ev_mikudorm35.missed) or show_complete:
                                if "(!)" in ev_mikudorm35.hint:
                                    textbutton _("[ev_mikudorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm35.hint]")

                            #Speed of Light (mikudorm40)
                            if (not ev_mikudorm40.completed and not ev_mikudorm40.missed) or show_complete:
                                if "(!)" in ev_mikudorm40.hint:
                                    textbutton _("[ev_mikudorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm40.hint]")

                            #Acute Love Triangle (mikudorm45)
                            if (not ev_mikudorm45.completed and not ev_mikudorm45.missed) or show_complete:
                                if "(!)" in ev_mikudorm45.hint:
                                    textbutton _("[ev_mikudorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm45.hint]")

                            #Chrysalis (mikudorm45p2)
                            if (not ev_mikudorm45p2.completed and not ev_mikudorm45p2.missed) or show_complete:
                                if "(!)" in ev_mikudorm45p2.hint:
                                    textbutton _("[ev_mikudorm45p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm45p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm45p2.hint]")

                            #Someone Else's Skin (mikuspecial50)
                            if (not ev_mikuspecial50.completed and not ev_mikuspecial50.missed) or show_complete:
                                if "(!)" in ev_mikuspecial50.hint:
                                    textbutton _("[ev_mikuspecial50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspecial50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspecial50.hint]")

                            #The Devil & God Are Raging Inside Me (mikudorm50)
                            if (not ev_mikudorm50.completed and not ev_mikudorm50.missed) or show_complete:
                                if "(!)" in ev_mikudorm50.hint:
                                    textbutton _("[ev_mikudorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm50.hint]")

                            text ("")

                            #Breakaway (mikuinvite1)
                            if (not ev_mikuinvite1.completed and not ev_mikuinvite1.missed) or show_complete:
                                if "(!)" in ev_mikuinvite1.hint:
                                    textbutton _("[ev_mikuinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuinvite1.hint]")

                            #Fair is Fair (mikuinvite2)
                            if (not ev_mikuinvite2.completed and not ev_mikuinvite2.missed) or show_complete:
                                if "(!)" in ev_mikuinvite2.hint:
                                    textbutton _("[ev_mikuinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuinvite2.hint]")

                            #Voice of Vibration (mikupool55)
                            if (not ev_mikupool55.completed and not ev_mikupool55.missed) or show_complete:
                                if "(!)" in ev_mikupool55.hint:
                                    textbutton _("[ev_mikupool55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikupool55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikupool55.hint]")

                            #Essence of Eiderdown (mikudorm55p1)
                            if (not ev_mikudorm55p1.completed and not ev_mikudorm55p1.missed) or show_complete:
                                if "(!)" in ev_mikudorm55p1.hint:
                                    textbutton _("[ev_mikudorm55p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm55p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm55p1.hint]")

                            #Rostrum of Recollection (mikudorm55p2)
                            if (not ev_mikudorm55p2.completed and not ev_mikudorm55p2.missed) or show_complete:
                                if "(!)" in ev_mikudorm55p2.hint:
                                    textbutton _("[ev_mikudorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikudorm55p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikudorm55p2.hint]")

                            text ("")

                            #Captain Sorrow (mikuspring1)
                            if (not ev_mikuspring1.completed and not ev_mikuspring1.missed) or show_complete:
                                if "(!)" in ev_mikuspring1.hint:
                                    textbutton _("[ev_mikuspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring1.hint]")

                            #Bonerville (mikuspring2)
                            if (not ev_mikuspring2.completed and not ev_mikuspring2.missed) or show_complete:
                                if "(!)" in ev_mikuspring2.hint:
                                    textbutton _("[ev_mikuspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring2.hint]")

                            #The Boys (mikuspring3)
                            if (not ev_mikuspring3.completed and not ev_mikuspring3.missed) or show_complete:
                                if "(!)" in ev_mikuspring3.hint:
                                    textbutton _("[ev_mikuspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring3.hint]")

                            #Live Fast, Die Young (mikuspring4)
                            if (not ev_mikuspring4.completed and not ev_mikuspring4.missed) or show_complete:
                                if "(!)" in ev_mikuspring4.hint:
                                    textbutton _("[ev_mikuspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring4.hint]")

                            #The Gazelle (mikuspring5)
                            if (not ev_mikuspring5.completed and not ev_mikuspring5.missed) or show_complete:
                                if "(!)" in ev_mikuspring5.hint:
                                    textbutton _("[ev_mikuspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring5.hint]")

                            #Practice Makes Perfect (mikulust5)
                            if (not ev_mikulust5.completed and not ev_mikulust5.missed) or show_complete:
                                if "(!)" in ev_mikulust5.hint:
                                    textbutton _("[ev_mikulust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikulust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikulust5.hint]")

                            #Bean Sprouts (mikuspring6)
                            if (not ev_mikuspring6.completed and not ev_mikuspring6.missed) or show_complete:
                                if "(!)" in ev_mikuspring6.hint:
                                    textbutton _("[ev_mikuspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring6.hint]")

                            #The Whale (mikuspring7)
                            if (not ev_mikuspring7.completed and not ev_mikuspring7.missed) or show_complete:
                                if "(!)" in ev_mikuspring7.hint:
                                    textbutton _("[ev_mikuspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mikuspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mikuspring7.hint]")

                    #MOLLYHINT

                    if showgirl == "Molly":

                        if not _in_replay:

                            #NTR & Pregnancy (mollycafe1)
                            if (not ev_mollycafe1.completed and not ev_mollycafe1.missed) or show_complete:
                                if "(!)" in ev_mollycafe1.hint:
                                    textbutton _("[ev_mollycafe1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe1.hint]")

                            #The Cult of Molly (mollyfirsthall)
                            if (not ev_mollyfirsthall.completed and not ev_mollyfirsthall.missed) or show_complete:
                                if "(!)" in ev_mollyfirsthall.hint:
                                    textbutton _("[ev_mollyfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyfirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyfirsthall.hint]")

                            #Remnants of Forgotten Memes (mollycafe5)
                            if (not ev_mollycafe5.completed and not ev_mollycafe5.missed) or show_complete:
                                if "(!)" in ev_mollycafe5.hint:
                                    textbutton _("[ev_mollycafe5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe5.hint]")

                            #Torrent of Power (mollydorm5)
                            if (not ev_mollydorm5.completed and not ev_mollydorm5.missed) or show_complete:
                                if "(!)" in ev_mollydorm5.hint:
                                    textbutton _("[ev_mollydorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm5.hint]")

                            #Something Out of a Nukige (mollycafe10)
                            if (not ev_mollycafe10.completed and not ev_mollycafe10.missed) or show_complete:
                                if "(!)" in ev_mollycafe10.hint:
                                    textbutton _("[ev_mollycafe10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe10.hint]")

                            #The Dark Entity (mollydorm10)
                            if (not ev_mollydorm10.completed and not ev_mollydorm10.missed) or show_complete:
                                if "(!)" in ev_mollydorm10.hint:
                                    textbutton _("[ev_mollydorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm10.hint]")

                            text ("")

                            #Onward to Valhalla (mollycafe15)
                            if (not ev_mollycafe15.completed and not ev_mollycafe15.missed) or show_complete:
                                if "(!)" in ev_mollycafe15.hint:
                                    textbutton _("[ev_mollycafe15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe15.hint]")

                            #Unpaid Promotion (mollydorm15)
                            if (not ev_mollydorm15.completed and not ev_mollydorm15.missed) or show_complete:
                                if "(!)" in ev_mollydorm15.hint:
                                    textbutton _("[ev_mollydorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm15.hint]")

                            #The Legacy of Thaum Pt. II (mollycafe20)
                            if (not ev_mollycafe20.completed and not ev_mollycafe20.missed) or show_complete:
                                if "(!)" in ev_mollycafe20.hint:
                                    textbutton _("[ev_mollycafe20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe20.hint]")

                            #Ahead of the Curve (mollydorm20)
                            if (not ev_mollydorm20.completed and not ev_mollydorm20.missed) or show_complete:
                                if "(!)" in ev_mollydorm20.hint:
                                    textbutton _("[ev_mollydorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm20.hint]")

                            #Resurrection Sickness (mollycafe25)
                            if (not ev_mollycafe25.completed and not ev_mollycafe25.missed) or show_complete:
                                if "(!)" in ev_mollycafe25.hint:
                                    textbutton _("[ev_mollycafe25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe25.hint]")

                            #Tír na nÓg (mollycafe25p2)
                            if (not ev_mollycafe25p2.completed and not ev_mollycafe25p2.missed) or show_complete:
                                if "(!)" in ev_mollycafe25p2.hint:
                                    textbutton _("[ev_mollycafe25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe25p2.hint]")

                            #Transmogrification (mollydorm25)
                            if (not ev_mollydorm25.completed and not ev_mollydorm25.missed) or show_complete:
                                if "(!)" in ev_mollydorm25.hint:
                                    textbutton _("[ev_mollydorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm25.hint]")

                            #Walkthrough (mollydorm30)
                            if (not ev_mollydorm30.completed and not ev_mollydorm30.missed) or show_complete:
                                if "(!)" in ev_mollydorm30.hint:
                                    textbutton _("[ev_mollydorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydorm30.hint]")

                            text ("")

                            #Hook (mollycafe30p1)
                            if (not ev_mollycafe30p1.completed and not ev_mollycafe30p1.missed) or show_complete:
                                if "(!)" in ev_mollycafe30p1.hint:
                                    textbutton _("[ev_mollycafe30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe30p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe30p1.hint]")

                            #A Night to Remember (mollycafe30p2)
                            if (not ev_mollycafe30p2.completed and not ev_mollycafe30p2.missed) or show_complete:
                                if "(!)" in ev_mollycafe30p2.hint:
                                    textbutton _("[ev_mollycafe30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycafe30p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycafe30p2.hint]")

                            #Anar'alah Belore (mollydate35p1)
                            if (not ev_mollydate35p1.completed and not ev_mollydate35p1.missed) or show_complete:
                                if "(!)" in ev_mollydate35p1.hint:
                                    textbutton _("[ev_mollydate35p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydate35p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydate35p1.hint]")

                            #Sardines (mollydate35p2)
                            if (not ev_mollydate35p2.completed and not ev_mollydate35p2.missed) or show_complete:
                                if "(!)" in ev_mollydate35p2.hint:
                                    textbutton _("[ev_mollydate35p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollydate35p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollydate35p2.hint]")

                            text ("")

                            #Corrupted Blood (mollycamp1)
                            if (not ev_mollycamp1.completed and not ev_mollycamp1.missed) or show_complete:
                                if "(!)" in ev_mollycamp1.hint:
                                    textbutton _("[ev_mollycamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollycamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollycamp1.hint]")

                            #Level One (mollyspring1)
                            if (not ev_mollyspring1.completed and not ev_mollyspring1.missed) or show_complete:
                                if "(!)" in ev_mollyspring1.hint:
                                    textbutton _("[ev_mollyspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyspring1.hint]")

                            #Fated to Love You (mollyspring2)
                            if (not ev_mollyspring2.completed and not ev_mollyspring2.missed) or show_complete:
                                if "(!)" in ev_mollyspring2.hint:
                                    textbutton _("[ev_mollyspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyspring2.hint]")

                            #The Farmer’s Daughter (mollylust10)
                            if (not ev_mollylust10.completed and not ev_mollylust10.missed) or show_complete:
                                if "(!)" in ev_mollylust10.hint:
                                    textbutton _("[ev_mollylust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollylust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollylust10.hint]")

                            #No Murder in the House (mollyinvite1)
                            if (not ev_mollyinvite1.completed and not ev_mollyinvite1.missed) or show_complete:
                                if "(!)" in ev_mollyinvite1.hint:
                                    textbutton _("[ev_mollyinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyinvite1.hint]")

                            #Pixels & Polygons (mollyinvite2)
                            if (not ev_mollyinvite2.completed and not ev_mollyinvite2.missed) or show_complete:
                                if "(!)" in ev_mollyinvite2.hint:
                                    textbutton _("[ev_mollyinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyinvite2.hint]")

                            #Power-Leveling (beachsixmolly1)
                            if (not ev_beachsixmolly1.completed and not ev_beachsixmolly1.missed) or show_complete:
                                if "(!)" in ev_beachsixmolly1.hint:
                                    textbutton _("[ev_beachsixmolly1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixmolly1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixmolly1.hint]")

                            #Nihongo Jouzu (mollyspring3)
                            if (not ev_mollyspring3.completed and not ev_mollyspring3.missed) or show_complete:
                                if "(!)" in ev_mollyspring3.hint:
                                    textbutton _("[ev_mollyspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyspring3.hint]")

                            #Missable Event (mollyspring4)
                            if (not ev_mollyspring4.completed and not ev_mollyspring4.missed) or show_complete:
                                if "(!)" in ev_mollyspring4.hint:
                                    textbutton _("[ev_mollyspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_mollyspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_mollyspring4.hint]")

                    #NAOHINT

                    if showgirl == "Nao":

                        if not _in_replay:

                            #Silver Tongue (naospecial1)
                            if (not ev_naospecial1.completed and not ev_naospecial1.missed) or show_complete:
                                if "(!)" in ev_naospecial1.hint:
                                    textbutton _("[ev_naospecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospecial1.hint]")

                            #Becoming a Kidnapper (naospecial2)
                            if (not ev_naospecial2.completed and not ev_naospecial2.missed) or show_complete:
                                if "(!)" in ev_naospecial2.hint:
                                    textbutton _("[ev_naospecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospecial2.hint]")

                            #Eternity Until (naospecial3)
                            if (not ev_naospecial3.completed and not ev_naospecial3.missed) or show_complete:
                                if "(!)" in ev_naospecial3.hint:
                                    textbutton _("[ev_naospecial3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospecial3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospecial3.hint]")

                            text ("")

                            #Flora (naocamp1)
                            if (not ev_naocamp1.completed and not ev_naocamp1.missed) or show_complete:
                                if "(!)" in ev_naocamp1.hint:
                                    textbutton _("[ev_naocamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naocamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naocamp1.hint]")

                            #What's in the Pot? (naocamp2)
                            if (not ev_naocamp2.completed and not ev_naocamp2.missed) or show_complete:
                                if "(!)" in ev_naocamp2.hint:
                                    textbutton _("[ev_naocamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naocamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naocamp2.hint]")

                            #Even Gods Get Lost (halloweennao1)
                            if (not ev_halloweennao1.completed and not ev_halloweennao1.missed) or show_complete:
                                if "(!)" in ev_halloweennao1.hint:
                                    textbutton _("[ev_halloweennao1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweennao1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweennao1.hint]")

                            #A House Near a Lake (The Same Place as Always) (halloweennao2)
                            if (not ev_halloweennao2.completed and not ev_halloweennao2.missed) or show_complete:
                                if "(!)" in ev_halloweennao2.hint:
                                    textbutton _("[ev_halloweennao2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweennao2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweennao2.hint]")

                            #Wings of Anhedonia (naospring1)
                            if (not ev_naospring1.completed and not ev_naospring1.missed) or show_complete:
                                if "(!)" in ev_naospring1.hint:
                                    textbutton _("[ev_naospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospring1.hint]")

                            #Miracle (naospring2)
                            if (not ev_naospring2.completed and not ev_naospring2.missed) or show_complete:
                                if "(!)" in ev_naospring2.hint:
                                    textbutton _("[ev_naospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospring2.hint]")

                            #Nao More Than Ever (naospring3)
                            if (not ev_naospring3.completed and not ev_naospring3.missed) or show_complete:
                                if "(!)" in ev_naospring3.hint:
                                    textbutton _("[ev_naospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospring3.hint]")

                            #Menma (naospring4)
                            if (not ev_naospring4.completed and not ev_naospring4.missed) or show_complete:
                                if "(!)" in ev_naospring4.hint:
                                    textbutton _("[ev_naospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_naospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_naospring4.hint]")

                    #NIKIHINT

                    if showgirl == "Niki":

                        if not _in_replay:

                            #Cotton Candy (nikidate1)
                            if (not ev_nikidate1.completed and not ev_nikidate1.missed) or show_complete:
                                if "(!)" in ev_nikidate1.hint:
                                    textbutton _("[ev_nikidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikidate1.hint]")

                            #Like it's Any Other Day (nikidate5)
                            if (not ev_nikidate5.completed and not ev_nikidate5.missed) or show_complete:
                                if "(!)" in ev_nikidate5.hint:
                                    textbutton _("[ev_nikidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikidate5.hint]")

                            #Thousands, If Not Millions (nikidate10)
                            if (not ev_nikidate10.completed and not ev_nikidate10.missed) or show_complete:
                                if "(!)" in ev_nikidate10.hint:
                                    textbutton _("[ev_nikidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikidate10.hint]")

                            #Hotel Rooms (nikidate15)
                            if (not ev_nikidate15.completed and not ev_nikidate15.missed) or show_complete:
                                if "(!)" in ev_nikidate15.hint:
                                    textbutton _("[ev_nikidate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikidate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikidate15.hint]")

                            #Sisters (nikiinvite1)
                            if (not ev_nikiinvite1.completed and not ev_nikiinvite1.missed) or show_complete:
                                if "(!)" in ev_nikiinvite1.hint:
                                    textbutton _("[ev_nikiinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikiinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikiinvite1.hint]")

                            #Dear You (nikiinvite2)
                            if (not ev_nikiinvite2.completed and not ev_nikiinvite2.missed) or show_complete:
                                if "(!)" in ev_nikiinvite2.hint:
                                    textbutton _("[ev_nikiinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikiinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikiinvite2.hint]")

                            text ("")

                            #What it Takes to Move Forward (nikilovesyou1)
                            if (not ev_nikilovesyou1.completed and not ev_nikilovesyou1.missed) or show_complete:
                                if "(!)" in ev_nikilovesyou1.hint:
                                    textbutton _("[ev_nikilovesyou1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikilovesyou1.hint]")

                            #The End of the Tour (Glasswalker) (nikilovesyou2)
                            if (not ev_nikilovesyou2.completed and not ev_nikilovesyou2.missed) or show_complete:
                                if "(!)" in ev_nikilovesyou2.hint:
                                    textbutton _("[ev_nikilovesyou2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikilovesyou2.hint]")

                            #How To Make Love Stay (nikilovesyou3)
                            if (not ev_nikilovesyou3.completed and not ev_nikilovesyou3.missed) or show_complete:
                                if "(!)" in ev_nikilovesyou3.hint:
                                    textbutton _("[ev_nikilovesyou3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikilovesyou3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikilovesyou3.hint]")

                            #Non-Disclosure Agreement (nikifirstlust)
                            if (not ev_nikifirstlust.completed and not ev_nikifirstlust.missed) or show_complete:
                                if "(!)" in ev_nikifirstlust.hint:
                                    textbutton _("[ev_nikifirstlust.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikifirstlust), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikifirstlust.hint]")

                            text ("")

                            #They Came Together (nikispring1)
                            if (not ev_nikispring1.completed and not ev_nikispring1.missed) or show_complete:
                                if "(!)" in ev_nikispring1.hint:
                                    textbutton _("[ev_nikispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring1.hint]")

                            #The Clod and the Pebble (nikispring2)
                            if (not ev_nikispring2.completed and not ev_nikispring2.missed) or show_complete:
                                if "(!)" in ev_nikispring2.hint:
                                    textbutton _("[ev_nikispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring2.hint]")

                            #Broken Furniture (beachfive8)
                            if (not ev_beachfive8.completed and not ev_beachfive8.missed) or show_complete:
                                if "(!)" in ev_beachfive8.hint:
                                    textbutton _("[ev_beachfive8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive8.hint]")

                            #That Funny Feeling (nikispring3)
                            if (not ev_nikispring3.completed and not ev_nikispring3.missed) or show_complete:
                                if "(!)" in ev_nikispring3.hint:
                                    textbutton _("[ev_nikispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring3.hint]")

                            #Costco (Dick Lover) (nikispring4)
                            if (not ev_nikispring4.completed and not ev_nikispring4.missed) or show_complete:
                                if "(!)" in ev_nikispring4.hint:
                                    textbutton _("[ev_nikispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring4.hint]")

                            #Beauty in What's Broken (nikispring5)
                            if (not ev_nikispring5.completed and not ev_nikispring5.missed) or show_complete:
                                if "(!)" in ev_nikispring5.hint:
                                    textbutton _("[ev_nikispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring5.hint]")

                            #Artificial Love (nikispring6)
                            if (not ev_nikispring6.completed and not ev_nikispring6.missed) or show_complete:
                                if "(!)" in ev_nikispring6.hint:
                                    textbutton _("[ev_nikispring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring6.hint]")

                            #This World, So Full of Fish (nikispring7)
                            if (not ev_nikispring7.completed and not ev_nikispring7.missed) or show_complete:
                                if "(!)" in ev_nikispring7.hint:
                                    textbutton _("[ev_nikispring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring7.hint]")

                            #Say Anything (nikispring8)
                            if (not ev_nikispring8.completed and not ev_nikispring8.missed) or show_complete:
                                if "(!)" in ev_nikispring8.hint:
                                    textbutton _("[ev_nikispring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nikispring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nikispring8.hint]")

                            #Take it Easy (Love Nothing) (dormwarssixniki1)
                            if (not ev_dormwarssixniki1.completed and not ev_dormwarssixniki1.missed) or show_complete:
                                if "(!)" in ev_dormwarssixniki1.hint:
                                    textbutton _("[ev_dormwarssixniki1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarssixniki1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarssixniki1.hint]")

                    #NODOKAHINT

                    if showgirl == "Nodoka":

                        if not _in_replay:

                            #Humbert Humbert (nodokafirsthall)
                            if (not ev_nodokafirsthall.completed and not ev_nodokafirsthall.missed) or show_complete:
                                if "(!)" in ev_nodokafirsthall.hint:
                                    textbutton _("[ev_nodokafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokafirsthall.hint]")

                            #The Man Who Would Be King (nodokadorm1)
                            if (not ev_nodokadorm1.completed and not ev_nodokadorm1.missed) or show_complete:
                                if "(!)" in ev_nodokadorm1.hint:
                                    textbutton _("[ev_nodokadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokadorm1.hint]")

                            #Cracks in the Armor (nodokalibrary1)
                            if (not ev_nodokalibrary1.completed and not ev_nodokalibrary1.missed) or show_complete:
                                if "(!)" in ev_nodokalibrary1.hint:
                                    textbutton _("[ev_nodokalibrary1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokalibrary1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokalibrary1.hint]")

                            #Coloring Book (nodokalibrary5)
                            if (not ev_nodokalibrary5.completed and not ev_nodokalibrary5.missed) or show_complete:
                                if "(!)" in ev_nodokalibrary5.hint:
                                    textbutton _("[ev_nodokalibrary5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokalibrary5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokalibrary5.hint]")

                            #I See Everything (nodokadorm5)
                            if (not ev_nodokadorm5.completed and not ev_nodokadorm5.missed) or show_complete:
                                if "(!)" in ev_nodokadorm5.hint:
                                    textbutton _("[ev_nodokadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokadorm5.hint]")

                            text ("")

                            #Beyond the Reach of God (nodokadorm15)
                            if (not ev_nodokadorm15.completed and not ev_nodokadorm15.missed) or show_complete:
                                if "(!)" in ev_nodokadorm15.hint:
                                    textbutton _("[ev_nodokadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokadorm15.hint]")

                            #So Far Below (nodokaspecial15p1)
                            if (not ev_nodokaspecial15p1.completed and not ev_nodokaspecial15p1.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial15p1.hint:
                                    textbutton _("[ev_nodokaspecial15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial15p1.hint]")

                            #Matador (nodokaspecial15p2)
                            if (not ev_nodokaspecial15p2.completed and not ev_nodokaspecial15p2.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial15p2.hint:
                                    textbutton _("[ev_nodokaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial15p2.hint]")

                            #Things That Hurt (nodokaspecial15p3)
                            if (not ev_nodokaspecial15p3.completed and not ev_nodokaspecial15p3.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial15p3.hint:
                                    textbutton _("[ev_nodokaspecial15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial15p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial15p3.hint]")

                            #Twisting Ivy (nodokaspecial20)
                            if (not ev_nodokaspecial20.completed and not ev_nodokaspecial20.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial20.hint:
                                    textbutton _("[ev_nodokaspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial20.hint]")

                            #Amoeba (Incontrovertible Peculiarity) (nodokaspecial30p1)
                            if (not ev_nodokaspecial30p1.completed and not ev_nodokaspecial30p1.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial30p1.hint:
                                    textbutton _("[ev_nodokaspecial30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial30p1.hint]")

                            #This is Us (nodokaspecial30p2)
                            if (not ev_nodokaspecial30p2.completed and not ev_nodokaspecial30p2.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial30p2.hint:
                                    textbutton _("[ev_nodokaspecial30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial30p2.hint]")

                            #Taco Attack (nodokaspecial30p3)
                            if (not ev_nodokaspecial30p3.completed and not ev_nodokaspecial30p3.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial30p3.hint:
                                    textbutton _("[ev_nodokaspecial30p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial30p3.hint]")

                            #Lavender (nodokaspecial30p4)
                            if (not ev_nodokaspecial30p4.completed and not ev_nodokaspecial30p4.missed) or show_complete:
                                if "(!)" in ev_nodokaspecial30p4.hint:
                                    textbutton _("[ev_nodokaspecial30p4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspecial30p4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspecial30p4.hint]")

                            text ("")

                            #Meet & Fuck (sportswars17)
                            if (not ev_sportswars17.completed and not ev_sportswars17.missed) or show_complete:
                                if "(!)" in ev_sportswars17.hint:
                                    textbutton _("[ev_sportswars17.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars17), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars17.hint]")

                            #The Silver King (beachfive6)
                            if (not ev_beachfive6.completed and not ev_beachfive6.missed) or show_complete:
                                if "(!)" in ev_beachfive6.hint:
                                    textbutton _("[ev_beachfive6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive6.hint]")

                            #Mille Crepe (beachfive10)
                            if (not ev_beachfive10.completed and not ev_beachfive10.missed) or show_complete:
                                if "(!)" in ev_beachfive10.hint:
                                    textbutton _("[ev_beachfive10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive10.hint]")

                            #When the Well Runs Dry (halloweennodoka1)
                            if (not ev_halloweennodoka1.completed and not ev_halloweennodoka1.missed) or show_complete:
                                if "(!)" in ev_halloweennodoka1.hint:
                                    textbutton _("[ev_halloweennodoka1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweennodoka1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweennodoka1.hint]")

                            #Perfect Hair Forever (nodokainvite1)
                            if (not ev_nodokainvite1.completed and not ev_nodokainvite1.missed) or show_complete:
                                if "(!)" in ev_nodokainvite1.hint:
                                    textbutton _("[ev_nodokainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokainvite1.hint]")

                            #Number One Fan (nodokainvite2)
                            if (not ev_nodokainvite2.completed and not ev_nodokainvite2.missed) or show_complete:
                                if "(!)" in ev_nodokainvite2.hint:
                                    textbutton _("[ev_nodokainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokainvite2.hint]")

                            #How to Fuck Your Father (nodokainvite3)
                            if (not ev_nodokainvite3.completed and not ev_nodokainvite3.missed) or show_complete:
                                if "(!)" in ev_nodokainvite3.hint:
                                    textbutton _("[ev_nodokainvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokainvite3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokainvite3.hint]")

                            #Hark! Now I Hear Them. (nodokachristmalloween1)
                            if (not ev_nodokachristmalloween1.completed and not ev_nodokachristmalloween1.missed) or show_complete:
                                if "(!)" in ev_nodokachristmalloween1.hint:
                                    textbutton _("[ev_nodokachristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokachristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokachristmalloween1.hint]")

                            #Beseech the Queen (nodokachristmalloween2)
                            if (not ev_nodokachristmalloween2.completed and not ev_nodokachristmalloween2.missed) or show_complete:
                                if "(!)" in ev_nodokachristmalloween2.hint:
                                    textbutton _("[ev_nodokachristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokachristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokachristmalloween2.hint]")

                            #The Hours of Folly (Return to Sender) (nodokachristmalloween3)
                            if (not ev_nodokachristmalloween3.completed and not ev_nodokachristmalloween3.missed) or show_complete:
                                if "(!)" in ev_nodokachristmalloween3.hint:
                                    textbutton _("[ev_nodokachristmalloween3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokachristmalloween3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokachristmalloween3.hint]")

                            #Rotten Wood & Rusty Nails (dormwarssixnodoka1)
                            if (not ev_dormwarssixnodoka1.completed and not ev_dormwarssixnodoka1.missed) or show_complete:
                                if "(!)" in ev_dormwarssixnodoka1.hint:
                                    textbutton _("[ev_dormwarssixnodoka1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarssixnodoka1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarssixnodoka1.hint]")

                            #Number Girl (nodokaspring1)
                            if (not ev_nodokaspring1.completed and not ev_nodokaspring1.missed) or show_complete:
                                if "(!)" in ev_nodokaspring1.hint:
                                    textbutton _("[ev_nodokaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspring1.hint]")

                            #Virgin Birth (Passer Montanus) (nodokaspring2)
                            if (not ev_nodokaspring2.completed and not ev_nodokaspring2.missed) or show_complete:
                                if "(!)" in ev_nodokaspring2.hint:
                                    textbutton _("[ev_nodokaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspring2.hint]")

                            #Worlds Unseen (nodokaspring3)
                            if (not ev_nodokaspring3.completed and not ev_nodokaspring3.missed) or show_complete:
                                if "(!)" in ev_nodokaspring3.hint:
                                    textbutton _("[ev_nodokaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_nodokaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_nodokaspring3.hint]")

                    #NORIKOHINT

                    if showgirl == "Noriko":

                        if not _in_replay:

                            #Sculpture (Dream Girl) (norikofirsthall)
                            if (not ev_norikofirsthall.completed and not ev_norikofirsthall.missed) or show_complete:
                                if "(!)" in ev_norikofirsthall.hint:
                                    textbutton _("[ev_norikofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikofirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikofirsthall.hint]")

                            #Nakayarakawayama (convenience1)
                            if (not ev_convenience1.completed and not ev_convenience1.missed) or show_complete:
                                if "(!)" in ev_convenience1.hint:
                                    textbutton _("[ev_convenience1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_convenience1.hint]")

                            #Semi-Constructive Criticism (norikodorm5)
                            if (not ev_norikodorm5.completed and not ev_norikodorm5.missed) or show_complete:
                                if "(!)" in ev_norikodorm5.hint:
                                    textbutton _("[ev_norikodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodorm5.hint]")

                            #Mouthjob (convenience5)
                            if (not ev_convenience5.completed and not ev_convenience5.missed) or show_complete:
                                if "(!)" in ev_convenience5.hint:
                                    textbutton _("[ev_convenience5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_convenience5.hint]")

                            #Kind Of, Yes. Kind Of, No. (norikodorm10)
                            if (not ev_norikodorm10.completed and not ev_norikodorm10.missed) or show_complete:
                                if "(!)" in ev_norikodorm10.hint:
                                    textbutton _("[ev_norikodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodorm10.hint]")

                            #New Shoes (norikoinvite1)
                            if (not ev_norikoinvite1.completed and not ev_norikoinvite1.missed) or show_complete:
                                if "(!)" in ev_norikoinvite1.hint:
                                    textbutton _("[ev_norikoinvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite1.hint]")

                            #Beginnings. Endings. Things in Between. (norikoinvite2)
                            if (not ev_norikoinvite2.completed and not ev_norikoinvite2.missed) or show_complete:
                                if "(!)" in ev_norikoinvite2.hint:
                                    textbutton _("[ev_norikoinvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite2.hint]")

                            #Fair & Square (norikospecial20)
                            if (not ev_norikospecial20.completed and not ev_norikospecial20.missed) or show_complete:
                                if "(!)" in ev_norikospecial20.hint:
                                    textbutton _("[ev_norikospecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospecial20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospecial20.hint]")

                            #Homes for the Homeless (norikodorm20)
                            if (not ev_norikodorm20.completed and not ev_norikodorm20.missed) or show_complete:
                                if "(!)" in ev_norikodorm20.hint:
                                    textbutton _("[ev_norikodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodorm20.hint]")

                            #That One FMK Scene (convenience25)
                            if (not ev_convenience25.completed and not ev_convenience25.missed) or show_complete:
                                if "(!)" in ev_convenience25.hint:
                                    textbutton _("[ev_convenience25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_convenience25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_convenience25.hint]")

                            #Loxosceles Reclusa (norikodorm25)
                            if (not ev_norikodorm25.completed and not ev_norikodorm25.missed) or show_complete:
                                if "(!)" in ev_norikodorm25.hint:
                                    textbutton _("[ev_norikodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodorm25.hint]")

                            text ("")

                            #Hotel Noriko (norikodate30)
                            if (not ev_norikodate30.completed and not ev_norikodate30.missed) or show_complete:
                                if "(!)" in ev_norikodate30.hint:
                                    textbutton _("[ev_norikodate30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodate30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodate30.hint]")

                            #Dotted Line (norikodorm30)
                            if (not ev_norikodorm30.completed and not ev_norikodorm30.missed) or show_complete:
                                if "(!)" in ev_norikodorm30.hint:
                                    textbutton _("[ev_norikodorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikodorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikodorm30.hint]")

                            #I Really Want to Stay at Your House (norikoinvite3)
                            if (not ev_norikoinvite3.completed and not ev_norikoinvite3.missed) or show_complete:
                                if "(!)" in ev_norikoinvite3.hint:
                                    textbutton _("[ev_norikoinvite3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite3.hint]")

                            #Somewhere (norikoinvite4)
                            if (not ev_norikoinvite4.completed and not ev_norikoinvite4.missed) or show_complete:
                                if "(!)" in ev_norikoinvite4.hint:
                                    textbutton _("[ev_norikoinvite4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite4.hint]")

                            text ("")

                            #Rivals (Taco Tuesday) (sportswars2)
                            if (not ev_sportswars2.completed and not ev_sportswars2.missed) or show_complete:
                                if "(!)" in ev_sportswars2.hint:
                                    textbutton _("[ev_sportswars2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars2.hint]")

                            #The Long Road Ahead (norikospring1)
                            if (not ev_norikospring1.completed and not ev_norikospring1.missed) or show_complete:
                                if "(!)" in ev_norikospring1.hint:
                                    textbutton _("[ev_norikospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospring1.hint]")

                            #Transpacific Sadness Symposium I: DEN OF THE MOLE RAT (norikospring2)
                            if (not ev_norikospring2.completed and not ev_norikospring2.missed) or show_complete:
                                if "(!)" in ev_norikospring2.hint:
                                    textbutton _("[ev_norikospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospring2.hint]")

                            #Hard-Off (norikospring3)
                            if (not ev_norikospring3.completed and not ev_norikospring3.missed) or show_complete:
                                if "(!)" in ev_norikospring3.hint:
                                    textbutton _("[ev_norikospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospring3.hint]")

                            #Haiku (norikospring4)
                            if (not ev_norikospring4.completed and not ev_norikospring4.missed) or show_complete:
                                if "(!)" in ev_norikospring4.hint:
                                    textbutton _("[ev_norikospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospring4.hint]")

                            #At The Beach, In Every Life (norikospring5)
                            if (not ev_norikospring5.completed and not ev_norikospring5.missed) or show_complete:
                                if "(!)" in ev_norikospring5.hint:
                                    textbutton _("[ev_norikospring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikospring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikospring5.hint]")

                            #Circling the Drain (beachsixnoriko1)
                            if (not ev_beachsixnoriko1.completed and not ev_beachsixnoriko1.missed) or show_complete:
                                if "(!)" in ev_beachsixnoriko1.hint:
                                    textbutton _("[ev_beachsixnoriko1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixnoriko1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixnoriko1.hint]")

                            #Reasons to Die (norikoinvite5)
                            if (not ev_norikoinvite5.completed and not ev_norikoinvite5.missed) or show_complete:
                                if "(!)" in ev_norikoinvite5.hint:
                                    textbutton _("[ev_norikoinvite5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite5.hint]")

                            #Love in Strange Forms (norikoinvite6)
                            if (not ev_norikoinvite6.completed and not ev_norikoinvite6.missed) or show_complete:
                                if "(!)" in ev_norikoinvite6.hint:
                                    textbutton _("[ev_norikoinvite6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_norikoinvite6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_norikoinvite6.hint]")

                    #OSAKOHINT

                    if showgirl == "Osako":

                        if not _in_replay:

                            #Pressure Point (osakodate1)
                            if (not ev_osakodate1.completed and not ev_osakodate1.missed) or show_complete:
                                if "(!)" in ev_osakodate1.hint:
                                    textbutton _("[ev_osakodate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakodate1.hint]")

                            #Floating Forever, Unfulfilled (osakodojo1)
                            if (not ev_osakodojo1.completed and not ev_osakodojo1.missed) or show_complete:
                                if "(!)" in ev_osakodojo1.hint:
                                    textbutton _("[ev_osakodojo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodojo1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakodojo1.hint]")

                            text ("")

                            #Young At Heart (osakodate15)
                            if (not ev_osakodate15.completed and not ev_osakodate15.missed) or show_complete:
                                if "(!)" in ev_osakodate15.hint:
                                    textbutton _("[ev_osakodate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakodate15.hint]")

                            #House of the Unholy (osakodate20)
                            if (not ev_osakodate20.completed and not ev_osakodate20.missed) or show_complete:
                                if "(!)" in ev_osakodate20.hint:
                                    textbutton _("[ev_osakodate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakodate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakodate20.hint]")

                            text ("")

                            #Chaos Spiral (Heterosexual Sex) (osakospring1)
                            if (not ev_osakospring1.completed and not ev_osakospring1.missed) or show_complete:
                                if "(!)" in ev_osakospring1.hint:
                                    textbutton _("[ev_osakospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring1.hint]")

                            #Meat-Pocket (osakospring2)
                            if (not ev_osakospring2.completed and not ev_osakospring2.missed) or show_complete:
                                if "(!)" in ev_osakospring2.hint:
                                    textbutton _("[ev_osakospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring2.hint]")

                            #Indecent Proposal (osakospring3)
                            if (not ev_osakospring3.completed and not ev_osakospring3.missed) or show_complete:
                                if "(!)" in ev_osakospring3.hint:
                                    textbutton _("[ev_osakospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring3.hint]")

                            #MILF of the Month Club (osakospring4)
                            if (not ev_osakospring4.completed and not ev_osakospring4.missed) or show_complete:
                                if "(!)" in ev_osakospring4.hint:
                                    textbutton _("[ev_osakospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring4.hint]")

                            #Girl C (osakospring5)
                            if (not ev_osakospring5.completed and not ev_osakospring5.missed) or show_complete:
                                if "(!)" in ev_osakospring5.hint:
                                    textbutton _("[ev_osakospring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring5.hint]")

                            #All Good Things (osakospring6)
                            if (not ev_osakospring6.completed and not ev_osakospring6.missed) or show_complete:
                                if "(!)" in ev_osakospring6.hint:
                                    textbutton _("[ev_osakospring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring6.hint]")

                            #When Harry Met Gandalf (osakospring7)
                            if (not ev_osakospring7.completed and not ev_osakospring7.missed) or show_complete:
                                if "(!)" in ev_osakospring7.hint:
                                    textbutton _("[ev_osakospring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring7.hint]")

                            #Troubles, Trials, and Tribadism (osakospring8)
                            if (not ev_osakospring8.completed and not ev_osakospring8.missed) or show_complete:
                                if "(!)" in ev_osakospring8.hint:
                                    textbutton _("[ev_osakospring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring8.hint]")

                            #Pica (osakospring9)
                            if (not ev_osakospring9.completed and not ev_osakospring9.missed) or show_complete:
                                if "(!)" in ev_osakospring9.hint:
                                    textbutton _("[ev_osakospring9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_osakospring9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_osakospring9.hint]")

                    #OTOHAHINT

                    if showgirl == "Otoha":

                        if not _in_replay:

                            #Everybody Loves Otoha (otohafirsthall)
                            if (not ev_otohafirsthall.completed and not ev_otohafirsthall.missed) or show_complete:
                                if "(!)" in ev_otohafirsthall.hint:
                                    textbutton _("[ev_otohafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohafirsthall.hint]")

                            #Conversations Outside of a Girls’ Dorm (otohadorm1)
                            if (not ev_otohadorm1.completed and not ev_otohadorm1.missed) or show_complete:
                                if "(!)" in ev_otohadorm1.hint:
                                    textbutton _("[ev_otohadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohadorm1.hint]")

                            #Japanese Summer (Double Suicide) (otohapark1)
                            if (not ev_otohapark1.completed and not ev_otohapark1.missed) or show_complete:
                                if "(!)" in ev_otohapark1.hint:
                                    textbutton _("[ev_otohapark1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohapark1.hint]")

                            #Locked In (otohapark5)
                            if (not ev_otohapark5.completed and not ev_otohapark5.missed) or show_complete:
                                if "(!)" in ev_otohapark5.hint:
                                    textbutton _("[ev_otohapark5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohapark5.hint]")

                            #Highly Pornographic (otohadorm5)
                            if (not ev_otohadorm5.completed and not ev_otohadorm5.missed) or show_complete:
                                if "(!)" in ev_otohadorm5.hint:
                                    textbutton _("[ev_otohadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohadorm5.hint]")

                            #Pull the Plug (otohapark10)
                            if (not ev_otohapark10.completed and not ev_otohapark10.missed) or show_complete:
                                if "(!)" in ev_otohapark10.hint:
                                    textbutton _("[ev_otohapark10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohapark10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohapark10.hint]")

                            #Two-Octave Pitch Glide (otohaspecial10)
                            if (not ev_otohaspecial10.completed and not ev_otohaspecial10.missed) or show_complete:
                                if "(!)" in ev_otohaspecial10.hint:
                                    textbutton _("[ev_otohaspecial10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspecial10.hint]")

                            #Breathing in Unison (otohadorm10)
                            if (not ev_otohadorm10.completed and not ev_otohadorm10.missed) or show_complete:
                                if "(!)" in ev_otohadorm10.hint:
                                    textbutton _("[ev_otohadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohadorm10.hint]")

                            #Vanilla Bean (otohadorm10p2)
                            if (not ev_otohadorm10p2.completed and not ev_otohadorm10p2.missed) or show_complete:
                                if "(!)" in ev_otohadorm10p2.hint:
                                    textbutton _("[ev_otohadorm10p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadorm10p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohadorm10p2.hint]")

                            text ("")

                            #King Midas (otohaspecial15p1)
                            if (not ev_otohaspecial15p1.completed and not ev_otohaspecial15p1.missed) or show_complete:
                                if "(!)" in ev_otohaspecial15p1.hint:
                                    textbutton _("[ev_otohaspecial15p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial15p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspecial15p1.hint]")

                            #White People (otohaspecial15p2)
                            if (not ev_otohaspecial15p2.completed and not ev_otohaspecial15p2.missed) or show_complete:
                                if "(!)" in ev_otohaspecial15p2.hint:
                                    textbutton _("[ev_otohaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspecial15p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspecial15p2.hint]")

                            #Breaking Character (otohadate20)
                            if (not ev_otohadate20.completed and not ev_otohadate20.missed) or show_complete:
                                if "(!)" in ev_otohadate20.hint:
                                    textbutton _("[ev_otohadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohadate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohadate20.hint]")

                            text ("")

                            #This Curse Called Youth (otohaspring1)
                            if (not ev_otohaspring1.completed and not ev_otohaspring1.missed) or show_complete:
                                if "(!)" in ev_otohaspring1.hint:
                                    textbutton _("[ev_otohaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring1.hint]")

                            #Taint the Sapling (otohaspring2)
                            if (not ev_otohaspring2.completed and not ev_otohaspring2.missed) or show_complete:
                                if "(!)" in ev_otohaspring2.hint:
                                    textbutton _("[ev_otohaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring2.hint]")

                            #Something Wonderful (otohaspring3)
                            if (not ev_otohaspring3.completed and not ev_otohaspring3.missed) or show_complete:
                                if "(!)" in ev_otohaspring3.hint:
                                    textbutton _("[ev_otohaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring3.hint]")

                            #Sisterly Love (christmasotoha1)
                            if (not ev_christmasotoha1.completed and not ev_christmasotoha1.missed) or show_complete:
                                if "(!)" in ev_christmasotoha1.hint:
                                    textbutton _("[ev_christmasotoha1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmasotoha1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmasotoha1.hint]")

                            #Becoming Closer to Closure (otohaspring4)
                            if (not ev_otohaspring4.completed and not ev_otohaspring4.missed) or show_complete:
                                if "(!)" in ev_otohaspring4.hint:
                                    textbutton _("[ev_otohaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring4.hint]")

                            #Something in the Water (beachsixotoha1)
                            if (not ev_beachsixotoha1.completed and not ev_beachsixotoha1.missed) or show_complete:
                                if "(!)" in ev_beachsixotoha1.hint:
                                    textbutton _("[ev_beachsixotoha1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixotoha1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixotoha1.hint]")

                            #Five Star Review (otohaspring5)
                            if (not ev_otohaspring5.completed and not ev_otohaspring5.missed) or show_complete:
                                if "(!)" in ev_otohaspring5.hint:
                                    textbutton _("[ev_otohaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring5.hint]")

                            #Billboard Hot 100 (otohaspring6)
                            if (not ev_otohaspring6.completed and not ev_otohaspring6.missed) or show_complete:
                                if "(!)" in ev_otohaspring6.hint:
                                    textbutton _("[ev_otohaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring6.hint]")

                            #Pet Sounds (otohaspring7)
                            if (not ev_otohaspring7.completed and not ev_otohaspring7.missed) or show_complete:
                                if "(!)" in ev_otohaspring7.hint:
                                    textbutton _("[ev_otohaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_otohaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_otohaspring7.hint]")

                    #RIKAHINT

                    if showgirl == "Rika":

                        if not _in_replay:

                            #Impregnation Spree (rikadate1)
                            if (not ev_rikadate1.completed and not ev_rikadate1.missed) or show_complete:
                                if "(!)" in ev_rikadate1.hint:
                                    textbutton _("[ev_rikadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikadate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikadate1.hint]")

                            #Back on Track (rikaspecial2)
                            if (not ev_rikaspecial2.completed and not ev_rikaspecial2.missed) or show_complete:
                                if "(!)" in ev_rikaspecial2.hint:
                                    textbutton _("[ev_rikaspecial2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspecial2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspecial2.hint]")

                            #James and the Giant Peach (Together-ish) (rikadive1)
                            if (not ev_rikadive1.completed and not ev_rikadive1.missed) or show_complete:
                                if "(!)" in ev_rikadive1.hint:
                                    textbutton _("[ev_rikadive1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikadive1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikadive1.hint]")

                            text ("")

                            #Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You (sportswars1)
                            if (not ev_sportswars1.completed and not ev_sportswars1.missed) or show_complete:
                                if "(!)" in ev_sportswars1.hint:
                                    textbutton _("[ev_sportswars1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sportswars1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sportswars1.hint]")

                            #Rat College (rikaspring1)
                            if (not ev_rikaspring1.completed and not ev_rikaspring1.missed) or show_complete:
                                if "(!)" in ev_rikaspring1.hint:
                                    textbutton _("[ev_rikaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring1.hint]")

                            #Sixty-Minute Mark (rikaspring2)
                            if (not ev_rikaspring2.completed and not ev_rikaspring2.missed) or show_complete:
                                if "(!)" in ev_rikaspring2.hint:
                                    textbutton _("[ev_rikaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring2.hint]")

                            #Sins of Thy Beloved (rikaspring3)
                            if (not ev_rikaspring3.completed and not ev_rikaspring3.missed) or show_complete:
                                if "(!)" in ev_rikaspring3.hint:
                                    textbutton _("[ev_rikaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring3.hint]")

                            #Four Hours, Thirteen Minutes, Eleven Seconds (rikaspring4)
                            if (not ev_rikaspring4.completed and not ev_rikaspring4.missed) or show_complete:
                                if "(!)" in ev_rikaspring4.hint:
                                    textbutton _("[ev_rikaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring4.hint]")

                            #A Horse Rides an Elephant (rikaspring5)
                            if (not ev_rikaspring5.completed and not ev_rikaspring5.missed) or show_complete:
                                if "(!)" in ev_rikaspring5.hint:
                                    textbutton _("[ev_rikaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring5.hint]")

                            #Solidarity (Hag Scene) (rikaspring6)
                            if (not ev_rikaspring6.completed and not ev_rikaspring6.missed) or show_complete:
                                if "(!)" in ev_rikaspring6.hint:
                                    textbutton _("[ev_rikaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring6.hint]")

                            #How to Escape a Quagmire (rikaspring7)
                            if (not ev_rikaspring7.completed and not ev_rikaspring7.missed) or show_complete:
                                if "(!)" in ev_rikaspring7.hint:
                                    textbutton _("[ev_rikaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rikaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rikaspring7.hint]")

                    #RINHINT

                    if showgirl == "Rin":

                        if not _in_replay:

                            #Guinea Pig (firsttimecafe)
                            if (not ev_firsttimecafe.completed and not ev_firsttimecafe.missed) or show_complete:
                                if "(!)" in ev_firsttimecafe.hint:
                                    textbutton _("[ev_firsttimecafe.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimecafe), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimecafe.hint]")

                            #The Flavor of Love (cafesugar)
                            if (not ev_cafesugar.completed and not ev_cafesugar.missed) or show_complete:
                                if "(!)" in ev_cafesugar.hint:
                                    textbutton _("[ev_cafesugar.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafesugar), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafesugar.hint]")

                            #Haruka (cafe10)
                            if (not ev_cafe10.completed and not ev_cafe10.missed) or show_complete:
                                if "(!)" in ev_cafe10.hint:
                                    textbutton _("[ev_cafe10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe10.hint]")

                            #Locked Out (rinfirsthall)
                            if (not ev_rinfirsthall.completed and not ev_rinfirsthall.missed) or show_complete:
                                if "(!)" in ev_rinfirsthall.hint:
                                    textbutton _("[ev_rinfirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinfirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinfirsthall.hint]")

                            #Skulls (rinfirstvisit)
                            if (not ev_rinfirstvisit.completed and not ev_rinfirstvisit.missed) or show_complete:
                                if "(!)" in ev_rinfirstvisit.hint:
                                    textbutton _("[ev_rinfirstvisit.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinfirstvisit), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinfirstvisit.hint]")

                            #Rin's Secret (rindorm10)
                            if (not ev_rindorm10.completed and not ev_rindorm10.missed) or show_complete:
                                if "(!)" in ev_rindorm10.hint:
                                    textbutton _("[ev_rindorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm10.hint]")

                            #Window of the Waking Mind (cafe15)
                            if (not ev_cafe15.completed and not ev_cafe15.missed) or show_complete:
                                if "(!)" in ev_cafe15.hint:
                                    textbutton _("[ev_cafe15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe15.hint]")

                            #Boundaries (rindorm15)
                            if (not ev_rindorm15.completed and not ev_rindorm15.missed) or show_complete:
                                if "(!)" in ev_rindorm15.hint:
                                    textbutton _("[ev_rindorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm15.hint]")

                            #Nothing Was Missing, Except Me (cafe20)
                            if (not ev_cafe20.completed and not ev_cafe20.missed) or show_complete:
                                if "(!)" in ev_cafe20.hint:
                                    textbutton _("[ev_cafe20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe20.hint]")

                            #Delirium (rindorm20)
                            if (not ev_rindorm20.completed and not ev_rindorm20.missed) or show_complete:
                                if "(!)" in ev_rindorm20.hint:
                                    textbutton _("[ev_rindorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm20.hint]")

                            #Good Day, Humans (cafe25)
                            if (not ev_cafe25.completed and not ev_cafe25.missed) or show_complete:
                                if "(!)" in ev_cafe25.hint:
                                    textbutton _("[ev_cafe25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe25.hint]")

                            #Sock Fetish (rindorm25)
                            if (not ev_rindorm25.completed and not ev_rindorm25.missed) or show_complete:
                                if "(!)" in ev_rindorm25.hint:
                                    textbutton _("[ev_rindorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm25.hint]")

                            #Nothing Was Different (cafe30)
                            if (not ev_cafe30.completed and not ev_cafe30.missed) or show_complete:
                                if "(!)" in ev_cafe30.hint:
                                    textbutton _("[ev_cafe30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe30.hint]")

                            #Two Steps Back (rindorm30)
                            if (not ev_rindorm30.completed and not ev_rindorm30.missed) or show_complete:
                                if "(!)" in ev_rindorm30.hint:
                                    textbutton _("[ev_rindorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm30.hint]")

                            #Ten Steps Forward (rindorm35)
                            if (not ev_rindorm35.completed and not ev_rindorm35.missed) or show_complete:
                                if "(!)" in ev_rindorm35.hint:
                                    textbutton _("[ev_rindorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm35.hint]")

                            #I Died With You (cafe35)
                            if (not ev_cafe35.completed and not ev_cafe35.missed) or show_complete:
                                if "(!)" in ev_cafe35.hint:
                                    textbutton _("[ev_cafe35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe35.hint]")

                            text ("")

                            #Sketchy Basement (cafe40)
                            if (not ev_cafe40.completed and not ev_cafe40.missed) or show_complete:
                                if "(!)" in ev_cafe40.hint:
                                    textbutton _("[ev_cafe40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe40.hint]")

                            #Semantics (rindorm40)
                            if (not ev_rindorm40.completed and not ev_rindorm40.missed) or show_complete:
                                if "(!)" in ev_rindorm40.hint:
                                    textbutton _("[ev_rindorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm40.hint]")

                            #Debatably Bisexual Musicians (cafe45)
                            if (not ev_cafe45.completed and not ev_cafe45.missed) or show_complete:
                                if "(!)" in ev_cafe45.hint:
                                    textbutton _("[ev_cafe45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe45.hint]")

                            #The Art of Never Knowing (rindorm45)
                            if (not ev_rindorm45.completed and not ev_rindorm45.missed) or show_complete:
                                if "(!)" in ev_rindorm45.hint:
                                    textbutton _("[ev_rindorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm45.hint]")

                            #The Paragon of Not Worrying About Stuff (cafe50)
                            if (not ev_cafe50.completed and not ev_cafe50.missed) or show_complete:
                                if "(!)" in ev_cafe50.hint:
                                    textbutton _("[ev_cafe50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_cafe50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_cafe50.hint]")

                            #Technicolored Happiness Explosion (rindorm50)
                            if (not ev_rindorm50.completed and not ev_rindorm50.missed) or show_complete:
                                if "(!)" in ev_rindorm50.hint:
                                    textbutton _("[ev_rindorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm50.hint]")

                            #Lifejacket (rindorm50special)
                            if (not ev_rindorm50special.completed and not ev_rindorm50special.missed) or show_complete:
                                if "(!)" in ev_rindorm50special.hint:
                                    textbutton _("[ev_rindorm50special.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm50special), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm50special.hint]")

                            #The Happiest Girl in the World (rindate50)
                            if (not ev_rindate50.completed and not ev_rindate50.missed) or show_complete:
                                if "(!)" in ev_rindate50.hint:
                                    textbutton _("[ev_rindate50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindate50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindate50.hint]")

                            text ("")

                            #Disaster Lesbian (rindorm55)
                            if (not ev_rindorm55.completed and not ev_rindorm55.missed) or show_complete:
                                if "(!)" in ev_rindorm55.hint:
                                    textbutton _("[ev_rindorm55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm55.hint]")

                            #Hot Boy Summer (rindorm55p2)
                            if (not ev_rindorm55p2.completed and not ev_rindorm55p2.missed) or show_complete:
                                if "(!)" in ev_rindorm55p2.hint:
                                    textbutton _("[ev_rindorm55p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rindorm55p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rindorm55p2.hint]")

                            #Ever Fallen In Love (rinspecial55)
                            if (not ev_rinspecial55.completed and not ev_rinspecial55.missed) or show_complete:
                                if "(!)" in ev_rinspecial55.hint:
                                    textbutton _("[ev_rinspecial55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspecial55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspecial55.hint]")

                            text ("")

                            #Anthem of the Heart (rinspring1)
                            if (not ev_rinspring1.completed and not ev_rinspring1.missed) or show_complete:
                                if "(!)" in ev_rinspring1.hint:
                                    textbutton _("[ev_rinspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring1.hint]")

                            #Voices of a Distant Star (rinspring2)
                            if (not ev_rinspring2.completed and not ev_rinspring2.missed) or show_complete:
                                if "(!)" in ev_rinspring2.hint:
                                    textbutton _("[ev_rinspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring2.hint]")

                            #Sex Dreams (rinspring3)
                            if (not ev_rinspring3.completed and not ev_rinspring3.missed) or show_complete:
                                if "(!)" in ev_rinspring3.hint:
                                    textbutton _("[ev_rinspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring3.hint]")

                            #Voice of Reason (rinspring4)
                            if (not ev_rinspring4.completed and not ev_rinspring4.missed) or show_complete:
                                if "(!)" in ev_rinspring4.hint:
                                    textbutton _("[ev_rinspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring4.hint]")

                            #Dear Sensei (Red Sea) (rinspring5)
                            if (not ev_rinspring5.completed and not ev_rinspring5.missed) or show_complete:
                                if "(!)" in ev_rinspring5.hint:
                                    textbutton _("[ev_rinspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring5.hint]")

                            #Love Long Overdue (rinspring6)
                            if (not ev_rinspring6.completed and not ev_rinspring6.missed) or show_complete:
                                if "(!)" in ev_rinspring6.hint:
                                    textbutton _("[ev_rinspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring6.hint]")

                            #The First Time Since the Last Time (dormwarsfiverin1)
                            if (not ev_dormwarsfiverin1.completed and not ev_dormwarsfiverin1.missed) or show_complete:
                                if "(!)" in ev_dormwarsfiverin1.hint:
                                    textbutton _("[ev_dormwarsfiverin1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarsfiverin1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarsfiverin1.hint]")

                            #Days to Waste (rinspring7)
                            if (not ev_rinspring7.completed and not ev_rinspring7.missed) or show_complete:
                                if "(!)" in ev_rinspring7.hint:
                                    textbutton _("[ev_rinspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring7.hint]")

                            #Table for Two (rinspring8)
                            if (not ev_rinspring8.completed and not ev_rinspring8.missed) or show_complete:
                                if "(!)" in ev_rinspring8.hint:
                                    textbutton _("[ev_rinspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring8.hint]")

                            #Transpacific Sadness Symposium VIII: AN ATOM (ME) AND ADAM (YOU) (rinspring9)
                            if (not ev_rinspring9.completed and not ev_rinspring9.missed) or show_complete:
                                if "(!)" in ev_rinspring9.hint:
                                    textbutton _("[ev_rinspring9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_rinspring9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_rinspring9.hint]")

                    #SANAHINT

                    if showgirl == "Sana":

                        if not _in_replay:

                            #Family Business (firsttimebar)
                            if (not ev_firsttimebar.completed and not ev_firsttimebar.missed) or show_complete:
                                if "(!)" in ev_firsttimebar.hint:
                                    textbutton _("[ev_firsttimebar.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimebar), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimebar.hint]")

                            #Nothing to Do (sanafirsthall)
                            if (not ev_sanafirsthall.completed and not ev_sanafirsthall.missed) or show_complete:
                                if "(!)" in ev_sanafirsthall.hint:
                                    textbutton _("[ev_sanafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanafirsthall.hint]")

                            #The Bare Minimum (bar5)
                            if (not ev_bar5.completed and not ev_bar5.missed) or show_complete:
                                if "(!)" in ev_bar5.hint:
                                    textbutton _("[ev_bar5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar5.hint]")

                            #Recluse (sanadorm5)
                            if (not ev_sanadorm5.completed and not ev_sanadorm5.missed) or show_complete:
                                if "(!)" in ev_sanadorm5.hint:
                                    textbutton _("[ev_sanadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm5.hint]")

                            #Supermom (bar10)
                            if (not ev_bar10.completed and not ev_bar10.missed) or show_complete:
                                if "(!)" in ev_bar10.hint:
                                    textbutton _("[ev_bar10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar10.hint]")

                            #Anywhere At All (sanadorm10)
                            if (not ev_sanadorm10.completed and not ev_sanadorm10.missed) or show_complete:
                                if "(!)" in ev_sanadorm10.hint:
                                    textbutton _("[ev_sanadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm10.hint]")

                            #Carry Me Home (bar15)
                            if (not ev_bar15.completed and not ev_bar15.missed) or show_complete:
                                if "(!)" in ev_bar15.hint:
                                    textbutton _("[ev_bar15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar15.hint]")

                            #Shaking The Tree (sanadorm15)
                            if (not ev_sanadorm15.completed and not ev_sanadorm15.missed) or show_complete:
                                if "(!)" in ev_sanadorm15.hint:
                                    textbutton _("[ev_sanadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm15.hint]")

                            #Scouting Mission (bar20)
                            if (not ev_bar20.completed and not ev_bar20.missed) or show_complete:
                                if "(!)" in ev_bar20.hint:
                                    textbutton _("[ev_bar20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar20.hint]")

                            #Nice Weather We're Having (sanadorm20)
                            if (not ev_sanadorm20.completed and not ev_sanadorm20.missed) or show_complete:
                                if "(!)" in ev_sanadorm20.hint:
                                    textbutton _("[ev_sanadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm20.hint]")

                            #Life is a Tomato (bar25)
                            if (not ev_bar25.completed and not ev_bar25.missed) or show_complete:
                                if "(!)" in ev_bar25.hint:
                                    textbutton _("[ev_bar25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar25.hint]")

                            #The Girl in the Black Dress (sanadorm25)
                            if (not ev_sanadorm25.completed and not ev_sanadorm25.missed) or show_complete:
                                if "(!)" in ev_sanadorm25.hint:
                                    textbutton _("[ev_sanadorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm25.hint]")

                            #Self-Medication (bar30)
                            if (not ev_bar30.completed and not ev_bar30.missed) or show_complete:
                                if "(!)" in ev_bar30.hint:
                                    textbutton _("[ev_bar30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar30.hint]")

                            #Tortoises and the Concept of Friendship (sanadorm30)
                            if (not ev_sanadorm30.completed and not ev_sanadorm30.missed) or show_complete:
                                if "(!)" in ev_sanadorm30.hint:
                                    textbutton _("[ev_sanadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm30.hint]")

                            text ("")

                            #Purest Intentions (bar35)
                            if (not ev_bar35.completed and not ev_bar35.missed) or show_complete:
                                if "(!)" in ev_bar35.hint:
                                    textbutton _("[ev_bar35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar35.hint]")

                            #Waiting for Anything (sanadorm35)
                            if (not ev_sanadorm35.completed and not ev_sanadorm35.missed) or show_complete:
                                if "(!)" in ev_sanadorm35.hint:
                                    textbutton _("[ev_sanadorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm35.hint]")

                            #Closer to Me (bar40)
                            if (not ev_bar40.completed and not ev_bar40.missed) or show_complete:
                                if "(!)" in ev_bar40.hint:
                                    textbutton _("[ev_bar40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar40.hint]")

                            #The Inside of a Triangle (sanadorm40)
                            if (not ev_sanadorm40.completed and not ev_sanadorm40.missed) or show_complete:
                                if "(!)" in ev_sanadorm40.hint:
                                    textbutton _("[ev_sanadorm40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm40.hint]")

                            #Sweet Vermouth (bar45)
                            if (not ev_bar45.completed and not ev_bar45.missed) or show_complete:
                                if "(!)" in ev_bar45.hint:
                                    textbutton _("[ev_bar45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar45.hint]")

                            #The Complete Absence of Everything (sanadorm45)
                            if (not ev_sanadorm45.completed and not ev_sanadorm45.missed) or show_complete:
                                if "(!)" in ev_sanadorm45.hint:
                                    textbutton _("[ev_sanadorm45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm45.hint]")

                            #Mine (Yours) (sanadorm50)
                            if (not ev_sanadorm50.completed and not ev_sanadorm50.missed) or show_complete:
                                if "(!)" in ev_sanadorm50.hint:
                                    textbutton _("[ev_sanadorm50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanadorm50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanadorm50.hint]")

                            #Melatonin (bar50)
                            if (not ev_bar50.completed and not ev_bar50.missed) or show_complete:
                                if "(!)" in ev_bar50.hint:
                                    textbutton _("[ev_bar50.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar50), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar50.hint]")

                            text ("")

                            #Black Sandy Beaches (bar55)
                            if (not ev_bar55.completed and not ev_bar55.missed) or show_complete:
                                if "(!)" in ev_bar55.hint:
                                    textbutton _("[ev_bar55.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_bar55), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_bar55.hint]")

                            #Ad Meliora (ayanesanabeach2)
                            if (not ev_ayanesanabeach2.completed and not ev_ayanesanabeach2.missed) or show_complete:
                                if "(!)" in ev_ayanesanabeach2.hint:
                                    textbutton _("[ev_ayanesanabeach2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanesanabeach2.hint]")

                            #It Comes to Claim Us All (ayanesanabeach3)
                            if (not ev_ayanesanabeach3.completed and not ev_ayanesanabeach3.missed) or show_complete:
                                if "(!)" in ev_ayanesanabeach3.hint:
                                    textbutton _("[ev_ayanesanabeach3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanesanabeach3.hint]")

                            #Ad Infinitum (ayanesanabeach4)
                            if (not ev_ayanesanabeach4.completed and not ev_ayanesanabeach4.missed) or show_complete:
                                if "(!)" in ev_ayanesanabeach4.hint:
                                    textbutton _("[ev_ayanesanabeach4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ayanesanabeach4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ayanesanabeach4.hint]")

                            text ("")

                            #Taller (sanaspring1)
                            if (not ev_sanaspring1.completed and not ev_sanaspring1.missed) or show_complete:
                                if "(!)" in ev_sanaspring1.hint:
                                    textbutton _("[ev_sanaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring1.hint]")

                            #Stutter-Step (sanaspring2)
                            if (not ev_sanaspring2.completed and not ev_sanaspring2.missed) or show_complete:
                                if "(!)" in ev_sanaspring2.hint:
                                    textbutton _("[ev_sanaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring2.hint]")

                            #Weak Man, Weak Boy (sanaspring3)
                            if (not ev_sanaspring3.completed and not ev_sanaspring3.missed) or show_complete:
                                if "(!)" in ev_sanaspring3.hint:
                                    textbutton _("[ev_sanaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring3.hint]")

                            #Transpacific Sadness Symposium III: TWO-HEADED HORSE (sanaspring4)
                            if (not ev_sanaspring4.completed and not ev_sanaspring4.missed) or show_complete:
                                if "(!)" in ev_sanaspring4.hint:
                                    textbutton _("[ev_sanaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring4.hint]")

                            #Piggy & The Boulder (sanainvite1)
                            if (not ev_sanainvite1.completed and not ev_sanainvite1.missed) or show_complete:
                                if "(!)" in ev_sanainvite1.hint:
                                    textbutton _("[ev_sanainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanainvite1.hint]")

                            #Four Letter Words (sanainvite2)
                            if (not ev_sanainvite2.completed and not ev_sanainvite2.missed) or show_complete:
                                if "(!)" in ev_sanainvite2.hint:
                                    textbutton _("[ev_sanainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanainvite2.hint]")

                            #Despicable Meat Toilet (beachsixsana1)
                            if (not ev_beachsixsana1.completed and not ev_beachsixsana1.missed) or show_complete:
                                if "(!)" in ev_beachsixsana1.hint:
                                    textbutton _("[ev_beachsixsana1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixsana1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixsana1.hint]")

                            #Addict in Training (sanaspring5)
                            if (not ev_sanaspring5.completed and not ev_sanaspring5.missed) or show_complete:
                                if "(!)" in ev_sanaspring5.hint:
                                    textbutton _("[ev_sanaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring5.hint]")

                            #Counting Down From Four (sanaspring6)
                            if (not ev_sanaspring6.completed and not ev_sanaspring6.missed) or show_complete:
                                if "(!)" in ev_sanaspring6.hint:
                                    textbutton _("[ev_sanaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sanaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sanaspring6.hint]")

                    #SARAHINT

                    if showgirl == "Sara":

                        if not _in_replay:

                            #A Woman's Heart (saradate1)
                            if (not ev_saradate1.completed and not ev_saradate1.missed) or show_complete:
                                if "(!)" in ev_saradate1.hint:
                                    textbutton _("[ev_saradate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saradate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saradate1.hint]")

                            #Zero Friction (saralust5)
                            if (not ev_saralust5.completed and not ev_saralust5.missed) or show_complete:
                                if "(!)" in ev_saralust5.hint:
                                    textbutton _("[ev_saralust5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saralust5.hint]")

                            #Third Wheel (sarainvite1)
                            if (not ev_sarainvite1.completed and not ev_sarainvite1.missed) or show_complete:
                                if "(!)" in ev_sarainvite1.hint:
                                    textbutton _("[ev_sarainvite1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarainvite1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarainvite1.hint]")

                            #A Mostly Empty Home (sarainvite2)
                            if (not ev_sarainvite2.completed and not ev_sarainvite2.missed) or show_complete:
                                if "(!)" in ev_sarainvite2.hint:
                                    textbutton _("[ev_sarainvite2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarainvite2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarainvite2.hint]")

                            #Medical Assistance (saralust10)
                            if (not ev_saralust10.completed and not ev_saralust10.missed) or show_complete:
                                if "(!)" in ev_saralust10.hint:
                                    textbutton _("[ev_saralust10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saralust10.hint]")

                            text ("")

                            #Uptown Girl (saradate10)
                            if (not ev_saradate10.completed and not ev_saradate10.missed) or show_complete:
                                if "(!)" in ev_saradate10.hint:
                                    textbutton _("[ev_saradate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saradate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saradate10.hint]")

                            #She's Always a Woman (sarabar20)
                            if (not ev_sarabar20.completed and not ev_sarabar20.missed) or show_complete:
                                if "(!)" in ev_sarabar20.hint:
                                    textbutton _("[ev_sarabar20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarabar20.hint]")

                            #Tell Me When (sarabar25)
                            if (not ev_sarabar25.completed and not ev_sarabar25.missed) or show_complete:
                                if "(!)" in ev_sarabar25.hint:
                                    textbutton _("[ev_sarabar25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarabar25.hint]")

                            #The Place She Falls Asleep At Night (sarabar25p2)
                            if (not ev_sarabar25p2.completed and not ev_sarabar25p2.missed) or show_complete:
                                if "(!)" in ev_sarabar25p2.hint:
                                    textbutton _("[ev_sarabar25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarabar25p2.hint]")

                            #Engulfed (saralust20)
                            if (not ev_saralust20.completed and not ev_saralust20.missed) or show_complete:
                                if "(!)" in ev_saralust20.hint:
                                    textbutton _("[ev_saralust20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saralust20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saralust20.hint]")

                            text ("")

                            #The Creaking of the Seventh Step (saraspecial30p1)
                            if (not ev_saraspecial30p1.completed and not ev_saraspecial30p1.missed) or show_complete:
                                if "(!)" in ev_saraspecial30p1.hint:
                                    textbutton _("[ev_saraspecial30p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspecial30p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspecial30p1.hint]")

                            #Halfway Down the Wishing Well (saraspecial30p2)
                            if (not ev_saraspecial30p2.completed and not ev_saraspecial30p2.missed) or show_complete:
                                if "(!)" in ev_saraspecial30p2.hint:
                                    textbutton _("[ev_saraspecial30p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspecial30p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspecial30p2.hint]")

                            #Nicolas Cage (sarabar30)
                            if (not ev_sarabar30.completed and not ev_sarabar30.missed) or show_complete:
                                if "(!)" in ev_sarabar30.hint:
                                    textbutton _("[ev_sarabar30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_sarabar30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_sarabar30.hint]")

                            text ("")

                            #The One With A Happy Ending (saracamp1)
                            if (not ev_saracamp1.completed and not ev_saracamp1.missed) or show_complete:
                                if "(!)" in ev_saracamp1.hint:
                                    textbutton _("[ev_saracamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saracamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saracamp1.hint]")

                            #I've Been Thinking About Leaving This Place (saracamp2)
                            if (not ev_saracamp2.completed and not ev_saracamp2.missed) or show_complete:
                                if "(!)" in ev_saracamp2.hint:
                                    textbutton _("[ev_saracamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saracamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saracamp2.hint]")

                            #Details in the Fabric (saraspring1)
                            if (not ev_saraspring1.completed and not ev_saraspring1.missed) or show_complete:
                                if "(!)" in ev_saraspring1.hint:
                                    textbutton _("[ev_saraspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring1.hint]")

                            #Silent Night (Onee-san) (saraspring2)
                            if (not ev_saraspring2.completed and not ev_saraspring2.missed) or show_complete:
                                if "(!)" in ev_saraspring2.hint:
                                    textbutton _("[ev_saraspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring2.hint]")

                            #Worthless Me (saraspring3)
                            if (not ev_saraspring3.completed and not ev_saraspring3.missed) or show_complete:
                                if "(!)" in ev_saraspring3.hint:
                                    textbutton _("[ev_saraspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring3.hint]")

                            #Two for the Price of One (saraspring4)
                            if (not ev_saraspring4.completed and not ev_saraspring4.missed) or show_complete:
                                if "(!)" in ev_saraspring4.hint:
                                    textbutton _("[ev_saraspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring4.hint]")

                            #The Puppeteer (saraspring5)
                            if (not ev_saraspring5.completed and not ev_saraspring5.missed) or show_complete:
                                if "(!)" in ev_saraspring5.hint:
                                    textbutton _("[ev_saraspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring5.hint]")

                            #The Most Beautiful Bitter Fruit (saraspring6)
                            if (not ev_saraspring6.completed and not ev_saraspring6.missed) or show_complete:
                                if "(!)" in ev_saraspring6.hint:
                                    textbutton _("[ev_saraspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring6.hint]")

                            #You and I in Unison (saraspring7)
                            if (not ev_saraspring7.completed and not ev_saraspring7.missed) or show_complete:
                                if "(!)" in ev_saraspring7.hint:
                                    textbutton _("[ev_saraspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_saraspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_saraspring7.hint]")

                            #Ring of Fire (dormwarssixsara1)
                            if (not ev_dormwarssixsara1.completed and not ev_dormwarssixsara1.missed) or show_complete:
                                if "(!)" in ev_dormwarssixsara1.hint:
                                    textbutton _("[ev_dormwarssixsara1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_dormwarssixsara1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_dormwarssixsara1.hint]")

                    #TOUKAHINT

                    if showgirl == "Touka":

                        if not _in_replay:

                            #Spontaneous Sentimentality (toukafirsthall)
                            if (not ev_toukafirsthall.completed and not ev_toukafirsthall.missed) or show_complete:
                                if "(!)" in ev_toukafirsthall.hint:
                                    textbutton _("[ev_toukafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukafirsthall.hint]")

                            #Trial Period (toukastreets1)
                            if (not ev_toukastreets1.completed and not ev_toukastreets1.missed) or show_complete:
                                if "(!)" in ev_toukastreets1.hint:
                                    textbutton _("[ev_toukastreets1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukastreets1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukastreets1.hint]")

                            #Fish Out of Water (toukadorm1)
                            if (not ev_toukadorm1.completed and not ev_toukadorm1.missed) or show_complete:
                                if "(!)" in ev_toukadorm1.hint:
                                    textbutton _("[ev_toukadorm1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm1.hint]")

                            #A Brief Moment in Time (toukastreets5)
                            if (not ev_toukastreets5.completed and not ev_toukastreets5.missed) or show_complete:
                                if "(!)" in ev_toukastreets5.hint:
                                    textbutton _("[ev_toukastreets5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukastreets5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukastreets5.hint]")

                            #Loser (toukadorm5)
                            if (not ev_toukadorm5.completed and not ev_toukadorm5.missed) or show_complete:
                                if "(!)" in ev_toukadorm5.hint:
                                    textbutton _("[ev_toukadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm5.hint]")

                            #House Call (toukadorm10)
                            if (not ev_toukadorm10.completed and not ev_toukadorm10.missed) or show_complete:
                                if "(!)" in ev_toukadorm10.hint:
                                    textbutton _("[ev_toukadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm10.hint]")

                            #A Commoner's Tour of Summer (toukaspecial15)
                            if (not ev_toukaspecial15.completed and not ev_toukaspecial15.missed) or show_complete:
                                if "(!)" in ev_toukaspecial15.hint:
                                    textbutton _("[ev_toukaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspecial15.hint]")

                            #Red-ish Light District (toukaspecial15p2)
                            if (not ev_toukaspecial15p2.completed and not ev_toukaspecial15p2.missed) or show_complete:
                                if "(!)" in ev_toukaspecial15p2.hint:
                                    textbutton _("[ev_toukaspecial15p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspecial15p2.hint]")

                            #Something Less Lonely (toukaspecial15p3)
                            if (not ev_toukaspecial15p3.completed and not ev_toukaspecial15p3.missed) or show_complete:
                                if "(!)" in ev_toukaspecial15p3.hint:
                                    textbutton _("[ev_toukaspecial15p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspecial15p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspecial15p3.hint]")

                            text ("")

                            #Kryptonite (toukaarchery20)
                            if (not ev_toukaarchery20.completed and not ev_toukaarchery20.missed) or show_complete:
                                if "(!)" in ev_toukaarchery20.hint:
                                    textbutton _("[ev_toukaarchery20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaarchery20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaarchery20.hint]")

                            #For Want Of (toukadorm25p1)
                            if (not ev_toukadorm25p1.completed and not ev_toukadorm25p1.missed) or show_complete:
                                if "(!)" in ev_toukadorm25p1.hint:
                                    textbutton _("[ev_toukadorm25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm25p1.hint]")

                            #To Lift This Aching Head (toukadorm25p2)
                            if (not ev_toukadorm25p2.completed and not ev_toukadorm25p2.missed) or show_complete:
                                if "(!)" in ev_toukadorm25p2.hint:
                                    textbutton _("[ev_toukadorm25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm25p2.hint]")

                            #Under My Wing (toukadorm25p3)
                            if (not ev_toukadorm25p3.completed and not ev_toukadorm25p3.missed) or show_complete:
                                if "(!)" in ev_toukadorm25p3.hint:
                                    textbutton _("[ev_toukadorm25p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukadorm25p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukadorm25p3.hint]")

                            text ("")

                            #Salt in the Wound (toukacamp1)
                            if (not ev_toukacamp1.completed and not ev_toukacamp1.missed) or show_complete:
                                if "(!)" in ev_toukacamp1.hint:
                                    textbutton _("[ev_toukacamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukacamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukacamp1.hint]")

                            #Blankets & Ball-Gags (toukaspring1)
                            if (not ev_toukaspring1.completed and not ev_toukaspring1.missed) or show_complete:
                                if "(!)" in ev_toukaspring1.hint:
                                    textbutton _("[ev_toukaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring1.hint]")

                            #Artisan Hands (toukaspring2)
                            if (not ev_toukaspring2.completed and not ev_toukaspring2.missed) or show_complete:
                                if "(!)" in ev_toukaspring2.hint:
                                    textbutton _("[ev_toukaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring2.hint]")

                            #One Thousand Penises (toukaspring3)
                            if (not ev_toukaspring3.completed and not ev_toukaspring3.missed) or show_complete:
                                if "(!)" in ev_toukaspring3.hint:
                                    textbutton _("[ev_toukaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring3.hint]")

                            #Come For Me (toukaspring4)
                            if (not ev_toukaspring4.completed and not ev_toukaspring4.missed) or show_complete:
                                if "(!)" in ev_toukaspring4.hint:
                                    textbutton _("[ev_toukaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring4.hint]")

                            #One of the Girls (toukaspring5)
                            if (not ev_toukaspring5.completed and not ev_toukaspring5.missed) or show_complete:
                                if "(!)" in ev_toukaspring5.hint:
                                    textbutton _("[ev_toukaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring5.hint]")

                            #Spermicide (toukaspring6)
                            if (not ev_toukaspring6.completed and not ev_toukaspring6.missed) or show_complete:
                                if "(!)" in ev_toukaspring6.hint:
                                    textbutton _("[ev_toukaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring6.hint]")

                            #The Corpse of Seth Rogen (toukaspring7)
                            if (not ev_toukaspring7.completed and not ev_toukaspring7.missed) or show_complete:
                                if "(!)" in ev_toukaspring7.hint:
                                    textbutton _("[ev_toukaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring7.hint]")

                            #One Step Closer (toukaspring8)
                            if (not ev_toukaspring8.completed and not ev_toukaspring8.missed) or show_complete:
                                if "(!)" in ev_toukaspring8.hint:
                                    textbutton _("[ev_toukaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_toukaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_toukaspring8.hint]")

                    #TSUBASAHINT

                    if showgirl == "Tsubasa":

                        if not _in_replay:

                            #Everbloom (Pride of the Sinful Sort) (tsubasadate1)
                            if (not ev_tsubasadate1.completed and not ev_tsubasadate1.missed) or show_complete:
                                if "(!)" in ev_tsubasadate1.hint:
                                    textbutton _("[ev_tsubasadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasadate1.hint]")

                            #The Deep End (tsubasadate1p2)
                            if (not ev_tsubasadate1p2.completed and not ev_tsubasadate1p2.missed) or show_complete:
                                if "(!)" in ev_tsubasadate1p2.hint:
                                    textbutton _("[ev_tsubasadate1p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate1p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasadate1p2.hint]")

                            text ("")

                            #Heart of Gold (tsubasaspecial15)
                            if (not ev_tsubasaspecial15.completed and not ev_tsubasaspecial15.missed) or show_complete:
                                if "(!)" in ev_tsubasaspecial15.hint:
                                    textbutton _("[ev_tsubasaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspecial15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspecial15.hint]")

                            #Playing God (tsubasadate20)
                            if (not ev_tsubasadate20.completed and not ev_tsubasadate20.missed) or show_complete:
                                if "(!)" in ev_tsubasadate20.hint:
                                    textbutton _("[ev_tsubasadate20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasadate20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasadate20.hint]")

                            #The Lucky Few (tsubasaspecial20)
                            if (not ev_tsubasaspecial20.completed and not ev_tsubasaspecial20.missed) or show_complete:
                                if "(!)" in ev_tsubasaspecial20.hint:
                                    textbutton _("[ev_tsubasaspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspecial20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspecial20.hint]")

                            text ("")

                            #The Bird & The Worm (tsubasaspring1)
                            if (not ev_tsubasaspring1.completed and not ev_tsubasaspring1.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring1.hint:
                                    textbutton _("[ev_tsubasaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring1.hint]")

                            #Petite Sirah (tsubasaspring2)
                            if (not ev_tsubasaspring2.completed and not ev_tsubasaspring2.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring2.hint:
                                    textbutton _("[ev_tsubasaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring2.hint]")

                            #The Pleasures of the Flesh (tsubasaspring3)
                            if (not ev_tsubasaspring3.completed and not ev_tsubasaspring3.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring3.hint:
                                    textbutton _("[ev_tsubasaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring3.hint]")

                            #Yes, Mother (christmastsubasa1)
                            if (not ev_christmastsubasa1.completed and not ev_christmastsubasa1.missed) or show_complete:
                                if "(!)" in ev_christmastsubasa1.hint:
                                    textbutton _("[ev_christmastsubasa1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastsubasa1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmastsubasa1.hint]")

                            #Hands-On Learning (tsubasaspring4)
                            if (not ev_tsubasaspring4.completed and not ev_tsubasaspring4.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring4.hint:
                                    textbutton _("[ev_tsubasaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring4.hint]")

                            #For the Sake of Brevity (tsubasaspring5)
                            if (not ev_tsubasaspring5.completed and not ev_tsubasaspring5.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring5.hint:
                                    textbutton _("[ev_tsubasaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring5.hint]")

                            #When We Dead Awaken (tsubasaspring6)
                            if (not ev_tsubasaspring6.completed and not ev_tsubasaspring6.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring6.hint:
                                    textbutton _("[ev_tsubasaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring6.hint]")

                            #Climbing Up the Ladder (tsubasaspring7)
                            if (not ev_tsubasaspring7.completed and not ev_tsubasaspring7.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring7.hint:
                                    textbutton _("[ev_tsubasaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring7.hint]")

                            #Human Veal (tsubasaspring8)
                            if (not ev_tsubasaspring8.completed and not ev_tsubasaspring8.missed) or show_complete:
                                if "(!)" in ev_tsubasaspring8.hint:
                                    textbutton _("[ev_tsubasaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsubasaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsubasaspring8.hint]")

                    #TSUKASAHINT

                    if showgirl == "Tsukasa":

                        if not _in_replay:

                            #National Tsukasa Day (tsukasaspecial1)
                            if (not ev_tsukasaspecial1.completed and not ev_tsukasaspecial1.missed) or show_complete:
                                if "(!)" in ev_tsukasaspecial1.hint:
                                    textbutton _("[ev_tsukasaspecial1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspecial1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspecial1.hint]")

                            #Jeeves Tsukioka XIII (tsukasaspecial1p2)
                            if (not ev_tsukasaspecial1p2.completed and not ev_tsukasaspecial1p2.missed) or show_complete:
                                if "(!)" in ev_tsukasaspecial1p2.hint:
                                    textbutton _("[ev_tsukasaspecial1p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspecial1p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspecial1p2.hint]")

                            text ("")

                            #Vow of Silence (Pole Position) (tsukasaspring1)
                            if (not ev_tsukasaspring1.completed and not ev_tsukasaspring1.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring1.hint:
                                    textbutton _("[ev_tsukasaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring1.hint]")

                            #Blood & Sunset (tsukasaspring2)
                            if (not ev_tsukasaspring2.completed and not ev_tsukasaspring2.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring2.hint:
                                    textbutton _("[ev_tsukasaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring2.hint]")

                            #Failsafe (tsukasaspring3)
                            if (not ev_tsukasaspring3.completed and not ev_tsukasaspring3.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring3.hint:
                                    textbutton _("[ev_tsukasaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring3.hint]")

                            #A Part of Your World (christmastsukasa1)
                            if (not ev_christmastsukasa1.completed and not ev_christmastsukasa1.missed) or show_complete:
                                if "(!)" in ev_christmastsukasa1.hint:
                                    textbutton _("[ev_christmastsukasa1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_christmastsukasa1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_christmastsukasa1.hint]")

                            #The Talk (tsukasaspring4)
                            if (not ev_tsukasaspring4.completed and not ev_tsukasaspring4.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring4.hint:
                                    textbutton _("[ev_tsukasaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring4.hint]")

                            #Six Inches of Suffering (tsukasaspring5)
                            if (not ev_tsukasaspring5.completed and not ev_tsukasaspring5.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring5.hint:
                                    textbutton _("[ev_tsukasaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring5.hint]")

                            #Useless, Flightless Fledgling (tsukasaspring6)
                            if (not ev_tsukasaspring6.completed and not ev_tsukasaspring6.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring6.hint:
                                    textbutton _("[ev_tsukasaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring6.hint]")

                            #The Gays (tsukasaspring7)
                            if (not ev_tsukasaspring7.completed and not ev_tsukasaspring7.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring7.hint:
                                    textbutton _("[ev_tsukasaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring7.hint]")

                            #To Bury a Body (tsukasaspring8)
                            if (not ev_tsukasaspring8.completed and not ev_tsukasaspring8.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring8.hint:
                                    textbutton _("[ev_tsukasaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring8.hint]")

                            #Simple Moving Average (tsukasaspring9)
                            if (not ev_tsukasaspring9.completed and not ev_tsukasaspring9.missed) or show_complete:
                                if "(!)" in ev_tsukasaspring9.hint:
                                    textbutton _("[ev_tsukasaspring9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsukasaspring9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsukasaspring9.hint]")

                    #TSUNEYOHINT

                    if showgirl == "Tsuneyo":

                        if not _in_replay:

                            #Snake Venom (ramen1)
                            if (not ev_ramen1.completed and not ev_ramen1.missed) or show_complete:
                                if "(!)" in ev_ramen1.hint:
                                    textbutton _("[ev_ramen1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen1.hint]")

                            #The Life of a Blue Whale (tsuneyofirsthall)
                            if (not ev_tsuneyofirsthall.completed and not ev_tsuneyofirsthall.missed) or show_complete:
                                if "(!)" in ev_tsuneyofirsthall.hint:
                                    textbutton _("[ev_tsuneyofirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyofirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyofirsthall.hint]")

                            #Between the Slurps of Pork Broth (ramen5)
                            if (not ev_ramen5.completed and not ev_ramen5.missed) or show_complete:
                                if "(!)" in ev_ramen5.hint:
                                    textbutton _("[ev_ramen5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen5.hint]")

                            #Drug Use & Jump-Rope (tsuneyodorm5)
                            if (not ev_tsuneyodorm5.completed and not ev_tsuneyodorm5.missed) or show_complete:
                                if "(!)" in ev_tsuneyodorm5.hint:
                                    textbutton _("[ev_tsuneyodorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyodorm5.hint]")

                            #A Short List (ramen10)
                            if (not ev_ramen10.completed and not ev_ramen10.missed) or show_complete:
                                if "(!)" in ev_ramen10.hint:
                                    textbutton _("[ev_ramen10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen10.hint]")

                            #The Man Who Loves Nothing (tsuneyodorm10)
                            if (not ev_tsuneyodorm10.completed and not ev_tsuneyodorm10.missed) or show_complete:
                                if "(!)" in ev_tsuneyodorm10.hint:
                                    textbutton _("[ev_tsuneyodorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyodorm10.hint]")

                            text ("")

                            #Seeds (ramen15)
                            if (not ev_ramen15.completed and not ev_ramen15.missed) or show_complete:
                                if "(!)" in ev_ramen15.hint:
                                    textbutton _("[ev_ramen15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen15.hint]")

                            #Moe Fan Service (tsuneyodorm15)
                            if (not ev_tsuneyodorm15.completed and not ev_tsuneyodorm15.missed) or show_complete:
                                if "(!)" in ev_tsuneyodorm15.hint:
                                    textbutton _("[ev_tsuneyodorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyodorm15.hint]")

                            #Fucking...Or What it Means to Live (Shio & Shoyu) (tsuneyodorm20)
                            if (not ev_tsuneyodorm20.completed and not ev_tsuneyodorm20.missed) or show_complete:
                                if "(!)" in ev_tsuneyodorm20.hint:
                                    textbutton _("[ev_tsuneyodorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyodorm20.hint]")

                            #Blackout (ramen20)
                            if (not ev_ramen20.completed and not ev_ramen20.missed) or show_complete:
                                if "(!)" in ev_ramen20.hint:
                                    textbutton _("[ev_ramen20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen20.hint]")

                            #Like Noodles in the Wind (ramen25)
                            if (not ev_ramen25.completed and not ev_ramen25.missed) or show_complete:
                                if "(!)" in ev_ramen25.hint:
                                    textbutton _("[ev_ramen25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen25.hint]")

                            #Green Onions and Contraceptives (ramen25p2)
                            if (not ev_ramen25p2.completed and not ev_ramen25p2.missed) or show_complete:
                                if "(!)" in ev_ramen25p2.hint:
                                    textbutton _("[ev_ramen25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen25p2.hint]")

                            #Unsleeping Aegis (tsuneyodorm25)
                            if (not ev_tsuneyodorm25.completed and not ev_tsuneyodorm25.missed) or show_complete:
                                if "(!)" in ev_tsuneyodorm25.hint:
                                    textbutton _("[ev_tsuneyodorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyodorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyodorm25.hint]")

                            #Things Like Stairs (ramen30)
                            if (not ev_ramen30.completed and not ev_ramen30.missed) or show_complete:
                                if "(!)" in ev_ramen30.hint:
                                    textbutton _("[ev_ramen30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_ramen30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_ramen30.hint]")

                            text ("")

                            #With Her (tsuneyoslumber1)
                            if (not ev_tsuneyoslumber1.completed and not ev_tsuneyoslumber1.missed) or show_complete:
                                if "(!)" in ev_tsuneyoslumber1.hint:
                                    textbutton _("[ev_tsuneyoslumber1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyoslumber1.hint]")

                            #Stripped Away (tsuneyoslumber2)
                            if (not ev_tsuneyoslumber2.completed and not ev_tsuneyoslumber2.missed) or show_complete:
                                if "(!)" in ev_tsuneyoslumber2.hint:
                                    textbutton _("[ev_tsuneyoslumber2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyoslumber2.hint]")

                            #Sudden Light (tsuneyoslumber3)
                            if (not ev_tsuneyoslumber3.completed and not ev_tsuneyoslumber3.missed) or show_complete:
                                if "(!)" in ev_tsuneyoslumber3.hint:
                                    textbutton _("[ev_tsuneyoslumber3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyoslumber3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyoslumber3.hint]")

                            text ("")

                            #Ramen Girl (tsuneyospring1)
                            if (not ev_tsuneyospring1.completed and not ev_tsuneyospring1.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring1.hint:
                                    textbutton _("[ev_tsuneyospring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring1.hint]")

                            #Soothsayer (tsuneyospring2)
                            if (not ev_tsuneyospring2.completed and not ev_tsuneyospring2.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring2.hint:
                                    textbutton _("[ev_tsuneyospring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring2.hint]")

                            #TH15 15NT M3 (tsuneyospring3)
                            if (not ev_tsuneyospring3.completed and not ev_tsuneyospring3.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring3.hint:
                                    textbutton _("[ev_tsuneyospring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring3.hint]")

                            #ELATION PROTOCOL 99: NOODLEFOOT DISCO (halloweentsuneyo1)
                            if (not ev_halloweentsuneyo1.completed and not ev_halloweentsuneyo1.missed) or show_complete:
                                if "(!)" in ev_halloweentsuneyo1.hint:
                                    textbutton _("[ev_halloweentsuneyo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweentsuneyo1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweentsuneyo1.hint]")

                            #Thomas Mato, M.D. (tsuneyospring4)
                            if (not ev_tsuneyospring4.completed and not ev_tsuneyospring4.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring4.hint:
                                    textbutton _("[ev_tsuneyospring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring4.hint]")

                            #Yamato Nadeshiko (tsuneyospring5)
                            if (not ev_tsuneyospring5.completed and not ev_tsuneyospring5.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring5.hint:
                                    textbutton _("[ev_tsuneyospring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring5.hint]")

                            #WORMGOD54 (tsuneyospring6)
                            if (not ev_tsuneyospring6.completed and not ev_tsuneyospring6.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring6.hint:
                                    textbutton _("[ev_tsuneyospring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring6.hint]")

                            #Defilement of a Temple (beachsixtsuneyo1)
                            if (not ev_beachsixtsuneyo1.completed and not ev_beachsixtsuneyo1.missed) or show_complete:
                                if "(!)" in ev_beachsixtsuneyo1.hint:
                                    textbutton _("[ev_beachsixtsuneyo1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixtsuneyo1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixtsuneyo1.hint]")

                            #Denouement (beachsixtsuneyo2)
                            if (not ev_beachsixtsuneyo2.completed and not ev_beachsixtsuneyo2.missed) or show_complete:
                                if "(!)" in ev_beachsixtsuneyo2.hint:
                                    textbutton _("[ev_beachsixtsuneyo2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachsixtsuneyo2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachsixtsuneyo2.hint]")

                            #Shaka-Shaka-HEY (tsuneyospring7)
                            if (not ev_tsuneyospring7.completed and not ev_tsuneyospring7.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring7.hint:
                                    textbutton _("[ev_tsuneyospring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring7.hint]")

                            #Anyone for Any Reason (tsuneyospring8)
                            if (not ev_tsuneyospring8.completed and not ev_tsuneyospring8.missed) or show_complete:
                                if "(!)" in ev_tsuneyospring8.hint:
                                    textbutton _("[ev_tsuneyospring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_tsuneyospring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_tsuneyospring8.hint]")

                    #UTAHINT

                    if showgirl == "Uta":

                        if not _in_replay:

                            #Far From Home (utafirsthall)
                            if (not ev_utafirsthall.completed and not ev_utafirsthall.missed) or show_complete:
                                if "(!)" in ev_utafirsthall.hint:
                                    textbutton _("[ev_utafirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utafirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utafirsthall.hint]")

                            #Abuse of Power (utamaid1)
                            if (not ev_utamaid1.completed and not ev_utamaid1.missed) or show_complete:
                                if "(!)" in ev_utamaid1.hint:
                                    textbutton _("[ev_utamaid1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid1.hint]")

                            #Love Me to Pieces (utamaid5)
                            if (not ev_utamaid5.completed and not ev_utamaid5.missed) or show_complete:
                                if "(!)" in ev_utamaid5.hint:
                                    textbutton _("[ev_utamaid5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid5.hint]")

                            #The VIP Treatment (utadorm5)
                            if (not ev_utadorm5.completed and not ev_utadorm5.missed) or show_complete:
                                if "(!)" in ev_utadorm5.hint:
                                    textbutton _("[ev_utadorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm5.hint]")

                            #Shawshank Redemption (utadorm10)
                            if (not ev_utadorm10.completed and not ev_utadorm10.missed) or show_complete:
                                if "(!)" in ev_utadorm10.hint:
                                    textbutton _("[ev_utadorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm10.hint]")

                            #Happier Things (utamaid10)
                            if (not ev_utamaid10.completed and not ev_utamaid10.missed) or show_complete:
                                if "(!)" in ev_utamaid10.hint:
                                    textbutton _("[ev_utamaid10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid10.hint]")

                            #Facetime With My Mom (Tonight) (utadorm15)
                            if (not ev_utadorm15.completed and not ev_utadorm15.missed) or show_complete:
                                if "(!)" in ev_utadorm15.hint:
                                    textbutton _("[ev_utadorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm15.hint]")

                            #Veins and the Circulatory System (utamaid20)
                            if (not ev_utamaid20.completed and not ev_utamaid20.missed) or show_complete:
                                if "(!)" in ev_utamaid20.hint:
                                    textbutton _("[ev_utamaid20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid20.hint]")

                            #Blood Everywhere (utadorm20)
                            if (not ev_utadorm20.completed and not ev_utadorm20.missed) or show_complete:
                                if "(!)" in ev_utadorm20.hint:
                                    textbutton _("[ev_utadorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm20.hint]")

                            text ("")

                            #Impulse (utaarchery1)
                            if (not ev_utaarchery1.completed and not ev_utaarchery1.missed) or show_complete:
                                if "(!)" in ev_utaarchery1.hint:
                                    textbutton _("[ev_utaarchery1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaarchery1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaarchery1.hint]")

                            #Where Wishes Come True (utamaid25p1)
                            if (not ev_utamaid25p1.completed and not ev_utamaid25p1.missed) or show_complete:
                                if "(!)" in ev_utamaid25p1.hint:
                                    textbutton _("[ev_utamaid25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid25p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid25p1.hint]")

                            #After the Rain (utamaid25p2)
                            if (not ev_utamaid25p2.completed and not ev_utamaid25p2.missed) or show_complete:
                                if "(!)" in ev_utamaid25p2.hint:
                                    textbutton _("[ev_utamaid25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utamaid25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utamaid25p2.hint]")

                            #Uta-chan (utadorm30)
                            if (not ev_utadorm30.completed and not ev_utadorm30.missed) or show_complete:
                                if "(!)" in ev_utadorm30.hint:
                                    textbutton _("[ev_utadorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm30.hint]")

                            #Young & Stupid (utaspecial35)
                            if (not ev_utaspecial35.completed and not ev_utaspecial35.missed) or show_complete:
                                if "(!)" in ev_utaspecial35.hint:
                                    textbutton _("[ev_utaspecial35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspecial35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspecial35.hint]")

                            #Enjo Kousai (utadate35)
                            if (not ev_utadate35.completed and not ev_utadate35.missed) or show_complete:
                                if "(!)" in ev_utadate35.hint:
                                    textbutton _("[ev_utadate35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadate35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadate35.hint]")

                            #Whore (utadorm40p1)
                            if (not ev_utadorm40p1.completed and not ev_utadorm40p1.missed) or show_complete:
                                if "(!)" in ev_utadorm40p1.hint:
                                    textbutton _("[ev_utadorm40p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm40p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm40p1.hint]")

                            #The Girl From Nara (utadorm40p2)
                            if (not ev_utadorm40p2.completed and not ev_utadorm40p2.missed) or show_complete:
                                if "(!)" in ev_utadorm40p2.hint:
                                    textbutton _("[ev_utadorm40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utadorm40p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utadorm40p2.hint]")

                            text ("")

                            #To Be Wanted (utaspring1)
                            if (not ev_utaspring1.completed and not ev_utaspring1.missed) or show_complete:
                                if "(!)" in ev_utaspring1.hint:
                                    textbutton _("[ev_utaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring1.hint]")

                            #Meet Me At Our Spot (utaspring2)
                            if (not ev_utaspring2.completed and not ev_utaspring2.missed) or show_complete:
                                if "(!)" in ev_utaspring2.hint:
                                    textbutton _("[ev_utaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring2.hint]")

                            #Reasons For Rain (beachfive14)
                            if (not ev_beachfive14.completed and not ev_beachfive14.missed) or show_complete:
                                if "(!)" in ev_beachfive14.hint:
                                    textbutton _("[ev_beachfive14.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive14), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive14.hint]")

                            #Songs of Autumn (utaspring3)
                            if (not ev_utaspring3.completed and not ev_utaspring3.missed) or show_complete:
                                if "(!)" in ev_utaspring3.hint:
                                    textbutton _("[ev_utaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring3.hint]")

                            #Heebie-Jeebies (utaspring4)
                            if (not ev_utaspring4.completed and not ev_utaspring4.missed) or show_complete:
                                if "(!)" in ev_utaspring4.hint:
                                    textbutton _("[ev_utaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring4.hint]")

                            #A Thousand Times, Yes (utaspring5)
                            if (not ev_utaspring5.completed and not ev_utaspring5.missed) or show_complete:
                                if "(!)" in ev_utaspring5.hint:
                                    textbutton _("[ev_utaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring5.hint]")

                            #Stolen Valor (utaspring6)
                            if (not ev_utaspring6.completed and not ev_utaspring6.missed) or show_complete:
                                if "(!)" in ev_utaspring6.hint:
                                    textbutton _("[ev_utaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring6.hint]")

                            #ASL (utaspring7)
                            if (not ev_utaspring7.completed and not ev_utaspring7.missed) or show_complete:
                                if "(!)" in ev_utaspring7.hint:
                                    textbutton _("[ev_utaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring7.hint]")

                            #ELATION PROTOCOL 99: DEFINE INTERVENTION (utaspring8)
                            if (not ev_utaspring8.completed and not ev_utaspring8.missed) or show_complete:
                                if "(!)" in ev_utaspring8.hint:
                                    textbutton _("[ev_utaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring8.hint]")

                            #Secret Admirer (utaspring9)
                            if (not ev_utaspring9.completed and not ev_utaspring9.missed) or show_complete:
                                if "(!)" in ev_utaspring9.hint:
                                    textbutton _("[ev_utaspring9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_utaspring9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_utaspring9.hint]")

                    #WAKANAHINT

                    if showgirl == "Wakana":

                        if not _in_replay:

                            #To the River (wakanadate1)
                            if (not ev_wakanadate1.completed and not ev_wakanadate1.missed) or show_complete:
                                if "(!)" in ev_wakanadate1.hint:
                                    textbutton _("[ev_wakanadate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate1.hint]")

                            #Soup, or Another Year With You (wakanadate5)
                            if (not ev_wakanadate5.completed and not ev_wakanadate5.missed) or show_complete:
                                if "(!)" in ev_wakanadate5.hint:
                                    textbutton _("[ev_wakanadate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate5.hint]")

                            text ("")

                            #Pseudonym (wakanadate15)
                            if (not ev_wakanadate15.completed and not ev_wakanadate15.missed) or show_complete:
                                if "(!)" in ev_wakanadate15.hint:
                                    textbutton _("[ev_wakanadate15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate15.hint]")

                            #Don't Hold Back (wakanaspecial15)
                            if (not ev_wakanaspecial15.completed and not ev_wakanaspecial15.missed) or show_complete:
                                if "(!)" in ev_wakanaspecial15.hint:
                                    textbutton _("[ev_wakanaspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspecial15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspecial15.hint]")

                            #The Desk Scene (wakanadate25p1)
                            if (not ev_wakanadate25p1.completed and not ev_wakanadate25p1.missed) or show_complete:
                                if "(!)" in ev_wakanadate25p1.hint:
                                    textbutton _("[ev_wakanadate25p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate25p1.hint]")

                            #Human Error (wakanadate25p2)
                            if (not ev_wakanadate25p2.completed and not ev_wakanadate25p2.missed) or show_complete:
                                if "(!)" in ev_wakanadate25p2.hint:
                                    textbutton _("[ev_wakanadate25p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate25p2.hint]")

                            #Follow My Lead (wakanadate25p3)
                            if (not ev_wakanadate25p3.completed and not ev_wakanadate25p3.missed) or show_complete:
                                if "(!)" in ev_wakanadate25p3.hint:
                                    textbutton _("[ev_wakanadate25p3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanadate25p3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanadate25p3.hint]")

                            text ("")

                            #Enough is Not Enough (wakanaspring1)
                            if (not ev_wakanaspring1.completed and not ev_wakanaspring1.missed) or show_complete:
                                if "(!)" in ev_wakanaspring1.hint:
                                    textbutton _("[ev_wakanaspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring1.hint]")

                            #In the Morning, I'll Forget (wakanaspring2)
                            if (not ev_wakanaspring2.completed and not ev_wakanaspring2.missed) or show_complete:
                                if "(!)" in ev_wakanaspring2.hint:
                                    textbutton _("[ev_wakanaspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring2.hint]")

                            #I'm Wide Awake, It's Morning (wakanaspring3)
                            if (not ev_wakanaspring3.completed and not ev_wakanaspring3.missed) or show_complete:
                                if "(!)" in ev_wakanaspring3.hint:
                                    textbutton _("[ev_wakanaspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring3.hint]")

                            #Dark White (Pretty Joy) (wakanaspring4)
                            if (not ev_wakanaspring4.completed and not ev_wakanaspring4.missed) or show_complete:
                                if "(!)" in ev_wakanaspring4.hint:
                                    textbutton _("[ev_wakanaspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring4.hint]")

                            #Connect the Dots (wakanaspring5)
                            if (not ev_wakanaspring5.completed and not ev_wakanaspring5.missed) or show_complete:
                                if "(!)" in ev_wakanaspring5.hint:
                                    textbutton _("[ev_wakanaspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring5.hint]")

                            #From the Horse’s Mouth (wakanaspring6)
                            if (not ev_wakanaspring6.completed and not ev_wakanaspring6.missed) or show_complete:
                                if "(!)" in ev_wakanaspring6.hint:
                                    textbutton _("[ev_wakanaspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring6.hint]")

                            #Road to Nowhere (wakanaspring7)
                            if (not ev_wakanaspring7.completed and not ev_wakanaspring7.missed) or show_complete:
                                if "(!)" in ev_wakanaspring7.hint:
                                    textbutton _("[ev_wakanaspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring7.hint]")

                            #Dick Wizard (wakanaspring8)
                            if (not ev_wakanaspring8.completed and not ev_wakanaspring8.missed) or show_complete:
                                if "(!)" in ev_wakanaspring8.hint:
                                    textbutton _("[ev_wakanaspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_wakanaspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_wakanaspring8.hint]")

                    #YASUHINT

                    if showgirl == "Yasu":

                        if not _in_replay:

                            #The Hole That Swallowed Everything (yasufirsthall)
                            if (not ev_yasufirsthall.completed and not ev_yasufirsthall.missed) or show_complete:
                                if "(!)" in ev_yasufirsthall.hint:
                                    textbutton _("[ev_yasufirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasufirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasufirsthall.hint]")

                            #Transference (church1)
                            if (not ev_church1.completed and not ev_church1.missed) or show_complete:
                                if "(!)" in ev_church1.hint:
                                    textbutton _("[ev_church1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church1.hint]")

                            #Armor of Older Gods (church5)
                            if (not ev_church5.completed and not ev_church5.missed) or show_complete:
                                if "(!)" in ev_church5.hint:
                                    textbutton _("[ev_church5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church5.hint]")

                            #Repentance (yasudorm10)
                            if (not ev_yasudorm10.completed and not ev_yasudorm10.missed) or show_complete:
                                if "(!)" in ev_yasudorm10.hint:
                                    textbutton _("[ev_yasudorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasudorm10.hint]")

                            #Sakura Season (church10)
                            if (not ev_church10.completed and not ev_church10.missed) or show_complete:
                                if "(!)" in ev_church10.hint:
                                    textbutton _("[ev_church10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church10.hint]")

                            text ("")

                            #Down The Rabbit Hole (church15)
                            if (not ev_church15.completed and not ev_church15.missed) or show_complete:
                                if "(!)" in ev_church15.hint:
                                    textbutton _("[ev_church15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church15.hint]")

                            #Sore Thumb (yasuspecial15)
                            if (not ev_yasuspecial15.completed and not ev_yasuspecial15.missed) or show_complete:
                                if "(!)" in ev_yasuspecial15.hint:
                                    textbutton _("[ev_yasuspecial15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspecial15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspecial15.hint]")

                            #Mother Duck (church20)
                            if (not ev_church20.completed and not ev_church20.missed) or show_complete:
                                if "(!)" in ev_church20.hint:
                                    textbutton _("[ev_church20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church20.hint]")

                            #Glossolalia (yasudorm20)
                            if (not ev_yasudorm20.completed and not ev_yasudorm20.missed) or show_complete:
                                if "(!)" in ev_yasudorm20.hint:
                                    textbutton _("[ev_yasudorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasudorm20.hint]")

                            #The River Styx (yasuspecial20)
                            if (not ev_yasuspecial20.completed and not ev_yasuspecial20.missed) or show_complete:
                                if "(!)" in ev_yasuspecial20.hint:
                                    textbutton _("[ev_yasuspecial20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspecial20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspecial20.hint]")

                            #Frankincense & Myrrh (church25)
                            if (not ev_church25.completed and not ev_church25.missed) or show_complete:
                                if "(!)" in ev_church25.hint:
                                    textbutton _("[ev_church25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_church25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_church25.hint]")

                            #Hand of God (yasudorm25)
                            if (not ev_yasudorm25.completed and not ev_yasudorm25.missed) or show_complete:
                                if "(!)" in ev_yasudorm25.hint:
                                    textbutton _("[ev_yasudorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasudorm25.hint]")

                            #An Apple Each Day (yasudorm30)
                            if (not ev_yasudorm30.completed and not ev_yasudorm30.missed) or show_complete:
                                if "(!)" in ev_yasudorm30.hint:
                                    textbutton _("[ev_yasudorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasudorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasudorm30.hint]")

                            text ("")

                            #Throne of Flesh (yasuspring1)
                            if (not ev_yasuspring1.completed and not ev_yasuspring1.missed) or show_complete:
                                if "(!)" in ev_yasuspring1.hint:
                                    textbutton _("[ev_yasuspring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring1.hint]")

                            #Fruits of Torment (yasuspring2)
                            if (not ev_yasuspring2.completed and not ev_yasuspring2.missed) or show_complete:
                                if "(!)" in ev_yasuspring2.hint:
                                    textbutton _("[ev_yasuspring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring2.hint]")

                            #The Art of Drowning (yasuspring3)
                            if (not ev_yasuspring3.completed and not ev_yasuspring3.missed) or show_complete:
                                if "(!)" in ev_yasuspring3.hint:
                                    textbutton _("[ev_yasuspring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring3.hint]")

                            #Infinity House (halloweenyasu1)
                            if (not ev_halloweenyasu1.completed and not ev_halloweenyasu1.missed) or show_complete:
                                if "(!)" in ev_halloweenyasu1.hint:
                                    textbutton _("[ev_halloweenyasu1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_halloweenyasu1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_halloweenyasu1.hint]")

                            #False Chameleon (yasuspring4)
                            if (not ev_yasuspring4.completed and not ev_yasuspring4.missed) or show_complete:
                                if "(!)" in ev_yasuspring4.hint:
                                    textbutton _("[ev_yasuspring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring4.hint]")

                            #Etinsib Ziwa & The Book of Colors (yasuspring5)
                            if (not ev_yasuspring5.completed and not ev_yasuspring5.missed) or show_complete:
                                if "(!)" in ev_yasuspring5.hint:
                                    textbutton _("[ev_yasuspring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring5.hint]")

                            #Before the Sun Sets (yasuchristmalloween1)
                            if (not ev_yasuchristmalloween1.completed and not ev_yasuchristmalloween1.missed) or show_complete:
                                if "(!)" in ev_yasuchristmalloween1.hint:
                                    textbutton _("[ev_yasuchristmalloween1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuchristmalloween1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuchristmalloween1.hint]")

                            #His Eternal Diary (yasuchristmalloween2)
                            if (not ev_yasuchristmalloween2.completed and not ev_yasuchristmalloween2.missed) or show_complete:
                                if "(!)" in ev_yasuchristmalloween2.hint:
                                    textbutton _("[ev_yasuchristmalloween2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuchristmalloween2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuchristmalloween2.hint]")

                            #Child of Light (yasuspring6)
                            if (not ev_yasuspring6.completed and not ev_yasuspring6.missed) or show_complete:
                                if "(!)" in ev_yasuspring6.hint:
                                    textbutton _("[ev_yasuspring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring6.hint]")

                            #Ichigo Daifuku (yasuspring7)
                            if (not ev_yasuspring7.completed and not ev_yasuspring7.missed) or show_complete:
                                if "(!)" in ev_yasuspring7.hint:
                                    textbutton _("[ev_yasuspring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring7.hint]")

                            #Heretic (yasuspring8)
                            if (not ev_yasuspring8.completed and not ev_yasuspring8.missed) or show_complete:
                                if "(!)" in ev_yasuspring8.hint:
                                    textbutton _("[ev_yasuspring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yasuspring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yasuspring8.hint]")

                    #YUKIHINT

                    if showgirl == "Yuki":

                        if not _in_replay:

                            #Rule #1 (yukidate1)
                            if (not ev_yukidate1.completed and not ev_yukidate1.missed) or show_complete:
                                if "(!)" in ev_yukidate1.hint:
                                    textbutton _("[ev_yukidate1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate1.hint]")

                            #Better Off Alone (yukidate5)
                            if (not ev_yukidate5.completed and not ev_yukidate5.missed) or show_complete:
                                if "(!)" in ev_yukidate5.hint:
                                    textbutton _("[ev_yukidate5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate5.hint]")

                            #Opposite Directions (yukidate10)
                            if (not ev_yukidate10.completed and not ev_yukidate10.missed) or show_complete:
                                if "(!)" in ev_yukidate10.hint:
                                    textbutton _("[ev_yukidate10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate10.hint]")

                            #A Thing of the Past (yukidate10p2)
                            if (not ev_yukidate10p2.completed and not ev_yukidate10p2.missed) or show_complete:
                                if "(!)" in ev_yukidate10p2.hint:
                                    textbutton _("[ev_yukidate10p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate10p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate10p2.hint]")

                            text ("")

                            #Funeral Plans (yukidate20p1)
                            if (not ev_yukidate20p1.completed and not ev_yukidate20p1.missed) or show_complete:
                                if "(!)" in ev_yukidate20p1.hint:
                                    textbutton _("[ev_yukidate20p1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate20p1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate20p1.hint]")

                            #Douchebag McDouchefuck (yukidate20p2)
                            if (not ev_yukidate20p2.completed and not ev_yukidate20p2.missed) or show_complete:
                                if "(!)" in ev_yukidate20p2.hint:
                                    textbutton _("[ev_yukidate20p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate20p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate20p2.hint]")

                            #Pride & Joy (yukidate25)
                            if (not ev_yukidate25.completed and not ev_yukidate25.missed) or show_complete:
                                if "(!)" in ev_yukidate25.hint:
                                    textbutton _("[ev_yukidate25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukidate25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukidate25.hint]")

                            text ("")

                            #Big Dog (yukicamp1)
                            if (not ev_yukicamp1.completed and not ev_yukicamp1.missed) or show_complete:
                                if "(!)" in ev_yukicamp1.hint:
                                    textbutton _("[ev_yukicamp1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukicamp1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukicamp1.hint]")

                            #My Heart is in Rotenburg (yukicamp2)
                            if (not ev_yukicamp2.completed and not ev_yukicamp2.missed) or show_complete:
                                if "(!)" in ev_yukicamp2.hint:
                                    textbutton _("[ev_yukicamp2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukicamp2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukicamp2.hint]")

                            #Small Plastic Baggies (yukispring1)
                            if (not ev_yukispring1.completed and not ev_yukispring1.missed) or show_complete:
                                if "(!)" in ev_yukispring1.hint:
                                    textbutton _("[ev_yukispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring1.hint]")

                            #Better Than Sex (yukispring2)
                            if (not ev_yukispring2.completed and not ev_yukispring2.missed) or show_complete:
                                if "(!)" in ev_yukispring2.hint:
                                    textbutton _("[ev_yukispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring2.hint]")

                            #As the Footsteps Die Out Forever (yukispring3)
                            if (not ev_yukispring3.completed and not ev_yukispring3.missed) or show_complete:
                                if "(!)" in ev_yukispring3.hint:
                                    textbutton _("[ev_yukispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring3.hint]")

                            #Heart of Fear (yukispring4)
                            if (not ev_yukispring4.completed and not ev_yukispring4.missed) or show_complete:
                                if "(!)" in ev_yukispring4.hint:
                                    textbutton _("[ev_yukispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring4.hint]")

                            #When I Say “Jump” (yukispring5)
                            if (not ev_yukispring5.completed and not ev_yukispring5.missed) or show_complete:
                                if "(!)" in ev_yukispring5.hint:
                                    textbutton _("[ev_yukispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring5.hint]")

                            #Bridge Burner (yukispring6)
                            if (not ev_yukispring6.completed and not ev_yukispring6.missed) or show_complete:
                                if "(!)" in ev_yukispring6.hint:
                                    textbutton _("[ev_yukispring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring6.hint]")

                            #Yuki-onna (yukispring7)
                            if (not ev_yukispring7.completed and not ev_yukispring7.missed) or show_complete:
                                if "(!)" in ev_yukispring7.hint:
                                    textbutton _("[ev_yukispring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yukispring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yukispring7.hint]")

                    #YUMIHINT

                    if showgirl == "Yumi":

                        if not _in_replay:

                            #Five Million Dollars (firsttimestreets)
                            if (not ev_firsttimestreets.completed and not ev_firsttimestreets.missed) or show_complete:
                                if "(!)" in ev_firsttimestreets.hint:
                                    textbutton _("[ev_firsttimestreets.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_firsttimestreets), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_firsttimestreets.hint]")

                            #Micropenis (yumifirsthall)
                            if (not ev_yumifirsthall.completed and not ev_yumifirsthall.missed) or show_complete:
                                if "(!)" in ev_yumifirsthall.hint:
                                    textbutton _("[ev_yumifirsthall.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumifirsthall), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumifirsthall.hint]")

                            #Three Second Smile (streets5)
                            if (not ev_streets5.completed and not ev_streets5.missed) or show_complete:
                                if "(!)" in ev_streets5.hint:
                                    textbutton _("[ev_streets5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets5.hint]")

                            #I See You (streets10)
                            if (not ev_streets10.completed and not ev_streets10.missed) or show_complete:
                                if "(!)" in ev_streets10.hint:
                                    textbutton _("[ev_streets10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets10.hint]")

                            #Fuck The Police (yumidorm5)
                            if (not ev_yumidorm5.completed and not ev_yumidorm5.missed) or show_complete:
                                if "(!)" in ev_yumidorm5.hint:
                                    textbutton _("[ev_yumidorm5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm5.hint]")

                            #Yumi Revitalization Project (yumidorm10)
                            if (not ev_yumidorm10.completed and not ev_yumidorm10.missed) or show_complete:
                                if "(!)" in ev_yumidorm10.hint:
                                    textbutton _("[ev_yumidorm10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm10.hint]")

                            #Worse Comes to Worst (yumidorm15)
                            if (not ev_yumidorm15.completed and not ev_yumidorm15.missed) or show_complete:
                                if "(!)" in ev_yumidorm15.hint:
                                    textbutton _("[ev_yumidorm15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm15.hint]")

                            #Apples to Apples (streets15)
                            if (not ev_streets15.completed and not ev_streets15.missed) or show_complete:
                                if "(!)" in ev_streets15.hint:
                                    textbutton _("[ev_streets15.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets15), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets15.hint]")

                            #Token Tsundere (streets20)
                            if (not ev_streets20.completed and not ev_streets20.missed) or show_complete:
                                if "(!)" in ev_streets20.hint:
                                    textbutton _("[ev_streets20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets20.hint]")

                            #Great Expectations (yumidorm20)
                            if (not ev_yumidorm20.completed and not ev_yumidorm20.missed) or show_complete:
                                if "(!)" in ev_yumidorm20.hint:
                                    textbutton _("[ev_yumidorm20.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm20), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm20.hint]")

                            #A Place Like This (streets25)
                            if (not ev_streets25.completed and not ev_streets25.missed) or show_complete:
                                if "(!)" in ev_streets25.hint:
                                    textbutton _("[ev_streets25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets25.hint]")

                            #Caught in the Vortex (yumidorm25)
                            if (not ev_yumidorm25.completed and not ev_yumidorm25.missed) or show_complete:
                                if "(!)" in ev_yumidorm25.hint:
                                    textbutton _("[ev_yumidorm25.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm25), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm25.hint]")

                            text ("")

                            #Where the Sidewalk Ends (streets30)
                            if (not ev_streets30.completed and not ev_streets30.missed) or show_complete:
                                if "(!)" in ev_streets30.hint:
                                    textbutton _("[ev_streets30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets30.hint]")

                            #Walls Too Thick to Hear Through (yumidorm30)
                            if (not ev_yumidorm30.completed and not ev_yumidorm30.missed) or show_complete:
                                if "(!)" in ev_yumidorm30.hint:
                                    textbutton _("[ev_yumidorm30.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm30), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm30.hint]")

                            #Tech Support (yumidorm35)
                            if (not ev_yumidorm35.completed and not ev_yumidorm35.missed) or show_complete:
                                if "(!)" in ev_yumidorm35.hint:
                                    textbutton _("[ev_yumidorm35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumidorm35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumidorm35.hint]")

                            #Abyss (yumicallnight35)
                            if (not ev_yumicallnight35.completed and not ev_yumicallnight35.missed) or show_complete:
                                if "(!)" in ev_yumicallnight35.hint:
                                    textbutton _("[ev_yumicallnight35.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumicallnight35), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumicallnight35.hint]")

                            #Reconciliation (yumispecial40)
                            if (not ev_yumispecial40.completed and not ev_yumispecial40.missed) or show_complete:
                                if "(!)" in ev_yumispecial40.hint:
                                    textbutton _("[ev_yumispecial40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispecial40.hint]")

                            #Neon Heart (If I Close My Eyes) (yumispecial40p2)
                            if (not ev_yumispecial40p2.completed and not ev_yumispecial40p2.missed) or show_complete:
                                if "(!)" in ev_yumispecial40p2.hint:
                                    textbutton _("[ev_yumispecial40p2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial40p2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispecial40p2.hint]")

                            #Unsung Heroes (streets40)
                            if (not ev_streets40.completed and not ev_streets40.missed) or show_complete:
                                if "(!)" in ev_streets40.hint:
                                    textbutton _("[ev_streets40.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_streets40), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_streets40.hint]")

                            #See You Around (yumispecial45)
                            if (not ev_yumispecial45.completed and not ev_yumispecial45.missed) or show_complete:
                                if "(!)" in ev_yumispecial45.hint:
                                    textbutton _("[ev_yumispecial45.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispecial45), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispecial45.hint]")

                            text ("")

                            #Two Months of Nothing (yumislumber1)
                            if (not ev_yumislumber1.completed and not ev_yumislumber1.missed) or show_complete:
                                if "(!)" in ev_yumislumber1.hint:
                                    textbutton _("[ev_yumislumber1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumislumber1.hint]")

                            #Loggerhead (yumislumber2)
                            if (not ev_yumislumber2.completed and not ev_yumislumber2.missed) or show_complete:
                                if "(!)" in ev_yumislumber2.hint:
                                    textbutton _("[ev_yumislumber2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumislumber2.hint]")

                            #A Day in the Life (yumislumber3)
                            if (not ev_yumislumber3.completed and not ev_yumislumber3.missed) or show_complete:
                                if "(!)" in ev_yumislumber3.hint:
                                    textbutton _("[ev_yumislumber3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumislumber3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumislumber3.hint]")

                            text ("")

                            #Kid of the Month (yumispring1)
                            if (not ev_yumispring1.completed and not ev_yumispring1.missed) or show_complete:
                                if "(!)" in ev_yumispring1.hint:
                                    textbutton _("[ev_yumispring1.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring1), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring1.hint]")

                            #Frog Boy (yumispring2)
                            if (not ev_yumispring2.completed and not ev_yumispring2.missed) or show_complete:
                                if "(!)" in ev_yumispring2.hint:
                                    textbutton _("[ev_yumispring2.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring2), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring2.hint]")

                            #Wake Me Up When It's Over (beachfive13)
                            if (not ev_beachfive13.completed and not ev_beachfive13.missed) or show_complete:
                                if "(!)" in ev_beachfive13.hint:
                                    textbutton _("[ev_beachfive13.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_beachfive13), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_beachfive13.hint]")

                            #A Life I Never Wanted (yumispring3)
                            if (not ev_yumispring3.completed and not ev_yumispring3.missed) or show_complete:
                                if "(!)" in ev_yumispring3.hint:
                                    textbutton _("[ev_yumispring3.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring3), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring3.hint]")

                            #Pogonomyrmex Occidentalis Owyheei (yumispring4)
                            if (not ev_yumispring4.completed and not ev_yumispring4.missed) or show_complete:
                                if "(!)" in ev_yumispring4.hint:
                                    textbutton _("[ev_yumispring4.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring4), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring4.hint]")

                            #The Dragon (yumispring5)
                            if (not ev_yumispring5.completed and not ev_yumispring5.missed) or show_complete:
                                if "(!)" in ev_yumispring5.hint:
                                    textbutton _("[ev_yumispring5.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring5), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring5.hint]")

                            #Ittekimasu (yumispring6)
                            if (not ev_yumispring6.completed and not ev_yumispring6.missed) or show_complete:
                                if "(!)" in ev_yumispring6.hint:
                                    textbutton _("[ev_yumispring6.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring6), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring6.hint]")

                            #Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS (yumispring7)
                            if (not ev_yumispring7.completed and not ev_yumispring7.missed) or show_complete:
                                if "(!)" in ev_yumispring7.hint:
                                    textbutton _("[ev_yumispring7.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring7), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring7.hint]")

                            #Death With Dignity (yumispring8)
                            if (not ev_yumispring8.completed and not ev_yumispring8.missed) or show_complete:
                                if "(!)" in ev_yumispring8.hint:
                                    textbutton _("[ev_yumispring8.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring8), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring8.hint]")

                            #Scar Tissue (yumispring9)
                            if (not ev_yumispring9.completed and not ev_yumispring9.missed) or show_complete:
                                if "(!)" in ev_yumispring9.hint:
                                    textbutton _("[ev_yumispring9.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring9), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring9.hint]")

                            #Chabudai (Plastic Corpses) (yumispring10)
                            if (not ev_yumispring10.completed and not ev_yumispring10.missed) or show_complete:
                                if "(!)" in ev_yumispring10.hint:
                                    textbutton _("[ev_yumispring10.hint]") action [ShowMenu("explanations"), SetVariable("explain_event", ev_yumispring10), SetVariable("previous_screen", "girls")] style "event_button" text_style "mod"
                                else:
                                    text ("[ev_yumispring10.hint]")

        vbox: #box for the Back button
            ypos 20
            hbox:
                if dark_mode:
                    textbutton _("Back") action ShowMenu("progressmod_dark")
                else:
                    textbutton _("Back") action ShowMenu("progressmod")
                textbutton _("       Toggle Completed Events") action SetVariable("show_complete", not show_complete)
                textbutton _("       Toggle Completed Girls") action SetVariable("show_completed_girls", not show_completed_girls)
                if show_hints:
                    textbutton _("       Hints") action ShowMenu("hinttracker")
                textbutton _("       Profile") action ShowMenu("gamemenu" + showgirl.lower())
