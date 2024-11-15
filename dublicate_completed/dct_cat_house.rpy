label dct_cat_house:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nПролог."
    $ day_time()
    play music music_list["mystery_girl_v2"]
    show headline_text u"Кошкин дом" at truecenter with dspr
    pause
    hide headline_text with dissolve
    stop music fadeout 1
    
    scene ext_square_night with dissolve
    show dct_dream_veil:
        shiver
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    show d_ar adl serious casual behind dct_dream_veil at center
    uv_cst "Прощай. Я сделаю, как ты сказал. Но однажды я приду за тобой. Что толку от хранительницы, если по этой земле не будут ходить люди?"
    
##############
#Первая жизнь#
##############
   
label dct_the_first_life:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nПервая жизнь."
    $ day_time()
    show headline_text2 u"Первая жизнь" at truecenter with dspr
    pause
    hide headline_text2 with dissolve

    scene dct_int_residential_block_day with blinds
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound dct_sfx_meow1
    "Это была обычная молоденькая кошка, жившая, правда, в необычном месте. Но кошка о том не знала и нисколько о том не беспокоилась."
    play music music_list["my_daily_life"] fadein 2
    "Тем более что и хозяева её беспокойства не проявляли, а кошечка считала себя во всём подобной своим хозяевам."
    show cat_uv washing small with dspr:
        pos (0.33, 0.56)
    mss "Миша! Не забывай девочку кормить! И играть с ней! И будешь уходить — смотри, чтобы она не убежала! Всё, тороплюсь, а то на автобус опоздаю!"
    play sound sfx_close_cabinet
    hide cat_uv with dspr
    mic "Девочка, девочка… Зачем только притащили её сюда?"
    mic "Ты где, кстати? Девочка?"
    show cat_uv attacking large with dspr:
        pos (0.3, 0.3)
    play sound dct_sfx_meow2
    mic "Ай! Брысь!"
    hide cat_uv
    show cat_uv itchy small:
        pos (0.6, 0.8)
    with dspr
    mic "{i}Ох, Светка. Завела себе заменителя ребёнка, а сама ему даже имя дать не удосужилась: доча, девочка, иногда кошечка, а чаще всего — кошкодевочка.{/i}"
    mic "{i}А теперь Светка на материк укатила, а эту «кошкодевочку» на меня спихнула.{/i}"
    show cat_uv waiting small with dspr:
        pos (0.6, 0.75)
    play sound dct_sfx_meow4
    $ renpy.pause (1)
    show cat_uv waiting medium with dspr:
        pos (0.5, 0.6)
    mic "Получишь ты свой завтрак, дай умыться."
    show cat_uv waiting large with dspr:
        pos (0.1, 0.15)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    mic "Чего? Лоток, говоришь, полный?"
    play sound dct_sfx_meow5
    $ renpy.pause (1)
    show cat_uv waiting small with dspr:
        pos (0.3, 0.75)
    mic "Всё тебе «мяу». А мне опять газеты в библиотеке просить."
    mic "А потом кто-нибудь поинтересуется: «Михаил Сергеевич, а куда вам столько газет?» — и что я отвечу? Сколько риска, оказывается, в содержании одной маленькой кошечки."
    mic "Кошкодевочка, может, ты на песок перейдёшь?"
    play sound dct_sfx_meow4
    $ renpy.pause (1)
    mic "Ну, как скажешь."
    hide cat_uv with dspr
    show blinking
    stop music fadeout 1
    $ renpy.pause (1)
    stop ambience
    
    scene dct_int_residential_block_day with dspr
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show cat_uv waiting small with dspr:
        pos (0.6, 0.75)
    mic "Ну что, зверь. Проживёшь без меня полдня?"
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    mic "Радуйся, завтра смена цикла, так что сегодня рабочий день сокращённый."
    show cat_uv waiting medium with dspr:
        pos (0.3, 0.6)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    mic "И не проси, больше еды не дам."
    show cat_uv itchy medium with dissolve:
        pos (0.25, 0.73)
    mic "Не доверяю я тебе. Боюсь, приду домой сегодня, а тут всё разгромлено одной ма-а-а-аленькой кошечкой. Выгнать её из дому тогда придётся."
    mic "А ты только и рада будешь, если выгоню. Эта каморка даже для кошки тесная. Но потерпи, командировка закончится — мы на материк вернёмся, в нормальную квартиру."
    mic "Молчишь? Понимаешь, что не выгоню? Так и ты веди себя прилично."
    mic "Всё, пока. Жди к обеду и не пакости."
    play sound sfx_close_cabinet
    show cat_uv waiting medium with dissolve:
        pos (0.3, 0.6)
    play sound dct_sfx_meow5
    $ renpy.pause (1)
    hide cat_uv with dspr
    show blinking
    $ renpy.pause (1)
    stop ambience
    
    scene dct_int_residential_block_day with dspr
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "А кошечка ещё поиграла, пытаясь поймать собственную тень, подремала на хозяйской кровати, посидела на подоконнике. А потом, когда порыв ветра распахнул не закрытую на завёртку форточку, перебралась туда."
    "Были бы дома хозяева — они бы не допустили такого. Домашних животных запрещалось держать в посёлке, и котёнка протащили нелегально, но хозяйка укатила на материк, хозяин ушёл на работу, и снять безымянную кошку с окна оказалось некому."
    stop ambience
    
    scene dct_ext_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["i_want_to_play"]
    "Эта кошечка ничего не знала про запреты. Эта кошечка не относилась к числу осторожных домоседок. Этой кошечке нравилось ходить где вздумается и гулять самой по себе."
    "Она посидела в проёме, потом чем-то заинтересовалась и перепрыгнула на разросшуюся поблизости старую рябину, а оттуда уже спустилась на землю."
    show cat_uv walking small with dspr:
        pos (0, 0.85)
    "И пошла изучать территорию, попутно пытаясь охотиться на воробьёв."
    d_u1 "Кис-кис-кис… Ты чья такая будешь, красивая?"
    show d_us smile sport at right with dspr:
        zoom 1.5
        ypos -0.05
    $ renpy.pause (0.5)
    show cat_uv waiting medium with dspr:
        pos (0.1, 0.6)
    voice "Ульяна! Ну где вы опять застряли? Тепловоз вас ждать не будет, давайте быстрее! Бумаги заберёте и с дневным поездом сразу назад. А то в тех краях буря ожидается."
    us "Вот ведь дядька — мало того, что похож на Сёмку как старший брат, так и такой же гад и зануда. Ладно, живи пока, киса. Ещё увидимся. Встретишь моего Сёмку — привет передавай!"
    show d_us normal sport at right with dspr:
        zoom 1.0
        ypos -0.05
    us "Иду, Семён Семёнович!"
    hide d_us with moveoutright
    show cat_uv walking small:
        pos (0, 0.85)
    with dspr
    $ renpy.pause (2)
    stop music fadeout 1
    stop ambience
    
    scene ext_path2_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    show cat_uv walking medium with dspr:
        pos (0.6, 0.6)
    "Рыжая девушка убежала по своим важным делам, а кошка отправилась дальше. Изучать свой новый мир."
    $ renpy.pause (2)
    stop ambience
    
    scene ext_path_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    show cat_uv walking medium with dspr:
        pos (0.3, 0.6)
    play sound dct_sfx_meow3
    $ renpy.pause (2)
    stop ambience
    
    scene dct_int_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["farewell_to_the_past_full"]
    "А у хозяина кошечки завершился рабочий день."
    play sound sfx_open_dooor_campus_1
    mic "Животное, я дома."
    mic "Выходи, сейчас обедать будем."
    mic "Кошочка!"
    play sound sfx_wood_floor_squeak
    mic "Ну и где ты спряталась?"
    show blinking
    $ renpy.pause (1)
    mic "Только не говори, что ты убежала. Потому что если на глаза кому попадёшься…"
    mic "Кис-кис-кис…"
    mic "Уволить, конечно, не уволят, но на материк вышлют — Толяныч постарается. И тогда прощай, диссертация, прощай, премия, прощай, двойной оклад. И прощай, новая квартира."
    mic "Кис-кис-кис…"
    mic "Светка меня убьёт. Сначала за то, что ты сбежала, а потом за всё остальное."
    show blinking
    $ renpy.pause (1)
    mic "Удрала. Придётся искать."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    mic "Ты только найдись побыстрее, пожалуйста. И сделай так, чтобы никто тебя не заметил."
    scene dct_ext_residential_block_day with slideleft
    mic "Кис-кис-кис…"
    stop ambience
    
    scene dct_ext_module_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    mic "А если ты нагуляешься, а потом корпус перепутаешь и придёшь к чужим людям? Тогда придётся отказываться, врать, что не знаю, чья это кошка."
    scene dct_ext_module_day with slideleft
    mic "Кис-кис-кис…"
    stop ambience
    
    scene dct_ext_module_smoking_place with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["just_think"]
    mic "А если ты в подвале где-то? Вы же, кошки, любите в подвалах прятаться. Это значит, у коменданта ключи просить, а как объяснишь, зачем?"
    voice "Михаил Сергеевич, потеряли что-то?"
    scene dct_ext_module_smoking_place with vpunch
    show d_to normal casual at center with dspr
    d_to "Вы что-то ищете?"
    mic "Нет, то есть да, Анатолий Васильевич."
    mic "То есть нет, бурундука выслеживаю. Иду, смотрю — бурундук сидит. Хотел его семечками угостить, а он убежал. Я за ним, но, кажется, увлёкся."
    show d_to smile casual with dspr
    d_to "А, ну тогда доброй охоты. И ни пуха, ни пера."
    mic "Спасибо."
    hide d_to with moveoutright
    mic "{i}Про{w=1}-нес{w=1}-ло.{w=2} Или надо было к чёрту его послать? А ловко я вывернулся с бурундуком.{/i}"
    mic "Кис-кис-кис…"
    stop ambience
    
    scene dct_int_residential_block2_sunset with squares
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_evening
    "Михаил обошёл весь посёлок: от складских пакгаузов до пристани и от мастерских до казармы. И сейчас, не включая света, сидел у себя в комнате, ужинал холодными слипшимися макаронами и страдал."
    mic "Удрала, котильда. А я даже объявления расклеить не могу. И на кой чёрт мы её сюда притащили? Это всё Светка, её прихоть."
    mic "Ладно если просто сбежала. Светка покричит, подуется и простит. А если её нашёл кто? Это же ЧП и нарушение режима: домашнее животное на территории посёлка."
    mic "Дурацкое правило, но Толяныч своего не упустит. Завтра же вызовет: «Михаил Сергеевич, как ваша вчерашняя охота на бурундука? А ваш бурундучок — он случайно не мяукает?»."
    play sound sfx_radio_squelch_1
    d_dy "Добрый вечер, жители посёлка. Напоминаю, что начинается смена циклов, в связи с чем с двадцати ноль-ноль пятницы и до восьми ноль-ноль понедельника выход в ночное время из посёлка запрещён."
    d_dy "Не рекомендуется также в ночное время выходить из зданий и сооружений без крайней необходимости. Исследовательские группы, находящиеся за пределами посёлка, должны укрыться в экранированных убежищах."
    play sound sfx_radio_squelch_2
    mic "Вот так. А ведь я мог бы ещё сегодня успеть и за территорией пробежаться. Забор-то вот он — рядом с корпусом. И дыр в этом заборе полно."
    mic "Ну ладно, кошка. Сделать сегодня уже ничего нельзя, а завтра продолжу тебя искать."
    stop music fadeout 1
    stop ambience
    show blink
    
    scene dct_ext_backroad_sunset_7 with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_forest_evening
    show cat_uv walking2 medium with dspr:
        pos (0, 0.7)
    "А кошка сначала охотилась на мелкую живность, потом, когда уже собралась возвращаться, пришлось спасаться на дереве от голодной лисы."
    stop ambience
    
    scene dct_ext_backroad_night_7 with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    "Так и просидела до темноты на дереве, пока лису не отвлекла более доступная еда."
    stop ambience
    
    scene dct_ext_backroad_light_7 with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    play music music_list["into_the_unknown"] fadein 2
    play sound dct_sfx_5500Hz
    "А когда стемнело, когда засвистело с частотой пять с половиной килогерц проволочное ограждение вокруг посёлка, когда над забором вспыхнули тускло-красные огни, от земли начал подниматься туман."
    show dct_ext_backroad_fog with dissolve2
    "Туман сочился, кажется, из самой почвы и постепенно распространялся вверх, достигая вершин самых высоких деревьев."
    "Только посёлок оставался в чистом пятне, да несколько пятен поменьше располагались в окружающих посёлок лесах."
    "Что интересно, всякая дикая ночная живность вела себя так, будто этого тумана вовсе не существует. Ёжики топотали. Летучие мыши носились, пронзая пространство пучками ультразвука."
    play sound sfx_owl_far
    "Сова спикировала на мышку, и никакой туман не помог той мышке укрыться. Так она и отправилась в свой последний полёт в когтях совы."
    play sound dct_sfx_meow3
    "Кошечка же боялась, звала хозяев на помощь всё громче и громче: «Где же вы! Помогите! Мне страшно!». Что-то, чего не замечали дикие твари из дикого леса, заставляло её бояться."
    "Так продолжалось до тех пор, пока туман не поднялся настолько, что коснулся кончика её хвоста. Крики о помощи тут же прекратились, когти втянулись, тельце расслабилось и съехало вниз по ветке к стволу, а оттуда уже безвольным комком рухнуло на землю."
    "А туман продолжал стоять, молочно-белой стеной окружая посёлок, иногда выпуская щупальце, которым касался ограды, пробуя её то ли на вкус, то ли на прочность."
    hide dct_ext_backroad_fog
    play sound dct_sfx_crow
    "А где-то за час до рассвета туман просто исчез, словно его взяли и выключили. А ещё через пятнадцать минут пришла в себя каштановая кошечка."
    show cat_uv washing medium with dspr:
        pos (0.8, 0.7)
    play sound dct_sfx_meow4
    "Встала как ни в чём не бывало, умылась и побежала к калитке в заборе."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show cat_uv walking2 medium with dspr:
        pos (-0.1, 0.75)
    "Пролезла под калиткой, прокралась мимо дремлющего дневального и оттуда уже по прямой направилась к дому. Очень хотелось есть, и она ужасно соскучилась по хозяевам."
    stop ambience

    scene dct_int_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Михаил проснулся, как всегда по выходным, в восемь утра."
    mic "Животное!.."
    mic "Ах да! Ну ничего, сейчас чаю попью и пойду тебя искать."
    play sound dct_sfx_meow1
    $ renpy.pause (1)
    mic "Кошка!"
    show cat_uv waiting small with dspr:
        pos (0.6, 0.75)
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    show blink
    "Всё, что кошка хотела в данный момент — это спать. Спать дома, на одном из своих привычных мест. Глаза у неё закрылись, она обвисла на руках у хозяина и даже не почувствовала, как её положили на любимое место — на спинку кресла."
    "Только приблизительно через час кошка проснулась ненадолго с тем, чтобы перебраться на колени к сидящему здесь же в кресле хозяину. Так они и продремали, снимая стресс друг у друга, почти до самого приезда хозяйки."
    stop ambience
    
    scene dct_int_residential_block_day with slideleft
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["afterword"]
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    mic "Ну и где ты шлялась?"
    play sound dct_sfx_meow7
    $ renpy.pause (1)
    mic "Я весь посёлок обежал."
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    mic "Ты, главное, Светке не рассказывай. И выпускай меня из дома уже. Пойду Светку встречать."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_residential_block_day with slideleft
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    "Полчаса спустя кошачий рассказ повторился."
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    ms_s "Ой ты моя девочка, по маме соскучилась, вон как разговорилась. Ой ты какая ласковая."
    mic "Это она с тобой ласковая. А на меня она охотится."
    play sound dct_sfx_meow7
    $ renpy.pause (1)
    ms_s "Правильно, кошкодевочка. На папку можно охотиться, он большой и сильный."
    show blinking
    hide cat_uv
    ms_s "Миша, тебе не кажется, что она изменилась?"
    mic "Свет, она же по сути котёнок ещё, дети всегда меняются."
    ms_s "Нет, это другое… Ну ладно."
    stop ambience
    
    scene dct_ext_residential_block_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play music i_tried_to_bring_it_back
    play ambience ambience_camp_center_night
    "И опять потянулись цикл за циклом. Может быть только кошечка росла чуть быстрее и становилась чуть крупнее, чем это положено обычной кошке, да стала интересоваться растительной пищей, опять же больше обычного. Но не настолько, чтобы это казалось чем-то из ряда вон."
    stop ambience
    
    scene dct_int_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show cat_uv washing medium with dspr:
        pos (0.3, 0.7)
    "И хозяйка периодически восхищалась кошачьей разумностью."
    ms_s "Такая умница, такая умница! Миш, она шпингалеты открывать научилась! А вчера я пришла раньше тебя, так она меня так встречала и всё-всё мне рассказала. Казалось, что я вот-вот её пойму! Правда? Кошкодевочка ты моя!"
    stop ambience
    
    scene dct_ext_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    "А Михаил так и не рассказал Светлане о пропаже и возвращении кошки."
    "Светлана между циклами каждый раз уезжала на материк — проверить старую квартиру. Михаил оставался, работал у себя в лаборатории, зарабатывал себе непрерывный стаж работы в районе аномалии и приближал свою пенсию."
    "«Кошкодевочка» всегда встречала хозяев с работы и больше не заставляла себя искать. Форточку в спальне, через которую кошка убежала, понятливый Михаил завесил сеткой — якобы от ос."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_residential_block_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    "Вот только в ночь между циклами, когда Михаил засыпал, или, бывало, что днём, когда все были на работе, уже в кухонном окне открывалась форточка, тёмный силуэт выскальзывал наружу и устремлялся за забор, за пределы экранированной территории."
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    stop ambience
    
    scene dct_int_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Но утром форточка оказывалась запертой, а «кошкодевочка», как обычно, караулила в засаде, чтобы, когда Михаил спустит ноги и всунет их в шлёпанцы, атаковать его левую лодыжку."
    show cat_uv attacking large with dspr:
        pos (0.3, 0.3)
    play sound dct_sfx_meow2
    $ renpy.pause (1)
    mic "Ай! Брысь!"
    stop ambience

