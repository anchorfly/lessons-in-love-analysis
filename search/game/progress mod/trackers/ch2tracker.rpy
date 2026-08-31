screen maintrackerch2m():

    tag menu

    use game_menu(_("Chapter 2"), scroll="viewport"):

        null

    key "m" action Return()

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    $ if show_complete: ch2_scroll = (MainEvent.max[2] - MainEvent.max[1]) * 26
    $ if not show_complete: ch2_scroll = (MainEvent.max[2] - (MainEvent.max[1] + chap2point)) * 26

    vbox:
        xpos .25
        ypos 35
        area (0,0,1450,930)

        vbox:
            ypos 40
            hbox:
                vbox:
                    textbutton _("<") action ShowMenu("maintrackerch1m")
                vbox:
                    textbutton _(">") action ShowMenu("maintrackerch3m")

        viewport:
            ypos 35
            area (0,0,1450,870)
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            child_size (None,ch2_scroll)

            vbox:
                style_prefix "tracker"

                if christmas1 and show_complete:
                    textbutton _("Snow-Covered Footprints {b}✓{/b}") action Replay("christmas1", locked=False) text_style "modmybutton"
                elif not christmas1 and not ev_christmas1.missed:
                    text _("Snow-Covered Footprints")
                if christmas2 and show_complete:
                    textbutton _("Patent-Pending {b}✓{/b}") action Replay("christmas2", locked=False) text_style "modmybutton"
                elif not christmas2 and not ev_christmas2.missed:
                    text _("Patent-Pending")
                if christmas3 and show_complete:
                    textbutton _("Fuck Christmas {b}✓{/b}") action Replay("christmas3", locked=False) text_style "modmybutton"
                elif not christmas3 and not ev_christmas3.missed:
                    text _("Fuck Christmas")
                if christmas4 and show_complete:
                    textbutton _("Disappointing Everyone {b}✓{/b}") action Replay("christmas4", locked=False) text_style "modmybutton"
                elif not christmas4 and not ev_christmas4.missed:
                    text _("Disappointing Everyone")
                if christmas5 and show_complete:
                    textbutton _("Bottled Dreams {b}✓{/b}") action Replay("christmas5", locked=False) text_style "modmybutton"
                elif not christmas5 and not ev_christmas5.missed:
                    text _("Bottled Dreams")
                if christmas6 and show_complete:
                    textbutton _("Christmas Miracle {b}✓{/b}") action Replay("christmas6", locked=False) text_style "modmybutton"
                elif not christmas6 and not ev_christmas6.missed:
                    text _("Christmas Miracle")
                if christmas7 and show_complete:
                    textbutton _("Fireworks, Chicken, and the Innate Fear of Death {b}✓{/b}") action Replay("christmas7", locked=False) text_style "modmybutton"
                elif not christmas7 and not ev_christmas7.missed:
                    text _("Fireworks, Chicken, and the Innate Fear of Death")
                if day237 and show_complete:
                    textbutton _("Suicide Pact {b}✓{/b}") action Replay("day237", locked=False) text_style "modmybutton"
                elif not day237 and not ev_day237.missed:
                    text _("Suicide Pact")
                if day239 and show_complete:
                    textbutton _("A Door that People Move Through {b}✓{/b}") action Replay("day239", locked=False) text_style "modmybutton"
                elif not day239 and not ev_day239.missed:
                    text _("A Door that People Move Through")
                if day240 and show_complete:
                    textbutton _("Uta's Last Stand {b}✓{/b}") action Replay("day240", locked=False) text_style "modmybutton"
                elif not day240 and not ev_day240.missed:
                    text _("Uta's Last Stand")
                if day244 and show_complete:
                    textbutton _("Opposites Attract {b}✓{/b}") action Replay("day244", locked=False) text_style "modmybutton"
                elif not day244 and not ev_day244.missed:
                    text _("Opposites Attract")
                if day246 and show_complete:
                    textbutton _("All Kinds of People, All Kinds of Things {b}✓{/b}") action Replay("day246", locked=False) text_style "modmybutton"
                elif not day246 and not ev_day246.missed:
                    text _("All Kinds of People, All Kinds of Things")
                if day247 and show_complete:
                    textbutton _("Caterpillar {b}✓{/b}") action Replay("day247", locked=False) text_style "modmybutton"
                elif not day247 and not ev_day247.missed:
                    text _("Caterpillar")
                if day261 and show_complete:
                    textbutton _("Let Me Die in Spring {b}✓{/b}") action Replay("day261", locked=False) text_style "modmybutton"
                elif not day261 and not ev_day261.missed:
                    text _("Let Me Die in Spring")
                if day263 and show_complete:
                    textbutton _("There's Always a Chance {b}✓{/b}") action Replay("day263", locked=False) text_style "modmybutton"
                elif not day263 and not ev_day263.missed:
                    text _("There's Always a Chance")
                if day264 and show_complete:
                    textbutton _("Forty Degrees Below Zero {b}✓{/b}") action Replay("day264", locked=False) text_style "modmybutton"
                elif not day264 and not ev_day264.missed:
                    text _("Forty Degrees Below Zero")
                if day269 and show_complete:
                    textbutton _("What Could Have Been {b}✓{/b}") action Replay("day269", locked=False) text_style "modmybutton"
                elif not day269 and not ev_day269.missed:
                    text _("What Could Have Been")
                if day270 and show_complete:
                    textbutton _("What Is {b}✓{/b}") action Replay("day270", locked=False) text_style "modmybutton"
                elif not day270 and not ev_day270.missed:
                    text _("What Is")
                if day271 and show_complete:
                    textbutton _("What Was {b}✓{/b}") action Replay("day271", locked=False) text_style "modmybutton"
                elif not day271 and not ev_day271.missed:
                    text _("What Was")
                if day280 and show_complete:
                    textbutton _("Annabel Lee {b}✓{/b}") action Replay("day280", locked=False) text_style "modmybutton"
                elif not day280 and not ev_day280.missed:
                    text _("Annabel Lee")
                if day281 and show_complete:
                    textbutton _("Yuritopia {b}✓{/b}") action Replay("day281", locked=False) text_style "modmybutton"
                elif not day281 and not ev_day281.missed:
                    text _("Yuritopia")
                if day282 and show_complete:
                    textbutton _("Birdcage {b}✓{/b}") action Replay("day282", locked=False) text_style "modmybutton"
                elif not day282 and not ev_day282.missed:
                    text _("Birdcage")
                if day283 and show_complete:
                    textbutton _("Survive! Grow! {b}✓{/b}") action Replay("day283", locked=False) text_style "modmybutton"
                elif not day283 and not ev_day283.missed:
                    text _("Survive! Grow!")
                if day287 and show_complete:
                    textbutton _("Another Long Year {b}✓{/b}") action Replay("day287", locked=False) text_style "modmybutton"
                elif not day287 and not ev_day287.missed:
                    text _("Another Long Year")
                if day288 and show_complete:
                    textbutton _("Adult Supervision {b}✓{/b}") action Replay("day288", locked=False) text_style "modmybutton"
                elif not day288 and not ev_day288.missed:
                    text _("Adult Supervision")
                if day295 and show_complete:
                    textbutton _("The WAP Man {b}✓{/b}") action Replay("day295", locked=False) text_style "modmybutton"
                elif not day295 and not ev_day295.missed:
                    text _("The WAP Man")
                if day295parttwo and show_complete:
                    textbutton _("The Color of a Heart {b}✓{/b}") action Replay("day295parttwo", locked=False) text_style "modmybutton"
                elif not day295parttwo and not ev_day295parttwo.missed:
                    text _("The Color of a Heart")
                if day297 and show_complete:
                    textbutton _("Call Me By Your Name {b}✓{/b}") action Replay("day297", locked=False) text_style "modmybutton"
                elif not day297 and not ev_day297.missed:
                    text _("Call Me By Your Name")
                if day302 and show_complete:
                    textbutton _("Lives and Minds of Laymen {b}✓{/b}") action Replay("day302", locked=False) text_style "modmybutton"
                elif not day302 and not ev_day302.missed:
                    text _("Lives and Minds of Laymen")
                if day303 and show_complete:
                    textbutton _("Sounds of Cicadas {b}✓{/b}") action Replay("day303", locked=False) text_style "modmybutton"
                elif not day303 and not ev_day303.missed:
                    text _("Sounds of Cicadas")
                if day304 and show_complete:
                    textbutton _("Horses or the Whispers of the Dead {b}✓{/b}") action Replay("day304", locked=False) text_style "modmybutton"
                elif not day304 and not ev_day304.missed:
                    text _("Horses or the Whispers of the Dead")
                if day318 and show_complete:
                    textbutton _("Operation: Firestarter {b}✓{/b}") action Replay("day318", locked=False) text_style "modmybutton"
                elif not day318 and not ev_day318.missed:
                    text _("Operation: Firestarter")
                if dormwar1 and show_complete:
                    textbutton _("Super Mega Ultimate Dorm War! {b}✓{/b}") action Replay("dormwar1", locked=False) text_style "modmybutton"
                elif not dormwar1 and not ev_dormwar1.missed:
                    text _("Super Mega Ultimate Dorm War!")
                if dormwar2 and show_complete:
                    textbutton _("Pre-Game Show! {b}✓{/b}") action Replay("dormwar2", locked=False) text_style "modmybutton"
                elif not dormwar2 and not ev_dormwar2.missed:
                    text _("Pre-Game Show!")
                if dormwar3 and show_complete:
                    textbutton _("Imouto Mode! {b}✓{/b}") action Replay("dormwar3", locked=False) text_style "modmybutton"
                elif not dormwar3 and not ev_dormwar3.missed:
                    text _("Imouto Mode!")
                if dormwar4 and show_complete:
                    textbutton _("Alive & Active! All Out Athletics! {b}✓{/b}") action Replay("dormwar4", locked=False) text_style "modmybutton"
                elif not dormwar4 and not ev_dormwar4.missed:
                    text _("Alive & Active! All Out Athletics!")
                if dormwar5 and show_complete:
                    textbutton _("Friend Zone Fight! {b}✓{/b}") action Replay("dormwar5", locked=False) text_style "modmybutton"
                elif not dormwar5 and not ev_dormwar5.missed:
                    text _("Friend Zone Fight!")
                if dormwar6 and show_complete:
                    textbutton _("Sphenopalatine Ganglioneuralgia {b}✓{/b}") action Replay("dormwar6", locked=False) text_style "modmybutton"
                elif not dormwar6 and not ev_dormwar6.missed:
                    text _("Sphenopalatine Ganglioneuralgia")
                if dormwar7 and show_complete:
                    textbutton _("Ruthless Rhyme Rhomp! Rap Rampage! {b}✓{/b}") action Replay("dormwar7", locked=False) text_style "modmybutton"
                elif not dormwar7 and not ev_dormwar7.missed:
                    text _("Ruthless Rhyme Rhomp! Rap Rampage!")
                if dormwar8 and show_complete:
                    textbutton _("Chaperone {b}✓{/b}") action Replay("dormwar8", locked=False) text_style "modmybutton"
                elif not dormwar8 and not ev_dormwar8.missed:
                    text _("Chaperone")
                if dormwar9 and show_complete:
                    textbutton _("Why Now? {b}✓{/b}") action Replay("dormwar9", locked=False) text_style "modmybutton"
                elif not dormwar9 and not ev_dormwar9.missed:
                    text _("Why Now?")
                if dormwar10 and show_complete:
                    textbutton _("In Some Cases, Love {b}✓{/b}") action Replay("dormwar10", locked=False) text_style "modmybutton"
                elif not dormwar10 and not ev_dormwar10.missed:
                    text _("In Some Cases, Love")
                if dormwar11 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. Z: Alentha Amastacia {b}✓{/b}") action Replay("dormwar11", locked=False) text_style "modmybutton"
                elif not dormwar11 and not ev_dormwar11.missed:
                    text _("The Legacy of Thaum Pt. Z: Alentha Amastacia")
                if dormwar12 and show_complete:
                    textbutton _("Us {b}✓{/b}") action Replay("dormwar12", locked=False) text_style "modmybutton"
                elif not dormwar12 and not ev_dormwar12.missed:
                    text _("Us")
                if dormwar13 and show_complete:
                    textbutton _("First Last Date {b}✓{/b}") action Replay("dormwar13", locked=False) text_style "modmybutton"
                elif not dormwar13 and not ev_dormwar13.missed:
                    text _("First Last Date")
                if dormwar14 and show_complete:
                    textbutton _("The Scary Room {b}✓{/b}") action Replay("dormwar14", locked=False) text_style "modmybutton"
                elif not dormwar14 and not ev_dormwar14.missed:
                    text _("The Scary Room")
                if dormwar15 and show_complete:
                    textbutton _("Fallen Angels {b}✓{/b}") action Replay("dormwar15", locked=False) text_style "modmybutton"
                elif not dormwar15 and not ev_dormwar15.missed:
                    text _("Fallen Angels")
                if dormwar16 and show_complete:
                    textbutton _("Post-Game Celebration! {b}✓{/b}") action Replay("dormwar16", locked=False) text_style "modmybutton"
                elif not dormwar16 and not ev_dormwar16.missed:
                    text _("Post-Game Celebration!")
                if dormwar17 and show_complete:
                    textbutton _("War's End {b}✓{/b}") action Replay("dormwar17", locked=False) text_style "modmybutton"
                elif not dormwar17 and not ev_dormwar17.missed:
                    text _("War's End")
                if day333 and show_complete:
                    textbutton _("Record Breaker {b}✓{/b}") action Replay("day333", locked=False) text_style "modmybutton"
                elif not day333 and not ev_day333.missed:
                    text _("Record Breaker")
                if day333part2 and show_complete:
                    textbutton _("Lesbian Stuff {b}✓{/b}") action Replay("day333part2", locked=False) text_style "modmybutton"
                elif not day333part2 and not ev_day333part2.missed:
                    text _("Lesbian Stuff")
                if day340 and show_complete:
                    textbutton _("Mana Transfer {b}✓{/b}") action Replay("day340", locked=False) text_style "modmybutton"
                elif not day340 and not ev_day340.missed:
                    text _("Mana Transfer")
                if day344 and show_complete:
                    textbutton _("The Price of Experience {b}✓{/b}") action Replay("day344", locked=False) text_style "modmybutton"
                elif not day344 and not ev_day344.missed:
                    text _("The Price of Experience")
                if thirdreset1 and show_complete:
                    textbutton _("Word of the Day {b}✓{/b}") action Replay("thirdreset1", locked=False) text_style "modmybutton"
                elif not thirdreset1 and not ev_thirdreset1.missed:
                    text _("Word of the Day")
                if thirdreset2 and show_complete:
                    textbutton _("Backwards Dancing {b}✓{/b}") action Replay("thirdreset2", locked=False) text_style "modmybutton"
                elif not thirdreset2 and not ev_thirdreset2.missed:
                    text _("Backwards Dancing")
                if thirdreset3 and show_complete:
                    textbutton _("Sayonara {b}✓{/b}") action Replay("thirdreset3", locked=False) text_style "modmybutton"
                elif not thirdreset3 and not ev_thirdreset3.missed:
                    text _("Sayonara")
                if day351 and show_complete:
                    textbutton _("Food Groups {b}✓{/b}") action Replay("day351", locked=False) text_style "modmybutton"
                elif not day351 and not ev_day351.missed:
                    text _("Food Groups")
                if day355 and show_complete:
                    textbutton _("Permission Slip {b}✓{/b}") action Replay("day355", locked=False) text_style "modmybutton"
                elif not day355 and not ev_day355.missed:
                    text _("Permission Slip")
                if secondbeach1 and show_complete:
                    textbutton _("Good Morning {b}✓{/b}") action Replay("secondbeach1", locked=False) text_style "modmybutton"
                elif not secondbeach1 and not ev_secondbeach1.missed:
                    text _("Good Morning")
                if secondbeach2 and show_complete:
                    textbutton _("Egg Tossing {b}✓{/b}") action Replay("secondbeach2", locked=False) text_style "modmybutton"
                elif not secondbeach2 and not ev_secondbeach2.missed:
                    text _("Egg Tossing")
                if secondbeach3 and show_complete:
                    textbutton _("De-Briefing the Teacher {b}✓{/b}") action Replay("secondbeach3", locked=False) text_style "modmybutton"
                elif not secondbeach3 and not ev_secondbeach3.missed:
                    text _("De-Briefing the Teacher")
                if secondbeach4 and show_complete:
                    textbutton _("TPK (Banana Boat) {b}✓{/b}") action Replay("secondbeach4", locked=False) text_style "modmybutton"
                elif not secondbeach4 and not ev_secondbeach4.missed:
                    text _("TPK (Banana Boat)")
                if secondbeach5 and show_complete:
                    textbutton _("The Next Best Thing {b}✓{/b}") action Replay("secondbeach5", locked=False) text_style "modmybutton"
                elif not secondbeach5 and not ev_secondbeach5.missed:
                    text _("The Next Best Thing")
                if secondbeach6 and show_complete:
                    textbutton _("The Yellow Wallpaper {b}✓{/b}") action Replay("secondbeach6", locked=False) text_style "modmybutton"
                elif not secondbeach6 and not ev_secondbeach6.missed:
                    text _("The Yellow Wallpaper")
                if secondbeach7 and show_complete:
                    textbutton _("Everything Ephemeral (Face Forward) {b}✓{/b}") action Replay("secondbeach7", locked=False) text_style "modmybutton"
                elif not secondbeach7 and not ev_secondbeach7.missed:
                    text _("Everything Ephemeral (Face Forward)")
                if secondbeach8 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. III: Changeling {b}✓{/b}") action Replay("secondbeach8", locked=False) text_style "modmybutton"
                elif not secondbeach8 and not ev_secondbeach8.missed:
                    text _("The Legacy of Thaum Pt. III: Changeling")
                if secondbeach9 and show_complete:
                    textbutton _("Alderaan {b}✓{/b}") action Replay("secondbeach9", locked=False) text_style "modmybutton"
                elif not secondbeach9 and not ev_secondbeach9.missed:
                    text _("Alderaan")
                if secondbeach10 and show_complete:
                    textbutton _("Torrential Downpour. Child of Man. {b}✓{/b}") action Replay("secondbeach10", locked=False) text_style "modmybutton"
                elif not secondbeach10 and not ev_secondbeach10.missed:
                    text _("Torrential Downpour. Child of Man.")
                if secondbeach11 and show_complete:
                    textbutton _("Getting Comfortable {b}✓{/b}") action Replay("secondbeach11", locked=False) text_style "modmybutton"
                elif not secondbeach11 and not ev_secondbeach11.missed:
                    text _("Getting Comfortable")
                if secondbeach12 and show_complete:
                    textbutton _("Left Out in Light {b}✓{/b}") action Replay("secondbeach12", locked=False) text_style "modmybutton"
                elif not secondbeach12 and not ev_secondbeach12.missed:
                    text _("Left Out in Light")
                if secondbeach13 and show_complete:
                    textbutton _("We Were Angels {b}✓{/b}") action Replay("secondbeach13", locked=False) text_style "modmybutton"
                elif not secondbeach13 and not ev_secondbeach13.missed:
                    text _("We Were Angels")
                if secondbeach14 and show_complete:
                    textbutton _("Lavender's Blue {b}✓{/b}") action Replay("secondbeach14", locked=False) text_style "modmybutton"
                elif not secondbeach14 and not ev_secondbeach14.missed:
                    text _("Lavender's Blue")
                if secondbeach15 and show_complete:
                    textbutton _("Pluto Was Never Really a Planet {b}✓{/b}") action Replay("secondbeach15", locked=False) text_style "modmybutton"
                elif not secondbeach15 and not ev_secondbeach15.missed:
                    text _("Pluto Was Never Really a Planet")
                if secondbeach16 and show_complete:
                    textbutton _("Try. Try. Try. {b}✓{/b}") action Replay("secondbeach16", locked=False) text_style "modmybutton"
                elif not secondbeach16 and not ev_secondbeach16.missed:
                    text _("Try. Try. Try.")
                if secondbeach17 and show_complete:
                    textbutton _("Goodnight {b}✓{/b}") action Replay("secondbeach17", locked=False) text_style "modmybutton"
                elif not secondbeach17 and not ev_secondbeach17.missed:
                    text _("Goodnight")
                if secondbeach18 and show_complete:
                    textbutton _("All is Bright. All is Beautiful. {b}✓{/b}") action Replay("secondbeach18", locked=False) text_style "modmybutton"
                elif not secondbeach18 and not ev_secondbeach18.missed:
                    text _("All is Bright. All is Beautiful.")
                if halloweentwo1 and show_complete:
                    textbutton _("Girls in Spandex {b}✓{/b}") action Replay("halloweentwo1", locked=False) text_style "modmybutton"
                elif not halloweentwo1 and not ev_halloweentwo1.missed:
                    text _("Girls in Spandex")
                if halloweentwo2 and show_complete:
                    textbutton _("Butterfly Facts {b}✓{/b}") action Replay("halloweentwo2", locked=False) text_style "modmybutton"
                elif not halloweentwo2 and not ev_halloweentwo2.missed:
                    text _("Butterfly Facts")
                if halloweentwo3 and show_complete:
                    textbutton _("Immernachtreich {b}✓{/b}") action Replay("halloweentwo3", locked=False) text_style "modmybutton"
                elif not halloweentwo3 and not ev_halloweentwo3.missed:
                    text _("Immernachtreich")
                if halloweentwo4 and show_complete:
                    textbutton _("Take Me Anywhere {b}✓{/b}") action Replay("halloweentwo4", locked=False) text_style "modmybutton"
                elif not halloweentwo4 and not ev_halloweentwo4.missed:
                    text _("Take Me Anywhere")
                if halloweentwo5 and show_complete:
                    textbutton _("Anglerfish {b}✓{/b}") action Replay("halloweentwo5", locked=False) text_style "modmybutton"
                elif not halloweentwo5 and not ev_halloweentwo5.missed:
                    text _("Anglerfish")
                if halloweentwo6 and show_complete:
                    textbutton _("Porcelain Labyrinth {b}✓{/b}") action Replay("halloweentwo6", locked=False) text_style "modmybutton"
                elif not halloweentwo6 and not ev_halloweentwo6.missed:
                    text _("Porcelain Labyrinth")
                if halloweentwo7 and show_complete:
                    textbutton _("The First Signs of Fraying Threads {b}✓{/b}") action Replay("halloweentwo7", locked=False) text_style "modmybutton"
                elif not halloweentwo7 and not ev_halloweentwo7.missed:
                    text _("The First Signs of Fraying Threads")
                if halloweentwo8 and show_complete:
                    textbutton _("Official Unofficial Double Date {b}✓{/b}") action Replay("halloweentwo8", locked=False) text_style "modmybutton"
                elif not halloweentwo8 and not ev_halloweentwo8.missed:
                    text _("Official Unofficial Double Date")
                if halloweentwo9 and show_complete:
                    textbutton _("In Circles {b}✓{/b}") action Replay("halloweentwo9", locked=False) text_style "modmybutton"
                elif not halloweentwo9 and not ev_halloweentwo9.missed:
                    text _("In Circles")
                if halloweentwo10 and show_complete:
                    textbutton _("Escape Rope {b}✓{/b}") action Replay("halloweentwo10", locked=False) text_style "modmybutton"
                elif not halloweentwo10 and not ev_halloweentwo10.missed:
                    text _("Escape Rope")
                if halloweentwo11 and show_complete:
                    textbutton _("Lavender's Green {b}✓{/b}") action Replay("halloweentwo11", locked=False) text_style "modmybutton"
                elif not halloweentwo11 and not ev_halloweentwo11.missed:
                    text _("Lavender's Green")
                if halloweentwo12 and show_complete:
                    textbutton _("Gallows Edge {b}✓{/b}") action Replay("halloweentwo12", locked=False) text_style "modmybutton"
                elif not halloweentwo12 and not ev_halloweentwo12.missed:
                    text _("Gallows Edge")
                if halloweentwo13 and show_complete:
                    textbutton _("Metal in Microwaves {b}✓{/b}") action Replay("halloweentwo13", locked=False) text_style "modmybutton"
                elif not halloweentwo13 and not ev_halloweentwo13.missed:
                    text _("Metal in Microwaves")
                if christmastwo1 and show_complete:
                    textbutton _("Three Amigos {b}✓{/b}") action Replay("christmastwo1", locked=False) text_style "modmybutton"
                elif not christmastwo1 and not ev_christmastwo1.missed:
                    text _("Three Amigos")
                if christmastwo2 and show_complete:
                    textbutton _("The Reliable and Totally Legitimate Princess Imani {b}✓{/b}") action Replay("christmastwo2", locked=False) text_style "modmybutton"
                elif not christmastwo2 and not ev_christmastwo2.missed:
                    text _("The Reliable and Totally Legitimate Princess Imani")
                if christmastwo3 and show_complete:
                    textbutton _("Room to Grow {b}✓{/b}") action Replay("christmastwo3", locked=False) text_style "modmybutton"
                elif not christmastwo3 and not ev_christmastwo3.missed:
                    text _("Room to Grow")
                if christmastwo4 and show_complete:
                    textbutton _("Dodging Snowflakes {b}✓{/b}") action Replay("christmastwo4", locked=False) text_style "modmybutton"
                elif not christmastwo4 and not ev_christmastwo4.missed:
                    text _("Dodging Snowflakes")
                if christmastwo5 and show_complete:
                    textbutton _("Everything Evil {b}✓{/b}") action Replay("christmastwo5", locked=False) text_style "modmybutton"
                elif not christmastwo5 and not ev_christmastwo5.missed:
                    text _("Everything Evil")
                if christmastwo6 and show_complete:
                    textbutton _("Tokimeki Labyrinth {b}✓{/b}") action Replay("christmastwo6", locked=False) text_style "modmybutton"
                elif not christmastwo6 and not ev_christmastwo6.missed:
                    text _("Tokimeki Labyrinth")
                if christmastwo7 and show_complete:
                    textbutton _("Love Set to Max (Class Warfare) {b}✓{/b}") action Replay("christmastwo7", locked=False) text_style "modmybutton"
                elif not christmastwo7 and not ev_christmastwo7.missed:
                    text _("Love Set to Max (Class Warfare)")
                if christmastwo8 and show_complete:
                    textbutton _("Dohoonkabhankoloos {b}✓{/b}") action Replay("christmastwo8", locked=False) text_style "modmybutton"
                elif not christmastwo8 and not ev_christmastwo8.missed:
                    text _("Dohoonkabhankoloos")
                if christmastwo9 and show_complete:
                    textbutton _("Fear of Missing Out {b}✓{/b}") action Replay("christmastwo9", locked=False) text_style "modmybutton"
                elif not christmastwo9 and not ev_christmastwo9.missed:
                    text _("Fear of Missing Out")
                if christmastwo10 and show_complete:
                    textbutton _("Walking on Eggshells {b}✓{/b}") action Replay("christmastwo10", locked=False) text_style "modmybutton"
                elif not christmastwo10 and not ev_christmastwo10.missed:
                    text _("Walking on Eggshells")
                if christmastwo11 and show_complete:
                    textbutton _("New Age Entrepreneurs {b}✓{/b}") action Replay("christmastwo11", locked=False) text_style "modmybutton"
                elif not christmastwo11 and not ev_christmastwo11.missed:
                    text _("New Age Entrepreneurs")
                if christmastwo12 and show_complete:
                    textbutton _("The Smile, The Face {b}✓{/b}") action Replay("christmastwo12", locked=False) text_style "modmybutton"
                elif not christmastwo12 and not ev_christmastwo12.missed:
                    text _("The Smile, The Face")
                if christmastwo13 and show_complete:
                    textbutton _("Shadowmeld {b}✓{/b}") action Replay("christmastwo13", locked=False) text_style "modmybutton"
                elif not christmastwo13 and not ev_christmastwo13.missed:
                    text _("Shadowmeld")
                if christmastwo14 and show_complete:
                    textbutton _("Chashu (A Cracked Bowl) {b}✓{/b}") action Replay("christmastwo14", locked=False) text_style "modmybutton"
                elif not christmastwo14 and not ev_christmastwo14.missed:
                    text _("Chashu (A Cracked Bowl)")
                if christmastwo15 and show_complete:
                    textbutton _("A Way's Away {b}✓{/b}") action Replay("christmastwo15", locked=False) text_style "modmybutton"
                elif not christmastwo15 and not ev_christmastwo15.missed:
                    text _("A Way's Away")
                if christmastwo16 and show_complete:
                    textbutton _("No Escape {b}✓{/b}") action Replay("christmastwo16", locked=False) text_style "modmybutton"
                elif not christmastwo16 and not ev_christmastwo16.missed:
                    text _("No Escape")
                if christmastwo17 and show_complete:
                    textbutton _("Spotless Mind {b}✓{/b}") action Replay("christmastwo17", locked=False) text_style "modmybutton"
                elif not christmastwo17 and not ev_christmastwo17.missed:
                    text _("Spotless Mind")
                if christmastwo18 and show_complete:
                    textbutton _("Me Without You {b}✓{/b}") action Replay("christmastwo18", locked=False) text_style "modmybutton"
                elif not christmastwo18 and not ev_christmastwo18.missed:
                    text _("Me Without You")
                if christmastwo19 and show_complete:
                    textbutton _("The Color White {b}✓{/b}") action Replay("christmastwo19", locked=False) text_style "modmybutton"
                elif not christmastwo19 and not ev_christmastwo19.missed:
                    text _("The Color White")
                if christmastwo20 and show_complete:
                    textbutton _("Glued to the Sky {b}✓{/b}") action Replay("christmastwo20", locked=False) text_style "modmybutton"
                elif not christmastwo20 and not ev_christmastwo20.missed:
                    text _("Glued to the Sky")
                if returntosummer1 and show_complete:
                    textbutton _("The Light of Last Summer {b}✓{/b}") action Replay("returntosummer1", locked=False) text_style "modmybutton"
                elif not returntosummer1 and not ev_returntosummer1.missed:
                    text _("The Light of Last Summer")
                if returntosummer2 and show_complete:
                    textbutton _("A Life of Prizes {b}✓{/b}") action Replay("returntosummer2", locked=False) text_style "modmybutton"
                elif not returntosummer2 and not ev_returntosummer2.missed:
                    text _("A Life of Prizes")
                if returntosummer3 and show_complete:
                    textbutton _("Utinam Ne Illum Numquam Conspexissem {b}✓{/b}") action Replay("returntosummer3", locked=False) text_style "modmybutton"
                elif not returntosummer3 and not ev_returntosummer3.missed:
                    text _("Utinam Ne Illum Numquam Conspexissem")

