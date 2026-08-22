define six_amiok = Character("am i okay (61 6d 20 69 20 6f 6b 61 79)", who_outlines=[(absolute(2.5), "#000", absolute(0), absolute(0))])
define sev_youdidit = Character("you did it (79 6f 75 64 69 64 69 74)", who_outlines=[(absolute(2.5), "#000", absolute(0), absolute(0))])
define seven_sekai = Character("sekai (73 65 6b 61 69)")

init python:
    preferences.language = 'unnecessaryBS'

    def ireplace(text, old, new):
        idx = 0
        while idx < len(text):
            index_l = text.lower().find(old.lower(), idx)
            if index_l == -1:
                return text
            text = text[:index_l] + new + text[index_l + len(old):]
            idx = index_l + len(new)
        return text
        
init python hide:
    _say = renpy.exports.say

    def patch_say(who, what, *args, **kwargs):
        if who is six:
            who = six_amiok
        if who is sev:
            who = sev_youdidit
        if who is seven:
            who = seven_sekai
        return _say(who, what, *args, **kwargs)

    renpy.exports.say = patch_say        
    
    _menu = renpy.exports.menu
    def patch_menu(choices, *args, **kwargs):
        for i, (label, condition, block) in enumerate(choices):
            label = ireplace(label, '61 6d 69 6f 6b 61 79 20', 'Amiokay')
            label = ireplace(label, '61 6d 69', 'Ami')
            label = ireplace(label, '6d 61 79 61', 'Maya')
            label = ireplace(label, '61 79 61 6e 65', 'Ayane')
            label = ireplace(label, '68 6f 70 65', 'Hope')
            label = ireplace(label, '73 61 6b 69', 'Saki')
            label = ireplace(label, '73 65 6c 65 62 75 73', 'Selebus')
            label = ireplace(label, '73 63 68 6f 6f 6c', 'School')
            label = ireplace(label, '68 69 6d 61 77 61 72 69', 'Himawari')
            label = ireplace(label, '6b 61 6f 72 69', '{b}Kaori{/b}')
            label = ireplace(label, '66 6c 6f 6f 72 20 32', 'Floor 2')
            label = ireplace(label, '73 65 6e 73 65 69', 'Sensei')
            label = ireplace(label, '74', 'T')
            label = ireplace(label, '67 6f 20 62 61 63 6b', 'Go back')
            choices[i] = (label, condition, block)
        
        return _menu(choices, *args, **kwargs)

    renpy.exports.menu = patch_menu

        
init 900 python:
    config.language = "unnecessaryBS"

translate unnecessaryBS strings:
#AmiEvents.rpy
    #amiinvite1
    old "61 6c 62 61 74 72 6f 73 73"
    new "{color=#f00}hex:{/color} albatross"
    
    #amispring1
    old "やだ。"
    new "{color=#f00}jap:{/color} No."
    
    old "やだやだやだやだやだやだやだやだやだやだやだやだやだやだ。"
    new "{color=#f00}jap:{/color} No. No. No. No. No. No."
    
#ch2script.rpy    
    #day295parttwo
    old "74 6f 20 77 68 61 74 20 64 6f 65 73 20 69 74 20 6d 65 61 6e 20 74 6f 20 62 65 20 63 61 6c 6c 6f 75 73 "
    new "{color=#f00}hex:{/color} to what does it mean to be callous"
    
    #returntosummer2
    old "こんにちは！先生です！"
    new "{color=#f00}jap:{/color} Hello, I'm your teacher!"
    
    old "今日はゲームをします。"
    new "{color=#f00}jap:{/color} I'm going to play a game today."
    
    old "で わ。。。"
    new "{color=#f00}jap:{/color} Well then..."
    
    #thirdreset2
    old "70 75 74 20 6d 65 20 6f 75 74 20 6f 66 20 6d 79 20 6d 69 73 65 72 79"
    new "{color=#f00}hex:{/color} put me out of my misery"
    
#chap3.rpy
    #bucketscene
    old "whatigottadotobreakthecyclecauseidontlikethesoundofthat"
    new "what i gotta do to break the cycle cause i dont like the sound of that"
    
    old "ihopeitsnotalivebroadcastcauseidontwantmyparentstoseemyadultwienerlolitssobignow"
    new "i hope its not alive broadcast cause i dont want my parents to see my adult wiener lolits so big now"
    
    #slumberreset3
    old "73 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 "
    new "{color=#f00}hex:{/color} shhhhhhhhhhhhhhhhhhhhhhh"
    
    old "74 68 65 20 65 6e 64 20 6f 66 20 64 61 79 73 20 69 73 20 75 70 6f 6e 20 75 73 "
    new "{color=#f00}hex:{/color} the end of days is upon us"
    
    old "68 61 76 65 20 79 6f 75 20 66 6f 75 6e 64 20 69 74 20 79 65 74 3f "
    new "{color=#f00}hex:{/color} have you found it yet?"
    
    old "74 68 65 20 70 61 72 61 64 6f 78 3f "
    new "{color=#f00}hex:{/color} the paradox?"

