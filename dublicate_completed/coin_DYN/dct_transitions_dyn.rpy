    ###################
    #Глава 2. Переходы#
    ###################

label dct_transitions_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Переходы\n(dynamic)"
    $ day_time()
    $ persistent.sprite_time = "day"
    scene black
    show headline_text2 u"Глава II. Переходы" at truecenter with dspr
    play ambience ambience_camp_center_evening fadein 2
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_ext_house_of_el_night
    show dct_ext_house_of_el_sunset:
        alpha 0.0
        linear 5.5 alpha 1.0
    $ renpy.pause(5.0,hard=True)
    play ambience ambience_int_cabin_day fadein 1
    
    scene dct_int_house_of_el_day
    show dct_int_house_of_el_sunset:
        alpha 1.0
        linear 5.5 alpha 0.0
    with dissolve
    $ renpy.pause(2.5,hard=True)
    play sound sfx_slavya_run
    $ renpy.pause (2.5,hard=True)
    stop sound fadeout 2.5
    "Электроник проснулся в тот момент, когда мимо их домика в сторону стадиона пробежала Саша. Полежал ещё, прислушиваясь к удаляющимся шагам, покосился на спокойно спящего соседа."
    th "Хорошо, что вчера Шурик в кружке ночевать не остался."
    th "Надо будет всё же над ним шефство взять, а то он легко может загнать сам себя. Такие гении нужны человечеству."
    th "Эта девочка, Александра — она бегать побежала."
    th "Наверное, на стадион."
    th "Хорошая девочка, сразу видно."
    extend " Почему я их вчера с этой японкой Мику так испугался?"
    th "Конечно! Мику же с Женей живёт, теперь расскажет Жене, как я вчера на крыльце библиотеки топтался — что Женя обо мне подумает?"
    th "Может, уже рассказала.{w=0.5} Стыдно."
    th "А мне сегодня обходной подписывать. Может, Шурика попросить сразу два обходных подать?"
    th "А Женя спросит: „Что, стыдно ему после автобуса на глаза показываться?“. И что Шурик ответит?"
    th "Нет, нехорошо Шурика подставлять. Пойду сам."
    th "Если Женя спросит про вчерашний вечер — скажу, что извиниться хотел; если не спросит, то сам извинюсь — может, она лучше ко мне относиться будет."
    play sound dct_sfx_alarm
    play sound2 dct_sfx_horn_rise
    "Электроник улыбнулся, вспоминая тяжесть Жениной головы у себя на плече и запах её волос."
    "Электроник взглянул на Шурика, укрывшегося с головой одеялом, и задумался: будить или нет?"
    "Поколебался пару минут и решил всё-таки разбудить. Сегодня же первый день смены, после завтрака будет первая линейка, важные объявления и прочее. Не стоит пропускать."
    stop ambience fadeout 1
    stop sound
    stop sound2 fadeout 1

    $ renpy.music.set_volume(0.6)
    play music music_list['orchid'] fadein 2
    scene dct_dream_sh_first_disert
    show dct_dream_veil at shiver
    with fade2
    "А Шурику снился странный сон."
    "Снилось, что он где-то в пустыне на полигоне."
    "Жёлто-бурый песок, серо-жёлтые редкие кустики, какое-то белёсое небо и неожиданно холодный и резкий, продувающий насквозь пальто, свитер, тело под пальто и свитером и летящий дальше ветер."
    "Шурик в компании нескольких военных стоит под навесом и смотрит на север, в сторону цепочки холмов, ограничивающих расстояние до горизонта парой километров."
    show dct_dream_sh_first_smoke 1 behind dct_dream_veil with dissolve
    "Что-то дымится на земле между холмами и наблюдателями."
    play sound_loop dct_sfx_UAZ_engine fadein 1
    "За спиной заводится мотор УАЗика, кто-то негромко переговаривается."
    show dct_dream_sh_first_smoke 2 with dissolve
    th "Я откуда-то знаю название: «полигон Иткуль». «Собачье озеро» — двойной обман. Ни собак, ни озера."
    show dct_dream_sh_first_smoke 3 with dissolve
    d_civ "Сейчас наша очередь."
    show dct_dream_sh_first_civilian behind dct_dream_veil at cright with dissolve
    "К Шурику обращается единственный, кроме него самого, гражданский в этой компании."
    d_civ "Вы готовы, Александр Александрович?"
    "Шурик только утвердительно кивает."
    show d_el delivery close behind dct_dream_veil:
        xcenter 0.1 ycenter 0.5
    with dissolve
    "И словно повинуясь этому кивку, откуда-то из-за спины, со стороны тарахтящего мотором Уазика в пустыню, в сторону холмов выходит Сыроежкин."
    show d_el delivery:
        xcenter 0.2 ycenter 0.5
    with dissolve
    "Несмотря на ледяной ветер, он в обычной пионерской форме."
    show d_el delivery far:
        xcenter 0.28 ycenter 0.5
    with dissolve
    "За спиной у Сыроежкина висит, как рюкзак на лямках, большой ящик, обтянутый зелёной тканью."
    stop music fadeout 2
    stop sound_loop fadeout 2
    show black:
        alpha 0
        linear 2 alpha 1
    th "Откуда здесь, наверху, миксы?"
    scene black
    
    play ambience ambience_int_cabin_day fadein 1.5
    el "Доброе утро, Шурик. Подъём был."
    show dct_int_house_of_el_day:
        blur 25
    show unblink
    sh "Доброе."
    show dct_int_house_of_el_day:
        blur 25
        pause 1
        linear 1 blur 0
    th "Так, очки."
    th "А что за странный сон?"
    th "Там всё выглядело так, будто и те люди, и то место мне давно знакомы."
    th "Может, сон о будущем? Теоретически, какая-то информация из будущего может просачиваться в наше время."
    th "А Сергей был в пионерской форме, потому что я ещё не представляю, каким он будет."
    th "И что за странное слово — микс?"
    $ renpy.music.set_volume(1.0, delay=0)
    stop ambience fadeout 1
    window hide
    hide dct_int_house_of_el_day with dissolve
    pause 0.5

    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_sl_day
    show black
    hide black with dissolve
    "Женя проснулась от голоса Мику."
    $ renpy.sound.set_volume(0.5)
    show mi grin pioneer far with dissolve
    play sound dct_sfx_horn_rise fadein 2
    mi "Женечка, ты слышишь, слышишь? Горн. Настоящий, а не запись! Вчера ко мне подошёл один мальчик и попросил послушать его, как он играет."
    show mi serious pioneer far with dissolve_fast
    mi "Ну вот… А потом мы пошли к Ольге Дмитриевне, и, в общем, у нас теперь в лагере есть свой горнист. Лучше бы он, конечно, играл на трубе или на саксофоне, мы тогда смогли бы с ним что-нибудь…"
    show mi serious pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    "Женя только вздохнула. Силы рычать и ругаться на соседку закончились ещё вчера."
    "Правда, и не хотелось ни рычать, ни ругаться на безобидного руководителя музыкального кружка."
    "Хотелось убежать."
    th "Надеюсь, она не станет записываться в библиотеку?"
    stop sound fadeout 1.5
    show mi upset pioneer far:
        alpha 0
        linear 1 alpha 1
    mi "… а здесь играет только Алиса, я видела у неё гитару. И ещё в кружке в журнале выдачи записано, что одна гитара на руках у физрука."
    show mi shy pioneer far with dissolve_fast
    mi "Как ты думаешь, Женечка, может, физрук тоже играет? Он славный дядька, было бы здорово, если бы он играл…"
    show mi shy pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    th "Я завидую Мику. Вчера только мельком познакомилась с человеком и уже знает, что тот славный дядька. А тут… Вот тот, Сыроежкин его фамилия, он какой? Он ведь действительно, наверное, просто не хотел меня будить."
    th "Эх, а он придёт, а я буду стесняться, и мне будет стыдно того, что я стесняюсь, и я опять начну на него кричать. Хоть бы помог кто. Подвёл бы его ко мне и сказал: „Женя, познакомься, это… Сергей“. Тогда я бы, может, так не стеснялась."
    show mi scared pioneer far:
        alpha 0
        linear 1 alpha 1
    mi "… а ещё этот, Сыроежкин Серёжа. Он ведь тоже играть умеет, на ксилофоне. У меня в кружке даже ксилофон есть, но Серёжа отказался почему-то, даже показалось, что убежал от меня. Неужели я такая страшная?.."
    show mi scared pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    th "А мне вот убежать некуда."
    th "Вот должна была Саша со мной жить, а Мику — с Леной, но Лена, наверное, в автобусе ещё с Сашей договорилась, и они с Мику поменялись."
    th "А я согласилась, я ещё не знала, что меня ждёт."
    show mi normal pioneer far:
        alpha 0
        linear 1 alpha 1
    pause 1
    mz "Мику, я умываться."
    show mi smile pioneer far with dissolve_fast
    mi "… Женечка, подожди, я тоже ещё не умывалась. А тут двое октябрят подходили, спрашивали про кружок, но я совсем не знаю, как с маленькими обходиться. Может быть, у тебя в библиотеке есть какие-нибудь методички? Я бы записалась…"
    th "Господи! Нет!"
    stop ambience fadeout 1
    $ renpy.sound.set_volume(1.0)
    show black with dissolve
    pause 2
    
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day
    show black
    hide black with dissolve
    window show
    "Столовая гудела пчелиным ульем."
    
    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show d_mt sad pioneer close orika as mt:
        xcenter 0.07
    show d_sf normal sport:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us normal sport:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_day_front
    with dissolve
    mt "В начале смены все они всегда рассаживаются по отрядам и по домикам."
    mt "Потом знакомятся, компании начинают перемешиваться, а потом они уезжают.{w} И вот так каждый цикл."
    mt "Хоть вы-то меня, надеюсь, поймёте."
    show d_sf smile sport with dspr
    me "Ты на этот раз осталась монитором, Оль?"
    show d_mt smile pioneer close orika as mt with dspr
    mt "Это временно, Семён. К линейке пройдёт. А пока нас никто не слышит, у меня получается."
    show d_mt normal pioneer close orika as mt with dspr
    mt "Надо кого-то в домик к Алисе подселять, Ульяна уже вряд ли назад вернётся."
    show d_us laugh sport with dspr
    us "А давайте Максима подселим?"
    show mt grin pioneer close
    show d_sf laugh sport
    show d_us smile sport
    with dissolve_fast
    us "Нет, на самом деле, из всего среднего отряда его первого можно в старший переводить. Одна эта его идея с горном чего стоит."
    show d_mt smile pioneer close orika as mt
    show d_sf smile sport
    with dissolve_fast
    mt "Смешно, Ульяна. И про Максима ты правильно говоришь. Но не могу же я мальчика к девочке селить. В общем, вы подумайте. И я подумаю."
    show d_mt normal pioneer close orika as mt
    show d_sf normal sport
    show d_us normal sport
    with dspr
    mt "И даже ментор, который сейчас проснётся, тоже подумает."
    show mt normal pioneer close with dissolve_fast
    "Ольга кивнула сама себе, и словно бы прозрачное забрало от этого движения опустилось на её лицо."
    "Вроде бы вот она, ничего не изменилось, а какие-то черты перестали различаться: где-то блик на забрале мешает детали разглядеть, а где-то царапины на прозрачном пластике."
    "И не видно ни тонкой игры разума, ни проблеска эмоций, ни глубины чувств. Так, обычная вожатка."
    show mt normal pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter -0.25
    pause 1.2
    show mt rage pioneer behind dct_int_dining_hall_table_day_chairs:
        xcenter -0.2 ycenter 0.29
        linear 0.6 xcenter 0.12
    pause 0.6
    mt "Внимание, пионеры! В одиннадцать ноль-ноль линейка, сбор на площади! Кто опоздает — тот первый в очереди на дежурство в столовой!"
    show mt normal pioneer with dissolve_fast:
        ycenter 0.32
    mt "Семён, Ульяна, особенно Семён. Надеюсь, смена обойдётся без ваших импровизаций. А то я не могу ни одну смену согласно Плану мероприятий провести."
    show mt normal pioneer:
        linear 2.5 xcenter 1.2
    pause 2.5
    me "Вот ведь — ментор-ментором, а помнит."
    show d_sf sad sport with dspr
    me "А я когда-то в первый раз сымпровизировал — всего лишь сбежал из лагеря на лодке, чтобы вырваться из этого бесконечного лета."
    me "И с тех пор только и делаю, что импровизирую, чтобы не провалиться в это лето обратно. Надоело до чёртиков, я же ленивый. Знал бы, что так будет — может, и не побежал бы никуда."
    show d_sf normal sport with dspr
    me "Но тогда тебя бы не встретил."
    me "Хотя нет. Тебя бы встретил."
    show d_sf smile sport
    show d_us smile sport
    with dspr
    me "Наш мирок слишком маленький для того, чтобы мы проскочили мимо друг друга."
    me "Пойдём, Рыжик, на площадь."
    stop ambience fadeout 1
    window hide
    show black with dissolve
    pause 0.5
    
    play ambience ambience_dining_hall_full fadein 1
    scene dct_int_dining_hall_table_day_back
    show dct_int_dining_hall_table_day_chairs
    show el normal pioneer close:
        xcenter 0.41 ycenter 0.47
    show sh serious pioneer close:
        xcenter 0.74 ycenter 0.47
    show dct_int_dining_hall_table_day_front
    show black
    hide black with dissolve
    window show
    el "Шурик, нам нужен для начала план. Чем мы будем заниматься в кружке?"
    show sh surprise pioneer close with dspr
    sh "План.{w=0.5} Да-да."
    show sh normal pioneer close with dspr
    extend " А чем же мы будем заниматься?"
    show sh serious pioneer close with dissolve_fast
    sh "Сергей, прости, я, кажется, задумался и отключился. А нам и правда нужно составить план занятий. И вожатая о чём-то таком говорила."
    sh "У тебя есть какие-то идеи?"
    show d_el think2 pioneer close as el with dspr
    "Электроник задумался."
    "Планы всегда были в компетенции Шурика, и сейчас Шурик должен был предложить построить робота, но после создания Яны роботостроительство в этом лагере постепенно сошло на нет."
    stop ambience fadeout 1
    play sound_loop ambience_clubs_inside_day fadein 1
    show cg d5_clubs_robot with squares
    "И с каждым циклом начатый вместо убежавшей Яны и частично даже функционирующий робот становился всё менее и менее близок к завершению."
    "Шурик проверял на нём какие-то свои идеи, часть деталей перекочёвывали, с подачи Алисы, из робота в музыкальную аппаратуру или дискотечный усилитель."
    show dct_disassembled_catrobot as cg with squares
    "И сейчас от робота оставалось безголовое туловище об одной руке и двух ногах, которое при подаче питания начинало хаотически шевелить конечностями."
    stop sound_loop fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    hide cg
    show el serious pioneer close
    with squares
    el "Ну... Можно было бы робота достроить. Я в кружке видел туловище безголовое — видимо, прошлая смена не доделала."
    sh "Робота достроить...{w} Знаешь, Сергей, мне нужно подумать над этим. Ты, сходи, пожалуйста, на линейку один. У меня, кажется, родилась идея, которую нужно срочно обдумать. Если что, я буду в кружке."
    show el laugh pioneer close with dspr
    el "Конечно, Шурик. Не беспокойся, я тебя от вожатой прикрою!"
    window hide
    show black with dissolve
    stop ambience fadeout 1
    pause 2
    
    play ambience ambience_camp_center_day fadein 1    
    play music music_list['i_want_to_play'] fadein 1
    scene bg ext_square_day
    show black
    hide black with dissolve    
    show dv normal pioneer far behind el:
        xcenter 0.2 alpha 0.0
        pause 0.3
        linear 0.5 alpha 1.0
    show d_ma normal pioneer:
        zoom .75 xcenter 0.4 yalign 1.01 alpha 0
        pause 0.3
        linear 0.5 alpha 1.0
    window show
    dv "В общем, так: ты теперь первый кандидат в старший отряд."
    dv "Лет тебе не меньше, чем было Ульяне, так что всё нормально."
    show dv grin pioneer far with dissolve_fast
    dv "Мы тебя ещё пронаблюдаем, а в субботу на сборе отряда решим положительно."
    dv "С Женей и кибернетиками, я думаю, проблем не будет, заместитель вожатой — за, вожатую убедим. Если отряд будет за, то в понедельник объявим на линейке о переводе."
    show dv normal pioneer far with dissolve_fast
    dv "А где жить тебе — это будем думать. Наверное, можешь и по-прежнему, с Витькой в домике. Хотя и положено старших со старшими селить, но…"
    show d_sf smile sport:
        xzoom -0.75 yzoom 0.75 xcenter 0.8 ycenter 0.56 alpha 0.0
        pause 0.3
        linear 0.5 alpha 1.0  
    me "Сам понимаешь, соседство с Алисой тебя до добра не доведёт. Она тебя плохому научит."
    show d_ma laugh
    with dspr
    show dv angry pioneer far with dissolve_fast
    dv "Сенька, придушу!"
    show d_ma smile
    show dv smile pioneer far
    with dissolve_fast
    dv "Имей в виду, Сенька он только для меня. И ещё два человека могут так его назвать без риска для здоровья и жизни."
    show d_ma serious
    show dv laugh pioneer far
    with dspr
    dv "Когда будешь с ним знаком столько же, сколько мы, тогда и ты сможешь рискнуть."
    stop ambience fadeout 1
    show black with dissolve
    hide d_ma
    hide d_sf
    hide dv
    
    play ambience ambience_camp_center_day fadein 1
    hide black with dissolve
    "Площадь постепенно заполнялась пионерами."
    show mt smile panama pioneer close with dissolve2
    mt "Лагерь, на линейку — становись!"
    "Электроник поколебался несколько секунд, решая, где ему встать: так, чтобы ему было удобнее самому смотреть на Женю, или чтобы Жене было удобнее видеть его, и встал в первой шеренге, рассудив, что сейчас важнее самому понравиться девушке."
    scene dct_lineup_two_lines with dissolve
    "А Женя всю линейку поглядывала в сторону нестриженого затылка Электроника и злилась:{w} на себя — за то, что так и не решилась извиниться за скандал в автобусе;{w} на Электроника — за то, что тот сам до сих пор не подошёл к ней;{w} на окружающих — за то, что никто ещё не догадался познакомить её с кибернетиком."
    mz "\~ Да хоть бы просто поговорить подошёл. Хоть спросил бы о том, когда библиотека открывается. \~"
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    scene black with dissolve
    pause 2
    
    play ambience ambience_library_day fadein 1
    play music music_list['your_bright_side'] fadein 2
    scene bg int_library_day with squares
    show d_mz angry glasses pioneer at center
    with dissolve
    window auto
    "Женя сидела в библиотеке и рычала на пионеров."
    hide d_mz with dissolve
    "Вообще-то в библиотеке должно быть тихо, а в библиотеке небольшого пионерского лагеря — ещё и безлюдно."
    "Именно ради того, чтобы поменьше общаться с другими людьми, Женя и попросилась в день приезда заведовать библиотекой."
    show d_mz sad pioneer glasses close at fleft with dissolve
    "Но сегодня был день особенный."
    
    scene bg int_library_day:
        zoom 1.5 xalign 1.0 ycenter 0.5
    show d_mz confused glasses pioneer far at cright
    with dissolve
    "Сегодня всему лагерю нужны были подписи в обходных листах. Всем шестидесяти с лишним пионерам."
    "И все они решили собрать эти подписи ещё до обеда, чтобы после обеда бездельничать с чистой совестью."
    
    scene bg int_library_day:
        zoom 1.5 xalign 0.0 ycenter 0.5
    show d_mz rage glasses pioneer at left
    with dissolve
    "Пионеры толкались перед столом, шумели, разбредались по залу, играли в прятки и догонялки, их нужно было контролировать, чтобы кто-то не опрокинул стенд, кто-то не утащил понравившийся журнал, не перепутал книги на стеллажах."
    
    scene int_library_day:
        zoom 1.25 xalign 0.0 ycenter 0.6
    show d_mz normal glasses pioneer close:
        xcenter 0.5 ycenter 0.53
    with dissolve
    th "Ушли. Всё на сегодня? Больше ни с кем общаться не придётся?"
    th "Шестьдесят человек за два часа. Как я никого не покусала ещё?"
    th "Но, кажется, больше никого не будет. Можно наводить порядок после прохода Орды. Всё поправить, расставить по местам, пол помыть. Вот с пола мы и начнём."
    play sound sfx_knock_door7_polite
    pause 1
    play sound sfx_door_squeak_light
    show d_mz bukal glasses pioneer close with dspr
    th "Та-а-ак!"
    show d_mz angry glasses pioneer close with dspr
    mz "Ну кого ещё с-силы небесные принесли?!"
    
    scene bg int_library_day
    show dct_int_library_day_el
    show d_mz_back2_pioneer:
        xcenter 0.4
    with dissolve
    "У дверей, на расстеленной и безжалостно затоптанной сегодняшней толпой пионеров половой тряпке робко переминался Сыроежкин."
    th "Ой. Неудобно-то как."
    scene dct_int_mirror_in_library
    show d_mz in_mirror shyangry_glare glasses at center:
        xzoom -1.0
    with squares
    "Женя кинула быстрый взгляд в зеркало."
    th "Накричала. Выражение лица «Всех ненавижу!». Лохматая, вихор этот чёртов! Очки на нос сбились! Лицо раскраснелось, рубашка выбилась из-под пояса, один гольф сполз до половины и — стыдоба какая! — перекрученная юбка!"
    th "Лучше бы кто-то другой пришёл."
    
    scene dct_int_library_standing_desk_back
    show el sad pioneer:
        xcenter 0.5 ycenter 0.46
    show dct_int_library_standing_desk_front
    with squares
    th "Так, быстро за стол, пока он не разглядел во всех подробностях такое позорище!"
    el "Я… вот, обходные."
    mz "Записываться будешь?"
    th "Господи, ну почему он пришёл сейчас? Я же не хочу его выгонять, но… Эх."
    show el normal pioneer 
    el "Д-да."
    mz "Заполняй! Фамилия, имя, возраст, отряд. Внизу распишись…"
    mz "… сейчас брать книги будешь?"
    "Сыроежкин протянул Жене через барьер обходные, формуляр и ручку."
    $ renpy.music.set_volume(0.0, delay=7)  # Глушим музыку, но не отключаем
    "На секунду их пальцы соприкоснулись, и оба синхронно отдёрнули руки."
    show d_el shy3 pioneer as el with dissolve_fast
    el "Д-да. Мне ч-что-нибудь по те-телемеханике."
    mz "Здесь нет такого, это не университет, а пионерский лагерь!"
    show d_el smile2 pioneer as el with dspr
    el "Ж-жаль. Т-тогда я п-пойду?"
    "Бедный Сыроежкин совсем стушевался."
    $ renpy.sound.set_volume(0.15)
    play sound dct_sfx_horn_dinner
    show el normal pioneer with dissolve_fast
    "Спас его горнист, подавший сигнал к обеду."
    show el normal pioneer:
        ease 1.6 xcenter 0.2
    mz "Подожди. Спроси своего друга, он будет записываться?"
    show el smile pioneer with dspr
    extend " И приходи после обеда — посмотрим, что есть в фондах."
    $ renpy.sound.set_volume(1.0)
    play sound sfx_close_door_1
    hide el with dissolve
    $ renpy.music.set_volume(1.0, delay=2)  # Возвращаем музыку обратно
    th "Ну почему? Почему я такая дура? Почему я даже нормально поговорить с человеком не могу? Сразу начинаю ругаться."
    th "Но этот-то тоже хорош."
    extend " Стоял и пялился."
    extend " На что?"
    
    scene dct_int_mirror_in_library
    show d_mz in_mirror shyangry glasses at center:
        xzoom -1.0
    with squares
    "Женя поправила злополучную юбку, натянула сползшие гольфы, заправила рубашку и завязала по-новой галстук."
    show d_mz smile2 glasses pioneer with dspr
    "Некоторое время боролась с торчащим вихром, потом обречённо махнула на него рукой."
    show d_mz sceptic glasses pioneer with dissolve_fast
    "Расправила плечи и распрямилась, посмотрела на своё отражение."
    show d_mz sad glasses pioneer at center with dissolve:
        xzoom -1.0
    mz "Поздравляю вас, Евгения: вы страшная, никому не интересная и не нужная."
    mz "И сидеть вам в библиотеке до самой старости, потому что никому вы не нужны."
    show d_mz bukal glasses pioneer with dspr
    mz "Ну значит, и вам никто не нужен. Значит, мы с вами обойдёмся!"
    show d_mz amazed glasses pioneer with dspr
    "Показалось, что в конце этого монолога кто-то хихикнул под самым окном."
    hide d_mz with dissolve
    "Женя бросилась к окну и выглянула наружу — никого."
    "Кусты через дорогу подозрительно качались, но добежать туда «шпион» не успел бы."
    
    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
    th "Он обходные забыл. Вернётся — отдам."
    th "Придётся мыть пол вместо обеда. А то после обеда Сергей придёт, а у меня грязно как в подземном переходе. Если придёт после всего."
    window hide
    stop music fadeout 1.5
    show black with dissolve
    pause 2

    play ambience ambience_dining_hall_full fadein 1
    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show d_sf normal pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show mt normal pioneer close:
        xcenter 0.74
    show dct_int_dining_hall_table_day_front
    with dissolve
    window auto
    mt "Семён, что ты думаешь о Максиме? О том, чтобы перевести его в старший отряд?"
    "Вопрос был задан, будто и не было утреннего разговора.{w} Впрочем, с точки зрения ментора, разговора действительно не было."
    mt "Алиса предложила его кандидатуру, и я склонна согласиться."
    me "Я за."
    "Семён утвердительно кивнул, попробовал борщ и поморщился."
    show d_sf serious pioneer with dspr
    "Всё-таки после ухода бабы Глаши качество блюд в ресторане «Совёнок» упало на одну ступень."
    show d_sf normal pioneer with dspr
    me "Осталось два вопроса: где селить Максима и кого из малышей переводить в средний отряд."
    show mt sad pioneer close with dspr
    "Ольга тоже поморщилась, попробовав борщ."
    show mt normal pioneer close with dspr
    mt "С Максимом я что-нибудь придумаю, а вот кандидатуру из малышей ищи сам. Ты с ними больше моего общаешься."
    mt "И вот ещё что…{w} Хотя нет, это я сама."
    show mt normal pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.9 xcenter 1.25
    "Взяв стакан чая, вожатая подсела за столик к кибернетикам."
    
    scene bg int_dining_hall_people_day with dissolve
    "А Семён отнёс посуду на мойку, покрутил головой и, не обнаружив Ульяны, пошёл к себе."
    stop ambience fadeout 1
    play sound_loop ambience_camp_center_day fadein 1
    scene dct_ext_сentral_alley_from_dining_hall_to_west with slideawayleft:
        walking
    "Действительно, нужно было решить, кого из мелких перевести в средний отряд на освобождающееся место Максима, а для этого нужно было посоветоваться с теми мелкими, которые не спят."
    "В отличие от старшего и младшего отрядов, средний, пионеры в котором не просыпались никогда, права голоса здесь не имел."
    stop sound_loop fadeout 1
    # play ambience ambience_soccer_play_background fadein 1
    play music music_list['farewell_to_the_past_full'] fadein 2
    
    scene bg ext_playground_day with irisout
    show d_oz n pioneer:
        xcenter 0.48 yalign 0.27
    show d_sz normal pioneer:
        xcenter 0.66 yalign 0.27
    show d_ge:
        zoom 0.88 xcenter 0.82 yalign 1.01
    show d_gr:
        zoom 0.87 xcenter 0.35 yalign 1.0
    show d_va normal:
        zoom 0.93 xcenter 0.21 yalign 0.46
    with dissolve
    "В итоге, когда после первой в смене тренировки пятеро мелких: Вася, Гриша, Оксана и Сергей Зайцевы и Геля, устроившись на футбольной трибуне, выбрали Васю, Семён огорчился."
    "Он ждал именно этого результата, но всё равно огорчился. Вот так — прощай, Вася."
    "Через неделю вожатая объявит о переводе, ещё неделю ребята отгуляют в своих отрядах, а на следующий цикл уже приедут в новом качестве."
    "И не спящий сейчас, Васька будет неизвестно сколько жить двухнедельными циклами, пока не перейдёт в старший отряд, и ещё неизвестно сколько в нём, пока не проснётся."
    show d_va upset:
        linear 2 zoom 0.837 xcenter 0.55 yalign 0.61
    show d_gr:
        linear 2.1 xcenter 0.855
    show d_oz d pioneer:
        linear 1.2 zoom 0.9 xcenter 0.64
    show d_sz normal pioneer:
        linear 1.2 xcenter 0.75
    show d_ge:
        linear 1.2 xcenter 0.93
    "Семён мысленно поздравил Максима, у которого появились шансы, и грустно посмотрел на Ваську.{w} И на Оксану, взявшую Васю за руку, тоже."
    th "Их обоих бы передвинуть"
    extend ", нет — троих, ещё и брата её."
    "Но место в среднем отряде освобождалось только одно."
    th "Я всегда только уходил. А вот теперь провожаю сам. И не знаю, когда увидимся."
    th "То есть знаю, что никогда. Потому что когда Васька проснётся снова, это будет уже другой человек."
    "Октябрята отошли на несколько шагов и о чём-то разговаривали вполголоса."
    show d_va serious:
        linear 1.6 zoom 1.16 xcenter 0.3 yalign 0.43
    show d_oz smile pioneer:
        linear 0.9 zoom 1.0 xcenter 0.73
    show d_sz normal pioneer:
        pause 0.3
        linear 0.6 xcenter 0.62
    extend " Потом Вася вернулся."
    d_va "У меня ещё две недели здесь."
    d_va "Я пока буду прощаться, а потом, Семён, до конца смены поможешь мне с лодкой?"
    show d_va sad with dspr
    d_va "Я сам не успею, а очень хочу пройти под парусом."
    me "Обязательно. Как Второй приедет и всё устаканится, так и сделаем."
    "Семён неумело и неловко прижал Ваську за плечо к себе, а Васька, также стесняясь, ткнулся головой ему в бок."
    show d_va shy with dspr
    me "Не жалеешь, что уходишь?"
    show d_va sad with dspr
    d_va "Жалею.{w=0.8} Но, Семён.{w=0.5} Мы никогда об этом тебе не говорили, но мы все очень-очень хотим вырасти."
    d_va "А вырасти можно только так."
    d_va "И все ребята ещё утром сказали, что я должен вырасти первым."
    window hide
    # stop ambience fadeout 1
    stop music fadeout 1.5
    show black with dissolve
    pause 2
    
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_clubs_male_day
    show sh serious pioneer close:
        xcenter 0.72 ycenter 0.70
    show black
    hide black with dissolve
    window auto
    "Шурик сидел за столом перед горкой радиодеталей, высыпанных из фанерного ящика, и выбирал необходимые, сверяясь с наскоро нарисованной схемой."
    "Плата, прорисованная нитрокраской на фольгированном гетинаксе, уже лежала в фотокювете, залитая раствором."
    "Простая и понятная работа нравилась хотя бы тем, что отвлекала от ненужных мыслей и непонятных, всплывающих перед глазами образов незнакомых людей."
    "Монолог Сыроежкина о перспективах робототехники работал бы не хуже, но Сергея пришлось отпустить."
    show sh normal pioneer close with dspr
    "Шурик пожал плечами. В конце концов, любой человек имеет право на личную жизнь."
    window show
    dreamgirl "Даже лаборант-микс?"
    show sh serious pioneer close with dspr
    sh "Любой."
    show sh scared pioneer close with dissolve_fast
    sh "Эй, ты кто такой?" with vpunch
    window auto
    "Тишина."
    show sh upset pioneer close with dspr
    th "Плохо. Сам с собой разговариваю. Не мысленно комментирую свои действия, а именно разговариваю. Очень плохо."
    "Шурик даже вздрогнул и бросил найденный транзистор обратно в горку деталей, вместо того чтобы присоединить его к уже отобранным."
    stop ambience fadeout 1
    show black with dissolve
    show sh serious pioneer close
    play sound_loop ambience_int_cabin_day fadein 1
    hide black with dissolve
    "Наконец всё, что требовалось, было найдено и отложено. Невостребованные детали перекочевали обратно в ящик, который занял своё прежнее место под одним из верстаков."
    show sh normal pioneer close with dspr
    "Шурик ещё раз сверился со схемой, кивнул сам себе, посмотрел, как травится плата, посмотрел на часы."
    show sh serious pioneer close with dspr
    th "Плохо, что нет ни азотки, ни хлорного железа. В медном купоросе плата травиться будет ещё часа три-четыре."
    stop sound_loop fadeout 1
    window hide

    play ambience ambience_dining_hall_full fadein 1
    play music music_list['everyday_theme'] fadein 3
    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show d_el smile2 pioneer close as el:
        xcenter 0.41 ycenter 0.47
    show sh normal pioneer close:
        xcenter 0.74 ycenter 0.47
    show dct_int_dining_hall_table_day_front
    with blinds
    show mt normal pioneer close behind dct_int_dining_hall_table_day_front:
        xcenter -0.25 ycenter 0.23
        linear 0.6 xcenter 0.07
        linear 0.5 ycenter 0.5
    pause 1.1
    window auto
    mt "Ну как вам наш горнист?"
    show mt smile pioneer close with dspr
    mt "Нигде в лагерях горнистов уже не осталось. Везде плёнки или пластинки крутят, а мы вот взяли и возродили традицию! Правда мы молодцы?"
    show sh surprise pioneer close with dspr
    sh "Горнист?"
    show sh normal pioneer close with dspr
    sh "Извините, Ольга Дмитриевна, не расслышал."
    show el normal pioneer close with dspr
    el "Да и правда, слышно было плохо. Зачем сейчас, в эпоху электроники, нужны горнисты?"
    show mt normal pioneer close
    show sh serious pioneer close
    with dspr
    el "Вот он подаёт сигнал с площади, а уже у клубов его плохо слышно, а на концертной площадке или на стадионе не слышно вовсе."
    el "Ведь запись хорошо слышно из всех динамиков, а горниста — только на площади."
    show mt smile pioneer close with dspr
    mt "Вот об этом я и хотела с вами поговорить."
    mt "Ваш кружок — он официально называется «Кружок кибернетики, робототехники и радиоэлектроники», я правильно помню?"
    show sh normal pioneer close with dspr
    show mt normal pioneer close with dspr
    mt "… В общем, задание вашему кружку. Сделать так, чтобы, начиная с завтрашнего утра, сигналы горниста были слышны изо всех динамиков по всему лагерю. Усилитель вы знаете где, что ещё нужно спаять — разберётесь."
    show el surprise pioneer close with dissolve_fast
    el "Но Ольга Дмитриевна… У нас же программа, у нас же робот…"
    show el sad pioneer close with dspr
    show mt smile pioneer close with dspr
    mt "Вот наладите трансляцию, и занимайтесь вашим роботом сколько душе угодно."
    show mt smile pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter -0.25
    "Вожатая встала из-за стола, поставив точку в разговоре."
    show sh normal_smile pioneer close with dissolve_fast
    sh "Ну что, пойдём посмотрим, что можно сделать."
    scene bg int_dining_hall_people_day with dissolve
    "Кибернетики отнесли грязную посуду на мойку и покинули столовую."
    stop ambience fadeout 2
    stop music fadeout 1
    
    play sound_loop ambience_camp_center_day fadein 1
    scene bg ext_square_day
    show el serious pioneer:
        xcenter 1.42
        easein 3 xcenter 0.42
    show sh serious pioneer:
        xcenter 1.72
        easein 3 xcenter 0.72
    with slideawayright
    "По дороге в кружок Сыроежкин то и дело останавливался и оглядывался куда-то через правое плечо."
    show el normal pioneer with dissolve_fast
    show sh normal pioneer with dspr
    sh "Тебя что-то беспокоит?"
    el "Да понимаешь, я в библиотеке не успел подписать наши обходные, как раз на обед просигналили. И заведующая библиотекой сказала, что будет ждать после обеда."
    show d_el shy3 pioneer as el with dspr
    el "А Женя — она такая строгая, я не хочу, чтобы она ругалась потом, если я не приду. И вожатой обходные без её подписи не отдашь."
    sh "Ладно уж, иди. Со схемой я сам управлюсь."
    show el smile pioneer with dspr
    sh "После ужина корпус делать будем, тогда приходи."
    el "Спасибо, Шурик. Я обязательно буду."
    window hide
    show sh serious pioneer:
        easeout 2.5 xcenter -0.5
    show 3500_el smile pioneer as el:
        anchor(0.5, 0.5) pos(0.42, 0.833)
        easein 4 zoom 0.15 pos(0.68, 0.65) knot(0.52, 0.66) #knot - это точка для скривления траектории (работает как вершина у сплайна), и требует, чтобы в предыдущей строчке тоже была чётко указана позиция, и обязательно через pos (и при необходиости anchor, если раньше не привязались), но никак не через xcenter и ycenter или xalign и yalign 
    pause 2.8
    stop sound_loop fadeout 3
    show black with dissolve
    pause 2
    
    # play ambience ambience_camp_center_day fadein 1
    play music music_list['get_to_know_me_better']  fadein 1
    scene bg ext_square_day
    show dv grin pioneer:
        xcenter 0.32
    show d_ma normal pioneer:
        xcenter 0.61 yalign 0.02
    show black
    hide black with dissolve
    window auto
    "Максим шагал рядом с Алисой, иногда искоса посматривая на неё."
    play ambience ambience_camp_center_day fadein 1.5
    
    scene bg ext_dining_hall_near_day
    show dv smile pioneer:
        xcenter 0.42 alpha 0
        pause 1.5
        linear 1 alpha 1
    show d_ma normal pioneer:
        xcenter 1.25 yalign 0.02
        pause 0.7
        easein 2 xcenter 0.7
    with blinds
    "Перед самым обедом та поймала его в дверях столовой и не терпящим возражений тоном скомандовала:"
    show dv normal pioneer with dspr
    dv "Слушай сюда, горнист. После обеда не убегай, инструктировать тебя буду."
    stop music fadeout 2
    
    scene dct_ext_dining_bench_day
    show d_ma normal pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    with blinds
    # "И вот «после обеда» наступило, Максим дожидался Алису, сидя на лавочке У КРЫЛЬЦА СТОЛОВОЙ и отклоняя приглашения пойти на пляж, на стадион, погулять, поиграть в карты…"   # По канону
    "И вот «после обеда» наступило, Максим дожидался Алису, сидя на лавочке у входа в столовую и отклоняя приглашения пойти на пляж, на стадион, погулять, поиграть в карты…"
    show d_ka normal pioneer with dissolve:
        zoom 1.1 xcenter 1.2 ycenter 0.87
        easein 1.5 xcenter 0.6
    pause 1.2
    show d_ka normal pioneer with dissolve_fast:
        zoom 0.935 xcenter 0.6 ycenter 0.97
    "Катя вышла из столовой и присела рядом."
    show d_ma shy pioneer with dspr
    "У Максима вздрогнуло сердце."
    show d_ma normal
    show d_ka smile pioneer
    with dspr
    d_ka "У тебя здорово получается. Ты долго учился?"
    show d_ma smile pioneer with dspr
    d_ma "Нет, мне только Мику показала чуть-чуть, а дальше само получилось."
    d_ka "Это значит, что у тебя талант."
    show d_ma shy pioneer with dspr
    d_ka "А я вот сколько на гитаре ни учусь — не получается. Как ты думаешь, может, у меня на горне получится?"
    play music music_list['that_s_our_madhouse'] fadein 2
    scene dct_ext_dining_door_day with dissolve_fast:
        anchor(0.52, 0.51) pos(0.5, 0.5)
    show dv grin pioneer at cright with dissolve_fast
    dv "Катерина, это место занято!"
    
    scene dct_ext_dining_bench_day
    show d_ma normal pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    show d_ka surprise pioneer:
        zoom 0.935 xcenter 0.6 ycenter 0.97
    show dv grin pioneer close:
        xcenter 0.88
    with dissolve_fast
    "Двусмысленная фраза оказалась понята даже более красноречиво, чем была высказана."
    show d_ka angry pioneer with dissolve_fast:
        zoom 1.1 xcenter 0.6 ycenter 0.87
    "Катя поднялась, сверкнула глазами в сторону Алисы, посмотрела на Максима, словно ждала от него какой-то реакции."
    show d_ka angry pioneer with Dissolve(0.0):
        easeout 1.5 xcenter 1.2
    show d_ma surprise
    show dv surprise pioneer close
    with dissolve_fast
    pause 0.1
    show dct_ext_dining_door_day:
        anchor(0.52, 0.51) pos(0.5, 0.5) alpha 0
        pause 0.5
        linear 0.5 alpha 1
    show d_ka normal pioneer as d_ka2:
        zoom 0.75 xcenter 0.45 ycenter 0.7 alpha 0
        pause 0.5
        linear 0.2 alpha 0.4
        linear 0.3 xcenter 0.37 alpha 1
        linear 0.6 xcenter 0.08 ycenter 0.9
        linear 0.6 xcenter -0.21
    show dct_ext_dining_door_day_front:
        anchor(0.52, 0.51) pos(0.5, 0.5) alpha 0
        pause 0.5
        linear 0.5 alpha 1
    show dv surprise pioneer at cright as dv2:
        alpha 0
        pause 0.5
        linear 0.5 alpha 1
    with dissolve_fast
    "Не дождалась, гордо вскинула голову, развернулась на каблуках и так, с гордо вскинутой головой, и удалилась."
    show dv guilty pioneer as dv2 with dissolve_fast
    th "Вот чёрт, я не хотела."
    show dv grin pioneer as dv2 with dissolve_fast
    th "Хотя перебьётся Катька, от неё и так мальчики не отходят."
    stop music fadeout 1.5
    
    scene dct_ext_dining_bench_day
    show d_ka angry pioneer:
        zoom 0.2 xcenter 0.575 ycenter 0.68
        pause 0.2
        linear 1.0 xcenter 0.7
    show dct_ext_dining_bench_day_front
    show d_ma surprise pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    show dv grin pioneer close:
        xcenter 0.88
    with dissolve_fast
    "А Максим... Он просто ничего не понял."
    stop ambience fadeout 3

    play music "<from 14.5 loop 0.0>sound/music/get_to_know_me_better.ogg" fadein 1.5
    scene bg ext_house_of_dv_day
    show dv grin pioneer far:
        xcenter 1.27
        easein 3 xcenter 0.57
    show d_ma normal pioneer:
        zoom 0.75 xcenter 1.5 yalign 1.01
        easein 3 xcenter 0.8
    with blinds
    "До домика Алисы шли молча, только зашли к Максиму за горном, благо было по пути."
    show dv laugh pioneer far at center with dissolve_fast
    dv "Заходи, можешь не разуваться."
    
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_dv_day
    with slidedown
    show dv laugh pioneer at cleft
    show d_ma normal pioneer at cright:
        xcenter 0.65 yalign 0.02
    with dissolve
    pause .5
    show dv guilty pioneer with dissolve
    "Алиса вздохнула, глянув на пустующую Ульянкину кровать, махнула на неё рукой — садись, мол. А сама полезла искать что-то по шкафам и тумбочкам."
    hide dv with dissolve
    "Максим разглядывал домик «страшной ДваЧе» с огромным любопытством, и, кажется, увиденное ему нравилось."
    show d_ma smile2 pioneer with dissolve_fast
    "Никогда раньше он здесь не был, вообще весь средний отряд с самого первого дня знал, что с Рыжими связываться опасно, и потому избегал их внимания."
    show d_ma smile pioneer with dissolve_fast
    "А тут сразу вспомнился беспорядок в его собственном жилище."
    show dv normal pioneer behind d_ma at cleft with dissolve 
    "Наконец Алиса нашла, что хотела: тетрадный листок с расписанием сигналов и кассету с записью горна."
    show d_ma normal pioneer with dissolve_fast
    dv "Вот, держи. Будешь играть по этому расписанию. Часы есть?"
    d_ma "Есть."
    dv "Хорошо, тогда первый пункт закрыли. Если проспишь — накажу."
    show d_ma serious pioneer with dissolve_fast
    dv "Сейчас пойдёшь в музыкальный кружок, там прослушаете с Мику запись, потом ты ей сыграешь. Если что, она подскажет, что и как."
    dv "А то к духовым инструментам, кроме неё, здесь никто и никак. В общем, сделаешь так, как она скажет."
    dv "И третье: вожатая согласна на твой перевод в старший отряд. Через неделю на линейке объявит, если ничего не изменится."
    dv "Но не думай, что у тебя какие-то права появятся после этого. Обязанности уже появились, а права ещё нет."
    show d_ma surprise pioneer with dissolve_fast
    dv "Следующую неделю будешь ещё числиться в среднем отряде, а в старшем — только кандидатом."
    dv "Жить будешь на старом месте, а на линейке и в столовой со следующей недели будешь со старшим отрядом."
    show dv smile pioneer with dspr
    dv "Короче, прав будет как у маленьких, а бить будем как взрослого."
    dv "А уж в следующую смену — добро пожаловать. Вопросы есть?"
    show d_ma normal pioneer with dissolve_fast
    pause 1
    d_ma "Тётя Алиса, а когда ты начнёшь меня учить плохому?"
    show dv surprise pioneer with dissolve_fast
    show d_ma smile2 pioneer with dspr
    show dv angry pioneer with dissolve_fast
    show d_ma laugh pioneer with dspr
    show d_ma laugh pioneer:
        linear 0.25 zoom 1.1 xcenter 0.7
        linear 0.25 zoom 1.25 xcenter 0.75 alpha 0
    show dv angry pioneer:
        linear 0.5 zoom 1.1 xcenter 0.5
    pause 0.8
    play sound sfx_close_door_1
    pause 0.2
    show dv laugh pioneer with dissolve_fast
    "Подзатыльник своей цели так и не достиг, но Алису это нисколечко не заботило. Она вернулась на кровать, откинулась на спину, на подушку, и беззвучно расхохоталась. Кажется, серая полоса в жизни заканчивалась."
    # stop ambience fadeout 1
    stop music fadeout 1.5
    window hide
    show black with dissolve
    pause 2
    
    play sound sfx_knock_door7_polite
    play music music_list['your_bright_side'] fadein 2.5
    scene black
    show dct_int_library_standing_desk_back:
        zoom 1.4 xcenter 0.3 ycenter 0.1  rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show dct_int_library_standing_desk_front:
        zoom 1.4 xcenter 0.3 ycenter 0.1 rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show dct_library_door_window_el:
        zoom 1.4 xcenter 0.3 ycenter 0.1 rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show unblink
    pause 1
    mz "Не заперто!"
    
    show dct_library_door_window_el:
        alpha 1
        pause 1
        alpha 0
    show el sad pioneer behind dct_int_library_standing_desk_front:
        xcenter 0.2 ycenter 0.46 alpha 0
        pause 1
        alpha 1
    show blinking
    pause 1
    play sound sfx_door_squeak_light
    pause 1.2
    el "З-з-з-дравствуй, это оп-пять я.{w} За об-бходным."
    mz "Ну заходи."
    show el sad pioneer:
        easein 0.6 xcenter 0.35
    pause 0.4
    show el surprise pioneer behind dct_int_library_standing_desk_front as el2:
        xcenter 0.35 ycenter 0.46 alpha 0
        pause 0.2
        linear 0.2 alpha 1
    mz "Стой!"
    mz "Ноги вытирай!{w=0.8} Забирай обходные."
    hide el
    show d_el smile2 pioneer as el2 with dissolve_fast
    el "Спасибо. Я пойду?"
    mz "А книги будешь брать?"
    show d_el shy pioneer as el2 with dspr
    show d_el shy pioneer as el2:
        ease 0.9 xcenter 0.2
    el "Я завтра, можно?"
    stop music fadeout 1.5
    
    play ambience ambience_forest_day fadein 1
    scene bg ext_path2_day with slideawayright:
        walking
    th "Ну вот, опять не решился заговорить с девушкой."
    th "Неудивительно, что она на меня рычит."
    th "Она думает, что я в автобусе к ней специально приставал; может, думает, что я и в библиотеку хожу, чтобы издеваться над ней?"
    th "Может, над ней все смеются?"
    
    scene bg ext_path2_day
    "Что-то толкнулось в ноги."
    stop ambience fadeout 1.5
    play music music_list['always_ready'] fadein 1.5
    show dct_cg_foots_and_ball with pushup
    "Электроник опустил глаза — мячик."
    "Незаметно для себя он вышел к западному краю футбольного поля."
    
    scene bg ext_playground_day with pushdown
    d_guys "Сыроежкин!{w=0.5} Пни мячик!"
    show dct_cg_el_kick_ball with squares
    pause 0.5
    $ renpy.sound.set_volume(1.5, delay=0)
    play sound sfx_soccer_ball_kick
    pause 0.2
    hide dct_cg_el_kick_ball with squares
    $ renpy.sound.set_volume(1.0, delay=0)
    d_guys "Эй, давай с нами!"
    
    scene bg ext_playground_day
    show el normal pioneer
    with dissolve
    th "А почему нет?"
    show d_el grin shorts at center:
        alpha 0
        pause 2
        alpha 1
    show el normal pioneer:
        alpha 1
        pause 2
        alpha 0
    show cg d4_el_wash:
        alpha 0
        linear 1 alpha 1
        pause 1
        linear 1 alpha 0
    th "Женя выгнала, Шурик ждёт меня только вечером. И пионер должен развивать не только мозг, но и тело."
    hide cg d4_el_wash
    hide el
    show d_el grin shorts:
        alpha 1
        linear 0.9 xcenter 0.86
    pause 0.4
    hide d_el with dissolve_fast
    play ambience ambience_soccer_play_background fadein 2
    pause 0.2
    show dct_el_running_back_and_forth
    "Игра помогла хотя бы тем, что отодвинулись назад грустные мысли. Некогда было думать о Жене — если уж взялся играть, то надо было играть в полную силу. И, конечно, не замыкаться в своих переживаниях."
    stop ambience fadeout 2
    hide dct_el_running_back_and_forth with dissolve
    show d_el normal shorts at center with dissolve
    pi4 "Серёга, ты же хорошо играешь. Охота тебе в своём кружке лето просиживать? Может, свою команду организуем?"
    show d_el smile shorts with dspr
    pause 0.6
    show d_el laugh shorts with dissolve_fast
    "Электроник оглянулся, прежде чем ответить, и неожиданно упёрся взглядом в Женю."
    stop music fadeout 2.5
    play ambience ambience_camp_center_day fadein 2
    show dct_ext_playground_opposite_gate_day
    show mz normal glasses pioneer close at fleft
    with dissolve
    "Та сидела на противоположном краю трибуны и сверлила его глазами."
    
    scene bg ext_playground_day
    show d_el surprise shorts as el at center
    with dissolve
    "Настроение играть мгновенно пропало."
    show el sad pioneer at center with dissolve:
        alpha 1
        pause 1.8
        linear 1 alpha 0
    "Сыроежкин накинул рубашку и, ничего не объясняя новым товарищам, убежал к умывальникам."
    stop ambience fadeout 3
    show black:
        alpha 0
        pause 1.3
        linear 1 alpha 1
    th "Что Женя обо мне подумает?{w=0.6} Ей же наверняка нравятся умные. А я тут мячик пинаю."
    window hide
    show black as black2 with dspr
    pause 1
    
    play ambience ambience_int_cabin_day fadein 1
    scene dct_int_sporthall
    show black
    hide black with dissolve
    window auto
    "Семён подошёл к тренерской и, услышав из-за двери голоса, задержал руку на дверной ручке."
    th "Ульяна и кто?"
    th "Интересно…"
    stop ambience fadeout 1
    play music music_list['i_want_to_play'] fadein 1
    
    scene dct_int_coaching_room2
    show us laugh sport close at center:
        zoom 1.25 anchor(0.52, 1.0) pos (0.5, 1.15)
    with vpunch
    "Он потянул дверь и чуть не упал от внезапной тяжести — повисшей на плечах Ульянки-младшей. Ульянки из его родного лагеря."
    show us surp1 sport close at center with dissolve_fast:
        zoom 1.0 anchor(0.5, 0.5) pos (0.5, 0.5)
    us "Я соскучилась, братишка!"
    scene dct_int_coaching_room3
    show d_sf laugh sport:
        zoom 0.75 xcenter 0.37 ycenter 0.56
    show d_us smile sport:
        xcenter 0.75 ycenter 1.15 rotate 30
    show us grin sport:
        xcenter 0.48
    with dissolve
    # "Ульяна-большая валялась на кровати, закинув ноги на спинку, и с улыбкой наблюдала за этой картиной."   # По канону
    "Ульяна-большая валялась на кровати и с улыбкой наблюдала за этой картиной."
    us_old "Представляешь, прохожу мимо кустов, а меня за руку хватают и в кусты тянут."
    show d_sf smile sport with dspr
    us_old "А в кустах — эта мелкая. Соскучилась, говорит, и пришла проведать."
    show us smile sport with dspr
    us "Ага, пришла. Вам привет от Алисы, и Слави, и Мику! А вы же придёте в среду? А то они тоже соскучились."
    show d_sf normal sport with dspr
    me "Ульянка, а назад ты как же? Мы-то только в среду собираемся."
    show us normal sport
    show d_us normal sport
    with dspr
    me "Тебя в вашем лагере не хватятся?"
    show us laugh2 sport with dspr
    us "А я теперь могу в любое время приходить туда и назад, вот."
    show us shy sport with dissolve_fast
    us "Я{w=0.5}, мне…{w=0.7} Я научилась."
    show us upset sport with dissolve_fast
    us "Только у других девочек не получается. Жалко."
    show d_sf serious sport
    show d_us smile sport
    with dspr
    show us normal sport with dissolve_fast
    us_old "Она и меня пыталась научить."
    show d_us normal sport with dspr
    us_old "Какая-то трава должна расти на поляне, какие-то жуки особые должны водиться, а потом просто захотеть, представить того, к кому хочешь попасть, закрыть глаза и шагнуть."
    show d_us shy sport
    show us sad sport
    with dspr
    us_old "Всего-то."
    us "Да, всего-то!"
    show us smile sport with dspr
    us "А ты, сестрёнка, не грусти. Всё у тебя получится."
    show d_us smile sport with dspr
    us "А я ещё погуляю у вас по лагерю, посмотрю, как вы живёте, а потом назад, к себе. Чтобы к ужину успеть."
    show d_sf normal sport
    show d_us normal sport
    show us grin sport
    with dspr
    us "Всё, пока! В среду увидимся, буду ждать!"
    show d_sf smile sport
    show d_us smile sport
    with dspr
    hide us with dissolve
    "И Ульянка-младшая, чмокнув в щёку обоих Персуновых, убежала из тренерской."
    stop music fadeout 1
    show black with dissolve
    window hide
    pause 1
    
    $ set_mode_nvl()
    window show
    play music music_list['everyday_theme'] fadein 1
    scene bg int_clubs_male2_night
    show black
    hide black with dissolve
    "Шурик закончил паять микрофонный усилитель, отодвинул паяльник, посмотрел ещё раз на схему, чуть качнул головой, подумал, что если бы сначала рассортировал имеющиеся детали, то можно было бы сделать и поизящнее.{w} Зато сейчас получилось просто и надёжно.{w} Тем более что задача стояла усиливать всего лишь звуки горна и транслировать их на развешанные на фонарных столбах динамики."
    "\nПодключил микрофон, подключил к выходу наушники, постучал пальцем по микрофону, потом свистнул в него.{w} Удовлетворённо кивнул, видя, как дёрнулось зелёное пятнышко на экране осциллографа.{w} Осталось только согнуть корпус из листа алюминия, но это уже работа для Сыроежкина.{w} У самого Шурика так аккуратно и точно, как у компаньона, работать с металлом ни за что не получится."
    "\nШурик глянул на часы: через полчаса Сергей подойдёт, и большая часть работы будет закончена.{w} После ужина нужно будет закрепить коробочку с усилителем на одном из флагштоков, отдать горнисту микрофон со шнуром и протянуть провод от усилителя к радиорубке.{w} Почему-то вожатая настаивала на том, что горнист должен подавать сигналы обязательно с площади."
    window hide
    $ set_mode_adv()
    window auto
    
    scene bg int_clubs_male_day
    show sh serious pioneer close at cright
    with dissolve
    "Шурик выволок из кладовки лист алюминия, положил его на верстак, достал со шкафа годовую подшивку журнала «Радио» и устроился ждать Сыроежкина."
    show sh serious pioneer close:
        linear 0.5 ycenter 0.70
    "В здании клубов было тихо, шум со стадиона сюда не долетал, пионеры предпочитали играть в других местах, а ближайший автобус должен был подъехать только в среду."
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Чуть слышно потрескивал паяльник, остывая; гудел трансформатор, выдавая положенные тридцать шесть вольт; за окном чирикали воробьи и хлопали чьи-то крылья, покрупнее воробьиных."
    stop music fadeout 1
    show black with dissolve
    window hide
    
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    window auto
    play sound dct_sfx_robot_run_club_attic fadein 1.5
    pause 0.8
    stop sound fadeout 1.5
    play sound_loop ambience_int_cabin_evening fadein 1
    scene bg int_clubs_male_sunset
    show sh surprise pioneer close at cright:
        ycenter 0.70
    with dissolve
    "Когда незаметно для себя Шурик начал задрёмывать, вдруг показалось, что прямо над головой по чердаку пробежал кто-то лёгкий."
    show sh normal pioneer close with dspr
    "Шурик вскинулся, покрутил головой, прислушался — тишина."
    hide sh with dissolve
    "Отложил журналы в сторону и, заинтересовавшись, вышел на улицу."
    stop sound_loop fadeout 1
    play ambience ambience_camp_center_evening fadein 1
    
    scene dct_ext_clubs_sunset:
        zoom 1.05 align(0.5, 0.0)
    show 3500_sh normal pioneer as sh:
        zoom 0.26 xcenter 0.58 ycenter 0.68
    show dct_ext_clubs_day_el_look_at_roof as el
    with slideawayup
    "У противоположного, пустующего здания стоял Сыроежкин и тоже внимательно смотрел на крышу."
    show sh serious pioneer far:
        zoom 1.0 xcenter 0.65 ycenter 0.5
    show el normal pioneer far at cleft:
        zoom 1.0 xcenter 0.35 ycenter 0.5
    with dissolve
    el "Понимаешь. Иду к тебе, и показалось, что кто-то мелкий по крыше бегает."
    show d_el think2 pioneer far as el with dspr
    el"Я подумал на октябрят, но им лестницу не поднять."
    show sh normal pioneer far
    show el normal pioneer far
    with dspr
    "Кибернетики переглянулись и синхронно пожали плечами."
    stop ambience fadeout 2
    show black:
        alpha 0
        linear 2 alpha 1
    show black with dspr
    pause 2    
    
    play music littleidea fadein 1
    scene dct_ext_washstand_sunset
    show mt angry panama pioneer far:
        xcenter 0.45 ycenter 0.50
    show us shy sport far:
        xcenter 0.56 ycenter 0.50
    with fade
    "Ульянка-младшая всё-таки не успела уйти до ужина, не попавшись на глаза вожатой."
    show d_sf normal sport behind mt:
        zoom .75 xcenter 0.3 ycenter .56
    show d_us normal sport behind mt:
        zoom .75 xcenter 0.7 ycenter .76
    with dissolve
    show d_mt shocked panama pioneer far as mt
    show us surp1 sport far
    with dspr
    "Пришлось физрукам врать Ольге Дмитриевне и выручать гостью — пришлось выдавать её за сестрёнку, прибежавшую погостить."
    show mt surprise panama pioneer far
    show us laugh2 sport far
    with dissolve_fast
    "Пришлось сказать, что родители тут недалеко, ниже по течению, стоят с палаткой."
    
    scene dct_int_dining_hall_people_sunset with wipeleft
    "Пришлось кормить ужином."
    show mt normal pioneer close with dissolve
    mt "Это, конечно, нарушение режима, но не могу же я оставить гостью голодной!"
    show mt smile pioneer close with dspr
    "Вот такая Ольга Дмитриевна тоже бывала."
    hide mt with dissolve
    "Пришлось обещать, что родители тоже придут."
    scene bg ext_square_sunset with wipeleft
    "Пришлось знакомить со всем лагерем, объясняя одним — одно, а другим — другое."
    scene dct_ext_music_club_sunset with wipeleft
    "Пришлось вести вечером в музыкальный кружок, к Мику на чаепитие."
    $ persistent.sprite_time = "sunset"    # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Надо было видеть потеплевшие глаза Алисы — Ульяна-большая даже заревновала чуть-чуть."
    
    $ persistent.sprite_time = "day"
    scene dct_int_coaching_room2 with wipeleft
    stop music fadeout 2.5
    play ambience ambience_int_cabin_evening fadein 2.5
    show us smile sport with dissolve
    us "А вы неплохо устроились! Я ещё немного побегаю сама по себе и тоже пойду в физруки!"
    us "Будем матчи футбольные между лагерями проводить!"
    show us grin sport with dspr
    $ sunset_time()                     # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    us "И чаепития эти ваши тоже понравились!"
    stop ambience fadeout 1
    window hide
    show black with dissolve
    pause 1
    $ night_time()
    $ persistent.sprite_time = "night"
    window auto

    play ambience ambience_camp_center_night fadein 1
    play music peritune_gentle_theme_piano fadein 2
    scene bg ext_playground_night with dissolve
    "Уже стемнело, когда дверь в спортзал открылась и на пороге показались два силуэта."
    
    scene bg ext_dining_hall_away_night with pushright
    "Они не торопясь прошли по главной аллее мимо столовой."
    
    scene bg ext_square_night with pushright
    "На площади свернули направо, в сторону домика вожатой."
    
    scene dct_ext_houses_night with pushleft
    "Где-то со стороны клубов слышались голоса кибернетиков, тянущих последние метры кабеля к радиорубке. И ещё слышалась музыка."
    show us sad sport at cleft with dissolve
    us "Там музыка, на сцене."
    show d_us normal sport at cright with dissolve:
        ypos -0.05
    us_old "Да, Саша танцует. Хочешь посмотреть?"
    show us normal sport with dspr
    us "Хочу."
    show d_us smile sport with dspr
    us_old "Только прячься, а то она стесняется жутко."
    
    scene bg ext_stage_normal_night
    show dct_ext_stage_normal_night_sl_dancing
    with pushleft
    "Они постояли, подглядывая из кустов на танцующую Сашу."
    "Это завораживало настолько, что обеим захотелось выйти и присоединиться. Если бы они умели ещё при этом."
    us "Очень красиво..."
    
    scene bg ext_house_of_mt_night with pushright
    "Потом обе Ульянки вернулись на аллею."
    
    scene dct_ext_house_of_un_night with pushright
    "Прокрались мимо домиков вожатой и Лены."
    
    scene dct_ext_musclub_backside_night_brightwindows
    show dct_ext_musclub_backside_night_ma_mi
    with pushright
    show us normal sport:
        xcenter 0.32
    show d_us normal sport:
        xcenter 0.78 ypos -0.05
    with dissolve
    "По тропе вышли к музыкальному кружку и остановились."
    us "Это здесь."
    us "Видишь — вот трава, а вон жучки эти ползают. Они всегда в местах перехода обитают."
    show us sad sport with dspr
    us "Жалко, что я провести вас не смогу, это вам самим научиться нужно."
    "Света, падающего из окон музыкального кружка, хватало, чтобы рассмотреть и траву, и жучков."
    show us normal sport with dspr
    "В кружке Мику, сидя за роялем, объясняла что-то Максиму, держащему в руках горн. Нет, не горн, а другой инструмент. Похожий на трубу, но покороче и с более широким раструбом."
    show d_us smile sport with dspr
    us_old "\~ Пропал Макс. \~"
    show us grin sport with dspr
    us "Ну пока, сестрёнка, до послезавтра. Все вас очень ждут."
    show d_us normal sport with dspr
    us_old "Пока."
    show us smile sport with dspr
    us "Значит, смотри, показываю."
    us "Вот трава, вот жучки эти. Это значит — место перехода здесь."
    show us normal sport with dspr
    us "Потом ты закрываешь глаза и представляешь себе человека, к которому хочешь попасть. И всё."
    us "Нужно только очень сильно хотеть. Делаешь шаг вперёд — и ты на месте."
    window hide
    show us normal sport:
        ease 0.6 xpos 0.5
    show 3500_us back1 sport as us with dissolve_fast:
        anchor (0.5, 0.617) pos(0.32, 1.06)
        ease 0.6 xpos 0.5
        easeout 0.7 zoom 0.34 ypos 0.63
        easein 0.6 zoom 0.3 ypos 0.5
    pause 0.6
    
    scene dct_ext_musclub_backside_night_brightwindows
    show dct_ext_musclub_backside_night_ma_mi
    show d_us normal sport:
        xcenter 0.78 ypos -0.05
    with irisin
    window auto
    "Ульянка-младшая прыгнула вперёд, делая кувырок через руки, и пропала в высшей точке кувырка."
    "Ульяна-большая представила себе «сестрёнку» и, не задумываясь о последствиях, закрыла глаза и шагнула следом."
    $ renpy.music.set_volume(0.3, delay=1.5, channel='ambience')
    window hide
    show black with dissolve
    pause 0.5
    $ renpy.music.set_volume(1.0, delay=1.5, channel='ambience')
    pause 0.5
    hide black with dissolve
    window auto
    "Открыла глаза."
    "Ничего не изменилось."
    "Оглянулась на музыкальный кружок: Максим стоял, прижав инструмент к губам, и пытался что-то играть; Мику страдальчески морщилась, отвернувшись, чтобы не обидеть Макса."
    "Никуда Ульяна не переместилась."
    show d_us sad sport with dspr
    th "Видимо, это не всем дано. Наверное, придётся как в прошлый раз — ногами топать."
    show d_us smile sport with dspr
    show dct_ext_musclub_backside_night_ma_mi:
        linear 3.5 alpha 0
    "Вспомнила ещё, как показалось на секунду, что в момент кувырка младшей на неё из кустов с противоположной стороны поляны глянули как будто два желто-зелёных глаза, принадлежащих очень большой кошке."
    show dct_ext_musclub_backside_night behind d_us:
        alpha 0
        linear 1.5 alpha 1
    $ night_time()                          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Всё, сестрёнку проводила, пора спать. Или, может, посидим ещё с Сёмкой. Посмотрим."
    show d_us normal sport with dspr
    show d_us normal sport:
        easeout 2.3 zoom 0.6 xcenter -0.2 ypos 0.125
    stop sound fadeout 2
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2
    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')