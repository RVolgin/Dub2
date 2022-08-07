    ############################
    #Глава 1. Шестичасовой цикл#
    ############################


label dct_sixhour:
    $ save_name = u"Дубликат. Монетка в фонтане -- Шестичасовой цикл"
    $ day_time()
    $ persistent.sprite_time = "day"
    scene black
    show headline_text2 u"Глава I. Шестичасовой цикл" at truecenter with dspr
    $ renpy.pause(3.0)

    play sound_loop sfx_bus_interior_moving fadein 1.5
    hide headline_text2 with dissolve


    scene black
    $ set_mode_nvl()
    "Полуоткинутое кресло, шум мотора, мягкое покачивание. Да, это автобус, начался очередной цикл."
    th "Это значит, что у меня, как и всегда, есть полчаса до того, как начнут просыпаться прочие пассажиры: копии и миксы."
    th "Как и всегда… «Вы умерли и у вас в запасе вечность!» — Только это меня и утешает.{w} Я про то, что я умер."
    th "Хорошо, я, как и всегда, потерплю до сегодняшней ночи, не буду нагонять жути и мрачных мыслей на «пионеров». В конце концов, они дети, сколько бы им ни было лет на самом деле, и сколько бы ни было лет их оригиналам."
    "\~ И чтобы не портить смену в пионерском лагере той копии-заглушке, с которой я делю это тело, надо произвести на товарищей по отряду более-менее приятное первое впечатление. Пусть я буду не привлекателен, но хотя бы забавен и безобиден. Как и всегда… «Разрешите представиться, Паганель, версия неизвестно какая по счету, стереотипная». \~\n"
    th "Плохо то, что моя память и память той копии практически не пересекаются. Он даже в более выгодном положении, чем я. Я о нем вообще ничего не знаю, а у него хотя бы мои имя, фамилия и все мои способности."
    th "А может быть, ему роль ДʼАртаньяна больше по душе?"
    stop music fadeout 3
    nvl clear
    $ set_mode_adv()
    "Ну что ж, пора присмотреться к компании."
    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh serious
    show el normal pioneer close:
        xcenter 1.5
    show dct_el_1_sleep:
        xcenter 1.5
    show dct_fantasy_in_mind
    with dissolve
    
    "Хотя, что к ней присматриваться? Все те же и там же."
    "Я никогда особо не интересовался здешними копиями, но, за столько циклов, запомнил — деваться некуда. Даже если от каждого цикла я оставляю себе всего лишь шесть часов."
    show el normal pioneer close:
        zoom 1.095 xcenter 0.34 ycenter 0.56 rotate -8.9
    show dct_el_1_sleep:
        zoom 1.095 xcenter 0.34 ycenter 0.56 rotate -8.9
    show dct_int_bus_middle_sh normal
    with dissolve
    "Сыроежкин спит на соседнем кресле.{w=0.4} Сейчас он проснется и начнет знакомиться."
    scene dct_int_bus_people
    show dct_int_bus_people_sl_mi front:
        zoom 0.625
    show dct_int_bus_people_vi sitdown
    show dct_fantasy_in_mind
    with pushleft
    "Где-то впереди Мику и Саша."
    scene dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body
    show dct_int_bus_another_middle_mz_head smile
    show dct_int_bus_another_middle_un
    show dct_fantasy_in_mind
    with pushleft
    "Через проход от нас — Женя и Лена."
    scene dct_int_bus_stern
    show dct_int_bus_stern_dv_us:
        zoom 0.5
    show dct_fantasy_in_mind
    with pushleft
    "Позади, в конце салона, — Ульяна и Алиса.{w} Вроде и всё, с остальными я не успеваю познакомиться, остальные меня не интересуют."

    scene black with dissolve
    $ set_mode_nvl()
    "Пока Сыроежкин не проснулся, надо сообразить, как избежать диалога с Глафирой Денисовной.\n\~ Потому что она опять начнет... \~"
    "Правда, я не видел ее десяток циклов, не меньше.\n\~ Неужели всё? Интересно, как Система это обыграла? \~"
    th "Нет, ничего интересного, повариха и повариха, кто ее запоминает, кроме активированных? Приехала заглушка: копия или микс из резерва."
    th "Господи, ну когда же я сдохну?{w} Когда мой сосед по этому телу разовьется на столько, что захватит над ним контроль целиком? Как же мне надоело просыпаться."
    "Можно и глаза открыть. Все равно скоро уже лагерь, а там притворяться спящим не получится."
    nvl clear
    $ set_mode_adv()


    scene dct_int_bus_people behind blink
    show dct_int_bus_people_sl_mi back behind blink:
        zoom 0.625
    show dct_int_bus_people_vi standup behind blink
    show unblink
    window show
    "Подлинник Александра Трофимова открыл глаза,{w=0.5} осторожно покосился на соседа справа,"
    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise
    show d_sf normal pioneer:
        zoom 1.292 xcenter 0.37 ycenter 0.8 rotate -6.34
    show d_sf_sleep:
        zoom 1.292 xcenter 0.37 ycenter 0.8 rotate -6.34
    with squares
    extend " и вздрогнул."
    window auto
    "Вместо привычного и ожидаемого Сыроежкина, на сиденье рядом дремал полузнакомый парень лет двадцати пяти.{w} Каштановые волосы, пионерская рубашка с закатанными рукавами, галстука нет, а на шее черный капроновый шнурок прячущий что-то под рубашкой, длинные брюки."
    show dct_int_bus_middle_sh serious with dspr
    th "Э-э-э… Физрук, кажется. Как его? Семен, да. Копия… забыл."
    th "Забыл должность человека-оригинала, кажется, он миксами занимался. Только эта копия, вроде как постарше стала выглядеть, чем была."
    hide d_sf_sleep
    show dct_int_bus_middle_sh normal
    with dspr
    "А парень почувствовал, что его разглядывают, открыл глаза, посмотрел на Александра понимающим взглядом, кивнул, здороваясь."
    show d_sf smile pioneer with dspr
    show d_sf smile pioneer:
        pause 2.5
        linear 1.0 alpha 0
    "И, ничего не говоря, поднялся с кресла и пошел в хвост автобуса, где с последнего ряда уже раздавались голоса проснувшихся Алисы и Ульяны."
    scene dct_int_bus_stern
    # show dct_int_bus_stern_un:
        # zoom 0.5 alpha 0.0
    show dct_int_bus_stern_dv_us:
        zoom 0.5
    show dct_fantasy_in_mind
    with fade
    # show dct_int_bus_stern_un:
        # pause 1
        # linear 1 alpha 1.0
    th "Проснулись уже. Значит, тоже активированные."
    show dct_int_bus_stern_un behind dct_int_bus_stern_dv_us with dissolve:
        zoom 0.5
    extend " О, и Лена с ними. А на ее месте кто?"
    scene dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body:
        blur 50
        linear 2.5 blur 0
    show dct_int_bus_another_middle_mz_head sleep:
        blur 50
        linear 2.5 blur 0
    show dct_int_bus_another_middle_el:
        blur 50
        linear 2.5 blur 0
    with fade
    "Александр поправил очки и пригляделся через проход. В кресле рядом с Женей, подставив ей свое плечо, вместо подушки, и, прижавшись щекой к ее затылку, спал Сыроежкин."
    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise
    with fade
    th "Сейчас они проснутся и случится скандал. Обычно скандал за ужином случается, а тут случится в автобусе. Флуктуация-с."
    show dct_int_bus_middle_sh normal
    usp "Сёмка…"
    "Сзади послышался голос. Александр подождал продолжения, но ничего, просто «Сёмка», и дальше шуршание, пыхтение и скрипнуло пару раз."
    scene dct_int_bus_stern
    show dct_int_bus_stern_un:
        zoom 0.5
    show dct_int_bus_stern_dv_us:
        zoom 0.5
    show dct_fantasy_in_mind
    with fade
    pause 0.5
    show dct_int_bus_stern_sf behind dct_fantasy_in_mind with dissolve:
        zoom 0.5
    "Как будто кто-то потеснился на сиденье, чтобы посадить еще одного человека."
    "Разговор за спиной продолжился, но разговаривали в четверть голоса, так что слов было не разобрать за шумом автобуса. Улавливался только сам факт разговора."


    stop sound_loop fadeout 2
    play music music_list["lightness"] fadein 3
    show blink
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
    show bg ext_no_bus
    show d_jnjn at center:
        zoom 0.75 ycenter 0.68
    with fade
    $ renpy.pause(2.0, hard = True)
    hide d_jnjn
    show d_jn at center:
        zoom 0.75 ycenter 0.64
    with wipeup
    $ renpy.pause(1.0, hard = True)
    
    #Яна
    show bg ext_no_bus:
        easeout 2.5 zoom 2.0 ycenter 0.6
    show d_jn:
        easeout 2.5 zoom 4.0 ycenter 1.1
    stop music fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 2
    show black with dissolve2
    
    
    "А разбудил его протестующий девичий крик."
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
    "Слова спросонья были непонятны, но вот то, что так может кричать только оскорбленная невинность, ясно было и без слов."
    show blink
    "Когда вопль прервался, стали слышны сдерживаемые смешки с заднего ряда."
    th "Пересадили Сыроежкина, пока он спал.\n{w=0.4}Хоть вы и активировались, но, как были детьми, так и остались"
    "Кто-то шлепнулся рядом на сиденье — \~ Понятное дело, кто \~ — и , тут же, следом, прилетела тряпка, зацепив Александра по носу и сбив с него очки."
    "Пришлось открывать глаза и изображать только что проснувшегося, благо, без очков это было не трудно."
    scene dct_int_bus_another_middle behind blink
    show d_mz shyangry pioneer far behind blink:
        xcenter 0.65
    show unblink
    mz "Как тебя там? Который в очках. Прости, я не хотела."
    show d_mz angry pioneer far with dspr
    mz "А ты, лохматый, еще раз начнешь руки распускать, лучше сразу костыли заказывай!"
    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh surprise
    show el scared pioneer close:
        zoom 1.095 xcenter 0.31 ycenter 0.57 rotate -12.9
    with dissolve
    mz "Или нет, не заказывай. Тебе же всё равно костыли держать нечем будет."
    show dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body
    show dct_int_bus_another_middle_mz_head upset
    with dissolve
    "Александр, наконец, нашел очки и смог разглядеть уже демонстративно отвернувшуюся к окну Женю."
    hide dct_int_bus_another_middle
    hide dct_int_bus_another_middle_mz_body
    hide dct_int_bus_another_middle_mz_head
    show el upset pioneer close
    with dissolve
    "А так же сбитого с толку Сыроежкина, и даже бейсболку, принадлежащую тому же Сыроежкину и валяющуюся сейчас на полу."
    show el sad pioneer close
    show dct_int_bus_middle_sh normal
    with dspr
    el "Ведь ничего же не делал. Проснулся, а ты у меня на плече спишь и с плеча сползать начала. Ну я и пошевелился чуть, чтобы тебе удобно было."
    "Сосед бормотал тихо, с опаской косясь через проход."
    th "Пора вживаться в роль"
    "Александр поднял с пола бейсболку, непонимающе оглядел ее, отряхнул. Потом, словно что-то сообразив, протянул ее Сыроежкину."
    adl_sh2 "Вот, возьми, пожалуйста. Ты, наверное, уронил, когда спал."
    show el upset pioneer close with dspr
    el "Да, спасибо."
    show el sad pioneer close with dspr
    "Сыроежкин чуть покраснел, но говорить, как было дело, не стал."
    "У Сыроежкина нашлась другая тема для разговора. Внимательно посмотрев на Александра, он округлил глаза и уже другим голосом, обращаясь как к старшему, спросил."
    show el surprise pioneer close with dspr
    el "А ты, тот самый Шурик Трофимов?"
    show dct_int_bus_middle_sh surprise with dspr
    adl_sh2 "Да, я… Шурик Трофимов, но почему, тот самый?"
    show el smile pioneer close with dissolve_fast:
        zoom 1.095 xcenter 0.34 ycenter 0.56 rotate -8.9
    el "Ну как же, я читал о тебе в журнале. Победитель трех всесоюзных олимпиад: по программированию, по кибернетике и по робототехнике. Мы по твоей статье в кружке робота собирали."
    show el normal pioneer close
    show dct_int_bus_middle_sh normal
    with dspr
    "И разговор пошел по накатанной многими циклами колее."
    "Можно было не задумываться об ответах, язык сам знал, что нужно говорить. Александр и не задумывался, поглядывая между репликами в окно автобуса."
    "Вот и последняя опора ЛЭП перед воротами, обозначающая внутренний Периметр."
    
    
    $ renpy.sound.set_volume(0.5)
    play sound dct_sfx_bus_braking fadein 1
    pause 1.2
    play sound_loop dct_sfx_loop_bus_moves_slow
    pause 0.7
    stop sound fadeout 2
    "Автобус начал плавно сбавлять ход. Зашевелились пионеры, самые нетерпеливые уже откинули подлокотники кресел и сидели выставив чемоданы, и свесив ноги в проход, готовые сорваться с места и побежать к дверям, в ответ на шипение пневматики."
    show dct_int_bus_another_middle
    show dct_int_bus_another_middle_mz_body
    show dct_int_bus_another_middle_mz_head smile
    show d_sf serious pioneer:
        xzoom -1.0 yzoom 1.0 xcenter 1.2 ycenter 0.57
        pause 1
        linear 2.2 xzoom -0.8 yzoom 0.8 xcenter -0.15 ycenter 0.54
    show d_sf_chevron_mirror:
        xzoom -1.0 yzoom 1.0 xcenter 1.2 ycenter 0.57
        pause 1
        linear 2.2 xzoom -0.8 yzoom 0.8 xcenter -0.15 ycenter 0.54
    show dct_int_bus_another_middle_close_seats
    with dissolve
    pause 2
    "По проходу быстрым шагом прошел Семен. Да, Александр узнал его, вот только, много циклов назад, перед расставанием в поселке, Семен выглядел на семнадцать лет, а сейчас казался двадцатипятилетним."
    th "Видимо активировался, сумел встроиться в систему, и система привела его облик в соответствие с новой функцией. Помнил бы я циклы, я бы знал точно"
    scene dct_int_bus_middle
    show dct_int_bus_middle_sh_body
    show dct_int_bus_middle_sh normal
    show el sad pioneer close:
        zoom 1.095 xcenter 0.31 ycenter 0.57 rotate -12.9
    with dissolve
    stop sound_loop fadeout 2
    
    
    $ renpy.sound.set_volume(0.3)
    play sound sfx_bus_stop
    "Австобус начал разворачиваться, перед тем, как окончательно остановиться и открыть двери, а пионеры приготовились сорваться с места и устроить свалку перед дверями."
    play sound2 dct_sfx_whistle     # Проигрывание свистка на втором звуковом канале (чтоб не пересекался с автобусом)
    play music music_list['eat_some_trouble'] fadein 1
    show dct_int_bus_middle_sh surprise
    show el shocked pioneer close:
    with dspr
    "И в этот момент от передних сидений раздался резкий свисток. Это было настолько неожиданно, что все вздрогнули."
    show dct_int_bus_middle_sh normal
    show el surprise pioneer close:
    with dspr
    th "Не по программе, хотя да, он же активированный."
    scene dct_int_bus_people
    show dct_int_bus_people_sl_mi_sf
    show dct_int_bus_people_vi sitdown
    with dissolve
    me "Уважаемые пионеры и примкнувшие, наш самолет совершил посадку в аэропорту «Совенок один», через несколько минут подадут трап, а пока прослушайте…"
    "В голосе Семёна явственно звучали интонации опытного экскурсовода."
    th "Дурачится..."
    "Не то, чтобы Александр был против, но не полагалось так."
    "Пионеры должны были сейчас, под управлением заложенных алгоритмов, встать и, устроив, конечно, свалку, но свалку управляемую и декоративную, выйти из автобуса. И уже там, на площадке, при появлении вожатой, жесткие поведенческие алгоритмы первого и второго уровней должны были перестать действовать."
    "А то, что делал сейчас Семен, оно просто сбивало с толку управляющие программы… Александр опять прислушался к Семену."
    me "…поэтому тот, кто выйдет последним…"
    show dct_int_bus_people_vi standup with dspr
    pi2 "Тот — тухлый помидор!"
    "В речь Семёна вклинился неизвестный пионер из среднего отряда."
    "Вернее Александру он был неизвестный, но не Семену, заблокировавшему входные двери. А тот, в свою очередь, делая ударение на последнем слоге имени, отчего оно начало звучать на французский манер, парировал:"
    me "Умница, Виктор. Но ты не угадал."
    me "Я всего лишь хотел сказать, что тот, кто покинет автобус последним, получит право выбрать себе любой домик для проживания. А первого выскочившего на улицу администрация заселит в домик по своему выбору."
    show dct_int_bus_people_vi sitdown with dissolve_fast
    "С задних рядов раздался возмущённо-насмешливый возглас:"
    dvp "Эй!"
    me "Поправку принимаю. Это касается только пионеров среднего отряда и их домиков."
    
    
    $ renpy.sound.set_volume(1.0)
    $ renpy.music.set_volume(0.5, delay=1.5)
    scene dct_ext_buses_filled
    show black
    with dissolve
    $ set_mode_nvl()
    window show
    pause 1
    hide black with dissolve
    
    "Давно уже вышел младший отряд, был встречен вожатой и построен у ворот. Только две девочки и три мальчика подбежали к компании с заднего сиденья Икаруса. Обнялись, некоторые с удовольствием, некоторые неловко, но все равно с радостью, и убежали назад, к своим."
    "Давно уже чинно (по сравнению с октябрятами чинно и степенно) вышел из Икаруса отряд старший и стоял кучкой на обочине."
    "Уже Ольга Дмитриевна подошла к старшим пионерам, заглянула в автобус, шепнула на ухо Семену: «Сам кашу заварил, сам и расхлебывай», — и увела октябрят в лагерь."
    "А средний отряд продолжал сидеть в автобусах, причем, как в Икарусе, так и, откуда-то прознавшая об праве выбора домиков, та часть отряда, что ехала в Лазе, вместе с октябрятами."

    "Старшие отошли с асфальта в тень и уселись, кто на чемоданы, кто просто на траву.\n"
    d_us_nvl "Алис, может, уведешь старшаков? А то им еще белье и форму получать, и домики, кстати, занимать."
    d_dv_nvl "И пропустить всё веселье?"
    
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    $ renpy.music.set_volume(0.25, delay=1.5)
    "Александр сидел на своем чемодане, вполуха слушал Сыроежкина, севшего на своего любимого конька о перспективах робототехники, и, неожиданно для себя, начал мысленно анализировать сбой поведенческого алгоритма среднего отряда."
    th "Нет, со своими механизмами я бы элементарно разобрался: перезагрузил, и всё. А эти, это Виолетты подопечные, и даже не Виолетты, а того, кто там у нее главный по этологии был. Длинный такой блондин, имени не помню."
    th "Можно и этих перезагрузить, конечно. Сейчас самое начало цикла, они даже не поймут ничего. Взять у Глафиры Выключатель и привет."
    th "Но что делать с активированными, уж очень они все похожи на людей? Распространяются ли на них этические нормы? Хотя у Глафиры двадцать пять лет назад рука не дрогнула, пусть она и любила их. Хватило у нее совести, хватило и у меня, пусть я и не довел дело до конца."
    th "Стоп! Вот мысли об этом — табу! Только, где та Глафира? И выключатель? Ну хорошо, если нельзя перезагрузить, то надо на них влиять с другой стороны…"
    
    window auto
    $ renpy.music.set_volume(0.0, delay=1.5)
    $ set_mode_adv()
    play ambience ambience_camp_entrance_day fadein 1.5 
    show dv laugh pioneer2 with dissolve:
        xcenter 0.76
    dv "Сенька, давай их пинками выгоним!"
    show d_sf laugh pioneer at left with dissolve
    me "Что? И Катьку с Викой, Макса и Витьку тоже выгонишь? Дружескими пенделями?"
    show dv grin pioneer2 at fright with dissolve_fast
    dv "М-да, проблема. А может, это не те? Не наши?"
    show d_sf smile pioneer with dspr
    me "Те-те. Я проверил."
    th "… а активированные, оказывается, могут дружить с пассивными. Интересно, чья это заслуга? Так, я, кажется, нашел выход."
    th "Но стоит ли помогать «Сеньке»? Наверное, стоит. Я, правда выйду из образа и подставлю Шурика, но не сидеть же здесь до конца цикла"
    show d_sf normal pioneer with dspr
    "Александр встал, извинился перед Сыроежкиным и, не глядя ни на кого, подошел к Семену."
    show sh serious pioneer with dissolve:
        xcenter 0.53
    adl_sh2 "Простите пожалуйста. Можно вас на пару минут?"
    show d_sf smile pioneer with dspr
    hide dv with dissolve
    me " Да, конечно. И, Александр, можно на «Ты»?"
    adl_sh2 "Тогда я Шурик, в крайнем случае, Саша. А Александр… Я… тебе уже, помнится, говорил…"
    

    $ renpy.music.set_volume(1.0, delay=3.5)
    stop ambience fadeout 2
    hide d_sf
    hide sh
    with dissolve2
    "Пять минут спустя сидячая забастовка среднего отряда закончилась."
    scene dct_int_bus_people
    show dct_int_bus_people_sf smile
    show dct_int_bus_people_vi sitdown
    with dissolve
    "Повеселевший Семен, сначала попросил весь средний отряд собраться в одном автобусе, чтобы не повторять два раза. Потом, когда просьба была выполнена и все пионеры собрались в Икарусе, от администрации лагеря последовала еще одна вводная."
    
    me "Я говорил, что последний вышедший из автобуса будет сам выбирать себе домик?"
    d_gays "Да-а-а!"
    me "Я говорил, что первого вышедшего из автобуса, администрация поселит не спросив его мнения?"
    kids "Да-а-а!"
    show dct_int_bus_people_sf normal with dspr
    me "Так вот, продолжаем разговор. Вас здесь сорок два человека."
    "Александр, услышавший эти слова, пожал плечами."
    me "Домик себе будет выбирать не один — самый последний, а домики будут выбирать те двадцать один человек, что выйдут последними."
    me "Последний выбирает из двадцати одного домика, предпоследний из двадцати, пред-предпоследний из девятнадцати. Вы меня поняли. Согласны?"
    kids "Да-а-а!"
    show dct_int_bus_people_sf laugh with dspr
    me "Но сначала администрация расселит вышедших первыми пионеров, в лучшие домики. А вы уже напрашивайтесь к ним в соседи. Если они, конечно, захотят вас взять."
    kids "У-у-у-у…"
    me "Вот такое у-у-у-у… Или вы сейчас разобьетесь на пары и сами разберетесь, кто, где и с кем будет жить."
    "Семен сунул в руки ближайшему пионеру план лагеря."
    show dct_int_bus_people_sf smile with dspr
    
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    me "Кстати, для этого не обязательно сидеть в автобусе."
    
    
    $ renpy.music.set_volume(1.0, delay=0)
    stop music fadeout 1.5
    scene bg ext_square_sunset
    show black
    with dissolve
    pause 1.5
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ set_mode_nvl()
    window show
    play music peritune_gentle_theme_piano fadein 1.5
    hide black with dissolve
    pause 0.5
    
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
    extend " визит на склад за бельем и пионерской формой, где задерганные Алиса с Ульяной рычали на бестолковых пионеров. («Ульяна тоже выросла и теперь старше Алисы», — отметил про себя Александр)."
    scene bg ext_playground_day
    show int_house_of_dv_day:
        xcenter 0.5 ycenter 0.5     # это чтоб потом зумировать красиво
    show int_house_of_sl_day
    show dct_int_house_of_el_day
    show int_house_of_un_day
    show dct_lineup_mi_not_us
    show int_dining_hall_people_day:
        alpha 1
        pause 3
        linear 1 alpha 0
    with blinds
    extend " Ужин и вечерняя линейка, на которой вожатая зачитала правила внутреннего распорядка и познакомила пионеров с персоналом лагеря."
    show dct_lineup_mi_not_us:
        easeout 1 ycenter 1.5
    show int_house_of_un_day:
        pause 2
        easeout 1 xcenter -0.5
    show dct_int_house_of_el_day:
        pause 4
        easeout 1 ycenter -0.5
    show int_house_of_sl_day:
        pause 6
        easeout 1 xcenter 1.5
    extend "\nА после линейки наступило некоторое затишье: пионеры распаковывали чемоданы, Алиса с Ульяной, умаявшиеся на складе, валялись у Алисы в домике и неспешно беседовали"
    show int_house_of_dv_day:
        anchor (0.5, 0.5)
        easeout 1 zoom 2 alpha 0
    extend ", Семен валялся на лавочке около футбольного поля, закинув руки за голову, разглядывая облака и размышляя"
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
    extend ", Ольга Дмитриевна, у себя в домике, спешно перепечатывала на взятой в библиотеке машинке «План мероприятий на I смену»."
    
    
    stop music fadeout 1.5
    scene dct_int_house_of_el_sunset
    show el sad pioneer at cleft
    show sh serious pioneer at right
    show black
    with dissolve_fast
    play ambience ambience_int_cabin_evening fadein 1.5
    pause 1
    window auto
    $ set_mode_adv()
    hide black with dissolve_fast
    el "Шурик, ты не хочешь в библиотеку записаться?"
    th "В библиотеку? И читать здешнюю идеологическую макулатуру и книги о приключениях?"
    adl_sh2 "Знаешь, Сергей, наверное, у меня не будет времени на библиотеку."
    show sh normal pioneer with dspr
    adl_sh2 "Но я подумаю до завтра."
    "Александр спохватился, что не знает — записывался ли Шурик в библиотеку."
    show sh serious pioneer with dspr
    adl_sh2 "Все равно с обходными бегать. Ты иди сейчас, если хочешь. Заодно посмотришь, что там есть. А я... поработаю."
    show el serious pioneer with dissolve_fast
    "Несколько минут Сергей колебался между интересом к науке и интересом к Жене."
    show el laugh pioneer with dspr
    "А потом убежал, для очистки совести пообещав, что вернется, как только запишется."
    stop ambience fadeout 2
    
    
    play music music_list['dance_of_fireflies'] fadein 2
    scene dct_ext_library_sunset with dissolve
    show dct_el_shuttles_back_and_forth:      # Сборная картинка: Электроник курсирует туда-сюда
    "Это «как только» продлится почти до полуночи. Сперва Сыроежкин несколько раз, с независимым видом, пройдет мимо библиотеки, как будто он там случайно гуляет."
    hide dct_el_shuttles_back_and_forth with dissolve_fast
    show el angry pioneer far at right with dissolve
    show el angry pioneer at cright with dissolve
    show el angry pioneer close at center with dissolve
    
    "Потом, почти решившись, подойдет к двери и уже почти возьмется за ручку, когда услышит смех и голоса Мику и Саши."
    show el shocked pioneer far at center with dissolve
    "Сыроежкин испуганно отпрыгнет и снова сделает вид, что он здесь ни при чем."
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
    "Девочки, даром что не проснувшиеся, прекрасно сообразят, в чем дело и, проходя мимо, захихикают."
    
    scene bg ext_library_night with dissolve2
    $ night_time()
    $ persistent.sprite_time = "night"
    "Отчего бедный Сыроежкин потеряет половину решимости, сделает еще круг по лагерным «Ульянкиным тропам» и вновь окажется у библиотеки только через полчаса после ее закрытия."
    show el sad pioneer close with dissolve
    "Подергает дверь, вздохнет, взъерошит волосы и уйдет на берег между пристанью и пляжем."
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
    "А Женя, наблюдавшая за всеми этими танцами через окно, и прождавшая Сыроежкина еще двадцать минут после закрытия, расстроенная засядет в своем домике и будет грустить."
    scene dct_int_house_of_sl_night
    show mz normal pioneer close
    with dissolve
    th "Вот, в общем-то, неплохой и, кажется, серьезный и интеллигентный парень так и не решился зайти. Я бы извинилась перед ним."
    th "Может, моя жизнь бы изменилась?"
    th "Зря я на него наорала там, в автобусе. Он же ничего плохого и не хотел. Может, завтра зайдет?"
    show d_mz sad pioneer close as mz with dspr
    
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Ну почему, почему у меня всегда все наперекосяк выходит?"
    stop music fadeout 2
        
    
    scene dct_int_house_of_el_sunset
    show sh serious pioneer
    show black
    with dissolve2
    play ambience ambience_int_cabin_evening fadein 1
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    hide black with dissolve
    "Александр Трофимов, после ухода соседа подождал еще минут тридцать, потом поднялся, и, оставив записку Сыроежкину, отправился в кружок кибернетики."
    hide sh with dissolve
    "До нужного ему времени оставалось еще больше двух с половиной часов, но Александру делать в домике было совершенно нечего — домик принадлежал Шурику."
    play ambience ambience_camp_center_evening fadein 1.5
    scene dct_ext_clubs_sunset with dissolve
    "Хотелось просто посидеть в одиночестве, когда никто не будет восхищаться «стальным фанатиком науки» (кажется так), но не получилось."
    play ambience ambience_int_cabin_evening fadein 1.5
    scene bg int_clubs_male_sunset
    show d_sf normal pioneer at left:
        zoom 1.25 ypos 0.20
    show d_us normal dress at right:
        zoom 1.25 ypos 0.08
    with dissolve
    "В клубе пахло свежезаваренным чаем и выпечкой, в клубе оказались Семен и Ульяна. Александр мысленно поморщился, но не выдал своего неудовольствия."
    show d_sf laugh pioneer with dspr
    me "Это ведь Шурика обиталище, а не Александра. А я все-таки замначальника здешней богадельни. Так что, присоединяйся."
    show d_sf smile pioneer with dspr
    show d_us smile dress with dspr
    us "Мы скоро уйдем. Попрощаемся с тобой и уйдем. А то нехорошо тебя просто так отпускать."
    show d_sf normal pioneer with dspr
    "Александр молча сел на свободный стул, налил, в придвинутый к нему Ульяной стакан, чаю из литровой банки, благодарно кивнул, и внимательно посмотрел на Ульяну."
    adl_sh2 "Ульяна, та самая? Нашлась?"
    "Александру не хотелось, чтобы кто-то начинал выспрашивать о причинах его поведения, или уговаривать остаться. Поэтому он и решил задать тему разговора."
    show d_us shy dress with dspr
    adl_sh2 "Я подозревал, что здесь именно ты, а теперь вижу."
    us "Да, наверное. Мне… нам подарили одну фотографию. И на ней точно мы с Сёмкой."
    stop ambience fadeout 6
    play music brush_marks fadein 6
    us "И я мало что помню, но как я печатала эту фотографию, я вспомнила. Сыроежка печатал фото по чьему-то заданию и я попросилась в лабораторию со своей пленкой."
    show d_us normal dress with dspr
    us "Ты знаешь, Саша, он почти не изменился с тех пор. Все тот же очень способный, безотказный, старательный и очень наивный мальчик."
    "Ульяна постепенно заводилась, это чувствовалось по голосу."
    show d_us hurt dress with dspr
    us "Он все рассказывал, что отучится еще год и поедет в Москву, поступать в Бауманку. Как он жалеет о том, что побоялся написать заявление и сдавать выпускные экзамены за десятый класс экстерном, и теперь из-за этого еще год в школе потеряет."
    us "А я тогдашняя слушала и все не решалась ему сказать, что никакого будущего, никакого «через год» и никакой Бауманки у него не будет. Что он так и останется тут, вечным Сыроежкой. Универсальным помощником-лаборантом."
    us "Александр, за что вы с ним так поступили? За что вы с ними так поступили?"
    show d_sf sad pioneer with dspr
    us "Я понимаю, копии, те — побочный эффект, дубликаты — они хоть информированы были, подлинники — вообще настоящие. Но миксы? Которых можно было и не создавать, не отправлять в этот бесцельный бег по кругу!"
    us "Я спрашивала у Сёмки, но он всего лишь дубликат, а вы — последний подлинник здесь. Я бы у бабы Глаши спросила, но тогда, когда она ушла, я еще не понимала ничего."
    us "Виола и Анатолий — Сёмка сбросил их до нуля, тоже не спросишь. Остались вы. Я вас не обвиняю, но хочу понять, хочу услышать хоть какой-то ответ."
    us "Вы сейчас уйдете, я не собираюсь вам мешать. Но в следующем цикле я задам тот же вопрос."
    show d_us hurt dress at right with dissolve_fast:
        zoom 1.0 ypos -0.05
    hide d_us with dissolve_fast
    "Ульяна вскочила на ноги и выбежала из здания клубов. Александр проводил Ульяну непонимающим взглядом."
    adl_sh2 "Семен.{w=0.4} Это ведь твой оригинал был заведующим лабораторией синтеза биосистем. Если хочешь Ульяне помочь — покопайся в памяти."
    adl_sh2 "А моё мнение: всё, что может быть создано — должно быть создано. Вопрос только правильного применения."
    show d_sf laugh pioneer with dspr
    me "«Какая великолепная физика!» Кроме того, что не мешать, я могу еще что-то для тебя сделать?"
    show d_sf serious pioneer with dspr
    adl_sh2 "У тебя есть Выключатель?"
    me "Нет, я уничтожил их. И свой, и Виолы."
    adl_sh2 "Тогда ничего."
    show d_sf serious pioneer at center:
        zoom 1.0 ypos 0.0
    show sh serious pioneer at fright
    with dissolve
    "Они поднялись одновременно, подошли к двери, Александр, как хозяин, протянул руку Семену, прощаясь."
    adl_sh2 "Спасибо, что зашли. И, передай Ульяне, пожалуйста, что когда рожают детей, то их согласия тоже не спрашивают"
    show d_sf normal pioneer with dspr
    show d_sf normal pioneer with dspr
                      
    $ persistent.sprite_time = "sunset" # Прописано, чтобы при обратной перемотке цвета не сбивались.
    adl_sh2 "Еще примерно час, если что понадобится, то обращайся. После — не приходи."
    stop music fadeout 1.5

    
    scene dct_int_coaching_room2
    show d_us sad dress at right:
        ypos -0.05
    show black
    with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_evening fadein 1.5
    hide black with dissolve
    "Когда пришел Семен, Ульяна сидела в бывшей тренерской, а теперь официальной квартире Персуновых, и всхлипывала."
    show d_sf normal pioneer at cleft with dissolve
    us "Сёмк, ты ведь у Шурика узнать что-то хотел. А я все испортила. Хотела просто попрощаться с ним, а все испортила."
    us "Не смогла замолчать. Но мне вдруг их так жалко стало. Миксов этих. Что Женю, что Мику, что Сыроежку."
    us "У нас, у всех остальных, хоть какое-то прошлое, но было. Помнишь, как плясала от радости Алиса, когда о своем детстве рассказывала, всё, что вспомнила. Про стрекозу эту."
    us "Хотя там рассказов то на полчаса — копия же. А она это детство все вспоминает и вспоминает. Вот и сегодня тоже."
    us "А у этих то и детства нет — всё придуманное, и вся жизнь только бег по кругу, а когда они проснутся, то ничего."
    show d_sf sad pioneer with dspr
    us "Ни{w=0.2}-че{w=0.2}-го.{w=0.4} Я же сама была в их шкуре. Я же, как проснулась, не могла ничего вспомнить о себе, о своем детстве, ни о настоящем, ни о придуманном."
    us "Знаешь, как это тоскливо. Пока девочки нам ту папку не принесли, и у меня не начала память просыпаться."
    us "А Шурик, ну, он не Шурик сейчас, конечно, но мне так привычнее, спросил: «Нашлась?» — Я-то нашлась, но я вот взяла и о миксах вспомнила. Они то никогда не найдутся."
    show d_sf smile pioneer with dspr
    "Семен привычно коснулся кончика Ульянкиного носа указательным пальцем."
    me "Рыжик, куда ты дела Ульянку?"
    show d_us normal dress with dspr
    us "Да никуда я ее не дела. Тут она, где всегда. Просто бывает и Ульянке грустно."
    show d_sf normal pioneer with dspr
    us "Ты лучше скажи, Сёмк, почему ты в автобусе не стал делать, как Шурик предложил? А взял и поступил по своему. Ведь ты же этим пионерам ничего нового не сказал. А они взяли и послушались."
    me "Просто, Рыжик, те пионеры и сами понимали, что сидячая забастовка зашла слишком далеко. Вот и ухватились с радостью за компромисс с администрацией."
    me "Помнишь, как в прошлом цикле двое чуть не подрались из-за Катьки? И зависли на полушаге к драке, и тоже не знали, что делать."
    me "Алгоритмы поведения сыпятся постепенно. Пионерам все больше приходится думать своей головой, а голову тренировать нужно."
    
    $ sunset_time()                     # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    me "Вот я и пытаюсь делать так, чтоб потом не бегать за ними и носы не подтирать, чтобы они сами за себя думали. Часто вот такие казусы получаются, как в автобусе."
    stop ambience fadeout 1.5
    
    
    scene dct_int_clubs_male_night_light_mon
    show sh serious pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    show black
    with dissolve
    $ night_time()
    $ persistent.sprite_time = "night"
    play music fm_freemusic_chillout_music fadein 1.5
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1.5
    hide black with dissolve
    "А Александр сидел перед включенным компьютером и набивал по памяти длинную последовательность знаков, лишенную видимого смысла."
    play sound_loop sfx_computer_noise fadein 0.5
    "Нажал «Ввод», подождал, пока на экран не выползет таблица, просмотрел ее, удовлетворенно кивнул, достал наушники и подключил их к компьютеру."
    show sh normal pioneer close with dspr
    "Посмотрел на часы, до нужного времени оставалось еще десять минут, хватит на одну сигарету."
    show sh serious pioneer close with dspr
    "Выдвинул нижний ящик стола, вытряхнул из него электрический хлам: обрезки проводов, мотки припоя, старые динамики, — и снял фальшивое дно."
    "Несколько пачек сигарет. «Дожили, — подумал, — талонную „Приму“ храню как величайшую драгоценность»."
    "Достал из начатой пачки одну сигарету, потом, вернув ящик в прежнее состояние, вышел на крыльцо."
    stop sound_loop fadeout 1.5
    
    play ambience ambience_camp_center_night fadein 1.5
    $ renpy.music.set_volume(0.35, delay=1.5)
    scene dct_ext_clubs_night_light_inside
    show sh serious pioneer far at cright
    with fade
    "Чтобы случайный пионер не заметил огонек, приходилось курить в кулак, и прятаться как пацану."
    "Александр курил не торопясь и вспоминал...{w} Хотя и всеми силами пытался этого не делать, с самого времени пробуждения в автобусе."
    "Всплыл в голове развернутый вариант ответа Ульяне, вторую часть которого он не стал озвучивать: «Когда рожают детей, то их согласия тоже не спрашивают. Но потом дети почему-то предпочитают жить»."
    "«Па, ты зачем наврал Семену?»{w} — показалось что детский голос задал вопрос."
    "«Лучше сразу отсечь лишние воспоминания, вопросы и разговоры», — мысленно ответил."
    "«И меня?»{w}\n«И тебя»."
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
    "Александр затушил окурок, закопал его, подвернувшейся кстати щепкой, в рыхлую землю, вернулся в кружок."
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1.5
    scene dct_clubs_male_comp_night
    show dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_dim:
        xcenter 0.5 ycenter 0.45
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    "Надел наушники, сел перед экраном, стер содержимое одной из ячеек таблицы, заменив его на еще одну бессмысленную цепочку из символов, ввел пароль, и, как полчаса назад, нажал «Ввод»."
    play sound_loop sfx_computer_noise fadein 0.5
    show dct_clubs_male_comp_sh with dissolve_fast:
        xcenter 0.5 ycenter 0.45
    hide dct_clubs_male_comp_table with dspr
    "В наушниках зашумело, а таблицу на экране сменило его собственное лицо, постепенно распадающееся на хаотически мелькающие разноцветные треугольники."
    show dct_clubs_male_comp_sh_crumble with dissolve_fast
    hide dct_clubs_male_comp_sh
    pause 9
    show dct_clubs_male_comp_night_light_mon:
        linear 0.5 alpha 0.5
    hide dct_clubs_male_comp_sh_crumble with dissolve_fast
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
    "Александр встал, с видимым трудом выключил компьютер, и деревянной ковыляющей походкой зашагал к выходу из кружка и дальше в сторону площади и домика."
    $ renpy.music.set_volume(0.3, delay=1)
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_clubs_night
    show sh upset pioneer far
    with fade
    "«Это инерция, сейчас все закончится. Удачи тебе!» — думалось тоже с трудом."
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
    "«Удачи тебе!»{w=1.2}\nШурик вздрогнул, огляделся, узнал памятник Генде и удовлетворенно кивнул." with hpunch
    show sh normal pioneer close
    "Посмотрел на часы, было самое начало первого часа ночи."
    th "Надо же, заработался. И голова болит нехорошо, не пришлось бы завтра в медпункт обращаться. Планов много, а смена такая короткая. Надо выспаться и все пройдет"


    scene black with fade
    $ renpy.music.set_volume(1.0, delay=1.5)
    scene dct_ext_camp_entrance_night
    show dct_jn_near_gate
    with fade
    "Маленькая серебристая фигурка, незаметная ночью на фоне крашенных серебрянкой ворот, была неподвижна, как статуя."
    "Она мало походила на человека, половина ее алюминиевого лица была закрыта черным зеркальным щитком, а вместо носа и рта чернела совмещенная решетка газоанализатора и динамика."
    show d_jn:
       zoom 4.0 xcenter 0.0 ycenter 1.2 alpha 0
       linear 2.5 xcenter 0.5 alpha 0.7
       linear 2.5 xcenter 1.0 alpha 0
    $ renpy.pause(2, hard=True)
    
    $ night_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "Но любой наблюдатель сказал бы про эту фигурку три слова: «Грусть и печаль»."
    stop ambience fadeout 2
    stop music fadeout 2
    scene black with dissolve2
   
    
    $ renpy.pause(3)
    
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')

    