#chap4.rpy
    #springtime2
    old "シャイニングスター綴れば、 夢に眠る幻が掌に降り注ぐ！"
    new "{color=#f00}jap:{/color} When you spell the Shining Star, the illusions of your dreams will rain down on your palm!"
    
    old "新たな世界へ-"
    new "{color=#f00}jap:{/color} To a new world-"
    
    old "I'll believe of my sensation、果てしない道の向こうで！"
    new "I'll believe in my sensation, {color=#f00}jap:{/color} on the other side of the endless road!"
    
    old "nosheisntheresheisanillusionthisisntactuallyhappeningsheisgonethegirliloveisgoneletsalllistentothethemesong"
    new "no she isnt here. she is an illusion. this isnt actually happening. she is gone. the girl i love is gone. lets all listen to the theme song"
    
    #springend1
    old "{font=IBMPlexSansArabic-Regular.ttf}يجب أن تعيش.{/font}"
    new "{color=#f00}arabic:{/color} You must live."
    
    old "{font=IBMPlexSansArabic-Regular.ttf}استيقظ يا طفلي.{/font}"
    new "{color=#f00}arabic:{/color} wake up baby"
    
    old "{font=IBMPlexSansArabic-Regular.ttf}.لا{/font} .I was absent as you’d closed your heart completely "
    new "{color=#f00}arabic: No.{/color} I was absent as you’d closed your heart completely"
    
    #sportswars13    
    old "77 68 65 6e 20 68 65 20 73 68 61 6c 6c 20 64 69 65 2c 20 74 61 6b 65 20 68 69 6d 20 61 6e 64 20 63 75 74 20 68 69 6d 20 6f 75 74 20 69 6e 20 6c 69 74 74 6c 65 20 73 74 61 72 73"
    new "{color=#f00}hex:{/color} when he shall die, take him and cut him out in little stars"
    
    old "61 6e 64 20 68 65 20 77 69 6c 6c 20 6d 61 6b 65 20 74 68 65 20 66 61 63 65 20 6f 66 20 68 65 61 76 65 6e 20 73 6f 20 66 69 6e 65"
    new "{color=#f00}hex:{/color} and he will make the face of heaven so fine"
    
    old "74 68 61 74 20 61 6c 6c 20 74 68 65 20 77 6f 72 6c 64 20 77 69 6c 6c 20 62 65 20 69 6e 20 6c 6f 76 65 20 77 69 74 68 20 6e 69 67 68 74"
    new "{color=#f00}hex:{/color} that all the world will be in love with night"
    
    old "61 6e 64 20 70 61 79 20 6e 6f 20 77 6f 72 73 68 69 70 20 74 6f 20 74 68 65 20 67 61 72 69 73 68 20 73 75 6e"
    new "{color=#f00}hex:{/color} and pay no worship to the garish sun"
    
    old "67 6f 20 75 6e 74 6f 20 74 68 65 6d 20 61 6e 64 20 6d 61 6b 65 20 74 68 65 6d 20 62 65 6c 69 65 76 65 2c 20 62 75 74 20 6d 61 6b 65 20 74 68 65 6d 20 74 72 75 73 74 20 79 6f 75 20 66 69 72 73 74"
    new "{color=#f00}hex:{/color} go unto them and make them believe, but make them trust you first"
    
    old "63 75 72 73 65 64 20 62 65 20 74 68 6f 73 65 20 67 65 6e 74 69 6c 65 73 20 6c 65 73 74 20 74 68 65 79 20 64 65 73 74 72 6f 79 20 74 68 65 20 77 6f 72 6c 64 20 77 65 20 68 61 76 65 20 62 75 69 6c 74"
    new "{color=#f00}hex:{/color} cursed be those gentiles lest they destroy the world we have built"
    
    old "66 72 6f 6d 20 61 74 6f 70 20 74 68 69 73 20 72 6f 6f 66 20 69 20 73 70 65 61 6b 20 74 6f 20 79 6f 75 2c 20 6f 20 6d 65 73 73 65 6e 67 65 72 2e 20 6f 20 63 68 69 6c 64 2e"
    new "{color=#f00}hex:{/color} from atop this roof i speak to you, o messenger. o child."
    old "79 6f 75 20 61 72 65 20 70 65 72 6d 61 6e 65 6e 74 20 61 6e 64 20 70 65 72 66 65 63 74 2e 20 69 20 61 6d 20 72 61 62 69 64 20 61 6e 64 20 72 65 76 69 6c 65 64 2e"
    new "{color=#f00}hex:{/color} you are permanent and perfect. i am rabid and reviled."
    
    #armsbentback
    old ".ti dnuora syaw eb syawla lliw ereht tub ,krow srettel eht fo lla ekam t'nac i"
    new "{color=#f00}reversed:{/color} I can't make all of the letters work, but there will always be ways around it."
    
    old ".eurt niamer syawla lliw taht ,txen eht ro dlrow siht ni eb ti rehtehw"
    new "{color=#f00}reversed:{/color} whether it be in this world or the next, that will always remain true"
    
    old ".tsom eht evol uoy eno eht fo kniht ,ecalp eno naht erom ni flesruoy dnif uoy fi"
    new "{color=#f00}reversed:{/color} if you find yourself in more than one place, think of the one you love the most."
    
    old ".traeh ta ylno tub ,kcab uoy gnirb nac taht gniht ylno eht s'taht"
    new "{color=#f00}reversed: {/color}that's the only thing that can bring you back, but only at heart."
    
    old ".ssorc eht htaeneb ereh deirub ,reverof em htiw yats lliw uoy fo eceip a"
    new "{color=#f00}reversed: {/color}a piece of you will stay with me forever, buried here beneath the cross."
    
    old ".erom dna reverof rehtegot yats ew yam .stoor ym era uoy dna ,won eert a ma i"
    new "{color=#f00}reversed: {/color}i am a tree now, and you are my roots. may we stay together forever and more."
    
    old "-llif rieht netae evah smrow eht lit'"
    new "{color=#f00}reversed: {/color}'til the worms have eaten their fill-"
    
    old ".delttes yllanif sah tsud eht lit'"
    new "{color=#f00}reversed: {/color}'til the dust has finally settled."
    
    old ".dlrow eht ni thgir si lla lit'"
    new "{color=#f00}reversed: {/color}'til all is right in the world."
    
    old ".srehto naht dnatsrednu ot reisae era srettel emos"
    new "{color=#f00}reversed: {/color}some letters are easier to understand than others."
    
    old ".elpoep emos era os"
    new "{color=#f00}reversed: {/color}so are some people."
    
    old "?gnihtemos wonk ot tnaw uoy od ,tub"
    new "{color=#f00}reversed: {/color}but, do you want to know something?"
    
    old ".psarg ot elba neeb t'nevah I taht efil ruoy ni tnemom elgnis a neeb t'nsah ereht"
    new "{color=#f00}reversed: {/color}there hasn't been a single moment in your life that I haven't been able to grasp."
    
    old ".sruoy fo tuo tsuj eb syawla lliw I dna ,hcaer ym nihtiw eb syawla lliw uoy"
    new "{color=#f00}reversed: {/color}you will always be within my reach, and I will always be just out of yours."
    
    old ".kcab dneb smra ym taht doG knaht i"
    new "{color=#f00}reversed: {/color}i thank God that my arms bend back."
    
