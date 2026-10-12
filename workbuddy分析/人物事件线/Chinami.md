# Chinami 事件线全析

## 一、角色基本盘

Chinami（千波）是 Chosokabe 家的小女儿，Chika 的亲妹妹（chinamidate20 中她明说"只有 big sis Chika 与我有血缘关系"），也是本作主要角色中年纪最小的之一。她的处境由五个支点构成：

1. **家庭结构**：母亲已故（chinamidate1 中她对母亲照片祈祷："Can you marry Sensei? He is a nice man and he bought Chinami a phone."；chinamispring1 中她说家里"终于有了真正的 altar"，可以好好祭奠母亲，并担心母亲会为她不完美的身体自责——"She doesn't want Mommy to blame herself for Chinami's body not being perfect. Especially since Mommy's body was never perfect either."）；父亲缺席（chinamidate10 中"Two dads in a row don't love Chinami! Is she doomed to live a life of sadness?!"；chinamidate25 中她说希望父亲还在，但"big sis Chika gets angry whenever Chinami says that, so she doesn't say it much"）。她主要由姐姐 Chika 照顾，Yumi 也以「大姐」身份一同照看她，但 Yumi 并非血亲（chinamidate20）。她主动把 Sensei 称作 "Papa"——这个称呼贯穿整条线，是她理解家庭与亲密关系的核心装置。
2. **体弱设定**：对花生致命过敏（chinamidate10 中自述"Chinami is very allergic to peanuts"，并提到此前的 "peanut incident"——Yumi 喂她吃花生，她自己知道过敏却没说，因为"Chinami just likes nuts!"；Sensei 记下"never give her anything with nuts"并自语"Is this what being a parent feels like?"）；免疫缺陷使她不能上学、出门须戴狗头盔（chinamidate5 中 Sensei 心想"she can't even go out in public without gloves and a mask"；chinamidate10 中她获准后只在阳台站了一会儿）；chinamispring3 中叙述者以 Sensei 口吻自述她患有免疫缺陷症（immunodeficiency disorder），并自嘲这病"really only pops up in random sections of the game"——疾病在此被承认为叙事便利，而非稳定的生理事实。她本人在 chinamidate15 用手机自查过病情（"she looked up all sorts of stuff about her condition. She wasn't very pleased with what she read"），并得出"Chinami has no future"的结论。
3. **第三人称自称**：Chinami 几乎全程以第三人称说话。chinamispring4 中她解释这是长年习惯，切换第一人称"harder than it sounds"（"Okay, {i}you{/i} try spending your entire life talking in third person and then having to switch for an entire conversation."）；chinamispring8 中 Hailey 把她持续用第三人称解读为"更信任、更自在"的表现（"You're pretty much exclusively stuck in third person now. Can I take that as you being more comfortable with me?"）。Sensei 也多次点破她在特定时刻"掉出角色"（chinamidate10 结尾旁白："I always feel a little strange when Chinami stops referring to herself in the third person."）。
4. **早熟的资本头脑**：Chinami-Corp 首现于 chinamidate5——她在电话里自称"the CEO"，又点题要听"a little girl who grows up to be the CEO of Chinami-Corp! The biggest Japanese dealer of cute animals!"的故事；chinamidate10 中她介绍公司是"the leading distributor of giraffes and giraffe paraphernalia in all of Japan"，刚完成一笔"acquisition"与"merger"。她懂得 "interest"（chinamidate5："That's what the adults call 'interest.'"）、GME、Jell-O pool 等商业/金融话术（chinamidate10："Chinami has gotten really into the stock market lately and it's opened a big can of worms!"），甚至已设立 Roth IRA（chinamispring8）；她向 Yumi 学商业知识（chinamidate15 中"Thank you for all of the business tips, big sis Yumi!"，Yumi 的口诀是"Just know who you're tryin' to sell to and things'll take care of themselves."）。她用商业话语包裹对亲密关系与家庭的全部理解。
5. **信息黑箱中的孩子**：大人们对她隐瞒性知识，而她恰恰是被这些隐瞒塑造得最扭曲的角色——她从《Game of Thrones》（chinamidate1、chinamispring4）、偷听大人（chinamispring5 中听见 Sensei 与 Chika、以及 Sensei 与 Tsukasa 在隔壁的动静）、以及身边人（如 chinamispring2 中她与 Tsukasa 当着 Sensei 的面大谈 "erection"）的接触中拼凑世界观，得出大量半对半错的结论。

