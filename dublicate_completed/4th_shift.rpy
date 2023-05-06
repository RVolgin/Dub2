label dct_4th_shift:
    scene black
    play music music_list["trapped_in_dreams"]
    show headline_text u"Четвёртая смена" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    stop music fadeout 1
    
###############
#Глава 1. Двое#
###############    
    
label d_duo:
    $ save_name = u"Дубликат. Четвёртая смена -\nДвое из леса"
    $ day_time()
    scene black
    show headline_text2 u"Двое из леса" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_ext_backdoor_day_7dl with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["i_want_to_play"]
    "Вся эта история началась на четвёртый день смены, перед обедом."
    "Ульянка, поднырнув под створки хозяйственных ворот лагеря, выбралась на волю и решала, как ей реализовать полученные возможности."
    show us smile sport far at fleft with moveinleft
    th "Ну, раз уж я сбежала, то чем я займусь? Так, чтобы потом не было мучительно больно за бездарно потраченное время."
    show us grin sport with dspr
    th "До обеда ещё целый час, между прочим."
    show us normal sport close with dspr
    th "Далеко не пойду — приключения приключениями, а обед по расписанию."
    th "Кошкодевочку поискать? Что там Сыроежкин вчера говорил?"
    stop music fadeout 1
    stop ambience

    scene ext_dining_hall_near_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    us "Сыроежка! Постой!"
    show el upset pioneer with dspr
    el "Ульяна, ну чего тебе?"
    us "Ты, ты, что ты за обедом про кошкодевочку Женьке говорил? Я всё слышала! Лучше сразу сознавайся, а то я вам спокойно жить не дам!"
    show el normal pioneer with dspr
    el "Ах вот что тебе надо."
    show el grin pioneer with dspr
    el "Ну слушай."
    show el serious pioneer with dspr
    el "Ходит слух, что водится тут в лесу такой человекокошачий гибрид: на вид — девушка лет шестнадцати, только с кошачьими ушами и хвостом, живёт где-то рядом с лагерем, кто её встретит — тому в жизни потом повезёт."
    show el grin pioneer with dspr
    el "Вот всё, что я знаю."
    stop ambience
    
    scene dct_ext_backdoor_day_7dl with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["i_want_to_play"]
    show us normal sport close at fleft with dspr
    th "Или ну её, кошкодевочку — Сыроежка наврал поди. Может, проверить малинник? Или сходить искупаться? Здесь вожатки нет, здесь никто из воды выгонять не будет."
    "Но пока Ульянка думала и крутила головой вправо-влево, выбирая между реальными и соблазнительными малинником и рекой и недостоверной, но зато романтично-загадочной кошкодевочкой, жизнь всё решила за неё."
    play sound dct_sfx_grass_steps
    "Со стороны леса послышались голоса, и на старый, заросший травой асфальт площадки перед воротами вышли двое."
    th "Стоп! А это ещё кто?" with hpunch
    "Первой шла невысокая девушка лет девятнадцати. Красная футболка, почти такая же, как у Ульяны, джинсы, обрезанные до колен, кеды и противогазная сумка через плечо."
    show us surp1 sport with dspr
    th "Тут же на триста километров, говорят, ни одной деревни нет, только лес вокруг."
    stop music fadeout 3
    show d_sf normal pioneer with dspr:
        xcenter 1.2
    show d_us normal sport at cright with moveinright:
        ypos -0.05
    show d_us smile sport with dspr
    stop sound
    voice "Вот мы и пришли, Рыжик."
    "Пионерка вздрогнула, но почти сразу поняла, что обращаются не к ней, а к гостье."
    "Вторым на поляну вышел парень лет двадцати пяти, высокий, худой, с копной каштановых волос, зачёсанных назад, в вожатской форме, но без галстука, только с каким-то чёрным шнурком на шее, прячущимся под рубашкой, и с выгоревшим на солнце, а когда-то голубым рюкзаком за плечами."
    show d_us normal sport with dspr
    show d_sf normal pioneer at fright with move
    $ renpy.pause (1)
    show d_sf laugh pioneer with dspr
    show us surp3 sport far with dspr
    $ renpy.pause (1)
    show d_sf normal pioneer with dspr
    d_s3 "Привет, Ульяна. Виола у себя?"
    show us shy2 sport far with dspr
    $ renpy.pause (1)
    show us normal sport far with dspr
    play music music_list["farewell_to_the_past_edit"] fadein 2
    us "У себя с утра была. Если уже не в столовой."
    hide us with moveoutleft
    show d_us smile sport at right with move:
        ypos -0.05
    hide d_sf
    hide d_us
    hide us
    with dspr
    "Парень молча кивнул головой, благодаря, а девушка поправила волну медно-красных волос на плечах и ещё раз улыбнулась Ульяне."
    "Парочка, обойдя Ульянку, прошла к воротам, а Ульянка смотрела им вслед и думала, где она могла их видеть, особенно парня."
    show us normal sport with pixellate
    th "И откуда он меня знает?"
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_backdoor_day_7dl_zoom with pixellate:
    play ambience ambience_forest_day
    show d_sf normal pioneer at left with dspr
    "У ворот парень подёргал створки, потрогал сквозь щель между ними висячий замок, запирающий ворота, удивлённо качнул головой и сказал, обращаясь к спутнице:"
    d_s3 "Обошлось. А если бы вы несовместимы в границах узла оказались? Позиция у тебя повыше, конечно, будет, но здешняя хозяйка-то тут у себя дома и четыре дня уже с самого начала цикла живёт."
    show d_sf smile pioneer with dspr
    "Тут парень глянул на подошедшую поближе Ульяну."
    show us surp1 sport far at fright with dspr
    show d_sf normal pioneer with dspr
    d_s3 "Кто-то мог бы и вылететь. Ты мне слишком дорога, а хозяйка достаточно симпатична, чтобы на кого-то из вас ставки делать."
    d_s3 "Отлавливай вас потом в следующем цикле по всей Сети."
    show d_us normal sport at fleft with dspr:
        ypos -0.05
    d_u1 "Зануда."
    hide d_us with dspr
    "Коротко ответила девушка и полезла под ворота."
    hide d_sf with dspr
    "А когда парень, кряхтя и как-то с трудом и неестественно сгибаясь, полез следом, уже с той стороны ворот добавила:"
    d_u1 "Вот влюбилась же в зануду."
    "И уже другим голосом спросила:"
    d_u1 "Болит спина, Сёмк?"
    d_s3 "Ничего, Виола подлечит."
    show us normal sport at center with move
    th "Сёмка? Семён? Запомним."
    hide us with pixellate
    play music music_list["mystery_girl_v2"]
    "Запах тайны и приключений был так силён, что Ульянка, едва подождав, пока пришельцы отойдут от ворот, полезла за ними следом и так и сопровождала парочку до самого медпункта, стараясь не пропустить ни одного слова."
    $ renpy.pause (4, hard = True)
    stop music fadeout 1
    stop ambience
    
    scene ext_path2_day with squares:
        walking
    play ambience ambience_forest_day
    play sound_loop dct_sfx_steps2
    play music cambo_coffee
    show d_sf normal pioneer at fleft with dspr
    me "Мы что, играем в шпионов, Рыжик? Почему через лес ломимся, почему как нормальные люди по асфальту не пошли?"
    hide d_sf
    show d_us normal sport at fright:
        ypos -0.05
    with dspr
    d_u1 "А где ты видишь нормальных? Так интереснее, да и Виоле твоей сюрприз будет."
    hide d_us
    show us surp1 sport
    with dspr
    th "Эй! Это же моя секретная тропинка к медпункту. Откуда вы её знаете?"
    hide us
    show d_sf normal pioneer at fleft
    with dspr
    me "Кому интереснее? Тебе от здешней публики прятаться, или твоей здешней тёзке нас скрадывать?"
    hide d_sf
    show d_us normal sport at fright:
        ypos -0.05
    with dspr
    d_u1 "Как ты меня учил, Сёмк? Да! А что «Да» — сам догадывайся…"
    hide d_us
    show d_sf normal pioneer at fleft
    with dspr
    me "Сам догадывайся, зануда?"
    hide d_sf
    show d_us normal sport at fright:
        ypos -0.05
    with dspr
    d_u1 "Вот видишь, ты сам всё понимаешь. Но не исправляешься."
    hide d_us
    show d_sf normal pioneer at fleft
    with dspr
    me "Молодая ты ещё. Я бы даже сказал, мелкая. Не понимаешь силу ностальгии — может, я хочу сейчас перед Гендой слезу пустить."
    hide d_sf
    show d_us normal sport at fright:
        ypos -0.05
    with dspr
    d_u1 "Здесь пускай свою слезу, старче, вот хоть у той берёзы. Сам же говорил, что всё тут облазил лучше, чем здешняя я."
    d_u1 "А я так не хочу, чтобы её и меня сравнивали и спрашивали, не родственники ли мы."
    show d_us hurt sport with dspr
    d_u1 "Это от твоих двойников вечно не протолкнуться, а я свою, своего в первый раз увидела. И сначала обрадовалась, а сейчас почему-то трясусь от страха."
    show d_us laugh sport with dspr
    d_u1 "Да и ты тоже. Думаешь, я не знаю, почему ты волосы назад зачёсывать начал? Надоело ведь, что все твоё сходство со Вторым замечают?"
    hide d_us
    show us surp1 sport
    with dspr
    th "Идите помедленнее. Я же не успеваю! Мне же ещё и прятаться от вас приходится."
    hide us
    show d_sf smile pioneer at fleft
    with dissolve
    me "Уела, Рыжик. А здешней не бойся, здешняя — хорошая. Можно сказать, эталонная."
    hide d_sf
    show d_us shy sport at fright:
        ypos -0.05
    with dspr
    d_u1 "Лучше меня? А как же я?"
    hide d_us
    show d_sf normal pioneer at fleft
    with dspr
    me "Кто мне в начале знакомства заявил, что «Я — не она!»? Ты — главная и любимая, и сравнению с тобой никто не подлежит."
    hide d_sf
    show us surp1 sport
    with dspr
    th "Ну разговаривайте же вы громче! Я же половину не слышу, половину не понимаю!"
    hide us
    show d_sf serious pioneer at fleft
    with dspr
    me "Ты знаешь, Рыжик, меня самого трясёт. Не от страха, а от узнавания."
    me "Всё-таки лагеря разные, хоть и очень похожие, и вот сейчас эти различия, эти детали… От понимания и узнавания этих деталей."
    me "Вон хоть та берёза, на которую ты показала. У нас её нет, а здесь есть. И когда Лене надоедает площадь, она забирается в изгиб её ствола и читает там."
    show d_sf sad pioneer with dspr
    me "И ещё много таких деталей, начиная с замка на хозяйственных воротах."
    hide d_sf
    show d_us hurt sport at fright:
        ypos -0.05
    with dspr
    d_u1 "Понятно."
    hide d_us
    show us surp1 sport
    with dspr
    th "Он и Лену знает. И про берёзу её. Нет, теперь я точно от них не отстану."
    hide us with dspr
    stop music fadeout 1
    stop sound_loop
    stop ambience
    
    scene ext_aidpost_day
    show us_in_bush
    with dissolve
    play ambience ambience_camp_center_day
    "Когда пришельцы вышли к медпункту, Виола уже запирала дверь, собираясь идти в столовую. Тут же рядом приплясывал и Толик, живущий в изоляторе."
    "Как выяснила Ульянка, Толик был чьим-то родственником: может, вожатой, может, кого из поварих, а может, самой Виолы."
    "Вот кто-то из них, пользуясь служебным положением, и привёз убогого в лагерь."
    "Вреда от него, впрочем, не было, а дразнить его было неинтересно, это Ульяна выяснила в первый же день — Толик жил в каком-то своём мире и на окружающих просто не реагировал."
    show d_sf normal pioneer at fright with moveinright
    me "Здравствуйте, Виолетта Церновна."
    show d_to moron pioneer at fleft with moveinleft
    d_t1 "Ы-ы-ы… Хи-хи-хи."
    show d_to moron pioneer at cleft with move
    "Толик повернул голову на звук, замычал, показывая правой рукой на пришельцев, а левую спрятав себе за спину, сделал шаг, и оказалось, что он стоит уже между пришельцами и Виолой."
    show d_to normal pioneer with pixellate
    $ renpy.pause (1)
    show d_to moron pioneer with pixellate
    "Воздух вокруг Толика вдруг странно замерцал, искажая его привычный облик. Кажется, даже его рост начал изменяться. Несколько секунд, и всё закончилось."
    "Он всё так же придурковато улыбался и пускал слюну, но Ульянка успела поймать мелькнувшее выражение глаз Толика, очень жёсткое и безжалостное, и что-то чёрное мелькнуло в его руке, мелькнуло и исчезло."
    "Виола же, бросив возиться с дверью, потянула из кармана халата какой-то прибор, тоже разворачиваясь лицом к гостям."
    me "Не придуривайся, Толяныч."
    "И похоже, слова парня подействовали. Если пришельцев тут и не ждали, то быстро оценили и сочли неопасными — да что там, своими их сочли."
    show d_to smile pioneer with dspr
    d_t1 "Home is the Voyager, home from the Voyage."
    show d_to moron pioneer at cright behind d_sf with move
    d_t1 "Забурел, забурел! Вот забурел!"
    me "Я рад тебя видеть, Толя! Зато ты не меняешься."
    
    scene ext_aidpost_day:
        linear 1.0 zoom 1.1 anchor (180, 45) 
    show us_in_bush:
        linear 1.0 zoom 1.1 anchor (180, 45)
    th "Ничего не понимаю, он же дурачок. Как?"
    
    scene ext_aidpost_day
    show us_in_bush
    show d_sf normal pioneer at fright
    show d_to moron pioneer at cright behind d_sf
    with dissolve
    hide d_to with moveoutleft
    "Виола же, справившись с карманом халата, достала оттуда непонятную металлическую коробочку, украшенную телефонным диском, и подкинула её в руке."
    show cs smile at left with moveinleft
    cs "Ещё раз «Церновну» услышу — запущу тебе в лоб вот этой штукой."
    "И, убирая уже «эту штуку» обратно в карман, обратила наконец внимание на девушку."
    show d_us shy sport at right with moveinright:
        ypos -0.05
    "Подняла бровь в своём стиле, быстро, но цепко оглядела с головы до ног, углядела кольцо на пальце, бросила взгляд на руку парня, подняла бровь ещё выше, кажется, захотела что-то сказать фирменное, но сказала только:"
    cs "Ульяна, я так понимаю? Нашлась?"
    me "Ульяна Ильинична Персунова."
   
    scene ext_aidpost_day:
        linear 1.0 zoom 1.1 anchor (180, 45) 
    show us_in_bush:
        linear 1.0 zoom 1.1 anchor (180, 45) 
    th "Значит, зовут нас одинаково."
    
    scene ext_aidpost_day
    show us_in_bush
    show cs normal at left
    show d_sf normal pioneer at fright
    show d_us shy sport at right:
        ypos -0.05
    with dissolve
    cs "Активировал… пионерку? Научился?"
    me "Разбудил, Виола. Это организмы активируют, а людей — будят. Только так и никак иначе."
    show d_to moron pioneer at fleft behind cs with moveinleft
    d_t1 "Съела? И Семён прав."
    show d_to normal pioneer with pixellate
    "И воздух вокруг Толика опять замерцал, искажая и изменяя его облик. Да таким изменённым и оставил."
    "И, кажется, с сегодняшнего дня Толика следовало называть Анатолий."
    hide d_to with moveoutleft
    show cs shy with dspr
    "А парню, похоже, удалось пробить защиту Виолы, потому что она, вернув бровь на место, только кивнула головой и скомандовала:"
    cs "Ну заходите, рады вас видеть… Персуновы."
    hide d_sf
    hide d_us
    with moveoutleft
    play sound sfx_dinner_jingle_speaker
    show cs normal with dspr
    "И, уже обращаясь к Ульянкиному кусту, добавила:"
    cs "Пионерка, предупреди, пожалуйста, на кухне, что мы задержимся, и попроси, пусть обед на четверых оставят."
    hide cs with moveoutleft
    play sound sfx_close_door_campus_1
    "И дверь в медпункт закрылась в бесполезной попытке отсечь Ульянку-младшую от тайн и приключений."
    stop ambience
    
###################
#Глава 2. Комиссия#
###################

label d_comission:
    $ save_name = u"Дубликат. Четвертая смена - Комиссия"
    $ day_time()
    scene black with dissolve
    show headline_text2 u"Комиссия" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day
    play music music_list["you_lost_me"]
    show us dontlike sport with moveinright
    th "И что? Я больше ничего не узнаю?"
    play sound sfx_dinner_jingle_speaker
    th "Обед. В столовую пора. Или остаться? Вдруг эта парочка как из лесу вышла, так в лес и уйдёт, пока я обедаю."
    th "Я быстро! Не уходите в лес, пожалуйста! А ещё лучше — без меня в лес не уходите, пожалуйста!"
    hide us with moveoutright
    stop ambience
    
    scene ext_dining_hall_near_day
    show us grin sport far at fright
    with dissolve
    play ambience ambience_camp_center_day
    th "Я балда! Виола же просила придержать ЧЕТЫРЕ порции — никуда эти гости от меня не денутся."
    stop ambience
    
    scene int_dining_hall_people_day
    show us normal sport close at left:
        ypos 0.05
    with dissolve
    play ambience ambience_dining_hall_full
    show dv normal pioneer at right with moveinright
    show dv normal pioneer close with dspr
    play sound dct_sfx_chair
    show dv normal pioneer close at right with move:
        ypos 0.2
    dv "Слышала, рыжая? Говорят, к Виоле какая-то комиссия приехала."
    us "От рыжей и слышу. Нам-то что с того, Алиса?"
    dv "А то, что Ольга, скорее всего, тоже сейчас в медпункт пойдёт, она же начальник над всеми здесь. Ей по шапке надают, если что."
    show dv grin pioneer close with dspr
    dv "Так что самое время, пока вожатка в медпункте, сходить и искупаться. Если Славя дежурит на пляже, то за территорией искупаться."
    $ renpy.pause (0.5)
    show dv smile pioneer close with dspr
    us "Только вот…"
    dv "Что?"
    us "Не похожи те двое на комиссию."
    stop music fadeout 2
    us "Где «Волга», на которой они приехали, или хотя бы автобус? Костюмов нет, портфелей нет. Одеты по-походному, рюкзак у парня и брезентовая сумка у девушки. Ну и молодые они слишком для комиссии."
    us "Вон, сама посмотри."
    show us normal sport close at fleft:
        ypos 0.05
    show dv smile pioneer close at cleft:
        ypos 0.2
    with move    
    show cs normal far at cright
    show d_sf smile pioneer at fright:
        zoom 0.8
    with moveinright
    show dv shocked pioneer close with dspr
    $ renpy.pause (1)
    hide cs
    hide d_sf
    with moveoutright
    show d_us normal sport at cright:
        zoom 0.8
    show d_to normal pioneer at fright:
        zoom 0.8 ypos 0.1
    with moveinright
    $ renpy.pause (1)
    hide d_us
    hide d_to
    with moveoutright
    dv "И где я его видела? И где я её видела?"
    dv "Видела же, а не могу вспомнить."
    show dv surprise pioneer close with dspr
    "Алиса же при виде гостей замерла. Долго смотрела на них, бормоча что-то себе под нос. А потом вышла, позабыв о планах."
    play sound dct_sfx_chair
    show dv surprise pioneer close with move:
        ypos 0
    show dv surprise pioneer with dspr
    hide dv with moveoutright
    "Виола что-то сказала вожатой, та покивала и разрешающе махнула рукой в сторону столов — садитесь."
    th "Алиса их видела?! Я теперь просто обязана выяснить, что это за люди, даже если придётся подглядывать и подслушивать."
    th "Кто у нас тут? Ага, Шурик. Ну, очкарик, прощайся с ватрушкой."
    play music music_list["eat_some_trouble"]
    hide us
    show d5_sh_us with hpunch
    $ renpy.pause (2)
    hide d5_sh_us
    show sh rage pioneer far at fleft
    show mt rage pioneer at right
    show us grin sport
    with dspr
    mt "Ульяна? Ну кто же ещё. Ты, я вижу, застоялась!"
    mt "Шурик — свободен! Сегодня Ульяна дежурит в столовой вместо тебя!"
    hide sh with dspr
    show mt angry pioneer
    show us upset sport
    with dspr
    mt "Некуда энергию девать — поработай."
    stop music fadeout 1
    hide us
    hide mt
    with dspr
    stop ambience
    
    scene ext_dining_hall_near_day
    show mt normal pioneer at right
    show us normal sport at left
    with dissolve
    play ambience ambience_camp_center_day
    us "Ольдмитриевна, а кто это?"
    "Вот что хорошо в вожатой, так это её принцип: «Наказан — прощён»."
    "Поэтому, когда Ульяна поймала её с вопросом на выходе из столовой, Ольга Дмитриевна не стала вредничать."
    mt "Это? Экологи районные, образцы собирают: почвы, воды, воздуха. Попросились остановиться у нас до завтра, а завтра дальше пойдут."
    mt "Виола их хорошо знает и поручилась, а раз так, то и я разрешила."
    show mt sad pioneer with dspr
    mt "Вот только придумать надо, где им ночевать."
    stop ambience
    
    scene int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty
    show us normal sport at fright with moveinright
    th "Экологи, значит."
    th "Образцы собирают, значит."
    th "То-то рюкзак почти пустой."
    show us normal sport at fleft with move
    th "Ничего, сейчас я до их столов доберусь и всё узнаю."
    show us normal sport at right with move
    th "О чём там Виола рассказывает? О чём-то интересном."
    "Виола говорила, обращаясь больше к Семёну."
    "Толик опять изображал дурачка, только веры ему теперь не было."
    "А гости внимательно слушали."
    show us surp2 sport at left with move
    show cs normal far at right with dspr
    cs "Не люблю домашних животных. Вроде бы и должна, а не люблю."
    cs "Но если ты притащил на объект собаку или кошку, да даже хомячка, нарушив все правила, то будь добр заботиться о нём."
    cs "Диким-то всё равно, дикие живут и плюют на наши циклы…"
    show cs smile far with dspr
    cs "…а эти, п-пушистики. Они же себя членами нашей стаи считают, такими же как мы; и то, что мы на двух ногах, а они на четырёх лапах — это такая мелочь с их точки зрения."
    cs "А управляющие центры здешние считывают сигнал из их мозга: «Я человек!» и начинают работать."
    cs "Посёлок-то — он экранированный был, но кошка — она же гуляет сама по себе."
    cs "Вышла за территорию и получила нейтринное кольцо в мозг, ещё раз вышла — и на тебе цикловую программу на это кольцо…" 
    show us normal sport far at right with move
    show cs normal at left with move
    "Грязные столы кончились, Ульянка сбегала за шваброй и начала елозить тряпкой по полу, оставаясь в пределах слышимости."
    cs "…тело выросло, начало резко изменяться на человеческое, и, что печально, проснулся разум."
    show cs shy glasses with dspr
    cs "А хозяева — мне неприятно ту историю вспоминать и стыдно за людей, но учёная степень совсем не мешает суевериям. Не доктора наук, а средневековые крестьяне какие-то."
    cs "Бедное животное — нет, тогда уже не животное — чудом спаслось от погони за «оборотнем»."
    cs "А ведь она их любила, своих бывших хозяев, и прибежала к ним за защитой, перепуганная. Наверное, и сейчас любит, я не знаю."
    cs "И вот тут кончилась драма и началась трагедия: это существо осознало себя и задало себе вечный вопрос: «Кто я?»…"
    hide cs with dspr
    show us normal sport close with dissolve
    th "Надо дальше пол мыть, а уходить не хочется — вдруг пропущу что-то важное."
    "Ульянка мало что понимала, но слушать было интересно. Она выпрямилась, делая вид, что устала, и тут перехватила взгляд своей старшей тёзки."
    th "Всё, сейчас выгонят, чтобы не подслушивала."
    "Это было бы обидно, если бы Ульяна-большая вдруг не поднялась с места, опираясь на плечо Семёна, и не подошла к младшей."
    play music music_list["went_fishing_caught_a_girl"]
    show us upset sport with dspr
    show d_us smile sport at left with moveinleft:
        ypos -0.05
    show us smile sport with dspr
    us_old "Давай помогу, сестрёнка. Пусть они без нас дальше умничают."
    stop ambience
    
    scene ext_dining_hall_near_day
    play ambience ambience_camp_center_day
    "Через двадцать минут обе Ульяны стояли на крыльце столовой и болтали, не забывая при этом таскать из кулька конфеты. Несмотря на разницу в возрасте, Ульяна-большая оказалась очень свойским и понятливым человеком."
    "Порой казалось, что она знала, о чём её спросят, раньше, чем собеседница формулировала вопрос; порой Ульяна-маленькая угадывала реплики гостьи. Только иногда гостья замирала, будто вспоминая что-то неприятное, и отвечала так, будто это неприятное в своих ответах обходила."
    show us smile sport at left
    show d_us smile sport at right:
        ypos -0.05
    with dissolve
    us "Тебе сколько лет?"
    us_old "Д… А знаешь, угадай сама."
    show us surp1 sport with dspr
    us "Эй, я бесплатно не угадываю. Что дашь, если угадаю?"
    us_old "Тогда, тогда ты возьмёшь конфету без очереди!"
    us "Ну… Девятнадцать!"
    us_old "Угадала! Тащи конфету!"
    show us grin sport with dspr
    us "Нет, конфету скучно. Тем более они и так мои. Можно я лучше ещё спрошу?"
    us "А ты замужем за Семёном? А вы правда комиссия? Или экологи?"
    show d_us normal sport with dspr
    us_old "Да, третий ци…, то есть уже месяц. И никакие мы не экологи и не комиссия, а просто путешествуем. Только вожатой не говори, а то расстроится."
    hide d_us with dspr
    show us normal sport close with dspr
    th "Замуж только дуры выходят, но свадебное путешествие правильное."
    show d_us smile sport at right:
        ypos -0.05
    show us normal sport at left
    with dspr
    us_old "Сюда завернули, чтобы Виоле письмо и посылку передать от общей знакомой."
    show d_us sad sport with dspr
    $ renpy.pause (1)
    show d_us normal sport with dspr
    "Тут гостья на мгновение помрачнела, а Ульянка сделала вид, что не заметила."
    us "А уйдёте когда?"
    us_old "Уйдём когда? Завтра, после обеда."
    show us sad sport with dspr
    us "У-у-у… жалко, что завтра."
    us_old "Самой жалко, но надо возвращаться."
    show us surp1 sport with dspr
    us "А откуда вы всё здесь знаете?"
    show d_us smile sport with dspr
    us_old "Ну я же не забыла, как сама пионеркой была и в таком же лагере отдыхала. А Семён здесь отдыхал, именно в этом лагере, тогда же и с Виолой познакомился."
    us "Подожди, а откуда он меня-то знает?"
    show d_us normal sport with dspr
    us_old "Откуда тебя знает? У самого спроси — просто угадал или справки наводил."
    show d_us smile sport with dspr
    us_old "Слушай, сестрёнка, а что мы просто так тут стоим? Покажи мне лагерь? А по дороге ещё поговорим."
    show us grin sport with dspr
    us "Покажу! Прямо сейчас. Только после этого мы пойдём купаться! Ты взрослая, с тобой меня за территорию отпустят."
    us_old "Сейчас, только Сёмку предупрежу."
    hide d_us with dissolve
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dspr
    show mt angry panama pioneer at left with moveinleft
    mt "Ульяна, ты куда собралась?"
    show us upset sport
    show d_us normal sport
    with dspr
    us "Я, Ольдмитревна, в столовой всё убрала, а сейчас гостье лагерь показываю."
    show mt grin panama pioneer with dspr
    mt "И, конечно, не бесплатно."
    show d_us hurt sport with dspr
    $ renpy.pause (1)
    show d_us normal sport with dspr
    "А Ульяна-большая, увидев вожатую, даже зажмурилась. Потом открыла глаза, и Ульяне-маленькой показалось, что та ответила, пересиливая себя."
    us_old "Конечно, не бесплатно, Ольга Дмитриевна. Но лагерь не пострадает, я надеюсь. Мы всего лишь искупаемся."
    show mt normal panama pioneer with dspr
    show us normal sport with dspr
    mt "Ладно, купайтесь. Вам уже говорили, что вы очень похожи?"
    show d_us smile sport with dspr
    us_old "Мы близнецы."
    "И близнецы отправились покорять лагерь."
    stop ambience
    
    scene ext_house_of_dv_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dissolve
    play ambience ambience_camp_center_day
    play music music_list["get_to_know_me_better"]
    us "Вот, это наш с Алисой домик."
    show d_us hurt sport at fright with dspr
    us "Сейчас я купальник возьму, и дальше пойдём."
    stop ambience
    
    scene ext_clubs_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dissolve
    play ambience ambience_camp_center_day
    play sound sfx_open_door_clubs
    us "А это клубы. Здесь живут два самых скучных и трудных человека в лагере. Вон один из них как раз выходит."
    show el normal pioneer far with dissolve
    stop music fadeout 2
    show d_us hurt sport at fright with dspr
    us "Эй, Сыроежка!"
    show d_us normal sport at fright with dspr
    show el upset pioneer far with dspr
    $ renpy.pause (0.5)
    hide el with dissolve
    play sound sfx_close_door_campus_1
    us "Я же говорю, они скучные. Ну, пойдём дальше."
    stop ambience
    
    scene ext_musclub_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dissolve
    play ambience ambience_camp_center_day
    play music music_list["so_good_to_be_careless"]
    show mi surprise pioneer at left with dissolve
    show d_us hurt sport at fright with dspr
    mi "Привет, Ульяночка, а кто это с тобой?"
    show d_us normal sport at fright with dspr
    us "Мику, это тоже Ульяна. Они с{w=0.5} мужем вдвоём путешествуют, сегодня переночуют у нас в лагере, а завтра дальше пойдут."
    mi "Как здорово путешествовать! Я тоже сюда из Японии приехала! Ульяночка, которая старшая, а ты случайно не играешь ни на каком инструменте?"
    us "Мику, Мику, нам некогда. Сестрёнка, идём дальше."
    show mi sad pioneer with dspr
    mi "Пока, Ульяночки."
    stop ambience
    
    scene ext_path2_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dissolve
    play ambience ambience_forest_day
    us "Нет, Мику — девочка хорошая, ты не подумай ничего, но сейчас мы бы застряли у неё. Сначала бы она рассказала, что у неё только мама японка, потом…"
    stop music fadeout 3
    us "Вот в этом домике она, кстати, и живёт вместе с Леной."
    stop ambience
    
    scene ext_house_of_un_day
    show d_us smile sport at fright:
        ypos -0.05
    show us smile sport at right
    with dissolve
    play ambience ambience_camp_center_day
    us "А Лена — ты, может, её видела в столовой? Ну, такая грустяша с четырьмя хвостиками? Она с тех пор, как приехала, какая-то печальная ходит."
    us_old "Дай угадаю. А ты всё хочешь её расшевелить, и ничего не получается."
    show us sad sport with dspr
    us "Ну да. Я хочу, чтобы она засмеялась, а она пугается."
    stop ambience
    
    scene ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day
    play music adaytoremember
    "Так и обходили лагерь по кругу, пока не добрались до медпункта."
    "А пока обходили, младшая замечала странности в поведении старшей, когда та, встречая кого-то, сначала улыбалась как старому знакомому, а потом разочарованно вздыхала, когда этот кто-то ведёт себя так, будто старшую в первый раз видит."
    "Или когда старшая, войдя в домик, погладила «Весёлого Роджера», как будто домой к себе вернулась после долгого отсутствия."
    "Вот и родилось у Ульяны-младшей решение."
    show us normal sport with pixellate
    th "Нет, что-то тут нечисто, ещё посмотрю и спрошу как есть."
    hide us with pixellate
    stop ambience
    
    scene int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day
    "В медпункте старшая достала из рюкзака купальник и потрогала бухту верёвки, висящую на рюкзаке."
    show d_us normal sport at center with dspr:
        ypos -0.05
    us_old "Сестрёнка, а ты куда меня вести хочешь?"
    hide d_us
    show us normal sport
    with dspr
    us "Ну, э…"
    hide us with dspr
    "Младшая задумчиво покосилась на Виолу, читавшую какую-то рукопись — наверное, то самое письмо, о котором рассказала гостья."
    show cs normal glasses with dspr
    cs "Я вас не слышу, близнецы."
    "Виола отреагировала, не отрываясь от чтения."
    cs "Вы, кажется, что-то про ужин говорили?"
    hide cs
    show us normal sport
    with dspr
    us "Я хочу через хозяйственные ворота выйти и мимо малинника к реке спуститься."
    hide us
    show d_us smile sport at center:
        ypos -0.05
    with dspr
    us_old "Понятно всё. Пойдём, я лучше тебе другое место покажу."
    show d_us normal sport with dspr:
        ypos -0.05
    us_old "Виола, мы на озеро — то, что ближе к Старому корпусу. Скажете Сёмке, чтоб не терял."
    hide d_us
    show cs glasses normal
    with dspr
    cs "Идите, не бойтесь. Твой Сёмка сейчас ностальгирует и до ужина ностальгировать будет. А после ужина приходи, лечить его будем."
    show cs glasses shy with dspr
    cs "И… Ульяны, я не хотела вас обидеть."
    stop music fadeout 1
    stop ambience
    
################
#Глава 3. Озеро#
################
   
label d_lake:
    $ save_name = u"Дубликат. Четвертая смена - Озеро"
    $ day_time()
    scene black with dissolve
    show headline_text2 u"Озеро" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    
    
    scene ext_square_day with blinds
    play ambience ambience_camp_center_day
    show d_us normal sport at center with dspr:
        ypos -0.05
    us_old "Алису с собой зовём?"
    hide d_us
    show us normal sport
    with dissolve
    us "Спрашиваешь! Вот только… Где она сейчас? Давай начнём с домика. Если там нет, то… Да, давай с домика."
    stop ambience
    
    scene ext_house_of_dv_day
    show us normal sport
    with dissolve
    play ambience ambience_camp_center_day
    play sound sfx_knocking_door_outside
    $ renpy.pause (2)
    us "Алиса!"
    stop sound
    stop ambience
    
    scene int_house_of_dv_day
    show us normal sport
    with dissolve
    play ambience ambience_int_cabin_day
    us "Нет, здесь её нет."
    show us surp2 sport with dspr
    us "Подожди. Я знаю, где она! Давай за домик."
    stop ambience
    
    scene d_ext_dv_hideout_day_7
    show dv sad pioneer at left
    with dissolve
    play ambience ambience_camp_center_day
    play sound dct_sfx_steps3
    play music music_list["i_want_to_play"]
    $ renpy.pause (0.5)
    stop sound
    show us smile sport at cright with moveinright
    $ renpy.pause (0.5)
    show dv surprise pioneer with dspr
    us "Рыжая. Хватит бездельничать! Бери купальник и идём с нами!"
    dv "А-а-а..?"
    us "Бэ-э-э… Или будешь здесь жариться и открытия пляжа ждать? Так дело твоё, два раза такие вещи не предлагают."
    dv "…"
    hide dv with moveoutleft
    show us smile sport at right with move
    show d_us normal sport at left with moveinright:
        ypos -0.05
    us "Да, познакомься: это тоже Ульяна. Моя сестра-близнец, между прочим."
    us "Ульяна, это Алиса. Сейчас она придёт в себя, дай ей две минуты."
    show us laugh sport with dspr
    us "Не каждый день близнецов встречаешь!"
    show us smile sport at cright with move
    show d_us smile sport at fright behind us with move:
        ypos -0.05
    show dv angry pioneer at cleft with moveinleft
    dv "Рыжая! Ты берега не попутала?"
    show us grin sport with dspr
    us "Сестрёнка, я же говорила, что она сейчас придёт в себя!"
    show dv rage pioneer with dspr
    dv "Кто-то очень любит подзатыльники!"
    us "Алиса, всё равно не догонишь! Лучше пойдём с нами купаться. За территорию, конечно."
    stop music fadeout 1
    stop ambience
    
    scene ext_path_day with dissolve:
        walking
    "Отказываться Алиса не стала, подзатыльник Ульянке пообещала дать позже, и через десять минут трое Рыжих уже шагали в сторону Старого лагеря."
    show d_us normal sport at left with dspr:
        ypos -0.05
    play ambience ambience_forest_day
    play sound_loop dct_sfx_steps2
    us_old "Нам прямо по тропинке, а потом направо."
    hide d_us with moveoutright
    stop sound_loop
    stop ambience
        
    scene ext_path2_day with slideleft:
        walking
    show dv normal pioneer2 with moveinleft
    play ambience ambience_forest_day
    play sound_loop dct_sfx_steps2
    play music music_list["went_fishing_caught_a_girl"]
    dv "Далеко идём?"
    hide dv with moveoutleft
    show d_us normal sport at center with moveinright:
        ypos -0.05
    us_old "Половину дороги прошли."
    show d_us smile sport at center:
        ypos -0.05
    us_old "Устала?"
    hide d_us with moveoutright
    show dv normal pioneer2 with moveinleft
    dv "П-ф-ф."
    hide dv with moveoutleft
    show us grin sport with moveinleft
    us "Устала, устала. Сейчас назад запросится."
    hide us with moveoutleft
    show dv smile pioneer2 with moveinright
    dv "Ой, Рыжая! Допросишься!"
    stop music fadeout 1
    stop sound_loop
    stop ambience
    
    scene dct_ext_old_building_day with slideleft
    show d_us normal sport at center with dspr:
        ypos -0.05
    play ambience ambience_old_camp_outside
    us_old "Ну вот, почти пришли. Пятьсот метров ещё, и мы на месте."
    show d_us smile sport with moveoutleft
    us_old "Нам направо. Следов не оставлять, фантики не бросать, траву не топтать, ветки не ломать."
    hide d_us with dspr
    show us normal sport with moveinright
    th "Вот, кстати, о старом лагере. Столько легенд и страшилок, о той же Чёрной вожатой, например, а так туда и не выбрались до сих пор. Всё другие занятия находятся."
    us "А может, завернём в Старый лагерь?"
    hide us with moveoutright
    show d_us normal sport at center with moveinleft:
        ypos -0.05
    us_old "В лагерь, говоришь… {w}Самой интересно, но мы вроде как на озеро шли. На обратном пути если, и ненадолго. Алиса, ты как?"
    hide d_us with moveoutright
    show dv normal pioneer2 with moveinleft
    dv "Замётано."
    hide dv with moveoutleft
    show d_us normal sport at center with moveinright:
        ypos -0.05
    us_old "Только имейте в виду: ничего там нет. Одна, как говорит мой Сёмка, мерзость запустения."
    hide d_us with moveoutright
    "И, петляя между деревьями, троица пошла одной только Ульяне-большой известной дорожкой."
    stop ambience
    
    scene dct_ext_lake_day with dissolve
    play ambience ambience_forest_day
    play music music_list["raindrops"] fadein 2
    "Озеро Ульянке понравилось."
    "Прямо посреди леса расположилось круглое блюдце чистой воды."
    "Небольшое — можно обойти по берегу за пять минут, со всех сторон окружённое лесом, и только со стороны, обращённой к далёкому «Совёнку», есть полянка, отгороженная от воды кустарником."
    "Там же, со стороны поляны, и удобный выход к воде по тропинке через кусты."
    "На поляну кто-то, ещё неизвестно в какие времена, притащил три бревна и положил их треугольником, в центре которого угадывалось давнее кострище."
    show us surp1 swim with moveinbottom
    us "Какое хорошее место. Спасибо, что показала."
    hide us with moveoutbottom
    show dv smile swim at right with moveinbottom
    dv "Точно, спасибо, Ульяна. А главное — от нашего домика добираться легко. Не надо через центр лагеря идти."
    hide dv with moveoutbottom
    show d_us smile swim at left with moveinbottom:
        ypos -0.05
    us_old "Пожалуйста. Сёмке нравится, что об этом озере почти никто не знает и тихо здесь. Ну и мне, как ему. Так что и вы не пакостите."
    "Да, на озере было тихо, не считая того момента, когда кто-то ломанулся от девушек через кусты. Или зверь средних размеров, или крупная птица."
    show d_us normal swim with dspr
    us_old "Может, барсука спугнули? Барсуки тут точно есть, Сёмка видел."
    hide d_us with moveoutbottom
    show dv normal swim at right with moveinbottom
    dv "А ты где со своим Семёном познакомилась?"
    hide dv with moveoutbottom
    show d_us hurt swim at left with moveinbottom:
        ypos -0.05
    us_old "Да в лагере же. Я ещё пионеркой была, а он на практику приехал физруком, после техникума."
    hide d_us with moveoutbottom
    show us normal swim with moveinbottom
    th "Простой вопрос, а сестрёнка опять погрустнела. Что-то не то."
    hide us with moveoutbottom
    stop music fadeout 1
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    play ambience dct_ambience_creaking_floor
    "Старый лагерь, куда завернули на обратном пути, разочаровал."
    show us dontlike sport at left with moveinleft
    th "Я думала, что тут интересно. Тайна какая-то. Что-то страшное."
    th "А тут только пыль, скрипучая лестница на чердак, обрывки газет и книги без переплётов."
    show us sad sport with dspr
    show d_us normal sport at right with moveinright:
        ypos -0.05
    us_old "Не понравилось? А я предупреждала."
    "И Ульяна-большая опять погрустнела."
    show d_us hurt sport with dspr
    us_old "Сюда нужно ночью идти в первый раз — тогда страшно. А сейчас просто грустно немножечко."
    us "Ты чего, Ульян? Весь день куксишься."
    us_old "Нормально всё, сестрёнка. Я просто поняла, как же далеко я от вас уже ушла."
    show d_us smile sport with dspr
    us_old "Не обращайте внимания. Что-то я сейчас рассуждаю как тридцатилетняя тётка, а мне ещё рано в неё превращаться, я ещё маленькая."
    us_old "А ну, побежали до лагеря!"
    hide d_us
    hide us
    with easeoutright
    $ renpy.sound.set_volume(0.1)
    play sound sfx_dinner_jingle_normal
    "И еле слышимый на таком расстоянии сигнал горна подтвердил, что да — если девочки не хотят остаться голодными, то надо бежать."
    stop sound
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ renpy.sound.set_volume(1)
    play ambience ambience_old_camp_outside
    "Рыжие, хохоча, ссыпались с крыльца и, где шагом, а где действительно бегом, не оглядываясь, заспешили на ужин."
    "Некоторое время ещё мелькали их спины: две в красных футболках и одна в пионерской рубашке, а потом деревья заслонили девушек окончательно."
    stop ambience
    
    scene ext_houses_day with dissolve
    play ambience ambience_camp_center_day
    play music music_list["timid_girl"]
    show d_sf smile pioneer at center with dspr
    me "Ну слава богу. А то я просто разрывался: то ли идти в столовую и ужин на вас бронировать, то ли идти к озеру и вас посиневших из воды вытаскивать."
    show d_sf smile pioneer at left with move
    show d_us smile sport at right with moveinright:
        ypos -0.05
    us_old "Сёмк, напомни мне, пожалуйста. Я уже говорила тебе, что ты зануда?"
    show d_sf laugh pioneer at cleft with move
    show d_us smile sport at cright with move:
        ypos -0.05
    show d_sf smile pioneer with dspr
    me "Рыжик, знаешь поговорку: «Бачили очі, що купували…»?"
    show d_us laugh sport with dspr
    us_old "Ах ты…"
    show d_us smile sport with dspr
    me "Что? Говорила тебе мама?"
    hide d_sf
    hide d_us
    with dspr
    show us normal sport with dspr
    th "Нет, всё хорошо. Улыбаются и за руки держатся. А я испугалась сначала, что они поссорились."
    th "Интересно, как они ведут себя, когда нужно что-то сделать вдвоём? Вот хотя бы в путешествии этом."
    hide us with dspr
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day
    "Перед столовой шуточная перепалка между гостями закончилась, и Семён поведал новость:"
    show d_sf normal pioneer at left
    show d_us normal sport at right:
        ypos -0.05
    with dspr
    me "Знаешь, куда нас поселили? В спортзал."
    us_old "Баба Глаша сказала бы про сходящиеся линии и устойчивые вероятностные потенциалы."
    show d_us sad sport with dspr
    us_old "Надо бы порядок там навести."
    me "Уже нет, я там последний час со Славей столы и маты двигал и пыль протирал."
    us_old "Мог бы и со мной."
    me "Что ты в этом спортзале не видела? А так хоть лагерь посмотрела и сама экскурсию провела."
    stop ambience
    
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    "Вся четвёрка разделилась уже в столовой: Ульяна-младшая и Алиса пошли к своему отряду, а гости — за стол администрации. Ульянка ещё услышала, как Виола произнесла, обращаясь к Семёну:"
    show d_sf normal pioneer at left:
        zoom 0.8
    show cs normal glasses far at right
    with dspr
    cs "После ужина ко мне. Не забыл?"
    stop ambience
    
    scene d_ext_dv_hideout_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play music music_list["farewell_to_the_past_edit"]
    show dv normal pioneer at left
    show us normal pioneer at right
    with dspr
    dv "Ну и как тебе гости, Уля?"
    us "Странные какие-то. Но вообще очень понравились. С Семёном не общалась почти, а с Ульяной как будто сама с собой разговариваю. Она ещё пошутила, что мы близнецы. А что такое?"
    show dv sad pioneer with dspr
    dv "Как бы объяснить. Ты заметила, что они как будто что-то недоговаривают, как будто сами себя одёргивают, чтобы лишнего не сболтнуть?"
    show dv normal pioneer with dspr
    dv "Нет-нет, мне они тоже понравились, но вот ещё: не знаю как ты, а я всё время пытаюсь понять, где я этого Семёна могла видеть?"
    show dv guilty pioneer with dspr
    dv "Ясно, что не в лагере, если он на восемь лет меня старше, а где тогда?"
    show dv normal pioneer with dspr
    show us surp2 pioneer with dspr
    us "И Лену он знает, и про берёзу её. Я днём шла за ними к медпункту и подслушала."
    us "А та Ульяна — ты заметила, что она иногда вздрагивает, как будто какую-то грустную вещь вспоминает? Или смотрит на пионеров здесь, как на старых знакомых. А потом огорчается, что это не тот человек."
    show us normal pioneer with dspr
    us "А ещё, ты знала, что Толик не дурачок на самом деле?"
    stop music fadeout 3
    "Ужин давно закончился, Рыжие сидели в кустах за своим домиком и перебирали странности сегодняшних гостей, когда к ним присоединилась Ульяна-большая."
    show d_us normal sport at center with dspr:
        ypos -0.05
    us_old "Девочки, можно с вами?"
    show d_us sad sport with dspr
    us_old "А то Виола сейчас в спину Сёмке вот такие здоровенные иглы навтыкала вдоль всего позвоночника."
    us_old "И ещё меня смотреть заставляла, говорит, что завтра вечером я буду иглы втыкать, а она только командовать."
    us_old "А сейчас Сёмка спит, а мне с Виолой и Анатолием не по себе. Не запираться же в спортзале."
    show d_us hurt sport with dspr
    us_old "Никогда не думала, что я такая чувствительная. Кнопку на стул подложить — легко, паука в руки взять — вообще как котёнка погладить, кого другого булавкой тыкать — пожалуйста, но Сёмку, оказывается, жалко."
    show us surp2 pioneer with dspr
    us "Завтра? Вы же уходите завтра, разве нет?"
    show d_us normal sport with dspr
    us_old "Анатолий Сёмкину спину помассировал чуть-чуть. Потом Виола Сёмку посмотрела и сказала, что раньше воскресения никуда не отпустит, что прочие коновалы — они только и могут, что таблетки пополам ломать. Так что три сеанса ещё."
    show us normal pioneer with dspr
    us_old "А ещё Виола меня научить хочет, чтобы я с Сёмкиной спиной сама справлялась. Добро пожаловать, говорит, в семейную жизнь."
    "Рыжие туземки помолчали сочувственно, а Ульяна-большая, успокоившись уже, добавила:"
    us_old "Спасибо вам. Выговорилась, так легче стало. Если надо учиться — буду учиться."
    show d_us smile sport with dspr
    "А потом посмотрела на Ульяну-младшую, на Алису, которые всё порывались открыть рот и спросить, например, о странностях в поведении некоторых гостей лагеря, улыбнулась своим мыслям и предложила сама:"
    show us normal pioneer with dspr
    us_old "Спрашивайте. Сёмка ворчать будет, может, и Виола ругаться будет, но спрашивайте."
    show dv guilty pioneer with dspr
    "И вышло так, что Ульяна с Алисой не смогли озвучить всю ту кучу вопросов, что накопилась за эти полдня в их головах, просто язык не повернулся."
    show us dontlike pioneer with dspr
    "Ульяна даже отвернулась от досады, чтобы не смотреть на гостью."
    "А Ульяна-большая ещё раз глянула на девушек, вздохнула, поднялась на ноги и, прощаясь, сказала больше самой себе:"
    show d_us sad sport with dspr
    us_old "Вот, значит, как оно бывает, а я не верила."
    us_old "Ну как только сможете спросить — спрашивайте, три дня сроку у вас есть."
    us_old "Я и Сёмка — мы точно на ваши вопросы ответим; Сёмка, правда, ворчать будет, но врать и уклоняться не станет."
    show d_us normal sport with dspr
    us_old "И приходите в спортзал через два часа, чай пить."
    hide d_us with dspr
    "И ушла вызволять Сёму из лап медицины."
    stop ambience

    scene dct_int_aidpost_sunset with dissolve
    play ambience ambience_medstation_inside_day
    play music music_list["silhouette_in_sunset"]
    "А у Виолы — у той тоже знаменательный день был: в кои-то веки ей в руки больной попался, да ещё и собеседник."
    show cs normal glasses at left with moveinleft
    cs "Мы же тут такие, какими себя ощущаем. Пионеры — те по программе живут, вожатые — по своей программе, а мы, получается, по своей."
    show d_sf normal pioneer at right with moveinright
    cs "Ты вон взял и повзрослел с семнадцати до двадцати пяти, и Ульяна твоя до девятнадцати, и так и застряли. Или неполные \"воспоминания о будущем\" твои, и глаз мой карий, кстати. Пометили меня, а зачем? Я не знаю."
    "{i}Семён, Виола и Анатолий сидели в медпункте, тут же на столе стояла литровая химическая склянка коричневого стекла и три маленьких, на пятьдесят миллилитров, лабораторных стакана.{/i}"
    me "А баба Глаша?"
    show cs normal glasses with dspr
    cs "Надо обладать личностью Глафиры Денисовны, чтобы наплевать на программу и жить собственной жизнью — это во-первых; и быть рождённой мамой с папой — это во-вторых."
    me "А Толя — он что, ощущает себя идиотом? Прости, Толя."
    cs "С Толей сложнее: он ещё и на систему частично завязан, вот ему и навязывается эта роль, когда он не сопротивляется; и если вокруг посторонние — маскировка."
    show cs smile glasses with dspr
    cs "Он сам выбрал, но, Толь, мне надоело с олигофреном жить, слышишь?"
    me "Маскировка? А, я понял."
    hide cs with moveoutleft
    show d_to smile pioneer at left with moveinleft
    d_to "Да, Сём. Я охраняю второй проход в Шлюз и по совместительству вот эту разноглазую особу. Думаешь, это первая попытка была, с твоим двойником? Так что не засиживайся тут. Узел номер один — твой. И сидеть тебе там все вторые половины циклов."
    play sound sfx_open_dooor_campus_1
    $ renpy.pause (1)
    "Вошла Ульяна."
    show d_us normal sport at cright with moveinright:
        ypos -0.05
    us_old "Виола, я у вас Сёмку забираю."
    hide d_to with moveoutleft
    show cs normal glasses at left with moveinleft
    cs "Забирай."
    cs "Семён, тяжести не поднимать пока, и вообще не нагружаться, а если поднимать, то беречься. Но лучше не поднимать."
    cs "Следи за ним, Ульяна. И завтра после ужина жду обоих… на сеанс."
    show cs smile glasses with dspr
    hide d_us
    hide d_sf
    with moveoutright
    "Почему-то теперь, после того, как удалось вытащить из Виолы человека, она перестала пугать."
    stop music fadeout 1
    stop ambience
    
####################
#Глава 4. Персуновы#
####################
   
label d_persunovs:
    $ save_name = u"Дубликат. Четвертая смена - Персуновы"
    $ sunset_time()
    scene black with dissolve
    show headline_text2 u"Персуновы" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_ext_playground_sunset with blinds
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play sound_loop dct_sfx_steps2
    show d_us normal sport at cleft with moveinleft:
        ypos -0.05
    us_old "Сём, как спина?"
    show d_sf normal pioneer at fleft behind d_us with moveinleft
    me "После Виолиных-то иголок? Как кисель, Рыжик. Так что зря мне Виола нагрузки ограничила, я и сам близко сейчас ни к чему тяжёлому не подойду."
    "Гости неспешно шли по тропинке от медпункта к спортзалу и делились впечатлениями о прошедшем дне."
    show d_us smile sport with dspr
    us_old "Я за купальником заходила когда, Виола сказала, что ты ностальгировать ушёл."
    show d_sf smile pioneer with dspr
    me "Ага. Сходил на пристань, к кибернетикам зашёл, к Мику в кружок, на площади с Леной посидел, парой слов перекинулся, насколько это возможно с нераскрывшейся Леной."
    me "Даже с местной мелюзгой на спортплощадке мячик попинал и пожалел себя за то, что я на эту мелочь пузатую раньше внимания не обращал. Но, правда, тогда я тебя бы не встретил."
    show d_sf normal pioneer with dspr
    me "А потом меня Славя выловила, и мы в тренерской мебель переставляли. Вас я видел, но не стал догонять."
    show d_us normal sport with dspr
    us_old "А я девочек к нам вечером на чай пригласила."
    me "Молодец. И я даже не спрашиваю, кого."
    me "Знаешь, Уля, с вами, Рыжими, у меня почему-то всегда были хорошие отношения. Во всех узлах. И вот я вернулся в родной лагерь, с которого у меня всё начиналось. И не пионер, а вроде как один из… Один из не знаю кого — из местного начальства, что ли, явного и тайного; но вот оказалось, что девочки мне ближе, мне с ними легче, чем с вожатой, с Виолой, с Толиком."
    stop sound_loop
    stop ambience
    
    scene dct_int_coaching_room2 with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_evening
    "Ульяна долго молчала, не решаясь спросить, а Семён терпеливо ждал. И только в спортзале разговор возобновился."
    show d_us normal sport at right:
        ypos -0.05
    show d_sf normal pioneer at left
    with dspr
    us_old "Сёмк, ты только не обижайся, пожалуйста."
    show d_sf serious pioneer with dspr
    me "Что случилось, Рыжик?"
    us_old "Вот ты здесь сто циклов прожил, так?"
    me "Ну плюс-минус, конечно, но так."
    us_old "И девочки здесь очень хорошие, я сегодня сама убедилась. Скажи…"
    show d_us shy sport with dspr
    us_old "Скажи, у тебя что-то серьёзное для тебя с ними было? Чтобы вот сердце болело. Или наоборот, улетало на небо от счастья?"
    play music music_list["a_promise_from_distant_days"]
    show d_us sad sport with dspr
    me "Уля. Я очень хочу, чтобы было. Но я не помню — вот в чём беда."
    me "Я знаю, что было, я уверен, что было, но то, что я помню — это или как чёрно-белые фотографии в чужом альбоме, или же сухие факты, как в протоколе, или сон, где всё перемешано и невозможно его толком описать."
    me "А что чувствовал в те моменты — не могу сказать вовсе; так, иногда, как проблеск проскакивает."
    me "Вот Алиса сидит на пристани, свесив ноги в воду, а я замираю от неожиданной нежности к этой хамке."
    me "А вот мы с Леной стоим, прислонившись спинами к одной и той же берёзе, и разговариваем, и мне больно от того, что я не могу до неё докричаться."
    me "Вот здешняя Ульяна с глазами по пять рублей слушает мою страшную историю, а я удивляюсь произведённому эффекту."
    me "Алиса, Лена, Славя, Мику…"
    me "Нет, Мику не здесь, не в этом лагере, или здесь? Я не помню, не могу вспомнить, от Мику даже картинки не осталось, только ощущение её руки и знание, что если держать Мику за руку и смотреть ей в глаза, то она успокаивается и перестаёт трещать как пулемёт; и помню, как мы купались на острове."
    me "Ульянка? Нет. Хотя дружили крепко, и на выручку мне она всегда бросалась не задумываясь: это, наверное, у вас, у всех Ульянок, в крови."
    me "Но это ещё до моего пробуждения. Зря ты об этом спросила, Рыжик. Я уже почти смирился со своим беспамятством, а теперь опять буду себе мозги наизнанку выворачивать, пытаясь вспомнить хоть что-то, хоть на один бит памяти, но стать богаче."
    me "Ну а про те циклы, которые я уже помню — ты про них всё знаешь, повторяться не буду."
    show d_us normal sport with dspr:
    us_old "Да, знаю, Сём. Я почему спросила. Помнишь, ты днём про здешнюю Лену сказал, а перед ужином ещё про Славю?"
    us_old "Я ревновать пыталась, честно. Не получилось. А сейчас, когда познакомилась с девочками здешними, и вовсе не получится."
    us_old "Потому что если бы не эти девочки, ты бы не стал таким, какой ты есть, какого я люблю, понимаешь?"
    us_old "Ты сам не замечаешь, а в тебе есть какие-то черты от всех девочек — те, которыми они поделились с тобой, это надо просто увидеть."
    us_old "Ты, конечно, пропустил всё, что тебе подарили, через свою личность и всё изменил под себя, но они, эти черты, есть и никуда не делись, и я их вдруг увидела — что-то от Алисы, от Лены, от Мику, понимаешь?"
    us_old "От тех девочек, которые ещё не проснулись. Я не знаю Славю, но то, что я в ней успела заметить, есть и в тебе."
    us_old "Сёмка, они сделали тебя, а ты сделал нас, понимаешь?"
    us_old "И если ты меня не поймёшь сейчас, то кто тогда?"
    me "Рыжик, думаю, мы все здесь делаем друг друга. И раньше делали, и продолжаем делать, и ты продолжаешь — вот прямо сейчас."
    show d_sf smile pioneer with dspr
    me "Но о Славе — я что, тоже люблю подметать площадь?"
    show d_us laugh sport with dspr
    us_old "Ты этого терпеть не можешь! Но ты ни разу не прошёл мимо нашей Алисы, когда она вспоминает о своих обязанностях, чтобы ей не помочь."
    show d_sf serious pioneer
    show d_us normal sport
    with dspr
    us_old "И порядок в спортзале: тебе неохота его поддерживать, но ты всегда за ним следишь. И октябрята: тебе же нравится с ними возиться, вот даже сегодня. Так что живи пока, Сёмк. Не буду я тебе сколопендру в постель подбрасывать, тем более это и моя постель тоже."
    show blink
    "Ульяна прижалась к Сёмке, спрятав лицо на его груди."
    us_old "Сёмка, я совсем не ревнивая и совсем не дура, да?"
    us_old "Я всё боялась, что за те пять циклов, за десять недель после твоего возвращения повзрослела физически на пять лет, а сама осталась той же четырнадцатилетней дурочкой, понимаешь?"
    "А Сёмка только прижимал Ульяну к себе, целовал в макушку и глупо улыбался."
    me "Рыжик мой, всё хорошо. Ты такая, какая есть, и именно такая, какая мне нужна. А когда ты меняешься, то становишься нужна такая, какая становишься."
    me "Думаешь, я не понял, почему ты вдруг разбираться в себе, во мне, в наших отношениях захотела? Ты сейчас боишься, что забудешь меня в следующий раз, в следующую активную фазу, или что не нужна мне окажешься, как уснёшь."
    me "Вот и пытаешься всё понять и всё запомнить, чтобы хоть что-то осталось. А ты не бойся: ты, когда опять проснёшься, всё вспомнишь. А если не вспомнишь, то я тебе напомню, обещаю. И пока ты спишь, тоже напоминать буду, каждый день, в каждом цикле."
    me "Только не вздумай впасть в детство и вернуться в свои четырнадцать лет. Иначе мне придётся опять ждать, пока ты не подрастёшь. Не хочу, одного раза мне хватило."
    hide blink
    show unblink
    show d_us laugh sport with dspr
    us_old "Да, а кто тебе спину лечить будет, пока я сплю? Будешь сюда к Виолке этой бегать, знаю тебя, ходока налево. Карий глаз ещё от неё подцепишь. Придётся, наверное, мне в активной фазе оставаться."
    show d_sf laugh pioneer with dspr
    me "Ну конечно, только я предвкушать свободу начал, как вот он, облом."
    "И эта шутливая разрядка после момента откровения продолжалась бы ещё, если бы дверь в тренерскую не открылась и в комнату не заглянули."
    stop music fadeout 1
    stop ambience
    
    scene d_ext_dv_hideout_sunset with dissolve
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    "Алиса долго сомневалась, откликаться или нет на приглашение Ульяны-большой. Если бы компания ограничилась только двумя Ульянами, то пошла бы не задумываясь: Ульяна-большая ей нравилась, даже несмотря на недавний неловкий момент, но Семён был личностью непонятной."
    show dv guilty pioneer at left with dspr
    dv "Уля, ты пойдёшь?"
    show us grin pioneer at right with dspr
    us "А то, Алиска. Где ещё чаем напоят? А может и чего интересного расскажут. А ты что, Семёна Ульяниного стесняешься?"
    show dv angry pioneer with dspr
    dv "Я?!"
    show dv shy pioneer with dspr
    dv "Да, есть немного. Сегодня, когда вечером встретились на площади, он так улыбнулся — как старой знакомой. И потом, пока к столовой шли, всё поглядывал на нас. Поглядит — улыбнётся, поглядит — улыбнётся, как будто убеждался, что всё у нас хорошо. Или вот это вот чувство, что мы обе его знаем."
    dv "А как на него другие смотрят, ты видела? У других тот же вопрос на физиономиях: «Где мы его видели?» — даже у вожатой. Хотя Ольга здесь же в детстве отдыхала и должна его знать, раз они ровесники."
    show us smile pioneer with dspr
    us "Вот и спросишь его сама. Ну, пойдёшь?"
    stop ambience
    
    scene dct_ext_playground_sunset
    show dv shy pioneer at fleft
    with dissolve
    play ambience ambience_camp_center_evening
    play sound_loop dct_sfx_steps2
    "Пошла, конечно. И люди интересные, и чтобы самой себе, Семёну и Ульяне-большой доказать, что никого не стесняется."
    th "Какой же вопрос гостям задать и не опозориться, как два часа назад с Ульяной?"
    "Ведь хотелось же спросить о многом, и Ульяна-большая разрешила, и даже сама попросила задавать вопросы — как будто стыдно стало спрашивать, и язык не повернулся."
    th "Обязательно надо что-то спросить."
    th "Ульянка эта ещё. Сказала, что переоденется и догонит, но не догнала. Придётся самой. Стра-а-ашно"
    stop sound_loop
    stop ambience
    
    scene dct_int_coaching_room2
    show d_sf smile pioneer at fright
    show d_us smile sport at cright:
        ypos -0.05
    with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_evening
    play sound sfx_knock_door2
    $ renpy.pause (0.5)
    show dv normal pioneer at fleft with moveinleft
    dv "Здравствуйте."
    me "Заходи, Алиса. Ты одна?"
    play sound sfx_open_door_strong
    $ renpy.pause (0.5)
    show dv normal pioneer at left
    show us smile sport at fleft
    with hpunch
    us "Нет, она не одна!"
    "Ульянка, всё-таки догнавшая Алису, протиснулась мимо неё в тренерскую и по-хозяйски огляделась."
    show us smile sport at center with move
    us "А здесь неплохо. Надо будет у вожатой ключ свистнуть. Или, может, попроситься в физруки? Женька в библиотеке, Мику у себя, а я здесь буду."
    "Почему-то гости лагеря переглянулись при этих словах, Ульяна-большая непонятно хмыкнула, а Семён тихо пробурчал что-то — кажется, опять про сходимость."
    show d_us normal sport with dissolve
    us_old "Девочки, чтобы не было вопросов, почему мы вас пригласили — нипочему."
    show d_sf serious pioneer with dspr
    us_old "Сёмка молчит, но ему было важно убедиться, что всё здесь в порядке. И не морщись, Сём, так оно и есть, сам же меня врать отучил."
    us_old "Поэтому я пока приготовлю чай, а Сёмка вам сейчас сказку расскажет. Или нет, лучше наоборот — я расскажу. У него сказки красивые получаются, он очень умный и умеет их сочинять и рассказывать, он вообще умнее нас всех, может быть, кроме Виолы и Шурика, но расскажу сказку я."
    hide d_sf with moveoutright
    us_old "Сёмка, не дёргайся, так надо."
    stop ambience

#################
#Глава 5. Сказка#
#################
   
label mediocris_fabula:
    $ save_name = u"Дубликат. Четвертая смена -\nСказка"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Сказка, рассказанная Ульяной-большой" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    
    
    scene dct_int_coaching_room2 with blinds
    $ sunset_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_evening
    show dv normal pioneer at left
    show us normal sport at cleft
    with dspr
    show d_us normal sport at right with dissolve:
        ypos -0.05
    us_old "Давным-давно…"
    show d_sf smile pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "В далёкой-далёкой галактике."
    hide d_sf with dspr
    us_old "Нет, Сёмка, не там."
    play music music_list["trapped_in_dreams"] fadein 1
    us_old "В некотором царстве, в некотором государстве стоял пионерский лагерь. И вот однажды приехал туда пионер. До конца смены оставалась всего неделя, а он взял и приехал, только что он, глупый, за эту неделю успеет?"
    show us dontlike sport with dspr
    us_old "Сестрёнка, не морщись, это история не про чёрного пионера, а наоборот."
    show us surp1 sport with dspr
    us "А откуда ты…"
    us_old "Откуда я про чёрного знаю? Так все про него сочиняют, не ты одна."
    show us normal sport with dspr
    us_old "Что он там делал эту неделю — никто не вспомнит, наверное: ни другие пионеры, ни он сам, ни вожатая; может, только кто-то из персонала, если захочет, но ведь давно же это было."
    us_old "А на следующую смену опять приехал, и тоже с опозданием, и на следующую, и на следующую…"
    show dv smile pioneer with dspr
    dv "Это сколько же лет этому пионеру было? Раз он так ездил и ездил."
    us_old "Что значит — сколько лет пионеру было? Не важно, это же сказка; Алиса, ты просто слушай. Про Питера Пена читала? Я знаю, что читала. Ну вот, а сейчас про пионера слушай."
    show dv surprise pioneer with dspr
    us_old "Семнадцать ему было, каждую смену. И другим пионерам тоже, а кому и меньше. Кое-кому и четырнадцать в сентябре исполнялось."
    show dv normal pioneer with dspr
    us_old "И так каждую смену, и всегда семнадцать лет — сказка же. Да, остальные пионеры тоже одни и те же приезжали, только не опаздывали к началу смены, и никто из них никогда прошлые приезды не помнил."
    us_old "Так, иногда, может, подумает кто: «Что-то мне эта девочка или этот мальчик знакомым кажется, где я его видел?». Помотает головой, пожмёт плечами и забудет эту свою мысль."
    show d_sf smile pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "Уля, ты не…"
    hide d_sf with dspr
    us_old "Сёмка, не мешайся, и вообще, не путайся под ногами — это моя сказка, а не твоя. Ты ту свою, которую на острове начал рассказывать, так и не закончил, а ведь Гришка всё ещё ждёт продолжения. Хорошо, что он маленький, и для него всё в одно бесконечное лето сливается, а то давно бы плюнул и ждать перестал."
    us_old "Ну и отличался наш пионер от остальных-прочих, а чем — потом расскажу."
    us_old "Много с ним всякого за эту неделю происходило, но всегда, в каждый его заезд, всё как будто повторялось. Начинал с того, что как положено с обходным бегал, с пионерами знакомился: с кем-то так, привет-привет, пока-пока, с кем-то ближе, с кем-то совсем близко."
    us_old "И каждый раз думал, что вот смена закончится — он друзей-то не потеряет. А смена заканчивалась, он домой приезжал, и оказывалось, что всё это сон, и что пионеру тому на самом деле двадцать семь лет, семьи у него нет, любимой девушки нет, друзей нет, любимой работы нет, интересов никаких нет — просто одна тоска безрадостная."
    us_old "День проходил, а вечером он засыпал, и опять ему снилось, что он пионер, опоздавший к началу смены."
    us_old "Так много смен прошло, а пионер тот…"
    dv "Ульяна, как его хоть звали, пионера твоего?"
    us_old "Как звали? Неважно, пусть будет Степан."
    us_old "Так вот…"
    $ set_mode_nvl ()
    hide dv
    hide us
    hide d_us
    with dissolve
    "{i}Так вот, Степан те свои сны утром забывал и днём жил обычной жизнью; а во сне сначала помнил, что хоть он и пионер, но ему на самом деле двадцать семь, и зима у него в городе, и Новый год скоро; а потом почти забывал, что это сон, верил, что всё, что в лагере, на самом деле с ним происходит, а сон — это та его взрослая жизнь.\nИ правильно верил, потому что однажды он взял и сам себе записку оставил и на следующую смену её прочитал. И на следующую, и на следующую… В общем, если долго колотить по одному месту, то когда-нибудь в этом месте появится трещина; в общем, когда в сто тысяч миллионный раз ему эта записка попалась, вспомнил он, как эту записку писал, и постепенно понял, что на самом деле все здесь, в лагере живут, просто забывают об этом, а то, что считают домом — только сон. Ну ещё разные проверки делал, и в лагере, и дома, но всё сходилось.\nИ как только он это понял, так начал свою жизнь в лагере запоминать; а те сны, что про взрослую жизнь, у него постепенно прекратились. Он помнил, что ему двадцать семь, и иногда вёл себя так, как будто ему двадцать семь, но внешне был как все пионеры и ничем от них старался не отличаться.{/i}"
    nvl clear
    "{i}А он отличался — помните, я говорила? Просто все в лагере жили как роботы: записано в программе у роботов, что нужно купальный сезон в четверг открывать, а в субботу спортивный праздник устраивать — так и будет; записано, что вон тому пионеру должна нравиться вот эта пионерка — так и будет; записано, что другая пионерка должна убежать купаться за территорию на четвёртый день после приезда — значит она убежит, и её там поймает вожатая и накажет, потому что у вожатой тоже программа — пойти и проверить выходы к воде за территорией.\nА что там дальше, вокруг лагеря — их не интересовало, и даже самые любопытные дальше костровой поляны не ходили никогда. И думали все, что так и надо, что это как будто они сами всё делают так, как хотят.{/i}"
    show dv normal pioneer at left
    show us normal sport at cleft
    show d_us normal sport at right:
        ypos -0.05
    with dissolve
    $ set_mode_adv ()
    show d_sf normal pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "Потому что очевидные причинно-следственные связи — вот они."
    hide d_sf with dspr
    us_old "Да, Сём, спасибо, «очевидные причинно-следственные связи» — именно так."
    us_old "А когда тот пионер…"
    $ set_mode_nvl ()
    hide dv
    hide us
    hide d_us
    with dissolve
    "{i}А когда тот пионер приезжал, вся программа начинала рассыпаться, потому что тот пионер просто жил, даже когда ещё ничего не помнил: сегодня он на гитаре учится играть, в следующую смену вдруг активистом оказывается, в следующую — прячется от всех; что-то в его программе не учли, и она не работала.\nНу а остальные только рады были и тоже начинали жить, потому что в программе поступки того пионера не записаны были, программа рассыпалась, и надо было уже самим думать.\nПотому что пионеры — они хоть и как куклы были, но не куклы же; пусть они ничего и не помнили и программа ими руководила, но они тоже любили и чувствовали, и плохо им было где-то внутри, пусть они и не понимали, что с ними происходит.{/i}"
    show dv normal pioneer at left
    show us normal sport at cleft
    show d_us normal sport at right:
        ypos -0.05
    with dissolve
    $ set_mode_adv ()
    us_old "Сём, если тяжело сидеть, ты ложись. Мы не обидимся."
    us_old "Ну а тот пионер…"
    $ set_mode_nvl ()
    hide dv
    hide us
    hide d_us
    with dissolve
    "{i}А тот пионер — он разворошит лагерь и хорошо ему, потому что видит, что и люди вокруг, оказывается, живые, и сам он живой, а не кукла и не сумасшедший.\nС кем-то подружится, в какую-то девочку влюбится, какая-то в него влюбится. Он, может, потому и понял всё про себя, что всё, что человеческого от пионеров получал, он в себя впитывал и сам изменялся — может быть, просто случайно, может, по недосмотру программы.\nА когда изменений много накопилось, он и стал отличаться от того пионера, для которого программа была записана, и начал помнить про себя всё.{/i}"
    show dv normal pioneer at left
    show us normal sport at cleft
    show d_us normal sport at right:
        ypos -0.05
    with dissolve
    $ set_mode_adv ()
    show d_sf smile pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "Сбой алгоритма поведения, не более."
    hide d_sf with dspr
    us_old "«Сбой алгоритма поведения» — спасибо, Сёмк."
    us_old "Девочки, я понятно рассказываю?"
    show us grin sport with dspr
    us "Всё-всё понятно. А что непонятно, то спросим. Ты рассказывай, сестрёнка."
    show us normal sport with dspr
    us_old "Хорошо."
    us_old "Вот только плохо Степану бывало уже потом, когда старый цикл заканчивался, а новый начинался."
    show us surp1 sport with dspr
    us "Что ещё за цикл?"
    us_old "Цикл? Да он, сестрёнка, смены циклами стал называть, потому что всё по кругу ходило."
    show us normal sport with dspr
    us_old "В общем, приезжает он в лагерь…"
    $ set_mode_nvl ()
    hide dv
    hide us
    hide d_us
    with dissolve
    "{i}Приезжает он в лагерь, а там всё по-прежнему и никто его не помнит; даже та, с кем в любви друг другу клялись, смотрит на него и не узнает, и надо всё сначала начинать.\nНачинает сначала, а результат другой: с кем неделю назад дружил — с тем сегодня поссорился, кто тебе жуков в ботинки подбрасывал — тебе в глаза заглядывает и каждое слово ловит, потому что живые же люди — и С… Степан, и те, что вокруг него, они не могут каждый раз жить одинаково.\nА на следующий цикл опять надо по полной выкладываться, чтобы до пионеров достучаться, потому что если просто сидеть и ничего не делать, то все пионеры и ведут себя как куклы; а так, из цикла в цикл в окружении кукол, с ума можно сойти.\nНекоторые и сходили.{/i}"
    show dv normal pioneer at left
    show us normal sport at cleft
    show d_us normal sport at right:
        ypos -0.05
    with dissolve
    $ set_mode_adv ()
    show d_sf serious pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "…"
    hide d_sf with dspr
    us_old "Молчи, Сёмка, не говори ничего."
    us_old "Вот тот пионер…"
    $ set_mode_nvl ()
    hide dv
    hide us
    hide d_us
    with dissolve
    "{i}Вот тот пионер и решил из этих циклов вырваться — взял и сбежал из лагеря.\nИз циклов, и чтобы больше близких людей не терять — может, думал, что одному ему лучше будет.\nИ получилось так, что прибежал в другой лагерь, точно такой же — думал, что убегает, а оказался в другом лагере.\nЦикл там прожил — убежал в третий. Потом в четвёртый, пятый, тридцать третий.\nМного лагерей, и все одинаковые, и в каждом одинаковые пионеры. Почти одинаковые, потому что живые же люди, а не болты какие-нибудь — не может программа совсем всё в человеке отключить.\nИ Степан тот опыта набирался и, не знаю как назвать, человечности, что ли. И вот однажды получилось у него до двоих достучаться, так что они тоже стали всё помнить.\nМожет быть, потому что человеческого, а не кукольного, в нём столько накопилось, что хватило и с теми двумя поделиться.\nА на следующий цикл ещё до одного, а потом ещё, потому что чем больше человек в лагере проснулось, тем легче разбудить следующего.\nИ даже если кто опять уснёт, он просыпается уже легко, как будто что-то там в голове у него включается.{/i}"
    nvl clear
    "{i}Вот только те пионер{w=0.5}…ры из самого первого лагеря, из которого Степан убежал — они же никуда не делись, они так с ним и остались, в памяти его, и забыть их не получается, и он себя виноватым перед ними чувствует.\nПотому что они столько ему дали человеческого, а он разбудить их не смог. Вот такая сказочка. Ложь, да в ней намёк.{/i}"
    show dv normal pioneer at left
    show us normal sport at cleft
    show d_us normal sport at right:
        ypos -0.05
    with dissolve
    stop music fadeout 1
    $ set_mode_adv ()
    show dv smile pioneer with dspr
    dv "Подруга, ты в журналы не пробовала писать? В «Уральский следопыт», или там в «Пионер» какой?"
    us_old "А зачем, Алиса? Всё равно не напечатают. Я же так, для себя и для вас, на ходу сочинила."
    show dv shy pioneer with dspr
    dv "Тогда запиши это и в нашу стенгазету отдай. Пусть народ почитает, потому что красиво у тебя получилось."
    show d_sf smile pioneer at center behind d_us with dspr:
        zoom 0.8 xpos 0.6
    me "Всё, дорогие барышни, хватит сказки слушать, садитесь чай пить."
    stop ambience
    
    #Вообще чаепитие удалось. Семён, внешне угрюмый, оказался остроумным и понимающим собеседником, нисколько не давящим разницей в возрасте и в статусе. 
    #«Девочки, окажетесь у меня на спортплощадке — будете звать меня по имени-отчеству, а сейчас, пожалуйста, просто по имени и на ты. 
    #Может быть потом, лет через десять, я и дорасту, а сейчас меня ещё пока официальное обращение коробит. 
    #А будете возражать — я вас буду на Вы и по имени-отчеству звать, и будем мы тут сидеть надутые и важные, и будем чай из блюдца вприкуску хлебать, как купцы первой гильдии». 
    #Гости рассказали про свой лагерь, удивительно похожий, расспросили про житьё в здешнем. 
    #«Почему вожатая меня не помнит — да кто ж её знает, сам удивляюсь. А бросаться ей на шею с криком: „Оля! Это же я, Сёма!“ — жены боюсь. 
    #Вдруг гусеницу под одеяло запустит». Рассказали про футбольную команду в своём лагере, тут Ульяна-младшая с особым интересом посмотрела на гостей и повздыхала: «Жаль, что у нас такой нет». 
    #Когда девочки поблагодарили за показанное озеро, то получили ответ: «Не за что, нам-то оно уже не пригодится, потом вам ещё одно место покажем. Считайте, что наследство от нас получили. 
    #Нет, Ольга о нем не должна знать, всё может быть, конечно, но вряд ли она знает. Вот Виола и Анатолий — те, наверное, знают, но туда не ходят и болтать не будут». 
    #«Кто такой Толик? Знаешь, давай не будем ворошить чужие секреты. Вы считали его дурачком, вот и продолжайте делать вид, что считаете. 
    #Вреда он никому не принёс, а пользу — многим». 
    #«Далеко ли до нашего лагеря? Мы за полдня добрались, но это дорогу нужно знать». О разном ещё поговорили, пошутили, Алиса даже пожалела, что гитару не взяла.

    scene ext_playground_night with dissolve
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound_loop dct_sfx_steps2
    show dv normal pioneer at fleft
    show us normal sport at left
    with dissolve
    "Где-то через час после отбоя Рыжие возвращались к себе."
    us "Ну и как тебе вечер?"
    dv "А знаешь, Уль. Понравилось. Даже не ожидала от себя такого. И вечер понравился, и гости понравились. Думала, Семён будет хуже, а он ничего так. Даже пожалела, что гитару не взяла."
    dv "Твоя «сестрёнка» — та, конечно, девушка очень хорошая, но молодая ещё. А вот Семён… Что он там говорил о себе? Что он физрук и заместитель вожатой у себя в лагере? Был бы он у нас в лагере — я бы, может, и образцовой пионеркой стала."
    us "Так я и поверила. Строем ходить ты не можешь и командовать собой не разрешаешь. Только очень близким людям если, и то когда они по делу говорят, а Семён уже занят."
    us "Другое дело, что он бы понимал тебя и на твоё поведение внимания бы не обращал, или даже придумал бы, что тебе поручить, раз ты строем ходить не любишь."
    dv "Да, я не знала, что умные физруки на свете бывают. Правда, он, может, на лето только физруком устроился, а зимой — не знаю, может, работает где-то там, где голова нужна."
    hide dv
    hide us
    with moveoutleft
    stop sound_loop
    "Тут девочки одновременно остановились и одновременно же сделали шаг в сторону ближайших кустов, куда не добивал свет от фонарей, чтобы пропустить совершающую вечерний обход Ольгу Дмитриевну."
    show mt normal panama pioneer with moveinright
    $ renpy.pause (0.5)
    hide mt with moveoutright
    "Ольга подошла к спортзалу, постояла на крыльце, занеся руку и собираясь постучаться, но передумала и пошла дальше, к хозяйственным воротам, чтобы оттуда свернуть к пляжу."
    show dv normal pioneer with moveinleft:
        xpos -150
    dv "Отбой тревоги."
    stop ambience
    
    scene int_house_of_dv_night with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_night
    show us normal sport at right
    show dv normal pioneer at left
    with dissolve
    us "Алис, а я всё о сказке этой думаю. Как ты думаешь, о ком она?"
    show dv surprise pioneer with dspr
    dv "А я знаю? Ну не о Семёне же. Не хочешь же ты сказать, что мы одну и ту же смену постоянно проживаем, а Семён раньше с нами жил и сейчас проведать приехал?"
    show dv smile pioneer with dspr
    dv "Я так думаю, что её та Ульяна сочинила и просто рассказать кому-то незнакомому захотела, чтобы проверить, как получилось."
    show blink
    stop ambience
    $ renpy.pause (0.5)
    "День, богатый неожиданными событиями, закончился. Девочки добрались до домика, взяли полотенца и убежали к умывальнику. Нужно было успеть умыться, вернуться и залечь в кровати."
    "Скоро мимо их домика должна была пройти вожатая, и выслушивать порцию воплей совершенно не хотелось, не хотелось портить впечатление от в целом неплохого дня."

#####################
#Глава 6. Бессонница#
#####################
   
label insomnia:
    $ save_name = u"Дубликат. Четвертая смена - Бессонница"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Бессонница" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene d_int_house_of_dv_night_without_light with blinds
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    "Алисе не спалось — слишком много впечатлений она получила за прошедший день."
    "Стоило закрыть глаза, как начинал сниться один и тот же сон: она и Мику учат Семёна играть на гитаре."
    stop ambience
    
    scene int_musclub_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play music music_list["orchid"]
    show d_sm sad pioneer at left with dspr
    dv "Сенька! Ещё раз слажаешь — получишь щелбан. Два раза слажаешь — два щелбана. У меня уже палец чешется!"
    stop music fadeout 3
    show mi normal pioneer at right with moveinright
    mi "Алисочка, не дави на Сенечку!\nСенечка, давай я тебе ещё раз покажу, смотри внимательнее, это очень просто."
    
    scene ext_stage_normal_day
    show d_sm smile pioneer at left
    with squares
    play ambience ambience_camp_center_day
    "Потом Мику исчезает, а Алиса с Семёном переносятся на эстраду, где вдвоём подбирают какую-то песню."
    me "Ну, может, ты хоть это слышала?"
    dv "Сенька, сознавайся, откуда ты это всё притащил?"
    show d_sm normal pioneer with dspr
    me "Сознаться? Но ты же всё равно не поверишь."
    "Почему-то Семён из сна — её ровесник. Он опоздал к началу смены, а сегодня попросил у Мику гитару, ушёл на концертную площадку и, кажется, не собирается идти на дискотеку."
    play music music_list["orchid"] fadein 3
    "Но это, несомненно, тот самый Семён, который сегодня пришёл в лагерь, которому Виола лечила спину и который угощал их вечером чаем с домашним печеньем."
    show d_sm sad pioneer with dspr
    me "Слушай тогда. Может, хоть на этот раз…"
    "Во сне этот Семён каждый раз собирается рассказать Алисе что-то важное, уже открывает рот, но в самый последний момент Алиса всегда просыпается."
    stop music fadeout 1
    stop ambience
    
    scene d_int_house_of_dv_night_without_light with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    play sound sfx_close_door_1
    show 3500_dv normal night at center with dspr:
        ypos -0.15
    th "Так я никогда не усну. Пойду проветрюсь."
    stop ambience
    
    scene ext_house_of_dv_night
    show 3500_dv normal night:
        ypos -0.15
    with dspr
    play ambience ambience_camp_center_night
    th "Подышу, может, уснуть получится."
    play sound dct_sfx_inhale
    th "Пахнет {w=0.5}ночью. Приключениями. Романтикой. Растревожила меня Ульяна-большая своей сказкой. Убежать из лагеря — это вам не в столовую по ночам лазить. Может,{w=0.5} лодку угнать и уплыть отсюда? Мелкая обидится, что без неё."
    th "Ольга спит, Славя спит — можно не опасаться. Темнотища, никто не увидит."
    th "Да, темнотища. Лампочку над дверями включить?"
    th "Нет, так я ничего не увижу, а меня всем видно будет."
    show 3500_dv shocked night with dspr
    th "Нечего им на меня в неглиже любоваться."
    show 3500_dv normal night with dspr
    th "Вот только кому это «им»? Спят же все."
    play sound dct_sfx_apple fadein 1
    th "Зверушка какая-то шуршит. Яблоко моё доедает, а я даже не откусила ни разу, как достала, так и забыла — Ульяна-большая меня отвлекла своим приходом." 
    th "Вспомнила! Я же с Сенькой песню подбирала во сне! Всё вспомнила: и слова, и аккорды!"
    th "Всё равно не усну, пойду поиграю."
    stop sound
    stop ambience
    
    scene d_int_house_of_dv_night_without_light with dspr
    play ambience ambience_int_cabin_night
    show 3500_dv normal night at center with dspr:
        ypos -0.15
    th "Так, а гитара где? Забыла сама же на сцене, раззява. Джинсы в шкафу. Хоть ночью в джинсы влезть, пока Ольга спит."
    play sound dct_sfx_wood_floor_squeak
    th "Ш-ш-ш. Тише ты, Алиса. Мелкую разбудишь."
    show 3500_dv normal casual with dspr
    th "Мелкая, я на сцену. А ты спи, пожалуйста."
    stop sound
    stop ambience
    
    scene dct_ext_houses_night
    show 3500_dv normal casual at fleft:
        ypos -0.15
    with dspr
    play ambience ambience_camp_center_night
    th "Сейчас пробегу пару раз песню. Вдруг её можно показывать? Или лучше будет спрятать подальше и постараться забыть?"
    stop ambience

    scene d_int_house_of_dv_night_without_light with dissolve
    play ambience ambience_int_cabin_night
    "Пять минут спустя, когда Алиса кралась, огибая по периметру площадь, проснулась Ульяна."
    us "Алиска."
    stop ambience
    
    scene dct_ext_boathouse_day_with_pass_train with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play music music_list["door_to_nightmare"] 
    "Ульяне тоже снился сон, и тоже с участием Семёна. Снилось Ульяне, что она стоит на берегу и смотрит на лодку, добравшуюся уже до середины протоки."
    show dv angry pioneer at fright with moveinright
    dv "Ну, Сенька, если не сумеешь сбежать — лучше до самого отъезда мне на глаза не попадайся."
    hide dv with moveoutleft
    "А Ульяна сначала прыгает на месте от избытка эмоций и машет Семёну обеими руками, как спортсмену на стадионе, а потом прекращает прыгать, опускает левую руку, а правой машет всё медленнее и наконец замирает, встав на цыпочки с поднятой правой рукой, прощаясь."
    "И на душе — там, во сне — становится одновременно и радостно за Семёна, потому что уже ясно, что всё у него получится; и грустно, что он уплывает; и обидно, что не позвал с собой и даже не попрощался."
    "С этим ощущением радости-грусти-обиды Ульяна-младшая и проснулась."
    stop music fadeout 1
    
    scene d_int_house_of_dv_night_without_light with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    us "Алиска." 
    us "Алиска. Ты спишь?"
    "Ульяна ничего не боялась. Ничего. Но она старалась никогда-никогда не оставаться ночью одна в домике. Сразу вспоминались все те страшные истории, которыми она любила пугать октябрят из младшего отряда, и в каждой тени, в каждом тёмном углу чудился кто-то из персонажей этих историй."
    "Ульянке бы встать, добежать до выключателя и зажечь свет, но не хватало храбрости выбраться из-под одеяла."
    th "Ушла. Страшно-то как одной."
    th "Ничего, я сейчас."
    show blink
    "Наконец, когда на борьбу со страхом не осталось никаких сил, Ульянка вскочила и, зажмурившись, схватила со стула одежду и побежала к выходу."
    stop ambience
    
    scene ext_house_of_dv_night
    show us calml sport
    with dissolve
    play ambience ambience_camp_center_night
    "И мгновенно стало спокойнее, и страх сразу куда-то ушёл. Девочка ещё постояла, приходя в себя и осматриваясь в поисках Алисы."
    show us normal sport with dspr
    play sound dct_sfx_apple
    th "Кто шумит? Алиска? За домиком сидит? Песню сочиняет?"
    "За домиком шуршали кусты, и Ульянка, всунув ноги в стоявшие тут же на крыльце сандалии, крадучись пошла в обход."
    show us grin sport with dspr
    th "Ну, Алиска, сейчас я тебя напугаю!"
    stop sound
    stop ambience
    
    scene dct_ext_aidpost_night_with_light with squares
    play ambience ambience_camp_center_night
    "Анатолий с Виолой тоже не спали, правда, никакие необычные сны их не тревожили.\nПоследние, не считая Шурика, люди-подлинники вспоминали."
    "Вспоминали закрытие проекта, вспоминали посёлок Шлюз, вспоминали Денисовну, которую видели последний раз лет десять назад, когда удалось созвониться, удалось договориться о встрече, и последние люди, сохранявшие память, собрались в ночь между циклами на автобусной остановке у ворот посёлка."
    "А ещё не давало уснуть письмо Глафиры Денисовны. По словам Семёна, пакет с письмом ему был вручён за один цикл до смерти профессора Андрейко."
    stop ambience
    
    scene int_dining_hall_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    show d_bg normal suit at right
    show d_sf normal sport at left
    with dissolve
    d_gd "Передашь Виоле или Анатолию. Если не сумеешь, прочти сам, а там уже решай, как поступить."
    stop ambience
    
    scene dct_ext_aidpost_night_with_light with pixellate
    $ night_time ()
    play ambience ambience_camp_center_night
    "А через две недели Глафира Денисовна ушла, и первый настоящий переход между узлами Персуновы совершили по печальному поводу."
    "А завтра нужно было ещё раз, уже внимательно перечитать письмо — в той его части, которая касалась Сети лагерей. Изучить содержимое общих тетрадей, проверить обоснованность содержащихся там выводов, и уже тогда принимать решение."
    "Кстати, нужно было показать это письмо ещё и Семёну, тем более что там была пара абзацев, обращённых к нему лично."
    stop ambience
    
    scene int_aidpost_night
    show d_to normal pioneer at left
    show cs normal glasses at right
    with dspr
    play ambience ambience_medstation_inside_night
    d_to  "Давай спать, старушка, головы должны быть свежими. Сейчас мы всё равно ничего не решим."
    show cs normal glasses with dspr
    cs "Семён?"
    d_to "Поговорю. Он не помнит почти ничего, но поговорю. Или ты поговори. Может, он что-то со стороны в этой ситуации увидит."
    show cs normal glasses with dspr
    cs "Да уж, человек-загадка какой-то… Он должен был вспомнить всё, либо давно уже отключиться, а он половины не помнит. У него в узле только пятеро в активной фазе, а он не спит. И похоже, пока он не спит, он и другим вокруг себя спать не даст. Ладно, оставим ему его проблемы. А нам спать действительно пора."
    play sound sfx_click_1
    show blink
    stop ambience
    
    scene dct_ext_aidpost_night_with_light with dspr
    play ambience ambience_camp_center_night
    scene ext_aidpost_night with dissolve
    "Свет в медпункте погас, и оба обитателя, не беспокоясь больше ни о чём, проспали до самого подъёма. Их ждало пять общих тетрадей, исписанных от корки до корки, и у них было трое с половиной суток на прочтение и принятие решения."
    stop ambience

    scene ext_stage_big_night
    $ persistent.sprite_time = "night"
    show d_us normal dress at right:
        ypos -0.05
    show d_sf normal hike at left
    with squares
    play ambience ambience_camp_center_night
    us_old "Сёмк, ты спать думаешь идти?"
    me "Думаю, Рыжик. Или поиграть ещё?"
    us_old "Пф. Что ты меня-то спрашиваешь? Я только поинтересовалась, собираешься ли ты спать. Ты ответил, что да. А идти спать или ещё поиграть — дело твоё. Поиграй, а?"
    me "Ты знаешь, я ведь учился играть именно на этой гитаре. А Алиса мне за каждую ошибку щелбан ставила."
    show d_us smile dress with dspr
    me "И не улыбайся, случится с тобой приступ ностальгии — поймёшь меня."
    show d_us normal dress with dspr
    me "Поздно уже. Поиграть, говоришь?"
    me "Чуть-чуть разве."
    stop ambience
    
    scene ext_stage_normal_night
    show d_us normal dress at right:
        ypos -0.05
    show d_sf normal hike at left
    with dspr
    play ambience ambience_camp_center_night
    us_old "Поводишь меня завтра по лагерю? Я хочу твоими глазами его увидеть."
    me "Я же водил."
    us_old "Ты по нашему водил, а я хочу по этому… {w=1}Кто-то идёт."
    show d_us normal dress at cleft with move
    show d_sf normal hike at fleft with move
    play sound dct_sfx_steps3 fadein 1
    $ renpy.pause (3)
    stop sound
    show 3500_dv normal casual at right with moveinright:
        ypos -0.15
    me "Хозяйка за гитарой пришла. Вот и поиграл. Так что — только спать, Рыжик."
    me "Спокойной ночи, Алиса."
    "А Алиса вдруг неожиданно для себя спросила Семёна о том, что мучило её с самого обеда."
    show 3500_dv shy casual with dspr
    dv "Послушай, Семён. Где я тебя видела?"
    "И что-то внутри Алисы оборвалось от её собственного вопроса."
    show 3500_dv shocked casual with dspr
    show d_us hurt dress with dspr
    show d_sf laugh hike with dspr
    me "Жаль, что ты не Славя. Потому что для неё я уже сто лет назад приготовил красивый ответ."
    show d_sf smile hike with dspr
    me "Но мне нравится то, что этот вопрос задала именно ты."
    show d_sf normal hike with dspr
    me "Последний раз ты меня видела в лодке: ты стояла на берегу и что-то говорила Ульяне-маленькой, а я уплывал от вас, делая двадцать гребков в минуту."
    me "Я бы помахал вам всем на прощание, но боялся сбиться с ритма."
    me "Что-то ещё? Спрашивай."
    show d_sf serious hike with dspr
    me "Алис! Ты в порядке?"
    hide 3500_dv
    show 3500_dv scared casual at cright with hpunch:
        ypos -0.15
    us_old "Сёмка, что смотришь? Она же сейчас упадёт!"
    show blink
    $ renpy.pause (1)
    play sound sfx_alisa_falls
    show 3500_dv scared casual at center:
        ypos -0.15
    show d_us normal dress at cright:
        ypos -0.05
    show d_sf serious hike with dspr:
        xcenter 0.32
    $ renpy.pause (3)
    hide blink
    show unblink
    us_old "Алиса, всё хорошо. Сейчас мы тебя к Виоле отведём."
    dv "Чт-то эт-то так-кое был-ло?"
    me "А что именно было?"
    dv "Т-ты сказал мне про лодку. И я вдруг увидела это всё, как будто вспомнила. И после этого мне стало плохо."
    me "Не знаю."
    us_old "Алис, ты идти сможешь?"
    show 3500_dv normal casual with dspr
    dv "К Виоле? Нет уж, нет уж."
    "Алиса постепенно приходила в себя."
    us_old "А домой тебя проводить?"
    dv "Да в порядке я уже!"
    dv "Вообще-то я поиграть пришла, на гитаре. Которую кое-кто успел потрогать."
    me "Ну не ломать же было дверь музыкального кружка, когда тут нашёлся инструмент, брошенный хозяйкой."
    me "Мы сейчас уйдём. Только скажи мне честно и откровенно: ты действительно в порядке?"
    show 3500_dv angry casual with dspr
    dv "Р-р-р-р!"
    show d_sf laugh hike with dspr
    show d_us smile dress with dspr
    "Да, Алиса пришла в себя."
    me "Ах-ах-ах-ах-ах… Всё, всё, всё, Алиска, теперь верю."
    show d_sf normal hike with dspr
    me "Пошли, Ульяныч, не будем мешать творческому процессу."
    hide d_us
    hide d_sf
    with moveoutright
    stop ambience
    
    scene ext_stage_big_night
    show 3500_dv shy casual at fleft:
        ypos -0.15
    with dspr
    play ambience ambience_camp_center_night
    "Семён и Ульяна уже уходили с площадки, когда Алиса неожиданно для самой себя позвала:"
    dv "Семён!"
    show d_sf normal hike at cright
    show d_us normal dress at fright:
        ypos -0.05
    with moveinright
    me "Да, Алиса."
    dv "А ты играешь?"
    me "Немного."
    dv "Сыграешь?"
    me "Не сейчас, но до отъезда — обязательно. А сейчас я спать. И ты не засиживайся, а то Ульянка одна проснётся."
    stop ambience
    
    scene ext_playground_night
    show d_us normal dress at cleft:
        ypos -0.05
    show d_sf normal hike at fleft
    with squares
    play ambience ambience_camp_center_night
    play sound_loop dct_sfx_steps3
    us_old "Я сейчас очень сильно испугалась за Алису."
    me "Я тоже. Никогда и ни у кого не было такой реакции на мои рассказы о прошлых циклах. Когда я на вас орал в бункере, вы просто боялись. Мику и Сашка мне не поверили. Вообще большинство или пальцем у виска крутило, или говорило, что я красивую сказочку рассказываю. А тут вот так…"
    me "Хорошо, что успели подхватить рыжую."
    stop sound_loop
    stop ambience
    
    scene dct_int_coaching_room3_night with squares
    play ambience ambience_int_cabin_night
    show d_sf normal hike at center with dspr
    me "Шоковую реакцию своими фразами у пионеров вызывает Виола — сам сегодня видел; правда, шок, гм, специфический. Шоковую реакцию вызывал Пионер — вспомни случай с Сашкой. И получается, что теперь шоковую реакцию вызываю ещё и я. Я боюсь, Рыжик. Я не хочу, чтобы от моих неосторожных слов кто-то пострадал или вообще исчез."
    stop ambience

    scene ext_stage_normal_night with squares
    play ambience ambience_camp_center_night
    "Алиса, оставшись одна, попробовала поиграть, но после непонятного приступа ничего толкового не получалось. Несколько раз пробовала — бесполезно. Перед глазами стояла описанная Семёном сцена и всплывали подробности, о которых Семён не упоминал."
    stop ambience
    
    scene dct_ext_boathouse_day_with_pass_train with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play music adaytoremember
    show sl scared sport with moveinleft
    sl "Ольга Дмитриевна, но почему, почему? Что мы ему сделали плохого?"
    hide sl with moveoutleft
    show us surp1 sport with moveinright
    us "Давай, Сёмка!"
    hide us with moveoutright
    show mt rage pioneer panama with moveinleft
    mt "Славя, отвязывай лодку! Сыроежкин, бей окно в сарае и доставай вёсла!"
    hide mt with moveoutleft
    show el surprise pioneer with moveinleft
    el "Бегу, Ольга Дмитриевна!"
    hide el with moveoutleft
    
    scene ext_stage_normal_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show 3500_dv shocked casual with dissolve:
        ypos -0.15
    th "Что за гипноз такой? Зачем спросила? Кто за язык тянул? Ведь пришла поиграть — вот и играла бы."
    stop music fadeout 1
    th "Спать надо идти, Рыжая. А то и правда Ульянка одна проснётся."
    stop ambience
    
    scene dct_ext_houses_night
    show 3500_dv normal casual at fright:
        ypos -0.15
    with squares
    play ambience ambience_camp_center_night
    play sound_loop dct_sfx_steps3
    "Пока шла домой, показалось, как кто-то побежал от домика в сторону забора."
    show 3500_dv shocked casual with dspr
    th "Ульяна? Решила себе нервы пощекотать?"
    show 3500_dv normal casual with dspr
    th "Нет, просто тени так сложились."
    stop sound_loop
    stop ambience
    
    scene ext_house_of_dv_night
    show us sad sport at fleft
    with squares
    play ambience ambience_camp_center_night
    show 3500_dv normal casual at fright with moveinright:
        ypos -0.15
    dv "Тоже не спится? Давно сидишь?"
    "Ульяна всегда делала вид, что ничего не боится, а Алиса — что ничего не знает об Ульянкиных страхах, только старалась не оставлять её одну. Но не всегда получалось, вот как сегодня."
    us "Нет, не очень. Как песня?"
    dv "Никак, надо ещё работать. Давай спать."
    us "Давай."
    show blink
    stop ambience
    "И последние обитатели лагеря наконец-то угомонились. До подъёма оставалось чуть больше пяти часов."
    
###########################
#Глава 7. Последнее письмо#
###########################
   
label last_letter:
    $ save_name = u"Дубликат. Четвертая смена - Письмо"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Последнее письмо" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_d2_mt_undressed with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["i_want_to_play"]
    "Вожатая только что вернулась от умывальников и сейчас, всё ещё дрожа от ледяной воды, переодевалась из спортивного костюма в форму."
    "Несмотря на запрограммированную привычку следовать нормам, уставам и правилам распорядка, Ольга этими правилами тяготилась и находила отдушину в мелкой бытовой лени и раздолбайстве."
    "Потому и спортивный костюм, и повседневная форма, и ночная рубашка, вместо того чтобы висеть в шкафу, лежали сейчас рядком на свободной кровати."
    
    scene dct_d2_mt_undressed_2 with dspr
    th "Скоро всё это закончится — скоро приедет опаздывающий пионер, а селить его негде, кроме как у себя."
    th "А это значит — прощай, свобода. И форму придётся прятать в шкаф. А не бросать где удобно."
    th "Не так уж и много этой самой свободы у вожатой. Каждый кусочек дорог."
    
    scene int_house_of_mt_day with slideleft
    show mt normal pioneer panama with moveinright
    th "Всё, Ольга Дмитриевна к новому дню готова."
    stop music fadeout 1
    stop ambience
    
    scene ext_house_of_mt_day 
    show mt normal pioneer panama at left
    with dspr
    play ambience ambience_camp_center_day
    play sound_loop sfx_slavya_run
    show sl smile sport close at right with moveinleft
    sl "Доброе утро, Ольга Дмитриевна."
    show mt smile pioneer panama with dspr
    mt "Доброе утро, Славя."
    hide sl with moveoutright
    stop sound_loop fadeout 1
    show mt normal pioneer panama with dspr
    th "Для начала — разбудить гостей. Славе, наверное, будет неловко отправлять на линейку взрослых людей. Сама схожу."
    th "Не знаю, зачем это нужно, но порядок есть порядок: линейка обязательна для всех."
    th "Алиса, конечно, линейку проспит. А я её, конечно, накажу."
    th "Если не забуду."
    hide mt with moveoutright
    "Ольга Дмитриевна ещё раз поправила галстук и, улыбнувшись возвращающейся с пробежки Славе, отправилась к спорткомплексу."
    stop ambience
    
    scene ext_playground_day
    show d_sf normal pioneer at center
    show d_us smile sport at cright:
        ypos -0.05
    with slideright
    play ambience ambience_camp_center_day
    play music music_list["timid_girl"]
    "По счастью, будить никого не пришлось."
    "И Семён, и Ульяна-большая (вот прижилось же в лагере в первые же часы пребывания гостей: Ульяна-большая и Ульяна-маленькая) стояли на улице и, судя по всему, только что пришли с пляжа."
    show d_sf smile pioneer at right
    show d_us smile sport at fright:
        ypos -0.05
    with move
    show mt normal pioneer panama at left with moveinleft
    me "Доброе утро, Ольга Дмитриевна."
    show mt normal pioneer panama with dspr:
        zoom 1.2
    th "Ну до чего же улыбка знакомая."
    show mt normal pioneer panama with dspr:
        zoom 1
    mt "Доброе утро, Семён. Я пришла предупредить вас, что ровно в восемь линейка — явка обязательна."
    me "Всё понятно, придём. И спасибо, что приютили нас."
    show mt grin pioneer panama with dspr
    mt "Пустяки. Два человека за три дня не смогут объесть пионерский лагерь."
    show mt normal pioneer panama with dspr
    mt "Но вот ещё что: вы, Семён, раз вы болеете, то болейте, но я бы хотела, чтобы вы, Ульяна, приняли участие в жизни лагеря."
    mt "В общем, жду вас обоих на линейке через полчаса."
    hide mt with moveoutleft
    stop music fadeout 1
    
    show d_sf normal pioneer at center
    show d_us smile sport at cright:
        ypos -0.05
    with move
    us_old "Прямо как наша. Найдите десять отличий."
    me "Ну что, умываемся и вперёд, на танки? А вожатая — вожатая нигде не меняется. Зато ты изменилась. Заметила?"
    me "Ты не стала возмущаться, ругаться или как-то пытаться избежать «участия», а отнеслась к этому с философским спокойствием."
    us_old "Сёмк. Я уверена, что вожатая и сама не знает, какое именно участие я должна принять. Что это за неё программа сейчас говорила."
    us_old "Так что я могу голубую ленточку на ногу Генде повязать и назвать это «участием», и прокатит."
    me "Вот-вот, я именно об этом, Рыжик. Ну давай умываться, и пойдём уже."
    stop ambience

    scene dct_lineup with squares
    play ambience ambience_camp_center_day
    play music music_list["always_ready"]
    "Тридцать минут спустя Семён и Ульяна-большая были представлены лагерю."
    "К счастью, про «экологов» никто не вспомнил, а то Семён уже мысленно чертыхался и ругал фантазию Виолы, представляя, как он мямлит что-то собирающейся вроде бы стать экологом Славе."
    "Правда, был ещё и запасной вариант: просто сказать Славе, что никакого «завтра» у неё нет и не будет, а есть только вечные две недели, и если она не начнёт меняться внутри себя, то так в этих четырнадцати днях и останется запертой."
    stop music
    stop ambience
    
    scene ext_square_day
    show mt normal pioneer panama
    with dissolve
    play ambience ambience_medium_crowd_outdoors
    mt "И последнее. Эти три дня в лагере будут гости."
    mt "Семён."
    show d_sf normal pioneer at left with moveinleft
    mt "И Ульяна."
    show d_us normal sport at right behind mt with moveinright:
        ypos -0.05
    mt "Так случилось, что у Семёна проблемы со здоровьем, а единственный доктор в округе — это наша Виола."
    mt "Поэтому пока они гостят у нас."
    hide d_sf
    hide d_us
    with moveoutleft
    mt "На этом у меня всё. Через тридцать минут завтрак, а сейчас…"
    show mt rage panama pioneer with dspr
    mt "Лагерь!{w=2} Разойдись!"
    stop ambience

    scene int_dining_hall_day
    show d_bg normal suit at center
    with pixellate
    play music forgotten_summer
    $ prolog_time()
    $ set_mode_nvl ()
    "{i}Здравствуй, Виола; здравствуй, Толя; Семён, я надеюсь, что ты это прочтёшь, поэтому здравствуй и ты.\nОчень плохо, что я не могу рассказать вам всего лично, но поездку к Шлюзу я уже точно не выдержу, а рассказать это одному лишь Семёну я не могу.\nПрости, Семён, ты просто не поймёшь, о чём речь, и когда будешь пересказывать, обязательно ошибёшься и исказишь смысл. Сам виноват: меньше надо было играть в педагога и воспитателя, а больше посещать занятия.{/i}"
    "{i}Можете считать это прощальным письмом, а, наверное, так оно и есть. До Шлюза я не доеду, а переписать себя в пионерку при помощи Выключателя, конечно, можно (если вы этого не знали, то знайте — можно), но — нет. Поэтому не взыщите, но я буду вспоминать.{/i}"
    nvl clear
    "{i}Уже давно мне кажется, что мы сделали что-то не то, свернули не туда, но раньше это было где-то на уровне интуиции и неоформившихся сомнений, а сейчас это уже на уровне уверенности — я всё же не зря прожила здесь эти двадцать лет; по крайней мере, никто не отвлекал от работы.\nВся наша возня здесь — это цепочка ошибок, начиная с самой первой, образца пятьдесят шестого года, когда, прикрываясь испытанием водородной бомбы, мы создали пространственную вакуоль.\nБудущий нулевой узел, будущий посёлок Шлюз.{/i}"
    "{i}Потом оказалось, что к искусственной вакуоли примыкает целая гроздь полостей, которые мы не создавали.\nА мы, вместо того, чтобы зафиксировать параметры и закрыть за собой дверь, мы начали посылать сюда экспедиции.\nКоторые здесь не ждали, но которые оказались как раз к месту.{i}"
    nvl clear
    "{i}Как мы удивились, когда к палаткам второй экспедиции вышли из закрытого туманом леса „участники“ — точные копии участников экспедиции первой.\nНужно было или в панике бежать, взрывая за собой мосты и тоннели, или сначала перестрелять этих „детей тумана“, а потом уже в панике бежать.\nСемён, прости, я сейчас говорю о твоих „братьях и сёстрах“, но от своего видения тех событий шестидесятилетней давности и от своих слов я отказываться не буду.{/i}"
    "{i}Кстати, двухнедельный интервал между первой и второй экспедициями и определил длительность сегодняшних циклов.{/i}"
    nvl clear
    "{i}И вот мы, вместо того, чтобы убраться, вляпались. Как мы засучили рукава, с каким энтузиазмом и удовольствием…\nТридцать лет мне тогда было, и я была молодая и энергичная без пяти минут доктор наук.\nПомните героиню Любови Орловой?{/i}"
    "{i}Вторая ошибка — когда мы, вместо того, чтобы извиниться и, осторожно прикрыв дверь, уйти, начали радостно изучать то, что наоткрывали…{/i}" 
    play sound sfx_dinner_jingle_normal
    stop music
    $ set_mode_adv ()
    
    scene int_aidpost_day with pixellate
    $ day_time()
    play ambience ambience_medstation_inside_day
    show d_sf serious pioneer at right
    show d_to normal pioneer at left
    with dspr
    me "Я возьму это письмо?"
    d_to "Бери, конечно. Для того и позвали тебя, чтобы ты прочитал, а потом сказал нам своё мнение."
    show d_sf sad pioneer with dspr
    me "Мнение… Я же не знаю почти ничего. Так, отдельные моменты помню, в промежутке от отправления последнего транспорта с эвакуируемыми и до разъезда по лагерям. Могу только сказать, что сумасшедшей баба Глаша точно не была."
    d_to "Может, это и хорошо, что не знаешь. Ладно, пошли завтракать — дурачок Толик не может пропустить приём пищи."
    show d_to moron pioneer with dspr
    d_to "Запеканка! Ы-ы-ы!"
    hide d_to with moveoutright
    "Семён аккуратно спрятал письмо в конверт, конверт спрятал в журнал — тот самый, «Советская модница», и через спортзал отправился в столовую."
    hide d_sf with moveoutright
    stop ambience
    
    scene ext_houses_day
    show d_sf normal pioneer at left
    with dissolve
    play ambience ambience_camp_center_day
    "Пока шёл, раскланивался направо и налево — вот и плюс от посещения линейки. Потому что в первый день очень хотелось с каждым встречным поздороваться, а фактически выходило, что этот встречный — совсем незнакомый пионер."
    "Не напоминать же, что уже познакомился с ним много-много циклов тому назад — не поймёт."
    stop ambience

    scene ext_square_day
    show dv normal pioneer at cright
    with squares
    play ambience ambience_camp_center_day
    show d_sf smile pioneer at left with moveinleft
    me "Привет."
    show dv smile pioneer at cright with dspr
    dv "Привет."
    hide d_sf with moveoutleft
    "Алиса кивнула прошедшему мимо Семёну."
    show dv normal pioneer with dspr
    th "Интересно, а модный журнал ему зачем? Ульяне-большой отдаст почитать? Не для себя же попросил…"
    th "Надо будет всё-таки прогнать ночную песню, может быть, дать оценить её Мику и как-то заставить Семёна поиграть на гитаре."
    show dv shocked pioneer with dspr
    dv "Гипнотизёр чёртов!"
    play music anewbeginning fadein 2
    "На самом деле Алиса так не считала, но как иначе, чем гипнозом, было объяснить продолжающееся с прошедшей ночи буйство воображения?"
    "Со вчерашнего вечера в голове всплывали картины и образы, странно связанные со вчерашней репликой Семёна про пристань, лодку и двадцать гребков в минуту."
    stop ambience
    
    scene dct_ext_boathouse_day_with_pass_train with pixellate
    $ prolog_time ()
    show us surp1 sport far with moveinright
    us "Сёмка, дава-а-ай!"
    show us grin sport with dspr
    us "Алиска, давай погребём, разомнёмся. За Сёмкой погоняемся. Он тормоз, мы его легко догоним."
    dv "Да не хочу я его догонять."
    show us sad sport close with dspr
    us "Алиса, да никто не хочет. Ты посмотри внимательно, как все себя ведут. Даже вожатка. Как будто их заставляют это делать."
    
    scene ext_square_day with pixellate
    $ day_time ()
    play ambience ambience_camp_center_day
    show dv shocked pioneer with dspr
    "А дальше вспоминался след от волочения лодки на песчаной стрелке острова, разбросанные инструменты, обрезки верёвки, щепки и неожиданно красиво идущая под светло-голубым самодельным парусом лодка."
    stop music fadeout 2
    "И Семён — нет, Сенька, сидящий на планшире наветренного борта лицом к выскочившей на берег погоне и всё-таки поднявший на прощание левую руку — совершенно искренне, без всякой издёвки поднявший."
    "А ещё почему-то представлялся импровизированный концерт и сорванная этим концертом дискотека, и они вдвоём — нет, втроём, ещё Мику, на сцене."
    dv "Гипнотизёр чёртов!"
    hide dv
    show dv shocked pioneer at left
    with dspr
    show us grin pioneer at right with moveinright
    us "Уж не влюбилась ли ты в самом деле?"
    show dv shy pioneer with dspr
    dv "Нет!"
    show dv normal pioneer with dspr
    dv "Точно нет. Это, наверное, гипноз. Точно: с тех пор, как нам сказку вчера вечером рассказали, всякая ерунда в голову лезет."
    show us calml pioneer with dspr
    us "Тебе тоже? И тоже про Семёна? Тогда точно: гипноз. А может, они нам что-то в печенье подмешали?"
    show us normal pioneer with dspr
    us "Нет, они же и сами его ели. А давай пока последим за ними…"
    hide dv
    hide us
    with moveoutright
    "На том порешили, успокоились и отправились завтракать."
    stop ambience
    
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    "Но в столовой обе девочки вспомнили о своих делах, похоронив утренние планы."
    play music music_list["my_daily_life"]
    show us normal pioneer close at left:
        ypos 0.05
    show dv normal pioneer close at right:
        ypos 0.2
    with dissolve
    dv "Ты куда сейчас?"
    us "Алиса, не спрашивай. Меньше знаешь — крепче спишь."
    show dv laugh pioneer close with dspr
    dv "Ну тогда я тебя сейчас сна лишу. Я — к Мику в кружок. Помучаю гитару."
    show dv normal pioneer close with dspr
    us "Угу. Учту."
    us "Ну? Мы позавтракали? Встаём и уходим?"
    dv "Давай. На обеде увидимся."
    stop music fadeout 1
    hide dv
    hide us
    show mi surprise pioneer
    with dissolve
    "Мику за завтраком постоянно поглядывала на гостей."
    th "Эта девушка просто копия нашей Ульяночки, когда наша вырастет, их будет не отличить."
    th "А парень — он совсем почти не улыбается, но такой милый. Ольга Дмитриевна сказала, что его зовут Семён. Ну какой же это Семён? Это Сенечка."
    show mi normal pioneer with dspr
    "{i}Нет, это была не та Мику, что однажды купалась с Семёном на дальнем берегу острова. Да и от той Мику не осталось практически ничего: душа, которую в здешних терминах называли «неуничтожимым ядром личности», и оболочка.{/i}"
    "{i}Но не могла та их встреча с Семёном, тот выплеск чувств пройти бесследно: как всем Алисам снилась одна и та же песня, так и уменьшительно-ласкательное «Сенечка» расползлось по всем узлам сети.{/i}"
    stop ambience
    
    scene int_musclub_day with squares
    play ambience ambience_music_club_day
    play sound sfx_knock_door2
    me "Мику, можно к тебе?"
    show mi surprise pioneer with moveinleft
    stop sound
    mi "Заходи, Сенечка! Конечно же можно!"
    play music music_list["so_good_to_be_careless"]
    show d_sf normal pioneer at left with moveinleft
    hide mi
    show mi smile pioneer at right
    with dspr
    mi "Здравствуй! Тебя на линейке всем представляли, а ещё я слышала, что ты разрешил всем к тебе на ты обращаться, поэтому я сразу к тебе на ты и обратилась."
    show mi normal pioneer with dspr
    mi "Я слышала, что вы с Ульяночкой путешествуете, это так здорово! А я вот всё время сижу в музыкальном кружке, жду, что кто-то придёт и запишется, но пионеры совсем не хотят заниматься музыкой. Так жаль, что ты не пионер, потому что ты бы обязательно в кружок записался."
    show mi grin pioneer with dspr
    mi "А меня зовут Мику, Мику Хатсуне, я японка. Но я японка только по маме, а папа у меня русский инженер…"
    show d_sf laugh pioneer with dspr
    "А Семён только слушал, кивал и улыбался чему-то своему."
    show d_sf smile pioneer with dspr
    "Наконец у Мику кончился запас воздуха в лёгких, и это позволило Семёну вклиниться в монолог."
    me "Здравствуй, Мику. А я гитару попросить зашёл. В долг до воскресенья."
    show mi happy pioneer with dspr
    mi "Сенечка! Так ты всё-таки играешь! Как это замечательно! А может быть, ты ещё зайдёшь ко мне в кружок? Я всегда рада, когда приходят новые люди! А сейчас я поищу что-нибудь подходящее."
    hide mi with moveoutleft
    stop music fadeout 1
    "Мику перемещалась по кружку, словно перепархивая с места на место. И перепархивания эти, при всей своей хаотичности, имели цель и завершились возле трёх одинаковых с виду инструментов."
    "Мику, поводив пальцем над прислонёнными к стене гитарами, остановилась на крайней левой, взяла её в руки, провела по струнам, удовлетворённо кивнула и вручила Семёну."
    show mi serious pioneer at right with moveinright
    mi "Это лучшее, что здесь есть. Не считая моей и Алискиной."
    show mi sad pioneer with dspr
    mi "Но пионеры даже гитарой не интересуются."
    "Жаль, что Алиса уже успела уйти, потому что она бы сразу взяла Семёна в оборот, напомнив про ночное обещание обязательно сыграть. А Мику просто стояла и смотрела, как Семён присел на табуретку, как взял несколько аккордов (тут Мику просто впилась в Семёна глазами), чтобы послушать, как звучит инструмент."
    show mi surprise pioneer with dspr
    "И тут Семён перехватил взгляд Мику."
    show d_sf serious pioneer with dspr
    me "Ну не могу же я уйти просто так."
    me "Ты же знаешь, что я отдыхал здесь раньше. Вот столько времени здесь не был, а сейчас пришёл и почему-то грустно. Наверное, потому что вырос. Правильно говорят про то, что нельзя дважды войти в одну реку."
    play music anewbeginning fadein 2
    me "Поэтому песня тоже будет невесёлая. Мелодию ты знаешь, а слова — может быть, тоже." 
    "Голос у Семёна оказался тихий, глуховатый, и Семён еле заметно картавил, что, правда, нисколько не испортило исполнение."
    show mi shocked pioneer with dspr
    $ renpy.pause (1)
    show mi normal pioneer with dspr
    "А Мику со второй строчки поняла, что да — она знает эту песню, и даже сама когда-то, неизвестно когда, но исполняла её именно на здешней сцене. Мику не смогла удержаться и, поймав взгляд Семёна, умоляюще посмотрела, дождалась его кивка, и второй куплет пела уже она."
    show mi normal pioneer at cright with move
    show dv normal pioneer at fright with moveinright
    $ renpy.pause (0.5)
    show dv surprise pioneer with dspr
    $ renpy.pause (0.5)
    show dv shocked pioneer with dspr
    $ renpy.pause (0.5)
    show dv normal pioneer with dspr
    "Всё-таки у обоих музыкантов Совёнка было чутьё и была интуиция. Потому что где-то в начале второго куплета в музыкальный кружок, сама не зная зачем, вернулась Алиса, и история повторилась, и уже новый голос подхватил третий куплет."
    show mi sad pioneer
    show dv sad pioneer
    with dspr
    $ renpy.pause (2)
    "Минутy все молчали, переживая песню."
    dv "Да… \"Никто из нас не знает ответ, где встретимся снова с тобой.\""
    show dv smile pioneer with dspr
    dv "Это что сейчас было? И почему я знаю твою манеру игры?"
    show mi shocked pioneer with dspr
    mi "Алисочка. Просто вы играете очень похоже."
    show dv normal pioneer with dspr
    dv "Да? А мне показалось, что это вы играете очень похоже."
    show mi normal pioneer with dspr
    stop music fadeout 2
    me "Девушки, это был сеанс активации генетической памяти. Можете считать, что мы с вами встречались две моих жизни назад. Спасибо, Мику. Так можно я гитару у себя подержу до воскресенья?"
    mi "Ой, да можно, конечно. Всё равно она тут никому не нужна. Только, Сенеч… Семён, поиграешь ещё? Я всё-таки хочу понять, откуда мне твоя манера знакома."
    show d_sf normal pioneer with dspr
    me "Поиграю. Приходи вечером. Все приходите."
    show mi grin pioneer with dspr
    mi "Семён. А может, выступим?"
    show d_sf smile pioneer with dspr
    me "Ага. И сорвём дискотеку."
    show dv shocked pioneer with dspr
    "Семён пробурчал тихо, про себя, но Алиса услышала и вздрогнула."
    show dv normal pioneer
    show mi normal pioneer
    show d_sf normal pioneer
    with dspr
    me "Знаешь, Мику. Я не наберу песен на концерт. Но собраться здесь, на веранде, вечером — почему нет? Или отойти подальше и костёр устроить, но лучше всё-таки собраться на веранде. Сегодня нет, а вот завтра — пожалуйста."
    hide d_sf with moveoutleft
    stop ambience
    
    scene ext_musclub_day 
    show mi normal pioneer at cright
    show dv normal pioneer at cleft
    with dissolve
    play ambience ambience_camp_center_day
    mi "Алисочка, ему даже гитару тяжело нести. Как же он ходит?"
    dv "А я знаю? Что-то там Виола делает с его спиной."
    stop ambience
    
#######################
#Глава 8. Рутина и быт#
#######################
   
label routine_:
    $ save_name = u"Дубликат. Четвертая смена - Рутина"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Рутина и быт" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene ext_dining_hall_away_day
    show d_us normal sport at center:
        ypos -0.05
    with blinds
    play ambience ambience_camp_center_day
    th "Ну и чем мне заняться? Сёмка обещал меня по лагерю поводить, а сам в музкружок улетел."
    play music music_list["timid_girl"] fadein 1
    sl "Ульяна! Подождите!"
    th "Та самая Славя. Если верить Сёмке, сейчас мы пойдём подметать площадь. Или кормить ёжиков. Или сажать цветы.\nНо как она похожа на Сашку."
    $ renpy.music.set_volume(0.2)
    show d_us hurt sport with dspr
    th "Ну да, это же и есть Сашка. Тело же одно. А я никак не привыкну."
    show d_us normal sport with dspr
    th "Только Сашка лицом серьёзнее и выглядит сдержанней и строже, что ли. Застенчивая — от Лены набралась, и командовать она не любит — её вообще лагерь особо не занимает. Танцы-соло на сцене, ночью, когда никто не видит; повозиться с мелкими, которых она делит с Сёмкой; и тот же Сёмка, через два цикла на третий — вот её интересы."
    th "А здешняя Славя — нет. Славя — хозяйка, ей лагерь как дом, а все пионеры — как младшие братья и сёстры. Причём сильно младшие. С которыми возиться не интересно, которыми нужно командовать и которых нужно опекать. А площадь-то она сама лично подметает просто потому, что в доме должен быть порядок…" 
    show d_us normal sport at right with move:
        ypos -0.05
    show sl smile2 pioneer at left with moveinleft
    $ renpy.music.set_volume(1)
    sl "Здравствуйте. Вы не могли бы мне помочь?"
    show d_us smile sport with dspr
    us_old "Славя, давай на ты. Я тебя всего на два года старше. И то, что в нашем лагере я начальник спорткомплекса, не делает меня ещё старше. Так что ты хотела?"
    show sl smile pioneer with dspr
    sl "Хорошо, на ты. Я как раз и хотела, чтобы ты помогла мне в спорткомплексе порядок навести, раз уж вы всё равно там поселились. Мы вчера с твоим Семёном начали, но не успели закончить."
    sl "А четверых мальчиков из среднего отряда для помощи и переноски тяжестей я сейчас пришлю."
    $ renpy.music.set_volume(0.1)
    hide sl
    with pixellate
    show d_us normal sport at center with move:
        ypos -0.05
    th "… А ещё она начальник по характеру, ей командовать нужно. Это не в упрёк Славе, потому что хороший администратор — человек нужный."
    th "Но где ж их взять-то, хороших, да ещё и с признаками совести? Вот Славя такая подрастает, но всё с Сёмкиных времён никак подрасти не может."
    th "А когда подрастёт, однажды случится так, что совесть у неё вступит в противоречие с долгом администратора."
    show d_us hurt sport with dspr
    th "{b}ТАК{/b}, кажется, я начинаю зависать как Семён. Заразилась. О чём я думаю вообще, мне же девятнадцать лет, а настоящих воспоминаний и того меньше?"
    th "Или память с предыдущей активной фазы? Или, как Сёмка говорил, есть ещё и чужая память? Других двойников? Оригинала? И вот она просыпается?"
    th "Бедный, как он с этим живёт?"
    show d_us normal sport at right with move:
        ypos -0.05
    $ renpy.music.set_volume(1)
    show sl smile pioneer at left with pixellate
    us_old "Присылай, буду ждать."
    stop music fadeout 2
    stop ambience
    
    scene dct_storeroom_day with squares
    "Вот так и прошёл целый час в привычных уже делах начальника спорткомплекса."
    show d_us smile sport at center with moveinright:
        ypos -0.05
    play ambience ambience_int_cabin_day
    us_old "Мальчики, спасибо большое за помощь. Больше я вас не задерживаю, отдыхайте."
    voice "Ульяна, ничего больше не нужно?"
    show d_us smile sport at left with move:
        ypos -0.05
    show d_ar normal pioneer at right with moveinright
    us_old "Спасибо…{w=0.5} Артём. Маты лежат, брусья стоят, канат и кольца висят. Пол помыт и пыль вытерта. Вроде всё."
    show d_ar sad pioneer with dspr
    d_ar "Совсем-совсем ничего?"
    show d_us laugh sport with dspr
    us_old "Совсем-совсем. Ещё раз всем спасибо."
    stop ambience
    
    scene dct_int_coaching_room2 with dspr
    play ambience ambience_int_cabin_day
    play music music_list["my_daily_life"]
    show d_us normal sport at center with moveinleft:
        ypos -0.05
    th "Раз уж начала играть в Золушку, так продолжу."
    th "Полотенца, плавки и купальник — сушиться, вещи из рюкзака — разложить по полкам в шкафу…"
    "Когда Ульяна разбирала рюкзак, из кармана в клапане выпал Выключатель."
    show d_us hurt sport with dspr
    th "Бр-р-р… Даже знать о существовании таких приборов неприятно, не то что в руки брать. А Семён ничего, терпит и таскает с собой."
    stop ambience
    
    scene dct_int_coaching_room3 with slideleft
    play ambience ambience_int_cabin_day
    show d_us normal sport at center with dissolve:
        ypos -0.05
    th "Сёмки всё нет, до обеда ещё уйма времени. Придётся работать. Что там у нас с обратным переходом?"
    "Ульяна достала из своей сумки рабочую тетрадь, ручку, план лагеря и окрестностей, логарифмическую линейку."
    "Надела стеклянный бегунок на древний артефакт. Провела пальцем по надписи, выцарапанной под движком: «А.Г.Д.»"
    "Вздохнула, вспомнила бабу Глашу."
    stop music fadeout 1
    stop ambience
    
    scene int_dining_hall_day
    show d_bg normal suit at center
    with pixellate
    play ambience ambience_dining_hall_empty
    $ prolog_time ()
    us "Глафира Денисовна. Что это за дрова? Я уж лучше на калькуляторе."
    d_gd "Калькулятор — хорошо, но доверять здешним калькуляторам не советую, особенно при {b}таких{/b} расчётах. А вот это полено — оно ещё с материка привезено, оно не подведёт."
    play sound sfx_break_cupboard
    
    scene slide_rule with squares
    #$ renpy.pause (2)
    pause
    
    scene int_dining_hall_day
    show d_bg normal suit at center
    with squares
    us "Злая вы, баба Глаша. Давайте ваше полено."
    stop ambience
    
    scene dct_int_coaching_room3 with pixellate
    play ambience ambience_int_cabin_day
    show d_us normal sport at center with dissolve:
        ypos -0.05
    $ day_time ()
    th "Значит, будем считать на \"полене\". Всё лучше, чем в столбик."
    "На столе лежал журнал мод. «Советская модница». Не то чтобы у Ульяны очень болела об этом голова, но она всё же была девочкой и, отложив в сторону тетрадь, потянулась к журналу."
    th "Спасибо, Сёмка, полистаю."
    play sound dct_sfx_pages
    "Журнал раскрылся, конечно же, на тех страницах, между которыми Семён вложил конверт с письмом. Да, тот самый конверт с письмом бабы Глаши."
    th "Сёмка придёт — спрошу. Баба Глаша не чужой мне человек."
    "Очень давно Ульяна, не задумываясь, схватилась бы за письмо: просто так, от любопытства. А сейчас повертела конверт в руках, потом, пересилив себя, отложила его в сторону и взялась за расчёты. Так и провозилась до полудня, когда пришёл Семён."
    stop ambience

    scene dct_int_coaching_room2 with dspr
    show d_sf normal pioneer at left with moveinleft
    play ambience ambience_int_cabin_day
    play sound sfx_open_door_1
    me "Рыжик, я дома."
    play music music_list["raindrops"] fadein 1
    show d_us normal sport at center with dissolve:
        zoom 0.8 xpos 0.53 ypos -0.05
    us_old "Привет, Сём. Спина болит?"
    me "Болит, Рыжик. Виола обещала, что после второго сеанса легче будет. Так что готовься: на тебя вся надежда."
    show d_us sad sport with dspr:
        zoom 0.8
    $ renpy.pause (1)
    show d_us normal sport with dspr:
        zoom 0.8
    us_old "К Мику ходил?"
    me "К ней, к болтушке нашей японской. Инструмент попросил, а заодно попытался напомнить ей и Алисе наши выкрутасы на сцене. Не знаю, что получилось. Может, и вспомнят потом. Попозже."
    us_old "А я порядок в спортзале навела по Славиной просьбе. Так что можно считать, участие в жизни лагеря мы приняли."
    me "Я заметил. Всё хорошо."
    play sound dct_sfx_slammed_book
    show d_us normal sport with dspr:
        zoom 0.8
    us_old "А обратно мы идём в воскресенье. После обеда, и даже ближе к ужину. Точку перехода я ещё не обсчитывала, но похоже, что на твоей поляне."
    me "Ну хоть топать недалеко. Лишь бы твоя сестрёнка не увязалась следить."
    "Так бы и говорили они ни о чём, но Ульяна взяла в руки конверт."
    us_old "Сёмк?"
    me "Да, Уля?"
    us_old "Ты письмо прочёл?"
    me "Прочёл, но если честно, то ничего не понял. Проблема обозначена, а остальное… Написано много и со смыслом, но уже устарело на двадцать лет."
    me "Может быть, моему оригиналу это и было бы интересно… Или тому, кем был я перед тем, как уехать из посёлка. А сейчас…"
    me "Ну узнал я, что баба Глаша — оригинал, наш Шурик, Толик и Виола — подлинники, я — дубликат, ты — скорее всего, копия, а Ольга или Сыроежкин и половина мелочи — миксы."
    show d_us hurt sport with dspr:
        zoom 0.8 
    me "Так! Я зря сейчас про копию сказал, Рыжик?"
    show d_us laugh sport with dspr:
        zoom 0.8
    us_old "Конечно, зря, Сёмк. Теперь тебе придётся мне объяснять, кто это такие и чем мы все друг от друга отличаемся. Это и мой мир, и я тоже хочу знать о нём всё. Но ты о письме говорил."
    show d_us smile sport with dspr:
        zoom 0.8
    show d_sf smile pioneer with dspr
    $ renpy.pause (1)
    show d_sf normal pioneer with dspr
    me "В общем, главная мысль в письме та, что наш мир, в котором мы живём, нестабилен. Рано или поздно всё здесь может начать сыпаться и в конце концов рухнет. Уже признаки есть."
    me "Помнишь, совершенно осеннее дерево по дороге попалось? А ведь сейчас июнь. И причина нестабильности вроде как в здешних обитателях."
    me "А что делать, баба Глаша не знает и уже не узнает, и оставляет решение нам троим, ну а теперь, получается, четверым — с тобой вместе."
    show d_sf sad pioneer with dspr
    me "Может ты, Рыжик мой, что поймёшь и подскажешь. Так что читай, а вечером нам нужно будет что-то промямлить. Потому что когда ещё все встретимся. Я бы…"
    stop music fadeout 1
    $ renpy.pause (1, hard = True)
    play sound sfx_dinner_jingle_normal
    show d_sf normal pioneer with dspr
    me "Вот так. А сейчас нас зовут. Пойдём, оценим здешнюю кухню."
    stop ambience

    scene ext_path2_day:
        walking
    show us smile sport at fleft
    with squares
    play ambience ambience_forest_day
    play sound_loop dct_sfx_running
    th "Кто молодец? Ульяна молодец."
    th "Старый лагерь — замечательное место. Зря сестрёнка куксилась."
    "Ульяна-маленькая возвращалась из Старого лагеря очень собою довольная."
    stop sound_loop
    stop ambience
    
    scene dct_ext_old_building_day with pixellate
    $ prolog_time ()
    play ambience ambience_old_camp_outside
    us "Эй, есть тут кто? Я иду!"
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    play ambience dct_ambience_creaking_floor
    us "И что? Совсем-совсем никого?"
    th "Ну нет так нет. И с чего начать? С чердака или с подвала?"
    show blink
    $ renpy.pause (3, hard = True)
    hide blink
    show unblink
    th "На крыше была, на чердаке была, на втором этаже была, по подземному ходу в комнату ходила. Шурика бы туда, он бы с приборами разобрался."
    th "Можно в лагерь возвращаться."
    play music music_list["mystery_girl_v2"]
    th "Или нельзя?"
    th "Вот надо домой, а что-то держит…"
    show blink
    $ renpy.pause (3, hard = True)
    hide blink
    show unblink
    th "Поняла! Вдруг тут живёт кто-то, а я в чужой дом забралась."
    th "Всё. Я знаю, что делать. И ещё записку оставлю."
    stop music fadeout 1
    stop ambience
    
    scene ext_path2_day:
        walking
    show us smile sport at fleft
    with pixellate
    $ day_time ()
    play ambience ambience_forest_day
    play sound_loop dct_sfx_running
    th "А жалко, что вторую дверь открыть не смогла. Что там дальше за ней? Куда-то подземный ход продолжается же!"
    stop sound_loop
    stop ambience
    
    scene ext_house_of_dv_day
    show us smile sport at left
    with squares
    play ambience ambience_camp_center_day
    us "Эй, Оксанка, я к обеду не опоздала?"
    show d_oz normal pioneer at cright with moveinright:
        yalign 0.2
    d_oz "Нет, Ульяна, ещё переодеться успеешь."
    us "Ага, спасибо."
    hide d_oz with moveoutright
    stop ambience
    
    scene int_house_of_dv_day with dspr
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    play music music_list["went_fishing_caught_a_girl"]
    show us smile sport at cright with moveinright
    th "Вот теперь я знаю, чем займусь остаток смены."
    th "А Алиске точно ничего не скажу. Прости, подруга, но на то место у меня свои планы. Может быть, когда-нибудь потом."
    th "Так. Надо записать всё, что узнала, и всё, что сделала. И план продумать."
    "Несмотря на темперамент и детскую ещё нетерпеливость, девочка умела и строить планы, и выполнять их."
    "Вот и сейчас, проведя полдня в Старом лагере и избавившись от украденной ватрушки, яблока и половины кулька конфет, она принесла назад несколько страниц, вырванных утром из Алисиной тетради со стихами. Когда-то чистых, а сейчас исчирканных записями, схемами и рисунками."
    "Ещё несколько страниц было оставлено в Старом лагере."
    "А ещё нужно было осмыслить всё это найденное богатство."
    show us normal sport with dspr
    play sound sfx_dinner_jingle_normal
    th "Вот уже и обед. Как я вовремя. Сейчас, только переоденусь и конфеты спрячу."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day
    show un normal pioneer far
    with squares
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_running fadein 1
    $ renpy.pause (0.5)
    show us smile pioneer close at cleft with moveinleft
    show un shocked pioneer far with dspr
    stop sound_loop
    $ renpy.pause (1)
    play sound_loop dct_sfx_running
    hide us with moveoutright
    stop sound_loop fadeout 1
    show un normal pioneer far with dspr
    th "Приключения приключениями, а обед по расписанию."
    show un smile pioneer with dspr
    th "От самого завтрака в лагере было необычно тихо и спокойно. Интересно, где же Ульянка пропадала?"
    show un normal pioneer with dspr
    th "Пора и мне. Только книжку домой отнесу"
    show un grin pioneer with dspr
    th "Представляю, что будет, если я сдам книжку со следами рассольника. Бедная Женя и бедная я."
    stop ambience
    
    scene ext_houses_day
    show un normal pioneer
    with dissolve
    play ambience ambience_camp_center_day
    play music music_list["two_glasses_of_melancholy"]
    un "Здравствуйте, Ольга Дмитриевна."
    show mt normal pioneer at right with moveinleft
    mt "Здравствуй, Лена. На обед не опаздывай."
    un "Уже иду. Только книжку занесу."
    hide mt with moveoutright
    stop ambience

    scene ext_house_of_un_day
    show un normal pioneer at right
    with dissolve
    play ambience ambience_camp_center_day
    $ renpy.pause (0.5)
    show un shy pioneer with dspr
    un "Здравствуйте."
    show d_sf normal pioneer at fleft
    show d_us smile sport at cleft
    with moveinleft
    me "Здравствуй."
    us_old "Привет, Лена."
    play sound dct_sfx_steps2
    hide d_sf
    hide d_us
    with moveoutright
    stop sound fadeout 3
    us_old "Сёмк, не забудь. Расскажешь мне, кто такие копии и дубликаты."
    me "Расскажу, но лучше у Виолы спросить. Я сам-то почти ничего не помню."
    show un surprise pioneer at center with move
    th "Что такое дубликат — я представляю, но вот КТО такие дубликаты?.."
    stop music fadeout 2
    th "Самое интересное — я чувствую, что знаю ответ. Как-будто читала когда-то, но успешно забыла."
    show un grin pioneer with dspr
    th "Как забыла, как решать квадратные уравнения. Не нужно было, вот и забыла."
    stop ambience
    
    show int_house_of_un_day
    show mi smile pioneer at right
    with dspr
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_campus_1
    show un normal pioneer at left with moveinleft
    mi "Здравствуй, Леночка. Ты на обед сейчас, или у тебя какие-то ещё дела? Если на обед, то пойдём вместе?"
    hide mi with dspr
    hide un
    show un normal pioneer
    with dissolve
    th "Микс, первый удачный микс."
    th "Стоп! О чём это я?"
    hide un
    show un normal pioneer at left
    show mi normal pioneer at right
    with dissolve
    un "Да, то есть нет, Мику. Нет никаких дел, зашла только книжку положить."
    stop ambience
    
    scene ext_house_of_un_day with dspr
    show un normal pioneer with dissolve
    play ambience ambience_camp_center_day
    th "Как я только что Мику назвала?"
    show un shocked pioneer with dspr
    th "Не могу вспомнить."
    hide un
    play sound sfx_close_door_1
    show un normal pioneer at left
    show mi normal pioneer
    with dissolve
    mi "Я готова, Леночка. Идём."
    stop ambience
    
    scene ext_houses_day:
        walking
    show un normal pioneer at left
    show mi normal pioneer
    with dissolve
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_steps2
    show d_oz normal pioneer with easeinright:
        yalign .12
    hide d_oz with easeoutleft
    play sound dct_sfx_running
    show d_sz normal pioneer with easeinright:
        yalign .12
    hide d_sz with easeoutleft
    play music music_list["so_good_to_be_careless"]
    show mi smile pioneer with dspr
    mi "Хорошо, что они маленькие. Правда, Леночка? А то затоптали бы."
    show mi surprise pioneer with dspr
    mi "А знаешь, Леночка, кто ко мне сегодня в кружок приходил? Семён, тот, что у нас лагере гостит."
    show mi happy pioneer with dspr
    mi "Представляешь, Леночка, он, оказывается, на гитаре играет."
    show mi upset pioneer with dspr
    mi "Он играет, конечно, средне, но терпеть можно."
    show mi sad pioneer with dspr
    mi "А вот пионеры, Леночка — они вообще никак и ни на чём играют, и не хотят учиться."
    show mi smile pioneer with dspr
    mi "А ещё, Леночка, ты знаешь, что Семён…"
    show un serious pioneer with dspr
    un "Мику."
    show mi serious pioneer with dspr
    mi "Да, Леночка."
    un "У меня такое впечатление, что Семён как минимум понравился всем девочкам в лагере. Начиная от Оксаны и заканчивая Ольгой Дмитриевной."
    show un grin pioneer with dspr
    un "И мы с тобой тоже в этом списке."
    show mi laugh pioneer with dspr
    mi "Жаль, что он так влюблён в свою рыжую. Всё время ищет её глазами."
    show mi smile pioneer with dspr
    show un smile pioneer with dspr
    mi "Не знаю как у тебя, Леночка, а и у меня, и у Алисы, и у нашей Ульянки такое чувство, будто все мы его давно знаем, причём с хорошей стороны."
    show mi normal pioneer with dspr
    mi "Знаешь, он, пока был у меня в кружке, всё время посматривал на то место, где должна висеть пятая портьера, которой не хватает."
    show mi upset pioneer with dspr
    mi "Мне было так неудобно, будто это я виновата, что их только четыре."
    stop music fadeout 1
    stop sound_loop
    stop ambience

    show dct_ext_dining_door_day:
        zoom 0.625
    show mt normal pioneer at right
    with squares
    "Ольга Дмитриевна стояла на крыльце столовой. Кивнула Виоле с подопечным Толиком, улыбнулась гостям — Семёну и Ульяне-большой."
    play ambience ambience_camp_center_day
    mt "Ульяна, спасибо за помощь в спортзале."
    # hide mt
    # show mt normal pioneer at left
    # with dissolve
    # show d_us laugh sport at right with moveinright:
        # ypos -0.05
    show d_us laugh sport at cleft:
        xzoom -1 ypos -0.05
    show d_us_sport_mirror at cleft:
        xzoom -1 ypos -0.05
    with dissolve
    us_old "Радастартьсятоварщвожатая!"
    show d_us smile sport with dspr
    us_old "Только ваши мальчики всю работу сделали, я лишь показывала, что и куда. Особенно, {w=1}особенно Артём. Отметьте его как-нибудь, пожалуйста. А то я только спасибо сказать могу."
    show mt smile pioneer with dspr
    mt "Я запомнила. Артём."
    us_old "А что вы тут стоите? Не хотите обедать?"
    mt "Всего лишь долг вожатой, не более. Вы идите, Ульяна, не ждите меня. Я сейчас всех запущу и тоже зайду."
    us_old "Тогда мы вас ждём."
    hide d_us
    hide d_us_sport_mirror
    with dissolve
    th "Пятый день смены без происшествий прожит до середины. Уже хорошо."
    stop ambience

###################
#Глава 9. Прогулка#
###################
   
label promenade_:
    $ save_name = u"Дубликат. Четвертая смена - Прогулка"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Прогулка" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene int_dining_hall_people_day with blinds
    $ day_time ()
    play ambience ambience_dining_hall_full
    show mt normal pioneer with moveinleft
    mt "Все здесь?"
    voices "Все. Все!"
    mt "Вот и хорошо."
    show mt smile pioneer with dspr
    mt "А кто не успел на обед, тот опоздал."
    hide mt with moveoutright
        
    show sl normal pioneer close at left with dissolve:
        ypos 0.2
    show mt normal pioneer at right with moveinright
    show mt normal pioneer close with dspr
    play sound dct_sfx_chair
    show mt normal pioneer close at right with move:
        ypos 0.2
    mt "Приятного аппетита. Можно?"
    show sl smile pioneer close with dspr
    sl "Спасибо, Ольга Дмитриевна. Конечно."
    show sl normal pioneer close with dspr
    "Вожатая не пошла за столик администрации, а подсела к своей помощнице."
    "Некоторое время обедали молча. Обе — и вожатая, и её помощница — отсутствием аппетита не страдали и предпочли сначала утолить первый голод, а потом уже говорить о делах."
    show blinking
    $ renpy.pause (1)
    play music music_list["timid_girl"]
    mt "Послезавтра по плану спортивный праздник. Есть какие-нибудь идеи?"
    sl "Нет пока, Ольга Дмитриевна. Но я что-нибудь придумаю. А если у вас из методичек списать? Или из «Вожатого»?"
    show mt sad pioneer close with dspr
    mt "Понимаешь. Хотелось, чтобы что-нибудь оригинальное было. Чтобы одновременно и по плану, и не как у всех."
    show mt normal pioneer close with dspr
    sl "А может, у гостей помощи попросить, Ольга Дмитриевна? Они, говорят, оба непростые: он — физрук, она — начальник спорткомплекса."
    show sl shy pioneer close with dspr
    sl "Только мне неудобно будет, я уже Ульяну один раз просила о помощи."
    show sl normal pioneer close with dspr
    show mt surprise pioneer close with dspr
    mt "Физрук? Что же мне Виола тогда…"
    show mt normal pioneer close with dspr
    mt "Ладно, я сама спрошу."
    mt "Так и поступим. Славя, тебе есть чем ещё заняться. Потом, если что, подключу."
    stop music fadeout 1
    stop ambience

    scene ext_path_day with squares
    play ambience ambience_forest_day
    play music buddy
    show d_sf normal pioneer at fleft
    show d_us normal sport at cleft:
        ypos -0.05
    with moveinleft
    me "Нам по тропинке. Вдоль забора и к остановке."
    me "Подожди, Уля, а то сейчас затопчут."
    play sound_loop dct_sfx_running
    show us normal sport at right with easeinright:
        running
    us "Привет!"
    hide us with easeoutright
    stop sound_loop
    show d_sf laugh pioneer
    show d_us smile sport
    with dspr
    me "Ульян, ночевать-то придёшь?!"
    show us smile sport far with easeinright:
        xpos 0.85
    us "Я ещё подумаю!"
    hide us with easeoutright
    me "Ну хотя бы подумает."
    me "Заметила? Карманы оттопырены, в руках пакет. Половину продовольственного склада твоя сестрёнка обчистила."
    us_old "А ты бинокль у неё на пузе заметил? Обязательно на крышу полезет."
    stop music fadeout 1
    show d_us sad sport with dspr
    us_old "А я вот в её возрасте не догадалась."
    stop ambience
    
    scene dct_ext_old_building_day with squares
    play ambience ambience_old_camp_outside
    show us normal sport at right with moveinright
    $ renpy.pause (1)
    hide us with dspr
    $ set_mode_nvl ()
    "Ульяна-маленькая же, добежав до старого корпуса, выгрузила на стол в бывшем кабинете начальника лагеря содержимое своих карманов."
    "Конфеты-батончики «Волейбол» — полпакета; яблоки средние зелёные — две штуки; ватрушки с творогом, остававшиеся в столовой от завтрака — две штуки; лимонад «Буратино» — одна бутылка; расчёска — одна штука."
    "Посмотрела на образовавшуюся кучку. Удивилась сама себе: как только донесла? И действительно полезла на крышу."
    play music anewbeginning fadein 2
    "Пока наконец не оказалась на самом коньке. Посидела на корточках, привыкая, медленно встала на ноги огляделась поверх деревьев и потянула с шеи бинокль."
    "Никто и никогда ещё не смотрел в бинокль на эту искрящуюся на солнце реку и нитку моста над ней, не ловил золотую искру на макушке Генды."
    "Никто не видел бесконечного леса, начинающегося за лагерем: сперва светлая зелень листвы, дальше — отдельные острова темной хвои, ещё дальше — острова сливаются в сплошной хвойный массив до самого горизонта."
    "Поля, разрезанные пополам узкой и прихотливо извилистой лентой шоссе. Лагерь, стоящий на стыке леса, реки и полей."
    "Автобусная остановка перед воротами и Мику, танцующая с метлой в руках на этой остановке."
    "Гости лагеря, идущие по шоссе к остановке. И вот сейчас они и Мику увидят друг друга."
    $ set_mode_adv ()
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day
    show mi normal pioneer
    with pixellate
    $ prolog_time ()
    play ambience ambience_camp_center_day
    mt "Хатсуне, стоять-бояться!"
    "Мику, на своё несчастье, пробегала мимо столовой в тот самый момент, когда оттуда вышла вожатая."
    hide mi
    show mi upset pioneer at right
    with dspr
    show mt normal pioneer at left with dspr
    mt "Хатсуне! Что у тебя сегодня по графику?"
    mt "Впрочем, неважно. Нужно подмести остановку, а Славе некогда. Сейчас получишь у неё на складе метлу и вперёд."
    hide mt with moveoutleft
    "Ольга Дмитриевна поймала очередную жертву, поставила перед той задачу и ушла, не слушая возражений."
    stop ambience
    
    scene ext_camp_entrance_day with pixellate
    $ day_time ()
    play ambience ambience_camp_entrance_day
    play music music_list["miku_song_flute"]
    show mi dontlike pioneer with moveinright
    $ renpy.pause (0.5)
    hide mi with moveoutleft
    $ set_mode_nvl ()
    "И вот Мику пришлось вместо прохладного кружка идти разминаться с метлой на солнцепёке автобусной остановки."
    "Сперва честно подметала, потом от скуки представила себя ведьмой на помеле, потом попыталась вообразить танец ведьмы: в этом лагере не было Саши, и здешней Мику, чтобы заполнить вакуум, система когда-то добавила хореографический талант."
    "В общем, когда танец закончился, на остановке обнаружились двое зрителей — гости."
    $ set_mode_adv ()
    show mi smile pioneer with moveinleft
    voice "Мику, нам очень понравилось. Это была самая весёлая ведьмочка на свете."
    show mi upset pioneer with dspr
    stop music
    $ renpy.pause (0.5)
        
    scene ext_no_bus
    show d_sf normal pioneer at left
    show d_us smile sport at cleft:
        ypos -0.05
    with slideleft
    $ renpy.pause (1)
    
    scene ext_camp_entrance_day
    show mi smile pioneer
    with slideright
    mi "Здравствуй, Сене…{w} Сем…{w} Ну не могу я! Ульяночка, можно мне твоего мужа звать Сенечкой?"
    
    scene ext_no_bus
    show d_sf normal pioneer at left
    show d_us smile sport at cleft:
        ypos -0.05
    with slideleft
    show d_us laugh sport with dspr
    us_old "Ну что с тобой делать, Мику? Зови, если иначе не получается. А то я все Сёмкой и Сёмкой. И Занудой ещё иногда."
    show d_sf serious pioneer with dspr
    "Мнением Семёна девушки не интересовались. А Семён опять вздрогнул. Нет, в его лагере Мику тоже, бывало, звала его Сенечкой, но там Семён к этому привык и не реагировал. А тут каждый раз как будто что-то простреливало в голове. Что-то, что он не успевал отследить."
    "Вот и сейчас. Что-то, какой-то образ мелькнул и исчез."
    play music cambo_coffee fadein 2
    show d_sf smile pioneer with dspr
    me "Иногда? Я понял, спасибо, любимая. Два раза в час — это значит «иногда»."
    $ set_mode_nvl ()
    "И понеслась… Семён и Ульяна-большая откровенно наслаждались этой пикировкой."
    "А Мику сначала испугалась того, что стала причиной семейного скандала, а потом положила метлу на асфальт, отошла к остановке, присев там на деревянную скамейку (два вкопанных в землю обрезка бревна и доска между ними)."
    "И так же, как Персуновы только что любовались её танцем, стала любоваться спектаклем. А то, что эта перепалка была именно спектаклем, не было никаких сомнений."
    $ set_mode_adv ()
    stop music fadeout 1
    show mi smile pioneer at right with moveinright
    mi "Ребята, может…{w=2} пьесу какую поставим, пока вы здесь? Хотя…{w=1} вы же в субботу уйдёте?"
    me "В воскресенье после обеда, Мику. Но всё равно толком ничего не успеем, а халтурить не хочется…"
    "Семёна после дня Нептуна уже ничего не пугало, а Мику очень обидно было ощущать свою бесполезность в лагере. Так и родился этот диалог."
    us_old "Мику, ты закончила здесь? А то мы помочь можем."
    mi "Нет, ребята, спасибо. Я уже всё."
    hide mi with moveoutleft
    "Мику спрятала метлу за гипсового пионера, улыбнулась гостям и упорхала. А гости пошли дальше, мимо клубов на площадь."
    stop ambience

    scene ext_clubs_day
    show d_sf normal pioneer at left
    show d_us smile sport at cleft:
        ypos -0.05
    with slideright
    play ambience ambience_camp_center_day
    me "Вот такой вот она человечек — Мику. Во всех лагерях, где я побывал."
    us_old "Только, Сёмк. Она чуть другая, не такая как наша. Если не знать, то не отличить. А вот если есть с кем сравнить, то есть разница."
    me "Разница, конечно, чувствуется, но всё равно никогда и нигде ничего, кроме позитивной улыбки, не вызывает. Хотя это её надо понять и к ней надо привыкнуть."
    me "А пока не привыкнешь, общаться с Мику, конечно, утомительно. Но это ты и сама знаешь."
    stop ambience

    scene ext_houses_day
    show d_sf normal pioneer at left
    show d_us normal sport at cleft:
        ypos -0.05
    with slideright
    play ambience ambience_camp_center_day
    play music music_list["dance_of_fireflies"]
    "Персуновы гуляли по лагерю до ужина, повторяя маршруты Семёна и проходя по памятным ему местам, и под Семёновы же комментарии."
    me "А вот здесь, на этом перекрёстке, в день моего приезда Алиса всегда хлопала меня по плечу, и её всегдашняя реплика была: \"Челюсть с пола подними\"."
    show d_us laugh sport with dspr
    us_old "Похоже на Рыжую."
    show d_us normal sport with dspr
    us_old "Сёмк. У тебя на лице знаешь что написано? \"Зачем это ей нужно?\" — вот что."
    show d_sf serious pioneer
    show d_us hurt sport
    with dspr
    me "Уля, я…"
    us_old "Не мешай."
    us_old "Понимаешь, Сёмка. Меня-то ты знаешь, можно сказать, с пелёнок. Говорят, что в женщине должна быть загадка, а я у себя для тебя даже никакой загадки не оставила. А тебя я тоже хочу знать, чем больше, тем лучше."
    me "С пелёнок, говоришь? Почему ты тогда мне приснилась уже взрослая, даже чуть постарше, чем сейчас, в городе, которого нет? Когда тебе в лагере было «почти четырнадцать». И до сих пор там и такая снишься? Так что не беспокойся, есть в тебе загадки."
    stop music fadeout 1
    stop ambience
    
    scene ext_playground_day
    show d_sf normal pioneer at left
    show d_us normal sport at cleft:
        ypos -0.05
    with squares
    play ambience ambience_soccer_play_background
    "Уже перед дверями спортзала гости столкнулись с уставшей загорать и купаться вожатой."
    show mt normal panama pioneer at right with moveinright
    us_old "Здравствуйте, Ольга Дмитриевна."
    show mt grin panama pioneer with dspr
    mt "Семён, Ульяна — давайте, пожалуйста, без отчества и на ты."
    show mt normal panama pioneer with dspr
    mt "Мне нужен ваш совет. В плане мероприятий на смену у меня стоит спортивный праздник, но не хочется обыденности, вдруг захотелось оригинального. Может, вы мне что подскажете?"
    us_old "Ольга Дми… Оля, времени мало что-то всерьёз менять, но мы подумаем, чем можно помочь."
    stop ambience

    scene int_house_of_un_day with squares
    play ambience ambience_int_cabin_day
    "Мику, вернувшись с остановки в домик, достала из чемодана тетрадку, уселась за стол и наморщила лоб."
    play sound sfx_close_door_campus_1
    play music dreamers_of_the_day
    show mi angry pioneer with moveinleft
    th "Рассчитывать можно только на себя, обеих Ульян, Семёна и Славю, да и то Славя пойдёт исключительно из чувства долга."
    th "Можно уговорить Алису, но это пятьдесят на пятьдесят."
    th "Но всё равно я это напишу. Я не могу больше терпеть!"
    "Ещё не сложившиеся в слова буквы рвались наружу и не давали больше ни о чём другом думать."
    "Мику погрызла колпачок ручки, посмотрела в окно на лес, посмотрела на акварель над Лениной кроватью. И с силой нажимая на стержень так, что едва не рвалась бумага, вывела заголовок на первой строке первой чистой страницы: «Костёр», и чуть ниже: «Действующие лица»."
    "Надо было поспешать: если Мику хотела поставить спектакль до того, как гости покинут лагерь, то надо было успеть написать текст до вечера."
    hide mi with moveoutright
    play sound sfx_dinner_jingle_normal
    "Так её и застала Лена, пришедшая положить книжку перед ужином: яростно строчащую в тетрадке, перечитывающую, вымарывающую не понравившиеся слова и предложения или даже вырывающую страницы целиком, тихо ругающуюся или тихо хвалящую саму себя по поводу качества написанного."
    "Лена подняла несколько вырванных страниц, почитала."
    play sound sfx_close_door_1
    show un serious pioneer with dspr
    un "Мику, я сейчас принесу тебе ужин. Не отвлекайся."
    stop music fadeout 1
    stop ambience
    
################################
#Глава 10. Трещины в мироздании#
################################
   
label cracks_:
    $ save_name = u"Дубликат. Четвертая смена - Трещины в мироздании"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Трещины в мироздании" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    
    
    scene dct_int_aidpost_sunset with blinds
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_medstation_inside_day
    show cs normal glasses with moveinright
    cs "Так, хорошо. А следующую куда?"
    cs "Нет-нет-нет. Смотри внимательней. Всё же на картинках есть."
    cs "Правильно. Ну, бери иглу и уже сама. Стой! Вот так иглу держат."
    "А Ульяна боялась. На грани паники. Нужно было вводить иглы в Семёна, а она боялась и каждый раз замирала, прежде чем коснуться иглой его кожи."
    "Но понимал это только Семён: просто чувствовал, как дрожит игла в момент касания."
    "Поэтому, когда всё закончилось, а спина его украсилась двумя рядами проволочных шипов, Семён осторожно повернул голову, поймал взгляд Ульяны и сказал ей одними глазами: «Ты молодец, Рыжик»."
    "Виола осторожно накрыла Семёна простынёй, перевернула песочные часы и уселась, развернув стул спинкой к столу. Приглашающе кивнула Ульяне: садись, мол, хоть на вторую кушетку."
    cs "Семён, тебя в сон не клонит? Нет? Это хорошо. Тогда можно и поговорить, если готов. Тебя, Ульяна, это тоже касается."
    stop ambience

    scene ext_house_of_un_day with squares:
        zoom 1.2
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show mi sad pioneer at left with dspr
    "Мику умела работать очень быстро, поэтому, когда Лена вернулась, принеся ужин, основная часть текста была уже написана, раскрытая тетрадка лежала на кровати, а Мику сидела на крыльце, глядя куда-то в пространство."
    show un normal pioneer with moveinright
    $ renpy.pause (0.5)
    stop ambience
    
    scene int_house_of_un_day with dspr
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    show un normal pioneer with moveinleft
    "Леночка занесла в домик судок с макаронами по-флотски и термос с чаем, коснулась рукой тетрадки, но без разрешения автора читать не решилась, а вместо этого вышла наружу и присела рядом с соседкой."
    stop ambience

    scene ext_house_of_un_day:
        zoom 1.2
    show mi sad pioneer at left
    with dspr
    play ambience ambience_camp_center_day
    $ renpy.pause (0.5)
    play sound sfx_close_door_campus_1
    show un normal pioneer at right with dspr
    $ renpy.pause (0.5)
    show mi normal pioneer with dspr
    un "Я тебе ужин принесла, Мику. Ешь, пока не остыл."
    mi "Спасибо, Леночка, я заметила."
    mi "Я сейчас."
    mi "Что-то вымотал меня этот четырёхчасовой марафон."
    mi "Никогда раньше столько не писала."
    mi "А тут вдруг как накатило."
    mi "Я и остановиться не могла."
    mi "Пока всё не закончила."
    "Мику действительно вымоталась. Это было заметно даже по тому, что говорила она непривычно медленно и короткими фразами, как будто с трудом подбирая слова, как будто все слова были истрачены на написание текста и сейчас их запас ещё не успел восстановиться."
    "Девушки одновременно поднялись. Чуть замешкавшись в дверях, пропуская одна другую, зашли в домик."
    stop ambience
    
    scene int_house_of_un_day with dspr
    play ambience ambience_int_cabin_day
    play music anewbeginning fadein 3
    show mi normal pioneer at right with moveinleft
    play sound sfx_close_door_1
    show un normal pioneer at left with moveinleft
    un "Мику, я почитаю пока?"
    mi "Конечно, Леночка. Я же для этого и писала."
    "Мику, постепенно приходя в себя, занялась ужином, а Лена устроилась у себя на кровати со свеженаписанной пьесой."
    mi "Ну и как, Леночка? Я писала, писала… Всё что приходило в голову."
    show mi serious pioneer with dspr
    mi "Остановлюсь, перечитаю всё что написала, что-то поправлю и дальше пишу. Как так можно?"
    mi "Говорят, что нужно сперва сюжет придумать, план написать, характеры прописать. А я ничего этого не сделала, потому что не умею."
    show mi sad pioneer with dspr
    mi "Я играть музыку и петь умею, а книги писать — нет. А ещё запятые не ставлю и не те буквы в словах пишу. Потому что папа научил меня хорошо говорить по-русски, но не научил по-русски хорошо писать."
    show mi shy pioneer with dspr
    mi "А если бы я по-японски писала, и пьеса получилась бы совсем другая, и никто не смог бы её прочесть. Её по-русски нужно было писать, чтобы получилось то, что я хочу. Вот я и писала по-русски…"
    "Мику ждала Лениной оценки и отчаянно волновалась. Впервые она написала что-то серьёзнее школьного сочинения. Впервые она придумала что-то."
    "Система и создатели наградили её способностями к музыке, вокалу, танцам, и всё это воспринималось обитателями как должное и было для здешнего мира естественно."
    "А тут впервые Мику сделала что-то такое, что не было ей подарено извне, что-то, что вышло изнутри неё ценой нервных клеток, ценой зверского голода, ценой головной боли и жуткой опустошённости. Что-то такое, что она довела до конца."
    "Впервые один из обитателей бесконечного лета придумал, создал, довёл до конца и представил на суд других что-то действительно новое, чего не было раньше."
    "И мир бесконечного лета ещё чуть-чуть изменился."
    un "Мику. Если хочешь, я могу помочь с запятыми. Скажи, ты ведь собираешься показать это Семёну? Ты ведь о нём это написала?"
    show mi normal pioneer with dspr
    mi "Да, Леночка. Сегодня Семён приходил за гитарой, а мы с Алисой после поговорили о гостях."
    mi "Как они рассказали Алисе и нашей Ульяне сказку про пионеров, которые всё время проживали одну и ту же смену по кругу, так что никто ничего не помнил, а один мальчик всё вспомнил, но начал расти."
    mi "Алиса пересказала её мне, а ещё рассказала про то, какой сон Ульяне приснился и как Алиса сама представила себе, что она стоит на берегу, а Семён уплывает на лодке. И вот я всё это объединила. Просто так представила себе, что это всё про нас и всё это было на самом деле."
    show mi serious pioneer with dspr
    mi "Хочу ли я Семёну это показать? Нет, в таком виде не хочу."
    "Мику катастрофически не с кем было посоветоваться. Ей был симпатичен Семён, но она не решалась подходить к нему с такой просьбой. Оставалась Лена, для моральной поддержки."
    mi "Леночка, я хочу поставить это на сцене. И хочу, чтобы гости это увидели. Хочу, чтобы все увидели, но и гости тоже. Но я понимаю, что могу не успеть, что времени только до вечера субботы."
    show un serious pioneer with dspr
    un "Вот что, Мику. Пошли в библиотеку."
    stop music fadeout 1
    "В библиотеке, кроме всего прочего, была пишущая машинка, к которой прилагалась Женя. Обе — заведующая библиотекой и руководитель музыкального кружка — всегда несколько пугали друг друга, но деваться им было некуда, тем более что текст был хорош."
    stop ambience

    scene dct_ext_aidpost_night_with_light with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinright
    us_old "Сёмк, неохота к себе сразу возвращаться. Давай ещё погуляем."
    me "Я музыкантш наших в гости зазывал, но их, похоже, не будет. Мику и за ужином не было, её порцию Лена в домик унесла. А Алиса задумчивая какая-то ходит."
    "Семён поймал удивлённый взгляд Ульяны."
    me "Чёрт! Наших, местных, тутошних, тамошних, здешних… Я запутался с этими двойниками, Уля. Конечно, здешних."
    me "Так что давай. Начнём от площади?"
    "Оба прокручивали в головах разговор с Виолой и Толиком, который никому ничего толком не дал."
    stop ambience

    scene int_aidpost_night with pixellate
    $ persistent.sprite_time = "day"
    $ prolog_time ()
    play ambience ambience_medstation_inside_night
    play music music_list["afterword"]
    show d_sf normal hike at right with moveinright
    me "Ну и к чему мы пришли? К тому, с чего начали."
    show cs normal glasses at left with moveinleft
    cs "Ну да, мир меняется и трещит. И причины этому — обитатели, выпадающие из циклов, и влияние извне. Но об этом ещё бабуля писала."
    show d_sf normal hike with move:
        xpos 0.9
    show d_us hurt dress at right with moveinright:
        ypos -0.05
    us_old "Виола. У вас в узле двое на подходе. Выключатель… Вы же не будете? Им?.."
    show cs normal glasses with move:
        xpos 0.1
    show d_to normal pioneer at left with moveinleft
    d_to "Не будем, Уля, не бойся. Я тоже против."
    d_to "Да, и не забывай. Что это как маятник. Чем больше спящих пионеров, тем меньше этот мир защищён от воздействия снаружи. Чем больше проснувшихся, тем больше он расшатывается изнутри."
    show d_us normal dress with dspr
    us_old "Я возьму тогда тетради Глафиры Денисовны? Вдруг разберусь."
    show d_to normal pioneer with move:
        xpos 0.1
    show cs normal glasses at left with move
    cs "Бери. Если успеешь до вашего ухода. Всё равно в цифрах лучше тебя никто не разберётся. Есть ещё Шурик из вашего узла, но он, сами понимаете…"
    show d_us normal dress with move:
        pos (0.9, -0.05)
    show d_sf normal hike at right with move
    me "А что там случилось двадцать лет назад с Шуриком? Или нам лучше не знать?"
    show cs normal glasses with move:
        xpos 0.1
    show d_to normal pioneer at left with move
    d_to "Наверное, лучше знать. Чтобы не навредить ему ненароком. Тем более что тогда ты был в курсе. Все мы были в курсе."
    d_to "Ты же помнишь, что такое было самое начало девяностых? Резня и война на окраинах бывшего Союза."
    d_to "А у Шурика, у Шурика-оригинала, были жена и дочка. Яна и Яна. Были. А потом уже нет."
    d_to "Поэтому он и оставался здесь, поэтому он и полез тушить пожар на маяке. Он же не знал, что уцелеет и Виола успеет отправить его в туман, а из тумана выйдет подлинник."
    d_to "Был Шурик-оригинал, а стал Шурик-подлинник, но какая разница? Даже на нашей аппаратуре было не отличить. Особенно если оригинал при этом, так или иначе, всегда погибает."
    d_to "Сразу, как в нашем с ним случае, или через пару месяцев, как в случае с Виолой. Потому он и собрал у себя в кружке упрощённый аналог Выключателя. Потому и бьёт себе по мозгам каждый цикл, чтобы не вспоминать."
    me "Понятно. Однажды я успел его поймать до того, как он в очередной раз стёр сам себя, и спросил только: «Почему?». А он ответил, что настоящий Александр давно умер, и не надо пытаться его вернуть, а надо дать шанс настоящему хозяину этого тела."
    d_to "Надо что-то решать. Время у нас ещё есть, но нельзя затягивать."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_houses_night with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with dspr
    me "Вот, значит, как оно было. Никогда бы не подумал про Виолу."
    us_old "Ты о чём, Сём?"
    me "Да сны мне снились и продолжают сниться, как Виола в туман уходит и возвращается. А потом ещё троих человек в туман отправляет, и я теперь знаю, кого. И баба Глаша намекала, только я тогда её не понял."
    us_old "То есть наша Виола — это…"
    me "Да, Рыжик. Она не совсем настоящая, как и мы с тобой. Только она — подлинник. То же самое, что и оригинал. Я их видел вдвоём: оригинала и её. Только не понимал, что происходит. Действительно, как один человек."
    me "Но подлинник или оригинал — хуже она от этого не стала."
    us_old "Вот, кстати, о Виоле. Сёмк, ведь лучше тебе стало. Я же видела, каким ты шёл в медпункт вчера, каким ты шёл туда сегодня и каким ты вышел оттуда."
    show d_sf smile hike with dspr
    me "Рыжик, у тебя лёгкая рука. Завтра ещё сеанс, и буду лучше чем был."
    show d_us hurt dress with dspr
    us_old "Ага, а знаешь, как я боялась."
    me "Замечательно быть здоровым. Рыжик, может послезавтра по волейболу? Вот и ответ на вопрос вожатой. Как вариант, а? Свисток с собой?"
    show d_us smile dress with dspr
    us_old "Скучаешь? Я тоже. Два дня не играли, а я уже скучаю. А вожатой не понравится такой ответ. Ей же оригинального хочется. Но если ничего другого не будет, она согласится."
    show d_sf normal hike with dspr
    stop ambience
    
    scene ext_square_night with slideleft
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinright
    me "Странно. Лены на площади нет."
    us_old "Странно? Сёмк?"
    me "Странно, конечно. Маргарет Митчелл сама себя не прочитает."
    stop ambience
    
    scene ext_house_of_dv_night with slideleft
    play ambience ambience_camp_center_night
    $ renpy.music.set_volume(0.05)
    play music higekitekina
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinright
    us_old "Слышишь? Алиса не спит, играет на гитаре. Сестрёнку мою ждёт — на крыльце одна пара обуви, Алисина."
    us_old "Зайдём, Сём?"
    me "Может, завтра, Уля? А то получится, что я разбираться пришёл, почему на приглашение не откликнулась."
    stop music
    $ renpy.music.set_volume(1)
    stop ambience
    
    scene dct_ext_houses_night with slideleft
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinright
    $ renpy.pause (0.5)
    play sound dct_sfx_running
    show us normal sport with moveinleft:
        running
    us "Привет, вы к клубам? Занесите бинокль кибернетикам, я обещала сегодня вернуть! Пожалуйста!"
    hide us with moveoutright
    me "Ну всё, показала ты мелкой дорогу. Теперь до конца смены девочка будет занята, а вожатая будет скучать."
    stop ambience
    
    scene ext_clubs_night with slideleft
    play ambience ambience_camp_center_night
    show sh normal pioneer with dspr
    me "Шурик, подожди, не убегай! Мелкая тебе бинокль передала."
    show sh surprise pioneer with dspr
    sh "Ульяна, Семён, добрый вечер. И спасибо."
    us_old "Шурик, можно спросить? За что у вас моя сестрёнка бинокль купила?"
    show sh laugh pioneer with dspr
    sh "За обещание не приближаться к клубам ближе чем на двадцать метров."
    sh "Врёт, конечно."
    me "Конечно, врёт. Спокойной ночи."
    show sh normal pioneer with dspr
    sh "Спокойной ночи."
    hide sh with moveoutright
    stop ambience
    
    scene dct_ext_musclub_night with squares
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinleft
    $ renpy.pause (1)
    stop ambience
    
    scene dct_ext_house_of_un_night with slideright
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinleft
    me "Хм. Мику и в кружке нет, и домик пустой."
    me "Неудобно окажется, если она как раз сейчас к нам стучится."
    stop ambience

    scene ext_house_of_mt_night with slideright
    play ambience ambience_camp_center_night
    play music music_list["confession_oboe"] fadein 2
    us_old "Добрый вечер, Оля. Не спится?"
    show mt smile panama pioneer with moveinleft
    mt "Добрый вечер. Сейчас ещё посижу полчасика, дам пионерам угомониться и пойду на обход."
    us_old "Тогда доброй охоты. И спокойной ночи."
    show mt laugh panama pioneer with dspr
    mt "Спокойной ночи."
    hide mt with moveoutright
    stop ambience
    
    scene dct_ext_library_night_with_light with slideleft
    play ambience ambience_camp_center_night
    show d_sf normal hike at cleft
    show d_us normal dress at cright:
        ypos -0.05
    with moveinleft
    "Библиотека оказалась обитаема: в библиотеке горел свет, и сквозь приоткрытое окно был отчётливо слышен стук пишущей машинки и спорящие о чём-то голоса."
    "Казалось, что спорят между собой скрипучая дверь и серебряный колокольчик."
    me "Женя. И Мику. Какая странная компания."
    us_old "Хочешь зайти, Сёмка? Не надо."
    me "Да, лучше не надо. Я понимаю, что с тех пор как я сбежал, у них здесь своя жизнь."
    show d_sf smile hike with dspr
    me "Хотя на Шопенгауэра глянуть неплохо бы было."
    "На оконной занавеске мелькнула тень. Сначала в профиль, потом повернулась, и стало видно причёску. Очень характерные хвостики."
    me "И Лена здесь. Ладно, спать пора, пусть делают что хотят. Всё, что нам нужно знать, мы узнаем завтра."
    stop music fadeout 1
    stop ambience
    
#######################################
#Глава 11. Здесь записывают в артисты?#
#######################################
   
label artists_:
    $ save_name = u"Дубликат. Четвертая смена -\nЗдесь записывают в артисты?"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Здесь записывают в артисты?" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene int_house_of_dv_day with blinds
    play ambience ambience_int_cabin_day
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound sfx_dinner_jingle_normal
    $ renpy.pause (3)
    play sound sfx_bed_squeak1
    dv "Ульяна."
    dv "Рыжая!"
    play sound sfx_bed_squeak2
    show 3500_dv surprise night at center with moveinbottom:
        ypos -0.15
    play music music_list["i_want_to_play"]
    th "Ого. Вот это я проспала. А всё Рыжая виновата."
    show 3500_dv shocked night with dspr
    th "Я проспала линейку, и теперь Ольга Дмитриевна меня накажет."
    show 3500_dv scared night with dspr
    th "Какой ужас!!!"
    show 3500_dv laugh night with dspr
    th "В общем, хана тебе, Рыжая. Одной конфетой не отделаешься."
    th "Двумя? Или тремя? Надо подумать."
    stop music fadeout 1
    stop ambience
    
    scene ext_house_of_dv_day with dspr
    play ambience ambience_camp_center_day
    "Вторую ночь подряд Алисе плохо спалось. Правда, на этот раз причина была не в ней… Ульянка. Ульянка поднималась несколько раз, выходила куда-то и при этом невольно будила соседку."
    "Пришлось Алисе шикнуть на неё, чтобы Ульянка, проворчав что-то недовольно-жалостливое, наконец угомонилась."
    "А Алиска так и проворочалась до самого утра, и в результате проспала линейку и едва-едва не проспала завтрак."
    play sound sfx_close_door_campus_1
    show dv normal pioneer with dspr
    th "В столовую, в столовую, в столовую… Пока всё не съели."
    hide dv with moveoutright
    stop ambience
    
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    show dv normal pioneer with moveinleft
    $ renpy.pause (1)
    show dv laugh pioneer with dspr
    th "Мелкая рыжая мясорубка уже позавтракала."
    th "И убежала."
    show dv normal pioneer with dspr
    th "Жаль, я с ней пообщаться хотела. Придётся дожидаться, когда прибежит."
    th "Куда она всё-таки бегает?"
    hide dv with moveoutright
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day
    show dv normal pioneer with dspr
    th "И чем мне теперь заняться?"
    show dv surprise pioneer with dspr
    play sound_loop ambience_medium_crowd_outdoors
    th "А там что за толпа?"
    show dv laugh pioneer with dspr
    th "Что там такое? Новый распорядок дня? Без линеек, со свободными подъёмом и отбоем и без ограничения в купании?"
    hide dv with moveoutleft
    "Алиса начала проталкиваться к информационному стенду."
    
    scene dct_ext_bulletin_board with dissolve
    "Все приказы, распорядок дня, правила поведения, план лагеря — всё оказалось скрыто под листами бумаги с каким-то напечатанным на машинке текстом."
    show dv surprise pioneer with moveinleft
    th "Ульяна-большая решила пионеров порадовать? Поглядим."
    stop sound_loop
    stop ambience
    
    scene white with dissolve
    play music music_list["so_good_to_be_careless"]
    show promo_text u"Мику Хатсуне" with dspr:
        xpos 0.4 ypos 0.1
    pause
    show promo_text u"К О С Т Ё Р" as promo_text_2:
        xpos 0.4 ypos 0.3
    show promo_text u"(пионерская сказка)" as promo_text_3:
        xpos 0.35 ypos 0.35
    with dspr
    pause
    show promo_text u"Действующие лица:" as promo_text_4 with dspr:
        xpos 0.1 ypos 0.5
    pause
    stop music
    play sound_loop dct_sfx_pulse_slow fadein 1
    show promo_text u"Анфиса — ранимая бунтарка," as promo_text_5 with dspr:
        xpos 0.1 ypos 0.55
    pause
        
    scene white with flash_red
    show promo_text2 u"Анфиса — ранимая бунтарка" at truecenter with dspr
    $ renpy.pause (1)
    show promo_text2 u"Алиса — ранимая бунтарка!" at truecenter with dissolve
    $ renpy.pause (4)
    stop sound_loop fadeout 3
    
    scene dct_ext_bulletin_board with flash_red
    play ambience ambience_camp_center_day
    play sound_loop ambience_medium_crowd_outdoors
    play music music_list["doomed_to_be_defeated"]
    show dv rage pioneer with dspr
    th "\"Ранимая бунтарка?\""
    th "Ну Мику… Вот тебе точно конец."
    "Зря Женя напечатала этот самый список действующих лиц в алфавитном порядке. Идиоткой Алиса точно не была, кто такая \"Анфиса\" — поняла сразу, а про свою характеристику она прекрасно знала, и характеристика эта её раздражала."
    "Тот же Семён её однажды так и назвал. Тот цикл давно уже канул в Лету, а вот эти два слова засели в памяти у всех причастных."
    th "А эти, вокруг, они ещё и хихикают. Начнут пальцем показывать — покалечу."
    show dv angry pioneer with dspr
    th "«Маша — позитивная болтушка»"
    th "Вот значит как!"
    th "Ладно, Микусенька, дам я тебе шанс. Дочитаю до конца, прежде чем идти и бить."
    show dv normal pioneer with dspr
    "Алиса, уже успокоившись, хмыкнула и приступила к собственно тексту."
    stop music fadeout 2
    stop sound_loop
    stop ambience

    scene white with dissolve
    play ambience ambience_camp_center_day
    show promo_text u"Сцена первая" with dspr:
        xpos 0.4 ypos 0.1
    pause
    show promo_text u"На лесной поляне вокруг костра сидят пионеры и вожатая. Одно место в круге пустует.\nАнфиса задумчиво перебирает струны на гитаре…\n{b}Лариса.{/b} Оксана Сергеевна, мы кого-то ждём? Почему мы сели так, чтобы одно место у костра осталось свободным?.." as promo_text_2 with dspr:
        xpos 0.05 ypos 0.2
    "Кто-то подошёл и встал за левым плечом. Семён — тоже заинтересовался."
    me "Степан, значит. Ну пусть будет Степан. Доброе утро, Алиса."
    stop ambience
    
    scene dct_ext_bulletin_board with dissolve
    play ambience ambience_camp_center_day
    show dv normal pioneer at left
    show d_sf normal pioneer at right
    with dspr
    "Алиса только молча кивнула в ответ."
    me "А очень даже здорово написано. Всё-таки Мику — гениальнейшая девочка. Вот и есть альтернатива спортивному празднику, осталось только «Оксану Сергеевну» уговорить."
    "На последнем листе пьесы была приписка от руки: «{i}Желающие принять участие в постановке — записывайтесь в библиотеке. Сегодня после обеда первая репетиция, завтра вечером — премьера»{/i}."
    me "Пойду с Женей пообщаюсь."
    show dv laugh pioneer with dspr
    dv "Что? В артисты запишешься?"
    show dv normal pioneer with dspr
    me "Нет, Алиса, не в этом случае, не пионера же мне играть. Но чем смогу — помогу. Вот сейчас, для начала, вожатую уговорю на эту авантюру."
    me "А вот ты могла бы и записаться."
    show d_sf smile pioneer with dspr
    me "На роль Оксаны Сергеевны, а?"
    hide d_sf with moveoutright
    "Алиса скептически хмыкнула, проводив Семёна взглядом. Постояла ещё, дочитывая текст, и отправилась к себе."
    hide dv with moveoutleft
    show mi shy pioneer with moveinright
    "А «гениальнейшая девочка», прятавшаяся всё это время на Ульянкином месте — в ближайших кустах, осторожно, так, чтобы никто не видел, выбралась на дорожку и, глупо улыбаясь подслушанной похвале, помчалась в библиотеку."
    "Несмотря на бессонную ночь, спать ей не хотелось совершенно."
    hide mi with moveoutright
    stop ambience

    scene ext_house_of_mt_day with squares:
        zoom 1.2
    play ambience ambience_camp_center_day
    play music music_list["timid_girl"]
    show mt normal pioneer at right
    show d_sf normal pioneer at left
    with dspr
    me "Оля, я тут подумал. Скажи, только честно и откровенно. Насколько тебе дорог твой План мероприятий?"
    "Ольга подняла голову, отвлёкшись от чтения, и искоса глянула на Семёна. Впервые за всю беседу."
    mt "Ты меня к какому решению подвести хочешь?"
    me "К взвешенному и ответственному, Оль. Ты тоже у стенда сегодня была. Поняла, к чему я?"
    "Так получилось, что у стенда, кроме работников столовой, не побывало только четверо: Виола с Анатолием и обе Ульяны."
    "Виола и Анатолий засели в медпункте, пытаясь понять, что же им нужно делать; Ульяна-большая, выгнав Семёна, чтобы не мешался, валялась в спорткомплексе на стопке матов, обложившись тетрадями в попытке разобраться в логике бабы Глаши; а Ульяна-маленькая, набив карманы конфетами, опять умчалась в старый лагерь."
    mt "Ну, предположим. Только не предлагай мне от Плана отказаться."
    me "Не отказаться, но изменить! Дай пионерам возможность проявить себя, а? Оль?"
    show mt sad pioneer with dspr
    mt "Тебе легко говорить. А ну как они провалятся с постановкой? Вы-то уйдёте, а детям провал переживать. Заклюют ведь."
    show mt angry pioneer with dspr
    mt "В общем, так: наберут они труппу до обеда — пусть считают, что моё разрешение у них в кармане; не наберут — значит не судьба. Будем тогда…"
    me "Оля, ну сыграем в волейбол тогда. Опыт есть."
    show mt normal pioneer with dspr
    $ renpy.pause (1)
    mt "Хорошо. Так и сделаем. Хочешь правду, Семён?"
    show mt grin pioneer with dspr
    mt "Самой интересно посмотреть, что получится."
    stop music fadeout 1
    stop ambience

    scene int_library_day with squares
    play ambience ambience_library_day
    play sound_loop dct_sfx_typewriter
    show mi scared pioneer with moveinleft
    mi "Женечка, а если это никому не понравилось? Нет, почему никому? Семёну же понравилось, правда-правда, я сама слышала! Но вдруг кроме Семёна больше никому и не понравилось?"
    mi "Что тогда? Значит, я написала ерунду? Совсем ерунду, которая никому не нравится, а Семён только из жалости меня похвалил. Значит, никто не придёт? Как же плохо, Леночка."
    mi "Это значит, я совсем-совсем никуда не гожусь."
    show mi scared pioneer with move:
        xpos 0.05
    show mz angry glasses pioneer with moveinright
    mz "Как мне хочется кого-нибудь придушить! Мику, не нагнетай! И не мешай мне печатать."
    show mz angry glasses pioneer with move:
        xpos 0.95
    show un scared pioneer with moveinleft
    $ renpy.pause (1)
    show un scared pioneer with move:
        xpos 0.1
    play sound sfx_close_door_1
    show d_sf normal pioneer at right with dspr:
    me "Здравствуйте, барышни."
    stop sound_loop
    show mz angry glasses pioneer with move:
        xpos 0.35
    mz "Да что это такое? Чуть страницу псу под хвост не отправила! Счастье твоё, что это исправить можно! Семён! Или говори, зачем припёрся, или сразу уходи! А то сейчас выгоню!"
    show un shocked pioneer
    show mz angry glasses pioneer with move:
        xpos 0.95
    show mi normal pioneer with move:
        xpos 0.35
    mi "Здравствуй, Сенечка. Ты записаться пришёл? Но у нас для тебя нет роли. Если только вожатым. Но тогда придётся Оксану Сергеевну из действующих лиц убирать, а она там нужна."
    me "Ни в коем случае, Мику. Никого не надо убирать. Я только пришёл сказать, что у тебя всё замечательно получилось. И вожатая пообещала вам помочь, если вы до обеда успеете набрать труппу."
    show mi shy pioneer with dspr
    mi "Ну что ты, Сенечка, не я же одна работала. Вот, мне девочки помогли очень."
    show un normal pioneer with dspr
    show mi shy pioneer with move:
        xpos 0.05
    show mz normal glasses pioneer with move:
        xpos 0.35
    mz "Одна-одна, Лена характеристики действующим лицам придумала, а я вообще только на клавиши давила."
    "Женя уже успокоилась и не рычала, а тихо и неожиданно уютно поскрипывала."
    me "Я, собственно, зачем пришёл, девочки. Подарите мне один экземпляр, пожалуйста."
    mz "Это можно. Мику, ты не против?"
    show mz normal glasses pioneer:
        xpos 0.95
    show mi smile pioneer:
        xpos 0.35
    with move
    show un smile pioneer with dspr
    mi "Конечно, не против. Вот, Сенечка."
    show d_sf laugh pioneer with dspr
    me "Мику. А подписать?"
    show d_sf normal pioneer with dspr
    show mi happy pioneer with dspr
    mi "…"
    "Правда, дальнейшие действия Семёна девочек несколько озадачили. Он вручную пронумеровал все страницы, что было понятно, а на последней странице, уже после текста, написал: «Узел №15» и ещё несколько цифр, которые очень походили на дату, если бы не год — две тысячи восьмой."
    me "Вот так. Теперь не пропадёт."
    me "Ладно, пойду я дальше, девочки. Будет помощь нужна — обращайтесь. И это, будущих артистов не пугайте. А то сразу убегут, а вам до обеда труппу набрать надо."
    "Семён встал, покрутил головой, углядел в одном из шкафов несколько пустых канцелярских скоросшивателей, спросил у Жени и, получив в ответ взмах рукой: «Можно-можно, только проваливай», взял один, вложил в него текст и направился к выходу."
    hide d_sf with dspr
    $ renpy.pause (1)
    show d_sf normal pioneer at right with dspr
    me "Ну, встречайте самых смелых."
    hide d_sf with dspr
    show mi normal pioneer with dspr
    "Будущие звёзды больших и малых академических театров несколько секунд молчали, глядя на администрацию театра, а потом Катя, пересилив накатившее волнение, спросила:"
    voice "Здравствуйте, а кто в артисты записывает?"
    stop ambience

    scene ext_playground_day with dissolve
    play ambience ambience_soccer_play_background
    show d_sf normal pioneer at center with moveinleft
    th "Ай да Мику!"
    th "Это не моё «…не просто так!», этот текст поубойнее будет."
    stop ambience

    scene dct_int_coaching_room2 with dspr
    show d_sf normal pioneer at left with moveinleft
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    me "Рыжик, как освободишься — свистни."
    play music music_list["raindrops"] fadein 1
    show d_us normal sport at center with dissolve:
        zoom 0.8 xpos 0.53 ypos -0.05
    us_old "Хорошо, Сёмк, а пока не мешай. Тут ещё гора работы. Если хочешь помочь, принеси мне обед. Пожалуйста."
    "На столе лежали логарифмическая линейка и две раскрытые тетради бабы Глаши. Рабочая тетрадь закрылась, когда Ульяна отвлеклась на приход Семёна, и только карандаш не давал тетради закрыться окончательно."
    "Семён ещё полюбовался выражением Ульяниного лица: внешне серьёзно-упрямым, и в то же время с то и дело проскакивающими хитровато-озорными проблесками в глазах."
    "Как будто Ульяна только что придумала очередную свою шкоду и сейчас работает над её воплощением в жизнь."
    stop music fadeout 1
    stop ambience
    
#######################################
#Глава 12. Невостребованное откровение#
#######################################
   
label unclaimed_revelation:
    $ save_name = u"Дубликат. Четвертая смена -\nНевостребованное откровение"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Невостребованное откровение" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene ext_dining_hall_near_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["raindrops"]
    show d_sf normal pioneer at right with moveinright
    show un normal pioneer at left with moveinleft
    me "Ну как успехи? Много записалось?"
    show un surprise pioneer with dspr
    un "Не очень.{w} Но достаточно."
    me "Понятно всё. Когда репетиция?"
    show un shy pioneer with dspr
    un "Через час."
    me "Ну, удачи вам тогда."
    un "Спасибо."
    hide un with moveoutright
    hide d_sf with moveoutleft
    stop music fadeout 1
    stop ambience
    
    scene dct_int_coaching_room2 with dspr
    show d_sf normal pioneer at left with moveinleft
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    me "Рыжик, обед пришёл."
    #play music music_list["raindrops"] fadein 1
    show d_us normal sport at center with dissolve:
        zoom 0.8 xpos 0.53 ypos -0.05
    us_old "Спасибо, Сёмк. Ты куда сейчас?"
    me "Не знаю, Уль, пойду погуляю."
    us_old "Вот, правильно. А я поработаю."
    us_old "У бабы Глаши, Сём, был Мозг; вот она всё, что мне нужно, и прописала только в самом общем виде и успокоилась."
    us_old "Мол, дальнейшее — очевидно. А мне теперь приходится пробираться сквозь её мысли и искать решение конкретно нашей задачи."
    show d_us hurt sport with dspr
    us_old "Голова пухнет. Так что ты не мешай мне, Сёмк. Ты тоже мозг, но в этих вещах я лучше тебя разбираюсь."
    stop ambience
    
    scene ext_playground_day with dissolve
    play ambience ambience_camp_center_day
    play music music_list["trapped_in_dreams"]
    show d_sf normal pioneer at center with dspr
    th "Ну и куда мне податься?"
    th "В медпункт к Виоле и Толянычу? Не хочется."
    th "Всё-таки дистанция между нами есть дистанция."
    th "И дело даже не в выстреле из Выключателя и не в стёртой памяти."
    th "Мы просто не совсем свои."
    th "Вот баба Глаша была своя, как ни странно. Единственный здесь оригинал, но безоговорочно считала себя частью здешнего мира."
    th "А обитатели медпункта — чужие. Доброжелательно-пристрастные, охраняющие здешний мир, но чужие."
    th "Они даже сами себя ощущают здесь инородными телами."
    th "Не повезло — хотеть вернуться и не мочь. А могли бы уплыть через теплообменник, но что-то держит. Может, обязательства, может, что-то ещё."
    show d_sf smile pioneer with dspr
    th "Так, я опять завис. Вернёмся к реальности."
    stop music fadeout 1
    stop ambience

    scene ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at center with dspr
    th "Медпункт отпадает. Из спортзала меня выгнали."
    th "Здешних \"артистов\" не хочется смущать."
    th "Пойду на пляж."
    stop ambience
    
    scene dct_ext_beach_day_with_pass_train with dissolve
    play ambience dct_ambience_beach
    show sl normal swim at right with dspr
    sl "Октябрята! Внимание! В воду, бего-ом, марш! Десять минут ваши!"
    kids "Ура-а-а!"
    show sl laugh swim with dspr
    show d_sf smile swim at left with moveinleft
    play music music_list["dance_of_fireflies"]
    me "Привет, Славя. Как мелкие? За буйки не заплывают?"
    show sl scared swim with dspr
    sl "П-привет."
    show sl shy swim with dspr
    sl "Не заплывают."
    hide d_sf with moveoutleft
    th "Что такое?"
    th "Никогда и никого в жизни не стеснялась, а тут такое неудобство."
    th "Лежала себе на пляже, купание у октябрят контролировала."
    th "А этот пришёл, поздоровался, разделся и улёгся так, чтобы всех видеть."
    show sl scared swim with dspr
    th "И вроде бы и не смотрит на меня, больше за октябрятами следит, как будто это он, а не я, сегодня дежурит. А я стесняюсь."
    th "Хочется сходить и окунуться, а почему-то неловко."
    th "Если неловко окунуться, то, может, подойти и побеседовать о чём-нибудь? Нет, подойти тоже неловко."
    hide sl with moveoutright
    "Вот у октябрят — у тех никаких комплексов не наблюдалось. Половина с визгом скатывалась по горке в воду, а несколько человек подошли к Семёну, присели рядом с ним на корточки и о чём-то с ним беседовали."
    "Славя даже заревновала чуть-чуть."
    show sl normal swim with dspr
    th "Я умею с малышнёй обходиться, и малыши меня чужой не считают, но чтобы самим вот так посвящать в свои дела…"
    th "Вон они — сидят на корточках, что-то по очереди Семёну объясняют; тот тоже приподнялся, сел по-турецки, взял прутик в руки и что-то говорит в ответ, рисует прутиком на песке непонятные схемы."
    th "А мне обидно."
    hide sl with dspr
    "Вдруг Вася, самый тихий, что-то сказал такое, что Семён аж замер на полуслове и вдруг разулыбался — рот до ушей, хлопнул ладонью по песку, ответил Васе так, что вся компания тоже заулыбалась, и пожал каждому руку."
    show sl normal swim with moveinleft
    sl "Девочки и мальчики, младший отряд! Купание закончено! Всем из воды, всем вытереться, всем переодеться! В мокрых трусах никто с пляжа не пойдёт!"
    kids "У-у-у-у… Что попало!"
    "Но как бы то ни было, а режим есть режим, и чаще добрым словом, а пару раз и мягким понуканием, но октябрята были выгнаны из воды, вытерты, переодеты, одеты и отправлены по домикам."
    "Пока Славя возилась с малышами, о Семёне и не вспоминала."
    show sl scared swim with dspr
    "Но как только последний малыш был одет и пришло время одеваться самой, голова сама повернулась к месту, где загорал гость лагеря."
    show sl shy swim with dspr
    th "Ушёл? И… хорошо."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with slideleft
    play ambience ambience_camp_center_day
    "До площади всем — и малышам, и Славе — было по пути, поэтому шли по главной аллее мимо склада и столовой, из которой уже вкусно пахло, не разбредаясь."
    play music music_list["what_do_you_think_of_me"]
    show sl normal pioneer with moveinleft:
        xpos 0.25
    sl "Вы чем так гостя обрадовали?"
    show sl normal pioneer with move:
        xpos 0.55
    show d_sz normal pioneer at left with moveinright:
        yalign 0.27
    d_sz "А он не гость, Славя. Он же здесь жил! Я только спросил его, почему он сразу же, в первый день, не подошёл и не поздоровался?"
    sl "А вы разве знакомы были?"
    "Серёжа вздохнул и повторил ещё раз, медленно и терпеливо, как умственно отсталой:"
    d_sz "Конечно, Славя, я же сказал, что он здесь жил. Вы, старшие, иногда не понимаете самых простых вещей."
    show sl surprise pioneer with dspr
    sl "Подожди, как вы могли быть знакомы, если ему двадцать пять, а тебе всего десять? Его даже вожатая не помнит, хотя тоже отдыхала в этом лагере, когда пионеркой была."
    d_sz "Забыла. Мы-то, младшие, многого не помним, а старшие вообще всегда всё-всё забывают. Все прошлые смены, какие прожили. Ты вот тоже забыла."
    hide d_sz
    show sl serious pioneer at center
    with pixellate
    th "Уф-ф-ф. Я ждала какой-то истины устами младенца, но, кажется, обошлось. Кажется, вместо истины мне подали простые детские фантазии. Но это лучше, чем «Чёрная вожатая». Это что-то новое, свежее и не страшное."
    show sl smile pioneer at right
    show d_sz normal pioneer at left:
        yalign 0.27
    with pixellate
    sl "И что же я забыла?"
    d_sz "Да всё. Ты встречала его каждую смену, когда он приезжал, а когда он уплыл от нас, ты плакала. А потом каждое воскресенье ходила к пустому автобусу."
    d_sz "А потом стал приезжать другой пионер, тоже Семён, но другой. Такой же, как вы все — тоже ничего не помнит."
    "Славя любила детей и любила общаться с детьми. Слушать их истории, а эта история была интересная."
    show sl smile2 pioneer with dspr
    sl "Вот как? А этот Семён, значит, помнит?"
    d_sz "Да, этот помнит. И Ульяна-большая тоже помнит, но ещё не всё — ещё бывает, что забывает."
    d_sz "Вы, старшие, иногда перестаёте забывать и много смен всё помните. А потом опять забываете."
    show sl laugh pioneer with dspr
    sl "А этот Семён — он тоже всё забудет?"
    "Славя и октябрята отошли к ближайшей скамье. Малыши, кажется, обрадовались, что у них появился слушатель, и фантазировали наперебой."
    show d_sz normal pioneer with move:
        xpos 0.12  yalign 0.27
    show d_oz normal pioneer at left with moveinleft:
        xpos 0.4  yalign 0.27
    d_oz "Семён ничего не забудет! Он в том своём лагере, где он сейчас физрук, должен был всё забыть, но ничего не забыл! Значит, уже не забудет."
    show sl normal pioneer with dspr
    sl "Оксана, а откуда ты знаешь, что он должен был всё забыть в том лагере?"
    d_oz "А мы, младшие, иногда меняемся лагерями и новости рассказываем. Переходим из лагеря в лагерь. Вот Артём — тот как раз из того самого лагеря, а наш Артём — тот сейчас там."
    show d_oz normal pioneer with move:
        xpos 0.12  yalign 0.27
    show d_sz normal pioneer at left with move:
        xpos 0.4  yalign 0.27
    d_sz "Вы, старшие, тоже иногда меняетесь лагерями, но ничего не помните. Для вас все лагеря одинаковыми кажутся."
    show d_sz normal pioneer with move:
        xpos 0.12  yalign 0.27
    show d_oz normal pioneer at left with moveinleft:
        xpos 0.4  yalign 0.27
    d_oz "Серёжа, не мешай, дай я ещё расскажу. Жалко, что этот Семён уплыл от нас, потому что Артём рассказывал, какая у них там футбольная команда. И какой праздник Нептуна там устраивают."
    show sl smile pioneer with dspr
    "Славя улыбнулась про себя, стараясь, чтоб малыши не заметили. Обижать их совсем не хотелось — малыши были очень славные. Они стояли напротив Слави, и на лицах у них горела жажда поделиться знанием."
    "Ну да, в таком возрасте охотно веришь в собственные фантазии. Славя не выдержала прилива нежности и запустила ладони в волосы близнецов, прихватила пряди и чуть подёргала, не больно и не обидно, а именно так, чтобы близнецы почувствовали ласку."
    d_oz "Артём говорит, что Семён очень хороший. Но ты, Славя, тоже хорошая."
    "А Серёжа — тот смутился и отдёрнул голову."
    sl "Оксана, ты сказала: тот Артём и наш Артём. А почему никто не заметил разницы?"
    d_oz "Потому что в каждом лагере мы одинаковые, как близнецы."
    sl "И что, в каждом лагере есть своя Оксана?"
    d_oz "И Оксана, и Серёжа, и Вася, и ты, и вообще все есть. И даже вожатая."
    play sound sfx_dinner_jingle_normal
    "Жалко было отпускать ребят, но режим важен для малышей."
    show sl normal pioneer with dspr
    sl "Так, мальчик и девочка. Мы с вами ещё обязательно побеседуем, а сейчас дуйте к умывальникам и на ужин! Пять минут ещё у вас есть, успеете, а иначе без сладкого останетесь — друзья съедят."
    hide d_sz
    hide d_oz
    with moveoutleft
    th "Надо будет ещё поговорить на эту тему с ребятами. Может быть, со всеми малышами разом. Уж больно фантазия интересная. Вдруг где-то сейчас другая Славя тоже сидит на лавочке и беседует с малышами."
    hide sl with moveoutleft
    stop music fadeout 1
    stop ambience
    
    scene ext_path2_day with squares
    play ambience ambience_forest_day
    "Если бы Славя видела сквозь деревья, то сейчас бы она смогла увидеть, как на Ульянкиной тропе столкнулись Семён, идущий из библиотеки к спортзалу, и Артём, бегущий с футбольного поля к себе в домик."
    "Как они стояли друг напротив друга, как потом одинаковыми движениями полезли себе за воротники и как достали оттуда висевшие у каждого на шее: Артём — свисток на зелёной тесьме, а Семён — двадцатикопеечную монету на витом чёрном капроновом шнурке."
    "Как оба расплылись в улыбках, как подошли друг к другу и пожали руки."
    show d_sf smile pioneer at left with moveinleft
    show d_ar smile pioneer at right with moveinright
    me "Вот ты где! Я рад тебя видеть!"
    d_ar "Ага!"
    me "Ладно, беги ужинать. Потом ещё поговорим."
    stop ambience
    
#############################
#Глава 13. Деформации сдвига#
#############################
   
label shear_deformations:
    $ save_name = u"Дубликат. Четвертая смена -\nДеформации сдвига"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Деформации сдвига" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene ext_house_of_sl_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    "Славя повесила сушиться купальник и пляжное полотенце."
    "Кто-то и когда-то натянул за домиком верёвку. Явно именно для этого."
    "Обошла домик, кивнула проходящему мимо Артёму."
    play music music_list["timid_girl"]
    show sl normal pioneer with moveinleft
    sl "Артёмка, на ужин не опоздай."
    show d_ar smile pioneer at fright with moveinright
    d_ar "Нет, Славя. Ни за что не опоздаю."
    hide d_ar with moveoutright
    show sl smile2 pioneer with dspr
    $ renpy.pause (1)
    th "Славный какой."
    hide sl with dspr
    stop ambience
    
    scene int_house_of_sl_day with dspr
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    show sl normal pioneer with moveinleft
    th "Ну приехал этот Артём из другого лагеря. В прошлую смену отдыхал там, а в эту здесь. Что тут такого?"
    show sl smile pioneer with dspr
    th "Ох и фантазия у малышей."
    th "Другой Сергей, другая Оксана, другая вожатая, другая Славя…"
    th "И все одинаковые, как близнецы."
    show sl normal pioneer with dspr
    th "Вот мы соберёмся все вместе, и как нам друг друга отличать?"
    show sl laugh pioneer with dspr
    th "Косы, что ли, отрезать, чтобы не путали?"
    th "Интересно, как я буду выглядеть?"
    stop music fadeout 1
    stop ambience
    
    scene int_house_of_sl_day with pixellate
    play ambience ambience_int_cabin_day
    $ prolog_time()
    show d_sl smile pioneer at center with pixellate:
        ypos -0.1
    th "Неплохо. Но с такой причёской нужно выглядеть строже."
    show d_sl serious pioneer with dspr
    th "Теперь к внешнему виду не подходит имя Славя. Славяна? Да, Славяна будет лучше."
    th "А послезавтра мне встречать опоздавшего пионера, «который тоже ничего не помнит». Как это может выглядеть с такой причёской?"
    stop ambience
    
    scene ext_camp_entrance_day with squares
    play ambience ambience_camp_entrance_day
    play music music_list["always_ready"]
    show d_sl serious pioneer at center with dspr:
        ypos -0.1
    sl "Здравствуй, это ты только что приехал? Добро пожаловать в «Совёнок». Я Славяна, помощник вожатой."
    show d_sl angry pioneer with dspr
    sl"Я отведу тебя к администрации лагеря, следуй за мной."
    stop music fadeout 1
    stop ambience
    
    scene int_house_of_sl_day with pixellate
    play ambience ambience_int_cabin_day
    $ day_time ()
    show sl laugh pioneer with dspr
    th "Это так чопорно, что даже смешно."
    show sl smile pioneer with dspr
    th "На ужин пора. А то Ольга Дмитриевна будет беспокоиться."
    hide sl with moveoutright
    stop ambience

    scene dct_int_coaching_room2 with squares
    "Когда Семён вернулся перед ужином в тренерскую, там ничего не изменилось. Его Ульяна всё так же сидела за столом, поджав под себя одну ногу, всё так же грызла колпачок ручки, всё так же периодически запускала пятерню в свои волосы."
    "Только количество исписанных листов в тетради выросло, а одну тетрадь бабы Глаши сменила другая. И ещё одна деталь изменилась: во взгляде Ульяны пропали озорные искорки. Теперь за столом сидела девушка, чем-то потрясённая. Например, свалившимся на неё известием."
    show d_sf normal pioneer at left with moveinleft
    play ambience ambience_int_cabin_day
    play sound sfx_close_door_1
    me "Что-то случилось, Рыжик?"
    play music music_list["trapped_in_dreams"]
    show d_us hurt sport at center with dissolve:
        zoom 0.8 xpos 0.53 ypos -0.05
    us_old "Случилось? Нет, Сёмк. То есть да, но не сегодня. Давно. Очень давно."
    me "Что-то плохое?"
    us_old "Ещё не знаю, ещё не разобралась. Сёмк, я поняла, почему баба Глаша не стала подробно расписывать эту часть своей работы."
    $ renpy.pause (2)
    us_old "Сёмка, я, кажется, знаю про Систему всё."
    show d_sf serious pioneer with dspr
    me "Страшно, Уль? У меня тоже есть свои мысли. И я боюсь их на тебя вывалить. А Виоле тем более боюсь их пересказать."
    show d_sf normal pioneer with dspr
    me "Я тебе лучше сказку расскажу."
    me "Жила-была одна маленькая девочка. У неё были рыжие волосы и голубые глаза, одеваться она любила в красную футболку и шорты, и ещё у неё был плюшевый медведь…"
    us_old "Сёмк?"
    me "Что?"
    show d_us normal sport with dspr
    us_old "Всё хочу тебя спросить. А дальше что было?"
    show d_sf laugh pioneer with dspr
    me "А дальше мы идём ужинать. Не я тебе сюда ужин несу, а мы идём в столовую вместе. А оттуда к Виоле, где ты меня будешь в спинку иголками тыц-тыц."
    show d_us laugh sport with dspr
    us_old "Сёмк. Ты придурок. В спинку ему тыц-тыц."
    show d_sf normal pioneer
    show d_us smile sport
    with dspr
    us_old "Хватит киснуть, ты прав, Сёмк. Не такой уж ты у меня и придурок."
    "У обоих были свои мысли. И про систему, и про Виолу с Анатолием, и оба боялись не то что вывалить их на друг на друга, но даже полностью проговорить их самим себе, оставляя пока на уровне ощущений и образов."
    stop music fadeout 1
    stop ambience

    scene int_house_of_dv_day with squares
    play ambience ambience_int_cabin_day
    play music higekitekina
    "Алису сигнал к ужину застал дома. Она мучила гитару, устроившись на кровати, и опять проживала в своём воображении тот давний момент бегства Семёна на украденной лодке."
    play sound sfx_dinner_jingle_normal
    show dv sad pioneer with moveinbottom
    th "На ужин зовут. Сейчас пойду, а там Ольга начнёт допрашивать, где Ульяна."
    th "Нет, я догадываюсь, где Ульяна. Но не подставлять же Рыжую."
    th "Врать или хамить настроения нет. Да и есть не хочется совершенно."
    show dv normal pioneer2 with dspr
    th "Нужно встряхнуться и отвлечься. А ужин… В крайнем случае, сделаем ночной набег на столовую."
    th "Надеюсь, из музыкального кружка меня не выгонят."
    "Репетиции внезапно возникшего театрального кружка шли в кружке у Мику, и Алисе было интересно. Всем было интересно, но посторонних не пускали."
    th "Мику у них за режиссёра. Может, если Мику занята, тогда им музыкальное сопровождение понадобится?"
    stop music fadeout 1
    stop ambience
    
    scene int_musclub_day with squares
    play ambience ambience_music_club_day
    "В музыкальном кружке по случаю прозвучавшего сигнала на ужин оставалась одна Мику. Редкий для Мику момент: она была сердитая и расстроенная."
    show mi dontlike pioneer at right with moveinright
    mi "Здравствуй, Алисочка. А мы вот репетируем-репетируем, только ничего толком не выходит. Я хочу одного, а ребята или хотят другого, или не понимают, чего я хочу. Мы спорим, спорим, а время идёт."
    show mi sad pioneer with dspr
    mi "Через сутки премьера, а ещё ничего не готово. Совсем ничего. А ещё пионеры — те, которые не записались в кружок. Ходят, подглядывают, отвлекают."
    mi "Когда Женя здесь была, она их гоняла и артистами командовала, но Жене в библиотеке нужно быть, а я совершенно не умею ругаться."
    mi "Мы уже дверь запираем, и окна занавесили. А одной портьеры не хватает, вот все любопытные у того окна и толпятся."
    show dv normal pioneer2 at left with moveinleft
    dv "Ну насчёт поругаться и погонять любопытных я тебе помогу, Мику. И ещё с разным чем. Если хочешь."
    show mi surprise pioneer with dspr
    mi "Алисочка, а ты правда хочешь помочь? Тогда сегодня ещё одна репетиция, и завтра до обеда две, и после обеда ещё одна."
    "Мику даже вспыхнула от удовольствия, мгновенно меняя настроение от текущей подавленности на свой повседневный сверхпозитивный оптимизм."
    show dv guilty pioneer2 with dspr
    "А Алисе опять вспомнился последний кадр из собственной фантазии: с лодкой, чуть накренившейся, с набравшим ветер небесно-голубым самодельным парусом."
    dv "Скажи, Мику. А ты не знаешь, где пятая портьера?"
    show mi shy pioneer with dspr
    mi "Пятая? Не знаю, Алисочка. Их так и было четыре, когда мы приехали. Вчера, когда Семён за гитарой приходил, он тоже всё смотрел на эти портьеры. Мне так неудобно было, будто это я сама пятую портьеру потеряла."
    dv "А ты не теряла?"
    show dv scared pioneer2 with dspr
    show mi dontlike pioneer with dspr
    mi "Алисочка, ну о чём ты говоришь? Мы же шесть дней как приехали."
    show mi normal pioneer with dspr
    mi "Говорят, когда-то давно один мальчик сделал из портьеры парус и уплыл из лагеря на лодке…"
    show mi scared pioneer with dspr
    mi "Алиса! С тобой всё хорошо?!"
    show dv normal pioneer2 with dspr
    dv "Нет-нет. Всё хорошо, Мику. Если тебе нужна помощь, я помогу."
    show mi happy pioneer with dspr
    mi "Тогда через полтора часа репетиция. Не опаздывай! А сейчас — на ужин!"
    stop ambience
    
    scene dct_ext_boathouse_day_with_pass_train with squares
    play ambience ambience_boat_station_day
    show dv shy pioneer2 with moveinleft
    "Алиса отпустила Мику вперёд, а сама, дойдя до главной аллеи, свернула к пристани. Ей нужно было попасть на остров для последней проверки. Для этого у Алисы было ещё полтора часа времени."
    stop ambience

    scene dct_int_aidpost_sunset with squares
    play ambience ambience_medstation_inside_day
    play music music_list["dance_of_fireflies"]
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    show cs normal glasses with moveinleft:
        xpos 0.25
    cs "Пришли на процедуру… {w}молодожёны? Семён, как самочувствие? Сейчас третий сеанс проведём, и если утром будешь себя хорошо чувствовать, то можешь нагружаться по полной программе. Ульяна, не трясёшься больше?"
    show cs normal glasses with move:
        xpos 0.05
    show d_us normal dress at right with moveinright:
        ypos -0.05
    us_old "Трясусь, Виола. Но давайте уже приступать. Раньше начнём — раньше закончим."
    show cs smile glasses with dspr
    cs "Инструмент и атлас теперь твои, Ульяна. Владей. Троих человек покалечишь, а четвёртого уже на ноги поставишь."
    show cs normal glasses with move:
        xpos -0.15
    show d_to normal pioneer at left with moveinleft
    d_to "Кстати, Семён: то, что твоя спина не восстановилась сама по себе, говорит о том, что ты отключён от системы. Как тебе такая мысля?"
    d_to "Что-нибудь накопали в тетрадках Денисовны?"
    "Ульяна и Семён посмотрели друг на друга, и девушка показала взглядом: «Говори ты»."
    show d_us normal dress with move:
        xpos 0.95 ypos -0.05
    show d_sf normal hike at right with moveinright
    me "Виола, Анатолий. Мы накопали. Ульяна и я, каждый по отдельности. Можно завтра, после спектакля? Просто пока не всё проверили. Скажу только, что вы двое тут тоже не просто так, и всё, кажется, завязано на вас. И вы тут… В общем, вас тут не должно быть. Так или иначе."
    show d_sf normal hike with move:
        xpos 0.90
    show d_us normal dress at right with move:
        ypos -0.05
    us_old "Сёмка прав. Я пока не знаю, что будет, ещё не проверила, но до завтра доделаю."
    stop music fadeout 1
    stop ambience

    scene dct_ext_island_reverse_sunset with squares
    play music music_list["orchid"]
    play ambience ambience_lake_shore_evening
    show dv normal pioneer2 with dspr
    th "Это здесь. Да, точно здесь."
    th "Ржавые гвозди, алюминиевая проволока, кусок верёвки, пассатижи, топо… Ах!" with flash_red
    play sound_loop dct_sfx_pulse
    show dv guilty pioneer2 with flash_red
    $ renpy.pause (1)
    show dv guilty pioneer2 with flash_red
    $ renpy.pause (1)
    th "Кажется, я с третьей попытки научилась переживать эти приступы непонятные."
    th "Обошлось. Только в ушах шумит и сердце колотится."
    stop sound_loop fadeout 2
    "Искать ничего не пришлось. Всё это барахло лежало именно там, под тем кустом, куда его сунула в своих, как она считала, фантазиях Алиса."
    stop ambience
    
    scene dct_ext_island_reverse_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_lake_shore_day
    show mt sad pioneer with dspr
    mt "Алиса, пожалуйста, собери инструмент, незачем ему тут валяться."
    show mt scared pioneer with dspr
    mt "Не удержали. Как же жаль! Теперь…"
    hide mt with moveoutleft
    stop ambience
    
    scene dct_ext_island_reverse_sunset with pixellate
    play ambience ambience_lake_shore_evening
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    show dv guilty pioneer2 with dspr
    "Алиса чуть дрожащими руками спрятала находку назад под куст, потом подумала, вытащила верёвку и так, с бухтой верёвки в руках, пошла на противоположную сторону острова — обратно к лодке."
    stop ambience
    
    scene dct_ext_island_sunset with slideright
    play ambience ambience_lake_shore_evening
    show dv guilty pioneer2 with moveinright
    th "Какая берёза интересная. Толстая ветка метра три от земли, и добраться до неё легко… Интересно, верёвка выдержит?" with flash_red
    show dv angry pioneer2 with vpunch
    dv "Не дождётесь!"
    stop music fadeout 2
    $ renpy.pause (2)
    play sound sfx_water_splash
    "И верёвка полетела подальше в воду."
    show dv laugh pioneer2 with dspr
    dv "Не дождётесь! У меня репетиция через полчаса."
    dv "Надо помочь Мику. А ещё надо решить: это я сошла с ума или Семён с Ульяной не врут?"
    stop ambience

    scene dct_int_house_of_sl_sunset with squares
    play ambience ambience_int_cabin_evening
    "Славя вернулась с ужина в домик и опять встала перед зеркалом."
    show sl normal pioneer at left with moveinleft
    $ renpy.pause (1)
    play sound sfx_close_door_1
    show mz normal pioneer at right with moveinleft
    mz "Ради кого прихорашиваешься?"
    sl "Женя. Ты можешь мне помочь?"
    mz "А что нужно? Только побыстрее, мне скоро на репетицию идти."
    "И неизвестно почему, ведь не хотела же. До ужина ещё не хотела, и сама посмеялась этой бредовой идее, но Славя попросила:"
    show sl scared pioneer with dspr
    sl "Женя, я хочу отрезать косы, а одна я не справлюсь."
    stop ambience
    
###################
#Глава 14. Осколки#
###################
   
label splinters_:
    $ save_name = u"Дубликат. Четвертая смена -\nОсколки"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Осколки" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_int_coaching_room3_night with blinds
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    play music music_list["door_to_nightmare"]
    "Семён проснулся как от толчка." with hpunch
    "Было самое начало третьего часа ночи, и всякая послеотбойная жизнь в лагере уже давно затихла: уже погас свет в медпункте, уже закончилась репетиция в театральном кружке, уже обошла территорию вожатая, уже Рыжие совершили ночной набег на столовую и успели уничтожить улики."
    "Давно уснули самые отъявленные полуночники и страдающие бессонницей. Кузнечики замолкли, а утренние птицы ещё не начинали проверять голос. Семён лежал и пытался понять одно: что же его разбудило?"
    "В тренерской было темно, и только под дверью угадывалась сероватая полоска; стояла абсолютная тишина, а на плече уютно сопела Ульяна, что за нарушение тишины не считалось; ни спина, ни зубы не болели. Казалось бы, закрывай глаза и досыпай."
    "А Семён лежал с открытыми глазами и героически пытался ни о чём не думать. Не получалось."
    "Вспоминался прошедший вечер: беседа с Виолой и Анатолием, особенно фраза, брошенная Виолой на прощание: «Думаешь, ты один до этого додумался?»; репетиция, на которую их деликатно, насколько это возможно со стороны Алисы, но решительно не пустили; вопросительный — нет, не вопросительный, а о чём-то молящий взгляд той же Алисы."
    "Вспоминалась высунувшаяся было из домика и тут же спрятавшаяся назад Славя: что-то было в ней не так, но она так быстро мелькнула, что Семён не понял, что именно."
    "Отдельно вспомнилась беседа с Артёмом за ужином. Они втроём специально сели за один стол, и никто, кроме мелких, не понял, почему и зачем."
    show blink
    $ renpy.pause (2, hard = True)
    stop music fadeout 1
    stop ambience
    
    scene int_dining_hall_people_day
    #show dct_dream_veil:
    #    shiver
    with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    show d_us normal sport at left:
        zoom 1.2
        ypos -0.02
    show d_ar normal pioneer at right:
        zoom 1.2
        #ypos 0.05
    with dspr
    me "Я всё гадал, куда ты подевался. А ты здесь."
    d_ar "А я здесь."
    me "А почему сразу не подошёл?"
    show d_ar dontlike pioneer with dspr
    d_ar "Я думал, ты всё забыл и не узнаешь меня, как…"
    show d_us sad sport with dspr
    us_old "Ой, Артёмка, ну я же извинилась перед тобой уже, но я и правда тебя не узнала."
    me "Бывает, Рыжик, мне сколько лагерей пришлось пройти, чтобы начать двойников уверенно различать."
    show d_ar normal pioneer with dspr
    me "Артём. Скажи. Вот ты не спишь. И в том лагере не спал. А тот Артём, который вместо тебя — он спит. Вы же, младшие, тоже не все не спите."
    show d_us normal sport with dspr
    d_ar "Да. Я раньше спал, сейчас не сплю, потом усну. А кто-нибудь ещё проснётся. Так всегда было."
    us_old "А много вас, младших, не спит?"
    d_ar "По разному. Часто один человек, иногда два, редко три."
    me "А как вы друг к другу относитесь? Те, кто спит, и те, кто не спит?"
    d_ar "Обыкновенно. Когда-то мы спали, а они нет. А потом мы проснулись, а они уснули."
    d_ar "Мы рассказываем тем, кто спит, о том, что происходит. Те, кто просыпается — те это запоминают и рассказывают дальше."
    me "То есть вам верят?"
    d_ar "Конечно, Семён. А как же иначе? Ведь это же правда!"
    me "Эх…"
    me "Вы и засыпаете, наверное, легко, потому что знаете, что рано или поздно снова проснётесь. Завидую."
    us_old "Артём. Скажи. Вот ты проснулся. А как ты нашёл других, кто не спит в вашем отряде?"
    show d_ar smile pioneer with dspr
    d_ar "А это у нас такая считалка есть специальная: \"Кто не спит, тот выйди вон!\"."
    d_ar "Мы в самый первый день как приехали, считаемся. Как будто домики делим. А те, кто не спит — те понимают, о чём речь, и называются."
    d_ar "А ты, Семён, когда сказку начал рассказывать — мы сразу всё поняли."
    me "Почему не сказали?"
    d_ar "Так интересно же. И потом, ты самый первый из старших, который с нами на эту тему заговорил. Всегда было, что мы сами по себе, а вы, старшие, сами по себе."
    th "И нет никому никакого дела…"
    stop ambience

    scene dct_int_coaching_room3_night with squares
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_day
    play music music_list["goodbye_home_shores"]
    th "И нет никому никакого дела…"
    th "Нет, так я никогда не засну. Может, выйти подышать?"
    play sound sfx_bed_squeak1
    "Семён осторожно вытянул плечо из-под Ульянкиной головы, жена обиженно засопела, но не проснулась. Поцеловал Ульяну в макушку, на мгновение втянув в себя запах её волос, сел на кровати, нашарил стул с одеждой, вслепую оделся и, осторожно нащупывая перед собой дорогу и стараясь ни во что не врезаться, направился к двери."
    play sound dct_sfx_wood_floor_squeak
    "Открыл дверь, и в лунном свете, заливавшем спортзал, нашёл свои кеды, обулся и вышел. Подумал об Ульяниных страхах и, прикрыв дверь, включил в спортзале свет. Если проснётся, то света, пробивающегося под дверь, ей будет достаточно."
    th "Взрослая ведь уже, а так и боится оставаться ночью одна в тёмной комнате. Что там было в её биографии? Мнимой или реальной. Её самой или её оригинала."
    "Подумал ещё написать записку, чтоб не волновалась, если проснётся одна, но не стал. Это надо было возвращаться в комнату, шариться в темноте по столу и в столе в поисках бумаги и ручки, включать свет. А значит, гарантированно разбудить Ульяну."
    th "Далеко не пойду. Так, постою на крыльце."
    stop ambience
    
    scene dct_ext_beach_night_with_pass_train with dissolve
    #play ambience ambience_camp_center_night
    "На улице было прохладно и светло от полной Луны."
    th "Вот интересно. В каждом лагере своя фаза Луны. Всю смену. В этом — всегда полнолуние."
    th "Окунуться? Нет. Это надо возвращаться за плавками, а не хочется. Конечно, сейчас можно и без плавок, пока зрители спят, но нет."
    #Семён вдохнул полную грудь ночного воздуха и задержал дыхание. 
    th "Всё-таки это мой мир. Не тот, с той стороны теплообменника, или откуда там приходил Пионер, а именно этот. Надо его сохранить, и как мне ни жаль, но придётся Виолу и Толяныча огорчать и ставить перед выбором. Интересно, что там Рыжик насчитала?"
    th "Пойти пройтись ещё? Я недалеко, только спортплощадку обойду по кругу и назад."
    #stop ambience

    scene ext_playground_night with dissolve
    #play ambience ambience_camp_center_day
    "Семён прошёл вдоль спортзала и по тропинке между туалетом и спортзалом вышел на футбольное поле."
    stop music fadeout 1
    th "Мяч забыли, футболисты."
    play sound sfx_soccer_ball_kick
    play ambience ambience_camp_center_night
    play sound_loop ambience_soccer_play_background
    "Семён огляделся — никто не видит? Разбежался и отправил мяч к центру поля."
    "И тут же, словно от удара по мячу, включились остальные, дополнительно к зрению, органы чувств. Стало слышно, как ёжик фыркает и топает где-то под скамьями, лёгкий ветерок приласкал правую щеку, запахло близким лесом."
    play sound dct_sfx_crow
    th "А в посёлке Шлюз между спортплощадкой и лесом стоят три пакгауза, к которым подходит железнодорожная ветка, и пахнет больше креозотом от шпал, чем грибной сыростью и листвой."
    th "На волейбольной площадке есть жизнь. Интересно, кто бы это мог быть? Да ещё в это время. Бадминтон — это Лена. А волейбол? Славя? А с кем?"
    stop sound_loop
    "Удары по мячу стихли, и стали слышны девичьи голоса. Знакомые и незнакомые одновременно."
    show d_sl tender sport with moveinleft:
        pos (0.5, -0.1)
    d_sl "Здравствуй, Сёмушка."
    me "Славя? Славяна?"
    show d_mi cry_smile casual with moveinleft:
        xpos 0.05
    mi "Здравствуй… Сенечка?"
    me "Мику… ся?" with flash
    "И заблокированный цикл с отчётливым таким щелчком занял в памяти Семёна своё место."
    me "Это… болезненно." with flash
    "Да что там — больно это было."
    me "Ох." with flash_red
    "К счастью, удалось устоять на ногах."
    play music a_v_to_the_crows fadein 2
    me "Вы — не они!"
    "В затылке Семёна что-то пульсировало, и мир плыл перед глазами. Очень хотелось сесть, хоть прямо на землю."
    mi "Прости, Сенечка. Я… Мы чувствуем, как тебе сейчас плохо. Но нам очень нужно было с тобой поговорить."
    sl "И мы — не они, ты прав, Сёмушка. Но мы ещё помним…"
    th "Я тоже помню…"
    stop ambience
    
    scene ext_camp_entrance_day with pixellate
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play sound dct_sfx_jump
    me "К воротам, рысью, марш-марш!"
    th "Я помню!" with flash_red
    stop ambience
    
    scene int_mine_door with dissolve
    $ persistent.sprite_time = "night"
    show d_mi serious casual at center with dspr:
        zoom 1.05
    play ambience dct_ambience_drips_in_mine
    mi "Сенечка, а меня ты любишь?"
    th "Я помню!" with flash_red
    stop ambience
    
    scene dct_life_line_fin with dissolve
    play sound_loop sfx_bus_interior_moving
    $ persistent.sprite_time = "night"
    mi "Сенечка!"
    th "Я помню!" with flash_red
    stop music fadeout 1
    stop sound_loop
    
    scene ext_playground_night with pixellate
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play music music_list["no_tresspassing"]
    show d_sl tender sport with dspr:
        pos (0.5, -0.1)
    show d_mi cry_smile casual with dspr:
        xpos 0.05
    mi "Сенечка!"
    mi "Вот так, Славечка. Говорила ты, говорила, и всё зря. Сенечке же очень плохо, и ему не до нас. Сенечка, мы — действительно не они. Мы — то, что осталось от них в памяти Системы."
    d_sl "Да, Сёмушка, можешь считать нас призраками. Это ближе всего к правде."
    show d_sl sad sport with dspr
    d_sl "Не удержалась я, Сёмушка. Наверное, я должна была умереть тогда, в душевой, и восстановиться с нуля, чтобы начать заново с чистой памятью."
    d_sl "Но оказалась слишком крепкой и выжила, а потом ты меня выдернул из кошмара, но я не смогла одна."
    d_sl "Тридцать циклов я держалась, мне было всё хуже и хуже, а меня всё перекидывало из лагеря в лагерь: это Система искала мне место, но не нашла."
    d_sl "И когда я проснулась в Городе, я сдалась. И рассеялась. И сейчас в одном из узлов живёт просто Славя. Только кос у ней нет, ещё не отросли."
    d_sl "Просто волосы до плеч. Но что-то от меня в Системе осталось, вот как и от Мику…"
    mi "Сенечка. Мы помогали тебе как могли. Жаль, что почти-почти никак. А пришли, чтобы сказать, что мы скоро не сможем этого делать. То, о чём догадался ты, и то, что вычислила Ульяна, навсегда изменит Систему. Уже изменило, просто, Сенечка, у ней очень большая инерция."
    d_sl "Сёмушка, мы сейчас уйдём. Нужно, чтобы девочки отдохнули. Если сумеешь, то попроси у них прощения от нашего имени."
    d_sl "И, Сёмушка, береги Мику и Славю, везде береги, во всех лагерях. Когда мы… {w}когда нас не… {w}когда мы рассеялись… {w}В общем, теперь в каждой из них есть наша частичка."
    me "Так и сказала бы: «Береги всех»."
    th "Бедные мои."
    th "Как же плохо-то. Не смог. Не удержал. Никого. А как же Ульяна?"
    mi "И Ульяну свою береги, Сенечка. Вы с ней вместе не просто так."
    d_sl "Пора идти, Мику. Сёмушка, пока мы ещё сможем — мы будем с тобой. С вами."
    mi "Да, Сенечка. Может, у нас почти и не осталось чувств и эмоций, но мы о них ещё помним."
    show d_sl serious sport with move:
        pos (-0.1, -0.1)
    d_sl "Идём, Мику."
    mi "Прощай, Сенечка. И спасибо тебе за всё. За то, что сделал нас живыми."
    show d_mi cry casual with dspr
    mi "Прощай!"
    hide d_mi with easeoutleft
    d_sl "Прощай, Сёмушка. Девочкам сейчас снится сон о нас троих. Так что завтра не удивляйся."
    hide d_sl with moveoutleft
    stop music fadeout 1
    stop ambience

    scene dct_int_coaching_room3_night with vpunch
    $ night_time ()
    play ambience ambience_int_cabin_night
    mi "Прощай, Сенечка."
    th "Я спал?"
    th "Это был сон?"
    th "Или нет?"
    $ renpy.pause (2)
    
    scene dct_us_old with dissolve
    th "Я тебе всё расскажу. Надо."
    show blink
    stop ambience
    
#####################
#Глава 15. Репетиция#
#####################
   
label repetition_:
    $ save_name = u"Дубликат. Четвертая смена -\nРепетиция"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Репетиция" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene int_house_of_mt_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Ольга Дмитриевна проснулась с чувством лёгкого беспокойства."
    th "Что-то сегодня обязательно пойдёт не так."
    play sound sfx_bed_squeak1
    play music music_list["timid_girl"]
    th "Что там у нас по расписанию? Три репетиции театрального кружка и спектакль после ужина; завтра приедет опоздавший пионер и уходят гости, но это завтра; и остальное — повседневная текучка."
    th "Кстати, не забыть выяснить, куда пропадает Ульяна-маленькая, и не забыть предложить гостям уехать на автобусе — всё-таки неплохие люди."
    stop ambience
    
    scene dct_d2_mt_undressed with dissolve
    play ambience ambience_int_cabin_day
    mt "Вот жили мы тут, жили, никого не трогали. И вот на тебе: получи, Оленька, соседа в домик. Пубертатного возраста."
    mt "Вещи... Можно всё развесить и завтра, но… Нет. Мало ли что может случиться до завтра."
    play sound dct_sfx_wood_floor_squeak
    "Вожатая одевалась, одновременно прятала разбросанную по домику одежду в шкаф и ворчала себе под нос."
    stop ambience
    
    scene dct_d2_mt_undressed_2 with dspr
    play ambience ambience_int_cabin_day
    mt "Он же подглядывать начнёт и в вещах рыться. И просто стеснять. А не в спортзал же его селить, и не третьим к этим чудо-изобретателям в домик."
    th "Нужно будет ещё постель на новенького получить и комплект формы."
    stop music fadeout 1
    stop ambience
    
    scene int_house_of_mt_day with dspr
    show mt normal pioneer with moveinright
    play ambience ambience_int_cabin_day
    play sound dct_sfx_wood_floor_squeak
    th "Это же за каждой мелочью придётся в шкаф лазить!"
    th "Ладно, ничего не сделаешь. Где-то плавки ещё были в шкафу."
    th "Вот так приезжает одинокая девушка, заселяется в домик, а в шкафу мужские трусы лежат."
    th "Отдам новенькому, вдруг подойдут."
    stop ambience
    
    scene ext_square_day with dissolve
    play ambience ambience_camp_center_day
    sl "Лагерь, по отрядам становись!"
    show mt normal panama pioneer at left with moveinleft
    play sound_loop ambience_medium_crowd_outdoors
    th "Начинается новый день…"
    th "Вот, Славя уже командует. Славя?"
    play music music_list["farewell_to_the_past_edit"]
    show mt shocked panama pioneer with dspr
    show d_sl serious pioneer with moveinright:
        pos (0.5, -0.1)
    $ renpy.pause (1)
    show d_sl serious pioneer with move:
        pos (0.75, -0.1)
    th "Ох… {w}Что… {w}Как…"
    th "Задранный подбородок, строгий взгляд. Это просто какая-то аристократка у меня в лагере."
    show mt normal panama pioneer with dspr
    th "Что это? Подростковый бунт? Надеюсь, что не против вожатой."
    th "Наказывать не за что. Причёска осталась в допустимых рамках — подумаешь, косы обрезала. Но мне ещё с её родителями разговаривать."
    th "Надо линейку проводить, пионеры ждут. Но как педагог я с ней ещё побеседую."
    hide d_sl with moveoutright
    stop sound_loop
    stop music fadeout 1
    show mt angry panama pioneer at center with move
    mt "Лагерь! Равняйсь! Смирно!.."
    th "Надеюсь, других сюрпризов больше не будет."
    stop ambience

    scene ext_dining_hall_away_day with slideleft
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at fleft with moveinleft
    show d_us smile sport at cleft with moveinright:
        ypos -0.05
    us_old "Ты куда-то ходил ночью? Ой, смотри, что это со Славей?"
    show d_sl normal pioneer at right with dspr:
        ypos -0.1
    $ renpy.pause (1)
    hide d_sl with moveoutright
    show d_sf normal pioneer at left with move
    show d_us smile sport at right with move:
        ypos -0.05
    show d_sf sad pioneer with dspr
    me "Это отдача, Уля. Помнишь, я тебе рассказывал про Славяну? Так вот, здешняя Славя, да и не только здешняя — теперь частично Славяна."
    show d_us normal sport with dspr
    us_old "Это как?"
    me "Чужая память. Как у меня."
    us_old "Знаешь, Сёмка, у меня, кажется, однажды так же было…"
    me "Мне ведь не спалось ночью, Рыжик. Я и вышел подышать. А может, это мне и приснилось."
    show d_sf serious pioneer with dspr
    me "Но так получилось, что попрощаться. Нет больше ни Славяны, ни Мику-моей."
    show d_us hurt sport with dspr
    us_old "Сёмк. Ты никого и никогда не называл раньше своим, своей."
    me "Кроме тебя, Рыжик. Я, наверное, зря тебе это рассказываю, но кому ещё, если не тебе? Помнишь, три дня назад ты спросила меня про девочек?"
    me "Так вот, я вспомнил Мику. Весь цикл, от знакомства до прощания. И тогда с ней мне действительно и взлететь хотелось, и сердце болело."
    me "А ещё она единственная из неготовых проснуться девочек поверила мне и понимала, что исчезнет. И вела себя так, что я и сейчас завидую её мужеству, и тогда завидовал."
    me "До сегодняшней ночи не помнил тот цикл, Система заблокировала его в моей памяти. А сегодня ночью те Мику и Славяна окончательно простились со мной. Уже окончательно."
    me "И приказали беречь тебя."
    show d_us sad sport with dspr
    us_old "Сём. Мне нужно время, чтобы принять это. Про Мику. А потом… {w}Обещай, что ты мне всё-всё про вас расскажешь."
    me "Конечно, Рыжик. По дороге домой всё расскажу."
    play music music_list["so_good_to_be_careless"] fadein 1
    show mi smile pioneer with dspr
    mi "Доброе утро, Сенечка, Ульяночка, а вы ещё не завтракали?. Простите, у меня репетиция, не могу задержаться…"
    show mi smile pioneer far with dspr
    mi "Простите, но некогда, некогда…"
    hide mi with dspr
    stop music fadeout 1
    show d_us smile sport with dspr
    us_old "Пошли завтракать, Сёмк. Может, там ещё не всё съели."
    stop ambience

    scene int_dining_hall_day with squares
    play ambience ambience_dining_hall_empty
    show dv normal pioneer2 at left with moveinleft
    th "Все разошлись? Светка-копуша осталась и эти два… {w}Яйцеголовых."
    show sh normal pioneer far with dspr:
        xpos 0.8
    show el normal pioneer far behind sh with dspr:
        xpos 0.75
    hide sh with dspr
    $ renpy.pause (0.5)
    hide el with dspr
    th "Светка много места не занимает, доест свою кашу и уйдёт. А эти, кажется, на весь день тут засели. Спорят о чём-то, обсуждают. А меня в музкружке на репетиции ждут."
    th "А я тут дежурная. И столы ещё не протёрты, и пол не вымыт."
    th "Сейчас шугану эту сладкую парочку, чтобы не задерживали."
    show dv laugh pioneer2 with dspr
    th "Бегите, умники."
    show d_us normal sport at cright with moveinright:
        zoom 0.8
    us_old "Привет, Алиска!"
    show dv shocked pioneer2 with dspr
    hide d_us with moveoutright
    show d_sf smile pioneer at fright with moveinright:
        zoom 0.8
    me "Доброе утро, Алиса."
    hide d_sf with moveoutright
    th "Э-э-э…"
    dv "П-привет."
    play music music_list["afterword"]
    show dv guilty pioneer2 with dspr
    th "Что такое? Почему я их боюсь? Нет, не боюсь, а волнуюсь. Кажется, никогда так не волновалась."
    th "А тут только расслабишься, как лодка с Семёном перед глазами всплывает. И сердце колотится."
    th "Сказка Ульяны? Это же просто сказка."
    show dv normal pioneer2 with dspr
    th "Барахло на острове? Увидела мельком в прошлый раз, когда с Рыжей за земляникой плавали."
    show dv shocked pioneer2 far with vpunch
    th "Не может быть, чтобы всё было ТАК!"
    show d_sf normal pioneer at cright:
        zoom 0.8
    show d_us normal sport at fright:
        zoom 0.8
    with dspr
    me "Его уже не втянешь в спор. И не заластишь… Но кое-кто сопротивляется."
    show dv shocked pioneer2 close with dspr
    th "Теперь я просто пялюсь на Семёна с Ульяной. Замечательно. А они, кажется, обо мне только что говорили."
    show dv shy pioneer2 far with dspr
    show d_sf serious pioneer with dspr:
        zoom 0.8
    me "Это и нас с тобой, Рыжик, касается. И вообще всех."
    show d_sf sad pioneer with dspr:
        zoom 0.8
    me "Сядь, посиди с нами, Алиса. Пусть ты и считаешь, что я морочу тебе голову."
    show dv surprise pioneer2 close with dspr
    th "А ведь можно задать любой вопрос! И больше не будет приступов этих дурацких! И получить точный и понятный ответ!"
    th "Я вчера вместе с верёвкой выбросила что-то ещё, какой-то запрет. И всё. Я свободна! Но я обещала Мику, что приду."
    show dv normal pioneer2 far with dspr
    dv "Семён, можно в другой раз?"
    show dv grin pioneer2 far with dspr
    dv "Только. Неужели это правда? То, что я провожала тебя на берегу?"
    show d_sf laugh pioneer:
        zoom 0.8
    show d_us laugh sport:
        zoom 0.8
    with dspr
    me "Ага, и ещё ругалась при этом. Я уже отплыл далеко, но выражение лица и то, что у тебя губы шевелятся, я разглядел."
    show dv laugh pioneer2 far
    show d_sf normal pioneer:
        zoom 0.8
    with dspr
    show d_us smile sport with dspr:
        zoom 0.8
    dv "Интересно, чем ты заслужил такое, что я тебя провожать пошла? Хорошо хоть не галстуком махала."
    stop music fadeout 3
    hide dv with moveoutleft
    show d_sf laugh pioneer with dspr:
        zoom 0.8
    me "Почему все вы, Рыжие, такие язвы?"
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day
    show dv laugh pioneer2 with dspr
    th "Я не знаю, что это и что со мной, но я не сумасшедшая!"
    th "Вы слышите? Я не сумасшедшая!"
    stop ambience
    
    scene int_musclub_day with squares
    play ambience ambience_music_club_day
    play sound_loop ambience_medium_crowd_indoors_1
    show mi angry pioneer with moveinleft
    mi "Ребята, ну нельзя же так. Нам репетировать нужно, а вы или капризничаете, или балуетесь. От нас же ждут, что мы хорошо выступим, а что мы покажем? Как вы бумажками друг в друга кидаетесь?"
    mi "Давайте ещё раз вторую сцену, с самого начала."
    stop sound_loop
    stop ambience
    
    scene int_musclub_day with slideleft
    play ambience ambience_music_club_day
    play sound_loop ambience_medium_crowd_indoors_1
    play sound sfx_close_door_1
    show dv smile pioneer2 with moveinright
    dv "Привет народным артистам! Как дела у вас?"
    voices "Привет… Здравствуй… Здравствуй, Алиса."
    show un normal pioneer with dspr:
        xpos -0.05
    un "Здравствуй."
    hide un with dspr
    hide dv with dspr
    show dv smile pioneer2 at right with dspr
    show mi cry_smile pioneer at left with moveinleft
    mi "Здравствуй, Алисочка. Всё-всё очень плохо. Репетиция не идёт, зрители мешают, а утихомирить их я не умею. Женя сказала, что ей надоело пугалом работать, и ушла. Да я ещё и не выспалась и сейчас плохо соображаю…"
    dv "Мику, какие зрители? Те, что в окна подглядывают?"
    show dv rage pioneer2 with dspr
    dv "Сейчас я кому-то…"
    show dv laugh pioneer2 with dspr
    dv "Э-э-э… Мику, где зрители?"
    dv "Одна проблема решена."
    show dv normal pioneer2 with dspr
    dv "Давай смотреть, что вы там нарепетировали."
    stop sound_loop
    show mi normal pioneer with dspr
    mi "Очень хорошо. Ребята, начинаем с того места, где прервались."
    stop ambience
    
    scene int_musclub_day
    show dv smile pioneer2 at right
    show mi normal pioneer at left
    with slideleft
    play ambience ambience_music_club_day
    play sound dct_sfx_facepalm
    $ renpy.pause (0.5)
    dv "Тп-р-р-ру, залётные!"
    play sound_loop ambience_medium_crowd_indoors_1
    dv "\"Не верю!\". Так, кажется, да?"
    mi "А что же делать, Алисочка? Я просто не знаю даже. Просто руки опускаются."
    show mi sad pioneer with dspr
    mi "Надо было, наверное, рассказ написать. Но я-то хотела, чтобы на сцене поставить, чтобы все всё сразу увидели. Неужели я такая бездарность?"
    show dv normal pioneer2 with dspr
    dv "Знаешь, Мику. Кажется, я поняла, в чём дело. Давай мы сами сейчас прочитаем отрывок и посмотрим, что у нас получится."
    stop sound_loop
    stop ambience
    
    scene int_musclub_day with slideleft
    play ambience ambience_music_club_day
    play sound sfx_piano_head_bump
    $ renpy.pause (0.5)
    show dv smile pioneer2 with dspr
    dv "Вот, можете же!"
    "Да, так дело пошло. Пионеры к середине репетиции наконец поняли, что от них хотят, и финальная сцена прошла уже почти без сбоев."
    play sound_loop ambience_medium_crowd_indoors_1
    voice "Музыки в конце не хватает."
    #Двойник той Кати, что бегала с Сашкой по утрам в лагере бабы Глаши, кокетливая блондинка в жизни — она играла Анфису. Причём очень хорошо играла. Алиса, наблюдая за ней, несколько раз вздрагивала: «Неужели это я? Я, я же не такая!», но понимала, что да — именно такая. «Да и чёрт с ним. Я такая, какая есть!»
    dv "А кто играть будет, а, Катя?"
    voice "Ты, Алиса. Или Мику. Или я, только я никогда не играла со сцены. Или можно Семёна попросить. Я не знаю."
    hide dv with dspr
    show dv normal pioneer2 at right with dspr
    show mi normal pioneer at left with moveinleft
    mi "Катечка, ну поздно уже всё переделывать, всего две репетиции осталось. Запутаемся. Если только действительно Семёна попросить."
    dv "Правильно, Мику. Семён у тебя гитару взял — пусть теперь отрабатывает. Посадим его за ширмой, чтобы зрители не видели. Только голос."
    show dv shy pioneer2 with dspr
    dv "Только, Мику. Ты пойдёшь с ним договариваться?"
    show mi shocked pioneer with dspr
    mi "Я? Алисочка, я. Я, я… я… мне… я…"
    dv "Понятно всё. И что нам теперь делать?"
    show un serious pioneer with dspr
    un "Девочки, если надо, то я могу попросить. Всё равно без дела тут сижу. Вы пока репетируйте, а я пойду его поищу."
    hide un with dspr
    stop sound_loop
    stop ambience
    
    scene ext_aidpost_day with squares
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at fleft
    show d_us normal sport at left:
        ypos -0.05
    with dspr
    us_old "Не хочется идти, Сёмка."
    me "Не хочется, Уля. Но надо. Эх."
    stop ambience

####################
#Глава 16. Ожидание#
####################
   
label anticipation_:
    $ save_name = u"Дубликат. Четвертая смена -\nОжидание"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Ожидание" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene int_aidpost_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_day
    play music dreamers_of_the_day
    show d_to normal pioneer at left
    show cs normal at right
    d_to "Как думаешь, до чего Семён с Ульяной додумались?"
    cs "Придут — узнаем, Толя. Боюсь, до того же, до чего и мы. Но, может, найдут какую-нибудь другую возможность."
    d_to "Страшно тебе, Вилка?"
    show cs shy with dspr
    cs "Давно ты меня так не звал… Значит, тоже боишься. Очень страшно. Главное, чтобы пионеры об этом не догадались."
    play sound sfx_medpunkt_door_open
    show d_to normal pioneer at fleft with move
    show cs normal at left with move
    show d_sf normal pioneer at right with moveinright
    show d_us normal sport at fright with moveinright:
        ypos -0.05
    me "Можно, хозяева?"
    show d_to normal pioneer with move:
        xpos 0.1
    show d_us normal sport with move:
        xpos 0.9 ypos -0.05
    play sound sfx_close_door_1
    show cs smile with dspr
    cs "Заходите… {w=1}молодожёны. Устраивайтесь… {w=1}на кушеточке."
    show d_sf smile pioneer with dspr
    me "Виола-Виола… Жаль, что я вас с Анатолием почти не помню."
    show cs normal
    cs "Семён, вы же не за этим пришли…"
    stop music fadeout 1
    stop ambience

    scene ext_square_day with squares
    play ambience ambience_camp_center_day
    show un normal pioneer with dspr
    th "Где прячется Семён?"
    th "В спортзале нет, на пляже нет, на остановке нет. Ходят где-то вдвоём с Ульяной-большой, по территории или за территорией."
    show un angry2 pioneer with dspr
    th "Они взрослые — им можно за территорию."
    th "Мне шестнадцать, Славе семнадцать, а Ульяна-большая всего на два года старше Слави, а уже считается взрослой."
    show un serious pioneer with dspr
    th "Если они ушли в Старый лагерь, я должна буду получить разрешение у вожатой, чтобы сходить за ними."
    th "А Ольга Дмитриевна наверняка откажет."
    th "Ульяна-маленькая, правда, говорят, бегает туда как к себе домой, без всяких формальностей, но на то она и Ульяна."
    th "Лагерь — он, конечно, маленький, но пока всё обойдёшь. А Семёна надо до обеда найти, чтобы он хоть на одну репетицию да попал."
    voice "Лена, ты кого-то ищешь?"
    show un surprise pioneer with vpunch
    $ renpy.pause (0.5)
    show un normal pioneer with dspr
    th "Славя. Без кос смотрится очень неплохо. Если бы ещё не искала несуществующую косу руками."
    th "Правда, Славя всегда будет хорошо смотреться. И в дворницком тулупе, и в купальнике, и в космическом скафандре."
    stop ambience
    
    scene ext_square_day
    play ambience ambience_camp_center_day
    play music music_list["trapped_in_dreams"]
    show un normal pioneer at left
    show d_sl smile pioneer at right:
        ypos -0.1
    with dissolve
    sl "Лена, ты кого-то ищешь?"
    un "Здравствуй, Славя. Я Семёна ищу. Или Ульяну-большую, в крайнем случае."
    sl "Так в медпункте они оба. Ушли после завтрака, заперлись с Виолой и Толиком и о чём-то спорят непонятном. Только…"
    show d_sl shy pioneer with dspr
    sl "Только… {w=1}Ты не подумай, что я подслушивала. Я сама Семёна искала. Спросить у него об одной вещи хотела."
    show d_sl sad pioneer with dspr
    sl "А они там так кричат, а окно открыто. Только не понятно ничего. Я и ушла сразу, чтобы не подумали, что я подслушиваю."
    show un serious pioneer with dspr
    un "Спасибо, Славя, я передам Семёну, что ты его искала."
    show d_sl smile pioneer with dspr
    sl "Спасибо, Лена."
    hide un with moveoutright
    show d_sl normal pioneer at center with move:
        ypos -0.1
    th "А ещё, Лена, спасибо, что про косы ничего не спросила."
    th "Женя тоже ничего не спросила, только ворчала вполголоса."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_house_of_sl_sunset with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_evening
    play sound_loop dct_sfx_scissors
    sl "Женя, тебе не нравится?"
    stop sound_loop
    show mz bukal glasses pioneer with moveinright
    mz "Какая разница? Это же твои косы, а не мои. Но ворчать ты мне не запретишь. Думаешь, я сюда приехала, чтобы парикмахером работать?"
    stop ambience
    
    scene ext_square_day with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_sl normal pioneer at center with dspr:
        ypos -0.1
    th "А вот Ольга Дмитриевна…"
    stop ambience
    
    scene ext_square_day with pixellate
    $ prolog_time ()
    play ambience ambience_camp_center_day
    play music music_list["always_ready"]
    show mt angry panama pioneer with dspr
    mt "Ла-агерь! Напра-во! На завтрак, шагом марш!"
    show mt normal panama pioneer with dspr
    mt "Славя, останься на минутку."
    sl "Да, Ольга Дмитриевна?"
    mt "Славя, ты уже догадалась, почему я тебя задержала?"
    sl "Ольга Дмитриевна, я хочу, чтобы вы мне сами об этом сказали."
    show mt smile panama pioneer with dspr
    mt "Ты знаешь, что ещё вчера ты бы ответила по-другому? Но как скажешь."
    show mt normal panama pioneer with dspr
    mt "Славя, речь идёт о твоих косах. Именно о них."
    mt "Мне нравится твоя новая причёска. Тебе идёт, и ругать я тебя не собираюсь."
    mt "Но есть ещё твои родители, которые через десять дней увидят тебя и прибегут ко мне с вопросами."
    show mt angry panama pioneer with dspr
    mt "«Ольга Дмитриевна. Наша девочка — примерная пионерка, отличница, замечательная дочь. И вдруг такой вызывающий поступок! Почему вы не вмешались?»"
    show mt normal panama pioneer with dspr
    mt "Вот, Славя, мне понадобится твоя помощь. Посоветуй, что сказать твоим родителям: что заставило тебя взяться за ножницы?"
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with pixellate
    $ day_time ()
    play ambience ambience_camp_center_day
    show d_sl normal pioneer at center with dspr:
        ypos -0.1
    th "Что заставило? Откуда я знаю? Просто как будто давило что-то. Начиная от встречи с Семёном на пляже и до вчерашнего вечера."
    th "А вот как Женя лязгнула ножницами и две косы упали на пол, так сразу стало понятно, что всё будет… нормально. Правильно всё будет."
    th "Да ещё сон этот непонятный, который я не помню. Так, отрывки, лишённые смысла."
    show d_sl smile pioneer at left with move:
        ypos -0.1
    th "Хватит копаться в себе, нужно работать, «Хочешь, чтобы что-то было сделано хорошо — сделай это сам»."
    sl "Серёжа, помоги мне, пожалуйста."
    show el surprise pioneer at right with dspr
    el "Славя? А что случилось с твоими…{w=1} То есть, что случилось?"
    show d_sl smile2 pioneer with dspr
    sl "Ничего не случилось, Серёжа. Я тут клумбы обустраиваю, ты принеси мне, пожалуйста, два ведра воды."
    show el smile pioneer with dspr
    el "Два ведра? И всё? Я сейчас, Славя. Жди!"
    hide el with moveoutright
    show d_sl normal pioneer at center with move:
        ypos -0.1
    th "Хорошо, что Серёжа передумал спрашивать. А то я уже устала всем отвечать."
    th "Может, имя поменять? Представляться всем Славяной, тогда и про косы спрашивать не будут."
    show d_sl serious pioneer with dspr
    th "Славяна. Славяна? Славяна!"
    show d_sl laugh pioneer with dspr
    th "Нет. Я — Славя!"
    stop ambience
    
    scene int_aidpost_day with squares
    play ambience ambience_medstation_inside_day
    play music music_list["smooth_machine"]
    show cs shy at left with dspr
    cs "Кажется, наша долгая командировка закончилась. По старым законам мы заработали с Толей кучу денег, может, и на пенсию нам уже пора, надо посчитать. Вот только…"
    cs "Уля, ты собиралась что-то переписать? Так сейчас самое время, пока мужчины наши где-то ходят."
    show d_us normal sport at right with moveinright:
        ypos -0.05
    us_old "Да, а можно?"
    show cs normal with dspr
    cs "Нужно. Чтобы не пропало, чтобы вам не скатиться в невежество. Устраивайся и пиши, спрашивай что непонятно, пока я здесь."
    stop ambience
    
    scene int_aidpost_day with slideleft
    play ambience ambience_medstation_inside_day
    show cs normal with dspr
    cs "Лет ему было побольше тридцати, носил он бороду, надевал свитер, играл на гитаре… Вообще был похож на геолога или альпиниста из старого кино."
    hide cs
    show cs normal at left
    with dissolve
    show d_us normal sport at right with moveinright:
        ypos -0.05
    us_old "Вы о чём? То есть о ком, Виола?"
    cs "Да о Сёмке твоём, то есть об оригинале его. И давай на ты."
    us_old "Виола, а расскажи о нём."
    cs "О ком? О дубликате или об оригинале?"
    us_old "О моём Сёмке. Я же не знаю о нём почти ничего. И он не помнит."
    cs "А никто почти ничего не знает о твоём Сёмке. Он особо не мелькал, ну и для нас в посёлке был одним из многих."
    cs "А потом, когда всё случилось, оказалось, что он единственный из вас в активной фазе — каким-то образом его оригинал сумел это устроить и спас его от Выключателя."
    cs "Да ещё и каким-то чудом оказался в Шлюзе на тот момент. Совпадение не случайное, но концов уже не найти."
    cs "Ну и каждый человек был тогда нужен. Люди — люди-оригиналы, я имею в виду — уехали, а он вписался в нашу компанию."
    cs "А когда всё устаканилось, вдруг заявил, что пионером был, и пионером останется. И оказалось, что был прав."
    show cs shy with dspr
    cs "Теперь он остаётся, а мы уходим."
    show cs normal with dspr
    cs "Деление это, на оригиналов, подлинников и так далее — это, кстати, его оригинал придумал. Потому что миксы — это его лаборатории дело…"
    show d_us smile sport with dspr
    us_old "Тётя Виола, это вы с кем сейчас разговаривали?"
    stop music fadeout 1
    show cs smile with dspr
    cs "Да что это такое? Один Церновной обзывается, другая тётей дразнит. Совсем меня в старуху превратить хотите?"
    stop ambience
    
    scene int_aidpost_day with slideleft
    play ambience ambience_medstation_inside_day
    show cs normal at left 
    show d_us normal sport at right:
        ypos -0.05
    with dspr
    cs "Кстати, про Систему. Ты уверена в своих расчётах? Я биолог и врач, я твои формулы понимаю плохо."
    us_old "То, что Система — это мы сами? В пассивной фазе и пока спим? И то что Система способна…"
    show d_us hurt sport with dspr
    us_old "Я боюсь продолжать, Виола."
    show cs shy with dspr
    cs "Понимаю. Продолжай оттуда, откуда не боишься."
    show cs normal with dspr
    show d_us normal sport with dspr
    us_old "Да. Глафира Денисовна это доказала, сама испугалась, не поверила и почти ничего записывать не стала, только намёки, а мне их двое суток расшифровывать пришлось."
    us_old "И даже вы с Анатолием в этом участвуете, хоть вы между циклами остаётесь здесь, а… Вы же в бомбоубежище отсиживаетесь, да?"
    us_old "Потому и противоречие, потому всё и разваливается, что те, кто уже проснулся, тянут в одну сторону; вы привязаны к тому миру, что снаружи. А те, кто спят — в третью. Вот и разваливается всё. Потому Сёмка и предложил вам уйти через теплообменник."
    show cs shy with dspr
    cs "Есть ведь ещё и Выключатель. Чтобы привести всё к одному вектору."
    us_old "Виола, ты о чём? Я не согласна, имей в виду. А Выключатель и у Сёмки есть."
    show cs normal with dspr
    cs "Да не переживай ты. Это я о своём."
    play sound sfx_dinner_jingle_normal
    cs "Вот и обед. Пойдём? Или дальше писать будешь?"
    us_old "Пойдём, Виола."
    stop ambience

    scene ext_dining_hall_near_day with squares
    play ambience ambience_camp_center_day
    show mt normal pioneer at cleft with dspr
    show cs normal at cright with moveinright
    cs "Привет, Оля."
    show d_us smile sport at right with moveinright:
        ypos -0.05
    us_old "Привет, Оля."
    hide cs with dspr
    mt "Здравствуйте, Виола, Ульяна."
    hide d_us with dspr
    show mt smile pioneer at center with move
    th "Полдня прошло без происшествий. Не считать же происшествием обрезанные косы у помощницы вожатой."
    show mt normal pioneer at cleft with move
    show d_sl smile pioneer at right with moveinright:
        ypos -0.1
    sl "Здравствуйте, Ольга Дмитриевна."
    mt "Здравствуй, Славя."
    hide d_sl with dspr
    show mt normal pioneer at center with move
    play music music_list["farewell_to_the_past_edit"]
    th "Славя так и не созналась, зачем она это сделала, но выглядело неплохо. Хуже точно не стало, а Славя стала казаться серьёзнее. Взрослее и солиднее."
    th "И вести себя начала чуть иначе. Да хоть с косами этими же."
    stop ambience
    
    scene ext_square_day with pixellate
    $ prolog_time()
    play ambience ambience_camp_center_day
    show d_sl serious pioneer at center with dspr:
        ypos -0.1
    mt "И всё-таки, Славя, что произошло?"
    show d_sl smile2 with dspr
    sl "Ольга Дмитриевна, есть ли ко мне претензии? И если есть, то какие?"
    th "Как отсекла дальнейшую дискуссию."
    th "Вот так внезапно взяла и повзрослела. Интересно, кем она станет? Вот отправить её в педагогический, а лет через пять я бы с удовольствием ей своё место отдала."
    mt "Очень твои косы всем нравились, Славя, теперь привыкай обходиться без них."
    show d_sl normal pioneer with dspr
    mt "Я не только о том, что ты их до сих пор руками ищешь. Держишься хорошо, но заметно, что нервничаешь."
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_near_day with pixellate
    $ day_time()
    play ambience ambience_camp_center_day
    show mt normal pioneer at cleft with moveinleft
    show dv smile pioneer at right with moveinright
    dv "Здравствуйте, Ольга Дмитриевна."
    mt "Здравствуй, Алиса. Как дела у тебя?"
    show dv laugh pioneer with dspr
    dv "Лучше всех!"
    hide dv with dspr
    show mt smile pioneer with dspr
    th "Кажется, у Алисы и правда всё хорошо. И она снова смотрит на меня весело и нахально."
    show d_sf normal pioneer at right
    show un serious pioneer at center
    show mi normal pioneer at fright
    with moveinright
    mi "Сенечка, что за отдача? Как она работает? Здравствуйте, Олечка Дмитриевна."
    mt "Мику, как подготовка? Не сорвёте?"
    hide un
    hide d_sf
    with dspr
    show mi happy pioneer at cright with dspr
    mi "Всё замечательно, Ольга Дмитриевна. Ещё и Семён согласился нам помочь!"
    mt "Тогда я делаю объявление."
    hide mi with dspr
    show d_to moron pioneer at right with moveinright
    d_t1 "Ы-ы-ы…"
    show mt normal pioneer with dspr
    mt "Проходи уже."
    hide d_to with dspr
    th "Бр-р-р."
    th "Хорошо, что он безобидный. И всё же надо поговорить с Виолой, чтобы на следующую смену она его не привозила."
    show us smile pioneer at right with easeinright
    us "ЗдрасьтеОльмитревна!"
    hide us with dspr
    th "Отчитать её за то, что опаздывает, а заодно напомнить про запрет выхода за территорию?"
    mt "Ульяна, руки мыла?"
    show us smile pioneer at right with dspr
    us "А как же, Ольмитревна!"
    hide us with dspr
    th "Кажется, все зашли."
    show cs normal at right with dspr
    cs "Оля, совсем забыла тебе сказать."
    show cs shy with dspr
    cs "В общем, Толю надо будет везти в райцентр, в больницу."
    cs "И я поеду с ним как сопровождающая и ответственная."
    cs "Насчёт замены я уже договорилась. В воскресенье приедет новый доктор, а мы уедем. Жаль, мне здесь нравилось."
    show mt surprise pioneer with dspr
    mt "Вот это новость, Виола."
    show mt sad pioneer with dspr
    mt "Мне тоже жаль с тобой расставаться."
    show mt normal pioneer with dspr
    mt "Но раз надо, значит надо. В конце концов, это жизнь."
    hide cs with dspr
    th "Жалко расставаться с Виолой, но ничего не поделаешь: это не эпидемия дизентерии, не побег пионера на лодке, не беременность одной из пионерок; это не ЧП, а нормальное течение жизни."
    hide mt with dspr
    stop ambience
    
    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    show mt normal pioneer with moveinleft
    $ renpy.pause (0.5)
    mt "Мику, ещё раз. Всё в порядке?"
    show mi shocked pioneer far at left behind mt with dspr
    mi "Конечно, конечно. Олечка Дмитриевна, я…"
    show mt angry pioneer with dspr
    mt "Внимание, пионеры, персонал и гости лагеря!"
    hide mi with easeoutleft
    show mt normal pioneer with dspr
    mt "Сегодня после ужина на концертной площадке театральный кружок покажет пьесу, сочинённую нашей Мику."
    show mt smile pioneer with dspr
    mt "В общем, будет двойная, нет — тройная премьера: премьера автора, премьера спектакля и премьера труппы."
    mt "А сейчас всем приятного аппетита."
    hide mt with dspr
    $ renpy.pause (1)
    $ set_mode_nvl ()
    "Что-то ещё беспокоило Ольгу Дмитриевну. То же самое неясное предчувствие непонятных перемен, что и утром."
    "И поэтому известие о том, что Толика нужно везти в город, вожатая восприняла даже с облегчением: кажется, ничего страшного."
    "Ольга Дмитриевна не могла видеть, что лагерь сейчас напоминает бак с перегретой водой, в который попало несколько пылинок; вокруг этих пылинок уже начали образовываться первые пузырьки пара, и вода в котле вот-вот вскипит, сразу и во всём объёме."
    "Следующий цикл обещал быть очень интересным. Система это фиксировала, и Ольга, как человек связанный с Системой, эту фиксацию подсознательно воспринимала, а уже сознание Ольги трактовало полученную информацию как ожидание перемен."
    "Нервное, но не тоскливо-безнадёжное, кстати, ожидание."
    $ set_mode_adv ()
    stop ambience

########################
#Глава 17. Чужая память#
########################
   
label strange_memory:
    $ save_name = u"Дубликат. Четвертая смена -\nЧужая память"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Чужая память" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene int_dining_hall_people_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    play music music_list["i_want_to_play"]
    show d_sf normal pioneer at left:
        ypos 0.1
    show d_us normal sport at right:
        ypos 0.05
    with dspr
    us_old "Сёмк, мне твой голубец жалко. Ты его или съешь уже, или отставь."
    show d_us smile sport with dspr
    us_old "А ты сеанс стриптиза ему устроил. Мясо отдельно, капуста отдельно, и всё равно не ешь, а только вилкой ковыряешь."
    me "Не повезло мне, Рыжик. Опять на гитарке петь заставляют. А мне ничего в голову не идёт."
    show d_us normal sport with dspr
    us_old "Ничего, Сёмк. «Петь на гитарке» у тебя наследственное, оказывается. Я это сегодня от Виолы узнала."
    show d_us smile sport with dspr
    us_old "Только ты, главное, смотри там, на Мику не заглядывайся. Мне-то сколопендру поймать недолго."
    me "За что ж ты так её?"
    us_old "Кого?"
    show d_sf laugh pioneer with dspr
    me "Да Мику же. Сколопендрой вот обозвала."
    show d_us laugh sport with dspr
    us_old "Ах ты! Сёмк, иногда видно, что ты вовсе не такой зануда, каким хочешь казаться."
    stop music fadeout 1
    stop ambience
    
    scene int_dining_hall_people_day with pushright
    play ambience ambience_dining_hall_full
    show d_sf normal pioneer at left:
        ypos 0.1
    show d_us normal sport at right:
        ypos 0.05
    with dspr
    us_old "А я ведь так и не прочитала пьесу. Некогда было."
    me "Вот сразу и посмотришь. Свежим взглядом."
    show d_sf sad pioneer with dspr
    me "Рыжик мой, я домой хочу. Не хочу я ни мировые проблемы решать, ни проблемы лагерного масштаба, ни чьи-то личные."
    me "Здесь посмотрел на девочек, успокоился, и уже хочу домой."
    show d_us normal sport with move:
        xpos 0.4 ypos 0.05
    us_old "Завтра дома будем, Сём. В восемь вечера надо в точке перехода быть, и идти недалеко. Так что к ужину, конечно, не успеем, но к ночи будем."
    show d_sf normal pioneer with dspr
    me "Я представляю, как там из-за нас волнуются. Уходили на сутки — почту передать, и застряли тут из-за моей спины."
    us_old "Сём. Прости меня. Это я тебе столько лишнего в рюкзак положила."
    me "Уля, не выдумывай. Пошли лучше прогуляемся, проводишь меня до кружка. А то ты как засела за свою писанину, так и не выходила."
    me "Я даже беспокоился, не заболела ли, не подменили ли."
    show mi normal pioneer far with dspr:
        xpos 0.7
    $ renpy.pause (1)
    hide d_sf
    hide d_us
    with dspr
    show mi normal pioneer far at center with move
    $ renpy.pause (1)
    stop ambience

    scene int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    play music music_list["so_good_to_be_careless"]
    show mi normal pioneer with dspr
    th "Кажется, Семён с Ульяной обо мне разговаривают. Да ещё сон этот. Когда во сне назвали Микусей, и это было хорошо, а потом стало так горько…"
    th "Некогда. Жалко, но некогда… Постановка важнее."
    th "Генеральная репетиция: прослушать, что там Семён споёт, всех артистов распустить до вечера, договориться с кибернетиками о реквизите и декорациях."
    th "Интересно, как спектакль примут? Нет, это будет интересно вечером, через час после ужина."
    th "Всё, всё, всё потом… А сейчас репетиция."
    hide mi with easeoutleft
    stop ambience
    
    scene int_musclub_day with squares
    play ambience ambience_music_club_day
    play sound sfx_close_door_1
    show mi normal pioneer with easeinright
    mi "Все пришли с обеда? Тогда — последний прогон!"
    stop music fadeout 1
    stop ambience

    scene ext_musclub_day with dissolve
    play ambience ambience_camp_center_day
    show d_us normal sport at center with dspr:
        ypos -0.05
    th "Сёмка пристроен, а мне чем заняться? На пляж без Сёмки не хочется, сестрёнка пропала в Старом лагере, мелких не видно. Не в медпункт же идти?"
    th "Попроситься в гости на репетицию?"
    play sound sfx_slavya_run
    voice "Ульяна!"
    $ renpy.pause (1)
    show d_us normal sport with move:
        xpos 0.2 ypos -0.05
    $ renpy.pause (1)
    show d_sl smile2 pioneer at right with moveinright:
        ypos -0.1
    sl "Мне…"
    show d_sl scared pioneer with dspr
    sl "…мне очень нужно с вами поговорить!"
    $ set_mode_nvl ()
    "Ульяна вспомнила, как Семён, когда он с больной спиной только вернулся из посёлка Шлюз и отлёживался в тренерской, выползая лишь в столовую, сказал ей, уже на равных: «Будь готова к тому, что пионеры — те, кто ещё не проснулся — будут бегать к тебе со своими проблемами, как к подруге или как к психологу. Может, чувствуют они в таких как мы что-то?»"
    "Но дома как-то так вышло, что если бегали, то бегали больше к Семёну (Ну как больше? Далеко не каждый цикл бегали даже. Всего-то и было раз пять или шесть. Сёмка после всегда ворчал, но никогда никого не прогонял и никогда о чужих проблемах не рассказывал). А остальные три проснувшиеся девочки были избавлены от этого."
    "Один такой «пациент» сказал потом: «Ну, понимаешь, Семён, можно, конечно, и к вожатой, но это как наябедничать получается. Если она что узнала, она не будет разбираться, она будет меры принимать и наказывать кого попало. А ещё будет кричать. А ты хоть и начальник, а свой. Даже если накажешь, то не обидно. И никогда не кричишь»."
    "А тут Славя пришла с бедой к Ульяне."
    $ set_mode_adv ()
    us_old "Если нужно, то пожалуйста. И, Славя, мы же на ты, не забыла?"
    show d_sl shy pioneer with dspr
    sl "Прости, я забыла от волнения — конечно, на ты."
    show d_sl normal pioneer with dspr
    sl "Только давай уйдём куда-нибудь. Где не помешает никто."
    us_old "Где никто не помешает? Это значит, не на площадь, не в домики и не в спортзал. Пойдём за сцену. Если хочешь, то пойдём вкруговую, вдоль забора."
    show d_us smile sport with dspr
    us_old "Чтобы вожатую не беспокоить."
    stop ambience
    
    
    scene ext_washstand_day with slideleft
    play ambience ambience_camp_center_day
    play music music_list["door_to_nightmare"]
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    sl "Ульяна, ты прости, что к тебе обращаюсь, но мне просто не к кому. Тем более что ты…"
    us_old "Тем более что я завтра уйду и никому ничего не разболтаю? Так?"
    show d_sl scared pioneer with dspr
    sl "Да.{w=1} Нет.{w=1} Не только…{w=1} Понимаешь…"
    stop music fadeout 1
    stop ambience
    
    scene ext_path_day with slideright
    play ambience ambience_forest_day
    $ set_mode_nvl ()
    "Не пошли они ни к какой сцене. Где-то было слышно, как пионеры играют в футбол, где-то вожатая искала свою помощницу, где-то Виола сформулировала мысль и искала Ульяну, чтобы поделиться с той до своего ухода."
    "А девушки просто неторопливо гуляли по лагерному лесу, переходя с тропинки на тропинку."
    $ set_mode_adv ()
    play sound_loop dct_sfx_steps2
    show d_us normal sport at right:
        ypos -0.05
    show d_sl scared pioneer at left:
        ypos -0.1
    with dspr
    sl "Понимаешь, вот как увидела вас с Семёном. Так у меня с памятью стало что-то происходить."
    sl "Постоянно вспоминаются такие вещи, что происходили не со мной, но одновременно и как бы со мной."
    sl "Вот хоть прихожу я к умывальнику, а там твой Семён…"
    show d_sl normal pioneer with dspr
    sl "Ой, смотри — земляника."
    stop sound_loop
    stop ambience
    
    scene ext_polyana_day with dissolve
    play ambience ambience_camp_center_day
    "Земляника была мелкая, было её немного, но задержаться около неё стоило."
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    us_old "Там Сёмка, так."
    play sound music_list["trapped_in_dreams"]
    sl "Да. Мы поздоровались, он ушёл, а я осталась умываться. А пока умывалась, вдруг вспомнила, как мы с Ольгой Дмитриевной делали пробежку утром и застали его около умывальника же, а он там, голый по пояс, обливался ледяной водой. Бр-р-р-р."
    sl "И главное — я точно знаю, что этого не было никогда, а Ольга Дмитриевна бегает только в исключительных случаях."
    show d_sl scared pioneer with dspr
    sl "Но я же помню! И какой спортивный костюм был на Ольге Дмитриевне, и то, что я поддразнивала Семёна там, у умывальников."
    us_old "Я слушаю тебя, Славя. Идём дальше?"
    show d_sl smile pioneer with dspr
    sl "Да, идём."
    stop ambience
    
    scene dct_ext_backroad_day_7 with slideleft
    play ambience ambience_forest_day
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    us_old "За территорию?"
    sl "Пойдём. Ни разу ещё не бывала за забором, всё некогда. Только на остановке."
    play sound_loop dct_sfx_steps2
    show d_sl shy pioneer with dspr
    sl "И есть ещё озеро, я туда купаться хожу."
    show d_sl normal pioneer with dspr
    show d_us smile sport with dspr
    us_old "Ага, я знаю это озеро. Если хочешь, можно и туда завернуть. Но ты про воспоминания и про Сёмку рассказывала."
    sl "Да там не только про Семёна воспоминания. Бывают и просто про меня, про лагерные дела."
    sl "Обычные воспоминания о том, что я могла бы делать, но точно знаю, что не делала."
    sl "А бывает, что вспоминаю что-то как давно прошедшее, а на следующий день это что-то происходит. Вот вроде голубцов сегодня на обед."
    stop music fadeout 1
    stop sound_loop
    stop ambience
    
    scene ext_path2_day with slideright
    play ambience ambience_forest_day
    "В лесу без ветра было по-особенному душно — обычный жаркий день бесконечного лета."
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    us_old "Уфф, жара. Может, к озеру сходим?"
    sl "Да. Духота. Давай искупаемся."
    stop ambience
    play sound sfx_click_2
    
    scene ext_path2_day with slideleft
    play ambience ambience_forest_day
    "Разговор незаметно отклонился от главной темы."
    show d_us smile sport at right:
        ypos -0.05
    show d_sl smile pioneer at left:
        ypos -0.1
    with dspr
    us_old "Славя, расскажи, как ты стала помощником вожатой?"
    sl "Ну-у-у. Я не знаю — мы, когда приехали, из автобуса выбрались, Ольга…"
    stop ambience
    play sound sfx_click_2
    
    scene ext_path2_day with slideright
    play ambience ambience_forest_day
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    sl "А теперь моя очередь спрашивать…"
    stop ambience
    play sound sfx_click_2
    
    scene ext_path2_day with slideleft
    play ambience ambience_forest_day
    show d_us smile sport at right:
        ypos -0.05
    show d_sl smile pioneer at left:
        ypos -0.1
    with dspr
    us_old "Славя, а ты купальник взяла?"
    show d_sl smile2 pioneer with dspr
    sl "А зачем? Здесь всё равно никто не ходит."
    show d_sl normal pioneer with dspr
    sl "Ульяна.{w=1} Вот только.{w=1} Я тебе ещё не всё рассказала."
    play music music_list["door_to_nightmare"]
    show d_sl scared pioneer with dspr
    sl "Самое страшное воспоминание — это как меня убивают. Не Семён, но кто-то очень на него похожий."
    sl "Вот я и хочу тебя спросить, Ульяна. Ты меня раньше не знала, и действительно уйдёшь завтра. Может быть, сможешь сказать как есть. Я понимаю, что я сошла с ума, но скажи — я похожа на нормальную?"
    stop music fadeout 1
    stop ambience
    play sound sfx_click_2

    scene ext_path_day with slideright
    play ambience ambience_forest_day
    "К счастью, мгновенного ответа не требовалось."
    "Девушки успели искупаться и уже возвращались в лагерь, когда Ульяна наконец нашла нужные слова."
    "Семён когда-то делился с ней своим опытом общения с ещё не проснувшимися пионерами, которые вот-вот проснутся. Но всё вылетело из головы."
    "Осталась только фраза: «Я тогда подумал, что вот я тебе вечером совру, а твой разум возьмёт и проснётся утром. И что мне? На сто восемьдесят градусов разворачиваться? Так я слишком ленивый для этого. Лучше было правду сказать, и наплевать на то, что ты в неё не поверишь»."
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    us_old "Славя, тебе, наверное, повезло."
    show d_sl serious pioneer with dspr
    sl "Повезло? Как?"
    us_old "…мне сейчас всё равно, поверишь ты или нет, я действительно уйду завтра. Но ты не похожа на нормальную, ты и есть нормальная!"
    us_old "А твои «лишние» воспоминания — это называется «чужая память». Не твоя, а чужая — твоих двойников. Просто кто-то может ей пользоваться, а кто-то нет."
    us_old "Я, например, нет, а Сёмка может. И ты, получается, можешь. Только ты ещё учишься ей пользоваться. Но повезло тебе не поэтому."
    us_old "В моём лагере нет твоего двойника, там живёт другая девочка. Похожая на тебя, но другая. Так что ты единственная Славя, которую я знаю."
    us_old "Но то, что я вижу… В общем, я уверена, что никто из твоих двойников никогда и никому не причинил зла, и {b}таких{/b} воспоминаний у тебя не будет."
    show d_us sad sport with dspr
    us_old "А у моего Сёмки они есть."
    stop ambience
    play sound sfx_click_2
    
    scene ext_no_bus with slideleft
    play ambience ambience_camp_entrance_day
    "Обратно шли молча, свернув на знакомую Славе тропинку, выводящую к остановке. Ульяна, чем-то расстроенная, молчала. Славя же не знала, как отнестись к словам гостьи. С одной стороны, Ульяне не было нужды её обманывать, а с другой — всё это звучало как продолжение вчерашних фантазий ребятишек из младшего отряда."
    show d_us normal sport at right:
        ypos -0.05
    show d_sl normal pioneer at left:
        ypos -0.1
    with dspr
    sl "Ульяна, если я сейчас нечаянно коснулась какой-то тайны…"
    play music anewbeginning fadein 2
    stop ambience

    scene ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day
    show d_us normal sport at center with moveinright:
        ypos -0.05
    us_old "Это не ты, Славя, тайны коснулась. Это мы тебя в неё нечаянно макнули. Скоро всё сама поймёшь. Дней через восемь-девять точно."
    show d_us smile sport with dspr
    us_old "Не бойся, теперь уж тебя одну не оставим. Главное — следующей среды дождитесь."
    us_old "Всё, прости, я к Сёмке побежала."
    hide d_us with dspr
    stop music fadeout 1
    stop ambience
    
#######################
#Глава 18. Точки над Ё#
#######################
   
label dots_over_yo:
    $ save_name = u"Дубликат. Четвертая смена -\nТочки над Ё"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Точки над Ё" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene ext_clubs_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at center with dspr
    us_old "Сёмк, подожди!"
    show d_sf smile pioneer at cleft with move
    show d_us smile sport at cright with easeinright:
        ypos -0.05
    show d_sl normal pioneer at center with moveinleft
    me "Здравствуй,{w=1} Славя."
    show d_sl scared pioneer with dspr
    sl "Здравствуй."
    hide d_sl with easeoutright
    me "Как вода в озере?"
    us_old "А ты откуда знаешь, что мы на озере были?"
    me "Элементарно, Ватсон. Вы со Славей были за территорией — это раз. Волосы у тебя и у неё ещё влажные — это два. Пахнут озёрной водой — это три. А самое главное — это тот предмет одежды, который утром был у тебя под футболкой, а сейчас ты держишь его в руках."
    show d_us laugh sport with dspr
    us_old "Да ну тебя, Холмс! Пошли?"
    stop ambience
    
    scene ext_houses_day with dissolve
    play ambience ambience_camp_center_day
    play music music_list["a_promise_from_distant_days"]
    show d_sf normal pioneer at cleft
    show d_us normal sport at cright:
        ypos -0.05
    with dspr
    us_old "Знаешь, Сём. Славя что-то начинает понимать. О чём-то догадываться. У неё…{w=1}появились вопросы. А я ей сказала, что она скоро всё сама поймёт. И, Сём. Придётся на следующий цикл сюда прийти. Я Славе пообещала, что одну её не оставим."
    me "Славя, Алиса, может быть, Ульянка и Мику. Лена вряд ли. А что из себя представляет здешний мой двойник, я не знаю. Да, нам придётся заглянуть."
    stop ambience
    
    scene ext_square_day with dissolve
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at fleft
    show d_us normal sport at cleft:
        ypos -0.05
    with dspr
    us_old "Вот только Ольга не меняется. Хотя она столько видела, что могла бы и сама измениться."
    me "Ольге незачем меняться."
    us_old "Ой! Вот она."
    show d_us normal sport at left with move:
        ypos -0.05
    mt "… а теперь поговорим о грязи в вашем домике!"
    voice "Ну Ольга Дмитриевна…"
    show mt rage panama pioneer far at fright with dspr
    $ renpy.pause (1)
    show mt normal panama pioneer far with dspr
    $ renpy.pause (1)
    show mt sad panama pioneer far with dspr
    me "Да. Монитору узла незачем меняться."
    stop ambience
    
    scene dct_ext_square_day with pixellate
    $ prolog_time ()
    #$ renpy.ambience.set_volume(0.1)
    play ambience ambience_camp_center_day
    th "Всё возвращается… Последние люди возвращаются домой. Семён вернулся туда, откуда начинал. В кои-то веки активация и побег пошли кому-то на пользу."
    th "Поговорить с ним? Поздороваться, наконец. Но ситуация не чрезвычайная, я же не смогу и рта раскрыть. За меня будет говорить даже не Матрица, а Ментор, а что она скажет?"
    th "Что нужно активнее участвовать в лагерной жизни? Что этому лагерю тоже нужен физрук? И это в лучшем случае. Даже если Семён разговорит Матрицу, то она только поулыбается и скажет, что Семён молодец."
    th "Как это всё-таки плохо: всё знать, всё помнить, всё понимать, а общаться только раз в две недели с себе подобными."
    th "С сестрёнками, как обе Ульяны, не сговариваясь, назвали друг друга. Да, с сестрёнками. А я теперь ему даже привет от своей сестрёнки передать не могу."
    th "Может, всё-таки бросить это дело, пустить узел на самотёк? Но Монитора и Матрицу жалко. Тоже личности своего рода. И одиночество. Так хоть с сестрёнками могу общаться, а иначе — только со случайно проснувшимися пионерами."
    th "А ещё — страшно."
    show d_sf normal pioneer at center with dspr
    mt "{i}Я рада, что ты заглянул к нам.{/i}"
    me "{i}Я тоже был рад всех увидеть, даже Ольгу Дмитриевну. Теперь будем заглядывать.{/i}"
    mt "{i}Заглядывайте.{/i}"
    voice "Ольга Дмитриевна, можно я пойду?"
    stop music fadeout 1
    stop ambience
    #$ renpy.ambience.set_volume(1)
    
    scene ext_square_day with vpunch
    $ day_time ()
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at fleft
    show d_us normal sport at cleft:
        ypos -0.05
    show mt normal panama pioneer far at fright
    with dspr
    voice "Ольга Дмитриевна, можно я пойду?"
    mt "Да-да, иди, конечно. Мне тоже нужно идти."
    hide mt with dspr
    $ renpy.pause (1)
    stop ambience
    
    scene ext_playground_day with squares
    play ambience ambience_soccer_play_background
    play music feeling_good
    "До ужина оставалось ещё целых три часа, и в бедном на события «Совёнке» всё замерло."
    "Мелкие сосредоточились на футбольном поле. Все, кроме Артёма."
    stop ambience
    
    scene dct_ext_house_of_kids_day with squares
    play ambience ambience_camp_center_day
    "Артём остался у себя в домике и что-то писал на вырванном из тетрадки двойном листе."
    stop ambience
    
    scene dct_ext_beach_day_with_pass_train with squares
    play ambience dct_ambience_beach
    "Средний отряд, включая артистов, оккупировал пляж."
    stop ambience
    
    scene ext_house_of_dv_day with squares
    play ambience ambience_camp_center_day
    "Алиса учила роль. Ей всё-таки навязали роль Оксаны Сергеевны, и сейчас, когда Ульянки не было, она ходила по домику и повторяла реплики."
    "Она бурчала про себя, что её заставили, но в глубине души была рада. Участие в спектакле, как ни странно, приводило в порядок её мысли и успокаивало."
    stop ambience

    scene dct_ext_cliff_day with squares
    play ambience ambience_lake_shore_day
    "Ульяна-маленькая осваивала территорию Старого лагеря, и в данный момент сидела над берегом, свесив ноги с обрыва и разглядывая речной простор во «временно позаимствованный» в клубах бинокль (кибернетики запирали двери, но всегда забывали про форточки)."
    stop ambience
    
    scene ext_square_day with squares
    play ambience ambience_camp_center_day
    "Славе нужно было обдумать разговор с Ульяной-большой, поэтому она опять занялась цветами на площади."
    stop ambience
    
    scene dct_ext_stage_big_day with squares
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_hammering
    "Кибернетики решили, что лучше уступить Мику, чем отбиваться, и обустраивали сцену, старательно заглушая стуком молотков бесконечный монолог руководителя музыкального кружка."
    stop sound_loop
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day with squares
    play ambience ambience_camp_center_day
    show d_sf normal pioneer at fleft
    show d_us normal sport at cleft:
        ypos -0.05
    with dspr
    us_old "Сёмк, может, ягоды наберём? Пролезем под хозяйственные ворота, а дальше…"
    cs "Клубнички захотелось{w=1}… молодожёны?"
    hide d_sf with dspr
    stop ambience
    
    scene ext_dining_hall_away_day with pixellate
    play ambience ambience_camp_center_day
    $ prolog_time ()
    show d_us shy sport at center with dspr:
        ypos -0.05
    th "Интересно, почему Виоле так нравится изрекать пошлые двусмысленности?"
    stop ambience
    
    scene ext_dining_hall_away_day with pixellate
    play ambience ambience_camp_center_day
    $ day_time ()
    show d_sf normal pioneer:
        xpos 0.65
    show d_us normal sport at right:
        ypos -0.05
    with dspr
    show cs shy at left with moveinleft
    cs "А мы вот ходим и прощаемся."
    show d_to normal pioneer with moveinleft:
        xpos -0.1
    us_old "Составить вам компанию?"
    show cs normal with dspr
    cs "Нет, не беспокойтесь, Ульяна. Хотя{w=1}… составьте, нам будет приятно."
    stop ambience
    
    scene dct_ext_beach_day_with_pass_train with dissolve
    play ambience dct_ambience_beach
    play music music_list["trapped_in_dreams"]
    $ renpy.pause (1)
    show cs shy with dspr
    cs "Вот так каждый раз. Они купаются, а ты следишь за ними. А потом, скажем, Максим и Витя, вот как сейчас, начинают бегать друг за другом. Игра у них такая, дети же. Выскакивают на асфальт…"
    $ set_mode_nvl ()
    cs "И кто-то из них обязательно спотыкается, и его приводят к тебе с разбитым носом, шатающимся зубом и очень живописным животом в вертикальную красную полоску. Но главное — с торчащим из этого живописного живота куском арматуры. Или острым сучком. Или ещё чем-то подобным. \nСлавя бегает, Ольга бегает, обе плачут. А ты знаешь, что независимо от твоих трудов пионер завтра будет как огурчик, но всё равно делаешь всё как надо.\nОбрабатываешь его по полной программе, потому что давала клятву лечить людей. Да и просто его жалко. Пионер-то не знает, что он завтра будет как огурчик, и страдает по-настоящему. И все вокруг страдают."
    nvl clear
    cs "А через две недели ты, кажется, принимаешь все меры, но калечится уже другой пионер: или током бьёт кого любознательного, или кто с качелей летит. И всё повторяется снова.\nИ ты принимаешь и принимаешь меры, и понимаешь, что бороться с этим — это как головы у змея рубить. Что всё это зашито в программу, которую сама для себя составила Система.\nИ если ты, Ульяна, говоришь, что Система — это мы сами, то непонятно, для чего это Системе нужно. И тебе пионеров жалко, в том числе и поэтому, и ещё за этот замкнутый цикл жалко, в который их сама же запихнула, а теперь не знаешь, как оттуда выдернуть.\nИ ты изображаешь из себя чудовище, чтобы не подпускать пионеров к себе, чтобы не пускать их себе в душу, а потом эта маска так прирастает, что уже не можешь остановиться. Но ты всё равно помнишь их всех по именам и все их болячки по циклам."
    nvl clear
    cs "А пионер, который опаздывает на неделю, и всё, что мы смогли сделать для которого — это поселить в этом лагере, у себя на глазах, тычется, как слепой котёнок и, кажется, не собирается просыпаться.\nА потом он внезапно сбегает, сначала подняв на уши, а потом вогнав в столбняк весь лагерь. И жизнь в лагере буквально останавливается. Все ходят как в воду опущенные, и столовая не работает, и даже на приезд автобуса обитатели не реагируют.\nИ ты уже подумываешь, не применить ли прибор и не сбросить ли текущий цикл у пионеров, но рука не подымается.\nА сбежавший пионер не появляется на следующую смену. Вместо него через несколько циклов приезжает копия с нулевой памятью, и ещё является проекция того… пионера-искусителя."
    nvl clear
    cs "А сбежавший пионер пропал, о нём никаких известий, и ты волнуешься, не встретился ли он с этим же самым пионером. Приборы не показывают изменения состояния Сети, но что приборы…\nА потом тревога: сброс ста восьми килограмм массы через теплообменник, и тебе опять ничего не понятно. Пока однажды не умудряется дозвониться Денисовна…"
    $ set_mode_adv ()
    show cs normal with move:
        xpos 0.75
    show d_to normal pioneer at left with moveinleft
    d_to "Пойдём дальше, Вилка. Это уже только воспоминания, а скоро и воспоминаний не будет."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_boathouse_day_with_pass_train with pushleft
    play ambience ambience_boat_station_day
    pause
    stop ambience
    
    scene dct_ext_boathouse_alt_day_7dl with dissolve
    play ambience ambience_boat_station_day
    play music music_list["farewell_to_the_past_full"]
    show d_to normal pioneer at left with dspr
    show d_sf normal pioneer at right with moveinright
    d_to "Устали мы, Семёныч. Потому и сбегаем так легко."
    me "По Виоле видно, как это легко. Если это легко, Толь, то что же тогда тяжело?"
    me "Лучше скажите. Как вы думаете, что будет после вашего ухода?"
    show d_sf normal pioneer at center with move
    show d_us sad sport at right with moveinright:
        ypos -0.05
    us_old "Я скажу, Сём. Закроется этот ваш переход через теплообменник. Потому что он держался только на убеждении Виолы, Анатолия и, раньше ещё, бабы Глаши, что всё происходит именно так."
    us_old "Это за три-четыре цикла произойдёт. Но небольшая вероятность попадания сюда или ухода отсюда сохранится. Не смейся, но при помощи магических действий. Неважно каких, главное — верить, что магия поможет."
    us_old "Это потому что у этой вероятности появится мнимая часть."
    show d_to smile pioneer
    d_to "Пойдём, Уля. Нам ещё столько обходить. А по дороге расскажешь."
    stop music fadeout 1
    stop ambience

    scene ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day
    show dv normal pioneer far with dspr
    $ renpy.pause (1)
    show dv surprise pioneer far with dspr
    $ renpy.pause (1)
    hide dv with dspr
    #Алиса, привлечённая голосами, выглянула из дверей, увидела Анатолия. Не Толика, а именно Анатолия: подтянутого, быстрого, опасного, сканирующего окрестности цепким взглядом. Округлила глаза и спряталась обратно в домик.
    $ renpy.pause (1)
    show d_sf smile pioneer at right with dspr
    me "Толяныч, видишь, как ты на детей действуешь?"
    show d_to smile pioneer at left with dspr
    d_to "Ничего, потерпит. Недолго терпеть осталось."
    show cs normal with dspr:
        xpos -0.05
    show d_us smile sport at center with dspr:
        ypos -0.05
    us_old "Так я продолжу?"
    show d_us normal sport with dspr
    us_old "Ещё несколько сотен циклов, и у этой вероятности почти полностью исчезнет реальная часть."
    show d_to normal pioneer with dspr
    d_to "«У вероятности исчезнет реальная часть…» — это как?"
    us_old "Что значит «Как»? Сниться будем друг другу, а попасть изнутри наружу и наоборот будет практически невозможно."
    us_old "Практически нужно будет опять водородную бомбу взрывать и, воспользовавшись энергетическим импульсом, создавать пузырь свёрнутого пространства, а из него уже пробивать каналы сюда."
    us_old "Вот только попадёшь ли именно сюда? И вообще, что такое мнимая вероятность — не спрашивай, этого даже Глафира Денисовна внятно объяснить не смогла."
    us_old "Да, Шлюз продублируется. Примерно по тому же механизму, как продублировались лагеря. Один останется здесь, а второй схлопнется и станет для нас недоступен."
    us_old "И всё это случится за те же несколько сот циклов. Он ведь построен в таком пузыре. Как это будет выглядеть снаружи, я не знаю. Мне это сейчас не интересно, а я и так безвылазно два дня просидела над бумагами…"
    stop ambience
    
    scene ext_clubs_day with dissolve
    play ambience ambience_camp_center_day
    show sh normal pioneer far at right
    show el normal pioneer far at left
    with dspr
    "У клубов четвёрка упёрлась в обоих кибернетиков."
    "Шурик и Электроник как раз опустили на землю конструкцию из направленного вертикально вверх бытового вентилятора и четырёх лампочек, смонтированных на деревянной раме."
    show cs normal with dspr
    show sh upset pioneer far
    show el upset pioneer far
    with dspr
    cs "Пионеры, а у вашего аппарата,{w} кроме пропеллера,{w} есть другие{w} насадки?"
    $ renpy.pause (1)
    hide sh
    hide el
    with dspr
    show cs normal with move:
        xpos 0.25
    show mi normal pioneer at right with moveinbottom
    mi "Ой, что вы, Виола, это же декорация костра. Вот, смотрите: сюда крепятся полоски бумаги, их раздувает вентилятором, а снизу подсвечивает лампочками — получается как будто костёр. Это ребята придумали, правда красиво? Ну, пойдёмте, мальчики, а то до ужина поставить не успеем."
    hide mi with easeoutright
    show d_to normal pioneer at right with dspr
    d_to "Надо будет сходить на спектакль. Очень интересно, что там она придумала. Ну, Ульяна, что там дальше?"
    show d_us normal sport at center with dspr:
        ypos -0.05
    play music music_list["afterword"]
    us_old "Дальше? Лагеря, или узлы, называйте как хотите, разойдутся друг от друга, но переходы между ними останутся доступными."
    us_old "Периметры искривлённого пространства вокруг лагерей начнут расползаться, а потом, с точки зрения математики, мгновенно кривизна поменяет знак."
    us_old "И окажется, что лагерь стоит не внутри пузыря, а на поверхности шара. Как на планете."
    us_old "На каждый лагерь, на шестьдесят пионеров и персонал — целая планета, и ещё куча планет незаселённых."
    us_old "Небольшие, конечно — пятьдесят семь километров диаметром. Правда, это и не планеты вовсе, а, как бы объяснить, тени от Земли на четырёхмерных плоскостях."
    us_old "Система сохранится, но изменится очень сильно. Большие сессии между циклами у Системы уйдут, останутся только малые — во время сна."
    hide d_us
    hide d_to
    hide cs
    with moveoutright
    show d_sf normal pioneer at center with dspr
    th "Только одно это уже хорошо, насмотрелся я на эту большую сессию. Хватило на всю жизнь."
    stop ambience
    
    scene ext_houses_day with dissolve
    play ambience ambience_camp_center_day
    show d_us normal sport at center with moveinleft:
        ypos -0.05
    show d_sf normal pioneer behind d_us with dspr:
        xpos 0.6
    show d_to normal pioneer at fleft with dspr
    show cs normal with dspr:
        xpos -0.15
    us_old "Система сохранится, но изменится очень сильно. Большие сессии между циклами у Системы уйдут, останутся только малые — во время сна."
    us_old "Что будет с людьми — я не знаю…"
    cs "Я знаю, всё-таки не зря здесь торчала."
    show d_us normal sport with move:
        xpos 0.85 ypos -0.05
    show cs normal at center with move
    cs "Только я коротко. Всё будет почти так, как сейчас."
    cs "Живёшь в октябрятах, освободилось место в среднем отряде — добро пожаловать. Живёшь в среднем отряде — переходишь в старший. Числишься в старшем, если готов — будь добр осознать себя."
    cs "Если, осознав себя, хоть что-то изменил в себе самом, то выпадаешь из этой сансары. Ну а закончится всё… так, как и должно в таком случае закончиться."
    cs "Люди — они умирают. Вот в этом «почти» и заключается."
    show cs shy with dspr
    cs "Как почувствовал, что стареешь, значит и выпал. Я, как видите, не старею."
    show d_us shy sport with dspr
    us_old "А… дети?"
    show cs smile with dspr
    cs "Если будет смерть, то будут и дети. Медицина не возражает. До семи лет дети как дети, а потом — в младший отряд, как все."
    show cs normal
    cs "А, ещё про медицину. Там, на материке, вас ни одна медкомиссия не выявит. Как и здесь людей оттуда."
    cs "Даже нейтринное кольцо, то, что в документации называется «неуничтожимое ядро личности» — оно присутствует у всех без исключения."
    cs "То, что когда-то в древности называлось Ка."
    me "И что, среди них, среди пионеров, могут быть люди? Оригиналы?"
    cs "Почему «могут?» Сам понимаешь, в каких узлах и как зовут — я тебе не скажу. Одна помешалась на вечной молодости, другой от семьи убежал… Кое-кто потом с должности слетел, но попробуй найди оригинал среди идентичных копий. Даже шрамы совпадают."
    stop music fadeout 3
    stop ambience
    
    scene ext_aidpost_day with dissolve
    show cs normal with dspr
    cs "Ужинайте без нас{w=1}… молодожёны, а мы ещё погуляем. Так что до вечера."    
    
#################################
#Глава 19. Послезавтрашняя бомба#
#################################
   
label the_day_after_tomorrow_bomb:
    $ save_name = u"Дубликат. Четвертая смена -\nПослезавтрашняя бомба"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Послезавтрашняя бомба" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    
    
    scene dct_ext_stage_big_sunset with blinds
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play sound_loop ambience_medium_crowd_outdoors
    play music music_list["i_want_to_play"]
    "И вот настали долгожданные \"двадцать ноль-ноль\", из-за которых пионеры потянулись на концертную площадку сразу же после ужина."
    "Все ждали начала спектакля, все уже сидели на скамейках и ждали, когда наконец откроется занавес."
    "«Совёнок» действительно был беден на развлечения, и любые внеплановые мероприятия здесь проходили на ура."
    "Ульяна-большая сидела в первом ряду, между Виолой и Ольгой Дмитриевной, и, пока не начался спектакль, оглянувшись, рассматривала публику."
    show d_us normal dress at right with moveinbottom:
        ypos -0.05
    th "Ну, Виола, Ольга, Анатолий — эти рядом, за Виолой — октябрята."
    show d_ar normal pioneer at cleft with moveinleft
    $ renpy.pause (1)
    show d_ar smile pioneer with dspr
    $ renpy.pause (1)
    d_ar "Ульяна, смотри, ты обещала."
    show d_us smile dress with dspr
    us_old "Артём, ты же меня знаешь. Сделаю без шума и пыли."
    hide d_ar with moveoutleft
    show d_us normal dress with dspr
    show mt smile pioneer at left with moveinbottom
    mt "Ульяна, как бы мне тебя в свой лагерь переманить? Пойдёшь в физруки?"
    mt "Со старшими подружилась, с младшими подружилась…"
    us_old "Не, Оля, не получится. Физрука воспитайте в своём коллективе."
    show mt grin pioneer with dspr
    mt "Ульяна, прости. Я просто заревновала чуть-чуть своих подопечных."
    hide mt with moveoutbottom
    th "Зря заревновала. Просто час назад в столовой Артём подошёл к нам…"
    stop music fadeout 1
    stop sound_loop
    stop ambience
    
    scene int_dining_hall_people_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    show d_sf normal pioneer at left with dspr
    show d_ar normal pioneer at right with moveinright
    d_ar "Здравствуйте, Семён, Ульяна. Ульяна-младшая сказала, что вы завтра уходите."
    me "Да, завтра до ужина."
    d_ar "Тогда…"
    show d_ar dontlike pioneer with dspr
    $ renpy.pause (1)
    d_ar "Семён, может, ты тогда передашь два письма?"
    d_ar "Зайцам из вашего лагеря."
    show d_sf smile pioneer with dspr
    me "Понятно. Конечно, передам."
    show d_ar smile pioneer with dspr
    "И два самодельных конверта перекочевали в карман к Семёну."
    d_ar "Спасибо, Семён. Только ты не забудь, пожалуйста."
    show d_us laugh sport at center with moveinbottom:
        ypos -0.05
    us_old "А если забудет, я его План мероприятий писать заставлю. Он этого больше всего боится."
    show d_ar laugh2 pioneer
    show d_sf laugh pioneer
    with dspr
    $ renpy.pause (1)
    hide d_ar
    hide d_sf
    hide d_us
    with pixellate
    $ renpy.pause (0.5)
    stop ambience
    
    scene dct_ext_stage_big_sunset with pixellate
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play sound_loop ambience_medium_crowd_outdoors
    play music music_list["goodbye_home_shores"]
    show d_us normal dress at right with dspr:
        ypos -0.05
    th "Средний отряд на месте. Весь, за вычетом артистов."
    th "Самый большой отряд и самый незаметный. И кажется, в среднем отряде никто и никогда не просыпался."
    us_old "Виола, правда, что в среднем отряде никто и никогда не просыпался?"
    show cs normal at left with moveinbottom
    cs "Средний — депо. Потому и не просыпаются."
    hide cs with moveoutbottom
    th "Что за депо? Как у вагонов, что ли? Не совсем понятно, но ладно. Завтра перед их отъездом ещё поспрашиваю."
    th "Пусть средний отряд и депо, но вот когда объявили набор артистов, именно из среднего отряда они и пришли."
    th "Тоже тяжело им, наверное, по цикловому графику жить. Так, получается? Надо не забыть спросить у Виолы."
    show d_us sad dress with dspr
    th "А я уже не в пионерах. И если опять не усну, а сумею так же, как Сёмка, удержаться, то кто-то из среднего отряда займёт моё место."
    stop music fadeout 2
    show blink
    th "Сёмка, помоги мне! Я не против стареть! Рядом с тобой."
    hide blink
    show d_us normal dress
    show unblink
    $ renpy.pause (1)
    show sh normal pioneer at left with moveinleft
    $ renpy.pause (0.5)
    hide sh with moveoutleft
    th "Ого."
    show el normal pioneer at left with moveinleft
    $ renpy.pause (1)
    show mz normal pioneer at left with moveinleft
    hide el with moveoutleft
    hide mz with moveoutleft
    th "Даже кибернетики выползли из своей берлоги."
    show d_us smile dress with dspr
    th "И Женя будет делать вид, что она здесь, рядом с Сыроежкиным, оказалась совершенно случайно."
    show d_us normal dress with dspr
    th "А где сестрёнка?"
    show us normal pioneer far at fleft with dissolve
    $ renpy.pause (1)
    hide us with dissolve
    th "Нашла! Но почему она не на скамейке со всеми, а возле кустов на самом краю площадки?"
    th "Сбежать, что ли, хочет? Нет, не похоже. Вон с каким интересом на сцену смотрит."
    th "А это кто?"
    us_old "Виола, кто это? Вон те два дядьки на последнем ряду."
    show cs normal at left with moveinbottom
    cs "Это? Водитель и грузчик. Продукты привезли из Шлюза на следующую неделю. Тебе их видеть не положено было, вот ты их раньше и не видела."
    show mt angry pioneer with moveinbottom
    mt "Ульяна, Виола, не мешайте! Уже начинается!"
    hide mt with moveoutbottom
    hide cs with moveoutbottom
    hide d_us with moveoutbottom
    stop sound_loop fadeout 3
    $ set_mode_nvl ()
    play music badstory
    "Зашелестели раздвигаемые половинки занавеса, и публика увидела пионеров, сидящих подковой вокруг костра на лесной поляне."
    nvl clear
    "Анфиса задумчиво перебирает струны на гитаре… Лариса — с альбомом для рисования на коленях."
    voice "{i}Оксана Сергеевна, мы кого-то ждём? Почему вы всегда просите нас сесть так, чтобы одно место у костра осталось свободным? …{/i}"
    nvl clear
    "Позже Ульяна-большая удивлялась тому, что почти не запомнила сам спектакль, но очень хорошо запомнила реакцию зрителей."
    "Первые пять минут, пока зрители узнавали артистов, пока толкали друг друга в бок и показывали пальцами, спектакль не шёл."
    "Мику готова была расплакаться совершенно всерьёз."
    "Но потом зрители стали узнавать в артистах уже самих себя, сопереживать им, замолчали, и до самого финала стояла тишина."
    "Такая, что было слышно даже шум вентилятора — того, что был составной частью бутафорского костра."
    "А когда пришло время финальной сцены, когда Степан (тот самый Максим, что четыре часа назад гонялся за Витькой по пляжу) чуть попятился от костра и, засунув руки в карманы шорт, грустно смотрел на пионеров, а невидимый за ширмой Семён в это время заиграл на гитаре, кто-то из зрителей закричал: «Стёпка! Останься! Пожалуйста!». Степан услышал, но только отрицательно качнул головой и, немного ссутулившись, тихо спустился со сцены и растворился в сумерках."
    nvl clear
    "А Семён на гитаре и Мику на клавишах продолжали играть."
    "Ульяна вспомнила рассказ Семёна о последней репетиции."
    me "{i}Знаешь, Рыжик. Мику сказала, что мы как будто уже сыгрались сто лет назад, а Алиса даже не вздрогнула, лишь кивнула головой.{/i}"
    nvl clear
    "На сцене встала Анфиса, оставив гитару около костра. Улыбнулась залу весело и нахально и тоже ушла."
    "Следом, почти сразу, ушла Лариса, оставив альбом."
    "Ушла Святослава, положив на сцену связку ключей."
    "Янка подскочила как пружинка, бросила куда-то вглубь сцены рогатку, подмигнула зрителям и убежала. Только подошвы застучали."
    "Артисты по одному спускались со сцены, кто по правой лесенке, кто по левой, и скрывались за ней…"
    "Последней ушла, ни на кого не глядя, Оксана Сергеевна, оставив панамку."
    nvl clear
    $ set_mode_adv ()
    stop music fadeout 1
    stop ambience
    
    scene ext_stage_big_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound_loop ambience_medium_crowd_outdoors fadein 3
    play sound sfx_concert_applause
    "Закончилась песня. Погасло освещение на сцене, медленно погас костёр. Зажглись фонари на зрительской площадке. Занавес. Аплодисменты."
    show d_to normal pioneer at left with moveinbottom
    show cs shy with moveinbottom
    cs "{i}Как?{/i}"
    d_to "{i}Бомба!{/i}"
    hide cs
    hide d_to
    with moveoutleft
    show mt scared pioneer with moveinbottom
    mt "…"
    hide mt with moveoutleft
    stop sound_loop fadeout 1
    "Зрители потянулись по домикам."
    "Славя подбежала к Мику. Ульяна-большая услыхала их разговор: что-то там про пирог, столовую и артистов."
    show d_us sad dress at center with moveinbottom:
        ypos -0.05
    th "Пойду спать. Сёмка пускай чаи гоняет, если бы не он — ничего бы и не было. Заслужил."
    hide d_us with moveoutleft
    stop ambience
    
    scene ext_playground_night with squares
    play ambience ambience_camp_center_night
    play sound dct_sfx_running
    me "Уля, подожди!"
    show d_us sad dress at cright with dspr:
        ypos -0.05
    show d_sf normal hike behind d_us at cleft with moveinleft
    stop sound
    us_old "Сём, говорят, артисты сейчас чай с пирогом в столовой пьют. Прямо сейчас."
    me "Правду говорят. Я не пошёл. Какой я артист? А во-вторых, без тебя идти не хотелось."
    us_old "Понятно."
    show d_sf serious hike with dspr
    me "Рыжик, что-то случилось?"
    us_old "Случилось?{w=2} Нет."
    show d_us shy dress with dspr
    us_old "Да."
    show d_us hurt dress with dspr
    us_old "Сём. Скажи. А тех девочек. Славяну и Мику. Ты их ещё любишь?"
    show d_sf sad hike with dspr
    me "Их больше нет, Рыжик. Но{w=2}… да."
    show d_us sad dress with dspr
    us_old "Это хорошо. Значит, когда я усну, ты меня не забудешь."
    show d_sf serious hike with dspr
    me "Так вот что тебя беспокоило. А я думал, может, я чего натворил и ты на меня обижаешься."
    show d_us sad dress at center with move:
        ypos -0.05
    me "Ульяныч, а почему ты, собственно, засыпать собралась? Я тебя чем-то не устраиваю?"
    show d_us hurt dress with dspr
    us_old "Сёмк, это же активная фаза. Ещё два-три цикла и всё. Она закончится, и я усну."
    me "И только-то? Ты вообще чем тётю Виолу сегодня, то есть уже вчера, слушала? «Если хоть что-то изменил в себе самом, то выпадаешь из этой сансары…»"
    me "А ты изменилась, Рыжик. Представь свою сестрёнку, которой нужно, как тебе сегодня, разложить по полочкам будущее нашего мира. Она скажет, что это скучно, и убежит."
    me "Кажется, в этой умнейшей и серьёзной девушке только я и видел прежнюю озорную и задорную Ульяну. Ну такую тебя я всегда буду видеть. Уж терпи."
    show d_us sad dress with dspr
    us_old "Правда, Сёмк?"
    show d_us normal dress at right with move
    us_old "Я тогда очень старалась."
    show d_us smile dress with dspr
    us_old "Но смотри, ты подарил мне надежду."
    show d_us laugh dress with dspr
    us_old "Не вздумай обмануть — житья не будет."
    hide d_us with easeoutright
    show d_sf smile hike with dspr
    hide d_sf with easeoutright
    stop ambience
    
    scene ext_square_night with dissolve
    play ambience ambience_camp_center_night
    play music music_list["mystery_girl_v2"]
    "Закончилось «сегодня» и наступило «завтра». Лагерь угомонился после запоздалого отбоя. Какое-то время на поляне за домиком Рыжих ещё можно было разглядеть две неясных фигуры. Но потом исчезли и они."
    stop music fadeout 1
    stop ambience fadeout 2
    $ renpy.pause (2)

############################
#Глава 19. Обратный автобус#
############################
   
label return_bus:
    $ save_name = u"Дубликат. Четвертая смена -\nОбратный автобус"
    $ night_time()
    scene black with dissolve
    show headline_text2 u"Обратный автобус" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_ext_cliff_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_lake_shore_day
    us "...на остановке тишина. Знаешь, так тихо, что сразу понимаешь: вокруг нет ни одного человека, ни души."
    us "Даже ветер стих."
    us "И жара — такая, что асфальт плавился. Я бы тоже где-то в домике от жары спряталась, но мне было интересно."
    us "Вот, я прячусь за кустами, думаю, может плюнуть на всё и убежать. Автобус-то уже приехал. Пассажиры уже вышли и ушли за ворота. Новый доктор — страшная, а опоздавший пионер — он какой-то ни рыба ни мясо... Да ещё тормоз и истеричка. На Семёна чем-то похож, кстати."
    us "А я сижу и жду неизвестно чего. Любуюсь этим автобусом, как будто у меня других дел нет."
    us "Я уже сварилась там и уйти собралась, и тут они появились."
    stop ambience
    
    scene ext_camp_entrance_day with pixellate
    $ prolog_time
    play ambience ambience_camp_entrance_day
    play sound sfx_open_door_mines_metal
    play music music_list["sunny_day"]
    show d_to normal casual at center with dspr
    $ renpy.pause (0.5)
    hide d_to with moveoutleft
    $ renpy.pause (0.5)
    show cs normal with dspr
    $ renpy.pause (0.5)
    hide cs with moveoutleft
    $ renpy.pause (0.5)
    show d_sf normal pioneer at center with dspr
    $ renpy.pause (0.5)
    hide d_sf with moveoutleft
    $ renpy.pause (0.5)
    show d_us normal sport at center with dspr:
        ypos -0.05
    hide d_us with moveoutleft
    stop ambience
    
    scene ext_bus with pushleft
    play ambience ambience_camp_entrance_day
    show cs normal at left
    show d_to normal casual:
        xpos -0.1
    show d_sf normal pioneer at right
    show d_us normal sport at fright:
        ypos -0.05
    with dspr
    d_to "Ну что, молодожёны, давайте прощаться."
    stop music fadeout 1
    stop ambience
    
    show dct_ext_cliff_day with pixellate
    $ day_time ()
    play ambience ambience_lake_shore_day
    us "Ну, пообнимались они. Но понимаешь, Виола с Толиком прощались так, как будто навсегда или очень надолго."
    us "Она плакала, понимаешь. Даже тушь потекла."
    stop ambience
    
    scene ext_bus with pixellate
    $ prolog_time ()
    play ambience ambience_camp_entrance_day
    play music its_in_the_fog
    show d_sf serious pioneer at center with dspr
    me "Виола. Ещё не поздно отказаться и уйти на лодке."
    show d_sf serious pioneer at left with move
    show cs shy at right with moveinbottom
    cs "Нет{w}… пионер. Мы остаёмся в вашей{w}… стране эльфов. Наш дом, оказывается, тоже здесь…"
    cs "Так вот, наш дом здесь. Мне не страшно за себя, мне не страшно за Толю. Я просто боюсь, что мы с ним потеряем друг друга и не найдём."
    cs "Ты обещал проследить, но мне всё равно страшно. И начинай с меня. А то я боюсь, что брошусь на тебя, когда ты прицелишься в Толю."
    hide d_sf with moveoutleft
    show d_to normal casual at cleft with moveinleft
    show cs shy at cright with move
    me "Разойдитесь на полшага."
    show d_to normal casual at left with move
    cs "Всё как сто лет назад? Так, Семён?"
    me "Что мне делать?"
    d_to "Стреляй, физрук, не тяни, ТЫ ЖЕ ВИДИШЬ — ЕЙ СТРАШНО! Ты прошёл через это, и мы пройдём."
    stop music fadeout 1
    stop ambience
     
    scene dct_ext_cliff_day with pixellate
    $ day_time ()
    play ambience ambience_lake_shore_day
    us "Семён взял какой-то прибор. И на нём телефонный диск, на том приборе. Вот он код на том диске набрал. Потом направил на них коробочку."
    us "Виола плачет, сестрёнка плачет, у Семёна руки дрожат."
    us "И только кнопка: щёлк, щёлк."
    us "Это, знаешь, было как расстрел. Как будто тот прибор из них жизни забирал."
    us "Кнопка щёлкает, а человек в лице меняется. И прямо чувствуешь, что человека там больше нет. Был человек, а вместо него стала кукла."
    us "И они так, как куклы на ниточках, ушли в автобус."
    stop ambience
    
    scene ext_bus with pixellate
    $ prolog_time ()
    play ambience ambience_camp_entrance_day
    play music music_list["orchid"]
    show d_to normal casual at cleft
    show cs shy at cright
    with dspr
    $ renpy.pause (1)
    play sound sfx_click_3
    show cs normal with vpunch
    $ renpy.pause (0.5)
    show d_to smile casual with dspr
    d_to "До встречи в следующей жизни. Проследи за Вилкой."
    $ renpy.pause (1)
    play sound sfx_click_3
    show d_to normal casual with vpunch
    d_to "Про{w}... Пр{w}... П{w}..."
    $ renpy.pause (3)
    hide d_to
    hide cs
    with dissolve
    play sound dct_sfx_bus_departure2
    $ renpy.pause (3)
        
    scene ext_no_bus with dissolve
    $ renpy.pause (2)
    stop music fadeout 1
    stop ambience
    
    scene ext_camp_entrance_day with pushright
    play ambience ambience_camp_entrance_day
    show d_sf serious pioneer at center
    show d_us sad sport at cright:
        ypos -0.05
    with dspr
    me "{i}Я никогда не умел умирать,\nПодскажите рецепт, капитан!{/i}"
    me "Вот и всё, Рыжик. Вот и закончилась эпоха. Хотя… нет, ещё не всё. Где же он у меня?.."
    stop ambience
    
    scene dct_ext_cliff_day with pixellate
    $ day_time ()
    play ambience ambience_lake_shore_day
    us "А Семён достал из рюкзака топор. Обычный топор с пожарного щита. Положил прибор на поребрик и расплющил прибор топором."
    us "Потом достал ещё один такой же прибор и разбил и его. Только осколки в разные стороны полетели."
    stop ambience
    
    scene ext_camp_entrance_day with pixellate
    $ prolog_time ()
    play ambience ambience_camp_entrance_day
    show d_sf normal pioneer at center with dspr
    me "Вот теперь действительно всё. Пошли, Ульяныч. К ночи дома будем."
    show d_sf smile pioneer with dspr
    me "Скоро двое новых октябрят появятся, да ещё с двойниками. Ума не приложу, как эту парочку вычислить и вместе собрать."
    show d_us normal sport at right with moveinbottom:
        ypos -0.05
    us_old "Пошли, Сёмк. И расскажи мне про Мику. Ты обещал."
    $ renpy.pause (1)
    hide d_sf
    hide d_us
    with moveoutleft
    stop ambience

    scene dct_ext_cliff_day with pixellate
    $ day_time ()
    play ambience ambience_lake_shore_day
    play music music_list["mystery_girl_v2"]
    us "Вот так. Виола и Анатолий уехали, а гости просто ушли."
    th "И унесли с собой и тайну, и приключения."
    voice "Жалеешь, что ушли без тебя?"
    us "Нет. Нисколечко."
    th "У меня теперь своя тайна!"
    th "Когда-нибудь я открою её Алисе и, может быть, Семёну. Он уже взрослый, но он поймёт."
    us "Как думаешь, дойдут к ночи?"
    voice "Дойдут. К ночи дойдут. Можно быстрее, но они не знают короткой дороги."
    us "Покажешь? Дорогу?"
    voice "Покажу."
    us "Ты так и не вспомнила, как тебя зовут?"
    voice "Нет. Когда я жила одна, мне было всё равно; когда мне оставляла еду та женщина, которая сейчас уехала, нам тоже было всё равно."
    us "Так не годится. У всех людей должны быть имена!"
    us "Скажи."
    us "Ты не против?"
    us "Если тебя."
    us "Будут звать."
    # "Ульянка повернулась, и, глядя тайне прямо в глаза, спросила."
    stop ambience fadeout 1
    
    scene dct_4th_shift_fin with dspr
    play sound_loop ambience_forest_day
    us "Юля?"
    stop music fadeout 3
    stop sound_loop
    $ renpy.pause (3)

    scene ext_camp_entrance_day with squares
    play ambience ambience_camp_entrance_day
    $ renpy.pause (1)
    show d_sl normal pioneer at center with dspr:
        ypos -0.1
    $ renpy.pause (1)
    show d_sl scared pioneer with dissolve
    sl "Ну вот зачем так? Неужели обязательно нужно беспорядок оставить?"
    th "Какие-то приборы разбитые. Может, кибернетики в кружок несли да отвлеклись на что-то?"
    show d_sl angry pioneer with dissolve
    th "Неужели они в старом лагере были? Туда же нельзя."
    show d_sl normal pioneer with dissolve
    th "Забыли об этом, наверное."
    th "Рассеянные оба. Что один, что другой."
    th "Отнесу им. Вдруг они ещё сумеют выпаять из этого хлама что-нибудь для своего робота?"
    hide d_sl with dspr
    $ renpy.pause (1)
    play sound sfx_open_door_clubs
    sl "Ребята, это вы, наверное, потеряли."
    $ renpy.pause (3)
    stop ambience
    #Хлопнула дверь клубов
    
    scene black with blinds
    $ persistent.d_shif = d_shif + 1
    
menu:
    "Конец книги «Четвёртая смена»"
    "Продолжить":
        jump dct_effector
    "В меню":
        jump dct_mnu2