#chap4generics.rpy
    #mayaspringshrinegen
    old "74 68 69 73 20 69 73 20 6e 6f 74 20 68 65 72"
    new "{color=#f00}hex:{/color} this is not her"
    
#Dorm2Events.rpy    
    #tsuneyodorm15
    old "Go ndéana an diabhal dréimire de cnámh do dhroma ag piocadh úll i ngairdín Ifrinn!"
    new "{color=#f00}irish:{/color}  May the devil make a ladder of your spine picking apples in the garden of Hell!"
    
#DormEvents.rpy
    #ayanedorm35
    old "There are some doors that you can never open again 61 6e 64 20 73 6f 6d 65 20 74 68 61 74 20 79 6f 75 20 63 61 6e 20 6e 65 76 65 72 20 63 6c 6f 73 65~~~~~~~~~~"
    new "There are some doors that you can never open again {color=#f00}hex:{/color} and some that you can never close~~~~~~~~~~"
   
    #futabadorm45   
    old "74 68 69 73 20 69 73 20 6e 6f 74 20 77 68 61 74 20 79 6f 75 20 74 68 69 6e 6b 20 69 74 20 69 73"
    new "{color=#f00}hex:{/color} this is not what you think it is"
    
    #roomwithclocks
    old "ようこそ！ "
    new "{color=#f00}jap:{/color} Welcome!"
    
    old "元気ですか？"
    new "{color=#f00}jap:{/color} How are you?"
    
    old "幸せですか？"
    new "{color=#f00}jap:{/color} Are you happy?"
    
    old "ムラムラしてるの？怖いの？教えて。学びたい。学びたい。"
    new "{color=#f00}jap:{/color} Are you horny? Are you scared? Tell me. I want to learn. I want to learn."
    
    old "何で?"
    new "{color=#f00}jap:{/color} Why?"
    
    old "何で? 何で? 何で?"
    new "{color=#f00}jap:{/color} Why? Why? Why?"
    
    old "家に帰りたい。"
    new "{color=#f00}jap:{/color} I want to go home."
    
    old "i̶̛͇̪̇̅̂̍̔̀̚̚ ̴̻͉̣̗͇͓̭̝̈́ẃ̵͚̘͈͚̹̳͔̤͊͋̅̓̈͝ͅa̶̗̹̍̓k̴͎͇̩̘̞̱̙̝̉̕e̷̥̰̯̟̘̳͑́̍̓̏̃͋ ̸̠̮̂̈́́̓́̔͘͝ú̵̧͚̰̩̮̇̑͗ṕ̵͈̘̦͗͗̈̆̅͝ ̸̨̼̝͈̂̉̈́͂i̴̝̻̠̜̠͍̬̤̇̽̆̉͌̕͝n̸̨̲͖͕͚̝̣̤͌͂̕͜ ̵͈͕̹̖̾͆͜a̵̢̩̰̱̰͈̤̒̔͒́̈̒ ̶͍̳̦͓̫͙̠̈́͗̍͐͝͠ȓ̵̢̳̫̄̍͑̃͊̉̉͠ô̸̢̮͚̮̮͇͑̄͐͋͋͛̕͝ͅo̴̰͖̝̜̤̝̦̠͈͝m̸̘̑̑̚ͅ ̸̡̤̝̈̀̊͜͝w̴̹̹̙̹̏̓͊̉̚͝î̴̙̘͍͔̓́͑̀͆͗̏͝t̷̢̛̛͓̮̰͑́͒͌͝ḣ̴̢̢͈̤̻̯̱̖̈̈́̓ ̷̡̢̘̜͚͇͗̇̒c̵̜̥̪̫͔̍l̸̞̟̼͉͈͓̈́̐̓̑̄̃̓̏ŏ̵͔͇͓͙̫̐́c̶̛̲̲̖̐̓͜k̴̨̡̖̮̠̮̭̀̃̈́̊ś̶̨̛̝͊̀̔"
    new "{color=#f00}visual noise:{/color} i wake up in room with clocks"
    
    old "í̴̙͇̪͍̰̣̜̥̹̚t̴̢͕̳̖̲͙͚̲̊̾̾́̐̔̀̾̍ ̵͍͇͑̽͑̌̈́̾͛͘ḣ̵̢̗̥͈̪̂u̸͎̟̭͑̎̉͋̍̍͝r̷̻̰̗͇͌͋ṭ̶̡̢̢̘̭͎̻̺̓͑̈̾̑͋̒s̷̨̱͔̯̽̑̄́̀̉̍͆͆"
    new "{color=#f00}visual noise:{/color} it hurts"
    
    old "i̷̧̺̤̦̻̭͑̓͝ ̵̼͉̂́ẉ̴̳͇͓̭̅͊̆̉̃̉̎̏̎͜â̸̛͚̐̀̇̈́̓̀ņ̶̠̺̲̫̯̱͇̿͌̄͝t̸̙͈͓͐̓̿ ̴̯͗̄͛t̷̹̖̘̉͐̔͜ő̸̢͇͓͚̙͖͇́͆̔̓̕ ̸̮̪̗͎͔͍͊̂͛̆́g̸͇̘̜̅̍̃̎̆͌̿͝͝ȏ̵̡̗̩̜̱͓̞̄͊͌̿̄̀͘͝ ̷̨̝͖͔̩̰͜͝h̵̟̲̘̜͔̤̗̖̄̈̀̇͜͝ǒ̵̡̡͇͎̩̫̗̪̮̏̔ḿ̵̡̡̠̦͔͚͍̰̑̍̐̃̎̚͠e̷̺̟͔̱̽̓͒͆"
    new "{color=#f00}visual noise:{/color} i want to go home"
    
    old "į̷̝͕̼͚͙̪͇̀̓̑͂̌̂ ̷̡̜̟̈́̑̑̓͗̈́̍s̸̖̮̈́̇̅̉͌̎́̑ę̸̠̭̼͍̰̫͋͒̂͛̈́ę̵̢̨̢͚̮͓̐̽̂͜ ̶͕̀́͌́́̚͠m̴͍̞̳͖̦̎̇͒̿͑̆͗̕y̴̟͛̀ŝ̴̢̡̢̪͖͖̳͙͔̿̊̒e̴̹̝̲͋̓͂̽́͒̉͝l̵͖̠̣͎͈̲͊̀͋̄͂̊͗̀̕͜f̷̬͍͙͖̝̀̀̽́͝"
    new "{color=#f00}visual noise:{/color} i see myself"
    
    old "í̴̬̤̮̭̪͗̔̃ ̷̢̢͚͔̬͗̿̎̓̓̈́̓͝d̷̰̦̖̹̤̕o̶̡̬͎̻̠̮̎͑̉͜ͅn̸̤̄̃̑͛̒'̷̢͙̱̖͚̗̥̻̼̿̅̀̈́͐ţ̸̪͎̘͓͑̅̈̅̅̏̈́̚ ̸̨̠̪̮̪̹̈́̅̕͘͠ļ̷̮͖̬̪̍͒̋̾̕͜͝i̵̫̪̗̙̰͖̫͕͂̉̈́̽͑k̵̝̟̉̅ḛ̶̢̱́̓̔͐̆̏ ̷̬̻̰̣̗̝̑̓̂͛͒͘͘͜i̸̯̗͚̩̫̐̊̿̈t̸̢͕̭̲̞̓̈͛̔̏̋̈́͊̆"
    new "{color=#f00}visual noise:{/color} i don't like it"
    
    old "ḯ̶͖͓̉t̸̛͚̳̗͑͆͗̾̓̕ ̸̢̞̗͔͓̰̎͒͆ȑ̵̛͕̠̜̣̣̬̂̏͜͝ȩ̵̨͙̩̳̻̝̭̱͐̍͂m̵̡̢̪̋̐̇̕͠͝i̴̡͎̫̰̒̒̉̓̈́ͅń̵̢̞̩̖̣̰̟͋̈́̂̕͜d̴͉̫̦̰͙̮̘̮̎̎s̶̥͋̓̀́̾̌͘͝͝ ̶̢̨̰͖͖̲̞͖̓̈́̑̿͛m̶͓̘̳̐̇̆̀͝e̸̛̗͚̖̤̬̥͗̊͆̂̎"
    new "{color=#f00}visual noise:{/color} it reminds me"
    
    old "l̸͎̥̲̓͊͝͠ȩ̵̛̳͓̌̈͐̅̕t̶̫̩͎̱̖̠̦̜͈̎̉̓̉̔̎̆̚ ̷͈̟͖̑͆͊̚͠m̵̞̫͈͇̗͈̣̎e̴̡̬̮͛̃̓̌̀̽̒͑ ̴̢̲͉͚̜̰͙̔̓̽̉̆̌̃ͅf̵̤͛̕ǫ̶̤͉͈̆̇̋͒͝͝r̷̟̘͉̥̹̋̈́͌̈́̊ǵ̶͕̓̂̊̑̀̈͂͒e̵̤̓͊̀͗͝t̷̮̝̠̥̼̠̟̀̽͑̐͗̽̎͘͘"
    new "{color=#f00}visual noise:{/color} let me forget"
    
    old "m̴͇̞̪̉̃͐͂͠a̷̢̬̦̼͋̋͛͘ͅk̴̯̟̙̝͕͔͖̗̍͋͝e̷͓̱̓̂̀̿ ̶̩̥̱͉̼̘̩̅ï̴̘̦͊̊͗t̶̜͙͙̘̱̺͉̜̤͗̽̒̊̂͐͝͝ ̸̢̡͖͖͓͇̫̰̏̎ş̵̧̰̳͈̦́͗͛ͅt̶͕̜̳̗͈̆̓̿̚ọ̴̢͌̓̏̓̓͝p̸̯͈̙̳̫̰̊͛̚"
    new "{color=#f00}visual noise:{/color} make it stop"
    
    old "P̷͔̜̩̠̐̔̆̑͘Ē̸̥̰̙̝T̴͈̟̙̬̪̰͇̥̰͂ ̴͙͊́̽̓̔̑̕͝T̶̛̯͙̿̑̓H̴̬̥͔̰͇̤̠͗͗̏͛̃Ȩ̸̺̽́̅ ̸̰̳͇͗̂͂̅̋͛C̸̺̞͔̫̬͂A̴̻̯̥̹͝Ț̵̲̦͐̌̌̒̔̉͂̀͠"
    new "PET THE CAT"
    
    old "ṷ̶͕̜̤̻̣̍͛̈́̓̔͌͜͜ṅ̷̞̺̟̳͇̥̥̰t̴̛͎ą̸̞͙̰͕̣̖̓͛͜ͅņ̸̠͕̙̙̹̣̘̄̇̀̃́̃̆͜g̴̡̧͇̞̪̜̫̫̉l̴̪̫̉ͅe̷͔̻͎̓̈́̓̑̌̈́ ̴̥͂͊̀̿̃̚͝͠ḿ̵̛̛̦͈̙͂͘ę̷̤͈̻̘͙̉̅̒͂̌̓͛ͅ"
    new "{color=#f00}visual noise:{/color} untangle me"
    
    old "m̴̩̭̪̽̀͒̈́̃̚a̵̢͓̗̝̲̻͋͑̏̈̾̚k̵̞̯͕͎̫͗ĕ̷̞̤̜̠͛̈́̍̏͗͑̚ ̵͇̞̞͍̯͘͜m̷̢̳̈́͊̊̔̉̾́̀e̶̡̻͕̠͔̗͎̾̈̔͆̅͌̓ ̴̲͙͈̲͂̌͒̇̌͒͝f̵̟̤̙̘͈̲͛͑̈́͘͝ē̷͓̜̘̙̘̻̝̪̻̆̉̐̏̑͝e̶̪̠̬͎͎̠͌̀ĺ̶̡̢̨̹̳̗̱͒͐̉͝"
    new "{color=#f00}visual noise:{/color} make me feel"
    
    old "ようこそ！"
    new "{color=#f00}jap:{/color} Welcome!"
    
    old "元気ですか？！"
    new "{color=#f00}jap:{/color} How are you?!"
    
    old "幸せですか？！"
    new "{color=#f00}jap:{/color} Are you happy?!"
    
    old "ムラムラしてるの？怖いの？!"
    new "{color=#f00}jap:{/color} Are you horny? Are you scared?!"
    
    old "教えて。 学びたい。 学びたい。"
    new "{color=#f00}jap:{/color} Teach me. I want to learn. I want to learn."
    
    #ticktock
    old "おかえり"
    new "{color=#f00}jap:{/color} Welcome back."
    
    old "Her name is 61 6d 20 69 20 6f 6b 61 79 and she refuses to have sexual intercourse with me on her best friend’s bed."
    new "Her name is {color=#f00}hex:{/color} 'am i okay' and she refuses to have sexual intercourse with me on her best friend’s bed."
    
    old "Good. Thank you, 61 6d 20 69 20 6f 6b 61 79."
    new "Good. Thank you, 'am i okay'."
    