## 二、love 线逐事件脉络

**callchinamimorning / callchinamiafternoon / callchinaminight 及日常系列**
Chinami 线的入口是三个呼叫 label。`callchinamimorning` 按 `chinami_love` 门控依次放行 chinamidate1（love>=0）、chinamidate10（love>=10 且 christmas7）、chinamidate15（love>=15 且 day355）、chinamidate25（love>=25 且 tsukasaspecial1p2）；`callchinamiafternoon` 放行 chinamidate5（love>=5、date1 已发生、day128）与 chinamidate20（love>=20、date15 已发生）；`callchinaminight` 则永远拒拨（"I'm not really sure how I'd explain calling Chinami at this hour if Chika is around, so it would probably be best to hold off for now..."）。无事件可推时，第四章走 chinamispringmorninggen / chinamispringnoongen，第三章走 chinamisummer2morninggen / chinamisummer2noongen，圣诞节后走 chinamimorninggen2 / chinaminoongen2，其余走 chinamigenmorning / chinamigenafternoon。这些日常段落各加 1 点 affection：她穿着睡衣吃 Sensei 做的麦片并提醒"她想要一个小妹妹"（chinamimorninggen2）、裹着冬装玩"pretend-snowman"（chinaminoongen2）、接"Chinami hotline"电话聊糖果和杀猪游戏（chinamigenmorning / chinamigenafternoon）。日常的密度本身即是伏笔——她的世界小到主要由电视、姐姐与电话构成。

**chinamidate1 —— 第一次 babysit**
Sensei 第一次照看 Chinami（Chika 称之为"dog-sit"，因为她今天"won't be wearing her mask"，所以只是"normal Chinami-sitting"）。她演示"假装看电视"（电视里根本没有节目，"Nothing's even playing on the TV"，她坚称"there are dragons and zombie things and a few really funny looking old people"），最爱《Game of Thrones》（手机测验说她属于 House Lannister，"A Lannister always pays her debts"），玩杀猪游戏，并对着亡母照片祈祷，请母亲答应让 Sensei 娶 Chika（"Can you marry Sensei? He is a nice man and he bought Chinami a phone."），理由是"If Sensei and big sis get married, Chinami will be alone less"，此外还想要一个小妹妹。此事件一次性给出她的三大创伤反应：用虚构填补空洞、用虚构亲属定义家庭、用祈祷处理愿望。

**chinamidate5 —— 故事时间与 Yumi 的暴怒**
Sensei 编故事时随口用了 "Chiaki" 一名，Chinami 当即点破那是她母亲的名字（"Chiaki was Chinami's mom's name!"）。故事选题是她指定的：想听"a little girl who grows up to be the CEO of Chinami-Corp! The biggest Japanese dealer of cute animals!"——Chinami-Corp 之名与 "interest" 一词均首现于此事件。她还从 Yumi 房间的壁橱里翻出漫画（"She likes the ones with lots of blood the most."），并以向 Chika 告状要挟 Sensei 讲故事（"Chinami is Chinami-mailing you."）。随后 Yumi 回家撞见 Sensei，暴怒赶人（"GET THE FUCK OUT OF HERE!"、"AND NEVER COME BACK!"、"DIE IN A FIRE!"）。此事件首次暴露 Chosokabe 家对外人（尤其成年男性）的防御机制，也为 Yumi—Sensei 的紧张关系埋线。

