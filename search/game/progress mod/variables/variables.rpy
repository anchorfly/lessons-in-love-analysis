################################################################################
## Variables
################################################################################

init python:

    show_complete = True                    # whether completed events should be shown on the event trackers
    show_hints = True                       # whether hints should be shown
    show_happy_hints = True
    show_next = False
    show_completed_girls = True             # whether icons for girls with no uncompleted events should be shown
    desaturate_girls = False                # whether icons for girls without hints should be desaturated
    show_exclam = False                     # whether exclamation points should be shown for girls without hints
    show_dlc = True
    dark_mode = False
    showgirl = "Sana"                       # default girl to be shown when opening the girls event tracker
    girls_shown = 0
    max_chapter = 1

    # Colors for each girl

    amicolor = "#ff4dd2"
    ayanecolor = "#00bab1"
    chikacolor = "#AF7F00"
    chinamicolor = "#FF9999"
    futabacolor = "#9326ff"
    harukacolor = "#B02E8C"
    imanicolor = "#80C9DC"
    iocolor = "#BBE3A1"
    kaoricolor = "#4B4B4B"
    karincolor = "#AC9D77"
    kirincolor = "#9C8080"
    makicolor = "#3B84A9"
    makotocolor = "#3c55fa"
    mayacolor = "#18b500"
    mikucolor = "#ff8112"
    mollycolor = "#4FCB80"
    naocolor = "#602F2B"
    nikicolor = "#FF0074"
    nodokacolor = "#AF89A2"
    norikocolor = "#FF61A9"
    osakocolor = "#9A6BA1"
    otohacolor = "#B83A6A"
    rikacolor = "#D18E77"
    rincolor = "#a30041"
    sanacolor = "#005730"
    saracolor = "#365D4C"
    toukacolor = "#F0E68C"
    tsubasacolor = "#eae6aa"
    tsukasacolor = "#f0ca8c"
    tsuneyocolor = "#C8B330"
    utacolor = "#AA4588"
    wakanacolor = "#540087"
    yasucolor = "#74d9e9"
    yukicolor = "#CDCDCD"
    yumicolor = "#d12e2e"

    # Girl objects
    # Name, color, day in dorm hallway, work event name 1, work event name 2 (if any)

    Ami = Girl("Ami", amicolor, "Friday", "her room", work2 = "the maid cafe (morning)")
    Ayane = Girl("Ayane", ayanecolor, "Thursday", "the dojo")
    Chika = Girl("Chika", chikacolor, "Wednesday", "the shopping mall", work2 = "the maid cafe (afternoon)")
    Chinami = Girl("Chinami", chinamicolor, "N/A", "N/A")
    Futaba = Girl("Futaba", futabacolor, "Tuesday", "the library (morning)")
    Haruka = Girl("Haruka", harukacolor, "N/A", "the cafe (morning)")
    Imani = Girl("Imani", imanicolor, "N/A", "N/A")
    Io = Girl("Io", iocolor, "Tuesday", "the bathhouse", work2 = "the archery range")
    Kaori = Girl("Kaori", kaoricolor, "N/A", "the streets (evening)")
    Karin = Girl("Karin", karincolor, "N/A", "the soccer field")
    Kirin = Girl("Kirin", kirincolor, "Thursday", "the soccer field", work2 = "the archery range")
    Maki = Girl("Maki", makicolor, "N/A", "the porn shop")
    Makoto = Girl("Makoto", makotocolor, "Thursday", "the porn shop")
    Maya = Girl("Maya", mayacolor, "Monday", "the shrine")
    Miku = Girl("Miku", mikucolor, "Tuesday", "the soccer field", work2 = "the pool")
    Molly = Girl("Molly", mollycolor, "Monday", "the cafe (night)")
    Nao = Girl("Nao", naocolor, "N/A", "N/A")
    Niki = Girl("Niki", nikicolor, "N/A", "N/A")
    Nodoka = Girl("Nodoka", nodokacolor, "Friday", "the library (afternoon)")
    Noriko = Girl("Noriko", norikocolor, "Wednesday", "the convenience store")
    Osako = Girl("Osako", osakocolor, "N/A", "the dojo")
    Otoha = Girl("Otoha", otohacolor, "Monday", "the park")
    Rika = Girl("Rika", rikacolor, "N/A", "the dive bar")
    Rin = Girl("Rin", rincolor, "Wednesday", "the cafe (morning)")
    Sana = Girl("Sana", sanacolor, "Friday", "the bar")
    Sara = Girl("Sara", saracolor, "N/A", "the bar")
    Touka = Girl("Touka", toukacolor, "Tuesday", "the streets (morning)", work2 = "the archery range")
    Tsubasa = Girl("Tsubasa", tsubasacolor, "N/A", "N/A")
    Tsukasa = Girl("Tsukasa", tsukasacolor, "N/A", "N/A")
    Tsuneyo = Girl("Tsuneyo", tsuneyocolor, "Wednesday", "the ramen shop", work2 = "the archery range (afternoon)")
    Uta = Girl("Uta", utacolor, "Friday", "the maid cafe (evening)", work2 = "the archery range")
    Wakana = Girl("Wakana", wakanacolor, "N/A", "N/A")
    Yasu = Girl("Yasu", yasucolor, "Thursday", "the church")
    Yuki = Girl("Yuki", yukicolor, "N/A", "the bar")
    Yumi = Girl("Yumi", yumicolor, "Monday", "the streets (afternoon)", work2 = "the pond")

    # hall day, work day
    girl_days = dict()

    # StoryEvent objects
    # Name, color

    MainEvent = StoryEvent("Main event", "#000000")
    HappyEvent = StoryEvent("Happy event", "#000000")

    # Creates list of all Girl objects

    girls_list = [Ami, Ayane, Chika, Chinami, Futaba, Haruka, Imani, Io, Kaori, Karin, Kirin, Maki, Makoto, Maya, Miku, Molly, Nao, Niki, Nodoka, Noriko, Osako, Otoha, Rika, Rin, Sana, Sara, Touka, Tsubasa, Tsukasa, Tsuneyo, Uta, Wakana, Yasu, Yuki, Yumi]

    # Creates list of days of the week (redundant due to built in Python method, but including "Null" means the numbering matches that of the game)

    days_of_the_week = ["Null", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Current chapter (default)
    current_chapter = 1

    # Temp variables (to be removed when/if Selebus adds them to the game)

    chinamimiss = 0
    iomiss = 0
    kaorimiss = 0
    mikumiss = 0
    mollymiss = 0
    naomiss = 0
    nikimiss = 0
    norikomiss = 0
    osakomiss = 0
    otohamiss = 0
    toukamiss = 0
    tsubasamiss = 0
    tsukasamiss = 0
    tsukasapoint = 0
    tsuneyomiss = 0
    utamiss = 0
    wakanamiss = 0
    yasumiss = 0
    yukimiss = 0
    yumimiss = 0

    chinami_lust = "N/A"
    imani_lust = "N/A"
    io_lust = "N/A"
    kaori_lust = "N/A"
    karin_lust = "N/A"
    maya_lust = "N/A"
    molly_lust = "N/A"
    nao_lust = "N/A"
    nodoka_lust = "N/A"
    osako_lust = "N/A"
    otoha_lust = "N/A"
    rika_lust = "N/A"
    rin_lust = "N/A"
    sana_lust = "N/A"
    touka_lust = "N/A"
    tsubasa_lust = "N/A"
    tsukasa_lust = "N/A"
    tsuneyo_lust = "N/A"
    uta_lust = "N/A"
    wakana_lust = "N/A"
    yasu_lust = "N/A"
    yuki_lust = "N/A"
    yumi_lust = "N/A"
    karinspring7miss = False

init 3 python:
    ProgressMod = LiLMod()
    config.after_replay_callback = ProgressMod.update_all
    explain_event = ev_amidorm10
    previous_screen = ""