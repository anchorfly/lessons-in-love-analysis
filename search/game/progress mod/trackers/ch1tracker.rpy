screen maintrackerch1m():

    tag menu

    use game_menu(_("Chapter 1"), scroll="viewport"):

        null

    key "m" action Return()

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    $ if show_complete: ch1_scroll = (MainEvent.max[1] - MainEvent.max[0]) * 26
    $ if not show_complete: ch1_scroll = (MainEvent.max[1] - (MainEvent.max[0] + chap1point)) * 26

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
                    textbutton _(">") action ShowMenu("maintrackerch2m")

        viewport:
            ypos 35
            area (0,0,1450,870)
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            child_size (None,ch1_scroll)

            vbox:
                style_prefix "tracker"

                if everyday and show_complete:
                    textbutton _("Every Day I Grow Some More {b}✓{/b}") action Replay("start", locked=False) text_style "modmybutton"
                elif not everyday and not ev_everyday.missed:
                    text _("Every Day I Grow Some More")
                if clichebath and show_complete:
                    textbutton _("A New You {b}✓{/b}") action Replay("startsleepover", locked=False) text_style "modmybutton"
                elif not clichebath and not ev_clichebath.missed:
                    text _("A New You")
                if amiawake and show_complete:
                    textbutton _("Am I Awake? {b}✓{/b}") action Replay("amiawake", locked=False) text_style "modmybutton"
                elif not amiawake and not ev_amiawake.missed:
                    text _("Am I Awake?")
                if firstclass and show_complete:
                    textbutton _("First (?) Day of School {b}✓{/b}") action Replay("thefirstclass", locked=False) text_style "modmybutton"
                elif not firstclass and not ev_firstclass.missed:
                    text _("First (?) Day of School")
                if sleepover and show_complete:
                    textbutton _("Slumber Party {b}✓{/b}") action Replay("slumparty", locked=False) text_style "modmybutton"
                elif not sleepover and not ev_sleepover.missed:
                    text _("Slumber Party")
                if day5 and show_complete:
                    textbutton _("The Devil Incarnate {b}✓{/b}") action Replay("day5", locked=False) text_style "modmybutton"
                elif not day5 and not ev_day5.missed:
                    text _("The Devil Incarnate")
                if day7 and show_complete:
                    textbutton _("Super Secret Sex Dungeon {b}✓{/b}") action Replay("day7", locked=False) text_style "modmybutton"
                elif not day7 and not ev_day7.missed:
                    text _("Super Secret Sex Dungeon")
                if day8 and show_complete:
                    textbutton _("Delinquent {b}✓{/b}") action Replay("day8", locked=False) text_style "modmybutton"
                elif not day8 and not ev_day8.missed:
                    text _("Delinquent")
                if day12 and show_complete:
                    textbutton _("Mitochondria {b}✓{/b}") action Replay("day12", locked=False) text_style "modmybutton"
                elif not day12 and not ev_day12.missed:
                    text _("Mitochondria")
                if day14 and show_complete:
                    textbutton _("Self-Esteem {b}✓{/b}") action Replay("day14", locked=False) text_style "modmybutton"
                elif not day14 and not ev_day14.missed:
                    text _("Self-Esteem")
                if day16 and show_complete:
                    textbutton _("Operation: Fallen Angel {b}✓{/b}") action Replay("day16", locked=False) text_style "modmybutton"
                elif not day16 and not ev_day16.missed:
                    text _("Operation: Fallen Angel")
                if day20 and show_complete:
                    textbutton _("I Thought of You {b}✓{/b}") action Replay("day20", locked=False) text_style "modmybutton"
                elif not day20 and not ev_day20.missed:
                    text _("I Thought of You")
                if day21 and show_complete:
                    textbutton _("Not Even Me {b}✓{/b}") action Replay("day21", locked=False) text_style "modmybutton"
                elif not day21 and not ev_day21.missed:
                    text _("Not Even Me")
                if day24 and show_complete:
                    textbutton _("No Romeo {b}✓{/b}") action Replay("day24", locked=False) text_style "modmybutton"
                elif not day24 and not ev_day24.missed:
                    text _("No Romeo")
                if day26 and show_complete:
                    textbutton _("Outside of Everything {b}✓{/b}") action Replay("day26", locked=False) text_style "modmybutton"
                elif not day26 and not ev_day26.missed:
                    text _("Outside of Everything")
                if day28 and show_complete:
                    textbutton _("Ponytail {b}✓{/b}") action Replay("day28", locked=False) text_style "modmybutton"
                elif not day28 and not ev_day28.missed:
                    text _("Ponytail")
                if day30 and show_complete:
                    textbutton _("Drowning {b}✓{/b}") action Replay("day30", locked=False) text_style "modmybutton"
                elif not day30 and not ev_day30.missed:
                    text _("Drowning")
                if day33 and show_complete:
                    textbutton _("So Many Voices {b}✓{/b}") action Replay("day33", locked=False) text_style "modmybutton"
                elif not day33 and not ev_day33.missed:
                    text _("So Many Voices")
                if day36 and show_complete:
                    textbutton _("Cleaning Duty {b}✓{/b}") action Replay("day36", locked=False) text_style "modmybutton"
                elif not day36 and not ev_day36.missed:
                    text _("Cleaning Duty")
                if day38 and show_complete:
                    textbutton _("Walk in the Park {b}✓{/b}") action Replay("day38", locked=False) text_style "modmybutton"
                elif not day38 and not ev_day38.missed:
                    text _("Walk in the Park")
                if day40 and show_complete:
                    textbutton _("Saved by the Bell {b}✓{/b}") action Replay("day40", locked=False) text_style "modmybutton"
                elif not day40 and not ev_day40.missed:
                    text _("Saved by the Bell")
                if day44 and show_complete:
                    textbutton _("This Town Has Two Halves {b}✓{/b}") action Replay("day44", locked=False) text_style "modmybutton"
                elif not day44 and not ev_day44.missed:
                    text _("This Town Has Two Halves")
                if day48 and show_complete:
                    textbutton _("Little Girl {b}✓{/b}") action Replay("day48", locked=False) text_style "modmybutton"
                elif not day48 and not ev_day48.missed:
                    text _("Little Girl")
                if day50 and show_complete:
                    textbutton _("Missing {b}✓{/b}") action Replay("day50", locked=False) text_style "modmybutton"
                elif not day50 and not ev_day50.missed:
                    text _("Missing")
                if day54 and show_complete:
                    textbutton _("The Sakakibara Diet {b}✓{/b}") action Replay("day54", locked=False) text_style "modmybutton"
                elif not day54 and not ev_day54.missed:
                    text _("The Sakakibara Diet")
                if day56 and show_complete:
                    textbutton _("Normal Office Visit {b}✓{/b}") action Replay("day56", locked=False) text_style "modmybutton"
                elif not day56 and not ev_day56.missed:
                    text _("Normal Office Visit")
                if day60 and show_complete:
                    textbutton _("O World (In Our Final Moments) {b}✓{/b}") action Replay("day60", locked=False) text_style "modmybutton"
                elif not day60 and not ev_day60.missed:
                    text _("O World (In Our Final Moments)")
                if day63 and show_complete:
                    textbutton _("One to Seven {b}✓{/b}") action Replay("day63", locked=False) text_style "modmybutton"
                elif not day63 and not ev_day63.missed:
                    text _("One to Seven")
                if day65 and show_complete:
                    textbutton _("Girl-Talk {b}✓{/b}") action Replay("day65", locked=False) text_style "modmybutton"
                elif not day65 and not ev_day65.missed:
                    text _("Girl-Talk")
                if day70 and show_complete:
                    textbutton _("The 'S' Word {b}✓{/b}") action Replay("day70", locked=False) text_style "modmybutton"
                elif not day70 and not ev_day70.missed:
                    text _("The 'S' Word")
                if day72 and show_complete:
                    textbutton _("Weight Limit {b}✓{/b}") action Replay("day72", locked=False) text_style "modmybutton"
                elif not day72 and not ev_day72.missed:
                    text _("Weight Limit")
                if day77 and show_complete:
                    textbutton _("Slope Intercept Form {b}✓{/b}") action Replay("day77", locked=False) text_style "modmybutton"
                elif not day77 and not ev_day77.missed:
                    text _("Slope Intercept Form")
                if day79 and show_complete:
                    textbutton _("Scientific Research {b}✓{/b}") action Replay("day79", locked=False) text_style "modmybutton"
                elif not day79 and not ev_day79.missed:
                    text _("Scientific Research")
                if day80 and show_complete:
                    textbutton _("Secret Ingredient {b}✓{/b}") action Replay("day80", locked=False) text_style "modmybutton"
                elif not day80 and not ev_day80.missed:
                    text _("Secret Ingredient")
                if day83 and show_complete:
                    textbutton _("Parasite {b}✓{/b}") action Replay("day83", locked=False) text_style "modmybutton"
                elif not day83 and not ev_day83.missed:
                    text _("Parasite")
                if day85 and show_complete:
                    textbutton _("Contractions {b}✓{/b}") action Replay("day85", locked=False) text_style "modmybutton"
                elif not day85 and not ev_day85.missed:
                    text _("Contractions")
                if day89 and show_complete:
                    textbutton _("Milk, Eggs, and Water {b}✓{/b}") action Replay("day89", locked=False) text_style "modmybutton"
                elif not day89 and not ev_day89.missed:
                    text _("Milk, Eggs, and Water")
                if day91 and show_complete:
                    textbutton _("Stronger I Become {b}✓{/b}") action Replay("day91", locked=False) text_style "modmybutton"
                elif not day91 and not ev_day91.missed:
                    text _("Stronger I Become")
                if day96 and show_complete:
                    textbutton _("Recall {b}✓{/b}") action Replay("day96", locked=False) text_style "modmybutton"
                elif not day96 and not ev_day96.missed:
                    text _("Recall")
                if day102 and show_complete:
                    textbutton _("Rewrite {b}✓{/b}") action Replay("day102", locked=False) text_style "modmybutton"
                elif not day102 and not ev_day102.missed:
                    text _("Rewrite")
                if day103 and show_complete:
                    textbutton _("Reset {b}✓{/b}") action Replay("day103", locked=False) text_style "modmybutton"
                elif not day103 and not ev_day103.missed:
                    text _("Reset")
                if day110 and show_complete:
                    textbutton _("Cursed Birds {b}✓{/b}") action Replay("day110", locked=False) text_style "modmybutton"
                elif not day110 and not ev_day110.missed:
                    text _("Cursed Birds")
                if day114 and show_complete:
                    textbutton _("Human Trafficking {b}✓{/b}") action Replay("day114", locked=False) text_style "modmybutton"
                elif not day114 and not ev_day114.missed:
                    text _("Human Trafficking")
                if day120 and show_complete:
                    textbutton _("Girl Talk Pt. II {b}✓{/b}") action Replay("day120", locked=False) text_style "modmybutton"
                elif not day120 and not ev_day120.missed:
                    text _("Girl Talk Pt. II")
                if day121 and show_complete:
                    textbutton _("A Different View {b}✓{/b}") action Replay("day121", locked=False) text_style "modmybutton"
                elif not day121 and not ev_day121.missed:
                    text _("A Different View")
                if day126 and show_complete:
                    textbutton _("On The Bright Side {b}✓{/b}") action Replay("day126", locked=False) text_style "modmybutton"
                elif not day126 and not ev_day126.missed:
                    text _("On The Bright Side")
                if day128 and show_complete:
                    textbutton _("Everything Horrible {b}✓{/b}") action Replay("day128", locked=False) text_style "modmybutton"
                elif not day128 and not ev_day128.missed:
                    text _("Everything Horrible")
                if day130 and show_complete:
                    textbutton _("Erotic Game Protagonist {b}✓{/b}") action Replay("day130", locked=False) text_style "modmybutton"
                elif not day130 and not ev_day130.missed:
                    text _("Erotic Game Protagonist")
                if day138 and show_complete:
                    textbutton _("Rumors {b}✓{/b}") action Replay("day138", locked=False) text_style "modmybutton"
                elif not day138 and not ev_day138.missed:
                    text _("Rumors")
                if day140 and show_complete:
                    textbutton _("The Gem of the Emerald Isle {b}✓{/b}") action Replay("day140", locked=False) text_style "modmybutton"
                elif not day140 and not ev_day140.missed:
                    text _("The Gem of the Emerald Isle")
                if day142 and show_complete:
                    textbutton _("Size Matters {b}✓{/b}") action Replay("day142", locked=False) text_style "modmybutton"
                elif not day142 and not ev_day142.missed:
                    text _("Size Matters")
                if day144 and show_complete:
                    textbutton _("Tsuneyo Tojo, Stand-up Comedian {b}✓{/b}") action Replay("day144", locked=False) text_style "modmybutton"
                elif not day144 and not ev_day144.missed:
                    text _("Tsuneyo Tojo, Stand-up Comedian")
                if day150 and show_complete:
                    textbutton _("A Proper Introduction {b}✓{/b}") action Replay("day150", locked=False) text_style "modmybutton"
                elif not day150 and not ev_day150.missed:
                    text _("A Proper Introduction")
                if day153 and show_complete:
                    textbutton _("Supreme Overlord {b}✓{/b}") action Replay("day153", locked=False) text_style "modmybutton"
                elif not day153 and not ev_day153.missed:
                    text _("Supreme Overlord")
                if day154 and show_complete:
                    textbutton _("Lifting the Curse {b}✓{/b}") action Replay("day154", locked=False) text_style "modmybutton"
                elif not day154 and not ev_day154.missed:
                    text _("Lifting the Curse")
                if beachvacation1 and show_complete:
                    textbutton _("What's Done is Done {b}✓{/b}") action Replay("beachvacation1", locked=False) text_style "modmybutton"
                elif not beachvacation1 and not ev_beachvacation1.missed:
                    text _("What's Done is Done")
                if beachvacation2 and show_complete:
                    textbutton _("All Along the Shoreline {b}✓{/b}") action Replay("beachvacation2", locked=False) text_style "modmybutton"
                elif not beachvacation2 and not ev_beachvacation2.missed:
                    text _("All Along the Shoreline")
                if beachvacation3 and show_complete:
                    textbutton _("My Heart is Full {b}✓{/b}") action Replay("beachvacation3", locked=False) text_style "modmybutton"
                elif not beachvacation3 and not ev_beachvacation3.missed:
                    text _("My Heart is Full")
                if beachvacation4 and show_complete:
                    textbutton _("Extra French Fries {b}✓{/b}") action Replay("beachvacation4", locked=False) text_style "modmybutton"
                elif not beachvacation4 and not ev_beachvacation4.missed:
                    text _("Extra French Fries")
                if beachvacation5 and show_complete:
                    textbutton _("Behind a Bathroom, Under the Blazing Sun {b}✓{/b}") action Replay("beachvacation5", locked=False) text_style "modmybutton"
                elif not beachvacation5 and not ev_beachvacation5.missed:
                    text _("Behind a Bathroom, Under the Blazing Sun")
                if beachvacation6 and show_complete:
                    textbutton _("Three Girls in a Line on the Beach {b}✓{/b}") action Replay("beachvacation6", locked=False) text_style "modmybutton"
                elif not beachvacation6 and not ev_beachvacation6.missed:
                    text _("Three Girls in a Line on the Beach")
                if beachvacation7 and show_complete:
                    textbutton _("The Moon is Beautiful {b}✓{/b}") action Replay("beachvacation7", locked=False) text_style "modmybutton"
                elif not beachvacation7 and not ev_beachvacation7.missed:
                    text _("The Moon is Beautiful")
                if beachvacation8 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. I {b}✓{/b}") action Replay("beachvacation8", locked=False) text_style "modmybutton"
                elif not beachvacation8 and not ev_beachvacation8.missed:
                    text _("The Legacy of Thaum Pt. I")
                if beachvacation9 and show_complete:
                    textbutton _("Summer and Winter {b}✓{/b}") action Replay("beachvacation9", locked=False) text_style "modmybutton"
                elif not beachvacation9 and not ev_beachvacation9.missed:
                    text _("Summer and Winter")
                if beachvacation10 and show_complete:
                    textbutton _("Where Puppies Roam Free {b}✓{/b}") action Replay("beachvacation10", locked=False) text_style "modmybutton"
                elif not beachvacation10 and not ev_beachvacation10.missed:
                    text _("Where Puppies Roam Free")
                if beachvacation11 and show_complete:
                    textbutton _("Die For What You Believe In {b}✓{/b}") action Replay("beachvacation11", locked=False) text_style "modmybutton"
                elif not beachvacation11 and not ev_beachvacation11.missed:
                    text _("Die For What You Believe In")
                if beachvacation12 and show_complete:
                    textbutton _("Reverse Cowgirl {b}✓{/b}") action Replay("beachvacation12", locked=False) text_style "modmybutton"
                elif not beachvacation12 and not ev_beachvacation12.missed:
                    text _("Reverse Cowgirl")
                if beachvacation13 and show_complete:
                    textbutton _("Smile Guide {b}✓{/b}") action Replay("beachvacation13", locked=False) text_style "modmybutton"
                elif not beachvacation13 and not ev_beachvacation13.missed:
                    text _("Smile Guide")
                if beachvacation14 and show_complete:
                    textbutton _("Prayer Position {b}✓{/b}") action Replay("beachvacation14", locked=False) text_style "modmybutton"
                elif not beachvacation14 and not ev_beachvacation14.missed:
                    text _("Prayer Position")
                if beachvacation15 and show_complete:
                    textbutton _("Cry. Cry. Cry. {b}✓{/b}") action Replay("beachvacation15", locked=False) text_style "modmybutton"
                elif not beachvacation15 and not ev_beachvacation15.missed:
                    text _("Cry. Cry. Cry.")
                if beachvacation16 and show_complete:
                    textbutton _("See You in the Morning {b}✓{/b}") action Replay("beachvacation16", locked=False) text_style "modmybutton"
                elif not beachvacation16 and not ev_beachvacation16.missed:
                    text _("See You in the Morning")
                if halloween1 and show_complete:
                    textbutton _("The Value of Sharing {b}✓{/b}") action Replay("halloween1", locked=False) text_style "modmybutton"
                elif not halloween1 and not ev_halloween1.missed:
                    text _("The Value of Sharing")
                if halloween2 and show_complete:
                    textbutton _("Guest of Honor {b}✓{/b}") action Replay("halloween2", locked=False) text_style "modmybutton"
                elif not halloween2 and not ev_halloween2.missed:
                    text _("Guest of Honor")
                if halloween3 and show_complete:
                    textbutton _("The Meat has Come {b}✓{/b}") action Replay("halloween3", locked=False) text_style "modmybutton"
                elif not halloween3 and not ev_halloween3.missed:
                    text _("The Meat has Come")
                if halloween4 and show_complete:
                    textbutton _("Mysterious Abundance of Chickens {b}✓{/b}") action Replay("halloween4", locked=False) text_style "modmybutton"
                elif not halloween4 and not ev_halloween4.missed:
                    text _("Mysterious Abundance of Chickens")
                if halloween5 and show_complete:
                    textbutton _("Sexy Land {b}✓{/b}") action Replay("halloween5", locked=False) text_style "modmybutton"
                elif not halloween5 and not ev_halloween5.missed:
                    text _("Sexy Land")
                if halloween6 and show_complete:
                    textbutton _("They're Just Lights {b}✓{/b}") action Replay("halloween6", locked=False) text_style "modmybutton"
                elif not halloween6 and not ev_halloween6.missed:
                    text _("They're Just Lights")
                if halloween7 and show_complete:
                    textbutton _("Once, Twice, Ten Times {b}✓{/b}") action Replay("halloween7", locked=False) text_style "modmybutton"
                elif not halloween7 and not ev_halloween7.missed:
                    text _("Once, Twice, Ten Times")
                if halloween8 and show_complete:
                    textbutton _("Mechanical Bull {b}✓{/b}") action Replay("halloween8", locked=False) text_style "modmybutton"
                elif not halloween8 and not ev_halloween8.missed:
                    text _("Mechanical Bull")
                if halloween9 and show_complete:
                    textbutton _("At Least It's Not Christmas {b}✓{/b}") action Replay("halloween9", locked=False) text_style "modmybutton"
                elif not halloween9 and not ev_halloween9.missed:
                    text _("At Least It's Not Christmas")
                if halloween10 and show_complete:
                    textbutton _("Samhain {b}✓{/b}") action Replay("halloween10", locked=False) text_style "modmybutton"
                elif not halloween10 and not ev_halloween10.missed:
                    text _("Samhain")
                if halloween11 and show_complete:
                    textbutton _("Wicked Witch of Kumon-mi {b}✓{/b}") action Replay("halloween11", locked=False) text_style "modmybutton"
                elif not halloween11 and not ev_halloween11.missed:
                    text _("Wicked Witch of Kumon-mi")
                if halloween12 and show_complete:
                    textbutton _("The Depressing Implication of Goosebumps {b}✓{/b}") action Replay("halloween12", locked=False) text_style "modmybutton"
                elif not halloween12 and not ev_halloween12.missed:
                    text _("The Depressing Implication of Goosebumps")
                if halloween13 and show_complete:
                    textbutton _("Pry With a Smile {b}✓{/b}") action Replay("halloween13", locked=False) text_style "modmybutton"
                elif not halloween13 and not ev_halloween13.missed:
                    text _("Pry With a Smile")
                if halloween14 and show_complete:
                    textbutton _("Kadrillionbilliontrillion {b}✓{/b}") action Replay("halloween14", locked=False) text_style "modmybutton"
                elif not halloween14 and not ev_halloween14.missed:
                    text _("Kadrillionbilliontrillion")
                if day214 and show_complete:
                    textbutton _("As Loud as a Whisper Can Be {b}✓{/b}") action Replay("day214", locked=False) text_style "modmybutton"
                elif not day214 and not ev_day214.missed:
                    text _("As Loud as a Whisper Can Be")
                if day215 and show_complete:
                    textbutton _("Two Wooden Doors {b}✓{/b}") action Replay("day215", locked=False) text_style "modmybutton"
                elif not day215 and not ev_day215.missed:
                    text _("Two Wooden Doors")
                if day216 and show_complete:
                    textbutton _("Happy Places {b}✓{/b}") action Replay("day216", locked=False) text_style "modmybutton"
                elif not day216 and not ev_day216.missed:
                    text _("Happy Places")
                if day217 and show_complete:
                    textbutton _("Tradition {b}✓{/b}") action Replay("day217", locked=False) text_style "modmybutton"
                elif not day217 and not ev_day217.missed:
                    text _("Tradition")
                if day218 and show_complete:
                    textbutton _("Stray Cat {b}✓{/b}") action Replay("day218", locked=False) text_style "modmybutton"
                elif not day218 and not ev_day218.missed:
                    text _("Stray Cat")
                if day220 and show_complete:
                    textbutton _("There is Nothing {b}✓{/b}") action Replay("day220", locked=False) text_style "modmybutton"
                elif not day220 and not ev_day220.missed:
                    text _("There is Nothing")
                if hoorayanotherreset and show_complete:
                    textbutton _("Changing of Seasons {b}✓{/b}") action Replay("hoorayanotherreset", locked=False) text_style "modmybutton"
                elif not hoorayanotherreset and not ev_hoorayanotherreset.missed:
                    text _("Changing of Seasons")