################################################################################

            if show_hints == True and not _in_replay:

                vbox:
                    xpos .4
                    style_prefix "tracker"

                    #Snow-Covered Footprints (christmas1)
                    if (not ev_christmas1.completed and not ev_christmas1.missed) or show_complete:
                        text ("[ev_christmas1.hint]")

                    #Patent-Pending (christmas2)
                    if (not ev_christmas2.completed and not ev_christmas2.missed) or show_complete:
                        text ("[ev_christmas2.hint]")

                    #Fuck Christmas (christmas3)
                    if (not ev_christmas3.completed and not ev_christmas3.missed) or show_complete:
                        text ("[ev_christmas3.hint]")

                    #Disappointing Everyone (christmas4)
                    if (not ev_christmas4.completed and not ev_christmas4.missed) or show_complete:
                        text ("[ev_christmas4.hint]")

                    #Bottled Dreams (christmas5)
                    if (not ev_christmas5.completed and not ev_christmas5.missed) or show_complete:
                        text ("[ev_christmas5.hint]")

                    #Christmas Miracle (christmas6)
                    if (not ev_christmas6.completed and not ev_christmas6.missed) or show_complete:
                        text ("[ev_christmas6.hint]")

                    #Fireworks, Chicken, and the Innate Fear of Death (christmas7)
                    if (not ev_christmas7.completed and not ev_christmas7.missed) or show_complete:
                        text ("[ev_christmas7.hint]")

                    #Suicide Pact (day237)
                    if (not ev_day237.completed and not ev_day237.missed) or show_complete:
                        text ("[ev_day237.hint]")

                    #A Door that People Move Through (day239)
                    if (not ev_day239.completed and not ev_day239.missed) or show_complete:
                        text ("[ev_day239.hint]")

                    #Uta's Last Stand (day240)
                    if (not ev_day240.completed and not ev_day240.missed) or show_complete:
                        text ("[ev_day240.hint]")

                    #Opposites Attract (day244)
                    if (not ev_day244.completed and not ev_day244.missed) or show_complete:
                        text ("[ev_day244.hint]")

                    #All Kinds of People, All Kinds of Things (day246)
                    if (not ev_day246.completed and not ev_day246.missed) or show_complete:
                        text ("[ev_day246.hint]")

                    #Caterpillar (day247)
                    if (not ev_day247.completed and not ev_day247.missed) or show_complete:
                        text ("[ev_day247.hint]")

                    #Let Me Die in Spring (day261)
                    if (not ev_day261.completed and not ev_day261.missed) or show_complete:
                        text ("[ev_day261.hint]")

                    #There's Always a Chance (day263)
                    if (not ev_day263.completed and not ev_day263.missed) or show_complete:
                        text ("[ev_day263.hint]")

                    #Forty Degrees Below Zero (day264)
                    if (not ev_day264.completed and not ev_day264.missed) or show_complete:
                        text ("[ev_day264.hint]")

                    #What Could Have Been (day269)
                    if (not ev_day269.completed and not ev_day269.missed) or show_complete:
                        text ("[ev_day269.hint]")

                    #What Is (day270)
                    if (not ev_day270.completed and not ev_day270.missed) or show_complete:
                        text ("[ev_day270.hint]")

                    #What Was (day271)
                    if (not ev_day271.completed and not ev_day271.missed) or show_complete:
                        text ("[ev_day271.hint]")

                    #Annabel Lee (day280)
                    if (not ev_day280.completed and not ev_day280.missed) or show_complete:
                        text ("[ev_day280.hint]")

                    #Yuritopia (day281)
                    if (not ev_day281.completed and not ev_day281.missed) or show_complete:
                        text ("[ev_day281.hint]")

                    #Birdcage (day282)
                    if (not ev_day282.completed and not ev_day282.missed) or show_complete:
                        text ("[ev_day282.hint]")

                    #Survive! Grow! (day283)
                    if (not ev_day283.completed and not ev_day283.missed) or show_complete:
                        text ("[ev_day283.hint]")

                    #Another Long Year (day287)
                    if (not ev_day287.completed and not ev_day287.missed) or show_complete:
                        text ("[ev_day287.hint]")

                    #Adult Supervision (day288)
                    if (not ev_day288.completed and not ev_day288.missed) or show_complete:
                        text ("[ev_day288.hint]")

                    #The WAP Man (day295)
                    if (not ev_day295.completed and not ev_day295.missed) or show_complete:
                        text ("[ev_day295.hint]")

                    #The Color of a Heart (day295parttwo)
                    if (not ev_day295parttwo.completed and not ev_day295parttwo.missed) or show_complete:
                        text ("[ev_day295parttwo.hint]")

                    #Call Me By Your Name (day297)
                    if (not ev_day297.completed and not ev_day297.missed) or show_complete:
                        text ("[ev_day297.hint]")

                    #Lives and Minds of Laymen (day302)
                    if (not ev_day302.completed and not ev_day302.missed) or show_complete:
                        text ("[ev_day302.hint]")

                    #Sounds of Cicadas (day303)
                    if (not ev_day303.completed and not ev_day303.missed) or show_complete:
                        text ("[ev_day303.hint]")

                    #Horses or the Whispers of the Dead (day304)
                    if (not ev_day304.completed and not ev_day304.missed) or show_complete:
                        text ("[ev_day304.hint]")

                    #Operation: Firestarter (day318)
                    if (not ev_day318.completed and not ev_day318.missed) or show_complete:
                        text ("[ev_day318.hint]")

                    #Super Mega Ultimate Dorm War! (dormwar1)
                    if (not ev_dormwar1.completed and not ev_dormwar1.missed) or show_complete:
                        text ("[ev_dormwar1.hint]")

                    #Pre-Game Show! (dormwar2)
                    if (not ev_dormwar2.completed and not ev_dormwar2.missed) or show_complete:
                        text ("[ev_dormwar2.hint]")

                    #Imouto Mode! (dormwar3)
                    if (not ev_dormwar3.completed and not ev_dormwar3.missed) or show_complete:
                        text ("[ev_dormwar3.hint]")

                    #Alive & Active! All Out Athletics! (dormwar4)
                    if (not ev_dormwar4.completed and not ev_dormwar4.missed) or show_complete:
                        text ("[ev_dormwar4.hint]")

                    #Friend Zone Fight! (dormwar5)
                    if (not ev_dormwar5.completed and not ev_dormwar5.missed) or show_complete:
                        text ("[ev_dormwar5.hint]")

                    #Sphenopalatine Ganglioneuralgia (dormwar6)
                    if (not ev_dormwar6.completed and not ev_dormwar6.missed) or show_complete:
                        text ("[ev_dormwar6.hint]")

                    #Ruthless Rhyme Rhomp! Rap Rampage! (dormwar7)
                    if (not ev_dormwar7.completed and not ev_dormwar7.missed) or show_complete:
                        text ("[ev_dormwar7.hint]")

                    #Chaperone (dormwar8)
                    if (not ev_dormwar8.completed and not ev_dormwar8.missed) or show_complete:
                        text ("[ev_dormwar8.hint]")

                    #Why Now? (dormwar9)
                    if (not ev_dormwar9.completed and not ev_dormwar9.missed) or show_complete:
                        text ("[ev_dormwar9.hint]")

                    #In Some Cases, Love (dormwar10)
                    if (not ev_dormwar10.completed and not ev_dormwar10.missed) or show_complete:
                        text ("[ev_dormwar10.hint]")

                    #The Legacy of Thaum Pt. Z: Alentha Amastacia (dormwar11)
                    if (not ev_dormwar11.completed and not ev_dormwar11.missed) or show_complete:
                        text ("[ev_dormwar11.hint]")

                    #Us (dormwar12)
                    if (not ev_dormwar12.completed and not ev_dormwar12.missed) or show_complete:
                        text ("[ev_dormwar12.hint]")

                    #First Last Date (dormwar13)
                    if (not ev_dormwar13.completed and not ev_dormwar13.missed) or show_complete:
                        text ("[ev_dormwar13.hint]")

                    #The Scary Room (dormwar14)
                    if (not ev_dormwar14.completed and not ev_dormwar14.missed) or show_complete:
                        text ("[ev_dormwar14.hint]")

                    #Fallen Angels (dormwar15)
                    if (not ev_dormwar15.completed and not ev_dormwar15.missed) or show_complete:
                        text ("[ev_dormwar15.hint]")

                    #Post-Game Celebration! (dormwar16)
                    if (not ev_dormwar16.completed and not ev_dormwar16.missed) or show_complete:
                        text ("[ev_dormwar16.hint]")

                    #War's End (dormwar17)
                    if (not ev_dormwar17.completed and not ev_dormwar17.missed) or show_complete:
                        text ("[ev_dormwar17.hint]")

                    #Record Breaker (day333)
                    if (not ev_day333.completed and not ev_day333.missed) or show_complete:
                        text ("[ev_day333.hint]")

                    #Lesbian Stuff (day333part2)
                    if (not ev_day333part2.completed and not ev_day333part2.missed) or show_complete:
                        text ("[ev_day333part2.hint]")

                    #Mana Transfer (day340)
                    if (not ev_day340.completed and not ev_day340.missed) or show_complete:
                        text ("[ev_day340.hint]")

                    #The Price of Experience (day344)
                    if (not ev_day344.completed and not ev_day344.missed) or show_complete:
                        text ("[ev_day344.hint]")

                    #Word of the Day (thirdreset1)
                    if (not ev_thirdreset1.completed and not ev_thirdreset1.missed) or show_complete:
                        text ("[ev_thirdreset1.hint]")

                    #Backwards Dancing (thirdreset2)
                    if (not ev_thirdreset2.completed and not ev_thirdreset2.missed) or show_complete:
                        text ("[ev_thirdreset2.hint]")

                    #Sayonara (thirdreset3)
                    if (not ev_thirdreset3.completed and not ev_thirdreset3.missed) or show_complete:
                        text ("[ev_thirdreset3.hint]")

                    #Food Groups (day351)
                    if (not ev_day351.completed and not ev_day351.missed) or show_complete:
                        text ("[ev_day351.hint]")

                    #Permission Slip (day355)
                    if (not ev_day355.completed and not ev_day355.missed) or show_complete:
                        text ("[ev_day355.hint]")

                    #Good Morning (secondbeach1)
                    if (not ev_secondbeach1.completed and not ev_secondbeach1.missed) or show_complete:
                        text ("[ev_secondbeach1.hint]")

                    #Egg Tossing (secondbeach2)
                    if (not ev_secondbeach2.completed and not ev_secondbeach2.missed) or show_complete:
                        text ("[ev_secondbeach2.hint]")

                    #De-Briefing the Teacher (secondbeach3)
                    if (not ev_secondbeach3.completed and not ev_secondbeach3.missed) or show_complete:
                        text ("[ev_secondbeach3.hint]")

                    #TPK (Banana Boat) (secondbeach4)
                    if (not ev_secondbeach4.completed and not ev_secondbeach4.missed) or show_complete:
                        text ("[ev_secondbeach4.hint]")

                    #The Next Best Thing (secondbeach5)
                    if (not ev_secondbeach5.completed and not ev_secondbeach5.missed) or show_complete:
                        text ("[ev_secondbeach5.hint]")

                    #The Yellow Wallpaper (secondbeach6)
                    if (not ev_secondbeach6.completed and not ev_secondbeach6.missed) or show_complete:
                        text ("[ev_secondbeach6.hint]")

                    #Everything Ephemeral (Face Forward) (secondbeach7)
                    if (not ev_secondbeach7.completed and not ev_secondbeach7.missed) or show_complete:
                        text ("[ev_secondbeach7.hint]")

                    #The Legacy of Thaum Pt. III: Changeling (secondbeach8)
                    if (not ev_secondbeach8.completed and not ev_secondbeach8.missed) or show_complete:
                        text ("[ev_secondbeach8.hint]")

                    #Alderaan (secondbeach9)
                    if (not ev_secondbeach9.completed and not ev_secondbeach9.missed) or show_complete:
                        text ("[ev_secondbeach9.hint]")

                    #Torrential Downpour. Child of Man. (secondbeach10)
                    if (not ev_secondbeach10.completed and not ev_secondbeach10.missed) or show_complete:
                        text ("[ev_secondbeach10.hint]")

                    #Getting Comfortable (secondbeach11)
                    if (not ev_secondbeach11.completed and not ev_secondbeach11.missed) or show_complete:
                        text ("[ev_secondbeach11.hint]")

                    #Left Out in Light (secondbeach12)
                    if (not ev_secondbeach12.completed and not ev_secondbeach12.missed) or show_complete:
                        text ("[ev_secondbeach12.hint]")

                    #We Were Angels (secondbeach13)
                    if (not ev_secondbeach13.completed and not ev_secondbeach13.missed) or show_complete:
                        text ("[ev_secondbeach13.hint]")

                    #Lavender's Blue (secondbeach14)
                    if (not ev_secondbeach14.completed and not ev_secondbeach14.missed) or show_complete:
                        text ("[ev_secondbeach14.hint]")

                    #Pluto Was Never Really a Planet (secondbeach15)
                    if (not ev_secondbeach15.completed and not ev_secondbeach15.missed) or show_complete:
                        text ("[ev_secondbeach15.hint]")

                    #Try. Try. Try. (secondbeach16)
                    if (not ev_secondbeach16.completed and not ev_secondbeach16.missed) or show_complete:
                        text ("[ev_secondbeach16.hint]")

                    #Goodnight (secondbeach17)
                    if (not ev_secondbeach17.completed and not ev_secondbeach17.missed) or show_complete:
                        text ("[ev_secondbeach17.hint]")

                    #All is Bright. All is Beautiful. (secondbeach18)
                    if (not ev_secondbeach18.completed and not ev_secondbeach18.missed) or show_complete:
                        text ("[ev_secondbeach18.hint]")

                    #Girls in Spandex (halloweentwo1)
                    if (not ev_halloweentwo1.completed and not ev_halloweentwo1.missed) or show_complete:
                        text ("[ev_halloweentwo1.hint]")

                    #Butterfly Facts (halloweentwo2)
                    if (not ev_halloweentwo2.completed and not ev_halloweentwo2.missed) or show_complete:
                        text ("[ev_halloweentwo2.hint]")

                    #Immernachtreich (halloweentwo3)
                    if (not ev_halloweentwo3.completed and not ev_halloweentwo3.missed) or show_complete:
                        text ("[ev_halloweentwo3.hint]")

                    #Take Me Anywhere (halloweentwo4)
                    if (not ev_halloweentwo4.completed and not ev_halloweentwo4.missed) or show_complete:
                        text ("[ev_halloweentwo4.hint]")

                    #Anglerfish (halloweentwo5)
                    if (not ev_halloweentwo5.completed and not ev_halloweentwo5.missed) or show_complete:
                        text ("[ev_halloweentwo5.hint]")

                    #Porcelain Labyrinth (halloweentwo6)
                    if (not ev_halloweentwo6.completed and not ev_halloweentwo6.missed) or show_complete:
                        text ("[ev_halloweentwo6.hint]")

                    #The First Signs of Fraying Threads (halloweentwo7)
                    if (not ev_halloweentwo7.completed and not ev_halloweentwo7.missed) or show_complete:
                        text ("[ev_halloweentwo7.hint]")

                    #Official Unofficial Double Date (halloweentwo8)
                    if (not ev_halloweentwo8.completed and not ev_halloweentwo8.missed) or show_complete:
                        text ("[ev_halloweentwo8.hint]")

                    #In Circles (halloweentwo9)
                    if (not ev_halloweentwo9.completed and not ev_halloweentwo9.missed) or show_complete:
                        text ("[ev_halloweentwo9.hint]")

                    #Escape Rope (halloweentwo10)
                    if (not ev_halloweentwo10.completed and not ev_halloweentwo10.missed) or show_complete:
                        text ("[ev_halloweentwo10.hint]")

                    #Lavender's Green (halloweentwo11)
                    if (not ev_halloweentwo11.completed and not ev_halloweentwo11.missed) or show_complete:
                        text ("[ev_halloweentwo11.hint]")

                    #Gallows Edge (halloweentwo12)
                    if (not ev_halloweentwo12.completed and not ev_halloweentwo12.missed) or show_complete:
                        text ("[ev_halloweentwo12.hint]")

                    #Metal in Microwaves (halloweentwo13)
                    if (not ev_halloweentwo13.completed and not ev_halloweentwo13.missed) or show_complete:
                        text ("[ev_halloweentwo13.hint]")

                    #Three Amigos (christmastwo1)
                    if (not ev_christmastwo1.completed and not ev_christmastwo1.missed) or show_complete:
                        text ("[ev_christmastwo1.hint]")

                    #The Reliable and Totally Legitimate Princess Imani (christmastwo2)
                    if (not ev_christmastwo2.completed and not ev_christmastwo2.missed) or show_complete:
                        text ("[ev_christmastwo2.hint]")

                    #Room to Grow (christmastwo3)
                    if (not ev_christmastwo3.completed and not ev_christmastwo3.missed) or show_complete:
                        text ("[ev_christmastwo3.hint]")

                    #Dodging Snowflakes (christmastwo4)
                    if (not ev_christmastwo4.completed and not ev_christmastwo4.missed) or show_complete:
                        text ("[ev_christmastwo4.hint]")

                    #Everything Evil (christmastwo5)
                    if (not ev_christmastwo5.completed and not ev_christmastwo5.missed) or show_complete:
                        text ("[ev_christmastwo5.hint]")

                    #Tokimeki Labyrinth (christmastwo6)
                    if (not ev_christmastwo6.completed and not ev_christmastwo6.missed) or show_complete:
                        text ("[ev_christmastwo6.hint]")

                    #Love Set to Max (Class Warfare) (christmastwo7)
                    if (not ev_christmastwo7.completed and not ev_christmastwo7.missed) or show_complete:
                        text ("[ev_christmastwo7.hint]")

                    #Dohoonkabhankoloos (christmastwo8)
                    if (not ev_christmastwo8.completed and not ev_christmastwo8.missed) or show_complete:
                        text ("[ev_christmastwo8.hint]")

                    #Fear of Missing Out (christmastwo9)
                    if (not ev_christmastwo9.completed and not ev_christmastwo9.missed) or show_complete:
                        text ("[ev_christmastwo9.hint]")

                    #Walking on Eggshells (christmastwo10)
                    if (not ev_christmastwo10.completed and not ev_christmastwo10.missed) or show_complete:
                        text ("[ev_christmastwo10.hint]")

                    #New Age Entrepreneurs (christmastwo11)
                    if (not ev_christmastwo11.completed and not ev_christmastwo11.missed) or show_complete:
                        text ("[ev_christmastwo11.hint]")

                    #The Smile, The Face (christmastwo12)
                    if (not ev_christmastwo12.completed and not ev_christmastwo12.missed) or show_complete:
                        text ("[ev_christmastwo12.hint]")

                    #Shadowmeld (christmastwo13)
                    if (not ev_christmastwo13.completed and not ev_christmastwo13.missed) or show_complete:
                        text ("[ev_christmastwo13.hint]")

                    #Chashu (A Cracked Bowl) (christmastwo14)
                    if (not ev_christmastwo14.completed and not ev_christmastwo14.missed) or show_complete:
                        text ("[ev_christmastwo14.hint]")

                    #A Way's Away (christmastwo15)
                    if (not ev_christmastwo15.completed and not ev_christmastwo15.missed) or show_complete:
                        text ("[ev_christmastwo15.hint]")

                    #No Escape (christmastwo16)
                    if (not ev_christmastwo16.completed and not ev_christmastwo16.missed) or show_complete:
                        text ("[ev_christmastwo16.hint]")

                    #Spotless Mind (christmastwo17)
                    if (not ev_christmastwo17.completed and not ev_christmastwo17.missed) or show_complete:
                        text ("[ev_christmastwo17.hint]")

                    #Me Without You (christmastwo18)
                    if (not ev_christmastwo18.completed and not ev_christmastwo18.missed) or show_complete:
                        text ("[ev_christmastwo18.hint]")

                    #The Color White (christmastwo19)
                    if (not ev_christmastwo19.completed and not ev_christmastwo19.missed) or show_complete:
                        text ("[ev_christmastwo19.hint]")

                    #Glued to the Sky (christmastwo20)
                    if (not ev_christmastwo20.completed and not ev_christmastwo20.missed) or show_complete:
                        text ("[ev_christmastwo20.hint]")

                    #The Light of Last Summer (returntosummer1)
                    if (not ev_returntosummer1.completed and not ev_returntosummer1.missed) or show_complete:
                        text ("[ev_returntosummer1.hint]")

                    #A Life of Prizes (returntosummer2)
                    if (not ev_returntosummer2.completed and not ev_returntosummer2.missed) or show_complete:
                        text ("[ev_returntosummer2.hint]")

                    #Utinam Ne Illum Numquam Conspexissem (returntosummer3)
                    if (not ev_returntosummer3.completed and not ev_returntosummer3.missed) or show_complete:
                        text ("[ev_returntosummer3.hint]")

        vbox:
            area (0,0,1450,8)

        hbox:
            ypos 20

            if dark_mode:
                textbutton _("Back") action ShowMenu("progressmod_dark")
            else:
                textbutton _("Back") action ShowMenu("progressmod")
            textbutton _("       Toggle Completed") action SetVariable("show_complete", not show_complete)
            if show_hints:
                textbutton _("       Hints") action ShowMenu("hinttracker")