**chinamidate10 —— 花生过敏与阳台**
Chinami 讲到此前的 "peanut incident"（Yumi 曾让她吃花生；她自己知道过敏却没说，"Chinami just likes nuts!"），并透露自己最近在炒股（GME）、想养 Jell-O pool。随后她只求获准上阳台站一会儿——她小时候爬栏杆差点摔死，此后每次都要先问许可。阳台上她短暂掉出第三人称（"{i}I{/i} appreciate that."），说出想要一个小妹妹、想要 Jell-O pool，也留下"Two dads in a row don't love Chinami! Is she doomed to live a life of sadness?!"一句。Sensei 旁白收束："I always feel a little strange when Chinami stops referring to herself in the third person. But I need to remember that she's a lot smarter than she lets on."阳台谈话把死亡焦虑转化为孩子式的补偿幻想。

**chinamidate15 —— 冬季泳池派对**
Yumi 在 kiddie pool 里教商业知识（"Just know who you're tryin' to sell to and things'll take care of themselves."），因被 Sensei 撞见而狼狈逃走。派对本身的理由是"big sis Chika and big sis Yumi felt bad for Chinami because she can't go to the beach with all of the other girls. So they tried to bring the beach to her instead."。Chinami 用手机自查病情（"she looked up all sorts of stuff about her condition. She wasn't very pleased with what she read"），并说出全线最冷的一句自我判定：

> ch: Chinami has no future.
> ch: Or at least not the kind of future her sisters and their future husband do.

一个孩子以商业评估的口吻宣判自己的未来，是她"用公司话语处理恐惧"模式的顶点。

**chinamidate20 —— 商场狗面具与 Rin 的眼泪**
商场偶遇 Rin 与 Otoha。Chinami 说出"There's big sis Chika and big sis Yumi! But only big sis Chika is related to Chinami by blood."，Rin 由此确认她是谁；Chinami 又转述 Chika 曾说 Rin "had very pretty eyes. And that she wanted hers to look more like yours."。Rin 含泪却并未崩溃——她自嘲"And here I thought I was done crying over this."，笑着说出"Better than nothing, I guess!"，并请 Chinami 对两个姐姐保密（"please don't say anything about this to either one of your sisters. I don't really want to confront it again after it's already over."）。Chinami 还从对话里第一次知道"girls could like other girls"（"Until today, she didn't know that girls could like other girls!"）。此事件把 Chinami 定位为各条创伤线（Rin—Chika）的意外引爆点：她自己毫不知情，却触发了他人最深的伤口。

**chinamidate25 —— 过家家与 Tsukasa、Touka**
Chinami 称"business partner"即将到访，实际是 Tsukasa 带着姐姐 Touka 一同上门。Sensei 被拉入"play house"：Tsukasa 提议"Chinami and I will be sisters and you two can be the parents!"；Chinami 追问"How come Chinami doesn't look like either one of her parents?"，把"Mother 有 affair"的玩笑说出口的是 Sensei（"There can only be one explanation." / "Your mother is having an affair."），Tsukasa 随即入戏追问是否是园丁。事件中她还喊"Chinami wants to eat peanuts!"，逼 Sensei 说出"I don't care how badly Chinami wants to eat peanuts when peanuts will kill her."；Touka 则为公寓的贫困当场泛泪（"I am beginning to believe that everything about today has been carefully designed to reduce me to tears."）。事件结尾 jump 至 yumichikaspecial1——Chinami 的日常事件在此接入 Chika/Yumi 与 Tsukasa/Touka 的交叉线。