##########
#Существо#
##########
    
label dct_creature:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nСущество."
    $ day_time()
    show headline_text2 u"Существо" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_int_residential_block_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    play music music_list["trapped_in_dreams"]
    "Была очередная ночь между циклами. Хозяйка, как всегда, укатила на материк. Хозяин спал. Да и вообще во всём посёлке не спали, может быть, только дежурные на воротах."
    show cat_uv walking2 medium with dspr:
        pos (0.35, 0.7)
    "Кошка бесшумно спрыгнула со спинки кресла и прошла на кухню. Постояла в дверях несколько секунд, потом осторожно толкнула лапой дверь, отделяющую кухню от спальни."
    "Посмотрела на спящего Михаила, кажется, даже с сожалением. Качнулась к нему, как будто собиралась позвать с собой."
    "Она и звала уже, не один раз. Только вот Михаил не понимал этого «мяу», означающего «Ты пойдёшь со мной?»."
    hide cat_uv
    "Кошка шагнула на кухню и прикрыла за собой дверь. Постояла, прислушиваясь, запрыгнула на подоконник, с подоконника — вертикально вверх к форточке, а там, зацепившись тремя лапами за переплёт, ухватилась четвёртой за форточную завёртку."
    "Неожиданно длинные пальцы обхватили металл, повернули и потянули. Путь на улицу был свободен."
    stop ambience

    scene dct_ext_residential_block_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show cat_uv walking medium with dspr:
        pos (0.6, 0.6)
    "Прочь из комнаты, из жилого блока, из посёлка! На волю!"
    "Кошка бежала вдоль аллеи к старому корпусу."
    "Можно было не опасаться, что её обнаружат: давно уже стемнело, а люди в последние ночи циклов предпочитали отсиживаться по домам."
    stop ambience
    
    scene ext_path_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    show cat_uv walking2 medium with dspr:
        pos (-0.1, 0.75)
    "Но вот, наконец, и калитка. Кошка обежала будку дневального сзади, прокралась вдоль забора, пролезла под калиткой и побежала прямо в туман, вся дрожа от радостного возбуждения."
    show ext_path_night_fog behind cat_uv with dissolve
    "И когда язык тумана прикоснулся к её голове, она не упала в обморок, а только замерла, подавшись чуть вперёд и тихо, незаметно для себя, мурлыкая."
    hide cat_uv with dspr
    "Так продолжалось с половину минуты, а потом кошка пришла в себя, встряхнулась и побежала в старый лагерь, по пути устраивая засады на мышей."
    "Какое-то время её скрадывала старая знакомая лиса, но, оценив размеры и энергию кошки, решила не связываться, а поискать добычу попроще, благо мышей, кузнечиков и лягушек хватало на всех."
    stop music fadeout 1
    stop ambience
    
    scene ext_old_building_night_moonlight with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_old_camp_outside
    "А кошка, закусив по пути неосторожной мышкой, добежала до старого корпуса, забралась там на чердак, где и проспала большую часть ночи."
    stop ambience
    
    scene dct_int_residential_block2_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_day
    show cat_uv walking2 medium with dspr:
        pos (0.25, 0.7)
    "Незадолго до рассвета кошка тем же путём вернулась домой, прихватив по пути ещё одну мышку."
    stop ambience
    
    scene dct_int_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow4
    $ renpy.pause (1)
    play music music_list["i_want_to_play"]
    mic "Ты решила со мной едой поделиться?"
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    mic "И за мышкой ты на улицу бегала, потому что дома у нас нет мышей."
    play sound dct_sfx_meow5
    $ renpy.pause (1)
    mic "Ты понимаешь, что нельзя так делать?"
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    mic "Вот тебе и «мяу». Попадёшься рано или поздно — скандал будет."
    play sound dct_sfx_meow4
    $ renpy.pause (1)
    hide cat_uv with dspr
    stop music fadeout 1
    "Невнимательный к мелочам, как и большинство мужчин, Михаил совсем не обращал внимания на происходящие с кошкой перемены."
    "А вот хозяйка…"
    show blinking
    $ renpy.pause (2)
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow6
    $ renpy.pause (1)
    ms_s "Ах ты моя кошечка, ну-ка иди сюда, мама сейчас посмотрит, что с тобой такое."
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow7
    $ renpy.pause (2)
    ms_s "Ми-и-иш! Кажется, наша девочка заболела."
    show cat_uv washing medium with dspr:
        pos (0.25, 0.65)
    ms_s "Смотри, у неё шерсть лезет."
    ms_s "Я её только погладила, а тут вот. И смотри, как голова у неё опухла. И шишки какие-то на теле и лапах. Может, её ветеринару показать? У тебя есть знакомые?"
    mic "Мои знакомые все на материке. И те коров и лошадей пользуют. А здесь… В виварий отнести, как-то же они своих крыс и макак лечат?"
    mic "Только это прямой путь вылететь отсюда в двадцать четыре часа."
    ms_s "И что же делать?"
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    ms_s "Доча, помолчи! Видишь, от тебя одни проблемы!"
    stop ambience

    scene dct_int_residential_block_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    ms_s "Миш, как думаешь, может, она мутацию какую подцепила? Может, и мы такие же станем? Вдруг она нас укусит?"
    mic "Ага, с нами живёт оборотень. Но мы такими же не станем. Мы станем другими. Не говори глупостей, Свет. Давай понаблюдаем за ней, а там видно будет."
    "Так слово «оборотень» было произнесено в первый раз."
    stop ambience
    
    scene dct_int_residential_block_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Однако понаблюдать не удалось."
    "В воскресенье ничего нового не произошло, а в понедельник Михаил ушёл на работу с твёрдым намерением договориться с ветеринаром вивария. Светлана же, которой на работу надо было на час позже, осталась с кошкой наедине."
    ms_s "Чем же ты болеешь, киса? Нет, ничем ты не болеешь, вон какая весёлая."
    queue sound sfx_home_phone_take
    queue sound dct_sfx_phone_disk
    $ renpy.pause (2)
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    ms_s "А может, ты уже и не киса вовсе?"
    show cat_uv itchy medium with dissolve:
        pos (0.25, 0.7)
    ms_s "Алло, это Светлана, я опоздаю сегодня на работу? Что-то плохо себя чувствую."
    voice "…"
    ms_s "Спасибо большое. К обеду обязательно приду."
    $ renpy.pause (1)
    play sound sfx_home_phone_break
    $ renpy.pause (1)
    play music music_list["dance_of_fireflies"]
    ms_s "Ну вот, кошкодевочка. А у нас с тобой есть дело. Хочешь, я тебя колбаской угощу? Любишь ведь колбаску?"
    show cat_uv waiting large with dspr:
        pos (0, 0.15)
    play sound dct_sfx_meow3
    $ renpy.pause (1)
    ms_s "Ну, иди тогда сюда."
    hide cat_uv with dspr
    ms_s "Вкусная колбаска? А сейчас мы с мамой пойдём на прогулку. А то сколько тут живём, а ни разу не гуляли."
    "Ловко перехваченная под живот кошка отправилась в старую спортивную сумку, с которой Михаил иногда ходил на рыбалку."
    "Чтобы кошка вела себя спокойно, Светлана наскоро накинула на неё старый ошейник."
    "Кошка не возражала, она доверяла своим хозяевам и помнила, как приехала сюда в этой самой сумке и в этом самом ошейнике."
    stop ambience
    
    scene dct_ext_cliff_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_lake_shore_day
    "Заблудиться было невозможно. Держись вдоль реки и отойди от посёлка как можно дальше. Самым трудным было пролезть сквозь дырку в заборе, но дальше всё прошло как по маслу."
    "Час Светлана двигалась по натоптанной тропинке вдоль берега, постепенно поднимающегося обрывом над рекой. Постояла, взвесила в руке сумку, прикинула, добросит до воды или нет, но пожалела животинку — всё-таки много хороших воспоминаний с ней было связано, и пошла дальше."
    "Удалившись от посёлка километров на пять и почти упёршись здесь в Периметр, Светлана остановилась. Она когда-то читала, что кошки не отходят в своих странствиях от дома дальше, чем на два километра, поэтому посчитала расстояние достаточным."
    stop music fadeout 1
    #show dct_sport_bag with dspr
    ms_s "Ну всё, киса. Будь счастлива."
    play sound dct_sfx_meow3
    show blink
    $ renpy.pause (3)
    stop ambience
    
    scene dct_int_residential_block_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    ms_s "Миша, доча убежала. Я дверь открыла, а она вперёд меня и на улицу. А я ещё не обутая была, пока обувалась, а дочи уже нет нигде."
    mic "Может, вернётся ещё? Не переживай."
    stop ambience
    
    scene dct_ext_cliff_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_lake_shore_night
    "А доча смогла наконец раздвинуть половинки молнии, выползти наружу и убежать, перепуганная, сама не зная куда. При этом она не замечала, что бежит на двух ногах, лишь изредка опускаясь на четвереньки. Для неё все перемены были естественными."
    $ set_mode_nvl ()
    play music music_list["two_glasses_of_melancholy"]
    "Так начался третий этап кошачьей жизни, о котором, в общем-то, мало что известно."
    "Люди кошку не видели, потому что не любили без нужды покидать посёлок."
    "Может быть, пионеры? Но о чём друг другу рассказывают НБО, собираясь вечерами в библиотеках лагерей, особо никто из людей не интересовался."
    "В общем-то, это была обычная жизнь дикой кошки: утром и вечером поймать по паре мышей, днём и ночью поспать."
    "А то, что шерсть с боков вылазит, оставляя голую кожу — это же, наверное, так и должно быть. И тело подрастало раз в две недели, так что мышей на пропитание скоро перестало хватать."
    "Бывшая кошка открыла для себя грибы, орехи и ягоды. Холодно ей в бесконечном лете не было, а в те дни, когда налетали местные, короткие и мощные бури, всегда можно было укрыться в старом корпусе или в подземелье."
    "Изменилось зрение: казалось, что всё пространство наполнено лёгкой светящейся дымкой, разрежённой в некоторых местах."
    "И если сделать определённое усилие — она бы не смогла объяснить, какое, — то можно, шагнув туда, в это место и сквозь это место, оказаться совсем в другом лесу."
    "Очень похожем на привычный, но всё же в другом. Шагнуть, поохотиться, но потом обязательно вернуться обратно."
    "О своих хозяевах и старом доме она почти не вспоминала. Так, две большие фигуры, весьма расплывчатые. И место, где не нужно было ловить мышей для пропитания и где можно было спать на тёплых коленях."
    "Что такое колени — бывшая кошка помнила и понимала, потому что у неё самой теперь были почти такие же."
    stop music fadeout 1
    $ set_mode_adv ()
    stop ambience

    scene dct_ext_old_building_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Кошки, даже бывшие, на самом деле не любят отходить далеко. Вот и эта только и освоила, что пятно радиусом два километра по горизонтали, и ещё такие же пятна в остальных узлах Сети, до которых могла дотянуться."
    #ЦГ с силуэтом "чудища".
    "Вот только центр этого промыслового участка постепенно смещался на восток, в сторону посёлка, пока не совпал со старым корпусом."
    stop ambience
    
    scene dct_ext_kpp3 with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play music music_list["door_to_nightmare"]
    $ set_mode_nvl ()
    "Дневальный по контрольно-пропускному пункту сидел в будке КПП и проигрывал битву со сном."
    "Делать было абсолютно нечего. Журнал, присланный из дома, был прочитан на пятый раз, письмо домой написано и отправлено ещё два дня назад."
    "Можно было позвонить в казарму и по телефону потрепаться с дежурным по роте, но с сегодняшним дежурным у рядового были натянутые отношения."
    "Да и о чём говорить? О нечистой силе? О том, что наряд с недавних пор боится ночью заступать на пост к воротам? Смех. Кому-то что-то пригрезилось, а слухи пошли как пожар."
    "И каждый из рассказчиков клянётся, что «сам видел». Сам видел горящие глаза, клыки, когти, женскую фигуру — без одежды, но обросшую шерстью. Бывает. Ах да, ещё и жуткий вой «сам слышал»."
    "А спать хотелось всё сильнее. Рядовой уже скурил ночной запас сигарет и обежал несколько кругов вокруг будки, чтобы не заснуть."
    "Ненадолго расшевелил дневального проверяющий, обходящий посты охраны. Поделился сигаретой, вставил пистон за затоптанный пол в будке и незаполненный журнал смены дежурств и отбыл по центральной аллее в сторону площади."
    "Дневальный проверил ещё раз замок на воротах. Прикинул, что раз дежурный офицер уже приходил проверять, то раньше пяти утра его не будет, выключил свет и лёг спать прямо на столе, повесив ремень со штык-ножом на спинку стула."
    "Но уже каких-то сорок минут спустя он проснулся от ощущения постороннего взгляда."
    $ set_mode_adv ()
    stop music fadeout 1
    show blink
    $ renpy.pause (2)
    play sound dct_sfx_fright
    "Ведомый звериным инстинктом, рядовой скатился со стола и первое, что проверил — заперта ли дверь в будку. После этого опоясался штык-ножом и, осторожно приподнявшись над столом, выглянул в окно."
    stop ambience
    
    scene dct_cat_house_part2 with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_fobos_daemos
    "Прямо на него через стекло смотрело Оно: горящие жёлтым светом глаза, хищные клыки, видимые в распахнутой пасти, звериные уши, торчащие над копной спутанных волос, лицо — смесь звериного и человеческого, тело, покрытое росшей клочками шерстью."
    play sound dct_sfx_roar
    "Существо протянуло руку, выпустило когти, провело со скрежетом ими по стеклу и зарычало."
    stop ambience
    
    scene dct_ext_kpp2 with squares:
        zoom 2
        anchor (900, 700)
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    "Так рядового и нашли утром — лежащего в позе эмбриона на полу запертой изнутри будки (пришлось вынимать стекло), поседевшего и повторявшего всё время: «Докладывает дневальный по КПП: на посёлок напал оборотень»."
    show d_to normal casual at right with moveinright
    d_to "Всё, что нужно, рассмотрела?"
    show cs normal glasses at left with moveinleft
    cs "Больше, чем нужно."
    d_to "Вот именно. Ну, пойдём? Нам всем ещё имитировать бурную деятельность и отписки писать."
    hide d_to with moveoutleft
    hide cs with moveoutleft
    stop ambience
    
    scene dct_ext_switchman_house_day with squares
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["my_daily_life"]
    show d_ss normal shirt with moveinright:
        xpos 0.4
    d_ss "Родственник, в посёлке пока не показывайся."
    me "А что такое?"
    d_ss "Охота на ведьм там развернулась. Все ловят «оборотня». Не хочу, чтобы ты под горячую руку попал. Ну и я вместе с тобой."
    me "Поймали?"
    d_ss "Нет, но двоих в двадцать четыре часа на материк выслали."
    me "А оборотень?"
    d_ss "А оборотень — это уже забота Толяныча."
    stop music fadeout 1
    stop ambience
    
    scene dct_cof with squares:
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound_loop dct_sfx_teaspoon
    cs "Толя, что-то надо делать с этим «оборотнем»."
    d_to "Надо. Сегодня дневальный чуть со страху не умер, завтра клумбу во время погони потопчут. Послезавтра дети начнут в оборотня играть."
    cs "Толя, шутить — это моя обязанность. А я сейчас серьёзная."
    stop sound_loop
    stop ambience
    
    scene dct_int_cabinet_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["sweet_darkness"]
    show d_to normal casual at right
    show cs normal at left
    with dspr
    show d_to normal casual at cright with move
    d_to "Согласно инструкции, все домашние животные, попавшие в вакуоль и вышедшие из-под контроля, должны быть или возвращены на материк для изучения, или, в исключительных случаях, уничтожены."
    d_to "Я-то смогу её выследить и поймать, а вот ты вернёшь её такую на материк? Чтобы появился ещё один экспонат, ещё одно чучело в спецхранилище?"
    cs "И что? Ты предлагаешь ничего не делать?"
    d_to "Почему? Вилка, ты представляешь, что будет, если она впишется в Систему? Инстинкты зверя и интеллект человека. Хищного зверя, между прочим."
    d_to "К бойцу тому она поласкаться и поиграть приходила, я уверен. А в следующий раз? А появится она в посёлке вечером, после киносеанса? Будут гнать толпой через весь посёлок, загонят в угол и убьют?"
    d_to "Если Система её размножит, как пионеров? Я уже молчу о том, что будет, если она проникнет на нижний уровень системы. Сегодня же и начну. Тебе что-нибудь от неё надо?"
    show cs shy glasses with dspr
    cs "Тушку? Ты про спецхранилище сам всё сказал — обойдутся. Только постарайся, чтобы она не мучилась."
    d_to "Вот и начинается самая неприятная часть моей работы. Спасибо вам за это, люди!"
    hide d_to with moveoutright
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_gate_entrance_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    #"Час спустя Анатолий, переодевшись в старую форму-афганку, с бывалым походным рюкзаком за плечами, вышел из западных ворот посёлка."
    show d_to normal milit with dspr:
        xpos -0.2
    d_to "Будут спрашивать — вернусь после ужина."
    voice "Понятно, това{w=1}… Анатолий Васильевич."
    $ renpy.pause (1)
    hide d_to with dspr
    $ renpy.pause (1)
    stop ambience
    
    scene ext_path2_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    $ renpy.pause (1)
    #"Свернув с шоссе на ближайшую тропинку, Анатолий достал из рюкзака разделённое на две части ружье, собрал его, и уже вооруженный зашагал по тропе, внимательно вглядываясь себе то под ноги, то вдоль тропы и оглядываясь каждые пятнадцать — двадцать шагов."
    show to_hunter with dspr
    $ renpy.pause (2)
    stop ambience

    
