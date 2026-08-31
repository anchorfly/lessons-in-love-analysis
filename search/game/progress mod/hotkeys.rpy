screen overlay_scr:

    zorder 100

    key "e" action ShowMenu("explaintracker")
    key "g" action ShowMenu("amitrackerm2")
    if current_chapter == 1:
        key "m" action ShowMenu("maintrackerch1m")
    if current_chapter == 2:
        key "m" action ShowMenu("maintrackerch2m")
    if current_chapter == 3:
        key "m" action ShowMenu("maintrackerch3m")
    if current_chapter == 4:
        key "m" action ShowMenu("maintrackerch4m")
    key "n" action ShowMenu("hinttracker")
    key "o" action ShowMenu("mod_options")
    if dark_mode:
        key "p" action ShowMenu("progressmod_dark")
    else:
        key "p" action ShowMenu("progressmod")
    key "t" action SetVariable("show_complete", not show_complete)
    key "u" action SetVariable("ProgressMod.last_events", 0)
    key "c" action SetVariable("show_completed_girls", not show_completed_girls)

    # vbox:
    #     text ("Hotkeys active") style "mod"