**chinamidate30 —— 商场、头盔与一声咳嗽**
由 ChikaEvents.rpy 在 `chinami_love >= 30`、`yumiyukispecial1 == True` 且 `chinamidate30 == False` 时跳入。开篇是 blood1–4 四张静态图与一个名为 "{s}transgression{/s}" 的转场；Sensei 去商场本是为了向"fake girlfriend"索取报酬（"time to fuck my fake girlfriend"），却撞见 Chika 带 Chinami 试穿衣服。Chika 讲到一半的"thick-"被 Chinami 的归来打断，慌忙改词"Meatloaf!"，Chinami 当街复读"Papa's thick meatloaf"；她又从 Tsukasa 的姐姐 Touka 处听说"affair"一词并当场使用（"Chinami knows something like that is called an affair now!"）。Sensei 的内心以删除线独白滚动（"{s}Fuck me while she can't see us.{/s} Yes."），Chinami 在美食广场摘下狗头盔透气，甚至短暂掉出第三人称（"I seriously can't do it anymore!"），Sensei 以"heatstroke"为她圆场。结尾旁白只有两行：

> "A stifled cough, silenced by the head of a dog."
> "And a reactive 'arf' to hide it."

事件设 `buckettoken = True`（该变量随后被 happytracker.rpy、newchecker.rpy、screens.rpy 的回放入口与 script.rpy 的 day 7 地名判定读取），chinami_love 与 chika_lust 各加 1。

**chinamispring1 —— 独处、鬼魂与 altar**
Chika 穿着女仆装出门（"I am {i}not{/i} supposed to be wearing this yet!"），Chinami 独自与 Sensei 相处。她追问 Sensei 为何可能不再来看她（"This might be the last time Chinami sees you?"），劝他别抛下 Chika（"If you stop coming here, big sis Chika might go crazy...And you'll be running away for the rest of your life."），并说"Come here, Papa"靠向他。Sensei 承认自己一直在逃离"A ghost."；她还用一部师生恋韩剧类比 Sensei 与 Chika 的关系（"She watched a K-drama where a teacher kissed a student and everybody got mad."）。她向母亲照片介绍 Sensei（"She can't hear you. She's just a picture."），提到家里"终于有了真正的 altar"、可以好好祭奠母亲，并担心母亲为她不完美的身体自责，最后说出"I don't want to hide behind a mask forever. I want to be a normal girl...and do normal things."，甚至说"And one day, Chinami will be 'just a picture' too."。结尾她谎称已替 Sensei 答应了"business partner"（Tsukasa）来授课，门响，jump chinamispring2。

**chinamispring2 —— business partner、Catcher in the Rye 与关游戏通牒**
Tsukasa 以"business partner / 学生"身份上门（她租下了 Chinami 隔壁的房间），逼 Sensei 当 tutor。Chinami 用"Papa 被 past 的鬼魂缠身，逼他做错误决定、不能好好爱 Chinami"解释 Sensei 的心病（"Papa is haunted by the ghost of his past. It forces him to make bad decisions and not love Chinami as much as she's supposed to."）。随后出现斜体恐声块——直接对玩家喊话的元叙事插入：

> "{i}Answer: The worst that could possibly happen is you 'falling' for one of them long before they're meant to be fallen for, and leveraging YOUR power to make them do what YOU want them to do!{/i}"
> "{i}Do it!{/i}" / "{i}Collect more skin!{/i}" / "{i}Be the PERVERT we all know you to be!{/i}" / "{i}If she will not come back, simply MAKE A NEW HER.{/i}" / "{i}CHOOSE.{/i}"

紧接着就是一个货真价实的菜单："Choose" Chinami（设 `chinamichosen`）或 "Choose" Tsukasa（设 `tsukasachosen`）——"CHOOSE."与选择界面被直接焊死。Sensei 问起《The Catcher in the Rye》，插入 Maya 与 Noriko 关于 Holden Caulfield 与抑郁症的争论；Tsukasa 随后把 Sensei 的沉默称作"silent method"（其实他睡着）。场景中出现关键元叙事注记：

> "She wasn't blurred this time."

——直接承认存在一套对角色面容/存在进行"模糊"处理的机制。随后 Chinami 与 Tsukasa 以粗体大字互相开 "erection" / "dog sex" 的玩笑（"Let's do dog sex!"），并插入 Maya/Noriko 的"lust stat"元对话（"You've had your lust stat turned on since you were added to the game"）。事件结尾以 molech 图像与系统提示收束：