##########
#Фелиноид#
##########
   
label dct_felinoid:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nФелиноид."
    $ day_time()
    show headline_text2 u"Фелиноид" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene ext_path2_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["you_won_t_let_me_down"]
    show to_hunter with dspr
    "Анатолий шёл в сторону старого лагеря. Механически разбирался в следах, оставленных людьми и животными на лесной тропинке, и ворчал про себя."
    d_to "{i}До каждого под роспись доводится, и ещё раз в шесть месяцев каждого здесь инструктируют.{/i}"
    d_to "{i} Но нет, стабильно, как по расписанию, раз в два года кто-то контрабандой провозит сюда кошку или собаку.{/i}"
    d_to "{i}«Ах, мы её так любим, так любим, ах, она без нас от тоски пропадает!». Точно, без вас — от тоски. А с вами её Толяныч в конце концов убьёт.{/i}"
    hide to_hunter
    show d_to normal milit:
        xpos 0.7
    with dspr
    d_to "{i}Можно подумать, что Толянычу это нравится. Любите домашних животных? Везите сюда черепаху. Ничего не случится, проверено. Или рыбок. Да хоть канарейку. Нарушения, но глаза можно закрыть и сделать вид, что ничего не знаешь.{/i}"
    hide d_to
    show to_hunter
    with dspr
    $ renpy.pause (2)
    hide to_hunter with dspr
    $ renpy.pause (2)
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_old_building_day with dissolve:
        subpixel True
        zoom 1
        ease 3.0 zoom 2 anchor (700, 900)
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    d_to "{i}Стоп!{/i}"
    show d_to normal milit at fright with dspr
    $ renpy.pause (1)
    hide d_to with moveoutright
    
    scene dct_ext_old_building_day with dissolve:
        zoom 2 anchor (700, 900)
    $ day_time()
    $ persistent.sprite_time = "day"
    #show d_to normal milit at center with dspr
    d_to "{i}Кажется, я не зря пришёл.{/i}"
    stop ambience
        
    scene dct_cat_house_part3_footprint with slideup
    $ day_time()
    $ persistent.sprite_time = "day"
    play music something_beautiful
    "На дощатом помосте, оставшемся то ли от веранды, то ли от небольшой эстрады, темнел след босой ноги."
    "Кто-то и где-то наступил на бегу в лужу, не останавливаясь, переместился в пространство узла номер один, оттолкнулся правой ногой от помоста и опять исчез из пространства узла." 
    "Анатолий остановился, разглядывая постепенно высыхающий отпечаток. Достал из рюкзака линейку и фотоаппарат."
    d_to "Вот значит как, киса… Ты уже научилась скакать между узлами. Прости меня, но наши миры опасны друг для друга, и ты — как раз одна из опасностей."
    play sound sfx_ghost_children_laugh
    
    scene dct_ext_old_building_day with dissolve:
        zoom 2 anchor (700, 900)
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Что-то мелькнуло слева. Анатолий сделал шаг в сторону, слившись с кустами. Потом медленно потянул с плеча ружьё, на ходу переключая селектор на нарезной ствол."
    stop ambience
    
    scene dct_landscape_forest1
    show uv_wild_in_forest_small
    with slideright
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    $ renpy.pause (2)
    stop ambience
    
    scene dct_landscape_forest1 with fade:
        zoom 3
        anchor (1400, 1700)
    show uv_wild_in_forest_medium:
        pos (600, 250)
    show posp:
        subpixel True
        ypos 0.0
        ease 2 ypos -80
        ease 2 ypos -40
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Охотник прицелился, чуть подавшись туловищем назад, выдохнул, задержал дыхание и плавно потянул спусковой крючок. Довёл его до середины и {w=2} опустил оружие."
    hide uv_wild_in_forest_medium with pixellate
    "Потому что дичь вдруг замерцала и растворилась в воздухе."
    $ renpy.pause (2)
    stop music fadeout 1
    stop ambience
        
    scene dct_landscape_forest1 with fade
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    d_to "По горячему следу взять тебя не получилось, придётся вести осаду по науке."
    d_to "Не ты первая, киса, не ты последняя."
    stop ambience

    scene dct_int_briefing_room with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["trapped_in_dreams"]
    play sound dct_sfx_solo_card
    show footprint_photo at center with moveinbottom:
        rotate (-4)
    d_to "Лет ей приблизительно шестнадцать, и человеческий облик она уже почти обрела. Осталось трансформировать кисти и завершить линьку."
    d_to "Хвост и кошачьи уши, скорее всего, останутся." 
    d_to "Теперь о грустном: она уже научилась перемещаться между узлами. Так что времени у нас — шесть месяцев без запаса. Я думал, с запасом, а оказалось — без."
    play sound dct_sfx_solo_card
    hide footprint_photo with moveoutbottom
    show d_bg normal suit at right with dspr:
        yalign 0.2
    d_gd "Справитесь, Анатолий?"
    d_to "Справлюсь, но с помощниками мне будет легче. Мне нужен человек, который разгрузит меня от бумажной работы здесь, и ещё один человек, который поможет мне в лесу."
    d_to "Оба из местных, чтобы не плодить формальности с допуском к секретным документам."
    show d_bg smile suit with dspr
    d_gd "Человек из местных…"
    show d_bg normal suit with dspr
    d_gd " Способностей к активации у вас, кажется, нет… Хорошо, берите двоих из первого узла, на ваш выбор."
    d_to "Тогда, пожалуй, Евгения-библиотекарь — здесь. И Елена-рисовальщик — там."
    d_gd "Микс здесь и копия там. Правильно, чтобы не было лишних вопросов. А если появятся вопросы, то микс здесь для контроля параметров. Утверждаю."
    stop music fadeout 1
    stop ambience
    
    scene dct_cof with squares:
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound_loop dct_sfx_teaspoon
    d_to "Думал ли я двадцать лет назад, что закончу свою карьеру охотником на кошек?"
    cs "Толя, хватит ворчать, это не кошка."
    d_to "Пока ещё это кошка. В почти человеческом облике, со сверхъестественными способностями, но кошка."
    stop sound_loop
    stop ambience
    
    scene int_aidpost_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_day
    play music music_list["memories"]
    show cs normal at left
    show d_to normal casual at cright
    with dspr
    d_to "А в прошлый раз на её месте была собака. А всё началось с овчарки Глафиры. И скажи, на них точно выключатель не действует?"
    show d_to normal casual at right with move
    show cs normal at cleft with move
    show cs shy with dspr
    cs "Не действует, Толя. Выключатель — он на пионеров рассчитан."
    cs "Я знаю, почему домашние животные здесь становятся похожими на людей. На нашем маленьком острове доктора Моро."
    cs "Мы оба знаем, зачем они возвращаются к своим хозяевам."
    cs "Но почему они не превращаются в людей — в таких, как мы, или в таких, как пионеры, хотя мозг у них вполне человеческий — я не знаю."
    show blink
    $ renpy.pause (1)
    stop music fadeout 1
    stop ambience
    
    scene dct_int_cabinet_day with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_to normal casual at center with dspr
    d_to "Вот, Женя, это твоё рабочее место. Приказы, картотека, личные дела сотрудников, график отпусков. И так далее, и тому подобное. Разберёшься?"
    hide d_to with moveoutright
    show mz normal pioneer with dspr
    mz "А чего тут разбираться, дядя Толя? Конечно, разберусь."
    show mz bukal glasses pioneer with dspr
    mz "Вот только… Дядя Толя?"
    show d_to normal casual at fright with moveinright
    d_to "Да, Женя?"
    mz "Другие стажёры. Мику и этот, Сыроежкин. Я буду жить с ними в одной секции?"
    d_to "Что-то не так?"
    show mz normal glasses pioneer with dspr
    mz "Нет. Ничего. Всё нормально."
    d_to "Тогда приступай к работе. Будут меня искать — я на территории."
    hide d_to with moveoutright
    stop ambience

    scene ext_polyana_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["mystery_girl_v2"]
    "Где-то на материке зима перевалила через середину. Скоро февраль, скоро воздух запахнет весной, как всегда, обещая перемены к лучшему и, как всегда, обманывая."
    "А в мире бесконечного лета жизнь бывшей кошки стабилизировалась."
    "Бывшая кошка перестала расти и менять облик и сейчас больше всего походила на девушку лет шестнадцати, какой она, собственно, и была по кошачьим меркам."
    stop ambience
    
    scene dct_uv_behind_tree with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Из кошачьего у ней остались только длинный хвост и скрывающиеся под нечёсаной копной каштановых волос треугольные подвижные уши. Всё как и описал Анатолий. Единственное, что он не разглядел — это вертикальные зрачки в жёлтых глазах."
    "И её интеллект — интеллект пока спал. Интеллектом она пока оставалась ненамного выше той кошечки-подростка, какой была ещё полгода назад."
    "Утром и вечером охотясь на мышей, дни и ночи она проводила, подрёмывая или в старом корпусе, или на одной из своих лёжек в лесу, окружающем посёлок."
    stop music fadeout 5
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_wild with dspr
    "Часто же она скрывалась в центре какого-нибудь пионерского лагеря, прячась в кустах и наблюдая оттуда за жизнью пионеров."
    stop ambience
    
    scene ext_dining_hall_near_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_wild with dspr
    "Лагеря решали и проблему с добыванием пищи, потому что мышами прокормить девушку, пусть даже миниатюрную, было сложно, и ловля мышей давно уже превратилась просто в игру."
    stop ambience
    
    scene ext_polyana_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "А если что-то чужое и поселилось в ней, то пока оно никак себя не проявляло. Беспокойство шло скорее снаружи."
    "Кошке-девушке казалось, что что-то всё сильнее и сильнее ограничивает её свободу, и это что-то рисовалось в её голове в образе невысокого человека с цепким и жёстким взглядом."
    stop ambience
    
    scene ext_path2_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    show to_hunter
    show uv_spy_wild
    with dspr
    "Несколько раз она встречала этого человека в лесу, несколько раз скрадывала, наблюдая из кустов, как он приседает над тропой, что-то на ней высматривая."
    stop ambience

    scene dct_ext_residential_block_day with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["i_want_to_play"]
    show uv_spy_wild
    d_to "Ульяна, можно вас на минутку?"
    show d_us normal dress at center behind uv_spy_wild with moveinright:
        ypos -0.05
    us "Я слушаю вас, Анатолий{w=0.5} Васильевич."
    show d_us normal dress at right with move:
        ypos -0.05
    show d_to normal casual at cleft behind uv_spy_wild with dspr
    d_to "Вы сейчас в будку{w=1}… то есть на удалённый пост?"
    us "Да. У меня…"
    d_to "Неважно. Ульяна, у меня к вам просьба. Если вы увидите в лесу что-то необычное или встретите кого-то необычного. Что-то, выбивающееся из картины мира. То не пытайтесь с этим разобраться сами, а обратитесь к руководству. К руководству Филиала, я имею в виду, а не к Персунову-старшему."
    d_to "К Глафире Денисовне, к Виоле. В крайнем случае, обратитесь ко мне. Вы меня поняли?"
    show d_us hurt dress with dspr
    us "Д-да, Анатолий Васильевич."
    d_to "Благодарю вас. И вашему Семёну передайте эту же мою просьбу."
    hide d_us with moveoutright
    stop music fadeout 1
    stop ambience

    scene dct_int_briefing_room with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show cs normal at left with dspr
    cs "Глафира Денисовна, я в старом корпусе до обеда."
    show d_bg normal suit at cright with moveinright:
        yalign 0.2
    d_gd "Это на вашей «даче»? Приручаете?"
    show d_bg smile suit with dspr
    cs "Приручаю? Да, наверное, Глафира Денисовна."
    show d_bg normal suit with dspr
    d_gd "Будь осторожна, Виолетта. Однажды она спросит тебя человеческим голосом: «Ты пойдёшь со мной?». А ты не сможешь ответить «нет»."
    cs "Глафира Денисовна, зачем вы мне страшилку, которой солдатики друг друга пугают, рассказываете?"
    show d_bg sad suit with dspr
    d_gd "Да, в общем, низачем. Будь осторожнее. Я попрошу армейцев восстановить туда телефонную линию. Вдруг поможет."
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    show uv_spy_wild
    play ambience ambience_old_camp_outside
    play music music_list["gentle_predator"]
    show cs normal at fright behind uv_spy_wild with dspr
    cs "Телефонную линию, говорите."
    cs "Никто сюда телефонную линию не потащит. Потому что боятся оборотня как огня."
    show cs normal at cright with move
    cs "Солдатики вон страшилку друг другу рассказывают. Что придёт к кому-то из них оборотень и позовёт с собой."
    cs "Ты слушай, киса, слушай. Я знаю, что ты где-то здесь и меня слышишь. Мне сейчас важно тебя к голосу приучить. Поэтому я буду болтать."
    show cs normal at center with move
    cs "Так вот, солдатики страшилками друг друга пугают. А все эти учёные — они над солдатиками смеются. А сами тоже верят и тоже тебя боятся, киса. Только не сознаются никому."
    cs "И в лес гулять не ходят. Даже за грибами. Сидят дома, за стенами и экранами. Наивные мышки."
    show cs normal at cleft with move
    show cs shy
    cs "Наивные мышки. Что они скажут, киса, когда ты шагнёшь прямо к ним в спальню и позовёшь с собой?"
    stop music fadeout 1
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    show cs normal at fright with dspr
    cs "Я вот тоже боюсь. Однажды ты спросишь меня человеческим голосом: «Ты пойдешь со мной?». А я не смогу ответить «нет»."
    cs "Бабуля права."
    cs "И если верить солдатской страшилке, буду жить как робот в пионерском лагере. Вот интересно, откуда солдатики про роботов узнали?"
    show cs normal at center with dspr
    show cs shy with dspr
    cs "Но я хотя бы оставлю записи. Ты слушай, киса, слушай. Привыкай к моему голосу. Неважно, что ты пока ничего не понимаешь."
    stop ambience
    
    scene dct_ext_lake_day with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Охотник допил чай и занялся своими записями."
    stop ambience
    
    scene dct_cat_house_part3_lenin_v_razlive with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["went_fishing_caught_a_girl"]
    "Лист блокнота был расчерчен на таблицу, в ячейки которой в виде условных значков охотник сейчас заносил обнаруженные факты."
    "И уже скоро в расположении значков стал виден определённый, ритмически повторяющийся узор."
    d_to "{i}Это удивительно предсказуемая бывшая кошка.{/i}"
    d_to "{i}Осталось посетить ещё пару узлов, и будет готово её поминутное расписание.{/i}"
    d_to "{i}И мне останется просто оказаться в нужном месте в нужное время. {/i}"
    show uv_spy_wild with dspr
    d_to "Кто сказал, что трудно ловить чёрную кошку в тёмной комнате? Это только вопрос системного подхода и правильной методики. Хоть ты и прыгаешь по узлам Сети, как кошка по мебели."
    stop music fadeout 2
    stop ambience
    
    scene ext_path2_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    show to_hunter with dspr
    play ambience ambience_forest_day
    "Очень довольный собой охотник собрал рюкзак, затушил маленький костёр и отправился в сторону лагеря."
    "Нужно было перед отъездом в посёлок подарить здешней Лене альбом для рисования и коробку с красками, просто в благодарность за помощь."
    d_to "{i}Начальство поворчит — мол, поставлен охранять от вмешательства, а сам нарушает, но плевать. Выговором больше, выговором меньше.{/i}"
    d_to "{i}Главное — опередить эту кису, пока она остаётся просто кисой. Или даже получеловеком.{/i}"
    stop ambience
    
    scene dct_ext_lake_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list ["mystery_girl_v2"]
    "Когда Анатолий ушёл, кусты раздвинулись, и на поляну вышла кошка-девушка. Обошла по кругу место, где сидел Анатолий, то нагибаясь, чтобы рассмотреть следы получше, то отходя на несколько шагов."
    #ЦГ Дикая Юлька делает записи в лесу.
    "Присела на бревно, принимая при этом разные позы, подражая Анатолию."
    "Потом сбегала к росшему на краю поляны лопуху, оторвала от него самый большой лист, подобрала с земли обгорелую щепку и, опять усевшись на бревно, стала имитировать процесс письма, периодически зажимая второй конец щепки в зубах и издавая различные звуки, которые всё чаще и чаще складывались в двух-трёхсложные сочетания."
    stop ambience
    
    scene dct_ext_lake_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "А когда ей это наскучило, кошка-девушка со смехом отбросила лист и побежала к озеру. Не останавливаясь, прыгнула в воду, чтобы вынырнуть уже на середине водного зеркала, и по-собачьи погребла к противоположному берегу."
    "На противоположном берегу она встряхнулась по-кошачьи и, опять засмеявшись от беспричинной радости, откинулась назад, в открывшийся портал, чтобы упасть на траву уже совсем в другом месте, далеко отсюда. Смеялась она уже совсем по-человечески."
    show dct_uv_wilde_laugh with fade
    $ renpy.pause (3)
    stop music fadeout 1
    stop ambience