################################################################################

            if show_hints == True and not _in_replay:

                vbox:
                    xpos .4
                    style_prefix "tracker"

                    #Every Day I Grow Some More (everyday)
                    if (not ev_everyday.completed and not ev_everyday.missed) or show_complete:
                        text ("[ev_everyday.hint]")

                    #A New You (clichebath)
                    if (not ev_clichebath.completed and not ev_clichebath.missed) or show_complete:
                        text ("[ev_clichebath.hint]")

                    #Am I Awake? (amiawake)
                    if (not ev_amiawake.completed and not ev_amiawake.missed) or show_complete:
                        text ("[ev_amiawake.hint]")

                    #First (?) Day of School (firstclass)
                    if (not ev_firstclass.completed and not ev_firstclass.missed) or show_complete:
                        text ("[ev_firstclass.hint]")

                    #Slumber Party (sleepover)
                    if (not ev_sleepover.completed and not ev_sleepover.missed) or show_complete:
                        text ("[ev_sleepover.hint]")

                    #The Devil Incarnate (day5)
                    if (not ev_day5.completed and not ev_day5.missed) or show_complete:
                        text ("[ev_day5.hint]")

                    #Super Secret Sex Dungeon (day7)
                    if (not ev_day7.completed and not ev_day7.missed) or show_complete:
                        text ("[ev_day7.hint]")

                    #Delinquent (day8)
                    if (not ev_day8.completed and not ev_day8.missed) or show_complete:
                        text ("[ev_day8.hint]")

                    #Mitochondria (day12)
                    if (not ev_day12.completed and not ev_day12.missed) or show_complete:
                        text ("[ev_day12.hint]")

                    #Self-Esteem (day14)
                    if (not ev_day14.completed and not ev_day14.missed) or show_complete:
                        text ("[ev_day14.hint]")

                    #Operation: Fallen Angel (day16)
                    if (not ev_day16.completed and not ev_day16.missed) or show_complete:
                        text ("[ev_day16.hint]")

                    #I Thought of You (day20)
                    if (not ev_day20.completed and not ev_day20.missed) or show_complete:
                        text ("[ev_day20.hint]")

                    #Not Even Me (day21)
                    if (not ev_day21.completed and not ev_day21.missed) or show_complete:
                        text ("[ev_day21.hint]")

                    #No Romeo (day24)
                    if (not ev_day24.completed and not ev_day24.missed) or show_complete:
                        text ("[ev_day24.hint]")

                    #Outside of Everything (day26)
                    if (not ev_day26.completed and not ev_day26.missed) or show_complete:
                        text ("[ev_day26.hint]")

                    #Ponytail (day28)
                    if (not ev_day28.completed and not ev_day28.missed) or show_complete:
                        text ("[ev_day28.hint]")

                    #Drowning (day30)
                    if (not ev_day30.completed and not ev_day30.missed) or show_complete:
                        text ("[ev_day30.hint]")

                    #So Many Voices (day33)
                    if (not ev_day33.completed and not ev_day33.missed) or show_complete:
                        text ("[ev_day33.hint]")

                    #Cleaning Duty (day36)
                    if (not ev_day36.completed and not ev_day36.missed) or show_complete:
                        text ("[ev_day36.hint]")

                    #Walk in the Park (day38)
                    if (not ev_day38.completed and not ev_day38.missed) or show_complete:
                        text ("[ev_day38.hint]")

                    #Saved by the Bell (day40)
                    if (not ev_day40.completed and not ev_day40.missed) or show_complete:
                        text ("[ev_day40.hint]")

                    #This Town Has Two Halves (day44)
                    if (not ev_day44.completed and not ev_day44.missed) or show_complete:
                        text ("[ev_day44.hint]")

                    #Little Girl (day48)
                    if (not ev_day48.completed and not ev_day48.missed) or show_complete:
                        text ("[ev_day48.hint]")

                    #Missing (day50)
                    if (not ev_day50.completed and not ev_day50.missed) or show_complete:
                        text ("[ev_day50.hint]")

                    #The Sakakibara Diet (day54)
                    if (not ev_day54.completed and not ev_day54.missed) or show_complete:
                        text ("[ev_day54.hint]")

                    #Normal Office Visit (day56)
                    if (not ev_day56.completed and not ev_day56.missed) or show_complete:
                        text ("[ev_day56.hint]")

                    #O World (In Our Final Moments) (day60)
                    if (not ev_day60.completed and not ev_day60.missed) or show_complete:
                        text ("[ev_day60.hint]")

                    #One to Seven (day63)
                    if (not ev_day63.completed and not ev_day63.missed) or show_complete:
                        text ("[ev_day63.hint]")

                    #Girl-Talk (day65)
                    if (not ev_day65.completed and not ev_day65.missed) or show_complete:
                        text ("[ev_day65.hint]")

                    #The 'S' Word (day70)
                    if (not ev_day70.completed and not ev_day70.missed) or show_complete:
                        text ("[ev_day70.hint]")

                    #Weight Limit (day72)
                    if (not ev_day72.completed and not ev_day72.missed) or show_complete:
                        text ("[ev_day72.hint]")

                    #Slope Intercept Form (day77)
                    if (not ev_day77.completed and not ev_day77.missed) or show_complete:
                        text ("[ev_day77.hint]")

                    #Scientific Research (day79)
                    if (not ev_day79.completed and not ev_day79.missed) or show_complete:
                        text ("[ev_day79.hint]")

                    #Secret Ingredient (day80)
                    if (not ev_day80.completed and not ev_day80.missed) or show_complete:
                        text ("[ev_day80.hint]")

                    #Parasite (day83)
                    if (not ev_day83.completed and not ev_day83.missed) or show_complete:
                        text ("[ev_day83.hint]")

                    #Contractions (day85)
                    if (not ev_day85.completed and not ev_day85.missed) or show_complete:
                        text ("[ev_day85.hint]")

                    #Milk, Eggs, and Water (day89)
                    if (not ev_day89.completed and not ev_day89.missed) or show_complete:
                        text ("[ev_day89.hint]")

                    #Stronger I Become (day91)
                    if (not ev_day91.completed and not ev_day91.missed) or show_complete:
                        text ("[ev_day91.hint]")

                    #Recall (day96)
                    if (not ev_day96.completed and not ev_day96.missed) or show_complete:
                        text ("[ev_day96.hint]")

                    #Rewrite (day102)
                    if (not ev_day102.completed and not ev_day102.missed) or show_complete:
                        text ("[ev_day102.hint]")

                    #Reset (day103)
                    if (not ev_day103.completed and not ev_day103.missed) or show_complete:
                        text ("[ev_day103.hint]")

                    #Cursed Birds (day110)
                    if (not ev_day110.completed and not ev_day110.missed) or show_complete:
                        text ("[ev_day110.hint]")

                    #Human Trafficking (day114)
                    if (not ev_day114.completed and not ev_day114.missed) or show_complete:
                        text ("[ev_day114.hint]")

                    #Girl Talk Pt. II (day120)
                    if (not ev_day120.completed and not ev_day120.missed) or show_complete:
                        text ("[ev_day120.hint]")

                    #A Different View (day121)
                    if (not ev_day121.completed and not ev_day121.missed) or show_complete:
                        text ("[ev_day121.hint]")

                    #On The Bright Side (day126)
                    if (not ev_day126.completed and not ev_day126.missed) or show_complete:
                        text ("[ev_day126.hint]")

                    #Everything Horrible (day128)
                    if (not ev_day128.completed and not ev_day128.missed) or show_complete:
                        text ("[ev_day128.hint]")

                    #Erotic Game Protagonist (day130)
                    if (not ev_day130.completed and not ev_day130.missed) or show_complete:
                        text ("[ev_day130.hint]")

                    #Rumors (day138)
                    if (not ev_day138.completed and not ev_day138.missed) or show_complete:
                        text ("[ev_day138.hint]")

                    #The Gem of the Emerald Isle (day140)
                    if (not ev_day140.completed and not ev_day140.missed) or show_complete:
                        text ("[ev_day140.hint]")

                    #Size Matters (day142)
                    if (not ev_day142.completed and not ev_day142.missed) or show_complete:
                        text ("[ev_day142.hint]")

                    #Tsuneyo Tojo, Stand-up Comedian (day144)
                    if (not ev_day144.completed and not ev_day144.missed) or show_complete:
                        text ("[ev_day144.hint]")

                    #A Proper Introduction (day150)
                    if (not ev_day150.completed and not ev_day150.missed) or show_complete:
                        text ("[ev_day150.hint]")

                    #Supreme Overlord (day153)
                    if (not ev_day153.completed and not ev_day153.missed) or show_complete:
                        text ("[ev_day153.hint]")

                    #Lifting the Curse (day154)
                    if (not ev_day154.completed and not ev_day154.missed) or show_complete:
                        text ("[ev_day154.hint]")

                    #What's Done is Done (beachvacation1)
                    if (not ev_beachvacation1.completed and not ev_beachvacation1.missed) or show_complete:
                        text ("[ev_beachvacation1.hint]")

                    #All Along the Shoreline (beachvacation2)
                    if (not ev_beachvacation2.completed and not ev_beachvacation2.missed) or show_complete:
                        text ("[ev_beachvacation2.hint]")

                    #My Heart is Full (beachvacation3)
                    if (not ev_beachvacation3.completed and not ev_beachvacation3.missed) or show_complete:
                        text ("[ev_beachvacation3.hint]")

                    #Extra French Fries (beachvacation4)
                    if (not ev_beachvacation4.completed and not ev_beachvacation4.missed) or show_complete:
                        text ("[ev_beachvacation4.hint]")

                    #Behind a Bathroom, Under the Blazing Sun (beachvacation5)
                    if (not ev_beachvacation5.completed and not ev_beachvacation5.missed) or show_complete:
                        text ("[ev_beachvacation5.hint]")

                    #Three Girls in a Line on the Beach (beachvacation6)
                    if (not ev_beachvacation6.completed and not ev_beachvacation6.missed) or show_complete:
                        text ("[ev_beachvacation6.hint]")

                    #The Moon is Beautiful (beachvacation7)
                    if (not ev_beachvacation7.completed and not ev_beachvacation7.missed) or show_complete:
                        text ("[ev_beachvacation7.hint]")

                    #The Legacy of Thaum Pt. I (beachvacation8)
                    if (not ev_beachvacation8.completed and not ev_beachvacation8.missed) or show_complete:
                        text ("[ev_beachvacation8.hint]")

                    #Summer and Winter (beachvacation9)
                    if (not ev_beachvacation9.completed and not ev_beachvacation9.missed) or show_complete:
                        text ("[ev_beachvacation9.hint]")

                    #Where Puppies Roam Free (beachvacation10)
                    if (not ev_beachvacation10.completed and not ev_beachvacation10.missed) or show_complete:
                        text ("[ev_beachvacation10.hint]")

                    #Die For What You Believe In (beachvacation11)
                    if (not ev_beachvacation11.completed and not ev_beachvacation11.missed) or show_complete:
                        text ("[ev_beachvacation11.hint]")

                    #Reverse Cowgirl (beachvacation12)
                    if (not ev_beachvacation12.completed and not ev_beachvacation12.missed) or show_complete:
                        text ("[ev_beachvacation12.hint]")

                    #Smile Guide (beachvacation13)
                    if (not ev_beachvacation13.completed and not ev_beachvacation13.missed) or show_complete:
                        text ("[ev_beachvacation13.hint]")

                    #Prayer Position (beachvacation14)
                    if (not ev_beachvacation14.completed and not ev_beachvacation14.missed) or show_complete:
                        text ("[ev_beachvacation14.hint]")

                    #Cry. Cry. Cry. (beachvacation15)
                    if (not ev_beachvacation15.completed and not ev_beachvacation15.missed) or show_complete:
                        text ("[ev_beachvacation15.hint]")

                    #See You in the Morning (beachvacation16)
                    if (not ev_beachvacation16.completed and not ev_beachvacation16.missed) or show_complete:
                        text ("[ev_beachvacation16.hint]")

                    #The Value of Sharing (halloween1)
                    if (not ev_halloween1.completed and not ev_halloween1.missed) or show_complete:
                        text ("[ev_halloween1.hint]")

                    #Guest of Honor (halloween2)
                    if (not ev_halloween2.completed and not ev_halloween2.missed) or show_complete:
                        text ("[ev_halloween2.hint]")

                    #The Meat has Come (halloween3)
                    if (not ev_halloween3.completed and not ev_halloween3.missed) or show_complete:
                        text ("[ev_halloween3.hint]")

                    #Mysterious Abundance of Chickens (halloween4)
                    if (not ev_halloween4.completed and not ev_halloween4.missed) or show_complete:
                        text ("[ev_halloween4.hint]")

                    #Sexy Land (halloween5)
                    if (not ev_halloween5.completed and not ev_halloween5.missed) or show_complete:
                        text ("[ev_halloween5.hint]")

                    #They're Just Lights (halloween6)
                    if (not ev_halloween6.completed and not ev_halloween6.missed) or show_complete:
                        text ("[ev_halloween6.hint]")

                    #Once, Twice, Ten Times (halloween7)
                    if (not ev_halloween7.completed and not ev_halloween7.missed) or show_complete:
                        text ("[ev_halloween7.hint]")

                    #Mechanical Bull (halloween8)
                    if (not ev_halloween8.completed and not ev_halloween8.missed) or show_complete:
                        text ("[ev_halloween8.hint]")

                    #At Least It's Not Christmas (halloween9)
                    if (not ev_halloween9.completed and not ev_halloween9.missed) or show_complete:
                        text ("[ev_halloween9.hint]")

                    #Samhain (halloween10)
                    if (not ev_halloween10.completed and not ev_halloween10.missed) or show_complete:
                        text ("[ev_halloween10.hint]")

                    #Wicked Witch of Kumon-mi (halloween11)
                    if (not ev_halloween11.completed and not ev_halloween11.missed) or show_complete:
                        text ("[ev_halloween11.hint]")

                    #The Depressing Implication of Goosebumps (halloween12)
                    if (not ev_halloween12.completed and not ev_halloween12.missed) or show_complete:
                        text ("[ev_halloween12.hint]")

                    #Pry With a Smile (halloween13)
                    if (not ev_halloween13.completed and not ev_halloween13.missed) or show_complete:
                        text ("[ev_halloween13.hint]")

                    #Kadrillionbilliontrillion (halloween14)
                    if (not ev_halloween14.completed and not ev_halloween14.missed) or show_complete:
                        text ("[ev_halloween14.hint]")

                    #As Loud as a Whisper Can Be (day214)
                    if (not ev_day214.completed and not ev_day214.missed) or show_complete:
                        text ("[ev_day214.hint]")

                    #Two Wooden Doors (day215)
                    if (not ev_day215.completed and not ev_day215.missed) or show_complete:
                        text ("[ev_day215.hint]")

                    #Happy Places (day216)
                    if (not ev_day216.completed and not ev_day216.missed) or show_complete:
                        text ("[ev_day216.hint]")

                    #Tradition (day217)
                    if (not ev_day217.completed and not ev_day217.missed) or show_complete:
                        text ("[ev_day217.hint]")

                    #Stray Cat (day218)
                    if (not ev_day218.completed and not ev_day218.missed) or show_complete:
                        text ("[ev_day218.hint]")

                    #There is Nothing (day220)
                    if (not ev_day220.completed and not ev_day220.missed) or show_complete:
                        text ("[ev_day220.hint]")

                    #Changing of Seasons (hoorayanotherreset)
                    if (not ev_hoorayanotherreset.completed and not ev_hoorayanotherreset.missed) or show_complete:
                        text ("[ev_hoorayanotherreset.hint]")

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