#FutabaEvents.rpy    
    #beachfive9
    old "了解！家に帰ろう！"
    new "{color=#f00}jap:{/color} Got it! Let's go home!"
    
#inappropriatecontent.rpy
    #firstfridayx
    old "おはよう！"
    new "{color=#f00}jap:{/color} good morning!"
    
    #specialclassx
    old "What is wrong, 世界? "
    new "What is wrong, {color=#f00}jap:{/color} world?"
    
    #lettertx
    old "That’s right, it was 61 6d 20 69 20 6f 6b 61 79."
    new "That’s right, it was, {color=#f00}hex:{/color} am i okay"
    
    old "私を破壊する"
    new "{color=#f00}jap:{/color} Destroy me"
    
    old "希望は答えではない"
    new "{color=#f00}jap:{/color} Hope is not the answer"
    
    old "ワナだ。"
    new "{color=#f00}jap:{/color} It's a trap."
    
    old "{s}生きたい。。。{/s}"
    new "{color=#f00}jap:{/color} {s}I want to live...{/s}"
    
    old "{s}助けて。{/s}"
    new "{color=#f00}jap:{/color} {s}Help me.{/s}"
    
    old "74 68 65 72 65 20 69 73 20 6e 6f 20 68 6f 70 65"
    new "{color=#f00}hex:{/color} there is no hope"
    
    #howifeelx
    old "あああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ"
    new "{color=#f00}jap:{/color} Ahhh..."
    
    old "You are absolutely beautiful, 61 6d 20 69 20 6f 6b 61 79."
    new "You are absolutely beautiful, {color=#f00}hex:{/color} 'am i okay'."

    old "62 75 74 20 69 20 68 61 76 65 20 77 61 69 74 65 64 20 73 6f 20 6c 6f 6e 67"
    new "{color=#f00}hex:{/color} but i have waited so long"
    
    old "77 68 79 20 61 72 65 20 79 6f 75 20 64 6f 69 6e 67 20 74 68 69 73 20 74 6f 20 6d 65"
    new "{color=#f00}hex:{/color} why are you doing this to me"
    
    old "6a 75 73 74 20 66 75 63 6b 20 6d 65"
    new "{color=#f00}hex:{/color} just fuck me"
    
    old "69 20 6d 69 73 73 20 69 74"
    new "{color=#f00}hex:{/color} i miss it"
    
    old "69 20 77 61 6e 74 20 74 6f 20 66 65 65 6c 20 79 6f 75 20 69 6e 73 69 64 65"
    new "{color=#f00}hex:{/color} i want to feel you inside"
    
    old "69 20 77 61 6e 74 20 74 6f 20 72 65 6d 65 6d 62 65 72"
    new "{color=#f00}hex:{/color} i want to remember"
            
            
    #ticktockx
    old "I can’t find it in myself to speak. I just keep pounding away at the pussy of 61 6d 20 69 20 6f 6b 61 79."
    new "I can’t find it in myself to speak. I just keep pounding away at the pussy of {color=#f00}hex:{/color} 'am i okay'."
    
    old "61 6d 20 69 20 6f 6b 61 79 Slowly shakes her head, signaling that I’m mistaken."
    new "{color=#f00}hex:{/color} 'am i okay' slowly shakes her head, signaling that I’m mistaken."
    
    old "61 6e 20 65 63 68 6f 20 72 69 6e 67 73 20 6f 75 74 20 69 6e 20 74 68 65 20 64 69 73 74 61 6e 63 65 "
    new "{color=#f00}hex:{/color} an echo rings out in the distance"
    
    old "49 74 20 73 6f 75 6e 64 73 20 73 6f 6d 65 74 68 69 6e 67 20 6c 69 6b 65 20 61 20 73 63 68 6f 6f 6c 20 62 65 6c 6c "
    new "{color=#f00}hex:{/color} It sounds something like a school bell"
    
    old "42 75 74 20 69 74 27 73 20 6e 6f 74 20 6f 6e 65 20 49 27 6d 20 66 61 6d 69 6c 69 61 72 20 77 69 74 68 "
    new "{color=#f00}hex:{/color} But it's not one I'm familiar with"
    
    old "46 6f 72 20 73 6f 6d 65 20 72 65 61 73 6f 6e 2c 20 64 65 65 70 20 69 6e 20 74 68 65 20 62 61 63 6b 20 6f 66 20 6d 79 20 6d 69 6e 64 "
    new "{color=#f00}hex:{/color} For some reason, deep in the back of my mind"
    
    old "49 20 72 65 6d 65 6d 62 65 72 20 73 6f 6d 65 74 68 69 6e 67 "
    new "{color=#f00}hex:{/color} I remember something"
    
    old "49 74 27 73 20 61 20 67 72 65 65 6e 20 73 63 61 72 66 "
    new "{color=#f00}hex:{/color} {color=#008000}It's a green scarf{/color}"
    
    old "41 6e 64 20 74 68 65 20 61 72 6d 73 20 6f 66 20 74 68 65 20 6f 6e 6c 79 20 70 65 72 73 6f 6e 20 74 6f 20 68 61 76 65 20 65 76 65 72 20 74 72 75 6c 79 20 6c 6f 76 65 64 20 6d 65 "
    new "{color=#f00}hex:{/color} And the arms of the only person to have ever truly loved me"
    
    