> "iT IS never TOo lATE TO TUrn OFf thE GAMe"

之后 jump 至 amispring1——Chinami 线的日常事件直接接入 Ami 线，暗示两条线底层共享同一循环结构。本事件也是全线唯一一次 chinami_love 与 tsukasa_love 各加 10 的跳跃。

**chinamispring3 —— 倒悬天空、病中照护与三分支**
开篇是倒悬天空、Backwards Boulevard 的意识流诗（"I'm the king of everything — with a black paper crown and cuff-links sewn by silkworms..."）。Chika 在 great pareidolia mall 找到新工作，托 Sensei 照顾发烧的 Chinami。Sensei 的内心独白以本名自白：

> "Hello. My name is Akira Arakawa. I have a wife named Chika and a daughter named Chinami."
> "These are not delusions."

他必须靠反复背诵才相信这个虚构家庭，并自嘲她的免疫缺陷"really only pops up in random sections of the game"。病中的 Chinami 要求 Papa 陪浴，Sensei 以"我是男人一切错误的总和、是会杀死你的病毒"拒绝（"I'm the amalgamation of all that's wrong with man...I'm a virus that would surely kill you if the right...precautions aren't taken."）。此处按 `sawchinami` / `tsukasachosen` / `tsukasarefused` 分为三种走向：
- **Endanger her**（仅当 `sawchinami == True and tsukasachosen == True and tsukasarefused == False` 时出现）：Sensei 屈服，闪过历代女孩的立绘与"{b}I MUST BE A GOOD BOY.{/b}"，随后 jump chinamispring4；
- **Protect her**（同上条件）：他拒绝，系统旁白一边赞他"such a good guy"，一边宣判在这个世界里他是懦夫、是 creep，并断言"Everyone else is growing. And you'll never catch up at this rate."，最后以"{i}Chinami enjoys the soup!{/i}"了事；
- **无条件拒绝（else 分支）**：Sensei 直接爆粗"Absolutely fucking not."，Chinami 哭喊"Chinami's Papa won't even wash her back!"后独自洗澡；旁白留下改写过去的执念——"If you'd have told me when I was younger that it's possible to rewrite the past...it's almost all I think about."，并交代"Chika returns home a short while later. She looks like she fell through a hole."

同一段叙事内同时给出赞许与羞辱，三个走向都不是干净的"好结局"。

**chinamispring4 —— 洗发与 Jaime Lannister**（仅在 Endanger 分支后可达）
延续浴场场景，但 Sensei 始终没有进入浴缸——他坐在缸外别过脸，最终只应 Chinami 要求为她洗头（"Chinami will come close to you."）。Chinami 用《Game of Thrones》类比 Sensei—Chika—Yumi 的三角关系（Jaime/Cersei/Brienne，"love triangles always make somebody upset and you're the tip of your own triangle"），并追问 Sensei 是否因为自己是"your type"才不敢共浴（"Or maybe {i}I'm{/i} your type and that's why you're afraid to get in the bath with me."）。她首次说出 "lolicon" 一词（自承学自 Yumi："Big sis Yumi accidentally taught Chinami {i}lots{/i} of bad words."）。Chika 提前回家撞见洗发的画面，狂喜大喊：

> c: KYAAAAAAAAH! OHMYGOD! THIS IS THE CUTEST THING I'VE EVER SEEN IN MY LIFE! IT'S LIKE WE'RE AN ACTUAL FAMILY!

还要换衣服进浴缸，Sensei 慌忙逃逸。虚构家庭在不知情的姐姐眼中达到了完满。

