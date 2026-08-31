screen maintrackerch4m():

    tag menu

    use game_menu(_("Chapter 4"), scroll="viewport"):

        null

    key "m" action Return()

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    $ if show_complete: ch4_scroll = (MainEvent.max[4] - MainEvent.max[3]) * 26
    $ if not show_complete: ch4_scroll = (MainEvent.max[4] - (MainEvent.max[3] + chap4point)) * 26

    vbox:
        xpos .25
        ypos 35
        area (0,0,1450,930)

        vbox:
            ypos 40
            hbox:
                vbox:
                    textbutton _("<") action ShowMenu("maintrackerch3m")
                vbox:
                    textbutton _(">") action ShowMenu("maintrackerch4m")

        viewport:
            ypos 35
            area (0,0,1450,870)
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            child_size (None,ch4_scroll)

            vbox:
                style_prefix "tracker"

                if springtime1 and show_complete:
                    textbutton _("The Collector {b}✓{/b}") action Replay("springtime1", locked=False) text_style "modmybutton"
                elif not springtime1 and not ev_springtime1.missed:
                    text _("The Collector")
                if springtime2 and show_complete:
                    textbutton _("On the Count of Three {b}✓{/b}") action Replay("springtime2", locked=False) text_style "modmybutton"
                elif not springtime2 and not ev_springtime2.missed:
                    text _("On the Count of Three")
                if springtime3 and show_complete:
                    textbutton _("Not the Nightingale {b}✓{/b}") action Replay("springtime3", locked=False) text_style "modmybutton"
                elif not springtime3 and not ev_springtime3.missed:
                    text _("Not the Nightingale")
                if springtime4 and show_complete:
                    textbutton _("Silver & Gold {b}✓{/b}") action Replay("springtime4", locked=False) text_style "modmybutton"
                elif not springtime4 and not ev_springtime4.missed:
                    text _("Silver & Gold")
                if springtime5 and show_complete:
                    textbutton _("November 1st {b}✓{/b}") action Replay("springtime5", locked=False) text_style "modmybutton"
                elif not springtime5 and not ev_springtime5.missed:
                    text _("November 1st")
                if springtime6 and show_complete:
                    textbutton _("Visibly Impatient {b}✓{/b}") action Replay("springtime6", locked=False) text_style "modmybutton"
                elif not springtime6 and not ev_springtime6.missed:
                    text _("Visibly Impatient")
                if springtime7 and show_complete:
                    textbutton _("The Final Human on the Face of the Earth {b}✓{/b}") action Replay("springtime7", locked=False) text_style "modmybutton"
                elif not springtime7 and not ev_springtime7.missed:
                    text _("The Final Human on the Face of the Earth")
                if springtime8 and show_complete:
                    textbutton _("Actual Jesus Quotes {b}✓{/b}") action Replay("springtime8", locked=False) text_style "modmybutton"
                elif not springtime8 and not ev_springtime8.missed:
                    text _("Actual Jesus Quotes")
                if springtime9 and show_complete:
                    textbutton _("In Regard to the Peony {b}✓{/b}") action Replay("springtime9", locked=False) text_style "modmybutton"
                elif not springtime9 and not ev_springtime9.missed:
                    text _("In Regard to the Peony")
                if springtime10 and show_complete:
                    textbutton _("When the Sun Sleeps {b}✓{/b}") action Replay("springtime10", locked=False) text_style "modmybutton"
                elif not springtime10 and not ev_springtime10.missed:
                    text _("When the Sun Sleeps")
                if springtime11 and show_complete:
                    textbutton _("Hunger Games {b}✓{/b}") action Replay("springtime11", locked=False) text_style "modmybutton"
                elif not springtime11 and not ev_springtime11.missed:
                    text _("Hunger Games")
                if springtime12 and show_complete:
                    textbutton _("Shut Up & Kiss {b}✓{/b}") action Replay("springtime12", locked=False) text_style "modmybutton"
                elif not springtime12 and not ev_springtime12.missed:
                    text _("Shut Up & Kiss")
                if springtime13 and show_complete:
                    textbutton _("Death (And Other Sad Stuff) {b}✓{/b}") action Replay("springtime13", locked=False) text_style "modmybutton"
                elif not springtime13 and not ev_springtime13.missed:
                    text _("Death (And Other Sad Stuff)")
                if springtime14 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. V: The Faceless Empyrean {b}✓{/b}") action Replay("springtime14", locked=False) text_style "modmybutton"
                elif not springtime14 and not ev_springtime14.missed:
                    text _("The Legacy of Thaum Pt. V: The Faceless Empyrean")
                if springtime15 and show_complete:
                    textbutton _("Goodnight Moon {b}✓{/b}") action Replay("springtime15", locked=False) text_style "modmybutton"
                elif not springtime15 and not ev_springtime15.missed:
                    text _("Goodnight Moon")
                if springtime16 and show_complete:
                    textbutton _("Your Blood in Spring {b}✓{/b}") action Replay("springtime16", locked=False) text_style "modmybutton"
                elif not springtime16 and not ev_springtime16.missed:
                    text _("Your Blood in Spring")
                if springtime17 and show_complete:
                    textbutton _("Rhythm of a Black Heart {b}✓{/b}") action Replay("springtime17", locked=False) text_style "modmybutton"
                elif not springtime17 and not ev_springtime17.missed:
                    text _("Rhythm of a Black Heart")
                if springtime18 and show_complete:
                    textbutton _("You & Me Against the World {b}✓{/b}") action Replay("springtime18", locked=False) text_style "modmybutton"
                elif not springtime18 and not ev_springtime18.missed:
                    text _("You & Me Against the World")
                if springtime19 and show_complete:
                    textbutton _("Miserably Ever After {b}✓{/b}") action Replay("springtime19", locked=False) text_style "modmybutton"
                elif not springtime19 and not ev_springtime19.missed:
                    text _("Miserably Ever After")
                if springend1 and show_complete:
                    textbutton _("Episcopalis: Pickled Plums & Polyrhythmic Psalms {b}✓{/b}") action Replay("springend1", locked=False) text_style "modmybutton"
                elif not springend1 and not ev_springend1.missed:
                    text _("Episcopalis: Pickled Plums & Polyrhythmic Psalms")
                if springend2 and show_complete:
                    textbutton _("Okonomiyaki {b}✓{/b}") action Replay("springend2", locked=False) text_style "modmybutton"
                elif not springend2 and not ev_springend2.missed:
                    text _("Okonomiyaki")
                if springend3 and show_complete:
                    textbutton _("500 Channels {b}✓{/b}") action Replay("springend3", locked=False) text_style "modmybutton"
                elif not springend3 and not ev_springend3.missed:
                    text _("500 Channels")
                if springend4 and show_complete:
                    textbutton _("Wild Boar {b}✓{/b}") action Replay("springend4", locked=False) text_style "modmybutton"
                elif not springend4 and not ev_springend4.missed:
                    text _("Wild Boar")
                if springend5 and show_complete:
                    textbutton _("All Eyes On Me {b}✓{/b}") action Replay("springend5", locked=False) text_style "modmybutton"
                elif not springend5 and not ev_springend5.missed:
                    text _("All Eyes On Me")
                if sportswars3 and show_complete:
                    textbutton _("War Never Changes: Egg Time Madness {b}✓{/b}") action Replay("sportswars3", locked=False) text_style "modmybutton"
                elif not sportswars3 and not ev_sportswars3.missed:
                    text _("War Never Changes: Egg Time Madness")
                if sportswars4 and show_complete:
                    textbutton _("Shohei Ohtani {b}✓{/b}") action Replay("sportswars4", locked=False) text_style "modmybutton"
                elif not sportswars4 and not ev_sportswars4.missed:
                    text _("Shohei Ohtani")
                if sportswars6 and show_complete:
                    textbutton _("Sea of Balls (Wise Turtle) {b}✓{/b}") action Replay("sportswars6", locked=False) text_style "modmybutton"
                elif not sportswars6 and not ev_sportswars6.missed:
                    text _("Sea of Balls (Wise Turtle)")
                if sportswars7 and show_complete:
                    textbutton _("Cock Party 2 (Better Than The First) {b}✓{/b}") action Replay("sportswars7", locked=False) text_style "modmybutton"
                elif not sportswars7 and not ev_sportswars7.missed:
                    text _("Cock Party 2 (Better Than The First)")
                if sportswars8 and show_complete:
                    textbutton _("Flowers & Forklifts {b}✓{/b}") action Replay("sportswars8", locked=False) text_style "modmybutton"
                elif not sportswars8 and not ev_sportswars8.missed:
                    text _("Flowers & Forklifts")
                if sportswars11 and show_complete:
                    textbutton _("David Beckham's Large Banana {b}✓{/b}") action Replay("sportswars11", locked=False) text_style "modmybutton"
                elif not sportswars11 and not ev_sportswars11.missed:
                    text _("David Beckham's Large Banana")
                if sportswars12 and show_complete:
                    textbutton _("Mr. Bones' Wild Ride {b}✓{/b}") action Replay("sportswars12", locked=False) text_style "modmybutton"
                elif not sportswars12 and not ev_sportswars12.missed:
                    text _("Mr. Bones' Wild Ride")
                if sportswars13 and show_complete:
                    textbutton _("Priestess of Fallen Snow {b}✓{/b}") action Replay("sportswars13", locked=False) text_style "modmybutton"
                elif not sportswars13 and not ev_sportswars13.missed:
                    text _("Priestess of Fallen Snow")
                if sportswars15 and show_complete:
                    textbutton _("Trauma Bond {b}✓{/b}") action Replay("sportswars15", locked=False) text_style "modmybutton"
                elif not sportswars15 and not ev_sportswars15.missed:
                    text _("Trauma Bond")
                if sportswars16 and show_complete:
                    textbutton _("Irregular Heartbeat {b}✓{/b}") action Replay("sportswars16", locked=False) text_style "modmybutton"
                elif not sportswars16 and not ev_sportswars16.missed:
                    text _("Irregular Heartbeat")
                if sportswars20 and show_complete:
                    textbutton _("Happy {b}✓{/b}") action Replay("sportswars20", locked=False) text_style "modmybutton"
                elif not sportswars20 and not ev_sportswars20.missed:
                    text _("Happy")
                if beachfive1 and show_complete:
                    textbutton _("From The Heart (Red Shell) {b}✓{/b}") action Replay("beachfive1", locked=False) text_style "modmybutton"
                elif not beachfive1 and not ev_beachfive1.missed:
                    text _("From The Heart (Red Shell)")
                if beachfive2 and show_complete:
                    textbutton _("Monkey's Paw {b}✓{/b}") action Replay("beachfive2", locked=False) text_style "modmybutton"
                elif not beachfive2 and not ev_beachfive2.missed:
                    text _("Monkey's Paw")
                if beachfive4 and show_complete:
                    textbutton _("Operation: Sleepytime {b}✓{/b}") action Replay("beachfive4", locked=False) text_style "modmybutton"
                elif not beachfive4 and not ev_beachfive4.missed:
                    text _("Operation: Sleepytime")
                if beachfive5 and show_complete:
                    textbutton _("Sod in the Seedbed {b}✓{/b}") action Replay("beachfive5", locked=False) text_style "modmybutton"
                elif not beachfive5 and not ev_beachfive5.missed:
                    text _("Sod in the Seedbed")
                if beachfive7 and show_complete:
                    textbutton _("Recycling {b}✓{/b}") action Replay("beachfive7", locked=False) text_style "modmybutton"
                elif not beachfive7 and not ev_beachfive7.missed:
                    text _("Recycling")
                if beachfive11 and show_complete:
                    textbutton _("Albatross {b}✓{/b}") action Replay("beachfive11", locked=False) text_style "modmybutton"
                elif not beachfive11 and not ev_beachfive11.missed:
                    text _("Albatross")
                if beachfive12 and show_complete:
                    textbutton _("Pros, Cons, and Countermeasures {b}✓{/b}") action Replay("beachfive12", locked=False) text_style "modmybutton"
                elif not beachfive12 and not ev_beachfive12.missed:
                    text _("Pros, Cons, and Countermeasures")
                if beachfive16 and show_complete:
                    textbutton _("Perfect Harmony {b}✓{/b}") action Replay("beachfive16", locked=False) text_style "modmybutton"
                elif not beachfive16 and not ev_beachfive16.missed:
                    text _("Perfect Harmony")
                if halloweenfive1 and show_complete:
                    textbutton _("Rubik’s Cube {b}✓{/b}") action Replay("halloweenfive1", locked=False) text_style "modmybutton"
                elif not halloweenfive1 and not ev_halloweenfive1.missed:
                    text _("Rubik’s Cube")
                if halloweenfive2 and show_complete:
                    textbutton _("More Than Her {b}✓{/b}") action Replay("halloweenfive2", locked=False) text_style "modmybutton"
                elif not halloweenfive2 and not ev_halloweenfive2.missed:
                    text _("More Than Her")
                if halloweenfive3 and show_complete:
                    textbutton _("Action/Inaction {b}✓{/b}") action Replay("halloweenfive3", locked=False) text_style "modmybutton"
                elif not halloweenfive3 and not ev_halloweenfive3.missed:
                    text _("Action/Inaction")
                if halloweenfive4 and show_complete:
                    textbutton _("Empty Heart Appeal {b}✓{/b}") action Replay("halloweenfive4", locked=False) text_style "modmybutton"
                elif not halloweenfive4 and not ev_halloweenfive4.missed:
                    text _("Empty Heart Appeal")
                if halloweenfive5 and show_complete:
                    textbutton _("The Art of Tribadism {b}✓{/b}") action Replay("halloweenfive5", locked=False) text_style "modmybutton"
                elif not halloweenfive5 and not ev_halloweenfive5.missed:
                    text _("The Art of Tribadism")
                if halloweenfive6 and show_complete:
                    textbutton _("Four Walls, A Garden {b}✓{/b}") action Replay("halloweenfive6", locked=False) text_style "modmybutton"
                elif not halloweenfive6 and not ev_halloweenfive6.missed:
                    text _("Four Walls, A Garden")
                if halloweenfive7 and show_complete:
                    textbutton _("SENSEI-QUEST {b}✓{/b}") action Replay("halloweenfive7", locked=False) text_style "modmybutton"
                elif not halloweenfive7 and not ev_halloweenfive7.missed:
                    text _("SENSEI-QUEST")
                if halloweenfive8 and show_complete:
                    textbutton _("Restart {b}✓{/b}") action Replay("halloweenfive8", locked=False) text_style "modmybutton"
                elif not halloweenfive8 and not ev_halloweenfive8.missed:
                    text _("Restart")
                if halloweenfive9 and show_complete:
                    textbutton _("Recap {b}✓{/b}") action Replay("halloweenfive9", locked=False) text_style "modmybutton"
                elif not halloweenfive9 and not ev_halloweenfive9.missed:
                    text _("Recap")
                if halloweenfive10 and show_complete:
                    textbutton _("Yellow Patch (Heaven in My Hands) {b}✓{/b}") action Replay("halloweenfive10", locked=False) text_style "modmybutton"
                elif not halloweenfive10 and not ev_halloweenfive10.missed:
                    text _("Yellow Patch (Heaven in My Hands)")
                if halloweenfive11 and show_complete:
                    textbutton _("Episcopalis: A Hymn for Him and She and Her {b}✓{/b}") action Replay("halloweenfive11", locked=False) text_style "modmybutton"
                elif not halloweenfive11 and not ev_halloweenfive11.missed:
                    text _("Episcopalis: A Hymn for Him and She and Her")
                if halloweenfive12 and show_complete:
                    textbutton _("Sigma Grindset {b}✓{/b}") action Replay("halloweenfive12", locked=False) text_style "modmybutton"
                elif not halloweenfive12 and not ev_halloweenfive12.missed:
                    text _("Sigma Grindset")
                if halloweenfive13 and show_complete:
                    textbutton _("All Around the Mulberry Bush {b}✓{/b}") action Replay("halloweenfive13", locked=False) text_style "modmybutton"
                elif not halloweenfive13 and not ev_halloweenfive13.missed:
                    text _("All Around the Mulberry Bush")
                if halloweenfive14 and show_complete:
                    textbutton _("Pop Goes the Weasel {b}✓{/b}") action Replay("halloweenfive14", locked=False) text_style "modmybutton"
                elif not halloweenfive14 and not ev_halloweenfive14.missed:
                    text _("Pop Goes the Weasel")
                if halloweenfive15 and show_complete:
                    textbutton _("God of Light {b}✓{/b}") action Replay("halloweenfive15", locked=False) text_style "modmybutton"
                elif not halloweenfive15 and not ev_halloweenfive15.missed:
                    text _("God of Light")
                if halloweenfive16 and show_complete:
                    textbutton _("Sonny Boy & The Magnificent Waiting Room {b}✓{/b}") action Replay("halloweenfive16", locked=False) text_style "modmybutton"
                elif not halloweenfive16 and not ev_halloweenfive16.missed:
                    text _("Sonny Boy & The Magnificent Waiting Room")
                if halloweenfive17 and show_complete:
                    textbutton _("What We’ll See When We Get There {b}✓{/b}") action Replay("halloweenfive17", locked=False) text_style "modmybutton"
                elif not halloweenfive17 and not ev_halloweenfive17.missed:
                    text _("What We’ll See When We Get There")
                if christmasfive1 and show_complete:
                    textbutton _("Aunt Niki (A Hundred Christmases) {b}✓{/b}") action Replay("christmasfive1", locked=False) text_style "modmybutton"
                elif not christmasfive1 and not ev_christmasfive1.missed:
                    text _("Aunt Niki (A Hundred Christmases)")
                if christmasfive2 and show_complete:
                    textbutton _("Caught in the Crossfire {b}✓{/b}") action Replay("christmasfive2", locked=False) text_style "modmybutton"
                elif not christmasfive2 and not ev_christmasfive2.missed:
                    text _("Caught in the Crossfire")
                if christmasfive3 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. VI: Thought Mirror {b}✓{/b}") action Replay("christmasfive3", locked=False) text_style "modmybutton"
                elif not christmasfive3 and not ev_christmasfive3.missed:
                    text _("The Legacy of Thaum Pt. VI: Thought Mirror")
                if christmasfive4 and show_complete:
                    textbutton _("DON’T TALK TO MONKS {b}✓{/b}") action Replay("christmasfive4", locked=False) text_style "modmybutton"
                elif not christmasfive4 and not ev_christmasfive4.missed:
                    text _("DON’T TALK TO MONKS")
                if christmasfive5 and show_complete:
                    textbutton _("The One With All the Sex Toys {b}✓{/b}") action Replay("christmasfive5", locked=False) text_style "modmybutton"
                elif not christmasfive5 and not ev_christmasfive5.missed:
                    text _("The One With All the Sex Toys")
                if christmasfive6 and show_complete:
                    textbutton _("Seed of Self-Doubt {b}✓{/b}") action Replay("christmasfive6", locked=False) text_style "modmybutton"
                elif not christmasfive6 and not ev_christmasfive6.missed:
                    text _("Seed of Self-Doubt")
                if christmasfive7 and show_complete:
                    textbutton _("Even Heaven {b}✓{/b}") action Replay("christmasfive7", locked=False) text_style "modmybutton"
                elif not christmasfive7 and not ev_christmasfive7.missed:
                    text _("Even Heaven")
                if christmasfive8 and show_complete:
                    textbutton _("Post-Nut Clarity {b}✓{/b}") action Replay("christmasfive8", locked=False) text_style "modmybutton"
                elif not christmasfive8 and not ev_christmasfive8.missed:
                    text _("Post-Nut Clarity")
                if dormwarsfive1 and show_complete:
                    textbutton _("Prepare For Battle! {b}✓{/b}") action Replay("dormwarsfive1", locked=False) text_style "modmybutton"
                elif not dormwarsfive1 and not ev_dormwarsfive1.missed:
                    text _("Prepare For Battle!")
                if dormwarsfive2 and show_complete:
                    textbutton _("Poetry At Best {b}✓{/b}") action Replay("dormwarsfive2", locked=False) text_style "modmybutton"
                elif not dormwarsfive2 and not ev_dormwarsfive2.missed:
                    text _("Poetry At Best")
                if dormwarsfive3 and show_complete:
                    textbutton _("Beach(?) Babe Breakfast Barrage! {b}✓{/b}") action Replay("dormwarsfive3", locked=False) text_style "modmybutton"
                elif not dormwarsfive3 and not ev_dormwarsfive3.missed:
                    text _("Beach(?) Babe Breakfast Barrage!")
                if dormwarsfive4 and show_complete:
                    textbutton _("Dungeons & Divas! Normies Gone Nerdy! {b}✓{/b}") action Replay("dormwarsfive4", locked=False) text_style "modmybutton"
                elif not dormwarsfive4 and not ev_dormwarsfive4.missed:
                    text _("Dungeons & Divas! Normies Gone Nerdy!")
                if dormwarsfive5 and show_complete:
                    textbutton _("Talentless & Talkative! Trivia Turmoil! {b}✓{/b}") action Replay("dormwarsfive5", locked=False) text_style "modmybutton"
                elif not dormwarsfive5 and not ev_dormwarsfive5.missed:
                    text _("Talentless & Talkative! Trivia Turmoil!")
                if dormwarsfive6 and show_complete:
                    textbutton _("Sweet Joy Befall Thee! Be Nice to Sensei Battle! {b}✓{/b}") action Replay("dormwarsfive6", locked=False) text_style "modmybutton"
                elif not dormwarsfive6 and not ev_dormwarsfive6.missed:
                    text _("Sweet Joy Befall Thee! Be Nice to Sensei Battle!")
                if dormwarsfive7 and show_complete:
                    textbutton _("Shadow Word: Death Ball {b}✓{/b}") action Replay("dormwarsfive7", locked=False) text_style "modmybutton"
                elif not dormwarsfive7 and not ev_dormwarsfive7.missed:
                    text _("Shadow Word: Death Ball")
                if dormwarsfive8 and show_complete:
                    textbutton _("Lovely Lawyers & The Laws of...Love! {b}✓{/b}") action Replay("dormwarsfive8", locked=False) text_style "modmybutton"
                elif not dormwarsfive8 and not ev_dormwarsfive8.missed:
                    text _("Lovely Lawyers & The Laws of...Love!")
                if dormwarsfive9 and show_complete:
                    textbutton _("Silhouettes of Scorned Princesses {b}✓{/b}") action Replay("dormwarsfive9", locked=False) text_style "modmybutton"
                elif not dormwarsfive9 and not ev_dormwarsfive9.missed:
                    text _("Silhouettes of Scorned Princesses")
                if dormwarsfive10 and show_complete:
                    textbutton _("A Ghost's Guide on Haunting {b}✓{/b}") action Replay("dormwarsfive10", locked=False) text_style "modmybutton"
                elif not dormwarsfive10 and not ev_dormwarsfive10.missed:
                    text _("A Ghost's Guide on Haunting")
                if dormwarsfive11 and show_complete:
                    textbutton _("Strippers? No! Swimsuits! (Pool-Toucher) {b}✓{/b}") action Replay("dormwarsfive11", locked=False) text_style "modmybutton"
                elif not dormwarsfive11 and not ev_dormwarsfive11.missed:
                    text _("Strippers? No! Swimsuits! (Pool-Toucher)")
                if dormwarsfive12 and show_complete:
                    textbutton _("Goth Girl Glamour Gala! {b}✓{/b}") action Replay("dormwarsfive12", locked=False) text_style "modmybutton"
                elif not dormwarsfive12 and not ev_dormwarsfive12.missed:
                    text _("Goth Girl Glamour Gala!")
                if dormwarsfive13 and show_complete:
                    textbutton _("And Then There Were Two {b}✓{/b}") action Replay("dormwarsfive13", locked=False) text_style "modmybutton"
                elif not dormwarsfive13 and not ev_dormwarsfive13.missed:
                    text _("And Then There Were Two")
                if nodokathontwo1 and show_complete:
                    textbutton _("John 13 (From God to God) {b}✓{/b}") action Replay("nodokathontwo1", locked=False) text_style "modmybutton"
                elif ev_nodokathontwo1.missed and show_complete:
                    text _("{color=EF1A1A}{s}New Commandments{/s}{/color}")
                elif not nodokathontwo1 and not ev_nodokathontwo1.missed:
                    text _("John 13 (From God to God)")
                if nodokathontwo2 and show_complete:
                    textbutton _("Genesis 19 (Pillars of Salt) {b}✓{/b}") action Replay("nodokathontwo2", locked=False) text_style "modmybutton"
                elif ev_nodokathontwo2.missed and show_complete:
                    text _("{color=EF1A1A}{s}Zoar in Flames{/s}{/color}")
                elif not nodokathontwo2 and not ev_nodokathontwo2.missed:
                    text _("Genesis 19 (Pillars of Salt)")
                if nodokathontwo3 and show_complete:
                    textbutton _("Thessalonians 4 (Lust Like the Pagans) {b}✓{/b}") action Replay("nodokathontwo3", locked=False) text_style "modmybutton"
                elif ev_nodokathontwo3.missed and show_complete:
                    text _("{color=EF1A1A}{s}The Trumpet Call of God{/s}{/color}")
                elif not nodokathontwo3 and not ev_nodokathontwo3.missed:
                    text _("Thessalonians 4 (Lust Like the Pagans)")
                if dormwarsfive14 and show_complete:
                    textbutton _("Partial to Jasmine {b}✓{/b}") action Replay("dormwarsfive14", locked=False) text_style "modmybutton"
                elif not dormwarsfive14 and not ev_dormwarsfive14.missed:
                    text _("Partial to Jasmine")
                if beachsix1 and show_complete:
                    textbutton _("The Legacy of Thaum (On a Bus) {b}✓{/b}") action Replay("beachsix1", locked=False) text_style "modmybutton"
                elif not beachsix1 and not ev_beachsix1.missed:
                    text _("The Legacy of Thaum (On a Bus)")
                if beachsix2 and show_complete:
                    textbutton _("Natural Instinct {b}✓{/b}") action Replay("beachsix2", locked=False) text_style "modmybutton"
                elif not beachsix2 and not ev_beachsix2.missed:
                    text _("Natural Instinct")
                if beachsix3 and show_complete:
                    textbutton _("Buyer's Remorse (Suicide Fund) {b}✓{/b}") action Replay("beachsix3", locked=False) text_style "modmybutton"
                elif not beachsix3 and not ev_beachsix3.missed:
                    text _("Buyer's Remorse (Suicide Fund)")
                if beachsix4 and show_complete:
                    textbutton _("Peregrine Falcon {b}✓{/b}") action Replay("beachsix4", locked=False) text_style "modmybutton"
                elif not beachsix4 and not ev_beachsix4.missed:
                    text _("Peregrine Falcon")
                if beachsix5 and show_complete:
                    textbutton _("Pulling Ahead {b}✓{/b}") action Replay("beachsix5", locked=False) text_style "modmybutton"
                elif not beachsix5 and not ev_beachsix5.missed:
                    text _("Pulling Ahead")
                if beachsix6 and show_complete:
                    textbutton _("Cities in Gifu {b}✓{/b}") action Replay("beachsix6", locked=False) text_style "modmybutton"
                elif not beachsix6 and not ev_beachsix6.missed:
                    text _("Cities in Gifu")
                if beachsix7 and show_complete:
                    textbutton _("Flowers for Algernon {b}✓{/b}") action Replay("beachsix7", locked=False) text_style "modmybutton"
                elif not beachsix7 and not ev_beachsix7.missed:
                    text _("Flowers for Algernon")
                if beachsix8 and show_complete:
                    textbutton _("Into the Void {b}✓{/b}") action Replay("beachsix8", locked=False) text_style "modmybutton"
                elif not beachsix8 and not ev_beachsix8.missed:
                    text _("Into the Void")
                if undeservedfuture11 and show_complete:
                    textbutton _("Behind the Scenes {b}✓{/b}") action Replay("undeservedfuture11", locked=False) text_style "modmybutton"
                elif not undeservedfuture11 and not ev_undeservedfuture11.missed:
                    text _("Behind the Scenes")
                if undeservedfuture12 and show_complete:
                    textbutton _("The Web This World Has Spun {b}✓{/b}") action Replay("undeservedfuture12", locked=False) text_style "modmybutton"
                elif not undeservedfuture12 and not ev_undeservedfuture12.missed:
                    text _("The Web This World Has Spun")
                if undeservedfuture13 and show_complete:
                    textbutton _("Engagement Farming {b}✓{/b}") action Replay("undeservedfuture13", locked=False) text_style "modmybutton"
                elif not undeservedfuture13 and not ev_undeservedfuture13.missed:
                    text _("Engagement Farming")
                if undeservedfuture14 and show_complete:
                    textbutton _("Wind Chime {b}✓{/b}") action Replay("undeservedfuture14", locked=False) text_style "modmybutton"
                elif not undeservedfuture14 and not ev_undeservedfuture14.missed:
                    text _("Wind Chime")
                if undeservedfuture15 and show_complete:
                    textbutton _("F4972-B {b}✓{/b}") action Replay("undeservedfuture15", locked=False) text_style "modmybutton"
                elif not undeservedfuture15 and not ev_undeservedfuture15.missed:
                    text _("F4972-B")
                if undeservedfuture16 and show_complete:
                    textbutton _("Last Supper {b}✓{/b}") action Replay("undeservedfuture16", locked=False) text_style "modmybutton"
                elif not undeservedfuture16 and not ev_undeservedfuture16.missed:
                    text _("Last Supper")
                if undeservedfuture17 and show_complete:
                    textbutton _("All That's Left Are Stars {b}✓{/b}") action Replay("undeservedfuture17", locked=False) text_style "modmybutton"
                elif not undeservedfuture17 and not ev_undeservedfuture17.missed:
                    text _("All That's Left Are Stars")
                if undeservedfuture18 and show_complete:
                    textbutton _("The First Christmalloween {b}✓{/b}") action Replay("undeservedfuture18", locked=False) text_style "modmybutton"
                elif not undeservedfuture18 and not ev_undeservedfuture18.missed:
                    text _("The First Christmalloween")
                if christmalloween1 and show_complete:
                    textbutton _("Double-Bestiality {b}✓{/b}") action Replay("christmalloween1", locked=False) text_style "modmybutton"
                elif not christmalloween1 and not ev_christmalloween1.missed:
                    text _("Double-Bestiality")
                if christmalloween2 and show_complete:
                    textbutton _("Pattern Recognition {b}✓{/b}") action Replay("christmalloween2", locked=False) text_style "modmybutton"
                elif ev_christmalloween2.missed and show_complete:
                    text _("{color=EF1A1A}{s}Burn the Arboretum{/s}{/color}")
                elif not christmalloween2 and not ev_christmalloween2.missed:
                    text _("Pattern Recognition")
                if christmalloween3 and show_complete:
                    textbutton _("Pen & Paper {b}✓{/b}") action Replay("christmalloween3", locked=False) text_style "modmybutton"
                elif not christmalloween3 and not ev_christmalloween3.missed:
                    text _("Pen & Paper")
                if christmalloween4 and show_complete:
                    textbutton _("The Forest (For the Trees) {b}✓{/b}") action Replay("christmalloween4", locked=False) text_style "modmybutton"
                elif not christmalloween4 and not ev_christmalloween4.missed:
                    text _("The Forest (For the Trees)")
                if christmalloween5 and show_complete:
                    textbutton _("A Game of Our Own {b}✓{/b}") action Replay("christmalloween5", locked=False) text_style "modmybutton"
                elif not christmalloween5 and not ev_christmalloween5.missed:
                    text _("A Game of Our Own")
                if christmalloween6 and show_complete:
                    textbutton _("Hot Father Juice {b}✓{/b}") action Replay("christmalloween6", locked=False) text_style "modmybutton"
                elif not christmalloween6 and not ev_christmalloween6.missed:
                    text _("Hot Father Juice")
                if springtimesadness1 and show_complete:
                    textbutton _("A Vivid Explosion of Color {b}✓{/b}") action Replay("springtimesadness1", locked=False) text_style "modmybutton"
                elif not springtimesadness1 and not ev_springtimesadness1.missed:
                    text _("A Vivid Explosion of Color")
                if springtimesadness2 and show_complete:
                    textbutton _("The Touch of God {b}✓{/b}") action Replay("springtimesadness2", locked=False) text_style "modmybutton"
                elif not springtimesadness2 and not ev_springtimesadness2.missed:
                    text _("The Touch of God")
                if dormwarssix1 and show_complete:
                    textbutton _("One Man's Hell {b}✓{/b}") action Replay("dormwarssix1", locked=False) text_style "modmybutton"
                elif not dormwarssix1 and not ev_dormwarssix1.missed:
                    text _("One Man's Hell")
                if dormwarssix2 and show_complete:
                    textbutton _("Athletics Abound! Keep in Shape With Karin! {b}✓{/b}") action Replay("dormwarssix2", locked=False) text_style "modmybutton"
                elif not dormwarssix2 and not ev_dormwarssix2.missed:
                    text _("Athletics Abound! Keep in Shape With Karin!")
                if dormwarssix3 and show_complete:
                    textbutton _("Kaori's Chaotic Cooking Class! {b}✓{/b}") action Replay("dormwarssix3", locked=False) text_style "modmybutton"
                elif not dormwarssix3 and not ev_dormwarssix3.missed:
                    text _("Kaori's Chaotic Cooking Class!")
                if dormwarssix4 and show_complete:
                    textbutton _("Familial Face-Off! {b}✓{/b}") action Replay("dormwarssix4", locked=False) text_style "modmybutton"
                elif not dormwarssix4 and not ev_dormwarssix4.missed:
                    text _("Familial Face-Off!")
                if dormwarssix5 and show_complete:
                    textbutton _("Amplified Artistry! Drawing With Nao-chan! {b}✓{/b}") action Replay("dormwarssix5", locked=False) text_style "modmybutton"
                elif not dormwarssix5 and not ev_dormwarssix5.missed:
                    text _("Amplified Artistry! Drawing With Nao-chan!")
                if dormwarssix6 and show_complete:
                    textbutton _("Think Fast! Flirt Faster! {b}✓{/b}") action Replay("dormwarssix6", locked=False) text_style "modmybutton"
                elif not dormwarssix6 and not ev_dormwarssix6.missed:
                    text _("Think Fast! Flirt Faster!")
                if dormwarssix7 and show_complete:
                    textbutton _("Trivial Trivia on Topical Topics! {b}✓{/b}") action Replay("dormwarssix7", locked=False) text_style "modmybutton"
                elif not dormwarssix7 and not ev_dormwarssix7.missed:
                    text _("Trivial Trivia on Topical Topics!")
                if dormwarssix8 and show_complete:
                    textbutton _("Teenage Teacher Takedown! {b}✓{/b}") action Replay("dormwarssix8", locked=False) text_style "modmybutton"
                elif not dormwarssix8 and not ev_dormwarssix8.missed:
                    text _("Teenage Teacher Takedown!")
                if dormwarssix9 and show_complete:
                    textbutton _("Sea of Balls 2: Electric Boogaloo {b}✓{/b}") action Replay("dormwarssix9", locked=False) text_style "modmybutton"
                elif not dormwarssix9 and not ev_dormwarssix9.missed:
                    text _("Sea of Balls 2: Electric Boogaloo")
                if dormwarssix10 and show_complete:
                    textbutton _("Barista Beatdown: Revenge of the White People! {b}✓{/b}") action Replay("dormwarssix10", locked=False) text_style "modmybutton"
                elif not dormwarssix10 and not ev_dormwarssix10.missed:
                    text _("Barista Beatdown: Revenge of the White People!")
                if dormwarssix11 and show_complete:
                    textbutton _("Mabby Dick (Sweetmeats for My Dolphin) {b}✓{/b}") action Replay("dormwarssix11", locked=False) text_style "modmybutton"
                elif not dormwarssix11 and not ev_dormwarssix11.missed:
                    text _("Mabby Dick (Sweetmeats for My Dolphin)")
                if dormwarssix12 and show_complete:
                    textbutton _("The Infinite Common Route {b}✓{/b}") action Replay("dormwarssix12", locked=False) text_style "modmybutton"
                elif not dormwarssix12 and not ev_dormwarssix12.missed:
                    text _("The Infinite Common Route")
                if postwarsix1 and show_complete:
                    textbutton _("Vault of Glass {b}✓{/b}") action Replay("postwarsix1", locked=False) text_style "modmybutton"
                elif not postwarsix1 and not ev_postwarsix1.missed:
                    text _("Vault of Glass")

