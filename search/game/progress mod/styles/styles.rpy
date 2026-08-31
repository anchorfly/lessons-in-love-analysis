################################################################################
## Styles
################################################################################

# Mod Options Screen

style optionbutton:
    size 26
    font "YuGothM.ttc"
    hover_color "#FF00F7"
    padding (0, 0)
    margin(0, 0)

style explanation:
    size 22
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)

# Event Trackers

style modmybutton:
    size 24
    font "YuGothM.ttc"
    color "#00C803"
    hover_color "#FF00F7"
    padding (0, 0)
    margin(0, 0)

style tracker_button:
    size 24
    font "YuGothM.ttc"
    color "#00C803"
    hover_color "#FF00F7"
    padding (0, 0)
    margin(0, 0)

style tracker_text:
    size 24
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)

# hinttracker.rpy

style hint_text:
    size 22
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)

# Progress Screen

style exclam_text:
    size 24
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)

style mod:
    size 23
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)

# Same as the style "mod", but with an "invisible" outline the same color as the background
# Needed for using textbuttons with the girls whose names are outlined
# (Renpy doesn't allow style changes within a single line of text, but it does allow outline color changes)

style invisibleoutline:
    size 28
    font "YuGothM.ttc"
    outlines [(absolute(1), "#f2eff0", absolute(0), absolute(0))]

# Same as the style "aff", but with an "invisible" outline the same color as the background
# Needed for using textbuttons with the girls whose names are outlined
# (Renpy doesn't allow style changes within a single line of text, but it does allow outline color changes)

style affoutline:
    size 35
    font "YuGothM.ttc"
    outlines [(absolute(2), "#f2eff0", absolute(0), absolute(0))]

# Styles for each girl 
# Each is the style "mod" with that girl's color; those ending in "outline" have a darker outline to aid legibility

style amimod:
    size 23
    font "YuGothM.ttc"
    color "#ff4dd2"

style amihint:
    size 22
    font "YuGothM.ttc"
    color "#ff4dd2"

style ayanemod:
    size 23
    font "YuGothM.ttc"
    color "#00bab1" 

style ayanehint:
    size 22
    font "YuGothM.ttc"
    color "#00bab1" 

style chikamod:
    size 23
    font "YuGothM.ttc"
    color "#AF7F00"

style chikahint:
    size 22
    font "YuGothM.ttc"
    color "#AF7F00"

style chinamimod:
    size 23
    font "YuGothM.ttc"
    color "#FF9999"

style chinamihint:
    size 22
    font "YuGothM.ttc"
    color "#FF9999"

style futabamod:
    size 23
    font "YuGothM.ttc"
    color "#9324ff"

style futabahint:
    size 22
    font "YuGothM.ttc"
    color "#9324ff"

style harukamod:
    size 23
    font "YuGothM.ttc"
    color "#B02E8C"

style harukahint:
    size 22
    font "YuGothM.ttc"
    color "#B02E8C"

style imanihint:
    size 22
    font "YuGothM.ttc"
    color "#80C9DC"

style imanimod:
    size 23
    font "YuGothM.ttc"
    color "#80C9DC"

style iooutline:
    size 23
    font "YuGothM.ttc"
    color "#BBE3A1"
    outlines [(absolute(1), "#a8cc91", absolute(0), absolute(0))]

style iomod:
    size 23
    font "YuGothM.ttc"
    color "#BBE3A1"
    outlines [(absolute(1), "#a8cc91", absolute(0), absolute(0))]

style iomod_dark:
    size 23
    font "YuGothM.ttc"
    color "#BBE3A1"

style iohint:
    size 22
    font "YuGothM.ttc"
    color "#BBE3A1"
    outlines [(absolute(1), "#a8cc91", absolute(0), absolute(0))]

style kaorimod:
    size 23
    font "YuGothM.ttc"
    color "#4B4B4B"

style kaorihint:
    size 22
    font "YuGothM.ttc"
    color "#4B4B4B"

style karinmod:
    size 23
    font "YuGothM.ttc"
    color "#AC9D77"

style karinhint:
    size 22
    font "YuGothM.ttc"
    color "#AC9D77"

style kirinmod:
    size 23
    font "YuGothM.ttc"
    color "#9C8080"

style kirinhint:
    size 22
    font "YuGothM.ttc"
    color "#9C8080"

style makimod:
    size 23
    font "YuGothM.ttc"
    color "#3B84A9"

style makihint:
    size 22
    font "YuGothM.ttc"
    color "#3B84A9"

style makotomod:
    size 23
    font "YuGothM.ttc"
    color "#3c55fa"

style makotohint:
    size 22
    font "YuGothM.ttc"
    color "#3c55fa"

style mayamod:
    size 23
    font "YuGothM.ttc"
    color "#18b500"

style mayahint:
    size 22
    font "YuGothM.ttc"
    color "#18b500"

style mikumod:
    size 23
    font "YuGothM.ttc"
    color "#ff8112"

style mikuhint:
    size 22
    font "YuGothM.ttc"
    color "#ff8112"