**chinamispring5 —— 偷听、Tsukasa 的包办婚姻危机**
开篇旁白是一段故意含混的淫乱记述（"The sorts of feelings {i}anyone{/i} would get after watching a little sister take LOADS of cum from the hung guy and his MASSIVE cock for the first time."），实写 Chinami 先后听见 Sensei 与 Chika、以及 Sensei 与 Tsukasa 在隔壁的动静。她与 Sensei 展开全线最惊人一段谈判：她透露 Tsukasa 的母亲 Tsubasa 正在为 Tsukasa 安排婚姻（"one of those 'arranged marriage' things"），而 Tsukasa 不敢拒绝；她从电影里学来逻辑——"A man no longer wants a girl if she's already been with another man..."——并暗示 Sensei 可以做那个男人，她保证保密（"She won't tell if he wants to be that man."）。Sensei 惊恐拒绝（"You watch too many movies."），但承诺去和 Tsukasa 谈（"Then...I'll talk to her. If she really {i}does{/i} look up to me. But that's all."）。此事件确立 Chinami 的核心矛盾：她不是无知，而是用从影视里学来的扭曲逻辑主动"安排"大人的性关系，动机是保护朋友（"No! Chinami just doesn't want to lose her friend!"）。

**chinamispring6 —— 阳台之夜与目击**
Chika 深夜在阳台把 Sensei 叫醒手交并发生关系（"I have a balcony..."），而 Chinami 半夜醒来找水，目睹了全程——"For ten minutes she watched them, standing still as a statue and hoping she'd be caught. But she wasn't."。她的反应不是兴奋，而是"She was angry, but she didn't know why. She was sad, but she didn't know why. She felt guilty, but she didn't know {i}why.{/i} Yet she couldn't look away."，并联想起"the video she'd watched earlier"。次日早晨的对峙是全线喜剧与恐怖的混合巅峰：Chika 用疯狂做五百块煎饼逃避话题、以"our phones are tracking us"为由要没收两人的手机防止她"自己查"（"I've decided that I'm going to get rid of {i}both{/i} of ours!"），最终承认错误并承诺"So I'll {i}teach{/i} you, but...I need time to figure out {i}how{/i} first."。结尾旁白：

> "And so one more fruit began to ripen."
> "How far will it fall from the tree, I wonder?"

明确宣告 Chinami 正在走向性成熟，而所有大人能做的只有拖延。

**chinamispring7 —— Niki 公开恋情与持刀的 Chika**
Niki 向全世界公开与 Sensei 的恋情（"I confirmed this to the entire world on social media"），Chika 当场心碎成紧张性木僵（叙述者直接用"catatonia"一词），手持菜刀一动不动——Chinami 叫人送一大袋花生上门、当场威胁要当着姐姐吃花生都无法让她眨眼，只能把她拖到椅子上。Chinami 独自应对失败后打电话向 Papa 求援，甚至提出"替姐姐同意 Sensei 用做爱唤醒她"的方案（"She grants you consent on behalf of her big sister."），被 Sensei 以"She's holding a knife."挡回。最终 Sensei 召来 Niki 本人处理（Niki 隔着电话骂他"teen-fucking human dildo"）。此事件中 Chinami 首次被推上"照护者"位置并明确抗议：

> ch: Chinami's not supposed to be the caregiver in this relationship! {i}She{/i} is!

**chinamispring8 —— 传送门、派对世界与 Hailey**
Chika 化身 Niki 周边扫货狂人（"Niki first, boba second!"），带 Chinami 搜遍唱片行。Chinami 与不会说话的 Nao（以"!"交流）偶遇商场里的两扇传送门（Death 门与 Life 门）；旁白给了一个关于"换一个新老婆"的黑色玩笑（"then replace her piece by piece until she's a new wife...JOKE."），Chinami 则说自己选"Life"门（"Because life is objectively better than death."），两人一同穿门进入一个美式派对世界：那里有 Hailey Hawthorne（野兔，密歇根来）、Paul、Octavia（章鱼，"three hearts"）、Beatrice（蜜蜂）、Howard、Lamar 等兽人角色；Howard 提到 Kumon-mi 是"that city they blocked off from the rest of the world during that extremely isolated space war a few years back"，Chinami 的手机在这里也没有信号（"International roaming plans don't make much sense when your city is closed off from the rest of the world"）。

