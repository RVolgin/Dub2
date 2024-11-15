
# Монетка в фонтане — динамичная. Оптимизирована по лекалам остальных частей мода. Выкинуты описательные моменты, которые и без того переданы визуалом, а так же мелкие, не влияющие на сюжет подробности, тормозящие повествование чуть ли не на треть. Мы постарались адаптировать текст под формат мода, так же, как это делал Тангейзер.

label dct_coin_dyn:
    scene black
    stop sound
    stop sound_loop
    stop ambience
    play music music_list['reminiscences']
    show headline_text u"Монетка в фонтане" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
    
############################
#Глава 1. Шестичасовой цикл#
############################

label dct_sixhour_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Шестичасовой цикл"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window hide
    scene black
    show headline_text2 u"Глава I. Шестичасовой цикл" at truecenter with dspr
    $ renpy.pause(3.0)
    play sound_loop sfx_bus_interior_moving fadein 1.5
    hide headline_text2 with dissolve

    scene black
    $ set_mode_nvl()
    "Полуоткинутое кресло, шум мотора, мягкое покачивание. Да, это автобус: начался очередной цикл.{w} Это значит, что у меня, как и всегда, есть полчаса до того, как начнут просыпаться прочие пассажиры — копии и миксы."
    "\nНу что ж, пора присмотреться к компании.{w} Хотя что к ней присматриваться? Всё те же и там же.{w} Я никогда особо не интересовался здешними копиями, но за столько циклов запомнил — деваться некуда.{w} Даже если от каждого цикла я оставляю себе всего лишь шесть часов."
    stop music fadeout 2
    nvl clear

    scene dct_int_bus_people
    show dct_int_bus_people_sl_mi back:
        zoom 0.625
    show dct_int_bus_people_vi standup
    show unblink
    $ set_mode_adv()
    window auto
    "Подлинник Александра Трофимова открыл глаза"

    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise
    show d_sf normal pioneer:
        zoom 1.292 xcenter 0.37 ycenter 0.8 rotate -6.34
    show d_sf_sleep:
        zoom 1.292 xcenter 0.37 ycenter 0.8 rotate -6.34
    with squares
    extend " и вздрогнул." with vpunch
    th "А это ещё кто?"
    "Вместо привычного и ожидаемого Сыроежкина на сиденье рядом дремал полузнакомый парень лет двадцати пяти."
    show dct_int_bus_middle_sh serious with dspr
    th "Э-э-э… Физрук, кажется. Как его? Семён, да. Копия… Только эта копия вроде как постарше стала выглядеть, чем была."
    hide d_sf_sleep
    show dct_int_bus_middle_sh normal
    with dspr
    "А парень почувствовал, что его разглядывают, открыл глаза, посмотрел на Александра понимающим взглядом, кивнул, здороваясь."
    show d_sf smile pioneer with dspr
    show d_sf smile pioneer:
        pause 2.0
        linear 1.0 alpha 0
    "И, ничего не говоря, поднялся с кресла и пошёл в хвост автобуса, где с последнего ряда уже раздавались голоса проснувшихся Алисы и Ульяны."

    scene dct_int_bus_stern
    show dct_int_bus_stern_dv_us:
        zoom 0.5
    show dct_dream_veil at shiver
    with fade
    th "Проснулись уже. Значит, тоже активированные."
    show dct_int_bus_stern_un behind dct_int_bus_stern_dv_us with dissolve:
        zoom 0.5
    extend " О, и Лена с ними. А на её месте возле Жени тогда кто?"

    scene dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body:
    show dct_int_bus_another_middle_mz_head sleep:
    show dct_int_bus_another_middle_el:
    with fade
    "В кресле рядом с Женей, подставив ей своё плечо вместо подушки и прижавшись щекой к её затылку, спал Сыроежкин."

    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise
    with fade
    th "Сейчас они проснутся и случится скандал. Обычно скандал за ужином случается, а тут случится в автобусе. Флуктуация-с."
    show dct_int_bus_middle_sh normal with dspr
    usp "Сёмка…"
    "Сзади послышалось шуршание, пыхтение и скрипнуло пару раз."
    "Как будто кто-то потеснился на сиденье, чтобы посадить ещё одного человека."
    "Разговор за спиной продолжился, но разговаривали в четверть голоса, так что слов было не разобрать за шумом автобуса. Улавливался только сам факт разговора."
    stop sound_loop fadeout 2
    play music music_list["lightness"] fadein 3
    show black:
        alpha 0
        pause 0.5
        linear 1.5 alpha 1
    "Под эти голоса Александр и задремал второй раз."

    scene black
    
    #Дорога
    show dct_int_bus_stern:
        zoom 2 xcenter 1.0 ycenter 0.49
    show dct_int_bus_stern_un:
        xcenter 1.0 ycenter 0.49
    show dct_int_bus_stern_dv_us:
        xcenter 1.0 ycenter 0.49
    show dct_int_bus_stern_sf:
        xcenter 1.0 ycenter 0.49
    show dct_road_anim:
        zoom 0.8 xcenter 0.5 ycenter 0.5
        linear 3.6 zoom 1.0 xcenter 0.5 ycenter 0.39
        linear 1.0 alpha 0.0
    with dissolve_fast
    $ renpy.pause(2.8, hard = True)
    
    #Задняя площадка
    show dct_int_bus_stern:
        ease 4 xcenter 0.28 ycenter 0.49
    show dct_int_bus_stern_un:
        ease 4 xcenter 0.28 ycenter 0.49
    show dct_int_bus_stern_dv_us:
        ease 4 xcenter 0.28 ycenter 0.49
    show dct_int_bus_stern_sf:
        ease 4 xcenter 0.28 ycenter 0.49
    $ renpy.pause(4.5, hard = True)
    
    #Электроник с Женей
    scene dct_int_bus_window_view
    show dct_int_bus_window_view_el_mz
    with fade
    $ renpy.pause(1.3, hard = True)
    
    #Передняя площадка
    scene dct_int_bus_people:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        ease 2.5 zoom 1.6 xcenter 0.28 ycenter 0.6
    show dct_int_bus_people_sl_mi back:
        zoom 0.625 xcenter 0.5 ycenter 0.5
        ease 2.5 zoom 1.0 xcenter 0.28 ycenter 0.6
    show dct_int_bus_people_vi sitdown:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        ease 2.5 zoom 1.6 xcenter 0.28 ycenter 0.6
    with fade
    $ renpy.pause(1.5, hard = True)
    show dct_int_bus_people_sl_mi front with dissolve_fast
    $ renpy.pause(0.8, hard = True)
    
    #Яна и Яна
    show dct_coin_bus-stop:
        zoom 0.75 xcenter 0.5
    show d_jn_old smile:
        zoom 0.75 xcenter 0.54
    show d_jn_young smile:
        zoom 0.75 xcenter 0.46
    with fade
    $ renpy.pause(2.0, hard = True)
    hide d_jn_old
    hide d_jn_young
    show d_jn at center:
        zoom 0.9 ycenter 0.64
    with wipeup
    $ renpy.pause(1.0, hard = True)
    
    #Яна
    show dct_coin_bus-stop:
        easeout 2.5 zoom 1.8 ycenter 0.6
    show d_jn:
        easeout 2.5 zoom 4.8 ycenter 1.2

    stop music fadeout 2

    scene black with dissolve2
    play sound_loop sfx_bus_interior_moving fadein 2
    "А разбудил его протестующий девичий крик."
    $ renpy.sound.set_volume(0.5, delay=0)
    play sound dct_sfx_femscreech
    $ renpy.pause(0.4, hard = True)

    scene dct_int_bus_another_middle behind blink
    show el shocked pioneer close behind blink:
        xcenter 0.43
    show d_mz rage pioneer far behind blink:
        xcenter 0.64
    show unblink
    pause 0.5
    show blink
    pause 1.0
    hide blink
    show unblink
    "Слова спросонья были непонятны, но вот то, что так может кричать только оскорблённая невинность, ясно было и без слов."
    show blink
    $ renpy.sound.set_volume(1.0, delay=0)
    "Когда вопль прервался, стали слышны сдерживаемые смешки с заднего ряда."
    th "Пересадили Сыроежкина, пока он спал. Хоть вы и активировались, но как были детьми, так и остались."
    play sound dct_sfx_fallen_book
    "Кто-то шлёпнулся рядом на сиденье — понятное дело, кто, — и тут же следом прилетела какая-то тряпка, зацепив Александра по носу и сбив с него очки."

    scene dct_int_bus_another_middle
    show d_mz shyangry pioneer far:
        xcenter 0.64
    show unblink
    mz "Как тебя там? Который в очках. Прости, я не хотела."
    show d_mz angry pioneer far with dspr
    mz "А ты, лохматый, ещё раз начнёшь руки распускать — лучше сразу костыли заказывай!"

    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise noglasses
    show el scared pioneer close:
        zoom 1.095 xcenter 0.31 ycenter 0.57 rotate -12.9
    with dissolve
    mz "Или нет, не заказывай. Тебе же всё равно костыли держать нечем будет."
    show dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body
    show dct_int_bus_another_middle_mz_head upset
    with dissolve
    "Александр наконец нашёл очки и смог разглядеть уже демонстративно отвернувшуюся к окну Женю."
    hide dct_int_bus_another_middle
    hide dct_int_bus_another_middle_mz_body
    hide dct_int_bus_another_middle_mz_head
    show dct_int_bus_middle_sh surprise
    show el upset pioneer close
    with dissolve
    "А также сбитого с толку Сыроежкина и его бейсболку, валяющуюся сейчас на полу."
    show el sad pioneer close
    show dct_int_bus_middle_sh normal
    with dspr
    el "Ведь ничего же не делал… Проснулся, а она у меня на плече спит и с плеча сползать начала. Ну я и пошевелился чуть, чтобы ей удобно было…"
    th "Пора вживаться в роль."
    "Александр поднял с пола бейсболку, непонимающе оглядел её, отряхнул. Потом, словно что-то сообразив, протянул её Сыроежкину."
    adl_sh4 "Вот, возьми, пожалуйста. Ты, наверное, уронил, когда спал."
    show el upset pioneer close with dspr
    el "Да, спасибо."
    show el surprise pioneer close with dspr
    el "А ты — тот самый Шурик Трофимов?"
    th "Узнал наконец. Вот теперь цикл действительно начался."
    show dct_int_bus_middle_sh surprise with dspr
    adl_sh4 "Да, я… Шурик Трофимов, но почему тот самый?"
    show el smile pioneer close with dissolve_fast:
        zoom 1.095 xcenter 0.34 ycenter 0.56 rotate -8.9
    el "Ну как же, я читал о тебе в журнале. Победитель трёх всесоюзных олимпиад: по программированию, по кибернетике и по робототехнике. Мы по твоей статье в кружке робота собирали."
    show el normal pioneer close
    show dct_int_bus_middle_sh normal
    with dspr
    "И разговор пошёл по накатанной многими циклами колее."

    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh normal
    show el sad pioneer close:
        zoom 1.095 xcenter 0.31 ycenter 0.57 rotate -12.9
    with dct_fade
    $ renpy.sound.set_volume(0.5)
    play sound dct_sfx_bus_braking fadein 1
    pause 1.2
    play sound_loop dct_sfx_loop_bus_moves_slow
    pause 0.7
    stop sound fadeout 2
    "Автобус начал плавно сбавлять ход. Зашевелились пионеры, готовые сорваться с места и побежать к дверям."
    "По проходу быстрым шагом прошёл Семён."
    show dct_int_bus_middle_sh serious with dspr
    th "Да, это тот же самый Семён, которого я помню по посёлку, только сейчас он выглядит на двадцать пять. Вырос."
    th "Видимо, активировался, сумел встроиться в Систему, и Система привела его облик в соответствие с новой функцией. Помнил бы я циклы — я бы знал точно."
    show dct_int_bus_middle_sh normal with dspr
    th "Но какая мне разница?"

    # scene dct_int_bus_middle
    # show dct_int_bus_middle_sh_body
    # show dct_int_bus_middle_sh normal
    # show el sad pioneer close:
        # zoom 1.095 xcenter 0.31 ycenter 0.57 rotate -12.9
    # with dct_fade
    stop sound_loop fadeout 2
    $ renpy.sound.set_volume(0.3)
    play sound sfx_bus_stop
    "Автобус начал разворачиваться, перед тем как окончательно остановиться и открыть двери, а пионеры приготовились сорваться с места и устроить свалку перед дверями."
    play sound2 dct_sfx_whistle     # Проигрывание свистка на втором звуковом канале (чтоб не пересекался с автобусом)
    play music music_list['eat_some_trouble'] fadein 1
    show dct_int_bus_middle_sh surprise
    show el shocked pioneer close:
    with dspr
    "И в этот момент от передних сидений раздался резкий свисток. Это было настолько неожиданно, что все вздрогнули."

    scene dct_int_bus_people
    show dct_int_bus_people_sl_mi_sf
    show dct_int_bus_people_vi sitdown
    with dissolve
    me "Уважаемые пионеры и примкнувшие, наш самолёт совершил посадку в аэропорту «Совёнок один», через несколько минут подадут трап, а пока прослушайте…"
    th "Дурачится…"
    "Пионеры должны были сейчас под управлением заложенных алгоритмов встать и, устроив, конечно, свалку, но свалку управляемую и декоративную, выйти из автобуса."
    "А то, что делал сейчас Семён — оно просто сбивало с толку управляющие программы…"
    me "…поэтому тот, кто выйдет последним…"
    show dct_int_bus_people_vi standup with dspr
    pi2 "Тот тухлый помидор!"
    me "Умница, Виктор. Но ты не угадал."
    me "Я всего лишь хотел сказать, что тот, кто покинет автобус последним, получит право выбрать себе любой домик для проживания. А первого выскочившего на улицу администрация заселит в домик по своему выбору."
    show dct_int_bus_people_vi sitdown with dissolve_fast
    dvp "Эй!"
    me "Поправку принимаю. Это касается только пионеров среднего отряда и их домиков."
    $ renpy.sound.set_volume(1.0)
    $ renpy.music.set_volume(0.35, delay=1.5)
    
    scene black with dissolve_fast
    $ set_mode_nvl()
    window show

    scene dct_ext_buses_filled with dissolve_fast
    "Давно уже вышел младший отряд, был встречен вожатой и построен у ворот. Только две девочки и три мальчика подбежали к компании с заднего сиденья Икаруса. Обнялись, некоторые с удовольствием, некоторые неловко, но всё равно с радостью, и убежали назад к своим."
    "\nДавно уже чинно (по сравнению с октябрятами — чинно и степенно) вышел из Икаруса отряд старший и стоял кучкой на обочине."
    "\nУже Ольга Дмитриевна подошла к старшим пионерам, заглянула в автобус, шепнула на ухо Семёну: «Сам кашу заварил, сам и расхлёбывай», и увела октябрят в лагерь."
    "\nА средний отряд продолжал сидеть в автобусах, причём как в Икарусе, так и откуда-то прознавшая об праве выбора домиков та часть отряда, что ехала в ЛАЗе вместе с октябрятами."
    "\nСтаршие отошли с асфальта в тень и уселись — кто на чемоданы, кто просто на траву."
    $ renpy.music.set_volume(0.0, delay=1.5)
    window auto
    $ set_mode_adv()
    play ambience ambience_camp_entrance_day fadein 1.5
    show d_sf normal pioneer at left with dissolve
    me "Алис, может, уведёшь старшаков? А то им ещё бельё и форму получать, и домики, кстати, занимать."
    show dv smile pioneer2 with dissolve:
        xcenter 0.76
    dv "И пропустить всё веселье?"
    show dv laugh pioneer2 with dspr
    dv "Сенька, давай их пинками выгоним!"
    show d_sf laugh pioneer at left with dspr
    me "Что? И Катьку с Викой, Макса и Витьку тоже выгонишь? Дружескими пенделями?"
    show dv grin pioneer2 at fright with dissolve_fast
    dv "М-да, проблема. А может, это не те? Не наши?"
    show d_sf smile pioneer with dspr
    me "Те, те. Я проверил."
    $ renpy.music.set_volume(1.0, delay=3.5)
    stop ambience fadeout 2
    hide d_sf
    hide dv
    with dissolve2
    "Пять минут спустя сидячая забастовка среднего отряда закончилась."

    scene dct_int_bus_people
    show dct_int_bus_people_sf smile
    show dct_int_bus_people_vi sitdown
    with dissolve
    me "Я говорил, что последний вышедший из автобуса будет сам выбирать себе домик?"
    d_guys "Да-а-а!"
    me "Я говорил, что первого вышедшего из автобуса администрация поселит, не спросив его мнения?"
    d_guys "Да-а-а!"
    show dct_int_bus_people_sf normal with dspr
    me "Так вот, вас здесь сорок два человека."
    me "Домик себе будет выбирать не один — самый последний, а те двадцать один человек, что выйдут последними."
    me "Последний выбирает из двадцати одного домика, предпоследний из двадцати, пред-предпоследний из девятнадцати. Вы меня поняли? Согласны?"
    d_guys "Да-а-а!"
    show dct_int_bus_people_sf laugh with dspr
    me "Но сначала администрация расселит вышедших первыми пионеров в лучшие домики. А вы уже напрашивайтесь к ним в соседи. Если они, конечно, захотят вас взять."
    d_guys "У-у-у-у…"
    me "Вот такое у-у-у-у… Или вы сейчас разобьётесь на пары и сами разберётесь, кто, где и с кем будет жить."
    "Семён сунул в руки ближайшему пионеру план лагеря."
    show dct_int_bus_people_sf smile with dspr
    $ day_time()    # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    me "Кстати, для этого не обязательно сидеть в автобусе."
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ set_mode_nvl()
    window show

    scene bg ext_square_sunset with dissolve_fast
    play music peritune_gentle_theme_piano fadein 1.5
    "Потом был сумасшедший вечер:"
    show dct_ext_storage_day:
        alpha 0.0
    show ext_house_of_dv_day:
        zoom 0.5 align(-1.0, -1.0)
        easein 1 align(0.0, 0.0)
    show ext_house_of_sl_day:
        zoom 0.5 align(2.0, -1.0)
        pause 0.5
        easein 1 align(1.0, 0.0)
    show dct_ext_house_of_el_day:
        zoom 0.5 align(2.0, 2.0)
        pause 1
        easein 1 align(1.0, 1.0)
    show ext_house_of_un_day:
        zoom 0.5 align(-1.0, 2.0)
        pause 1.5
        easein 1 align(0.0, 1.0)
    extend " расселение по домикам,"
    show dct_ext_storage_day:
        alpha 1.0
    show ext_house_of_dv_day:
        easeout 0.7 align(-1.0, -1.0)
    show ext_house_of_sl_day:
        easeout 0.7 align(2.0, -1.0)
    show dct_ext_house_of_el_day:
        easeout 0.7 align(2.0, 2.0)
    show ext_house_of_un_day:
        easeout 0.7 align(-1.0, 2.0)
    show dct_int_warehouse_day:
        alpha 0.0
        pause 2.5
        linear 1 alpha 1.0
    show dv angry pioneer2 at cright:
        alpha 0.0
        pause 2.5
        linear 1 alpha 1.0
    show d_us hurt sport at left:
        alpha 0.0 ypos -0.1
        pause 2.5
        linear 1 alpha 1.0
    extend " визит на склад за бельём и пионерской формой, где задёрганные Алиса с Ульяной рычали на бестолковых пионеров."

    scene bg ext_playground_day
    show int_house_of_dv_day:
        xcenter 0.5 ycenter 0.5     # это чтоб потом зумировать красиво
    show dct_int_house_of_mi_day
    show dct_int_house_of_el_day
    show dct_int_house_of_sa_day
    show dct_lineup_mi_not_us
    show int_dining_hall_people_day:
        alpha 1
        pause 3
        linear 1 alpha 0
    with blinds
    extend " Ужин и вечерняя линейка, на которой вожатая зачитала правила внутреннего распорядка и познакомила пионеров с персоналом лагеря."
    show dct_lineup_mi_not_us:
        easeout 1 ycenter 1.5
    show dct_int_house_of_sa_day:
        pause 2
        easeout 1 xcenter -0.5
    show dct_int_house_of_el_day:
        pause 4
        easeout 1 ycenter -0.5
    show dct_int_house_of_mi_day:
        pause 6
        easeout 1 xcenter 1.5
    extend "\n\nА после линейки наступило некоторое затишье: пионеры распаковывали чемоданы, Алиса с Ульяной, умаявшиеся на складе, валялись у Алисы в домике и неспешно беседовали"
    show int_house_of_dv_day:
        anchor (0.5, 0.5)
        easeout 1 zoom 2 alpha 0
    extend ", Семён валялся на лавочке около футбольного поля, закинув руки за голову, разглядывая облака и размышляя"

    scene dct_camp_stroll_to_the_right      # псевдокартинка из пролистывающихся фонов
    show sl surprise pioneer far at center:
        ycenter 0.55
    show un normal pioneer far:
        xcenter 0.33 ycenter 0.55
    show mi upset pioneer far at fleft:
        ycenter 0.55
    with squares
    extend ", Лена, в который уже раз за все циклы, обходила с Сашкой и Мику лагерь, показывая достопримечательности и закоулки"    # Почему-то текст перевёрстывается

    scene bg int_house_of_mt_sunset
    show mt sad pioneer close:
        xcenter 0.5 ycenter 0.75
    with wipeup
    extend ", Ольга Дмитриевна у себя в домике спешно перепечатывала на взятой в библиотеке машинке «План мероприятий на I смену»."
    nvl hide dissolve
    nvl clear    
    stop music fadeout 1

    scene black with dissolve_fast
    window hide
    pause 0.5

    scene dct_int_house_of_el_sunset
    show el sad pioneer at cleft
    show sh serious pioneer at right
    with dissolve_fast
    play ambience ambience_int_cabin_evening fadein 1
    $ set_mode_adv()
    window auto
    el "Шурик, ты не хочешь в библиотеку записаться?"
    th "В библиотеку? И читать здешнюю идеологическую макулатуру и книги о приключениях?"
    adl_sh4 "Знаешь, Сергей, наверное, у меня не будет времени на библиотеку."
    show sh normal pioneer with dspr
    adl_sh4 "Но я подумаю до завтра."
    th "А вдруг этот Шурик туда всё же записывался?"
    show sh serious pioneer with dspr
    adl_sh4 "Всё равно с обходными бегать. Ты иди сейчас, если хочешь. Заодно посмотришь, что там есть. А я… поработаю."
    show el serious pioneer with dissolve_fast
    "Несколько минут Сергей колебался между интересом к науке и интересом к Жене."
    show el laugh pioneer with dspr
    "А потом убежал, для очистки совести пообещав, что вернётся, как только запишется."
    stop ambience fadeout 1

    scene dct_ext_library_sunset with dissolve
    play music music_list['dance_of_fireflies'] fadein 1
    show dct_el_shuttles_back_and_forth:      # Сборная картинка: Электроник курсирует туда-сюда
    "Это «как только» продлится почти до полуночи. Сперва Сыроежкин несколько раз с независимым видом пройдёт мимо библиотеки, как будто он там случайно гуляет."
    hide dct_el_shuttles_back_and_forth with dissolve_fast
    show el angry pioneer far at right with dissolve
    show el angry pioneer at cright with dissolve
    show el angry pioneer close at center with dissolve
    "Потом, почти решившись, подойдёт к двери и уже почти возьмётся за ручку, когда услышит смех и голоса Мику и Саши."
    show el shocked pioneer far at center with dissolve
    pause 0.4
    show el normal pioneer far with dissolve:
        pause 2
        linear 1.5 alpha 0
    show sl laugh pioneer:
        xcenter 1.13 
        linear 3 xcenter -0.33
    show mi grin pioneer:
        xcenter 1.32
        linear 3 xcenter -0.14
    $ sunset_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    "Девочки, даром что не проснувшиеся, прекрасно сообразят, в чём дело, и, проходя мимо, захихикают."

    scene bg ext_library_night with dissolve2
    $ night_time()
    $ persistent.sprite_time = "night"
    "Отчего бедный Сыроежкин потеряет половину решимости, сделает ещё круг по лагерным «Ульянкиным тропам» и вновь окажется у библиотеки, только через полчаса после её закрытия."
    show el sad pioneer close with dissolve
    "Подёргает дверь, вздохнёт, взъерошит волосы и уйдёт на берег между пристанью и пляжем."
    hide el with dissolve
    "И там, укрывшись за деревьями от посторонних глаз, сидя на бревне, будет грустно кидать камушки в воду."

    scene bg int_library_night2
    show mz normal glasses pioneer:
        xcenter 0.52
    show int_library_night:
        alpha 0
        pause 4
        linear 2 alpha 1
    with fade
    "А Женя, наблюдавшая за всеми этими танцами через окно и прождавшая Сыроежкина ещё двадцать минут после закрытия, расстроенная засядет в своём домике и будет грустить."

    scene dct_int_house_of_mi_night
    show mz normal pioneer close
    with dissolve
    th "Вот, в общем-то, неплохой и, кажется, серьёзный и интеллигентный парень так и не решился зайти. Я бы извинилась перед ним."
    th "Может, моя жизнь бы изменилась?"
    th "Зря я на него наорала там, в автобусе. Он же ничего плохого и не хотел. Может, завтра зайдёт?"
    show d_mz sad pioneer close as mz with dspr
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Ну почему, почему у меня всегда всё наперекосяк выходит?"
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ sunset_time()
    $ persistent.sprite_time = "sunset"

    scene dct_int_house_of_el_sunset
    show sh serious pioneer
    with dissolve_fast
    play ambience ambience_int_cabin_evening fadein 1
    "Александр Трофимов после ухода соседа подождал ещё минут тридцать, потом поднялся и, оставив записку Сыроежкину, отправился в кружок кибернетики."
    hide sh with dissolve

    scene dct_ext_clubs_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 1
    show int_clubs_male_sunset:
        alpha 0
        pause 1.8
        linear 0.7 alpha 1
    play sound sfx_open_door_clubs
    th "Хотел посидеть в одиночестве, когда никто не будет восхищаться «стальным фанатиком науки», но не получилось. Тут чаепитие в самом разгаре."

    scene bg int_clubs_male_sunset
    show d_sf normal pioneer at left:
        zoom 1.25 ypos 0.20
    show d_us normal dress at right:
        zoom 1.25 ypos 0.08
    with dissolve
    play ambience ambience_int_cabin_evening fadein 1
    adl_sh4 "Здравствуйте, Семён. Здравствуйте, Ульяна."
    show d_sf laugh pioneer with dspr
    me "Саша. Не обижайся на нас, мы тут похозяйничали. Это ведь Шурика обиталище, а не Александра. А я всё-таки замначальника здешней богадельни."
    show d_sf smile pioneer with dspr
    me "Так что наливай себе чай и присоединяйся."
    show d_us smile dress with dspr
    us "Мы скоро уйдём. Попрощаемся с тобой и уйдём. А то нехорошо тебя просто так отпускать."
    th "Чай. И домашняя выпечка — хорошо. Но сейчас меня начнут уговаривать остаться."
    show d_sf normal pioneer with dspr
    adl_sh4 "Спасибо."
    th "Надо перехватывать инициативу."
    adl_sh4 "Ульяна, та самая? Нашлась?"
    show d_us shy dress with dspr
    adl_sh4 "Я подозревал, что здесь именно ты, а теперь точно вижу."
    us "Да, наверное.{w} Мне…{w=0.4} Нам подарили одну фотографию. И на ней точно мы с Сёмкой."
    us "И я мало что помню, но как я печатала эту фотографию — я вспомнила. Сыроежка печатал фото по чьему-то заданию, и я попросилась в лабораторию со своей плёнкой."
    show d_us normal dress with dspr
    us "Ты знаешь, Саша, он почти не изменился с тех пор. Всё тот же очень способный, безотказный, старательный и очень наивный мальчик."
    show d_us sad dress with dspr
    us "Он всё рассказывал, что отучится ещё год и поедет в Москву поступать в Бауманку. Как он жалеет о том, что побоялся написать заявление и сдавать выпускные экзамены за десятый класс экстерном, и теперь из-за этого ещё год в школе потеряет."
    show d_us hurt dress with dspr
    us "А я тогдашняя слушала и всё не решалась ему сказать, что никакого будущего, никакого «через год» и никакой Бауманки у него не будет."
    us "Что он так и останется тут, вечным Сыроежкой. Универсальным помощником-лаборантом. Александр, за что вы с ним так поступили? За что вы с {b}ними{/b} так поступили?"
    us "Я понимаю, копии, те — побочный эффект, дубликаты — они хоть информированы были, подлинники — вообще настоящие. Но миксы? Которых можно было и не создавать, не отправлять в этот бесцельный бег по кругу!"
    us "Я спрашивала у Сёмки, но он всего лишь дубликат, а вы — последний подлинник здесь. Я бы у бабы Глаши спросила, но тогда, когда она ушла, я ещё не понимала ничего. Виола и Анатолий — Сёмка сбросил их до нуля, тоже не спросишь. Остались вы."
    us "Я вас не обвиняю, но хочу понять, хочу услышать хоть какой-то ответ. Вы сейчас уйдёте, я не собираюсь вам мешать. Но в следующем цикле я задам тот же вопрос! И в следующем!"
    show d_us hurt dress at right with dissolve_fast:
        zoom 1.0 ypos -0.05
    hide d_us with dissolve_fast
    play sound sfx_slam_door_campus
    pause 0.5
    adl_sh4 "Не понимаю."
    adl_sh4 "Семён.{w=0.4} Это ведь твой оригинал был заведующим лабораторией синтеза биосистем. Если хочешь Ульяне помочь, покопайся в памяти."
    adl_sh4 "А моё мнение — всё, что может быть создано, должно быть создано. Вопрос только правильного применения."
    show d_sf grin pioneer with dspr
    me "«Какая великолепная физика!»."
    show d_sf serious pioneer with dspr
    me "Кроме того, что не мешать, я могу ещё что-то для тебя сделать?"
    adl_sh4 "У тебя есть выключатель?"
    me "Нет, я уничтожил их. И свой, и Виолы."
    adl_sh4 "Тогда ничего."
    show d_sf serious pioneer at center:
        zoom 1.0 ypos 0.0
    show sh serious pioneer at fright
    with dissolve
    adl_sh4 "Спасибо, что зашли. И передай Ульяне, пожалуйста, что когда рожают детей, то их согласия тоже не спрашивают."
    show d_sf normal pioneer with dspr
    stop ambience fadeout 6
    adl_sh4 "Ещё примерно час, если что понадобится, то обращайся. После — не приходи."
    hide d_sf with MoveTransition(1.1, leave=_moveright, leave_time_warp=_ease_time_warp)
    play sound sfx_close_door_1
    $ persistent.sprite_time = "sunset" # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "И каждый цикл я надеюсь, что этот час станет последним."

    scene black with dissolve_fast
    pause 0.5
    $ persistent.sprite_time = "day"
    
    scene dct_int_coaching_room2
    show d_us sad dress at right:
        ypos -0.05
    with dissolve_fast
    play ambience ambience_int_cabin_evening fadein 1
    show d_sf normal pioneer at cleft with dissolve
    play music forgotten_summer fadein 3
    us "Сёмк, ты ведь у Шурика узнать что-то хотел. А я всё испортила. Хотела просто попрощаться с ним, а всё испортила. Не смогла замолчать."
    us "Но мне вдруг их так жалко стало. Миксов этих. Что Женю, что Мику, что Сыроежку. У нас, у всех остальных, хоть какое-то прошлое, но было."
    us "Помнишь, как плясала от радости Алиса, когда о своём детстве рассказывала, всё, что вспомнила. Про стрекозу эту. Хотя там рассказов-то на полчаса — копия же."
    us "А она это детство всё вспоминает и вспоминает. Вот и сегодня тоже."
    us "А у этих-то и детства нет — всё придуманное, и вся жизнь — только бег по кругу, а когда они проснутся, то ничего. Ни{w=0.2}-че{w=0.2}-го."
    show d_us hurt dress
    show d_sf serious pioneer
    with dspr
    us "Я же сама была в их шкуре. Я же как проснулась, не могла ничего вспомнить о себе, о своём детстве, ни о настоящем, ни о придуманном."
    us "Знаешь, как это тоскливо?"
    show d_us sad dress
    show d_sf normal pioneer
    with dspr
    us "Пока девочки нам ту папку не принесли и у меня не начала память просыпаться. А Шурик — ну, он не Шурик сейчас, конечно, но мне так привычнее — спросил: «Нашлась?». Я-то нашлась, но я вот взяла и о миксах вспомнила."
    us "Они-то никогда не найдутся."
    show d_sf smile pioneer with dspr
    me "Рыжик, куда ты дела Ульянку?"
    show d_us normal dress with dspr
    us "Да никуда я её не дела. Тут она, где всегда. Просто бывает и Ульянке грустно."
    stop music fadeout 4
    show d_sf normal pioneer with dspr
    us "Ты лучше скажи, Сёмк, зачем ты устроил этот цирк в автобусе? Оставил пионеров на пять минут, а потом вернулся и повторил всё слово в слово. Ведь ты же им ничего нового не сказал. А они взяли и послушались."
    me "Просто, Рыжик, те пионеры и сами понимали, что сидячая забастовка зашла слишком далеко. Вот и ухватились с радостью за компромисс с администрацией."
    me "Помнишь, как в прошлом цикле двое чуть не подрались из-за Катьки? И зависли на полушаге к драке, и тоже не знали, что делать."
    me "Алгоритмы поведения сыпятся постепенно. Пионерам всё больше приходится думать своей головой, а голову тренировать нужно."
    $ sunset_time()                     # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    me "Вот я и пытаюсь делать так, чтоб потом не бегать за ними и носы не подтирать, чтобы они сами за себя думали. Часто вот такие казусы получаются, как в автобусе."
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ night_time()
    $ persistent.sprite_time = "night"

    scene dct_int_clubs_male_night_light_mon
    show sh serious pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    with dissolve_fast
    $ renpy.music.set_volume(1.0)
    play music fm_freemusic_chillout_music fadein 1
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1
    th "Какой там пароль? Двадцать лет назад боялся, что забуду или что Сыроежкин найдёт. Страдал: записать или запомнить. И не забыл, и не нашёл."     
    play sound_loop sfx_computer_noise fadein 0.5
    "Александр нажал «Ввод», подождал, пока на экран не выползет таблица, просмотрел её, удовлетворённо кивнул, достал наушники и подключил их к компьютеру."
    show sh normal pioneer close with dspr
    "Посмотрел на часы: до нужного времени оставалось ещё десять минут, хватит на одну сигарету."
    show sh serious pioneer close with dspr
    "Выдвинул нижний ящик стола, вытряхнул из него электрический хлам: обрезки проводов, мотки припоя, старые динамики, и снял фальшивое дно."
    th "Дожили, талонную «Приму» храню, как величайшую драгоценность."
    stop sound_loop fadeout 1.5
    $ renpy.music.set_volume(0.35, delay=1.5)

    scene dct_ext_clubs_night_light_inside
    show sh serious pioneer far at cright
    with fade
    play ambience ambience_camp_center_night fadein 1
    th "Позорище. Доктору наук приходится курить в кулак и прятаться как пацану."
    "Александр курил не торопясь и вспоминал…{w} Хотя и всеми силами пытался этого не делать с самого времени пробуждения в автобусе."
    "Всплыл в голове развёрнутый вариант ответа Ульяне, вторую часть которого он не стал озвучивать: «Когда рожают детей, то их согласия тоже не спрашивают. Но потом дети почему-то предпочитают жить»."
    dreamgirl "Па, ты зачем наврал Семёну?"
    adl_sh4 "Лучше сразу отсечь лишние воспоминания, вопросы и разговоры."
    dreamgirl "И меня?"
    adl_sh4 "И тебя."
    th "Всё. Время."
    stop ambience fadeout 4
    $ renpy.music.set_volume(1.0, delay=5)
    show dct_int_clubs_male_night_light_mon:
        alpha 0
        pause 3
        alpha 1
    show black:
        alpha 0
        pause 2.5
        linear 0.5 alpha 1
        linear 0.5 alpha 0
    "Александр затушил окурок, закопал его подвернувшейся кстати щепкой в рыхлую землю, вернулся в кружок."

    scene dct_clubs_male_comp_night
    show dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_dim:
        xcenter 0.5 ycenter 0.45
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1.5
    "Надел наушники, сел перед экраном, стёр содержимое одной из ячеек таблицы, заменив его на ещё одну бессмысленную цепочку из символов, ввёл пароль и, как полчаса назад, нажал «Ввод»."
    play sound_loop sfx_computer_noise fadein 0.5
    show dct_clubs_male_comp_sh with dissolve_fast:
        xcenter 0.5 ycenter 0.45
    hide dct_clubs_male_comp_table with dspr
    "В наушниках зашумело, а таблицу на экране сменило его собственное лицо, постепенно распадающееся на хаотически мелькающие разноцветные треугольники."
    window hide
    show dct_clubs_male_comp_sh_crumble with dissolve_fast
    hide dct_clubs_male_comp_sh
    pause 9
    show dct_clubs_male_comp_night_light_mon:
        linear 0.5 alpha 0.5
    hide dct_clubs_male_comp_sh_crumble with dissolve_fast
    window auto
    "Через десять минут экран погас."
    stop sound_loop fadeout 3.5
    show dct_int_clubs_male_night_light:
        alpha 0
        pause 2
        linear 0.5 alpha 1
    show dct_int_clubs_male_night:
        alpha 0
        pause 3.5
        linear 0.5 alpha 1
    hide dct_clubs_male_comp_night_light_mon
    hide dct_clubs_male_comp_dim
    with dissolve_fast
    "Александр встал, с видимым трудом выключил компьютер и деревянной ковыляющей походкой зашагал к выходу из кружка и дальше, в сторону площади и домика."

    scene bg ext_clubs_night
    show sh upset pioneer far
    with fade
    $ renpy.music.set_volume(0.3, delay=1)
    play ambience ambience_camp_center_night fadein 1
    th "Это инерция, сейчас всё закончится. Удачи тебе!"
    "Думалось тоже с трудом."
    show sh upset pioneer far:
        ease 1.2 xcenter 0.7
    "Показалось, что от ворот кто-то смотрит в спину, но оглядываться уже не было сил."
    $ renpy.music.set_volume(0.4, delay=2, channel='ambience')
    show sh upset pioneer far:
        easeout 2 xcenter 1.25 alpha 0
    "Подлинник Александра Трофимова, заведующего лабораторией спецавтоматики, в очередной раз перестал существовать."
    hide sh
    $ renpy.music.set_volume(0.0, delay=0.25)
    $ renpy.music.set_volume(1.0, delay=0.25, channel='ambience')
    show ext_square_night
    show sh surprise pioneer close at right
    show ext_clubs_night:
        alpha 1
        linear 0.25 alpha 0
    dreamgirl "Удачи тебе!" with vpunch
    "Шурик вздрогнул, огляделся, узнал памятник Генде и удовлетворённо кивнул."
    show sh normal pioneer close
    th "Двадцать четыре часа тринадцать минут. Надо же, заработался. И голова болит нехорошо, не пришлось бы завтра в медпункт обращаться. Планов много, а смена такая короткая. Надо выспаться, и всё пройдёт."

    scene dct_ext_camp_entrance_night
    show dct_jn_near_gate
    with dct_fade
    $ renpy.music.set_volume(1.0, delay=1.5)
    "Маленькая серебристая фигурка, незаметная ночью на фоне крашенных серебрянкой ворот, была неподвижна, как статуя."
    "Она мало походила на человека: половина её алюминиевого лица была закрыта чёрным зеркальным щитком, а вместо носа и рта чернела совмещённая решётка газоанализатора и динамика."
    window hide
    show d_jn:
       zoom 4.0 xcenter 0.0 ycenter 1.2 alpha 0
       linear 2.5 xcenter 0.5 alpha 0.7
       linear 2.5 xcenter 1.0 alpha 0
    $ renpy.pause(4, hard=True)
    $ night_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    window auto
    "Но любой наблюдатель сказал бы про эту фигурку три слова: «Грусть и печаль»."
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
    
    
    
###################
#Глава 2. Переходы#
###################

label dct_transitions_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Переходы"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава II. Переходы" at truecenter with dspr
    play ambience ambience_camp_center_evening fadein 2
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_ext_house_of_el_night with dissolve
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
    th "Эта девочка, Александра — она на пробежку отправилась."
    th "Хорошая девочка, сразу видно."
    extend " Почему я их вчера с этой японкой Мику так испугался?"
    th "Конечно! Мику же с Женей живёт, теперь расскажет Жене, как я вчера на крыльце библиотеки топтался — что Женя обо мне подумает?"
    th "Может, уже рассказала.{w=0.5} Стыдно."
    th "А мне сегодня обходной подписывать. Может, Шурика попросить сразу два обходных подать?"
    th "А Женя спросит: «Что, стыдно ему после автобуса на глаза показываться?». И что Шурик ответит?"
    th "Нет, нехорошо Шурика подставлять. Пойду сам."
    th "Если Женя спросит про вчерашний вечер — скажу, что извиниться хотел; если не спросит, то сам извинюсь — может, она лучше ко мне относиться будет."
    play sound dct_sfx_alarm
    play sound2 dct_sfx_horn_rise
    "Электроник улыбнулся, вспоминая тяжесть Жениной головы у себя на плече и запах её волос."
    th "Будить Шурика или нет?"
    th "Наверное, лучше всё-таки разбудить. Сегодня же первый день смены, после завтрака будет первая линейка, важные объявления и прочее. Не стоит пропускать."
    stop ambience fadeout 1
    stop sound
    stop sound2 fadeout 1

    scene dct_dream_sh_first_disert
    show dct_dream_veil at shiver
    with fade2
    play music music_list['orchid'] fadein 1
    "А Шурику снился странный сон."
    "Снилось, что он где-то в пустыне на полигоне."
    "Жёлто-бурый песок, серо-жёлтые редкие кустики, какое-то белёсое небо и неожиданно холодный и резкий, продувающий насквозь пальто, свитер, тело под пальто и свитером и летящий дальше ветер."
    "Шурик в компании нескольких военных стоит под навесом и смотрит на север, в сторону цепочки холмов, ограничивающих расстояние до горизонта парой километров."
    show dct_dream_sh_first_smoke 1 behind dct_dream_veil with dissolve
    "Что-то дымится на земле между холмами и наблюдателями."
    play sound_loop dct_sfx_UAZ_engine fadein 1
    "За спиной заводится мотор УАЗика, кто-то негромко переговаривается."
    show dct_dream_sh_first_smoke 2 with dissolve
    th "Я откуда-то знаю название: «полигон Иткуль». «Собачье озеро» — двойной обман. Ни собак, ни озера."
    show dct_dream_sh_first_smoke 3 with dissolve
    d_civ "Сейчас наша очередь."
    show dct_dream_sh_first_civilian behind dct_dream_veil at cright with dissolve
    "К Шурику обращается единственный, кроме него самого, гражданский в этой компании."
    d_civ "Вы готовы, Александр Александрович?"
    "Шурик только утвердительно кивает."
    show d_el delivery close behind dct_dream_veil:
        xcenter 0.1 ycenter 0.5
    with dissolve
    "И, словно повинуясь этому кивку, откуда-то из-за спины, со стороны тарахтящего мотором УАЗика в пустыню, в сторону холмов выходит Сыроежкин."
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
    play ambience ambience_int_cabin_day fadein 1
    el "Доброе утро, Шурик. Подъём был."
    show dct_int_house_of_el_day:
        blur 25
    show unblink
    sh "Доброе."
    show dct_int_house_of_el_day:
        blur 25
        pause 1
        linear 1 blur 0
    play sound sfx_bed_squeak1
    th "Так, очки."
    th "А что за странный сон?"
    th "Там всё выглядело так, будто и те люди, и то место мне давно знакомы."
    th "Может, сон о будущем? Теоретически, какая-то информация из будущего может просачиваться в наше время."
    th "А Сергей был в пионерской форме, потому что я ещё не представляю, каким он будет."
    th "И что за странное слово — микс?"
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5

    scene dct_int_house_of_mi_day
    show mi grin pioneer far
    show unblink
    play ambience ambience_int_cabin_day fadein 1
    $ renpy.sound.set_volume(0.5)
    play sound dct_sfx_horn_rise fadein 2    
    mi "Женечка, ты слышишь, слышишь? Горн. Настоящий, а не запись! Вчера ко мне подошёл один мальчик и попросил послушать его, как он играет."
    show mi serious pioneer far with dissolve_fast
    mi "Ну вот… А потом мы пошли к Ольге Дмитриевне, и, в общем, у нас теперь в лагере есть свой горнист. Лучше бы он, конечно, играл на трубе или на саксофоне, мы тогда смогли бы с ним что-нибудь…"
    show mi serious pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    "Женя только вздохнула. Силы рычать и ругаться на соседку закончились ещё вчера."
    "Правда, и не хотелось ни рычать, ни ругаться.{w} Хотелось убежать."
    th "Надеюсь, она не станет записываться в библиотеку?"
    stop sound fadeout 1.5
    show mi upset pioneer far:
        alpha 0
        linear 1 alpha 1
    mi "…а здесь играет только Алиса, я видела у неё гитару. И ещё в кружке в журнале выдачи записано, что одна гитара на руках у физрука."
    show mi shy pioneer far with dissolve_fast
    mi "Как ты думаешь, Женечка, может, физрук тоже играет? Он славный дядька, было бы здорово, если бы он играл…"
    show mi shy pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    th "Я завидую Мику. Вчера только мельком познакомилась с человеком и уже знает, что тот славный дядька. А тут…"
    th "Вот тот, Сыроежкин его фамилия, он какой? Он ведь действительно, наверное, просто не хотел меня будить."
    th "Эх, а он придёт, а я буду стесняться, и мне будет стыдно того, что я стесняюсь, и я опять начну на него кричать. Хоть бы помог кто. Подвёл бы его ко мне и сказал: «Женя, познакомься, это… Сергей». Тогда я бы, может, так не стеснялась."
    show mi scared pioneer far:
        alpha 0
        linear 1 alpha 1
    mi "…а ещё этот, Сыроежкин Серёжа. Он ведь тоже играть умеет, на ксилофоне. У меня в кружке даже ксилофон есть, но Серёжа отказался почему-то, даже показалось, что убежал от меня. Неужели я такая страшная?.."
    show mi scared pioneer far:
        alpha 1
        pause 0.5
        linear 2.5 alpha 0
    th "А мне вот убежать некуда."
    th "Вот должна была Саша со мной жить, а Мику — с Леной, но Лена, наверное, в автобусе ещё с Сашей договорилась, и они с Мику поменялись."
    th "А я согласилась, я ещё не знала, что меня ждёт."
    show mi normal pioneer far:
        alpha 0
        linear 1 alpha 1
    pause 1
    mz "Мику, я умываться."
    show mi smile pioneer far with dissolve_fast
    mi "…Женечка, подожди, я тоже ещё не умывалась. А тут двое октябрят подходили, спрашивали про кружок, но я совсем не знаю, как с маленькими обходиться. Может быть, у тебя в библиотеке есть какие-нибудь методички? Я бы записалась…"
    th "Господи! Нет!"
    stop ambience fadeout 1
    $ renpy.sound.set_volume(1.0)

    scene bg int_dining_hall_people_day with dct_fade
    play ambience ambience_dining_hall_full fadein 1
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
    mt "В начале смены они все всегда рассаживаются по отрядам и по домикам."
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
    play sound "<from 1.2>" + dct_sfx_chair 
    show mt normal pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter -0.25
    pause 1.2
    show mt rage pioneer behind dct_int_dining_hall_table_day_chairs:
        xcenter -0.2 ycenter 0.29
        linear 0.6 xcenter 0.12
    pause 0.6
    mt "Внимание, пионеры! В одиннадцать ноль-ноль линейка, сбор на площади! Кто опоздает — тот первый в очереди на дежурство в столовой!"
    show mt normal pioneer with dissolve_fast:
        ycenter 0.32
    mt "Семён, Ульяна, особенно Семён. Надеюсь, смена обойдётся без ваших импровизаций. А то я не могу ни одну смену согласно Плану мероприятий провести."
    show mt normal pioneer:
        linear 2.5 xcenter 1.2
    pause 2.5
    me "Вот ведь — ментор-ментором, а помнит."
    show d_sf sad sport with dspr
    me "А я когда-то в первый раз сымпровизировал — всего лишь сбежал из лагеря на лодке, чтобы вырваться из этого бесконечного лета."
    me "И с тех пор только и делаю, что импровизирую, чтобы не провалиться в это лето обратно. Надоело до чёртиков, я же ленивый. Знал бы, что так будет — может, и не побежал бы никуда."
    show d_sf normal sport with dspr
    me "Но тогда тебя бы не встретил."
    me "Хотя нет. Тебя бы встретил."
    show d_sf smile sport
    show d_us smile sport
    with dspr
    me "Наш мирок слишком маленький для того, чтобы мы проскочили мимо друг друга."
    stop ambience fadeout 1

    scene dct_int_dining_hall_table_day_back
    show dct_int_dining_hall_table_day_chairs
    show el normal pioneer close:
        xcenter 0.41 ycenter 0.47
    show sh serious pioneer close:
        xcenter 0.74 ycenter 0.47
    show dct_int_dining_hall_table_day_front
    with dct_fade
    play ambience ambience_dining_hall_full fadein 1
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
    show el serious pioneer close with squares
    el "Ну… Можно было бы робота достроить. Я в кружке видел туловище безголовое — видимо, прошлая смена не доделала."
    sh "Робота достроить…{w} Знаешь, Сергей, мне нужно подумать над этим. Ты, сходи, пожалуйста, на линейку один. У меня, кажется, родилась идея, которую нужно срочно обдумать. Если что, я буду в кружке."
    show el laugh pioneer close with dspr
    el "Конечно, Шурик. Не беспокойся, я тебя от вожатой прикрою!"
    stop ambience fadeout 1

    scene bg ext_square_day with dct_fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list['i_want_to_play'] fadein 1
    show dv normal pioneer far behind el:
        xcenter 0.2 alpha 0.0
        pause 0.3
        linear 0.5 alpha 1.0
    show d_ma normal pioneer:
        zoom .75 xcenter 0.4 yalign 1.01 alpha 0
        pause 0.3
        linear 0.5 alpha 1.0
    dv "В общем, так, Максим: ты теперь первый кандидат в старший отряд."
    dv "Лет тебе не меньше, чем было Ульяне, так что всё нормально."
    show dv grin pioneer far with dissolve_fast
    dv "Мы тебя ещё пронаблюдаем, а в субботу на сборе отряда решим положительно."
    dv "С Женей и кибернетиками, я думаю, проблем не будет, заместитель вожатой — за, вожатую убедим. Если отряд будет за, то в понедельник объявим на линейке о переводе."
    show dv normal pioneer far with dissolve_fast
    dv "А где жить тебе — это будем думать. Наверное, можешь и по-прежнему, с Витькой в домике. Хотя и положено старших со старшими селить, но…"
    show d_sf smile sport:
        xzoom -0.75 yzoom 0.75 xcenter 0.8 ycenter 0.56 alpha 0.0
        pause 0.3
        linear 0.5 alpha 1.0  
    me "Сам понимаешь, соседство с Алисой тебя до добра не доведёт. Она тебя плохому научит."
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

    scene bg ext_square_day
    show mt smile panama pioneer close
    with dct_fade
    play ambience ambience_camp_center_day fadein 1
    mt "Лагерь, на линейку — становись!"
    "Электроник поколебался несколько секунд, решая, где ему встать: так, чтобы ему было удобнее самому смотреть на Женю, или чтобы Жене было удобнее видеть его, и встал в первой шеренге, рассудив, что сейчас важнее самому понравиться девушке."

    scene dct_lineup_two_lines with dissolve
    "А Женя всю линейку поглядывала в сторону нестриженого затылка Электроника и злилась:{w} на себя — за то, что так и не решилась извиниться за скандал в автобусе,{w} на Электроника — за то, что тот сам до сих пор не подошёл к ней,{w} на окружающих — за то, что никто ещё не догадался познакомить её с кибернетиком."
    mz "\~ Да хоть бы просто поговорить подошёл. Хоть спросил бы о том, когда библиотека открывается. \~"
                                                                                                                              
    stop ambience fadeout 1
    stop music fadeout 1

    scene bg int_library_day
    show d_mz angry glasses pioneer at center
    with dct_fade
    play ambience ambience_library_day fadein 1
    play music music_list['your_bright_side'] fadein 1
    "Женя сидела в библиотеке и рычала на пионеров."
    "Сегодня всему лагерю нужны были подписи в обходных листах. Всем шестидесяти с лишним пионерам."
    "И все они решили собрать эти подписи ещё до обеда, чтобы после обеда бездельничать с чистой совестью."

    scene int_library_day:
        zoom 1.25 xalign 0.0 ycenter 0.6
    show d_mz normal glasses pioneer close:
        xcenter 0.5 ycenter 0.53
    with dissolve
    th "Шестьдесят человек за два часа. Как я никого не покусала ещё?"
    th "Можно наводить порядок после прохода Орды. Всё поправить, расставить по местам, пол помыть."
    play sound sfx_knock_door7_polite
    pause 1
    play sound sfx_door_squeak_light
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
    th "Накричала. Выражение лица «Всех ненавижу!». Лохматая, вихор этот чёртов! Очки на нос сбились! Лицо раскраснелось, рубашка выбилась из-под пояса, один гольф сполз до половины и — стыдоба какая! — перекрученная юбка!"

    scene dct_int_library_standing_desk_back
    show el sad pioneer:
        xcenter 0.5 ycenter 0.46
    show dct_int_library_standing_desk_front
    with squares
    play sound "<from 1.2>" + dct_sfx_chair 
    th "Так, быстро за стол, пока он не разглядел во всех подробностях такое позорище!"
    el "Я… Вот, обходные."
    mz "Записываться будешь?"
    th "Господи, ну почему он пришёл именно сейчас?"
    show el normal pioneer with dissolve_fast
    el "Д-да."
    mz "Заполняй! Фамилия, имя, возраст, отряд. Внизу распишись…"
    mz "…сейчас брать книги будешь?"
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
    extend " И приходи после обеда — посмотрим, что есть в фондах."
    play sound sfx_close_door_1
    hide el with dissolve
    $ renpy.music.set_volume(1.0, delay=3)  # Возвращаем музыку обратно
    th "Ну почему? Почему я такая дура? Почему я даже нормально поговорить с человеком не могу? Сразу начинаю ругаться."
    th "Но этот-то тоже хорош."
    extend " Стоял и пялился."
    extend " На что?"
    $ renpy.sound.set_volume(1.0)

    scene dct_int_mirror_in_library
    show d_mz in_mirror shyangry glasses at center:
        xzoom -1.0
    with squares
    "Женя поправила злополучную юбку, натянула сползшие гольфы, заправила рубашку и завязала по новой галстук."
    show d_mz smile2 glasses pioneer with dspr
    "Некоторое время боролась с торчащим вихром, потом обречённо махнула на него рукой."
    show d_mz sad glasses pioneer at center with dissolve:
        xzoom -1.0
    mz "Поздравляю вас, Евгения: вы страшная, никому не интересная и не нужная."
    mz "И сидеть вам в библиотеке до самой старости, потому что никому вы не нужны."
    show d_mz bukal glasses pioneer with dspr
    mz "Ну, значит, и вам никто не нужен. Значит, мы с вами обойдёмся!"
    show d_mz amazed glasses pioneer with dspr
    "Показалось, что в конце этого монолога кто-то хихикнул под самым окном."
    hide d_mz with dissolve
    "Женя бросилась к окну и выглянула наружу — никого."
    "Кусты через дорогу подозрительно качались, но добежать туда «шпион» не успел бы."

    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
    th "Он обходные забыл. Вернётся — отдам."
    th "Придётся мыть пол вместо обеда. А то после обеда Сергей придёт, а у меня грязно, как в подземном переходе. Если придёт после всего."
    stop ambience fadeout 1
    stop music fadeout 1

    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show d_sf normal pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show mt normal pioneer close:
        xcenter 0.74
    show dct_int_dining_hall_table_day_front
    with dct_fade
    play ambience ambience_dining_hall_full fadein 1
    mt "Семён, что ты думаешь о Максиме? О том, чтобы перевести его в старший отряд?"
    "Вопрос был задан, будто и не было утреннего разговора.{w} Впрочем, с точки зрения ментора разговора действительно не было."
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
    play sound "<from 1.2>" + dct_sfx_chair 
    show mt normal pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.9 xcenter 1.25
    "Взяв стакан чая, вожатая подсела за столик к кибернетикам."

    scene bg int_dining_hall_people_day with dissolve
    "А Семён отнёс посуду на мойку, покрутил головой и, не обнаружив Ульяны, пошёл к себе."
    stop ambience fadeout 1

    scene dct_ext_сentral_alley_from_dining_hall_to_west with slideawayleft:
        walking
    play sound_loop ambience_camp_center_day fadein 1
    play sound_loop2 sfx_far_steps
    "Действительно, нужно было решить, кого из мелких перевести в средний отряд на освобождающееся место Максима, а для этого нужно было посоветоваться с теми мелкими, которые не спят."
    "В отличие от старшего и младшего отрядов, средний, пионеры в котором не просыпались никогда, права голоса здесь не имел."
    stop sound_loop fadeout 1
    stop sound_loop2

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
    play music music_list['farewell_to_the_past_full'] fadein 2
    "В итоге, когда после первой в смене тренировки пятеро мелких: Вася, Гриша, Оксана и Сергей Зайцевы и Геля, устроившись на футбольной трибуне, выбрали Васю, Семён огорчился."
    "Он ждал именно этого результата, но всё равно огорчился. Вот так — прощай, Вася."
    "Через неделю вожатая объявит о переводе, ещё неделю ребята отгуляют в своих отрядах, а на следующий цикл уже приедут в новом качестве."
    "И не спящий сейчас Васька будет неизвестно сколько жить двухнедельными циклами, пока не перейдёт в старший отряд, и ещё неизвестно сколько в нём, пока не проснётся."
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
    extend ", нет — троих, ещё и брата её."
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
    d_va "У меня ещё две недели здесь."
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
    stop music fadeout 1
    
    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show d_el smile2 pioneer close as el:
        xcenter 0.41 ycenter 0.47
    show sh normal pioneer close:
        xcenter 0.74 ycenter 0.47
    show dct_int_dining_hall_table_day_front
    with blinds
    play ambience ambience_dining_hall_full fadein 1
    play sound "<from 0.5>" + dct_sfx_chair 
    show mt normal pioneer close behind dct_int_dining_hall_table_day_front:
        xcenter -0.25 ycenter 0.23
        linear 0.6 xcenter 0.07
        linear 0.5 ycenter 0.5
    pause 1.1
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
    el "Ведь запись хорошо слышно из всех динамиков, а горниста — только на площади."
    show mt smile pioneer close with dspr
    mt "Вот об этом я и хотела с вами поговорить."
    mt "Ваш кружок — он официально называется «Кружок кибернетики, робототехники и радиоэлектроники», я правильно помню?"
    show sh normal pioneer close with dspr
    show mt normal pioneer close with dspr
    mt "…В общем, задание вашему кружку. Сделать так, чтобы, начиная с завтрашнего утра, сигналы горниста были слышны изо всех динамиков по всему лагерю. Усилитель вы знаете где, что ещё нужно спаять — разберётесь."
    show el surprise pioneer close with dissolve_fast
    el "Но Ольга Дмитриевна… У нас же программа, у нас же робот…"
    show el sad pioneer close with dspr
    show mt smile pioneer close with dspr
    mt "Вот наладите трансляцию, и занимайтесь вашим роботом сколько душе угодно."
    play sound "<from 1.2>" + dct_sfx_chair 
    show mt smile pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter -0.25
    pause 1.5
    show sh normal_smile pioneer close with dissolve_fast
    sh "Ну что, пойдём посмотрим, что можно сделать."
    stop ambience fadeout 1

    scene bg ext_square_day
    show el serious pioneer:
        xcenter 1.42
        easein 3 xcenter 0.42
    show sh serious pioneer:
        xcenter 1.72
        easein 3 xcenter 0.72
    with slideawayright
    play sound_loop ambience_camp_center_day fadein 1
    play music music_list['everyday_theme'] fadein 1
    "По дороге в кружок Сыроежкин то и дело останавливался и оглядывался куда-то через правое плечо."
    show el normal pioneer with dissolve_fast
    show sh normal pioneer with dspr
    sh "Тебя что-то беспокоит?"
    el "Да понимаешь, я в библиотеке не успел подписать наши обходные, как раз на обед просигналили. И заведующая библиотекой сказала, что будет ждать после обеда."
    show d_el shy3 pioneer as el with dspr
    el "А Женя — она такая строгая, я не хочу, чтобы она ругалась потом, если я не приду. И вожатой обходные без её подписи не отдашь."
    sh "Ладно уж, иди. Со схемой я сам управлюсь."
    show el smile pioneer with dspr
    sh "После ужина корпус делать будем, тогда приходи."
    el "Спасибо, Шурик. Я обязательно буду."
    stop sound_loop fadeout 1
    stop music fadeout 1

    scene bg int_clubs_male_day
    show sh serious pioneer close:
        xcenter 0.72 ycenter 0.70
    with dct_fade
    play ambience ambience_clubs_inside_day fadein 1
    "Шурик сидел за столом перед горкой радиодеталей, высыпанных из фанерного ящика, и выбирал необходимые, сверяясь с наскоро нарисованной схемой."
    "Плата, прорисованная нитрокраской на фольгированном гетинаксе, уже лежала в фотокювете, залитая раствором."
    "Простая и понятная работа нравилась хотя бы тем, что отвлекала от ненужных мыслей и непонятных, всплывающих перед глазами образов незнакомых людей."
    "Монолог Сыроежкина о перспективах робототехники работал бы не хуже, но Сергея пришлось отпустить."
    show sh normal pioneer close with dspr
    "Шурик пожал плечами. В конце концов, любой человек имеет право на личную жизнь."
    dreamgirl "Даже лаборант-микс?"
    show sh serious pioneer close with dspr
    sh "Любой."
    $ renpy.sound.set_volume(0.3)
    play sound sfx_suspence_bang
    show sh scared pioneer close with dissolve_fast
    sh "Эй, ты кто такой?" with vpunch
    "Тишина."
    show sh upset pioneer close with dspr
    th "Плохо. Сам с собой разговариваю. Не мысленно комментирую свои действия, а именно разговариваю. Очень плохо."
    stop ambience fadeout 1
    $ renpy.sound.set_volume(1.0)

    scene bg int_clubs_male_day
    show sh serious pioneer close:
        xcenter 0.72 ycenter 0.70
    with dct_fade
    play sound_loop ambience_int_cabin_day fadein 1
    "Наконец все требуемые детали были найдены и отложены."
    show sh normal pioneer close with dspr
    "Шурик ещё раз сверился со схемой, кивнул сам себе, посмотрел, как травится плата, посмотрел на часы."
    show sh serious pioneer close with dspr
    th "Плохо, что нет ни азотки, ни хлорного железа. В медном купоросе плата травиться будет ещё часа три-четыре."
    stop sound_loop fadeout 1

    scene bg ext_dining_hall_near_day
    show dv smile pioneer:
        xcenter 0.42 alpha 0
        pause 1.5
        linear 1 alpha 1
    show d_ma normal pioneer:
        xcenter 1.25 yalign 0.02
        pause 0.7
        easein 2 xcenter 0.7
    with dct_fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list['get_to_know_me_better']  fadein 1
    "Перед самым обедом Алиса поймала Максима в дверях столовой и не терпящим возражений тоном скомандовала:"
    show dv normal pioneer with dspr
    dv "Слушай сюда, горнист. После обеда не убегай, инструктировать тебя буду."

    scene dct_ext_dining_bench_day
    show d_ma normal pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    with blinds
    "И вот «после обеда» наступило, Максим дожидался Алису, сидя на лавочке у входа в столовую и отклоняя приглашения пойти на пляж, на стадион, погулять, поиграть в карты…"
    stop music fadeout 3
    show d_ka p4 normal pioneer with dissolve:
        zoom 1.1 xcenter 1.2 ycenter 0.87
        easein 1.5 xcenter 0.6
    pause 1.2
    show d_ka p4 normal pioneer with dissolve_fast:
        zoom 0.935 xcenter 0.6 ycenter 0.97
    "Катя вышла из столовой и присела рядом."
    show d_ma shy pioneer with dspr
    "У Максима вздрогнуло сердце."
    show d_ma normal
    show d_ka p4 smile pioneer
    with dspr
    d_ka "У тебя здорово получается. Ты долго учился?"
    show d_ma smile pioneer with dspr
    d_ma "Нет, мне только Мику показала чуть-чуть, а дальше само получилось."
    show d_ka p1 smile pioneer with dissolve_fast
    d_ka "Это значит, что у тебя талант."
    show d_ma shy pioneer with dspr
    d_ka "А я вот сколько на гитаре ни учусь — не получается. Как ты думаешь, может, у меня на горне получится?"

    scene dct_ext_dining_door_day with dissolve_fast:
        anchor(0.52, 0.51) pos(0.5, 0.5)
    play music music_list['that_s_our_madhouse']
    show dv grin pioneer at cright with dissolve_fast
    dv "Катерина, это место занято!"

    scene dct_ext_dining_bench_day
    show d_ma normal pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    show d_ka p3 surprise pioneer:
        zoom 0.935 xcenter 0.6 ycenter 0.97
    show dv grin pioneer close:
        xcenter 0.88
    with dissolve_fast
    "Двусмысленная фраза оказалась понята даже более красноречиво, чем была высказана."
    show d_ka p2 angry pioneer with dissolve_fast:
        zoom 1.1 xcenter 0.6 ycenter 0.87
    "Катя поднялась, сверкнула глазами в сторону Алисы, посмотрела на Максима, словно ждала от него какой-то реакции."
    show d_ka p2 angry pioneer with Dissolve(0.0):
        easeout 1.5 xcenter 1.2
    show d_ma surprise
    show dv surprise pioneer close
    with dissolve_fast
    pause 0.1
    show dct_ext_dining_door_day:
        anchor(0.52, 0.51) pos(0.5, 0.5) alpha 0
        pause 0.5
        linear 0.5 alpha 1
    show d_ka p3 normal pioneer as d_ka2:
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
    stop music fadeout 1

    scene dct_ext_dining_bench_day
    show d_ka p3 angry pioneer:
        zoom 0.2 xcenter 0.575 ycenter 0.68
        pause 0.2
        linear 1.0 xcenter 0.7
    show dct_ext_dining_bench_day_front
    show d_ma surprise pioneer:
        zoom 0.85 xcenter 0.4 ycenter 0.75
    show dv grin pioneer close:
        xcenter 0.88
    with dissolve_fast
    "А Максим… Он просто ничего не понял."
    stop ambience fadeout 1

    scene bg ext_house_of_dv_day
    show dv grin pioneer far:
        xcenter 1.27
        easein 3 xcenter 0.57
    show d_ma normal pioneer:
        zoom 0.75 xcenter 1.5 yalign 1.01
        easein 3 xcenter 0.8
    with blinds
    play music "<from 14.5 loop 0.0>" + music_list["get_to_know_me_better"] fadein 1
    "До домика Алисы шли молча, только зашли к Максиму за горном, благо было по пути."
    show dv laugh pioneer far at center with dissolve_fast
    dv "Заходи, можешь не разуваться."

    scene bg int_house_of_dv_day
    with slidedown
    play sound sfx_close_door_campus_1
    show dv laugh pioneer at cleft
    show d_ma normal pioneer at cright:
        xcenter 0.65 yalign 0.02
    with dissolve
    pause 0.5
    show dv guilty pioneer with dissolve
    "Алиса вздохнула, глянув на пустующую Ульянкину кровать, махнула на неё рукой — садись, мол. А сама полезла искать что-то по шкафам и тумбочкам."
    hide dv with dissolve
    play sound sfx_bed_squeak1
    "Максим разглядывал домик «страшной ДваЧе» с огромным любопытством, и, кажется, увиденное ему нравилось."
    show d_ma smile2 pioneer with dissolve_fast
    "Никогда раньше он здесь не был, вообще весь средний отряд с самого первого дня знал, что с Рыжими связываться опасно, и потому избегал их внимания."
    show d_ma smile pioneer with dissolve_fast
    "А тут сразу вспомнился беспорядок в его собственном жилище."
    show dv normal pioneer behind d_ma at cleft with dissolve 
    play ambience ambience_int_cabin_day fadein 1
    stop music fadeout 1
    "Наконец Алиса нашла, что хотела: тетрадный листок с расписанием сигналов и кассету с записью горна."
    show d_ma normal pioneer with dissolve_fast
    play sound sfx_paper_bag
    dv "Вот, держи. Будешь играть по этому расписанию. Часы есть?"
    d_ma "Есть."
    dv "Хорошо, тогда первый пункт закрыли. Если проспишь — накажу."
    show d_ma serious pioneer with dissolve_fast
    dv "Сейчас пойдёшь в музыкальный кружок, там прослушаете с Мику запись, потом ты ей сыграешь. Если что, она подскажет, что и как."
    dv "И третье: вожатая согласна на твой перевод в старший отряд. Через неделю на линейке объявит, если ничего не изменится."
    dv "Но не думай, что у тебя какие-то права появятся после этого. Обязанности уже появились, а права — ещё нет."
    show d_ma surprise pioneer with dissolve_fast
    dv "Следующую неделю будешь ещё числиться в среднем отряде, а в старшем — только кандидатом."
    dv "Жить будешь на старом месте, а на линейке и в столовой со следующей недели будешь со старшим отрядом."
    show dv smile pioneer with dspr
    dv "Короче, прав будет как у маленьких, а бить будем как взрослого."
    dv "А уж в следующую смену — добро пожаловать. Вопросы есть?"
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
    play sound sfx_close_door_campus_1
    pause 0.2
    show dv laugh pioneer with dissolve_fast
    play sound [ "<silence 1.0>", sfx_bed_squeak2 ]
    "Подзатыльник своей цели так и не достиг, но Алису это нисколечко не заботило. Она вернулась на кровать, откинулась на спину, на подушку, и беззвучно расхохоталась. Кажется, серая полоса в жизни заканчивалась."
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5

    scene dct_int_library_standing_desk_back:
        zoom 1.4 xcenter 0.3 ycenter 0.1  rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show dct_int_library_standing_desk_front:
        zoom 1.4 xcenter 0.3 ycenter 0.1 rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show dct_library_door_window_el:
        zoom 1.4 xcenter 0.3 ycenter 0.1 rotate -30 blur 20 transform_anchor True
        easein 1.4 zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0 blur 0 transform_anchor True
    show unblink
    play ambience ambience_library_day fadein 1
    play sound sfx_knock_door7_polite
    play music music_list['your_bright_side'] fadein 2.5
    pause 1.5
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
    stop ambience fadeout 1
    stop music fadeout 1

    scene bg ext_path2_day with slideawayright:
        walking
    play ambience ambience_forest_day fadein 1
    play sound_loop dct_sfx_grass_steps
    th "Ну вот, опять не решился заговорить с девушкой."
    th "Неудивительно, что она на меня рычит."
    th "Она думает, что я в автобусе к ней специально приставал, может, думает, что я и в библиотеку хожу, чтобы издеваться над ней?"
    th "Может, над ней все смеются?"
    stop sound_loop

    scene bg ext_path2_day
    play sound dct_sfx_fallen_book
    "Что-то толкнулось в ноги."
    stop ambience fadeout 1
    play music music_list['always_ready'] fadein 1
    scene dct_cg_foots_and_ball with pushup
    "Электроник опустил глаза — мячик."
    "Незаметно для себя Электроник вышел к западному краю футбольного поля."

    scene bg ext_playground_day with pushdown
    d_guys "Сыроежкин!{w=0.5} Пни мячик!"

    scene dct_cg_el_kick_ball with squares
    pause 0.5
    $ renpy.sound.set_volume(1.5, delay=0)
    play sound sfx_soccer_ball_kick
    pause

    scene bg ext_playground_day with squares
    $ renpy.sound.set_volume(1.0, delay=0)
    d_guys "Эй, давай с нами!"
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
    "Игра помогла хотя бы тем, что отодвинулись назад грустные мысли. Некогда было думать о Жене — если уж взялся играть, то надо было играть в полную силу. И, конечно, не замыкаться в своих переживаниях."
    stop ambience fadeout 2
    hide dct_el_running_back_and_forth with dissolve
    show d_el normal shorts at center with dissolve
    pi4 "Серёга, ты же хорошо играешь. Охота тебе в своём кружке лето просиживать? Может, свою команду организуем?"
    show d_el smile shorts with dspr
    pause 0.6
    show d_el laugh shorts with dissolve_fast
    "Электроник оглянулся, прежде чем ответить, и неожиданно упёрся взглядом в Женю."
    stop music fadeout 2.5

    scene dct_ext_playground_opposite_gate_day
    show mz normal glasses pioneer close at fleft
    with dissolve
    play ambience ambience_camp_center_day fadein 2
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

    scene dct_int_sporthall with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    "Семён подошёл к тренерской и, услышав из-за двери голоса, задержал руку на дверной ручке."
    th "Ульяна и кто?"
    th "Интересно…"

    scene dct_int_coaching_room2
    show us laugh sport close at center:
        zoom 1.25 anchor(0.52, 1.0) pos (0.5, 1.15)
    with vpunch
    play music music_list['i_want_to_play']  
    "Он потянул дверь и чуть не упал от внезапной тяжести — повисшей на плечах Ульянки-младшей. Ульянки из его родного лагеря."
    show us surp1 sport close at center with dissolve_fast:
        zoom 1.0 anchor(0.5, 0.5) pos (0.5, 0.5)
    us "Я соскучилась, братишка!"

    scene dct_int_coaching_room3
    show d_sf laugh sport:
        zoom 0.75 xcenter 0.37 ycenter 0.56
    show d_us smile sport:
        xcenter 0.75 ycenter 1.15
    show us grin sport:
        xcenter 0.48
    with dissolve
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
    stop ambience fadeout 1
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ set_mode_nvl()
    window show

    scene bg int_clubs_male2_night with dissolve_fast
    play ambience ambience_clubs_inside_day
    $ set_mode_nvl()
    "Шурик закончил паять микрофонный усилитель, отодвинул паяльник, посмотрел ещё раз на схему, чуть качнул головой, подумал, что если бы сначала рассортировал имеющиеся детали, то можно было бы сделать и поизящнее.{w} Зато сейчас получилось просто и надёжно.{w} Тем более что задача стояла усиливать всего лишь звуки горна и транслировать их на развешанные на фонарных столбах динамики."
    "\nПодключил микрофон, подключил к выходу наушники, постучал пальцем по микрофону, потом свистнул в него.{w} Удовлетворённо кивнул, видя, как дёрнулось зелёное пятнышко на экране осциллографа.{w} Осталось только согнуть корпус из листа алюминия, но это уже работа для Сыроежкина.{w} У самого Шурика так аккуратно и точно, как у компаньона, работать с металлом ни за что не получится.\n"
    th "После ужина нужно будет закрепить коробочку с усилителем на одном из флагштоков, отдать горнисту микрофон со шнуром и протянуть провод от усилителя к радиорубке.{w} Почему-то вожатая настаивала на том, что горнист должен подавать сигналы обязательно с площади."
    nvl hide dissolve
    nvl clear    

    scene black with dissolve_fast
    window hide

    scene bg int_clubs_male_day
    show sh serious pioneer close at cright
    with dissolve_fast
    $ renpy.sound.set_volume(0.3)
    play sound dct_sfx_clang
    $ set_mode_adv()
    window auto
    "Шурик выволок из кладовки лист алюминия, положил его на верстак, достал со шкафа годовую подшивку журнала «Радио» и устроился ждать Сыроежкина."
    show sh serious pioneer close:
        linear 0.5 ycenter 0.70
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Чуть слышно потрескивал паяльник, остывая, гудел трансформатор, выдавая положенные тридцать шесть вольт, за окном чирикали воробьи и хлопали чьи-то крылья, покрупнее воробьиных."
    stop ambience
    $ renpy.sound.set_volume(1.0)

    scene black with dissolve_fast
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    pause 0.5
    play sound dct_sfx_robot_run_club_attic fadein 1.5
    pause 0.8
    stop sound fadeout 1.5

    scene bg int_clubs_male_sunset
    show sh surprise pioneer close at cright:
        ycenter 0.70
    with dissolve_fast
    play sound_loop ambience_int_cabin_evening fadein 1
    "Когда незаметно для себя Шурик начал задрёмывать, вдруг показалось, что прямо над головой по чердаку пробежал кто-то лёгкий."
    show sh normal pioneer close with dspr
    "Шурик вскинулся, покрутил головой, прислушался — тишина."
    hide sh with dissolve
    "Отложил журналы в сторону и, заинтересовавшись, вышел на улицу."
    stop sound_loop fadeout 1
    play sound sfx_open_door_clubs_2

    scene dct_ext_clubs_sunset:
        zoom 1.05 align(0.5, 0.0)
    show 3500_sh normal pioneer as sh:
        zoom 0.26 xcenter 0.58 ycenter 0.68
    show dct_ext_clubs_day_el_look_at_roof as el
    with slideawayup
    play ambience ambience_camp_center_evening fadein 1
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
    stop ambience fadeout 1

    scene dct_ext_washstand_sunset
    show mt angry panama pioneer far:
        xcenter 0.45 ycenter 0.50
    show us shy sport far:
        xcenter 0.56 ycenter 0.50
    with dct_fade
    play music littleidea fadein 1
    "Ульянка-младшая всё-таки не успела уйти до ужина, не попавшись на глаза вожатой."
    show d_sf normal sport behind mt:
        zoom .75 xcenter 0.3 ycenter .56
    show d_us normal sport behind mt:
        zoom .75 xcenter 0.7 ycenter .76
    with dissolve
    show d_mt shocked panama pioneer far as mt
    show us surp1 sport far
    with dspr
    "Пришлось физрукам врать Ольге Дмитриевне и выручать гостью — пришлось выдавать её за сестрёнку, прибежавшую погостить."
    show mt surprise panama pioneer far
    show us laugh2 sport far
    with dissolve_fast
    "Пришлось сказать, что родители тут недалеко, ниже по течению, стоят с палаткой."

    scene dct_int_dining_hall_people_sunset with wipeleft
    "Пришлось кормить ужином."
    show mt smile pioneer close with dissolve
    mt "Это, конечно, нарушение режима, но не могу же я оставить гостью голодной!"
    hide mt with dissolve
    "Пришлось обещать, что родители тоже придут."

    scene bg ext_square_sunset with wipeleft
    "Пришлось знакомить со всем лагерем, объясняя одним — одно, а другим — другое."

    scene dct_ext_music_club_sunset with wipeleft
    "Пришлось вести вечером в музыкальный кружок, к Мику на чаепитие."
    $ persistent.sprite_time = "sunset"    # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Надо было видеть потеплевшие глаза Алисы — Ульяна-большая даже заревновала чуть-чуть."
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ night_time()
    $ persistent.sprite_time = "night"

    scene bg ext_playground_night with dissolve_fast
    play ambience ambience_camp_center_night fadein 1
    play music peritune_gentle_theme_piano fadein 1
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
    us "Очень красиво…"

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
    us "Это здесь."
    us "Видишь — вот трава, а вон жучки эти ползают. Они всегда в местах перехода обитают."
    show us sad sport with dspr
    us "Жалко, что я провести вас не смогу, это вам самим научиться нужно."
    "Света, падающего из окон музыкального кружка, хватало, чтобы рассмотреть и траву, и жучков."
    show us normal sport with dspr
    "В кружке Мику, сидя за роялем, объясняла что-то Максиму, держащему в руках горн. Нет, не горн, а другой инструмент. Похожий на трубу, но покороче и с более широким раструбом."
    show d_us smile sport with dspr
    us_old "\~ Пропал Макс. \~"
    show us grin sport with dspr
    us "Ну, пока, сестрёнка, до послезавтра. Все вас очень ждут."
    show d_us normal sport with dspr
    us_old "Пока."
    show us smile sport with dspr
    us "Значит, смотри, показываю."
    us "Вот трава, вот жучки эти. Это значит, место перехода здесь."
    show us normal sport with dspr
    us "Потом ты закрываешь глаза и представляешь себе человека, к которому хочешь попасть. И всё."
    us "Нужно только очень сильно хотеть. Делаешь шаг вперёд — и ты на месте."
    window hide
    play sound [ "<silence 0.3>", sfx_uliana_jumps_down ]
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
    window hide
    $ renpy.music.set_volume(0.3, delay=1.5, channel='ambience')
    show black with dissolve
    pause 0.5
    $ renpy.music.set_volume(1.0, delay=1.5, channel='ambience')
    pause 0.5
    hide black with dissolve
    window auto
    "Открыла глаза.{w} Ничего не изменилось."
    "Никуда Ульяна не переместилась."
    show d_us sad sport with dspr
    th "Видимо, это не всем дано. Наверное, придётся как в прошлый раз — ногами топать."
    show d_us smile sport with dspr
    show dct_ext_musclub_backside_night_ma_mi:
        linear 3.5 alpha 0
    "Вспомнила ещё, как показалось на секунду, что в момент кувырка младшей на неё из кустов с противоположной стороны поляны глянули как будто два жёлто-зелёных глаза, принадлежащих очень большой кошке."
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
    
    
    
#####################
#Глава 3. Отклонение#
#####################

label dct_fluctuation_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Отклонение"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава III. Отклонение" at truecenter with dspr
    play ambience ambience_int_cabin_day fadein 2
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    $ renpy.pause(0.2)

    scene dct_int_house_of_mi_day with blinds
    play sound dct_sfx_horn_rise_through_loudspeaker fadein 1.5 
    "Женя на этот раз первой услышала горн: непривычно громкий, прямо над ухом. А только потом уже щебетание соседки."
    show mi smile pioneer with dissolve
    mi "Женя, Женечка. Ты слышала? Всё очень даже неплохо. Я так переживала, что не могу Максиму ничего толком показать, я ведь горн даже в руках никогда не держала. А ещё Максима хотят в наш отряд перевести, Женечка, ты же не против?"
    mz "Не против я, не против."
    th "Господи, только помолчи ты хоть две минуты!"
    show mi cry_smile pioneer with dissolve
    mi "А ещё, Женечка, вот — это тебе принесли. Ты знаешь, я прямо тебе завидую, мы третий день в лагере, а тебе уже цветы дарят. А мне никто… И никому из девочек ещё… Никто…"
    mz "А ты уверена, что это мне?"
    show mi normal pioneer with dissolve
    mi "Ну, Женечка, я утром встала пораньше, чтобы послушать, как будет играть Максим. Вышла на крыльцо. Ещё подумала, не забыл ли он горн у меня в кружке?"
    mi "Потому что если забыл, значит, ему придётся срочно бежать в кружок, а ключи только у меня, вожатой и Алисы. А ты же знаешь вожатую и Алису, и Максим их знает, значит, он прибежит сюда. И я хотела сразу вернуться в домик за ключами, и тут увидела на крыльце…"
    mi "Женечка, я думала, это мне, но это тебе. Мне бы ноты положили…"
    "Действительно, на столе рядом лежали букет ромашек и чистый бланк библиотечного формуляра."
    show mi smile pioneer with dissolve
    mi "Женечка, я умываться. Тебя подождать?"
    mz "Н-нет. Ты иди, я попозже."
    play sound sfx_close_door_campus_1
    hide mi with dissolve
    "А как только Мику ушла, Женя начала рвать этот формуляр. Пополам, потом ещё пополам, потом ещё, пока хватало сил в пальцах. Хотела выкинуть букет, но остановилась — цветы ни в чём не были виноваты. Поэтому в пустую молочную бутылку была налита вода, и цветы заняли место на столе."
    th "Сейчас приду в библиотеку, а там ещё один букет. А после обеда или после ужина — записка, приглашение на свидание. А вечером вместо свидания будут всеобщие смех и веселье над одиноко сидящей Женей, ждущей непонятно чего."
    play sound sfx_open_cupboard
    show dct_mz_mirror bukal with squares
    th "Потому что кто будет звать такую, как я, на свидание? А если и будет, то с какой целью? Посмеяться? А если действительно на свидание? Кому я нужна такая? Сыроежкину?"
    show dct_mz_mirror normal with dspr
    th "Плохо, если так. Надо признаться самой себе — он мне нравится. Но здесь есть миллион девочек красивее и лучше меня. Нет, именно потому, что он мне нравится, ничего у нас не будет."
    th "Или это чернявый. Юморист из среднего отряда. Как его — Витька, кажется, пошутить решил? Какая разница? Может, мальчики тут и вовсе ни при чём. Девочки издеваются ещё изобретательнее. Проходили, знаем."
    show dct_mz_mirror bukal with dspr
    "То, что все эти «проходили, знаем» были воспоминаниями других людей, прочитанными, обработанными и записанными Системой в память заведующего библиотекой микса, ничего опять же не меняло."
    hide dct_mz_mirror with squares
    th "Я жду, что люди будут относиться ко мне так, как я к ним отношусь. Мне не надо, чтобы лучше. Мне достаточно так же."
    stop ambience fadeout 1

    scene dct_ext_square_profile_view_day with dct_fade
    play music music_list['afterword'] fadein 3
    "Максим, сидя напротив памятника, ждал начала линейки. Из-за новых обязанностей приходилось уже второе утро вставать на полчаса раньше и постоянно следить за временем."
    "Но зато эти обязанности освободили его от всех отрядных мероприятий и обеспечили пропуск в старший отряд."
    "Максим, правда, не понял ещё, последнее — это хорошо или плохо: с одной стороны, никто не контролировал, как он проводит время и не заставлял ходить строем, а с другой, он уже дважды за сутки успел получить втык — от вожатой и от Алисы."

    scene anim prolog_1 with fade
    show mt angry pioneer with dissolve
    mt "Ты, кажется, горнист?"
    th "Будто не сама же назначила."
    mt "Вот и занимайся, а не валяйся в домике. Или можешь со своим отрядом идти и к смотру строя и песни готовиться!"
    hide mt with dissolve
    "Вот уж от чего избавь бог, так это от этого смотра. Пришлось взять кассету и отправляться в музыкальный кружок к Мику. А в кружке в присутствии Алисы назвал Ульяну Ракетой. А что? Её все так зовут. Оказалось, не все."
    show dv normal pioneer behind dct_dream_veil with dissolve
    dv "Понимаешь, Максим…"
    dv "Tы у себя в отряде мог называть нас, как хочешь — это было смешно, это вот как маленькие дети пришивают себе на рубашку нарисованные погоны и воображают себя генералами."
    dv "А вот когда взрослый выдаёт себя за генерала, ему приходится соответствовать. Или его за это наказывают. У нас погон нет, но эти прозвища — это как знаки отличия, которые заслужить надо."
    dv "Помнишь, я тебе про Семёна и Сеньку вчера говорила? Так что и тебе надо ещё «Макса» заслужить и право звать Ульяну иначе, чем Ульяной, заработать."
    hide dv with dissolve
    show mi normal pioneer behind dct_dream_veil with dissolve
    "Мику — вот та оказалась гораздо более приветливой девушкой. Правда, настояла, чтобы Максим обязательно попробовал сыграть на… на корнете — так, кажется, а других духовых инструментов в кружке не оказалось."
    "Оказалось, правда, что подавать сигналы с помощью горна — это одно, а играть, чтобы получалась музыка — совсем другое. Разница примерно как между художником и мастером нанесения дорожной разметки."

    scene bg ext_square_day
    show d_vi smile pioneer:
        xcenter 0.39
    show d_ka p3 smile pioneer2:
        zoom 1.1 xcenter 0.2 ycenter 0.87
    with fade
    "Со стороны клубов на площадь вышли Катерина и Витька, сосед по домику. Катерина мазнула глазами по Максиму и повернулась к Витьке, о чём-то его спрашивая."
    show d_ka p3 smile pioneer2:
        ease 0.4 xcenter 0.24
    show d_ka p3 laugh pioneer2 with dspr:
        ease 0.4 xcenter 0.24
    "Витька ответил, глупо улыбаясь, а Катя засмеялась и взяла его под локоть."

    scene dct_ext_square_profile_view_day with dissolve
    show d_vi smile pioneer:
        zoom 0.75 xcenter -0.15 ycenter 0.642
        easein 2.2 xcenter 0.68
    show d_ka p3 laugh pioneer2:
        zoom 0.825  xcenter -0.26 ycenter 0.76
        easein 2.2 xcenter 0.57
    "Сердце Максима дёрнулось, но тут же и успокоилось, никак не реагируя на её спутника."
    show d_ka p3 artificial_smile pioneer2 with dspr
    "А Катя, внезапно перестав смеяться, уже смотрела холодными глазами куда-то в сторону столовой."
    show d_ka p2 smile pioneer2 with dissolve_fast
    pause 0.2
    show d_vi shock pioneer with dspr
    show d_ka p2 smile pioneer2:
        easeout 1.8 zoom 1.1 xcenter 1.2 ycenter 0.87
    show d_vi shock pioneer:
        pause 1.2
        easeout 1.1 zoom 1.0 xcenter 1.2 ycenter 0.713
    "Вдруг отвернулась, что-то сказав Витьке такое, что его лицо удивленно вытянулось, высвободила руку, опять мазнула глазами по Максиму и величественно удалилась."
    show dv smile pioneer:
        xcenter -0.2
        easein 1.2 xcenter 0.3
    dv "Ну что расселся? Цигель ай-лю-лю! Труби сбор на линейку!"
    show black behind dv:
        alpha 0
        pause 0.5
        linear 1.5 alpha 1
    "Максим побежал к флагштокам на своё место и подумал: почему он совершенно не обижается на Алису за её, казалось бы, грубость и вчера, и сегодня? Что-то чувствовалось хорошее за её показной резкостью."
    stop music fadeout 1

    scene dct_ext_between_beach_and_boathouse_day with dct_fade
    play music music_list['your_bright_side'] fadein 1
    "Уже не первый час Электроник грустил на своём, ставшем привычным месте: на берегу между пляжем и пристанью. Сидя на наполовину занесённом песком бревне, бросал в воду камушки."
    "Было плохо. Кажется, Женя ему сегодня дала чётко и ясно понять, что его общество ей не интересно."
    window hide
    pause 0.2
    $ set_mode_nvl()
    window show
    "Начиналось утро даже и романтично: пришлось подняться в пять утра, пройти на концертную площадку и там, за сценой, нарвать ромашек, спрятаться с букетом около домика Жени и, дождавшись, когда внутри начнут ходить туда-сюда обитательницы, положить букет на крыльцо, приложив к нему украденный бланк библиотечного формуляра, чтобы девочки не гадали, кому букет."
    "\nСтрашно было не то чтобы просто подойти к Жене и заговорить с ней. Страшно было даже идти с букетом к её домику. Вдруг увидят."
    nvl clear

    scene dct_lineup_mi_not_us with blinds
    "На линейку Шурик опять не пошёл, сославшись на занятость, и Электронику пришлось одному представлять там кружок."
    "\nПотом вожатой было объявлено, что сегодня «День чистоты и порядка», что пионерам предстоит навести эти самые чистоту и порядок на территории лагеря, что кибернетики должны будут навести порядок в кружке, подмести дорожки и пройти с граблями газоны вокруг кружка."
    "\nЭто Электроник слушал краем уха — фронт работ был ясен и так. Жене досталась библиотека и всё вокруг неё."
    nvl clear

    scene bg int_library_day
    show mz normal pioneer
    with dissolve
    "И вот, когда Электроник где-то через час после завтрака в нервной трясучке прибежал к библиотеке и предложил свою помощь… Да что теперь вспоминать? В общем, отлуп, бессмысленный и беспощадный. {w}«За книгами приходи, раз уж записывался», — сказано было вдогонку, равнодушно, как к стотысячному посетителю за сегодня. Это если без подробностей, которые вспоминать не хотелось."
    window auto

    scene dct_ext_between_beach_and_boathouse_day with pixellate
    $ set_mode_adv()
    "Надо было чем-то занять себя. Идеальным было бы запереться в кружке и там что-то мастерить, пока не упадёшь от усталости, но видеть никого не хотелось, даже Шурика."
    "Под ногами валялся принесённый водой кусок сосновой коры."
    "Электроник достал из кармана перочинный нож и, примерившись, начал неспешно вырезать из коры кораблик."
    "Никогда раньше, в прошлых циклах, ни Женя так себя не вела, ни Электроник так не переживал. Что-то сместилось в них, когда Рыжие в автобусе пересадили полусонного Электроника на освободившееся место рядом с Женей, а те проснулись на плечах друг у друга."

    scene dct_int_house_of_sa_day
    show 3500_sl smile3 pioneer:
        xcenter 0.4 ycenter 0.833
    show dct_dream_veil at shiver
    with dissolve
    "Саша однажды, в один из циклов, похвалила его, когда он помогал с какой-то мелочью девочкам в домике."
    sa "Серёжа, у тебя очень умные руки. Как бы мы тебя ни отвлекали, они всё делают сами, правильно и красиво."

    scene dct_ext_between_beach_and_boathouse_day with dissolve
    "Вот и сейчас из большого куска коры выходил не просто кораблик, какие дети пускают по лужам. То, что вышло из-под его ножа, больше всего походило на «Эспаньолу» из «Острова сокровищ» — с намеченными досками обшивки, окнами на корме и трюмным люком, с палубой, опущенной ниже уровня бортов."
    "Электроник повертел бывший кусок коры в руках, отложил его в сторону и отправился к ближайшим кустам, чтобы срезать подходящие сучки — заготовки для будущих мачт и бушприта."
    th "Что вот с ней делать, когда будет готова? Сейчас доделаю и оставлю на пристани. Кто найдёт — того и будет."
    stop music fadeout 2.5
    play ambience ambience_boat_station_day fadein 1.5 
    show d_oz normal pioneer with dissolve:
        xcenter 0.31 yalign 0.28
    "Электроник оглянулся на берег: на его месте сидела девочка и вертела в руках недоделанную «Эспаньолу»." 
    show d_oz d pioneer with dspr
    el "Нравится?"
    d_oz "Да, очень всё здорово. Скажи, а ты научишь меня такие делать? Это же парусник?"
    el "А зачем тебе учиться? Этот забирай, только подожди — я его доделаю."
    d_oz "Нет, я хочу обязательно сама сделать."
    "Они ещё долго сидели рядышком. Сергей выстругивал мачты и пристраивал их к корпусу, объясняя, что и зачем он делает. Потом: «Ты же девочка, у тебя должны быть с собой иголка и нитки», — натягивал ванты. А девочка сидела рядом и внимательно следила за его руками."
    el "Ну вот, осталось паруса привязать, и всё будет готово. По воде его не пустить — опрокинется, но на полку можно поставить. Может, всё-таки заберёшь его себе?"
    d_oz "А можно? Но я всё равно хочу сама сделать."
    el "А если не тайна, скажи — зачем тебе это?"
    d_oz "Понимаешь…"
    show d_oz n pioneer with dissolve
    d_oz "Есть один мальчик, который бредит парусами. А после этой смены он всё… В общем, мы можем больше не встретиться. Я всё думала, что ему подарить, чтобы он… Ну, на память."
    d_oz "И вот, тебя увидела и придумала. Только надо обязательно, чтобы я сама всё сделала, своими руками, а то всё пропадёт."
    el "Тогда приходи завтра в кружок. Или нет, там мы Шурику будем мешать. Приходи сюда."
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ set_mode_nvl()
    window show

    scene black
    show dv angry pioneer:
        xcenter 0.5 alpha 0
        linear 1 alpha 1
    with dissolve_fast
    play music music_list['eat_some_trouble']
    "Алиса, как всегда в этот день, командовала средним отрядом."
    show ext_houses_day:
        align(0.0, 1.0) alpha 0
        linear 0.8 alpha 0.5
        easein 0.8 zoom 0.5 alpha 1.0
    show dct_ext_boathouse_day_with_pass_train:
        align(1.0, 1.0) alpha 0
        pause 1
        linear 0.8 alpha 0.5
        easein 0.8 zoom 0.5 alpha 1.0
    show ext_no_bus:
        align(0.0, 0.0) alpha 0
        pause 2
        linear 0.8 alpha 0.5
        easein 0.8 zoom 0.5 alpha 1.0
    show ext_camp_entrance_day:
        align(1.0, 0.0) alpha 0
        pause 3
        linear 0.8 alpha 0.5
        easein 0.8 zoom 0.5 alpha 1.0
    "\nСорок один бестолковый пионер должен был подмести дорожки, пристань и автобусную остановку, подкрасить гипсовых пионеров у ворот, а если нужно, то и сами ворота, ничего не поломать и не перемазаться в краске самим."
    show dct_ext_bathhouse_day with irisin
    extend " Как правило, к четырём часам все заканчивали, но приходилось устраивать дополнительный банный день, особенно для мальчиков — возможностей рукомойника явно не хватало.\n\n"
    show mt smile panama pioneer far:
        xcenter 1.15 ycenter 0.55
        easein 1.5 xcenter 0.5
    mt "А ты-то почему устала?"
    show mt grin panama pioneer far with dissolve_fast
    extend " Не ты же с метлой танцевала?"
    show mt laugh panama pioneer far with dspr
    show mt laugh panama pioneer far:
        pause 0.5
        easein 1.5 xcenter -0.15
    extend " Назначь участки, обозначь фронт работ и только ходи и контролируй."
    nvl hide dissolve
    nvl clear
    nvl show dissolve

    scene black
    show dv sad pioneer
    with dissolve
    "Вы не пробовали проконтролировать сорок одну Ульянку сразу?"
    show dv guilty pioneer with dspr
    extend " Нет, не сорок одну, конечно, Ульянка — она была уникум в этом плане, но у неё уже в том возрасте были мозги. А у этих…"
    show dv angry pioneer with dissolve_fast
    "\nВот и приходится носиться по всей территории, пресекать, где надо, и заставлять — тоже где надо."
    show dv rage pioneer as dv2 behind dv
    show d_ext_dv_hideout_day_7 behind dv2:
        alpha 0
        linear 1 alpha 1
    show dv angry pioneer:
        pause 1.2
        linear 0.2 alpha 0
    extend " Да иногда за кусты отзывать и физическим воздействием угрожать. Тогда понимают какое-то время."

    scene black
    show dv scared pioneer
    with dissolve_fast
    "\nИ это ещё они спят и алгоритмами управляются. А что будет, когда они проснутся?"
    show dv sad pioneer with dissolve_fast
    window auto
    show dct_int_coaching_room3 behind dv:
        zoom 2.5 xcenter 0.5 ycenter 0.475 alpha 0
        linear 1 alpha 1
    stop music fadeout 1
    play ambience ambience_int_cabin_day fadein 1
    $ set_mode_adv()
    "В общем, Алиса набегалась за сегодня на неделю вперёд и сейчас сидела в тренерской у Семёна и Ульяны, вытянув ноги и опиваясь чаем."

    scene dct_int_coaching_room2
    show d_us sad sport:
        zoom 0.825  xcenter 0.31 ycenter 0.78
    show d_sf normal sport:
        zoom 0.825  xcenter 0.69 ycenter 0.58
    with dissolve
    "У Алисы много чего крутилось на языке с прошлого цикла, но спрашивать и самой рассказывать она пока не была готова. Поэтому спросила о другом — о волейболе."
    show d_us laugh sport
    show d_sf smile sport
    with dspr
    us "А в самом деле — давно не играли, с прошлого цикла! Алиса, беги переодевайся, я за Леной, Мику и Сашей сбегаю."
    hide d_us with dissolve
    "И только тогда Алиса решилась чуть приоткрыться:"
    dv "Сенька, я понимаю, почему ты ничего про Шлюз не рассказываешь. Но знаешь, как мне теперь перед тобой стыдно."
    show d_sf normal sport with dissolve
    me "Алиса, я не…"
    dv "Да знаю я, что ты «не». Мне не за то стыдно, что ты мог меня голой увидеть, хоть ты и говоришь, что «не». Я тебе доверяю. А за то своё скотское состояние.{w} Ладно, побегу переодеваться. Через полчаса на площадке."
    stop ambience fadeout 1

    scene bg int_clubs_male_day with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    "Шурик, явившись утром в кружок, протёр пыль со всех приборов, достал из ящика стола общую тетрадь, достал остатки второй версии кошкоробота, вытащил на верстак все имеющиеся в наличии радиодетали, болты, гайки и всякий механический хлам и замер."
    "Нет, конечно, с самого начала было ясно, что из этого барахла ничего хорошего создать не удастся, а тем более вторую Яну. Они и первую непонятно как создали, выпаивая детали из списанных приборов."
    th "Да, чтобы из этого сделать что-то достойное, нужно быть гением."
    dreamgirl "Не обязательно. Но из этого действительно ничего сложнее ультразвуковой пугалки, мышей гонять, не спаяешь."
    "И опять Шурик сначала мысленно согласился, а потом уже вздрогнул в испуге."
    th "Надо, надо к доктору." 
    stop ambience fadeout 1

    scene bg ext_dining_hall_away_day with dissolve
    play sound_loop ambience_dining_hall_full

    scene bg int_dining_hall_people_day with dissolve
    $ renpy.pause(1.2, hard=True)
    stop sound_loop fadeout 1

    scene bg ext_clubs_day with dissolve

    scene dct_ext_glade_behind_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    "Шурик сходил на обед, удивился, не встретив там Сыроежкина, вернулся обратно и засел с тетрадью за кустами барбариса у задней стены здания клубов, чтобы попытаться составить план работы кружка кибернетики."
    "Ничего не получалось, хоть плачь."
    "С такой ситуацией Шурик ещё не сталкивался. Стоило занести ручку над тетрадным листом, как в голове всплывала эта фраза:"
    dreamgirl "Ничего сложнее пугалки не спаяешь."
    th "Звучит словно проклятие. Mожет, зря я Сергея отпустил? Может, с ним вдвоём что-нибудь и придумали бы?"
    play sound dct_sfx_robot_run_club_attic fadein 1.5
    pause 0.8
    stop sound fadeout 1.5
    "Опять кто-то лёгкий пробежал по краю крыши, на Шурика сверху посыпался мусор, но задремавший Шурик не отреагировал."
    stop ambience fadeout 1

    scene black with dct_fade
    play music twinkling fadein 1
    "Сон на этот раз был несвязный. Может быть, там, во сне, внутренняя логика и присутствовала, но вот запомнился он разрозненными фрагментами."

    scene dct_dream_sh_first_disert
    show dct_dream_veil at shiver
    with dissolve
    "Вот полигон, где падают с неба горящие мишени и догорают уже на земле."
    "Вот тот же самый полигон, только по нему бегает маленький, с пятилетнего ребёнка, алюминиевый человечек. Все военные недоуменно переглядываются, а Сыроежкин стоит тут же, у раскрытого ящика, и довольный улыбается."

    scene dct_coin_bus-stop:
        zoom 0.75
    show d_jn_old normal:
        zoom 0.55 xcenter 0.44 ypos 0.15
    show d_jn_young dontlike:
        zoom 0.55 xcenter 0.32 ypos 0.15
    show dct_dream_veil at shiver
    with dissolve
    "А вот автобусная остановка, на которой стоят удивительно знакомые женщина лет тридцати пяти и десяти-одиннадцатилетняя девочка. Женщина по случаю прохладной погоды в лёгком свитере, а девочку заставили надеть куртку, чем она крайне недовольна."
    show d_jn_old smile
    show d_jn_young smile
    with dspr
    "Они обе заметили Шурика, но стоят и не шевелятся, девочка радостно улыбается, а женщина пытается спрятать улыбку под строгой маской."
    "Во сне Шурик знает, что их зовут Яна и Яна. Во сне Шурик знает, что сами они не заговорят — к ним надо подойти, знает и то, что не надо к ним подходить. Но сдерживаться нет сил, и Шурик подходит."
    show dct_coin_bus-stop:
        zoom 1 anchor (0.1, 0.17)
    show d_jn_old smile:
        zoom 1 xcenter 0.51 ycenter 0.833
    show d_jn_young smile:
        zoom 1 xcenter 0.29 ycenter 0.833
    with dissolve
    d_jn_old "Здравствуй, Саша."
    show d_jn_old cry
    show d_jn_young smile
    with dspr
    "Женщина смотрит в глаза Шурику, и по её щеке стекает слеза. Только что сдерживала улыбку, и вот уже плачет. "
    d_jn_old "Ты опять нарушил своё же обещание."
    show d_jn_young laugh with dspr
    d_jn_young "Привет, Па! Как тебя долго не было! А мы сейчас к бабушке едем!"
    show d_jn_young smile with dspr
    show d_jn_old normal
    show d_jn_young normal
    with dspr
    d_jn_old "Пожалуйста, не приходи больше. И не пытайся нас вызывать. Всё, что было в Системе, ты уже вытащил. А сейчас… Даже то, что мы с тобой говорим — это только твоё воображение."
    "Из-за угла слышен шум мотора. Как обычно в этом сне. Пора расставаться. И Шурика, независимо от его желания, относит от обеих Ян."
    stop music fadeout 1 

    scene anim prolog_1 with dissolve
    play sound dct_sfx_horn_dinner_through_loudspeaker
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Сквозь сон Шурик слышит горн — сигнал к ужину, и тут же Шурика будит пришедший за ним Сыроежкин."

    scene black with dissolve_fast
    pause 0.5
    $ sunset_time()
    $ persistent.sprite_time = "sunset"

    scene dct_ext_glade_behind_clubs_sunset
    show el laugh pioneer close
    with dissolve_fast
    play ambience ambience_camp_center_evening fadein 1
    "Какое-то время сон ещё сохраняется в памяти, но через несколько минут уже всё забывается."
    th "Ультразвуковая пугалка?"
    show el smile pioneer close with dissolve_fast
    th "А если не пугалка?"
    dreamgirl "Ай!" with hpunch
    sh "Сергей, a не замахнуться ли нам на тайны мозга? Что ты знаешь об ультразвуке?"
    show el surprise pioneer close with dissolve_fast
    # pause 0.5
    stop ambience fadeout 1

    scene dct_int_dining_hall_table_sunset_back_people    
    show dct_int_dining_hall_d_ka blur:
        xcenter 0.35 ycenter 0.35
    show dct_int_dining_hall_table_sunset_chairs
    show mt smile pioneer close:
        xcenter 0.74
    show dct_int_dining_hall_table_sunset_front
    with dct_fade
    play ambience ambience_dining_hall_full
    play music music_list['i_want_to_play'] fadein 1
    mt "Всё готово к дискотеке?"
    dv "Не знаю, Ольга Дмитриевна. А что к ней может быть не готово?"

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show dct_int_dining_hall_table_sunset_chairs:
        xzoom -1
    show dv grin pioneer close:
        xcenter 0.58 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    "Вообще день сегодня оказался неплохим. Даже несмотря на необходимость пасти средний отряд на уборке и намеченный на «когда будет время, но не позже воскресенья» разговор с Леной и Персуновыми — всем четверым проснувшимся обитателям лагеря было что обсудить с прошлого цикла."
    "Главное — исчезла серость и скука, засасывавшая в себя Алису, когда хотелось забыть прошлый цикл, и позапрошлый, и поза-позапрошлый…{w} Так и заканчивается активная фаза."
    mt "…Алиса, ты вообще меня слушаешь?"
    show dv surprise pioneer close with dissolve_fast
    "Ольга, оказывается, что-то говорила. "

    scene dct_int_dining_hall_table_sunset_back_people
    show dct_int_dining_hall_d_ka blur:
        xcenter 0.35 ycenter 0.35
    show dct_int_dining_hall_table_sunset_chairs
    show mt normal pioneer close:
        xcenter 0.74
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    mt "Как тебе наш горнист? Готов он к самостоятельной жизни?"
    dv "Ольга Дмитриевна, мы сами себе до субботы сроку дали — присмотреться, а вы уже сегодня меня спрашиваете. Похоже, что готов."
    show mt normal pioneer close:
        linear 0.5 blur 10
    show dct_int_dining_hall_d_ka sharp with dissolve_fast
    "Алиса поймала неприязненный взгляд Кати и ещё раз подтвердила."
    dv "Да, считаю, что готов. "
    th "Пусть Катька позлится."
    show mt normal pioneer close:
        linear 0.5 blur 0
    show dct_int_dining_hall_d_ka blur with dissolve_fast
    mt "Тогда я не вмешиваюсь. Всё на ваше усмотрение."
    play sound "<from 1.2>" + dct_sfx_chair 
    show mt normal pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.9 xcenter 1.25
    "Алиса, не удержавшись и наплевав на манеры, нацепила на вилку кусок хлеба и принялась вычищать тарелку от остатков соуса. Ужин у поваров сегодня получился превосходным, что после смерти бабы Глаши было скорее исключением."
    th "Я с ней и не общалась почти. Но это был последний человек из пришедших снаружи. Они там, снаружи, ничем не лучше нас, я уверена. Но всё равно что-то мы потеряли." 
    th "Интересно, а чего это Максим так вопросительно на меня смотрит?{w} Понятно: хочет что-то узнать, а спросить не решается."
    th "Странно, за сутки с небольшим близкого знакомства он не показался мне особо стеснительным."
    show mi normal pioneer behind dct_int_dining_hall_table_sunset_chairs with MoveTransition(1.5, enter=_moveleft, enter_time_warp=_ease_time_warp):
        xcenter 0.38 ycenter 0.29
    mi "Алисочка, можно к тебе подсесть?"

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show dct_int_dining_hall_table_sunset_chairs:
        xzoom -1
    show dv smile pioneer close:
        xcenter 0.58 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    "Подошла задержавшаяся у себя в кружке Мику и, не дожидаясь разрешения, поставила на столик поднос с ужином. Присела, огляделась вокруг, разулыбалась и помахала рукой проходящему мимо Максиму."
    show dv sad pioneer close with dissolve_fast
    extend " А Алису это почему-то неприятно кольнуло."
    show dv shy pioneer close with dspr
    th "Ты что, Рыжая, ревнуешь, что ли? Вы ещё женскую драку с Катькой устройте. То есть с Мику, а Катька будет драться с победительницей. Вот шоу-то будет!"

    scene dct_int_dining_hall_table_sunset_back_people
    show dct_int_dining_hall_d_ka blur:
        xcenter 0.35 ycenter 0.35
    show dct_int_dining_hall_table_sunset_chairs
    show mi smile pioneer close:
        xcenter 0.4 ycenter 0.42
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    mi "Знаешь, Алисочка, я вчера пыталась заниматься с Максимом — думала, раз он умеет на горне играть, то может, он и на корнете сумеет. Но оказалось, что музыка у него не получается. За что ни возьмётся — всё время сигналы выходят какие-то."
    show mi laugh pioneer close with dissolve_fast:
        xcenter 0.425
    "Мику хихикнула."
    show mi smile pioneer close with dissolve_fast:
        xcenter 0.4
    mi "А вообще мальчик очень хороший. Он похож на молодую породистую собачку, которая уже выросла из щенков, но всё ещё хочет поиграть. Алисочка, а правда он будет жить у тебя в домике?"

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show dct_int_dining_hall_table_sunset_chairs:
        xzoom -1
    show dv shocked pioneer close:
        xcenter 0.58 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    "Алиса даже поперхнулась."
    dv "А? С чего ты взяла?"
    mi "Ну все так говорят. Нет, конечно, это неправильно, когда мальчика селят в одном домике с девочкой…"
    show dv shy pioneer close with dissolve_fast
    extend " Наверное?"
    "Алиса уже собралась сказать, что где Максим будет жить — пусть думает Ольга Дмитриевна, но, скорее всего, Алисе придётся перебраться к вожатой в домик, а Максима поселят в её домике вместе с опоздавшим пионером, или же Алису оставят на старом месте, а Максим так и будет жить вместе с Витькой."

    scene dct_int_dining_hall_table_sunset_back_people
    show dct_int_dining_hall_d_ka blur:
        xcenter 0.35 ycenter 0.35
    show dct_int_dining_hall_table_sunset_chairs
    show mi shy pioneer close:
        xcenter 0.425 ycenter 0.42
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    "Но тут увидела еле сдерживаемую улыбку в глазах Мику."
    dv "Точно. Так и будет."
    dv "Мы только что с вожатой составили список, чему именно из «плохого» я буду его учить."
    show mi laugh pioneer close with dspr
    mi "Алисочка…"

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show dct_int_dining_hall_table_sunset_chairs:
        xzoom -1
    show dv laugh pioneer close:
        xcenter 0.58 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    mi "Максим хочет тебя вечером пригласить на танец, но стесняется."
    show dv surprise pioneer close with dissolve_fast
    extend " Не отказывай ему, пожалуйста."
    play sound "<from 1.0>" + dct_sfx_chair
    show dv shy pioneer close with dissolve_fast
    show dv shy pioneer close:
        linear 0.4 ycenter 0.23
        pause 0.12
        easeout 1.2 xcenter -0.25
    pause 0.8

    scene dct_int_dining_hall_table_sunset_back_people
    show dct_int_dining_hall_d_ka blur:
        xcenter 0.35 ycenter 0.35
    show dct_int_dining_hall_table_sunset_chairs
    show mi grin pioneer close:
        xcenter 0.425 ycenter 0.42
    show dct_int_dining_hall_table_sunset_front
    with dissolve_fast
    $ sunset_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    dv "Пока, Мику. На площади увидимся."                                       
    stop ambience fadeout 1
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ night_time()
    $ persistent.sprite_time = "day"

    scene bg int_library_night with dissolve_fast
    $ renpy.music.set_volume(0.09, delay=0)
    play ambience ambience_library_day fadein 1
    play music music_list["lightness_radio_bus"] fadein 3
    "На дискотеку Женя, конечно же, не пошла. Она никогда не ходила на первую дискотеку цикла, всегда оправдываясь тем, что не успела ещё навести порядок в библиотеке, а на самом деле стесняясь своей внешности, неуклюжести, неумения танцевать и, главное, чувствуя себя крайне неуютно в такой толпе." 
    th "Зря я сюда приехала. Дома, по крайней мере, никто не требует «обязательно участвовать в общелагерных мероприятиях», и можно не чувствовать себя клоуном. Завтра начнут подкладывать кнопки на стул, начнут мазать край стола мелом. И всем будет смешно."
    th "Одни будут травить активно, другие следить с интересом за происходящим, третьи просто не будут вмешиваться, предоставляя возможность выпутываться самой. Это одно."
    th "А другое — как дать понять нравящемуся самой мальчику, что он зря теряет время? А из лагеря просто так не уедешь, эти две недели надо просто пережить."
    play sound sfx_clench2
    pause 0.2

    scene dct_int_library_night_full_light with dspr
    pause 0.2
    un "Ой!"
    mz "Кто здесь?"
    show un surprise pioneer far with dissolve
    un "Женя, это я. Я зашла, чтобы взять что-нибудь почитать. Дверь открыта была, а тебя не было, и я задремала в кресле."
    mz "Вообще-то библиотека уже закрыта. Но бери, раз уж пришла."
    un "Спасибо, я уже. Вот…"
    show un shy pioneer far with dissolve
    "Лена протянула книгу и покраснела."
    un "А тебя ждала, чтобы ты записала."
    hide un with dissolve
    play sound sfx_open_cabinet_1
    "Женя, не садясь, записала в формуляр книгу, заперла за Леной дверь и только тогда позволила себе всё проверить."
    "Нет, никаких «сюрпризов» в библиотеке после посещения Лены не оказалось: ни подпиленной ножки стула, ни воды, налитой в один из ящиков стола, ничего."
    "Женя от Лены гадостей и не ждала, но запустившаяся программа требовала всё проверить. Хотя нет, один сюрприз был."
    "В кресле, в котором дремала Лена, осталась после неё серая канцелярская папка-скоросшиватель — родная сестра тех, что были свалены кучкой на нижней полке одного из библиотечных стеллажей."
    "Женя переложила папку к себе на стол, а сама, походив между шкафов и выбрав книгу, уселась в то же кресло, закинув ноги на журнальный столик."

    scene int_library_night2 with dissolve
    "С площади доносилось только приглушённое «бум-бум-бум». Верхний свет Женя погасила, остался только тот, что проникал снаружи от уличных фонарей, и настольная лампа."
    "Книжка не шла."
    "Во-первых, всё время казалось, что Женя её уже читала, и не один раз, всегда с первых же слов угадывая содержание очередного абзаца."
    "А во-вторых, вспоминался сегодняшний день, начиная с букета. И как больно было прогонять Сыроежкина. Нет, книжкой не отвлечёшься. На глаза попалась Ленина папка."
    "Было бы письмо — Женя бы не полезла, медицинские карточки выглядят совсем не так, надписи «Личное дело» на обложке тоже не было. А была надпись «Костёр» красным фломастером. Женя откинула обложку."
    "Самым верхним был вложен рисунок цветными карандашами."
    "Лесная поляна, окружённая кустами, посреди поляны догоревший, но ещё дымящийся костёр, вокруг костра лежат буквой П три больших бревна, на брёвнах и рядом с брёвнами всякие мелкие и не очень предметы вроде связки ключей, рогатки, вожатской панамки, гитары, книги, отвёртки, ещё чего-то…"
    "Розовеющее небо давало понять, что время там, на рисунке — раннее утро."
    "Людей на рисунке не было. Только из кустов выглядывала чья-то намеченная несколькими штрихами голова. Но только намеченная, так что не поймёшь, молоденькая девушка это с забавной причёской или крупная кошка. Женя перевернула страницу."
    "«Костёр, пионерская сказка» — было отпечатано на машинке."
    "Следующая страница — рукописный текст, каллиграфически выведенный явно женской рукой: «Сенечке, которому, несмотря ни на что, так и осталось семнадцать. И Ульянке, которая доросла до девятнадцати!», и несколько непонятных загогулин вместо подписи."
    "Следующая — опять рукопись: на этот раз, похоже, рукой физрука…"
    "Чем дальше открывались страницы, тем сильнее начинало биться сердце."
    "Женя всё никак не могла заставить себя разобраться в кривых невозможного почерка и прочитать, что же там понаписал физрук на целых полстраницы, когда в дверь библиотеки постучали.{nw}"
    play sound sfx_knock_door7_polite
    extend" Женя вздрогнула, закрыла папку и пошла к двери."
    play sound sfx_open_door_clubs_2
    show un shy pioneer with dissolve
    un "Женя…"
    "Лена быстро взглянула и опять опустила глаза."
    un "Я забыла у тебя одну вещь."
    mz "Да, конечно. Забирай."
    $ persistent.sprite_time = "day"        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Очень хотелось спросить: «А что это? Можно почитать?». Но Женя пока не настолько доверяла окружающим, чтобы вот так вот взять и показать свою слабость."
    stop music fadeout 1
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ persistent.sprite_time = "night"

    scene bg ext_square_night_party2    
    show dv normal pioneer far:
        xcenter 0.4 yalign 0.02
    with dissolve_fast
    play ambience ambience_camp_center_night fadein 1
    d_ma "Тётя Алиса, а правда, что через полчаса дискотека?"
    dv "Чего тебе надобно, дитятко?"
    d_ma "Тётя Алиса… Алиса, а если я тебя приглашу на танец, ты меня не прогонишь?"
    show dv grin pioneer far with dissolve_fast
    dv "Не прогоню. Приглашай… племянник."
    show dv smile pioneer far with dissolve_fast
    extend " Но с условием. Жени и Ленки не будет, скорее всего, но чтобы Мику и Сашу пригласил обязательно."
    stop ambience fadeout 1

    scene bg ext_path_night with blinds
    $ renpy.music.set_volume(1.0, delay=0)
    play music music_list['dance_of_fireflies'] fadein 2
    "И вот сейчас Максим искал Алису, чтобы проводить её до домика под тем предлогом, что сам живёт в соседнем. Пошёл по тропинке на голос и уже перед аллеей нечаянно подслушал разговор."
    dv "Завтра уходите?"
    me "Да, в пять утра."
    dv "Смотрите, не пропадайте на неделю, как в прошлый раз. А то спасай вас потом."
    us "Рыжая! И вовсе не на неделю, а на пять дней! И вы спасали уже один раз, хватит. ОД очень мудрая женщина и не дала развалиться лагерю без ключевых фигур. Ну и мелкие ей помогли, конечно."
    th "Кажется, физруки собрались куда-то, а Алиса сейчас прощалась с ними."
    me "Сейчас налегке пойдём, а Рыжик подлечит, если что. Так что завтра туда, а послезавтра утром вернёмся."
    dv "Да я понимаю, а всё равно беспокоюсь за вас, Сенька. Должна же я хоть о ком-то беспокоиться?"
    me "А ты не беспокойся, а глянь лучше, что Лена нарисовала…"

    scene ext_square_night_party with dissolve
    $ set_mode_nvl()
    "С танцами вообще получилось неплохо. Алиса — как обычно, чуть насмешливая, Саша — благодарно улыбнувшаяся, танцевавшая на пионерской дистанции и в конце сказавшая: «У тебя есть способности, если хочешь, приходи к Мику в кружок, подучим», Мику — «Максимочка, конечно же можно!»." 
    extend " Всех этих девочек как будто знал и со всеми как будто был в хороших отношениях уже давно-давно, с детского сада.{w} Ещё раз Алиса. Катя фыркнула и отправилась танцевать с Витькой, соседом по домику."
    "\nА больше медленных танцев и не было.{w} То есть был один — белый, в конце дискотеки. Катька мазнула глазами и опять пошла танцевать с Витькой, а Максим даже не обратил внимания. Он втайне надеялся, что его пригласит Алиса — не пригласила.{w} И вот это, а вовсе не постоянные насмешки, было обидно. На насмешки Максим отвечал той же монетой, но в нахальные янтарные глаза хотелось посмотреть ещё раз, чтобы ещё раз углядеть в их глубине искру улыбки."
    nvl clear
    stop music fadeout 1

    scene bg ext_path_night with blinds
    play ambience ambience_camp_center_night fadein 1
    $ set_mode_adv()
    dv "Ну, тогда до послезавтра."
    us "Да, до послезавтра. К полудню будем. И не вздумайте нас спасать ещё раз!"
    "Силуэты обнялись. Двое пошли в сторону спортзала, а третий повернул назад, к площади. Максим бегом обогнал Алису по тропинке, вывалился из кустов на площадь и перехватил её на аллее."

    scene bg ext_square_night
    show dv surprise pioneer2 far
    with dissolve
    play music adaytoremember fadein 1
    d_ma "Тётя Алиса, ты домой? Позволишь проводить?"
    show dv grin pioneer2 far with dissolve_fast
    dv "Провожай, провожатор."

    scene bg ext_square_night with fade
    "Через площадь шли, пиная по очереди бумажный стаканчик, неизвестно кем брошенный у питьевого фонтанчика."
    d_ma "Алис, а ты правда физруков спасала?"
    dv "Подслушивал.{w=0.5} Спасала, только они сами спаслись, без моей…{w=0.5} без нашей помощи."

    scene dct_ext_houses_night with dissolve
    d_ma "А куда они пошли?"
    show dv guilty pioneer2 with dissolve
    dv "Куда?"
    dv "К сестрёнке Ульяниной в гости — наверное, так."
    d_ma "В следующий раз я пойду с тобой."
    show dv surprise pioneer2 close with dissolve_fast
    "Максим остановился и развернулся лицом к девушке. Лицо его потерялось в тени, только глаза блестели, отражая свет фонарей."
    show dv normal pioneer2 close with dissolve_fast
    dv "Ты ещё…"
    show dv guilty pioneer2 close with dissolve_fast
    "Алиса представила себе растерянного и перепуганного пионера в посёлке Шлюз в окружении Семёновых двойников. Неизвестно вообще, как сознание Максима отреагирует на эту штуку."
    dv "Ты ещё…"
    d_ma "Маленький? Глупый? Недостойный?"
    show dv grin pioneer2 close with dissolve_fast
    dv "Ну-ка назови мне свой домашний адрес."
    hide dv with MoveTransition(1.2, leave=_moveleft, leave_time_warp=_ease_time_warp)
    "И Алиса пошла к себе, оставив на площади хватающего ртом воздух Максима. А уже от домиков обернулась и грустно добавила:"

    scene bg ext_house_of_dv_night
    show 3500_dv sadness pioneer2 at cright:
        zoom 0.75
    with dissolve
    dv "…Просто ты ещё не проснулся. Но спасибо, действительно спасибо."

    scene dct_ext_houses_night
    show d_ma normal pioneer:
        xcenter 0.5 yalign 0.02
    with fade
    "Алиса ушла и не услышала, как Максим ответил уже в пустоту:"
    d_ma "В следующий раз я пойду с тобой."
    show d_ma serious pioneer with dissolve_fast
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    extend " Это не просьба, Алиса. Это просто информация."
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
    
    
    
######################
#Глава 4. Расстановка#
######################

label dct_disposition_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Расстановка"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава IV. Расстановка" at truecenter with dspr
    play music buddy fadein 2.5
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    $ renpy.pause(0.2)

    scene bg ext_clubs_day
    show el serious pioneer close at cleft
    with dissolve
    "Электроник был занят с самого утра.{w} Настолько занят, что даже мысли о Жене отошли куда-то на задний план."
    
    scene bg int_clubs_male_day:
        zoom 1.2 align (0.0, 0.9)
    show sh normal pioneer at right:
        ycenter 0.53
    show dct_dream_veil at shiver
    with dissolve
    "Помочь Шурику в разработке принципиальной схемы. Помочь — значит в основном не мешать и слушать рассуждения Шурика, но пару раз тот похвалил Сергея за дельные мысли."

    scene bg int_musclub_day
    show mi normal pioneer
    show dct_dream_veil at shiver
    with dissolve
    "Выпросить в музыкальном кружке вращающийся стул."
    show mi shocked pioneer with dissolve_fast
    mi "Серёженька, а вам зачем? Как интересно!{nw}"
    show mi smile pioneer as mi2 at center behind dct_dream_veil:
        alpha 0
        linear 0.5 alpha 1
    show mi shocked pioneer:
        linear 0.5 alpha 0
    mi "{cps=0}Серёженька, а вам зачем? Как интересно! {/cps}Серёженька, только обязательно позовите меня на испытания! Я хочу стать подопытным кроликом! Слышишь? Ты обещал!"

    scene dct_int_warehouse_day
    show dv normal pioneer at left
    show dct_dream_veil at shiver
    with dissolve
    "Собрать вокруг стула каркас установки: круглую клетку из лыжных палок и гимнастических обручей, которые пришлось выпрашивать у Алисы."
    show dv grin pioneer with dissolve_fast
    dv "И что? Робота делать не будете? Ну вы даёте, вы не заболели там? Надо будет зайти и глянуть."

    scene dct_int_clubs_male2_night_zoom
    show dct_dream_veil at shiver
    with dissolve
    "Разработать конструкцию ультразвуковых излучателя и приёмника. Готовых-то нет, а из всей литературы — только пара подшивок журнала «Радио» в кружке да десятка два разрозненных номеров «Моделиста-Конструктора» и «Юного техника» в библиотеке."
    show dct_camp_hustle_to_the_left behind dct_dream_veil
    "До самого обеда Электроник с поражающей окружающих энергией носился по лагерю в поисках материалов, пилил, клепал, паял, прессовал из мела и сухих белил, а сначала надо было придумать, как и чем прессовать, а потом обжигал керамические таблетки излучателя."
    "Забегал, не обращая ни на кого внимания, в библиотеку и там молча шёл к стеллажу с журналами, перечитывал их на двадцать пятый раз, делал выписки и опять бежал в клуб."
    "Увлечённый любимой работой, Электроник мог переплюнуть по энергичности и целеустремлённости Ульянку в её лучшие годы."

    scene bg int_library_day
    show d_mz hope pioneer glasses far at fright
    show dct_dream_veil at shiver
    with dissolve
    "Только иногда в библиотеке Сергей ловил спиной взгляд Жени сквозь стеллажи, замирал и оборачивался."
    show d_mz amazed pioneer glasses far with dspr
    pause 0.3
    show d_mz confused pioneer glasses far with dissolve_fast
    "Но Женя всегда успевала спрятать глаза в очередную книгу и лишь вздрагивала."
    "Очень хотелось подойти, отодвинуть эту проклятую книгу и заглянуть ей в глаза.{w} Спросить: «Женька, ты что творишь? Со мной и с собой? С нами».{w} Но не хватало смелости."
    "Сергей вздыхал и возвращался к своим журналам."
    pause 0.3
    show d_mz smile pioneer glasses far with dspr
    pause 0.3
    show d_mz normal pioneer glasses far with dissolve_fast
    "Женя выныривала из-за книги и опять начинала гипнотизировать Сыроежкину спину, пока тот снова не убегал в кружок."
    stop music fadeout 4

    scene bg int_clubs_male_day with dct_fade:
        zoom 1.2 align (0.0, 0.5)
    play ambience ambience_clubs_inside_day fadein 4
    "Наконец ближе к обеду сегодняшняя порция работы закончилась. Печатные платы травились в растворе, и оставаться им там следовало до вечера, двадцать керамических излучателей остывали вместе с муфельной печью — нужно четыре штуки, но хорошо если каждый третий заработает как надо."
    "Принципиальная схема на листе оранжевой миллиметровки была пришпилена к дверце шкафа поверх чертежа авиамодели, горка деталей, извлечённых из ящика и выпаянных из некондиционных плат, лежала на втором листе миллиметровки, и сейчас Шурик, прозванивая, раскладывал их по кучкам: резисторы отдельно, транзисторы отдельно, и так далее."

    scene dct_int_clubs_male2_night_zoom
    show sh normal pioneer close at right
    with dissolve
    sh "Сергей, на сегодня, наверное, всё. Вечером я приду, платы из раствора достану и промою."
    show sh normal_smile pioneer close with dissolve_fast
    "Шурик покачал рукой каркас установки, похожий на сегмент Шуховской башни, одобрительно кивнул и, подтверждая собственные слова, повторил:"
    sh "На сегодня всё. Ты свободен, а я детали рассортирую до конца и тоже пойду."

    scene bg int_clubs_male_day:
        zoom 1.2 align (0.0, 0.5)
    show el smile pioneer close at fleft with dissolve
    el "Шурик, а может, я сам деталями займусь?"
    sh "Нет, иди-иди, а то мне ещё подумать надо."
    show el normal pioneer close:
        pause 1
        linear 0.8 alpha 0
    th "Подумать — это святое. Нельзя никого отвлекать, когда он думает."
    stop ambience fadeout 1
    play sound [ "<silence 0.4>", sfx_close_door_1 ]

    scene ext_clubs_day:
    show 3500_el normal pioneer:
        zoom .18 anchor (.5, 1.0) pos (.48, .707)
    with slideawayup
    play sound_loop ambience_camp_center_day fadein 1
    th "В библиотеку?"
    extend " Сейчас, когда голова на время освободилась от забот, очень хочется увидеть Женю."
    hide 3500_el with dissolve
    th "Я только возьму что-нибудь почитать." 

    scene bg ext_library_day
    show el surprise pioneer far at cright
    with pushleft
    th "А вдруг она о чём-нибудь меня спросит?"
    show el laugh pioneer far with dissolve_fast
    extend " Придумаю что-нибудь."
    stop sound_loop fadeout 1
    play sound sfx_open_door_clubs_2

    scene bg int_library_day with slidedown
    play ambience ambience_library_day
    "Не спросила."
    show d_ma normal pioneer:
        zoom 0.75 xcenter 0.25 yalign 1.01 alpha 0
        pause 2.5
        linear 1 alpha 1
    show un normal pioneer close:
        xcenter 0.7
    with dissolve
    "Вместо Жени за столом-конторкой сидела Лена, а в кресле у журнального столика пристроился Максим. И, похоже, Электроник прервал их беседу."
    el "П-привет. А где Женя?"
    un "Попросила подменить её до обеда."
    show un smile pioneer close with dspr
    un "Ты что-то хотел взять? Возьми, я запишу."
    th "Раз уж пришёл, придётся что-нибудь взять."
    show un normal pioneer close with dspr
    "Лена записала книгу в формуляр и спросила:"
    un "Сергей. Правда, что вы у себя машину для чтения памяти собираете?"
    show un shy pioneer close with dspr
    un "Я бы хотела попробовать."
    el "Если доктор решит, что это безопасно, то почему нет?"
    show un serious pioneer close with dissolve_fast
    un "Сергей. Я хочу попробовать, что бы там доктор ни решила. Вы же сами на себе попробуете?"
    show d_ma surprise pioneer with dspr:
        pause 0.5
        easeout 1.1 xcenter 1.2
    play sound [ "<silence 1.1>", sfx_open_door_kick ]
    d_ma "Ё-моё! На обед же надо сигналить, а я тут сижу!"
    "Неожиданное бегство Максима спасло Электроника от необходимости отвечать."
    "Сергей пробормотал что-то невнятное и выскочил вслед за горнистом."
    play sound [ "<silence 0.4>", sfx_close_door_campus_1 ]
    stop ambience fadeout 1

    scene bg int_library_day:
        matrixcolor BrightnessMatrix(value=-0.25)
    show dct_int_library_rain:
        alpha 0.3
    show dct_int_library_rain_lamp
    with dct_fade
    play music peritune_gentle_theme_piano fadein 1
    show d_mz sad pioneer glasses far with dissolve:
        xcenter 0.8
    "Лена утром зашла в библиотеку без всякой глобальной цели, просто поменять книжку, но зацепилась взглядом за Женю. Та грустила в углу зала за своим столом-конторкой, чем-то напоминая нахохленную птицу под дождём."
    th "Зря мы в автобусе тогда пошутили. Сейчас бы Женя вовсю Сергея гоняла."
    extend " И Сергей не прятался бы от всех в работе."
    "А потом ещё в разговоре выяснилось, что она со вчерашнего дня сидит безвылазно в библиотеке с перерывами только на еду и сон."
    "И понадобились всё искусство убеждения и умение выдавать свои мысли за чужие желания, которыми обладала Лена, чтобы уговорить Женю просто сходить прогуляться по лагерю."
    show d_mz sad pioneer at right with dissolve_fast
    mz "Лена, а если кто-то придёт…"
    un "Тогда я выдам ему нужное издание и заполню формуляр не хуже тебя."
    mz "Я только…"
    un "Хорошо-хорошо. Я подежурю. Только ты недолго."
    stop music fadeout 2.5
    play sound ["<silence 0.7>", sfx_close_door_1]
    hide d_mz sad pioneer with MoveTransition(1.0, leave=_moveright, leave_time_warp=_ease_time_warp)
    "До обеда оставалось ещё около часа."
    play sound sfx_open_drapes

    scene int_library_day with dissolve
    play ambience ambience_library_day fadein 1
    "Лена погасила настольную лампу, отодвинула тяжёлую портьеру у себя за спиной и впустила в библиотеку солнечные лучи.{w} Взвесила в руке выбранную книжку: на пару дней чтения хватит. Бросила взгляд на библиотечные стеллажи."
    th "А ведь рано или поздно книги кончатся. Всё, что было здесь хорошего, я уже прочитала. Сейчас читаю средненькое. А потом?"
    extend " Может, Семён что-то принесёт?"
    "Семён с Ульяной ушли сегодня утром и клятвенно обещали вернуться завтра часам к десяти, оставалось надеяться, что они вернутся не с пустыми руками."
    "По крайней мере, та пьеса, что они принесли в прошлый раз, была проглочена Леной за сутки, потом ещё три раза перечитывалась и породила массу карандашных рисунков-иллюстраций, самый доведённый до ума из которых сейчас ехал обратно как подарок автору пьесы. Та, другая Мику — автор пьесы, обладала ещё и литературным талантом."
    "А ещё интересно было осознавать, что где-то есть очень похожие на тебя Лены, встретиться с которыми, по словам того же Семёна, почти невозможно."
    th "Как там он сказал?"
    show dct_int_coaching_room2
    show dct_dream_veil at shiver
    show d_sf serious sport at center behind dct_dream_veil:
        ypos 0.0
    with dissolve_fast
    me "Останется только один!"
    hide dct_int_coaching_room2
    hide d_sf
    hide dct_dream_veil
    with dissolve_fast
    th "Можно, только во сне."
    "Лена вспомнила обрывки сна, которым завершилась их с Алисой спасательная экспедиция.{w} Сколько там Алис в одном месте оказалось? Три минимум.{w} Сон сном, но волдыри на ладонях потом сходили до самого конца цикла.{w} И это ощущение тепла от поддерживающих тебя дружеских рук на твоих плечах."
    th "Кажется, мальчики какую-то машину для чтения памяти придумывают, надо будет с ними поговорить."

    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
    play sound "<from 1.2>" + dct_sfx_chair 
    "Лена грустно вздохнула и уселась на Женино место. Какая бы средненькая книга ни была, но постепенно и она увлекла."
    play sound sfx_knock_door2
    play sound2 [ "<silence 1.1>", sfx_close_door_campus_1 ]
    show d_ma normal pioneer behind dct_int_library_standing_desk_front:
        xcenter 0.15 ycenter 0.55 alpha 0
        pause 1
        linear 0.4 xcenter 0.3 alpha 1
    extend " Поэтому, когда минут через пятнадцать в дверь постучали, Лена вздрогнула от неожиданности." with vpunch
    show d_ma surprise pioneer with dissolve_fast
    d_ma "Привет. А ты сегодня за библиотекаря, что ли?"
    un "Наверное.{w=0.5} Да.{w=0.5} Подменяю Женю до обеда."
    show d_ma grin with dissolve_fast
    d_ma "А, ну тогда ладно. Я книжку возьму, можно?"
    hide d_ma with dissolve
    stop ambience fadeout 1
    $ renpy.music.set_volume(0.5, delay=0, channel='sound_loop')
    play sound_loop dct_ambience_rattle_in_library fadein 1   # Пока так, но лучше бы найти что-то более подходящее
    "И, не дожидаясь ответа, пошёл шарить по стеллажам."
    "Лена несколько раз порывалась вскочить и посмотреть на происходящую катастрофу, но всякий раз удерживала себя на месте."
    th "Женя меня съест."
    stop sound_loop fadeout 1
    play ambience ambience_library_day fadein 1
    show d_ma grin pioneer behind dct_int_library_standing_desk_front:
        xcenter 0.5 ycenter 0.55 alpha 0
        pause 2
        linear 1 alpha 1
    "Наконец из-за стеллажей показался Максим: весь в пыли и с номерами «Знание-сила» в руках."
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    show d_ma grin pioneer:
        alpha 1
    un "Максим."
    show d_ma shy pioneer with dissolve_fast
    un "Ты только что разгромил половину библиотеки ради пары журналов.{w} Возьмёшь их? Давай, я запишу."
    show d_ma grin2 pioneer with dissolve_fast
    d_ma "Не, не половину. Четвёртую часть, в дальнем углу, куда никто не заглядывает."
    show d_ma normal pioneer with dissolve_fast
    show d_ma normal pioneer:
        pause 0.15
        linear 1.5 xpos 1.25
    "Максим посмотрел на журналы, посмотрел на часы над дверью и устроился за столиком."
    d_ma "Я, наверное, их здесь почитаю."
    "Была бы тут Женя — не остался бы, конечно, но общество Лены было гораздо приятнее."

    scene bg int_library_day
    show un normal pioneer:
        xcenter 0.75
    show d_ma normal pioneer:
        zoom 0.75 xcenter 0.25 yalign 1.01
    with squares
    "Лена против общества Максима тоже не возражала, поэтому скоро тишину в библиотеке прерывало только шуршание страниц и шмыгающий нос нелегально искупавшегося вчера Максима."
    show d_ma serious pioneer with dissolve_fast
    d_ma "Лен, а можно спросить?"
    show un shy pioneer with dspr
    play music music_list["raindrops"] fadein 1
    d_ma "Скажи, вы нашего физрука давно знаете? Ты и Алиса."
    show un normal pioneer with dspr
    un "Давно. Не очень, но давно."
    show d_ma surprise pioneer with dissolve_fast
    show un smile pioneer with dspr
    un "С рождения, наверное."
    show d_un hope pioneer as un
    show d_ma normal pioneer 
    with dissolve_fast
    un "А почему ты спросил?"
    d_ma "Тогда понятно.{w=0.5} Да просто даже Алиса никогда не будет взрослого, пусть и хорошо знакомого человека, Сенькой называть.{w} И она всегда так заботится о Семёне, а Ульяна видит это и только улыбается."
    show un serious pioneer with dspr
    un "Ты наблюдательный…"
    show d_ma grin2 pioneer with dissolve_fast
    "Лена думала, как закруглить разговор. В конце концов, Максим пока ещё только непроснувшийся кандидат в старший отряд, и разъяснять тонкости взаимоотношений Рыжих с Семёном постороннему человеку не хотелось."
    "Но, кажется, Максим понял слова «с рождения» буквально и сделал свои собственные выводы."
    show d_ma smile pioneer with dissolve_fast
    d_ma "То есть ему было лет восемь.{w=0.5} Ну да, если так, то он для вас не заместитель начальника лагеря, а просто как старший брат. Понятно."
    show un smile pioneer with dissolve
    stop music fadeout 2
    "Всё было не так, но Лена не стала поправлять."
    show un normal pioneer with dspr
    play sound sfx_open_door_clubs_2
    show el laugh pioneer close with dissolve
    "Скрипнула дверь, и на пороге показался Сыроежкин."
    show d_ma normal pioneer
    show el normal pioneer close:
        alpha 1
        pause 1.2
        linear 1 alpha 0
    with dissolve_fast
    "Поздоровался — Лене показалось, что разочарованно — и пошёл выбирать себе книжку."
    stop ambience fadeout 1

    scene bg int_clubs_male_day with dct_fade:
        zoom 1.2 align (0.0, 0.5)
    play ambience ambience_clubs_inside_day fadein 1
    "Шурик, отпустив Сыроежкина, закончил отбирать нужные детали, высыпал их в жестяную коробку из-под леденцов и убрал в ящик стола. Посмотрел, как травятся платы, поболтал кюветой, чтобы перемешать раствор."
    th "Ладно азотная кислота, но хлорное железо шефы могли бы лагерю для кружка подарить. Сейчас бы полдня не теряли."
    extend " Нет, потеряли бы — керамике всё равно остывать до утра вместе с печью."
    stop ambience fadeout 1
    play sound sfx_unlock_medpunkt_door

    scene ext_clubs_day with dissolve
    play sound_loop ambience_camp_center_day fadein 1
    "Шурик запер клуб и, огибая здание, пошёл на своё вчерашнее место."
    stop sound_loop fadeout 1

    scene dct_ext_glade_behind_clubs_day                                        
    show dct_ext_glade_behind_clubs_day_barberry
    with dissolve
    play ambience ambience_forest_day fadein 1
    play music the_day_when_i_die fadein 2
    "Прежде чем начинать зондировать собственный мозг, Шурику предстояло разобраться, что ему известно об этих своих сновидениях и голосе в голове, и записать данные самонаблюдения и самоанализа в рабочую тетрадь, чтобы иметь точку отсчёта."
    "Сыроежкин уже согласился быть вторым — контрольным экземпляром. Неплохо было бы для статистики набрать ещё добровольцев, но Шурик опасался возможного риска. В любом случае, как настоящий учёный из любимых книг, он твёрдо знал, что начнёт с себя."

    scene dct_ext_glade_behind_clubs_day
    $ set_mode_nvl()
    "Шурик открыл личную рабочую тетрадь и на первой чистой странице написал:{w}\n{i}Дневник самонаблюдения. Начат в четвёртый день смены. Данные по предыдущим дням восстановлены по памяти{/i}."
    "\nПотом дописал в конце:\n{i}…по памяти и опросам очевидцев{/i}."
    "\nДальше следовал подзаголовок:\n{i}Необычные сны и мысли. Галлюцинации и явления.{/i}"
    "\nДалее следовало описать события первого дня."
    "\n{i}Событие первое — сон в автобусе. Приснилось, что мне сорок лет и я еду в лагерь с пионерами. Почему-то называю пионеров {b}миксами{/b} и {b}копиями{/b}.{/i}"
    "{i}Событие второе — провал в памяти. Поздно вечером обнаружил себя стоящим на площади, спиной к лаборатории.\nЧто делал в лаборатории — не помню, и восстановить свои действия не удалось{/i}."
    "\nЗачеркнул «лабораторию» и написал «кружок». Вроде бы всё.\n"
    stop music fadeout 1
    mip "Привет. А ты Сергея не видел?"

    $ set_mode_adv()
    show d_oz n pioneer behind dct_ext_glade_behind_clubs_day_barberry:
        zoom 0.75 xcenter 0.77 yalign 0.1 alpha 0
        linear 0.5 alpha 1
    play sound dct_sfx_slammed_book
    "Шурик вздрогнул и уронил карандаш." with hpunch
    th "Сергея? А! Это Сыроежкина, что ли?"
    sh "Нет, занятия закончились, и он ушёл. Поищи его в библиотеке."
    mip "Понятно. Если увидишь, то передай, пожалуйста, что его Оксана Зайцева искала."
    play sound sfx_bush_leaves
    hide d_oz with MoveTransition(1.2, leave=_moveright, leave_time_warp=_ease_time_warp)
    "И, не дожидаясь ответа, девочка исчезла, нырнув куда-то в кусты."
    "Шурик повертел в руках карандаш. Синий «Картограф» сломался после контакта с бетоном отмостки, и теперь, чтобы его очинить для продолжения записей, нужно было возвращаться в клуб."
    play sound dct_sfx_horn_dinner_through_loudspeaker
    "Кстати прозвучавший горн напомнил об обеде. Пришлось отклеивать спину от стены клуба, подниматься, отряхивать форму."
    th "Здесь удивительно чисто. Ни копоти, ни глины, ни мазута. Отряхнулся, и форма как новая. А чтобы найти грязь, нужно специально постараться."
    stop ambience fadeout 1

    scene bg ext_houses_day at walking with dct_fade
    play ambience ambience_camp_center_day fadein 1
    play sound_loop dct_sfx_steps2
    th "Почему Алиса куксилась, что всё из цикла в цикл одно и то же? Может, она просто видеть не умеет? Не знаю. И пионеры, и природа каждый цикл хоть чуть-чуть, но разные."
    th "Вон куст подсыхает — прошлый цикл зелёный стоял, а в этом листья теряет. А здесь за четыре дня новую тропинку протоптали — интересно, приживётся или нет? А уж люди как меняются… Это просто надо увидеть."
    "Лена шла из столовой к себе в домик и размышляла."
    stop sound_loop

    scene bg ext_house_of_un_day with dissolve
    th "Я, наверное, порисую сейчас. Портрет Саши начну, а то сколько времени живём в одном домике, а так Саши у меня и нету."
    stop ambience fadeout 1
    play sound_loop ambience_int_cabin_day fadein 1
    play sound sfx_open_door_1

    scene dct_int_house_of_sa_day with slidedown
    "Саши дома не оказалось."
    th "Или возится с мелкими, или ещё где-то — хоть у Мику в кружке, в этом цикле они сблизились раньше обычного."
    th "В следующий раз."
    th "Взять этюдник и уплыть на остров?"
    extend " Или уйти с этюдником на остановку и в очередной раз нарисовать дорогу, убегающую в поля?"
    "Лена взвесила в руках этюдник и поморщилась — тяжёлый. Да и не очень-то и хотелось."
    th "Может, остаться в домике и изобразить ту сценку приручения стрекозы двумя маленькими девочками?"
    extend " И подарить Алисе?{w=0.4} Алиске понравится."
    "Лицо маленькой Алисы встало перед глазами как живое.{w} Так, одна идея есть, и ладошка зачесалась — хороший признак. Значит, результат будет удачный."
    "А потом, без перехода, Лена вспомнила, как в столовой Женя и Электроник постоянно бросали взгляды друг на друга и как они вздрагивали, отводили глаза и зажимались, если этим взглядам случалось встретиться.{w} Да, это оно."
    "Лена быстро набросала сцену приручения стрекозы, чтобы поработать над ней после, когда время будет, а сама взяла карандаши, папку с бумагой и направилась к Жене в библиотеку."
    stop sound_loop fadeout 1

    scene bg int_library_day
    show mz normal pioneer glasses at right
    with dct_fade
    play ambience ambience_library_day fadein 1
    play sound sfx_open_door_clubs_2
    mz "А, это ты. Заходи."
    "Женя постепенно отходила от вчерашнего приступа чёрной меланхолии и встретила Лену почти приветливо."
    un "Я почитаю тут?"
    show d_mz bukal pioneer glasses as mz with dspr
    mz "Библиотека публичная."
    show d_mz fun pioneer glasses as mz with dspr
    "Женя фыркнула на слове «публичная» и пожала плечами."
    show mz normal pioneer glasses with dspr
    mz "Читай."
    hide mz with dissolve
    "Лена так и сделала — ну, почти так. Выбрала книгу побольше форматом, устроилась за одним из читательских столов так, чтобы Женя оказалась в нужном ракурсе, и, спрятав в раскрытой книге лист бумаги, начала делать зарисовки, стараясь поймать эмоции." #цг-шку бы сюда
    "Женя читала что-то своё, время от времени бросая взгляды за окно и на входную дверь, хмурилась, коротко поджимала губы и переворачивала страницу.{w} А после очередной страницы проскрипела, не глядя на Лену:"
    show d_mz shyangry pioneer glasses far as mz at right with dissolve
    mz "Между прочим, можешь не прятаться. А если бы спросила разрешения, то и совсем хорошо было бы."
    "Лена покраснела."
    show d_mz confused pioneer glasses far as mz with dissolve_fast
    mz "Рисуй, если хочешь. Но я не понимаю…"
    "Женя не договорила и, всё так же не глядя на Лену, пожала плечами."
    show mz smile pioneer glasses with dissolve_fast
    mz "И спасибо, что посидела тут вместо меня."
    show d_mz confused pioneer glasses far at right:
        alpha 0
        pause 1
        linear 1 alpha 1
    th "А ведь она ждёт, что Сергей заглянет, а тот боится и где-то прячется."
    extend " Зря девочки посадили Сергея на моё место, и зря я на это согласилась. Нужно бы сейчас всё рассказать, но Женя не поверит — решит, что я Сергея выгораживаю. С её-то точки зрения всё было так, как она увидела."
    hide mz
    show d_mz sceptic pioneer glasses far with dissolve_fast:
        alpha 1
    mz "Лена. А что за рукопись ты вчера у меня забыла?"
    un "Это…"
    "Лена задумалась, как не соврать так, чтобы Женя не стала потом крутить пальцем у виска."
    un "Это девочка одна, знакомая нашего физрука, сказку написала. И Семён попросил, чтобы я к ней иллюстрации сделала."
    show d_mz hope pioneer glasses far with dspr
    "И, отвечая на висящий в воздухе вопрос, добавила:"
    un "Можешь взять почитать. Заходи вечером. Я Саше скажу, если меня не будет."
    stop ambience fadeout 1

    play music fm_freemusic_chillout_music fadein 3.5
    scene bg int_library_day
    show d_mz sad pioneer glasses close:
        zoom 1.25 align (-0.5, 0.5)
    with dct_fade
    show dct_cg_mz_dreams_of_el:
        alpha 0
        linear 2 alpha 0.45
        pause 2
        linear 2 alpha 0.6
        pause 3.5
        linear 2 alpha 0.75
        pause 5
        linear 2 alpha 0.9
    "Женя действительно ждала Сыроежкина. Даже самой себе не сознавалась в этом, но ждала."
    "Провожала взглядом пробегающих за окнами пионеров,{w} прислушивалась, когда казалось, что кто-то топчется на крыльце"
    play sound ["<silence 1.2>", "<to 1.0>" + sfx_open_door_clubs]
    show int_library_day as int_library_day2:
        alpha 0
        pause 1.3
        linear 1 alpha 1
    show d_mz amazed pioneer glasses close as mz:
        zoom 1.25 align (-0.5, 0.5) alpha 0
        pause 1.3
        linear 1 alpha 1
    extend ", вздрогнула, когда вдруг повернулась дверная ручка.\n«Он!» — ёкнуло внутри."
    play sound sfx_medpunkt_door_open

    scene dct_int_library_standing_desk_back
    show un normal pioneer at center:
        ycenter 0.46
    show dct_int_library_standing_desk_front
    with dissolve
    "Но, к счастью, это оказалась Лена.{w} Или, может быть, к сожалению, это оказалась Лена. Этого Женя даже под гипнозом не сказала бы."
    show dct_int_library_standing_desk_reader_place behind un
    show d_un hope pioneer as un behind dct_int_library_standing_desk_reader_place with dissolve:
        zoom 0.2 xcenter 0.48 ycenter 0.32
    "Лену Женя уже отнесла к числу безопасных, подвоха от неё не ждала, поэтому выгонять из библиотеки не стала, а разрешила остаться и посидеть-почитать." 
    "И даже то, что Лена вместо чтения занялась рисованием, Женю особо не раздражало."
    show un surprise pioneer with dissolve_fast
    extend " Так только, дала понять, что заметила, и всё.{w} Только поначалу неприятно немного было оказаться в фокусе чужого внимания."
    stop music fadeout 2
    play ambience ambience_library_day fadein 2
    show d_un hope pioneer as un with dspr
    un "Женя, в субботу сбор отряда будет."
    mz "Я не приду."
    un "Я, может, тоже. Я не об этом. Будем решать, принимать новенького или нет. В…"
    show un cry_smile pioneer with dissolve_fast
    "Лена чуть не ляпнула: «Вместо Ульяны»."
    show d_un hope pioneer as un with dissolve_fast
    un "Вот того, который горнист, Максима."
    mz "Да мне как-то всё равно. Если нужен мой голос, можешь передать, что я — за."
    show un grin pioneer with dspr
    un "Я передам."
    hide dct_int_library_standing_desk_reader_place
    show un normal pioneer at cleft:
        zoom 1.0 ycenter 0.46
    with Dissolve(1.5)
    "Лена закончила рисовать."
    play sound [ "<silence 0.4>", sfx_close_door_campus_1 ]
    show un normal pioneer:
        linear 1 alpha 0
    extend " Женя ждала, что ей покажут результат, но Лена просто попрощалась, собрала бумагу и ушла."
    th "Ну, значит, не больно-то и хотелось, значит, мне и не нужно это видеть."
    "Женя ещё раз обвела глазами библиотеку, увидела журналы на полке с прочитанной и возвращённой литературой."
    th "Интересно, кто брал?"
    show dct_formular_d_ma:
        xcenter 0.5 rotate -15 alpha 0
        pause 0.5
        linear 0.25 alpha 1
    "Глянула в ящик с читательскими формулярами."
    th "Cудя по почерку, «средний» на «старший» Лена исправила."

    scene bg int_library_day
    show d_mz smile2 pioneer glasses close
    with squares
    mz "Любит ли читать — я ещё не знаю, но умеет — это точно."
    show d_mz sceptic pioneer glasses close with dspr
    play music music_list['just_think'] fadein 2
    "Женя взяла самый верхний журнал и быстро пролистала его. Нет, всё верно, вон и библиотечный штамп на месте. Но всё же."
    show d_mz surprise pioneer glasses close with dspr
    "Женя подошла к каталогу, выдвинула несколько ящичков и умело пробежалась по картотеке, потом проделала это ещё раз, читая каждую карточку, вынимая карточки из ящичков и проверяя, не завалилась ли какая-нибудь карточка, выпав из общего ряда."
    show d_mz amazed pioneer glasses close with dspr
    "Ничего нового, никаких поступлений, но в фондах библиотеки «Совёнка» не числилось ни одного номера журнала «Знание-сила». Несмотря на библиотечный штамп на этих самых журналах."
    show d_mz normal pioneer glasses close with dissolve_fast
    "Женя вернулась к журналам, взяла с полки самый верхний, посмотрела на первую страницу обложки, потом перевернула и посмотрела на типографские данные."
    "«Сдано в набор 06.09.1991»."
    show d_mz smile2 pioneer glasses close with dissolve_fast
    "Согласно календарику, притаившемуся под оргстеклом, покрывающим стол, на дворе стоял июнь 1987 года."
    show d_mz sceptic pioneer glasses close with dissolve_fast
    th "Кажется, придётся прийти на сбор отряда."
    th "Кажется, придётся спросить у новенького, где он берёт журналы. Может, он и книг хороших оттуда же натаскает?"
    stop ambience fadeout 1
    stop music fadeout 1

    scene dct_int_house_of_sa_day with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    "Саша, чуть-чуть разминувшаяся с Леной, сейчас сидела у себя в домике и с огромным удовольствием читала ту самую пионерскую сказку. Читала, возвращалась к началу, закрывала глаза и как живых представляла себе героинь: Анфису, Ларису, Жанну, Машу. Тем более что и представлять особо не нужно."
    th "Вон же они, как живые. Ясно, с кого их списывали. Нет, разница, конечно, есть, так на то и сказка."
    "Вот ни Святославы, ни Янки, ни Степана здесь не было. Святослава чуть походила на саму Сашу, но совсем-совсем чуть-чуть."
    th "Янка… Может быть, если бы Ульяна была помоложе лет на пять, то так она себя бы и вела. Степан? Не могу себе представить — неужели Семён был таким?"
    th "Нет, в нём, конечно, живёт семнадцатилетний пионер, это невооружённым глазом видно, но и двадцатипятилетний заместитель начальника лагеря — тоже в нём."
    th "Как, когда Мику успела всё это сочинить? Она же сама говорила в день приезда, когда знакомились, что она впервые в СССР, а её папа с мамой сейчас едут на поезде из Владивостока в Москву с остановками в крупных городах."
    th "Но вот же автор: Мику Хацуне, а вот посвящение: «Сенечке, которому… и Ульянке…», и подпись японскими закорючками. То есть Мику знала Семёна, когда тому было семнадцать? А самой Мику, получается, восемь-девять? Ничего не понимаю, надо будет спросить для начала у Лены."
    "Саша посмотрела на стену над Лениной кроватью, всю увешанную картинами. Портреты и пейзажи. Три портрета особенно притягивали взгляд."
    "Женщина, похожая на Лену как родная мама, протягивает руки открытыми ладонями к зрителю, губы плотно сжаты, глаза чуть прищурены, как будто какую-то работу делает или спорит с кем-то, а если присмотреться, то такая бездна боли в этих прищуренных глазах…"
    "Второй портрет: парень, похожий на Семёна — наверное, таким он и был в семнадцать лет, только глаза не семнадцатилетние, а взрослые и какие-то уставшие, что ли, но понимаешь, что он сейчас улыбнётся этими уставшими глазами и скажет: «Всё ерунда, прорвёмся!»."
    "Третий портрет — тот очень позитивный: на нём Семён и Ульяна, сидящие рядышком, рука в руке, на крыльце этого самого домика — оба улыбаются, оба счастливы, как раз и видно, что подросток из заместителя начальника лагеря никуда не делся."
    play sound sfx_knock_door7_polite
    "В дверь постучали."
    play sound sfx_open_door_1 
    show d_ma normal pioneer with dissolve:
        xcenter 0.5 yalign 0.02
    d_ma "Привет."
    sa "Здравствуй!"
    "Саша улыбнулась хорошему человеку."
    show d_ma smile2 pioneer with dspr
    "Очень заразительно улыбнулась — так, что Максим сразу разулыбался в ответ."
    show d_ma smile pioneer with dissolve_fast
    d_ma "Саш, ты не могла бы чуть поучить меня танцевать? К следующей дискотеке?"
    sa "Хочешь Алису удивить…"
    show d_ma shy pioneer with dissolve_fast
    "Саша не спрашивала, а просто констатировала факт."
    sa "Приходи в музыкальный кружок после ужина. С Мику я договорюсь."
    stop ambience fadeout 1

    scene dct_ext_between_beach_and_boathouse_day
    show el smile pioneer at cleft
    show d_oz smile pioneer at cright:
        yalign 0.27
    with dct_fade
    play ambience ambience_lake_shore_day fadein 1
    play music music_list['she_is_kind'] fadein 1
    "Вторую половину дня Сыроежкин провёл в компании милой девушки Оксаны."
    hide el
    hide d_oz
    with dissolve
    "Показывал ей, как правильно держать нож, объяснял, когда режут от себя, а когда — к себе, ругался на нож, который она принесла, а потом объяснял, почему острый нож безопаснее тупого."
    show el normal pioneer at cleft with dissolve
    el "Ты когда острым ножом режешь, рука просто идёт за ножом и всё, и не надо лишних усилий делать. Просто следи, чтобы пальцы на пути у лезвия не оказались."
    show el serious pioneer with dissolve_fast
    extend " А когда режешь тупым, то ты напрягаешься, и у тебя нож обязательно сорвётся и попадёт по пальцам, как бы ты их ни берегла."
    hide el with dissolve   
    stop ambience fadeout 1

    scene bg int_clubs_male_day:
        zoom 1.2 align (0.0, 0.9)
    show sh serious pioneer far at fright:
        ycenter 0.515
    with dissolve_fast
    play sound sfx_close_door_1
    pause 0.2
    show sh normal pioneer far with dspr
    $ day_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Сходили в клуб, извинились перед Шуриком за то, что помешали, и заточили нож Оксане."

    scene black with dissolve_fast
    $ set_mode_nvl()
    window show

    scene dct_ext_between_beach_and_boathouse_day with dissolve_fast
    "Потом искали вдвоём подходящий кусок коры, и Оксана пыталась выстругать хоть что-то похожее на кораблик.\n"
    el "Стой. А теперь, прежде чем за нож браться, нарисуй, что ты хочешь. Да вот хоть на мокром песке палочкой и нарисуй."
    d_oz_nvl "Вот так, да?"
    el "Нет, смотри, как надо."
    "\nПотом разбирали проект Оксаны по косточкам.\n"
    el "А ты хочешь, чтобы он просто на полке стоял или чтобы его ещё и на воду спустить можно было?"    
    d_oz_nvl "..."
    el "Знаешь, напиши ему письмо, небольшое, чтобы упаковать можно было.{w} Потом в полиэтилен запаяем и внутри корабля спрячем.{w} Если всё так, как ты говоришь — он обязательно полезет разбирать твой подарок. Там письмо и найдёт. Может, это сработает."
    "\nИ снова взялись за ножи."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    el "А почему ты всё своими руками должна делать?"
    d_oz_nvl "..."
    el "Что значит — иначе цикл не переживёт?"
    d_oz_nvl "..."
    el "Не знаю, Оксана, права ты или нет, но, может, это мы уходим куда-то дальше, а вы здесь задерживаетесь."
    nvl hide dissolve
    nvl clear

    scene black with dissolve_fast
    window hide

    scene dct_ext_between_beach_and_boathouse_sunset with dissolve_fast
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_lake_shore_evening fadein 1
    $ set_mode_adv()
    window auto
    "Ну и всё это перемежалось другими разговорами."
    show d_oz n pioneer at cright with dissolve:
        yalign 0.27
    d_oz "Вот знаешь, Серёжа, мне кажется, ты ей нравишься."
    show d_oz smile pioneer with dspr
    extend " Если бы не нравился, она бы не стала тебя прогонять."
    show d_el smile2 pioneer at cleft with dissolve
    el "Эх, Оксана, твои бы слова да богу, которого нет, в уши."
    hide d_oz
    hide d_el
    with dissolve
    "И расстались уже перед самым ужином, договорившись о завтрашней встрече."
    show d_oz d pioneer at center:
        yalign 0.27
    with dissolve
    d_oz "Знаешь, Серёжа…"
    show d_oz smile pioneer with dspr
    extend " Нет, потом, в конце смены. До завтра!"
    hide d_oz with dissolve_fast
    "И убежала, прихватив с собой недоделанный кораблик."
    "А Электроник ещё посидел на берегу, улыбаясь и думая о том, какая это славная девочка, и о её словах, что он Жене нравится."
    stop music fadeout 2
    play sound dct_sfx_horn_dinner_through_loudspeaker
    $ sunset_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    "Дождался горна и уже тогда встал, отряхнулся и пошёл — сперва в кружок за Шуриком, а оттуда на ужин."
    stop ambience fadeout 1
    stop sound fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ night_time()
    $ persistent.sprite_time = "day"

    scene bg int_house_of_dv_night
    show 3500_dv sad night2 0pt at right:
        ycenter 0.83
    with dissolve_fast
    play ambience ambience_int_cabin_night fadein 1
    "Алиса была помощницей вожатой в этом лагере исключительно из-за отсутствия альтернатив, и помощница вожатой из неё вышла плохая, но какие-то привычки въелись, и их уже не вытравить. Вот и сейчас она перебирала в памяти прожитый день, анализировала свои ошибки, делала выводы и строила планы на завтра."
    show 3500_dv normal night2 0pt with dissolve_fast
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Что там со мной и лагерем происходило сегодня?"
    stop ambience fadeout 1

    scene bg ext_path_day
    show ext_path_sunset:
        alpha 0.6
    show d_sf normal sport at right
    show d_us normal sport at center:
        ypos -0.05
    show dct_dream_veil at shiver
    with blinds
    $ day_time()
    play music music_list['raindrops'] fadein 1
    "Прощание с Персуновыми в пять утра. Алиса не утерпела и вскочила в такую рань, чтобы проводить своих самых близких людей, уходящих в утреннюю хмарь."
    dv "Вы туда же, на то же место?"
    me "Да, Алис. Точка стабильная и ещё долго продержится. Да не кисни, Рыжая. Завтра же придём назад!"

    scene bg ext_playground_day
    show dct_dream_veil at shiver
    with dissolve
    "Спать уже не хотелось, поэтому присела на крыльце спортзала, кутаясь в куртку. И в каком-то оцепенении провела час, пока не появилась Сашка, возобновившая свои утренние пробежки."
    show sl smile sport behind dct_dream_veil at right with dissolve
    dv "Привет."
    sa "Доброе утро, Алиса. Побежали со мной?"
    dv "Пф-ф. Я что, больная? Ты-то почему одна? Катька отказалась?"
    show sl sad sport with dissolve_fast
    sa "Да, не пойму я её что-то. Вчера просилась, а вечером, после дискотеки, я зашла к ней напомнить, а та уже передумала.{w} Ещё и смотрит обиженно, и глаза красные, будто плакала."
    show sl normal sport with dissolve_fast
    sa "Ладно, побежала я."
    play sound "<from 2>" + sfx_slavya_run fadein 1
    $ renpy.pause (0.2)
    hide sl with MoveTransition(1.2, leave=_moveleft, leave_time_warp=_ease_time_warp)
    $ renpy.pause (0.4)
    stop sound fadeout 1.3
    "И убежала, только лёгкие шлепки подошв о покрытие беговой дорожки были слышны за спиной."

    scene bg ext_square_day
    show d_ma normal pioneer:
        zoom 1.25 xcenter 0.5 yalign 0.08
    show dct_dream_veil at shiver
    with dissolve
    "Чуть позже — Максим, который хотел спросить о чём-то, но так и не решился."

    scene dct_lineup_mi_not_us
    show dct_dream_veil at shiver
    with dissolve
    "Ещё чуть позже — линейка, слава богу, в этом цикле не военизированная."

    scene bg ext_square_day
    show mt normal panama pioneer
    show dct_dream_veil at shiver
    with dissolve
    mt "Алиса, а ты не в курсе, где наши физруки? Они предупредили, что появятся завтра после завтрака, но о подробностях умолчали."
    dv "Ольга Дмитриевна, помните, в первый день сестрёнка Ульянина отметилась, которая отдыхает тут недалеко? Вот, кажется, её навестить."
    show mt surprise panama pioneer with dspr
    mt "Недалеко? Странно. До ближайших людей здесь километров триста."
    show mt normal panama pioneer with dspr
    extend " Ну ладно, Алиса, на субботу какие мероприятия запланировала?"

    scene bg ext_clubs_day
    show el smile pioneer at cright
    show sh laugh pioneer at cleft
    show dct_dream_veil at shiver
    with dissolve
    "Кибернетики затеяли что-то новое в своей берлоге."
    show d_el smile2 pioneer as el
    show sh smile pioneer
    with dspr
    $ day_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Надо будет убедиться, что это безопасно для окружающих."
    stop music fadeout 2

    scene black with dissolve_fast
    pause 0.5
    $ night_time()

    scene bg int_house_of_dv_night
    show 3500_dv normal night2 0pt at left:
        ycenter 0.83
    with blinds
    play ambience ambience_int_cabin_night fadein 1
    "И так обо всём дне."
    show 3500_dv shocked night2 0pt with dissolve_fast
    "А ещё завтра открытие купального сезона, и физруки на пляже были бы ох как уместны."
    show 3500_dv sad night2 0pt with dissolve_fast
    th "Надо будет на следующий цикл убедительно попросить их не уходить вдвоём."
    show 3500_dv grin night2 0pt with dissolve_fast
    extend " Стоп.{w=0.5} Они же завтра к одиннадцати обещали вернуться, так что всё нормально."
    show 3500_dv guilty night2 0pt with dissolve_fast
    "Алиса покосилась на бывшую Ульянкину кровать, занятую сейчас гитарой и одеждой."
    show 3500_dv sad night2 0pt with dspr
    th "Привыкаю постепенно — вот уже и её кровать своими вещами занимаю, и бельё на эту кровать брать на складе не стала. Но всё равно вечерами тоскливо. Хорошо хоть Ульянка каждый вечер специально поболтать заходит."
    show 3500_dv normal night2 0pt with dissolve_fast
    th "И хорошо, что она меня простила."
    hide 3500_dv
    show d_us normal sport at center:
        zoom 1.25 ypos -0.1
    show dct_dream_veil at shiver
    with dissolve_fast
    us "Алиса, если бы ты в тот раз промахнулась, то Семён прошёл бы сквозь наш лагерь мимо и дальше."
    hide d_us
    hide dct_dream_veil
    show 3500_dv shy night2 0pt at left with dissolve_fast:
        ycenter 0.83
    with dissolve_fast
    th "А эта «сестрёнка» Ульянкина тоску разбередила."
    th "Уговорить бы её здесь остаться — так в её лагере своя Алиса есть, той тогда совсем плохо будет. Хуже, чем мне в прошлом цикле.{nw}"
    
    ########## Предварительная подгрузка первой половины шаров ##########
    show dct_multiverse_ball_to_dv_01:
        xcenter 2.0 ycenter -2.5
    show dct_multiverse_ball_to_dv_02:
        xcenter 2.0 ycenter -2.0
    show dct_multiverse_ball_to_dv_03:
        xcenter 2.0 ycenter -1.5
    show dct_multiverse_ball_to_dv_04:
        xcenter 2.0 ycenter -1.0
    show dct_multiverse_ball_to_dv_05:
        xcenter 2.0 ycenter -0.5
    show dct_multiverse_ball_to_dv_06:
        xcenter 2.0 ycenter 0.0
    show dct_multiverse_ball_to_dv_07:
        xcenter 2.0 ycenter 0.5
    show dct_multiverse_ball_to_dv_08:
        xcenter 2.0 ycenter 1.0
    show dct_multiverse_ball_to_dv_09:
        xcenter 2.0 ycenter 1.5
    show dct_multiverse_ball_to_dv_10:
        xcenter 2.0 ycenter 2.0
    #####################################################
    
    extend ""  # Тег {nw} из предыдущей строки с текстом автоматически подтягивает эту строку, и пока читатель дочитывает предыдущую, происходит предварительная прогрузка шаров, прописанных между этими двумя строками
    show 3500_dv normal night2 0pt with dissolve_fast
    th "А у меня уже какие-то просветы появились. Вроде Макса того же."
    show 3500_dv laugh night2 0pt with dspr
    extend " Правильно Мику про него сказала, что он тычется всюду с любопытством и дружелюбием, как молодой пёс.{nw}" # Тег {nw} автоматически подтягивает следующую текстовую строку
    
    ########## Предварительная подгрузка второй половины шаров ##########
    show dct_multiverse_ball_to_dv_11:
        xcenter -1.0 ycenter -2.5
    show dct_multiverse_ball_to_dv_12:
        xcenter -1.0 ycenter -2.0
    show dct_multiverse_ball_to_dv_13:
        xcenter -1.0 ycenter -1.5
    show dct_multiverse_ball_to_dv_14:
        xcenter -1.0 ycenter -1.0
    show dct_multiverse_ball_to_dv_15:
        xcenter -1.0 ycenter -0.5
    show dct_multiverse_ball_to_dv_16:
        xcenter -1.0 ycenter 0.0
    show dct_multiverse_ball_to_dv_17:
        xcenter -1.0 ycenter 0.5
    show dct_multiverse_ball_to_dv_18:
        xcenter -1.0 ycenter 1.0
    show dct_multiverse_ball_to_dv_19:
        xcenter -1.0 ycenter 1.5
    show dct_multiverse_ball_to_dv_20:
        xcenter -1.0 ycenter 2.0
    #####################################################
    
    extend ""  # Тег {nw} из предыдущей строки с текстом автоматически подтягивает эту строку, и пока читатель дочитывает предыдущую, происходит предварительная прогрузка шаров, прописанных между этими двумя строками
    show 3500_dv smile night2 0pt with dspr
    th "Было бы ему хоть на пару лет побольше."
    show 3500_dv normal night2 0pt with dspr
    "Алиса посмотрела на гитару, но нет — настроения не было."
    show d_int_house_of_dv_night_without_light behind bg
    show 3500_dv normal night2 0pt as dv at left behind bg:
        ycenter 0.83 alpha 1 matrixcolor TintMatrix("#A1C9D0")  # Перекраска спрайта через преобразование matrixcolor. Свойство TintMatrix с цветом "#A1C9D0" даёт результат почти идентичный ночным спрайтам
    show dct_cg_christmas_balls_composite behind d_int_house_of_dv_night_without_light:     # КОМПОЗИТНЫЙ АРТ: еловый фон; площадь в форме шара; Алиса в шаре; матовое полупрозрачное напыление поверх шара
        zoom 1.0 anchor (1.0, 0.5) pos (1.0, 0.5)
    th "Ну, значит, спать."
    play sound sfx_click_1
    pause 0.2
    hide bg
    hide 3500_dv smile night2 0pt
    show 3500_dv normal night2 0pt as dv at left:
        ycenter 0.83 alpha 1 matrixcolor TintMatrix("#A1C9D0")  # Перекраска спрайта через преобразование matrixcolor. Свойство TintMatrix с цветом "#A1C9D0" даёт результат почти идентичный ночным спрайтам
        pause 0.8
        linear 1 alpha 0
    with dspr
    play sound sfx_bed_squeak2
    "Погасила свет и завернулась в простыню."
    $ night_time()
    extend " Она уже знала, что ей приснится."
    window hide
    
    #
    #   Сон Алисы
    #
    $ prolog_time()
    $ renpy.music.set_volume(0.3, delay=0)
    stop ambience fadeout 3
    play music music_list['tried_to_bring_it_back'] fadein 3
    show d_int_house_of_dv_night_without_light as d_int_house_of_dv2 at shiver with Dissolve (0.0)
    hide d_int_house_of_dv_night_without_light
    hide d_int_house_of_dv2
    with Dissolve (3.5)
    window auto
    "Каждую ночь с середины прошлого цикла Алисе обязательно снился один и тот же сон.{nw}"
    
    ##########   Предварительная подгрузка тумана и сияния  ##########
    
    # Полярное сияние
    show dct_multiverse_polar_lights_1:
        anchor (0.0, 0.5) pos (1.1, 0.5) alpha 0.3
    show dct_multiverse_polar_lights_2:
        anchor (0.5, 0.0) pos (0.5, 1.1) alpha 0.3
    
    # Туман
    show dct_multiverse_fog_1:
        anchor (1.0, 0.5) pos (-0.1, 0.5)
    show dct_multiverse_fog_2:
        anchor (0.5, 1.0) pos (0.5, -0.1)
    show dct_multiverse_fog_3:
        anchor (1.0, 1.0) pos (-0.1, -0.1)
    show dct_multiverse_fog_4:
        anchor (1.0, 0.0) pos (-0.1, 1.1)
    show dct_multiverse_fog_5:
        anchor (0.0, 1.0) pos (1.1, -0.1)
    show dct_multiverse_fog_6:
        anchor (0.0, 0.0) pos (1.1, 1.1)
    ##################################################################
    
    extend " "  # Это такая пауза в виде пробела, чтобы текст не пропадал, пока идёт предварительная прогрузка сияния и тумана
    extend "Очень спокойный, никуда не зовущий, не оставляющий после себя никаких эмоций — он просто снился."
    window hide
    $ renpy.music.set_volume(1.0, delay=3)
    show dct_cg_christmas_balls_composite:     # КОМПОЗИТНЫЙ АРТ: еловый фон; площадь в форме шара; Алиса в шаре; матовое полупрозрачное напыление поверх шара
        parallel:
            pause 1.6
            ease 2.2 pos (1.8, 0.5)
        parallel:
            ease 1.9 zoom 0.6
            ease 1.9 zoom 1
    $ renpy.pause(3.8,hard=True)
    
    # В этот момент единый композитный арт подменяется четырьмя раздельными слоями

    scene dct_cg_christmas_balls_back:                  # Фон с еловыми ветками
        zoom 1.0 anchor (0.35, 0.5) pos (0.5, 0.5)
    show dct_ball_to_world01:                           # Площадь в форме ёлочного шара
        zoom 1.23 xcenter 0.5 ycenter 0.5 matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.6, 0.05)) * TintMatrix("#be6012")
    show dct_dv_in_christmas_ball:                      # Алиса в ёлочном шаре
        zoom 0.82 anchor (0.521, 0.328) pos (0.5, 0.5) matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.8, 0.05)) * TintMatrix("#be8012")
    show dct_christmas_ball:                            # Декоративная имитация ёлочного шара поверх площади и Алисы
        zoom 1.0 anchor (0.5, 0.5) pos (0.5, 0.5)

    window show
    "Начинался сон с того, что Алиса оказывалась заперта внутри латунно-жёлтого зеркального шара — ёлочной игрушки."
    show dct_cg_christmas_balls_back:                   # Фон с еловыми ветками
        zoom 1 pos (0.5, 0.5)
    show dct_ball_to_world01:                           # Площадь в форме ёлочного шара    
        zoom 1.23 xcenter 0.5
    show dct_dv_in_christmas_ball:                      # Алиса в ёлочном шаре
        zoom 0.82 pos (0.5, 0.5)
    show dct_christmas_ball:                            # Декоративная имитация ёлочного шара поверх площади и Алисы
        zoom 1 pos (0.5, 0.5)
    show dct_cg_christmas_balls_back:                   # Фон с еловыми ветками
        linear 2 zoom 1.22 blur 80
    show dct_ball_to_world as dct_ball_to_world01 behind dct_dv_in_christmas_ball:  # Площадь распахивается из шара. Подменяет собой площадь в ёлочном шаре (и имеет те же искажённые матрицей цвета), чтобы не возникало визуального конфликта со следующей картинкой
        linear 2 zoom 1.5
    show dct_ball_to_world behind dct_dv_in_christmas_ball:     # Площадь распахивается из шара. Самостоятельная версия, постепенно проявляется, и перекрывает своим цветом предыдущую картинку
        zoom 1.23 xcenter 0.5 ycenter 0.5 alpha 0
        linear 2 zoom 1.5 alpha 1
    show dct_dv_in_christmas_ball:                      # Алиса в ёлочном шаре
        linear 2 zoom 1
    show 3500_dv normal pioneer2:                       # Алиса на площади в полный рост
        zoom 0.82 anchor (0.521, 0.328) pos (0.5, 0.5) alpha 0
        linear 2 zoom 1 alpha 1
    show dct_christmas_ball:
        linear 1 zoom 1.11 alpha 0                      # Декоративная имитация ёлочного шара поверх площади и Алисы. ГЛУШИМ ЕЁ.
    "Постепенно размеры игрушки росли, стенки отдалялись, теряли чёткость, горизонт становился всё дальше, и вдруг Алиса понимала, что она уже не внутри зеркального шара, а снаружи.{nw}"

    ########## Запускаем шары, и прячем их под Алисой, площадью и белой вспышкой ##########

    # Звёздное небо
    scene stars_1:
    show stars_3:
        linear 0.7 alpha 0
        pause 0.3
        linear 0.7 alpha 1
        pause 0.3
        repeat
    
    # Полярное сияние
    show dct_multiverse_polar_lights_1:
        anchor (0.0, 0.5) pos (0.0, 0.5) alpha 0.0
        parallel:
            easeout 68.4 anchor (0.5, 0.35) pos (0.5, 0.35) knot (0.5, 0.5)
            easein 68.4 anchor (1.0, 0.5) pos (1.0, 0.5) knot (0.5, 0.5)
            easeout 68.4 anchor (0.5, 0.65) pos (0.5, 0.65) knot (0.5, 0.5)
            easein 68.4 anchor (0.0, 0.5) pos (0.0, 0.5) knot (0.5, 0.5)
            repeat
        parallel:
            dct_polar_lights        # Периодическое сверкание
    show dct_multiverse_polar_lights_2:
        anchor (0.5, 0.0) pos (0.5, 0.0) alpha 0.0
        parallel:
            easeout 49.8 anchor (0.35, 0.5) pos (0.35, 0.5) knot (0.5, 0.5)
            easein 49.8 anchor (0.5, 1.0) pos (0.5, 1.0) knot (0.5, 0.5)
            easeout 49.8 anchor (0.65, 0.5) pos (0.65, 0.5) knot (0.5, 0.5)
            easein 49.8 anchor (0.5, 0.0) pos (0.5, 0.0) knot (0.5, 0.5)
            repeat
        parallel:
            dct_polar_lights        # Периодическое сверкание

    # Туман
    show dct_multiverse_fog_1:
        anchor (0.5, 0.5) pos (0.425, 0.5) rotate 0
        linear 11 pos (0.45, 0.4) rotate -45
        linear 11 pos (0.5, 0.37) rotate -90
        linear 11 pos (0.55, 0.4) rotate -135
        linear 11 pos (0.575, 0.5) rotate -180
        linear 11 pos (0.55, 0.6) rotate -225
        linear 11 pos (0.5, 0.63) rotate -270
        linear 11 pos (0.45, 0.6) rotate -315
        linear 11 pos (0.425, 0.5) rotate -360
        repeat
    show dct_multiverse_fog_2:
        anchor (0.5, 0.5) pos (0.575, 0.5) rotate 0
        linear 10 pos (0.55, 0.4) rotate 45
        linear 10 pos (0.5, 0.37) rotate 90
        linear 10 pos (0.45, 0.4) rotate 135
        linear 10 pos (0.425, 0.5) rotate 180
        linear 10 pos (0.45, 0.6) rotate 225
        linear 10 pos (0.5, 0.63) rotate 270
        linear 10 pos (0.55, 0.6) rotate 315
        linear 10 pos (0.575, 0.5) rotate 360
        repeat
    show dct_multiverse_fog_3:
        align (1.0, 0.0)
        ease 76.6 align (0.0, 1.0)
        ease 76.6 align (1.0, 0.0)
        repeat
    show dct_multiverse_fog_4:
        align (0.0, 0.0)
        ease 66.2 align (1.0, 1.0)
        ease 66.2 align (0.0, 0.0)
        repeat
    show dct_multiverse_fog_5:
        xcenter 0.5 yalign 0.0
        ease 61.0 yalign 1.0
        ease 61.0 yalign 0.0
        repeat
    show dct_multiverse_fog_6:
        xalign 0.0 ycenter 0.5
        ease 53.6 xalign 1.0
        ease 53.6 xalign 0.0
        repeat
        
    # Шары-миры
    $ renpy.random.shuffle(dct_balls_list)   # Перемешиваем список шаров, чтобы в разных случаях на переднем плане оказывались разные шары
    show expression "dct_multiverse_ball_[dct_balls_list[0]]" as dct_ball_00 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[1]]" as dct_ball_01 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[2]]" as dct_ball_02 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[3]]" as dct_ball_03 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[4]]" as dct_ball_04 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[5]]" as dct_ball_05 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[6]]" as dct_ball_06 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[7]]" as dct_ball_07 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[8]]" as dct_ball_08 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[9]]" as dct_ball_09 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[10]]" as dct_ball_10 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[11]]" as dct_ball_11 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[12]]" as dct_ball_12 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[13]]" as dct_ball_13 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[14]]" as dct_ball_14 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[15]]" as dct_ball_15 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[16]]" as dct_ball_16 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[17]]" as dct_ball_17 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[18]]" as dct_ball_18 at dct_balls_scale
    show expression "dct_multiverse_ball_[dct_balls_list[19]]" as dct_ball_19 at dct_balls_scale
    ##########################################################################################
    
    show dct_ext_square_extended_day:           # Площадь. Псевдорасширенная версия. Но так как мы уводим всё в белый цвет, то годится и такая
        zoom 1.5 xcenter 0.5 ycenter 0.5
    show 3500_dv normal pioneer2:               # Алиса на площади в полный рост
        zoom 1 anchor (0.521, 0.328) pos (0.5, 0.5)
    extend " "  # Это такая пауза в виде пробела, чтобы предыдущий текст не пропадал, пока идёт предварительная прогрузка вышепрописанной простыни
    show dct_ext_square_extended_day:           # Площадь. Псевдорасширенная версия. Но так как мы уводим всё в белый цвет, то годится и такая
        zoom 1.5 xcenter 0.5 ycenter 0.5
        easeout_cubic 5 zoom 0.58
    show 3500_dv normal pioneer2:               # Алиса на площади в полный рост
        zoom 1 anchor (0.521, 0.328) pos (0.5, 0.5)
        easeout 5 zoom 0.32
    show white:
        alpha 0
        pause 4.0
        ease 1.0 alpha 1
    "А потом этот шар начинал уменьшаться в размерах, горизонт опять приближался, и оказывалось, что вокруг Алисы плавают, иногда соприкасаясь, а иногда слипаясь в устойчивые гроздья, множество таких шаров."
    window hide
    
    ########## Убираем Алису, площадь и белый экран, являя шары читателю ##########
    hide dct_ext_square_extended_day
    hide 3500_dv normal pioneer2
    show white:
        linear 1.5 alpha 0
    pause
    
    # Добавляем Алис к шарам
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[0]]" as dct_ball_00
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[1]]" as dct_ball_01
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[2]]" as dct_ball_02
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[3]]" as dct_ball_03
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[4]]" as dct_ball_04
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[5]]" as dct_ball_05
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[6]]" as dct_ball_06
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[7]]" as dct_ball_07
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[8]]" as dct_ball_08
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[9]]" as dct_ball_09
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[10]]" as dct_ball_10
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[11]]" as dct_ball_11
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[12]]" as dct_ball_12
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[13]]" as dct_ball_13
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[14]]" as dct_ball_14
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[15]]" as dct_ball_15
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[16]]" as dct_ball_16
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[17]]" as dct_ball_17
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[18]]" as dct_ball_18
    show expression "dct_multiverse_ball_to_dv_[dct_balls_list[19]]" as dct_ball_19

    window auto
    "И внутри каждого спрятана своя Алиса — в чём-то абсолютно такая же, а в чём-то похожая только на саму себя."
    "И можно перепрыгнуть со своего шара на соседний и проснуться уже там, внутри, рядом с двойником. И с двойником при таком проникновении ничего не случится. Вот только надо решиться прыгнуть."
    th "Интересно, Ленке то же самое снится?"
    stop music fadeout 4
    show black:
        alpha 0
        pause 0.5
        linear 3 alpha 1
    th "Она ведь та ещё партизанка — будет молчать, пока совсем плохо не станет."
    stop sound fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2
    
    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    
    
    
################
#Глава 5. Дебют#
################

label dct_debut_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Дебют"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава V. Дебют" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene save_bg
    show black
    play music crush
    show promo_text_un u"{color=#fff226}Из рабочей тетради Шурика Трофимова.{/color}" at truecenter with dspr
    $ renpy.pause(3.0)
    show promo_text_un u"{color=#fff226}Из рабочей тетради Шурика Трофимова.{/color}":
        ease 1.2 yalign 0.05
    hide black with dissolve
    $ set_mode_nvl()
    window show
    "Пятый день смены."
    "\nНеобычные мысли, сны и явления."
    "\n1. Опять приснился сон про полигон и маленького человечка.{w} Рассмотрел во сне этого «человечка» и вычёркиваю его из списка загадок. Человечек похож на недоделанного робота, оставленного пионерами, отдыхавшими здесь до нас.{w} Видимо, во сне реализовалось моё подсознательное желание видеть этого робота функционирующим."
    "\n2. Обнаружено нештатное потребление электроэнергии.{w} Вчера вечером перед уходом были обесточены все электроприборы и отключены автоматы на щитке. Сегодня утром счётчик показал расход 2 кВт·ч электроэнергии.{w} Сыроежкин ничего не смог пояснить по этому поводу: утверждает, что ничего не включал."
    "\n3. Когда вижу кого-либо из пионеров или персонала лагеря, включая вожатую, я могу сразу сказать, микс это или копия.{w} Что значат эти слова применительно к человеку — я не знаю."
    "\n4. Регулярно вспоминается женское имя «Яна».{w} Твёрдо уверен, что у меня нет знакомых с таким именем."
    "\n\nПлан работы в кружке кибернетики на день…"
    stop music fadeout 1
    nvl hide dissolve
    nvl clear
    
    scene black with dissolve_fast
    window hide

    scene dct_int_clubs_male2_night_zoom
    show sh serious pioneer
    with dissolve
    play ambience ambience_int_cabin_day fadein 1
    $ set_mode_adv()
    window auto
    sh "Сергей, на мне сегодня пайка, а ты собираешь излучатели и приёмники ультразвука. Так?"
    show sh normal pioneer with dspr
    "Сыроежкин только пожал плечами: всё было обговорено ещё вчера."
    sh "…и, Сергей, ты говоришь, что девочки хотели поучаствовать в испытаниях прибора."
    el "Да, Лена и Мику. Я сказал им, что если доктор не возражает, то мы не против."
    show sh serious pioneer with dspr
    sh "Хорошо, тогда мнением доктора сам поинтересуйся, пожалуйста."
    sh "А то девочки начнут доктору рассказывать и что-нибудь напутают."
    show sh normal pioneer with dspr
    "Шурик оглянулся на товарища и увидел, что тот, весь подобравшись, как охотничья собака, внимательно смотрит сквозь открытую дверь на противоположную сторону аллеи."

    scene int_clubs_male_day
    show el serious pioneer close at cleft
    with dissolve
    play music homeworldcollapse 
    "Что-то невидимое, жужжа электромоторами и иногда задевая за кусты, скрывающие заброшенное здание напротив, двигалось со скоростью пешехода по обочине главной аллеи от перекрёстка в направлении ворот."
    show el angry pioneer close with dspr
    el "Уйдёт ведь!"
    show sh surprise pioneer close at right with moveinright
    sh "Сергей, нет!"
    show el serious pioneer close
    show sh normal pioneer close
    with dspr
    extend " Лучше понаблюдаем. Если это пришло сюда один раз, то придёт и ещё."
    show sh serious pioneer close with dspr
    sh "И пожалуйста, вдруг это там, за кустами, октябрёнок балуется?"
    show el surprise pioneer close with dissolve_fast
    el "Ох-х-х… Да."
    play sound sfx_chair_fall
    "Небольшой трансформатор выпал из разжавшейся кисти Сыроежкина обратно на стол, глухо стукнув при этом."
    show el sad pioneer close with dspr
    stop music fadeout 2
    el "Этого я не учёл."
    show sh normal_serious pioneer close dct with dissolve_fast
    sh "Но, Сергей."
    sh "Предположим, мы действительно видели то, что видели. Тогда наш долг перед наукой — описать всё это."
    show sh normal pioneer close with dissolve_fast
    extend " И надо обязательно указать время. Сейчас девять часов двадцать семь минут."
    stop ambience fadeout 1

    scene bg ext_path2_day
    show ext_path2_day at walking
    with dct_fade
    play ambience ambience_forest_day fadein 1
    play sound_loop "<from 7.0 loop 7.0>" + dct_sfx_steps3
    us "Сёмк."
    me "Да, Рыжик?"
    us "Хорошо как. Девочки теперь знают, что они не одни."
    us "Жалко, что мы все вместе собраться не можем.{w} Только в Шлюзе, а там мы спим."
    "И тут мысль Ульянки перескочила."
    us "Сём, а ты ведь не спишь в Шлюзе. Расскажи, что ты там делаешь?"
    me "Страдаю, Уля…"
    stop sound_loop fadeout 1
    stop ambience fadeout 1
    play music higekitekina fadein 1
    show ext_path2_day at walking:
        linear 0.5 alpha 0

    scene bg ext_path2_day
    $ set_mode_nvl()
    "Ну как рассказать обо всём в двух словах?{w} Рассказать, как стараешься выскочить из автобуса первым и страхуешь девочек. Видишь, как они строятся, и сам борешься с желанием встать в тот же строй. Как стараешься прикоснуться ко всем пионерам, как целуешь Ульянку.{w} А когда автобусы глушат двигатели, то над остановкой воцаряется только шаркающий звук шагов, усиленный многократным повторением. Это спящие пионеры начинают перемещаться к воротам."
    "\nКак ты идёшь параллельным курсом, держа Рыжика за руку, стараясь подстроиться под её ковыляющую походку.{w} Как строй втягивается в ворота, и ты отпускаешь руку Ульяны, оставаясь снаружи. Как ты на прощание пожимаешь предплечье Мику, замыкающей строй, прощаясь в её лице со всеми пионерами.{w} И как, стараясь не заглядывать в ворота, возвращаешься к остановке и там дремлешь, время от времени приходя в себя от сырости и предутреннего холода и проверяя — далеко ли до рассвета, на месте ли автобусы, не начали ли возвращаться пионеры?{w} Убеждаешься, что всё в порядке, подкидываешь ещё пару сучьев в костёр и продолжаешь ждать, пребывая в полудрёме. А вокруг тебя крутятся картины вероятностных миров с твоим и твоих близких участием."
    "\nКак иногда к костру подсаживается Яна, у которой последнее время всё более и более муторно в её электронно-нейтринной душе.{w} Кошкоробот не жалуется, но в ней всё больше и больше от человека, и блики костра на алюминиевом лице и щитке, закрывающем фотоматрицы, вполне заменяют мимику. И эмоции видны совершенно ясно.{w} «Почему папа меня не видит?» — нарушает тишину Яна.{w} Что ей ответить? «Не положено папе» — если только.{w} И хочется прижать к себе эту тушку, бывшую когда-то алюминиевым бидоном. И думаешь о том, что когда-нибудь Яна научится плакать."
    nvl hide dissolve
    nvl clear
    nvl show dissolve 
    "А потом начинает светлеть небо, и слышно, как в автобусах заводятся двигатели, и нужно идти к воротам Шлюза и встречать своих, всматриваться в лица и пытаться понять, не подменили ли человека там, на стадионе.{w} За Артёмом не уследил, и сейчас в лагере другой Артём. Хороший парнишка, но спящий.{w} А вот Мику перехватить удалось, но утро тогда вышло сумасшедшее — пока искал среди всех Мику всех лагерей именно нашу и потом брал за руку и вёл её, покорную, к своему автобусу, говоря ей, спящей в обоих смыслах, какую-то ворчливо-успокоительную чушь, пока отводил «приблудную» Мику к её автобусу, так же успокаивая. И не важно, слышала она что-то или нет.{w} Не знаю, от Алисы заразился, что ли, но бросить своих не могу."
    "\nА когда пионеры начинают просыпаться, тебя начинает трясти страх: вдруг кто-то из девочек выпал из активной фазы?"
    stop music fadeout 3
    extend " Как всё это рассказать, когда вот уже виден забор лагеря в просветы между деревьями?"
    play ambience ambience_forest_day fadein 1
    $ set_mode_adv()
    me "…Страдаю, Уля. Из людей нельзя делать роботов, если уж вложили в них души. А я не могу взять и отключить здесь всю механику. А если бы мог — побоялся бы."
    stop ambience fadeout 1

    scene ext_no_bus with dissolve
    play sound_loop ambience_camp_entrance_day fadein 1
    "Ульяна подождала Семёна, взяла его за руку, и к воротам они подошли уже вместе."
    show d_us normal sport at center:
        ypos -0.05
    show d_sf normal sport:
        xzoom -1.0 xcenter 0.7
    with dissolve
    us "Сём, я не хотела, чтобы ты огорчался, прости."
    us "Но ты бы, если б мог, всё бы отключил — я знаю. Злился бы: «Почему опять я?!». Ругался бы нехорошими словами, но выключил бы этот рубильник."

    scene ext_camp_entrance_day with dissolve
    me "Ты-то тут при чём, Рыжик? Не ты же это устроила, чтобы извиняться."
    stop sound_loop fadeout 1

    scene ext_clubs_day
    show d_sf normal sport:
        xcenter 0.57
    show d_us normal sport:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    show d_us_sport_mirror:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with irisout
    play ambience ambience_camp_center_day fadein 1
    "Лагерь встретил Семёна и Ульяну тишиной и безлюдьем. Даже на клубах висел замок."
    "Асфальт главной аллеи уже успел раскалиться, и в колыхающемся мареве скорее угадывались, чем были ясно различимы вдалеке, фигуры бегающих между спорткомплексом и пляжем пионеров."

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
    us "У тебя ещё и склероз."
    show d_sf normal sport with dspr
    "Ульяна ткнула Семёна кулаком в бок."
    show d_us smile sport with dspr
    us "Сегодня открытие купального сезона же. Ты что, Ольгу не знаешь? Наверняка все на пляже сейчас."
    "И, подражая интонациям вожатой, добавила:"
    show d_us serious sport with dspr
    us "Мероприятие общелагерное, никаких исключений!"
    show d_sf laugh sport with dspr
    stop ambience fadeout 1

    scene dct_ext_beach_day_with_pass_train
    show mt angry panama swim close
    with dct_fade
    play ambience ambience_lake_shore_day fadein 1
    play music music_list['she_is_kind'] fadein 1
    mt "Мальчики, девочки, младший отряд!{w} Все построились и по моей команде заходим в воду!"
    mt "О! Вот и физруки подошли!"

    scene dct_ext_beach_day_lifesaving_shield
    show d_sf normal swim:
        xcenter 0.57
    show d_us normal swim:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with dissolve
    mt "Семён, Ульяна! Вы почти не опоздали, поэтому я почти не буду вас ругать."
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
    mt "Ещё накупаетесь так, что из ушей вода побежит, а в первый раз заходим в воду по моей команде и ровно на две минуты.{w} Кто не услышит команды на выход — тот завтра останется без купания!"
    show mt rage panama swim close with dspr
    mt "Повторяю: по моей команде спокойно заходим в воду, кто в воду побежит — тот без купания останется уже сегодня!"
    hide mt with Dissolve(1.5)
    show dct_ext_beach_day_with_pass_train:
        linear 1 alpha 0
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
    "Вообще-то на пляже было неплохо: лезть в воду Женю никто не заставлял и общество не навязывал. Вообще большинство делало вид, что Жени не замечает."
    show d_mz smile glasses pioneer far with dspr
    "Только Лена и Саша кивнули, но подходить не стали, хотя как раз против их общества Женя не возражала."
    show d_mz shy glasses pioneer far with dspr
    "И Сыроежкин ещё притягивал взгляд."

    scene dct_ext_beach_day_lifesaving_shield
    show d_el smile swim at cright
    with pushright
    "Не хотела на него смотреть, но каждый раз, как пересекались взгляды, что-то словно обмирало внутри."
    show 3500_sh smile swim at cleft:
        ycenter 0.833 alpha 0
        pause 2
        linear 1 alpha 1
    show d_el think2 swim as el2 at cright:
        alpha 0
        pause 3.0
        linear 0.2 alpha 1
    "И было так одновременно страшно и приятно, что Женя даже начинала злиться на обоих кибернетиков, когда Шурик отвлекал Сыроежкина и тот не бросал взглядов на Женю."

    scene dct_ext_beach_barhan
    show d_mz shyangry glasses pioneer far at right:
        ycenter 0.73
    with pushleft
    pause

    scene dct_ext_beach_barhan
    show mz normal glasses pioneer far at right:
        ycenter 0.73
    with dct_fade
    play sound_loop dct_ambience_beach fadein 1
    "Физруки отправили в воду средний отряд, и воздух заполнился криками и девчоночьим визгом."
    show mz bukal glasses pioneer far with dspr
    th "Что за люди? Зачем так кричать?"

    scene dct_cg_coin_volleyball with squares
    "Старший отряд, за вычетом Жени и кибернетиков, но зато с добавкой Максима и обоих физруков, затеял игру в волейбол."
    "Рядом с Женей шлёпнулся мячик, обдав её ноги песком."

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
    show d_ma grin2 swim with dissolve:
        xcenter 0.4 yalign 0.02
    d_ma "Уходишь?{w=0.5} А может, с нами поиграешь?"
    "Упустивший подачу и прибежавший за мячиком Максим ждал ответа и улыбался."
    show d_mz surprise pioneer with dspr
    "Это предложение было так неожиданно и так нахально, что Женя чуть было не согласилась, и только осознание того, что вот она будет играть, такая неуклюжая и некрасивая, а её будет разглядывать Сыроежкин, вынудило Женю не торопиться с ответом."
    show d_mz sceptic pioneer with dspr
    "А потом уже всплыло и подозрение, что и приглашают-то исключительно чтобы посмеяться над её неуклюжестью. Но всё равно отказалась Женя гораздо мягче, чем могла бы."
    show d_mz smile2 pioneer with dissolve_fast
    mz "Не хочу пачкать форму. Так что без меня."
    show d_ma smile swim with dspr
    "Тут Женя вспомнила про загадочные журналы, про то, что хотела допросить Максима с пристрастием — где он нашёл журналы, которые напечатают только через пять лет?{w} Но решила пока не пугать младенца."
    show d_mz sceptic pioneer with dissolve_fast
    mz "В библиотеку-то ещё зайдёшь?"
    show d_ma smile2 swim with dspr
    d_ma "Обязательно."
    show d_mz normal pioneer with dspr
    show d_ma normal swim with dspr
    hide d_mz with Dissolve(1.5)
    "Женя кивнула и, мысленно улыбаясь, пошла к себе в домик."
    hide d_ma with dissolve
    stop sound_loop fadeout 1.5
    stop ambience fadeout 1.5
    stop music fadeout 1
    show black:
        alpha 0
        pause 0.5
        linear 1 alpha 1
    "До обеда оставалось сорок минут, и открывать библиотеку смысла не было, а вот план допроса юного пионера разработать стоило."

    scene bg int_house_of_dv_day with fade
    play music music_list['went_fishing_caught_a_girl'] fadein 2
    "Письмо, забытое, лежало в кармане."

    scene dct_ext_beach_day_lifesaving_shield
    show d_sf sad swim:
        xcenter 0.57
    show d_us smile swim:
        xzoom -1.0 xcenter 0.43 ypos -0.05
    with blinds
    play sound_loop dct_ambience_beach fadein 1
    "Когда на пляже появились довольная Ульяна и, как обычно, замороченный своими думами Сенька, Алиса взяла протянутый Ульяной тетрадный листок в клеточку, положила его в нагрудный карман рубашки, накинутой на плечи, и помчалась сразу к своему отряду."

    scene dct_ext_beach_day_with_pass_train with dissolve
    th "Всё! А этих балбесов сами купайте, а то я с ними намучилась!"
    "У грибка, занятого отрядом, скинула не глядя рубашку и побежала в воду, откуда уже махала ладошкой Мику."

    scene dct_cg_coin_dv_on_beach with squares
    "На кромке воды остановилась и обвела взглядом пляж: Ольга с секундомером в руках и свистком в зубах готовится дать октябрятам отмашку и разрешить им залезть в воду."
    "Семён с Ульяной построили средних лицом к реке, Семён что-то говорит им, средние хохочут в ответ, потом Ульяна отбегает к воде, а Семён отходит к левому флангу шеренги и командует: «На старт! Внимание! Марш!» — отряд срывается с места, и пионеры с визгом и хохотом несутся к воде."
    "Даже Катька забыла, что считает себя взрослой, и тоже бежит в воду с визгом и хохотом."
    "Алиса на секунду ощутила острую зависть к малолетке — самой так же с хохотом пробежать хочется, а стеснительно, а даже вспомнить, каково это, не получается, потому что сохранённых воспоминаний у копии — кот наплакал."
    th "Ну и чёрт с ним!"
    extend " Зато я по-настоящему живу, а она ещё нет!"
    stop sound_loop fadeout 1

    scene dct_ext_water_islands_buoys_day with squares
    "Алиса опять повернулась к воде, погрозила кулаком Максиму, готовящемуся пустить ладошкой веер брызг в сторону Лены и, разбежавшись, покуда глубина позволяла бежать, в скольжении вошла в воду."
    "И красивым баттерфляем пошла к буйкам, уже ни о чём больше не думая и не видя Максима, проводившего её восхищённым взглядом."
    show int_dining_hall_people_day:
        alpha 0
        pause 1.5
        linear 1 alpha 1
    "Купание, пляжный волейбол, обед… Так часов до трёх письмо и пролежало в кармане, забытое и нетронутое."
    stop music fadeout 1 

    scene bg int_house_of_dv_day with blinds
    play ambience ambience_int_cabin_day fadein 1
    play sound sfx_bed_squeak1
    "И только после обеда, когда Алиса завалилась в домике на койку, сложенный вчетверо листок напомнил о себе."
    play sound sfx_paper_bag
    "Алиса потянула его из кармана, развернула и некоторое время просто разглядывала буквы собственного почерка."
    stop ambience fadeout 1

    scene bg int_house_of_dv_day
    show dct_coin_letter1 at truecenter
    with dissolve
    play music twisterium_eternal_love fadein 1
    pause 3
    $ set_mode_nvl()
    "Привет…{w=0.8} сестрёнка.{w} Раз уж Ульяны так между собой общаются и я к тебе во сне так же обратилась, то и буду обращаться так же. Насколько я себя (тебя) знаю, ты не будешь против.{w} Кстати, это точно был сон? Потому что нашим Мику, Ульянке и Славе снилось то же самое.{w} Но что-то меня не туда понесло, начинаю сначала."
    "\nПривет, сестрёнка!{w} Обе Ульяны и Сенька очень хорошо о тебе отзываются, вот я и решила написать.{w} Очень бы хотелось познакомиться лично, но Сенька бьёт себя пятками в грудь, морщит верхнюю губу и качает головой.{w} «Я, — говорит, — не уверен, что это безопасно для вас. Что одна из вас не исчезнет в течение получаса. Вы не настолько друг от друга отличаетесь, чтобы безопасно сосуществовать в одном узле. Имею, — мол, — опыт».{w} Приходится ему верить, а жаль.{w} А мне кажется, что мы с тобой не отражения одного и того же человека, а самостоятельные люди — просто, ну, как двойняшки. Или потомки того самого человека.{w} Ты, конечно, поопытнее меня будешь и вон как высоко прыгнула — в помощницы вожатой (шучу), но и я не хуже.{w} Рассказала о твоей должности Славе, а та только улыбнулась и сказала, что сочувствует тебе. Вот так, тогда я тоже тебе сочувствую."
    "\nНе знаю, как вы себя чувствовали, когда проснулись, а мы четверо — я, Ульянка, Мику и Славя — просто в какой-то эйфории сейчас.{w} Всё одновременно и знакомое, и новое, а главное — не знаю как у других, но у меня это чувство свободы, когда я понимаю, что могу сама построить свою жизнь, а не крутиться внутри двух недель цикла. У меня даже со Славей отношения чуть получше стали.{w} Да, Сенька рассказал мне про активную фазу, но это же не окончательный приговор — Сенька же вырвался, и Ульяна ваша, надеюсь, тоже."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "\nО наших делах не пишу — они, наверное, не очень отличаются от ваших.{w} Ульяна сказала, что на её место в отряде вы Максима выбираете, надо будет к нашему присмотреться. Только не селите его третьим в домик к кибернетикам — пропадёт парень."
    "\nЗавидую вам и сержусь на Сеньку, что он к вам от нас сбежал (про сержусь тоже шутка), потому что новый его двойник… Он пока так — ни рыба ни мясо.{w} Но хоть Сенька и сбежал к вам, но проснулся он именно у нас, я надеюсь, что в этом есть и моя заслуга, пусть я и не понимала, что делаю. Так что тоже можешь мне завидовать."
    "\nСестрёнка, я очень хочу рискнуть и тебя увидеть, и если ты не против — дай знать. Хоть через ваших Сеньку с Ульянкой дай знать, они в следующем цикле собрались опять к нам.\n\n\n{space=1200}{i}{size=+10}Алиса{/size}{/i}"
    "\nP.S. Приготовь свои детские воспоминания. Мы обязательно должны их сравнить!"
    window hide
    pause
    stop music fadeout 1

    scene int_clubs_male_day with dct_fade
    play ambience ambience_clubs_inside_day fadein 1
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
    "Шурик — тот весь погрузился в пайку и отключился от внешнего мира. Очень уж ему хотелось если не приступить к настройке, то хотя бы спаять электронную часть схемы."
    hide sh with dissolve
    show dct_fog:
        alpha 0
        linear 7 alpha 0.75
    "Поэтому он сидел спиной ко всем, время от времени бормотал что-то про себя, шипел, когда пальцы хватали раскалённые выводы радиодеталей и концы проводов, да канифольный дым из-под жала паяльника всё больше и больше наполнял комнату."
    "Когда в помещении кружка стало есть глаза, Электроник не выдержал. Открыл окно, распахнул дверь, выдернул из розетки паяльник и громко объявил:"
    show el serious pioneer behind dct_fog with dissolve
    el "Как ответственный за технику безопасности, объявляю пятнадцатиминутный перерыв на проветривание. Просьба всем выйти на улицу.{w} Шурик, тебя это тоже касается!"
    hide el with dissolve
    stop ambience fadeout 1
    play sound sfx_open_door_clubs

    scene bg ext_clubs_day with slideawayup:
        zoom 2.8 xcenter 0.5 ycenter 0.62
    play music music_list['everyday_theme'] fadein 1
    "Шурик с листом миллиметровки в руках тут же убежал на полюбившееся ему место за зданием клубов, а Сергей с Оксаной никуда не пошли и присели тут же на крылечке."
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
    d_oz "Ну, распорядок, Серёжа, это…"
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
    "Пятнадцать минут истекли, и пунктуальный Шурик появился на крыльце клубов, а Оксана и Сергей всё ещё увлечённо беседовали."

    scene dct_ext_clubs_sunset with dissolve2:
        zoom 2.8 xcenter 0.5 ycenter 0.62
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    "И так и продолжили разговор до самого вечера."
    show dct_ext_clubs_sunset:
        ease 1.5 zoom 1.0 ycenter 0.5
    show d_oz n pioneer:
        zoom .18 anchor (.5, 1.0) pos (.54, .72) alpha 0
        pause 1.8
        linear 0.7 alpha 1
    show 3500_el normal pioneer:
        zoom .18 anchor (.5, 1.0) pos (.46, .707) alpha 0
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
    "Электроник закончил монтировать приёмники и излучатели на каркас установки, Оксана оставила почти готовый корпус корабля на верстаке, дождалась Сергея и пошла с ним по главной аллее в сторону площади, продолжая что-то объяснять."

    scene dct_int_house_of_el_sunset with fade
    "После ужина Электроник у себя в домике завалился на кровать, закинул руки за голову и улыбнулся."
    show d_oz smile pioneer at center with dissolve_fast:
        zoom 2.5 ycenter 0.95 alpha 0.5
    th "«Серёжа, а давай я как будто на тихом часе?»."
    show d_oz:
        linear 0.5 alpha 0
    extend " Хорошо им, маленьким."
    extend " Даже если вожатая и обратит внимание, то скажет, что маленькая же, какой с неё спрос? Никакого."
    th "Ну а с другой стороны, когда ей ещё чем-то заниматься?"
    extend " Распорядок просто не предусматривает, что девочка из младшего отряда будет заниматься судомоделизмом."
    th "А у Оксаны хорошо получается."
    extend " Жаль, что она сейчас свой кораблик вырежет и уйдёт, славная девочка, с ней как-то веселее работается."
    th "Но вот получается, что Оксана нарушила правила, чтобы сделать что-то новое."
    extend " Никому же раньше она кораблики не вырезала? Наверное, нет."
    th "И мальчику тому никто раньше корабликов не дарил."
    th " То есть чтобы сделать что-то новое, нужно нарушить старые правила."
    th "Кстати, мы же должны были делать робота — вот и корпус для него уже готовый, и деталей куча, и в плане работы кружка у вожатой тоже робот записан."
    extend " А Шурик сказал Ольге Дмитриевне, что план — это не забор, чтобы вдоль него ходить."
    th "Интересно, а к отношениям между людьми это можно применить?"
    stop music fadeout 1

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show un smile3 pioneer close:
        xcenter 0.59 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dct_fade
    play ambience ambience_dining_hall_full fadein 1
    un "Как сходили?"

    scene dct_int_dining_hall_table_sunset_back_people
    show d_sf smile pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us normal dress:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    me "Замечательно."
    "Семён аккуратно переложил свой кусок рыбы на пустую тарелку."
    me "Девочки, кто хочет рыбу — может не стесняться."
    show d_sf normal pioneer with dspr
    "Лена кивнула Семёну, пододвинув тарелку к себе."
    us "Ленка, тебе большое и даже огромное спасибо от тамошней Мику."
    show d_us smile dress with dspr
    us "Она так и сказала: «А вашей Леночке передайте мою большую благодарность и даже огромное спасибо! Всё так, как я и представляла, когда писала, и даже лучше!»."

    scene dct_int_dining_hall_table_sunset_back:
        xzoom -1
    show un serious pioneer close:
        xcenter 0.59 ycenter 0.41
    show dct_int_dining_hall_table_sunset_front:
        xzoom -1
    with dissolve
    un "Передавайте."
    show d_un serious pioneer holds_out_hands close as un with dissolve_fast
    un "Передавайте, передавайте."

    scene dct_int_dining_hall_table_sunset_back_people
    show d_sf laugh pioneer:
        zoom 1.25 xcenter 0.42 ycenter 0.74
    show d_us laugh dress:
        zoom 1.25 xcenter 0.77 ycenter 0.94
    show dct_int_dining_hall_table_sunset_front
    with dissolve
    un "Ребята, я, конечно, девушка необщительная, но знаете, как я хочу попасть туда и посмотреть, что там делается."

    scene dct_int_dining_hall_people_sunset with fade
    "Ужин шёл своим чередом."
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
    "Электроник неожиданно оказался за одним столом с тремя октябрятами из младшего отряда и о чём-то с ними оживлённо беседовал."
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
    "Ещё одна драма: Максим за одним столом с Сашей и Мику, и от их стола тоже доносится смех и оживлённый разговор."
    show d_ka p2 angry2 pioneer:                     
        zoom 0.825 xcenter 0.955 ycenter 0.95 alpha 0
        pause 0.5
        linear 0.7 alpha 1
    show dv guilty pioneer far:
        xcenter 0.07 ycenter 0.73 alpha 0
        pause 1.2
        linear 0.7 alpha 1
    "Вот только недовольные взгляды на Максима кидают двое: Катя, что ожидаемо, и Алиса."
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
    "Нет, Максим тоже на Алису посматривает: вот они случайно пересеклись взглядами, покраснели и уткнулись в тарелки."

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
    un "А кое-кому и сильно больше."
    show mt normal pioneer close behind dct_int_dining_hall_table_sunset_front:
        xcenter 1.25 ycenter 0.23
        linear 0.6 xcenter 0.89
        pause 0.15
        linear 0.5 ycenter 0.5
    show un normal pioneer close with dissolve_fast
    "Подошла вожатая со стаканом чая в руках, присела четвёртой за столик.{w} Посмотрела на Семёна с Ульяной, хотела что-то сказать, но передумала."
    show mt smile pioneer close with dspr
    pause 0.2
    show mt smile pioneer close:
        linear 0.5 ycenter 0.23
        pause 0.15
        linear 0.6 xcenter 1.25
    play sound "<from 1.0>" + dct_sfx_chair
    extend " Только кивнула, улыбнулась и молча ушла."
    show un smile2 pioneer close with dspr
    un "Зря от рыбы отказался. Кажется, повара научились готовить без указаний бабы Глаши."
    stop ambience fadeout 1

    scene bg ext_square_sunset:
    show un normal pioneer at cright:
        ycenter 0.65
    with dct_fade
    play ambience ambience_camp_center_evening fadein 1
    play music music_list['farewell_to_the_past_full'] fadein 1
    "После ужина Лена устроилась на своей любимой лавочке, пыталась вчитаться, и ничего не получалось. Книжка не шла."
    "Вместо этого вспоминался разговор с Семёном и Ульяной за ужином и привет от чужой Мику."
    show un smile pioneer with dspr
    th "Спасибо, Мику, твою сказку я зачитаю до дыр."
    "Опять вспомнилась баба Глаша."
    show un sad pioneer with dissolve_fast
    $ sunset_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    th "Вот так умрёшь, а через три дня о тебе уже никто и не помнит."

    scene black with dissolve_fast
    $ night_time()
    $ persistent.sprite_time = "night"

    scene bg ext_square_night
    show un normal pioneer at cright:
        ycenter 0.65
    with dissolve_fast
    "Уже стемнело."
    show d_sf normal pioneer at cleft with MoveTransition(1.5, enter=_moveleft, enter_time_warp=_ease_time_warp)
    show d_sf normal pioneer:
        linear 0.4 ypos 0.12
    extend " Семён, совершающий вечерний обход лагеря, на минутку подсел рядом."
    show d_sf smile pioneer with dspr
    me "Лен, я всё думал — что ты будешь делать, когда в библиотеке кончатся книги? И вот, кажется, я дождался."
    show un smile pioneer with dspr
    un "Буду просить вас с Ульяной проводить меня в Шлюз и обратно. В тамошнюю библиотеку. Там, наверное, есть ещё что-то."
    show d_sf sad pioneer with dspr
    me "Знаешь, я не помню. На тот момент меня содержимое библиотеки интересовало слабо."
    show d_sf normal pioneer with dspr
    extend " Но можно ещё пройтись по жилым корпусам…"
    show un normal pioneer
    show d_sf serious pioneer
    with dspr
    me "Лен, если пойти сейчас — там Второй. Ты выдержишь, но я не уверен, что тебе понравится увиденное."
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
    "Семён глянул в глаза Лене, хотел что-то сказать, но только кивнул, дёрнулся, чтобы пожать предплечье, но не стал, а снова кивнул."
    show d_sf normal pioneer:
        linear 0.4 ypos 0.0
        pause 0.15
        easeout 2.5 xcenter 1.2
    "Пожелал спокойной ночи и, махнув рукой пробегавшей мимо Ульяне, чтобы подождала, ушёл к себе в спорткомплекс."
    show un serious pioneer with dissolve_fast
    th "Надо будет обязательно собраться: мне, физрукам, Алисе, может быть, моему Семёну."
    extend " Собраться и поговорить о прошлом цикле."
    th "Алиса что-то знает, но молчит, несколько раз порывалась поговорить, но сама же передумывала. Персуновы тоже странно смотрели на ожоги на моих руках."
    show un sad pioneer with dissolve_fast
    th "А я ничего почти не помню: провал в памяти и словно обрывки сна."
    th "Но они же держали свои руки на моих плечах, отдавая мне свою силу — это точно. И я помню это, и они помнят."
    show un surprise pioneer with dspr
    th "Сегодня Алиска на пляже положила свою ладонь мне на плечо, так мы обе вздрогнули!"
    stop music fadeout 3
    show un normal pioneer with dissolve_fast
    "На площади появился Максим с горном под мышкой."
    show un smile pioneer with dspr
    "Махнул рукой Лене, поставил горн на землю, повозился с металлической коробочкой, прикреплённой позавчера кибернетиками к одному из флагштоков."
    $ renpy.sound.set_volume(1.5, delay=0)
    $ renpy.sound.set_volume(0.5, delay=0, channel='sound2')
    play sound2 sfx_radio_squelch_2 
    play sound [ "<silence 1.7>", dct_sfx_horn_rebound_through_loudspeaker ]
    show un smile pioneer with dspr
    "В громкоговорителях, развешанных на столбах, что-то зашипело, а потом зазвучал сигнал отбоя."
    th "Пора и мне умываться и спать."
    show un normal pioneer with dspr
    "Лена закрыла книгу, глянула на название и вздохнула."
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Завтра верну в библиотеку, незачем себя мучить."
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
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound3')
    
    
    
################
#Глава 6. d7-d5#
################

label dct_d7_d5_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- d7-d5"
    $ night_time()
    $ persistent.sprite_time = "night"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop ambience
    stop sound_loop
    play music "<from 19.0 loop 0.0>" + music_list["a_promise_from_distant_days"]
    show headline_text2 u"Глава VI. d7-d5" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_coaching_room2_night with dissolve
    play ambience ambience_int_cabin_night fadein 1
    $ renpy.music.set_volume(0.25, delay=2)
    "Семён ворочался, всё никак не мог уснуть, пока Ульяне не надоело и та не шикнула на Семёна."
    us "Сёмк, вообще ты должен сейчас сопеть носом в угол, а ты дыру в матрасе протираешь. С тобой всё в порядке?"
    me "Не спится, Рыжик. Пойду подышу."
    show dct_insomnia with squares
    us "А который час, Сём?"
    me "Час быка.{w=.4} Два часа ночи."
    stop ambience fadeout 1

    scene bg ext_house_of_dv_night with dct_fade
    $ renpy.music.set_volume(1.0, delay=1)
    "Ночь была в самой глухой своей фазе, спали даже самые отъявленные нарушители режима."
    "Алисе опять снился сон про шары. И она там, во сне, почти решилась шагнуть на ближайший."

    scene dct_ext_house_of_un_night with pushdown
    "Лене снилась женщина, тянущая к ней руки. Глядящая ей в глаза — кто первый сдастся и отведёт взгляд."
    "И близкие, держащие свои руки у Лены на плечах."
    
    scene dct_ext_house_of_sl_night with pushdown
    "Мику снилась музыка и почему-то незнакомый автобус, в котором она и какой-то мальчик едут в пионерский лагерь."
    "На улице зима, а они едут в пионерский лагерь."
    "Мальчик дремлет у неё на плече, а Мику хочет повернуть голову, чтобы посмотреть на него, и понимает, что этого нельзя делать, что тогда случится что-то непоправимое."

    scene dct_ext_house_of_el_night with pushdown
    "Шурику опять снились сны Александра — опять он видел во сне живых Яну и Яну."
    stop music fadeout 1

    scene dct_ext_beach_night_view_from_gym with dct_fade
    play ambience ambience_camp_center_night fadein 1
    "Ближайший дежурный фонарь освещал хозяйственные ворота, да вход в столовую был ярко освещён своими фонарями."
    "Луна, выросшая в три четверти, висела где-то за лесом, но света звёзд хватало для глаз."
    "Семён и Ульяна, укрывшись одной курткой на двоих, сидели на крыльце спортзала и смотрели поверх главной аллеи на пустой пляж и слабо мерцающую реку за ним."
    "Кто-то мелкий шуршал в траве, неясные тени летучих мышей проносились над головами. Свежий воздух прогнал последние остатки сна."
    us "Сём, помнишь, в наш первый цикл, когда мы ходили за Алисой в бомбоубежище. Ты ещё спросил о звёздах, что-то вроде: «Интересно, здесь те же звёзды, что и дома?»."
    me "Помню."
    us "Вот и я себе сейчас этот вопрос задаю."
    us "Знаешь, я думаю, что звёзды для всех общие. И если мы отсюда сможем улететь к ним, то, вернувшись назад, окажемся где угодно. Здесь, в соседнем узле, в…"
    us "В материнском мире.{w=.5} Я название придумала, а то мы всё «снаружи» да «снаружи»."
    me "В мирах, Рыжик."
    me "Я так подозреваю, что материнский мир не один."
    me "Тот Пионер, который приходил ко мне. И Семён, который сюда приедет через два дня, которого всё ждёт Лена. Они ведь из разных миров."
    me "И сама Лена — она тоже у меня под подозрением, что она из нашего мира."
    me "А раз Лена, то и Алиса, раз у них общие воспоминания из детства."
    me "Я не могу ничего доказать, но подозреваю, что они, их оригиналы, пришли сюда из других миров."
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "Семён замолчал, не желая продолжать, вспомнив ещё мельком оброненные бабулей слова о том, что, когда удалось пробиться сюда, оказалось, что здесь уже бывали люди."
    stop ambience fadeout 1

    scene bg int_dining_hall_day
    $ day_time()
    $ persistent.sprite_time = "day"
    show d_bg normal suit at cright:
        yalign .1
    show dct_dream_veil at shiver
    with blinds
    play ambience ambience_dining_hall_empty fadein 1
    d_gd "Попадёшь в двести первый узел — увидишь там развалины домов."
    d_gd "Десяток старых срубов, примерно там, где домик твоих рыжих подружек."
    $ day_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    d_gd "Кто и когда там жил — мы не знаем. На всякий случай просто не стали тот узел заселять, так он и стоит пустой."
    stop ambience fadeout 1

    scene dct_ext_beach_night_view_from_gym
    show d_jn:
        zoom .15 xcenter .74 ycenter .545
    show dct_ext_beach_night_view_from_gym_bush
    with blinds
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 1
    play sound sfx_bush_leaves
    "Громко хрустнула ветка за кустами на противоположной стороне главной аллеи."
    "Через минуту в просвете мелькнуло что-то металлическое."
    me "А вот и Яна."
    show d_jn:
        linear .6 xcenter .775 ycenter .51 rotate 10
    pause .6
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "Семён махнул рукой, подзывая кошкоробота."
    stop ambience fadeout 1

    scene dct_coin_bus-stop:
        zoom 0.75
    show dct_dream_veil at shiver
    with dct_fade
    $ day_time()
    $ persistent.sprite_time = "day"
    play music twinkling fadein 1
    show d_jn_old angry behind dct_dream_veil:
        zoom 0.75 xcenter 0.39
    show d_jn_old normal as d_jn_old_norm behind dct_dream_veil:
        zoom 0.75 xcenter 0.39 alpha 1
        pause 1.6
        linear 0.2 alpha 0
    show d_jn_young normal behind dct_dream_veil:
        zoom 0.75 xcenter 0.31
    with dissolve
    "Шурику опять снились обе Яны, стоящие на остановке.{w=.7} И опять старшая Яна ругала его во сне."
    d_jn_old "Ты снова пришёл сюда. Неужели ты не понимаешь, что только разрушаешь себя самого? Что ты просто отдаёшь кусочек себя каждый раз, когда приходишь? Что мы даже не фантомы? Ты же знаешь, чем всё кончается."
    th "А может, я и хочу, чтобы всё так и кончилось."
    "Всё уже много раз повторялось, в том числе и этот сон, и человек, чей сон видит Шурик, снова молча смотрит на Яну."
    "Кирпичная остановка, бетонный забор с одной стороны улицы и глинобитная стена, которую офицеры с полигона называют «дувал» — с другой, пыльные пирамидальные тополя, растущие в два ряда между проезжей частью и забором, железные ворота в заборе, сейчас приоткрытые — это всё воспринимается попутно."
    "Главное сейчас — не отрываясь смотреть по очереди на одну и вторую Яну."
    show d_jn_old cry with dspr
    d_jn_old "А я не хочу, слышишь! Я слишком тебя любила, чтобы позволить тебе исчезнуть!"
    show d_jn_young normal with dissolve_fast:
        zoom 1 xcenter 0.33 ycenter 0.833
    "А Яна-младшая — та просто прижимается к Шурику и обещает, что позвонит сразу же, как только они окажутся у бабушки."
    show d_jn_old normal
    show d_jn_young laugh
    with dspr
    d_jn_young "Я телефон в трёх местах записала и ещё выучила, вот!"
    show d_jn_young dontlike with dissolve_fast:
        zoom 0.75 xcenter 0.31 yalign 0.0
    "Нарастающий шум мотора, который мешал разговору в течение всего сна, становится уже совершенно невыносимым, и вот из-за угла, осторожно высунув сперва свою щучью морду, выворачивает БТР, и следом за ним совершенно бесшумный в сравнении с БТР Икарус."
    show dct_dream_sh_third_BTR_bus behind d_jn_old with dissolve:
        zoom 0.75
    "С брони спрыгивает незнакомый майор, отдаёт честь:"
    show d_jn_young normal with dspr
    show dct_dream_sh_third_major behind d_jn_young at right with dissolve:
        zoom 0.68 yalign 1.0
    d_maj "Всё готово?{w=0.5} Хорошо."
    "Майор поворачивается к женщинам."
    d_maj "Садитесь, пожалуйста, в автобус."
    hide d_jn_old
    hide d_jn_young
    with dissolve
    show dct_dream_sh_third_major at cright with dissolve_fast:
        zoom 1.0 yalign 0.0
    d_maj "Экстремисты захватили и разграбили полигон и движутся на город. Получен приказ: эвакуировать весь гражданский персонал."
    d_maj "Автобус не успеет обернуться, поэтому через час за вами подойдёт Урал, будьте дома."
    d_maj "Вот, распишитесь здесь."
    "Шурик расписывается в разграфлённом листе: «С приказом об эвакуации ознакомлен. Дата. Подпись. Фамилия»."
    hide dct_dream_sh_third_major with dissolve
    "Майор ещё раз отдаёт честь, забирается на броню, БТР выпускает в небо облако чёрного дыма, взрёвывает мотором, и маленький конвой уезжает."
    hide dct_dream_sh_third_BTR_bus with dissolve
    show black:
        alpha 0
        pause 2
        linear 2 alpha 1
    stop music fadeout 4.5
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Яна-младшая машет рукой из окна автобуса, Шурик, преодолевая чудовищную слабость, пытается поднять руку, чтобы помахать в ответ, и от этого усилия просыпается."

    scene dct_int_house_of_el_night with dct_fade
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night fadein 1
    "Проснувшись, некоторое время Шурик просто лежал; кажется, что слабость, не давшая ему помахать рукой во сне, проснулась вместе с ним."
    "На соседней кровати сопел Сыроежкин."
    th "Вот кому кошмары, наверное, никогда не снятся."
    "Луна наконец сумела подняться выше деревьев и светила прямо в окно, так что можно было разобрать даже надпись на спортивной сумке Сыроежкина, закинутой тем на шкаф."
    th "Что же происходит? Что пытается донести до меня подсознание?"
    th "Почему от имени «Яна» у меня начинает болеть в груди?"
    th "Нет, не зря мы отложили робота и занялись человеческим мозгом."
    $ night_time()
    $ persistent.sprite_time = "night"
    th "Завтра настраиваем схему и излучатели, послезавтра проводим эксперимент, и в воскресенье обрабатываем результаты."
    stop ambience fadeout 1

    scene bg ext_house_of_sl_day with dct_fade
    $ day_time()
    $ persistent.sprite_time = "day"
    play music buddy fadein 1
    "У Мику со вчерашнего вечера было прекрасное настроение, и даже серьёзный сон, приснившийся под утро, этого настроения не нарушил."

    scene dct_mi_piano1 with squares
    "В кои-то веки у неё попросили помощи, пусть даже и нужно было всего лишь играть на фортепиано для Саши и Максима."
    "А параллельно можно было разговаривать и общаться, и никто от неё не отмахивался."

    scene dct_int_house_of_mi_day with squares
    "Вот и сегодня утром можно было встать, открыть форточку, не обращая внимания на бурчащую соседку, пожелать той доброго, наидобрейшего утра и побежать к умывальникам."
    stop music fadeout 2
    play ambience ambience_int_cabin_day fadein 1
    show mz normal glasses pioneer far at cleft with dissolve
    mz "Мику, ты должна знать. Что это значит?"
    show mi upset pioneer close at right with dissolve
    th "Надо же, она имя моё запомнила. Ну-ка, посмотрим."
    play sound sfx_wood_floor_squeak
    show mi normal pioneer far with dissolve:
        xanchor .0 xpos .45
    pause .4
    show d_mz sceptic glasses pioneer far as mz
    show mi shocked pioneer far
    with dissolve_fast
    "И посмотреть, и удивиться, как Женя старательно выводит незнакомые ей закорючки."
    show mz normal glasses pioneer far
    show mi smile pioneer far
    with dissolve_fast
    mi "Женечка, так это же очень просто. Здесь написано «Первый звук будущего»."
    show mi normal pioneer far with dissolve_fast
    mi "А по-японски это будет «хатсуне мику», а ещё это моё имя — Хатсуне Мику."
    show d_mz amazed glasses pioneer far as mz
    show mi serious pioneer far
    with dspr
    mi "А где ты это увидела? Нет, я понимаю, если бы ты это у меня в документах подглядела, но все мои японские документы у мамы с папой, а здесь — только советские, потому что папа сказал, что если я еду в советский пионерский лагерь, то у меня и должны быть…"
    show d_mz hope glasses pioneer far as mz
    show mi upset pioneer far
    with dspr
    mi "Женечка?"
    show mz normal glasses pioneer far
    show mi normal pioneer far
    with dspr
    "Женя, видимо, поколебавшись и что-то решив для себя, достала из тумбочки серую канцелярскую папку-скоросшиватель и протянула её Мику."
    show dct_mz_1_binder_far at cleft with dissolve
    mz "Вот, почитай. Мне это дала Лена, а той принёс наш физрук: говорит, что это сочинила одна его знакомая."
    hide dct_mz_1_binder_far
    show dct_mi_3_binder_far:
        xanchor .0 xpos .45
    with dissolve
    show d_mz sceptic glasses pioneer far as mz with dspr
    mz "И мне интересно твоё мнение обо всём этом."
    show mi serious pioneer far with dspr
    hide mz with dissolve
    "Женя взяла полотенце и вышла, бросив в дверях:"
    mz "Я в библиотеке."
    play sound sfx_close_door_1
    hide dct_mi_3_binder_far
    show mi serious pioneer close at center
    with dissolve
    play sound sfx_open_journal
    "Мику открыла папку на середине, прочитала полстранички текста."
    "Какая-то пьеса — судя по увиденному, довольно интересная."
    show mi normal pioneer close with dspr
    th "Позже почитаю. От меня же не требуют, чтобы я дала ответ к завтраку?"
    hide mi with dissolve
    stop ambience fadeout 1

    scene bg ext_houses_day
    show mz bukal glasses pioneer close at cright
    with dct_fade                 
    play music music_list['my_daily_life'] fadein 1
    "У Жени же всё вертелась в голове характеристика Жанны из пьесы: «Жанна, заведующая библиотекой. Любит книги, а людей не вполне понимает и потому опасается»."
    play sound sfx_open_water_sink

    scene bg ext_washstand2_day with dissolve
    stop sound fadeout 1
    play sound_loop sfx_water_sink_stream fadein 0.2
    "Когда начала читать — не обратила внимания, а потом, когда начали всё больше и больше вылазить параллели с «Совёнком» и его обитателями, то вспомнила, и не то чтобы обиделась, но что-то ущипнуло за сердце."
    play sound sfx_close_water_sink
    stop sound_loop

    scene bg ext_houses_day
    show mz normal glasses pioneer
    with dissolve
    "Женя применила к себе эту характеристику и вообще всё, что касалось Жанны, и признала:"
    show d_mz sad glasses pioneer as mz with dspr
    th "Да, это я — такая и есть."

    scene bg ext_square_day with blinds
    "А раннее утро постепенно переходило в день."
    show mt normal panama pioneer:
        xcenter 0.26
    show d_sf smile pioneer:
        xcenter 0.52
    show d_us smile sport:
        xcenter 0.74 ypos -0.05
    with dissolve
    "Ещё одна линейка, напоминание о том, что сегодня шестой день смены, о том, что завтра по Плану мероприятий будет спортивный праздник, и комментарий Семёна: «Никакой обязаловки, но призы будут»."

    scene bg int_dining_hall_people_day with dissolve
    "Завтрак с привычными кашей, какао, маслом и яблочным джемом в аэрофлотовской упаковке."

    scene bg ext_library_day with dissolve
    "И здравствуй, библиотека."
    play sound sfx_door_squeak_light

    scene bg int_library_day with slidedown
    pause 0.5

    scene dct_int_mirror_in_library
    show mz bukal glasses pioneer at center:
        xzoom -1.0
    with squares
    th "Опять эта прядь выбилась."
    show d_mz sceptic glasses pioneer as mz with dspr
    th "Внешность — ладно, внешность неизвестный мне автор даже сильно приукрасил, но вот характер — тут всё правда."

    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
    play sound sfx_medpunkt_door_open    
    show d_sf smile sport as d_sf2 behind dct_int_library_standing_desk_front with dissolve:
        zoom 0.95 xcenter 0.35 ypos -0.04
    "Зашёл Семён за тренерскими методичками."
    stop music fadeout 2
    play ambience ambience_library_day fadein 2
    show d_sf sad sport as d_sf2 with dspr
    show d_sf serious sport behind dct_int_library_standing_desk_front:
        zoom 0.95 xcenter 0.35 ypos -0.04 alpha 0
        pause 1.3
        linear 0.2 alpha 1
    "Расписался в формуляре, поднял глаза и внимательно посмотрел на Женю."
    me "Женя, что-то случилось?"
    hide d_sf2
    mz "Почему вы так решили?"
    show d_sf normal sport with dspr
    me "Во-первых, я же просил мне не выкать, а во-вторых, раньше ты вела себя иначе."
    show d_sf smile sport with dspr
    me "Раньше ты бы рычала на меня, а сейчас только очками поблёскиваешь из своего угла."
    th "Конечно, иначе. Прочитала этот чёртов текст, и оказалось, что я боюсь вас, людей."
    th "Спросить, откуда он взялся, текст этот, будь он неладен?"
    extend " Куча вопросов про него."
    show d_sf normal sport with dspr
    "Не было в программах, заложенных Системой в Женю, правил поведения в подобных ситуациях, не было их и в программах, заложенных в неё создателями-людьми."
    "Никто и никогда не проявлял к ней искреннего участия и не должен был проявлять."
    "И сейчас Женя мучительно пыталась думать своей головой. Было трудно, мысли разбегались, и даже пойманную мысль не удавалось озвучить."
    "Наконец что-то сформировалось в голове. Это было не главное, о чём хотела сказать Женя. Но это было хоть что-то."
    show d_sf serious sport with dspr
    mz "Семён, я у Лены вчера брала почитать одну распечатку."
    mz "Скажите…{w=.5} Скажи, кто её настоящий автор?"
    show d_sf smile sport with dspr
    me "Понравилось?"
    show d_sf normal sport with dspr
    me "Её действительно написала Мику Хатсуне.{w} Правда, это не та Мику, которую ты знаешь."
    me "Ну а то, что персонажи такие узнаваемые…"
    show d_sf serious sport with dspr
    me "Она вас не знает, и я ей о вас не рассказывал — в этом я уверен."
    "Семён пристально смотрел на Женю, как будто ждал от неё чего-то."
    "Смотрел серьёзно, вовсе без улыбки, а чуть сжав губы, но Жене так было даже легче."
    "Серьёзный разговор двух серьёзных людей."
    "И никто не посмеётся над ней, и никто не отмахнётся от неё. Просто обмен информацией."
    mz "Скажи, а я действительно такая, как эта Жанна? Отталкиваю от себя?"
    show d_sf normal sport with dspr
    me "Лучше бы ты Лене этот вопрос задала. Она лучше меня в людях разбирается и ответила бы лучше меня — правда, если бы захотела."
    me "Но раз уж спросила меня — то да, отталкиваешь."
    show d_sf serious sport with dspr
    me "Когда кто-то, за редчайшим исключением, приходит в библиотеку, у тебя такой вид, будто ты хочешь немедленно выпроводить посетителя, отвлёкшего тебя от важного дела."
    me "Когда к тебе обращаются, ты всем своим видом показываешь, что снисходишь до человечка.{w} Даже шутки твои очень часто выглядят пропитанными ядом."
    show d_sf normal sport with dspr
    me "А люди ленивы и не хотят понять, что под этим хитиновым панцирем скрывается живой человек."
    me "Очень умный, образованный, смелый, чувствующий и, когда забывает надеть стервозную маску, очень симпатичный."
    show d_sf normal sport with dissolve_fast:
        xzoom -0.95
    show d_sf normal sport:
        ease 1.2 xcenter 0.2
    pause 1
    $ renpy.music.set_volume(0.1)
    play music music_list["kostry"] fadein 1.5
    "Семён приоткрыл входную дверь, впустив в библиотеку запахи цветов и звуки музыки, слабо доносящиеся с концертной площадки."
    show d_sf sad sport with dspr
    me "Бедолагу Сыроежкина-то ты точно не отталкиваешь, только я не знаю, алгоритмы это или свобода воли у вас обоих."
    stop music fadeout 1.5
    hide d_sf with dissolve
    play sound sfx_close_door_1
    pause 0.5

    scene dct_int_mirror_in_library
    show d_mz sceptic glasses pioneer at center:
        xzoom -1.0
    with squares
    mz "Ну что, Евгения, получили вы по сусалам?"
    mz "Люди от вас, Евгения, разбегаются, и правильно делают."
    show d_mz smile2 glasses pioneer with dissolve_fast
    mz "И что интересно, Евгения, я даже не уверена, что стоит что-то менять."
    mz "Как там у классика: «Полюбите нас чёрненькими!». Так честнее будет, чем я начну фальшиво всем улыбаться."
    stop ambience fadeout 1

    scene dct_ext_stage_close_day
    show 3500_dv dontlike pioneer2 guitar playing:
        zoom .37 xcenter .6 ycenter .4
    with dct_fade
    $ renpy.music.set_volume(1.0)
    play music "<from 6.5 loop 0.0>" + music_list["blow_with_the_fires"] fadein 1
    "Концертную площадку оккупировала Алиса.{w} Мрачная и задумчивая."
    "И музыка у неё выходила такая же — мрачная и задумчивая."
    "Усилитель, выкрученный на половинную мощность, электрогитара…{w} Можно, практически свесившись с края сцены, упиваться своим плохим настроением, машинально перебирая струны, и пытаться размышлять под случайные аккорды."
    show 3500_dv sadness pioneer2 guitar playing with dspr
    "Вчерашнее письмо от Алисы-двойника не шло из памяти: «Я хочу рискнуть и увидеться… Мы должны сравнить наши детские воспоминания»."
    show 3500_dv dontlike pioneer2 guitar playing with dspr
    th "Сравнить и дополнить!"
    show 3500_dv normal pioneer2 guitar playing with dspr
    th "Интересно, если собрать все детские воспоминания всех Алис, удастся ли восстановить всё моё детство?"
    th "А если собрать всех Алис вместе — может, мы просто сольёмся в одну Алису-настоящую?"
    extend " Как злой волшебник из кино про Аладдина?"
    show 3500_dv sadness pioneer2 guitar playing with dspr
    th "Нет, чушь. Сенька с Ульяной, конечно, лучше меня в этом разбираются, но я и без них понимаю, что это так не работает."
    $ renpy.music.set_volume(0.25, delay=1)

    scene dct_ext_stage_big_day
    show 3500_dv dontlike pioneer2 guitar playing:
        zoom .15 anchor (0.5, 1.0) pos (0.5, 0.75)
    with dissolve
    "На звуки музыки, а может и в поисках Алисы, на площадку забежала пионерка."
    show d_sv smile:
        zoom 0.97 xcenter 1.2 yalign 0.21
        easein 1.5 xcenter 0.62 
    extend " Или из младшего, или из среднего отряда, неважно."
    show d_sv shock with dspr
    pause 0.2
    show d_sv upset with dspr
    hide d_sv with easeoutleft
    "Увидала выражение её лица, что-то испуганно пискнула и исчезла."
    th "Вот и умничка."
    extend " Этот лагерь ещё часок обойдётся без меня."
    $ renpy.music.set_volume(1.0, delay=4)
    show 3500_dv dontlike pioneer2 guitar playing:
        pause 0.5
        linear 1 alpha 0
    show dct_ext_stage_edge_day:
        alpha 0
        pause 2
        linear 1 alpha 1
    show d18_alisa_guitar two:
        xpos -0.12 alpha 0
        pause 3.5
        linear 1 alpha 1
    "Край сцены начал резать стопы, Алиса перебралась ближе к углу и уселась возле стены купола."
    th "А что будет с нами обеими, окажись мы в одном узле?"
    th "Как там в книжке, что я у Жени брала?"
    th "Про экипаж космической станции, к которым приходили существа, взятые инопланетным разумом из их памяти."
    extend " Выглядящие как люди и считающие себя людьми, но не люди."
    extend " И исчезающие со вспышкой света при определённых условиях."
    th "Вот так исчезнешь, оставив после себя вспышку света — и всё, и привет, сестрёнка."
    th "И посоветоваться ведь не с кем.{w} Сенька с Ульяной со слов бабули говорили что-то о том, что пионеры-двойники не могут находиться одновременно в одном узле, о преимуществах «своего» узла по принципу «дома и стены помогают», об уровне развития личности субъекта, но всё это была голая теория."
    th "Это вот та Алиса, из старого Сенькиного лагеря, менее развита, чем я?"
    extend " Вон она какое письмо написала, я вот не догадалась."
    th "И вообще, я же вроде как собралась с концертами по лагерям проехаться."
    extend " Это что же — приезжая в каждый новый лагерь, я буду аннигилировать тамошнюю Алису?"
    extend " Не согласная я."
    th "А тут ещё за горнистом присмотреть надо."
    extend " Начал-то он хорошо, интересно, что в нём к следующему циклу изменится."
    show d18_alisa_guitar one with dissolve_fast
    th "В общем, так. В следующем цикле я точно здесь остаюсь, но схожу вместе с Ульяной в первый Сенькин лагерь."
    extend " Нужно с тамошней Алисой повидаться!"
    th "На остальных плевать, но с этой нужно."
    extend " Тем более Сенька нас связывает."
    th "И интересно, чего этой мелочи от меня надо было?"
    "И успокоившаяся Алиса заиграла уже не размышляя, просто ради самой музыки."
    stop music fadeout 1

    scene bg ext_clubs_day with dct_fade
    play sound_loop ambience_camp_center_day fadein 1
    el "Чуть левее датчик, ещё левее, ещё…{w} Стоп{w=0.3}, сейчас чуть-чуть правее.{w} Так, хорошо."
    el "Шурик, сейчас чуть выше.{w} Стой{w=0.3}, опусти назад, ещё опусти{w=0.3}, нет, верни как было.{w} Всё, зажимай, поймали."
    stop sound_loop fadeout 1

    scene bg int_clubs_male_day
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    play ambience ambience_int_cabin_day fadein 1
    play sound [ "<silence 1.0>", sfx_knock_door2 ]
    "Кибернетики стояли и благоговейно смотрели на зелёное колечко на экране осциллографа, когда в двери постучали."
    sa "Ребята, можно?"
    show el smile pioneer with dspr
    el "Заходи, Саша."
    play sound sfx_open_door_clubs
    show sl normal pioneer with dissolve
    el "Глянь на красоту."
    "Электроник махнул рукой в сторону осциллографа."
    show sh serious pioneer
    show sl surprise pioneer
    with dissolve_fast
    sa "А что это означает?"
    el "Это означает, Сашенька, что мы настроили прибор и завтра засунем в него свои свежие и выспавшиеся головы."
    show sl smile pioneer
    show el laugh pioneer
    with dissolve_fast
    el "Попытаемся переписать те объёмы информации, которая в них есть, и попытаемся её расшифровать. Всё, что есть в нашем подсознании, всё, что есть в нашей памяти."
    "Увлёкшийся Электроник заговорил, как герой его любимой фантастики шестидесятых годов."
    show el serious pioneer with dspr
    el "Может быть, мы сумеем понять принципы работы человеческого мозга, может быть, мы сумеем применить эти знания при проектировании кибермозга для будущих роботов!"
    el "Разве это не прекрасно?"
    show sl smile2 pioneer with dissolve_fast
    sa "Наверное, ты прав."
    show el smile pioneer with dissolve_fast
    sa "Я верю, что всё у вас, мальчики, получится. Но я к вам за помощью, раз вы освободились."
    sa "Серёжа, в половине библиотеки свет только что погас — посмотри, пожалуйста."
    show sh serious pioneer
    show d_el shy3 pioneer as el
    with dissolve_fast
    el "Шурик, а может, ты сходишь? А я пока тут всё поотключаю и порядок до обеда наведу."
    show sh normal_smile pioneer with dissolve_fast
    sh "Сергей, ну что за метания?"
    show sh laugh pioneer
    show d_el shy2 pioneer as el
    with dissolve_fast
    sh "Договорились же — по твоей просьбе, между прочим — что если есть какая-нибудь работа на дальней стороне лагеря, то ей занят ты, а на ближней — я."
    show d_el shy3 pioneer as el
    show sh smile pioneer
    show sl happy pioneer
    with dspr
    sh "Иди, Сергей. На обеде увидимся. А завтра уже займёмся экспериментом."
    hide sl with dissolve
    hide sh with dissolve
    show d_el shy2 pioneer as el with dspr:
        pause 2
        linear 1 alpha 0
    "Безотказному Сыроежкину осталось только собрать необходимый инструмент в старый, специально для таких случаев предназначенный школьный портфель и выйти на крыльцо."
    stop ambience fadeout 1

    scene bg ext_clubs_day
    show 3500_sl serious pioneer:
        zoom .18 anchor (.5, 1.0) pos (.46, .707)
    with slideawayup
    play ambience ambience_camp_center_day fadein 1
    play music music_list['two_glasses_of_melancholy'] fadein 1
    show 3500_el normal pioneer briefcase with dissolve:
        zoom .18 anchor (.5, 1.0) pos (.54, .707)
    el "Меня ждёшь?"
    show 3500_sl scared pioneer with dissolve_fast
    show 3500_sl surprise pioneer with dissolve_fast
    "Саша, стоящая лицом в сторону приоткрытых ворот лагеря и что-то там высматривающая, вздрогнула."
    sa "Да, Серёжа, пошли."

    scene bg ext_houses_day
    show 3500_el normal pioneer briefcase:
        xcenter .35 ycenter.833
    show sl normal pioneer at cright
    with wipeleft
    "К удивлению Сергея, Саша на перекрёстке не свернула налево, в сторону музыкального кружка и короткой дороги к своему домику. А наоборот, догнав его и подстроившись под его шаг, пошла рядом."
    show 3500_el surprise pioneer briefcase with dissolve_fast
    el "Ты на пляж? Я думал, ты к себе свернёшь."
    show sl serious pioneer with dspr
    sa "Сергей, я в библиотеку."
    sa "Что там у вас с Женей происходит — я не знаю, и это ваше дело. Но она сначала не хотела звать тебя, а после — категорически не хотела оставаться с тобой один на один. Как и ты пять минут назад."
    show sl serious pioneer
    show 3500_el sad pioneer briefcase
    with dspr
    el "Как и я."
    stop ambience fadeout 1

    scene bg ext_square_day
    show 3500_el shy2 pioneer briefcase:
        xcenter .35 ycenter.833
    show sl normal pioneer at cright
    with pushleft
    "На аллеях и площади было малолюдно. В связи с открытием купального сезона и жаркой погодой жизнь лагеря переместилась на пляж или в тень от деревьев, да футболисты занимались на стадионе по своему графику. Поэтому вспыхнувшие уши Сергея видела только Саша."
    show sl smile pioneer with dspr
    el "Хороший ты человек, Сашенька. Вот ответь, зачем мелькать перед глазами у человека, если он не хочет меня видеть?"
    show 3500_el shy3 pioneer briefcase with dspr
    "Сыроежкин вздохнул."
    show sl normal pioneer with dspr
    el "Оксана не знает, но ей только девять лет. Может, ты мне скажешь?"
    show 3500_el normal pioneer briefcase with dspr
    el "Женя, наверное, думает, что я буду объясняться с ней. Потому и не хочет со мной наедине оказываться."
    show 3500_el scared pioneer briefcase with dissolve_fast
    el "А зачем мне объясняться, когда всё уже сказано? Только нервы мотать."

    scene dct_ext_square_profile_view_day
    show sl sad pioneer zorder 2
    show 3500_el sad pioneer briefcase zorder 3:
        xcenter .26 ycenter.833
    show sl sad pioneer as sl2 zorder 4:        # Дополнительно вырезаем юбку Слави и помещаем перед чемоданом
        corner1 (191, 700) corner2 (900, 1080) xcenter 0.55 yalign 1.0
    show un serious pioneer far at fright
    with pushleft
    pause 0.5
    show 3500_el smile2 pioneer briefcase
    show sl smile2 pioneer 
    hide sl2
    with dissolve_fast
    show un grin pioneer far with dspr
    "Саша с Сергеем прошли по площади, обогнули Генду и синхронно помахали рукой Лене, сидящей на своём привычном месте и делающей какие-то заметки в блокноте."
    show un normal pioneer far
    show sl smile pioneer
    with dissolve_fast
    sa "Серёжа, а может, всё ещё не было сказано окончательно? Может, Женя сама не уверена ни в чём?"
    show un serious pioneer far
    show 3500_el normal pioneer briefcase
    with dissolve_fast
    "Сыроежкин остановился, оглядел площадь, перехватив внимательный взгляд Лены."
    show un serious pioneer far:
        linear 1.5 alpha 0
    "Впрочем, Лена была далеко и услышать его не могла."
    show 3500_el angry pioneer briefcase
    show sl smile pioneer zorder 4
    with dissolve_fast
    el "Сашенька. Я простой как отвёртка и привык иметь дело с техникой, которая либо работает, либо нет. И всегда можно найти причину, почему она не работает. И «нет» всегда означает только «нет»."
    show sl sad pioneer as sl2 zorder 4:
        corner1 (191, 700) corner2 (900, 1080) xcenter 0.55 yalign 1.0
    show sl sad pioneer zorder 2
    with dissolve_fast
    el "А вашего женского языка, где «да» означает «да», а «нет» означает «может быть», а «может быть» — это значит «нет», я просто не понимаю."
    el "Я получил информацию о том, что я Жене не нравлюсь — я информацию принял к сведению. И докучать симпатичному мне человеку, который не хочет меня знать, я не буду."
    show sl tender pioneer zorder 4
    hide sl2
    with dissolve_fast
    sa "Но… Я же вижу, что ты Жене нравишься. Что она злится, когда тебя не видит, или когда видит, но ты на неё не смотришь, или когда кто-то из девочек с тобой разговаривает."
    show 3500_el normal pioneer briefcase with dissolve_fast
    sa "Я уверена, что она сейчас и на меня злится за то, что я иду и с тобой разговариваю. Может, Женя вовсе не то хотела сказать, что ты услышал?"

    scene bg ext_aidpost_day
    show sl serious pioneer at cleft
    show 3500_el sad pioneer briefcase:
        xcenter .65 ycenter.833
    with pushleft
    sa "Серёжа, здесь на этом, как ты выразился, «женском» языке может говорить только Катя. Умеет ещё Лена, но она делать этого никогда не будет, и точно не умеет Женя."
    sa "А то, что она тебе сказала… Или ты убежал, не дослушав, или — вспомни, Женя почти ни с кем не общается — ей это просто трудно, общаться с людьми."
    show 3500_el surprise pioneer briefcase with dissolve_fast
    sa "И она может думать одно, а когда пытается озвучить мысль, то без практики получается совсем другое."
    sa "Даже её шутки, когда она просто хочет, чтобы человек улыбнулся, обычно воспринимаются как колкости."
    sa "Или же она накрутила сама на себя. Потому что если у неё с её характером до лагеря были проблемы в отношениях с людьми, она могла посчитать себя никому не нужной."
    show 3500_el upset pioneer briefcase with dspr
    sa "Дайте друг другу ещё один шанс — вот что я хотела сказать."

    scene bg ext_library_day
    show 3500_el scared pioneer briefcase:
        zoom 0.75 xcenter .86
    show sl serious pioneer far:
        xcenter .7
    with pushright
    "Саша без стука отворила дверь библиотеки и втащила за руку Сыроежкина."
    hide 3500_el
    hide sl
    with dissolve
    play sound sfx_open_door_clubs_2

    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    show 3500_el shy2 pioneer briefcase behind dct_int_library_standing_desk_front:
        zoom 0.9 xcenter .35 ycenter .755
    show sl serious pioneer behind dct_int_library_standing_desk_front:
        xcenter .6 ycenter .46
    with slidedown
    sa "Вот, я его привела.{w=0.5} Женя, это Сергей: очень хороший парень, но слишком наивный и доверчивый."
    show sl smile pioneer with dspr:
        pause .3
        linear .9 xcenter .3
        linear .3 xcenter .2 alpha 0
    show 3500_el surprise pioneer briefcase with dissolve_fast
    play sound ["<silence 0.9>", sfx_close_door_1]
    sa "А сейчас — убегаю. Прости, Женя, но меня Лена помочь ей попросила."
    stop music fadeout 1

    scene bg int_dining_hall_people_day with dct_fade
    play ambience ambience_dining_hall_full fadein 1
    "В обед пионеров кормили щами и свиной поджаркой с рожками."
    "Персонал кухни действительно научился готовить — и щи не были пересоленными, и макароны не склеились, и мясо не подгорело, и чай не отдавал тряпкой.{w} Всё бы хорошо, но брызги томатного жира от поджарки оставляли оранжевые пятна на рубашках неаккуратных пионеров."
    show mt sad pioneer close at left with dissolve
    "Ольга Дмитриевна наблюдала за этим явлением и каждый раз морщилась."
    th "Эдак никаких рубашек не напасёшься."
    th "Пионеры же через час все ко мне прибегут и заканючат: «Ольмитревна, рубашка грязная, поменяйте, пожалуйста»."
    th "Стирать им лень, к Алисе бежать побоятся: знают, что можно физически пострадать."
    show mt normal pioneer close with dspr
    th "Может, всё-таки Сашу помощником назначить?"
    extend " Алиса только «за» будет."
    th "Нет, не вариант — Саша занята собой и каждым пионером, попавшим в её поле зрения, по отдельности."
    show mt sad pioneer close with dspr
    th "Никому нет дела до лагеря в целом — наверное, даже Семёну."
    show 3500_el shy pioneer briefcase:
        zoom 0.75 xcenter .71
    show mz shy glasses pioneer far:
        xcenter 0.6
    with dissolve
    "В столовую зашли ещё двое: Сыроежкин и Женя."
    show mt surprise pioneer close with dspr
    show 3500_el shy pioneer briefcase:
        ease 1.7 xcenter 1.26
    show mz shy glasses pioneer far:
        ease 1.7 xcenter 1.15
    "Оба в землю смотрят, оба постоянно друг на друга оглядываются и сразу краснеют, при этом вместе подошли к раздаче."
    "Женя переставила на свой поднос большую часть тарелок, ткнув перед этим пальцем в портфель Сыроежкина, и вместе же они пошли за один столик, за которым и устроились, уткнувшись в тарелки."
    show mt normal pioneer close with dspr
    th "Так, ещё одна парочка."
    th "Теперь надо за ними присматривать. Дети книжные, а поговорка про тихий омут не зря придумана."
    th "Пусть делают что угодно, но только не в мою смену."
    show mt smile pioneer close with dspr
    "И вспомнилась ещё одна Ленина работа, совсем свежая, висящая в тренерской."
    stop ambience fadeout 1

    scene dct_int_coaching_room3:
        zoom 8.0 anchor (.72, .5) pos (.5, .5)
    show dct_int_coaching_room3_zoom_OSB:
        zoom 2 anchor (.44, .484) pos (.5, .5)
    show dct_mz_and_el_go_to_library_sketch:
        anchor (.5, .4) pos (.5, .5)
    show dct_mz_and_el_go_to_library:
        anchor (.5, .4) pos (.5, .5)
    with blinds
    play music peritune_gentle_theme_piano fadein 1
    "Лагерная аллея, по которой идут двое — те же Сыроежкин и Женя."
    show dct_mz_and_el_go_to_library_sketch:
        linear 1.5 zoom 0.8 anchor (.5, .46)
    show dct_mz_and_el_go_to_library:
        linear 1.5 zoom 0.8 anchor (.5, .46)
    "Идут от площади — за спинами у них Генда угадывается — в сторону библиотеки. Идут каждый по своей стороне и старательно не смотрят друг на друга."
    show dct_int_coaching_room3:
        linear 1 zoom 6.5
        linear 1 zoom 5.0
    show dct_int_coaching_room3_zoom_OSB:       # Апскейл в 4 раза задней стенки шкафа, чтоб не так шакально смотрелось. Нет, ну шакально конечно. Но не так.
        linear 1 zoom 1.625 anchor (.44, .492)
        linear 1 zoom 1.25 anchor (.44, .5)
    show dct_mz_and_el_go_to_library_sketch:
        linear 1 zoom 0.65 anchor (.5, .48)
        linear 1 zoom 0.5 anchor (.5, .5)
    show dct_mz_and_el_go_to_library:
        linear 1 zoom 0.65 anchor (.5, .48) alpha 0
        linear 1 zoom 0.5 anchor (.5, .5)
    "У Жени на лице растерянная полуулыбка, а Сергей, наоборот, сосредоточен: брови нахмурены, глаза прищурены, как будто целится куда-то, губы плотно сжаты, а в руке у него этот самый портфель, кстати."
    show dct_int_coaching_room3:
        linear 3 zoom 1 pos (.72, .5)
    show dct_int_coaching_room3_zoom_OSB:
        linear 3 zoom 0.25 pos (.72, .5) alpha 0
    show dct_mz_and_el_go_to_library_sketch:
        linear 3 zoom 0.1 pos (.72, .5)
    show dct_mz_and_el_go_to_library:
        linear 3 zoom 0.1 pos (.72, .5) alpha 0
    "И идут эти мальчик с девочкой вроде бы каждый сам по себе, но по тому, как они чуть склонились друг к другу, как они старательно при этом отводят друг от друга глаза, как они идут в ногу, видно, что уже связаны они, хотя ещё и сами об этом не подозревают."
    stop music fadeout 1

    scene bg int_dining_hall_people_day with blinds
    play ambience ambience_dining_hall_full fadein 1
    "Столовский шум волнами накатывался и отступал, иногда из него удавалось выделить отдельные голоса."
    $ d_voice_color = "#79cdf7"  # Голос Максима
    d_vocal_noise "Тётя Алиса, а если мне…"
    $ d_voice_color = "#e1dd7d"  # Голос Семёна
    d_vocal_noise "Вот и вопрос, Рыжик — как привести сюда чужую футбольную команду? Или наших туда…"
    $ d_voice_color = "#ffaa00"  # Голос Алисы
    d_vocal_noise "…собрание отряда, племянничек. Готовься."
    $ d_voice_color = "#00b4cf"  # Голос Мику
    d_vocal_noise "Леночка, а кто же это написал? Мы с Сашей думали, но так и не придумали ничего."
    $ d_voice_color = "#fff226"  # Голос Шурика. Наверное. Ну а кого ещё…
    d_vocal_noise "…Женю прозондировать, не всё так безнадёжно, тяжело, но не…"
    $ d_voice_color = "#b7b7b7"  # Голос Витьки
    d_vocal_noise "Катя, мы что, на пляж не идём?"
    $ d_voice_color = "#4de2f3"  # Голос Оксаны
    d_vocal_noise "Вася, ты после обеда не уходи никуда, пожалуйста. Я хочу…"
    $ d_voice_color = "#ff3200"  # Голос Ульяны
    d_vocal_noise "Сёмк. Я, наверное, смогу попробовать. Но уговаривать обеих вожатых будешь ты."
    "Только Женя и Сергей молчали, уткнувшись друг напротив друга каждый в свою тарелку, и отчаянно краснели, когда их взгляды пересекались."
    stop ambience fadeout 1

    scene bg int_clubs_male_day
    show sh serious pioneer close
    with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    "После обеда Шурик вернулся в кружок."
    
    scene dct_int_clubs_male2_night_zoom
    show sh smile pioneer at fright
    with dissolve
    "Он долго стоял перед установкой, гладил кончиками пальцев каркас и вращающийся табурет, установленный внутри каркаса, проводил ладонями над электронными платами."
    "Для ускорения работ корпус решили не делать, и сейчас эти платы рядком лежали на рабочем столе на плоском листе шифера, соединённые между собой экранированными проводами. Видеомагнитофон, заряженный чистой кассетой, стоял тут же."
    "Очень хотелось попробовать — останавливало только обещание, данное Сыроежкину, что без него ни-ни."
    show sh smile pioneer:
        ease 1.2 xcenter 1.25
    "Шурик забрался внутрь каркаса, уселся на табурет, проверил, как он вращается."
    "Всё было в полном порядке — включай установку и начинай запись."
    show sh normal pioneer close:
        ease 1.2 xcenter 0.8
    "Нужно было придумать, как включить и выключить установку без посторонней помощи."
    show sh normal_smile pioneer close with dissolve_fast
    th "В конце концов, Сергей не хотел, чтобы я включал без него, только как ответственный за технику безопасности, но что тут может случиться?"
    show sh serious pioneer close with dissolve_fast
    "Шурик уговаривал сам себя как мог."
    th "Если я сейчас сделаю запись, то на завтра останется меньше работы."
    show sh serious pioneer close:
        ease 1 xcenter 0.5
    play sound sfx_paper_bag
    "Шурик раскрыл рабочую тетрадь:"
    "«Шестой день смены, 15-00, пробный запуск установки. Подопытный — Александр Трофимов, оператор — Александр Трофимов. Расчётное время эксперимента — десять минут. Описание эксперимента…»"
    show sh normal pioneer close with dspr
    "Осталось только принять меры предосторожности, чтобы никто не помешал."
    play music dreamers_of_the_day fadein 1.5
    hide sh with dissolve
    play sound [ "<silence 0.5>", sfx_close_door_clubs_nextroom ]
    play sound2 [ "<silence 1.9>", sfx_open_window ]
    "Шурик вышел на крыльцо и запер двери на висячий замок, после чего обошёл здание и влез внутрь через окно."
    show sh normal_serious pioneer dct close with dissolve:
        xcenter .6
        easeout 1.5 xcenter 1.25
    "Включил установку на разогрев, а сам прямо на включённой установке стал наращивать провод, ведущий к кнопке «Пуск»."

    scene dct_int_clubs_male2_night_zoom with dct_fade
    "Вскоре всё было готово."
    
    scene dct_sh_in_cage_with_pushbutton with squares
    stop ambience
    "Шурик сидел внутри каркаса, как в клетке, табурет под ним, приводимый во вращение мотором, вытащенным из механизма дворников «Волги», медленно, почти незаметно для глаза, вращался с частотой один оборот за десять минут."
    "Сменялись цифры на дисплее магнитофона, предназначенного для записи считываемой информации."
    "Наконец табурет повернулся так, что временная кнопка «Пуск», примотанная изолентой к каркасу, оказалась напротив левого колена кибернетика."
    "Шурик мысленно перекрестился и, нажав на кнопку, начал эксперимент."
    "Теперь — главное: надо было высидеть на табурете десять минут, не меняя положения головы и стараясь ни о чём не думать."
    "Как обычно это бывает по закону подлости, всем что-то понадобилось в клубах именно в это время."
    play sound sfx_knock_door_closed_hard1
    "Кто-то трогал висячий замок и дёргал входную дверь, кто-то пытался заглянуть в окна — благо Шурик предусмотрительно задвинул шпингалеты и задёрнул занавески."
    el "Шурик, ты здесь?"
    play sound "<to 1.05>" + sfx_knock_door_closed_hard2
    "Замок подёргали ещё пару раз, и две пары ног потопали с крыльца."
    "Десять минут истекли, табурет сделал полный оборот, кнопка «Пуск» опять оказалась напротив колена."
    stop music fadeout 2

    scene dct_int_clubs_male2_night_zoom with squares
    play ambience ambience_int_cabin_day fadein 1
    show sh normal pioneer at right:
        xcenter 1.2
        pause 1.7
        ease 1 xcenter 0.72
    "Шурик отключил установку, перемотал кассету на самое начало, подключил магнитофон к компьютеру и запустил программу дешифровки."
    hide sh with dissolve
    play sound2 [ "<silence 1.5>", sfx_open_window ]
    "После этого восстановил в кружке всё как было, вылез в окно и отправился на пляж."
    "Хоть пару раз за смену, но нужно было выбраться на свежий воздух."
    stop ambience fadeout 1

    scene dct_ext_beach_day_with_pass_train
    show d_sf normal swim:
        xcenter 0.35 ypos 0.2
    show d_us normal swim:
        xcenter 0.65 ypos 0.09
    with dct_fade
    play ambience ambience_lake_shore_day fadein 1
    play sound_loop dct_ambience_beach fadein 1
    "Ульяна и Семён валялись на пляже."
    show d_sf serious swim
    show d_us serious swim
    with dspr
    "Не просто так валялись, а по делу. Нужно было пасти средний и младший отряды."
    show dct_ext_beach_day_lifesaving_shield
    show 3500_sh normal_smile swim:
        xcenter 0.25
    with dissolve
    "Исторически и в теории сложилось так, что пионеры из старшего отряда приходили на пляж и уходили когда хотели — вот как Шурик сейчас, сидевший на лавочке под щитом со спасательными кругами."
    hide dct_ext_beach_day_lifesaving_shield
    hide 3500_sh
    with dissolve
    "Средний отряд приходил по расписанию, и за ними присматривал кто-то из персонала или помощник вожатой, младшему же отряду требовались ещё и команды, выгоняющие октябрят из воды и разрешающие им снова лезть в воду."
    show d_sf smile swim
    show d_us normal swim
    with dspr
    "На деле же мелкие были довольно самостоятельными людьми и обходились без эксцессов на воде; единственное, что приходилось их выгонять оттуда, когда они уж совсем посинеют, и общаться с ними, но это Семёну было только в удовольствие."
    me "Знаешь, Рыжик, я как-то обнаружил, что они в свои семь лет ничем не хуже нас."
    show d_sf normal swim with dspr
    me "И проблем у них не меньше, и проблемы не менее важные. Это нам они кажутся смешными, а для них-то проблемы самые настоящие."
    me "Есть такая работа — называется «взросление», и неважно, в какой ты фазе, когда тебе всё равно семь, восемь, девять лет — ты всё равно взрослеешь. Если я могу помочь хорошим людям — почему нет?"
    
    scene dct_ext_beach_day_with_pass_train
    show dv grin pioneer far:
        xcenter 0.61
    show un smile2 pioneer far:
        xcenter 0.41
    show d_sf normal swim:
        xcenter 0.25 ypos 0.2
    show d_us normal swim:
        xcenter 0.75 ypos 0.09
    with dct_fade
    "На пляже появились Алиса с Леной."
    show dv grin swim far:
        pause 1.2
        linear 1 alpha 0
    show un smile2 swim far:
        pause 1.3
        linear 1 alpha 0
    with dissolve_fast
    "Кивнули Шурику, скинули форму, устроившись рядом с физруками, и побежали к воде."
    
    scene dct_ext_beach_barhan
    show d_ka p4 angry2 pioneer2swim:
        zoom 0.825 xcenter 0.65 ycenter 0.9
    with dissolve
    "Катя, сидящая неподалёку под грибком, неприязненно покосилась на Алису."
    
    scene dct_ext_beach_day_with_pass_train
    show d_sf normal swim:
        xcenter 0.35 ypos 0.2
    show d_us normal swim:
        xcenter 0.65 ypos 0.09
    with dissolve
    us "Сём, Катя переживает. Только не пялься на неё, а то убежит."
    me "Конечно, переживает. В прошлом цикле все вокруг неё бегали, а тут Макс взял и перерос её."
    me "А Катька в прошлом цикле развлекалась, а сейчас взяла и влюбилась. Тринадцать лет — самое время для первого раза, себя нынешнюю вспомни."
    show d_us shy swim with dspr
    me "Жалко её, но одна мудрая женщина сказала, что такие вещи и превращают организмы в людей."
    show d_sf laugh swim
    show d_us serious swim
    with dspr
    us "Эй, мне почти четырнадцать было!"
    show d_sf smile swim
    show d_us smile swim
    with dspr
    us "И знаешь, Сём, мне сейчас кажется, что мне внутри всегда было девятнадцать, пока я тебя ждала. А когда встретила тебя — всё на свои места встало."
    show d_sf normal swim
    show d_us normal swim
    with dspr
    show d_us normal swim:
        linear 0.5 ypos -0.05    
    us "Сёмк, последишь за средним отрядом?{w=0.5} А я пока за мячиком сбегаю. Давно не играли."
    show d_sf normal swim:
        linear 0.5 ypos 0.0
    show d_us normal swim:
        pause 0.5
        linear 1 alpha 0
    "И Ульяна, как была в купальнике и босиком, только накинув на плечи футболку, побежала в спортзал, благо он располагался от пляжа через дорогу."
    stop ambience fadeout 1
    stop sound_loop fadeout 1

    scene dct_sky_over_flowerbed_behind_library with dct_fade:
        align (1.0, 0.0)
    play ambience ambience_camp_center_day fadein 1
    mz "И что нам теперь полагается делать?"
    "Женя выглядела совершенно растерянной — точь-в-точь как на Ленином рисунке."
    el "Я не знаю, Женя, я думал, ты знаешь."
    
    scene dct_mz_and_el_sitting_on_bench_near_flowerbed with squares
    play music music_list['confession_oboe'] fadein 2
    "Женя и Сыроежкин сидели на скамейке недалеко от библиотеки и большую часть времени молчали."
    "Обоим было ужасно неловко, оба не знали, куда девать руки, оба краснели, едва пересекаясь взглядом, но разбежаться, как будто ничего не было, казалось ещё хуже."
    mz "Ничего я не знаю, Серг… Серёжа. Всё, что я знаю, я прочитала в книгах. Но я же не идиотка восторженная, я же понимаю, что книги и реальная жизнь — это разные вещи."
    mz "Может, давай для начала просто будем больше вместе проводить время."
    el "Да-да, Женя. Хочешь, я покажу тебе наш кружок, нашу работу?"
    mz "Это то, ради чего ты позавчера бегал в библиотеку каждые полчаса? Пойдём."
    mz "Всё равно в библиотеку никто не ходит, кроме Лены, а она сегодня уже была. Да и портфель этот тебе надо на место вернуть."
    
    scene bg ext_houses_day
    show 3500_el laugh pioneer briefcase:
        xcenter .35 ycenter.833
    show d_mz smile3 glasses pioneer at cright
    with squares
    "Это было новое для «Совёнка» событие: по аллее — сперва по боковой, потом, пройдя по площади, по главной — шли Женя и Сыроежкин и о чём-то разговаривали."
    "Они ещё не держались за руки, но уже и не отворачивались друг от друга, и — о чудо! — Женя даже улыбалась."
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Жаль, что это некому было видеть — старшие были заняты своими делами, а средние и младшие уже к тому времени были на пляже."
    stop ambience fadeout 1
    stop music fadeout 1

    scene black with dissolve_fast
    pause 1
    $ sunset_time()
    $ persistent.sprite_time = "night"
    
    scene black
    play ambience ambience_camp_center_evening fadein 1
    d_voice_me "Оль."
    th "Кто-то устроился в соседнем шезлонге."
    th "И этого кого-то зовут Семён."
    th "Сейчас опять начнёт уговаривать. А закончится всё полетевшим к чертям Планом мероприятий и срывом…"
    extend " Срывом чего, кстати?"
    show d_sf smile swim:
        xzoom -0.75 yzoom 0.75 xcenter 1.15 ypos 0.55
        linear 0.2 xcenter 0.93
        pause 0.6
        linear 0.2 xcenter 1.15
    me "О-оль."
    th "Нет, он очень хороший помощник.{w} Действительно помощник, и я не представляю, как в других лагерях вожатые в одиночку со всем справляются."
    th "Но он же готовый начальник ещё одного лагеря, но почему-то остаётся здесь."
    show d_sf smile swim:
        xcenter 0.05 ycenter 0.5 rotate 50.0 alpha 0
        linear 0.5 alpha 1
        pause 1.1
        linear 2 alpha 0
    show d_sf smile swim as d_sf_2:
        xcenter 0.55 ycenter 1.0 rotate 340.0 alpha 0
        pause 0.35
        linear 0.5 alpha 1
        pause 0.75
        linear 2 alpha 0
    show d_sf smile swim as d_sf_3:
        zoom 1.25 xcenter 0.9 ycenter -0.1 rotate 200.0 alpha 0
        pause 0.7
        linear 0.5 alpha 1
        pause 0.4
        linear 2 alpha 0
    me "Оль, я знаю, что ты не спишь — у тебя дрожат веки."
    mt "Семён, скажи: что ты будешь делать, если я тебе сейчас не отвечу?"
    me "Тогда…"
    "Я ясно слышу усмешку в его голосе."
    show d_sf laugh swim:
        xzoom -3.5 yzoom 3.5 xcenter 0.53 yalign -0.09 rotate 0.0 alpha 1
        ease_quad 3.5 yalign 0.14
    me "Тогда я буду действовать так, будто получил твоё согласие."
    show d_sf laugh swim:
        linear 0.5 alpha 0
    $ persistent.sprite_time = "night"      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Вот и кто начальник лагеря, спрашивается?"

    scene bg ext_house_of_mt_sunset
    play music tenderness fadein 2
    $ persistent.sprite_time = "sunset"
    show d_sf normal pioneer at left:
        ypos 0.2
    show unblink
    "Приходится открывать глаза."
    show d_sf smile pioneer with dspr
    th "Время-то к отбою, оказывается. Скоро темнеть начнёт."
    "Оглядываюсь: всё тихо и спокойно. Никто не убился, никто не подрался, никто, кажется, не убежал."
    show d_sf normal pioneer with dspr
    "Вон идёт один из Семёновых футболистов с подружкой. Несёт в руках кораблик, вырезанный из коры."
    th "Просто галеон испанский какой-то, даже поразглядывать хочется. Надо будет потом попросить."
    "А вон Лена с этюдником — сидит на лавочке напротив своего домика, а на крыльце ей Сашенька позирует."
    show d_sf serious pioneer with dspr
    th "Как бы ещё Семёна позлить, время потянув?"
    th "Вот!"
    show int_house_of_mt_sunset:
        ycenter -0.5
        pause 1.2
        linear 1 ycenter 0.5
    mt "Семён Семёнович, не изволите ли чаю?"
    "Пионеров в пределах слышимости нет, так что можно и подурачиться, но насчёт чаю я вполне серьёзна."
    me "Премного обяжете, Ольга Дмитриевна."
    "Одна из проблем состоит в том, что мы знакомы уже чёрт знает сколько и уже угадываем реплики друг друга до того, как кто-то из нас откроет рот."
    th "А кстати, сколько мы знакомы?"
    th "В прошлую смену — да, в позапрошлую — да. Дальше?"
    extend " А дальше — при попытке вспомнить у меня начинает болеть голова."
    "Беру из тумбочки три кружки."
    "Три — это потому что через пять минут здесь будет Ульяна. Это я тоже могу предсказать с вероятностью сто процентов."
    "Высыпаю на блюдце из целлофанового пакета конфеты-батончики."
    mt "Семён, иди помогай!"
    show d_sf smile pioneer at center:
        yalign 0.0
    show d_sf smile pioneer as d_sf2 with dissolve:
        zoom .75 xcenter .22 ycenter .56
        pause 0.7
        ease 1 xcenter .5
        pause 0.3
        ease 1 zoom 1 yalign 0.0 alpha 0
    show int_house_of_mt_sunset:
        pause 1.6
        linear 1 ycenter -0.5
    "Появляется Семён, достаёт из шкафа удлинитель, разматывает его и протягивает на крыльцо, выносит на крыльцо чайник и включает в розетку."
    me "Оль, чёрный или зелёный?"
    mt "Давай зелёный сегодня."
    show d_sf normal pioneer with dspr:
        pause 1
        ease 1 xcenter .28
        linear 0.5 ypos 0.2
    "Всё, я сажусь в один шезлонг. Семён разворачивает второй, ставит его с другой стороны крыльца и тоже усаживается лицом ко мне."
    show d_us smile dress:
        xcenter 1.2 ypos -0.05
        pause 1
        easein 1.5 xcenter 0.55
    "Слышу шлёпанье босых ног по дорожке: этот ритм полубега-полушага ни с чьим не спутаешь — Ульяна."
    show d_us smile dress:
        xcenter 0.55
        linear 0.5 ypos 0.09
    show d_sf smile pioneer with dspr
    "Усаживается на крыльцо.{w} Теперь, когда вся администрация лагеря в сборе, можно начинать совещание."
    "Семён смотрит, как устраивается Ульяна, и я вижу нежность в его глазах. Поэтому не начинаю, пока он не примет деловой вид."
    show d_sf serious pioneer
    show d_us normal dress
    with dspr
    th "Поразительно, но сколько эмоций можно выразить движениями одних только уголков глаз."
    $ sunset_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    mt "Ну-с, что вы сегодня приготовили для бедной задёрганной вожатой, дорогие мои?"
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
    
    
    
##############################
#Глава 7. Чужие в чужой земле#
##############################

label dct_foreign_land_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Чужие в чужой земле"
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop ambience
    stop sound_loop
    play music music_list['your_bright_side'] fadein 2
    show headline_text2 u"Глава VII. Чужие в чужой земле" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene bg ext_no_bus_sunset with dissolve:
        zoom 2 pos (-0.33, -0.2)
    "Оказывается, это трудно — наладить отношения с другим человеком, даже если этот человек тебе нравится.{w} Даже если ты нравишься этому человеку."
    "За шесть часов Электроник и Женя успели три раза поссориться и два раза помириться. И сейчас пытались помириться в третий раз."
    "Началось всё с того, что Женя пошутила в своей обычной манере, когда окружающим не понятно, что это — или шутка, или очередной укол."

    scene black
    show d_mz smile2 glasses pioneer close at center
    with squares
    mz "Тебе не поздно ещё убежать и сделать вид, что ничего не было."
    "А Электроник понял всё буквально."
    hide d_mz
    show el serious pioneer close at center
    with pixellate
    extend " Ну, почти буквально."
    el "Если ты так говоришь, значит, ты хочешь, чтобы я убежал."
    hide el
    show d_mz shyangry glasses pioneer close at center
    with pixellate
    "И Женя не нашлась, что ответить."
    "Убеждать, что её не так поняли, она не хотела, сказать в ответ: «Ну и скатертью дорога!» — не смогла. {w}Собиралась, но перехватило дыхание."

    scene dct_mz_and_el_sitting_on_grass with squares
    "Были там ещё, конечно, и другие слова, и в результате парочка, собирающаяся распасться, не успев сложиться, молча сидела в тени деревьев, стараясь не смотреть друг на друга."
    "Электроник держался за ручку всё того же многострадального портфеля, всё искал и не находил в себе силы встать, попрощаться и уйти в кружок.{w} Всё-таки Жене он не нужен…"
    "Женя же всё мучительно пыталась понять, что она сделала не так. Отчего сейчас всё рушится?"
    th "Сейчас он встанет и уйдёт."
    extend " И всё."

    scene bg ext_path_sunset:
        zoom 1.5 align (1.0, 0.1)
    show 3500_el sad pioneer briefcase:
        xcenter .65 ycenter.833
    with dissolve
    "Сергей вздохнул, как-то сгорбившись поднялся на ноги, прихватив портфель левой рукой, повернулся к Жене, собираясь что-то сказать на прощание."

    scene bg ext_path_sunset:
        zoom 1.5 align (0.0, 0.1)
    show d_mz cry glasses_glare pioneer at cleft
    with dissolve
    mz "Спасибо за то, что потратил на меня время."
    "Женя тоже поднялась и стояла, наклонив голову так, чтобы в очках отражалось садящееся Солнце, и произносила такие слова, какие сумела подобрать, когда поняла, что Сергей сейчас уйдёт."
    "Что вот эта мелькнувшая между ними сегодня не любовь, не дружба, не влюблённость, а так, тень взаимной симпатии — это всё, что она получила и получит от жизни. Вообще всё."
    stop music fadeout 2

    scene dct_int_bus_window_view
    show dct_int_bus_window_view_el_mz
    show dct_dream_veil at shiver
    with blinds
    "Это потом, уже в автобусе, когда они сядут рядом и Женя склонит голову на его плечо, Электроник признается:"
    play sound_loop sfx_bus_interior_moving fadein 1
    el "Понимаешь, Женя, я вдруг понял, что ты пускаешь солнечные зайчики очками мне в глаза не для того, чтобы дополнительно позлить меня, а чтобы спрятать от меня слёзы.{w} И тогда увидел тебя."
    el "Не умную и симпатичную девочку, которая мне понравилась с первого дня, и не стервозную грымзу."
    mz "\~ Ну спасибо. \~"
    el "А перепуганную, не знающую, что ей делать, девушку, которая прячет свои испуг и растерянность под иронией.{w} Которая еле сдерживается, чтобы не дать себе разреветься в моём присутствии.{w} Которая действительно не умеет говорить о каких-то вещах."
    el "Я сам не умею, а та девушка — ещё хуже. И я нарушил своё правило: рискнул и решил всё про нас двоих, самостоятельно и в одиночку."
    mz "А стервозная грымза вдруг увидела твою простоту, Серёжа."
    mz "Не примитивность, а простоту."
    el "\~ Как у отвёртки. \~"
    mz "Гениальную простоту, о которой говорят: «Без страха и упрёка». Что бы ты о себе ни думал."
    stop sound_loop fadeout 2
    "Но случится это только неделей позже, когда смена закончится."

    scene bg ext_path_sunset
    show el laugh pioneer far:
        xcenter 0.54
    show d_mz confused glasses pioneer far:
        xcenter 0.46
    with blinds
    play music tenderness fadein 2
    "Портфель упал на траву, и Сергей, внезапно оказавшись напротив Жени, взял её за запястья и сказал, запинаясь, краснея и спотыкаясь через слово:"
    el "Тратить время на тебя, Женька, полезно, удивительно легко и приятно. И я собираюсь это так и продолжать."
    show el upset pioneer far:
        xcenter 0.53
    show d_mz shy_cry pioneer far:
        xcenter 0.47
    with dissolve_fast
    "А Женя вдруг уткнулась лицом в Электроника, уронив очки, и впервые в жизни заплакала на людях."
    $ sunset_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    mz "Ты…{w=0.3} ты…{w=0.5} никто…{w=0.5} никогда…{w=0.3} никогда не…{w=0.2} не называл меня Женькой."
    stop music fadeout 2

    scene black with dissolve2
    $ night_time()
    $ persistent.sprite_time = "day"
    pause 0.5

    scene dct_int_musclub_night_light
    show mi smile pioneer far
    show sl smile2 pioneer:
        xcenter 0.68
    show d_ma smile pioneer:
        xcenter 0.32 yalign 0.02
    with dissolve
    play ambience ambience_music_club_night fadein 1
    mi "Ребята, спасибо, что пришли. Гораздо приятнее играть для кого-то, даже просто аккомпанировать, чем сидеть одной в кружке."
    show sl happy pioneer
    with dspr
    sa "Тебе спасибо, Мику."
    show mi shy pioneer far
    show sl smile pioneer
    with dissolve_fast
    sa "Максим, до дискотечного уровня я тебя подтянула."
    sa "Ещё пару раз позанимаемся, чтобы у тебя всё автоматически получалось, и можешь смело приглашать свою «тётю Алису»."
    show d_ma shy pioneer
    show mi smile pioneer far
    with dissolve_fast
    "Мику смотрела на Сашу с Максимом, стоящих рядом и ещё разгорячённых после танца, и любовалась ими. Они так здорово смотрелись вдвоём — оба спортивные, светловолосые, голубоглазые, и оба одновременно открытые и застенчивые.{w} Жалко даже, что они не вместе."
    show d_ma normal pioneer with dissolve_fast
    "И так неохота их отпускать, потому что они сейчас уйдут, и опять нужно будет сидеть тут в четырёх стенах музыкального кружка в надежде, что кто-то из пионеров вдруг захочет научиться играть на ксилофоне."
    mi "Максим, Саша, а может, вы дальше будете заниматься? Ко мне всё равно никто не приходит, так что аккомпанемент я вам обеспечу."  
    "Танцоры переглянулись, пожали плечами."
    show d_ma grin2 pioneer with dissolve_fast
    $ persistent.sprite_time = "day"      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    d_ma "Мы подумаем."
    hide mi
    hide d_ma
    hide sl
    with dissolve
    stop ambience fadeout 1

    scene dct_int_musclub_night_nolight with dissolve
    pause 0.5
    $ persistent.sprite_time = "night"

    scene dct_ext_music_club_verandah_night
    show mi normal pioneer far:
        xcenter 0.24
    show d_ma smile pioneer:
        zoom 0.75 xcenter 0.41 yalign 1.01
    show sl smile pioneer far:
        xcenter 0.56
    with slideawayup
    play ambience ambience_camp_center_night fadein 1
    "Уже стемнело и жара отступила, была та самая комфортная температура, когда солнце уже не обжигает, а в то же время прогревшиеся за день воздух и земля отдают достаточно теплоты, не давая мёрзнуть."
    show sl smile pioneer at center with dissolve
    sa "Давайте посидим ещё. Не хочется расходиться."
    show d_ma smile pioneer with dissolve:
        zoom 1.0 xcenter 0.27 yalign 0.02
    sa "Только свет не включайте, а то насекомые налетят."
    show sl smile pioneer behind d_ma:
        linear 0.5 ypos 0.19
    show d_ma smile pioneer:
        linear 0.5 ypos 0.21
    hide mi with dissolve
    "Они присели, вытянув ноги.{nw}"    # Обрываем реплику тегом {nw}, чтобы запустить пластинку
    $ renpy.music.set_volume(0.4)
    play sound_loop dct_sfx_record_crackling fadein 1
    play music ["<silence 1.0>", music_list['so_good_to_be_careless'], "<silence 1.0>", music_list['forest_maiden'], "<silence 1.0>", music_list['farewell_to_the_past_full'], "<silence 1.0>", music_list['reflection_on_water'], "<silence 1.0>", music_list['what_do_you_think_of_me']]     # Очередь из музыкальных файлов с паузами в 1 секунду между ними
    "{cps=0}Они присели, вытянув ноги. {/cps}{w=0.8}Мику ещё на минутку вернулась в кружок, чтобы поставить там пластинку с музыкой и приоткрыть окно." # Вставляем дубль предыдущей реплики внутри тега {cps=0} {/cps}, чтобы она появлялась мгновенно. Тем самым создаётся впечатление, что это единая плавно текущая реплика, а музыка и треск включается посреди неё.
    show mi normal pioneer behind sl with dissolve:
        xcenter 0.78 ypos 0.19
    d_ma "Саш, а ты давно танцуешь?"
    show sl happy pioneer with dissolve_fast
    sa "Да сколько себя помню."
    sa "Бальные танцы."
    show sl smile pioneer
    show d_ma normal pioneer
    with dissolve_fast
    extend " Поэтому мне до здешнего уровня ой как тяжело опускаться, цени. Исключительно ради тебя и Алисы."
    d_ma "А я подглядывал, как ты танцуешь, Саш.{w} Это не бальные."
    show mi shocked pioneer
    show d_ma serious pioneer
    with dissolve_fast
    d_ma "Скажи, почему ты стараешься, чтобы тебя не видели?"
    show sl surprise pioneer
    show mi upset pioneer
    with dissolve_fast
    sa "Все подглядывали…{w} Ну, не все, конечно."
    show sl smile2 pioneer
    show mi normal pioneer
    show d_ma normal pioneer
    with dissolve_fast
    sa "Видишь ли, Максим, те соло — это просто для души. И как часть души."
    sa "Вот у Мику — музыка, у той девочки, которая написала сказку и подписалась «Мику Хатсуне» — у той слова."
    show mi upset pioneer with dissolve_fast
    extend " Лена — рисует. А у меня — вот такие танцы соло."
    sa "Я не против, если кто-то увидит кусочек моей души, но раскрывать свою душу специально для публики я не готова."
    show mi sad pioneer with dissolve_fast
    "Саша кивнула сама себе, каким-то своим мыслям и замолчала."
    mi "Максимчик, завтра собрание отряда, ты готов?"
    show sl serious pioneer
    show d_ma serious pioneer
    with dissolve_fast
    d_ma "Нет, Мику.{w} А как я должен к нему подготовиться?{w} Клятву страшную выучить? Или подойти к каждому из вас и попросить проголосовать за меня?"
    show sl normal pioneer with dspr
    sa "Вообще-то все и так проголосуют за тебя."
    show mi upset pioneer with dissolve_fast
    sa "Собрание не для того, чтобы тебя не принять, а для того, чтобы ты имел возможность отказаться. Потому что понять, что тебя ожидает, ты ещё не можешь. Но если внутренний голос против, то лучше будет к нему прислушаться."
    show sl smile pioneer with dspr
    sa "Так мне вчера Лена сказала. Только не выдавайте меня."
    show d_ma smile pioneer
    show mi normal pioneer
    with dissolve_fast
    "Они посидели ещё немного, обсуждая странности в поведении Лены и Алисы. Вспомнили и про физруков."
    show d_ma normal pioneer
    show sl normal pioneer
    show mi upset pioneer
    with dspr
    mi "Но откуда-то же появилась эта папка. И подписано моим именем и моим почерком, Сашенька, Максимчик. И я чувствую, что могла бы так написать, ну, пусть не так хорошо, но похоже. А Леночка и Сенечка отвечают совершенно непонятно."
    stop music fadeout 2
    pause 1
    show mi normal pioneer with dspr
    stop sound_loop fadeout 1
    "А потом кончилась пластинка."
    show sl smile pioneer:
        linear 0.5 ypos 0.0
    show sl smile2 pioneer with dissolve_fast:
        ypos 0.19
        linear 0.5 ypos 0.0
    sa "Пойду я — спать скоро, а надо ещё душ после танцев принять."
    show sl smile pioneer with dissolve_fast
    sa "Максим, я и для тебя душ зарезервировала у Ульяны. Пошли в спортзал, я тебя вперёд пропущу, а то тебе ещё отбой играть."
    show d_ma smile pioneer:
        linear 0.5 ypos 0.0
    show d_ma shy pioneer with dissolve_fast:
        ypos 0.21
        linear 0.5 ypos 0.0
    pause 0.3
    hide sl
    hide d_ma
    with dissolve_fast
    show mi smile pioneer with dissolve_fast
    "А Мику смотрела вслед Максиму, уходящему по освещённой аллее, и думала, что пусть эти двое и не влюблены друг в друга, но, кажется, у Саши вот-вот появится или уже появился хороший друг, и это здорово."
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Потому что Леночка — она замечательная девушка, но иногда её бывает так трудно понять."
    stop ambience fadeout 1

    scene black with dissolve_fast
    $ renpy.music.set_volume(1.0)
    pause 0.5
    $ night_time()
    $ persistent.sprite_time = "day"

    scene dct_int_house_of_el_night_light with dissolve_fast
    play ambience ambience_int_cabin_night fadein 1
    "Шурик лежал, глядя в потолок, и ждал, когда угомонится Сыроежкин.{w} Очень хотелось, не дожидаясь утра, пойти и посмотреть на результаты расшифровки."
    play sound_loop dct_sfx_wood_floor_squeak
    show el smile pioneer close at left with dissolve
    show el smile pioneer at center with dissolve
    show el smile pioneer far at cright with dissolve
    hide el with dissolve
    "Потому что завтра, во-первых, будет неудобно перед напарником за то, что первое испытание провёл без него. А во-вторых, вдруг там записалось что-то такое, за что потом перед Сергеем будет стыдно."
    show el laugh pioneer far at cright with dissolve
    show el laugh pioneer at center with dissolve
    show el laugh pioneer close at left with dissolve
    hide el with dissolve
    $ persistent.sprite_time = "day"                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "А Сыроежкин всё никак не хотел затихать."
    show dct_int_house_of_el_night with dissolve
    $ persistent.sprite_time = "night"
    "Ходил по комнате взбудораженный, что-то фальшиво напевая."
    show d_el grin shorts at cleft with dissolve
    extend " Всё порывался рассказать Шурику, какая замечательная девушка работает в библиотеке."
    show d_el upset nude at cright with dissolve
    extend " И выяснял, не припрятан ли у Шурика в чемодане флакон с одеколоном."
    hide d_el with dissolve
    stop sound_loop
    play sound sfx_bed_squeak1
    "А потом, когда уже улёгся, всё мечтательно вздыхал и ворочался с боку на бок. И уснул далеко после отбоя."
    stop ambience fadeout 1
    play music music_list['you_lost_me'] fadein 3
    show 3500_sh normal_smile shirt at center with dissolve:
        ycenter 0.833 alpha 0
        pause 1.5
        linear 1 alpha 1
    "Шурик подождал ещё минут тридцать, дожидаясь, когда дыхание у соседа успокоится, после чего встал и, не одеваясь, осторожно вышел на крыльцо, прихватив с собой одежду."
    hide 3500_sh with dissolve

    scene dct_ext_house_of_el_night
    show 3500_sh smile shirt:
        zoom 0.75 xcenter 0.6
    with slideawayup
    "Лагерь ещё не уснул до конца. Ещё горел свет в отдельных домиках, слышно было, как кто-то мелкий, ступая бесшумно, но выдавая себя сосредоточенным сопением, крадётся от укрытия к укрытию."
    show 3500_sh upset shirt with dspr
    "Ещё можно было нарваться и на вожатую, совершающую вечерний обход."
    show 3500_sh upset pioneer with dissolve_fast
    "Шурик, не зажигая фонаря над дверью, оделся"
    show 3500_sh serious pioneer with dissolve_fast:
        pause 0.7
        easeout 2 xcenter -0.15
    extend " и, избегая чужого внимания, свернул направо, чтобы обогнуть тёмное здание административного корпуса и через полосу молоденьких сосенок выйти на дорожку, соединяющую музыкальный кружок с главной аллеей."

    scene dct_ext_forest_dark_night
    show sh upset pioneer close
    with fade
    "То, что он плохо ориентируется в ночном лесу, Шурик понял почти сразу."
    "Захотел повернуть назад, на свет фонарей, освещавших аллею, но, услышав, как хлопнула дверь в крайнем домике, передумал."
    th "Ещё не хватало, чтобы увидели, как я из кустов выбираюсь."
    "Поэтому оставалось двигаться только вперёд, используя для ориентировки исключительно внутренний компас потомственного горожанина, не бывавшего нигде дальше городского парка с аттракционами, куда восьмилетнего Шурика водила мама."
    show sh rage pioneer close with dissolve_fast
    "Это было… нелегко."
    "Паутина липла к лицу, ноги спотыкались о невидимые кочки, ветки норовили сбить очки с лица, и приходилось очки придерживать рукой, потому что со зрением минус шесть передвигаться без очков в ночном лесу остаётся только на ощупь."

    scene bg ext_path2_night
    show ext_path2_night at walking
    with squares
    "Так что когда впереди показался свет, Шурик обрадовался и зашагал энергичнее."
    th "Кажется, это фонарь, и я вышел к поперечной аллее."
    extend " Сейчас мне налево, и я окажусь на перекрёстке."
    stop music fadeout 1

    scene dct_ext_musclub_night_lantern_light with irisout
    play music music_list['timid_girl']
    show mi shocked pioneer with dissolve
    mi "Ой, Сашечка, а что ты здесь делаешь? Ты ко мне пришёл? Но уже поздно. Я вот задержалась у себя в кружке, играла и думала, думала и играла, пересела в кресло и задремала. А проснулась — уже поздно. На часы посмотрела — отбой давно был, а я и не слышала. А жалко, мне так нравится Максима слушать, ведь когда живой человек играет — это гораздо лучше, чем запись."
    sh "Здравствуй, Мику. Я…{w} гулял.{w} И заблудился в лесу, а к твоему кружку вышел случайно."
    show mi upset pioneer with dissolve_fast
    th "Вот ведь как невовремя!"
    th "Сейчас пойдут разговоры, она же не удержится. А попросить не болтать — так ещё хуже выйдет."
    show mi serious pioneer with dspr
    th "Хотя попробую. Девочка она добрая…"
    dreamgirl "Микс!"
    th "…и понимающая, хоть и болтушка."
    sh "Мику, можно тебя попросить об одной вещи?"
    show mi smile pioneer close with dissolve_fast
    mi "Конечно, Сашечка."
    sh "Не рассказывай никому, что я заблудился. Неудобно."
    mi "Конечно-конечно, Сашечка. Я — могила! Но пойдём я тебя до домика провожу. Вот тропинка. А то ты опять куда-нибудь заблудишься."
    "Приговаривая так, Мику убирала хвою, сор, мелкие веточки с одежды Шурика. Материализовав откуда-то носовой платок и поплевав на него, стёрла паутину и попыталась оттереть следы смолы с лица."
    show mi shy pioneer close with dissolve_fast
    mi "Только…{w=0.7} Сашечка, может, тебе сначала к умывальникам? Мыло и полотенце у меня в кружке есть. А я подожду."
    "Вот к умывальникам идти было совершенно незачем. Еле-еле удалось доказать Мику, что до клубов идти ближе и по асфальту, что там есть раковина, что там есть и полотенце, и мыло."

    scene dct_ext_houses_night_lantern_light with pushright
    "Но отделаться от Мику не удалось, и Шурику пришлось идти в её сопровождении по самой середине ярко освещённой аллеи под её бесконечное чириканье, привлекая внимание всех, кто хотел и мог это увидеть."
    "Кажется, кто-то увидел, кажется, чья-то тень мелькнула от фонаря в кусты."
    show mi laugh pioneer close at fleft with dissolve_fast
    mi "Ну всё, хи-хи, Сашечка, теперь нас точно в парочку запишут."
    hide mi with dissolve_fast
    "Но Шурику было всё равно."
    "Шурик, оставив щебетанье Мику как звуковой фон, размышлял, как ему достаточно вежливо и не обижая избавиться от её общества, но так ничего и не успел придумать."
    stop music fadeout 1

    scene bg ext_clubs_night
    show mi smile pioneer close at fright
    with dct_fade
    play ambience ambience_camp_center_night fadein 1
    mi "Вот и пришли, Сашечка. Ой, а там же ваша машина, мне Серёжа про неё рассказывал, когда табуретку в кружке просил. А можно на неё посмотреть?"
    stop ambience fadeout 1

    play music "<silence 0.5>"
    queue music my_2nd_summer fadein 1.5
    scene dct_int_clubs_male_night with slidedown
    pause 0.4

    scene dct_int_clubs_male_night_light with dissolve
    $ persistent.sprite_time = "night"                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Пришлось сначала показывать."
    $ persistent.sprite_time = "day"

    scene dct_int_clubs_male2_night_zoom
    show sh serious pioneer at right
    with dissolve
    "А потом пришлось, выполняя обещание Сыроежкина, усадить Мику на вращающийся табурет и сделать запись."
    mi "Нет-нет, Сашечка, я понимаю, что Серёжа будет обижаться, поэтому буду делать вид, будто завтра я в первый раз всё это вижу.{w} Понимаешь, для меня это очень важно.{w} А когда можно будет увидеть результаты?"
    show sh normal pioneer with dspr
    "А вот с результатами было неясно."

    scene dct_mi_in_cage with squares
    "Мику рассматривала интерьеры кружка кибернетики и хихикала, сидя внутри клетки:"
    mi "Я обезьянка Мику, умею петь и играть на всех инструментах. Дорогая публика, подходите поближе, не стесняйтесь!"
    "Потом она внезапно погрустнела."
    mi "Сашечка, неужели я и есть всего лишь такая забавная учёная обезьянка?"
    "И пока Мику крутилась, совершая один оборот за десять минут на своём табурете, наблюдая за Шуриком так и оставшимися печальными глазами, тот сидел перед монитором и пытался понять, что же выдала ему программа расшифровки."

    scene dct_int_clubs_male_night_light_mon
    show sh serious pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    with dissolve
    "Теоретически, это должно было быть что-то вроде отдельных кадриков, сменяющих друг друга как слайды и склеенных в тридцатисекундный ролик."
    "И эти кадрики должны были служить подсказками для самого Шурика или любого другого испытуемого, кто там перед этим сидел на вращающемся табурете. Большего от имеющейся у кибернетиков аппаратуры и ждать было нельзя."
    "А сейчас, с разрешением 640 х 200, с монитора на Шурика смотрело его собственное лицо — ну, почти его собственное."

    scene dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_al:
        xcenter 0.5 ycenter 0.45
    with dissolve
    th "Кто-то меня состарил лет на двадцать."
    th "Где-то ошибка в программе."

    scene dct_int_clubs_male_night_light_mon
    show sh normal pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    with dissolve
    th "Утешает одно: какой-то результат мы получили."
    show dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    show dct_clubs_male_comp_night:
        alpha 0
        pause 1.5
        linear 1 alpha 1
    "Шурик запустил программу дешифровки и выключил монитор."

    scene dct_int_clubs_male2_night_zoom
    show sh serious pioneer
    show mi sad pioneer at fright
    with dissolve
    "Потом помог выбраться из клетки Мику и машинально, совсем не задумываясь и не слыша себя, ответил на её вопрос, заданный десять минут назад."
    stop music fadeout 2

    scene dct_int_clubs_male_night_light
    show sh serious pioneer at cleft:
        xcenter 0.4
    show mi shocked pioneer at fleft
    with dissolve
    play ambience ambience_int_cabin_night fadein 1
    sh "Мику, если даже и так. Подумай о том, что, задав себе такой вопрос, ты сделала первый шаг из клетки."
    "А потом, уже придя в себя, продолжил более впопад."
    show sh normal pioneer with dspr
    sh "Результаты будут завтра утром, но где-то я ошибся, поэтому истолковать их правильно, скорее всего, не получится…"
    show mi serious pioneer with dissolve_fast
    $ persistent.sprite_time = "day"                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " В общем, завтра после подъёма встречаемся здесь."
    hide sh
    hide mi
    with dissolve
    stop ambience fadeout 1

    scene bg ext_clubs_night with slideawayup
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 1
    "Шурик проводил девушку до перекрёстка, откуда Мику убежала по боковой аллее, зацокав каблучками."

    scene dct_ext_houses_night_lantern_light
    show mi normal pioneer far at cleft
    with pushleft
    mi "Нет-нет, Сашечка, дальше провожать не надо, дальше я сама, короткой дорогой."

    scene dct_ext_house_of_el_night with fade
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "А Шурик, вернувшись к себе в домик, проспал без сновидений до самого подъёма, даже не задумавшись о том, что уверенно добрался до него, тоже через лес, тоже самой короткой дорогой — так, как будто исходил тут всё вдоль и поперёк."
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ day_time()
    $ persistent.sprite_time = "day"

    scene dct_ext_house_of_el_day with dissolve_fast
    play ambience ambience_camp_center_day fadein 1
    "Утром, однако, никто и ничего не сказал про то, что видел, как Шурик и Мику поздно вечером вдвоём шли к клубам, а потом возвращались обратно."    
    play sound dct_sfx_horn_rise_through_loudspeaker
    "Протрубил в горн Максим, пионеры, пользуясь тем, что никто не гоняет на зарядку, начали медленно выползать из домиков и перемещаться в направлении умывальников."
    show 3500_el smile pioneer:
        zoom 0.2 anchor (0.5, 0.5) pos (0.55, 0.58) alpha 0
        pause 0.8
        linear 0.3 alpha 1
        linear 0.7 zoom 0.4 pos (0.72, 0.7) knot (0.55, 0.7)
        linear 0.8 zoom 0.4 pos (1.1, 0.7)
    show dct_sl_sport_running_surprise:             # Псевдокартинка, где Саша сначала серьёзная, а через 1,4 сек удивлённая
        zoom 0.4 anchor (0.5, 0.5) pos (-0.1, 0.7)
        linear 3.2 pos (1.1, 0.7)
    "Сашка пробежала в сторону стадиона, счастливый Сыроежкин с первыми звуками горна подскочил и убежал на пост, к домику Жени."

    scene black with dissolve
    show bg ext_house_of_mt_day
    show unblink
    "Вожатая, додрёмывая в шезлонге, наблюдала за постепенным пробуждением лагеря и думала о том, что завтра прибывает опоздавший пионер, что придётся селить Алису у себя, а опоздавшего — вместе с Максимом, в Алисином домике."
    show blinking
    th "Ох и ругаться будет Рыжая."
    "Небо с запада постепенно затягивало тучами, да ещё и неприятный такой ветерок потянул с реки."
    stop sound fadeout 2.5
    th "Кажется, погода всё портит, кажется, весь день сегодня будем сидеть по домикам."
    play sound dct_sfx_horn_assembly_through_loudspeaker
    th "Нет, горнист в лагере — это действительно здорово."
    "Ольга поднялась и пошла на площадь, чтобы там довести до пионеров программу сегодняшнего дня."

    scene bg ext_square_day
    show d_sf normal pioneer:
        xcenter 0.25
    show mt angry panama pioneer close
    with squares
    mt "Лагерь, по отрядам, на линейку."
    show mt rage panama pioneer close with dspr
    extend " Становись!"
    show d_sf smile pioneer
    show mt angry panama pioneer close
    with dspr
    "Семён сзади чуть слышно фыркнул — он всегда фыркает при этой команде, но ничего не объясняет."
    "Средний отряд, подгоняемый Ульяной, встал на своё место."
    show d_us smile sport behind mt:
        xcenter 0.75 ypos -0.05
    with dissolve
    "Прибежали малыши, построились."
    show d_sf normal pioneer with dspr
    "Солидно выступили старшие: Мику, Лена, Саша, Алиса на правом фланге."
    show d_us normal sport with dspr
    th "Стоп, а где остальные?"
    "Но спрашивать не пришлось: со стороны домиков прибежали Женя с Сергеем Сыроежкиным, а со стороны клубов — Шурик."
    th "Все на местах?"
    show mt rage panama pioneer close with dspr
    mt "Равняйсь! Смирно! Вольно!"
    show mt angry panama pioneer close
    show d_sf smile pioneer
    show d_us smile sport
    with dspr
    "Можно начинать."
    show mt normal panama pioneer close with dissolve_fast
    mt "Дорогие пионеры, сегодня седьмой день смены…"
    show d_sf normal pioneer
    show d_us normal sport
    with dspr
    "Как обычно в эти минуты, разум у Ольги отключился, а текст пошёл на полном автопилоте."
    mt "…а программу спортивного праздника до вас доведёт мой заместитель."
    show mt normal panama pioneer behind d_sf:
        xcenter 0.55
    show d_sf normal pioneer:
        zoom 1.25 xcenter 0.3 ypos -0.05
    with dissolve_fast
    me "Вот скажите, товарищи пионеры. А чего вы ждёте от сегодняшнего праздника?"
    kids "Бега!\nПлавания!\nФутбола!"
    show d_sf smile pioneer with dspr
    "На слове «футбол» Семён заинтересованно повернул голову в сторону кричавшего, но промолчал."
    kids "Поспать!"
    show mt sad panama pioneer
    show d_sf laugh pioneer
    show d_us laugh sport
    with dspr
    "Все засмеялись, Ольга поджала губы, а Семён одобрительно кивнул, показав большой палец."
    show dct_ext_square_after_rain behind mt:
        alpha 0
        linear 10 alpha 0.5
    show dct_overcast_rain_1:
        xzoom -1.0 alpha 0
        linear 10 alpha 1
    show mt smile panama pioneer with dspr
    mt "\~ Вот клоун. Сейчас скажет, что… \~"
    stop ambience fadeout 2
    play sound_loop "<loop 2 to 51>" + dct_ambience_light_rain fadein 2
    $ renpy.pause(0.8,hard=True)
    show mt surprise panama pioneer
    show d_sf normal pioneer
    show d_us hurt sport
    with dspr
    $ renpy.pause(0.9,hard=True)
    "Ничего Семён не сказал, потому что серые и низкие тучки уже начали сеять дождиком. Сперва мелким, но постепенно всё более и более сильным и уверенным."
    "Пионеры уже ёжились в своих тонких рубашках."
    show d_sf serious pioneer
    me "Лагерь. Напра-во! В столовую, бегом, марш!"
    show d_us serious sport behind d_sf:
        xzoom -1.0
    show d_us_sport_mirror behind d_sf:
        xzoom -1.0 xcenter 0.75 ypos -0.05
    with dissolve_fast
    show d_us serious sport:
        ease 2 xcenter 1.5
    show d_us_sport_mirror:
        ease 2 xcenter 1.5
    show mt normal panama pioneer:
        ease 2 xcenter 1.25
    show d_sf normal pioneer:
        ease 1.6 xcenter 1.3
    pause 0.3
    
    play sound_loop2 "<from 1.9 loop 3.5>" + dct_sfx_steps_in_swamp fadein 1.2
    scene dct_ext_сentral_alley_from_dining_hall_to_west_after_rain at running
    show dct_overcast_rain_1 at running:
        xzoom -1.0
    show dct_overcast_rain_2 at running:
        xzoom -1.0
    with squares
    "И уже под хорошим таким ливнем, оставив Ольгу с Ульяной управляться в столовой с пионерами, Семён побежал с Алисой к складу за плащами — прозрачными накидками из плёнки: красными для малышей, жёлтыми для среднего отряда, синими для старшего и бесцветными для персонала."
    stop sound_loop fadeout 1
    stop sound_loop2 fadeout 1

    scene white with dct_fade
    play music music_list['get_to_know_me_better']
    "Женя в хорошем настроении и Женя в настроении обычном — это два разных человека."
    show ext_house_of_sl_day
    show el laugh pioneer close at right
    show dct_int_house_of_mi_day
    show mi upset pioneer far at cright
    show mz laugh glasses pioneer close at left
    with dissolve
    "Начиная с самого утра, когда поздоровалась с куда-то торопящейся соседкой и выбежала навстречу Сергею — нет, Серёже."
    show dct_int_house_of_mi_day:
        linear 1 ycenter -0.5
    show mi upset pioneer far at cright:
        linear 1 ycenter -0.5
    show mz shy glasses pioneer close at left with dissolve_fast
    mz "Доброе утро, я рада тебя видеть."
    el "А как я рад, Женя."
    hide dct_int_house_of_mi_day
    hide mi
    "И вот это «как я рад» ещё добавило градус счастья. Даже торчащие у Сергея из кармана шорт полотенце и зубная щётка вызвали только умиление."
    show mz shy pioneer close at left as mz2:
        alpha 0
        pause 0.5
        linear 0.5 alpha 1
    show ext_house_of_sl_day:
        xcenter 0.5
        linear 1 xcenter 1.5
    show ext_washstand_day behind el:
        xcenter -0.5
        linear 1 xcenter 0.5
    "Что может быть романтичнее совместного утреннего похода к умывальникам и обратно?"
    show mz shy pioneer close as mz2:
        alpha 1
        linear 0.5 alpha 0
    show ext_washstand_day:
        xcenter 0.5
        linear 1 xcenter -0.5
    show dct_int_house_of_mi_day behind el:
        xcenter 1.5
        linear 1 xcenter 0.5
    hide ext_house_of_sl_day
    pause 1
    show mi upset pioneer behind el with dissolve
    "Зашла Мику, отчего-то грустная и серьёзная, кивнула Сергею."
    show ext_house_of_sl_day behind dct_int_house_of_mi_day
    hide mi with dissolve
    show dct_int_house_of_mi_day:
        pause 0.5
        linear 1 ycenter -0.5
    "Кажется, Мику едва сдерживала слёзы, но это парочку сейчас не интересовало, парочка сейчас была самодостаточна."

    scene dct_ext_house_of_el_day with pushright
    "Потом была совместная романтическая пробежка к домику Сергея, чтобы тот оставил в домике свои умывальные принадлежности"
    show bg ext_square_day with pushleft
    extend ", романтическая пробежка на площадь."
    show dct_ext_square_after_rain:
        alpha 0
        linear 10 alpha 0.5
    show dct_overcast_rain_1:
        xzoom -1.0 alpha 0
        linear 10 alpha 1
    show d_sf smile pioneer:
        xcenter 0.25
    show d_us smile sport:
        xcenter 0.75 ypos -0.05
    show mt angry panama pioneer
    with dissolve
    "Романтическая линейка, когда можно стоять рядом и поминутно оглядываться друг на друга и касаться случайно руками. Взяться за руки ни Сергей, ни Женя пока ещё не решались."

    scene dct_ext_dining_hall_near_rain with pushleft
    $ persistent.sprite_time = "day"                          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Романтическая пробежка под дождём к столовой, когда Сергей всё норовил стащить с себя рубашку, чтобы прикрыть ею Женю."

    scene dct_int_dining_hall_people_rain with slidedown
    $ persistent.sprite_time = "night"
    "В столовой Женя перехватила взгляд Шурика."
    show d_mz smile2 glasses pioneer close at left with dissolve
    mz "На тебя Шурик ворчать не будет? Если будет — ты скажи мне. Я его на место поставлю."
    show d_el smile2 pioneer close at right with dissolve
    el "Не знаю."
    show el grin pioneer close as d_el with dspr
    el "Сейчас провожу тебя до библиотеки и проверю."
    hide d_mz
    hide d_el
    with dissolve
    show dct_ext_library_rain behind dct_int_dining_hall_people_rain
    show dct_int_dining_hall_people_rain:
        pause 0.3
        linear 1 xcenter 1.5
    "Они забрали у Семёна накидки и, стараясь передвигаться по поребрику, чтобы не намочить ноги, побежали под дождём в библиотеку."

    scene dct_int_library_rain
    show d_el rain mirror:
        xcenter 0.6
    show mz shy pioneer:
        xcenter 0.4
    with blinds
    el "Женя, у меня в кружке сегодня опыт важный, я побежал!"
    hide d_el with dissolve
    "После этого Женя десять раз поправила на нём капюшон накидки, прежде чем выпустить из помещения библиотеки."
    hide mz with dissolve
    "Потом следила за ним в окно и махала рукой, пока он не скрылся за поворотом аллеи."
    show dct_int_library_rain_lamp:
        alpha 0
        pause 1.5
        linear 0.25 alpha 1
    "И вот, после того, как Сергей убежал наконец в свой кружок, Женя включила настольную лампу и, выбрав книжку, соответствующую настроению — романтическую и тёплую, устроилась за столом, забравшись с ногами на стул."
    "Пролистала пару страниц, подняла глаза на зеркало, но под этим углом отражения своего не увидела."
    mz "Я хочу сказать, Евгения, что вы определённо влюблены.{w} Это замечательно, но если бы не ваша мнительность, вы бы не потеряли целую неделю так бездарно."
    $ persistent.sprite_time = "night"  # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Улыбнулась своим мыслям и продолжила чтение под шум дождя."
    $ persistent.sprite_time = "day"
    show d_mz hope pioneer close at fleft with dissolve
    th "И как там Серёжа? Не промок ли, пока бежал в свой кружок?"
    show d_mz sceptic pioneer close at fleft with dspr
    th "Надо будет, чтобы он телефон сюда провёл. Из кружка в библиотеку."
    show d_mz smile pioneer close at fleft with dissolve_fast
    th "Тогда в следующий раз я буду знать, что с ним всё в порядке."
    stop music fadeout 1

    scene dct_int_house_of_el_day with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    play sound dct_sfx_horn_rise_through_loudspeaker
    pause 3
    show d_el laugh nude far at right with dissolve
    show d_el laugh shorts at cright with dissolve
    show el laugh pioneer close at center as d_el with dissolve
    hide d_el with dissolve
    play sound2 sfx_close_door_campus_1
    "Сыроежкин убежал, едва протрубили подъём."
    show sh normal_serious pioneer dct with dissolve
    play sound2 sfx_bed_squeak2
    "Шурик встал, вспомнил о договорённости с Мику."
    show sh smile pioneer close with dissolve_fast
    "Порадовался тому, что не придётся ничего говорить соседу."
    hide sh with dissolve
    "И для начала отправился к умывальникам."
    stop ambience fadeout 1
    stop sound fadeout 1

    scene dct_dormitory_at_range
    show black
    with squares
    play music music_list['you_won_t_let_me_down'] fadein 1
    show black:
        linear 1 alpha 0
    $ set_mode_nvl()
    window show
    "Александр Трофимов-оригинал, заведующий лабораторией спецавтоматики, стоял у общежития, кутаясь в чёрное пальто от стылого, тянущего со стороны полигона ветра, и ждал машину.{w} Хотелось закурить, но, по закону подлости, как только закуришь, машина обязательно подойдёт, а курить в кузове Александр почему-то стеснялся."
    "\nМашины всё не было, Александр уже собрался сунуть руку за сигаретами в карман, когда за углом загудело и со стороны центральной улицы городка выкатилась колонна из трёх Уралов и двух БТР."
    show dct_dormitory_at_range_Ural_BTR with dissolve
    extend " Знакомый уже майор узнал Александра, махнул рукой, крикнув: «В третью машину!», и открыл планшет, чтобы поставить там ещё одну галочку.{w} Александр подхватил зажатый между ног портфель, подбежал к Уралу, кивнув прапорщику, сидящему рядом с водителем, и, откинув полог тента, полез в кузов.{w} Его подхватили несколько рук, приняли портфель, помогли забраться самому, устроили на одной из поперечных лавок."

    scene dct_convoy_of_trucks with dissolve
    "Урал дёрнулся и покатил по улицам городка."
    "\nАлександр огляделся, поздоровался. Вокруг сидели более-менее знакомые люди, командировочные и гражданский персонал полигона — инженеры из почтовых ящиков, ремонтники, научные сотрудники различных номерных НИИ, пара учительниц из местной школы, в том числе классная руководительница дочери."
    "\nУрал куда-то ехал, поворачивая в несколько приёмов на узких улочках.{w} Потом — короткая остановка, полог открыли, и в кузов заглянул дежурный по КПП. Пробежал глазами по пассажирам и исчез, скрытый упавшим пологом.{w} Александр услышал: «Проезжайте», и колонна, медленно набирая скорость, покатила в сторону аэродрома."
    show black:
        alpha 0
        linear 1 alpha 1
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "А потом — резкое торможение и тишина.{w} Только приглушённые голоса снаружи, в которых угадывались попытки связаться по рации.{w} Пассажиры Урала, выждав несколько минут, полезли наружу, полез и Александр."
    show dct_road_bus_BTR:
        alpha 0
        pause 1
        linear 1.5 alpha 1
    "\nИ первое, что он увидел, был зад знакомого автобуса, торчащий из кювета.{w} Тут же стоял подбитый БТР, около которого кто-то бинтовал кого-то. Но это было неважно, потому что на пассажирах автобуса не было ни царапинки, но и живых среди них тоже не было."
    show dct_road_bus_BTR:
        linear 1.0 alpha 0
    extend " Некоторые ещё дышали, но это ненадолго."
    $ renpy.music.set_volume(0.0, delay=1)
    window auto

    scene bg ext_washstand2_day with squares
    play sound_loop sfx_water_sink_stream fadein 1
    $ set_mode_adv()
    mi "Сашечка, доброе утро! Ты идёшь в кружок?"

    scene bg ext_washstand_day with dissolve
    "Шурик вздрогнул, непонимающим взглядом обвёл умывальники."
    show mi serious pioneer far at left:
        alpha 0
        linear 1 alpha 1
    extend " Сфокусировался на Мику."
    th "Как я здесь оказался?"
    sh "Да-да, конечно."

    scene bg ext_washstand2_day with dissolve
    sh "Сейчас, только занесу полотенце."
    play sound sfx_close_water_sink
    stop sound_loop

    scene black with squares
    $ renpy.music.set_volume(1.0, delay=1)
    $ set_mode_nvl()
    window show
    "Когда начали изучать первых двойников, когда начали изучать их оригиналов, обнаружили в мозгу — сперва у людей-копий, потом у высокоинтеллектуальных животных, а потом и всех людей — некую область, отвечающую за его личное «я». Своего рода маяк-идентификатор.{w} И в недрах института Глафиры Денисовны возникла теория, одним из пунктов которой было так называемое нейтринное кольцо.{w} Считалось, что таких колец существует бесконечно много, и каждой человеческой или не человеческой личности соответствует одно кольцо.{w} Как только личность возникала, сразу же начинал работать такой маяк, сразу же устанавливалась связь между ним и свободным на тот момент кольцом."
    "\nПессимисты утверждали, что это не более чем математическая конструкция: мол, где вы видели нейтрино вживую, да ещё и в составе кольца из себе подобных?{w} Мистики, всегда имеющиеся в подобных учреждениях, считали кольцо доказательством существования души, Бога, богов, переселения душ — в зависимости от исповедуемого учения.{w} А с точки зрения энтузиастов науки, такие кольца действительно существовали в некой сопряжённой с нашей вселенной с иными физическими свойствами, и связь между вселенными осуществляется через пространственные вакуоли, подобные тем, где находились пионерский лагерь «Совёнок» или посёлок Шлюз, и принадлежащие одновременно обеим вселенным."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "Как бы то ни было, но теория работала.{w} Находясь внутри вакуоли, можно было скопировать такое кольцо, и тогда в вакуоли появлялось несколько организмов-копий, можно было воздействовать на кольцо, изменяя характеристики организма, а можно было разорвать связь кольца и организма. Организм при этом прекращал функционировать, мгновенно и безболезненно."
    "\nТо, что создавалось в лаборатории Александра и испытывалось на полигоне, как раз и разрывало такую связь, создавая при этом временную вакуоль прямо внутри нашего пространства.{w} Из этой штуки и выстрелили по автобусу.{w} Целились в БТР, с тем, чтобы пассажиров автобуса захватить в заложники, а попали в автобус. Просто временная вакуоль образовалась вокруг объекта с наибольшим числом организмов.{w} То, что нападавшие были уничтожены огнём из БТР, Александру было уже всё равно."
    $ renpy.music.set_volume(0.0, delay=1)
    window auto

    scene dct_ext_house_of_el_day with squares
    play ambience ambience_camp_center_day fadein 1
    $ set_mode_adv()
    "Холодная вода привела ненадолго Шурика в чувство. Ровно настолько, чтобы он умылся и дошёл до домика."
    stop ambience fadeout 1

    scene black with squares
    $ renpy.music.set_volume(1.0, delay=1)
    $ set_mode_nvl()
    window show
    "Дальнейшие события дня в памяти Александра сохранились плохо, отрывками.{w} Вот он лезет внутрь автобуса, вот он берёт из руки Яны-младшей бумажку с номером телефона, вот он сидит на асфальте перед автобусом, а вот он уже в салоне самолёта."
    "\nВ институте к трагедии Александра отнеслись с пониманием и не тревожили.{w} Все хлопоты по сворачиванию лаборатории и подготовке к эвакуации взял на себя его заместитель, а Александр сидел, заперевшись у себя в кабинете, и только рассматривал фотографию жены и дочери. Хотел убить себя, но никак не мог решиться."
    "\nПоэтому, когда случился пожар на маяке, Александр сознательно полез тушить, невзирая на очевидную опасность, и не ошибся. Ожоги, отравление газами, выделяемыми горящим пластиком.{w} Ему оставалось жить не более двух суток, когда Виола решилась и вот так, впервые, не считая себя самой, на практике создала настоящие организмы-подлинники: Александра и Анатолия, тоже пострадавшего при пожаре."
    stop music fadeout 1
    window auto

    scene black with dissolve

    scene dct_mi_morning_house with blinds
    play ambience ambience_int_cabin_day fadein 1
    $ set_mode_adv()
    "Мику, проснувшись, сразу вспомнила об окончании вчерашнего вечера."
    "О Шурике, испачканном, взъерошенном и не понимающем, куда он попал, выпавшем на неё из кустов, когда Мику запирала здание музыкального кружка.{w} О совершенно материнском желании этого Шурика умыть и почистить.{w} О визите в кружок кибернетики и загадочной установке, стоящей в центре кладовки и занимающей почти всё свободное место."

    scene dct_int_house_of_mi_day
    show mi upset pioneer close
    with dissolve
    play sound sfx_bed_squeak2
    "А потом всплыл в памяти недавний сон."
    stop ambience fadeout 1

    scene dct_ext_cliff_day_zoom
    show dct_ext_cliff_day_boat_bow
    show dct_dream_veil at shiver
    with fade
    play music music_list['tried_to_bring_it_back'] fadein 1
    "Журчащая за бортом лодки вода"
    show dct_railway_embankment_overcast behind dct_dream_veil:
        alpha 0
        linear 1 alpha 1
    extend " и надвигающаяся громада дамбы на фоне чёрной тучи"
    show dct_int_train_day behind dct_dream_veil:
        alpha 0
        linear 1 alpha 1
    extend ", пустой общий вагон, по которому сквозняк гоняет какие-то бумажки"
    show dct_int_410bus_night behind dct_dream_veil:
        alpha 0
        linear 1 alpha 1
    extend ", промороженный автобус"
    show dct_intro_xx behind dct_dream_veil:
        alpha 0
        linear 1 alpha 1
    extend ", зимний город, где она никогда не бывала"
    show dct_int_cafe behind dct_dream_veil:
        alpha 0
        linear 0.8 alpha 1
    show dct_cof behind dct_dream_veil:
        alpha 0
        pause 1.2
        linear 0.7 alpha 1
    extend ", уютная кофейня и чашка ароматного горячего кофе"
    show dct_life_line_fin behind dct_dream_veil:
        alpha 0
        linear 1 alpha 1
    extend ", спутник, на лицо которого нельзя смотреть."

    scene white
    show d_sf normal pioneer at cleft:
        zoom 1.25 ycenter 0.74
    show d_us normal dress at cright:
        zoom 1.25 ycenter 1.04
    with fade
    $ persistent.sprite_time = "day"      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "И непонятное желание заботиться о Семёне с Ульяной, оберегать их от всего плохого."

    scene black with dissolve_fast
    $ persistent.sprite_time = "night"

    scene dct_ext_musclub_night_lantern_light
    show sh upset pioneer
    with dissolve_fast
    "И как-то интуитивно почувствовав, что завтра будет поздно, уговорить Шурика на эксперимент: «Сашечка, ну пожалуйста, пожалуйста, пожалуйста, мне это очень важно, и именно сегодня, сейчас!»."
    stop music fadeout 1

    scene black with dissolve
    $ persistent.sprite_time = "day"

    scene bg ext_clubs_day
    show mi dontlike pioneer far
    with blinds
    play sound_loop ambience_camp_center_day fadein 1
    "И вот сейчас Мику, обогнав Шурика, стояла возле крыльца клубов, нетерпеливо притоптывая левой ногой."
    show sh normal pioneer far at right with MoveTransition(1.5, enter=_moveright, enter_time_warp=_ease_time_warp)
    "Что-то изменилось в нём за ночь, что-то появилось ещё, что иногда диссонировало с образом рассеянного учёного, а что именно — Мику пока понять не могла."
    show mi normal pioneer far with dissolve_fast
    sh "Доброе утро, Мику."
    show mi upset pioneer far with dissolve_fast
    show sh serious pioneer far
    with dspr
    mi "Доброе утро ещё раз, Сашечка. С тобой всё в порядке?"
    show sh surprise pioneer far with dspr
    sh "Что? А, да, конечно."
    show mi normal pioneer far with dspr
    stop sound_loop fadeout 1

    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day with slidedown
    play ambience ambience_int_cabin_day fadein 1
    "В кружке ничего не изменилось. Сразу бросились в глаза оставленные вчера Шуриком около раковины полотенце и мыло."

    scene dct_clubs_male_comp_day
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1
    "Шурик скинул со стула стопку каких-то чертежей, сел перед монитором и начал набивать на клавиатуре последовательность команд, читая появляющиеся ответы и удовлетворённо кивая или морщась в зависимости от отклика."
    stop sound_loop fadeout 1

    scene dct_ext_laboratory_of_d_sh
    show dct_d_sh_in_lab_window
    show black
    with squares
    play music homeworldcollapse fadein 1
    $ set_mode_nvl()
    window show
    "Александр Трофимов-подлинник на второй цикл окреп настолько, что Виола отпустила его из медпункта."
    show black:
        linear 1 alpha 0
    extend " Он сидел в трёхэтажном модуле, в своей бывшей лаборатории, и смотрел, как на площади у ног истукана совещается о чём-то весь оставшийся персонал института: Глафира Денисовна, Виола-подлинник, Анатолий-подлинник и Семён Персунов-дубликат.{w} Последний официально не относился к персоналу, но каким-то образом сумел влиться в остатки коллектива — может быть, как активный представитель бесчисленных пассивных миксов и копий, населявших узлы Сети.{w} Александра это особо не интересовало, Александр занимался исключительно личными делами."
    "\nКогда галлюцинации — побочные эффекты переноса сознания и фантомные боли, наследство умершего старого тела — прошли, когда прошёл психологический шок и Александр примирился со своим новым статусом, он вернулся мыслями к своей погибшей семье.{w} Новый же статус подсказал ему и выход. То, что считал неприемлемым для себя оригинал, казалось возможным для подлинника. Александр решил воссоздать одну из Ян."
    hide dct_d_sh_in_lab_window with dissolve
    "\nИ вот, пока остальные четверо переводили Сеть в автономный режим функционирования, пока корректировали систему циклов, пока изменяли топологию Сети, оставив непосредственный доступ к Шлюзу только из двух узлов, Александр творил.{w} Нужно было: создать компактное электронное устройство, излучающее сигналы, похожие на ряд сигналов человеческого мозга;{w} разработать конструкцию робота и заучить её наизусть;{w} закинуть в первый узел Сети необходимые для строительства робота материалы;"
    show black:
        linear 1 alpha 1
    extend " продумать и запрограммировать техническую личность-копию — Шурика Трофимова."
    $ renpy.music.set_volume(0.0, delay=1)
    window auto

    scene dct_clubs_male_comp_day
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with squares
    play ambience ambience_int_cabin_day fadein 1
    play sound_loop sfx_computer_noise fadein 1
    $ set_mode_adv()
    sh "Мику, садись на моё место. Сейчас я выйду, и ты нажмёшь вот эту кнопку."
    sh "Что ты увидишь — я не знаю. Какие-то подсказки для твоей памяти."
    mi "Я поняла. Спасибо, Сашечка. Ты что, куришь?"
    sh "Сегодня — да, Мику."
    "Шурик, не скрываясь, открыл и закрыл тайник с сигаретами."
    sh "Так надо."
    stop ambience fadeout 1
    stop sound_loop fadeout 1

    scene bg int_mine_coalface
    show black
    with squares
    $ renpy.music.set_volume(1.0, delay=1)
    show black:
        linear 1 alpha 0
    $ set_mode_nvl()
    window show
    "Действуя по своему плану, Александр заложил в первом узле, в пещере, это самое электронное устройство — как он его однажды назвал, «ловушка для души».{w} Вся задача этого устройства состояла в том, чтобы, имитируя человеческий мозг, привязать к себе нейтринное кольцо.{w} Практически вероятность этого события была минимальной, и ждать предстояло долго."

    scene white
    show adl_sh glasses scared at center:
        ycenter 0.528
    with dissolve
    show adl_sh glasses scared at center:
        ycenter 0.528
        pause 0.5
        alpha 0
        pause 0.1
        alpha 1
        pause 0.5
        alpha 0
        pause 0.2
        alpha 1
        pause 0.4
        alpha 0
        pause 0.3
        alpha 1
        pause 0.3
        alpha 0
        pause 0.4
        alpha 1
        pause 0.2
        alpha 0
        pause 0.5
        alpha 1
        pause 0.1
        alpha 0
    show 3500_sh normal_smile pioneer at center:
        zoom 0.88 ycenter 0.815 alpha 0
        pause 1.8
        alpha 1
        pause 0.1
        alpha 0
        pause 0.5
        alpha 1
        pause 0.2
        alpha 0
        pause 0.4
        alpha 1
        pause 0.3
        alpha 0
        pause 0.3
        alpha 1
        pause 0.4
        alpha 0
        pause 0.2
        alpha 1
        pause 0.5
        alpha 0
        pause 0.1
        alpha 1
    show ext_square_day behind adl_sh:
        alpha 0
        pause 5.0
        linear 1 alpha 1
    "\nЧтобы не тратить время на ожидание, Александр потребовал заглушить своё сознание выключателем и жил в своём узле в виде Шурика — такого же, как и все его копии в прочих узлах."
    show int_mine_coalface behind adl_sh
    show 3500_sh serious pioneer
    with dissolve
    extend " Но на одиннадцатый день двухнедельного цикла сознание возвращалось к Александру, и он спускался вниз, в пещеру, к своему прибору, проверяя, не сработала ли ловушка.{w} Что при этом происходило с его копиями в других узлах — Александра не интересовало: эгоизм тоже является движущей силой Вселенной наравне с любовью, страхом и ленью."
    show 3500_sh normal pioneer with dspr
    "\nИ вот в первый цикл пребывания Семёна в лагере бабы Глаши Александр обнаружил, что ловушка сработала."
    hide 3500_sh with dissolve
    extend " Ещё цикл ушёл на создание робота."

    scene black
    show ext_clubs_day:
        zoom 1.1
    show sh cry pioneer:
        xalign 0.3
    show d_jn:
        xalign 0.5 yalign 0.1
    with dissolve
    extend " На одиннадцатый день второго цикла Семёна Александр, вставив в робота сработавшую ловушку, отпустил его и стал ждать результатов."
    hide ext_clubs_day
    hide sh
    with dissolve
    show d_jn:
        linear 2 zoom 1.5 ycenter 0.6
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "\nРобот должен был уехать на автобусе в Шлюз и там остаться."
    show dct_fog:
        alpha 0
        linear 1.5 alpha 1
    extend " Опять же на одиннадцатый день цикла вокруг посёлка возникал туман — видимый результат взаимодействия двух вселенных. Робот должен был пройти сквозь туман, нейтринное кольцо, пойманное прибором-ловушкой, должно было клонироваться, и из тумана к роботу должен был шагнуть новый стерильный организм."
    show d_jn with Dissolve(0.0):
        linear 1 zoom 1.0 ycenter 0.9
    hide dct_fog
    show d_jn_old smile behind d_jn:
        zoom 1 xcenter 0.3 ycenter 0.73
    show d_jn_young normal behind d_jn:
        zoom 1 xcenter 0.7 ycenter 0.73
    with dissolve
    "\nНа этом судьба робота как временной технической личности должна была завершиться.{w} Робот, обнимая стерильный организм, превращался в антенну, принимающую всё, что осталось от обеих Ян в инфосфере Сети, транслируя это новому организму, тем самым формируя его «я». Выполнив свою задачу, робот отключался."
    show d_jn:
        linear 1 alpha 0
    show d_jn_old smile:
        pause 0.6
        linear 0.6 alpha 0
        pause 2.1
        linear 0.6 alpha 1
        pause 0.9
        repeat
    show d_jn_young normal:
        pause 0.9
        linear 0.6 alpha 1
        pause 1.5
        linear 0.6 alpha 0
        pause 1.2
        repeat
    extend " Похожим образом создавались миксы, только там записывались те или иные таланты и навыки организма, а не его личность, личность возникала по принципу «как получится». Похожим образом создавались подлинники, только там личность транслировалась непосредственно от оригинала.{w} «Воскреснуть» после контакта с роботом могла только одна Яна: или жена, или дочь. Кто именно — определял случай, Александр был согласен на любой вариант."
    show d_jn_old smile:
        linear 1.5 alpha 0
    show d_jn_young normal:
        linear 1.5 alpha 0
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "Но Александр был гением."

    scene dct_int_datacenter with dissolve:
        ycenter 0.5
    extend " Понимая, что маленький робот не сможет таскать на себе развитый мозг, он сумел выделить внутри вроде бы абсолютно защищённой Системы независимую и невидимую Системой область, обсчитывающую поведение робота, чем наделил кошкоробота Яну избыточными мощностями.{w} Наличие собственного нейтринного кольца сделало из неё личность, а возможность пользоваться вычислительными ресурсами системы подарила интеллект."

    scene bg ext_playground_day
    show d_sf smile pioneer:
        xcenter 0.43 ypos 0.065
    show d_jn:
        xcenter 0.58 yalign 0.1
    with dissolve
    "\nИ ещё кошкоробот Яна по-своему, но подружилась с Семёном.{w} Всё это привело к тому, что записанная в памяти робота программа действий оказалась стёртой, кошкоробот получил свободу воли и уехал обратно в родной лагерь вместе с физруком, а Яна-человек, понятно, так и не появилась."

    scene dct_int_clubs_male_night_light_mon
    show sh cry pioneer close at left
    with dissolve
    "\nРесурсов, чтобы повторить попытку, у Александра не было."

    scene dct_int_clubs_male_night with dissolve
    show black:
        alpha 0
        pause 2
        linear 1 alpha 1
    extend " После этого ему только и оставалось, что убивать себя каждый цикл в надежде, что в Шурике активируется его собственная, Шурика, личность, которая навсегда сотрёт Александра."
    stop music fadeout 1
    window auto

    scene bg ext_clubs_day:
        zoom 2.8 xcenter 0.5 ycenter 0.62
    show sh serious pioneer far:
        zoom 0.8 xcenter 0.75 ycenter 0.87
    with squares
    play ambience ambience_camp_center_day fadein 1
    $ set_mode_adv()
    "Шурик сидел на крыльце клубов и курил. Маловероятно, что сейчас его кто-то поймает с сигаретой, да и наплевать ему было на всё."
    "Приступы чужих воспоминаний накатывали волнами, почти полностью при этом подавляя его личность."
    dreamgirl "Вот теперь ты знаешь всё."
    show sh normal pioneer far with dspr
    dreamgirl "Я надеялся, что ты активируешься, тогда бы ушёл спокойно — ты бы нашёл применение моим знаниям."
    dreamgirl "А сейчас я не уверен, что ты перейдёшь в следующий цикл, не отключившись."
    dreamgirl "Но ты, читая, стёр мою память, перезаписав её себе. То, что я ещё функционирую — это инерция, это скоро пройдёт, как только ты ляжешь спать."
    show sh surprise pioneer far with dspr
    dreamgirl "Спроси Семёна, как это выглядит изнутри и снаружи — он видел и сам участвовал в таком со всех трёх сторон баррикады."
    show sh scared pioneer far with dissolve_fast
    sh "Александр? Подожди!"
    show sh upset pioneer far with dspr
    dreamgirl "Ты теперь единственный Александр, и других нет."
    "И с каким-то щелчком незримый собеседник исчез."
    show sh cry pioneer far with dissolve_fast
    "Болело сердце."
    play sound sfx_close_door_1
    show mi cry pioneer far with dissolve:
        zoom 0.8 xcenter 0.5 yalign 1.0
    show sh serious pioneer far with dissolve_fast
    "Хлопнула за спиной дверь. Из клубов, придерживаясь за ручку двери, вышла плачущая Мику."
    show sh serious pioneer far:
        linear 0.5 yalign 1.0
    mi "Ничего, цирковая обезьянка Мику — она сильная, она справится."
    show sh normal pioneer far:
        ease 1.0 xcenter 0.58
    "Мику пошатнулась, и Шурик (или Александр?) подхватил её, не давая упасть."
    show mi upset pioneer far with dissolve_fast
    sh "Ты тоже вспомнила то, что нельзя было вспоминать?"
    show sh normal pioneer far:
        linear 0.5 xcenter 0.6 ycenter 0.87
    show mi upset pioneer far:
        linear 0.5 xcenter 0.48 ycenter 0.85
    "Они осторожно присели на верхнюю ступеньку крыльца."
    mi "Сашечка, скажи. Серёжа — он уже записывал свою память на твоей машине?"
    "Мику не ответила прямо. Но и такого ответа было достаточно."
    sh "Нет. Собирались после завтрака."
    show mi sad pioneer far with dissolve_fast
    mi "Это хорошо, Сашечка. Потому что эта ваша машина — она не должна существовать."
    show sh serious pioneer far with dspr
    $ persistent.sprite_time = "day"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    sh "Да. Я всё сделаю прямо сейчас, не беспокойся."
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ persistent.sprite_time = "night"

    scene dct_int_clubs_male_rain with dissolve_fast
    play music music_list['afterword'] fadein 1
    pause 0.3
    show el serious pioneer close at right with dissolve
    el "Ты готов, Шурик?"
    sh "Давно уже.{w=0.5} Включай, да начнём запись."
    show el laugh pioneer close with dspr
    el "Шурик, а ты знаешь, что Женя…"
    sh "И что же она?"

    scene dct_int_clubs_male2_night_zoom with slideleft
    el "Включаю. Отсчёт по команде «ноль». Три, два, один. Ноль!"
    "А в лабораторном журнале кружка добавилась запись: «10-05, начало эксперимента. Первая в истории запись памяти человека! Испытуемый — Александр Трофимов, оператор — Сергей Сыроежкин»."

    scene dct_int_clubs_male_rain
    show d_el think2 pioneer as el at cleft
    with dissolve
    "А пока Шурик совершал свой десятиминутный оборот, пока на экране осциллографа электронный луч рисовал вместо окружности диковинные кривые, символизирующие запутанность процесса мышления, Сыроежкин с тоской поглядывал то на часы, то на входную дверь и думал:"
    show el smile pioneer with dspr
    th "Как хорошо, что сейчас запишем, а программа расшифрует без нашего участия."
    th "Как хорошо, что я сразу побегу в библиотеку."
    show el normal pioneer with dspr
    th "Надо бы телефон в кружок провести, а то завтра засядем за анализ результатов, а я буду беспокоиться, как там Женя?"

    scene dct_int_clubs_male_rain
    show d_el think2 pioneer as el at cleft
    with fade
    "Жужжал привод табуретки, дождь своими каплями колотил по стёклам, шуршал видеомагнитофон."
    "Электроник скучал, глядя в окно туда, где на противоположном конце лагеря располагалась библиотека, и ждал, когда пискнет десятиминутный таймер."
    th "Ещё шесть минут"
    extend ", пять с половиной"
    extend ", пять…"
    play sound sfx_door_bell

    scene dct_sh_in_cage
    show dct_el_in_cage:
        alpha 0
        pause 4
        linear 1 alpha 1
    with squares
    "В отмеренный срок Сергей выключил установку, поменял в видеомагнитофоне кассету, внёс новую запись в лабораторный журнал и сам полез внутрь установки."

    scene dct_int_clubs_male_rain
    show sh cry pioneer close
    with dissolve
    sh "Сергей, ты готов?"
    $ persistent.sprite_time = "night"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Что-то c Шуриком не так."

    scene dct_int_clubs_male2_night_zoom with dissolve
    $ persistent.sprite_time = "day"
    th "Отсутствие энтузиазма?"
    extend " Нет, не может быть! Шурик же настоящий стальной фанатик науки."
    th "Он даже на наши отношения с Женей смотрел с той точки зрения, чтобы они не мешали занятиям в кружке."
    extend " И всё же что-то не так."
    show sh serious pioneer with dissolve
    "Эта мысль мелькнула и исчезла, Электроник принял устойчивую позу на табурете."
    el "Готов!"
    show sh normal pioneer with dspr
    sh "Три, два, один. Ноль!"

    scene dct_el_in_cage with squares
    "И стена с окном медленно поползла слева направо, а шкаф начал вплывать в поле зрения."
    "Предстояло самое трудное: усидеть десять минут, не думая о Жене. Вообще ни о чём не думая, но главное — о Жене."

    scene white with dissolve
    "Электроник прикрыл глаза и представил перед собой белую, слабо светящуюся стену, за которой остался весь внешний мир."
    show mz normal pioneer close:
        zoom 1.2 xcenter 0.48 yalign 1.0 alpha 0
        linear 0.5 alpha 0.2
    th "Женя…"
    show mz normal pioneer close:
        alpha 0.2
        linear 0.5 alpha 0.0
    extend " Нет, прости, Женя, но наука иногда требует самоотречения."
    show mz smile pioneer close:
        alpha 0
        linear 0.5 alpha 0.2
    extend " Женя…"
    show black with dissolve
    hide mz
    pause 0.5
    play sound sfx_door_bell
    hide black with dissolve
    "Прозвенел таймер, десять минут пытки безмыслием истекли."

    scene dct_int_clubs_male2_night_zoom
    show el laugh pioneer at right
    with dissolve
    $ persistent.sprite_time = "day"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Табурет прекратил вращаться, Сергей открыл глаза и полез из клетки наружу."
    hide el with dissolve
    $ persistent.sprite_time = "night"

    scene dct_int_clubs_male_rain
    show sh serious pioneer close:
        xcenter 0.7 ycenter 0.7
    with dissolve
    "Шурик уже отключал приборы и подключал видеомагнитофон к компьютеру."
    show sh normal pioneer close with dspr
    sh "Ну, кого первого дешифруем?"
    show el normal pioneer close at left with dissolve
    el "Шурик, как хочешь, давай тебя. Или меня — мне всё равно."
    show sh serious pioneer close with dspr
    sh "Хорошо, тогда меня."
    show sh normal pioneer close with dspr
    sh "Сейчас одиннадцать, раньше пяти вечера ничего не будет, можешь заниматься своими делами."
    show sh serious pioneer close with dspr
    sh "А мне неохота в такой дождь лишний раз по улице бегать, я здесь поработаю."
    show el smile pioneer close with dspr:
        pause 2.5
        linear 1 alpha 0
    "Сыроежкин благодарно кивнул, снял с вешалки накидку, подошёл к двери и выглянул сквозь стекло на улицу."
    stop music fadeout 2

    scene dct_ext_clubs_rain
    show dct_ext_clubs_rain_el_in_window as d_el
    show dct_overcast_rain_2
    with dissolve # Здесь никто не выходит, поэтому не слайдим сцену, а дизолвим
    play sound_loop dct_ambience_light_rain fadein 1
    "Дождь разошёлся не на шутку: напротив крыльца на всю ширину главной аллеи, от поребрика до поребрика, разлилась лужа, вся в жёлтых разводах пыльцы."
    "Крупные дождевые капли выбивали пузыри на её поверхности. Вода достаточно быстро текла в сторону стоянки, чтобы там уйти в кюветы и через дренажные канавы и овраг попасть в реку где-то между старым лагерем и Периметром."
    "Сыроежкин посмотрел на лужу, потом посмотрел на свои ноги в свежевысушенных носках, обутые в дырявые сандалии."
    play sound sfx_close_door_1
    show d_el rain behind dct_overcast_rain_2 with dissolve:
        xcenter 0.6
    "После чего разулся, снял носки, засунув их поглубже в карман шорт, открыл дверь и, держа сандалии в одной руке, а другой придерживая накидку, сбежал с крыльца прямо в лужу."
    play sound "<from 2.4>" + dct_sfx_steps_in_swamp
    hide d_el with MoveTransition(1.0, leave=_moveright, leave_time_warp=_ease_time_warp)
    stop sound fadeout 2.5
    $ day_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Женя, я уже бегу, ставь чайник!"
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    
    
    
#################
#Глава 8. Замена#
#################

label dct_replacement_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Замена"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава VIII. Замена" at truecenter with dspr
    play ambience dct_ambience_volley_in_gym fadein 2
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_sporthall with dissolve
    pause 0.5
    show d_sf normal sport at cleft:
        zoom 1.25 ycenter 0.84 alpha 0
        linear 0.2 alpha 1
    me "Ап-чхи!"
    show d_us normal sport:
        zoom 1.25 xcenter 1.25 ycenter 1.1
        easein 0.5 xcenter 0.95 ycenter 1.09 rotate -15.0
    us "Будь здоров, Сёмк!"
    show d_us normal sport:
        zoom 1.25 xcenter 0.95 ycenter 1.09 rotate -15.0
        easein 0.5 xcenter 1.25 ycenter 1.1 rotate 0.0
    show d_sf smile sport with dspr
    me "Спасибо."
    show d_sf sad sport with dspr
    extend " Ап-чхи!"
    show d_us serious sport at fright with easeinright:
        zoom 1.25 ycenter 1.1
    us "Будь здоров же."
    show d_ge:
        zoom 1.1 xcenter 0.96 ycenter 0.72
    show d_gr:
        zoom 1.09 xcenter 0.84 ycenter 0.75
    with easeinright
    th "В носу свербит, а скоро потечёт."
    us "Вот зачем под дождём бегал? Алиска бы одна справилась прекрасно."
    th "Вот-вот, и я о том же."
    th "Зачем я бегал под дождём?"
    show d_sf smile sport with dspr
    extend " Ответ: за дождевиками."
    show d_sf normal sport
    show d_us normal sport:
        pause 1.2
        easeout 0.7 xcenter 1.25
    with dspr
    show d_ge:
        pause 1.2
        easeout 0.8 xcenter 1.41
    show d_gr:
        pause 1.1
        easeout 0.9 xcenter 1.29
    "На улицу не выйти — дождь. Средний отряд оккупировал столовую, с ними там Ольга и Алиса."
    "Младший весь целиком, а не только футбольная команда, здесь, в спортзале. Половина перекидывает мячик через сетку, играя в игру, которую они считают волейболом."
    "А вторая половина окружила Ульяну и о чём-то серьёзно с ней беседует."
    th "Я даже ревную чуть."
    "Ну а старшие — те старшие, они сами по себе."
    "Но вот через час у старших собрание, где Максим — главный герой."
    me "Рыжик, ты не в курсе, где собрание будет?"
    show d_us normal sport:
        zoom 1.25 xcenter 1.25 ycenter 1.1
        easein 0.5 xcenter 0.95 ycenter 1.09 rotate -15.0
    us "У ребят? У Алисы на складе."
    us "Нас, кстати, приглашали.{w} Без права голоса."
    show d_us normal sport:
        zoom 1.25 xcenter 0.95 ycenter 1.09 rotate -15.0
        easein 0.5 xcenter 1.25 ycenter 1.1 rotate 0.0
    show d_sf serious sport with dspr
    th "Понятно, что без права голоса."
    th "Я уже давно потерял право на участие в отрядной жизни — наверное, с тех пор, как заявил свои права на Ульяну."
    extend " Или с тех пор, как Рыжик заявила свои права на меня."
    show d_sf sad sport with dspr
    th "Вот так: сохранил прекрасные отношения со всеми, даже со спящими ещё Мику и  Сашкой, даже с Женей, даже с кибернетиками. А из отряда, из компании, которая пусть изредка, но выделяет себя из общей лагерной массы, выпал."
    th "Понятно, что двадцатипятилетний заместитель руководителя лагеря по физическому воспитанию не может быть в пионерском отряде наравне с пионерами, но обидно."
    show d_sf normal sport with dspr
    th "Даже мелкие больше меня за октябрёнка держат, чем старшие — за пионера. Даже волейбол и посиделки наши с девочками теперь от случая к случаю проходят, а не каждый вечер, как раньше."
    th "У всех свои дела."
    extend " Вот могли бы собрание и здесь провести, но предпочли чаепитие у Алисы на складе."
    show d_sf serious sport with dspr
    "Дальше посидеть и посокрушаться не получается."
    stop ambience fadeout 1
    play sound dct_sfx_sveta_falls_in_gym
    show d_sf serious sport:
        pause 0.5
        linear 0.5 alpha 0
    "Одна из девочек бросается за мячом, неловко наступает, подворачивает ногу и падает, пытается встать, вскрикивает и снова падает."

    scene dct_int_sporthall
    show d_va normal:
        zoom 0.93 xcenter 0.04 yalign 0.46
    show d_sz normal pioneer:
        xcenter 0.14 yalign 0.27
    show d_sf serious sport:
        xcenter 0.3 ypos 0.2
    show d_sv sad:
        zoom 0.97 xcenter 0.444 yalign 0.21
    show d_us normal sport:
        xcenter 0.95 ypos -0.1
    show d_oz normal pioneer:
        xcenter 0.88 yalign 0.27
    show d_gr:
        zoom 0.81 xcenter 0.81 yalign 1.0
    show d_ge:
        zoom 0.88 xcenter 0.67 yalign 1.01
    with pixellate
    play music music_list['afterword'] fadein 1
    me "Больно? Давай гляну."
    "Эта мелочь развернулась в мою сторону и протягивает правую ногу, положив лодыжку мне на колени."
    th "А вот не нравится мне эта лодыжка. Растяжение — даже доктором быть для этого не обязательно, чтобы понять."
    show d_sv upset with dspr
    "Знаю, что завтра отроковица будет в полном здравии, но сейчас ей больно и она еле сдерживается, чтоб не заплакать."
    show d_sf serious sport:
        pause 0.6
        linear 1 alpha 0
    me "Больно. Вижу. Посиди здесь, я сейчас."
    show d_sf sad sport with dissolve:
        alpha 1
    "Приношу из тренерской эластичный бинт и обматываю Светкину щиколотку."
    show d_sv sad with dspr
    th "В принципе, можно больше ничего не делать до завтра — всё равно у пионеров все повреждения восстанавливаются за несколько часов."
    th "Но пионеры же об этом не знают, девочке же страшно и больно. Надо её в медпункт."
    show d_sf normal sport with dspr
    me "Ходить ты, конечно, не в состоянии."
    show d_sf smile sport
    show d_sv surprise
    with dspr
    me "Ну, хватайся крепче, понесу тебя к доктору."
    show d_sf smile sport:
        anchor (0.5, 0.0) pos (0.3, 0.2)
        linear 1 anchor (0.5, 0.0) pos (0.51, 0.0) knot (0.5, 0.2)
    show d_sf_carrying_d_sv smile:                                  # Подхватывание Светы
        alpha 0
        parallel:
            anchor (0.5, 0.0) pos (0.3, 0.2)
            linear 1 anchor (0.5, 0.0) pos (0.51, 0.0) knot (0.5, 0.2)
        parallel:
            pause 0.55
            alpha 1
    show d_sv surprise:
        pause 0.55
        alpha 0
    pause 1
    show d_sf sad sport
    show d_oz n pioneer
    with dspr
    th "Ох, спина ты моя молодая!"
    show d_sf_carrying_d_sv smile:
        xcenter 0.51
    hide d_sf_grabs_d_sv
    show d_us hurt sport with dspr
    us "Донесёшь, Сёмк?"
    show d_sf smile sport with dspr
    $ persistent.sprite_time = "day"        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    me "Куда я денусь, тут живого весу-то…"

    scene black with dissolve_fast
    $ persistent.sprite_time = "night"

    scene dct_ext_сentral_alley_from_dining_hall_to_west_after_rain
    show d_sf normal sport at left
    show d_sf_carrying_d_sv sad at left
    with dissolve_fast
    "Пока играли, пока лодыжку щупали, дождь унесло куда-то на север, и он поливает в районе той поляны, где есть переход в лагерь Виолы."
    "Осторожно несу калеку в обход столовой и через площадь к медпункту, лавируя между лужами."
    "Со спортплощадки есть прямая дорожка по задам столовой и склада, но ну её — она сейчас раскисла, и тащить по ней груз, даже такой лёгкий, как вот эта второклассница, занятие архинеприятное."
    "Вот и тучи начали расступаться, сейчас всё быстро высохнет."

    scene dct_ext_dining_hall_away_after_rain
    show d_sf normal sport at center
    show d_sf_carrying_d_sv sad at center
    with dissolve
    d_sv "Тебе не тяжело меня нести?"
    show d_sf serious sport with dspr
    "А я прямо сейчас понял, почему я так привязался к мелким. Всё дело в их безоговорочном ко мне доверии всего-навсего."
    "Я ещё держу в голове остатки фантомных воспоминаний, внушённых Системой мне, спящему дубликату."
    show d_sf sad sport with dspr
    "Так вот, в той своей фантомной биографии я не доверял никому. Вовсе."
    "И сам вот так, как они, не смог бы — просто не хватило бы сил."
    show d_sf normal sport with dspr
    "И поэтому вот такое доверие — оно в моём представлении что-то настолько ценное, что просто не может существовать."
    "Почти столь же ценное, как Ульянкина любовь ко мне.{w} Которая тоже не должна была случиться."

    scene dct_ext_square_after_rain
    show d_sf smile sport at right
    show d_sf_carrying_d_sv sad at right
    with dissolve
    me "Уж как-нибудь, мелочь, я тебя донесу."
    show d_sf_carrying_d_sv shy with dspr
    "Мелочь благодарно прижимается, насколько это возможно в её положении и состоянии."
    show d_sf sad sport with dspr
    "А вот моя спина благодарности не высказывает, моя спина высказывает свои претензии."
    show d_sf normal sport
    show d_sf_carrying_d_sv smile
    with dspr
    "Я всё-таки тормоз, Рыжик права. Надо было посадить девочку на раму, и мы прекрасно бы с ней доехали на велосипеде. Зря, что ли, мы их со склада забирали?"
    show d_sf sad sport with dspr
    "А сейчас спина будет болеть, а Ульяна ворчать."

    scene dct_ext_aidpost_after_rain with dissolve
    $ persistent.sprite_time = "night"        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Вот и медпункт.{w} Осторожно толкаю дверь."
    $ persistent.sprite_time = "day"

    play sound sfx_open_door_2
    scene bg int_aidpost_day
    with slidedown
    show dct_int_aidpost_day_curtain
    show d_cs normal far
    show d_sf normal sport at left
    show d_sv sad:
        zoom 0.97 xcenter 0.65 yalign 0.21
    with dissolve
    me "Доктор, я к вам пациента принёс."
    show d_cs normal stethoscope far:
        xcenter 0.8
    show d_sv sad:
        zoom 0.73 xcenter 0.93 ycenter 0.69
    show d_sf sad sport:
        xcenter 0.12 ypos 0.2
    with fade
    th "С прошлого цикла ничего здесь не поменялось."
    show d_sf serious sport with dspr
    th "А что и кто здесь может поменяться?{w=0.4} Докторица?"
    show d_cs smile stethoscope far
    show d_sv shock
    with dspr
    th "Вот интересно, я сам в конце концов в подобного «физрука» превращусь?"
    extend " Или скачусь назад, в пионеры?"
    show d_sf sad sport with dspr
    extend " И каково девчонкам это видеть будет?"
    "Занавеска вокруг второй кушетки была задёрнута, и кто-то иногда тихонько всхлипывал за ней, скрытый от посторонних глаз."
    show d_sf normal sport with dspr
    show d_cs normal stethoscope far with dspr
    "Я поймал взгляд доктора и кивнул головой в сторону занавески."
    show d_sv upset with dspr
    d_cs "Растяжение.{w=0.4} Семён, дальше уже моя забота."
    "Доктор сделала вид, что не поняла вопроса."
    show d_sv sad with dspr
    me "Свет, обед тебе сюда принесут, я распоряжусь. И сам зайду перед обедом."
    show d_sv smile with dspr
    show d_sf sad sport:
        linear 0.5 ypos 0.0
    pause 0.5
    "Я уже взялся за ручку двери, когда из-за занавески донёсся тихий голос:"
    show dct_int_aidpost_day_mi_behind_curtain
    show dct_int_aidpost_day_curtain ajar
    with dissolve_fast
    mi "Се… Сен-нечка, подожди меня."
    hide dct_int_aidpost_day_mi_behind_curtain
    show d_sf serious sport
    with dissolve_fast
    me "Я буду на крыльце, Мику."
    hide  d_sf with dissolve
    stop music fadeout 1

    scene bg ext_aidpost_day:
        zoom 2 xcenter 0.45 ycenter 0.4
    show d_sf normal sport:
        xcenter 0.3
    with slideawayup
    play ambience ambience_camp_center_day fadein 1
    pause 0.4
    show d_cs normal stethoscope with dissolve:
        xcenter 0.67
    me "Что с нею, доктор?"
    d_cs "Ничего заразного."
    show d_sf serious sport with dspr
    d_cs "Сами же понимаете, что я не скажу."
    d_cs "Привела её эта блондинка с косами, можете у неё спросить."
    "Они ещё постояли на крыльце, глядя на быстро высыхающий под солнцем лагерь."
    d_cs "Редко здесь такие дожди бывают."
    "Семён хотел ответить что-нибудь столь же нейтральное, но не успел."
    play sound sfx_medpunkt_door_open
    show mi sad pioneer far behind d_sf with dissolve
    mi "Простите за задержку. Я ещё с девочкой поговорила, успокоила её."
    mi "А то вы её бросили одну на кушетке, а она же маленькая."
    show mi dontlike pioneer far with dissolve_fast
    extend " Стыдно!"
                           
    scene dct_ext_square_profile_view_day
    show d_sf normal sport at center:
        xzoom -1.0
    show mi sad pioneer at right
    with dct_fade
    "Семён и Мику шли к складу длинной дорогой: опять мимо Генды, через площадь и налево по главной аллее в сторону хозворот."
    "Солнце активно сушило лагерь после помывки, асфальт уже почти везде из чёрного становился серым, и обвисшие мокрые флаги уже начинали расправляться на флагштоках, обсыхая на солнце и ветерке."
    "Воробьи вылезли из укрытий и массово принимали водные процедуры в оставшихся лужах."

    scene bg ext_square_day
    show mi upset pioneer at fright
    show d_sf normal sport at cright:
        xcenter 0.65
    with dissolve
    mi "Вот представь себе, Сенечка, лабораторию, а в ней за стеклянной перегородкой клетки с обезьянками, глупыми и шумными обезьянками.{w} Виварий."
    mi "Сотрудники ходят, разговаривают между собой, свои проблемы обсуждают. Иногда детей своих приводят, «на обезьянок посмотреть»."
    show mi sad pioneer with dissolve_fast
    mi "А всем командует там высокий, слегка сутулый дядька с серыми глазами. Лет ему за тридцать, у него каштановые волосы и борода."
    mi "И зовут этого дядьку…"
    stop ambience fadeout 1

    scene black with dissolve
    pause 0.5
    show promo_text_un u"{color=#00b4cf}Рассказ Мику{/color}" at truecenter with dspr
    play music forgotten_summer fadein 1
    $ renpy.pause(3.0)
    $ set_mode_nvl()
    window show

    scene black
    show dct_ext_сentral_alley_from_dining_hall_to_west:
        alpha 0.6
    with dissolve
    "А знаешь, как делали миксов в вашей лаборатории?"
    "\nНет-нет, Сенечка, не отвечай — я знаю, что такое миксы, я знаю, что это не твоя лаборатория, что ты не оригинал и не подлинник, я многое теперь знаю.{w} И про тебя, и вообще. Про тебя, может, даже в чём-то больше, чем ты сам про себя.{w} Машина у Шурика работает{w=0.4}, работала.{w=0.4} Он обещал её сломать, и я ему верю."
    "\nВ общем, взяли такую обезьянку, посадили её в клетку, клетку обвешали какими-то приборами и вынесли в туман. А из тумана потом к клетке шагнуло…{w} Существо?{w=0.5} Да, пусть будет существо: глупое, пустое, беспамятное и бесполое существо. Первичный организм. Оно вцепилось в клетку и хотело дотянуться до обезьянки, но не могло.{w} А его били током.{w} Как это называется?{w=0.3} Ударили неотпускающим током через прутья клетки и начали это существо «наполнять информацией» — так, кажется. Вот только когда оно, это существо — нет, уже она, девочка, осознала себя и впервые посмотрела на мир осмысленно, первое, что она увидела — это вцепившаяся с той стороны в прутья решетки мёртвая обезьянка.{w} И табличка на клетке: пол, возраст, вес, инвентарный номер и кличка: «Мику»."
    nvl hide dissolve
    nvl clear
    nvl show dissolve 
    "\nВот у вас у всех, Сенечка, были мама и папа. Пусть у ваших оригиналов, но всё равно были. А у таких, как я — только обезьянка.{w} Я не обижаюсь на твоего оригинала — это ведь была его лаборатория, если бы не он — меня бы не было на свете. Так что я считаю его своим папой. А мой оригинал — обезьянка по кличке Мику. А твой оригинал — он действительно хотел нам только добра и относился к нам, как к собственным детям. И у него всё получилось. Но обезьянку жалко.{w} А может, Сенечка, она не умерла? Может, она во мне теперь живёт? Потому что я помню теперь всё, что она видела и слышала. Все разговоры и всех людей, которые проходили мимо. Она слышала разговоры, запоминала, но не понимала.{w} А я поняла только то, что смогла, ведь я всего лишь шестнадцатилетняя пионерка, подвинутая на музыке, а не технарь, как Серёжа. И помню, как обезьянке было страшно одной в том тумане."
    "\nСенечка, я сегодня чуть с ума не сошла. Сижу в кружке у себя, пытаюсь играть — под дождь так хорошо играется, а вижу себя обезьянкой в клетке.{w} У меня истерика случилась, а Сашенька с доктором меня валерьянкой и ещё какими-то таблетками отпаивали. Поэтому я замороженная сейчас, не обращай внимания, это пройдёт.{w} А знаешь, почему я с ума не сошла? Из-за той сказки, что ты принёс. Я подумала, что если моя сестра способна творить, то, значит, и я сумею.{w} А обезьянка — нет, обезьянки творить не умеют. А ещё я за твою историю с Микусей уцепилась. Я и эту историю тоже теперь помню. Да, Микуся там, в мире наших снов, и здесь она не появится никогда, но свою память она нам подарила."
    show dct_ext_сentral_alley_from_dining_hall_to_west:
        linear 2 alpha 0
    extend " Сенечка, ведь если она была счастлива, пусть даже так коротко и такой ценой, значит, и для меня где-то запасён в мире кусочек счастья?!"
    stop music fadeout 1

    scene black with dissolve_fast
    window hide

    scene dct_ext_storage_day
    show d_sf normal sport:
        xcenter 0.2
    show mi sad pioneer at cright
    with dissolve_fast
    play ambience ambience_camp_center_day fadein 1.3
    $ set_mode_adv()
    window auto
    mi "Сенечка, я ещё хочу сказать, что я, может быть, забуду всё между циклами. Но прежней Мику, какой вы её знали в этом узле, уже не будет."
    me "Мику.{w=0.5} Куда ты денешься?{w} Ты и сейчас прежняя, только ещё не поняла этого."
    stop ambience fadeout 1
    play sound sfx_open_door_2

    scene dct_int_warehouse_day with slidedown
    play sound_loop ambience_int_cabin_day fadein 1
    "Семён наконец потянул за ручку и, пропустив Мику на склад, зашёл сам."
    "Восемь пар глаз смотрели на них. Пахло пылью, свежим постельным бельём, крепко заваренным чаем и Сашкиной выпечкой."
    show dv angry pioneer2 far at left with dissolve
    dv "Ну наконец-то."
    show dv grin pioneer2 far with dissolve_fast
    extend " Наливайте себе чай, и начинаем."
    stop sound_loop fadeout 1

    scene dct_ext_clubs_rain with dct_fade
    play music music_list['confession_oboe'] fadein 1
    "Делать Шурику было совершенно нечего.{w} Может быть, впервые за все бесчисленные циклы."

    scene bg int_clubs_male_day
    show dct_int_clubs_male_rain
    with squares
    "Он сидел в кружке, листал подшивку «Радио», не вникая в суть текста, смотрел, как компьютер пытается расшифровать абракадабру, записанную на ленте видеомагнитофона."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.95
    "Всего-то и нужно было, что поменять местами две платы, благо они внешне были совершенно одинаковые."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.9
    "Александр помалкивал. Шурик чувствовал его присутствие у себя в голове, но и только.{w} Как будто находишься в комнате, где за твоей спиной есть кто-то ещё.{w} Этот кто-то молчит и вообще старается никак не проявлять себя, но ты его чувствуешь."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.85
    th "Значит, прибор работает, то есть работал."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.8
    th "Сам сделал, сам и сломал."
    "Легко можно было всё исправить, но Шурик точно знал, что он этого делать не будет."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.75
    th "Если каждый из обитателей вспомнит что-то подобное тому, что вспомнил я…"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.7
    extend " Эта штука в масштабах Сети будет посильнее атомной бомбы."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.65
    extend " А для большинства людей, которые всё вспомнят, это просто катастрофа."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.6
    th "Александр — он бы обязательно сделал что-то подобное. Просто чтобы посмотреть, что получится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.55
    extend " Семён верно сказал в день приезда: «Какая великолепная физика!»."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.5
    th "Прежний Шурик — тот бы проделал всё ради торжества прогресса, а вот нынешний я без сожаления взял и всё уничтожил, свою Нобелевскую премию, которой тут нет."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.45
    "В голове что-то поворочалось и опять затихло."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.4
    th "Интересно, что я себя с Александром не отождествляю — просто посторонний человек, делящий со мной моё тело и подаривший мне свою память."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.35
    "Шурик выглянул в окно: дождь заканчивался, он ещё сеял россыпью мелких капель по лужам, но небо на юго-западе уже голубело, тучу явно утягивало в сторону леса."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.3
    "Делать было решительно нечего, а начинать новый проект не хотелось. Пока объяснишь Сыроежкину, почему бросаем старый, пока сам поставишь себе задачу, пока, пока, пока… Так и цикл закончится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.25
    extend " Тем более в условиях Сети ничего глобального, что имело бы перспективы, создать не получится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.2
    "Проще дождаться нового цикла, когда сбросится память, и начать с чистого листа, когда будешь верить, что ты — Шурик Трофимов, перспективный выпускник, за которого бьются пять ведущих вузов СССР, а не копия давно умершего человека, живущая двухнедельными циклами внутри пространственной вакуоли."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.15
    "А сейчас нужно подчистить следы своих манипуляций с установкой."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.1
    "Сыроежкин, конечно, сейчас видит только Женю, но парень он умный и наблюдательный."
    dreamgirl "Микс."
    th "Человек!"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.05
    th "На собрание сходить?"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0
    th "Можно и сходить, но сначала ещё одно дело. Кое-кому я сильно задолжал."
    stop music fadeout 1

    play sound ["<silence 0.5>", sfx_close_door_1]
    scene bg ext_clubs_day
    show 3500_sh normal_smile pioneer:
        zoom .18 anchor (.5, 1.0) pos (.48, .72)
    with slideawayup
    play ambience ambience_camp_center_day fadein 1
    "Шурик вышел на крыльцо. Дождь окончательно прекратился, лужа, разливавшаяся на всю ширину главной аллеи, уже стекла ручьём в реку, и сейчас асфальт быстро сох под летним солнцем."
    show 3500_sh smile pioneer with dissolve_fast
    th "Должна она появиться, должна."
    show 3500_sh normal pioneer with dissolve_fast
    th "Ограничители в моей голове сняты, сейчас здесь только я и Вселенная. И никаких дополнительных фильтров восприятия, кроме своих личных — тех, что у всех людей присутствуют."

    scene dct_ext_another_clubhouse_day with dissolve
    "Шурик вынес на улицу табурет и присел под навесом, внимательно глядя на крыльцо заброшенного здания напротив."
    th "Нужно только один раз увидеть, а дальше пойдёт само."
    stop ambience fadeout 3
    play music "<from 42.0 loop 0.0>" + twisterium_eternal_love fadein 7
    show d_jn:
       xzoom 1.8 yzoom 0.35 anchor (0.5, 1.0) pos (0.46, 0.795) blur 70 alpha 0
       easein 3 xzoom 0.21 yzoom 0.21 blur 10 alpha 1
       linear 1 blur 0
    "Воздух над крыльцом начал дрожать, а пожарный щит, закрывавший входную дверь, замерцал, затмеваемый металлическим блеском. Область металлического блеска всё сокращалась, делаясь всё более непрозрачной, пока не собралась в небольшую, ростом с пяти-шестилетнего ребенка, металлическую фигурку."
    "Потускневшая полировка панциря, исцарапанный лицевой щиток, прикрывающий фотоэлементы, кончик левого уха чуть загнут назад. Серая от микротрещин, а когда-то была чёрной, резиновая гофра на суставах."
    "Серебристая фигурка стояла абсолютно неподвижно, как умеют стоять только памятники и механизмы.{w} И в то же время Шурик ясно чувствовал, что оттуда, из-за зеркального лицевого щитка, за ним внимательно наблюдают."
    "Шурик встал с табурета, сделал несколько шагов, спустившись с крыльца на асфальт аллеи, и, присев на корточки, протянул руки навстречу механоиду. Почти как когда-то, множество циклов тому назад."
    "Что-то толкалось в груди, что-то не давало говорить ровно."
    sh "Ну здравствуй, Яна."

    ##################################################    Яна бежит к Шурику (сделано двуя попеременнми обращениями к спрайту, чтоб возникала иллюзия перехода Dissolve)
    show d_jn:
        xzoom 1.0 yzoom 1.0 zoom 0.21
        linear 0.5 alpha 0
        pause 0.2
        zoom 0.46 xcenter 0.452 ycenter 0.731
        linear 0.5 alpha 1
        pause 0.2
        linear 0.5 alpha 0
    show d_jn as d_jn2:
        zoom 0.27 xcenter 0.459 ycenter 0.66 alpha 0
        linear 0.5 alpha 1
        pause 0.2
        linear 0.5 alpha 0
        pause 0.2
        zoom 1.0 xcenter 0.435 ycenter 0.91
        linear 0.5 alpha 1
        pause 0.2
        linear 0.5 alpha 0
    ##################################################

    "Зажужжали приводы, застучали каучуковые подошвы по доскам крыльца и асфальту. Подхваченный двумя руками кошкоробот взлетел к небу и плавно опустился на землю."

    scene dct_sh_d_jn_reunion with squares
    "Корпус робота изредка подрагивал, и на эти единичные импульсы накладывалась ещё и низкочастотная вибрация."
    "Резиновые ладони обхватили ладони белковые, бывший алюминиевый бидон прижался к человеческим ногам, голова, когда-то выколоченная Сыроежкиным из металлического листа вокруг деревянной болванки, сначала уткнулась лбом в пряжку ремня, а через минуту задралась, так что в лицевом щитке отразились очки и мокрые глаза за ними."
    d_jn "Здравствуй, па!"
    stop music fadeout 1

    scene dct_int_warehouse_day
    show dv smile pioneer2 far at fleft
    show black
    show d_ma normal pioneer:
        xcenter 0.5 yalign 0.02
    with dct_fade
    play music music_list['farewell_to_the_past_full'] fadein 1
    "Несмотря на вчерашние слова Саши, что все проголосуют за него, Максим волновался."
    show d_ma serious pioneer with dissolve_fast
    "Он уже привык относить себя к старшему отряду, и если вдруг большинство проголосует против…{w} Он, конечно, переживёт, но будет обидно."
    show d_ma rage pioneer with dspr
    "А уж в среднем отряде как обрадуются. И найдутся желающие поднять свой авторитет за счёт «выскочки», обязательно найдутся."
    show d_ma angry pioneer with dspr
    extend " Разберётся, конечно, но отдых будет испорчен."
    show d_ma normal pioneer with dissolve_fast
    hide black with dissolve2
    "Сразу после завтрака Максим увязался за Алисой и почти три часа помогал ей наводить порядок на складе."
    show d_ma normal pioneer:
        easeout 1 xcenter 0.75 alpha 0
    "Во-первых, чтобы не трястись от волнения."
    hide dv with dissolve
    "Во-вторых, от Витьки, соседа по домику, всё равно никакой поддержки ждать не приходится."
    "Витька вообще в последнее время изменился. Дёрганый какой-то стал, как будто Максим ему чем-то не нравится."
    show d_ma angry pioneer with dissolve:
        zoom .75 xcenter 0.36 yalign 1.01 alpha 1
    "Вчера поздно вечером вообще чуть не подрались по непонятному поводу: Катерину Максим у Витьки уводит."
    show d_ma serious pioneer with dspr
    "Максим пожал плечами.{w} То, что лагерь маленький и Катя всё время на глаза попадается — разве Максим в этом виноват?"
    show d_ma normal pioneer with dissolve_fast
    "Кто этих влюблённых поймёт?"
    show dv grin pioneer2 close at fright:
        alpha 0
        linear 1.5 alpha 1
    show d_ma shy pioneer with dspr
    "В-третьих, из-за самой Алисы, конечно."
    show dv grin pioneer2 close at fright:
        linear 1.5 alpha 0
    extend " Особенно когда разглядел за насмешками и подколками живую девушку."
    hide d_ma with dissolve
    "И Максим три часа таскал по складу тюки с грязным бельём, пересчитывал и переписывал лампочки и банки с краской на стеллажах, раскладывал по размерам комплекты пионерской формы."
    "Ну и разговаривал с Алисой, уже без взаимных подколок, а просто с интересом слушая девушку и рассказывая о своём."
    show dv grin pioneer2 far at cright:
        alpha 1
    show d_ma normal pioneer:
        zoom .75 xcenter 0.45 yalign 1.01
    with dissolve
    "Вот только однажды случился неловкий момент. Когда после одного не очень приличного, но ужасно смешного анекдота Алиса, отсмеявшись, прокомментировала старушечьим голосом: «Ох и молодежь нонеча пошла…»."
    show dv laugh pioneer2 far
    show d_ma grin pioneer
    with dissolve_fast
    d_ma_dv "Алиса, ты ещё скажи: «Вот я в твои годы!».\nВот я, помню, в твои годы…"
    show dv sad pioneer2 far with dissolve_fast
    "Алиса неожиданно погрустнела, будто действительно что-то вспомнила, и оборвала реплику."
    show d_ma serious pioneer with dspr
    d_ma "Алиса, что-то не так?"
    show 3500_dv sadness pioneer2 as dv with dissolve_fast:
        zoom 0.75 xoffset 20
    dv "Всё так, Максим. Не обращай внимания."
    show 3500_dv normal pioneer2 as dv with dspr
    extend " Так, вспомнила одну вещь неприятную."
    hide dv with dissolve
    "А Максим сделал вывод: не провоцировать Алису на воспоминания."
    stop music fadeout 1

    scene dct_int_warehouse_day
    show sl smile2 pioneer at cright
    with dct_fade
    play ambience ambience_int_cabin_day fadein 1
    "Первой на склад прибежала Сашка, положила на стол пахнущий корицей пакет, тепло улыбнулась Максиму и поздоровалась с ним."
    show dv scared pioneer2 close behind sl:
        xcenter 0.14
    show sl scared pioneer close:
        xcenter 0.36
    with dissolve
    "А следом начала что-то на ухо говорить Алисе, Максим уловил только имя Мику."
    show dv guilty pioneer2 close with dissolve_fast
    dv "Может, к ней вернёшься, Саш?"
    show sl normal pioneer close with dissolve_fast
    sa "Нет-нет, она сама меня сюда отправила, а то Максимке тут, говорит, совсем страшно будет."
    show dv shy pioneer2 close
    show sl smile pioneer close
    with dspr
    sa "И сама она, может быть, ещё подойдёт."
    hide sl
    show dv sad pioneer2 close:
        pause 2
        linear 1 alpha 0
    with dissolve
    "Деятельная Сашка сразу кинулась наводить порядок на рабочем месте Алисы, превращая его в стол для чаепития и не обращая внимания на ворчание хозяйки."
    "Складывалось впечатление, что Алису здесь, внутри отряда, не особо-то и боятся."
    "Все журналы и пачка бланков накладных были убраны на подоконник, стол застелен миллиметровкой, отмотанной от неизвестно откуда появившегося рулона, на столе появилась тарелка, а в тарелку была высыпана из пакета горка печенья."
    hide dv
    "Тут же рядом был водружён чайник и выставлена батарея разномастных чашек."
    show sl happy pioneer with dissolve_fast
    sa "Всё, на всех хватит и никто не уйдёт обиженным!"
    hide sl with dissolve
    pause 0.7
    show un normal pioneer far at left with dissolve
    "Второй пришла Лена.{w} Тихо, на грани шёпота, поздоровалась, на мгновение показала свои зелёные глаза и опять спрятала их под ресницами."
    hide un with dissolve
    "Села около окна и принялась что-то то ли записывать, то ли зарисовывать в блокноте, потаскивая потихоньку печенье."
    show d_us smile sport at cright with dissolve:
        ypos -0.05
    "Прибежала Ульяна. Принесла охапку малышовых дождевиков."
    show d_us normal sport with dspr
    us "Сёмка чуть задержится. Светка ногу подвернула, он её в медпункт потащил."
    hide d_us
    with dissolve
    pause 0.7
    show d_el shy pioneer close:
        xcenter 0.37
    show mz shy glasses pioneer close:
        xcenter 0.20
    show dct_int_warehouse_day as sklad2:
        alpha 1
        pause 1.6
        linear 1 alpha 0
    show sh serious pioneer close at fright
    with dissolve
    "Следом пришёл Шурик, и почти сразу за ним — Сыроежкин и Женя."
    hide sh with dissolve
    "Шурик сел в углу, обвёл взглядом помещение и снял очки. Казалось, что он не очень понимает, где находится и зачем он здесь."
    hide d_el
    hide mz
    with dissolve
    "Сыроежкин и Женя как зашли, держась за руки, поздоровались, так и сели рядом, не отпуская рук."
    show d_sf normal sport at cright:
        xcenter 0.65
    show mi serious pioneer at center
    with dissolve
    pause 0.4
    show sl surprise pioneer far at fleft with dissolve
    pause 0.2
    show mi upset pioneer with dspr
    "Последними зашли Семён и Мику."
    show d_sf normal sport:
        pause 0.5
        linear 1 alpha 0
    show mi normal pioneer with dspr
    pause 0.5
    show sl normal pioneer far with dissolve_fast:
        alpha 1
        pause 1.3
        linear 1 alpha 0
    show mi serious pioneer as mi2 at center:
        alpha 0
        pause 1.6
        linear 0.2 alpha 1
    show dct_int_warehouse_day as sklad3:
        alpha 0
        pause 2.3
        linear 1 alpha 1
    "Мику обменялась взглядами с Сашкой — Сашка встревоженным, Мику успокаивающим, взглянула на Шурика, дождалась его еле заметного кивка, так же еле заметно кивнула в ответ и взялась за чайник."
    "Семён устроился рядом с Ульяной, откинувшись спиной на стеллаж, как обычно, с непроницаемым выражением лица."

    scene dct_int_warehouse_day with fade
    "Минуту все молчали, спрятавшись за чашками с чаем. Только девочки переглядывались и нервно пересмеивались. Все стеснялись начать."
    show mi dontlike pioneer close at fleft with dissolve
    mi "Ну давайте же, ребята. В первый раз для чего-то важного собрались, и все стесняемся."
    show mi shy pioneer close with dspr
    extend " Сенечка, может, ты начнёшь?"
    show d_sf sad sport at fright with dissolve:
        xzoom -1.0
    me "Мику, но я же вроде как уже не…"
    show mi scared pioneer close
    show dv angry pioneer2 far:
        xcenter 0.55
    with dissolve_fast
    dv "Что ты?"
    show d_sf serious sport
    show 3500_dv dontlike pioneer2 as dv:
        zoom 0.75 xoffset 20
    with dissolve_fast
    dv "Сенька, ты всё равно свой.{w} Пока хоть один из нас здесь присутствует — ты свой!"
    show dv angry pioneer2 far:
        zoom 1.0
    show mi shocked pioneer close
    with dissolve_fast
    dv "Кто против?"
    show un surprise pioneer far behind mi at cleft with dissolve_fast
    un "Я за."
    hide un
    show dv sad pioneer2 far
    show mi smile pioneer close
    show d_sf normal sport
    with dissolve_fast
    mi "Ну конечно, Алисочка, как же может быть иначе?"
    hide dv with dissolve
    "Мику уже оправилась от стресса и вернулась к своей обычной манере разговора."
    show d_sf smile sport with dspr
    me "Ну хорошо, опять всё свалилось на бедного меня."
    show d_sf normal sport
    hide mi smile pioneer close
    with dissolve
    "Семён отхлебнул чай."
    me "Начинаю опрос."
    show d_sf smile sport with dspr
    show sl happy pioneer close at left:
        alpha 0
        pause 0.5
        linear 1 alpha 1
    me "Ляксандра?{w=0.8} Есть что сказать?"
    show sl shy pioneer close with dspr
    "Саша покачала головой, благодарно улыбаясь Семёну."
    hide sl with dissolve
    "Что там было в памяти у этой девушки, появившейся на свет в результате сбоя вместо здешней Слави — знали только Система и она сама."
    stop ambience fadeout 1

    scene dct_int_warehouse_day with fade
    play ambience ambience_int_cabin_day fadein 1
    hide black with dissolve
    "Все, как и обещала Сашка, проголосовали «за»."
    show el grin pioneer at left with dissolve
    "Сыроежкин только попытался затащить Максима в кружок кибернетики"
    show d_ma surprise pioneer with dissolve:
        zoom 0.75 xcenter 0.55 yalign 1.01
    show d_mz facepalm glasses pioneer with dissolve:
        xcenter 0.14
    extend ", но был остановлен, к  удивлению большинства присутствующих, самим Шуриком."
    show 3500_sh normal2 noglasses pioneer glasses with dissolve:
        zoom 0.85 xcenter 0.76 ycenter 0.79
    sh "Сергей, мы здесь не за этим собрались, ты не находишь?"
    show el normal pioneer
    show d_mz smile2 glasses pioneer
    show d_ma normal pioneer
    with dissolve_fast
    extend " И ещё, зачем нам участник, которого пришлось уговаривать?"
    hide el
    hide d_mz
    hide 3500_sh
    hide d_ma
    with dissolve
    "А потом настала очередь Максима."
    show d_sf serious sport at fright behind d_ma with dissolve:
        xzoom -1.0
    me "Максим, а теперь скажи, согласен ли ты перейти в старший отряд?"
    show d_ma serious pioneer with dissolve:
        xcenter 0.5 yalign 0.02
    stop ambience fadeout 1
    play music "<from 32.5 loop 0.0>" + music_list["farewell_to_the_past_full"] fadein 1.5
    show black behind d_ma with squares
    "Вспомнились вдруг вчерашние слова Лены в пересказе Саши и сегодняшние — Алисы: «Ты думаешь, что в старшем отряде вся жизнь повидлом намазана? Ну-ну»."
    show d_ma normal pioneer with dissolve_fast
    "Что-то Алиса хотела до него донести сегодня, пока вместе наводили порядок на складе, о чём-то предупредить."
    show d_ma angry pioneer with dissolve_fast
    "Но едва она начинала говорить, как Максим переставал понимать: вроде и слова все знакомые, а смысл ускользает. Только ощущение тревоги Алисиной осталось в памяти."
    "Максим попытался вспомнить вчерашний разговор."
    show d_ma serious pioneer with dspr
    th "Как там?"
    extend " Если внутренний голос будет против, то нужно к нему прислушаться."
    $ renpy.music.set_volume(0.0, delay=1.0)
    play ambience ambience_int_cabin_day fadein 1
    hide d_sf
    show sl surprise pioneer close at left behind black
    hide black with squares
    sa "Может, дать ему время подумать?"
    show 3500_sh normal2 noglasses pioneer glasses with dissolve:
        zoom 0.85 xcenter 0.725 ycenter 0.79
    show sl surprise pioneer close:
        pause 1.2
        linear 1 alpha 0
    sh "Нет.{w=0.6} Решать он должен сейчас.{w=1.0} Пока мы все здесь рядом."
    show 3500_sh angry_serious noglasses pioneer glasses
    show d_ma surprise pioneer
    with dissolve_fast
    sh "Мы сейчас в роли экрана, понимаете?{w} И то, что он сейчас решит — это решит он сам, а не…"
    show 3500_sh normal noglasses pioneer glasses with dissolve_fast
    "Шурик споткнулся на полуслове и только ткнул рукой с зажатыми в ней очками куда-то вниз, себе под ноги."
    sh "Одним словом, Максим, посмотри на нас и скажи, хочешь ли ты перейти в наш отряд?"
    hide sl
    hide 3500_sh with dissolve
    stop ambience fadeout 3
    $ renpy.music.set_volume(1.0, delay=2)
    "Впервые у пионера из среднего отряда спрашивали его желание."
    show d_ma normal pioneer with dissolve_fast
    "Максим оглядел собравшихся."
    show sl smile2 pioneer close with dissolve:
        xcenter 0.1
    "Сашка улыбается радостно и чуть кивает головой — она-то в ответе не сомневается и только ждёт подтверждения."
    hide sl
    show 3500_sh normal2 noglasses pioneer glasses behind d_ma:
        zoom 0.85 xcenter 0.715 ycenter 0.79
    with dissolve
    "Шурик сидит и протирает очки с отсутствующим видом, мыслями у себя в кружке.{w} Но те два замечания, что он подал, говорят о его внимании к происходящему."
    hide 3500_sh
    show un serious pioneer far behind d_ma:
        xcenter 0.37
    with dissolve
    "Лена подняла ресницы, кажется, изучила всего, пока Макс барахтался в её зелёных глазищах, и отпустила. Сделав какие-то свои выводы."
    hide un
    show mi cry_smile pioneer close:
        xcenter 0.9
    with dissolve
    "Мику копирует Сашку, только улыбается чуть печально. Будто провожает во взрослую жизнь, которая будет далеко не мёдом."
    hide mi
    show el smile pioneer:
        xcenter 0.22
    show mz shy glasses pioneer:
        xcenter 0.15
    with dissolve
    "Сыроежкин и Женя так и сидят не отпуская рук — им, кажется, нет особого дела до Максима, они заняты сами собой"
    show mz smile glasses pioneer with dspr
    pause 0.1
    show d_mz excitement pioneer as mz with dissolve_fast
    extend "; но вот Женя бросила на Максима быстрый взгляд, сняла свои круглые очки и чуть улыбнулась."
    "И оказалось, что зря он её побаивался, что это она сама всех боится, но готова подпустить Максима чуть поближе, переведя в круг доверенных лиц.{w} Чего ей бояться, когда Сергей рядом?"
    hide el
    hide mz
    show dv grin pioneer2 far behind d_ma:
        xcenter 0.6
    with dissolve
    "Алиса смотрит насмешливо, но и с надеждой почему-то."
    hide dv
    show d_sf normal sport:
        xzoom -1.0 xcenter 0.88
    with dissolve
    "Семён…{w} По лицу Семёна ничего не разобрать.{w} Вообще непонятно, в каком он тут качестве, но что-то связывает его с отрядом — почему-то Алиса сказала про то, что он свой здесь, и остальные приняли это как должное."
    hide d_sf
    show d_us serious sport:
        xcenter 0.77 ypos -0.05
    with dissolve
    "Ульяна очень серьёзно ждёт ответа. И тоже смотрит оценивающе и почему-то чуть-чуть ревниво."
    hide d_us with dissolve
    show d_ma grin2 pioneer with dissolve_fast
    th "Да что я маюсь? Не смогу я теперь в детские игры играть, хватит."
    $ renpy.music.set_volume(0.25, delay=1.0)
    d_ma "Да, я хочу перейти в старший отряд!"
    show d_sf laugh sport with dspr:
        xzoom -1.0 xcenter 0.88
    me "Быть по сему!"
    $ renpy.music.set_volume(1.0, delay=2)
    show dv grin pioneer2 far behind d_ma:
        xcenter 0.6 alpha 0
        linear 1 alpha 1
    show un smile pioneer far behind d_ma:
        xcenter 0.37 alpha 0
        linear 1 alpha 1
    show 3500_sh smile noglasses pioneer glasses behind d_ma:
        zoom 0.85 xcenter 0.715 ycenter 0.79 alpha 0
        pause 0.6
        linear 1 alpha 1
    show el smile pioneer:
        xcenter 0.22 alpha 0
        pause 0.6
        linear 1 alpha 1
    show mz smile pioneer:
        xcenter 0.15 alpha 0
        pause 1.2
        linear 1 alpha 1
    show d_us smile sport:
        xcenter 0.77 ypos -0.05 alpha 0
        pause 1.2
        linear 1 alpha 1
    show sl smile2 pioneer close:
        xcenter 0.02 alpha 0
        pause 1.8
        linear 1 alpha 1
    show mi smile pioneer close:
        xcenter 0.97 alpha 0
        pause 1.8
        linear 1 alpha 1
    show d_sf smile sport with dspr
    "Впервые пионер из среднего отряда перешёл в старший по собственной воле."
    window hide
    show black behind dv with dissolve
    pause 0.5
    hide mi
    hide sl
    hide d_us
    hide mz
    hide el
    hide 3500_sh
    hide un
    hide dv
    hide d_sf
    with Dissolve(1.5)
    pause 0.5

    scene black with pixellate
    show dct_ext_warehouse2_day_7:
        xalign 0.5 yalign 1.2
    with dissolve
    show dct_ext_warehouse2_day_7:
        yalign 0.7
        easeout 0.8 yzoom 5.0 yalign 1.5 blur 20 alpha 0
    show int_catacombs_entrance:
        yzoom 3.0 xalign 0.5 yalign 0.0 blur 20 alpha 0
        pause 0.9
        linear 0.3 yalign 0.5 alpha 0.8
        linear 0.3 yalign 1.0 alpha 0
    show dct_int_tonnel:
        yzoom 3.0 xalign 0.5 yalign 0.0 blur 20 alpha 0
        pause 1.6
        linear 0.3 yalign 0.5 alpha 0.7
        linear 0.3 yalign 1.0 alpha 0
    show dct_int_datacenter:
        yzoom 5.0 xalign 0.5 yanchor -0.15 ypos 0.0 blur 20 alpha 0
        pause 2.3
        easein 0.8 yzoom 1.0 ypos -0.32 blur 0 alpha 1
    window auto
    "Глубоко в шахте под посёлком Шлюз что-то щёлкнуло, и погасли лампочки на одном блоке, тут же вспыхнув на другом."
    stop music fadeout 5
    show dct_int_datacenter:
        pause 1
        linear 2.5 alpha 0
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "И мир Сети ещё чуть изменился." with vpunch
    stop sound fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    
    
    
###########################
#Глава 9. Системные ошибки#
###########################

label dct_system_errors_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Системные ошибки"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop music
    play ambience ambience_clubs_inside_day fadein 2.5
    show headline_text2 u"Глава IX. Системные ошибки" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_int_clubs_male2_night_zoom
    show el surprise pioneer at cleft
    with dissolve
    el "Шурик, как же так?"
    "Сыроежкин огорчался совершенно искренне. Столько работы, и всё зря."
    el "Ты ведь не мог ошибиться."
    show el sad pioneer with dspr
    el "И я за тобой всё проверял. И схема работает, сигнал — вот он."
    "Сергей кивнул на колечко, светящееся на экране осциллографа."

    scene bg int_clubs_male_day
    show sh normal pioneer close at cright
    with dissolve
    sh "Сергей, я думаю, что просто мы ещё слишком мало знаем о мозге, и ошибка закралась в самом начале."
    "Шурику было неудобно перед товарищем, но он старался не показывать виду, сказывался опыт Александра, которому случалось представлять неудачи в экспериментах как запланированные результаты."
    stop ambience fadeout 1

    scene dct_ext_another_clubhouse_day with squares
    play music higekitekina fadein 1
    "В окно открывался вид на заброшенное здание напротив — логово Яны."
    sh "\~ Она и сейчас где-то там, внутри.{w} Или ещё где-то.\~"

    scene bg int_clubs_male_day
    show d_el think2 pioneer as el at fleft
    show sh serious pioneer at right
    with squares
    sh "\~ Я могу с большой вероятностью отключиться в следующем цикле. \~"
    sh "\~ Я ещё не готов к активации — нужно оценивать объективно. Даже не знаю, должен ли я огорчаться этому. \~"
    show sh normal pioneer with dspr
    sh "\~ Но вот Яну жалко. \~"
    sh "\~ Надо попросить Семёна, чтобы приглядывал за ребёнком, пока меня не будет. \~"
    show sh serious pioneer with dspr
    sh "\~ Правда, он и так приглядывает. \~"
    show el normal pioneer with dspr
    el "\~ Переживает. \~"
    el "\~ Неудачу переживает. Мне простительно ошибаться, я всего лишь школьник, и дальше городского КЮТа меня не знают, а вот Шурику тяжело. \~"
    show el smile pioneer with dspr
    el "Саша, да чёрт с ним, с этим прибором."
    show sh normal pioneer with dspr
    show el normal pioneer at center with MoveTransition(1.3, time_warp=_ease_time_warp)
    el "Зато мы теперь знаем, что вот эта схема не работает и нужно делать другую! Давай подумаем, чем мы можем ещё заняться до конца смены."
    show d_el smile2 pioneer as el with dspr
    el "Может, робота доделаем? Или просто отдохнём? Или…"
    show sh surprise pioneer with dspr
    el "Тебе же поступать в этом году. Может, будешь готовиться? У Жени есть кое-какие учебники, как раз на этот случай."
    show d_el think2 pioneer as el with dspr
    el "Но тебе, наверное, они и не нужны."
    show sh normal pioneer with dspr
    sh "\~ Добрая и наивная душа. \~"
    show el normal pioneer
    show sh serious pioneer
    with dspr
    sh "\~ Никогда не высовывавшаяся за пределы «Совёнка» и Сети, потому добрая и наивная. \~"
    show sh normal pioneer
    show el serious pioneer
    with dissolve_fast
    el "…я со вчерашнего вечера вижу, что с тобой что-то не так, Саша, и дело не в нашей установке. Я могу чем-то помочь?"
    show 3500_sh normal2 noglasses pioneer glasses as sh with dissolve_fast:
        ycenter 0.856
    sh "\~ Конечно, добрый волшебник дядя Сергей. Всего лишь верни назад старого Шурика. \~"
    sh "\~ Или верни Александра и сделай так, чтобы однажды в автобусе рядом с ним проснулась Яна-человек. \~"
    show el sad pioneer with dissolve_fast
    sh "\~ Это, правда, убьёт Яну-робота и нынешнего Шурика, но кому они нужны, кроме друг друга? Они — так, побочный результат сбоев в экспериментах. \~"
    sh "\~ Но то, что дело не в нашей установке — ты ошибаешься, дело именно в ней. \~"
    stop music fadeout 2
    play ambience ambience_clubs_inside_day fadein 1
    show sh normal_smile pioneer with dissolve_fast:
        ycenter 0.5
    sh "Спасибо, Сергей. Дело именно в установке, что бы ты ни думал. Я справлюсь, не переживай."
    show el normal pioneer with dissolve_fast
    sh "Так что давай, в самом деле, отдыхать. До конца цикла чуть больше недели, а что там дальше будет — никто не знает."
    show sh laugh pioneer with dissolve_fast
    sh "Давай разберём этот агрегат и объявим всем, что факир был пьян и фокус не удался."
    show sh smile pioneer with dspr
    el "Хорошо, Шурик. Вот только Лена огорчится — я пообещал ей, а тут такое…"
    show d_el smile2 pioneer as el with dspr
    el "И знаешь, если тебе сегодня вечером нечем будет заняться — приходи в библиотеку. Женя на чай приглашала."
    show sh upset pioneer with dspr
    sh "\~ Я сказал «цикла», но Сергей, кажется, ничего не понял. \~"
    show sh normal pioneer with dissolve_fast
    sh "Спасибо, но вам будет комфортнее без меня. Мне кажется."
    stop ambience fadeout 1

    scene dct_ext_island_reverse_day
    show d_ma sit_back at cright:
       ycenter 0.65
    with dct_fade
    play ambience ambience_lake_shore_day fadein 1
    pause 1
    un "Чем пахнет ветер, Максим?"

    scene dct_ext_island_glance_south_day
    show un smile2 pioneer far at fright:
        ycenter 0.74
    with pushleft
    d_ma "Лена. Я не…{w} То есть лодку я видел, но думал, что ты где-то на другом конце острова. Иначе не стал бы тебе мешать."
    show un smile pioneer far with dspr
    "Максим смутился."
    show d_un hope pioneer far as un with dissolve_fast
    d_ma "Понимаешь, Лена, я сейчас вышел из столовой, встал на крыльце и вдруг понял, насколько он маленький, наш лагерь. А я даже на территории ещё побывал не везде."
    "Максим ещё помялся и выдохнул."
    show un smile pioneer far with dissolve_fast
    d_ma "Простором ветер пахнет."

    scene dct_ext_island_reverse_day
    show d_ma normal pioneer at fleft:
        yalign 0.02
    with dissolve
    un "Хочешь земляники? Она вкусная."
    show d_ma shy pioneer:
        linear 0.4 ycenter 0.76
    un "Ну, неделю ещё поживешь тут…"
    th "Семён будет доволен."
    show d_ma smile pioneer with dspr
    th "Максиму ещё расти и расти, но, кажется, ему есть куда расти, кажется, когда проснётся, он в лагере на одном месте сидеть не будет."
    un "…а потом закончится смена, и делай, что хочешь."
    show d_ma rage pioneer with dissolve_fast
    d_ma "Да какое там — что хочешь… Школа, родители и всё решают за тебя."
    show d_ma surprise pioneer with dissolve_fast
    d_ma "И в лагерь я ехать не хотел."
    show d_ma angry pioneer with dissolve_fast
    extend " Сейчас не жалею о том, что поехал, но не хотел же."
    un "Ну вот ты же сам в горнисты вызвался, никто тебя не просил, никто тебя не назначал."
    show d_ma shy pioneer with dissolve_fast
    d_ma "Да. Вдруг захотелось сделать что-то, что-то своё, чего до меня не было. Вот я и соврал, что умею на горне играть."
    show d_ma normal pioneer with dissolve_fast
    d_ma "Думал, что Мику покажет."
    show d_ma smile pioneer with dissolve_fast
    extend " А Мику только теорию знает, а у самой не получается."
    show d_ma surprise pioneer with dspr
    d_ma "А оказалось, что не соврал. Оказалось, что это легко, когда поймёшь, как."
    show d_ma serious pioneer with dissolve_fast
    d_ma "Завтра пойду к вожатой и к Мику, извинюсь за обман."

    scene dct_ext_island_glance_south_day
    play music peritune_gentle_theme_piano fadein 1
    show un smile pioneer close:
        xcenter 0.86 ycenter 0.6
    with dissolve
    "Лёгкий ветерок шевелил волосы, слышно было, как шлёпают волны о берег."
    "Лена наблюдала за охотящейся скопой: как скопа парит над водой на уровне вершин сосен, как она, увидев рыбу, пикирует и входит в воду, выставив перед собой ноги, как появляется на поверхности и, сделав сильный взмах, тяжело отрывается от воды с рыбой в когтях и несёт рыбу куда-то на остров Длинный."
    show un normal pioneer close with dspr
    th "Не работает машина у кибернетиков."
    show un angry2 pioneer close with dissolve_fast
    extend " Или врут, что не работает. Шурик как-то глаза отводил."
    show un serious pioneer close with dspr
    th "Ну и пусть."
    extend " Зачем мне эта машина? Зачем мне знать, кем я была?"
    th "Семён и Алиса правильно говорят: я — это я, такая, какая есть. И всё, что было вложено в меня — это как удобрение, не больше. А я выросла собой."
    show d_un hope pioneer close as un with dspr
    th "А совсем скоро приедет МОЙ Семён."
    show un cry_smile pioneer close with dissolve_fast
    extend " Вдруг он наконец проснётся?"
    show un smile pioneer close with dissolve_fast
    "Лена мечтательно улыбнулась, потом спрятала улыбку и оглянулась на Максима."
    show un normal pioneer close with dspr
    "Горнист привалился плечом к дереву и, кажется, задремал."

    scene dct_ext_island_reverse_day
    show d_ma blink_smile pioneer:
        zoom 0.75 xcenter 0.05 ycenter 0.84 rotate -15
    with dissolve
    "Лена осторожно встала, подняла с земли альбом, отошла подальше и, присев на прибитый к берегу и облизанный волнами ствол, начала делать зарисовки спящего Максима."
    th "А ведь Семён его вместо себя оставить хочет. Сам ещё не знает об этом, но уже хочет."
    extend " Подтянет его, оставит вместо себя, а сам уйдёт."
    th "Даже не важно, физруком будет Максим или кем-то ещё — просто кем-то, на кого можно оставить лагерь, потому что вожатая не всесильна."
    th "А сам уйдёт и Ульяну с собой уведёт."
    extend " Жалко, очень жалко."
    show d_ma blink pioneer with dspr
    th "Но Алисе будет к кому возвращаться."
    th "А позже и Максим уйдёт. И Алиска уйдёт рано или поздно — вон, вместе с Максимом и уйдёт."
    th "И я уйду, когда мой Семён готов будет — это ещё не скоро, но я подожду."
    th "Потому что нельзя вечно жить в детском манеже."
    extend " Будем заглядывать иногда, невидимые пионерами. Да если между сменами попадём, будем с Ольгой общаться."
    extend " Ну и между собой нельзя связь терять."
    show d_ma blink_smile pioneer with dspr
    th "А кто-то и останется: доктором, поваром, водителем, да хоть и физруком."
    th "А вот куда уйдём — я не знаю. В Шлюз? В пустые узлы? В материнские миры?"
    th "Ульяна говорила, что выход туда через теплообменник скоро закроется, но ведь есть же ещё точки перехода в пещерах."
    extend " Что-то я запомнила из прошлого цикла, из того, что не хотела запоминать, никуда не денешься."
    stop music
    $ renpy.sound.set_volume(1.7, delay=0, channel='sound2')
    $ renpy.sound.set_volume(2.5, delay=0, channel='sound3')
    play sound sfx_blow_out_candle
    play sound2 [ "<silence .3>", sfx_blow_out_candle ]
    play sound3 [ "<silence .6>", sfx_blow_out_candle ]
    show us smile pioneer as us2 at center:
        xzoom 0.2 yzoom 1.0 yalign 0.75 alpha 0
        ease 0.1 xzoom 0.2 yzoom 2.5 alpha 0.2
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 3.5 yzoom 0.3 alpha 0.2
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 0.2 yzoom 2.5 alpha 0.2
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 3.5 yzoom 0.3 alpha 0.2
        ease 0.1 xzoom 1 yzoom 1 alpha 0
    show us smile pioneer as us3 at center:
        xzoom 1 yzoom 0.3 yalign 0.75 alpha 0
        ease 0.1 xzoom 3.5 yzoom 0.3 alpha 0.05
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 0.2 yzoom 2.5 alpha 0.05
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 3.5 yzoom 0.3 alpha 0.05
        ease 0.1 xzoom 1 yzoom 1 alpha 0.05
        ease 0.1 xzoom 0.2 yzoom 2.5 alpha 0.05
        ease 0.1 xzoom 1 yzoom 1 alpha 0
    show us smile pioneer as us4 at center:
        zoom 1.6 yalign 0.75 blur 60 alpha 0
        linear 0.05 alpha 0.15
        pause 0.1 
        linear 0.05 alpha 0
        zoom 1.4 yalign 0.75 blur 30 alpha 0
        linear 0.05 alpha 0.2
        pause 0.1 
        linear 0.05 alpha 0
        zoom 1.2 yalign 0.75 blur 15 alpha 0
        linear 0.1 alpha 0.25
        pause 0.1 
        linear 0.1 alpha 0
    show us smile pioneer at center:
        alpha 0
        pause 0.1
        alpha 0.2
        pause 0.05
        alpha 0
        pause 0.2
        alpha 0.4
        pause 0.05
        alpha 0
        pause 0.15
        alpha 0.6
        pause 0.05
        alpha 0
        pause 0.1
        alpha 0.8
        pause 0.05
        alpha 0
        pause 0.05
        alpha 1
    pause 0.8
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound3')
    hide us2
    hide us3
    hide us4
    show d_ma blink pioneer
    with dspr
    us "Привет!"
    show us shy pioneer with dissolve_fast
    "Ульяна увидела спящего Максима и продолжила вполголоса:"
    show us shy pioneer close with dissolve_fast:
        xcenter 0.48
    us "Выбрали?"
    show us surp1 pioneer close with dspr
    extend " И он согласился?"
    show us smile pioneer close with dissolve_fast
    extend " А наш ещё телёнок-телёнком, хотя в спектакле сыграл неплохо."
    un "Это потому что у вас в отряде для него места нет."
    un "Переходи в физруки — появится."
    show us grin pioneer close with dspr
    us "Не, я ещё не нагулялась.{w} Вот, держи, принесла."
    "Лена взяла протянутые ей листки с текстом, листки с её собственными рисунками и с какими-то пометками на обратной стороне."
    show us normal pioneer close with dspr
    "Просмотрела, кивнула. Достала из альбома такие же листки, вручила Ульянке."
    un "Спасибо, ты прямо как почтальон. Ну что, поплыли в лагерь?"
    show us smile pioneer close
    show d_ma blink_smile pioneer
    with dspr
    us "Поплыли.{w=0.5} Точка  перехода у музыкального кружка."
    us "Вот только к сестрёнке забегу ещё.{w=0.5} Этого будить?"
    un "Нет, пусть спит. Лодка у него своя, не потеряется."
    stop ambience fadeout 1

    scene bg int_library_day
    show d_mz smile3 glasses pioneer close at right
    with dct_fade
    play ambience ambience_library_day fadein 1
    play music music_list['your_bright_side'] fadein 1
    "Женя сияла."
    show d_mz excitement glasses pioneer close with dissolve_fast
    "Приветливо улыбалась, не ругалась, даже поскрипывала уютно. Так, как будто знакомая половица в родительском доме, где тебя всегда ждут и куда вернулся через много лет."
    hide d_mz with dissolve
    extend " И при этом порхала по библиотеке как мотылёк."
    show d_sf smile pioneer with dissolve:
        xcenter 0.5
    me "Женя, а правда, что влюблённые глупеют?"
    show d_mz shyangry glasses pioneer far at fleft with dissolve
    mz "Ты это к чему?"
    "Женя-новая мгновенно превратилась в Женю-прежнюю, но, заметив улыбку Семёна, отыграла назад."
    show d_mz smile2 glasses pioneer far with dspr
    mz "Да, случается."
    show d_mz smile glasses pioneer far with dissolve_fast
    extend " А что, заметно?"
    show d_sf sad pioneer
    show d_mz shy glasses pioneer far
    with dspr
    "Женя мельком глянула на Семёна, склонившегося над журнальным столиком и что-то пишущего, и подмигнула своему отражению."
    show d_sf normal pioneer
    show d_mz smile glasses pioneer far
    with dspr
    me "Вы уже думали, что будете делать после лагеря?"
    show d_mz hope glasses pioneer far with dissolve_fast
    $ renpy.music.set_volume(0.25, delay=1)
    play sound sfx_door_squeak_light
    show mz normal glasses pioneer far at fleft:
        alpha 0
        pause 1
        linear 0.25 alpha 1
    show d_sf normal pioneer:
        pause 2
        linear 0.7 ypos 0.2
    show d_ge with MoveTransition(2, enter=_moveright, enter_time_warp=_ease_time_warp):
        zoom 0.88 xcenter 0.65 yalign 1.01
    "Скрипнула дверь, и в библиотеку зашла, опасливо косясь на Женю, одна из мелких, прошептала: «Здрасьте», подбежала, прошлёпав по половицам босыми ногами, к Семёну и что-то спросила у него на ухо."
    show d_sf smile pioneer with dspr
    "Семён улыбнулся, достал из кармана ключи, отцепил один от связки."
    me "Справа, на второй или третьей полке."
    me "И там на столе журнал лежит, запишите сами, что взяли. А то меня Ульяна съест, а вами закусит."
    "Мелкая улыбнулась в ответ, часто-часто закивала, качнулась опять к Семёну, будто хотела то ли ещё о чём-то спросить, то ли просто прижаться, но застеснялась и передумала."
    show d_sf smile pioneer:
        pause 0.3
        linear 0.7 ypos 0.0
    hide d_ge with MoveTransition(1, leave=_moveright, leave_time_warp=_ease_time_warp)
    play sound sfx_open_cabinet_1
    $ renpy.music.set_volume(1.0, delay=1)    
    me "Прости. Так что там у вас с «после лагеря»? Решили?"
    hide mz
    mz "Конечно. Мы, оказывается, живём в соседних городах, пять часов на поезде."
    mz "Я приеду к нему в гости на каникулы, а на следующий год Серёжа приедет поступать в наш университет.{w} Он хотел в Бауманку, но передумал и решил в наш университет, на мехмат…"
    show d_mz sceptic glasses pioneer far with dspr
    stop music fadeout 2
    "Женя блеснула очками, улыбнулась левой стороной лица и продолжила своим обычным скрипучим голосом, но без сварливых интонаций. Как она обычно говорила с людьми, которым доверяла настолько, что разрешала заходить в библиотеку без дела."
    mz "Я не обманываю себя, Семён. И не думаю, что наши отношения продлятся намного дольше, чем эта смена."
    mz "А до следующего лета они точно не доживут."
    show d_mz bukal glasses pioneer far with dspr
    mz "На свете есть миллион девушек, значительно более похожих на девушку, чем я. Думаешь, я не знаю своего прозвища?"
    mz "Так получилось, что первой девушкой, которую увидел Серёжа, подняв голову от паяльника, оказалась Жужелица."
    show d_mz confused glasses pioneer far with dissolve_fast
    mz "Он очень порядочный и благородный, он, конечно, будет мучиться.{w} Но лучше мне его отпустить и на всю жизнь превратиться обратно в Жужелицу."
    show d_mz fun glasses pioneer far with dissolve_fast
    mz "Но в Жужелицу, в которую были влюблены как минимум две недели, а это — огромная разница с прежней."
    show d_sf serious pioneer with dspr
    me "Ну, кто же тебя в насекомых держит?"
    show d_mz normal glasses pioneer far with dspr
    me "На общественное мнение тебе плевать, Сыроежкин в тебе дыру вот-вот проглядит, значит, остаёшься только ты сама."
    show d_sf normal pioneer with dspr
    me "Я всегда считал, что это дело двоих. И ответственность, и право двоих — решать, сколько им быть вместе.{w} Даже если один из них внезапно убегает, решение об этом всегда принимают вдвоём — может, не замечают этого, но вдвоём."
    show d_sf sad pioneer with dspr
    "Семён замолчал. Перечитав ещё раз написанное, сложил листки бумаги пополам, спрятал написанное в конверт, собрался заклеить, но передумал."
    "И, написав что-то на конверте, но явно не адрес, сунул его в карман, попрощался и бросил напоследок:"
    show d_sf smile pioneer with dspr
    me "Пойду спасать спорткомплекс от малолетних варваров. Улька добрая, она мелких не тронет, она меня схарчит."
    play sound sfx_open_cabinet_1
    hide d_sf with dissolve
    show d_mz sceptic glasses pioneer far with dspr
    th "Интересно, что такого физрук писал?"
    show d_mz surprise glasses pioneer far with dspr
    "А потом Женя вспомнила, что в пять часов придёт Серёжа, а у неё ещё чайник не поставлен, и отбросила этот вопрос как несущественный."
    stop ambience fadeout 1
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"

    scene black with dissolve
    pause 0.5
    play music fm_freemusic_chillout_music fadein 2
    show promo_text_un u"{color=#e1dd7d}Из записей Семёна Персунова{/color}" at truecenter with dspr
    $ renpy.pause(3.0)
    hide promo_text_un with dissolve
    $ set_mode_nvl()
    window show
    "Вот уже давно — наверное, половину всей моей активной фазы, а с того самого эпического побега на лодке — это точно, меня не оставляет ощущение взгляда в спину.{w} Нет, не в спину, а через плечо.{w} Кто-то наблюдает за мной, за моими поступками. Наблюдает, стараясь не выдавать себя.{w} Только иногда я улавливаю тени его мыслей и эмоций. Не сами мысли и эмоции, а их тени. Вот они были, а вот их уже нет."
    "\nРаньше я думал, что так проявляет себя личность-коллега Пионера, подсаженная мне из одного из материнских миров. Тем более что после отправки Пионера через теплообменник этот наблюдатель очень долго себя не проявлял никак.{w} И вот пару циклов назад, во время нашего визита к Виоле, он опять появился.{w} Так вот, судя по симпатии, то есть по тени симпатии, которую я иногда улавливаю от наблюдателя, это явно не подсаженная из мира Пионера личность. Не сознание-наездник, как его назвали в начале всей этой истории.{w} В конце прошлого цикла Алиса рассказала про разум, возникший и погибший в cистеме, но опять же нет. Ощущение, что за мной наблюдает именно человек.{w} Просто кто-то следит за тем, что я делаю, и иногда одобрительно кивает, или хвалит вслух, или хлопает в ладоши. И вот, я не слышу самого хлопка, но чувствую лёгкий ветерок от движущихся ладоней. Примерно так выглядит тень эмоции, если попытаться привести какие-то понятные аналогии."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "Этот наблюдатель сопровождал меня после побега на лодке первый цикл, что я был со Славяной. Сопровождал в цикле Микуси, сопровождал первые два цикла здесь, в этом узле.{w} Сопровождает в этом цикле и сопровождал в предыдущем. Никак не вмешивается, исчезает в интимные моменты, за что ему отдельное спасибо.{w} Но иногда я думаю: «А как бы я поступил, если бы наблюдателя не было?».{w} А ещё, хоть мне почему-то приятна тень его молчаливого одобрения, но мысль о том, что мы здесь — всего лишь компьютерная симуляция, меня тревожит.{w} А иначе зачем за нами наблюдать? Ну, может, не компьютерная, может, просто лаборатория или зоопарк."
    "\nВедь компьютер можно выключить в любой момент, сохранить в памяти результаты, если нужны, и выключить. Или сбросить всё и запустить симуляцию заново. А зоопарк можно закрыть, питомцев пристроить в другие зоопарки, а кого не удалось — усыпить гуманно и безболезненно."
    "\nВозможно, что у меня с головой не всё в порядке, но недавно Ульяна пожаловалась мне, что стесняется. Что за ней иногда кто-то наблюдает, а она стесняется этого.{w} А на мой вопрос, когда это началось, надолго задумалась и сказала, что, пожалуй, с нашего знакомства. Потом наблюдатель исчез, а в прошлом цикле опять появился.{w} Так что с некоторых пор в нашем лагере стало уже два параноика: я и Рыжик."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "К сожалению, посоветоваться уже не с кем: ни Глафиры Денисовны, ни Виолы, ни Толяныча.{w} Вчера задал Лене вопрос: нет ли у той ощущения, что за ней наблюдают? Потому что если что-то нужно почувствовать, то лучше Лены с этим никто не справится.{w} Но Лена была не в настроении и отреагировала в своей обычной в таких случаях манере — подняла глаза и ответила вопросом на вопрос: «А оно должно быть? Ощущение?».{w} Вот только невербальные сигналы сказали, что да, есть такое ощущение.{w} Читаем мы с Леной друг друга. Очень неудобно иногда от этого: ни соврать, ни уклониться от ответа.{w} Так что комиссией из трёх голосов единогласно была принята гипотеза, что мы все находимся под колпаком у Мюллера. Мыши в лабиринте."
    "\nНе знаю, кажется важным всё это записать.{w} После ужина отнесу в пещеру и спрячу. Там же, где лежит моя записка-маячок.{w} Кажется, если что и уцелеет здесь, когда экспериментаторы соберутся перезагрузить здешний мир, то это только пещера. Ни разу со времён своего первого цикла здесь не был в пещере, и вот, понадобилось.{w} А ещё надо будет поговорить об этом с девочками — мы всё-таки собираемся вместе впервые за цикл: Алиса, Лена, Ульяна, теперь с нами ещё и Мику. Приглашать ли Шурика — вот вопрос."
    "\n\n{i}Надпись на конверте:{/i} {size=+5} Ульяна, если конверт не вскрыт — вскрой и прочти обязательно. С{/size}." 
    window hide
    stop music fadeout 1
    $ sunset_time()
    $ persistent.sprite_time = "sunset"

    scene bg ext_houses_sunset
    show mi normal pioneer far:
        xcenter 0.49 ycenter 0.5
    show el smile pioneer close:
        xcenter -0.28
        easein 2 xcenter 0.16
    with dct_fade
    play ambience ambience_camp_center_evening fadein 1
    show mi normal pioneer with dissolve:
        xcenter 0.5 ycenter 0.54
    show mi normal pioneer close with dissolve:
        xcenter 0.48 ycenter 0.51
    $ set_mode_adv()
    window auto
    el "Привет, Мику."
    mi "Здравствуй, Серёжа. Ты из клуба?"
    show mi normal pioneer close:
        easeout 2 xcenter 1.45
    show el smile pioneer close:
        easeout 2 xcenter 1.26
    "Мику вынырнула с боковой аллеи, от музыкального кружка, и они вместе с Электроником двинулись в сторону площади."

    scene bg ext_square_sunset
    show mi normal pioneer far at cleft
    show el normal pioneer far at fleft
    with pushleft
    mi "…как там машина ваша?"
    show el sad pioneer far with dissolve_fast
    el "Никак, Мику. Что-то записали, а расшифровать не смогли."
    el "Шурик так расстроился, что взял и стёр всю программу дешифровки.{w} И машину мы размонтировали."
    show mi upset pioneer far with dspr
    mi "Серёжа, а может и правильно, что размонтировали? Представь, вдруг мы бы узнали о себе что-то такое, что… Ну, лишило бы нас радости."

    scene dct_ext_square_profile_view_sunset
    show mi normal pioneer at right
    show el normal pioneer:
        xcenter 0.45
    with pushleft
    th "Что за место такое?"
    show d_el think2 pioneer as el with dspr
    th "Вчера я здесь с Сашей о нас с Женей беседовал, сегодня с Мику о…"
    extend " Вообще непонятно, о чём."
    show mi upset pioneer with dspr
    "Так же, как и вчера, блестел на солнце памятник, так же сидела Лена на лавочке с большим блокнотом или, может, с небольшим альбомом на коленях, так же бегали малыши."

    scene bg ext_square_sunset
    show mt angry panama pioneer
    with squares
    "Маршировал вдоль дальнего края площади, где-то напротив лодочной станции, средний отряд, играя в свою всегдашнюю игру с Ольгой Дмитриевной."
    hide mt with dissolve
    "Стоило той отвлечься, как Витька вместо уставной отрядной речёвки-кричалки выдавал:"
    show d_vi rage pioneer with dissolve:
        xcenter 0.28
    d_vi "Пионерский наш отряд! Выходи топить котят!"
    show d_vi smile pioneer with dspr
    d_guys "Раз, два! Левой, правой! Мы идём топить котят!"
    hide d_vi with dissolve
    "Понятно, что никаких котят никто топить и не собирался, если бы в лагере оказался хоть один котёнок — его бы скорее зацеловали, загладили, закормили и затискали. А за намёк на «утопить» намекнувший сам оказался бы на дне."
    "Но подразнить вожатую, заставившую отряд маршировать вместо пляжа — это святое.{w} А всего-то не спали в тихий час."
    show mt rage panama pioneer with dissolve
    "Ольга Дмитриевна рычала, грозила сгноить в нарядах по столовой и раздавала эти наряды направо и налево, но опять и опять вместо «Кто шагает дружно в ряд?» звучали «котята»."
    hide mt with dissolve
    "И только Лена, делавшая зарисовки, иногда замечала улыбку в глазах вожатой."

    scene dct_ext_square_profile_view_sunset
    show mi normal pioneer at right
    show el normal pioneer:
        xcenter 0.45
    with squares
    el "Не понимаю, Мику. Как всплывшее воспоминание, даже старательно забытое перед этим, может лишить нас радости?"
    el "Если это какое-то событие — оно уже в прошлом, а мы-то живём сейчас.{w} Если это какой-то наш проступок, то, я не знаю, надо попросить прощения за него и заслужить, чтобы тебя простили."
    show mi sad pioneer with dissolve_fast
    mi "А если ничего не исправить уже?"
    show el angry pioneer with dissolve_fast
    el "А тогда остаётся только двигаться дальше, а не стонать и ныть. Ты узнала о себе что-то новое — значит, пользуйся этим. Я бы так поступал."
    show mi shocked pioneer with dissolve_fast
    el "Принять, понять и обдумать. Если это что-то хорошее — то повторить, если плохое — больше так не делать."
    show el serious pioneer with dspr
    el "Да что говорить: установку разобрали, программу стёрли — теперь никто ничего ненужного не вспомнит."
    show el normal pioneer
    show mi sad pioneer
    with dissolve_fast
    el "Побегу я по делам."
    show d_el smile2 pioneer as el with dspr
    el "До вечера."
    show mi smile pioneer with dspr
    mi "До вечера, Серёженька."
    "Мику впервые улыбнулась за всю беседу."
    show d_el smile2 pioneer as el:
        easeout 1.6 xcenter 1.2
    mi "Жене привет передавай."
    stop ambience fadeout 2
    show black:
        alpha 0
        pause 1
        linear 1.5 alpha 1
    $ sunset_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    el "\~ В этом лагере что-то можно долго хранить в секрете? \~"

    scene black as black2 with dissolve_fast
    $ night_time()
    $ persistent.sprite_time = "night"
    pause 0.5

    scene dct_ext_beach_night_view_from_gym with dissolve_fast
    play music music_list['sweet_darkness']
    "Семён и Ульяна, как и позавчера, сидели на крыльце спорткомплекса, смотрели на звёзды, на блестевшую за аллеей и пляжем реку, на железнодорожный мост, раскинувшийся от края до края бухты."
    "Было тихо, до отбоя оставалось ещё около часа, но пляж уже опустел. Прохладный ветерок с реки забирался Ульяне под футболку, и девушка зябко вжималась в тёплый Семёнов бок."
    me "Может, внутрь зайдёшь?"
    us "Не, Сём, я сейчас ветровку накину, и мы пойдём погуляем.{w} Тебе, кстати, тоже захвачу, а то с твоей спиной…"

    scene dct_ext_beach_night_with_pass_train with irisout
    "Они легко сбежали с крыльца, пересекли аллею и, чуть зарываясь в песок ногами, дошли до уреза воды."
    "Ульяна присела на корточки и что-то написала на мокром песке подобранной щепкой."
    "Глянула на Семёна, смотрящего в небо, лукаво улыбнулась и стёрла надпись. Только одна буква «У» и осталась видна."
    "Не сговариваясь, они повернули вдоль берега по заросшему берёзами и кустарником участку между пляжем и пристанью, вдоль невысокого, по колено, обрывчика."
    stop music fadeout 2

    scene dct_ext_boathouse_night_with_pass_train with pushleft
    play ambience ambience_boat_station_night fadein 1
    "Заглянули на пристань."
    $ renpy.music.set_volume(0.2, delay=0, channel='sound_loop')
    play sound_loop "<to 23.0>" + dct_sfx_cry  # Плач, но обрезанный, а то он там прям в рыдания переходит
    "Так и ушли бы, но Ульяна услышала чьи-то всхлипывания."
    show d_sf normal hike:
        xcenter 0.35
    show d_us serious sport_windbreaker:
        xcenter 0.65 ypos -0.05
    with dissolve
    us "Сёмк, погоди: кажется, плачет кто-то."
    show d_sf serious hike with dspr
    th "Мику?"
    "Но это оказалась Катя."
    show d_sf normal hike
    show d_us normal sport_windbreaker
    with dspr
    extend " Она сидела на палубе дебаркадера, спрятавшись за надстройку, и всхлипывала, прижавшись лбом к стойке ограждения и свесив ноги в воду."
    us "Подожди, Сём, я сама."
    hide d_us with dissolve
    show d_sf sad hike with dspr
    th "Это хорошо, что сама, потому что я не силён в любовной тригонометрии."
    stop sound_loop fadeout 4
    show d_sf sad hike:
        pause 1.5
        linear 1 alpha 0
    "Ульяны не было довольно долго, Семён прошёл по мосткам и спрыгнул в ближайшую лодку. Развалился там, вытянув ноги на кормовой банке, и прикрыл глаза."
    "Спать не хотелось, хотелось слушать вечернюю тишину: плеск воды о дебаркадер, поскрипывание мостков, перестук бортов лодок, тихие девичьи голоса, шелест листвы близких берёз."
    "Голоса смолкли, и послышалось шлёпанье по палубе дебаркадера двух пар босых ног."
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')

    scene dct_ext_pier_night
    show d_ka p4 cry pioneer:                     
        zoom 1.1 xcenter 0.42 ycenter 0.87
    show d_us normal sport_windbreaker:
        xcenter 0.5 ypos -0.05
    with dissolve
    us "Вот, Катя с нами погуляет, Сём."
    "Катя пряталась за Ульяну, стесняясь."
    show d_ka p4 sad pioneer with dspr
    me "Почему нет? Пойдём, Кать. Ты до домика с нами?"
    show d_ka p4 sad pioneer with MoveTransition(0.8, time_warp=_ease_time_warp):
        xcenter 0.35
    d_ka "Нет, я тоже по лагерю."
    show d_ka p4 upset pioneer with dspr
    extend " Ольга Дмитриевна ругается, когда мы поздно гуляем, а сейчас, с вами, можно."
    stop ambience fadeout 1

    scene dct_coin_dv_sits_on_porch with squares
    play sound_loop ambience_lake_shore_night fadein 1
    play music music_list['farewell_to_the_past_edit'] fadein 1
    "Дорога шла вдоль берега, справа за деревьями показался домик Алисы. Можно было разглядеть хозяйку, сидящую на крыльце и что-то пишущую в тетрадь."
    us "Последнюю ночь у себя ночует. Сём, я забегу ещё к ней после прогулки."
    th "Интересно, когда-нибудь Алиса решится показать содержимое своей тетрадки?"

    scene dct_ext_shore_behind_boathouse_night_2
    show d_ka p3 surprise pioneer:                     
        zoom 0.825 xcenter 0.39 ycenter 0.71
    show d_us normal sport_windbreaker:
        xcenter 0.55 ypos -0.05
    show d_sf normal hike:
        xzoom -1.11 yzoom 1.11 xcenter 0.73 ypos 0.05
    with squares
    d_ka "Почему последнюю?"
    me "Кать, завтра опоздавший пионер приезжает, его надо где-то разместить. И Максим с сегодняшнего дня официально в старшем отряде, его тоже переселять из старого домика нужно."
    show d_ka p4 sad pioneer with dissolve_fast
    me "А вожатая и Алиса живут по одной в домике. Вот, скорее всего, Максима и новенького в Алисином домике поселят, а Алиса будет жить с вожатой."
    show d_ka p4 upset pioneer with dspr
    "Катя при упоминании о Максиме каждый раз вздрагивала, но терпела."
    th "Ничего, через восемь дней всё забудешь, а там Максим окончательно пропишется в старшем отряде и для тебя считай что просто исчезнет."
    stop sound_loop fadeout 1

    scene dct_ext_alley_from_shore_to_clubs_night
    show d_ka p3 normal pioneer:                     
        zoom 1.1 xcenter 0.48 ycenter 0.87
    show d_sf normal hike:
        xzoom -1.0 xcenter 0.9
    show d_us normal sport_windbreaker:
        xcenter 0.75 ypos -0.05
    with dissolve
    play ambience ambience_camp_center_night fadein 1
    "В самом узком месте лесного перешейка они вышли по тропке на поперечную аллею, ведущую к клубам."
    show d_ka p1 smile pioneer with dissolve_fast
    d_ka "Здесь, оказывается, столько тропинок. Я и не знала."
    show d_sf smile hike with dspr
    me "Узнаешь ещё, какие твои годы."
    show d_ka p1 normal pioneer with dspr
    th "Интересно, какая она будет, когда попадёт в старший отряд? Макс начал меняться буквально на глазах и из клоуна и шалопая превращаться в Славю мужского пола."
    show d_sf serious hike
    show d_ka p3 normal pioneer
    with dissolve_fast
    th "Что-то там переключает Система в их поведении. Гадко это, но, чтобы проснуться, им, наверное, придётся пройти и через это."
    show d_ka p2 smile pioneer with dissolve_fast
    d_ka "Знаете, я, наверное, не пойду дальше с вами. Спасибо за компанию."
    show d_sf normal hike
    show d_ka p2 normal pioneer
    with dspr
    d_ka "Правда спасибо. И можно, я…"
    show d_ka p4 shy pioneer with dissolve_fast
    extend " Можно, я буду к вам в гости заходить?"
    show d_us smile sport_windbreaker
    show d_sf smile hike
    with dspr
    us "Конечно, можно, Катя."
    show d_ka p3 smile pioneer with dissolve_fast
    hide d_ka with MoveTransition(1.5, leave=_moveleft, leave_time_warp=_ease_time_warp)
    "Катя забежала на крыльцо своего домика, помахала рукой с крыльца и скрылась за дверью."
    show d_sf normal hike
    show d_us serious sport_windbreaker:
        xzoom -1.0 xcenter 0.55
    with dissolve_fast
    us "Сёмк, ей всего-то и нужно было, чтобы кто-то с ней поговорил и её выслушал.{w} А у них в отряде некому, раз уж она там…"
    show d_us normal sport_windbreaker with dspr
    "Ульяна замешкалась, подбирая определение."
    show d_sf smile hike
    with dspr
    th "Альфа-самка."

    scene dct_ext_camp_entrance_night
    show d_jn:
        zoom 0.125 anchor (0.5, 1.0) pos (0.39, 0.685)
    show 3500_sh smile pioneer:
        zoom 0.125 anchor (0.5, 1.0) pos (0.416, 0.682)
    with fade
    "Они стояли на перекрёстке у клубов и смотрели, как от ворот идёт Шурик, держа Яну за руку."
    show d_jn:
        zoom 0.165 anchor (0.5, 1.0) pos (0.562, 0.755)
    show 3500_sh normal pioneer:
        zoom 0.165 anchor (0.5, 1.0) pos (0.595, 0.75)
    with dissolve
    "Яна заметила Персуновых, что-то сказала Шурику и помахала им рукой. Шурик солидно кивнул Семёну и Ульяне, достал из кармана ключи от кружка."
    sh "Зайдёте?"
    me "Нет, мы ещё погуляем, спокойной ночи."
    hide d_jn
    hide 3500_sh
    with dissolve
    me "Я не знаю, что там вспомнил Шурик, но он нашёл для себя якорь."
    us "Сёмк, как думаешь, он окончательно проснулся? Или только на этот цикл?"
    me "Не знаю, Рыжик. Но теперь ему деваться некуда. Сейчас он проснулся, или проснётся через сто циклов — какая разница?"
    $ persistent.sprite_time = "night"
    me "Куда дальше идём? На площадь или к Мику?"
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
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound3')
    
    
    
#########################
#Глава 10. Снореальность#
#########################

label dct_dreamreality_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Снореальность"
    $ night_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    stop music
    show headline_text2 u"Глава X. Снореальность" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene bg int_house_of_dv_night with dissolve
    play ambience ambience_int_cabin_night fadein 1.5
    dv "Ну, в последний раз на старом месте. Отвяжись жених от невесты!"
    show 3500_dv smile night2 0pt at center with dissolve_fast:
        ypos -0.15
    "Алиса хмыкнула, глядя в потолок."
    th "Что бы ещё сказать соответствующее моменту?"
    show 3500_dv grin night2 0pt with dissolve_fast
    th "Завтра надо будет пнуть Рыжую — пусть забирает остатки своего барахла. А то одно сплошное расстройство."
    show 3500_dv laugh night2 0pt with dissolve_fast
    th "А флаг себе оставлю и на новом месте вывешу."
    th "А если меня Ольга к себе в домик определит? Приедет Второй, спросит, где вожатая, а его в домик с пиратским флагом отправят. Пионерский лагерь, ага. Дурдом «Совёнок»."
    show 3500_dv guilty night2 0pt with dissolve_fast
    th "Это всё Сенька виноват, до него всё чинно и благородно было. Может, ночью на флагштоке пиратский флаг поднять?"
    show 3500_dv smile night2 0pt with dissolve_fast
    th "{i}Я подниму чёрно-белый флаг, закончится этот угар. Я уплыву, и это будет знак того, что Земля есть шар.{/i}"
    show 3500_dv sad night2 0pt with dissolve_fast
    th "Только флаг тогда сразу Ольга конфискует, выцарапывай его потом."
    show 3500_dv guilty night2 0pt with dspr
    "Где-то в домике в какой-то щели надрывался сверчок. Когда он уставал и делал перерыв, становилось слышно, как звенит спираль в лампочке."
    "Спать не хотелось — давили какие-то недодуманные мысли, несказанные слова, несовершённые поступки, которые надо было в своё время додумать, досказать, доделать, а сейчас уже поздно."
    th "Пойти погулять? Или поиграть на эстраде? Тут где-то Сенька с Рыжей шатались, пойти их поискать?"
    show 3500_dv sad night2 0pt with dspr
    th "Я, кажется, наконец-то простила себе тот выстрел из арбалета. Надо будет сказать об этом Семёну, это очень важно."
    show 3500_dv normal night2 0pt with dissolve_fast
    th "Но это можно и завтра."
    show 3500_dv grin night2 0pt with dissolve
    th "Пойду поиграю."
    play sound sfx_wood_floor_squeak
    show 3500_dv grin night2 0pt:
        ease 1 xcenter .16
    th "Надену джинсы и футболку. А то всё в форме да в форме."
    show 3500_dv grin casual 1pt with dissolve2
    pause 1
    show 3500_dv guilty casual 1pt with dissolve_fast
    "Алиса подержалась за кожаную куртку, висящую на гвозде."
    th "Откуда она у меня?"
    th "Я помню, что приехала в ней в первый свой цикл активной фазы, потом при отъезде оставила её здесь, и с тех пор она так тут и висит."
    show 3500_dv normal casual 1pt with dissolve_fast
    th "Мужская кожаная куртка с крошками табака в кармане."
    show 3500_dv smile casual 1pt with dspr
    th "Возьму с собой, уже прохладно."
    $ renpy.sound.set_volume(0.5)
    play sound sfx_door_squeak_light
    pause 0.4
    play sound2 sfx_knock_door3_dull
    pause 0.5
    stop sound2 fadeout 0.3
    $ renpy.sound.set_volume(1.0)
    "Заскрипело крыльцо, и в домик, коротко перед этим стукнув в дверь, заглянула вожатая."
    show 3500_dv normal casual 1pt
    show mt normal pioneer at cright
    with dissolve
    mt "Ты далеко собралась на ночь глядя?"
    dv "Не дальше ограды, Ольга Дмитриевна."
    show mt sad pioneer with dspr
    "Ольга пошевелила губами, но не стала озвучивать ответ. Только кивнула разрешающе."
    mt "Не гуляй долго. Я всё же беспокоюсь о вас, хоть по мне этого и не заметно."
    show 3500_dv guilty casual 1pt with dissolve_fast
    dv "До отбоя ещё полчаса — имею полное право."
    show mt smile pioneer with dspr
    mt "Имеешь, имеешь."
    show 3500_dv normal casual 1pt with dissolve_fast
    show mt smile pioneer:
        pause 0.5
        linear 1 alpha .0
    play sound sfx_door_squeak_light
    "Ольга кивнула ещё раз и, прикрыв дверь, пошла в сторону кружка кибернетики — по своему извечному маршруту вечернего обхода."
    show 3500_dv guilty casual 1pt with dissolve_fast
    th "Что это с нами?"
    th "Раньше бы уже орали друг на друга, а сейчас спокойно разошлись."
    show 3500_dv shocked casual 1pt with dissolve_fast
    th "Стареем? Если мне сорок пять, то сколько же Ольге?"
    show 3500_dv angry casual 1pt with dissolve_fast
    th "Так, стоп, Алиска! Прекрати маяться дурью — тебе семнадцать! Сем-над-цать! Правильно тебя Улька ругает!"
    show 3500_dv normal casual 1pt with dissolve_fast
    "Алиса закинула, как мешок, на плечо куртку."
    show 3500_dv normal casual 1pt coat guitar carried with dissolve_fast
    show d_int_house_of_dv_night_without_light:
        alpha .0
        pause 1
        linear 1 alpha 1.0
    $ persistent.sprite_time = "day"    # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Чтобы куртка не сваливалась с плеча, подпёрла её гитарой и вышла, закрыв дверь не запирая."
    play sound sfx_close_door_campus_1
    stop ambience fadeout 1

    scene black with dissolve_fast
    $ persistent.sprite_time = "night"

    scene bg ext_house_of_dv_night
    show 3500_dv normal casual 1pt coat guitar carried at cright:
        zoom .75
    with dissolve_fast
    play ambience ambience_camp_center_night fadein 1
    th "Всё-таки в удивительном мире мы живём. Никому просто не приходит в голову, что нужно запирать за собой домик, когда уходишь."
    show 3500_dv normal casual 1pt coat guitar carried at cright:
        easeout 1.3 xcenter 1.25

    scene bg ext_house_of_dv_night with fade
    show d_us normal sport_windbreaker:
        zoom .75 xcenter 1.2
        easein 2  xcenter .62
    "Через десять минут после её ухода в домик заглянула Ульяна."
    play sound sfx_door_squeak_light
    hide d_us with dissolve
    "Обнаружила отсутствие гитары, всё поняла, но, чтобы не разминуться, не пошла на эстраду, а завалилась подремать, поджидая, и так и уснула."
    stop ambience fadeout 1
    
    scene bg ext_stage_big_night
    show 3500_dv blink casual 1pt guitar playing:
        zoom .15 anchor (0.5, 1.0) pos (0.45, 0.75)
    with dct_fade
    $ renpy.music.set_volume(0.6, delay=1.5, channel='ambience')
    $ renpy.music.set_volume(0.3)
    play ambience ambience_camp_center_night fadein 1
    play music Everlasting_Summer_guitar_cover fadein 1
    pause .2
    show dct_ext_stage_big_night_sl_sitting
    show d_ma sit_back:
        zoom .24 anchor (0.5, 0.98) pos (0.39, 0.96)
    with dissolve
    $ renpy.pause(3.0, hard=True)
    d_ma "Я и не думал, что на простой гитаре возможно такое."
    "Максим говорил почти шёпотом, и Саша отвечала ему столь же тихо."
    sa "Это же Алиса, в чём-то она даже лучше Мику."
    sa "Я, пожалуй, пойду к себе — потанцевать хотела, но, видно, сегодня не судьба."
    sa "Нет, не провожай меня. Лучше подойди к Алисе, когда она в домик засобирается, только не восхищайся слишком активно. А то она засмущается и начнёт ругаться."
    hide dct_ext_stage_big_night_sl_sitting with dissolve
    "Саша ушла, а Максим остался"
    show d_ma sit_back with dissolve_fast:
        zoom .22 anchor (0.5, 0.98) pos (0.37, 0.92)
    extend ", постепенно перебираясь с заднего ряда всё ближе и ближе к эстраде"
    show d_ma sit_back with dissolve_fast:
        zoom .2 anchor (0.5, 0.98) pos (0.34, 0.89)
    extend ", пока не оказался на самом первом ряду"
    $ renpy.music.set_volume(0.6, delay=1)

    scene dct_ext_stage_normal_night_darker
    show ext_stage_normal_night
    show 3500_dv blink casual 1pt guitar playing:
        zoom .27 anchor (0.5, 1.0) pos (0.28, 0.67)
    show d_ma sit_back:
        zoom .7 xcenter 0.18 ycenter 0.81
    with squares
    extend ", прямо напротив Алисы, балансировавшей на самом краю сцены."
    show 3500_dv normal casual 1pt guitar playing with dspr
    pause 0.8
    show 3500_dv blink casual 1pt guitar playing with dspr
    "А Алиса только мельком глянула на Максима, как бы отметив: «Ты здесь». И опять ушла в музыку."
    th "Музыка — это ритмически и мелодически организованные звуки."
    "Так оно и было сперва. Были просто красивые звуки."
    "Потом за звуками Максим услышал эмоции, потом… Потом показалось, что за эмоциями следом идёт ещё и мысль, или даже Мысль."
    stop music fadeout 5
    show 3500_dv blink casual 1pt guitar playing:
        ease 6 alpha 0
    show 3500_dv normal casual 1pt guitar standing as dv2:
        zoom .27 anchor (0.5, 1.0) pos (0.28, 0.67) alpha 0
        ease 6 alpha 1
    show ext_stage_normal_night:
        linear 40 alpha 0
    th "Понять бы её. Ведь вот она — Алиса настоящая. Поймёшь мысль — поймёшь и то, над чем Алиса сейчас бьётся, и саму Алису."
    "А потом Максим обнаружил, что музыка кончилась."
    "Что Алиса, отставив гитару, будто приросла к сцене и молча смотрит на него. Что глаза её в свете единственной сорокаваттной лампочки, спрятавшейся высоко под куполом, кажутся бездонными и тёмными-тёмными."
    "Мальчик и девочка смотрели друг другу в глаза и молчали."
    "Максим поёжился: то ли от прохлады, заползающей под рубашку, то ли от внимательного и серьёзного взгляда Алисы."
    th "Что меня тянет к тебе? Злая и насмешливая помощница вожатой, которая почти на три года старше меня."
    th "Есть же Катька — я уже понял, что Катька в меня влюбилась. Есть же Саша и Мику, в конце концов, если уж мне так нравятся девушки постарше."
    th "А я трачу время и силы в надежде понравиться тебе."
    $ renpy.music.set_volume(1.0)
    show black with dissolve_fast:
        alpha 0.6
    hide black with dissolve_fast
    play music music_list['tried_to_bring_it_back'] fadein 2
    stop ambience fadeout 1
    "Лампочка под куполом мигнула. Вдруг показалось, что, кроме этой эстрады, ничего больше в мире не существует, что весь мир сжался до янтарно-жёлтого шара, в который заключена эстрада и два человека на ней."
    th "Как там Алиса сказала? «Вспомни свой домашний адрес», а я не помню! Как я могу его вспомнить, если его не существует, если существуют только Алиса и её глаза?"
    th "Вот был целый мир, а лампочка мигнула, и раз — и нет мира, остался только лагерь внутри жёлтого шара, а прочий мир перестал существовать."
    stop ambience fadeout 1
    show black with dissolve_fast:
        alpha 0.6
    hide black with dissolve_fast
    th "А потом лампочка мигнула ещё раз, и этот шар сжался вокруг эстрады, оставив всё прочее снаружи, и внутри остались только мы двое: пионерка с гитарой и глупый пионер с горном, которого держат в плену эти глаза."
    th "А потом лампочка мигнёт в третий раз, шар сожмётся ещё, и останется только Алиса, а всё прочее исчезнет."
    window hide
    hide 3500_dv
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    show black with dissolve_fast:
        alpha 0.6
    show black:
        alpha 1
    show 3500_dv normal casual 1pt guitar standing:
        zoom .27 anchor (0.5, 1.0) pos (0.28, 0.67)
    with dissolve_fast
    pause 0.3
    show 3500_dv normal casual 1pt guitar standing:
        ease 2 zoom .43 anchor (0.5, 1.0) pos (0.4, 0.75)
    pause 2
    window auto
    th "Может, я уже исчез? Может, меня уже не существует, как и всего мира?"
    hide d_ma
    show dct_ext_stage_close_night_darker behind black:
        blur 20
    hide black with dissolve2
    "Показалось, что ровный горизонтальный край сцены начал терять чёткость очертаний и размываться."
    "Страшно не было."
    th "Вот и всё. Я исчез, не успев даже влюбиться в тебя."
    stop music fadeout 2
    play ambience ambience_camp_center_night fadein 2
    show dct_ext_stage_close_night_darker:
        linear 2 blur 0
    dv "Заигралась я."
    "Слова Алисы смыли наваждение."
    dv "Вон уже и фонари погасили."
    show 3500_dv smile casual 1pt guitar standing with dspr
    dv "Раз уж ты здесь, кавалер, пойдём — проводишь меня."
    "И правда, обычно на концертную площадку попадал свет от фонарей, освещавших аллею. Но не сейчас — сейчас светила только тусклая лампочка под самым куполом."
    th "Значит, уже больше двенадцати."
    hide d_ma with dissolve
    show d_ma normal pioneer with dissolve:
        zoom .43 anchor (0.5, 0.99)  pos (0.5, 1.0)
    d_ma "Пойдём."
    "Максим протянул руку Алисе, помогая той спрыгнуть с эстрады."

    scene dct_ext_stage_close_night_darker
    show d_ma normal pioneer:
        zoom .43 anchor (0.5, 0.99)  pos (0.5, 1.0)
    show 3500_dv surprise casual 1pt guitar carried:
        zoom .43 xcenter .4 ycenter .85
    with wipedown
    dv "Ты ледяной как мертвец!"
    show 3500_dv grin casual 1pt guitar carried with dissolve_fast
    dv "Я думала, примёрзну к твоей руке."
    "K Алисе вернулась привычная манера."
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast
    dv "Держи."
    show d_ma surprise pioneer coat with dissolve_fast
    "Откуда-то появилась кожаная куртка, неожиданно заботливо накинутая на плечи Максиму."
    show d_ma serious pioneer coat with dspr
    "Тот дёрнул было плечами, но Алиса удержала куртку."
    show 3500_dv laugh casual 1pt guitar carried with dspr
    show d_ma shy pioneer coat with dspr
    dv "Держи, держи. А когда я начну мёрзнуть — вернёшь."

    scene bg ext_library_night
    show d_ma normal pioneer coat at center:
        yalign 0.02
    show 3500_dv normal casual 1pt guitar carried at right:
        xcenter 0.75 ycenter 0.83
    with fade
    play music music_list['no_tresspassing'] fadein 3
    "Фонари, оказывается, светили. Но у них едва получалось осветить пятачок земли вокруг столба."
    "Светили и лампочки в окнах домиков — тех, в которых ещё не спали. Но казалось, что до них так же далеко, как до звёзд."
    show 3500_dv smile casual 1pt guitar carried with dspr
    dv "Тьма окутала маленький лагерь…"
    show 3500_dv normal casual 1pt guitar carried with dspr
    dv "Скажи, кавалер, ты знаешь, что такое гомеостаз?"
    show d_ma grin2 pioneer coat with dspr
    d_ma "Ну да, я же, говорят, умный и начитанный мальчик.{w=0.3} Гомеостаз — это равновесие, если одним словом."
    show 3500_dv laugh casual 1pt guitar carried with dspr
    dv "Начитанный, умный. Ещё и отличник поди?"
    show d_ma grin pioneer coat with dspr
    d_ma "Нет, троечник с плюсом. Я же ленивый. И есть более приятные и полезные вещи, чем школьная учёба."
    show 3500_dv smile casual 1pt guitar carried with dspr
    "Алиса кивнула понимающе."

    scene bg ext_aidpost_night
    show 3500_dv normal casual 1pt guitar carried at cright:
        ycenter 0.83
    show d_ma normal pioneer coat at cleft:
        yalign 0.02
    with dissolve
    dv "Когда-то давно мне снился сон. Я почти ничего не помню, но ты похож на одного из героев этого сна."
    show 3500_dv laugh casual 1pt guitar carried with dspr
    dv "А я вот — дура. Я когда слово «гомеостаз» услышала, полчаса смеялась. Думала, что это что-то про отношения между двумя мужчинами."
    show 3500_dv smile casual 1pt guitar carried with dspr
    show d_ma smile2 pioneer coat with dspr
    dv "Так вот, такие, как я, говорят, этот самый гомеостаз нарушают, и лагерь пытается от них избавиться."
    show 3500_dv normal casual 1pt guitar carried with dspr
    show d_ma normal pioneer coat with dspr
    dv "Это мне Рыжая сказала, и Сенька подтвердил. А они знают, о чём речь — они сами такие же нарушители гомеостаза, как и я."
    dv "И ещё больше, чем я. Так что это я такая же, как они."

    scene dct_ext_square_profile_view_night_darker
    show dct_ext_square_profile_view_night_darkest:
        alpha 0.0
    show 3500_dv grin casual 1pt guitar carried:
        xcenter 0.32 ycenter 0.83
    show d_ma normal pioneer coat:
        xcenter 0.61 yalign 0.02
    with dissolve
    dv "И вот, кажется, что-то происходит."
    show dct_ext_square_profile_view_night_darkest:
        pause 1
        linear 3 alpha 0.2
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast:
        xcenter 0.37
    "Алиса как будто размышляла вслух, не особо интересуясь присутствием Максима, но потом протянула ладонь и сама взяла его за руку."
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast:
        xcenter 0.42
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 0.4
    "Максим слегка сжал руку Алисы: «Я здесь, я с тобой, не бойся»."
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 0.6
    "Они уже подошли к самому сердцу лагеря, к площади, утыканной фонарями, но вокруг становилось всё темнее и темнее."
    show dct_ext_square_profile_view_night_darkest:
        linear 1 alpha 0.7
    th "Как в чернильнице."
    show dct_ext_square_profile_view_night_darkest:
        linear 1.5 alpha 0.8
    "И неожиданный холод пробирал до костей."
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 1.0
    "А когда стало совсем невыносимо холодно, Алиса пробурчала:"
    dv "И надо только решиться шагнуть с шара на шар."
    stop ambience fadeout 1
    stop music fadeout 1

    scene dct_ball_to_ball_1
    show dct_ball_to_ball_dv_ma
    with pixellate
    play music music_list['sparkles'] fadein 1 # Момент перехода с шара на шар

    scene dct_ball_to_ball_2
    show dct_ball_to_ball_dv_ma
    with pixellate

    scene dct_ball_to_ball_3
    show dct_ball_to_ball_dv_ma
    with pixellate

    scene dct_ball_to_ball_4
    show dct_ball_to_ball_dv_ma
    with pixellate

    scene dct_ball_to_ball_5
    show dct_ball_to_ball_dv_ma
    with pixellate

    scene dct_ball_to_ball_6
    show dct_ball_to_ball_dv_ma
    with pixellate
    stop music fadeout 2

    scene dct_ball_to_ball_7
    show dct_ball_to_ball_dv_ma
    with pixellate

    scene dct_ext_square_profile_view_night
    show 3500_dv normal casual 1pt guitar carried:
        xcenter 0.42 ycenter 0.83
    show d_ma normal pioneer coat:
        xcenter 0.61 yalign 0.02
    with pixellate
    play ambience ambience_camp_center_night fadein 2
    "И сразу же стало светло, как и должно быть при таком количестве фонарей"
    show d_ma normal pioneer coat carried with dissolve_fast
    extend ", и сразу же стало тепло, как и должно быть в середине лета"
    $ renpy.music.set_volume(0.3, delay=0, channel='sound_loop')
    play sound_loop sfx_broom_sweep fadein 2
    extend ", и сразу же стало слышно, как кто-то подметает площадь."
    show 3500_dv shocked casual 1pt guitar carried
    show d_ma surprise pioneer coat carried
    with dissolve_fast
    show 3500_dv shocked casual 1pt guitar carried:
        easeout 1.5 xcenter -0.3
    show d_ma surprise pioneer coat carried:
        easeout 1.5 xcenter -0.11
    d_ma_dv "Саша? Что ты здесь делаешь?\nСлавя…на?"
    stop sound_loop fadeout 2
    "Знакомая и в то же время незнакомая девушка подняла глаза, улыбнулась, сначала растерянно, а потом понимающе, и неожиданно звонко произнесла:"
    slp "Я — Славя!"
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    stop ambience fadeout 1

    scene black with dissolve
    pause 0.5
    $ set_mode_nvl()
    window show
    play music music_list['waltz_of_doubts'] fadein 3  #Славя подметает площадь
    show anim prolog_1 with dissolve2
    "Объясните мне, зачем я подметаю площадь каждый вечер? Я могла бы этого не делать, но я это делаю."
    hide anim prolog_1
    show dct_sl_clean_square_1
    with dissolve
    extend " Программа, заложенная в меня как в обитателя лагеря, виновата?"
    show anim prolog_1
    hide dct_sl_clean_square_1
    with dissolve
    extend " Нет, конечно — я просто делаю это, потому что мне приятно видеть чистый лагерь. Потому что это мой дом. Теперь уже точно — дом."
    hide anim prolog_1
    show arseniy_chebynkin_izbad
    show d_sl_casual at left
    show black as black2:
        alpha 0.3
    with dissolve
    extend " Очень жаль, что большая семья с кучей братьев, и большой дом, и мама с папой — это всё сон. А может и не сон, ведь если есть мои двойники в других лагерях, то, может быть, где-то живёт и настоящая девочка Славя, у которой есть мама с папой и свой дом."
    show anim prolog_1
    hide arseniy_chebynkin_izbad
    hide d_sl_casual
    hide black2
    with dissolve
    extend " Она настоящая, а я? Я ведь тоже настоящая, только в непонятном месте."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "Плохо только то, что по-настоящему мало с кем можно поговорить."
    show anim prolog_1:
        linear 1 alpha 0
    show dct_sl_clean_square_2:
        alpha 0 yalign 1.0
        easein 2.5 yalign 0.5 alpha 1
    pause 1
    extend " Я была чудовищно одинока до того, как проснулась, и спасалась в общественной активности от одиночества, и отгораживалась от людей активностью же."
    show anim prolog_1:
        pause 1
        linear 1 alpha 1
    show dct_sl_clean_square_2:
        easeout 2.5 yalign 0.0 alpha 0
    pause 1
    extend " Но и сейчас стало ненамного лучше. Эйфория первой недели прошла, и вот — накатило."
    hide anim prolog_1
    show dct_sl_clean_square_3
    with dissolve
    extend " Здесь чудесные люди, мальчики и девочки, но я уже знаю всё, что они могут сказать."
    show anim prolog_1
    hide dct_sl_clean_square_3
    with dissolve
    extend " Нет, есть ещё Алиса, Ульяна и Мику, но мы никогда не были особо близки, пока спали, и странно было бы, если бы мы сблизились сейчас. Характеры — их не изменишь."
    hide anim prolog_1
    show dct_sl_clean_square_4
    with dissolve
    extend " А малыши, те, что не спят — они всё равно малыши: с ними интересно и забавно, но как поговорить с ними откровенно? Они просто не поймут. Бедный-бедный Семён, как он с этим со всем справлялся в одиночку?"
    show anim prolog_1
    hide dct_sl_clean_square_4
    with dissolve
    extend " Хорошо, что они есть на свете, те жители другого лагеря, которые тоже не спят, хорошо, что они помнят о нас. Иначе просто опустились бы от растерянности руки."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    "А есть ещё, как её Ульяна-большая назвала, чужая память. Сейчас я уже понимаю, что большая часть этой памяти — это воспоминания того моего двойника, Славяны, из-за которой я обрезала косы."
    hide anim prolog_1
    show dct_dsl_in_shop
    with dissolve
    extend " И так хочется иногда в минуту слабости махнуть рукой и дать ей жизнь. Наверное, это получится, если очень захотеть. Просто ляжет спать Славя, а проснётся Славяна. Почти никто подмены и не заметит."
    show anim prolog_1
    hide dct_dsl_in_shop
    with dissolve
    $ persistent.sprite_time = "night"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Но она не хочет, я не знаю, как, но я чувствую, что она этого не хочет. Да и я сама не хочу, потому что я — Славя! Такая, какая есть — та помощница вожатой, которая провожала нашего Семёна, стоя на берегу."
    $ persistent.sprite_time = "day"          # В сцене на берегу перекраска спрайтов будет осуществрена матрицами по месту
    hide anim prolog_1
    show dct_bank_from_water_side
    show 3500_mz normal pioneer glasses:
        zoom 0.15 xcenter 0.54 ycenter 0.54
    show 3500_el surprise pioneer:
        zoom 0.15 xcenter 0.49 ycenter 0.54
    show 3500_sl scared sport binoculars:
        zoom 0.15 xcenter 0.38 ycenter 0.54
    show 3500_mt rage pioneer panama megaphone:
        zoom 0.15 xcenter 0.32 ycenter 0.55
    show 3500_dv smile pioneer2:
        zoom 0.15 xcenter 0.16 ycenter 0.57
    show 3500_us surp1 sport:
        zoom 0.15 xcenter 0.21 ycenter 0.56
    show black as black2:
        alpha 0.15
    with dissolve
    extend " А чтобы никто не увидел, как она плачет, прижимала бинокль к глазам. Наверное, я тогда была влюблена в него — не знаю, не помню. Или мне было очень жалко, что он убегает от нас? Может быть, я думала, что мы его чем-то обидели?"
    show dct_bank_from_water_side_zoom:
        xalign 1.0
    show 3500_sl scared sport binoculars as sl2:
        zoom 0.75 xcenter 0.65 ypos 0.15
    show 3500_mt rage pioneer panama megaphone as mt2:
        zoom 0.75 xcenter 0.35 ypos 0.15
    show dv guilty pioneer2 far:
        xcenter -0.62 ycenter 0.65
    show us sad sport far:
        xcenter -0.38 ycenter 0.65
    show black as black3:
        alpha 0.2
    with dissolve2
    extend " Не помню, столько времени прошло, и я спала тогда. Только и помню, что само бегство Семёна — от момента, когда, возвращаясь с пробежки, встретила запыхавшуюся Женю, стучащую кулачками в дверь к Ольге Дмитриевне, и до того, как понурая, как будто лишившаяся внутреннего стержня, вожатая даже не скомандовала, а тихо попросила: «Давайте не будем говорить об этом»."
    hide 3500_sl
    hide 3500_mt
    show dct_bank_from_water_side_zoom:
        pause 0.7
        ease 3 xalign 0.0
    show 3500_sl scared sport binoculars as sl2:
        linear 0.7 alpha 0
    show 3500_sl sad sport binoculars behind black3:
        zoom 0.75 xcenter 0.65 ypos 0.15 alpha 0
        linear 0.7 alpha 1
        ease 3 xcenter 1.65
    show 3500_mt rage pioneer panama megaphone as mt2:
        linear 0.7 alpha 0
    show 3500_mt scared pioneer panama megaphone behind black3:
        zoom 0.75 xcenter 0.35 ypos 0.165 alpha 0
        linear 0.7 alpha 1
        ease 3 xcenter 1.35
    show dv guilty pioneer2 far:
        pause 0.7
        ease 3 xcenter 0.38
    show us sad sport far:
        pause 0.7
        ease 3 xcenter 0.62
    show black as black4 behind dv:
        alpha 0.0
        pause 5.5
        linear 1.5 alpha 1.0
    pause 3.7
    extend " И у Алисы с Ульяной тоже только эти воспоминания с того цикла и сохранились."
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    show dv guilty pioneer2 far:
        linear 1 alpha 0
    show us sad sport far:
        linear 1 alpha 0
    pause 1

    scene black
    show anim prolog_1
    with dissolve
    "Так вот, это именно я, и я на своём месте."
    show anim prolog_1:
        linear 1 alpha 0
    show dct_sl_clean_square_5:
        alpha 0 yalign 0.0
        easein 2.5 yalign 0.5 alpha 1
    pause 1
    $ persistent.sprite_time = "day"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Я уверена, что и Славяна это понимает, и сейчас согласна со мной. Значит, буду просто жить здесь, у себя дома — в лагере «Совёнок»."
    show anim prolog_1:
        pause 1
        linear 1 alpha 1
    show dct_sl_clean_square_5:
        easeout 2.5 yalign 1.0 alpha 0
    pause 1
    $ persistent.sprite_time = "night"          # Cцена на берегу закончилась, спрайты возвращаются к ночному режиму
    extend " Делать добро из зла, потому что ничего больше под руками у меня нет. Делать лагерь лучше, помогать другим его обитателям осознать себя, делать так, чтобы, когда они проснутся, они проснулись в самом лучшем лагере."
    hide anim prolog_1
    show dct_sl_clean_square_6:
        alpha 0.6
    with dissolve
    extend " А ещё это мой дом, и мне уплывать отсюда некуда. А когда решу, что хватит, тогда и буду дальше думать."
    show dct_sl_clean_square_6 with dissolve_fast:
        alpha 1.0
    extend " А что там решат для себя другие мальчики и девочки — это им решать. Я…"
    show dct_sl_clean_square_7:
        alpha 0
        linear 1.5 alpha 1
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    window hide
    stop music fadeout 4
    play ambience ambience_camp_center_night fadein 4
    play sound_loop sfx_broom_sweep fadein 4
    $ set_mode_adv()
    th "Кто-то идёт на площадь. Двое: что за парочка? Отбой ведь уже был, придётся воспитывать влюблённых."

    scene dct_ext_square_night_crop
    show 3500_dv grin casual 1pt guitar carried at cleft:
        zoom 1.25 yalign 0.15
    show d_ma normal pioneer coat carried at right:
        zoom 1.25 yalign 0.08
    with fade
    window auto
    th "Алиса? И Максим? Что за странный союз. Или…"
    stop sound_loop fadeout 1

    scene bg ext_square_night
    show d_sl surprise pioneer broom:
        zoom 0.55 xcenter 0.34 ycenter 0.67
    show d_ma normal pioneer coat carried at right:
        zoom 0.75 xcenter 0.78 yalign 1.01
    show 3500_dv grin casual 1pt guitar carried at cright:
        zoom 0.75 xcenter 0.57 yalign 0.0
    with dissolve
    th "Но ведь это не наша Алиса!"
    th "И Максим не наш. Оба чуть взрослее выглядят, что ли. Как будто на год постарше."
    show d_sl surprise pioneer broom:
        zoom 0.75 xcenter 0.37 yalign 0.0
    show 3500_dv normal casual 1pt guitar carried at fleft:
        zoom 1.0 ycenter 0.83
    show d_ma normal pioneer coat carried at cright:
        zoom 1.0 yalign 0.02
    with dissolve
    th "Но ведь им же нельзя здесь находиться — это Семён очень ясно дал понять. Или можно?"
    show d_sl smile2 pioneer broom:
        zoom 1.0 ycenter 0.83
    show 3500_dv smile casual 1pt guitar carried
    with dissolve_fast
    sl "Здравствуй, Алиса. У тебя получилось? Ты теперь тоже можешь прыгать туда-сюда, как наша Ульяна?"
    "И голос Алисы, нашей Алисы, из-за спины:"
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.6 xcenter 0.88 ycenter 0.67 alpha 0.0
        linear 1 alpha 1.0
    show d_sl surprise pioneer broom
    show 3500_dv normal casual 1pt guitar carried
    show d_ma surprise pioneer coat carried
    with dissolve_fast
    stop ambience fadeout 2
    play music my_2nd_summer fadein 2
    dv "Ну здравствуй, сестрёнка."
    show black with dissolve
    hide d_ma
    show d_ma serious pioneer coat carried guitar standing at center with dissolve:
        yalign 0.86
    $ persistent.sprite_time = "night"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Потом, в следующие циклы, в этот день Максиму всегда снился один и тот же сон."

    scene black with dissolve_fast
    $ persistent.sprite_time = "day"          # В сцене сна Максима перекраска спрайтов будет осуществрена матрицами по месту

    scene dct_ext_square_night_purple:
        xzoom 1.1 yzoom 1.16 xcenter 0.535 ycenter 0.552 rotate 1.24 blur 10
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.6 xcenter 0.84 ycenter 0.7 matrixcolor TintMatrix("#A1C9D0")
    show 3500_dv grin pioneer3 as dv4:
        zoom 0.6 xcenter 0.84 ycenter 0.7 matrixcolor TintMatrix("#98A0E8")*BrightnessMatrix(value=0.1) alpha 0
    show 3500_dv normal casual 1pt at fleft:
        ycenter 0.83 matrixcolor TintMatrix("#A1C9D0")
    show 3500_dv normal casual 1pt as dv3 at fleft:
        ycenter 0.83 matrixcolor TintMatrix("#98A0E8")*BrightnessMatrix(value=0.1) alpha 0
    show d_sl smile2 pioneer broom close at center:
        matrixcolor TintMatrix("#A1C9D0")
    show black:
        alpha 0.65
    with dissolve_fast
    "Как будто он стоит на краю площади, а посередине, напротив памятника, три фигуры:"
    show black behind d_sl with dissolve
    extend " первая, которую он сначала принимает за Сашу, но это не Саша — это какая-то другая девушка, очень похожая, но не она."
    th "Славная девушка."
    show d_sl smile2 pioneer broom close:
        linear 1.3 alpha 0
    show black behind dv2 with Dissolve(1.8)
    "А потом уже смотрит только на двух других участников сна — на двух Алис."
    show 3500_dv grin pioneer3 as dv4:
        linear 15 alpha 0.5
    show 3500_dv normal casual 1pt as dv3:
        linear 15 alpha 0.5
    show black:
        linear 20 alpha 0
    "Они стоят, зеркальные отражения одна другой, и жадно разглядывают друг друга, а всей разницы между ними — что одна вся в чёрном, а другая в обычной пионерской форме с хулигански повязанным на запястье красным галстуком."
    "Губы их шевелятся, но слов с того места, где стоит Максим, не слышно."
    show 3500_dv normal casual 1pt:
        zoom 0.91 xcenter 0.32 ycenter 0.8
    show 3500_dv normal casual 1pt as dv3:
        zoom 0.91 xcenter 0.32 ycenter 0.8 alpha 0.6
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.66 xcenter 0.74 ycenter 0.72
    show 3500_dv grin pioneer3 as dv4:
        zoom 0.66 xcenter 0.74 ycenter 0.72 alpha 0.6
    with Dissolve(1.5)
    "Потом обе Алисы одновременно, как по команде, начинают медленно сходиться."
    show 3500_dv normal casual 1pt:
        zoom 0.825 xcenter 0.46 ycenter 0.78
    show 3500_dv normal casual 1pt as dv3:
        zoom 0.825 xcenter 0.46 ycenter 0.78 alpha 0.7
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.72 xcenter 0.64 ycenter 0.74
    show 3500_dv grin pioneer3 as dv4:
        zoom 0.72 xcenter 0.64 ycenter 0.74 alpha 0.7
    with Dissolve(1.5)
    th "Как на дуэли."

    scene dct_ext_square_night_purple_blur_HD
    show dct_dv_two_pieces_pioneer:
        anchor(0.5,0.7) pos(0.65,0.8) rotate 2.3 transform_anchor True
    show dct_dv_two_pieces_casual:
        anchor(0.5,0.7) pos(0.35,0.8) rotate -2.3 transform_anchor True
    with fade
    "Когда девушки оказываются на расстоянии шага друг от друга, они останавливаются, поднимают руки: та, что в чёрном, та, что привела его сюда — правую, а её отражение — левую, и начинают тянуться друг к другу."
    show dct_dv_two_pieces_pioneer:
        ease 2 pos(0.61,0.8)
    show dct_dv_two_pieces_casual:
        ease 2 pos(0.39,0.8)
    $ renpy.pause(0.2,hard=True)
    "И вот, когда между кончиками их пальцев остаются считанные сантиметры, обе Алисы оглядываются на Максима, местная Алиса что-то говорит, а та, что привела Максима на площадь, ловит его взгляд и как будто просит разрешения."
    "Что Максиму остаётся? Он машет рукой, это разрешение давая."
    window hide
    show dct_dv_two_pieces_pioneer:
        linear 1.1 pos(0.6,0.8) rotate 0 transform_anchor True
    show dct_dv_two_pieces_casual:
        linear 1.1 pos(0.4,0.8) rotate 0 transform_anchor True
    $ renpy.music.set_volume(0.0, delay=1.0)
    play sound sfx_intro_bus_stop_sigh
    $ renpy.pause(0.5,hard=True)
    play sound2 sfx_intro_bus_transition
    show dct_dv_two_pieces_bg_square with Fade(.5, .3, .7, color="#fff")
    $ renpy.pause(0.5,hard=True)
    show dct_dv_two_pieces_bg_dark with Dissolve(1.5)
    $ renpy.pause(0.4,hard=True)

    scene black with dissolve_fast
    window auto
    "И в момент касания рук всё вокруг накрывает тьма, и Максим просыпается."
    $ renpy.pause(0.5,hard=True)
    $ renpy.music.set_volume(1.0, delay=3.0)
    "А перед самым пробуждением, уже в полусне, он видит лицо той, второй Алисы, думает во сне же, что эти Алисы — они всё-таки разные, и слышит голос:"
    show dct_dv_argue with flash
    dv "Смотри, горнист. Обидишь сестрёнку — найду и оторву башку!"
    show dct_dv_argue sternsmile with dspr
    "Но Максим уже понимает язык Алисы, и понимает, что пусть звучит это как угроза, но ещё это — пожелание удачи или даже счастья."
    hide dct_dv_argue with dissolve2
    stop music fadeout 2
    stop sound
    stop sound2
    $ persistent.sprite_time = "day"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "«Рыж-ж-жевская!» — с оттяжкой произносит вслух Максим и просыпается окончательно."
    play ambience ambience_camp_center_night fadein 1
    $ persistent.sprite_time = "night"
    dv "Что ты сейчас сказал? Повторить не боишься?"

    scene dct_ext_stage_close_night behind blink
    show 3500_dv angry casual 1pt behind blink:
        zoom 0.75 xcenter 0.4 yalign 0.0
    show unblink
    "Максим вздрогнул и открыл глаза. Прямо над ним, абсолютно готовая к рукоприкладству, нависала Алиса.{w} Злая Алиса."
    "Она протянула левую руку к галстуку Максима, а правую уже занесла для сокрушительного щелбана."
    "Но Максим откуда-то знал правильный ответ."
    d_ma "Рыжевская, скажи. Вы успели коснуться друг друга? Там, на площади?"
    show 3500_dv smile casual 1pt with dissolve_fast:
        xcenter 0.42
    "И случилось чудо: пальцы правой руки страшной ДваЧе распрямились, кисть развернулась в расслабленную пятерню, и пятерня эта погрузилась в шевелюру Максима, ласково потрепав."
    dv "Много будешь знать, Макс — скоро состаришься."
    show 3500_dv laugh casual 1pt with dspr
    dv "Вот примерно как я. Я тут играю, стараюсь, можно сказать, для единственного слушателя. А единственный слушатель взял и заснул прямо на концерте."
    show 3500_dv normal casual 1pt with dspr
    dv "Что там тебе снилось — я не знаю. И ты как хочешь, а я всё — в домик и спать."

    scene bg ext_square_night
    show 3500_dv smile casual 1pt guitar carried at center:
        ycenter 0.83
    show d_ma smile2 pioneer coat carried at right:
        yalign 0.02
    with fade
    "И фонари светили нормально, и холода не было, и куртку Алиса сунула Максиму со словами:"
    dv "На, тащи, хоть какая-то от тебя польза будет."
    show un normal pioneer far at fleft with dissolve
    "На площади, как обычно в это время, сидела Лена, молча кивнувшая им обоим."
    show un smile pioneer far
    show d_ma normal pioneer coat carried
    with dspr
    th "А ведь она впервые назвала меня Максом."

    scene bg ext_house_of_dv_night
    show 3500_dv normal casual 1pt guitar carried at center:
        ycenter 0.83
    show d_ma normal pioneer coat carried at right:
        yalign 0.02
    with fade
    th "Не Максимом, племянником, кавалером или горнистом, а Максом."
    show black:
        alpha 0
        linear 1 alpha 1
    stop ambience fadeout 3
    $ night_time()
    $ persistent.sprite_time = "night"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Это должно что-то значить?"
    scene black with dspr
    stop sound fadeout 2
    stop music fadeout 2
    stop sound_loop fadeout 2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    
    
    
####################################
#Глава 11. Горизонтальный транспорт#
####################################

label dct_horizontal_transport_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Горизонтальный транспорт"
    $ night_time()
    $ persistent.sprite_time = "night"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop sound
    stop sound_loop
    stop ambience
    show headline_text2 u"Глава XI. Горизонтальный транспорт" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene bg ext_square_night
    show un normal pioneer at left:
        ycenter 0.65
    show d_sf normal hike at right:
        xzoom -1 ypos 0.12
    with dissolve
    play ambience ambience_camp_center_night fadein 1
    un "Семён, значит, ты думаешь, что мы не настоящие?"
    show d_sf sad hike with dspr
    me "Я не знаю, Лен…"
    show d_sf normal hike with dspr
    me "Для самих себя мы, конечно, настоящие. И мир вокруг нас тоже.{w} Но вот то, как этот мир устроен… И как мы устроены. И физически, и духовно."
    show un serious pioneer with dissolve_fast
    un "Продолжай, я поняла."
    show un normal pioneer with dissolve_fast
    "Лена принялась что-то рисовать, поглядывая на Семёна."
    show d_sf laugh hike with dspr
    me "Мне красивую позу принять? Я могу."
    hide d_sf with dissolve
    "Семён вскочил со скамейки и встал напротив Лены, копируя Генду."
    show un smile pioneer with dspr
    un "Ну если ты именно таким хочешь остаться в памяти потомков."
    show un normal pioneer with dspr
    un "Но ты говорил про наш мир."
    show d_sf normal hike at right with dissolve:
        xzoom -1 ypos 0.12
    play sound sfx_inhale
    "Семён тоскливо огляделся. Сел рядом. Вздохнул."
    show un normal pioneer with dspr
    me "Видишь, Лена. Сначала я думал, что все мы — всего лишь модель, которую обсчитывает какой-то супер-пупер компьютер. Но потом…{w} Слишком у нас всё нерационально. Люди — ладно, но даже лагеря не во всём одинаковые."
    me "Будь я компьютером, здесь бы всё было по одному образцу. И пионеры говорили бы одинаковыми наборами фраз. Исключительно для экономии ресурсов."
    me "А мы в каждом лагере хоть чуть, но разные. А уж когда просыпаемся…{w} Те же две Алисы — это два абсолютно разных человека. Похожих очень, но перепутать можно, только если не знаешь обеих.{w} Про Ульян вообще молчу."
    "Лена закончила рисовать и повернула альбом к Семёну."
    show un smile pioneer with dspr
    "Получился «Семён, доказывающий теорему». Стоит у едва намеченной классной доски, мел в правой руке, а сам обернулся к классу и смотрит на зрителя чуть ехидно.{w} Вот только…"
    show d_sf laugh hike with dspr
    me "Ты меня семнадцатилетним сделала."
    show un smile2 pioneer with dspr
    un "Терпи, я тебя таким вижу."
    show d_sf smile hike with dspr
    me "А можно посмотреть?"
    show un shy pioneer with dspr
    "Лена долго решалась, но разрешила и протянула альбом."
    un "Смотри."
    show d_sf normal hike
    show un normal pioneer
    with dspr
    play sound sfx_open_journal
    "Семён начал листать:{w} Женя с разными выражениями лица,{w} Шурик, поправляющий очки,{w} Максим с горном, сидящий на скамье,{w} тот же Максим, спящий в тени берёзы,{w} две Ульяны, большая и маленькая, хлопающие друг друга пятернями,{w} Ольга Дмитриевна, читающая нотацию среднему отряду."
    show d_sf serious hike with dspr
    me "Когда успела, Лен?"
    show un smile pioneer with dspr
    un "Ну, книги в библиотеке кончились…"
    show d_sf normal hike with dspr
    me "Понятно."
    show un normal pioneer with dspr
    play sound sfx_open_journal
    "Семён, прохаживающийся перед строем футболистов.{w} Семён, держащий за руку Ульяну.{w} Уже виденный Семён у школьной доски.{w} Саша, танцующая с Максимом.{w} Саша на площади, что-то доказывающая Сыроежкину.{w} Саша в спортивной форме на беговой дорожке.{w} Мику за роялем и Мику на собрании отряда — грустная-грустная."
    show d_sf serious hike with dspr
    me "Ты знаешь, что Мику и Шурик проснулись?"
    show un sad pioneer with dissolve_fast
    un "Знаю. И радости им это не доставило."
    show d_sf sad hike with dspr
    un "Помнишь, давно-давно я говорила тебе про занозы в душе. Вот, похоже, они не были готовы к тому, чтобы проснуться, но проснулись из-за машины Шурика, а теперь им очень больно."
    me "Особенно Мику. Ты права."
    show un serious pioneer with dissolve_fast
    un "Но мы же не бросим их?"
    show d_sf normal hike with dspr
    "Семён только кивнул как само собой разумеющемуся, перелистывая страницы дальше."
    show un normal pioneer with dissolve_fast
    "Вот Славя, подметающая площадь…"
    th "Стоп!{w=0.3} Славя?"
    show d_sf serious hike with dspr
    "Семён поднял глаза на Лену."
    show un shy pioneer with dspr
    un "Ну ты рассказывал о девочке, похожей на Сашу. Помощнице вожатой в других лагерях. Вот я и представила себе её."
    "Звучало неубедительно, но…{w=0.5} пусть."
    show d_sf normal hike
    show un normal pioneer
    with dspr
    play sound sfx_open_journal
    "А дальше… Дальше были две Алисы: одна здешняя, а другая из лагеря Виолы — тут ошибиться было невозможно."
    "Они о чём-то спорили яростно, схватив друг друга за пионерские галстуки. Почти на грани драки.{w} Почти — потому что уже ясно: сейчас они ещё поорут друг на друга, выпустят пар, потом одна из Алис хлопнет другую по плечу, и обе рассмеются."
    "А дальше шли уже совсем незнакомые люди. Мальчики, девочки, мужчины, женщины — все набросаны достаточно схематично, но всё же узнаваемо. Под некоторыми подписаны имена, некоторые безымянные."
    me "Лена?"
    show un cry_smile pioneer with dissolve_fast
    "Лена посмотрела на Семёна неожиданно доверчиво. И, как когда-то рассказала ему о себе и Семёне-втором, начала свой рассказ."
    stop ambience fadeout 1

    scene black with dissolve
    pause 0.5
    show promo_text_un u"Рассказ Лены" at truecenter with dspr
    play music twinkling fadein 1
    $ renpy.pause(3.0)
    $ set_mode_nvl()
    window show

    scene anim prolog_1 with dissolve                
    "Всё это началось в прошлом цикле, после той спасательной экспедиции, которую мы с Алисой предприняли в поисках тебя и Ульяны.{w} Я тогда тоже, как ты, решила, что наш мир не может существовать.{w} Только я решила, что он не компьютерная модель, а чья-то фантазия.\n"
    "А потом меня заинтересовал человек, придумавший наш мир.{w} Какое-то время я отбрасывала от себя эту мысль, но снова и снова к ней возвращалась.{w} А дальше приехал мой Семён, и стало уже не до того.{w} В конце цикла, когда мы ехали в автобусе и мой Семён уже уснул, я подумала, что, может, если я пойму этого человека, то я тогда пойму и то, как мне разбудить моего Семёна — ведь он такой же придуманный, как и мы все.{w} И я попыталась на основе того, что знаю о мире, представить себе придумавшего его автора.{w} Так у меня в альбоме появился первый «портрет неизвестного».\n"
    "А потом я поняла, что не может один человек столько выдумать и в голове держать.{w} И появились ещё портреты других людей.{w} Портретов оказалось мало, возникла необходимость в словах.{w} И я пошла к Алиске.\n"
    "И оказалось, что Алиса тоже думала об этом, да так, что за неполный цикл исписала уже полторы тетради.{w} Вдвоём дело пошло веселее, у некоторых «неизвестных» появились имена или хотя бы прозвища.{w} Алиса ещё сказала, что эти прозвища называются «ники»."
    nvl hide dissolve
    nvl clear
    nvl show dissolve 
    "А потом ты унёс мой рисунок в тот, другой лагерь, а через два часа появилась недовольная тем, что её оторвали от каких-то своих дел, Ульяна-маленькая и передала новую работу Мику из того лагеря и её просьбу: «Что-нибудь с этим сделать».{w} Мику написала сказку про маленькую планету. Астероид, прямо как в «Маленьком принце».{w} Маленькую планету, на которой только и есть, что один-единственный пионерский лагерь.{w} На Земле мало кто знает про эту планету, только несколько человек.{w} И вот, пока хоть один человек помнит и думает о той планете, на ней и в лагере всё хорошо.{w} А иначе каждую смену что-то в том мире теряется навсегда.{w} Уменьшается радиус планеты, исчезают пионеры и никто не вспоминает о них, сокращается территория лагеря, становятся короче смены.{w} И так пока не останется каменная глыба астероида, лишённого атмосферы.\n"
    "Но и пионеры в том лагере тоже знают о Земле.{w} Не все, конечно.{w} И тоже, пока они помнят о ней, то всё на Земле хорошо.{w} Ну, не хорошо, конечно, Земля — она вон какая большая, а пионеров вон как мало, но хоть чуточку, но лучше.\n"
    "И вот у нас всё встало на свои места.{w} Никакая мы не модель. Никто нас не придумывал. Есть наши лагеря — Сеть, как вы с Ульяной их называете, есть материнские миры и есть Земля.{w} И всё это связано — через людей.{w} И там, и там, и здесь.{w} И вот мы сейчас переписываем рассказик.{w} То есть переписывают Мику из того лагеря с нашей Алиской, а я так, на подхвате — почитать, покритиковать, иллюстрации сделать.{w} И Ульянка-маленькая, она — наш почтальон."
    stop music fadeout 1

    scene black with dissolve_fast
    window hide

    scene bg ext_square_night
    show un serious pioneer at left:
        ycenter 0.65
    show d_sf normal hike at right:
        xzoom -1 ypos 0.12
    with dissolve_fast
    play ambience ambience_camp_center_night fadein 1
    $ set_mode_adv()
    window auto
    un "И ещё в рассказе Мику те пионеры, что знают о Земле, рано или поздно, но уходят туда."
    show un angry2 pioneer with dspr
    extend " Понятно?"
    show d_sf serious hike with dspr
    me "Да, Лен. Понятно."
    show d_sf smile hike
    show un serious pioneer
    with dspr
    me "Девочки, вы умницы.{w} Это лучше моего компьютера.{w} Я горд тем, что дружу с вами."
    show un shy pioneer with dissolve_fast
    me "И если всё это правда, я не хочу, чтобы вы, то есть мы, там потерялись."
    "Семён махнул рукой куда-то за горизонт."
    show un normal pioneer
    show d_sf normal hike
    with dspr
    un "Если всё это правда, то не потеряемся."
    show un smile pioneer with dspr
    un "Говорят, беженцы из Атлантиды всегда узнавали друг друга."
    show d_sf smile hike with dspr
    un "Ну, спокойной ночи. Вон и Ульяна идёт."
    pause 0.5
    show d_us normal sport_windbreaker with dissolve:
        xcenter 0.54 ycenter 1.04 rotate 15.5
    us "Это хорошо, что ты здесь, Лен. Мне чтобы два раза не рассказывать. Знаете, какой завтра день?"
    show d_sf serious hike with dspr
    me "Воскресенье. Восьмой день цикла."
    show un shy pioneer with dspr
    un "Завтра приезжает мой Семён."
    show d_sf normal hike with dspr
    us "Ты, Лена, почти правильно ответила. Завтра приезжают автобусы во все лагеря."
    show un normal pioneer
    show d_us serious sport_windbreaker
    with dspr
    us "И барьеры между мирами будут проницаемыми. Одним словом, я ещё подумаю, что тут можно сделать."
    show d_us normal sport_windbreaker with dspr
    extend " И сестрёнка подумает. И Алиса подумает."
    show d_us smile sport_windbreaker with dspr
    extend " А сейчас — пошли спать, Сёмк."
    stop ambience fadeout 1

    scene black with dct_fade
    play sound_loop ambience_int_cabin_night fadein 1
    pause 0.3
    d_jn "Па, а зачем я?"

    scene dct_int_house_of_el_night:
        blur 25
    show d_jn:
        xalign 0.5 yalign 0.3 blur 50
    show unblink
    pause 2
    show blink
    pause 1.3
    d_jn "Па, а зачем я?"
    hide blink
    show unblink
    show dct_int_house_of_el_night:
        pause 1
        linear 1 blur 0
    show d_jn:
        pause 1
        linear 1 blur 0
    "Шурик нащупал на стуле очки и глянул на фосфоресцирующие стрелки часов: «вчера» уже закончилось, а «сегодня» потихоньку вступало в свои права."
    sh "Ян, давай днём."
    d_jn "Нет, сейчас."
    play sound sfx_bed_squeak2
    "Пришлось вылезать из-под одеяла, натягивать шорты и идти на крыльцо, чтобы не разбудить Электроника."
    sh "Счастье твоё, Яна, что сегодня воскресенье и можно спать до девяти утра."
    play sound sfx_door_squeak_light
    stop sound_loop fadeout 1

    scene dct_ext_house_of_el_night with slideawayup
    play ambience ambience_camp_center_night fadein 1
    "Шурик прислушался к своим ощущениям.{w} Нет, признаков присутствия Александра в голове не наблюдалось, хотя часть его привычек, черт характера и ключевые воспоминания перешли к дубликату."
    th "Покоя тебе, где бы ты ни был."
    show d_jn with dissolve_fast:
        xalign 0.5 yalign 0.3
    stop ambience fadeout 1
    play music fm_freemusic_chillout_music fadein 2
    d_jn "Па, а зачем я?"
    "Нужно было отвечать."
    th "Я не должен чувствовать вину, но мне стыдно."
    th "Всё проделано Александром. Пусть руками старого Шурика, но Александром."
    th "Старый Шурик был такой же технической личностью, как и Яна, но мне всё равно стыдно."
    sh "Яна, ты для того, чтобы исчезнуть, умереть.{w} Ты должна была собрать рассеянную в Системе информацию…"
    "Шурик говорил долго, рассказывая то, что он вытащил из памяти Александра."
    sh "…а потом лишённый памяти робот бестолково ходил бы по Шлюзу, пока у него не кончился бы заряд. Не удерживаемое ничем, нейтринное кольцо вылетело бы из ловушки, а связь с Системой оборвалась. И всё. Для тебя всё."
    "Про то, что для Шурика это тоже было бы всё, он умолчал."
    th "Вот теперь я Яне ничего не должен."
    th "Теперь я ей должен только то, что хочу дать."
    extend " Надо бы ей ухо поправить и полировку восстановить."
    th "И повоспитывать чуть-чуть, чтобы не будила в пять утра."
    "А Яна замерла неподвижно, только повернув голову так, чтобы держать Шурика в поле зрения обоих оптических датчиков."
    th "Интересно, о чём она думает? Надо бы ей сказать, чтобы не замирала надолго, что неприятно так с ней разговаривать."
    th "Яна, ты когда замираешь — шевели чуть-чуть какой-нибудь частью тела, чтобы понятно было, что ты не статуя, а живая."
    extend " Живая? "
    extend "Да, живая!"
    d_jn "Па, это не то. Это я и сама знала. Твоя старшая личность не зашифровала программу."
    th "Вот, значит, как. Моя старшая личность."
    sh "И ты спокойно об этом говоришь?"
    d_jn "Это было моё предназначение."
    "Шурик не удержался и притянул Яну к себе."
    show d_jn with dissolve_fast:
        zoom 1.25 yalign 0.33
    extend " Удивительно, но металлический корпус не холодил руку и тело. Удивительно, но Яна приняла это как должное, переступив поближе к Шурику и опустившись рядом с ним на крашеные доски."
    d_jn "Па, я решила, что это предназначение — ложное. И теперь я ищу, зачем я."
    th "Дожили: робот спрашивает о смысле жизни."
    "Если бы кто-то, хорошо знающий Шурика, хоть тот же Семён, сейчас наблюдал за ним, он очень бы удивился — Шурик смеялся."
    sh "Дочка…"
    "Cлово было произнесено неожиданно, легко и — неожиданно легко."
    sh "Дочка, ты задаёшь такой вопрос, на который отвечает, даже для самих себя, едва ли десятая часть всех людей.{w} И то многие только в конце жизни. А большинство живёт не думая, просто как трава растёт."
    d_jn "Я поняла, па. Тогда я буду думать над этим."
    d_jn "Я бы поцеловала тебя сейчас, но не могу. Конструкция не позволяет."
    show d_jn:
        pause 0.6
        linear 1 alpha 0
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    extend " Над конструкцией я тоже буду думать."
    stop music fadeout 1

    scene black with dissolve_fast
    pause 0.5
    $ day_time()
    $ persistent.sprite_time = "day"

    scene bg ext_playground_day with dissolve_fast
    play ambience ambience_camp_entrance_day fadein 1   # Тут специально амбиенс не от спортплощадки, потому что на ней никто не играет.
    "Сашка закончила нарезать круги по стадиону."
    play sound "<from 2.9>" + sfx_slavya_run fadein 1.5
    $ renpy.pause (2.2)
    show sl sad sport far with easeinleft:
        xanchor 0.0 xpos 0.15
    th "А пионеры спят."
    extend " Пользуются тем, что сегодня нет линейки и можно спать до завтрака. И спят."
    show d_us hurt sport at fright:
        ypos 0.09 alpha 0
        linear 1 alpha 1
    th "Вот и Ульяна зря сидит и ждёт желающих провести зарядку."
    show 3500_sl smile3 sport as sl with dspr:
        zoom 0.75
    sa "Доброе утро."
    show d_us normal sport with dspr
    us "Ага, привет."
    "Ульяна зевнула."
    us "Я тут убегаю до завтрака, и после завтрака до обеда. Не обижайте Сёмку без меня."
    show sl smile2 sport far with dissolve_fast:
        zoom 1.0
    sa "Я могу тебе помочь?"
    show d_us shy sport with dspr
    us "Ты?"
    "Она пожала плечами."
    show d_us normal sport with dspr
    us "Нет. Но спасибо."
    hide d_us
    show sl sad sport far
    with dissolve
    "Ульяна удалилась куда-то в сторону хозяйственных ворот.{w} Саша вздохнула. Чувствовалось, что Ульяна всеми силами старается поддерживать от неё дистанцию, а причина была непонятна."
    show sl normal sport far with dissolve_fast
    "Но насильно мил не будешь, и, поскольку Ульяна никогда не показывала своего недовольства, Саша тоже не лезла выяснять отношения. Потому что всего через неделю смена закончится, и кто знает, удастся ли приехать в этот лагерь на следующий год?"
    hide sl with dissolve
    stop ambience fadeout 1

    scene bg ext_dining_hall_away_day with pushright
    play sound_loop ambience_camp_center_day fadein 1
    pause 0.3

    scene bg ext_square_day with pushright
    "Спорткомплекс, столовая, площадь… Нигде ни души, и только на площади случилась остановка."

    scene dct_ext_square_profile_view_day
    show d_ma shy pioneer:
        zoom 0.75 xcenter 0.9 yalign 1.01
    with dissolve
    show 3500_sl smile3 sport as sl:
       zoom 0.75 xcenter -0.1
       easein 1.8 xcenter 0.66
    pause 0.5
    d_ma "Привет. Я уже привык, оказывается, в семь утра трубить подъём. И сбор в восемь утра. А сегодня не надо, надо только в девять — на завтрак."
    show 3500_sl smile3 sport as sl:
       zoom 0.75 xcenter 0.66
    show d_ma serious pioneer
    with dissolve_fast
    d_ma "А я вскочил и прибежал, ещё думал, что проспал. И только здесь опомнился. Так глупо. Сосед смеяться будет."
    show sl happy sport far at cright with dissolve_fast:
        zoom 1.0
    sa "Ничего, Максимка. Зато я теперь стала лучше думать о пионерах — не все из них, оказывается, спят до завтрака."
    show sl smile sport far with dissolve_fast
    sa "Пошли умываться, раз уж не спишь."

    scene bg ext_musclub_day with pushright
    "Неизвестно зачем, проходя мимо музыкального кружка, они решили заглянуть в окно.{w} Неизвестно зачем, увидев Мику за роялем, они решили заглянуть на минутку и поздороваться."

    scene dct_ext_music_club_verandah_opendoor_day
    show d_ma smile pioneer at right:
        yalign 0.02
    with dissolve
    "Максим чуть отстал от проскользнувшей вперёд Сашки и, может быть, даже так бы и прождал её на веранде, если бы не…"
    show d_ma surprise pioneer with dspr
    stop sound_loop fadeout 1
    play music music_list['you_lost_me'] fadein 2
    sa "Максииим!"

    scene bg int_musclub_day with slidedown
    "Мику играла.{w} Руки бегали по клавишам, голова чуть покачивалась в такт музыке, спина наклонялась то вправо, то влево.{w} Губы её шевелились, а на щеках блестели влажные следы слёз.{w} Но рояль не издавал ни звука, пальцы проваливались сквозь неподвижные клавиши, а сквозь тело Мику начинал просвечивать интерьер кружка."
    show d_ma surprise pioneer at left:
        zoom 0.75 yalign 1.01
    show sl scared sport at right
    show mi cry pioneer close at center:
        alpha 0.7
    with dissolve
    "«Привидение!» — первое, что подумал Максим."
    show mi cry pioneer close:
        linear 2 alpha 0.6
    show sl scared sport close at cright with dissolve_fast
    "А белая как мел, отчаянно трусящая Сашка не думала ни о каких привидениях, а бросилась к Мику." #, обнимая её.
    stop music fadeout 2
    show mi cry pioneer close:
        linear 2 alpha 0.5
    show d_ma surprise pioneer at cleft with dissolve_fast:
        zoom 1.0 yalign 0.02
    "Неизвестно, что сработало — инстинкт или Сашина скрытая память о том, как она сама начала похоже растворяться после контакта с Пионером."
    play music music_list['memories_piano_outdoors'] fadein 2
    show d_ma surprise pioneer with dissolve_fast:
        zoom 1.25 yalign 0.08
    show mi cry pioneer close:
        linear 2 alpha 0.4
    "Но дальше они вместе с Максимом уже крепко обнимали Мику с двух сторон за поролоново-мягкие, но уже постепенно твердеющие и набирающие плотность плечи."
    show mi scared pioneer close with dspr:
        linear 5 alpha 1.0
    "А Сашка пронзительно кричала:"
    pause 0.5
    sa "Мику, останься!"
    stop music fadeout 1

    scene bg ext_dining_hall_near_day with dct_fade
    play sound_loop ambience_camp_center_day fadein 1
    "Женя обогнула стайку пионеров из среднего отряда, изучающих график посещения бани, и зашла в столовую."
    stop sound_loop fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    show int_dining_hall_people_day with pushright
    "Помахала рукой Серёже, стоящему в очереди к раздаче, и пошла отвоёвывать столик на двоих."
    show d_sf smile sport:
        xcenter 0.55 ypos 0.2 alpha 0
        linear 1 alpha 1
    show d_us smile sport:
        xcenter 0.75 ypos 0.09 alpha 0
        pause 0.5
        linear 1 alpha 1
    show dv smile pioneer at cleft:
        ycenter 0.66 alpha 0
        pause 1.0
        linear 1 alpha 1
    "Семён с Ульяной и Алиса с ними за одним столиком что-то спокойно обсуждали." # Немного отсебятинки
    hide d_sf
    hide d_us
    hide dv
    with dissolve
    show mi grin pioneer far:
        xcenter 0.55 ycenter 0.72 alpha 0
        linear 1 alpha 1
    show sl laugh pioneer far:
        xcenter 0.4 ycenter 0.74 alpha 0
        pause 0.4
        linear 1 alpha 1
    show d_ma laugh pioneer:
        zoom 0.75 xcenter 0.25 ycenter 0.78 alpha 0
        pause 0.8
        linear 1 alpha 1
    show un smile pioneer far:
        xcenter 0.1 ycenter 0.73 alpha 0
        pause 1.2
        linear 1 alpha 1
    "Мику, Саша, Максим и Лена сидели вместе за соседним столом."
    "Мику была необычно осунувшаяся и бледная, но улыбалась и ела с аппетитом, как будто выздоравливая после тяжёлой болезни."
    show d_cs smile glasses far:
        zoom 0.8 anchor (0.5, 0.9) pos (1.1, 0.975) rotate 0.0 transform_anchor True
        linear 0.6 pos (1.035, 0.975) rotate -17.5 transform_anchor True
    "Доктор, кстати, поглядывала на Мику с лёгким профессиональным интересом."

    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show mz normal pioneer close:
        xcenter 0.39 ycenter 0.4
    show dct_int_dining_hall_table_day_front
    with fade
    show el laugh pioneer close behind dct_int_dining_hall_table_day_front:
        xcenter 1.25 ycenter 0.22
        linear 0.9 xcenter 0.76
        pause 0.15
        linear 0.5 ycenter 0.47
    play sound "<from 0.5>" + dct_sfx_chair     
    el "Вот и я, с добычей." 
    show mz smile pioneer close with dissolve_fast:
        xcenter 0.4
    mz "Приятного аппетита."
    show d_mz sceptic pioneer close as mz:
        xcenter 0.39
    show d_el shy3 pioneer close as el
    with dissolve_fast
    mz "Что нового, Серёжа?"
    show el normal pioneer close with dspr
    el "Нового? Шурик что-то затеял, но пока меня в секреты не посвящал.{w} Вставал ни свет ни заря, и сейчас позавтракал вперёд всех и куда-то убежал."
    mz "Будешь ему помогать?"
    show el sad pioneer close with dissolve_fast
    el "Ох, Женька."
    show d_mz hope pioneer close as mz with dspr
    mz "Если позовёт — помогай. Я знаю, для тебя это важно."
    show int_dining_hall_people_day with dissolve
    "Поток пионеров от входных дверей к раздаче постепенно иссякал."
    "Последней зашла Ольга Дмитриевна, взяла на раздаче кусок хлеба, положила на него вчерашнюю холодную котлету, накрыла вторым куском и с этаким гамбургером в одной руке и стаканом какао в другой прошла за столик к Семёну."
    "Какое-то время было тихо, только иногда брякали вилки о тарелки да стоял равномерный шум, обычный для столовых в час пик."
    show el grin pioneer close
    show mz normal pioneer close
    hide int_dining_hall_people_day with dissolve
    el "Жень, давай ты библиотеку сегодня не будешь открывать."
    show d_mz fun pioneer close as mz with dspr
    mz "Я и не собиралась."
    show el smile pioneer close with dspr
    extend " Всё равно никого не будет. Воскресенье же: уборка, стирка, баня и так далее."
    show d_mz excitement pioneer close as mz with dissolve_fast:
        xcenter 0.4
    mz "Скажи, а ты умеешь грести?"
    show d_el shy pioneer close as el with dspr
    pause 0.2
    stop ambience fadeout 1

    scene black with dissolve_fast
    pause 1

    scene dct_dv_mirror
    play music music_list['my_daily_life'] fadein 1
    show black:
        alpha 1
        pause 1.0
        linear 1 alpha 0
    "Перетаскивающая вещи Алиса старательно делала злобное лицо, но на самом деле была страшно довольна."
    th "Что тут у нас осталось?"
    extend " Полный шкаф платьев?"
    show dct_closet_with_dresses with dissolve:
        yalign 0.0
    th "Интересно, для чего человеку столько платьев, если их ни разу не надевали?"
    show dct_closet_with_dresses:
        ease 2 yalign 1.0
    "Взять эти платья, постараться сложить их покомпактнее и закинуть охапку на плечо. В руки дополнительно взять картонную коробку с чайными чашками, сахаром, печеньем и мелким барахлом."

    scene dct_ext_houses2_day
    show dv angry pioneer:
        xcenter 0.17
    show d_ma normal pioneer:
        xcenter 0.5 yalign 0.02
    with dissolve
    "Выйдя из домика, столкнуться с Максимом."
    d_ma "Алиска, тебе помочь?"
    "Сдуть локон со лба."
    show dv shy pioneer with dissolve_fast:
        xcenter 0.18
    dv "Своё таскай."
    "Ну Максим и таскал своё.{w} А что своё? Походный рюкзак, с которым он приехал, и пару удочек."
    show dv guilty pioneer with dspr
    dv "Ты что, на рыбалку ходишь?"
    show d_ma smile pioneer with dissolve_fast
    d_ma "Если получается."
    show dv grin pioneer with dissolve_fast:
        xcenter 0.16
    dv "Пойдёшь — меня позови."

    scene black with squares
    show mt smile pioneer close with dissolve:
        xcenter 0.38
    mt "Я, между прочим, в твоих интересах всё решила."
    show mt grin pioneer close with dissolve_fast
    extend " Так что, Алиса, таскать тебе."
    hide mt with dissolve
    "Вот Алиса и таскала."

    scene bg ext_houses_day with squares
    th "Сразу с крыльца повернуть направо, через два домика налево, ещё раз налево и опять через два домика направо."
    th "Прочь с дороги, иду по приборам, а то из-за этих чёртовых платьев ничего не видно."

    scene dct_ext_сentral_alley_from_dining_hall_to_west
    show d_sf normal pioneer at cleft
    with dissolve
    th "А вот и Сенька. Тоже сегодня в роли грузчика."
    th "Тяжёлое ему Ульяна таскать запретила, поэтому у него ходок больше выйдет."
    show d_sf serious pioneer
    extend " Но ему таскать проще — всё по главной аллее."
    th "Ну Ольга, ну реформатор."
    extend " А сама сейчас на пляже."

    scene bg ext_houses_day with squares:
        xzoom -1
    show dv normal pioneer at right:
    show d_ma normal pioneer at cleft:
        yalign 0.02
    with dissolve
    dv "Сенька, не хватайся за коробку, она лёгкая. Лучше дверь открой."
    show dv smile pioneer with dspr
    extend " Как там наша Рыжая?"
    me "Обещала к двенадцати."
    dv "Значит, один час у нас ещё есть."
    show dv laugh pioneer with dspr
    show d_ma grin pioneer at cleft as d_ma2:
        yalign 0.02 alpha 0
        pause 1.1
        linear 0.2 alpha 1
    extend " Таскай давай. Круглое тащи, квадратное кати."

    scene black with dissolve
    show mt smile pioneer close with dissolve:
        xcenter 0.38 alpha 0
        linear 1 alpha 1
    th "Но Ольга всё равно молодец, я ей даже дерзить до конца цикла не буду."
    show mt sad pioneer close as mt2:
        xcenter 0.38 alpha 0
        pause 0.25
        linear 0.25 alpha 1
    extend " Наверное."
    stop music fadeout 1

    scene dct_int_dining_hall_table_day_back_people
    show mt normal pioneer close:
        xcenter 0.38
    show dct_int_dining_hall_table_day_front
    with blinds
    play sound_loop ambience_dining_hall_full fadein 1
    mt "Ну как, готова к переезду?"
    dv "Нет."
    show mt smile pioneer close with dspr
    mt "А придётся."
    play sound "<from 1.2>" + dct_sfx_chair     
    show mt smile pioneer close:
        linear 0.55 ycenter 0.23

    scene int_dining_hall_people_day
    show mt normal pioneer:
        xcenter 0.5 ycenter 0.7
        linear 0.5 ycenter 0.5
    with dissolve_fast
    mt "Пионеры и к ним примкнувшие, минутку внимания."
    mt "Во-первых, с сегодняшнего дня наш горнист уже официально переводится в старший отряд."
    "Свист, улюлюканье, шум аплодисментов."
    show mt grin pioneer
    show d_ma laugh pioneer:
        zoom 0.75 xcenter 0.85 yalign 1.01
    with dissolve_fast
    "Максим, встав со своего места, шутовски раскланивается."
    show d_ma shy pioneer with dissolve_fast
    extend " Ловит взгляд Алисы и подмигивает."
    show mt smile pioneer
    hide d_ma
    with dissolve_fast
    show mt normal pioneer with dspr
    mt "Но это ещё не всё."
    mt "Я решила навести порядок с проживанием персонала."
    show mt smile pioneer with dspr
    extend " И отдельных пионеров тоже."
    stop sound_loop fadeout 1
    play ambience ambience_int_cabin_day fadein 1
    show dct_int_chief_corridor_day with squares
    "И вот, командирским решением Ольга, две поварихи из трёх и Персуновы сейчас переселяются в административный корпус."
    stop ambience fadeout 1

    scene bg ext_house_of_mt_day with dissolve    
    play ambience ambience_camp_center_day fadein 1
    "Максим и Семён-второй, который, кстати, ещё не приехал, поселяются в бывшем домике Ольги."
    show dv grin pioneer at right:
        alpha 0
        pause 1
        linear 1 alpha 1
    "Но таскать Ольгины вещи приходится Алисе — невеликая цена за то, чтобы остаться жить в своём домике."
    show dv normal pioneer with dissolve_fast
    th "А ведь есть и минусы. Теперь вот так запросто к Сеньке с Рыжей не забежишь: всегда есть шанс нарваться на вожатку."
    show dv laugh pioneer with dspr
    extend " Ну ничего, у меня будем собираться."
    stop ambience fadeout 1

    scene dct_int_chief_corridor_day with blinds
    play sound_loop ambience_int_cabin_day fadein 1
    "Всё, последняя ходка была, дальше уж пусть сама вожатая разбирается, чего и куда повесить."

    scene dct_int_residential_block_day with dissolve
    play sound sfx_drop_alisa_bag
    "Алиса и Максим скинули охапку платьев на незастеленный матрац и огляделись."
    th "А ведь неплохо можно устроиться."
    "Всё очень маленькое, но своё. Даже ванная с душем и кухонная ниша с плиткой. Хочешь — питайся и мойся отдельно, хочешь — ходи в столовую и в баню."
    show dct_int_chief_corridor_day with dissolve
    "Алиса вышла в коридор и просунула голову в дверь Семёновой комнаты.{w} Тот сидел на кровати, утирая лоб, и тоже оглядывал помещение, прикидывая явно, как и куда сдвинуть вместе две кровати."
    $ renpy.music.set_volume(1.0)
    play music dreamers_of_the_day fadein 2
    dv "Ну что, идём?"
    me "Идём, Алиса."
    stop sound_loop fadeout 1

    scene bg ext_path2_day with dct_fade
    show un smile pioneer far:
        xcenter 0.41
    show sl smile dress far:
        xcenter 0.59
    with dissolve
    "Осведомлённые или приглашённые пионеры и к ним примкнувшие из двух лагерей поодиночке, парами и тройками, стараясь не привлекать внимания, исчезали за забором и тянулись к костровым полянам."
    hide un
    hide sl
    with dissolve

    scene bg ext_path_day with fade
    show d_sz normal pioneer:
        zoom .75 xcenter .42 yalign 0.1
    show d_oz smile pioneer:
        zoom .75 xcenter .75 yalign 0.1
    show mi normal pioneer far:
        xcenter .58
    with dissolve
    "Не все — в основном старший отряд и чуть-чуть мелких, оставляя на часок лагеря на произвол судьбы."
    hide mi
    hide d_sz
    hide d_oz
    with dissolve

    scene dct_ext_glade_behind_clubs_day with fade
    show sh normal_serious pioneer far dct at right with dissolve
    pause 0.5
    show sh serious pioneer far with dissolve_fast
    show sh serious pioneer far at fleft with MoveTransition(1.5):
        alpha 1
        pause 0.6
        linear 0.8 alpha 0
    $ day_time()                      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "А всё потому, что вчера вечером Семён изрёк:"
    play ambience ambience_camp_center_night fadein 1.5
    hide sh
    $ renpy.music.set_volume(0.25, delay=2)
    $ night_time()
    $ persistent.sprite_time = "night"

    scene bg ext_square_night
    show un normal pioneer at left:
        ycenter 0.65
    show d_sf smile hike at right:
        xzoom -1 ypos 0.12
    show d_us normal sport_windbreaker:
        xcenter 0.54 ycenter 1.04 rotate 15.5
    with blinds
    me "Между прочим, костровая поляна выглядит абсолютно одинаково во всех узлах, где я побывал."
    me "Как говорится, видел одну — видел все."
    show d_sf laugh hike with dspr
    extend " Есть ещё несколько мест, но поляна симпатичнее всего, не в пещеру же спускаться."
    show un shy pioneer with dspr
    "За что был вознаграждён приглушённым, но восторженным воплем Ульяны:"
    show d_us laugh sport_windbreaker
    show d_sf smile hike
    with dspr
    us "Гениально, Сёмка!"
    show d_us smile sport_windbreaker
    show un smile pioneer
    with dspr
    extend " Хоть ты, конечно, тормоз."
    show d_us serious sport_windbreaker
    show d_sf normal hike
    with dspr
    $ night_time()                      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Почему раньше не догадался?"
    show d_us smile sport_windbreaker
    show d_sf sad hike
    show un smile2 pioneer
    with dspr
    pause 0.3
    stop ambience fadeout 1
    $ renpy.music.set_volume(1.0, delay=1)

    scene ext_bus
    show dct_ext_bus_alone_passenger:
        anchor (0.0, 1.0) pos (0.1, 0.5)
    show dct_ext_сentral_alley_from_dining_hall_to_west:
        xcenter 0.5
    show ext_square_day:
        xcenter -0.5
    show dct_ext_camp_entrance_day:
        xcenter -0.5
    with blinds
    $ day_time()
    "Всё когда-нибудь бывает впервые."
    show dct_ext_сentral_alley_from_dining_hall_to_west:
        linear 1 xcenter 1.5
    show ext_square_day:
        linear 1 xcenter 0.5
    extend "{w=1} Впервые обитатели двух узлов нашли способ встретиться."
    show ext_square_day:
        linear 1 xcenter 1.5
    show dct_ext_camp_entrance_day:
        linear 1 xcenter 0.5
    extend "{w=1} Сеть начинала жить новой, самостоятельной, невозможной, но нормальной жизнью."
    stop music fadeout 4
    play ambience ambience_camp_entrance_day fadein 3
    $ renpy.sound.set_volume(0.3, delay=0)
    play sound sfx_bus_stop fadein 1.5
    show dct_ext_camp_entrance_day:
        pause 3
        linear 1 alpha 0
    $ persistent.sprite_time = "night"
    "И никто из заинтересованных лиц не услышал, как на остановке зафырчал приехавший на три часа раньше положенного срока Икарус."
    hide dct_ext_сentral_alley_from_dining_hall_to_west
    hide ext_square_day
    hide dct_ext_camp_entrance_day
    show dct_uv_peeping:
        anchor (0.25, 0.15) pos (-0.13, 0.68) rotate -12 transform_anchor True
        pause 0.6
        easeout 0.9 pos (0.01, 0.47) rotate 5.5 transform_anchor True
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
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound3')
    
    
    
#############################
#Глава 12. Монетка в фонтане#
#############################

label dct_coin_final_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Финал"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    window auto
    scene black
    stop ambience
    stop sound_loop
    play music music_list['mystery_girl_v2']
    play sound dct_sfx_uv_call
    show headline_text2 u"Глава XII. Монетка в фонтане" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    scene dct_int_bus_shimmer                   # Сцена в автобусе с переливами красок
    show dct_uv_coin_bus                        # Включение Юлек
    show dct_coin_bus_sparkle_a                 # Включение сверканий
    show dct_coin_bus_sparkle_b
    show dct_coin_bus_sparkle_c
    show dct_coin_bus_sparkle_d
    show dct_coin_bus_sparkle_e
    show dct_wave_left_to_up:                               # Запуск волн
        alpha 0 xcenter 0.15 yalign 0.0
        ease_quad 21.0 alpha 1 xcenter 0.5 yalign 1.0
    show dct_wave_right_to_down:
        alpha 0 xcenter 0.85 yalign 1.0
        ease_quad 21.0 alpha 1 xcenter 0.5 yalign 0.0
    $ renpy.pause(18,hard=True)
    show dct_uv_coin_bus_asked at center with dissolve2     # Юля задаёт вопрос
    $ renpy.pause(2,hard=True)

    scene dct_d1_uv with dissolve
    stop sound fadeout 3.5
    uvp "Ты пойдёшь со мной?"
    show dct_uv_coin_bus_shocked_1     # Псевдокартинка, подставляющая другую картинку, но с паузой
    show dct_uv_coin_bus_shocked_2     # ----------//-----------
    show dct_uv_coin_bus_shocked_3     # ----------//-----------
    stop music fadeout 1
    my "БРЫСЬ!"

    scene bg int_bus
    show uv shocked
    show uv guilty with dissolve_fast
    my "Юля, ты же знаешь, что со мной это не сработает. Тем более в этом варианте «Совёнка»."
    show uv smile with dissolve_fast
    uv "Знаю."
    show uv laugh with dissolve_fast
    "Юля подумала, не сделать ли вид, что обижена, но потом улыбнулась."
    show uv grin with dspr
    pause 0.25
    show uv laugh with dspr
    uv "Это всё потому, что я не материализовавшееся подсознание и не ходячий портал, а всего-лишь кошка-мутант."
    my "Ага. Была бы ты на самом деле кошкой — ты бы об этом не задумывалась."
    $ renpy.music.set_volume(0.25)
    play music music_list['mystery_girl_v2'] fadein 2
    show uv smile close with dissolve
    my "Животным, знаешь, по барабану. Так что смирись с тем, что ты — человек."
    $ renpy.music.set_volume(0.5, delay=2)
    show dct_uv_coin_bus_asked as uv with dissolve
    "Наклонилась надо мной, загораживая весь обзор и глядя мне прямо в глаза. Зрачки расширились, готовится все свои чары выпустить. А я делаю рывок и целую Юлю в нос."
    stop music fadeout 1
    show uv sad close with dissolve_fast
    extend " Хотел в губы, но она дёрнулась и получилось в нос. Ну, тоже неплохо."
    show uv smile close with dspr
    uv "Ну вот, всю таинственность момента нарушил. Ладно, пойду."
    show uv smile with dspr
    uv "Скоро Славя придёт — не люблю, когда меня видят. Я, в конце-концов, как там у тебя: «кошкодевочка, легенда лагеря», и должна являться избранным и в критические минуты."
    show uv smile far with dspr
    uv "Ещё увидимся, пока."
    my "Мяу!"
    show uv laugh far with dissolve_fast
    uv "Не дразнись!"
    hide uv with dissolve
    "И убежала."
    $ renpy.music.set_volume(1.0)
    play music fm_freemusic_chillout_music fadein 4
    "А я выхожу в проход между сиденьями, подбираю пакет и свитер. Пальто, кажется, нужно оставить, а вот телефон не забыть."
    "Или смартфон?{w=0.5} Или МР3-плеер?{w=0.5} Под моим взглядом старенькая кнопочная Нокия начинает увеличиваться в размерах, экран у неё наползает на кнопки…"
    "Кручу головой: «Отставить!». Телефон возвращается к привычному облику. М-да, и вот пошёл бы я такой за Юлей — я бы натворил там дел, в лагере-то."
    "А так…"

    scene dct_int_bus_rightwindow_day with pushleft
    "Пригибая шею, смотрю в окна автобуса — снаружи всё как положено: приоткрытые ворота с прорезанной звездой, надпись «Пионерлагерь Совёнок», два гипсовых пионера, кирпичный забор, лес по обе стороны забора, автобусная остановка."
    show dct_int_bus_rightwindow_day:
        linear 1 xcenter 1.5
    show int_bus:
        xcenter -0.5
        linear 1 xcenter 0.5
        linear 1 xcenter 1.5
    show dct_int_bus_leftwindow_day:
        xcenter -0.5
        pause 1
        linear 1 xcenter 0.5
    show dct_int_bus_leftwindow_day_wheat_Maya:
        xcenter -0.5
        pause 1
        linear 1 xcenter 0.5
    pause 2
    "Оглядываюсь назад: дорога, убегающая в холмы, ЛЭП, то ли поля, то ли луга, непонятно."

    scene bg ext_camp_entrance_day with slideawayleft
    play ambience ambience_camp_entrance_day fadein 2
    "Оставляю вещи в автобусе, а сам выхожу. Не стоит заставлять Славю ждать."
    show d_sl smile pioneer at center with dissolve_fast:
        zoom 0.75
    sl "Привет, ты, наверное, только что приехал?"
    my "Славюшка, ты же давно уже проснулась. А всё повторяешь так, как тебя научили."
    stop music fadeout 3
    show d_sl surprise pioneer with dissolve_fast
    "Какая она всё-таки красавица: смотрю в эти глаза и чуть не тону в них."
    show d_sl scared pioneer with dissolve_fast
    sl "Ты… Ты… Это ты приехал?! Так что ж стоишь, пойдём скорее."
    show d_sl happy pioneer with dissolve_fast:
        zoom 1.0 ycenter 0.83
    th "Рад бы, но нет. Внутрь мне нельзя — я сам себе такое правило установил, и поэтому я его выполню."
    "Вспоминаю трансформацию телефона."
    th "Здесь я ещё сдерживаюсь, а внутри — боюсь, что не смогу. И дело не только в пионерлагере, но и, по закону отдачи, во мне самом."
    my "Нет, Славюшка, туда мне вход заказан."
    show d_sl shy pioneer with dspr
    sl "Тогда подожди, я быстро. Мы быстро!"
    show d_sl smile2 pioneer with dissolve_fast:
        zoom 0.75 yalign 0.0
    "Срывается с места к воротам. Внезапно что-то вспоминает, останавливается, разворачивается и бежит ко мне."
    show d_sl tender pioneer close with dissolve_fast:
        zoom 1.0
    "Виснет у меня на шее и целует. Вот у Слави получилось в губы. Устами сахарными, именно."
    show d_sl laugh pioneer close with dissolve_fast
    sl "Пока никто не видит!"
    show d_sl normal pioneer close with dissolve_fast
    sl "И не думай ничего такого, это тебе от всех нас!"
    show d_sl happy pioneer close with dissolve_fast
    sl "Другие-то постесняются."
    show d_sl shy pioneer close with dspr
    sl "И обязательно дождись!"
    show d_sl smile2 pioneer close with dspr
    sl "Или нет — костровую поляну знаешь? Подходи туда через час!"
    hide d_sl with dissolve
    "И бегом, в темпе, приличном Ульянке-маленькой, а не помощнице вожатой, скрывается за воротами."
    th "Конечно, знаю, конечно, подойду — затем я тут и оказался."

    scene dct_ext_bus_road
    show dct_ext_bus_road_wheat_Maya
    with pushright
    "Присаживаюсь на лавочку: до поляны двадцать минут хода, так что полчаса свободного времени у меня ещё есть."
    "Или я лучше даже прилягу. Устраиваюсь у ног правого пионера в удивительно непыльной и мягкой здешней траве, закидываю руки за голову и лежу, разглядывая облака."
    "Как их называют? Цирусы, если я правильно вспомнил. Когда я ещё здешнее небо увижу?"
    play music badstory fadein 2
    show pi normal at cright:
        alpha 0.0
        pause 1
        linear 2 alpha 0.7
    pi "Спасибо, что не стал описывать меня как абсолютного злодея."
    "Облака загораживает фигура, вставшая надо мной башней."
    "Пионер. Визитёр третий, виртуальный. Через него небо просвечивает, значит — виртуальный."
    my "Пожалуйста. Абсолютных злодеев вообще не бывает. А ты и на относительного злодея не тянешь."
    pi "Любопытно, а на кого же я тяну? Как ты меня характеризуешь?"
    my "Как, в общем-то, неплохого человека, загнавшего себя в причинно-следственную воронку событий."
    my "Каждый твой шаг сужал тебе поле для манёвра, и ты в итоге оказался там, где оказался."
    my "И вот за последствия того, что ты загнал или позволил загнать себя в эту воронку, ты и должен нести ответственность."
    my "А ведь и нужно было тебе, когда всё началось, всего-то встать на чужое место и посмотреть оттуда."
    pi "Мудрёно.{w=0.5} Но, прощай."
    show pi:
        linear 2 alpha 0.0
    my "Прощай."
    stop music fadeout 3
    th "Интересно, в какой материнский мир из всего пакета его тогда выкинуло вместе с лодкой? Ну это так, праздный интерес, оставим эту тему в покое."
    "Перевожу взгляд с облаков на средний план. На кусте барбариса сидит птичка — не разбираюсь я в них. Мелкая, чуть побольше воробья, очень аккуратное тельце, небольшой тонкий клюв, по серо-коричневому тельцу жёлто-коричневые продолговатые пятнышки."
    "Птиц косит на меня правым глазом, потом я перестаю его интересовать. Вдруг он вспархивает с места, подлетает метра на полтора и возвращается на свою ветку с каким-то насекомым в клюве. Значит, назовём этого птица мухоловкой."
    play music littleidea fadein 2
    "Трещит ветка, вспугнутая мухоловка улетает, бросив добычу. Кто-то кидает в меня сосновой шишкой."
    show us smile sport at right with moveinright
    us "Его все уже ждут, а он тут разлёгся!"
    my "Имею право, Рыжая белка."
    th "Я знаю, она не обидится."
    "Поднимаюсь с травы, оглядываюсь. Вон там — начало тропинки к озеру и дальше к старому лагерю. Туда мне можно, но время поджимает. Поэтому я протягиваю Ульянке руку."
    my "Пошли?"
    stop ambience fadeout 1

    scene bg ext_path_day
    show dct_uv_ears_bush:       # Уши спрятаны за кустом
        zoom 0.354 anchor(0.54, 0.445)
    show dct_uv_dress_bush:      # Платье спратано за кустом
        zoom 0.354 anchor(0.56, 0.5)
    show dct_ext_path_day_bush  # Куст слева от дороги
    show us smile sport at right
    with squares
    "И мы идём на костровую поляну, не заходя в лагерь. Мне же в лагерь нельзя — я помню."
    "Карман на Ульянкиных шортах оттопырен до пределов возможности. Ну конечно — яблоко. Ульянка хочет откусить, но останавливает руку, не донеся фрукт до рта."
    show us sad sport with dspr
    us "У тебя есть нож?"
    show uv laugh far:
        xcenter 1.14
        ease 1.2 xcenter 1.01
        pause 1
        ease 1.2 xcenter 1.14
    th "Нож у меня есть, но не в этом случае."
    "Так и говорю Ульяне."
    show us normal sport with dspr
    us "Тогда давай так: я кусаю с одной стороны, а ты — с другой."
    my "Давай лучше по-другому."
    "Забираю у Ульяны яблоко и разламываю по его яблочному меридиану."
    show uv smile far:
        xcenter -0.1
        ease 1 xcenter -0.05
        pause 1
        ease 1 xcenter -0.1
    show us laugh2 sport with dspr
    extend " Вот теперь каждый грызёт свою половину."
    show us normal sport with dspr
    "Пока Ульяна занята яблоком, я кручу головой по сторонам. Вот так, вживую, увидеть всё когда ещё удастся?"
    "Куча мелких деталей вроде муравейника у самой тропы, или лесных цветов, или заросшей просеки, уходящей неизвестно куда. И всё это раньше не замечалось или проскакивало мимо сознания."
    show uv laugh far:
        xcenter 1.14
        ease 1.2 xcenter 1.01
        pause 1
        ease 1.2 xcenter 1.14
    "И пахнет грибами, и хорошо бы проверить на этот счёт во-о-он тот косогор."
    show us smile sport with dspr
    us "А я знаю, зачем ты приехал."
    "Ульянка справилась с яблоком."
    my "Молодец, Рыжик. Я тоже знаю."
    show us sad sport with dspr
    us "Жалко?"
    show dct_uv_ears_bush:
        linear 1.5 anchor(0.5, 0.5)
    my "Грустно. Но не жалко."
    show us normal sport with dspr
    th "Кто-то ещё крадётся возле нас вдоль тропинки — я это чувствую."
    show dct_uv_ears_bush:
        linear 0.25 anchor(0.54, 0.445)
    show dct_uv_dress_bush:
        pause 0.2
        linear 0.1 anchor(0.5, 0.5)
        pause 0.9
        linear 0.1 anchor(0.56, 0.5)
    pause 1.3
    "Резко поворачиваю голову и успеваю заметить мелькнувшее в кусты коричневое платьице."
    show us grin sport with dspr
    us "Не оглядывайся, это Юлька, просто она стесняется."
    th "Ну да, Ульянка же о нашей встрече ничего не знает."
    stop music fadeout 2

    scene bg ext_path2_day
    show us normal sport at right
    with irisout
    play ambience ambience_forest_day fadein 1
    "Мы идём к костровой поляне, оставляя забор лагеря по правую руку. Слева мелькает прогал: в той стороне озеро, где купается Славя."
    us "Расскажи, как ты живёшь?"
    my "Нормально живу, Уля. Всё вроде бы нормально, и проблем не много и не мало — так, среднее количество. И близкие люди есть, которые меня понимают и которых понимаю я. Но вот узнал о вас и захотел познакомиться."
    show us smile sport with dspr
    us "И напридумывал всякого."
    my "Нет. Всё, что можно придумать, где-то уже существует. В моём мире придуманные вы, в вашем мире — я. Где-то — ещё кто-то третий."
    show us normal sport with dspr
    my "Так что я просто подсмотрел, как вы живёте. Было трудно, но кое-что я увидел."
    show us sad sport with dspr
    "Ульянка некоторое время молчит, переваривая мои слова, а потом уточняет:"
    show us surp1 sport with dissolve_fast
    us "Значит, мы настоящие?"
    my "Самые настоящие."
    show us surp2 sport with dspr
    us "И ты настоящий?"
    show us surp3 sport with dspr
    my "Хочешь, ущипну? Конечно, настоящий."
    show us grin sport with dissolve_fast
    us "А скажи тогда, как тебя зовут?"
    th "Сказать? Да легко."
    "Называю ей сетевой ник. Рыжик недовольно морщит носик."
    show us dontlike sport with dissolve_fast
    us "Нет, не то! Как зовут по-настоящему? Как мама с папой назвали. Не бойся, я умею хранить тайны."
    show us normal sport with dissolve_fast
    th "Да я, собственно, и не боюсь, я просто не хочу. Но Ульянка настаивает, и, кажется, ей действительно это надо."
    my "Рыжая белка, зачем тебе моё имя?"
    show us smile sport with dspr
    us "Надо!"
    my "Ну хорошо, скажу перед уходом."
    stop ambience fadeout 1

    scene bg ext_polyana_day
    show dct_bonfire_day_anim:
        xcenter 0.5 yanchor 0.0 ypos 0.55
    with irisout
    play ambience ambience_medium_crowd_outdoors fadein 1
    play music rustic_ballad fadein 2
    "А мы, собственно, уже вышли на костровую поляну."
    show d_sl shy pioneer close at left with dissolve
    sl "Ну наконец-то!"
    "Оглядываю поляну. Знакомые все лица, и все улыбаются."
    show d_sl smile2 pioneer close with dspr
    sl "Здесь все. Кто смог и кто захотел."
    "Да, действительно — все, кто смог и кто захотел."
    show d_sl smile pioneer close with dissolve_fast
    sl "Узнаёшь тех двоих?"
    show d_to m smile at cright:
        alpha 0.0
        pause 1
        linear 2.0 alpha 1.0
    show d_cs m at fright:
        alpha 0.0
        pause 1
        linear 2.0 alpha 1.0
    "Дети лет семи.{w=0.5} Темноволосая девочка нацепила фонендоскоп и с серьёзным видом слушает полноватого мальчишку, задравшего по такому случаю рубашку."
    "Ха! А у девочки-то глаза разного цвета."
    extend " Она замечает меня, улыбается, что-то говорит мальчику."
    show d_to m serious with dspr
    "Мальчик поворачивает голову в мою сторону, на мгновение мы пересекаемся взглядами, и из глубины семилетних глаз на меня смотрят глаза сорокалетнего дядьки. Очень опасного дядьки. Смотрят и прячутся."
    show d_to m smile with dspr
    "Я взвешен, оценён и признан безопасным."
    th "Интересно, что бы стал делать этот пузанчик, если бы решил, что я представляю опасность? Забил бы фонендоскопом? Самый первый цикл в младшем отряде, и старые привычки ещё не стёрлись до конца."
    hide d_cs
    hide d_to
    with dissolve2
    my "Что-то много народу, Славя."
    sl "Сколько смогло и сколько захотело. А захотели все, кто понял, что происходит, про кого ты упомянул и даже просто подумал, и ещё сверх того."
    sl "Ну, будешь речь толкать или пойдёшь к костру?"
    th "К костру, конечно. Ишь, чего удумала — речь ей толкать."
    hide d_sl with dissolve
    "Мне освобождают место рядом с Алисами, дают в руки уже очищенную печёную картошку, ставят рядом кружку с заваренной смородиной."
    show dv grin pioneer at cright
    show 3500_dv laugh pioneer2 at cleft:
        ycenter 0.83
    with dissolve
    "Алисы — вот они, обе. Здороваются со мной по-мужски, за руку, улыбаются."
    dv "Значит, всё-таки один из Семёнов?"
    show dv normal pioneer:
        xzoom -1.0
    show dv_4_badge_mirror at cright:
        xzoom -1.0
    show 3500_dv smile pioneer2
    with dissolve_fast
    "Загадка для меня: угадай, кто откуда.{w=1} И тут же моя отгадка."
    my "Алис, ты ведь та, которая помощница вожатой в лагере физруков и бабы Глаши?"
    show dct_dv_4_blink at cright with dspr:
        xzoom -1.0
    pause 0.25
    hide dct_dv_4_blink with dspr
    my "Нет, не Семён. Я просто воспользовался на три-четыре часа его телом, пока он спит в автобусе."
    my "Надо будет вернуть."
    show dv grin pioneer:
        xzoom 1.0
    hide dv_4_badge_mirror
    with dspr
    dv "А я-то думала!"
    my "Нет. И даже близко не попала."
    "А теперь моя очередь спрашивать."
    my "Алиска, а ты поедешь с концертами по лагерям?"
    show 3500_dv normal pioneer2 with dspr
    show dv sad pioneer with dissolve_fast
    dv "Цикл назад собиралась.{w=0.7} А сейчас — думаю."
    show dv guilty pioneer with dspr
    "Алиса бросает взгляд в дальний конец поляны, где кто-то учит кого-то играть на горне."
    show dv sad pioneer with dspr
    "Ну, это уже не моя забота, я просто полюбопытствовал."
    show dv normal pioneer far at cright:
        xzoom -1.0
    show dv_4_guitar_standing far at cright:
        xzoom -1.0 yalign 0.0
    show dv_4_badge_mirror far at cright:
        xzoom -1.0
    show 3500_dv normal pioneer2 guitar standing:
        zoom 0.75 yalign 0.0
    with dissolve
    "Алисы встают, обе с гитарами, обе — нет, не одинаковые, но очень похожие."
    "Я делаю на прощание им подарок."
    my "Между прочим, квартира в двухэтажке сорок шестого года постройки была на втором этаже, в ней было три комнаты, кухня и туалет с ванной. Только вот чтобы помыться в горячей воде, приходилось топить дровяной титан, и плита на кухне тоже оставалась дровяная. В ваш дом газ так и не провели. Это вам в копилку ваших общих воспоминаний."
    show dv smile pioneer far
    show 3500_dv smile pioneer2 guitar standing
    with dspr
    "Девушки улыбаются очень по-доброму и уходят на край поляны."
    hide dv
    hide 3500_dv
    hide dv_4_guitar_standing
    hide dv_4_badge_mirror
    with dissolve
    "А я начинаю изучать печёную картошку. Дегустировать. Её и смородиновый чай."
    "Странно, но пионеры почти не обращают на меня внимания, а больше заняты друг другом."
    "Где-то двойники общаются между собой, а где-то двойники оказываются в разных компаниях. Интересно, почему?"
    "Скорее угадываю, чем улавливаю — настолько он слаб, запах грейпфрута. Поворачиваю голову и тону в зелёных глазищах. Ко мне подсела Лена."
    show un normal pioneer close at fleft with dissolve
    my "Привет. Ты одна здесь?"
    un "Да, остальные не могут. Пока не могут. Жаль."
    my "Они проснутся, Лен, обязательно."
    show un smile pioneer close with dspr
    un "Я знаю, [ggname]."
    "И Лена называет меня настоящим именем. Тем, которое я обещал Ульянке.\nЯ чуть не обливаюсь чаем и на некоторое время теряю дар речи.\nКак?"
    my "Как? Как ты…"
    show un grin pioneer close with dissolve_fast
    un "Ты же сумел узнать наши имена."
    my "Ну, к вам-то заглядывал не я один. Так что имена я уже знал. Так, несколько имён добавил в копилку и всё."
    show un smile3 pioneer close with dspr
    un "Ну вот, а мы со здешней Мику вдвоём заглянули к тебе. Не бойся — обещаю тебе, что все подумают, что это выдуманное нами имя."
    show un serious pioneer close with dspr
    un "Скажи, как ты думаешь, когда мой Семён проснётся?"
    my "Скоро, Лен. Не в этом цикле, но очень скоро."
    show un surprise pioneer close with dissolve_fast
    my "Он зайдёт в лагерь, повернёт голову к клубам, увидит тебя и скажет одними губами: «Ленка! Я прорвался!», но ты его прекрасно услышишь и бросишься к нему на шею, завизжав так, что перепуганные кибернетики выскочат на крыльцо."
    show un cry_smile pioneer close with dspr
    my "Тебя спасать, между прочим, выскочат. Вот только ты к концу этого цикла забудешь всё, а вспомнишь уже потом, когда всё произойдёт."
    th "Что я там говорил Ульянке, что не выдумывал их мир? Что я только наблюдатель и регистратор? Но это правда, просто наблюдатель всегда влияет на наблюдаемый объект, и я пользуюсь этой возможностью."
    show un smile pioneer close with dissolve_fast
    th "И, кажется, Лена это знает, если задала такой вопрос. А если ещё не знает, то догадается."
    show un smile pioneer close:
        linear 6 alpha 0.0
    th "И они тоже наблюдатели, это правило распространяется и на них. Но я не жду ничего плохого ни от Лены, ни от Мику — пусть они заглядывают ко мне. Мне будет приятно."
    "Пока я так размышляю, Лена бесшумно уходит."
    th "Пора и мне подойти к кому-нибудь."
    show un normal pioneer far at center:
        alpha 0.0
        pause 2.4
        linear 1 alpha 1.0
    show mi smile pioneer far at fright:
        alpha 0.0
        pause 1.7
        linear 1 alpha 1.0
    show sl shy dress far at cright with dissolve
    th "К Сашке, которая застенчиво мне улыбается, сидя между здешней Мику и вернувшейся к ним Леной? Проснулась? Нет, просто захотела компанию Лене составить."
    th "Но уже скоро — чувствую, что от хорошего пинка она проснётся прямо сейчас, и проснётся безболезненно. Обойдёмся без пинков, всё должно быть естественно."
    "Поэтому я улыбаюсь этим троим девочкам, машу им рукой: «Я узнал вас, кто вы и откуда, и очень рад вас видеть», — Мику в ответ энергично машет мне рукой"
    show mi laugh pioneer far with dissolve_fast
    extend ", но я иду к своему протагонисту."
    hide un
    hide mi
    hide sl
    with dissolve_fast
    stop music fadeout 5
    show mt grin panama pioneer far:
        zoom 0.8 xcenter 0.19 ycenter 0.60 alpha 0.0
        pause 2.8
        linear 0.5 alpha 1.0
    show d_mt normal dress sombrero far:
        zoom 0.8 xcenter 0.32 ycenter 0.60 alpha 0.0
        pause 2.5
        linear 0.5 alpha 1.0
    show d_mt2 calm sport far:
        zoom 0.8 xcenter 0.09 ycenter 0.60 alpha 0.0
        pause 3.1
        linear 0.5 alpha 1.0
    show d_sf normal pioneer:
        zoom 0.9 ypos 0.1 alpha 0.0 xcenter 0.69
        pause 0.5
        linear 1 alpha 1.0
    show d_us normal dress:
        zoom 0.9 ypos 0.05 alpha 0.0 xcenter 0.86
        pause 1
        linear 1 alpha 1.0
    show us smile sport at center:
        zoom 0.9 ycenter 0.55 alpha 0.0
        pause 1.7
        linear 1 alpha 1.0
    "Они тоже сидят своей компанией: Семён, Ульяна-большая, Ульяна-маленькая и чуть поодаль все три Ольги."
    "Но Ольги уткнулись носом в какие-то вожатские бумаги, и, кажется, им не до нас. Когда ещё получится встретиться?"
    "Пока все ресурсы Системы заняты на то, чтобы выкинуть меня из здешнего мира, любые двойники могут сосуществовать в одном узле и не аннигилировать, но сколько мне здесь ещё находиться? Час-два, вряд ли больше."
    hide mt
    hide d_mt
    hide d_mt2
    show d_sf normal pioneer:
        zoom 1.0 ypos 0.0 xcenter 0.6
    show d_us normal dress:
        zoom 1.0 ypos -0.05 xcenter 0.81
    show us smile sport at cleft:
        zoom 1.0 ycenter 0.5
    with Dissolve(1.5)
    show d_sf serious pioneer with dspr
    me "Привет. Ты знаешь, я давно уже чувствовал, что за мной кто-то подглядывает."
    show d_us laugh dress
    show us laugh sport
    with dspr
    my "Ну прости. Я больше не буду."
    show d_sf laugh pioneer with dspr 
    me "А куда ты денешься?"
    show us normal sport
    show d_us normal dress
    with dspr
    my "Есть много миров, кроме вашего. В том числе те, куда ещё никто не заглядывал."
    th "Но за вами тоже подглядывать буду — тут я наврал Семёну, и мы оба это понимаем, и не только мы."
    show d_sf serious pioneer with dspr
    show d_us hurt dress with dspr
    us_old "Врёшь ты всё."
    show us grin sport
    show d_us shy dress
    with dspr
    us_old "Не будет он… Ты уже отравился «Совёнком». Подглядывай, тебе можно."
    show d_us normal dress with dspr
    us_old "Слышишь, Сёмк — ему можно!"
    show us smile sport with dspr
    th "Ну да. Наблюдатель влияет на объект, а объект влияет на наблюдателя."
    show d_sf sad pioneer with dspr
    me "Конечно, можно. Никто и не запрещает. Все — только «за»."
    "Решаю поделиться мыслью с Ульяной-большой."
    show us normal sport with dspr
    my "Ульяна, зря ты про миксов переживала. Вон, здешняя Мику проснулась и прекрасно себя чувствует."
    show d_us sad dress with dspr
    us_old "Проснулась. Но для этого пришлось исчезнуть «Микусе» и самой Мику такую работу проделать, какую я бы не смогла, например."
    show us sad sport
    show d_sf normal pioneer
    with dspr
    my "Всё бы ты смогла. Решилась же тогда, в девяносто втором. И другие смогут или уже смогли, им просто нужно вспомнить."
    show d_us normal dress with dspr
    hide us with moveoutleft
    play music adaytoremember fadein 2
    "Про Мику из их лагеря молчим: оба понимаем, что её случай из ряда вон выходящий. Что Мику за два дня стала старше на целую жизнь."
    "Сидим ещё некоторое время молча. Слышны только общий гул голосов и две гитары."
    "Обе Алисы, друг напротив друга, устроили гитарную дуэль. Одна начинает играть, а другая подхватывает, потом порядок меняется, и так до первого сбоя — кто не узнает мелодию."
    "И столько азарта в их глазах, и так хочется дождаться конца состязания, но чувствую, что время уже поджимает, что мне всё труднее и труднее удерживаться в лагере."
    my "Я сейчас подойду."
    "Встаю и ищу глазами…"
    hide d_sf
    hide d_us
    with dissolve
    "Ага, вот он."
    show mt grin panama pioneer far:
        xcenter 1.3
    show d_mt normal dress sombrero far:
        xcenter 1.3
    show d_mt2 calm sport far:
        xcenter 1.3
    show us normal sport far:
        xcenter 1.3
    show sh serious pioneer far at left with dissolve:
        ycenter 0.75
    "Сидит и несколько рассеянно смотрит по сторонам."
    show sh serious pioneer at cleft with dissolve_fast:
        ycenter 0.7
    my "Привет. И кто ты сейчас?"
    show sh surprise pioneer with dspr
    sh "Добрый день. Я?"
    show sh normal pioneer with dspr
    show d_mt normal dress sombrero far:
        zoom 0.8 xcenter 0.92 ycenter 0.6 alpha 0.0
        pause 1
        linear 1.5 alpha 1.0
    show d_mt2 calm sport far:
        zoom 0.8 xcenter 0.69 ycenter 0.60 alpha 0.0
        pause 1
        linear 1.5 alpha 1.0
    sh "А… Ты имеешь в виду…{w=0.4} Я — как Ольга, стал целым, и знаешь, я больше Шурик.{w} Александр, он…{w=0.3} Он растворился во мне."
    show us normal sport far:
        zoom 0.8 xcenter -0.2 ycenter 0.60
        ease 2 xcenter 0.8
    show sh serious pioneer with dspr
    sh "Я знаю и помню всё, что знал он. Но я — Шурик, который никогда не был знаком с его Янами, только заочно."
    sh "Ни полигон, ни тот автобус, ни то, что было потом — меня не коснулось. Даже пожар на маяке."
    show us normal sport far:
        zoom 0.8 xcenter 0.8 ycenter 0.60
        ease 2 xcenter 1.8
    "Ещё один вопрос меня мучает."
    show sh normal pioneer with dspr
    my "А скажи, я понимаю — робот. Могу догадаться, почему робот-девочка. Но кошка тут при чём?"
    show 3500_sh smile noglasses pioneer glasses as sh with dissolve_fast:
        ycenter 1.056
    show mt grin panama pioneer far:
        zoom 0.8 xcenter 1.2 ycenter 0.60
        ease 2.5 xcenter 0.79
    sh "Не знаю.{w=0.3}.{w=0.3}.{w=0.4} Наверное, подсознательно вспомнил ту историю с кошкой-мутантом."
    my "Юля. Её зовут Юля. И она — человек."
    show sh normal_smile pioneer with dissolve_fast:
        ycenter 0.7
    sh "Я запомню."
    show sh normal_smile pioneer:
        linear 4 alpha 0.0
    stop music fadeout 3
    "Вот, собственно, и всё."
    "Есть ещё несколько человек, с которыми я бы пообщался, но и время поджимает, и столько общения уже тяжело для меня."
    "Пора уходить. Пионеры тоже это чувствуют."
    hide d_mt with moveoutright
    pause 0.2
    show mt angry panama pioneer far
    show d_mt2 angry sport far
    with dissolve_fast
    show d_mt2 angry sport far:
        ease 1.5 xcenter 0.28
    show mt angry panama pioneer far:
        pause 0.5
        ease 0.6 xcenter 0.65
    "Ольги поднимаются, одна сразу уходит куда-то вбок по тропинке, а две других начинают строить каждая своих подопечных."
    d_gm "Я большая! Я сама дорогу найду, я большая!"
    hide mt
    hide d_mt2
    hide us
    with dissolve
    "Подхожу поближе: Славя уговаривает встать в строй маленькую девочку, тоже из новичков."
    show d_sl smile pioneer at cright:
        zoom 0.75 yalign 0.0
    show d_bg m shy:
        zoom 0.85 xcenter 0.4 ycenter 0.58
    with dissolve
    "Коротенькое платьице, сандалики, бантики, две жиденьких светленьких косички. И возмущённый взгляд серых глаз."
    my "Как тебя зовут, большая?"
    show d_bg m angry with dspr
    d_gm "А тебе какое дело? В стенгазете напишешь?"
    show d_sl surprise pioneer
    show d_bg m shy
    with dissolve_fast
    d_gm "Глафира Андрейко я! Денисовна!"
    show d_sl happy pioneer with dissolve_fast
    my "Ну, удачи тебе, Глафира Андрейко Денисовна."
    hide d_sl
    hide d_bg
    with dissolve
    stop ambience fadeout 1
    play music my_2nd_summer fadein 2
    show us normal sport at cleft with dissolve
    us "Я провожу тебя."
    th "Конечно, проводишь. Тем более я тебе обещал кое-что."
    show uv smile far with moveinbottom:
        xcenter 0.89
    "Мы остались втроём на костровой поляне: я, Ульянка и выскочившая из кустов, как только все ушли, Юля."
    show uv grin far with dissolve_fast
    "Вот, кстати, о Юле. Раз уж наблюдателю суждено влиять на объект наблюдения, сделаю-ка я в очередной раз этот процесс управляемым."
    show dct_uv_newdress:
        xcenter 0.89 alpha 0.0
        pause 0.5
        linear 2.0 alpha 1.0
    "Представляю себе, как изрядно обветшалое платье на Юле становится новым"
    show uv surprise2 far with dspr
    show dct_uv_newdress_edging:
        xcenter 0.89 alpha 0.0
        pause 0.5
        linear 1.5 alpha 1.0
    extend ", а потом, расшалившись, пускаю по подолу и вороту платья полосы вышивки. Она девочка, ей должно понравиться."
    show uv laugh far
    show dct_uv_newdress_laugh_shy:
        xcenter 0.89
    with dspr
    "Фелиноид краснеет, но делает вид, что ничего не произошло."
    my "Пошли?"

    scene bg ext_path2_day
    show us normal sport at cleft
    show uv laugh far at fright:
        xcenter 0.89
    show dct_uv_newdress:
        xcenter 0.89
    show dct_uv_newdress_edging:
        xcenter 0.89
    show dct_uv_newdress_face:
        xcenter 0.89
    with irisin
    "И мы идём обратно к автобусу, только на этот раз Юля не прячется по кустам, а идёт рядом с нами."
    show us smile sport with dspr
    us "Так как тебя зовут?"
    my "[ggname]. Как Мику и написала."
    show us surp3 sport with dissolve_fast
    us "Значит, это правда?{w=0.7} Значит, и у неё в книге ты не придуманный, а живой!"
    my "Конечно, у меня же вы тоже живые."

    scene bg ext_path_day
    show us shy sport at cleft
    with irisin
    "Юле в конце-концов наскучило нас сопровождать, и она где-то отстала."
    show us shy2 sport with dspr
    "Ульянка думает о чём-то своём, я опять верчу головой, чтобы запомнить детали."
    show us sad sport with dissolve_fast
    "Вон уже и остановка, вон уже и Икарус. Никуда он не уехал, родимый."
    stop music fadeout 2

    scene bg ext_bus
    show us sad sport at cleft
    with wiperight
    play ambience ambience_camp_entrance_day fadein 1
    us "Мы ещё увидимся? По-настоящему?"
    my "Каким образом, Рыжая белка? У вас я могу существовать только несколько часов и в чужом теле — вот как сейчас, у нас ты — только в виде картинки на мониторе."
    my "Разве что в следующей жизни. Либо ты к нам, либо я к вам — как получится."
    my "Так что если в лагерь приедет новенький, высокий, сутулый и худой, по характеру и любви к книгам и технике — что-то среднее между Электроником и Женей, присмотрись к нему, прежде чем подбрасывать членистоногих в пюре."
    show us calml sport with dissolve_fast
    us "Вот далось вам всем это пюре!"
    show us shy sport with dissolve_fast
    us "А скажи, мы здесь сильно отличаемся от того, что ты и другие про нас написали?"
    my "И да, и нет. В основном деталями."
    my "Например, вот скажи, Рыжик — у тебя же веснушки с шеи переходят на плечи и дальше на грудь? По моему, очень мило."
    show us surp3 sport with dspr
    pause 0.7
    show us fear sport with dissolve_fast
    us "Ты! Ты! Ты подглядывал!"
    show us shy2 sport with dissolve_fast
    my "Нет, Рыжик, я догадался. Эти веснушки — обычное для рыжих дело, а у нас про них никто не вспомнил. Ладно, прощай."
    show us normal sport with dissolve_fast
    us "Прощай.{w=0.5} Нет, подожди, время ещё есть. Побежали, я тебя с Майей познакомлю!"
    stop ambience fadeout 1

    scene bg ext_road_day:
        running
    show dct_ext_road_day_wheat_Maya:
        running
    with irisout
    play ambience ambience_ext_road_day fadein 1
    play music anewbeginning fadein 2
    "«Что ещё за Майя такая?» — бурчу про себя, но послушно бегу за Улькой по шоссе."
    "Двести метров,{w=0.3} пятьсот,{w=0.3} восемьсот…"
    "Ульянка останавливается в одном ей ведомом месте и ждёт меня. Догоняю, оглядываюсь."

    scene dct_ext_outside_field:
        zoom 1.0 pos (-0.067, -0.1)
    show dct_ext_outside_field_Maya:
        zoom 1.0 pos (-0.067, -0.1)
    show us normal sport far:
        zoom 1/0.75 pos (0.2, -0.1)
    with irisout
    "Когда-то здесь был свёрток с шоссе на старый лагерь. Потом лагерь закрыли, а дорожную насыпь срыли бульдозерами."
    "О том, что здесь была дорога, можно догадаться только по чуть отличающемуся оттенку пшеницы и по заросшей уже просеке, просматривающейся там, где насыпь упиралась в лес."
    show dct_us_shy2_sport_far_mirror as us with dissolve_fast
    show dct_ext_outside_field:
        ease 3 zoom 0.75 pos (0.0, 0.0)
    show dct_ext_outside_field_Maya:
        ease 3 zoom 0.75 pos (0.0, 0.0)
    show dct_us_shy2_sport_far_mirror as us:
        ease 3 zoom 1.0 pos (0.2, 0.0)
    "И ещё есть она: девочка, пионерка, как будто из моего старого-старого отряда. Футболка, шорты, галстук на голой шее, стрижка, закрывающая уши. Лет ей двенадцать или тринадцать, не больше."
    "Шла вдоль дороги из старого лагеря, дошла до шоссе, присела на гранитный валун, сняла сандалию, подтянула правую ногу ступнёй к себе и что-то там рассматривает: то ли камешек, то ли занозу."
    show dct_us_shy_sport_far_mirror as us with dspr
    "То есть рассматривала только что, а сейчас услышала шум мотора, подняла голову и так и превратилась в бронзовую скульптуру. И теперь вечно со спокойным любопытством смотрит на шоссе: кого там везут в лагерь во внеурочный день? Хорошее такое лицо."
    th "Может, у скульптора бронза осталась после отливки Генды, и он постарался уже не для халтуры, а для души — я не знаю. И не важно на самом деле."
    show us normal sport far with dissolve_fast
    us "Вот, это Майя."
    "Но я и сам догадался. Подхожу, сажусь напротив Майи на корточки, чтобы не смотреть на неё сверху вниз."
    show us sad sport far with dspr
    my "Здравствуй, Майя."
    "Протягиваю правую руку и осторожно трогаю её бронзовое запястье."
    "Кажется, что взгляд у Майи на мгновение сфокусировался на мне."
    show us laugh2 sport far with dspr
    extend " Краем глаза вижу, как расцветает в улыбке Ульянка, а до того стояла, замерев в непонятно-тревожном ожидании."
    show us grin sport far with dspr
    us "Врёшь ты всё, что никогда здесь не был! Ты же всё сделал правильно!"
    us "А теперь побежали обратно."
    th "И действительно пора, а то Семён проснётся не в автобусе, а непонятно где."

    scene dct_ext_bus_road
    show dct_ext_bus_road_wheat_Maya
    show us sad sport close at cright
    with irisin
    play ambience ambience_camp_entrance_day fadein 1
    "Мы стоим у автобуса, я, прежде чем залезть внутрь, пытаюсь отдышаться. Вот теперь уже совсем пора."
    "А Ульянка всё не хочет меня отпускать."
    us "Послушай, вот ты наблюдал за нами. А можно, я тоже буду наблюдать, как там ты живёшь?"
    my "Конечно, можно. Мне будет очень приятно, что ты обо мне беспокоишься."
    show us shy sport close with dspr
    show dct_uv_newdressedging_close at cleft:
        alpha 0.0
        pause 1
        linear 1 alpha 1.0
    "Обнимаюсь с Ульянкой, целую её в щёку,{w=0.8} обнимаюсь с прибежавшей Юлей, она целует меня в нос и хохочет — отомстила, и лезу в автобус."
    stop ambience

    scene bg int_bus with slideright
    "Всё на месте: и пальто, и пакет. Сейчас я усну, а проснётся уже Семён, и через положенное время выйдет из автобуса и пойдёт к воротам «Совёнка» навстречу Славе."
    "А я уже, наверное, не стану узнавать, что его там ждёт."
    "Надо бы сделать для него что-то хорошее, но что?"
    "Делаю последнее усилие и заряжаю аккумулятор в его телефоне по самую крышку. Потом заполняю карту памяти музыкой со своей автомагнитолы — пусть разбирается, может, что и пригодится. Вот удивится-то."
    $ day_time()                            # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Всё, спать! Посчитаю-ка я для разнообразия автобусы: «Первый четырестадесятый подъехал к остановке, второй четырестадесятый подъехал к остановке, третий…»."
    window hide
    stop music fadeout 2
    show blink
    pause 1

    scene black with dct_fade
    play sound_loop sfx_computer_noise fadein 1
    $ prolog_time()
    window auto
    voice "Зая хренов, я думала, он работает, а он беспардонно дрыхнет! Ужин готов! Кушать подано, садитесь жрать, пожалуйста!"

    scene dct_author_room
    show unblink
    my "Повинуюсь, мой злобный хомячок!"
    voice "Всё написал?"
    my "Возможно…"
    voice "Мистер загадочность…"
    "Ну да, я такой."

    scene anim prologue_monitor_4
    show dct_epilogue_monitor_screensaver
    with dissolve
    "Поднимаюсь с дивана, подхожу к столу."
    show dct_epilogue_monitor_document with dissolve
    hide dct_epilogue_monitor_screensaver with dissolve
    "Шевелю мышкой, чтобы разбудить комп."
    "Сохраняю написанное и закрываю редактор."
    show dct_epilogue_monitor_ussr_wallpaper with dissolve
    hide dct_epilogue_monitor_document with dissolve
    "Обои рабочего стола с рыжей егозой."
    show dct_epilogue_monitor_ussr_grin with dissolve
    "Улыбаюсь егозе, и егоза подмигивает мне левым глазом."
    stop sound_loop fadeout 2
    show black:
        alpha 0.0
        linear 2 alpha 1.0
    "Всё хорошо, сестрёнка.{w=1} Я сейчас бросил монетку и надеюсь, что она останется стоять на ребре."
    window hide
    stop sound fadeout 2
    stop ambience fadeout 2
    
    $ renpy.pause(2.5)

    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound_loop')
    
    $ persistent.d_coin = d_coin + 1
    show image("images/gui/choice/prologue/choice_box.png"):
        xzoom 4 yzoom 0.5 align (0.5, 0.5)
    show text "{color=#496463}{size=50}Конец книги «Монетка в фонтане»{/size}{/color}":
        align (0.5, 0.5)
    with dspr
    pause 2
    hide image("images/gui/choice/prologue/choice_box.png")
    hide text
    with dissolve_fast
    jump dct_titles