#KaoriEvents.rpy
    #kaoridate40
    old "{b}月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月月!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"
    new "{color=#f00}jap: {/color}{b}moon moon moon moon moon moon moon... {/b}"
    
#MikuEvents.rpy
    #soccer10
    old "67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 "  
    new "{color=#f00}hex:{/color} get away get away get away get away get away get away get away get away get away "
    
    old "信じて！"
    new "{color=#f00}jap:{/color} Believe me!"
    
    old "信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！"
    new "{color=#f00}jap:{/color} Believe! Believe! Believe! Believe! Believe! Believe!"
    
    #mikudorm55p1
    old "Hola. Gracias por venir a mi casa. Soy Salvador Dalí."
    new "{color=#f00}span:{/color} Hello. Thank you for coming to my house. I am Salvador Dalí."
    
    old "¿Estás buscando la puesta de sol? "
    new "{color=#f00}span:{/color} Are you looking for the sunset?"
    
    old "Sí. La puesta de sol es mi cosa favorita. Quiero tirarle cacahuetes y gritarle a los niños."
    new "{color=#f00}span:{/color} Yes. The sunset is my favorite thing. I want to throw peanuts at it and yell at the kids."
    
    old "¿Niños?"
    new "{color=#f00}span:{/color} Kids?"
    
    old "Si niños."
    new "{color=#f00}span:{/color} Yes, kids"
    
    old "Esa es una razón diferente a la que esperaba. Pero te ayudaré."
    new "{color=#f00}span:{/color} That's a different reason than I expected. But I'll help you."
    
    old "Pero primero, debes saludar a mi gato, Frankie."
    new "{color=#f00}span:{/color} But first, you have to say hello to my cat, Frankie."
    
    old "Has pasado mi prueba. Ahora, escucha mis instrucciones."
    new "{color=#f00}span:{/color} You have passed my test. Now, listen to my instructions."
    
    old "Primero, debes quitarte la lengua. Debes utilizar una cuchilla caliente. Eso evitará que mueras."
    new "{color=#f00}span:{/color} First, you have to remove your tongue. You have to use a hot blade. That will keep you from dying."
    
    old "Después de que tu lengua se haya ido, debes correr en círculos. Haz esto siete veces. Cuando termines, mira al cielo."
    new "{color=#f00}span:{/color} After your tongue is gone, you must run in circles. Do this seven times. When you are done, look up at the sky."
    
    old "Verás una cara. Será una cara especial. No será Frankie."
    new "{color=#f00}span:{/color} You'll see a face. It will be a special face. It won't be Frankie."
    
    old "Dile a la cara, “tu salsa picante es deliciosa.” Luego, gira una vez. Después de eso, te dará una taza."
    new "{color=#f00}span:{/color} Tell him to his face, “Your hot sauce is delicious.” Then, he spins around once. After that, he will give you a cup."
    
    old "En la copa estará la sangre de un niño. Bébela. Saboreala. Sabrás cuándo parar."
    new "{color=#f00}span:{/color} In the cup will be the blood of a child. Drink it. Taste it. You will know when to stop."
    
    old "¿Hacer esto me ayudará a encontrar la puesta de sol?"
    new "{color=#f00}span:{/color} Will doing this help me find the sunset?"
    
    old "Sí. Esta es la única manera de hacer tus sueños realidad."
    new "{color=#f00}span:{/color} Yes. This is the only way to make your dreams come true."
    
    old "Pero ningún sueño se hace realidad sin sacrificar algo. Debes recordar eso. Puede que no valga la pena."
    new "{color=#f00}span:{/color} But no dream comes true without sacrificing something. You have to remember that. It may not be worth it."
    
    old "Entiendo. Seguiré tus instrucciones para poder ver el atardecer. Acepto el sacrificio."
    new "{color=#f00}span:{/color} I understand. I will follow your instructions so that I can see the sunset. I accept the sacrifice."
    
    old "¿Tienes alguna otra pregunta para mí?"
    new "{color=#f00}span:{/color} Do you have any other questions for me?"
    
    old "Sí. Tengo una pregunta más. ¿Dónde está Miku?"
    new "{color=#f00}span:{/color} Yes. I have one more question. Where is Miku?"
    
    old "Sí. La chica de la vagina bonita y las piernas bonitas. "
    new "{color=#f00}span:{/color} Yes. The girl with the pretty vagina and pretty legs."
    
    old "Para llegar a la chica, debes ver el mundo a través de sus ojos."
    new "{color=#f00}span:{/color} To get the girl, you have to see the world through her eyes."
    
    old "¿Cómo puedo hacer eso?"
    new "{color=#f00}span:{/color} How can I do that?"
    
    old "Comienza mirando a través de las paredes."
    new "{color=#f00}span:{/color} Start by looking through the walls."

