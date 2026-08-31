screen maintrackerch3m():

    tag menu

    use game_menu(_("Chapter 3"), scroll="viewport"):

        null

    key "m" action Return()

    $ renpy.show_screen("overlay_scr", transient=False, zorder=100)

    $ if show_complete: ch3_scroll = (MainEvent.max[3] - MainEvent.max[2]) * 26
    $ if not show_complete: ch3_scroll = (MainEvent.max[3] - (MainEvent.max[2] + chap3point)) * 26

    vbox:
        xpos .25
        ypos 35
        area (0,0,1450,930)

        vbox:
            ypos 40
            hbox:
                vbox:
                    textbutton _("<") action ShowMenu("maintrackerch2m")
                vbox:
                    textbutton _(">") action ShowMenu("maintrackerch4m")

        viewport:
            ypos 35
            area (0,0,1450,870)
            scrollbars None
            mousewheel True
            draggable True
            pagekeys True

            child_size (None,ch3_scroll)

            vbox:
                style_prefix "tracker"

                if chapthree1 and show_complete:
                    textbutton _("The Virgin of the Apocalypse {b}✓{/b}") action Replay("chapthree1", locked=False) text_style "modmybutton"
                elif not chapthree1 and not ev_chapthree1.missed:
                    text _("The Virgin of the Apocalypse")
                if chapthree2 and show_complete:
                    textbutton _("Memories {b}✓{/b}") action Replay("chapthree2", locked=False) text_style "modmybutton"
                elif not chapthree2 and not ev_chapthree2.missed:
                    text _("Memories")
                if chapthree3 and show_complete:
                    textbutton _("Empty Eyes {b}✓{/b}") action Replay("chapthree3", locked=False) text_style "modmybutton"
                elif not chapthree3 and not ev_chapthree3.missed:
                    text _("Empty Eyes")
                if chapthree4 and show_complete:
                    textbutton _("The Great Migration {b}✓{/b}") action Replay("chapthree4", locked=False) text_style "modmybutton"
                elif not chapthree4 and not ev_chapthree4.missed:
                    text _("The Great Migration")
                if chapthree5 and show_complete:
                    textbutton _("Creatures of Habit {b}✓{/b}") action Replay("chapthree5", locked=False) text_style "modmybutton"
                elif not chapthree5 and not ev_chapthree5.missed:
                    text _("Creatures of Habit")
                if chapthree6 and show_complete:
                    textbutton _("Everything Everywhere All At Once {b}✓{/b}") action Replay("chapthree6", locked=False) text_style "modmybutton"
                elif not chapthree6 and not ev_chapthree6.missed:
                    text _("Everything Everywhere All At Once")
                if chapthree7 and show_complete:
                    textbutton _("Normal-ish {b}✓{/b}") action Replay("chapthree7", locked=False) text_style "modmybutton"
                elif not chapthree7 and not ev_chapthree7.missed:
                    text _("Normal-ish")
                if chapthree8 and show_complete:
                    textbutton _("Life is Changing {b}✓{/b}") action Replay("chapthree8", locked=False) text_style "modmybutton"
                elif not chapthree8 and not ev_chapthree8.missed:
                    text _("Life is Changing")
                if yumichikaspecial1 and show_complete:
                    textbutton _("Dead in the Water {b}✓{/b}") action Replay("yumichikaspecial1", locked=False) text_style "modmybutton"
                elif not yumichikaspecial1 and not ev_yumichikaspecial1.missed:
                    text _("Dead in the Water")
                if yumiyukispecial1 and show_complete:
                    textbutton _("The Road to Recovery {b}✓{/b}") action Replay("yumiyukispecial1", locked=False) text_style "modmybutton"
                elif not yumiyukispecial1 and not ev_yumiyukispecial1.missed:
                    text _("The Road to Recovery")
                if imanispecial1 and show_complete:
                    textbutton _("No Strings Attached {b}✓{/b}") action Replay("imanispecial1", locked=False) text_style "modmybutton"
                elif not imanispecial1 and not ev_imanispecial1.missed:
                    text _("No Strings Attached")
                if rikaspecial1 and show_complete:
                    textbutton _("Metronome In Love {b}✓{/b}") action Replay("rikaspecial1", locked=False) text_style "modmybutton"
                elif not rikaspecial1 and not ev_rikaspecial1.missed:
                    text _("Metronome In Love")
                if day543 and show_complete:
                    textbutton _("Grief Seed {b}✓{/b}") action Replay("day543", locked=False) text_style "modmybutton"
                elif not day543 and not ev_day543.missed:
                    text _("Grief Seed")
                if dormwartwo1 and show_complete:
                    textbutton _("A Walk Through Hell {b}✓{/b}") action Replay("dormwartwo1", locked=False) text_style "modmybutton"
                elif not dormwartwo1 and not ev_dormwartwo1.missed:
                    text _("A Walk Through Hell")
                if dormwartwo2 and show_complete:
                    textbutton _("Dorm War II: Pre-Game Show {b}✓{/b}") action Replay("dormwartwo2", locked=False) text_style "modmybutton"
                elif not dormwartwo2 and not ev_dormwartwo2.missed:
                    text _("Dorm War II: Pre-Game Show")
                if dormwartwo3 and show_complete:
                    textbutton _("A Frame on a Shelf in a House {b}✓{/b}") action Replay("dormwartwo3", locked=False) text_style "modmybutton"
                elif not dormwartwo3 and not ev_dormwartwo3.missed:
                    text _("A Frame on a Shelf in a House")
                if dormwartwo4 and show_complete:
                    textbutton _("Gamer Girl Grindfest {b}✓{/b}") action Replay("dormwartwo4", locked=False) text_style "modmybutton"
                elif not dormwartwo4 and not ev_dormwartwo4.missed:
                    text _("Gamer Girl Grindfest")
                if dormwartwo5 and show_complete:
                    textbutton _("Hiding in Plain Sight {b}✓{/b}") action Replay("dormwartwo5", locked=False) text_style "modmybutton"
                elif not dormwartwo5 and not ev_dormwartwo5.missed:
                    text _("Hiding in Plain Sight")
                if dormwartwo6 and show_complete:
                    textbutton _("She Is {b}✓{/b}") action Replay("dormwartwo6", locked=False) text_style "modmybutton"
                elif not dormwartwo6 and not ev_dormwartwo6.missed:
                    text _("She Is")
                if dormwartwo7 and show_complete:
                    textbutton _("Burden to Bear {b}✓{/b}") action Replay("dormwartwo7", locked=False) text_style "modmybutton"
                elif not dormwartwo7 and not ev_dormwartwo7.missed:
                    text _("Burden to Bear")
                if dormwartwo8 and show_complete:
                    textbutton _("Everyone {b}✓{/b}") action Replay("dormwartwo8", locked=False) text_style "modmybutton"
                elif not dormwartwo8 and not ev_dormwartwo8.missed:
                    text _("Everyone")
                if dormwartwo9 and show_complete:
                    textbutton _("Midnight Mom Mosh {b}✓{/b}") action Replay("dormwartwo9", locked=False) text_style "modmybutton"
                elif not dormwartwo9 and not ev_dormwartwo9.missed:
                    text _("Midnight Mom Mosh")
                if dormwartwo10 and show_complete:
                    textbutton _("The Way it Scatters {b}✓{/b}") action Replay("dormwartwo10", locked=False) text_style "modmybutton"
                elif not dormwartwo10 and not ev_dormwartwo10.missed:
                    text _("The Way it Scatters")
                if dormwartwo11 and show_complete:
                    textbutton _("Misfit Maid Madness {b}✓{/b}") action Replay("dormwartwo11", locked=False) text_style "modmybutton"
                elif not dormwartwo11 and not ev_dormwartwo11.missed:
                    text _("Misfit Maid Madness")
                if dormwartwo12 and show_complete:
                    textbutton _("Somewhere Far From Here {b}✓{/b}") action Replay("dormwartwo12", locked=False) text_style "modmybutton"
                elif not dormwartwo12 and not ev_dormwartwo12.missed:
                    text _("Somewhere Far From Here")
                if dormwartwo13 and show_complete:
                    textbutton _("Swimming With Sharks {b}✓{/b}") action Replay("dormwartwo13", locked=False) text_style "modmybutton"
                elif not dormwartwo13 and not ev_dormwartwo13.missed:
                    text _("Swimming With Sharks")
                if dormwartwo14 and show_complete:
                    textbutton _("Remove Curse {b}✓{/b}") action Replay("dormwartwo14", locked=False) text_style "modmybutton"
                elif not dormwartwo14 and not ev_dormwartwo14.missed:
                    text _("Remove Curse")
                if dormwartwo15 and show_complete:
                    textbutton _("The Cracking of the Egg (Nothing is Beautiful) {b}✓{/b}") action Replay("dormwartwo15", locked=False) text_style "modmybutton"
                elif not dormwartwo15 and not ev_dormwartwo15.missed:
                    text _("The Cracking of the Egg (Nothing is Beautiful)")
                if dormwartwo16 and show_complete:
                    textbutton _("World of Lines {b}✓{/b}") action Replay("dormwartwo16", locked=False) text_style "modmybutton"
                elif not dormwartwo16 and not ev_dormwartwo16.missed:
                    text _("World of Lines")
                if dormwartwo17 and show_complete:
                    textbutton _("Popping Off {b}✓{/b}") action Replay("dormwartwo17", locked=False) text_style "modmybutton"
                elif not dormwartwo17 and not ev_dormwartwo17.missed:
                    text _("Popping Off")
                if dormwartwo18 and show_complete:
                    textbutton _("Tip Your Bartender {b}✓{/b}") action Replay("dormwartwo18", locked=False) text_style "modmybutton"
                elif not dormwartwo18 and not ev_dormwartwo18.missed:
                    text _("Tip Your Bartender")
                if dormwartwo19 and show_complete:
                    textbutton _("Redeemer {b}✓{/b}") action Replay("dormwartwo19", locked=False) text_style "modmybutton"
                elif not dormwartwo19 and not ev_dormwartwo19.missed:
                    text _("Redeemer")
                if beachmas1 and show_complete:
                    textbutton _("Walk Into the Water {b}✓{/b}") action Replay("beachmas1", locked=False) text_style "modmybutton"
                elif not beachmas1 and not ev_beachmas1.missed:
                    text _("Walk Into the Water")
                if beachmas2 and show_complete:
                    textbutton _("Imaginary Veins {b}✓{/b}") action Replay("beachmas2", locked=False) text_style "modmybutton"
                elif not beachmas2 and not ev_beachmas2.missed:
                    text _("Imaginary Veins")
                if beachmas3 and show_complete:
                    textbutton _("Friends (The Maya Route) {b}✓{/b}") action Replay("beachmas3", locked=False) text_style "modmybutton"
                elif not beachmas3 and not ev_beachmas3.missed:
                    text _("Friends (The Maya Route)")
                if beachmas4 and show_complete:
                    textbutton _("Chandler's Law {b}✓{/b}") action Replay("beachmas4", locked=False) text_style "modmybutton"
                elif not beachmas4 and not ev_beachmas4.missed:
                    text _("Chandler's Law")
                if beachmas5 and show_complete:
                    textbutton _("The Chains That Bind {b}✓{/b}") action Replay("beachmas5", locked=False) text_style "modmybutton"
                elif not beachmas5 and not ev_beachmas5.missed:
                    text _("The Chains That Bind")
                if beachmas6 and show_complete:
                    textbutton _("No Cumming on Christmas {b}✓{/b}") action Replay("beachmas6", locked=False) text_style "modmybutton"
                elif not beachmas6 and not ev_beachmas6.missed:
                    text _("No Cumming on Christmas")
                if beachmas7 and show_complete:
                    textbutton _("Fetch Quest {b}✓{/b}") action Replay("beachmas7", locked=False) text_style "modmybutton"
                elif not beachmas7 and not ev_beachmas7.missed:
                    text _("Fetch Quest")
                if beachmas8 and show_complete:
                    textbutton _("A Thousand Truths {b}✓{/b}") action Replay("beachmas8", locked=False) text_style "modmybutton"
                elif not beachmas8 and not ev_beachmas8.missed:
                    text _("A Thousand Truths")
                if beachmas9 and show_complete:
                    textbutton _("The Bending of Italics {b}✓{/b}") action Replay("beachmas9", locked=False) text_style "modmybutton"
                elif not beachmas9 and not ev_beachmas9.missed:
                    text _("The Bending of Italics")
                if beachmas10 and show_complete:
                    textbutton _("Treasured {b}✓{/b}") action Replay("beachmas10", locked=False) text_style "modmybutton"
                elif not beachmas10 and not ev_beachmas10.missed:
                    text _("Treasured")
                if beachmas11 and show_complete:
                    textbutton _("いないいない。。。ばあ！ {b}✓{/b}") action Replay("beachmas11", locked=False) text_style "modmybutton"
                elif not beachmas11 and not ev_beachmas11.missed:
                    text _("いないいない。。。ばあ！")
                if beachmas12 and show_complete:
                    textbutton _("Robin Hood {b}✓{/b}") action Replay("beachmas12", locked=False) text_style "modmybutton"
                elif not beachmas12 and not ev_beachmas12.missed:
                    text _("Robin Hood")
                if beachmas13 and show_complete:
                    textbutton _("The Legacy of Thaum Pt. IV {b}✓{/b}") action Replay("beachmas13", locked=False) text_style "modmybutton"
                elif not beachmas13 and not ev_beachmas13.missed:
                    text _("The Legacy of Thaum Pt. IV")
                if beachmas14 and show_complete:
                    textbutton _("On The Fence {b}✓{/b}") action Replay("beachmas14", locked=False) text_style "modmybutton"
                elif not beachmas14 and not ev_beachmas14.missed:
                    text _("On The Fence")
                if beachmas15 and show_complete:
                    textbutton _("To the Future With a Smile {b}✓{/b}") action Replay("beachmas15", locked=False) text_style "modmybutton"
                elif not beachmas15 and not ev_beachmas15.missed:
                    text _("To the Future With a Smile")
                if beachmas16 and show_complete:
                    textbutton _("Neverender {b}✓{/b}") action Replay("beachmas16", locked=False) text_style "modmybutton"
                elif not beachmas16 and not ev_beachmas16.missed:
                    text _("Neverender")
                if beachmas17 and show_complete:
                    textbutton _("Moon-Touched {b}✓{/b}") action Replay("beachmas17", locked=False) text_style "modmybutton"
                elif not beachmas17 and not ev_beachmas17.missed:
                    text _("Moon-Touched")
                if beachmas18 and show_complete:
                    textbutton _("Smells of Summer {b}✓{/b}") action Replay("beachmas18", locked=False) text_style "modmybutton"
                elif not beachmas18 and not ev_beachmas18.missed:
                    text _("Smells of Summer")
                if beachmas19 and show_complete:
                    textbutton _("I Will Deliver You to the Fireflies {b}✓{/b}") action Replay("beachmas19", locked=False) text_style "modmybutton"
                elif not beachmas19 and not ev_beachmas19.missed:
                    text _("I Will Deliver You to the Fireflies")
                if beachmas20 and show_complete:
                    textbutton _("Shelter {b}✓{/b}") action Replay("beachmas20", locked=False) text_style "modmybutton"
                elif not beachmas20 and not ev_beachmas20.missed:
                    text _("Shelter")
                if slumberreset1 and show_complete:
                    textbutton _("To Catch Me If I Fall {b}✓{/b}") action Replay("slumberreset1", locked=False) text_style "modmybutton"
                elif not slumberreset1 and not ev_slumberreset1.missed:
                    text _("To Catch Me If I Fall")
                if slumberreset2 and show_complete:
                    textbutton _("Approximation {b}✓{/b}") action Replay("slumberreset2", locked=False) text_style "modmybutton"
                elif not slumberreset2 and not ev_slumberreset2.missed:
                    text _("Approximation")
                if slumberreset3 and show_complete:
                    textbutton _("December 28, 2020 (Clay & Clockwork) {b}✓{/b}") action Replay("slumberreset3", locked=False) text_style "modmybutton"
                elif not slumberreset3 and not ev_slumberreset3.missed:
                    text _("December 28, 2020 (Clay & Clockwork)")
                if slumberreset4 and show_complete:
                    textbutton _("Untitled {b}✓{/b}") action Replay("slumberreset4", locked=False) text_style "modmybutton"
                elif not slumberreset4 and not ev_slumberreset4.missed:
                    text _("Untitled")
                if slumberreset5 and show_complete:
                    textbutton _("A Thousand Years {b}✓{/b}") action Replay("slumberreset5", locked=False) text_style "modmybutton"
                elif not slumberreset5 and not ev_slumberreset5.missed:
                    text _("A Thousand Years")
                if postnodokachain1 and show_complete:
                    textbutton _("White-Fronted Parrot {b}✓{/b}") action Replay("postnodokachain1", locked=False) text_style "modmybutton"
                elif not postnodokachain1 and not ev_postnodokachain1.missed:
                    text _("White-Fronted Parrot")
                if treasureisland and show_complete:
                    textbutton _("First Contact {b}✓{/b}") action Replay("treasureisland", locked=False) text_style "modmybutton"
                elif not treasureisland and not ev_treasureisland.missed:
                    text _("First Contact")
                if amispecial50mainp1 and show_complete:
                    textbutton _("All For You {b}✓{/b}") action Replay("amispecial50mainp1", locked=False) text_style "modmybutton"
                elif not amispecial50mainp1 and not ev_amispecial50mainp1.missed:
                    text _("All For You")
                if amispecial50mainp2 and show_complete:
                    textbutton _("From the Desk of the Ninth God {b}✓{/b}") action Replay("amispecial50mainp2", locked=False) text_style "modmybutton"
                elif not amispecial50mainp2 and not ev_amispecial50mainp2.missed:
                    text _("From the Desk of the Ninth God")
                if predormwars3 and show_complete:
                    textbutton _("May the Winter Come {b}✓{/b}") action Replay("predormwars3", locked=False) text_style "modmybutton"
                elif not predormwars3 and not ev_predormwars3.missed:
                    text _("May the Winter Come")
                if beachwars1 and show_complete:
                    textbutton _("Boner on the Bus {b}✓{/b}") action Replay("beachwars1", locked=False) text_style "modmybutton"
                elif not beachwars1 and not ev_beachwars1.missed:
                    text _("Boner on the Bus")
                if beachwars2 and show_complete:
                    textbutton _("When You Snap {b}✓{/b}") action Replay("beachwars2", locked=False) text_style "modmybutton"
                elif not beachwars2 and not ev_beachwars2.missed:
                    text _("When You Snap")
                if beachwars3 and show_complete:
                    textbutton _("Until My Back is Broken {b}✓{/b}") action Replay("beachwars3", locked=False) text_style "modmybutton"
                elif not beachwars3 and not ev_beachwars3.missed:
                    text _("Until My Back is Broken")
                if beachwars4 and show_complete:
                    textbutton _("The Rest of Me {b}✓{/b}") action Replay("beachwars4", locked=False) text_style "modmybutton"
                elif not beachwars4 and not ev_beachwars4.missed:
                    text _("The Rest of Me")
                if beachwars5 and show_complete:
                    textbutton _("Hyzenthlay {b}✓{/b}") action Replay("beachwars5", locked=False) text_style "modmybutton"
                elif not beachwars5 and not ev_beachwars5.missed:
                    text _("Hyzenthlay")
                if beachwars6 and show_complete:
                    textbutton _("More Human Than Human {b}✓{/b}") action Replay("beachwars6", locked=False) text_style "modmybutton"
                elif not beachwars6 and not ev_beachwars6.missed:
                    text _("More Human Than Human")
                if beachwars7 and show_complete:
                    textbutton _("Eyes Closed, Chin Up {b}✓{/b}") action Replay("beachwars7", locked=False) text_style "modmybutton"
                elif not beachwars7 and not ev_beachwars7.missed:
                    text _("Eyes Closed, Chin Up")
                if beachwars8 and show_complete:
                    textbutton _("Sexy Swimsuit Showdown {b}✓{/b}") action Replay("beachwars8", locked=False) text_style "modmybutton"
                elif not beachwars8 and not ev_beachwars8.missed:
                    text _("Sexy Swimsuit Showdown")
                if beachwars9 and show_complete:
                    textbutton _("Fairytale (The End Until Tomorrow) {b}✓{/b}") action Replay("beachwars9", locked=False) text_style "modmybutton"
                elif not beachwars9 and not ev_beachwars9.missed:
                    text _("Fairytale (The End Until Tomorrow)")
                if beachwars10 and show_complete:
                    textbutton _("Monsters {b}✓{/b}") action Replay("beachwars10", locked=False) text_style "modmybutton"
                elif not beachwars10 and not ev_beachwars10.missed:
                    text _("Monsters")
                if beachwars11 and show_complete:
                    textbutton _("Pairs in Different Places {b}✓{/b}") action Replay("beachwars11", locked=False) text_style "modmybutton"
                elif not beachwars11 and not ev_beachwars11.missed:
                    text _("Pairs in Different Places")
                if beachwars12 and show_complete:
                    textbutton _("Forbidden Artistry {b}✓{/b}") action Replay("beachwars12", locked=False) text_style "modmybutton"
                elif not beachwars12 and not ev_beachwars12.missed:
                    text _("Forbidden Artistry")
                if beachwars13 and show_complete:
                    textbutton _("Too Many Cooks {b}✓{/b}") action Replay("beachwars13", locked=False) text_style "modmybutton"
                elif not beachwars13 and not ev_beachwars13.missed:
                    text _("Too Many Cooks")
                if beachwars14 and show_complete:
                    textbutton _("Judgement Day {b}✓{/b}") action Replay("beachwars14", locked=False) text_style "modmybutton"
                elif not beachwars14 and not ev_beachwars14.missed:
                    text _("Judgement Day")
                if beachwars15 and show_complete:
                    textbutton _("Mother May I {b}✓{/b}") action Replay("beachwars15", locked=False) text_style "modmybutton"
                elif not beachwars15 and not ev_beachwars15.missed:
                    text _("Mother May I")
                if beachwars16 and show_complete:
                    textbutton _("Cicadian Rhythm (The Gardener) {b}✓{/b}") action Replay("beachwars16", locked=False) text_style "modmybutton"
                elif not beachwars16 and not ev_beachwars16.missed:
                    text _("Cicadian Rhythm (The Gardener)")
                if beachwars17 and show_complete:
                    textbutton _("Bidder's Organs {b}✓{/b}") action Replay("beachwars17", locked=False) text_style "modmybutton"
                elif ev_beachwars17.missed and show_complete:
                    text _("{color=EF1A1A}{s}Bitter Organs{/s}{/color}")
                elif not beachwars17 and not ev_beachwars17.missed:
                    text _("Bidder's Organs")
                if beachwars18 and show_complete:
                    textbutton _("Flowerchild {b}✓{/b}") action Replay("beachwars18", locked=False) text_style "modmybutton"
                elif not beachwars18 and not ev_beachwars18.missed:
                    text _("Flowerchild")
                if beachwars19 and show_complete:
                    textbutton _("Danger to Society {b}✓{/b}") action Replay("beachwars19", locked=False) text_style "modmybutton"
                elif not beachwars19 and not ev_beachwars19.missed:
                    text _("Danger to Society")
                if halloweenfour1 and show_complete:
                    textbutton _("Eggside Octopus {b}✓{/b}") action Replay("halloweenfour1", locked=False) text_style "modmybutton"
                elif not halloweenfour1 and not ev_halloweenfour1.missed:
                    text _("Eggside Octopus")
                if halloweenfour2 and show_complete:
                    textbutton _("The Tenth Step {b}✓{/b}") action Replay("halloweenfour2", locked=False) text_style "modmybutton"
                elif not halloweenfour2 and not ev_halloweenfour2.missed:
                    text _("The Tenth Step")
                if halloweenfour3 and show_complete:
                    textbutton _("BONE-TOWN {b}✓{/b}") action Replay("halloweenfour3", locked=False) text_style "modmybutton"
                elif not halloweenfour3 and not ev_halloweenfour3.missed:
                    text _("BONE-TOWN")
                if halloweenfour4 and show_complete:
                    textbutton _("Try Honesty {b}✓{/b}") action Replay("halloweenfour4", locked=False) text_style "modmybutton"
                elif not halloweenfour4 and not ev_halloweenfour4.missed:
                    text _("Try Honesty")
                if halloweenfour5 and show_complete:
                    textbutton _("Heartache {b}✓{/b}") action Replay("halloweenfour5", locked=False) text_style "modmybutton"
                elif not halloweenfour5 and not ev_halloweenfour5.missed:
                    text _("Heartache")
                if halloweenfour6 and show_complete:
                    textbutton _("The King of Thebes {b}✓{/b}") action Replay("halloweenfour6", locked=False) text_style "modmybutton"
                elif not halloweenfour6 and not ev_halloweenfour6.missed:
                    text _("The King of Thebes")
                if halloweenfour7 and show_complete:
                    textbutton _("Our Fathers {b}✓{/b}") action Replay("halloweenfour7", locked=False) text_style "modmybutton"
                elif not halloweenfour7 and not ev_halloweenfour7.missed:
                    text _("Our Fathers")
                if halloweenfour8 and show_complete:
                    textbutton _("Eighth Eye of the Wolf Spider {b}✓{/b}") action Replay("halloweenfour8", locked=False) text_style "modmybutton"
                elif not halloweenfour8 and not ev_halloweenfour8.missed:
                    text _("Eighth Eye of the Wolf Spider")
                if halloweenfour9 and show_complete:
                    textbutton _("Childspawn {b}✓{/b}") action Replay("halloweenfour9", locked=False) text_style "modmybutton"
                elif not halloweenfour9 and not ev_halloweenfour9.missed:
                    text _("Childspawn")
                if halloweenfour10 and show_complete:
                    textbutton _("An Excerpt From a Waterlogged Journal {b}✓{/b}") action Replay("halloweenfour10", locked=False) text_style "modmybutton"
                elif not halloweenfour10 and not ev_halloweenfour10.missed:
                    text _("An Excerpt From a Waterlogged Journal")
                if halloweenfour11 and show_complete:
                    textbutton _("Party Animal {b}✓{/b}") action Replay("halloweenfour11", locked=False) text_style "modmybutton"
                elif not halloweenfour11 and not ev_halloweenfour11.missed:
                    text _("Party Animal")
                if halloweenfour12 and show_complete:
                    textbutton _("Girls Just Want to Have Fun {b}✓{/b}") action Replay("halloweenfour12", locked=False) text_style "modmybutton"
                elif not halloweenfour12 and not ev_halloweenfour12.missed:
                    text _("Girls Just Want to Have Fun")
                if halloweenfour13 and show_complete:
                    textbutton _("Happy Memories {b}✓{/b}") action Replay("halloweenfour13", locked=False) text_style "modmybutton"
                elif not halloweenfour13 and not ev_halloweenfour13.missed:
                    text _("Happy Memories")
                if halloweenfour14 and show_complete:
                    textbutton _("For More Than Just Me {b}✓{/b}") action Replay("halloweenfour14", locked=False) text_style "modmybutton"
                elif not halloweenfour14 and not ev_halloweenfour14.missed:
                    text _("For More Than Just Me")
                if halloweenfour15 and show_complete:
                    textbutton _("I Won't Say I'm In Love {b}✓{/b}") action Replay("halloweenfour15", locked=False) text_style "modmybutton"
                elif not halloweenfour15 and not ev_halloweenfour15.missed:
                    text _("I Won't Say I'm In Love")
                if halloweenfour16 and show_complete:
                    textbutton _("The End of the World {b}✓{/b}") action Replay("halloweenfour16", locked=False) text_style "modmybutton"
                elif not halloweenfour16 and not ev_halloweenfour16.missed:
                    text _("The End of the World")
                if resetsix1 and show_complete:
                    textbutton _("Times New Roman {b}✓{/b}") action Replay("resetsix1", locked=False) text_style "modmybutton"
                elif not resetsix1 and not ev_resetsix1.missed:
                    text _("Times New Roman")
                if resetsix2 and show_complete:
                    textbutton _("Paper City {b}✓{/b}") action Replay("resetsix2", locked=False) text_style "modmybutton"
                elif not resetsix2 and not ev_resetsix2.missed:
                    text _("Paper City")
                if resetsix3 and show_complete:
                    textbutton _("Meant to Be {b}✓{/b}") action Replay("resetsix3", locked=False) text_style "modmybutton"
                elif not resetsix3 and not ev_resetsix3.missed:
                    text _("Meant to Be")
                if resetsix4 and show_complete:
                    textbutton _("Remember to Smile {b}✓{/b}") action Replay("resetsix4", locked=False) text_style "modmybutton"
                elif not resetsix4 and not ev_resetsix4.missed:
                    text _("Remember to Smile")