################################################################################

            if show_hints == True and not _in_replay:

                vbox:
                    xpos .4
                    style_prefix "tracker"

                    #The Collector (springtime1)
                    if (not ev_springtime1.completed and not ev_springtime1.missed) or show_complete:
                        text ("[ev_springtime1.hint]")

                    #On the Count of Three (springtime2)
                    if (not ev_springtime2.completed and not ev_springtime2.missed) or show_complete:
                        text ("[ev_springtime2.hint]")

                    #Not the Nightingale (springtime3)
                    if (not ev_springtime3.completed and not ev_springtime3.missed) or show_complete:
                        text ("[ev_springtime3.hint]")

                    #Silver & Gold (springtime4)
                    if (not ev_springtime4.completed and not ev_springtime4.missed) or show_complete:
                        text ("[ev_springtime4.hint]")

                    #November 1st (springtime5)
                    if (not ev_springtime5.completed and not ev_springtime5.missed) or show_complete:
                        text ("[ev_springtime5.hint]")

                    #Visibly Impatient (springtime6)
                    if (not ev_springtime6.completed and not ev_springtime6.missed) or show_complete:
                        text ("[ev_springtime6.hint]")

                    #The Final Human on the Face of the Earth (springtime7)
                    if (not ev_springtime7.completed and not ev_springtime7.missed) or show_complete:
                        text ("[ev_springtime7.hint]")

                    #Actual Jesus Quotes (springtime8)
                    if (not ev_springtime8.completed and not ev_springtime8.missed) or show_complete:
                        text ("[ev_springtime8.hint]")

                    #In Regard to the Peony (springtime9)
                    if (not ev_springtime9.completed and not ev_springtime9.missed) or show_complete:
                        text ("[ev_springtime9.hint]")

                    #When the Sun Sleeps (springtime10)
                    if (not ev_springtime10.completed and not ev_springtime10.missed) or show_complete:
                        text ("[ev_springtime10.hint]")

                    #Hunger Games (springtime11)
                    if (not ev_springtime11.completed and not ev_springtime11.missed) or show_complete:
                        text ("[ev_springtime11.hint]")

                    #Shut Up & Kiss (springtime12)
                    if (not ev_springtime12.completed and not ev_springtime12.missed) or show_complete:
                        text ("[ev_springtime12.hint]")

                    #Death (And Other Sad Stuff) (springtime13)
                    if (not ev_springtime13.completed and not ev_springtime13.missed) or show_complete:
                        text ("[ev_springtime13.hint]")

                    #The Legacy of Thaum Pt. V: The Faceless Empyrean (springtime14)
                    if (not ev_springtime14.completed and not ev_springtime14.missed) or show_complete:
                        text ("[ev_springtime14.hint]")

                    #Goodnight Moon (springtime15)
                    if (not ev_springtime15.completed and not ev_springtime15.missed) or show_complete:
                        text ("[ev_springtime15.hint]")

                    #Your Blood in Spring (springtime16)
                    if (not ev_springtime16.completed and not ev_springtime16.missed) or show_complete:
                        text ("[ev_springtime16.hint]")

                    #Rhythm of a Black Heart (springtime17)
                    if (not ev_springtime17.completed and not ev_springtime17.missed) or show_complete:
                        text ("[ev_springtime17.hint]")

                    #You & Me Against the World (springtime18)
                    if (not ev_springtime18.completed and not ev_springtime18.missed) or show_complete:
                        text ("[ev_springtime18.hint]")

                    #Miserably Ever After (springtime19)
                    if (not ev_springtime19.completed and not ev_springtime19.missed) or show_complete:
                        text ("[ev_springtime19.hint]")

                    #Episcopalis: Pickled Plums & Polyrhythmic Psalms (springend1)
                    if (not ev_springend1.completed and not ev_springend1.missed) or show_complete:
                        text ("[ev_springend1.hint]")

                    #Okonomiyaki (springend2)
                    if (not ev_springend2.completed and not ev_springend2.missed) or show_complete:
                        text ("[ev_springend2.hint]")

                    #500 Channels (springend3)
                    if (not ev_springend3.completed and not ev_springend3.missed) or show_complete:
                        text ("[ev_springend3.hint]")

                    #Wild Boar (springend4)
                    if (not ev_springend4.completed and not ev_springend4.missed) or show_complete:
                        text ("[ev_springend4.hint]")

                    #All Eyes On Me (springend5)
                    if (not ev_springend5.completed and not ev_springend5.missed) or show_complete:
                        text ("[ev_springend5.hint]")

                    #War Never Changes: Egg Time Madness (sportswars3)
                    if (not ev_sportswars3.completed and not ev_sportswars3.missed) or show_complete:
                        text ("[ev_sportswars3.hint]")

                    #Shohei Ohtani (sportswars4)
                    if (not ev_sportswars4.completed and not ev_sportswars4.missed) or show_complete:
                        text ("[ev_sportswars4.hint]")

                    #Sea of Balls (Wise Turtle) (sportswars6)
                    if (not ev_sportswars6.completed and not ev_sportswars6.missed) or show_complete:
                        text ("[ev_sportswars6.hint]")

                    #Cock Party 2 (Better Than The First) (sportswars7)
                    if (not ev_sportswars7.completed and not ev_sportswars7.missed) or show_complete:
                        text ("[ev_sportswars7.hint]")

                    #Flowers & Forklifts (sportswars8)
                    if (not ev_sportswars8.completed and not ev_sportswars8.missed) or show_complete:
                        text ("[ev_sportswars8.hint]")

                    #David Beckham's Large Banana (sportswars11)
                    if (not ev_sportswars11.completed and not ev_sportswars11.missed) or show_complete:
                        text ("[ev_sportswars11.hint]")

                    #Mr. Bones' Wild Ride (sportswars12)
                    if (not ev_sportswars12.completed and not ev_sportswars12.missed) or show_complete:
                        text ("[ev_sportswars12.hint]")

                    #Priestess of Fallen Snow (sportswars13)
                    if (not ev_sportswars13.completed and not ev_sportswars13.missed) or show_complete:
                        text ("[ev_sportswars13.hint]")

                    #Trauma Bond (sportswars15)
                    if (not ev_sportswars15.completed and not ev_sportswars15.missed) or show_complete:
                        text ("[ev_sportswars15.hint]")

                    #Irregular Heartbeat (sportswars16)
                    if (not ev_sportswars16.completed and not ev_sportswars16.missed) or show_complete:
                        text ("[ev_sportswars16.hint]")

                    #Happy (sportswars20)
                    if (not ev_sportswars20.completed and not ev_sportswars20.missed) or show_complete:
                        text ("[ev_sportswars20.hint]")

                    #From The Heart (Red Shell) (beachfive1)
                    if (not ev_beachfive1.completed and not ev_beachfive1.missed) or show_complete:
                        text ("[ev_beachfive1.hint]")

                    #Monkey's Paw (beachfive2)
                    if (not ev_beachfive2.completed and not ev_beachfive2.missed) or show_complete:
                        text ("[ev_beachfive2.hint]")

                    #Operation: Sleepytime (beachfive4)
                    if (not ev_beachfive4.completed and not ev_beachfive4.missed) or show_complete:
                        text ("[ev_beachfive4.hint]")

                    #Sod in the Seedbed (beachfive5)
                    if (not ev_beachfive5.completed and not ev_beachfive5.missed) or show_complete:
                        text ("[ev_beachfive5.hint]")

                    #Recycling (beachfive7)
                    if (not ev_beachfive7.completed and not ev_beachfive7.missed) or show_complete:
                        text ("[ev_beachfive7.hint]")

                    #Albatross (beachfive11)
                    if (not ev_beachfive11.completed and not ev_beachfive11.missed) or show_complete:
                        text ("[ev_beachfive11.hint]")

                    #Pros, Cons, and Countermeasures (beachfive12)
                    if (not ev_beachfive12.completed and not ev_beachfive12.missed) or show_complete:
                        text ("[ev_beachfive12.hint]")

                    #Perfect Harmony (beachfive16)
                    if (not ev_beachfive16.completed and not ev_beachfive16.missed) or show_complete:
                        text ("[ev_beachfive16.hint]")

                    #Rubik’s Cube (halloweenfive1)
                    if (not ev_halloweenfive1.completed and not ev_halloweenfive1.missed) or show_complete:
                        text ("[ev_halloweenfive1.hint]")

                    #More Than Her (halloweenfive2)
                    if (not ev_halloweenfive2.completed and not ev_halloweenfive2.missed) or show_complete:
                        text ("[ev_halloweenfive2.hint]")

                    #Action/Inaction (halloweenfive3)
                    if (not ev_halloweenfive3.completed and not ev_halloweenfive3.missed) or show_complete:
                        text ("[ev_halloweenfive3.hint]")

                    #Empty Heart Appeal (halloweenfive4)
                    if (not ev_halloweenfive4.completed and not ev_halloweenfive4.missed) or show_complete:
                        text ("[ev_halloweenfive4.hint]")

                    #The Art of Tribadism (halloweenfive5)
                    if (not ev_halloweenfive5.completed and not ev_halloweenfive5.missed) or show_complete:
                        text ("[ev_halloweenfive5.hint]")

                    #Four Walls, A Garden (halloweenfive6)
                    if (not ev_halloweenfive6.completed and not ev_halloweenfive6.missed) or show_complete:
                        text ("[ev_halloweenfive6.hint]")

                    #SENSEI-QUEST (halloweenfive7)
                    if (not ev_halloweenfive7.completed and not ev_halloweenfive7.missed) or show_complete:
                        text ("[ev_halloweenfive7.hint]")

                    #Restart (halloweenfive8)
                    if (not ev_halloweenfive8.completed and not ev_halloweenfive8.missed) or show_complete:
                        text ("[ev_halloweenfive8.hint]")

                    #Recap (halloweenfive9)
                    if (not ev_halloweenfive9.completed and not ev_halloweenfive9.missed) or show_complete:
                        text ("[ev_halloweenfive9.hint]")

                    #Yellow Patch (Heaven in My Hands) (halloweenfive10)
                    if (not ev_halloweenfive10.completed and not ev_halloweenfive10.missed) or show_complete:
                        text ("[ev_halloweenfive10.hint]")

                    #Episcopalis: A Hymn for Him and She and Her (halloweenfive11)
                    if (not ev_halloweenfive11.completed and not ev_halloweenfive11.missed) or show_complete:
                        text ("[ev_halloweenfive11.hint]")

                    #Sigma Grindset (halloweenfive12)
                    if (not ev_halloweenfive12.completed and not ev_halloweenfive12.missed) or show_complete:
                        text ("[ev_halloweenfive12.hint]")

                    #All Around the Mulberry Bush (halloweenfive13)
                    if (not ev_halloweenfive13.completed and not ev_halloweenfive13.missed) or show_complete:
                        text ("[ev_halloweenfive13.hint]")

                    #Pop Goes the Weasel (halloweenfive14)
                    if (not ev_halloweenfive14.completed and not ev_halloweenfive14.missed) or show_complete:
                        text ("[ev_halloweenfive14.hint]")

                    #God of Light (halloweenfive15)
                    if (not ev_halloweenfive15.completed and not ev_halloweenfive15.missed) or show_complete:
                        text ("[ev_halloweenfive15.hint]")

                    #Sonny Boy & The Magnificent Waiting Room (halloweenfive16)
                    if (not ev_halloweenfive16.completed and not ev_halloweenfive16.missed) or show_complete:
                        text ("[ev_halloweenfive16.hint]")

                    #What We’ll See When We Get There (halloweenfive17)
                    if (not ev_halloweenfive17.completed and not ev_halloweenfive17.missed) or show_complete:
                        text ("[ev_halloweenfive17.hint]")

                    #Aunt Niki (A Hundred Christmases) (christmasfive1)
                    if (not ev_christmasfive1.completed and not ev_christmasfive1.missed) or show_complete:
                        text ("[ev_christmasfive1.hint]")

                    #Caught in the Crossfire (christmasfive2)
                    if (not ev_christmasfive2.completed and not ev_christmasfive2.missed) or show_complete:
                        text ("[ev_christmasfive2.hint]")

                    #The Legacy of Thaum Pt. VI: Thought Mirror (christmasfive3)
                    if (not ev_christmasfive3.completed and not ev_christmasfive3.missed) or show_complete:
                        text ("[ev_christmasfive3.hint]")

                    #DON’T TALK TO MONKS (christmasfive4)
                    if (not ev_christmasfive4.completed and not ev_christmasfive4.missed) or show_complete:
                        text ("[ev_christmasfive4.hint]")

                    #The One With All the Sex Toys (christmasfive5)
                    if (not ev_christmasfive5.completed and not ev_christmasfive5.missed) or show_complete:
                        text ("[ev_christmasfive5.hint]")

                    #Seed of Self-Doubt (christmasfive6)
                    if (not ev_christmasfive6.completed and not ev_christmasfive6.missed) or show_complete:
                        text ("[ev_christmasfive6.hint]")

                    #Even Heaven (christmasfive7)
                    if (not ev_christmasfive7.completed and not ev_christmasfive7.missed) or show_complete:
                        text ("[ev_christmasfive7.hint]")

                    #Post-Nut Clarity (christmasfive8)
                    if (not ev_christmasfive8.completed and not ev_christmasfive8.missed) or show_complete:
                        text ("[ev_christmasfive8.hint]")

                    #Prepare For Battle! (dormwarsfive1)
                    if (not ev_dormwarsfive1.completed and not ev_dormwarsfive1.missed) or show_complete:
                        text ("[ev_dormwarsfive1.hint]")

                    #Poetry At Best (dormwarsfive2)
                    if (not ev_dormwarsfive2.completed and not ev_dormwarsfive2.missed) or show_complete:
                        text ("[ev_dormwarsfive2.hint]")

                    #Beach(?) Babe Breakfast Barrage! (dormwarsfive3)
                    if (not ev_dormwarsfive3.completed and not ev_dormwarsfive3.missed) or show_complete:
                        text ("[ev_dormwarsfive3.hint]")

                    #Dungeons & Divas! Normies Gone Nerdy! (dormwarsfive4)
                    if (not ev_dormwarsfive4.completed and not ev_dormwarsfive4.missed) or show_complete:
                        text ("[ev_dormwarsfive4.hint]")

                    #Talentless & Talkative! Trivia Turmoil! (dormwarsfive5)
                    if (not ev_dormwarsfive5.completed and not ev_dormwarsfive5.missed) or show_complete:
                        text ("[ev_dormwarsfive5.hint]")

                    #Sweet Joy Befall Thee! Be Nice to Sensei Battle! (dormwarsfive6)
                    if (not ev_dormwarsfive6.completed and not ev_dormwarsfive6.missed) or show_complete:
                        text ("[ev_dormwarsfive6.hint]")

                    #Shadow Word: Death Ball (dormwarsfive7)
                    if (not ev_dormwarsfive7.completed and not ev_dormwarsfive7.missed) or show_complete:
                        text ("[ev_dormwarsfive7.hint]")

                    #Lovely Lawyers & The Laws of...Love! (dormwarsfive8)
                    if (not ev_dormwarsfive8.completed and not ev_dormwarsfive8.missed) or show_complete:
                        text ("[ev_dormwarsfive8.hint]")

                    #Silhouettes of Scorned Princesses (dormwarsfive9)
                    if (not ev_dormwarsfive9.completed and not ev_dormwarsfive9.missed) or show_complete:
                        text ("[ev_dormwarsfive9.hint]")

                    #A Ghost's Guide on Haunting (dormwarsfive10)
                    if (not ev_dormwarsfive10.completed and not ev_dormwarsfive10.missed) or show_complete:
                        text ("[ev_dormwarsfive10.hint]")

                    #Strippers? No! Swimsuits! (Pool-Toucher) (dormwarsfive11)
                    if (not ev_dormwarsfive11.completed and not ev_dormwarsfive11.missed) or show_complete:
                        text ("[ev_dormwarsfive11.hint]")

                    #Goth Girl Glamour Gala! (dormwarsfive12)
                    if (not ev_dormwarsfive12.completed and not ev_dormwarsfive12.missed) or show_complete:
                        text ("[ev_dormwarsfive12.hint]")

                    #And Then There Were Two (dormwarsfive13)
                    if (not ev_dormwarsfive13.completed and not ev_dormwarsfive13.missed) or show_complete:
                        text ("[ev_dormwarsfive13.hint]")

                    #John 13 (From God to God) (nodokathontwo1)
                    if (not ev_nodokathontwo1.completed and not ev_nodokathontwo1.missed) or show_complete:
                        text ("[ev_nodokathontwo1.hint]")

                    #Genesis 19 (Pillars of Salt) (nodokathontwo2)
                    if (not ev_nodokathontwo2.completed and not ev_nodokathontwo2.missed) or show_complete:
                        text ("[ev_nodokathontwo2.hint]")

                    #Thessalonians 4 (Lust Like the Pagans) (nodokathontwo3)
                    if (not ev_nodokathontwo3.completed and not ev_nodokathontwo3.missed) or show_complete:
                        text ("[ev_nodokathontwo3.hint]")

                    #Partial to Jasmine (dormwarsfive14)
                    if (not ev_dormwarsfive14.completed and not ev_dormwarsfive14.missed) or show_complete:
                        text ("[ev_dormwarsfive14.hint]")

                    #The Legacy of Thaum (On a Bus) (beachsix1)
                    if (not ev_beachsix1.completed and not ev_beachsix1.missed) or show_complete:
                        text ("[ev_beachsix1.hint]")

                    #Natural Instinct (beachsix2)
                    if (not ev_beachsix2.completed and not ev_beachsix2.missed) or show_complete:
                        text ("[ev_beachsix2.hint]")

                    #Buyer's Remorse (Suicide Fund) (beachsix3)
                    if (not ev_beachsix3.completed and not ev_beachsix3.missed) or show_complete:
                        text ("[ev_beachsix3.hint]")

                    #Peregrine Falcon (beachsix4)
                    if (not ev_beachsix4.completed and not ev_beachsix4.missed) or show_complete:
                        text ("[ev_beachsix4.hint]")

                    #Pulling Ahead (beachsix5)
                    if (not ev_beachsix5.completed and not ev_beachsix5.missed) or show_complete:
                        text ("[ev_beachsix5.hint]")

                    #Cities in Gifu (beachsix6)
                    if (not ev_beachsix6.completed and not ev_beachsix6.missed) or show_complete:
                        text ("[ev_beachsix6.hint]")

                    #Flowers for Algernon (beachsix7)
                    if (not ev_beachsix7.completed and not ev_beachsix7.missed) or show_complete:
                        text ("[ev_beachsix7.hint]")

                    #Into the Void (beachsix8)
                    if (not ev_beachsix8.completed and not ev_beachsix8.missed) or show_complete:
                        text ("[ev_beachsix8.hint]")

                    #Behind the Scenes (undeservedfuture11)
                    if (not ev_undeservedfuture11.completed and not ev_undeservedfuture11.missed) or show_complete:
                        text ("[ev_undeservedfuture11.hint]")

                    #The Web This World Has Spun (undeservedfuture12)
                    if (not ev_undeservedfuture12.completed and not ev_undeservedfuture12.missed) or show_complete:
                        text ("[ev_undeservedfuture12.hint]")

                    #Engagement Farming (undeservedfuture13)
                    if (not ev_undeservedfuture13.completed and not ev_undeservedfuture13.missed) or show_complete:
                        text ("[ev_undeservedfuture13.hint]")

                    #Wind Chime (undeservedfuture14)
                    if (not ev_undeservedfuture14.completed and not ev_undeservedfuture14.missed) or show_complete:
                        text ("[ev_undeservedfuture14.hint]")

                    #F4972-B (undeservedfuture15)
                    if (not ev_undeservedfuture15.completed and not ev_undeservedfuture15.missed) or show_complete:
                        text ("[ev_undeservedfuture15.hint]")

                    #Last Supper (undeservedfuture16)
                    if (not ev_undeservedfuture16.completed and not ev_undeservedfuture16.missed) or show_complete:
                        text ("[ev_undeservedfuture16.hint]")

                    #All That's Left Are Stars (undeservedfuture17)
                    if (not ev_undeservedfuture17.completed and not ev_undeservedfuture17.missed) or show_complete:
                        text ("[ev_undeservedfuture17.hint]")

                    #The First Christmalloween (undeservedfuture18)
                    if (not ev_undeservedfuture18.completed and not ev_undeservedfuture18.missed) or show_complete:
                        text ("[ev_undeservedfuture18.hint]")

                    #Double-Bestiality (christmalloween1)
                    if (not ev_christmalloween1.completed and not ev_christmalloween1.missed) or show_complete:
                        text ("[ev_christmalloween1.hint]")

                    #Pattern Recognition (christmalloween2)
                    if (not ev_christmalloween2.completed and not ev_christmalloween2.missed) or show_complete:
                        text ("[ev_christmalloween2.hint]")

                    #Pen & Paper (christmalloween3)
                    if (not ev_christmalloween3.completed and not ev_christmalloween3.missed) or show_complete:
                        text ("[ev_christmalloween3.hint]")

                    #The Forest (For the Trees) (christmalloween4)
                    if (not ev_christmalloween4.completed and not ev_christmalloween4.missed) or show_complete:
                        text ("[ev_christmalloween4.hint]")

                    #A Game of Our Own (christmalloween5)
                    if (not ev_christmalloween5.completed and not ev_christmalloween5.missed) or show_complete:
                        text ("[ev_christmalloween5.hint]")

                    #Hot Father Juice (christmalloween6)
                    if (not ev_christmalloween6.completed and not ev_christmalloween6.missed) or show_complete:
                        text ("[ev_christmalloween6.hint]")

                    #A Vivid Explosion of Color (springtimesadness1)
                    if (not ev_springtimesadness1.completed and not ev_springtimesadness1.missed) or show_complete:
                        text ("[ev_springtimesadness1.hint]")

                    #The Touch of God (springtimesadness2)
                    if (not ev_springtimesadness2.completed and not ev_springtimesadness2.missed) or show_complete:
                        text ("[ev_springtimesadness2.hint]")

                    #One Man's Hell (dormwarssix1)
                    if (not ev_dormwarssix1.completed and not ev_dormwarssix1.missed) or show_complete:
                        text ("[ev_dormwarssix1.hint]")

                    #Athletics Abound! Keep in Shape With Karin! (dormwarssix2)
                    if (not ev_dormwarssix2.completed and not ev_dormwarssix2.missed) or show_complete:
                        text ("[ev_dormwarssix2.hint]")

                    #Kaori's Chaotic Cooking Class! (dormwarssix3)
                    if (not ev_dormwarssix3.completed and not ev_dormwarssix3.missed) or show_complete:
                        text ("[ev_dormwarssix3.hint]")

                    #Familial Face-Off! (dormwarssix4)
                    if (not ev_dormwarssix4.completed and not ev_dormwarssix4.missed) or show_complete:
                        text ("[ev_dormwarssix4.hint]")

                    #Amplified Artistry! Drawing With Nao-chan! (dormwarssix5)
                    if (not ev_dormwarssix5.completed and not ev_dormwarssix5.missed) or show_complete:
                        text ("[ev_dormwarssix5.hint]")

                    #Think Fast! Flirt Faster! (dormwarssix6)
                    if (not ev_dormwarssix6.completed and not ev_dormwarssix6.missed) or show_complete:
                        text ("[ev_dormwarssix6.hint]")

                    #Trivial Trivia on Topical Topics! (dormwarssix7)
                    if (not ev_dormwarssix7.completed and not ev_dormwarssix7.missed) or show_complete:
                        text ("[ev_dormwarssix7.hint]")

                    #Teenage Teacher Takedown! (dormwarssix8)
                    if (not ev_dormwarssix8.completed and not ev_dormwarssix8.missed) or show_complete:
                        text ("[ev_dormwarssix8.hint]")

                    #Sea of Balls 2: Electric Boogaloo (dormwarssix9)
                    if (not ev_dormwarssix9.completed and not ev_dormwarssix9.missed) or show_complete:
                        text ("[ev_dormwarssix9.hint]")

                    #Barista Beatdown: Revenge of the White People! (dormwarssix10)
                    if (not ev_dormwarssix10.completed and not ev_dormwarssix10.missed) or show_complete:
                        text ("[ev_dormwarssix10.hint]")

                    #Mabby Dick (Sweetmeats for My Dolphin) (dormwarssix11)
                    if (not ev_dormwarssix11.completed and not ev_dormwarssix11.missed) or show_complete:
                        text ("[ev_dormwarssix11.hint]")

                    #The Infinite Common Route (dormwarssix12)
                    if (not ev_dormwarssix12.completed and not ev_dormwarssix12.missed) or show_complete:
                        text ("[ev_dormwarssix12.hint]")

                    #Vault of Glass (postwarsix1)
                    if (not ev_postwarsix1.completed and not ev_postwarsix1.missed) or show_complete:
                        text ("[ev_postwarsix1.hint]")

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