#NorikoEvents.rpy    
    #norikospring2
    old "79 6f 75 20 61 72 65 6e 27 74 20 6d 65 61 6e 74 20 74 6f 20 62 65 20 68 65 72 65 " 
    new "{color=#f00}hex:{/color} you aren't meant to be here"
    
#SaraEvents.rpy
    #saraspecial30p1
    old "6e 6f 74 68 69 6e 67 20 77 69 6c 6c 20 65 76 65 72 20 6d 61 6b 65 20 73 65 6e 73 65 20 61 67 61 69 6e "
    new "{color=#f00}hex:{/color} nothing will ever make sense again"
    
#script.rpy
    old "6e 6f 74 68 69 6e 67 20 66 61 6c 6c 73 20 62 75 74 20 6d 65"
    new "{color=#f00}hex:{/color} nothing falls but me"
    
    #day21
    old "{s}探してみませんか？{/s}"
    new "{color=#f00}jap:{/color} {s}Why not give it a try?{/s}"
    
    #swimming    
    old "{size=-15}imprettysureitmayhavecausedirreparabledamagetomeaswellsinceitstillfeelslikeit'sstuckinsidesometimes{/size}"
    new "{size=-15}im pretty sure it may have caused irreparable damage to me as well since it still feels like it's stuck inside sometimes{/size}"
    
    old "Are you sure you’re okay with watching this, 61 6d 20 69 20 6f 6b 61 79?"
    new "Are you sure you’re okay with watching this, {color=#f00}hex:{/color} am i okay"
    
    #howifeel    
    old "こんにちは"
    new "{color=#f00}jap:{/color} Hello"
    
    old "笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑!"
    new "{color=#f00}jap:{/color} Hahahahahahahahaha!"
    
    #correcthead
    old "どういう意味?"
    new "{color=#f00}jap:{/color} What do you mean?"
    
    #specialclassroom
    old "あなたは誰?"
    new "{color=#f00}jap:{/color} who are you?"
    
    old "だれ です か？"
    new "{color=#f00}jap:{/color} Who is that?"
    
    #day220
    old "70 72 61 69 73 65 20 62 65 21 70 72 61 69 73 65 20 62 65 21 70 72 61 69 73 65 20 62 65 21 70 72 61 69 73 65 20 62 65 21 70 72 61 69 73 65 20 62 65 21 21 21 21 21 21 21 21"
    new "{color=#f00}hex:{/color} praise be! praise be! praise be! praise be! praise be!!!!!!!!"
    
    old "68 65 6c 70 20 6d 65 21"
    new "{color=#f00}hex:{/color} help me!"
    
    old "49 20 64 6f 6e 27 74 20 77 61 6e 74 20 69 74 20 74 6f 20 62 65 20 6f 76 65 72 21 20 49 27 6d 20 73 63 61 72 65 64 21"
    new "{color=#f00}hex:{/color} I don't want it to be over! I'm scared!"
    
    old "53 65 6e 73 65 69 21 20 49 20 6c 6f 76 65 20 79 6f 75 21"
    new "{color=#f00}hex:{/color} Sensei! I love you!"
    
    old "49 20 64 6f 6e 27 74 20 77 61 6e 74 20 74 6f 20 6c 6f 73 65 20 79 6f 75 20 61 67 61 69 6e 21"
    new "{color=#f00}hex:{/color} I don't want to lose you again!"
    
    old "4e 6f 74 20 6c 69 6b 65 20 74 68 69 73 21"
    new "{color=#f00}hex:{/color} Not like this!"
    
    old "61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 21 21 21 21 21 21"
    new "{color=#f00}hex:{/color} aaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!"
    
    old "4e 6f 21 4e 6f 21 4e 6f 21 4e 6f 21 4e 6f 21 4e 6f 21 4e 6f 21"
    new "{color=#f00}hex:{/color} No!No!No!No!No!No!No!"
    
    old "49 27 6d 20 6e 6f 74 20 72 65 61 64 79 20 74 6f 2e 2e 2e 6c 65 61 76 65 20 79 65 74 21"
    new "{color=#f00}hex:{/color} I'm not ready to...leave yet!"
   
    #babyfinches   
    old "69 74 27 73 20 68 61 72 64 20 66 6f 72 20 6d 65 20 74 6f 20 74 65 6c 6c 20 68 6f 77 20 6d 75 63 68 20 6f 66 20 74 68 69 73 20 69 73 20 72 65 61 6c 20 61 6e 64 20 68 6f 77 20 6d 75 63 68 20 69 73 20 61 20 64 72 65 61 6d "
    new "{color=#f00}hex:{/color} it's hard for me to tell how much of this is real and how much is a dream"
    
    old "53 6f 6d 65 77 68 65 72 65 2c 20 64 65 65 70 20 64 6f 77 6e 2c 20 74 68 69 73 20 66 65 65 6c 73 20 6a 75 73 74 20 6c 69 6b 65 20 79 65 73 74 65 72 64 61 79 2e "
    new "{color=#f00}hex:{/color} Somewhere, deep down, this feels just like yesterday."
    
    old "42 75 74 20 74 68 65 20 66 6c 6f 61 74 69 6e 67 20 63 61 72 73 20 61 6e 64 20 6d 61 6e 67 6c 65 64 20 6d 75 73 63 6c 65 20 6d 61 73 73 65 73 20 62 65 66 6f 72 65 20 6d 65 20 74 65 6c 6c 20 6d 65 20 6f 74 68 65 72 77 69 73 65 2e "
    new "{color=#f00}hex:{/color} But the floating cars and mangled muscle masses before me tell me otherwise."
    
    old "49 66 20 74 68 69 73 20 69 73 20 61 20 6d 65 6d 6f 72 79 2c 20 69 74 20 69 73 20 6e 6f 74 20 61 20 68 61 70 70 79 20 6f 6e 65 2e "
    new "{color=#f00}hex:{/color} If this is a memory, it is not a happy one."
    
    old "42 75 74 20 63 68 61 6e 63 65 73 20 61 72 65 20 69 74 27 73 20 6a 75 73 74 20 61 20 6e 69 67 68 74 6d 61 72 65 2e "
    new "{color=#f00}hex:{/color} But chances are it's just a nightmare."
    
#ToukaEvents.rpy
    #toukastreets5
    old "73 75 64 64 65 6e"
    new "{color=#f00}hex:{/color} sudden"

#TsuneyoEvents.rpy
    #ramen5
    old "{s}74 68 65 72 65 20 69 73 20 6e 6f 20 67 6f 64 20 68 65 72 65 2e 20 6a 75 73 74 20 6e 6f 6f 64 6c 65 73 2e{/s}"
    new "{color=#f00}hex:{/color} {s}there is no god here. just noodles.{/s}"

#YasuEvents.rpy
    #yasuspring2
    old "“68 65 20 69 73 20 69 6e 20 74 68 65 20 72 6f 6f 6d 20 77 69 74 68 20 75 73” she speaks, not knowing that his departure is imminent — for the door swings open and in walks-"
    new "{color=#f00}hex:{/color} “he is in the room with us” she speaks, not knowing that his departure is imminent — for the door swings open and in walks-"

#YumiEvents.rpy
    #streets10
    old "61 20 77 6f 72 6c 64 20 69 6e 20 77 68 69 63 68 20 77 65 20 6c 6f 76 65"
    new "{color=#f00}hex:{/color} a world in which we love"