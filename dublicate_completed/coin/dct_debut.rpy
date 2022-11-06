    ################
    #Глава 5. Дебют#
    ################


label dct_debut:
    $ save_name = u"Дубликат. Монетка в фонтане -- Дебют"
    $ day_time()
    $ persistent.sprite_time = "day"
    
    scene black
    # stop sound
    # stop sound_loop
    # stop ambience
    # stop music
    show headline_text2 u"Глава V. Дебют" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    
    $ renpy.music.set_volume(0.5, delay=0)
    play music crush
    scene dct_int_clubs_male2_night_zoom
    show sh serious pioneer
    show save_bg
    show black
    show promo_text_un u"{color=#fff226}Из рабочей тетради Шурика Трофимова.{/color}" at truecenter with dspr
    $ renpy.pause(3.0)
    show promo_text_un u"{color=#fff226}Из рабочей тетради Шурика Трофимова.{/color}":
        ease 1.2 yalign 0.05
    hide black with dissolve
    $ set_mode_nvl()
    "Пятый день смены."
    "\n\nНеобычные мысли, сны и явления."
    "\n1. Опять приснился сон про полигон и маленького человечка.{w} Рассмотрел во сне этого «человечка» и вычеркиваю его из списка загадок. Человечек похож на недоделанного робота, оставленного пионерами, отдыхавшими здесь до нас.{w} Видимо, во сне реализовалось мое подсознательное желание видеть этого робота функционирующим."
    "\n2. Обнаружено нештатное потребление электроэнергии.{w} Вчера вечером перед уходом были обесточены все электроприборы и отключены автоматы на щитке. Сегодня утром счётчик показал расход 2 квт/ч. электроэнергии.{w} Сыроежкин ничего не смог пояснить по этому поводу, утверждает, что ничего не включал."
    "\n3. Когда вижу кого-либо из пионеров или персонала лагеря, включая вожатую, я могу сразу сказать, микс это или копия.{w} Что значат эти слова, применительно к человеку, я не знаю."
    "\n4. Регулярно вспоминается женское имя «Яна».{w} Твердо уверен, что у меня нет знакомых с таким именем."
    "\n\nПлан работы в кружке кибернетики на день…"
    stop music fadeout 3
    play ambience ambience_int_cabin_day fadein 2
    show save_bg:
        linear 0.7 alpha 0
    show promo_text_un u"{color=#fff226}Из рабочей тетради Шурика Трофимова.{/color}":
        linear 0.7 alpha 0
    window hide
    $ set_mode_adv()
    pause 0.4
    
    window auto
    
    "Шурик еще раз перечитал написанное и кивнул."
    sh "Сергей, на мне сегодня пайка, а ты собираешь излучатели и приемники ультразвука. Так?"
    show sh normal pioneer with dspr
    "Сыроежкин только пожал плечами, все было обговорено еще вчера."
    sh "… и, Сергей, ты говоришь, что девочки хотели поучаствовать в испытаниях прибора."
    el "Да, Лена и Мику. Я сказал им, что если доктор не возражает, то мы не против."
    show sh serious pioneer with dspr
    sh "Хорошо, тогда мнением доктора сам поинтересуйся, пожалуйста."
    sh "А то девочки начнут доктору рассказывать и что-нибудь напутают."
    "Сыроежкин молчал."
    # Шурик поднял голову и увидел, что тот, весь подобравшись, как охотничья собака, внимательно смотрит сквозь открытую дверь на противоположную сторону аллеи.   # По канону
    show sh normal pioneer with dspr
    "Шурик оглянулся на товарища и увидел, что тот, весь подобравшись, как охотничья собака, внимательно смотрит сквозь открытую дверь на противоположную сторону аллеи."
    scene int_clubs_male_day
    show el serious pioneer close at cleft
    with dissolve
    "Что-то невидимое, жужжа электромоторами и иногда задевая за кусты, скрывающие заброшенное здание напротив, двигалось со скоростью пешехода, по обочине главной аллеи от перекрестка в направлении ворот."
    show el angry pioneer close with dspr
    el "Уйдет ведь!"
    "Шурик услышал шепот и увидел, как Сыроежкин вслепую шарит рукой по столу."
    show sh surprise pioneer close at right with moveinright
    sh "Сергей, нет!"
    show el serious pioneer close
    show sh normal pioneer close
    with dspr
    extend " Лучше понаблюдаем. Если это пришло сюда один раз, то придет и еще."
    show sh serious pioneer close with dspr
    sh "И, пожалуйста, вдруг это там, за кустами, октябренок балуется?"
    show el surprise pioneer close with dissolve_fast
    el "Ох-х-х… Да."
    play sound sfx_chair_fall
    "Небольшой трансформатор выпал из разжавшейся кисти Сыроежкина обратно на стол, глухо стукнув при этом."
    show el sad pioneer close with dspr
    el "Этого я не учел."
    show sh normal_serious pioneer close dct with dissolve_fast
    sh "Но Сергей."
    "Шурик поправил очки и строго посмотрел на Сыроежкина."
    sh "Предположим, мы действительно видели то, что видели. Тогда наш долг перед наукой описать все это."
    show sh normal pioneer close with dissolve_fast
    extend " И надо обязательно указать время. Сейчас девять часов двадцать семь минут."
    stop ambience fadeout 1
    $ renpy.music.set_volume(1.0, delay=0)
    scene black with dissolve
    
    pause 0.5


    play sound_loop "<from 7.0 loop 7.0>mods/dublicate_completed/sounds/sfx/dct_sfx_steps3.ogg"
    play ambience ambience_forest_day fadein 1
    scene bg ext_path2_day
    show ext_path2_day at walking
    with dissolve
    us "Сёмк."
    me "Да, Рыжик?"
    us "Хорошо как. Девочки теперь знают, что они не одни."
    us "Жалко, что мы все вместе собраться не можем.{w} Только в Шлюзе, а там мы спим."
    "И тут мысль Ульянки перескочила."
    us "Сём, а ты ведь не спишь в Шлюзе. Расскажи, что ты там делаешь?"
    me "Страдаю, Уля…"
    stop sound_loop fadeout 1
    stop ambience fadeout 1
    play music higekitekina fadein 2
    show ext_path2_day at walking:
        linear 0.5 alpha 0
    $ set_mode_nvl()
    "Ну как рассказать обо всем в двух словах?{w} Рассказать, как стараешься выскочить из автобуса первым и страхуешь девочек. Видишь, как они строятся и сам борешься с желанием встать в тот же строй. Как стараешься прикоснуться ко всем пионерам, как целуешь Ульянку.{w} А когда автобусы глушат двигатели, то над остановкой воцаряется только шаркающий звук шагов, усиленный многократным повторением. Это спящие пионеры начинают перемещаться к воротам."
    "\nКак ты идешь параллельным курсом, держа Рыжика за руку, стараясь подстроиться под ее ковыляющую походку.{w} Как строй втягивается в ворота и ты отпускаешь руку Ульяны, оставаясь снаружи. Как ты, на прощание, пожимаешь предплечье Мику, замыкающей строй, прощаясь, в ее лице, со всеми пионерами.{w} И как, стараясь не заглядывать в ворота, возвращаешься к остановке и там дремлешь, время от времени приходя в себя от сырости и предутреннего холода, и проверяя: далеко ли до рассвета, на месте ли автобусы, не начали ли возвращаться пионеры?{w} Убеждаешься, что все в порядке, подкидываешь еще пару сучьев в костер и продолжаешь ждать, пребывая в полудреме. А вокруг тебя крутятся картины вероятностных миров, с твоим и твоих близких участием."
    "\nКак иногда к костру подсаживается Яна, у которой последнее время все более и более муторно в ее электронно-нейтринной душе.{w} Кошкоробот не жалуется, но в ней все больше и больше от человека, и блики костра на алюминиевом лице и щитке закрывающем фотоматрицы вполне заменяют мимику. И эмоции видны совершенно ясно.{w} «Почему папа меня не видит?» — Нарушает тишину Яна.{w} Что ей ответить? «Не положено папе», — если только.{w} И хочется прижать к себе эту тушку, бывшую когда-то алюминиевым бидоном. И думаешь о том, что когда-нибудь Яна научится плакать."
    "\nА потом начинает светлеть небо и слышно, как в автобусах заводятся двигатели, и нужно идти к воротам Шлюза и встречать своих, всматриваться в лица и пытаться понять, не подменили ли человека там, на стадионе.{w} За Артемом не уследил, и сейчас в лагере другой Артем. Хороший парнишка, но спящий.{w} А вот Мику перехватить удалось, но утро тогда вышло сумасшедшее, пока искал среди всех Мику всех лагерей именно нашу, и потом брал за руку и вел ее, покорную, к своему автобусу, говоря ей, спящей в обоих смыслах, какую-то ворчливо-успокоительную чушь, пока отводил «приблудную» Мику к ее автобусу, так же успокаивая. И не важно, слышала она что-то или нет.{w} Не знаю, от Алисы заразился что ли, но бросить своих не могу."
    "\nА когда пионеры начинают просыпаться, тебя начинает трясти страх, вдруг кто-то из девочек выпал из активной фазы?"
    stop music fadeout 6
    extend " Как все это рассказать, когда вот уже виден забор лагеря, в просветы между деревьями?"
    play ambience ambience_forest_day fadein 1
    $ set_mode_adv()
    me "… Страдаю, Уля. Из людей нельзя делать роботов, если уж вложили в них души. А я не могу взять и отключить здесь всю механику. А если бы мог — побоялся бы."
    stop ambience fadeout 1
    play sound_loop ambience_camp_entrance_day fadein 1
    scene ext_no_bus with dissolve
    "Ульяна подождала Семена, взяла его за руку, и к воротам они подошли уже вместе."
    show d_us normal sport at center:
        ypos -0.05
    show d_sf normal sport:
        xzoom -1.0 xcenter 0.7
    with dissolve
    us "Сём, я не хотела, чтобы ты огорчался, прости."
    us "Но ты бы, если мог, все бы отключил, я знаю. Злился бы: «Почему опять я?!» Ругался нехорошими словами, но выключил бы этот рубильник."
    scene ext_camp_entrance_day with dissolve
    me "Ты-то тут причем, Рыжик? Не ты же это устроила, чтобы извиняться."
    stop sound_loop fadeout 1
    play ambience ambience_camp_center_day fadein 1
    scene ext_clubs_day
    show d_sf normal sport:
        xcenter 0.57
    show d_us normal sport:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    show d_us_sport_mirror:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with irisout
    "Лагерь встретил Семена и Ульяну тишиной и безлюдьем. Даже на клубах висел замок."
    "Асфальт главной аллеи уже успел раскалиться и, в колыхающемся мареве, скорее угадывались, чем были ясно различимы вдалеке фигуры бегающих между спорткомплексом и пляжем пионеров."
    scene ext_square_day
    show d_sf normal sport:
        xcenter 0.44
    show d_us normal sport:
        xzoom -1.0 xcenter 0.3 ypos -0.05
    show d_us_sport_mirror:
        xzoom -1.0 xcenter 0.3 ypos -0.05
    with pushleft
    me "И где хлеб-соль, где встречающие? Ладно Лена с Алисой, но хоть один пионер должен бегать.{w} Уж Шурик-то должен быть на месте."
    show d_us shy sport with dspr
    us "Сёмк, напомни мне. Когда я тебе последний раз говорила, что ты тормоз?"
    show d_sf smile sport with dspr
    me "В день нашего знакомства, да?"
    show d_us hurt sport with dspr
    us "У тебя еще и склероз."
    show d_sf normal sport with dspr
    "Ульяна ткнула Семена кулаком в бок."
    show d_us smile sport with dspr
    us "Сегодня открытие купального сезона же. Ты что, Ольгу не знаешь? Наверняка все на пляже сейчас."
    "И, подражая интонациям вожатой, добавила:"
    show d_us serious sport with dspr
    us "Мероприятие общелагерное, никаких исключений!"
    show d_sf laugh sport with dspr
    stop ambience fadeout 1.25
    pause 0.25
    scene black with dissolve
    
    pause 0.5


    play ambience ambience_lake_shore_day fadein 1
    scene dct_ext_beach_day_with_pass_train
    show mt angry panama swim close
    with dissolve
    "А Ольга Дмитриевна и на самом деле царила сейчас над пляжем."
    mt "Мальчики, девочки, младший отряд!{w} Все построились и по моей команде заходим в воду!"
    mt "О! Вот и физруки подошли!"
    scene dct_ext_beach_day_lifesaving_shield
    show d_sf normal swim:
        xcenter 0.57
    show d_us normal swim:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with dissolve
    mt "Семен, Ульяна! Вы почти не опоздали, поэтому я почти не буду вас ругать."
    show d_sf smile swim
    show d_us smile swim
    with dspr
    mt "Забирайте себе средний отряд и отпустите уже Алису купаться!"
    scene dct_ext_beach_barhan                      # Заранее посовываем сцену с грибком и Женей.
    show mz bukal glasses pioneer far at right:
        ycenter 0.73
    
    show dct_ext_beach_day_with_pass_train
    show mt rage panama swim close
    with dissolve
    mt "Младший отряд! Стоять!"
    show mt angry panama swim close with dspr
    mt "Еще накупаетесь так, что из ушей вода побежит, а в первый раз заходим в воду по моей команде и ровно на две минуты.{w} Кто не услышит команды на выход, тот завтра останется без купания!"
    show mt rage panama swim close with dspr
    mt "Повторяю, по моей команде спокойно заходим в воду, кто в воду побежит, тот без купания останется уже сегодня!"
    hide mt with Dissolve(1.5)
    th "С таким голосом можно охотиться без ружья. Птицы сами падать будут."
    th "Или деревья таким голосом можно валить."
    extend " Как там героиню сказки звали?"
    show dct_ext_beach_day_with_pass_train:
        linear 1 alpha 0
    
    extend "{w=1} Перепилиха, кажется."
    "Женя сидела на опушке рощицы, отделяющей пляж от лодочной станции, и страдальчески морщилась."
    th "Зачем звали, спрашивается?"
    extend " Слушать эти вопли?"
    show d_mz hope glasses pioneer far as mz
    extend " Или…"
    scene dct_ext_beach_day_lifesaving_shield
    show d_el smile swim at cright
    show d_el shy2 swim as el2 at cright:
        alpha 0
        pause 2.5
        linear 0.2 alpha 1
    with pushright
    "Женя подняла глаза, чтобы глянуть на противоположный край пляжа, перехватила взгляд Сыроежкина, вздрогнула и опять зарылась носом в книгу."
    scene dct_ext_beach_barhan
    show d_mz confused glasses pioneer far at right:
        ycenter 0.73
    with pushleft
    "Пошарила левой рукой в пакете, извлекла оттуда бутылку с минералкой и пластиковый складной стаканчик. Сделала пару глотков и перелистнула страницу."
    show d_mz smile glasses pioneer far with dspr
    "Вообще-то на пляже было неплохо: лезть в воду Женю никто не заставлял и общество не навязывал. Вообще, большинство делало вид, что Жени не замечает."
    "Только Лена и Саша кивнули, но подходить не стали, хотя, как раз против их общества Женя не возражала."
    show d_mz shy glasses pioneer far with dspr
    "И Сыроежкин еще притягивал взгляд."
    scene dct_ext_beach_day_lifesaving_shield
    show d_el smile swim at cright
    with pushright
    "Не хотела на него смотреть, но каждый раз как пересекались взгляды, что-то словно обмирало внутри."
    show 3500_sh smile swim at cleft:
        ycenter 0.833 alpha 0
        pause 2
        linear 1 alpha 1
    show d_el think2 swim as el2 at cright:
        alpha 0
        pause 3.0
        linear 0.2 alpha 1
    "И было так одновременно страшно и приятно, что Женя даже начинала злиться на обоих кибернетиков, когда Шурик отвлекал Сыроежкина и тот не бросал взглядов на Женю."
    window hide
    scene dct_ext_beach_barhan
    show d_mz shyangry glasses pioneer far at right:
        ycenter 0.73
    with pushleft
    pause
    show black with dissolve
    play sound_loop dct_ambience_beach fadein 1
    scene dct_ext_beach_barhan
    show mz normal glasses pioneer far at right:
        ycenter 0.73
    with dissolve
    window auto
    "Физруки отправили в воду средний отряд и воздух заполнился криками и девчоночьим визгом."
    show mz bukal glasses pioneer far with dspr
    th "Что за люди? Зачем так кричать?"
    #опять недовольно поморщилась Женя.     # Опускаем
    "Официальная часть открытия купального сезона завершилась. Вожатая, окунув младший отряд, уже увела октябрят на спортплощадку. Средний отряд оказался предоставленным самому себе и устроил кучу-малу где-то на границе воды и суши."
    scene dct_cg_coin_volleyball with squares
    "Старший отряд, за вычетом Жени и кибернетиков, но зато с добавкой Максима и обоих физруков, затеял игру в волейбол."
    "Рядом с заведующей библиотекой шлепнулся мячик, обдав ее ноги песком."
    scene dct_ext_beach_barhan
    show d_mz sceptic glasses pioneer at right:
        ycenter 0.8
    with squares
    th "Так, пора закругляться."
    extend " Вожатая ушла, и больше меня тут никто и ничто не держит."
    show d_mz normal pioneer with dspr
    pause 0.25
    show d_mz normal pioneer:
        ease 0.6 ycenter 0.5
    "Книжка отправилась в пакет к бутылке с минералкой, а Женя поднялась с неожиданной грацией."
    show d_ma grin2 swim with dissolve:
        xcenter 0.4 yalign 0.02
    d_ma "Уходишь?{w=0.5} А может, с нами поиграешь?"
    "Упустивший подачу, и прибежавший за мячиком, Максим ждал ответа, вопросительно смотрел на Женю своими голубыми глазами невинного ангелочка и улыбался."
    show d_mz surprise pioneer with dspr
    # "Это предложение было так неожиданно и так нахально, что Женя чуть было не согласилась, и только осознание того, что вот она будет играть, такая неуклюжая и некрасивая, а ее будет разглядывать Сыроежкин, заставило Женю отказаться."   # По канону
    "Это предложение было так неожиданно и так нахально, что Женя чуть было не согласилась, и только осознание того, что вот она будет играть, такая неуклюжая и некрасивая, а ее будет разглядывать Сыроежкин, вынудило Женю не торопиться с ответом."
    show d_mz sceptic pioneer with dspr
    "А потом уже всплыло и подозрение, что и приглашают-то исключительно чтобы посмеяться над ее неуклюжестью. Но все равно, отказалась Женя гораздо мягче, чем могла бы."
    show d_mz smile2 pioneer with dissolve_fast
    mz "Не хочу пачкать форму. Так что без меня."
    show d_ma smile swim with dspr
    "Тут Женя вспомнила про загадочные журналы, про то, что хотела допросить Максима с пристрастием — где он нашел журналы, которые напечатают только через пять лет?{w} Но решила пока не пугать младенца и только спросила, прощаясь:"
    show d_mz sceptic pioneer with dissolve_fast
    mz "В библиотеку-то еще зайдешь?"
    show d_ma smile2 swim with dspr
    d_ma "Обязательно."
    show d_mz normal pioneer with dspr
    show d_ma normal swim with dspr
    hide d_mz with Dissolve(1.5)
    "Женя кивнула и, мысленно улыбаясь, пошла к себе в домик."
    hide d_ma with dissolve
    stop sound_loop fadeout 1.5
    stop ambience fadeout 1.5
    show black:
        alpha 0
        pause 0.5
        linear 1 alpha 1
    "До обеда оставалось сорок минут, и открывать библиотеку смысла не было, а вот план допроса юного пионера разработать стоило."
    scene black with dspr
    
    pause 0.5


    play music music_list['eat_some_trouble'] fadein 6
    scene bg int_house_of_dv_day with dissolve
    "Письмо, забытое, лежало в кармане."
    play sound_loop dct_ambience_beach fadein 1.5
    scene dct_ext_beach_day_lifesaving_shield
    show d_sf sad swim:
        xcenter 0.57
    show d_us smile swim:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with blinds
    "Когда на пляже появились довольная Ульяна и, как обычно, замороченный своими думами Сенька, Алиса взяла протянутый Ульяной тетрадный листок в клеточку, положила его в нагрудный карман рубашки, накинутой на плечи и помчалась сразу к своему отряду."
    scene dct_ext_beach_day_with_pass_train with dissolve
    th "Всё! А этих балбесов сами купайте, а то я с ними намучилась!"
    "У грибка, занятого отрядом, скинула, не глядя, рубашку и побежала в воду, откуда уже махала ладошкой Мику."
    scene dct_cg_coin_dv_on_beach with squares
    "На кромке воды остановилась и обвела взглядом пляж: Ольга с секундомером в руках и свистком в зубах, готовится дать октябрятам отмашку и разрешить им залезть в воду."
    "Семен с Ульяной построили средних лицом к реке, Семен что-то говорит им, средние хохочут в ответ, потом Ульяна отбегает к воде, а Семен отходит к левому флангу шеренги и командует: «На старт! Внимание! Марш!» — отряд срывается с места, и пионеры с визгом и хохотом несутся к воде."
    "Даже Катька забыла, что считает себя взрослой и тоже бежит в воду с визгом и хохотом."
    "Алиса на секунду ощутила острую зависть к малолетке: самой так же с хохотом пробежать — хочется, а стеснительно; а даже вспомнить, каково это — не получается, потому что сохраненных воспоминаний у копии — кот наплакал."
    th "Ну и черт с ним!"
    extend " Зато я живу, а она еще нет!"
    th "Катька, я против тебя ничего не имею, ты тоже обязательно проснешься и начнешь жить, но я уже сейчас живу, а ты еще нет!"
    scene dct_ext_water_islands_buoys_day with squares
    "Алиса опять повернулась к воде, погрозила кулаком Максиму, готовящемуся пустить ладошкой веер брызг в сторону Лены и, разбежавшись, покуда глубина позволяла бежать, в скольжении вошла в воду."
    th "Хоть Сенька и физрук, а плаваю-то я получше его."
    stop sound_loop fadeout 4
    "И красивым баттерфляем пошла к буйкам, уже ни о чем больше не думая и не видя Максима, проводившего ее восхищенным взглядом."
    show int_dining_hall_people_day:
        alpha 0
        pause 1.5
        linear 1 alpha 1
    "Купание, пляжный волейбол, обед… так часов до трех письмо и пролежало в кармане забытое и нетронутое."
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_dv_day with blinds
    "И только после обеда, когда Алиса завалилась в домике на койку и потянула к себе тетрадку, сложенный вчетверо листок напомнил о себе."
    stop music fadeout 2.5
    "Алиса потянула его из кармана, развернула и некоторое время просто разглядывала буквы собственного почерка."
    window hide
    
    pause 0.5
    
    $ set_mode_nvl()
    play music anewbeginning fadein 0.5
    stop ambience fadeout 0.5
    window show
    "Привет…{w=0.8} сестренка.{w} Раз уж Ульяны так между собой общаются, и я к тебе во сне так же обратилась, то и буду обращаться так же. Насколько я себя (тебя) знаю, ты не будешь против.{w} Кстати, это точно был сон? Потому что нашим: Мику, Ульянке и Славе снилось тоже самое.{w} Но что-то меня не туда понесло, начинаю сначала."
    "\nПривет, сестренка!{w} Обе Ульяны и Сенька очень хорошо о тебе отзываются, вот я и решила написать.{w} Очень бы хотелось познакомиться лично, но Сенька бьет себя пятками в грудь, морщит верхнюю губу и качает головой.{w} «Я, — говорит, — не уверен, что это безопасно для вас. Что одна из вас не исчезнет в течение получаса. Вы не настолько друг от друга отличаетесь, чтобы безопасно сосуществовать в одном узле. Имею, — мол, — опыт».{w} Приходится ему верить, а жаль.{w} А мне кажется, что мы с тобой не отражения одного и того же человека, а самостоятельные люди, просто, ну как двойняшки. Или потомки того самого человека.{w} Ты, конечно, поопытнее меня будешь и вон как высоко прыгнула — в помощницы вожатой (шучу), но и я не хуже.{w} Рассказала о твоей должности Славе, а та только улыбнулась и сказала, что сочувствует тебе. Вот так, тогда я тоже тебе сочувствую."
    "\nНе знаю, как вы себя чувствовали, когда проснулись, а мы четверо: я, Ульянка, Мику и Славя, просто в какой-то эйфории сейчас.{w} Все одновременно и знакомое и новое, а главное, не знаю как у других, но у меня это чувство свободы, когда я понимаю, что могу сама построить свою жизнь, а не крутиться внутри двух недель цикла. У меня даже со Славей отношения чуть получше стали.{w} Да, Сенька рассказал мне про активную фазу, но это же не окончательный приговор, Сенька же вырвался и Ульяна ваша, надеюсь, тоже."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "\nО наших делах не пишу, они, наверное, не очень отличаются от ваших.{w} Ульяна сказала, что на ее место в отряде вы Максима выбираете, надо будет к нашему присмотреться. Только не селите его третьим в домик к кибернетикам — пропадет парень."
    "\nЗавидую вам и сержусь на Сеньку, что он к вам от нас сбежал (про сержусь тоже шутка), потому что новый его двойник он пока так, ни рыба ни мясо.{w} Но хоть Сенька и сбежал к вам, но проснулся он именно у нас, я надеюсь, что в этом есть и моя заслуга, пусть я и не понимала что делаю. Так что тоже можешь мне завидовать."
    "\nСестренка, я очень хочу рискнуть и тебя увидеть, и, если ты не против, дай знать. Хоть через ваших Сеньку с Ульянкой дай знать, они в следующем цикле собрались опять к нам.\n\n\n{space=1200}{i}{size=+10}Алиса{/size}{/i}"
    "\nP.S. Приготовь свои детские воспоминания. Мы обязательно должны их сравнить!"
    stop music fadeout 2.5
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    scene black with dissolve2
    window hide
    
    pause 1
    nvl hide


    play ambience ambience_clubs_inside_day fadein 1
    scene int_clubs_male_day with dissolve
    $ set_mode_adv()
    window auto
    "Открытие купального сезона сдвинуло занятия кружка кибернетики на послеобеденное время."
    show d_oz n pioneer at right with dissolve:
        yalign 0.27
    extend " Ну и Оксана пришла."
    hide d_oz with dissolve
    "Ей выделили место за верстаком в углу, где она тихо, никому не мешая, вырезала из коры свой прощальный подарок Василию, иногда спрашивая помощи или совета у Электроника."
    show sh serious pioneer close with dissolve:
        zoom 1.25 anchor (0.5, 0.56) pos (0.15, 1.0)
    "Шурик, тот весь погрузился в пайку и отключился от внешнего мира. Очень уж ему хотелось, если не приступить к настройке, то хотя бы спаять электронную часть схемы."
    hide sh with dissolve
    show dct_fog:
        alpha 0
        linear 7 alpha 0.65
    "Поэтому он сидел спиной ко всем, время от времени бормотал что-то про себя, шипел, когда пальцы хватали раскаленные выводы радиодеталей и концы проводов, да канифольный дым из под жала паяльника все больше и больше наполнял комнату."
    "Когда в помещении кружка стало есть глаза, Электроник не выдержал. Открыл окно, распахнул дверь, выдернул из розетки паяльник и громко объявил:"
    show el serious pioneer behind dct_fog with dissolve
    el "Как ответственный за технику безопасности, объявляю пятнадцатиминутный перерыв на проветривание. Просьба всем выйти на улицу.{w} Шурик, тебя это тоже касается!"
    hide el with dissolve
    stop ambience fadeout 1
    
    play music music_list['everyday_theme'] fadein 2
    scene bg ext_clubs_day with slideawayup:
        zoom 3.0 xcenter 0.5 ycenter 0.6
    "Так и вышли на крыльцо все трое: Шурик, с листом миллиметровки в руках, тут же убежавший на полюбившееся ему место за зданием клубов, и Сергей с Оксаной, которые никуда не пошли, а присели тут же, на крылечке."
    show el normal pioneer far:
        zoom 0.8 xcenter 0.2 ycenter 0.87
    show d_oz n pioneer:
        zoom 0.6 xcenter 0.35 ycenter 0.9
    with dissolve
    el "Оксан, а ты почему не спишь? У младшего отряда же тихий час?"
    d_oz "Не хочу. Подарок важнее."
    show d_el think pioneer far as el with dspr
    el "А как же распорядок?"
    show d_oz d pioneer with dspr
    #Сергей искренне недоумевал. # Опускаем
    d_oz "Ну, распорядок, Сережа, это…"
    show black with dissolve_fast
    show el normal pioneer far:
        zoom 0.8 xcenter 0.2 ycenter 0.87
    show d_oz n pioneer:
        zoom 0.6 xcenter 0.35 ycenter 0.9
    show sh serious pioneer far behind black:
        zoom 0.8 xcenter 0.6 yalign 1.0
    hide black with dissolve_fast
    $ day_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Пятнадцать минут истекли, и пунктуальный Шурик появился на крыльце клубов, а Оксана и Сергей все еще увлеченно беседовали."
    window hide
    scene dct_ext_clubs_sunset with dissolve2:
        zoom 3.0 xcenter 0.5 ycenter 0.6
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    window auto
    "И так и продолжили разговор до самого вечера."
    show dct_ext_clubs_sunset:
        ease 1.5 zoom 1.0 ycenter 0.5
    show d_oz n pioneer:
        zoom .17 anchor (.5, 1.0) pos (.54, .72) alpha 0
        pause 1.8
        linear 0.7 alpha 1
    show 3500_el normal pioneer:
        zoom .17 anchor (.5, 1.0) pos (.46, .71) alpha 0
        pause 3
        linear 0.7 alpha 1
    show ext_houses_sunset:
        alpha 0
        pause 5.1
        linear 1 alpha 1
    show d_oz d pioneer as d_oz2 at cright:
        yalign 0.27 alpha 0
        pause 5.1
        linear 1 alpha 1
    show el normal pioneer at cleft:
        alpha 0
        pause 5.1
        linear 1 alpha 1
    "Электроник закончил монтировать приемники и излучатели на каркас установки, Оксана оставила почти готовый корпус корабля на верстаке, дождалась Сергея и пошла с ним по главной аллее в сторону площади, продолжая что-то объяснять, иногда забегая вперед и пятясь задом, чтобы видеть лицо Сергея."
    scene dct_int_house_of_el_sunset with fade
    "После ужина Электроник у себя в домике завалился на кровать, закинул руки за голову и улыбнулся."
    show d_oz smile pioneer at center with dissolve_fast:
        zoom 2.5 ycenter 0.95 alpha 0.5
    th "«Сережа, а давай я как-будто на тихом часе?»"
    show d_oz:
        linear 0.5 alpha 0
    extend " — Хорошо им, маленьким."
    extend " Даже если вожатая и обратит внимание, то скажет, что маленькая же, какой с нее спрос? Никакого."
    th "Ну а, с другой стороны, когда ей еще чем-то заниматься?"
    extend " Распорядок просто не предусматривает, что девочка из младшего отряда будет заниматься судомоделизмом."
    th " А у Оксаны хорошо получается."
    extend " Жаль, что она сейчас свой кораблик вырежет и уйдет, славная девочка, с ней как-то веселее работается."
    th "Но вот получается, что Оксана нарушила правила, чтобы сделать что-то новое."
    extend " Никому же раньше она кораблики не вырезала? Наверное, нет."
    th "И мальчику тому никто раньше корабликов не дарил."
    th " То есть, чтобы сделать что-то новое, нужно нарушить старые правила."
    th "Кстати, мы же должны были делать робота, вот и корпус для него уже готовый, и деталей куча, и в плане работы кружка у вожатой тоже робот записан."
    extend " А Шурик сказал Ольге Дмитриевне, что план это не забор, чтобы вдоль него ходить."
    extend " Надо будет еще поговорить с Шуриком на эту тему."
    th "Интересно, а к отношениям между людьми это можно применить?"
    stop music fadeout 1.5
    scene black with dissolve
    
    pause 1


    play ambience ambience_dining_hall_full fadein 1
    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show un smile3 pioneer close:
        xcenter 0.59 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    un "Как сходили?"
    "Сегодня за ужином у Леночки было настроение пообщаться, поэтому вопрос был задан с улыбкой и глядя в глаза."
    scene dct_int_dining_hall_table_sunset_back_people
    show d_sf smile pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us normal dress:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    me "Замечательно."
    "Семен аккуратно переложил свой кусок рыбы на пустую тарелку."
    me "Девочки, кто хочет рыбу, может не стесняться."
    show d_sf normal pioneer with dspr
    "Лена кивнула Семену, пододвинув тарелку к себе."
    us "Ленка, тебе большое и даже огромное спасибо от тамошней Мику."
    show d_us smile dress with dspr
    us "Она так и сказала: «А вашей Леночке передайте мою большую благодарность и даже огромное спасибо! Все так, как я и представляла, когда писала, и даже лучше!»"
    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show un serious pioneer close:
        xcenter 0.59 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    un "Передавайте."
    show d_un serious pioneer holds_out_hands close as un with dissolve_fast
    "Лена с преувеличенно серьезным выражением лица протянула обе руки к Персуновым."
    un "Передавайте, передавайте."
    scene dct_int_dining_hall_table_sunset_back_people
    show d_sf laugh pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us laugh dress:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    un "Ребята, я конечно девушка необщительная, но знаете, как я хочу попасть туда и посмотреть, что там делается."
    scene dct_int_dining_hall_people_sunset with fade
    "Ужин шел своим чередом."
    show el smile pioneer:
        xcenter 0.62 ycenter 0.7 alpha 0
        linear 1 alpha 1
    show d_va smile:
        zoom 0.93 xcenter 0.92 yalign -0.11 alpha 0
        pause 1
        linear 1 alpha 1
    show d_sz normal pioneer:
        xcenter 0.43 yalign 0.15 alpha 0
        pause 0.5
        linear 1 alpha 1
    show d_oz laugh pioneer:
        xcenter 0.78 yalign 0.15 alpha 0
        pause 0.5
        linear 1 alpha 1
    "Электроник неожиданно оказался за одним столом с тремя октябрятами из младшего отряда и о чем-то с ними оживленно беседовал."
    hide el
    hide d_va
    hide d_oz
    hide d_sz
    with dissolve
    show d_mz shyangry pioneer glasses at fleft:
        ycenter 0.65 alpha 0
        pause 0.5
        linear 1 alpha 1
    "Судя по особенно мрачному выражению лица Жени, то, что Сергей отвлекается на кого-то, ей явно не нравилось."
    hide d_mz with dissolve
    show mi grin pioneer far:
        xcenter 0.65 ycenter 0.72
    show d_ma laugh pioneer:
        zoom 0.75 xcenter 0.51 ycenter 0.78
    show sl laugh pioneer far:
        xcenter 0.34 ycenter 0.74
    with dissolve
    "Еще одна драма: Максим за одним столом с Сашей и Мику, и от их стола тоже доносится смех и оживленный разговор."
    show d_ka angry2 pioneer:                     
        zoom 0.825 xcenter 0.955 ycenter 0.95 alpha 0
        pause 0.5
        linear 0.7 alpha 1
    show dv guilty pioneer far:
        xcenter 0.07 ycenter 0.73 alpha 0
        pause 1.2
        linear 0.7 alpha 1
    "Вот только недовольные взгляды на Максима кидают двое: Катя — что ожидаемо, и Алиса."
    hide sl
    hide mi
    hide d_ka
    show d_ma smile pioneer
    with dissolve
    show d_ma shy pioneer as d_ma2:
        zoom 0.75 xcenter 0.51 ycenter 0.78 alpha 0
        pause 2
        linear 0.2 alpha 1
    show dv shy pioneer far as dv2:
        xcenter 0.07 ycenter 0.73 alpha 0
        pause 2
        linear 0.2 alpha 1
    "Нет, Максим тоже на Алису посматривает, вот они случайно пересеклись взглядами, покраснели и уткнулись в тарелки."
    scene dct_int_dining_hall_table_sunset_back_people
    show d_sf smile pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us normal dress:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    me "Как интересно. Пока мы ходили туда и обратно, Максим запал на пани Двачевскую?"
    us "Ты иронизируешь, Сём.{w} А вот Алиса подсчитала возраст своего тела и теперь комплексует по этому поводу."
    show d_sf normal pioneer with dspr
    me "Рыжик, так большинству здесь под сорок минимум."
    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show un sad pioneer close:
        xcenter 0.58 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    "А Лена тихо добавила:"
    un "А кое-кому и сильно больше."
    show mt normal pioneer close behind dct_int_dining_hall_table_sunset_front:
        xcenter 1.25 ycenter 0.23
        linear 0.6 xcenter 0.89
        pause 0.15
        linear 0.5 ycenter 0.5
    show un normal pioneer close with dissolve_fast
    "Подошла вожатая со стаканом чая в руках, присела четвертой за столик.{w} Посмотрела на Семена с Ульяной, хотела что-то сказать, но передумала."
    show mt smile pioneer close with dspr
    pause 0.2
    show mt smile pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter 1.25
    extend " Только кивнула, улыбнулась и молча ушла."
    show un smile2 pioneer close with dspr
    un "Зря от рыбы отказался. Кажется, повара научились готовить без указаний бабы Глаши."
    show un smile pioneer close with dspr
    "Лена разделалась с одной рыбиной и приступила ко второй."
    stop ambience fadeout 1
    scene black with dissolve
    
    pause 1


    play ambience ambience_camp_center_evening fadein 1
    scene bg ext_square_sunset:
    show un normal pioneer at cright:
        ycenter 0.65
    with dissolve
    "После ужина Лена устроилась на своей любимой лавочке, пыталась вчитаться и ничего не получалось. Книжка не шла."
    "Вместо этого вспоминался разговор с Семеном и Ульяной за ужином и привет от чужой Мику."
    show un smile pioneer with dspr
    th "Спасибо, Мику, твою сказку я зачитаю до дыр."
    show d_us normal dress behind un:
        zoom 0.5 xcenter 1.1 ycenter 0.66
        linear 2.8 xcenter -0.1
    "Опять вспомнилась баба Глаша."
    show un sad pioneer with dissolve_fast
    # Лена погрустнела.   # Опускаем
    $ sunset_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    th "Вот так умрешь, а через три дня о тебе уже никто и не помнит."
    show black with dissolve_fast
    $ night_time()
    $ persistent.sprite_time = "night"
    show bg ext_square_night
    show un normal pioneer
    hide black with dissolve_fast
    "Уже стемнело."
    show d_sf normal pioneer at cleft with MoveTransition(1.5, enter=_moveleft, enter_time_warp=_ease_time_warp)
    show d_sf normal pioneer:
        linear 0.4 ypos 0.12
    extend " Семен, совершающий вечерний обход лагеря, на минутку подсел рядом."
    show d_sf smile pioneer with dspr
    me "Лен, я все думал, что ты будешь делать, когда в библиотеке кончатся книги? И вот, кажется, я дождался."
    show un smile pioneer with dspr
    un "Буду просить вас с Ульяной проводить меня в Шлюз и обратно. В тамошнюю библиотеку. Там, наверное, есть еще что-то."
    show d_sf sad pioneer with dspr
    me "Знаешь, я не помню. На тот момент меня содержимое библиотеки интересовало слабо."
    show d_sf normal pioneer with dspr
    extend " Но можно еще пройтись по жилым корпусам…"
    # Семен оборвал сам себя.   # Опускаем
    show un normal pioneer
    show d_sf serious pioneer
    with dspr
    me "Лен, если пойти сейчас — там Второй. Ты выдержишь, но я не уверен, что тебе понравится увиденное."
    show un sad pioneer
    show d_sf normal pioneer
    with dissolve_fast
    me "А через три дня он приедет сюда, и тебе не захочется покидать лагерь."
    show un serious pioneer with dissolve_fast
    un "Да, ты прав. Только, пожалуйста, не называй его больше Вторым.{w} Я понимаю, что ничего обидного ты в это прозвище не вкладываешь, но не надо."
    show d_sf serious pioneer with dspr
    pause 0.4
    show d_sf normal pioneer
    show un normal pioneer
    with dissolve_fast
    "Семен глянул в глаза Лене, хотел что-то сказать, но только кивнул, дернулся, чтобы пожать предплечье, но не стал, а снова кивнул."
    show d_us normal dress:
        xzoom -1.0 xcenter -0.1 ycenter 0.66
        easein 2.8 xcenter 1.1
    show d_sf normal pioneer:
        linear 0.4 ypos 0.0
        pause 0.15
        easeout 2.5 xcenter 1.2
    "Пожелал спокойной ночи и, махнув рукой пробегавшей мимо Ульяне, чтобы подождала, ушел к себе в спорткомплекс."
    show un serious pioneer with dissolve_fast
    th "Надо будет обязательно собраться: мне, физрукам, Алисе, может быть моему Семену."
    extend " Собраться и поговорить о прошлом цикле."
    th "Алиса что-то знает, но молчит, несколько раз порывалась поговорить, но сама же передумывала. Персуновы тоже странно смотрели на ожоги на моих руках."
    show un sad pioneer with dissolve_fast
    th "А я ничего почти не помню, провал в памяти и словно обрывки сна."
    th "Но они же держали свои руки на моих плечах, отдавая мне свою силу, это точно. И я помню это, и они помнят."
    show un surprise pioneer with dspr
    th "Сегодня Алиска на пляже положила свою ладонь мне на плечо, так мы обе вздрогнули!"
    show un normal pioneer with dissolve_fast
    "На площади появился Максим с горном под мышкой."
    show un smile pioneer with dspr
    "Махнул рукой Лене, поставил горн на землю, повозился с металлической коробочкой, прикрепленной позавчера кибернетиками к одному из флагштоков."
    $ renpy.sound.set_volume(1.5, delay=0)
    $ renpy.sound.set_volume(0.5, delay=0, channel='sound2')
    play sound2 sfx_radio_squelch_2 
    play sound [ "<silence 1.7>", dct_sfx_horn_rebound_through_loudspeaker ]
    show un smile pioneer with dspr
    "В громкоговорителях, развешанных на столбах, что-то зашипело, а потом зазвучал сигнал отбоя."
    # "Максим протрубил трижды, выключил усилитель, улыбнулся Лене и убежал к домикам." # Опускаем
    th "Пора и мне умываться и спать."
    show un normal pioneer with dspr
    "Лена закрыла книгу, глянула на название и вздохнула."
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Завтра верну в библиотеку, незачем себя мучить."



    stop sound fadeout 3.5
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound3')