######
#Нэко#
######
   
label dct_catgirl:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nНэко."
    $ day_time()
    show headline_text2 u"Нэко" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    

    scene dct_uv_behind_tree with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["a_promise_from_distant_days"]
    "Жизнь состояла из циклов, циклы — из дней, а дни — из часов и минут. Кошка-девушка не замечала их течения, никак не выделяя себя из окружающего мира."
    stop ambience
    
    scene ext_polyana_night with dissolve
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    "А жизнь её была чем-то средним между жизнью пионеров, населяющих лагеря, и жизнью учёных, техников и военных, обитающих в посёлке."
    "Как и пионеры, кошка-девушка не старела, зафиксировавшись в человеческом аналоге своего кошачьего возраста. Как и пришельцы извне, она сохраняла свою память, не обращая внимания на смену циклов."
    stop ambience
    
    scene ext_polyana_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Тумана, попасть в который так боялись люди, она просто не замечала. Еды ей хватало, скучно ей не было, и она была по-своему счастлива."
    stop ambience
    
    scene dct_ext_houses_night with dissolve
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    "Всё так же держась поблизости от посёлка, бывшая кошка открыла для себя незаселённые узлы. Где можно было пройтись по абсолютно пустому лагерю, в котором никогда не звучали детские голоса."
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    "Человек — неважно, был ли то пионер из лагеря, или обитатель посёлка, или бывшая кошка — чувствовал в них себя очень неуютно."
    "Бывшая кошка чаще всего просто легко пробегала по главной аллее такого лагеря и скрывалась в тоннеле между узлами."
    stop ambience
    
    scene ext_house_of_mt_night_without_light with dissolve
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    "Ей казалось неправильным, что никто не живёт в этих домиках, никто не ходит по аллеям, никто не принимает пищу в столовой и не играет на спортивной площадке."
    stop music fadeout 3
    stop ambience
    
    scene dct_cat_house_part2 with dissolve
    show dct_dream_veil:
        shiver
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    "Дважды она уже пыталась позвать с собой людей: «Приходите, живите, радуйтесь! Там столько места!». Но оба раза люди её не поняли."
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_wild with dspr
    "И всё же бывшую кошку всё больше и больше тянуло к людям. Даже вечерняя погоня за ней, когда она едва спаслась от обитателей посёлка, не отвратила её."
    "Прятаться она умела, а голая человеческая кожа маскирует не хуже камуфляжа."
    "Поэтому наблюдение за жизнью обитателей какого-нибудь из лагерей или самого посёлка стало основным её занятием."
    stop ambience
    
    scene dct_ext_old_building_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_old_camp_outside
    "А вечерами, забираясь после охоты в старый корпус в одном из узлов, или в подземелье, или оставаясь на одной из своих лёжек, кошка-девушка разыгрывала целые представления, по-своему проживая заново увиденное."
    "Полученный ею человеческий мозг был слишком велик для кошачьего разума, и его требовалось чем-то заполнить."
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    play music music_list["raindrops"]
    "Она любила наблюдать за всеми людьми, но больше всего привлекали её двое: женщина, которая с некоторых пор стала проводить время в её главном логове, и мужчина, на которого она то и дело натыкалась в лесу."
    stop ambience
    
    scene ext_path2_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    show to_hunter
    show uv_spy_wild
    with dspr
    "За мужчиной было интересно следить — как он ходит по лесу, по её любимым тропинкам, то наклоняясь к самой земле, то, наоборот, оглядываясь и всматриваясь в близкий лесной горизонт."
    stop ambience
    
    scene dct_cat_house_part3_lenin_v_razlive with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    show uv_spy_wild
    "Несколько раз она была свидетельницей того, как раздавался гром и неосторожный рябчик падал с дерева под ноги мужчине. Мужчина обдирал с рябчика кожу вместе с перьями, потрошил, отварив мясо в котелке, съедал и уходил, оставив на месте своего обеда только затоптанный маленький костёр и кучку птичьих потрохов."
    stop ambience
    
    scene dct_bonfire with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_bonfire
    "Потрохами она брезговала, оставляя их воронам, а к костру подходила."
    "Иногда ей удавалось раздуть тлеющие угли, и тогда она долго сидела, задумчиво глядя на языки пламени, пока не догорали последние сучья."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Если за мужчиной было интересно наблюдать, то женщину было интересно слушать. Кошка-девушка обычно устраивалась на краю крыши над открытым окном или, в те редкие дни, когда портилась погода, в соседней комнате и слушала бесконечный монолог."
    "Иногда кошке-девушке казалось, что обращаются прямо к ней, иногда — что она понимает, о чём идёт речь. Но как после наблюдения за мужчиной хотелось в пантомиме повторить его действия, так и тут каждый вечер она повторяла за женщиной как попугай, не понимая смысла произносимых слов."
    "Перед кошкой-девушкой стояла сложная задача: не понимая смысла слов, выделить те, которыми люди зовут друг друга. Чтобы самой потом позвать: «Ты пойдёшь со мной?»."
    "А сделать это можно было, только наблюдая за людьми."
    stop ambience
    
    scene ext_house_of_un_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    show un normal pioneer far
    show uv_spy_wild
    $ renpy.pause (1)
    hide un with moveoutleft
    play ambience ambience_camp_center_day
    "И она опять и опять возвращалась в лагеря и в посёлок — наблюдать за их обитателями."
    stop ambience

    scene dct_int_briefing_room with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["into_the_unknown"]
    show d_bg normal suit at right with moveinright:
        yalign 0.2
    show d_bg normal suit at right with move:
        ypos 0.1
    d_gd "Как ваши успехи, Анатолий? Что-нибудь конкретное скажете?"
    show d_to normal casual at cleft with moveinleft
    show d_to normal casual at cleft with move:
        ypos 0.20
    d_to "Скажу. На восьмой день следующего цикла, Глафира Денисовна. Это основная дата. И две контрольных: через день и через пять дней от основной."
    d_to "В семнадцать ноль-ноль, в четырнадцать тридцать и в двадцать один ноль-семь."
    d_gd "Всё распланировали."
    d_gd "А это не будет слишком поздно?"
    d_to "У нас ещё один цикл в запасе остаётся, Глафира Денисовна. Время есть."
    d_gd "Хорошо, действуйте по вашему плану."
    show blink
    stop music fadeout 1
    stop ambience fadeout 1
    $ renpy.pause (2)
    "Анатолию очень не хотелось убивать, и он неосознанно тянул время."
    
    scene dct_int_cabinet_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_to normal casual at right with moveinright
    d_to "А ты даже на польты не годишься."
    show mz normal glasses pioneer at cleft with moveinleft
    mz "Вы что-то сказали, дядя Толя?"
    d_to "Не обращай внимания, Женя. Это я о своём."
    show mz angry glasses pioneer with dspr
    mz "Ох и запустили вы дела, дядя Толя."
    show mz normal glasses pioneer with dspr
    d_to "Запустил, Женечка. Но ты же не собираешься в лагерь уезжать? А то на тебя вся надежда."
    show mz rage glasses pioneer with dspr
    mz "Что я там забыла? Детей этих бестолковых? Или «общественные мероприятия»? А тут у вас четыре часа до обеда отработала и свободна."
    show mz normal glasses pioneer with dspr
    d_to "Тогда командуй тут. Я в лес до обеда, держи оборону без меня! Пленных не брать, а если брать, то не кормить!"
    show mz smile glasses pioneer with dspr
    mz "Ни пуха ни пера, дядя Толя."
    stop ambience
    
    scene dct_int_chief_corridor_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["waltz_of_doubts"]
    show d_to smile casual at right with dspr
    d_to "«Свободна» — знаем мы эту её свободу."
    hide d_to with moveoutleft
    "«Свобода» в понимании Жени означала взять книжку в библиотеке и завалиться на кровать у себя в комнате."
    "А поздно вечером, когда все уже улягутся спать, отправиться на пляж, прихватив с собой «дядю Толю» для охраны девичьей чести."
    "Там окунуться, проплыть по-собачьи десяток метров и убежать к себе."
    stop ambience
    
    scene dct_ext_module_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_to normal casual at fleft with dspr
    th "Привязался я к ней. Может, оставить её здесь постоянно? Надо будет потрясти Персунова-оригинала — как он умудряется сохранять своего дубликата в нашей вакуоли? А то надоело каждый цикл в лагерь мотаться."
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_wild
    show d_to normal milit at fleft behind uv_spy_wild with moveinleft
    show cs normal behind uv_spy_wild with moveinright
    cs "Здравствуй, Толя. Гостей высматриваешь?"
    show d_to smile milit with dspr
    d_to "Гостью, Виола."
    show cs smile with dspr
    cs "Понимаю. Отпусти её побыстрее. Не перегружай{w=0.5}… навязчивым гостеприимством."
    cs "А я пойду, у себя гостью подожду. У тебя своя программа встречи гостей, у меня — своя."
    hide cs with moveoutright
    d_to "А зачем мне гостей ждать? Вон она, в кустах сидит. Строго по графику."
    d_to "Всё-таки, гостья, ты уже не наша. Ни человек, ни животное не способны выдерживать расписание с такой точностью."
    d_to "Ты уже один из органов Системы, будь она неладна. Будь вы обе неладны."
    stop ambience

    scene dct_int_old_building_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    "В старом корпусе Виола стояла вполоборота ко входу и делала вид, что внимательно разглядывает кончик карандаша. Фантазия у неё уже давно истощилась, и потому она несла полную околесицу."
    show cs normal with dspr:
        xpos 0.9
    cs "Карандаш мягкий, хорошо заточенный, но затупить его совсем недолго." 
    cs "Им можно рисовать, им можно чертить, им можно…"
    "Виола тихо приговаривала, не слушая себя, а сама краем глаза следила за старым зеркалом, принесённым в здание и прислонённым к стене так, чтобы в зеркале отражался вход. А там уже час как чувствовалось чьё-то присутствие."
    cs "Только не испугнись…"
    "Виола говорила всё тише, надеясь, что любопытство пересилит осторожность."
    "Наконец кто-то невидимый за дверью сдался, и в проём просунулась лохматая голова."
    "Виола замерла, замолчала и медленно повернулась лицом к двери, стараясь не спугнуть пришельца и улыбаясь одними глазами. Смотреть она старалась чуть в сторону, а руки спрятала."
    stop ambience
    
    scene dct_int_old_building_day
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    play music music_list["mystery_girl_v2"]
    show uv_wild_in_forest_medium with dissolve:
        zoom 0.4 pos (310, 554) matrixcolor TintMatrix("#8BA9B0")*BrightnessMatrix(value=-0.1)
    "Голова исчезла через десять секунд."
    "А ещё через десять секунд в проём шагнула хозяйка."
    
    scene dct_cs_and_uv_meeting_1 with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    "Виола замерла, не шевелясь, а пришелицу уже стало возможно разглядеть во всей красе."
    cs "Ну заходи… кошочка. И имей в виду: звать меня с собой не нужно. Меня не зовут, я сама прихожу…"
    stop music fadeout 1
    stop ambience
    
    scene dct_cs_and_uv_meeting_2 with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    "Виола говорила и говорила, а кошачий хвост поднимался всё выше и выше. И что-то сломалось в бывшей кошке: она сделала в комнату первый шаг, второй, третий и уткнулась головой в грудь Виолы, как утыкалась когда-то в колени хозяйки."
    cs "…вот и все вы такие, хоть и гуляете сами по себе. Если хочешь, можешь ходить и так. А если хочешь перестать быть кошкой, для начала тебе нужно вымыться, причесаться, одеться и научиться разговаривать."
    uv_cgl "Я-н-а-а-а-ю…"
    cs "Конечно, знаешь. А ещё я не люблю животных, так что другого выхода, кроме как перестать быть кошкой, у тебя нет."
    cs "И сними, наконец, ошейник."
    stop ambience

    scene dct_ext_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Бывшая кошка ничего не знала об оставленных ей двух неделях жизни, но спешила жить, используя все свои маленькие возможности."
    "«Надо научиться говорить? Я научусь говорить за три дня»."
    "И на третий день она поздоровалась с приходящей к ней женщиной."
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    uv_cgl "Р… Дра-авсуй."
    show cs smile with dspr
    cs "Здравствуй и ты, неведома зверушка."
    stop ambience
    
    scene dct_int_old_building_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    play music music_list["dance_of_fireflies"]
    show cs normal
    cs "Ну, рассказывай, где ты была?"
    uv_cgl "Ты была-аа в лесу."
    cs "Нет, я была в посёлке, а вот где ты была?"
    uv_cgl "Я-аа была-аа в посёлке, а ты была-аа в лесу."
    cs "Так, стоп."
    "Виола подводит девушку к зеркалу: та уже знает зеркало и не пугается."
    stop ambience
    
    scene dct_cs_and_uv_mirror_finger
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Палец направлен на отражение Виолы…"
    cs "Это — я."
    "Палец показывает на отражение девушки."
    cs "А это — ты. Повтори."
    "Девушка показывает пальцем на Виолу."
    uv_cgl "Это — я."
    "Виола перехватывает руку девушки. Та испуганно вздрагивает, но расслабляется, доверившись."
    cs "Повторяй за мной. Это — я."
    cs "Это — ты."
    cs "Теперь сама повторяй."
    uv_cgl "Это — я. Это — ты."
    cs "Молодец, а теперь вместе."
    "С третьей попытки у них получается, и два голоса звучат синхронно, и пальцы показывают совершенно правильно: «Это — я, а это — ты!»."
    "Девушка поняла и счастливо смеётся. «Как просто!». Виола же так ни разу и не улыбнулась."
    stop music fadeout 1
    stop ambience
    
    scene dct_cs_and_uv_mirror with dissolve:
        subpixel True
        zoom 1 anchor (400, 0)
        ease 5.0 zoom 0.5 anchor (0, 0)
    play ambience ambience_int_cabin_day    
    cs "Видишь, можешь же."
    cs "Кто бы ещё рассказал мне, что с тобой делать? А ещё — как ты живёшь с двумя наборами хромосом? Хотя последнее — это уже личное, можешь не отвечать."
    "Смысла вопроса девушка не понимает."
    uv_cgl "Я-а не зна-аю."
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Язык заставил девушку-кошку выучить местоимения, всего два: «я» и «ты», но и этого оказалось достаточно, чтобы отделить себя от окружающего мира."
    "Чтобы где-то на интуитивном уровне понять, что есть она и есть весь остальной мир."
    stop ambience

    scene dct_int_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    play music music_list["i_want_to_play"]
    "А как только бывшая кошка заговорила, так с тех пор и не умолкала, ей хотелось общения."
    show cs normal
    uv_cgl "При-иве-ет!"
    cs "На этот раз не привет, а до свидания."
    uv_cgl "До свидания-а-у."
    hide cs
    stop ambience
    
    scene ext_houses_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    "Но собеседник приходил только утром, и очень скоро бывшей кошке этого стало мало."
    "Помня свой неудачный опыт обращения к жителям посёлка, она попробовала поговорить с пионерами, но пионеры либо не замечали её, либо испуганно убегали."
    show uv_spy_wild with dspr
    $ renpy.pause (2)
    hide uv_spy_wild with dspr
    show el normal pioneer with moveinright
    uv_cgl "Приве-ет."
    show el scared pioneer with dspr
    $ renpy.pause (2)
    hide el with easeoutleft
    el "А-а-а!"
    stop music fadeout 1
    "Бывшая кошка задумалась, что же в ней не так, и решила, что ей нужно одеться. Платье она позаимствовала там же, в одном из лагерей, на складе. Даже размер совпал."
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    show cs smile
    cs "Вижу, ты решила меня послушаться{w=1}… кошочка. Давай только платье вывернем на правую сторону."
    uv_cgl "Выверняа-у-у-у."
    show cs normal with dspr
    cs "Правильно говорить ты почти научилась."
    cs "И на оборотня совсем не похожа."
    cs "Главное — не рви обои, а то впечатление испортишь."
    hide cs with moveoutright
    uv_cgl "Н-е-е рви-и."
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_neko
    $ renpy.pause (2)
    hide uv_spy_neko with dspr
    show dv normal pioneer with moveinright
    uv_cgl "Здра-авствуй." 
    show dv shocked pioneer with dspr
    $ renpy.pause (1)
    hide dv with easeoutleft
    play music music_list["trapped_in_dreams"]
    "Реакция пионеров добавила в её картину мира третью сторону: теперь в ней была она, была вселенная и были другие."
    "А ещё она задумалась: чем она отличается от этих других? С этим вопросом она и пришла к своему единственному собеседнику."
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    show cs normal glasses
    uv_cgl "Кто йаа-аа-ау-у?"
    cs "Невозможное явление природы. И теперь передо мной стоит вопрос: что будет дальше?"
    stop music fadeout 1
    stop ambience

    scene dct_to_hunter with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    play music music_list["mystery_girl_v2"]
    d_to "Бывшая кошка танцует на опушке леса. Как мило."
    show dct_dancing_uv with dspr:
        zoom 2
        anchor (700, 350)
    show posp
    d_to "Она вообще понимает, что это называется танец?"
    d_to "Танец кошки, превращающейся в человека."
    stop ambience
    
    scene dct_dancing_uv with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "В трёхстах метрах от кошки в тени дерева устроился Анатолий и смотрел в оптический прицел, как в тетральный бинокль."
    stop ambience
    
    scene dct_to_hunter with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    d_to "Кошки не носят платья и не танцуют. Если ты ещё и заговорила… В общем, спасибо, Виола. Теперь мне будет легче."
    
    scene dct_dancing_uv with dspr:
        zoom 2
        anchor (700, 350)
    show posp
    d_to "А красиво танцует."
    "Анатолий уже различил две параллельные линии: кошка на охоте и радующаяся жизни девушка."
    d_to "Завораживает. Хочется подойти поближе, усесться в траву и отбивать ритм ладонями."
    stop music fadeout 1
    stop ambience
    
    scene dct_to_hunter with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    d_to "Представление закончено, я так понимаю?"
    stop ambience
    
    scene dct_landscape_forest3 with dissolve:
        zoom 2
        anchor (700, 430)
    play ambience ambience_forest_day
    show posp
    show uv laugh close behind posp
    $ renpy.pause (2)
    hide uv with pixellate
    $ renpy.pause (1)
    stop ambience
    
    scene dct_to_hunter with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    d_to "Ладно, живи ещё, срок до послезавтра ты заслужила."
    $ renpy.pause (1)
    stop ambience
    
