label dct_prologue:
    scene black
    show headline_text u"Пролог" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
label dream1:
    $ prolog_time()
    $ set_mode_nvl()
    $ save_name = u"Дубликат. Пролог"
    play music music_list["orchid"]
    scene dct_ext_square_day_gate with blinds #пока так, заказать — должна быть площадь п. Шлюз
    show dct_dream_veil:
        shiver
    "Вот уже который цикл я вижу один и тот же сон. Почти каждую ночь."
    "Начинается он с того, что я смотрю в окно. Смотрю на площадь, по которой гуляют пылевые смерчики."
    "На клумбы, уже успевшие зарасти сорняками. На сломанную ветром ветку, лежащую поперёк скамейки."
    "Полугода не прошло, а всё уже пришло в запустение. Только Генда вечен."
    "Ничего, скоро здесь опять будет порядок. Может быть, даже я сам и уберу эту несчастную ветку."
    "Или подмету площадь. Или полью цветы на клумбах."
    nvl clear
    play ambience dct_ambience_conf fadein 2
    "А в помещении за моей спиной идёт совещание. Люди не могут без совещаний. Даже сейчас."
    "Что делать — они напуганы. Не могут смириться с произошедшим."
    "И прячутся от своего страха в работе. Или вот в таких совещаниях."
    "А одному из них послезавтра предстоит убить меня."
    "Да. Послезавтра тот я, который снится, исчезнет. Так надо. Нет, так необходимо."
    "Тот я… Он давно уже решился, но ему всё равно страшно. Страшно и не хочется исчезать."
    nvl clear
    "А совещание заканчивается."
    "Я вслушиваюсь в голоса: два мужских голоса и два женских."
    stop music fadeout 2
    $ set_mode_adv()
    "Начинает женщина. Пожилая и властная, судя по голосу. Голос тихий, но такой, что к нему сразу прислушиваешься."
    d_prlg_voice1 "…значит, так и поступим. Давайте тогда ещё раз проговорим всё."
    d_prlg_voice1 "Начну с себя:"
    d_prlg_voice1 "Энергия — с внешней подпиткой проживём без ограничений, без внешней подпитки придётся необитаемые узлы отключать; {w}снабжение — синтезаторов хватит лет на двести."
    d_prlg_voice1 "Связь с материком — я одну телефонную линию оставляю здесь и факс на ней, если там найдут, что сказать умного, то пусть попытаются; {w}связь между нами — телефоны есть, но, сами понимаете, не всегда работают."
    d_prlg_voice2 "Управляющие системы исправны, Город и Имитатор я только что протестировал — в порядке."
    "В разговор вступает мужчина. Этот говорит так, как будто только что думал о чём-то своём. Не совсем впопад и после небольшой паузы."
    d_prlg_voice1 "Ты тоже намерен жить как…{w} пионеры?"
    d_prlg_voice2 "Уж сколько раз говорилось — да. И давайте оставим эту тему. У меня всё."
    d_prlg_voice3 "Шлюз перекрыт, маяк разобран. Пробиться к нам снаружи физически нереально, даже через теплообменник. {w}Через Имитатор, в виде сознания-наездника, насколько я понимаю, тоже."
    "Это подключается третий участник радиопостановки. Тоже мужчина. Говорит чётко, громко, внятно и по существу. Голос чуть хриплый, словно когда-то был сорван." 
    d_prlg_voice2 "Не совсем. Я не могу полностью перекрыть обмен информацией. Поэтому подсадить наездника кому-то из пионеров возможно…"
    d_prlg_voice3 "Понятно кому."
    d_prlg_voice2 "…но канал я зажал настолько, что полноценно можно перекинуть только одну персону, и та будет распределена между двойниками. Кстати, очень хорошая Гауссовская кривая получается. Остальные персоны будут недееспособны."
    d_prlg_voice3 "Ну, одного как-нибудь отследим. У меня тоже всё."
    d_prlg_voice4 "Пионерам оставляем двухнедельный цикл под наблюдением мониторов."
    "А это говорит женщина. Глубоким и бархатистым голосом. И она явно моложе первой."
    d_prlg_voice4 "Тех, кто необратимо выпадает из цикла, либо переносим в Город, либо в незанятые узлы, либо предлагаем присоединиться к нам, либо предлагаем эвакуацию на материк."
    d_prlg_voice3 "Почему нельзя оставлять таких в узлах? Почему вообще не отключить все эти циклы?"
    d_prlg_voice4 "Во-первых, есть риск, что всё посыпется."
    d_prlg_voice1 "Подтверждаю."
    d_prlg_voice4 "Спасибо, я сама. А во-вторых, если отключить циклы, то здесь половина, чей мозг ещё не развит, скатится до уровня животных, {w}а вторая половина — дети от семи до семнадцати, что бы у них в голове спрятано ни было."
    d_prlg_voice4 "Я не рискую их отпустить в свободное плавание, мне их жалко. Поэтому только циклы. {w}А кто вырастет из циклов — тем уже самим решать свою судьбу. Если хотите, это как экзамен на аттестат зрелости. {w}И не думайте, что мне это нравится, циклы эти."
    d_prlg_voice1 "В таком случае никого не задерживаю. Вы были не самые дисциплинированные подчинённые, но вы оказались очень хорошими людьми. Всем спасибо."
    play sound dct_sfx_chair
    "Слышно, как двигаются стулья, слышно, как люди встают и идут к выходу."
    play sound sfx_open_door_1 
    d_prlg_voice1 "Послезавтра расстаёмся. Завтра собираем чемоданы. А сегодня вечером жду всех в столовой. Приглашаю всех, даже тех, кто проглядел дыру в окне."
    d_prlg_voice3 "Если бабушка зовёт в столовую, значит будет вкусно. Рекомендую."
    "Последняя реплика звучит над самым моим ухом и явно предназначена мне."
    "Голоса ужасно знакомые."
    "Мы оба — и тот я, которому снится сон, и тот, который действует во сне — хотим повернуться, чтобы увидеть этих людей."
    "И в этот момент я всегда просыпаюсь."
    stop ambience
    $ renpy.pause(2.0)    
        
