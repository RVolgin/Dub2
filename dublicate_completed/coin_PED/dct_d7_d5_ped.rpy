    ################
    #Глава 6. d7-d5#
    ################


label dct_d7_d5_ped:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- d7-d5\n(pedantic)"
    $ night_time()
    $ persistent.sprite_time = "night"
    scene black
    stop sound
    stop ambience
    stop sound_loop
    play music "<from 19.0 loop 0.0>sound/music/a_promise_from_distant_days.ogg"
    show headline_text2 u"Глава VI. d7-d5" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    play ambience ambience_int_cabin_night fadein 1
    $ renpy.music.set_volume(0.25, delay=2)
    scene dct_int_coaching_room2_night with dissolve
    "Семён ворочался, всё никак не мог уснуть, пока Ульяне не надоело и та не шикнула на Семёна."
    us "Сёмк, вообще ты должен сейчас сопеть носом в угол, а ты дыру в матрасе протираешь. С тобой всё в порядке?"
    me "Не спится, Рыжик. Пойду подышу."
    us "А который час, Сём?"
    show dct_insomnia with squares
    "Семён посветил фонариком на циферблат будильника."
    me "Час быка.{w=.4} Два часа ночи."
    stop ambience fadeout 1
    $ renpy.music.set_volume(1.0, delay=1.5)
    scene bg ext_house_of_dv_night with fade
    "Ночь была в самой глухой своей фазе, спали даже самые отъявленные нарушители режима."
    "Алисе опять снился сон про шары. И она там, во сне, почти решилась шагнуть на ближайший."
    scene dct_ext_house_of_un_night with pushdown
    "Лене снилась женщина, тянущая к ней руки. Глядящая ей в глаза — кто первый сдастся и отведёт взгляд."
    "И близкие, держащие свои руки у Лены на плечах."
    scene dct_ext_house_of_sl_night with pushdown
    "Мику снилась музыка и почему-то незнакомый автобус, в котором она и какой-то мальчик едут в пионерский лагерь."
    "На улице зима, а они едут в пионерский лагерь."
    "Мальчик дремлет у неё на плече, а Мику хочет повернуть голову, чтобы посмотреть на него, и понимает, что этого нельзя делать, что тогда случится что-то непоправимое."
    scene dct_ext_house_of_el_night with pushdown
    "Шурику опять снились сны Александра — опять он видел во сне живых Яну и Яну."
    play ambience ambience_camp_center_night fadein 1
    $ renpy.music.set_volume(1.0, delay=0)
    stop music fadeout 4
    scene dct_ext_beach_night_view_from_gym with fade
    "Ближайший дежурный фонарь освещал хозяйственные ворота, да вход в столовую был ярко освещён своими фонарями."
    "Луна, выросшая в три четверти, висела где-то за лесом, но света звёзд хватало для глаз."
    "Семён и Ульяна, укрывшись одной курткой на двоих, сидели на крыльце спортзала и смотрели поверх главной аллеи на пустой пляж и слабо мерцающую реку за ним."
    "Кто-то мелкий шуршал в траве, неясные тени летучих мышей проносились над головами. Свежий воздух прогнал последние остатки сна."
    us "Сём, помнишь, в наш первый цикл, когда мы ходили за Алисой в бомбоубежище. Ты ещё спросил о звёздах, что-то вроде: «Интересно, здесь те же звёзды, что и дома?»"
    me "Помню."
    us "Вот и я себе сейчас этот вопрос задаю."
    us "Знаешь, я думаю, что звёзды для всех общие. И если мы отсюда сможем улететь к ним, то, вернувшись назад, окажемся где угодно. Здесь, в соседнем узле, в…"
    us "В материнском мире.{w=.5} Я название придумала, а то мы всё «снаружи» да «снаружи»."
    me "В мирах, Рыжик."
    me "Я так подозреваю, что материнский мир не один."
    me "Тот Пионер, который приходил ко мне. И Семён, который сюда приедет через два дня, которого всё ждет Лена. Они ведь из разных миров."
    me "И сама Лена — она тоже у меня под подозрением, что она из нашего мира."
    me "А раз Лена, то и Алиса, раз у них общие воспоминания из детства."
    me "Я не могу ничего доказать, но подозреваю, что они, их оригиналы, пришли сюда из других миров."
    
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "Семён замолчал, не желая продолжать, вспомнив ещё мельком оброненные бабулей слова о том, что когда удалось пробиться сюда — оказалось, что здесь уже бывали люди."
    window hide
    
    
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty fadein 1
    scene bg int_dining_hall_day
    show d_bg normal suit at cright:
        yalign .1
    with blinds
    window auto
    d_gd "Попадёшь в двести первый узел — увидишь там развалины домов."
    d_gd "Десяток старых срубов, примерно там, где домик твоих рыжих подружек."
    
    $ day_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    d_gd "Кто и когда там жил — мы не знаем. На всякий случай просто не стали тот узел заселять, так он и стоит пустой."
    window hide
    play ambience ambience_camp_center_night fadein 1
    scene dct_ext_beach_night_view_from_gym
    show d_jn:
        zoom .15 xcenter .74 ycenter .545
    show dct_ext_beach_night_view_from_gym_bush
    with blinds
    $ night_time()
    $ persistent.sprite_time = "night"
    window auto
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
    show black with dissolve
    window hide
    
    pause 0.5
    
    
    $ day_time()
    $ persistent.sprite_time = "day"
    window auto
    play music brush_marks fadein 1
    scene dct_coin_bus-stop
    show dct_dream_veil at shiver
    with dissolve
    "А Шурику действительно снова снился сон Александра."
    show d_jn_old angry:
        zoom 0.75 xcenter 0.39
    show d_jn_old normal as d_jn_old_norm:
        zoom 0.75 xcenter 0.39 alpha 1
        pause 1.6
        linear 0.2 alpha 0
    show d_jn_young normal:
        zoom 0.75 xcenter 0.31
    with dissolve
    "Опять ему снились обе Яны, стоящие на остановке.{w=.7} И опять старшая Яна ругала его во сне."
    d_jn_old "Ты снова пришёл сюда. Неужели ты не понимаешь, что только разрушаешь себя самого? Что ты просто отдаёшь кусочек себя каждый раз, когда приходишь? Что мы даже не фантомы? Ты же знаешь, чем всё кончается."
    "«А может, я и хочу, чтобы всё так и кончилось», — думает во сне Шурик.{w} Нет, не Шурик, а тот человек, чей сон он видит."
    "Всё уже много раз повторялось, в том числе и этот сон, и этот человек снова молча смотрит на Яну."
    "Кирпичная остановка; бетонный забор с одной стороны улицы, и глинобитная стена, которую офицеры с полигона называют «дувал» — с другой; пыльные пирамидальные тополя, растущие в два ряда между проезжей частью и забором; железные ворота в заборе, сейчас приоткрытые — это всё воспринимается попутно."
    "Главное сейчас — не отрываясь смотреть по очереди на одну и вторую Яну."
    "Словно прочитав мысли, Яна-старшая продолжает:"
    show d_jn_old cry with dspr
    d_jn_old "А я не хочу, слышишь! Я слишком тебя любила, чтобы позволить тебе исчезнуть!"
    show d_jn_young normal with dissolve_fast:
        zoom 1 xcenter 0.33 ycenter 0.833
    "А Яна-младшая — та просто прижимается к Шурику и обещает, что позвонит сразу же, как только они окажутся у бабушки."
    show d_jn_old normal
    show d_jn_young laugh
    with dspr
    d_jn_young "Я телефон в трех местах записала и ещё выучила, вот!"
    show d_jn_young dontlike with dissolve_fast:
        zoom 0.75 xcenter 0.31 yalign 0.0
    "Нарастающий шум мотора, который мешал разговору в течение всего сна, становится уже совершенно невыносимым, и вот из-за угла, осторожно высунув сперва свою щучью морду, выворачивает БТР и следом за ним совершенно бесшумный в сравнении с БТР Икарус."
    show dct_dream_sh_third_BTR_bus behind d_jn_old with dissolve
    "С брони спрыгивает незнакомый майор, отдаёт честь:"
    show d_jn_young normal with dspr
    show dct_dream_sh_third_major behind d_jn_young at right with dissolve:
        zoom 0.68 yalign 1.0
    d_maj "Все готово?{w=0.5} Хорошо."
    "Майор поворачивается к женщинам."
    d_maj "Садитесь, пожалуйста, в автобус."
    hide d_jn_old
    hide d_jn_young
    with dissolve
    "А потом, когда женщины в сопровождении бойца, помогающего с чемоданами, уходят к Икарусу, добавляет:"
    show dct_dream_sh_third_major at cright with dissolve_fast:
        zoom 1.0 yalign 0.0
    d_maj "Экстремисты захватили и разграбили полигон и движутся на город. Получен приказ: эвакуировать весь гражданский персонал."
    d_maj "Автобус не успеет обернуться, поэтому через час за вами подойдёт Урал, будьте дома."
    d_maj "Вот, распишитесь здесь."
    "Шурик расписывается в разграфленном листе: «С приказом об эвакуации ознакомлен. Дата. Подпись. Фамилия»."
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
    window hide
    
    play ambience ambience_int_cabin_night fadein 1
    scene dct_int_house_of_el_night with dissolve
    $ night_time()
    $ persistent.sprite_time = "night"
    window auto
    "Проснувшись, некоторое время Шурик просто лежал; кажется, что слабость, не давшая ему помахать рукой во сне, проснулась вместе с ним."
    "На соседней кровати сопел Сыроежкин."
    th "Вот кому кошмары, наверное, никогда не снятся."
    "Луна, наконец, сумела подняться выше деревьев и светила прямо в окно, так что можно было разобрать даже надпись на спортивной сумке Сыроежкина, закинутой тем на шкаф."
    th "Что же происходит? Что пытается донести до меня подсознание?"
    th "Почему от имени „Яна“ у меня начинает болеть в груди?"
    th "Нет, не зря мы отложили робота и занялись человеческим мозгом."
    th "Завтра настраиваем схему и излучатели, послезавтра проводим эксперимент и в воскресенье обрабатываем результаты."
    "Надо бы было записать только что увиденный сон, он явно был необычным, но не было сил даже пошевелить рукой."
    th "Может быть, я ещё сплю? И мне только снится, что я проснулся?"
    stop ambience fadeout 3
    show black:
        alpha 0
        pause 1.3
        linear 1 alpha 1
    
    $ night_time()
    $ persistent.sprite_time = "night"
    "Только и успел подумать Шурик, чтобы снова уснуть, проспать до самого утра уже совершенно без сновидений и проснуться, не помня ночной сон."
    window hide
    show black as black2 with dspr
    
    pause 0.5
    
    
    play music buddy fadein 1
    scene bg ext_house_of_sl_day with dissolve
    $ day_time()
    $ persistent.sprite_time = "day"
    window auto
    "У Мику со вчерашнего вечера было прекрасное настроение, и даже серьёзный сон, приснившийся под утро, этого настроения не нарушил."
    scene dct_mi_piano1 with squares
    "В кои-то веки у неё попросили помощи, пусть даже и нужно было всего лишь играть на фортепиано для Саши и Максима."
    "А параллельно можно было разговаривать и общаться, и никто от неё не отмахивался."
    scene bg int_house_of_sl_day with squares
    "Вот и сегодня утром можно было встать, открыть форточку, не обращая внимания на бурчащую соседку, пожелать той доброго, наидобрейшего утра и побежать к умывальникам."
    stop music fadeout 2
    play ambience ambience_int_cabin_day fadein 1
    show mz normal glasses pioneer far at cleft with dissolve
    "А на полдороги до двери вдруг остановиться на зов соседки."
    mz "Мику, ты должна знать. Что это значит?"
    show mi upset pioneer close at right with dissolve
    th "Надо же, она имя моё запомнила. Ну-ка, посмотрим."
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
    mi "Женечка, так это же очень просто. Здесь написано: «Первый звук будущего»."
    "Мику, взяв ручку, чуть поправила надпись."
    show mi normal pioneer far with dissolve_fast
    "А по-японски это будет «хатсуне мику», а ещё это моё имя — Хатсуне Мику."
    show d_mz amazed glasses pioneer far as mz
    show mi serious pioneer far
    with dspr
    mi "А где ты это увидела? Нет, я понимаю, если бы ты это у меня в документах подглядела, но все мои японские документы у мамы с папой, а здесь — только советские, потому что папа сказал, что если я еду в советский пионерский лагерь, то у меня и должны быть…"
    show d_mz hope glasses pioneer far as mz
    show mi upset pioneer far
    with dspr
    mi "Женечка?"
    "Мику оборвала сама себя. Было заметно, как Женя колеблется, что ответить."
    show mz normal glasses pioneer far
    show mi normal pioneer far
    with dspr
    "Потом, видимо, что-то решив для себя, она достала из тумбочки серую канцелярскую папку-скоросшиватель и протянула её Мику."
    show dct_mz_1_binder_far at cleft with dissolve
    mz "Вот, почитай. Мне это дала Лена, а той принёс наш физрук: говорит, что это сочинила одна его знакомая."
    hide dct_mz_1_binder_far
    show dct_mi_3_binder_far:
        xanchor .0 xpos .45
    with dissolve
    show d_mz sceptic glasses pioneer far as mz with dspr
    mz "И мне интересно твоё мнение обо всём этом."
    show mi serious pioneer far with dspr
    show d_mz sceptic glasses pioneer close as mz with dissolve
    hide mz with dissolve
    "Сказав так, Женя взяла полотенце и вышла, бросив в дверях:"
    mz "Я в библиотеке."
    hide dct_mi_3_binder_far
    show mi serious pioneer close at center
    with dissolve
    "Мику открыла папку на середине, прочитала полстранички текста."
    "Какая-то пьеса — судя по увиденному, довольно интересная."
    show mi normal pioneer close with dspr
    th "Позже почитаю. От меня же не требуют, чтобы я дала ответ к завтраку?"
    hide mi with dissolve
    "И Мику побежала к умывальникам, обогнав по пути Женю."
    stop ambience fadeout 1
    

    play music music_list['my_daily_life'] fadein 1
    scene bg ext_houses_day
    show mi normal pioneer far:
        zoom 0.8 xcenter 0.591 ycenter 0.52
    show mz normal glasses pioneer at cright
    with dissolve
    
    show mi normal pioneer far with dissolve:
        zoom 1.0 xcenter 0.52 ycenter 0.525
    
    show mi normal pioneer:
        xcenter 0.4 ycenter 0.525
    show mz normal glasses pioneer close:
        xcenter 0.62
    with dissolve
    
    show mi normal pioneer close at left with dissolve:
        ycenter 0.5
    
    hide mi normal pioneer close with dissolve
    
    show mz bukal glasses pioneer close with dspr
    "Женя пропустила мимо себя соседку и поморщилась: постоянный оптимизм Мику раздражал, а сегодня особенно."
    "У Жени же всё вертелась в голове характеристика Жанны из пьесы: «Жанна, заведующая библиотекой. Любит книги, а людей не вполне понимает и потому опасается»."
    play sound sfx_open_water_sink
    scene bg ext_washstand2_day with dissolve
    stop sound fadeout 1
    play sound_loop sfx_water_sink_stream fadein 0.2
    "Когда начала читать — не обратила внимания, а потом, когда начали всё больше и больше вылазить параллели с «Совёнком» и его обитателями, то вспомнила, и не то чтобы обиделась, но что-то ущипнуло за сердце."
    play sound sfx_close_water_sink
    stop sound_loop
    scene bg ext_houses_day
    show mz normal glasses pioneer
    with dissolve
    "Женя применила к себе эту характеристику и вообще всё, что касалось Жанны, и признала:"
    show d_mz sad glasses pioneer as mz with dspr
    th "Да, это я — такая и есть."


    scene bg ext_square_day with dissolve
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
    scene bg int_library_day with slidedown
    "Женя прикрыла за собой дверь и глянула на себя в зеркало."
    scene dct_int_mirror_in_library
    show mz bukal glasses pioneer at center:
        xzoom -1.0
    with squares
    th "Опять эта прядь выбилась."
    show d_mz sceptic glasses pioneer as mz with dspr
    th "Внешность — ладно, внешность неизвестный мне автор даже сильно приукрасил, но вот характер — тут всё правда."
    scene bg int_library_day with squares
    "Начался рабочий день.{w} Тихий и спокойный рабочий день нелюдимой заведующей маленькой библиотеки маленького лагеря."
    "Могла прийти Лена, мог прийти кто-то из малышей за сказками, обещал зайти Максим и мог зайти физрук — всё."
    "Четыре человека в день, с которыми даже разговаривать не обязательно."
    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
    th "Наверное, лучше и не разговаривать."
    th "А то люди обижаются на мои реплики и шутки."
    show d_sf smile sport as d_sf2 behind dct_int_library_standing_desk_front with dissolve:
        zoom 0.95 xcenter 0.35 ypos -0.04
    "Зашёл Семён за тренерскими методичками."
    stop music fadeout 3
    play ambience ambience_library_day fadein 3
    show d_sf sad sport as d_sf2 with dspr
    show d_sf serious sport behind dct_int_library_standing_desk_front:
        zoom 0.95 xcenter 0.35 ypos -0.04 alpha 0
        pause 1.3
        linear 0.2 alpha 1
    "Расписался в формуляре, поднял глаза и внимательно посмотрел на Женю."
    me "Женя, что-то случилось?"
    hide d_sf2
    th "Заметил, надо же."
    extend " Правда, это его обязанность, но всё равно."
    mz "Почему вы так решили?"
    show d_sf normal sport with dspr
    me "Во-первых, я же просил мне не выкать, а во-вторых, раньше ты вела себя иначе."
    show d_sf smile sport with dspr
    me "Раньше ты бы рычала на меня, а сейчас только очками поблёскиваешь из своего угла."
    th "Конечно, иначе. Прочитала этот чёртов текст, и оказалось, что я боюсь вас, людей."
    th "Спросить, откуда он взялся, текст этот, будь он неладен?"
    extend " Куча вопросов про него."
    show d_sf normal sport with dspr
    "Не было в программах, заложенных системой в Женю, правил поведения в подобных ситуациях; не было их и в программах, заложенных в неё создателями-людьми."
    "Никто и никогда не проявлял к ней искреннего участия, и не должен был проявлять."
    "И сейчас Женя мучительно пыталась думать своей головой. Было трудно, мысли разбегались, и даже пойманную мысль не удавалось озвучить."
    "Наконец что-то сформировалось в голове."
    "Это было не главное, о чём хотела сказать Женя. Но это было хоть что-то."
    show d_sf serious sport with dspr
    mz "Семён, я у Лены вчера брала почитать одну распечатку."
    mz "Скажите…{w=.5} Скажи, кто её настоящий автор?"
    show d_sf smile sport with dspr
    me "Понравилось?"
    
    # "Семён присел в кресло напротив конторки заведующей."  # По канону
    
    show d_sf normal sport with dspr
    me "Её действительно написала Мику Хатсуне.{w} Правда, это не та Мику, которую ты знаешь."
    me "Ну а то, что персонажи такие узнаваемые…"
    show d_sf serious sport with dspr
    me "Она вас не знает, и я ей о вас не рассказывал — в этом я уверен."
    
    # "Семён сидел на краешке кресла, подавшись вперед, и смотрел на Женю не отрываясь. Как будто ждал от неё чего-то."    # По канону
    
    "Семён пристально смотрел на Женю, как будто ждал от неё чего-то."
    "Смотрел серьёзно, вовсе без улыбки, а чуть сжав губы, но Жене так было даже легче."
    th "Серьёзный разговор двух серьёзных людей."
    "И никто не посмеётся над ней, и никто не отмахнётся от неё. Просто обмен информацией."
    "Женя узнала про автора распечатки, а взамен сейчас скажет о том, что её беспокоит."
    mz "Скажи, а я действительно такая, как эта Жанна? Отталкиваю от себя?"
    show d_sf normal sport with dspr
    me "Лучше бы ты Лене этот вопрос задала. Она лучше меня в людях разбирается и ответила бы лучше меня — правда, если бы захотела."
    me "Но раз уж спросила меня — то да, отталкиваешь."
    show d_sf serious sport with dspr
    me "Когда кто-то, за редчайшим исключением, приходит в библиотеку — у тебя такой вид, будто ты хочешь немедленно выпроводить посетителя, отвлёкшего тебя от важного дела."
    me "Когда к тебе обращаются — ты всем своим видом показываешь, что снисходишь до человечка.{w} Даже шутки твои очень часто выглядят пропитанными ядом."

    show d_sf normal sport with dspr
    me "А люди ленивы и не хотят понять, что под этим хитиновым панцирем скрывается живой человек."
    me "Очень умный, образованный, смелый, чувствующий и, когда забывает надеть стервозную маску, очень симпатичный."
    
    # "Семён поднялся, выровнял стопку полученных методичек, попросил разрешения оставить их у себя и такое разрешение получил."  # По канону
    
    "Семён выровнял стопку полученных методичек, попросил разрешения оставить их у себя, и такое разрешение получил."

    show d_sf normal sport with dissolve_fast:
        xzoom -0.95
    show d_sf normal sport:
        ease 1.2 xcenter 0.2
    pause 1
    $ renpy.music.set_volume(0.1)
    play music music_list["kostry"] fadein 1.5
    
    "Открыл входную дверь, впустив в библиотеку запахи цветов и звуки музыки, слабо доносящиеся с концертной площадки."
    show d_sf sad sport with dspr
    "И уже с порога непонятно добавил с какой-то обречённой грустью в голосе, как говорят о застарело больном зубе:"
    me "Бедолагу Сыроежкина-то ты точно не отталкиваешь, только я не знаю — алгоритмы это или свобода воли у вас обоих."
    stop music fadeout 1.5
    hide d_sf with dissolve2
    "И, не объясняя ничего, бесшумно закрыл дверь — уже с той стороны."
    scene dct_int_mirror_in_library
    show d_mz sceptic glasses pioneer at center:
        xzoom -1.0
    with squares
    "После ухода Семёна Женя выбралась из-за своей конторки, подошла к зеркалу и, глядя в глаза своему отражению, проговорила:"
    mz "Ну что, Евгения, получили вы по сусалам?"
    mz "Люди от вас, Евгения, разбегаются, и правильно делают."
    show d_mz smile2 glasses pioneer with dissolve_fast
    mz "И что интересно, Евгения, я даже не уверена, что стоит что-то менять."
    mz "Как там у классика: „Полюбите нас чёрненькими!“. Так честнее будет, чем я начну фальшиво всем улыбаться."
    stop ambience fadeout 1
    show black with dissolve
    window hide
    
    
    $ set_mode_nvl()
    $ renpy.music.set_volume(0.5)
    play music "<from 6.5 loop 0.0>sound/music/blow_with_the_fires.ogg" fadein 2
    pause 0.5    

    
    scene dct_ext_stage_close_day
    show 3500_dv dontlike pioneer2 guitar playing:
        zoom .37 xcenter .6 ycenter .4
    show black
    
    window show
    hide black with dissolve
    "\nКонцертную площадку оккупировала Алиса."
    "Мрачная и задумчивая."
    "И музыка у неё выходила такая же — мрачная и задумчивая."
    # "Усилитель, выкрученный на половинную мощность, электрогитара… Можно сидеть, свесив ноги со сцены, упиваться своим плохим настроением, машинально перебирая струны, и пытаться размышлять под случайные аккорды."   # По канону
    "Усилитель, выкрученный на половинную мощность, электрогитара…{w} Можно, практически свесившись с края сцены, упиваться своим плохим настроением, машинально перебирая струны, и пытаться размышлять под случайные аккорды."
    show 3500_dv sadness pioneer2 guitar playing with dspr
    "Вчерашнее письмо от Алисы-двойника не шло из памяти: «Я хочу рискнуть и увидеться… Мы должны сравнить наши детские воспоминания»."
    show 3500_dv dontlike pioneer2 guitar playing with dspr
    th "Сравнить и дополнить!"
    show 3500_dv normal pioneer2 guitar playing with dspr
    th "Интересно, если собрать все детские воспоминания всех Алис, удастся ли восстановить всё моё детство?"
    th "А если собрать всех Алис вместе — может, мы просто сольёмся в одну Алису-настоящую?"
    extend " Как злой волшебник из кино про Аладдина?"
    show 3500_dv sadness pioneer2 guitar playing with dspr
    th "Нет, чушь. Сенька с Ульяной, конечно, лучше меня в этом разбираются, но я и без них понимаю, что это так не работает."
    $ renpy.music.set_volume(0.25, delay=1.5)
    window hide
    $ set_mode_adv()
    
    window auto
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
    pause .2
    show d_sv upset with dspr
    hide d_sv with easeoutleft
    "Увидала выражение лица девушки, что-то испуганно пискнула и исчезла."
    th "Вот и умничка."
    extend " Этот лагерь ещё часок обойдётся без меня."
    $ renpy.music.set_volume(0.75, delay=4)
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
        
    # "Край сцены начал резать ноги, девушка перебралась ближе к углу и уселась, вытянув их вдоль досок покрытия и опираясь спиной о вертикальное начало половинки купола."   # По канону
    
    "Край сцены начал резать стопы, девушка перебралась ближе к углу и уселась, вытянув их вдоль досок покрытия и опираясь спиной о вертикальное начало половинки купола."
    window hide
    $ set_mode_nvl()
    scene dct_ext_stage_edge_day
    show d18_alisa_guitar two:
        xpos -0.12 
    with dspr
    window auto
    "Оставалась проблема совместимости двух Алис в одном узле."
    th "Как там в книжке, что я у Жени брала?"
    th "Про экипаж космической станции, к которым приходили существа, взятые инопланетным разумом из их памяти."
    extend " Выглядящие как люди и считающие себя людьми, но не люди."
    extend " И исчезающие со вспышкой света при определённых условиях."
    th "Вот так исчезнешь, оставив после себя вспышку света — и всё, и привет, сестрёнка."
    "Плохо было то, что не с кем было посоветоваться.{w} Сенька с Ульяной, со слов бабули, говорили что-то о том, что пионеры-двойники — они называли их «субъектами» — не могут находиться одновременно в одном узле, о преимуществах «своего» узла по принципу «дома и стены помогают», об уровне развития личности субъекта, но всё это была голая теория."
    th "Это вот та Алиса, из старого Сенькиного лагеря, менее развита, чем я?"
    extend " Вон она какое письмо написала, я вот не догадалась."
    th "И вообще, я же вроде как собралась с концертами по лагерям проехаться."
    extend " Это что же — приезжая в каждый новый лагерь, я буду аннигилировать тамошнюю Алису?"
    extend " Не согласная я."
    "Да и поездка, похоже, откладывалась."
    th "А тут ещё за горнистом присмотреть надо."
    extend " Начал-то он хорошо; интересно, что в нём к следующему циклу изменится."
    "Мрачное настроение ещё держалось, но, кажется, опять появился интерес к жизни своего лагеря."
    nvl hide dissolve
    nvl clear
    pause 0.15
    show d18_alisa_guitar one with dissolve_fast
    nvl show dissolve
    th "В общем, так. В следующем цикле я точно здесь остаюсь, но схожу вместе с Ульяной в первый Сенькин лагерь."
    extend " Нужно с тамошней Алисой повидаться!"
    th "На остальных плевать, но с этой нужно."
    extend " Тем более Сенька нас связывает."
    th "И интересно, чего этой мелочи от меня надо было?"
    "И успокоившаяся Алиса заиграла уже не размышляя, просто ради самой музыки."
    stop music fadeout 1.5
    show black with dissolve
    window hide
    $ set_mode_adv()
    
    pause 0.5
    $ renpy.music.set_volume(1.0, delay=0)
    
    
    play sound_loop ambience_camp_center_day fadein 1
    scene bg ext_clubs_day with dissolve
    window auto
    el "Чуть левее датчик, ещё левее, ещё…{w} Стоп{w=0.3}, сейчас чуть-чуть правее.{w} Так, хорошо."
    el "Шурик, сейчас чуть выше.{w} Стой{w=0.3}, опусти назад, ещё опусти{w=0.3}, нет, верни как было.{w} Всё, зажимай, поймали."
    stop sound_loop fadeout 1
    play ambience ambience_int_cabin_day fadein 1
    play sound [ "<silence 1.0>", sfx_knock_door2 ]
    scene bg int_clubs_male_day
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    "Кибернетики стояли и благоговейно смотрели на зелёное колечко на экране осциллографа, когда в двери постучали."
    sa "Ребята, можно?"
    show el smile pioneer with dspr
    el "Заходи, Саша."
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
    el "Попытаемся переписать те объёмы информации, которая в них есть, и попытаемся её расшифровать. Всё, что есть в нашем подсознании; всё, что есть в нашей памяти."
    "Увлёкшийся Электроник заговорил, как герой его любимой фантастики шестидесятых годов."
    show el serious pioneer with dspr
    el "Может быть, мы сумеем понять принципы работы человеческого мозга; может быть, мы сумеем применить эти знания при проектировании кибермозга для будущих роботов!"
    el "Разве это не прекрасно?"
    show sl smile2 pioneer with dissolve_fast
    sa "Наверное, ты прав."
    "Саша улыбнулась наивному восторгу Сыроежкина, но ответила совершенно искренне."
    show el smile pioneer with dissolve_fast
    sa "Я верю, что всё у вас, мальчики, получится. Но я к вам за помощью, раз вы освободились."
    sa "Серёжа, в половине библиотеки свет только что погас — посмотри, пожалуйста."
    show el normal pioneer
    show sh normal pioneer
    with dissolve_fast
    "Кибернетики переглянулись. В библиотеке света нет, а там Женя!"
    show d_el shy2 pioneer as el
    show sh serious pioneer
    with dissolve_fast
    pause 0.5
    show d_el shy3 pioneer as el with dissolve_fast
    "Сердце застучало в два раза чаще. Сергей вскинулся, открыл рот и…"
    el "Шурик, а может, ты сходишь? А я пока тут всё поотключаю и порядок до обеда наведу."
    show sh normal_smile pioneer with dissolve_fast
    sh "Сергей, ну что за метания?"
    show sh laugh pioneer
    show d_el shy2 pioneer as el
    with dissolve_fast
    sh "Договорились же — по твоей просьбе, между прочим — что если есть какая-нибудь работа на дальней стороне лагеря, то ей занят ты, а на ближней — я."
    show d_el shy3 pioneer as el
    show sh smile pioneer
    show sl happy pioneer
    with dspr
    sh "Иди, Сергей. На обеде увидимся. А завтра уже займёмся экспериментом."
    hide sl with dissolve
    hide sh with dissolve
    "И, показывая, что разговор окончен, Шурик начал отключать приборы и собирать всё с верстака."
    show d_el shy2 pioneer as el with dspr:
        pause 2
        linear 1 alpha 0
    "Безотказному Сыроежкину осталось только собрать необходимый инструмент в старый, специально для таких случаев предназначенный школьный портфель и выйти на крыльцо клубов к дожидавшейся его Саше."
    
    
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_clubs_day
    show 3500_sl serious pioneer:
        zoom .17 anchor (.5, 1.0) pos (.46, .71)
    with slideawayup
    show 3500_el normal pioneer briefcase with dissolve:
        zoom .17 anchor (.5, 1.0) pos (.54, .71)
    el "Меня ждёшь?"
    show 3500_sl scared pioneer with dissolve_fast
    show 3500_sl surprise pioneer with dissolve_fast
    "Саша, стоящая лицом в сторону приоткрытых ворот лагеря и что-то там высматривающая, вздрогнула."
    sa "Да, Серёжа, пошли."
    show 3500_sl smile3 pioneer:
        zoom 1.0 anchor(0.5, 0.5) pos(0.42, 0.833)
    show 3500_el normal pioneer briefcase:
        zoom 1.0 anchor(0.5, 0.5) pos(0.65, 0.833)
    with dissolve
    show 3500_sl smile3 pioneer:
        easein 2.5 xcenter 1.6
    show 3500_el normal pioneer briefcase:
        easein 1.4 xcenter 1.25
    "Пионеры сбежали с крыльца клубов и свернули к площади: до первой развилки им было по пути."
    
    scene bg ext_houses_day
    show 3500_el normal pioneer briefcase:
        xcenter .35 ycenter.833
    show sl normal pioneer at cright
    with wipeleft
    "Но, к удивлению Сергея, Саша на перекрёстке не свернула налево — в сторону музыкального кружка и короткой дороги к своему домику. А наоборот, догнав его и подстроившись под его шаг, пошла рядом."
    show 3500_el surprise pioneer briefcase with dissolve_fast
    el "Ты на пляж? Я думал, ты к себе свернёшь."
    show sl serious pioneer with dspr
    sa "Сергей, я в библиотеку."
    "Саша коротко посмотрела на Сыроежкина, чуть повернув голову."
    sa "Что там у вас с Женей происходит — я не знаю, и это ваше дело. Но она сначала не хотела звать тебя, а после — категорически не хотела оставаться с тобой один на один. Как и ты пять минут назад."
    show sl serious pioneer
    show 3500_el sad pioneer briefcase
    with dspr
    el "Как и я."
    "Сергей согласно кивнул."
    scene bg ext_square_day
    show 3500_el shy2 pioneer briefcase:
        xcenter .35 ycenter.833
    show sl normal pioneer at cright
    with pushleft
    "На аллеях и площади было малолюдно. В связи с открытием купального сезона и жаркой погодой жизнь лагеря переместилась на пляж или в тень от деревьев, да футболисты занимались на стадионе по своему графику. Поэтому вспыхнувшие уши Сергея видела только Саша."
    show sl smile pioneer with dspr
    el "Хороший ты человек, Сашенька. Вот ответь — зачем мелькать перед глазами у человека, если он не хочет меня видеть?"
    show 3500_el shy3 pioneer briefcase with dspr
    "Сыроежкин вздохнул."
    show sl normal pioneer with dspr
    el "Оксана не знает, но ей только девять лет; может, ты мне скажешь?"
    show 3500_el normal pioneer briefcase with dspr
    el "Женя, наверное, думает, что я буду объясняться с ней. Потому и не хочет со мной наедине оказываться."
    show 3500_el scared pioneer briefcase with dissolve_fast
    el "А зачем мне объясняться, когда всё уже сказано? Только нервы мотать."

    scene dct_ext_square_profile_view_day
    show sl sad pioneer zorder 2
    show 3500_el sad pioneer briefcase zorder 3:
        xcenter .26 ycenter.833
    show sl sad pioneer as sl2 zorder 4:        # Дополнительно вырезаем юбку Слави, и помещаем перед чемоданом
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
    el "Сашенька. Я простой, как отвёртка, и привык иметь дело с техникой, которая либо работает, либо нет. И всегда можно найти причину, почему она не работает. И «нет» всегда означает только «нет»."
    show sl sad pioneer as sl2 zorder 4:
        corner1 (191, 700) corner2 (900, 1080) xcenter 0.55 yalign 1.0
    show sl sad pioneer zorder 2
    with dissolve_fast
    el "А вашего женского языка, где «да» означает «да», а «нет» означает «может быть», а «может быть» — это значит «нет», я просто не понимаю."
    el "Я получил информацию о том, что я Жене не нравлюсь — я информацию принял к сведению. И докучать симпатичному мне человеку, который не хочет меня знать, я не буду."
    "Саша тоже остановилась, развернувшись лицом к Сергею и глядя ему в глаза."
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
    "«Хотела одно, сказала другое», — собирался ответить Сергей, но Саша перехватила инициативу."
    sa "Серёжа, здесь на этом, как ты выразился, «женском» языке может говорить только Катя. Умеет ещё Лена, но она делать этого никогда не будет, и точно не умеет Женя."
    sa "А то, что она тебе сказала… Или ты убежал, не дослушав, или — вспомни, Женя почти ни с кем не общается — ей это просто трудно, общаться с людьми."
    show 3500_el surprise pioneer briefcase with dissolve_fast
    sa "И она может думать одно, а когда пытается озвучить мысль, то без практики получается совсем другое."
    sa "Даже её шутки, когда она просто хочет, чтобы человек улыбнулся, обычно воспринимаются как колкости."
    show 3500_el shocked pioneer briefcase with dspr
    sa "Или же она накрутила сама на себя. Потому что если у неё, с её характером, до лагеря были проблемы в отношениях с людьми, она могла посчитать себя никому не нужной."
    show 3500_el upset pioneer briefcase with dspr
    sa "Дайте друг другу ещё один шанс — вот что я хотела сказать."
    scene bg ext_library_day
    show 3500_el scared pioneer briefcase:
        zoom 0.75 xcenter .86
    show sl serious pioneer far:
        xcenter .7
    with pushright
    "Саша без стука отворила дверь библиотеки, втащила за руку Сыроежкина и сказала, обращаясь к Жене, испуганно вжавшейся в спинку стула:"
    stop ambience fadeout 1
    hide 3500_el
    hide sl
    with dissolve
    
    play ambience ambience_library_day fadein 1
    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    #with slidedown
    show 3500_el shy2 pioneer briefcase behind dct_int_library_standing_desk_front:
        zoom 0.9 xcenter .35 ycenter .755
    show sl serious pioneer behind dct_int_library_standing_desk_front:
        xcenter .6 ycenter .46
    with slidedown
    #with dissolve
    sa "Вот, я его привела.{w=0.5} Женя, это Сергей: очень хороший парень, но слишком наивный и доверчивый."
    show sl smile pioneer with dspr:
        pause .3
        linear .9 xcenter .3
        linear .3 xcenter .2 alpha 0
    show 3500_el surprise pioneer briefcase with dissolve_fast
    sa "А сейчас — убегаю. Прости, Женя, но меня Лена помочь ей попросила."
    stop ambience fadeout 1
    show black with dissolve
    
    pause 0.5
    

    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "В обед пионеров кормили щами и свиной поджаркой с рожками."
    "Персонал кухни действительно научился готовить: и щи не были пересоленными, и макароны не склеились, и мясо не подгорело, и чай не отдавал тряпкой.{w} Всё бы хорошо, но брызги томатного жира от поджарки оставляли оранжевые пятна на рубашках неаккуратных пионеров."
    show mt sad pioneer close at left with dissolve
    "Ольга Дмитриевна наблюдала за этим явлением и каждый раз морщилась."
    th "Эдак никаких рубашек не напасёшься."
    th "Пионеры же через час все ко мне прибегут и заканючат: „Ольмитревна, рубашка грязная, поменяйте, пожалуйста“."
    th "Стирать им лень, к Алисе бежать побоятся: знают, что можно физически пострадать."
    show mt normal pioneer close with dspr
    "Мысль вожатой переключилась на фигуру помощницы:"
    th "Может, всё-таки Сашу помощником назначить?"
    extend " Алиса только «за» будет."
    th "Нет, не вариант — Саша занята собой и каждым пионером, попавшим в её поле зрения, по отдельности."
    show mt sad pioneer close with dspr
    th "Никому нет дела до лагеря в целом — наверное, даже Семёну."
    show 3500_el shy pioneer briefcase:
        zoom 0.75 xcenter .71
    show mz shy glasses pioneer far:
        xcenter 0.6
    with dissolve
    "В столовую зашли ещё двое: Сыроежкин и Женя."
    show mt surprise pioneer close with dspr
    "Сыроежкин с портфелем в руках — это понятно: в библиотеке свет делал, но это не суть. Поведение у них необычное — вот что главное."
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
    
    play sound_loop ambience_camp_center_day fadein 1
    scene black
    show dct_int_coaching_room3:
        zoom 8.0 anchor (.72, .5) pos (.5, .5)
    show dct_int_coaching_room3_zoom_OSB:
        zoom 2 anchor (.44, .484) pos (.5, .5)
    show dct_mz_and_el_go_to_library_sketch:
        anchor (.5, .4) pos (.5, .5)
    show dct_mz_and_el_go_to_library:
        anchor (.5, .4) pos (.5, .5)
    with blinds
    "Лагерная аллея, по которой идут двое: те же Сыроежкин и Женя."
    show dct_mz_and_el_go_to_library_sketch:
        linear 1.5 zoom 0.8 anchor (.5, .46)
    show dct_mz_and_el_go_to_library:
        linear 1.5 zoom 0.8 anchor (.5, .46)
    "Идут от площади — за спинами у них Генда угадывается — в сторону библиотеки. Идут каждый по своей стороне и старательно не смотрят друг на друга."
    stop sound_loop fadeout 1
    play sound_loop2 ambience_int_cabin_day fadein 1
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
    "У Жени на лице растерянная полуулыбка, а Сергей, наоборот, сосредоточен: брови нахмурены, глаза прищурены, как будто целится куда-то, губы плотно сжаты; а в руке у него этот самый портфель, кстати."
    show dct_int_coaching_room3:
        linear 3 zoom 1 pos (.72, .5)
    show dct_int_coaching_room3_zoom_OSB:
        linear 3 zoom 0.25 pos (.72, .5) alpha 0
    show dct_mz_and_el_go_to_library_sketch:
        linear 3 zoom 0.1 pos (.72, .5)
    show dct_mz_and_el_go_to_library:
        linear 3 zoom 0.1 pos (.72, .5) alpha 0
    "И идут эти мальчик с девочкой вроде бы каждый сам по себе, но по тому, как они чуть склонились друг к другу, как они старательно при этом отводят друг от друга глаза, как они идут в ногу, видно, что уже связаны они, хотя ещё и сами об этом не подозревают."
    stop sound_loop2 fadeout 1

    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with blinds
    "Столовский шум волнами накатывался и отступал, иногда из него удавалось выделить отдельные голоса."
    

    $ d_voice_color = "#79cdf7"  # Голос Максима
    d_vocal_noise "Тётя Алиса, а если мне…"
    $ d_voice_color = "#e1dd7d"  # Голос Семёна
    d_vocal_noise "Вот и вопрос, Рыжик — как привести сюда чужую футбольную команду? Или наших туда…"
    $ d_voice_color = "#ffaa00"  # Голос Алисы
    d_vocal_noise "… собрание отряда, племянничек. Готовься."
    $ d_voice_color = "#00b4cf"  # Голос Мику
    d_vocal_noise "Леночка, а кто же это написал? Мы с Сашей думали, но так и не придумали ничего."
    $ d_voice_color = "#fff226"  # Голос Шурика. Наверное. Ну а кого ещё...
    d_vocal_noise "…Женю прозондировать, не всё так безнадежно, тяжело, но не…"
    $ d_voice_color = "#b7b7b7"  # Голос Витьки
    d_vocal_noise "Катя, мы что — на пляж не идем?"
    $ d_voice_color = "#4de2f3"  # Голос Оксаны
    d_vocal_noise "Вася, ты после обеда не уходи никуда, пожалуйста. Я хочу…"
    $ d_voice_color = "#ff3200"  # Голос Ульяны
    d_vocal_noise "Сёмк. Я, наверное, смогу попробовать. Но уговаривать обеих вожатых будешь ты."

    
    "Только библиотекарь и младший кибернетик молчали, уткнувшись, друг напротив друга, каждый в свою тарелку, и отчаянно краснели, когда их взгляды пересекались."
    stop ambience fadeout 1
    show black with dissolve
    
    pause 0.5
    

    play ambience ambience_int_cabin_day fadein 1
    scene bg int_clubs_male_day
    show sh serious pioneer close
    "После обеда Шурик вернулся в кружок."
    scene dct_int_clubs_male2_night_zoom
    show sh smile pioneer at fright
    with dissolve
    "Он долго стоял перед установкой, гладил кончиками пальцев каркас и вращающийся табурет, установленный внутри каркаса, проводил ладонями над электронными платами."
    "Для ускорения работ корпус решили не делать, и сейчас эти платы рядком лежали на рабочем столе на плоском листе шифера, соединённые между собой экранированными проводами. Видеомагнитофон, заряженный чистой кассетой, стоял тут же."
    "Очень хотелось попробовать — останавливало только обещание, данное Сыроежкину, что без него ни-ни."
    show sh smile pioneer:
        ease 1.2 xcenter 1.25
    "Шурик забрался внутрь каркаса, уселся на табурет, проверил, как он вращается."
    "Всё было в полном порядке — включай установку и начинай запись."
    show sh normal pioneer close:
        ease 1.2 xcenter 0.8
    "Нужно было придумать, как включить и выключить установку без посторонней помощи."
    show sh normal_smile pioneer close with dissolve_fast
    th "В конце-концов, Сергей не хотел, чтобы я включал без него, только как ответственный за технику безопасности, но что тут может случиться?"
    th "Изобретение почти целиком моё, а программа-дешифратор моя полностью."
    show sh normal pioneer close with dissolve_fast
    th "Я не спорю, Сергей здорово помог с излучателями и каркасом, но я бы и без него справился."
    show sh serious pioneer close with dspr
    "Шурик уговаривал сам себя как мог."
    th "Если я сейчас сделаю запись, то на завтра останется меньше работы."
    show sh serious pioneer close:
        ease 1 xcenter 0.5
    "Шурик раскрыл рабочую тетрадь:"
    "«Шестой день смены, 15-00, пробный запуск установки. Подопытный — Александр Трофимов, оператор — Александр Трофимов. Расчетное время эксперимента — десять минут. Описание эксперимента…»"
    show sh normal pioneer close with dspr
    "Осталось только принять меры предосторожности, чтобы никто не помешал."
    hide sh with dissolve
    play sound [ "<silence 0.5>", sfx_close_door_clubs_nextroom ]
    play sound2 [ "<silence 1.9>", sfx_open_window ]
    "Шурик вышел на крыльцо и запер двери на висячий замок, после чего обошёл здание и влез внутрь через окно."
    show sh normal_smile pioneer close with dissolve:
        xcenter .6
        easeout 1.5 xcenter 1.25
    "Включил установку на разогрев, а сам прямо на включённой установке стал наращивать провод, ведущий к кнопке «Пуск»."
    stop ambience fadeout 1
    show black with dissolve

    play ambience ambience_int_cabin_day fadein 1
    scene dct_int_clubs_male2_night_zoom with dissolve
    "Вскоре всё было готово."
    scene dct_sh_in_cage_with_pushbutton with squares
    "Шурик сидел внутри каркаса, как в клетке; табурет под ним, приводимый во вращение мотором, вытащенным из механизма дворников «Волги», медленно, почти незаметно для глаза, вращался с частотой один оборот за десять минут."
    "Сменялись цифры на дисплее магнитофона, предназначенного для записи считываемой информации."
    th "Жаль, что пока нельзя записывать информацию прямо в память компьютера и расшифровывать в реальном времени. Жаль, что у нашего компьютера память, как у Буратино."
    "За это время табурет повернулся так, что временная кнопка «Пуск», примотанная изолентой к каркасу, оказалась напротив левого колена кибернетика."
    "Шурик мысленно перекрестился и, нажав на кнопку, начал эксперимент."
    "Теперь — главное: надо было высидеть на табурете десять минут, не меняя положения головы и стараясь ни о чём не думать."
    $ renpy.music.set_volume(0.08)
    play music "<from 32.0 loop 0.0>mods/dublicate/Sounds/music/dreamers_of_the_day.ogg" fadein 1.5
    "Как обычно это бывает по закону подлости, всем что-то понадобилось в клубах именно в это время."
    play sound sfx_knock_door_closed_hard1
    "Кто-то трогал висячий замок и дёргал входную дверь; кто-то пытался заглянуть в окна — благо, Шурик предусмотрительно задвинул шпингалеты и задёрнул занавески."
    "Из-за двери послышался голос Сыроежкина:"
    el "Шурик, ты здесь?"
    play sound "<to 1.05>sound/sfx/knock_door_closed_hard2.ogg"
    stop music fadeout 1.5
    "Замок подёргали ещё пару раз, и две пары ног потопали с крыльца."
    stop music
    $ renpy.music.set_volume(1.0)
    "Десять минут истекли, табурет сделал полный оборот, кнопка «Пуск» опять оказалась напротив колена."
    scene dct_int_clubs_male2_night_zoom with squares
    show sh normal pioneer at right:
        xcenter 1.2
        pause 1.7
        ease 1 xcenter 0.72
    "Шурик отключил установку, перемотал кассету на самое начало, подключил магнитофон к компьютеру и запустил программу дешифровки."
    hide sh with dissolve
    play sound2 [ "<silence 1.5>", sfx_open_window ]
    "После этого восстановил в кружке всё как было, вылез в окно и отправился на пляж."
    "Хоть раз за смену, но нужно было выбраться на свежий воздух."
    stop ambience fadeout 3
    show black:
        alpha 0
        pause 1.3
        linear 1 alpha 1
    "До расшифровки результатов делать Шурику было совершенно нечего, а работать компьютеру предстояло ещё несколько часов."
    show black as black2 with dspr
    
    pause 0.5
    
    
    play ambience ambience_lake_shore_day fadein 1
    play sound_loop dct_ambience_beach fadein 1
    scene dct_ext_beach_day_with_pass_train
    show d_sf normal swim:
        xcenter 0.35 ypos 0.2
    show d_us normal swim:
        xcenter 0.65 ypos 0.09
    with dissolve
    "Ульяна и Семён валялись на пляже."
    show d_sf serious swim
    show d_us serious swim
    with dspr
    "Не просто так валялись, а по делу. Нужно было пасти средний и младший отряды."
    show dct_ext_beach_day_lifesaving_shield
    show 3500_sh normal_smile swim:
        xcenter 0.25
    with dissolve
    "Исторически и в теории сложилось так, что пионеры из старшего отряда приходили на пляж и уходили когда хотели — вот как Шурик сейчас, сидевший на лавочке под щитом со спасательными кругами."
    hide dct_ext_beach_day_lifesaving_shield
    hide 3500_sh
    with dissolve
    "Средний отряд приходил по расписанию, и за ними присматривал кто-то из персонала или помощник вожатой; младшему же отряду требовались ещё и команды, выгоняющие октябрят из воды и разрешающие им снова лезть в воду."
    show d_sf smile swim
    show d_us normal swim
    with dspr
    "На деле же мелкие были довольно самостоятельными людьми и обходились без эксцессов на воде; единственное, что приходилось их выгонять оттуда, когда они уж совсем посинеют, и общаться с ними, но это Семёну было только в удовольствие."
    me "Знаешь, Рыжик, я как-то обнаружил, что они в свои семь лет ничем не хуже нас."
    show d_sf normal swim with dspr
    me "И проблем у них не меньше, и проблемы не менее важные. Это нам они кажутся смешными, а для них-то проблемы самые настоящие."
    me "Есть такая работа — называется „взросление“, и неважно, в какой ты фазе; когда тебе всё равно семь, восемь, девять лет — ты всё равно взрослеешь. Если я могу помочь хорошим людям — почему нет?"
    show d_us sad swim with dspr
    "Со средним же отрядом Ульяна намучилась."
    scene dct_ext_beach_barhan
    show d_us serious swim:
        xzoom -1.0 xcenter 0.16 ypos -0.05
    with dissolve
    us "Оля, тебе пять лет?{w=0.4} Ты можешь бросать песком сколько угодно, но потом сама всех поведёшь к доктору глаза промывать.{w} Да-да, именно ты поведёшь."
    scene dct_ext_beach_day_lifesaving_shield
    show d_us serious swim:
        xcenter 0.84 ypos -0.05
    with dissolve
    us "Егорка, если тебе нравится девочка, то просто скажи ей об этом, а не щёлкай по спине тесьмой от купальника."
    scene dct_ext_beach_day_with_pass_train
    show d_us serious swim:
        xzoom -1.0 xcenter 0.5 ypos -0.05
    with dissolve
    us "Тпр-р-ру, мальчики, быстро из воды и разбежались в разные стороны. Остыньте, а то вы уже злиться начинаете."
    show d_us hurt swim with dissolve_fast:
        xzoom 1.0 xcenter 0.5 ypos -0.05
    "И так постоянно."
    show d_us normal swim with dspr
    "Только собственная энергия и позволяла углядеть за всеми и не устать."
    scene dct_ext_beach_barhan
    show d_ka serious pioneer with dissolve:
        zoom 0.825 xcenter 0.2 ycenter 0.76
    with dissolve
    "А тут ещё Катерина обращает на себя внимание."
    show d_ka serious pioneer2swim with dissolve_fast:
        pause 0.5
        ease 2 xcenter 0.65
        linear 0.5 ycenter 0.9
    show d_ka upset pioneer2swim as d_ka2:
        zoom 0.825 xcenter 0.65 ycenter 0.9 alpha 0
        pause 3
        linear 0.2 alpha 1
    "Пришла на пляж, потому что уклониться нельзя, купание — мероприятие отрядное, но раздеваться не стала — только стянула юбку, развязала галстук и села под грибком прямо на песок, обхватив колени руками. И смотрит куда-то в бесконечность."
    show d_ka angry pioneer2swim as d_ka2 with dspr
    "Витька потащил её в воду, получил резкую отповедь, ничего не понял, ещё покрутился вокруг и полез купаться со всем отрядом, а Катя осталась сидеть одна под грибком."
    scene dct_ext_beach_day_with_pass_train
    show d_sf normal swim:
        xcenter 0.35 ypos 0.2
    show d_us normal swim:
        xcenter 0.65 ypos 0.09
    with dissolve
    us "Сём, Катя переживает. Только не пялься на неё, а то убежит."
    me "Конечно, переживает. В прошлом цикле все вокруг неё бегали, а тут Макс взял и перерос её."
    me "А Катька в прошлом цикле развлекалась, а сейчас взяла и влюбилась. Тринадцать лет — самое время для первого раза, себя нынешнюю вспомни."
    show d_us shy swim with dspr
    me "Жалко её, но одна мудрая женщина сказала, что такие вещи и превращают организмы в людей."
    show d_sf laugh swim
    show d_us serious swim
    with dspr
    us "Эй, мне почти четырнадцать было!"
    show d_sf smile swim
    show d_us smile swim
    with dspr
    us "И знаешь, Сём, мне сейчас кажется, что мне внутри всегда было девятнадцать, пока я тебя ждала. А когда встретила тебя — всё на свои места встало."
    show dct_ext_beach_day_lifesaving_shield
    show 3500_sh smile noglasses swim:
        zoom 0.75 xcenter 0.8
    with dissolve
    pause 0.3
    show dv normal pioneer at center
    show un normal pioneer at left
    with dissolve
    "На пляже появились Алиса с Леной."
    window hide
    show dv smile pioneer
    show un smile pioneer
    with dspr
    
    pause 0.5
    
    show dv normal pioneer:
        pause 0.2
        ease 2.5 xcenter 1.4
    show un normal pioneer:
        pause 0.2
        ease 2.5 xcenter 1.18
    with dspr
    
    pause 1
    
    scene dct_ext_beach_day_with_pass_train
    show dv grin pioneer far:
        xcenter 0.61
    show un smile2 pioneer far:
        xcenter 0.41
    show d_sf normal swim:
        xcenter 0.25 ypos 0.2
    show d_us normal swim:
        xcenter 0.75 ypos 0.09
    with dissolve
    
    pause 0.5
    
    show dv grin swim far:
        pause 1.2
        linear 1 alpha 0
    show un smile2 swim far:
        pause 1.3
        linear 1 alpha 0
    with dissolve_fast
    window auto
    "Кивнули Шурику, скинули форму, устроившись рядом с физруками, и побежали к воде."
    scene dct_ext_beach_barhan
    show d_ka angry2 pioneer2swim:
        zoom 0.825 xcenter 0.65 ycenter 0.9
    with dissolve
    "Катя неприязненно покосилась на Алису, но позы не переменила."
    scene dct_ext_beach_day_with_pass_train
    show d_sf normal swim:
        xcenter 0.35 ypos 0.2
    show d_us normal swim:
        xcenter 0.65 ypos -0.05
    with dissolve
    us "Сёмк, последишь за средним отрядом?{w=0.5} А я пока за мячиком сбегаю. Давно не играли."
    show d_sf normal swim:
        linear 0.5 ypos 0.0
    show d_us normal swim:
        pause 0.5
        linear 1 alpha 0
    "И Ульяна, как была в купальнике и босиком, только накинув на плечи футболку, побежала в спортзал, благо он располагался от пляжа через дорогу."
    stop sound_loop fadeout 1
    stop ambience fadeout 1
    show black with dissolve
    
    pause 0.5
    

    play ambience ambience_camp_center_day fadein 1
    scene dct_sky_over_flowerbed_behind_library with dissolve:
        align (1.0, 0.0)
    mz "И что нам теперь полагается делать?"
    "Женя выглядела совершенно растерянной — точь-в-точь как на Ленином рисунке."
    el "Я не знаю, Женя, я думал, ты знаешь."
    window show
    scene dct_sky_over_flowerbed_behind_library:
        size (2400, 1565) align (1.0, 0.0)
        ease 2.5 size (1920, 1252) align (1.0, 0.5)
    "Та аллея, на которой стояла библиотека — она расширялась в самом конце; посередине расширения располагалась клумба, увенчанная очередным гипсовым пионером, и в этом лагере, где не было своей Слави, совершенно заброшенная, а по периметру были расставлены скамейки."
    window auto
    stop ambience fadeout 1
    play music dreamers_of_the_day fadein 1
    scene dct_mz_and_el_sitting_on_bench_near_flowerbed with squares
    "Вот на одной из этих скамеек сейчас и сидели Женя и Сыроежкин и большую часть времени молчали."
    "Обоим было ужасно неловко, оба не знали, куда девать руки, оба краснели, едва пересекаясь взглядом, но разбежаться, как будто ничего не было, казалось ещё хуже."
    mz "Ничего я не знаю, Серг… Серёжа. Всё, что я знаю — я прочитала в книгах. Но я же не идиотка восторженная, я же понимаю, что книги и реальная жизнь — это разные вещи."
    mz "Может, давай для начала просто будем больше вместе проводить время."
    el "Да-да, Женя. Хочешь, я покажу тебе наш кружок, нашу работу?"
    mz "Это то, ради чего ты позавчера бегал в библиотеку каждые полчаса? Пойдём."
    mz "Всё равно в библиотеку никто не ходит, кроме Лены, а она сегодня уже была. Да и портфель этот тебе надо на место вернуть."
    scene bg ext_houses_day
    show 3500_el laugh pioneer briefcase:
        xcenter .35 ycenter.833
    show d_mz smile3 glasses pioneer at cright
    with squares
    "Это было новое для «Совёнка» событие: по аллее — сперва по боковой, потом, пройдя по площади, по главной — шли Женя и Сыроежкин и о чём-то разговаривали."
    "Они ещё не держались за руки, но уже и не отворачивались друг от друга, и — о чудо! — Женя даже улыбалась."
    
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Жаль, что это некому было видеть: старшие были заняты своими делами, а средние и младшие уже к тому времени были на пляже."
    stop music fadeout 1.5
    show black with dissolve
    window hide

    pause 1.0
    $ sunset_time()
    $ persistent.sprite_time = "night"
    window auto
    

    play ambience ambience_camp_center_evening fadein 1
    scene black
    d_voice_me "Оль."
    th "Кто-то устроился в соседнем шезлонге."
    th "И этого кого-то зовут Семён."
    th "Сейчас опять начнёт уговаривать. А закончится всё полетевшим к чертям планом мероприятий и срывом…"
    extend " Срывом чего, кстати?"
    show d_sf smile swim:
        xzoom -0.75 yzoom 0.75 xcenter 1.15 ypos 0.55
        linear 0.2 xcenter 0.93
        pause 0.6
        linear 0.2 xcenter 1.15
    me "О-оль."
    "Нет, он очень хороший помощник.{w} Действительно помощник, и я не представляю, как в других лагерях вожатые в одиночку со всем справляются."
    "Но он же готовый начальник ещё одного лагеря, но почему-то остаётся здесь."
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
    me "Оль, я знаю, что ты не спишь — у тебя дрожат веки."
    mt "Семён, скажи: что ты будешь делать, если я тебе сейчас не отвечу?"
    me "Тогда…"
    th "Я ясно слышу усмешку в его голосе."
    show d_sf laugh swim:
        xzoom -3.5 yzoom 3.5 xcenter 0.53 yalign -0.09 rotate 0.0 alpha 1
        ease_quad 3.5 yalign 0.14
    me "Тогда я буду действовать так, будто получил твоё согласие."
    show d_sf laugh swim:
        linear 0.5 alpha 0
        
    $ persistent.sprite_time = "night"      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Вот и кто начальник лагеря, спрашивается?"
    window show
    
    $ persistent.sprite_time = "sunset"
    scene bg ext_house_of_mt_sunset
    show d_sf normal pioneer at left:
        ypos 0.2
    show unblink
    window auto
    "Приходится открывать глаза."
    show d_sf smile pioneer with dspr
    th "Время-то к отбою, оказывается. Скоро темнеть начнёт."
    "Оглядываюсь: всё тихо и спокойно. Никто не убился, никто не подрался, никто, кажется, не убежал."
    "Вон идёт один из Семёновых футболистов с подружкой. Несёт в руках кораблик, вырезанный из коры."
    th "Просто галеон испанский какой-то, даже поразглядывать хочется. Надо будет потом попросить."
    show d_sf normal pioneer with dspr
    "А вон Лена с этюдником: сидит на лавочке напротив своего домика, а на крыльце ей Сашенька позирует."
    th "Да, в таком образе дореволюционной барышни — это именно Сашенька."
    th "Вот интересно, где они взяли это платье, эту шляпку и этот зонтик? Разве что на складе у Алисы, в мешках с театральным реквизитом?"
    th "Или в музыкальном кружке, в костюмерной. Но там, кажется, такого нет."
    show d_sf serious pioneer with dspr
    th "Как бы ещё Семёна позлить, время потянув?"
    th "Вот!"
    show int_house_of_mt_sunset:
        ycenter -0.5
        pause 1.2
        linear 1 ycenter 0.5
    extend " Потягиваюсь, потом аккуратно закрываю книжку, встаю с шезлонга, отношу книжку в домик."
    mt "Семён Семёнович, не изволите ли чаю?"
    "Пионеров в пределах слышимости нет, так что можно и подурачиться, но насчёт чаю я вполне серьёзна."
    me "Премного обяжете, Ольга Дмитриевна."
    "Одна из проблем состоит в том, что мы знакомы уже чёрт знает сколько, и уже угадываем реплики друг друга до того, как кто-то из нас откроет рот."
    th "А кстати, сколько мы знакомы?"
    th "В прошлую смену — да, в позапрошлую — да. Дальше?"
    extend " А дальше — при попытке вспомнить у меня начинает болеть голова."
    "Беру из тумбочки три кружки."
    "Три — это потому что через пять минут здесь будет Ульяна. Это я тоже могу предсказать с вероятностью сто процентов."
    "Высыпаю на блюдце из целлофанового пакета конфеты-батончики."
    mt "Семён, иди помогай!"
    
    # — Зову своего заместителя, обернувшись к дверям.    # По канону.
    
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
    "Слышу шлёпанье босых ног по дорожке: этот ритм полубега-полушага ни с чьим не спутаешь — Ульяна."
    show d_us smile dress:
        xcenter 0.55
        linear 0.5 ypos 0.09
    show d_sf smile pioneer with dspr
    "Усаживается на крыльцо.{w} Теперь, когда вся администрация лагеря в сборе, можно начинать совещание."
    "Семён смотрит, как устраивается Ульяна, и я вижу нежность в его глазах. Поэтому не начинаю, пока он не примет деловой вид."
    show d_sf serious pioneer
    show d_us normal dress
    with dspr
    "Поразительно, но сколько эмоций можно выразить движениями одних только уголков глаз."
    
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