#########
#Богиня?#
#########
   
label dct_goddess:
    scene black with dissolve
    $ save_name = u"Дубликат. Кошкин дом -\nБогиня?"
    $ day_time()
    show headline_text2 u"Богиня?" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve    
    
    scene dct_ext_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    play music music_list["trapped_in_dreams"]
    "Прошел ещё один цикл — последний цикл, отведённый Анатолием девушке-кошке. А в остальном ничем не примечательный."
    "Наверху, «на материке», как говорили в посёлке, уже распалась Империя. Перемены докатились и до посёлка: кого-то из обитателей возвращали на материк, кого-то просто сокращали."
    stop ambience
    
    scene ext_old_building_night_moonlight with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_old_camp_outside
    "Сворачивались военные, закрывая свои, не известные гражданским, проекты и сокращая присутствие до неполной роты, охранявшей имущество, которое пока ещё не успели вывезти на материк."
    "Так что об «оборотне» большинство населения посёлка просто позабыло, тем более что пошёл устойчивый слух о полном закрытии Филиала."
    stop ambience
    
    scene dct_ext_module_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_neko
    narrator "Девушку-кошку это не интересовало — она жила своей жизнью, общаясь с Виолой, наблюдая за жизнью людей, воруя еду в столовых."
    stop ambience
    
    scene int_house_of_un_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    "Однажды, украв у одной из Лен пачку печенья, она оставила Лене на столе яблоко."
    show dct_apple_uv_un
    "Просто так."
    stop ambience
    
    scene ext_house_of_un_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_neko
    show un shocked pioneer far behind uv_spy_neko with dspr
    "Нет, совесть за кражу её не мучила, она не знала ни что значит «украсть», ни что такое «совесть». Бывшей кошке просто понравилась идея обмена."
    show un shy pioneer far with dspr
    "И идея подарков с её практическим воплощением."
    stop music fadeout 1
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show uv_spy_neko
    "То, что люди, кроме Виолы, либо от неё убегают, либо её не замечают, стало привычным, и к людям она больше не подходила, наблюдая за их жизнью издалека."
    stop ambience
    
    scene ext_polyana_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Изменилось мировосприятие. То, что раньше казалось ей прорехами в туманном флёре, постоянно висящем в воздухе, теперь воспринималось как тоннели в другой мир."
    show gate_ext_camp_entrance_day:
        alpha 0
        ease 3 alpha 0.8
    play sound ambience_camp_entrance_day fadein 3
    stop ambience fadeout 3
    $ renpy.pause (3)
    stop sound
    
    scene ext_camp_entrance_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    "Она шагала в них, на мгновение оказывалась в коридоре со стенами, сотканными из тумана, и следующим шагом уже выходила в нужном ей месте нужного ей узла Сети."
    show gate_ext_bus_stop:
        alpha 0
        ease 3 alpha 0.8
    play sound dct_ambience_street2 fadein 3
    stop ambience fadeout 3
    $ renpy.pause (3)
    "Стали видимы входы и в другие тоннели — похожие, но другие. Девушка-кошка, несколько раз сунувшись в них, в дальнейшем этого избегала."
    hide gate_ext_bus_stop with vpunch
    stop sound
    play ambience ambience_camp_entrance_day
    narrator "Всякая попытка шагнуть в новый тоннель приводила её или в место, заполненное людьми, большими домами и механизмами…"
    show gate_ext_pyramid:
        alpha 0
        ease 3 alpha 0.9
    play sound dct_ambience_wind fadein 3
    stop ambience fadeout 3
    $ renpy.pause (3)
    "…или на пустую, продуваемую ледяным ветром равнину, украшенную только грудой чёрных камней."
    hide gate_ext_pyramid with vpunch
    stop sound
    play ambience ambience_camp_entrance_day
    "И то, и другое пугало девушку, поэтому она сразу пряталась назад, в привычные ей миры, едва высунув голову и осмотревшись в новом месте."
    stop ambience

    scene int_aidpost_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_day
    play music music_list["just_think"]
    d_to "Виола, я оценил результат."
    show d_to normal casual at right with moveinright
    d_to "…вот только зачем ты это сделала?"
    show cs shy glasses at cleft with moveinleft
    cs "Мне показалось неправильным, что мы не даём им шанса. Просто уничтожаем их."
    d_to "Думаешь, ты первая? Сначала они хорошие, а потом в них просыпается… Нет, не зверь. Не знаю, что или кто."
    d_to "И они начинают таскать людей: сначала сюда, а потом на{w=1}… Неважно куда."
    show cs normal glasses with dspr
    cs "А мне стало её жалко."
    d_to "Жалко."
    d_to "Мне кошку жалко. Может быть, человека было бы жалко. А вот это существо — нет. Так что не проси меня ни о чём."
    d_to "И не пытайся её уговорить, спрятать или запереть — это бесполезно. В любом случае, она только думает, что гуляет сама по себе."
    d_to "А в нужное время она прибежит в нужное место и будет думать, что так и надо."
    d_to "Так что у тебя своя работа, а у меня{w=1}… И я буду делать её хорошо. До свидания."
    hide d_to with moveoutright
    play sound sfx_close_door_1
    show cs normal glasses at center with move
    cs "И ты будешь делать её хорошо."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_old_building_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    show cs normal glasses with dspr
    cs "Что же с тобой делать, «существо»? И кто ты есть? Толя знает, но он молчит, и он{w=1}… практик. А я разглядывала твои клетки в микроскоп и ничего не поняла."
    uv_cgl "Я не зна-а-а-ю."
    stop ambience
    
    #show Yulka_na_divane
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["you_lost_me"]
    cs "А что ты вообще знаешь? То, что ты в опасности, ты знаешь? То, что Анатолий вот-вот убьёт тебя, ты знаешь? То, что тебе лучше залечь где-нибудь в пятьдесят лохматом узле и не отсвечивать месяца два, ты знаешь?"
    cs "Ты знаешь, что я сама ещё не уверена, правильно ли я сделала, или прав Анатолий?"
    uv_cgl "А что такое «убьёт»?"
    show blink
    "Попытаться объяснить девушке, что такое смерть, заняло все оставшиеся до обеда три часа. Бесполезно."
    hide blink
    show unblink
    uv_cgl "Я есть, и вот меня — нет? Так не бывает. Я была всегда и буду всегда."
    cs "Ты трудная… Только обещай не показываться Анатолию на глаза."
    uv_cgl "Я попробую."
    stop ambience
    
    scene dct_int_old_building_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_old_house_wind
    show cs shy glasses with dspr
    cs "Она попробует, нечеловеческий разум. Чтоб его. Как была кошка, так кошкой и осталась."
    "Пора было возвращаться в посёлок и работать — вчера Глафира привезла приказ о ликвидации Филиала и передаче материальных ценностей и результатов научных разработок вновь создаваемой коммерческой структуре. И надо было решить, что отдать, что оставить, а что уничтожить, как будто этого и не было."
    cs "Как ты думаешь, имеет сейчас значение судьба отдельной бывшей кошки?"
    uv_cgl "Я не зна-а-ю."
    cs "И я не знаю."
    "Виола так и не приняла бывшую кошку как равную себе. Так и продолжала относиться в глубине души к ней как к лабораторному животному."
    cs "Сумеешь ты не попасться Толе — значит, сумеешь, значит, это уже проблема новых хозяев. Попадёшься — значит, так тому и быть, я пыталась до тебя достучаться."
    show cs smile glasses far with dspr
    cs "Пока{w=1}, кошочка. Береги себя."
    stop music fadeout 1
    stop ambience

    scene dct_int_briefing_room with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_bg normal suit at right
    d_gd "Анатолий, завтра не исчезайте никуда. Будет совещание."
    d_to "Но, Глафира Денисовна, у меня…"
    d_gd "Я знаю, что у вас. Это приказ с материка. Приедет представитель новых{w=1} собственников, будем согласовывать порядок передачи дел."
    stop ambience
    
    scene ext_polyana_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Так девушке-кошке неожиданные обстоятельства подарили ещё три дня."
    stop ambience
    
    scene ext_dining_hall_near_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["goodbye_home_shores"]
    "А три дня спустя девушка-кошка устроилась на крыше поселковой столовой. Скинув с себя платье, грелась на солнце и думала. Кажется, впервые в жизни."
    $ set_mode_nvl ()
    "Всё-таки Виоле удалось заставить её думать, заставить шагнуть от животного «сейчас» к человеческому «настоящему»."
    th "Вот я есть, а вот меня нет. Как это — нет? Как вот этой осы?"
    "Девушка ловко смахнула рукой надоевшее насекомое. Покрутила головой, нет ли у насекомого группы поддержки, и опять легла, закинув руки за голову и глядя в небо."
    th "Я помню, как я бегала на четырёх{w=1}… лапах и не умела разговаривать. Или умела? Не знаю, но люди меня не понимали."
    th "Я была меньше ростом и покрыта шерстью. Со мной жили двое: мужчина и женщина. А потом женщина посадила меня в мешок и унесла далеко. Я стала от неё далеко, как оса от меня."
    "Девушка опять подняла голову и посмотрела на трупик осы, откатившийся к самому краю крыши."
    th "Но я прибежала назад, а оса уже никуда не прилетит. Как и те мыши. Значит, если меня сильно ударить, то я уже ничего не буду понимать и чувствовать. Не буду двигаться вообще, от меня останется только тело."
    th "Об этом говорила та женщина? А тем мышам было больно? Я вот разрезала себе голень — было больно, а если ударить так, что «умру», то будет ещё больнее?"
    th "Надо будет поговорить об этом с той женщиной. И с тем мужчиной. Он, правда, хочет меня «убить», он сильнее меня, но я быстрее."
    $ set_mode_adv ()
    stop music fadeout 1
    stop ambience
    
    scene int_dining_hall_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    play music music_list["reminiscences"] fadein 1
    "Девушке надоело валяться на крыше и захотелось есть. Она поднялась, надела платье, открыла тоннель и прямо с крыши столовой шагнула в зал."
    "Сейчас, когда порядок после обеда наведён, у девушки было немного времени, пока не начнут готовить ужин."
    "Девушка прислушалась. В столовой было тихо, только на кухне шумела вода и с крыльца доносился разговор."
    "Пускай девушка и не понимала почти ничего, но разговор её заинтересовал, ведь девушка любила наблюдать за людьми."
    "Неслышно ступая, она прошла через зал и встала, спрятавшись за распахнутой входной дверью так, чтобы её не было видно, насторожив свои кошачьи уши."
    d_vo_2 "И что ты думаешь об оборотне?"
    d_ar_voice "О том, которого гоняли три месяца назад? Славная была погоня, только глупая. Что бы эти охотники с ним делали, если бы поймали?"
    d_ar_voice "Мы не знаем и десятой доли о здешних местах. Мало ли что за неизученная живность в посёлок забрела. И теперь уже не узнаем."
    d_ar_voice "А в посёлке за тридцать пять лет уже накопилось столько легенд, в том числе и об оборотнях. Мифы и легенды образованщины."
    d_ar_voice "Вот, например, про чёрные алтари и жертвоприношения слыхал? Ладно, слушай."
    $ set_mode_nvl ()
    "В общем, есть такая теория, что, кроме нас, сюда лезут или лезли обитатели другой реальности. Мы сосуществуем с ними в одной вселенной, но ощутить друг друга не можем. Просто не пересекаемся. А здесь мы и они чужие, и пусть видим только следы друг друга, но видим."
    "Это всё подтверждается расчётами, но там столько переменных, что вывести можно всё что угодно."
    "Так вот, тринадцатая экспедиция, когда создавали Сеть, натыкалась на вакуоли с примитивными каменными алтарями, расположенными там, где у нас стоит этот бронзовый мужик."
    "Понимаешь? У нас репер узла — это бронзовая статуя. А у них — пирамида из базальтовых глыб. И на глыбах, прямо на базальте, оплавленные углубления в форме ладоней."
    "А в «Справочнике» написано просто: «Экспедиция №13 — изучение узлов четвёртого порядка (эфемерных узлов)»."
    "Информацию закрыли, но следы её можно найти в здешней библиотеке. А вот дальше уже мистика пойдёт."
    nvl clear
    "Мы проникли сюда, используя взрыв водородной бомбы, а они — человеческие жертвоприношения. И отпечатки ладоней как раз остались от жертв."
    "Они тоже люди, но у них совершенно другая цивилизация. И если что-то непонятно здесь, то можно приложить ладони к камню и получить ответ там. Или исчезнуть."
    "Муж Бабули приложил. И исчез."
    "А потом трассу к тем вакуолям стёрли из памяти ЭВМ, поставили двойной барьер, непроницаемый для людей и НБО, отчёт экспедиции засекретили, а сами участники как-то быстро пропали."
    "Но и это ещё не всё. Говорят, что среди наших пионеров-НБО иногда появляются копии людей оттуда, и кончается это трагедией. Либо резнёй в узле, либо узел просто исчезает."
    "Как попадают сюда из-за барьера? Да кто ж их знает. Например, в виде нейтринных колец. Для них-то всё проницаемо."
    "Вот и оборотни наши вполне могут оказаться пришельцами с той стороны."
    stop music fadeout 3
    $ set_mode_adv ()
    show d_ar adl smile2 casual with dspr
    d_ar_voice "Ведь так?"
    hide d_ar with dspr
    "Девушка не сразу поняла, что обращаются к ней. А когда поняла — вздрогнула." 
    "Рассказчик смотрел на отражение девушки в зеркале, висящем в тамбуре столовой."
    stop ambience
    
    scene int_dining_hall_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    d_vo_2 "Ты у меня спрашиваешь? Я человек практический и люблю легенды слушать, а не придумывать. Ладно, побежал я, демонтаж у меня. А ты приходи через два часа, машина придёт — будем твоё оборудование грузить."
    play sound dct_sfx_steps2
    "Застучали подошвы, и невидимый собеседник сбежал с крыльца. А девушка-кошка продолжала стоять и смотреть в глаза парню."
    "Хотела убежать и не могла. Хотела спрятать лицо, закрыв его руками, и тоже не могла. Было и тревожно, и радостно одновременно. И ещё непонятное ощущение, смесь тепла и щекотки, разливалось по телу, беря начало где-то в районе диафрагмы."
    "Парень шагнул в двери столовой."
    show d_ar adl smile2 casual with dspr
    d_ar_voice "Ты удивительно красивая. Не пойму, почему тебя назвали «оборотнем»? Лучше я буду считать тебя{w=1}… нимфой, или лучше{w=1}… нэкой, или, знаешь, была такая богиня — женщина-кошка, а звали её{w=1}… Баст. Весьма положительный персонаж." 
    d_ar "А меня зовут Артём."
    stop ambience
    
    scene black with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play music peritune_gentle_theme_piano
    "Никуда он не пошёл через два часа, так что лаборатория грузила оборудование без него."
    "А в общежитии он появился только поздно вечером и на вопрос соседа по секции: «Где был?» — лишь тепло улыбнулся."
    
    scene ext_path2_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Они бродили, взявшись за руки, по всей Сети и говорили обо всём на свете."
    "Парень находил очень доходчивые слова и за шесть часов сумел сделать то, что так и не смогла Виола."
    "Может быть, потому что увидел в девушке — девушку, а не бывшую кошку. А может быть, потому что у него был талант объяснять и рассказывать."
    "Или потому что девушке интересно было слушать парня. А девушка — девушка просто была. И показывала парню весь свой мир."
    stop ambience
    
    scene dct_ext_old_building_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_old_camp_outside
    "Они побывали в разных местах."
    "Они стояли на крыше старого корпуса и смотрели, как Генда на мгновение превращается в чёрный цилиндр, достающий до неба."
    stop ambience
    
    scene dct_landscape_forest3 with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_forest_day
    "Они шли вдоль кромки леса, парень в своих больших ладонях нёс полную пригоршню малины, а девушка брала ягоду и клала её парню в рот."
    stop ambience
    
    scene dct_ext_lake_sunset with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_forest_evening
    "Они купались в Зеркальном озере, где до воды можно добросить камнем, но нельзя дойти пешком, и жарили на прутьях пойманную девушкой рыбу."
    "Они увидели всё, что девушка хотела показать парню."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_pyramid with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_wind
    "А в самом конце их путешествия они оказались перед пирамидой, сложенной из базальтовых блоков."
    stop ambience
    
    scene dct_altar with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_wind
    play music music_list["door_to_nightmare"]
    show d_ar adl serious casual with dspr
    d_ar "Значит, это правда, значит, действительно есть место, где можно получить ответы."
    "Парень поёжился от ледяного ветра, занёс и долго держал руку над одним из отпечатков-углублений, но так и не приложил."
    d_ar "Мне не о чем спрашивать у мёртвых."
    "Потом он склонился над алтарём, над каменными желобами, уходящими под основание пирамиды, над бронзовыми кольцами, вделанными в камни."
    "Вернулся к алтарю и провёл пальцем по значкам, вырезанным на поверхности."
    d_ar "Египет."
    d_ar "Похоже на Египет. Но, наверное, это какой-то другой Египет."
    stop ambience

    scene dct_ext_pyramid with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_wind
    show d_ar adl serious casual with dspr
    d_ar "Но если это Египет, значит ты и правда — Она…"
    d_ar "Баст! Знаешь, это плохое место, не ходи сюда. Оставайся лучше местной богиней. Хранительницей этой земли."
    d_ar "Завтра я уеду, но я буду помнить, что влюбился в настоящую богиню. Прощай."
    uv_cst "Прощай. Я сделаю как ты сказал. Но однажды я приду за тобой. Что толку от хранительницы, если эта земля существует только пока по ней ходят люди?"
    show gate_ext_square_night behind d_ar:
        alpha 0
        ease 3 alpha 0.8
    uv_cst "Идём."
    hide d_ar with dspr
    stop music fadeout 1
    stop ambience
    
    scene ext_square_night with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    $ renpy.pause (1)
    "Она подала ему руку и провела по туманному коридору прямо на площадь, и там, в тени памятника, они поцеловались в последний раз."
    #show kiss_uv_ar
    show d_ar adl serious casual with dspr
    d_ar "Ты знаешь, что я не смогу остаться, Баст. Если я останусь, это буду не я. Зачем тебе шестьдесят маленьких пионеров, которые ничего не помнят? Зачем им богиня?"
    uv_cst "Я знаю, и тут я бессильна. Но не называй меня так. Лучше я буду обычной девушкой, пусть даже девушкой-кошкой. И всё-таки однажды я приду за тобой."
    show d_ar adl smile2 casual with dspr
    d_ar "Приходи, обычная девушка-кошка. Я буду ждать."
    uv_cgl "Нет, ты скоро всё забудешь, я знаю. Но однажды я приду и позову тебя. А после я тоже буду ждать. Ты обязательно вспомнишь. Прощай."
    hide d_ar with dissolve
    $ renpy.pause (2)
    stop ambience
    
    scene ext_bus with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play music music_list["no_tresspassing"]
    show uv_spy_neko
    show d_us smile dress behind uv_spy_neko with dspr:
        ypos -0.05
    $ renpy.pause (1)
    hide d_us with moveoutright
    "Утром она смотрела из кустов, как к воротам подъехал автобус. Как оттуда выгрузились приехавшие, в том числе и смутно знакомая рыжеволосая девушка."
    show d_ar adl smile2 casual behind uv_spy_neko with moveinright
    "Как в автобус садились уезжающие, а вчерашний парень, прежде чем скрыться в автобусе, долго смотрел на то место, где засела девушка."
    "Он не мог её видеть сквозь деревья, но безошибочно угадал направление."
    show d_ar adl serious casual with dspr
    play sound dct_sfx_cry_short
    "А потом вскинул руку в прощальном взмахе и исчез в салоне, а девушка заплакала — впервые в жизни."
    hide d_ar with dspr
    play sound dct_sfx_bus_departure2
    stop music fadeout 1
    stop ambience
    
    scene ext_no_bus with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    "А когда автобус скрылся за восточными воротами, Генда на мгновение превратился в чёрный цилиндр, достающий до неба, а всех обитателей узла, где бы они ни были, пробрал секундный озноб. Тогда ей стало так плохо, что она, забыв обещания, шагнула к чёрной пирамиде и, не задумываясь, приложила руки к углублениям в базальте."
    show gate_ext_pyramid:
        alpha 0
        ease 3 alpha 0.5
    $ renpy.pause (1)
    stop ambience
    
    scene dct_ext_pyramid with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_wind
    $ renpy.pause (1)
    
    scene dct_altar with dissolve
    $ night_time ()
    play music its_in_the_fog
    $ persistent.sprite_time = "night"
    whisper "Что ты хочешь?"
    uv_cgl "Забыть!"
    "В шум ветра вплетались слова."
    whisper "Хорошо. Завтра ты забудешь, не навсегда, но надолго. Может быть, даже на всю твою нынешнюю жизнь."
    uv_cgl "Подожди! Я не хочу забывать!"
    whisper "Ты хочешь отменить то, что уже решено? Тогда ты должна принести жертву."
    "И ладони вытолкнуло из углублений в камне."
    play sound dct_sfx_knife_drop
    "Что-то брякнуло под ногами — нож. Она подняла его, подержала в руках и уронила на землю. Делать у пирамиды было больше нечего, и девушка-кошка вернулась в привычный лес."
    stop music fadeout 1
    stop ambience
    
    scene dct_to_in_bog with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_swamp
    "Охотник лежал, распластавшись животом на трясине, и пытался отстегнуть ружейный ремень. Паники не было, была злость."
    "Отстегнул. Забросил ружьё на твёрдую землю, по соседству с полевой сумкой. Ремешок от полевой сумки и поясной ремень, уже связанные между собой, были намотаны на левую руку охотника."
    "Теперь нужно было зацепить одним карабином оружейный ремень за пряжку поясного ремня, а ко второму карабину зацепить нож в ножнах."
    d_to "Ну что? Бросаем?"
    scene dct_to_in_bog with vpunch
    play sound dct_sfx_jump_in_swamp
    d_to "Это был громкий плюх. А ещё я, кажется, погрузился чуть глубже. Вторая попытка."
    scene dct_to_in_bog with vpunch
    play sound dct_sfx_jump_in_swamp
    d_to "Толяныч, лежи и не дёргайся! А то погружаешься. Отдышись и делай ещё попытку."
    scene dct_to_in_bog with vpunch
    play sound dct_sfx_jump_in_swamp
    "С третьей попытки охотнику удалось зацепиться. Конец ремня с ножом закрутился вокруг ствола чахлой сосенки, и охотник осторожно потянул."
    "Сосенка начала угрожающе наклоняться в его сторону, выворачиваясь с корнями из слабой почвы."
    "Это было нормально. Осталось подтянуть её к себе, и получилась бы опора для тела."
    "Сосенка наклонилась ещё сильнее, и конец ремня соскользнул со ствола."
    play sound dct_sfx_jump_in_swamp
    d_to "М-мать!"
    scene dct_to_in_bog with vpunch
    "Охотник подтянул ремень к себе, отдохнул немного и забросил ремень снова."
    "Дерево изменило своё положение, и зацепиться не получалось, а каждый бросок чуть притапливал охотника."
    "Какое-то время спустя охотник выдохся. Он лежал, повернув голову так, чтобы можно было дышать, и старался не шевелиться."
    stop ambience
    
    
    scene dct_to_in_bog_2 with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience dct_ambience_swamp_night
    play music music_list["orchid"]
    d_to "Темнеет. Скоро туман будет, тот самый. Если я не буду двигаться, чтобы меня не засасывало дальше — я, наверное, дотяну здесь до тумана."
    d_to "А там уже будет неважно. Не хотелось бы, конечно. Я всё делал, чтобы люди не попадали в лапы к этой мерзости, а сейчас вот сам жду тумана."
    play sound dct_sfx_steps_in_swamp
    d_to "И будет шестьдесят маленьких Толь, ничего не помнящих и живущих двухнедельными циклами — это тоже жизнь."
    "Что-то потянуло его за левую руку — ремень от полевой сумки. Охотник проследил глазами и увидел «свою» девушку-кошку."
    d_to "Вот и встретились. Глупо."
    "А та развернула лихорадочную деятельность."
    "Схватила ружьё, положила его стволами поперёк сосенок-близнецов, обмотала конец ремня вокруг стволов. Сама схватилась за ремень, сев на землю и уперевшись ногами."
    
    scene dct_ext_lake_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    show uv rage with dspr
    uv_cgl "Тяни! Тяни же!"
    
    #scene uv_to_boloto with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play sound dct_sfx_splash_in_swamp
    $ renpy.pause (2)
    stop music fadeout 1
    stop ambience
    
    scene d_to_and_uv_close with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_bonfire
    "Через час, уже в темноте, они сидели плечом к плечу у костра и сушили одежду. И девушка выглядела и разговаривала совсем не так, как два дня назад с Виолой."
    uv_cgl "Зачем ты залез в эту топь, Охотник?"
    d_to "Эта топь у нас называется Бескрайнее болото. А Охотник — дурак и не поверил."
    d_to "Место он для засады искал. Ну знал, что болото, ну почва колышется под ногами, а она возьми да провались — почва."
    uv_cgl "И я даже знаю, на кого эта засада. Но вот так вышло."
    uv_cgl "Ты должен был прийти сюда, а я должна была позвать тебя с собой. Но я подумала, что неправильно звать тебя в таком состоянии."
    uv_cgl "Ты бы согласился сейчас на что угодно, а зачем ты, такой «доброволец», нужен?"
    d_to "А я должен был убить тебя, пока ты не трансформировалась, а сейчас не знаю, что мне делать."
    d_to "Ты же трансформировалась полностью? Так что теперь я просто обязан это сделать. А я не хочу."
    
    scene d_to_and_uv_far with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_bonfire
    uv_cgl "Преобразилась. И теперь, чтобы остаться такой, я просто обязана привести тебя на алтарь. А я не хочу."
    uv_cgl "И можешь меня убить. Всё равно кто-то притащит сюда кошку, и я опять воплощусь. И может быть, вспомню то, что забуду завтра."
    "Трещали сучья в костре. Анатолий разглядывал девушку, доедающую его бутерброд. Сейчас она выглядела скорее безвозрастной и казалась то пятнадцати-, а то сорокапятилетней."
    d_to "Преобразилась и воплощаешься. Ещё скажи, что ты богиня."
    
    scene black with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    show uv laugh with dspr
    $ renpy.pause (1)
    uv_cgl "Точно, Баст. Или Сехмет. Мифы Древнего Египта. Я ещё не решила."
    
    scene d_to_and_uv_far with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_bonfire
    uv_cgl "Говоря вашим языком, блуждающее нейтринное кольцо, которое может материализоваться в достаточно интеллектуальном домашнем животном."
    d_to "А слов таких где нахваталась?"
    uv_cgl "Вытаскивала из памяти животных — животные всё запоминают. Не понимают, но запоминают."
    
    scene black with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    show uv sad with dspr
    $ renpy.pause (1)
    uv_cgl "Шучу. Мне рассказали и объяснили. А завтра я это забуду."
    stop ambience
    
    scene dct_ext_lake_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    $ renpy.pause (1)
    show gate_ext_camp_entrance_night:
        alpha 0
        ease 3 alpha 0.8
    $ renpy.pause (1)
    show uv grin with dspr
    uv_cgl "Ну, ты закончил сушиться? Отвести тебя домой? Или ты здесь ночевать думаешь?"
    stop ambience

    scene ext_no_bus_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    play music feeling_good
    show gate_ext_polyana_night:
        alpha 0
        ease 3 alpha 0.8
    $ renpy.pause (1)
    "Девушка-кошка возвращалась домой. Шаг, и ты прямо с автобусной остановки оказываешься в тоннеле со стенами, сотканными из тумана."
    "Ещё шаг, и ты оказываешься у себя, в одной из квартир — пусть сегодня это будет лесная поляна."
    "Там такая удобная ветка, невысоко нависающая над землёй. И есть зажигалка, которую подарил тот человек на прощание."
    stop ambience
    
    scene dct_bonfire with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_bonfire
    "Можно развести костёр, а самой запрыгнуть на ветку и смотреть на пламя сверху: как оно разгорается, пожирая сучья, и как оно умирает, когда пища заканчивается."
    "Смотреть, как бегают красные искры по остывающим углям, а потом уснуть. А проснувшись, спрыгнуть вниз, прямо с ветки прямо к погасшему костру."
    "Потрогать тыльной стороной ладони ещё тёплое кострище и убежать к озеру умываться, а оттуда — на промысел еды."
    stop music fadeout 1
    stop ambience
    
    scene ext_no_bus_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    show gate_ext_polyana_night:
        alpha 0.8
    play sound dct_sfx_cry
    "Девушка-кошка остановилась, перед тем как сделать шаг, когда услышала плач."
    "Плакала девочка. Плакала где-то недалеко, за одним из выходов. Плакала горько и безнадёжно. И девушка-кошка, не задумываясь, шагнула туда."
    stop sound
    stop ambience
    
    scene d_us_cry_far with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    play sound dct_sfx_cry
    "Девочка. Вся зарёванная."
    
    scene d_us_cry_close with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    "Всхлипывает, уткнувшись лицом в колени."
    stop sound
    stop ambience

    scene d_us_and_uv_far with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    play music i_tried_to_bring_it_back
    uv_cgl "Что стряслось у тебя? Расскажешь?"
    
    scene d_us_and_uv_close with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    us "А я тебя помню. Я тебя видела в посёлке год назад. Ты тогда была кошкой, а теперь выросла."
    uv_cgl "Я тоже тебя помню. Ты была большой, а стала маленькой. Ты обещала, что мы ещё встретимся — вот и встретились. Так что случилось у тебя?"
    us "Я. Я осталась Сёмку ждать, а его нет и нет. И теперь мне страшно. И назад я уйти не хочу, потому что Сёмка где-то здесь. А если уйду — ему совсем плохо будет. У него никого, кроме меня, нет. И мне плохо будет."
    uv_cgl "Ну так пойдём. Ты пойдёшь со мной?"
    us "Куда?"
    uv_cgl "Туда, где тебя обязательно найдёт твой Сёмка."
    stop music fadeout 1
    stop ambience
    
    scene gate_ext_camp_entrance_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    "Девочка доверчиво хватает девушку-кошку за руку, и они идут по тоннелю, сотканному из тумана."
    "Девушке-кошке достаточно одного шага, а вот девочка так не умеет, и ей приходится идти дольше. Но это ничего не значит, потому что здесь, в тумане, время и расстояние — вещь субъективная."
    us "Только{w=1}… Я была большая, и Сёмка — он большой. А сейчас я маленькая. Он же может меня не заметить. Или не узнать."
    uv_cgl "Захочет — заметит и узнает. Но твоему горю можно помочь. Только ты должна будешь поделиться."
    us "Чем? У меня же ничего нет, только медведь."
    uv_cgl "Собой. Не бойся, это не больно. Ты ничего не потеряешь и ничего не почувствуешь. Просто у тебя появится много сестрёнок. Очень похожих на тебя, но в чём-то других. Совсем большой ты не станешь, но наполовину подрастёшь. Где-то до границы детства. Дальше у меня силы нет, дальше — сама."
    us "Я согласна!"
    "А ладонь девушки-кошки сжимает уже не одна ладошка, а сразу несколько десятков. Это странное место нуждается в обитателях-людях. Без людей его просто не существует, а заселить себя оно может только так."
    stop ambience
    
    scene ext_camp_entrance_night with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    play music music_list["a_promise_from_distant_days"]
    uv_cgl "Вот мы и пришли. Тебе туда. Вам всем — туда."
    "Ладошки — все, кроме одной — отцепляются, и девочка бежит, обнимая медведя, к воротам."
    "Девушка-кошка видит, как коридор раздваивается, и по каждому уже бежит по девочке. Потом ещё и ещё."
    show us smile sport far with dspr
    "Внезапно одна из девочек останавливается, разворачивается и бежит обратно."
    show us smile sport with dspr
    us "Спасибо, сестрёнка."
    show us smile sport close with dspr
    us "Ещё увидимся, киса!"
    hide us with dspr
    "Перед воротами остаются двое."
    "Девушка-кошка легонько подталкивает в спину последнюю девочку."
    uv_cgl "Прощай, тебе тоже туда."
    "Та идёт, но у самого выхода оборачивается и машет рукой."
    show us smile sport far with dissolve
    "И на зарёванном лице проступает озорная улыбка."
    "А девочка, оказывается, уже не девочка, а девушка. Молоденькая, ещё одной ногой стоящая в детстве, но уже девушка."
    hide us with dissolve
    stop music fadeout 1
    show gate_ext_polyana_night:
        alpha 0
        ease 3 alpha 0.8
    $ renpy.pause (1)
    "Бывшая кошка машет в ответ, делает шаг в сторону и оказывается на знакомой поляне."
    stop ambience

    scene ext_polyana_night with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    play music music_list["mystery_girl_v2"]
    uv_cgl "Мифы древнего Египта закончились, осталась полусказка-полунаука, сутки, отпущенные на жертвоприношение, истекли, и пора возвращаться в обычное состояние кошки-мутанта."
    uv_cgl "Но это лучше, чем убивать того охотника на алтаре. Я Баст, а не Семхет."
    "Она ещё размышляет, не развести ли ей костёр, но решает, что и так хорошо."
    show blink
    "Запрыгивает на ветку, устраивается на ней и засыпает, свесив вниз руки."
    stop music fadeout 1
    stop ambience


    scene white with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play sound dct_sfx_typewriter
    show promo_text u"Секретно\nЭкземпляр: единственный.\nЗаместителю директора\nИнститута xxxxxx АН СССР\nТема: «Куколка»"  with dissolve:
        pos (0.6, 0.1)
    $ renpy.pause (1)
    pause
    hide promo_text with dspr
    show promo_text u"По результатам наблюдений, ожидаемый срок трансформации объекта — не позднее 05 июня 1992 года.\nДоставка объекта в институт в связи с ликвидацией филиала невозможна.\nВследствие вышеизложенного, согласно Руководящей инструкции и в связи с необходимостью оперативного реагирования, мною по согласованию с руководством филиала было принято решение об изъятии и ликвидации объекта.\nВ ходе оперативных мероприятий объект был блокирован и уничтожен 31 мая 1992 года в 20ч. 32м. в точке с координатами: узел 22; квадрат 1134; квартал Ж6; в 55 метрах от центра квартала в направлении на репер узла.\nРасход спецбоеприпасов — 1 патрон.\nВ связи с тем, что данная точка находится в болоте, достать физическое тело объекта без применения тяжёлой техники и осушения болота не представляется возможным. Сфотографировать объект не удалось в связи с тёмным временем суток.\n\nПриложения:\n1. План местности с указанием точки захоронения объекта.\n2. Образец тканей объекта (волосы).\n\nЗаместитель руководителя филиала Института xxxxxx АН СССР\nГ***в Анатолий Васильевич."  with dissolve:
        pos (0.02, 0.1)
    pause
    stop sound
    
    scene black with blinds
    $ persistent.d_miuki = d_miuki + 1
    
menu:
    "Конец книги «Кошкин дом»"
    "Продолжить":
        jump dct_olga
    "К оглавлению":
        jump dct_mnu2