label morning_zero:
    $ night_time()
    $ set_mode_nvl()
    $ persistent.sprite_time = "night"
    scene int_house_of_mt_night2 with blinds
    play ambience ambience_int_cabin_night
    "Сон очень реалистичный. Даже запахи в нём присутствуют: пыли с улицы, дерева от столов, женских духов и табака. И ветерок из приоткрытого окна холодит щеку."
    "Это сон, а есть ещё и реальность. Или другие сны? Или всё же реальность?"
    "Впрочем, я уже запутался и не знаю, что считать сном, а что — реальностью."
    "Моё бытие у себя дома?" 
    "Моё пребывание в пионерском лагере?"
    play music music_list["trapped_in_dreams"]
    $ set_mode_adv()
    play sound sfx_open_journal
    "Извольте."
    "Вот вам мой первый вариант реальности."
    play sound dct_sfx_solo_card
    show dct_intro_xx_grayscale_small:
        pos(0.1,0.35)
        rotate(-8)
    "Текущий год в этой реальности — две тысячи седьмой, действующее лицо — Персунов Семён Семёнович, двадцати семи лет, незаконченное высшее, эникейщик, живёт один."
    play sound dct_sfx_solo_card
    show dct_prolog_4_grayscale_small with dissolve:
        pos(0.15,0.30)
        rotate(-4)
    $ renpy.pause(1.0)
    play sound dct_sfx_solo_card
    show dct_semen_room_grayscale_small with dissolve:
        pos(0.2,0.25)
    "Из дома выходит всё реже и реже, предпочитая общаться и работать дистанционно."
    play sound dct_sfx_solo_card
    show dct_intro_8_grayscale_small with dissolve:
        pos(0.25,0.20)
        rotate(4)
    "Вариант вроде бы правдоподобный и приемлемый, но, чёрт, я в нём давно уже не уверен."
    "А вот второй вариант: конец восьмидесятых, тот же самый Персунов Семён Семёнович, но семнадцати лет, пионерский лагерь «Совёнок»."
    play sound dct_sfx_solo_card
    show dct_d2_lineup_grayscale_small:
        pos(0.35,0.35)
        rotate(-8)
    "Почему именно «Совёнок», а не какая-нибудь «Юная смена» — я не знаю. И семнадцатилетние пионеры никого в этом лагере не смущают,{w} так же как и бронзовый памятник неизвестному мне мужику по имени Генда на центральной площади этого лагеря."
    play sound dct_sfx_solo_card
    show dct_d2_mirror_grayscale_small with dissolve:
        pos(0.4,0.3)
        rotate(-4)
    "Звучит как бред, но это так. И этот вариант мне кажется, несмотря на всю его бредовость, гораздо более правдоподобным. Даже несмотря на то, что в этом варианте реальности присутствуют как минимум трое моих двойников и намёки одного из них на множество таких лагерей."
    play sound dct_sfx_solo_card
    show dct_d3_disco_grayscale_small with dissolve:
        pos(0.45,0.25)
    "Поэтому я и пытаюсь действовать, исходя прежде всего из этого варианта. Тем более что первый вариант давно уже не напоминал о себе."
    play sound dct_sfx_solo_card
    show dct_int_dining_hall_people_day_grayscale_small with dissolve:
        pos(0.5,0.2)
        rotate(4)
    "И точка, объединяющая обе реальности — автобус маршрута четыреста десять."
    show intro_13 with dissolve2
    $ renpy.pause(2.0)
    stop music fadeout 1
    stop ambience
    
    scene int_house_of_mt_night2
    play ambience ambience_int_cabin_night
    $ set_mode_nvl()
    "И чему верить?"
    "Моей памяти?"
    "Реальности, данной мне в ощущениях?"
    "Снам?"
    $ set_mode_adv()
    play music music_list["goodbye_home_shores"]
    th "Хватит валяться. Который час?"
    "Смотрю на будильник и сам же себе отвечаю:"
    th "Без десяти минут пять утра. Самое подходящее время, чтобы ещё поспать."
    "Осторожно встаю, стараясь не скрипеть кроватью. Прислушиваюсь к дыханию вожатой — нет, всё тихо. Начинаю одеваться. Если проснётся, то скажу, что на пробежку."
    th "Так, надо будильник перевести на час вперёд, а то бегать в пять утра — это не то, что должен делать «порядочный пионер». {w}И не забыть потом обратно стрелки переставить."
    "Всё, оделся. Тихо-тихо, но не забыв прихватить с собой будильник, выскальзываю в утренний сумрак. Ключ от сарая с вёслами в кармане, будильник в руках."
    stop music fadeout 3
    th "Вперёд, во имя… Не знаю я, во имя чего, но вперёд."
    stop music fadeout 1
    stop ambience
    
    scene ext_house_of_mt_night_without_light with dissolve
    play sound sfx_close_cabinet
    play ambience dct_ambience_morning_birds
    th "Пока ещё темно, но скоро уже рассветёт."
    th "Я как раз успею дойти до пристани."
    th "Так я и не узнал, как называется здешняя река. И, наверное, уже не узнаю."
    stop ambience fadeout 3
    
    scene ext_houses_sunset with dissolve:
        walking
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_night
    "До пристани — метров пятьсот примерно на юг и пересечь две аллеи и площадь."
    th "По тропинкам или по асфальту?"
    "Смотрю направо, в сторону домика Лены и Мику, смотрю налево, на ближайшие кусты, и сворачиваю направо же, на асфальт."
    "Маловероятно, что меня сейчас кто-то увидит, а идти тропинками — это значит делать большой крюк. Времени жалко."
    stop ambience
    
    scene ext_square_sunset with dissolve:
        walking
    play ambience ambience_camp_center_day
    "Как это началось? Если верить моей памяти, конечно, то можно выстроить вроде бы стройный и непротиворечивый вариант." 
    "Вроде бы. {w}Выстроить. {w}Стройный. {w}Непротиворечивый. {w}Ни разу не фантастический."
    stop ambience
    
    scene black with squares
    $ prolog_time()
    play music music_list["no_tresspassing"]
    show intro_8 with dspr
    "{i}Живёт на свете эникейщик Семён Персунов. Девушки нет, друзей нет, квартира досталась от бабушки, университет бросил на третьем курсе, в армию не взяли по здоровью.{/i}"
    hide intro_8
    show prologue_monitor_4
    with dissolve
    "{i}Любимое занятие — висеть на имиджбордах, переписываясь с себе подобными. Не любимое, конечно, но это всё, на что его хватает. Днём на работе, вечером где-то на имиджбордах.{/i}"
    hide prologue_monitor_4
    show prologue_monitor_3
    with dissolve
    "{i}Денег хватает на еду и одежду, большего и не надо. А окружающий мир давно уже не интересует. На винчестере скачанные и не просмотренные фильмы, непрослушанная музыка, непрочитанные книги, непройденные игры.{/i}"
    hide prologue_monitor_3
    show prologue_monitor_2
    with dissolve
    "{i}Даже на игры уже не хватает сил и желания. Иногда ещё аниме глянет, а ведь когда-то был фанатом. Социофоб. Хикка. Как ещё назвать? Не знаю, сами придумайте.{/i}"
    hide prologue_monitor_2
    show prologue_monitor_1
    with dissolve
    stop music fadeout 3
    "{i}И вот однажды в его мирок стучится посторонний.{/i}"
    play sound sfx_home_phone_ring
    $ renpy.pause(4, hard=True)
    me "{i}Да.{/i}"
    
    scene semen_room_window
    play ambience dct_ambience_living_room
    voice "{i}Привет. Узнал?{/i}"
    me "{i}Не узнал. Но какая разница?{/i}"
    odn "{i}Мы тут встречу потока затеваем. Я всех обзвонил уже, ты один остался.{/i}"
    me "{i}Понятно.{/i}"
    th "{i}Зачем я там?{/i}"
    "{i}Одногруппник долго меня уговаривает, и в конце концов я сдаюсь. Проще было согласиться и пообещать прийти, чем отказаться.{/i}"
    odn "{i}В общем, мы тебя ждём.{/i}"
    play sound dct_sfx_short_beeps
    $ renpy.pause(4, hard=True)
    stop ambience
    play sound dct_sfx_bus_arrival
    $ renpy.pause(1, hard=True)
    show intro_9 with dspr
    $ renpy.pause(1, hard=True)
    "{i}«Так и помрёшь эникейщиком?», — это меня одногруппник спросил, когда уговаривал на встречу потока приехать. Он был очень настырным и, кажется, поставил себе целью вытащить меня из дома.{/i}"
    $ renpy.pause(1, hard=True)
    hide intro_9
    show intro_11
    with dissolve
    $ renpy.pause(1, hard=True)
    "{i}Если бы я считал себя какой-то значительной фигурой, я бы задался вопросом о том, кому и зачем надо было так активно меня уговаривать. С какой целью?{/i}"
    hide intro_11
    show intro_13
    with dissolve
    $ renpy.pause(1, hard=True)
    play sound dct_sfx_bus_departure
    "{i}И ещё: почему на остановку пришёл именно этот автобус — древний, дребезжащий и разваливающийся на ходу ЛиАЗ, которых уже почти не осталось?{/i}"
    $ renpy.pause(4, hard=True)
    stop sound
    
    scene dct_ext_boathouse_sunset with squares
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    play music music_list["eat_some_trouble"]
    play ambience ambience_boat_station_day
    "Вот так, пока размышлял, и добрался до пристани. Вот и сарай с вёслами. Тот ли я ключ украл со связки вожатой? Тот."
    play sound "<from 2.6>" + sfx_slavya_run fadein 1.5
    $ renpy.pause (2)
    show 3500_sl smile3 sport at left with moveinleft:
        ycenter 0.83
    "Захожу в сарай, и вовремя. Славя. Ранняя пташка. Уже проснулась и отправилась на пробежку."
    play sound "<from 2>" + sfx_slavya_run
    $ renpy.pause (0.2)
    hide 3500_sl with moveoutright
    $ renpy.pause (0.8)
    stop sound fadeout 1.5
    "Славя — первая, кто всегда меня встречает по приезду, и так получилось, что она, сама не зная того, пришла меня проводить."
    "Слежу в щёлку, как пробегает мимо меня девушка в сторону домика Рыжих. Пробежала. Это хорошо, это славно. А я выбираю вёсла."
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    "Выбираю те, что ближе лежат. Сейчас запру сарай, сломаю ключ в замке, чтобы сразу не открыли, и… И всё."
    stop music fadeout 2.0
    stop ambience
    
    scene black with squares
    $ day_time()
    $ persistent.sprite_time = "day"
    play music dreamers_of_the_day
    "Символично. Первый человек в лагере, которого я вижу — это Славя. И вот она же — надеюсь, последний."
    show intro_13 with dspr
    $ prolog_time()
    "{i}Представьте себе: Семён Персунов образца декабря две тысячи седьмого года садится вечером в ЛиАЗ в своём городе, чтобы уехать на встречу с однокурсниками.{/i}"
    "{i}Проще было согласиться приехать, чем послать подальше, а когда пришло время ехать, в голове мелькнуло: «Почему бы и нет?» — вот он и поехал.{/i}"
    show blink
    hide intro_13
    $ renpy.pause (2)
    show int_bus
    show unblink
    play sound sfx_bus_stop
    "{i}По дороге Семён засыпает, а просыпается жарким июньским днём восемьдесят непонятного года в Икарусе, стоящем перед воротами пионерского лагеря.{/i}"
    stop sound
    "{i}Паника, попытка дозвониться хоть куда-нибудь, наконец с обречённым спокойствием он выходит из автобуса, подходит к воротам, а там этакая русская красавица \(ну действительно же красавица, хоть картину пиши\).{/i}"
    stop music fadeout 2.0
    $ renpy.pause(2, hard=True)
    $ persistent.sprite_time = "day"
    
    scene ext_camp_entrance_day with dspr
    play ambience ambience_camp_entrance_day
    show sl normal pioneer at center with dissolve
    sl "{i}Привет! Ты, наверное, только что приехал? Меня Славя зовут. Вообще-то полное имя Славяна, но все зовут Славя. И ты зови.{/i}"
    stop ambience
    
    scene black
    play music music_list["gentle_predator"]
    "{i}И завертелось. Внезапно оказывается, что этому Семёну семнадцать лет и он приехал в пионерский лагерь последний раз после школы.{/i}"
    show d2_mirror with dissolve2
    "{i}Что он опоздал к началу смены и его давно ждут.{/i}"
    hide d2_mirror
    show dct_lineup
    with dissolve2
    "{i}И участие в жизни отряда — его обязанность как «порядочного пионера».{/i}"
    "{i}Вот только сбежать из этого лагеря не получается. А все попытки Семёна прояснить ситуацию ни к чему не приводят, и Семён за пару дней сдаётся: «Чёрт с вами, раз вы считаете, что я пионер, значит я пионер», — тем более что в зеркале-то он видит себя семнадцатилетним.{/i}"
    hide dct_lineup
    show int_bus_people_day
    with dissolve2
    "{i}А через неделю внезапно смена заканчивается. Все пионеры на том же самом Икарусе едут в некий мифический «райцентр».{/i}"
    hide int_bus_people_day
    show int_bus_people_night
    with dissolve2
    "{i}Едут долго, по дороге все засыпают, и Семён просыпается в своём городе.{/i}"
    hide int_bus_people_night
    show semen_room_window
    with dissolve
    "{i}На следующий день после той самой встречи однокурсников. Или за несколько дней до той самой встречи однокурсников. Или за несколько недель, или за несколько лет. Тут возможны варианты. И проще всего считать всё пережитое сном.{/i}"
    "{i}Проходит время, сон забывается, пока однажды вечером вновь не раздаётся телефонный звонок.{/i}"
    hide semen_room_window with dspr
    odn "{i}Пять лет выпуска же, Сём, я всех обзвонил, тебя только не хватает!{/i}"
    "{i}И Семён опять садится в автобус, чтобы проснуться перед воротами пионерского лагеря.{/i}"
    "{i}И так цикл за циклом. И в каждом текущем цикле память о предыдущем у Семёна стирается, и он так и бегает по кругу, как трамвай между двумя конечными остановками: «Город» и «Лагерь».{/i}"
    "Так я сначала и жил, а потом начал что-то вспоминать по кусочкам. И когда просыпался перед воротами «Совёнка», уже знал, что меня ждёт."
    stop music fadeout 2.0
    
    scene dct_boathouse_semen with squares
    $ day_time ()
    play music music_list["door_to_nightmare"]
    "И вот сейчас я здесь, на пристани, кажется, впервые не знаю, что случится через тридцать минут. Ещё не поздно вернуться в домик, поставить будильник на стол и лечь спать, как будто ничего и не было."
    "Мне отчаянно страшно на самом деле. Может быть, даже страшнее, чем тому мне, который мне же и снился час назад. Но я больше не могу. {w}Прощайте."
    $ renpy.pause(3.0)
    
    scene black with blinds
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    $ persistent.d_prolog = d_prolog + 1
    
    jump dct_mnu2