################################################################################

            if show_hints == True and not _in_replay:

                vbox:
                    xpos .4
                    style_prefix "tracker"

                    #The Virgin of the Apocalypse (chapthree1)
                    if (not ev_chapthree1.completed and not ev_chapthree1.missed) or show_complete:
                        text ("[ev_chapthree1.hint]")

                    #Memories (chapthree2)
                    if (not ev_chapthree2.completed and not ev_chapthree2.missed) or show_complete:
                        text ("[ev_chapthree2.hint]")

                    #Empty Eyes (chapthree3)
                    if (not ev_chapthree3.completed and not ev_chapthree3.missed) or show_complete:
                        text ("[ev_chapthree3.hint]")

                    #The Great Migration (chapthree4)
                    if (not ev_chapthree4.completed and not ev_chapthree4.missed) or show_complete:
                        text ("[ev_chapthree4.hint]")

                    #Creatures of Habit (chapthree5)
                    if (not ev_chapthree5.completed and not ev_chapthree5.missed) or show_complete:
                        text ("[ev_chapthree5.hint]")

                    #Everything Everywhere All At Once (chapthree6)
                    if (not ev_chapthree6.completed and not ev_chapthree6.missed) or show_complete:
                        text ("[ev_chapthree6.hint]")

                    #Normal-ish (chapthree7)
                    if (not ev_chapthree7.completed and not ev_chapthree7.missed) or show_complete:
                        text ("[ev_chapthree7.hint]")

                    #Life is Changing (chapthree8)
                    if (not ev_chapthree8.completed and not ev_chapthree8.missed) or show_complete:
                        text ("[ev_chapthree8.hint]")

                    #Dead in the Water (yumichikaspecial1)
                    if (not ev_yumichikaspecial1.completed and not ev_yumichikaspecial1.missed) or show_complete:
                        text ("[ev_yumichikaspecial1.hint]")

                    #The Road to Recovery (yumiyukispecial1)
                    if (not ev_yumiyukispecial1.completed and not ev_yumiyukispecial1.missed) or show_complete:
                        text ("[ev_yumiyukispecial1.hint]")

                    #No Strings Attached (imanispecial1)
                    if (not ev_imanispecial1.completed and not ev_imanispecial1.missed) or show_complete:
                        text ("[ev_imanispecial1.hint]")

                    #Metronome In Love (rikaspecial1)
                    if (not ev_rikaspecial1.completed and not ev_rikaspecial1.missed) or show_complete:
                        text ("[ev_rikaspecial1.hint]")

                    #Grief Seed (day543)
                    if (not ev_day543.completed and not ev_day543.missed) or show_complete:
                        text ("[ev_day543.hint]")

                    #A Walk Through Hell (dormwartwo1)
                    if (not ev_dormwartwo1.completed and not ev_dormwartwo1.missed) or show_complete:
                        text ("[ev_dormwartwo1.hint]")

                    #Dorm War II: Pre-Game Show (dormwartwo2)
                    if (not ev_dormwartwo2.completed and not ev_dormwartwo2.missed) or show_complete:
                        text ("[ev_dormwartwo2.hint]")

                    #A Frame on a Shelf in a House (dormwartwo3)
                    if (not ev_dormwartwo3.completed and not ev_dormwartwo3.missed) or show_complete:
                        text ("[ev_dormwartwo3.hint]")

                    #Gamer Girl Grindfest (dormwartwo4)
                    if (not ev_dormwartwo4.completed and not ev_dormwartwo4.missed) or show_complete:
                        text ("[ev_dormwartwo4.hint]")

                    #Hiding in Plain Sight (dormwartwo5)
                    if (not ev_dormwartwo5.completed and not ev_dormwartwo5.missed) or show_complete:
                        text ("[ev_dormwartwo5.hint]")

                    #She Is (dormwartwo6)
                    if (not ev_dormwartwo6.completed and not ev_dormwartwo6.missed) or show_complete:
                        text ("[ev_dormwartwo6.hint]")

                    #Burden to Bear (dormwartwo7)
                    if (not ev_dormwartwo7.completed and not ev_dormwartwo7.missed) or show_complete:
                        text ("[ev_dormwartwo7.hint]")

                    #Everyone (dormwartwo8)
                    if (not ev_dormwartwo8.completed and not ev_dormwartwo8.missed) or show_complete:
                        text ("[ev_dormwartwo8.hint]")

                    #Midnight Mom Mosh (dormwartwo9)
                    if (not ev_dormwartwo9.completed and not ev_dormwartwo9.missed) or show_complete:
                        text ("[ev_dormwartwo9.hint]")

                    #The Way it Scatters (dormwartwo10)
                    if (not ev_dormwartwo10.completed and not ev_dormwartwo10.missed) or show_complete:
                        text ("[ev_dormwartwo10.hint]")

                    #Misfit Maid Madness (dormwartwo11)
                    if (not ev_dormwartwo11.completed and not ev_dormwartwo11.missed) or show_complete:
                        text ("[ev_dormwartwo11.hint]")

                    #Somewhere Far From Here (dormwartwo12)
                    if (not ev_dormwartwo12.completed and not ev_dormwartwo12.missed) or show_complete:
                        text ("[ev_dormwartwo12.hint]")

                    #Swimming With Sharks (dormwartwo13)
                    if (not ev_dormwartwo13.completed and not ev_dormwartwo13.missed) or show_complete:
                        text ("[ev_dormwartwo13.hint]")

                    #Remove Curse (dormwartwo14)
                    if (not ev_dormwartwo14.completed and not ev_dormwartwo14.missed) or show_complete:
                        text ("[ev_dormwartwo14.hint]")

                    #The Cracking of the Egg (Nothing is Beautiful) (dormwartwo15)
                    if (not ev_dormwartwo15.completed and not ev_dormwartwo15.missed) or show_complete:
                        text ("[ev_dormwartwo15.hint]")

                    #World of Lines (dormwartwo16)
                    if (not ev_dormwartwo16.completed and not ev_dormwartwo16.missed) or show_complete:
                        text ("[ev_dormwartwo16.hint]")

                    #Popping Off (dormwartwo17)
                    if (not ev_dormwartwo17.completed and not ev_dormwartwo17.missed) or show_complete:
                        text ("[ev_dormwartwo17.hint]")

                    #Tip Your Bartender (dormwartwo18)
                    if (not ev_dormwartwo18.completed and not ev_dormwartwo18.missed) or show_complete:
                        text ("[ev_dormwartwo18.hint]")

                    #Redeemer (dormwartwo19)
                    if (not ev_dormwartwo19.completed and not ev_dormwartwo19.missed) or show_complete:
                        text ("[ev_dormwartwo19.hint]")

                    #Walk Into the Water (beachmas1)
                    if (not ev_beachmas1.completed and not ev_beachmas1.missed) or show_complete:
                        text ("[ev_beachmas1.hint]")

                    #Imaginary Veins (beachmas2)
                    if (not ev_beachmas2.completed and not ev_beachmas2.missed) or show_complete:
                        text ("[ev_beachmas2.hint]")

                    #Friends (The Maya Route) (beachmas3)
                    if (not ev_beachmas3.completed and not ev_beachmas3.missed) or show_complete:
                        text ("[ev_beachmas3.hint]")

                    #Chandler's Law (beachmas4)
                    if (not ev_beachmas4.completed and not ev_beachmas4.missed) or show_complete:
                        text ("[ev_beachmas4.hint]")

                    #The Chains That Bind (beachmas5)
                    if (not ev_beachmas5.completed and not ev_beachmas5.missed) or show_complete:
                        text ("[ev_beachmas5.hint]")

                    #No Cumming on Christmas (beachmas6)
                    if (not ev_beachmas6.completed and not ev_beachmas6.missed) or show_complete:
                        text ("[ev_beachmas6.hint]")

                    #Fetch Quest (beachmas7)
                    if (not ev_beachmas7.completed and not ev_beachmas7.missed) or show_complete:
                        text ("[ev_beachmas7.hint]")

                    #A Thousand Truths (beachmas8)
                    if (not ev_beachmas8.completed and not ev_beachmas8.missed) or show_complete:
                        text ("[ev_beachmas8.hint]")

                    #The Bending of Italics (beachmas9)
                    if (not ev_beachmas9.completed and not ev_beachmas9.missed) or show_complete:
                        text ("[ev_beachmas9.hint]")

                    #Treasured (beachmas10)
                    if (not ev_beachmas10.completed and not ev_beachmas10.missed) or show_complete:
                        text ("[ev_beachmas10.hint]")

                    #いないいない。。。ばあ！ (beachmas11)
                    if (not ev_beachmas11.completed and not ev_beachmas11.missed) or show_complete:
                        text ("[ev_beachmas11.hint]")

                    #Robin Hood (beachmas12)
                    if (not ev_beachmas12.completed and not ev_beachmas12.missed) or show_complete:
                        text ("[ev_beachmas12.hint]")

                    #The Legacy of Thaum Pt. IV (beachmas13)
                    if (not ev_beachmas13.completed and not ev_beachmas13.missed) or show_complete:
                        text ("[ev_beachmas13.hint]")

                    #On The Fence (beachmas14)
                    if (not ev_beachmas14.completed and not ev_beachmas14.missed) or show_complete:
                        text ("[ev_beachmas14.hint]")

                    #To the Future With a Smile (beachmas15)
                    if (not ev_beachmas15.completed and not ev_beachmas15.missed) or show_complete:
                        text ("[ev_beachmas15.hint]")

                    #Neverender (beachmas16)
                    if (not ev_beachmas16.completed and not ev_beachmas16.missed) or show_complete:
                        text ("[ev_beachmas16.hint]")

                    #Moon-Touched (beachmas17)
                    if (not ev_beachmas17.completed and not ev_beachmas17.missed) or show_complete:
                        text ("[ev_beachmas17.hint]")

                    #Smells of Summer (beachmas18)
                    if (not ev_beachmas18.completed and not ev_beachmas18.missed) or show_complete:
                        text ("[ev_beachmas18.hint]")

                    #I Will Deliver You to the Fireflies (beachmas19)
                    if (not ev_beachmas19.completed and not ev_beachmas19.missed) or show_complete:
                        text ("[ev_beachmas19.hint]")

                    #Shelter (beachmas20)
                    if (not ev_beachmas20.completed and not ev_beachmas20.missed) or show_complete:
                        text ("[ev_beachmas20.hint]")

                    #To Catch Me If I Fall (slumberreset1)
                    if (not ev_slumberreset1.completed and not ev_slumberreset1.missed) or show_complete:
                        text ("[ev_slumberreset1.hint]")

                    #Approximation (slumberreset2)
                    if (not ev_slumberreset2.completed and not ev_slumberreset2.missed) or show_complete:
                        text ("[ev_slumberreset2.hint]")

                    #December 28, 2020 (Clay & Clockwork) (slumberreset3)
                    if (not ev_slumberreset3.completed and not ev_slumberreset3.missed) or show_complete:
                        text ("[ev_slumberreset3.hint]")

                    #Untitled (slumberreset4)
                    if (not ev_slumberreset4.completed and not ev_slumberreset4.missed) or show_complete:
                        text ("[ev_slumberreset4.hint]")

                    #A Thousand Years (slumberreset5)
                    if (not ev_slumberreset5.completed and not ev_slumberreset5.missed) or show_complete:
                        text ("[ev_slumberreset5.hint]")

                    #White-Fronted Parrot (postnodokachain1)
                    if (not ev_postnodokachain1.completed and not ev_postnodokachain1.missed) or show_complete:
                        text ("[ev_postnodokachain1.hint]")

                    #First Contact (treasureisland)
                    if (not ev_treasureisland.completed and not ev_treasureisland.missed) or show_complete:
                        text ("[ev_treasureisland.hint]")

                    #All For You (amispecial50mainp1)
                    if (not ev_amispecial50mainp1.completed and not ev_amispecial50mainp1.missed) or show_complete:
                        text ("[ev_amispecial50mainp1.hint]")

                    #From the Desk of the Ninth God (amispecial50mainp2)
                    if (not ev_amispecial50mainp2.completed and not ev_amispecial50mainp2.missed) or show_complete:
                        text ("[ev_amispecial50mainp2.hint]")

                    #May the Winter Come (predormwars3)
                    if (not ev_predormwars3.completed and not ev_predormwars3.missed) or show_complete:
                        text ("[ev_predormwars3.hint]")

                    #Boner on the Bus (beachwars1)
                    if (not ev_beachwars1.completed and not ev_beachwars1.missed) or show_complete:
                        text ("[ev_beachwars1.hint]")

                    #When You Snap (beachwars2)
                    if (not ev_beachwars2.completed and not ev_beachwars2.missed) or show_complete:
                        text ("[ev_beachwars2.hint]")

                    #Until My Back is Broken (beachwars3)
                    if (not ev_beachwars3.completed and not ev_beachwars3.missed) or show_complete:
                        text ("[ev_beachwars3.hint]")

                    #The Rest of Me (beachwars4)
                    if (not ev_beachwars4.completed and not ev_beachwars4.missed) or show_complete:
                        text ("[ev_beachwars4.hint]")

                    #Hyzenthlay (beachwars5)
                    if (not ev_beachwars5.completed and not ev_beachwars5.missed) or show_complete:
                        text ("[ev_beachwars5.hint]")

                    #More Human Than Human (beachwars6)
                    if (not ev_beachwars6.completed and not ev_beachwars6.missed) or show_complete:
                        text ("[ev_beachwars6.hint]")

                    #Eyes Closed, Chin Up (beachwars7)
                    if (not ev_beachwars7.completed and not ev_beachwars7.missed) or show_complete:
                        text ("[ev_beachwars7.hint]")

                    #Sexy Swimsuit Showdown (beachwars8)
                    if (not ev_beachwars8.completed and not ev_beachwars8.missed) or show_complete:
                        text ("[ev_beachwars8.hint]")

                    #Fairytale (The End Until Tomorrow) (beachwars9)
                    if (not ev_beachwars9.completed and not ev_beachwars9.missed) or show_complete:
                        text ("[ev_beachwars9.hint]")

                    #Monsters (beachwars10)
                    if (not ev_beachwars10.completed and not ev_beachwars10.missed) or show_complete:
                        text ("[ev_beachwars10.hint]")

                    #Pairs in Different Places (beachwars11)
                    if (not ev_beachwars11.completed and not ev_beachwars11.missed) or show_complete:
                        text ("[ev_beachwars11.hint]")

                    #Forbidden Artistry (beachwars12)
                    if (not ev_beachwars12.completed and not ev_beachwars12.missed) or show_complete:
                        text ("[ev_beachwars12.hint]")

                    #Too Many Cooks (beachwars13)
                    if (not ev_beachwars13.completed and not ev_beachwars13.missed) or show_complete:
                        text ("[ev_beachwars13.hint]")

                    #Judgement Day (beachwars14)
                    if (not ev_beachwars14.completed and not ev_beachwars14.missed) or show_complete:
                        text ("[ev_beachwars14.hint]")

                    #Mother May I (beachwars15)
                    if (not ev_beachwars15.completed and not ev_beachwars15.missed) or show_complete:
                        text ("[ev_beachwars15.hint]")

                    #Cicadian Rhythm (The Gardener) (beachwars16)
                    if (not ev_beachwars16.completed and not ev_beachwars16.missed) or show_complete:
                        text ("[ev_beachwars16.hint]")

                    #Bidder's Organs (beachwars17)
                    if (not ev_beachwars17.completed and not ev_beachwars17.missed) or show_complete:
                        text ("[ev_beachwars17.hint]")

                    #Flowerchild (beachwars18)
                    if (not ev_beachwars18.completed and not ev_beachwars18.missed) or show_complete:
                        text ("[ev_beachwars18.hint]")

                    #Danger to Society (beachwars19)
                    if (not ev_beachwars19.completed and not ev_beachwars19.missed) or show_complete:
                        text ("[ev_beachwars19.hint]")

                    #Eggside Octopus (halloweenfour1)
                    if (not ev_halloweenfour1.completed and not ev_halloweenfour1.missed) or show_complete:
                        text ("[ev_halloweenfour1.hint]")

                    #The Tenth Step (halloweenfour2)
                    if (not ev_halloweenfour2.completed and not ev_halloweenfour2.missed) or show_complete:
                        text ("[ev_halloweenfour2.hint]")

                    #BONE-TOWN (halloweenfour3)
                    if (not ev_halloweenfour3.completed and not ev_halloweenfour3.missed) or show_complete:
                        text ("[ev_halloweenfour3.hint]")

                    #Try Honesty (halloweenfour4)
                    if (not ev_halloweenfour4.completed and not ev_halloweenfour4.missed) or show_complete:
                        text ("[ev_halloweenfour4.hint]")

                    #Heartache (halloweenfour5)
                    if (not ev_halloweenfour5.completed and not ev_halloweenfour5.missed) or show_complete:
                        text ("[ev_halloweenfour5.hint]")

                    #The King of Thebes (halloweenfour6)
                    if (not ev_halloweenfour6.completed and not ev_halloweenfour6.missed) or show_complete:
                        text ("[ev_halloweenfour6.hint]")

                    #Our Fathers (halloweenfour7)
                    if (not ev_halloweenfour7.completed and not ev_halloweenfour7.missed) or show_complete:
                        text ("[ev_halloweenfour7.hint]")

                    #Eighth Eye of the Wolf Spider (halloweenfour8)
                    if (not ev_halloweenfour8.completed and not ev_halloweenfour8.missed) or show_complete:
                        text ("[ev_halloweenfour8.hint]")

                    #Childspawn (halloweenfour9)
                    if (not ev_halloweenfour9.completed and not ev_halloweenfour9.missed) or show_complete:
                        text ("[ev_halloweenfour9.hint]")

                    #An Excerpt From a Waterlogged Journal (halloweenfour10)
                    if (not ev_halloweenfour10.completed and not ev_halloweenfour10.missed) or show_complete:
                        text ("[ev_halloweenfour10.hint]")

                    #Party Animal (halloweenfour11)
                    if (not ev_halloweenfour11.completed and not ev_halloweenfour11.missed) or show_complete:
                        text ("[ev_halloweenfour11.hint]")

                    #Girls Just Want to Have Fun (halloweenfour12)
                    if (not ev_halloweenfour12.completed and not ev_halloweenfour12.missed) or show_complete:
                        text ("[ev_halloweenfour12.hint]")

                    #Happy Memories (halloweenfour13)
                    if (not ev_halloweenfour13.completed and not ev_halloweenfour13.missed) or show_complete:
                        text ("[ev_halloweenfour13.hint]")

                    #For More Than Just Me (halloweenfour14)
                    if (not ev_halloweenfour14.completed and not ev_halloweenfour14.missed) or show_complete:
                        text ("[ev_halloweenfour14.hint]")

                    #I Won't Say I'm In Love (halloweenfour15)
                    if (not ev_halloweenfour15.completed and not ev_halloweenfour15.missed) or show_complete:
                        text ("[ev_halloweenfour15.hint]")

                    #The End of the World (halloweenfour16)
                    if (not ev_halloweenfour16.completed and not ev_halloweenfour16.missed) or show_complete:
                        text ("[ev_halloweenfour16.hint]")

                    #Times New Roman (resetsix1)
                    if (not ev_resetsix1.completed and not ev_resetsix1.missed) or show_complete:
                        text ("[ev_resetsix1.hint]")

                    #Paper City (resetsix2)
                    if (not ev_resetsix2.completed and not ev_resetsix2.missed) or show_complete:
                        text ("[ev_resetsix2.hint]")

                    #Meant to Be (resetsix3)
                    if (not ev_resetsix3.completed and not ev_resetsix3.missed) or show_complete:
                        text ("[ev_resetsix3.hint]")

                    #Remember to Smile (resetsix4)
                    if (not ev_resetsix4.completed and not ev_resetsix4.missed) or show_complete:
                        text ("[ev_resetsix4.hint]")

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