Hailey 以典型 grooming 话术逐步接近 Chinami：先请她"step outside to get some air and escape from all the noise"脱离人群，把接吻重新定义为"impulses"（"Don't call them mistakes. They're {i}impulses.{/i} Just {i}wanting{/i} to do something doesn't automatically make it wrong."），再以"practice with me"提出练习接吻，最后直接告白"I want to kiss you. Your mouth. Your neck. Your hands. Everywhere. I have since the moment I saw you."；她也把自己的越界欲说成"Getting close to someone you know you shouldn't...there's just something so...exciting and {i}new{/i} about it."。Chinami 同意（"You can kiss Chinami. But only for a little while, okay? And only because you made her heart beat really fast just now."），并要她对自己姐姐保密——Hailey 回答"Yeah, don't worry. I've had plenty of girls tell me the exact same thing."。接吻前的最后几个画面（闭眼、"I'll start slow..."、"Please forgive me if I can't control myself after a few seconds."）在静态图序列后切黑，随即被 Nao 的归来打断，场景切回 Chika 的扫货狂潮。

而派对宾客早已把 Hailey 的模式说穿：Beatrice——"this was done and dusted the second Hailey found out she wasn't from around here. Exactly her type too."，并补充"{i}inexperienced{/i} is more politically correct"；Octavia——"Hailey seemed different this time. Maybe she actually likes her." / "It's not {i}my{/i} fault she subsequently {i}stops{/i} liking them shortly afterward."；Lamar——"Manic pixie Hailey is back in action to swipe some newcomer off her feet."。此事件是 Chinami 线第一次让她暴露在"另一个掠食者"面前——而叙事在此处戛然而止，把最危险的接触留成悬案。

## 三、lust 线概貌

Chinami 线中直接涉及性/成人话题的段落，在叙事功能上可归为五类：

1. **感官启蒙段**：阳台目击（chinamispring6）前后，Chinami 第一次将"性"与"身边的具体的人"挂钩。她的反应不是欲望，而是无法命名的愤怒、悲伤与愧疚的混合物（"She was angry, but she didn't know why..."），功能是呈现"过早目击"对儿童心理的腐蚀。
2. **语言污染段**：从 "erection"（chinamispring2 中她与 Tsukasa 当众大谈）、"lolicon"（chinamispring4，Chinami 自承学自 Yumi）到 "dog sex"（chinamispring2 中"Let's do dog sex!"）、"affair"（chinamidate30，学自 Tsukasa 的姐姐），这些段落记录她词汇表中成人词汇的累积——每个新词都来自某个大人的失职或玩笑。
3. **掠食者引力段**：Hailey 派对事件（chinamispring8）构成完整的 grooming 教科书样本：孤立（"step outside to get some air and escape from all the noise"）、正常化（impulses 理论）、升级（"practice with me"）、保密要求（"I've had plenty of girls tell me the exact same thing."）。Chinami 的体弱、缺爱、无朋辈（"Basically never. I'm not even allowed to go to school."），使她成为理论上最易猎食的目标。
4. **成人欲望的擦边段**：chinamidate30 中 Sensei 赴商场本欲向 Chika 索取"报酬"（"time to fuck my fake girlfriend"），全程以删除线独白与"thick meatloaf"谐音梗把儿童在场的欲望压抑喜剧化；这段的落点却不是性，而是那声被狗头闷住的咳嗽。
5. **循环填充段**：gen2 系列与部分日常场景（看电视、吃饭、游戏）以近似重复出现，其功能与 callchinami 日常 label 一致：为循环提供可无限重放的"安全日"，同时用重复本身暗示时间并未真正前进。

## 四、与主线/元叙事咬合点

