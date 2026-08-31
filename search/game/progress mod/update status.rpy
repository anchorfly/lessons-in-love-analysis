# functions used by progress_screens.rpy

init python:

    # function used on progressmod screen to determine placement
    def count_girls_shown():

        shown = 0
        for g in girls_list:
            if g.active:
                shown = shown + 1
        return shown

    # function to determine values needed for the events column on progress screen
    def update_chapter_values():

        globals()["max_chapter"] = len(chapter_finals)
        for i in range(max_chapter):
            if eval(chapter_finals[i].var_name):
                globals()["current_chapter"] = i + 2
                if globals()["current_chapter"] > max_chapter:
                    globals()["current_chapter"] = max_chapter

        for current_girl in ProgressMod.all_girls:
            current_girl.current_max = current_girl.max[current_chapter]
        for current_girl in [MainEvent, HappyEvent]:
            current_girl.points = current_girl.max[current_chapter-1]
            for current_event in current_girl.event_list:
                if current_event.chapter == current_chapter:
                    if current_event.completed:
                        current_girl.points = current_girl.points + 1

    # function to determine when girls start being listed on the progress screen
    def activate_girls():

        for current_girl in girls_list:
            current_girl.active = False
        Ami.active = True
        Ayane.active = True
        Chika.active = True
        Futaba.active = True
        Makoto.active = True
        Maya.active = True
        Miku.active = True
        Rin.active = True
        Sana.active = True
        Yumi.active = True
        if day89:
            Haruka.active = True
        if day114:
            Kaori.active = True
        if soccer20:
            Karin.active = True
            Kirin.active = True
        if mall20:
            Chinami.active = True
        if day154:
            Maki.active = True
            Molly.active = True
            Tsuneyo.active = True
        if day247:
            Io.active = True
            Uta.active = True
        if bathhouse5:
            Yuki.active = True
        if day269:
            Noriko.active = True
        if day271:
            Niki.active = True
        if day288:
            Nodoka.active = True
            Otoha.active = True
        if day333part2:
            Wakana.active = True
        if osakodate1:
            Osako.active = True
        if bar15:
            Sara.active = True
        if day304:
            Touka.active = True
            Yasu.active = True
        if toukaspecial15p3:
            Tsubasa.active = True
        if wakanaspecial15:
            Imani.active = True
        if iospecial30 and karindate25:
            Tsukasa.active = True
        if nodokaspecial30p4:
            Rika.active = True
        if predormwars3:
            Nao.active = True