style mollymod:
    size 23
    font "YuGothM.ttc"
    color "#4FCB80"

style mollyhint:
    size 22
    font "YuGothM.ttc"
    color "#4FCB80"

style naomod:
    size 23
    font "YuGothM.ttc"
    color "#602F2B"

style naohint:
    size 22
    font "YuGothM.ttc"
    color "#602F2B"

style nikimod:
    size 23
    font "YuGothM.ttc"
    color "#FF0074"

style nikihint:
    size 22
    font "YuGothM.ttc"
    color "#FF0074"

style nodokamod:
    size 23
    font "YuGothM.ttc"
    color "#AF89A2"

style nodokahint:
    size 22
    font "YuGothM.ttc"
    color "#AF89A2"

style norikomod:
    size 23
    font "YuGothM.ttc"
    color "#FF61A9"

style norikohint:
    size 22
    font "YuGothM.ttc"
    color "#FF61A9"

style osakomod:
    size 23
    font "YuGothM.ttc"
    color "#9A6BA1"

style osakohint:
    size 22
    font "YuGothM.ttc"
    color "#9A6BA1"

style otohamod:
    size 23
    font "YuGothM.ttc"
    color "#B83A6A" 

style otohahint:
    size 22
    font "YuGothM.ttc"
    color "#B83A6A" 

style rikamod:
    size 23
    font "YuGothM.ttc"
    color "#D18E77"

style rikahint:
    size 22
    font "YuGothM.ttc"
    color "#D18E77"

style rinmod:
    size 23
    font "YuGothM.ttc"
    color "#a30041"

style rinhint:
    size 22
    font "YuGothM.ttc"
    color "#a30041"

style sanamod:
    size 23
    font "YuGothM.ttc"
    color "#005730"

style sanahint:
    size 22
    font "YuGothM.ttc"
    color "#005730"

style saramod:
    size 23
    font "YuGothM.ttc"
    color "#365D4C"

style sarahint:
    size 22
    font "YuGothM.ttc"
    color "#365D4C"

style blankexclam:
    size 23
    font "YuGothM.ttc"
    color "#f2eff0"
    outlines [(absolute(1), "#f2eff0", absolute(0), absolute(0))]

style toukaoutline:
    size 23
    font "YuGothM.ttc"
    color "#F0E68C"
    outlines [(absolute(1), "#d8cf7e", absolute(0), absolute(0))]

style toukamod:
    size 23
    font "YuGothM.ttc"
    color "#F0E68C"
    outlines [(absolute(1), "#d8cf7e", absolute(0), absolute(0))]

style toukamod_dark:
    size 23
    font "YuGothM.ttc"
    color "#F0E68C"

style toukahint:
    size 22
    font "YuGothM.ttc"
    color "#F0E68C"
    outlines [(absolute(1), "#d8cf7e", absolute(0), absolute(0))]

style tsubasamod:
    size 23
    font "YuGothM.ttc"
    color "#eae6aa"
    outlines [(absolute(1), "#f0ca8c", absolute(0), absolute(0))]

style tsubasamod_dark:
    size 23
    font "YuGothM.ttc"
    color "#eae6aa"

style tsubasahint:
    size 22
    font "YuGothM.ttc"
    color "#eae6aa"
    outlines [(absolute(1), "#f0ca8c", absolute(0), absolute(0))]

style tsukasamod:
    size 23
    font "YuGothM.ttc"
    color "#f0ca8c"

style tsukasahint:
    size 22
    font "YuGothM.ttc"
    color "#f0ca8c"

style tsuneyomod:
    size 23
    font "YuGothM.ttc"
    color "#C8B330"

style tsuneyohint:
    size 22
    font "YuGothM.ttc"
    color "#C8B330"

style utamod:
    size 23
    font "YuGothM.ttc"
    color "#AA4588"

style utahint:
    size 22
    font "YuGothM.ttc"
    color "#AA4588"

style wakanamod:
    size 23
    font "YuGothM.ttc"
    color "#540087"

style wakanahint:
    size 22
    font "YuGothM.ttc"
    color "#540087"

style yasumod:
    size 23
    font "YuGothM.ttc"
    color "#74d9e9"

style yasuhint:
    size 22
    font "YuGothM.ttc"
    color "#74d9e9"

style yukioutline:
    size 23
    font "YuGothM.ttc"
    color "#CDCDCD"
    outlines [(absolute(1), "#a4a4a4", absolute(0), absolute(0))]

style yukimod:
    size 23
    font "YuGothM.ttc"
    color "#CDCDCD"
    outlines [(absolute(1), "#a4a4a4", absolute(0), absolute(0))]

style yukimod_dark:
    size 23
    font "YuGothM.ttc"
    color "#CDCDCD"

style yukihint:
    size 22
    font "YuGothM.ttc"
    color "#CDCDCD"
    outlines [(absolute(1), "#a4a4a4", absolute(0), absolute(0))]

style yumimod:
    size 23
    font "YuGothM.ttc"
    color "#d12e2e" 

style yumihint:
    size 22
    font "YuGothM.ttc"
    color "#d12e2e" 