1. **模糊机制的自供**： "She wasn't blurred this time." 是 Chinami 线（chinamispring2）中直接承认"存在对角色进行模糊处理机制"的注记。
2. **"CHOOSE."与真菜单**： chinamispring2 的斜体恐声块以"CHOOSE."收尾，紧接着就是 "Choose" Chinami / "Choose" Tsukasa 的选择界面——元叙事层的恫吓与游戏机制被直接拼接。
3. **lust stat 的自供**： 同场插入 Maya 与 Noriko 的对话——"You've had your lust stat turned on since you were added to the game"——角色数值被当成谈资。
4. **关掉游戏的最后通牒**： chinamispring2 的乱码警告 "iT IS never TOo lATE TO TUrn OFf thE GAMe" 把 USER 层的劝退信息嵌进儿童日常事件，随后以 molech 图像跳 amispring1——Chinami 线与 Ami 线在循环结构上直接连通。
5. **免疫缺陷的自指**： chinamispring3 中叙述者明说她的病"really only pops up in random sections of the game"，疾病被承认为叙事便利而非生理事实。
6. **Kumon-mi 封闭的外部证词**： 派对世界的 Howard 说 Kumon-mi 是"that city they blocked off from the rest of the world during that extremely isolated space war a few years back"（chinamispring8），从异世界人口中侧证主舞台与外界隔绝；Chinami 自己也知道手机在这里没有信号、"walls are down"尚需时日。
7. **传送门系统**： Death/Life 双门出现在 pareidolia mall，与 Nao（不能说话的女孩）绑定。Nao 的沉默、传送门、派对世界共同构成 Chinami 线独有的支线入口；源文中 Chinami 与 Nao 经由 mall 的传送门进入派对世界，门是谁放置的、为何只有她们进入，正文均无交代。
8. **Akira 的自我催眠**： chinamispring3 中 Sensei 以真名背诵虚构家庭关系（"Akira Arakawa... wife Chika... daughter Chinami"）来维持现实感，说明 Chinami 的 "Papa" 叙事已经反噬施术者本人。
9. **果实成熟的宣告**： chinamispring6 的 "one more fruit began to ripen" 以旁白身份把 Chinami 的性成熟登记为叙事事件——她的成长被系统性地当作倒计时管理。
10. **buckettoken 的跨文件引用**： chinamidate30 设 `buckettoken = True`，该变量随后被 happytracker.rpy、newchecker.rpy、screens.rpy 的回放入口与 script.rpy 的 day 7 地名判定读取——一场儿童日常事件直接挂接着收集/进度系统。

## 五、未解伏笔

1. **阳台目击的后果**： Chinami 目击了十分钟却未被发现的性爱场景（chinamispring6），这段记忆将如何影响她对 Sensei 与 Chika 的态度，事件结束时未爆发。
2. **Hailey 的未完成接触**： 接吻已进行到闭眼阶段即被 Nao 打断（chinamispring8），但 Hailey 知道她的名字、城市（Kumon-mi）、家庭结构（只有一个姐姐），且 Chinami 承诺保密；宾客更已预言 Hailey"subsequently {i}stops{/i} liking them shortly afterward"。这条掠食线索完全悬置。
3. **传送门与 Nao**： 门是谁放置的、为何只有 Chinami 与 Nao 进入、Nao 为何不能说话、她在派对世界经历了什么、两人如何回家——全部无解。
4. **Chiaki / 母亲之名**： chinamidate5 中 Sensei 编故事用到 "Chiaki"，Chinami 点明那是她母亲的名字；母亲已故，名字背后的往事未再展开。
5. **"Chinami has no future" 的字面性**： chinamidate15 中她的自我判定，与 chinamispring1 中"And one day, Chinami will be 'just a picture' too."的自觉，究竟是抑郁式修辞，还是对"这个角色不会活到结局"的元叙事直觉，未验证。
6. **Tsubasa 的包办婚姻**： Sensei 承诺去和 Tsukasa 谈（chinamispring5），Chinami 线本身未再直接交代此事结果。
7. **Rin 与 Chika 的过去**： "you had very pretty eyes" 引发的眼泪（chinamidate20）指向两人共享的一段历史，Chinami 永远不会知道全貌——Rin 甚至要求她保密。

> 按源行号检索本角色 label，见 `索引/Chinami索引.md`。
