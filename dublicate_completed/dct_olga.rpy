label dct_olga:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга."
    $ day_time()
    play music music_list["farewell_to_the_past_edit"]
    show headline_text u"О — значит Ольга" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    stop music fadeout 1

#########
#Часть 1#
#########

label dct_olga_p1:
    scene black with blinds
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 1."
    $ day_time()
    show headline_text2 u"Часть I" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_ext_gate_entrance_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play sound dct_sfx_bus_departure
    play ambience ambience_camp_entrance_day
    play music music_list["i_want_to_play"]
    th "Приехали. И куда мне теперь?"
    th "Надо было дорогу спросить ещё в автобусе. А сейчас все разбежались. Придётся разбираться самой."
    th "Вот позорище будет, если потеряюсь. И море шуток про топографический кретинизм у девушек."
    th "Учительница географии, которая потерялась. Ну хорошо — будущая учительница."
    stop music fadeout 1
    stop sound
    stop ambience
    
    scene ext_clubs_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    voice "Не стойте на дороге!"
    show adl_sh glasses dontlike at right with moveinright
    d_mt2 "Да-да, извините. А вы не подскажете? Мне в отдел кадров надо."
    th "Как на Шурика из кино похож!"
    show adl_sh dontlike with dspr
    adl_sh2 "В отдел ка-а-адров."
    show adl_sh normal with dspr
    adl_sh2 "Это в модуле, на первом этаже."
    d_mt2 "В модуле?"
    adl_sh2 "Пройдёте по главной аллее. Справа будет металлическое здание. Вот, вам туда. Первый этаж, налево, а там табличка на дверях."
    d_mt2 "Спасибо вам!"
    hide adl_sh with moveoutleft
    th "Убежал изобретать машину времени."
    th "Значит, мне прямо и направо. Может, стоило поулыбаться дядечке?"
    adl_sh2 "Детский сад."
    th "Обойдётся."
    stop ambience
    
    scene dct_ext_module_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["my_daily_life"]
    th "Прямо и направо. Металлическое здание. Кажется, это здесь."
    stop ambience
    
    scene dct_int_chief_corridor_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    th "Здесь хотя бы прохладно. Кажется, мне сюда."
    play sound dct_sfx_knock_door1
    th "Стучат, откройте дверь!"
    play sound dct_sfx_knock_door2
    th "Да что это такое?! Сначала завкафедрой с деканом, в два рта, лично уговаривают меня согласиться поехать именно сюда на эту практику."
    play sound dct_sfx_knock_door3
    th "Приезжаешь в какую-то дыру — и до тебя нет никому дела! Сейчас пойду стучать во все двери подряд!"
    voice "Девушка, вы так дверь сломаете."
    stop music
    show d_to normal casual with moveinleft:
        ypos 0.05
    d_t2 "Если вы ко мне, то заходите."
    th "Да не хочу я уже никуда заходить! Сейчас сяду в автобус и уеду."
    show d_to smile casual with dspr
    d_t2 "Имейте в виду, автобус только завтра. А ночевать вам где-то надо."
    d_t2 "Правда, если хотите, то можете заночевать на скамье, на площади. Я попрошу, чтобы патруль вас не трогал."
    d_t2 "Но лучше ночевать под одеялом в кровати, как вы полагаете? Так что заходите."
    stop ambience
    
    scene dct_int_cabinet_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_to smile casual with dissolve:
        ypos 0.15
    d_t2 "Присаживайтесь, и давайте ваши бумаги."
    show d_to normal casual with dspr
    play sound dct_sfx_pages
    d_t2 "Миронова Ольга Дмитриевна, 1967 года рождения, русская, из семьи служащих, член ВЛКСМ, не судимая, на оккупированной территории не проживала…"
    d_t2 "… направляется для прохождения педагогической практики в период с 08.06.1987 г. по 19.07.1987 г. в качестве пионервожатой." 
    d_t2 "И при чём тут мы?"
    stop ambience
    
    scene dct_int_cabinet_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_to normal casual:
        ypos 0.15
    dreamgirl "Листал бумаги незнакомец долго. А в конце выдал…"
    d_t2 "Боюсь, что вы зря сюда приехали, Ольга{w=1}… Дмитриевна."
    d_t2 "Меня зовут Анатолий Васильевич, кадровыми вопросами занимаюсь здесь я, и официально вам заявляю: здесь нет потребности ни в вожатых, ни в иных педагогах."
    play sound sfx_wind_gust
    $ renpy.pause (2)
    play music music_list["door_to_nightmare"]
    #dreamgirl "А Ольга, которая десять минут назад была готова хлопнуть дверью и уехать, вдруг испугалась."
    th "Как же так? А где я сейчас отметку о прохождении практики получу?"
    d_mt2 "Но меня же направили к вам, сюда. В пионерский лагерь, вожатой. Я же не сама сюда приехала."
    show d_to smile casual with dspr
    d_t3 "Конечно, не сами, иначе меня бы уволили."
    show d_to normal casual with dspr
    d_t3 "Вот что, Ольга Дмитриевна, давайте сделаем так. Сейчас идите к коменданту — это на складе, рядом со столовой."
    d_t3 "Скажете, что от меня, получите у него ключи от комнаты и талоны в столовую, и до завтра вы свободны, только за территорию не выходите."
    d_t3 "Можете на пляж сходить, в библиотеку, в бильярдную, можете лодку взять и на ближний остров сплавать. А завтра утром, после завтрака, приходите."
    d_t3 "Ну а мы пока решим, что с вами делать."
    stop music fadeout 1
    stop ambience

    scene dct_int_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound sfx_open_dooor_campus_1
    d_mt2 "Здравствуйте, Ольга{w=1}… Дмитриевна. Заходите, Ольга{w=1}… Дмитриевна. Располагайтесь, Ольга{w=1}… Дмитриевна."
    th "Может, это и к лучшему, что здесь им не нужна пионервожатая?"
    th "А то встретили плохо, разместили плохо — вон сколько пыли на подоконнике, и цветок высох. Если и покормят так же плохо, то точно к лучшему."
    th "Не хочу в комнате порядок наводить, раз встречают так неприветливо.{w} Но коменданта за погибший цветок я отругаю!"
    th "До ужина ещё часа четыре. Что там мне посоветовали? Погулять? Вот пойду и погуляю."
    stop ambience
    
    scene ext_boathouse_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_boat_station_day
    dreamgirl "Несмотря на плохое первое впечатление, посёлок Ольге скорее понравился. Пляж, стадион, лодочная станция, лес. Расслабленная атмосфера, шорты, футболки, короткие юбки и лёгкие платья, яркие цвета в одежде. И только изредка попадающиеся военные хранили верность своей форме."
    th "А тут не так и плохо. Как будто в санаторий попала. Вот только для чего я столько анкет заполняла?"
    play sound sfx_dinner_horn_processed
    $ renpy.pause (2)
    th "Это… сигнал к ужину? «Бери ложку, бери хлеб…» Кстати, про пионерский лагерь. А может, это у здешнего радиста юмор такой?"
    th "Сейчас узнаю."
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["i_want_to_play"]
    th "Завтра меня отсюда вышибут, и я побегу в деканат ругаться."
    th "Вот только с кем ругаться, каникулы же? Ну, найду с кем."
    stop ambience
    
    scene int_dining_hall_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    th "Никому я тут не нужна, даже знакомиться никто не лезет. Тогда где здесь обменивают бумажные талоны на настоящий ужин?"
    stop ambience
    
    scene d1_food_normal with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    th "А выглядит неплохо. Если и на вкус так же, то я один балл этому месту добавлю."
    th "Но я что — должна всё это съесть?"
    th "И сдобная булка? Прощай, фигура."
    th "Но вкусно. Ладно, раз обеда сегодня не было, то можно."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_residential_block2_sunset with squares
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_night
    play music music_list["trapped_in_dreams"]
    th "День прошёл. Будем считать это однодневной путёвкой в профилакторий."
    th "На пляже я была, по лесу погуляла. Осталось для того, чтобы поставить галочку, потанцевать, пофлиртовать, и что там ещё делают в домах отдыха?"
    th "А утром явлюсь пред светлы очи, получу от ворот поворот и отчалю на автобусе."
    th "Здесь и правда не нужен пионерский лагерь. За весь день ни одного пионера не попалось. Только дети сотрудников."
    th "Или была одна пионерка?"
    stop ambience
    
    # scene ext_square_day with pixellate
    # show dct_dream_veil:
        # shiver
    # $ prolog_time ()
    # $ persistent.sprite_time = "day"
    # play ambience ambience_camp_center_day
    # show mi normal pioneer far behind dct_dream_veil with moveinright
    # d_mt2 "…"
    # show mi shocked pioneer far with dspr
    # hide mi with easeoutleft
    # $ renpy.pause (1)
    # stop ambience
    
    scene ext_houses_day:
        zoom 1.25 align (0.5, 1.0)
    show dct_ext_houses_day_mi_goes_away
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    d_mt2 "…"
    $ renpy.pause (0.3)
    stop ambience
    
    scene dct_int_residential_block_night with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    th "Нет. Показалось. Не бывает у людей волос такого цвета и такой длины."
    show blink
    stop music fadeout 1
    $ renpy.pause (1)
    stop ambience

#########
#Часть 2#
#########

label dct_olga_p2:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 2."
    $ day_time()
    show headline_text2 u"Часть II" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_briefing_room with dissolve
    $ prolog_time ()
    $ persistent.sprite_time ="day"
    play ambience ambience_int_cabin_day
    show d_bg normal suit at cright with dspr
    d_gd "И что вы об этом думаете, Анатолий?"
    show d_bg normal suit at right with move
    play sound [ "<silence 0.7>", dct_sfx_chair ] 
    show d_to normal casual at cleft with MoveTransition(1.5, enter=_moveleft, enter_time_warp=_ease_time_warp)
    pause 0.6
    show d_to normal casual at cleft with move:
        ypos 0.18
    d_to "Девочку немного жалко, но она молодая, она ничего не потеряет. В худшем случае поругается с деканатом. И будет проходить практику где-нибудь в городском лагере."
    d_gd "Нет, я о том, как она здесь вообще оказалась."
    d_to "Глафира Денисовна, а кто в Плане на прошлый год утвердил: «Организовать в узлах детские лагеря»? — и далее по тексту. Вот и получите-распишитесь."
    d_gd "Не показывай пальцем, я и так знаю. Это скажи спасибо, что только одну прислали. А мы теперь страдай и думай: что с ней делать?"
    d_gd "Особенно всем нам будет неприятно, если всплывёт правда о том, что Система вышла из-под контроля. И так применение Выключателя по активным НБО с трудом обосновали."
    d_to "Может, рискнём и отправим её, скажем, в первый узел? Всё равно лагеря создавать надо."
    d_to "Цикла на три, а потом, когда она и Система адаптируются друг к другу, сделаем миксов и закроем вакансии во всех узлах."
    d_to "А её отчет автоматически окажется секретным; те, кто имеет допуск, ничего не поймут, а кто поймёт — те допуска не имеют."
    d_to "А что касается Выключателя: ты уверена, что была права?"
    show d_bg sad suit with dspr
    d_bg "Анатолий, я не знаю… Но другого выхода я не вижу... {w=1} И не видела."
    d_bg "Потому что иначе тут всё и всех выжгут, во всех узлах, включая эфемерные."
    show d_bg normal suit with dspr
    d_bg "В общем, приглашай девочку в директорский кабинет на десять ноль-ноль, остальных я сама обзвоню. Там и посмотрим, и решим, как с ней быть."
    stop ambience

    scene black with squares
    show dct_int_residential_block_day
    show unblink
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["timid_girl"]
    d_mt2 "Доброе утро."
    show blink
    play sound sfx_bed_squeak1
    dreamgirl"Ольгу разбудил солнечный зайчик, неяркий, но настойчивый. Он щекотал лицо, пробиваясь между неплотно задёрнутыми занавесками, и совершенно не давал доспать."
    th "Умыться, позавтракать, получить от здешнего начальства отказ, поваляться на пляже, если останется время до автобуса, и уехать домой. Ничего не перепутала?. Тогда встаём." 
    hide unblink
    hide blink
    show unblink
    d_mt2 "…"
    stop ambience
    
    scene int_dining_hall_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    d_mt2 "…"
    show d_to normal casual at center with moveinleft
    d_t3 "Доброе утро и приятного аппетита, Ольга Дмитриевна."
    d_mt2 "Спасибо. И вам доброго утра."
    d_t3 "Ольга Дмитриевна, подходите, пожалуйста, через час в кабинет руководителя филиала. Будем вас ждать{w=1}. Это в модуле, на втором этаже, напротив лестницы…"
    d_mt2 "Чемодан брать?"
    d_t3 "Оставьте пока. Сдать ключи коменданту вы всегда успеете."
    hide d_to with moveoutleft
    th "Неужели меня оставляют?! А хорошо бы..."
    th "Это как обещание продолжения истории."
    stop music fadeout 1
    stop ambience

    scene dct_int_chief_corridor_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound dct_sfx_knock_door1
    th "Разрешите мне остаться. Ну пожалуйста."
    stop ambience
    
    scene dct_int_briefing_room with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_conf
    play sound sfx_close_cabinet
    show d_to normal casual at center with dspr
    d_t3 "Заходите, Ольга Дмитриевна."
    show d_to normal casual at fleft with move
    d_t3 "Позвольте представить: Миронова Ольга Дмитриевна, направлена к нам для прохождения практики в качестве пионервожатой. Глафира Денисовна…"
    voice "Хм-м."
    show adl_sh glasses normal at cright with moveinright
    adl_sh2 "Ольга Дмитриевна, что вы думаете о человекоподобных роботах?"
    th "Нет, это не Шурик из кинокомедии."
    d_mt2 "Никогда не интересовалась роботами."
    th "Надо было сдерзить: «фантастикой не увлекаюсь», но что-то страшновато. С таким Шуриком, пожалуй, даже царь Иван Васильевич поостерёгся бы фамильярничать."
    show adl_sh glasses dontlike with dspr
    adl_sh2 "Очень плохо."
    hide adl_sh with moveoutright
    show d_bg normal suit at cright with moveinright
    show d_to smile casual with dspr
    d_gd "Александр Сергеевич своё мнение высказал. Может быть, начнём работать?"
    $ set_mode_nvl ()
    "И разговор продолжился. То превращаясь в коллективную лекцию, то в перекрёстный допрос. Иногда Ольга слушала, раскрыв рот, иногда тряслась, как на экзамене."
    "Кажется, экзаменаторов (или допрашивающих) интересовало про Ольгу буквально всё: от успеваемости до хобби, от школьных влюбленностей до любимого времени года."
    "Но и она узнала немало о том странном месте, куда привёз её автобус."
    "Помалкивали двое: пожилая, на грани старости, женщина очень властного вида — кажется, исполняющая обязанности здешнего директора; и мужчина с копной каштановых волос и такой же бородой, больше всего похожий на геолога из старого, ещё чёрно-белого фильма."
    "А потом Ольгу попросили покинуть помещение."
    $ set_mode_adv ()
    d_t3 "Ольга, погуляйте, пожалуйста, полчасика. А мы пока посоветуемся, сможем ли мы вам помочь с практикой."
    dreamgirl "Ольга в ходе совещания из Ольги Дмитриевны уже стала Ольгой. Впрочем, она и не возражала."
    stop ambience
    
    scene dct_ext_module_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    $ renpy.pause (0.8)
    play sound sfx_bus_honk
    th "Автобус уехал, а следующий только завтра."
    th "В этой истории есть один плюс: ещё сутки здесь, на курорте, я получила."
    stop ambience
    
    scene dct_ext_module_smoking_place with dissolve:
        ease 2 zoom 1.5 anchor (400, 300)
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["dance_of_fireflies"]
    th "Далеко не пойду. Вот и лавочка, специально для меня."
    th "Одиннадцать утра: разгар рабочего дня. Вряд ли кто-то сейчас выйдет покурить."
    show blink
    dreamgirl "Ольга вытянула ноги, прикрыла глаза и почти прислонилась к ребристой стене модуля, и так и замерла в положении неустойчивого равновесия, вцепившись в край лавки руками."
    th "Если я отклонюсь назад чуть сильнее, я испачкаю блузку о стену."
    play sound sfx_bed_squeak2
    dreamgirl "Кто-то сел рядом, на дальний край лавочки."
    show d_ss normal shirt at cright
    hide blink
    show unblink
    pause 0.8
    th "Дядька из кабинета директора, заведующий то ли лабораторией, то ли сектором. Зовут его Семён Семёнович, а вот фамилию я не запомнила."
    d_ss "Оля, чем вы занимались в стройотряде?"
    d_mt2 "Мы были проводниками на железной дороге."
    d_ss "Вот как. И много объездили?"
    d_mt2 "Да всю страну, от Бреста до Владивостока."
    show d_ss smile shirt with dspr
    d_ss "Значит, справитесь. С пассажирами справлялись, и с пионерами справитесь."
    show d_ss normal shirt with dspr
    d_ss "Вас ждёт начальство, Оля. Сейчас вам сделают предложение, от которого вы, конечно, сможете отказаться."
    d_ss "Только помните: те пионеры — они нуждаются в вас больше, чем вам сперва покажется."
    show d_ss smile shirt with dspr
    d_mt2 "Так я пойду?"
    th "Какой-то блаженный, хорошо, что безобидный."
    show d_ss normal shirt with dspr
    d_ss "Да-да, конечно."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_briefing_room with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_conf
    show adl_sh glasses normal at cright with moveinright
    dreamgirl "В кабинете Ольге действительно было сделано предложение, правда, «Шурик» в начале чуть было всё не испортил."
    adl_sh1 "Ольга, у нас действительно нет вакансий для пионервожатых, но вы можете попробовать себя в программировании человекоподобных роботов."
    d_mt2 "Но я же ничего не понимаю в программировании."
    th "Знаете, нет. Без меня."
    show d_bg normal suit at center with moveinleft
    d_gd "Александр, ну при чём тут ваши взгляды?"
    hide adl_sh with moveoutright
    d_gd "Оля, Александр слишком много общался с машинами, не слушайте его. Нет никаких перфолент с программами, и нет никаких роботов. Они почти такие же, как мы с вами."
    d_gd "Есть, конечно, отличия, но ничего сверхъестественного — по сути, это обычные подростки, которые сейчас неорганизованно болтаются."
    d_gd "Тут скорее ваши педагогические знания пойдут на пользу. Вы сюда как пионервожатая приехали, вот и попробуйте организовать пионерский лагерь."
    d_gd "Тем более что основы там уже заложены."
    th "А почему нет?"
    d_mt2 "Я… Я согласна."
    dreamgirl "И дальше события побежали по бюрократической колее."
    stop ambience
    
    scene dct_int_residential_block2_sunset with pixellate
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_night
    extend " Так что Ольга только бегала, собирала подписи, расписывалась сама, проходила бесконечные инструктажи."
    th "Устала я за сегодняшний день. Сейчас только форму приготовлю, и спать."
    show blink
    dreamgirl "Но даже в снах всё продолжался прожитый день."
    stop ambience
    
    scene dct_int_cabinet_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play music music_list["trapped_in_dreams"]
    show dct_dream_veil:
        shiver
    show d_to smile casual at center behind dct_dream_veil with dissolve
    d_to "Оля, сейчас подпишите здесь, здесь и здесь. Потом пройдёте в соседний кабинет, потом…"
    stop ambience
    
    scene int_aidpost_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_day
    show dct_dream_veil:
        shiver
    show cs normal behind dct_dream_veil with dspr
    csp "Зовут меня Виолетта Церновна Коллайдер, что запоминать тебе абсолютно не обязательно. Надевай шлем на голову и смотри на экран. Сейчас тебе будут быстро-быстро показывать картинки, если содержание картинки тебе нравится — жми на кнопку."
    stop ambience
    
    scene dct_int_cabinet_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show dct_dream_veil:
        shiver
    show d_to normal casual at center behind dct_dream_veil with dspr
    d_to "Видите ли, Ольга. В самом пионерском лагере, конечно, секретного ничего нет. Весь секрет в том, где он находится, и в его обитателях."
    stop ambience
    
    scene dct_int_laboratory with dissolve:
        zoom 0.75 anchor (300, 100)
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show dct_dream_veil:
        shiver
    show d_ss normal shirt at center behind dct_dream_veil with dspr
    d_ss "Ольга Дмитриевна, вам предстоит общаться с не совсем обычными… людьми."
    stop ambience

    scene dct_int_cabinet_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show dct_dream_veil:
        shiver
    show d_to normal casual at center behind dct_dream_veil with dspr
    d_to "Распишитесь ещё здесь… За два комплекта ключей от всех помещений лагеря."
    play sound dct_sfx_knock_door2
    stop music
    stop ambience
    
    pause 0.4
    
    scene dct_int_residential_block_night with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    pause 0.6
    play sound dct_sfx_knock_door3
    $ renpy.pause (2)
    play ambience ambience_int_cabin_night
    d_mt2 "Да?"
    th "Половина четвёртого. Кого ещё несёт?"
    voice "Ольга Дмитриевна? Через полчаса автобус, я провожу вас. Собирайтесь, пожалуйста."
    stop ambience
    
    scene dct_ext_residential_block_night with squares:
        walking
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound_loop dct_sfx_steps2
    dreamgirl "Офицер с повязкой на рукаве шёл чуть впереди, показывая дорогу. Ольга отставала на полшага, а ещё на два шага позади шёл солдатик с вещмешком, замыкая процессию."
    th "Романтика. Запах какой… Цветами и близким лесом пахнет."
    th "Могли бы и фонари включить."
    th "Странно, уже должно начать светать, а темно, как будто мы где-то на юге, хотя ехала я сюда на автобусе всего часов пять."
    dreamgirl "Солдату Ольгин чемодан не доверили, и офицер нёс его самолично, держа в левой руке."
    stop ambience
    
    scene dct_ext_module_night with dissolve:
        walking
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    dreamgirl "Ночные аллеи были пустынны, только один раз навстречу попались ещё трое военных — тот самый патруль, судя по повязкам, заступиться перед которым обещал ей Анатолий."
    dreamgirl "Девушка ожидала, что они выйдут к площади, но провожатый свернул на узкую тропку и, обогнув с тыльной стороны административный модуль, вывел Ольгу к западным воротам и дальше на остановку."
    stop sound_loop
    stop ambience
    
    
    scene ext_bus_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    play music music_list["goodbye_home_shores"]
    show d_to normal casual at center with dspr
    d_t3 "Ну, удачи вам, Ольга Дмитриевна. К семи утра будете на месте."
    dreamgirl "Анатолий вынырнул как из ниоткуда."
    d_t3 "Совсем одну вас не оставим, не беспокойтесь, раза два-три в неделю кто-то будет к вам заглядывать, а пока желаю вам проявить себя."
    dreamgirl "Анатолий оглянулся на сопровождавших Олю военных и понизил голос."
    d_t3 "И если вам покажется знакомым кто-то из пионеров, не говорите никому об этом. А ему самому — тем более."
    dreamgirl ""
    stop ambience
    
    scene int_bus_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    queue sound [ sfx_intro_bus_door_open , sfx_intro_bus_engine_start , sfx_intro_bus_engine_loop ] 
    dreamgirl "Двери автобуса с шипением закрылись, и автобус, мазнув фарами по кирпичному забору и воротам, развернулся и понёс Ольгу сквозь южную ночь навстречу будущему."
    play ambience sfx_bus_interior_moving
    dreamgirl "Ольга поглядывала на вещмешок, стоящий на соседнем сидении, и вспоминала слова передавшего мешок офицера: «Это вам на случай, если что-то пойдёт не так.»"
    dreamgirl "А потом офицер зеркально скопировал действия Анатолия, оглянувшись на того, маячащего в воротах: «И если всё пойдет совсем не так, то послезавтра в двадцать три ноль-ноль на остановке будет автобус»."
    th "Как? Что? Что значит — не так?"
    dreamgirl "Что-то он знал, невзрачный капитан с повязкой дежурного по части."
    dreamgirl "А у Ольги впервые мелькнуло ещё даже не подозрение, а предчувствие подозрения, что утром в приёмной ей рассказали не всю правду. Но мелькнуло и исчезло."
    stop music fadeout 1
    stop ambience

#########    
#Часть 3#
#########

label dct_olga_p3:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 3."
    $ day_time()
    show headline_text2 u"Часть III" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_briefing_room with dissolve
    $ prolog_time ()
    $ persistent.sprite_time ="day"
    play ambience ambience_int_cabin_day
    play sound dct_sfx_knock_door1
    play music music_list["your_bright_side"]
    show d_bg normal suit at right with dspr
    d_gd "Заходите!"
    show d_to normal casual at fleft with moveinleft
    d_to "Вызывали, Глафира Денисовна?"
    d_gd "Садитесь.{w=1} Скажите мне, куда она уехала?"
    play sound dct_sfx_chair
    pause 0.2
    show d_to normal casual at left with move
    pause 0.4
    show d_to normal casual with move:
        ypos 0.18
    d_to "В пятнадцатый узел."
    d_gd "Вот именно. А почему не в первый, как было запланировано?"
    d_to "Первый был закрыт туманом."
    d_gd "Можно было подождать и отправить её днём. Опоздала бы к линейке, ничего страшного. Вы, мужчины — все поголовно авантюристы. Так что готовьтесь к служебному несоответствию или к выговору. Смотря по результатам вашего эксперимента."
    stop music fadeout 1
    stop ambience
    
    scene black with dissolve
    $ renpy.pause (2)

    scene int_bus with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play sound sfx_bus_stop
    dreamgirl "Ольга проснулась, когда автобус начал разворачиваться на площадке перед воротами. Вот он чуть сдал назад, дёрнулся и заглох."
    $ renpy.sound.set_volume(1.5, delay=0, channel='sound2')
    play sound2 sfx_ikarus_open_doors
    dreamgirl "С шипением отошла в сторону дверь." 
    dreamgirl "Было страшно вот так, одной, без поддержки, начинать самостоятельную жизнь. Поэтому и открывать-то глаза не хотелось, но пришлось." 
    dreamgirl "Ольга обвела глазами пустой салон — никого. Правда, никого и не ожидалось. И водитель, похоже, уже успел куда-то уйти."
    th "Здесь очень загадочные и занятые водители автобусов — не успеешь оглянуться, как они куда-то исчезают."
    th "Надо выходить. Невозможно спрятаться от жизни в салоне автобуса."
    dreamgirl "Ольга подтянула к себе чемодан, подтянула подаренный вещмешок, судя по весу, по округлому и твердому на ощупь содержимому, набитый консервными банками."
    th "Не могу на них злиться, не могу над ними смеяться. Как там брат писал, что тушенка — самое дорогое, что есть у солдата."
    th "Но могли бы и подумать о том, каково таскать такую тяжесть хрупкой мне."
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound2')
    stop ambience
    
    scene int_bus with dissolve:
        zoom 1.5 anchor (400, 300)
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    dreamgirl "Тяжёлый чемодан, тяжёлый вещмешок… Ольга, пока допыхтела до двери, прокляла всё."
    th "Сейчас как выпинаю эти сундуки из салона!"
    stop ambience
    
    play sound dct_sfx_jump
    pause 0.3
    scene ext_camp_entrance_day with vpunch
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play music music_list["just_think"]
    th "Здорово. Как будто никуда и не уезжала!"
    th "Нет, надпись на воротах поменяли."
    th "Ну, Ольга{w=1}… Дмитриевна! Покажем им всем!"
    th "Но сначала в зеркальце на себя гляну."
    dreamgirl "Ольга поправила форму, проверила, как повязан галстук, ровно ли сидит панама."
    th "Первое впечатление никто не отменял."
    th "А ещё чемодан с мешком надо спрятать пока. И зайти в лагерь налегке."
    th "А то хороша будет красная от натуги и пыхтящая вожатая."
    dreamgirl "Было семь часов пятьдесят минут первого утра двухнедельного цикла. Впрочем, Ольга про циклы ничего не знала — для неё это было воскресенье, первый день смены."
    th "Ой, мама, спаси меня. Страшно! Вперёд, Оля!"
    stop music fadeout 1
    stop ambience
    
    scene ext_clubs_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "«Клубы» — кажется, это здесь."
    stop ambience
    
    scene ext_clubs_day:
        ease 2 zoom 1.5 anchor (500, 300)
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Ну и который ключ? Кажется, вот этот."
    play sound "<from 1>sound/sfx/lock_open.ogg"
    stop ambience
    pause 1.5
    
    scene int_clubs_male_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    play sound sfx_close_cabinet
    th "Всё как и говорили: кружки по интересам и радиорубка."
    th "Господи, только бы получилось."
    dreamgirl "Ольгу от предстоящей встречи с аборигенами то бросало в дрожь, то, наоборот, охлаждало до бесчувствия."
    th "Мне так никто толком и не объяснил, кто они и откуда взялись: роботы, искусственные организмы, люди?"
    th "Мама, моя мамочка, и спрятаться не за кого."
    th "Чёрт, ну и беспорядок! Где же аппаратура?"
    stop ambience
    

    scene dct_int_radioroom_nolight with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    th "А, вот же она. Ну, Ольга Дмитриевна, отступать некуда."
    play sound sfx_clench2
    pause 0.2
    show dct_int_radioroom_light with dspr
    dreamgirl "К счастью, кто-то когда-то повесил на стене тетрадный листок, где был расписан алгоритм включения трансляции."
    queue sound [sfx_click_2 , sfx_click_1 , sfx_click_3 , dct_sfx_horn_rise_tape ]
    dreamgirl "И в восемь часов ноль четыре минуты сигнал «Подъём» разбудил обитателей узла номер двадцать два, или, как они сами считали, пионерского лагеря «Совёнок»."
    th "Поспешай медленно, как говорит папа."
    stop ambience
    
    scene ext_clubs_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound2 sfx_slavya_run
    play music adaytoremember
    $ renpy.pause (2)
    dreamgirl "Звонкий девичий голос прозвучал из-за спины:"
    voice "Привет, ты только что приехала?"
    scene ext_clubs_day with vpunch
    dreamgirl "Ольгу опять затрясло. Ольга медленно, стараясь не подать вида, спрятала связку с ключами в сумочку и так же медленно обернулась к спрашивающей."
    show 3500_sl smile3 sport as sl at center with MoveTransition(1.2, enter=_moveleft, enter_time_warp=_ease_time_warp):
        ycenter 0.833
    # show sl normal sport with moveinleft
    th "Кто это? Не могу вспомнить."
    th "Анатолий на инструктаже записывать запретил, сослался на секретность."
    th "Как же её зовут? С{w}… С{w}… Нет, не Светлана."
    th "Ну же, Оля! Не могу вспомнить, как зовут — вот позорище-то."
    d_mt2 "Здравствуй, только знаешь, я всё-таки ваша вожатая, так что давай на Вы. Меня Ольга Дмитриевна зовут."
    show sl happy sport with dspr:
        ycenter 0.5
    slg "Вожатая? Здорово как!"
    show sl normal sport with dspr
    slg "А то мы поздно вечером приехали, и нас никто не встречает."
    show sl sad sport with dspr
    slg "Я уже думала, что мы и не нужны никому."
    show sl smile sport with dspr
    slg "Я побегу, остальным расскажу!"
    show 3500_sl smile3 sport as sl:
        ycenter 0.833
    hide sl with MoveTransition(1.2, leave=_moveright, leave_time_warp=_ease_time_warp)
    # hide sl with moveoutright
    $ renpy.pause (1)
    show sl normal sport at cright with MoveTransition(1.1, enter=_moveright, enter_time_warp=_ease_time_warp):
        ycenter 0.5
    slg "Простите, Ольга Дмитриевна, меня Славяна зовут. Можно Славя. Я быстро, обегу все домики и назад."
    show 3500_sl smile3 sport as sl:
        ycenter 0.833
    hide sl with MoveTransition(1.1, leave=_moveright, leave_time_warp=_ease_time_warp)
    play sound sfx_slavya_gets_out
    th "Ну Славяна же!"
    mt "Стой, Славя!"
    show sl normal sport at fright with easeinright:
        ycenter 0.5
    mt "Раз уж бежишь, сообщи всем, что линейка на площади в девять. Там и встретимся."
    sl "Поняла!"
    show 3500_sl smile3 sport as sl:
        ycenter 0.833
    hide sl with easeoutright
    sl "Линейка в девять!"
    th "А я пока в свой домик номер, кажется, семнадцать."
    th "Куда тут я спрятала чемодан?"
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    dreamgirl "Сорок минут спустя Ольга стояла на площади под обстрелом детских и уже почти не детских, всего-то на три года младше её, глаз и снова отчаянно тряслась."
    play sound_loop ambience_medium_crowd_outdoors
    show sl normal pioneer far at left with dissolve
    th "Надо что-то сказать, надо что-то сказать."
    show dv angry pioneer far at right with dissolve
    th "Как-то представиться, как-то скомандовать, чтобы меня услышали и послушались."
    hide sl
    show el serious pioneer far at left
    with dissolve
    th "Сейчас, потяну время до девяти. Пусть думают, что я пунктуальная."
    hide dv
    show mi surprise pioneer far at right
    with dissolve
    th "Оля, их же не больше, чем пассажиров в вагоне, а ты боишься!"
    hide el
    show mz glasses normal pioneer far at left
    with dissolve
    th "Нет, это точно не роботы, роботов я бы так не боялась и от их взглядов вся не чесалась бы."
    hide mi
    show un shocked pioneer far at right
    with dissolve
    th "Пора!"
    
    hide mz
    hide un
    with pixellate
    play music music_list["always_ready"]
    show mt panama shocked pioneer with dissolve
    show mt panama rage pioneer with dissolve_fast
    mt "Лагерь, по отрядам — становись!"
    stop sound_loop
    scene dct_lineup_mi_not_us with pixellate
    th "Как ни странно, но меня послушались."
    dreamgirl "Ольга оглядела подобие строя, кивнула Славе, подождала, когда последние из малышей займут свои места, и начала свою первую линейку: пожалуй, единственное хорошее, что удалось Ольге в этот и в следующий день."
    stop music fadeout 2
    stop ambience

    scene ext_square_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    dreamgirl "Как вскоре выяснила Ольга, лагерь прекрасно функционировал и без неё. Пионеры… Вот с пионерами было сложнее."
    dreamgirl "Пионеры тоже прекрасно функционировали без Ольги, скорее Ольга им даже мешала. Как будто в лагере действовала какая-то тайная сила."
    dreamgirl "И пока Ольга, раздавая поручения, не противоречила этой силе — всё было хорошо. Но стоило, например, поручить Лене…"
    stop ambience
    
    scene ext_square_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["door_to_nightmare"]
    mt "Тихонова Лена."
    show el normal pioneer far:
        xcenter 0.07 alpha 0
        pause 1.4
        linear 0.8 alpha 1
    show sl surprise pioneer far:
        xcenter 0.23 alpha 0
        pause 1.2
        linear 0.8 alpha 1
    show d_mz sceptic glasses pioneer far:
        xcenter 0.36 alpha 0
        pause 1.0
        linear 0.8 alpha 1
    show mi upset pioneer at right:
        alpha 0
        pause 0.8
        linear 0.8 alpha 1
    show dv grin pioneer:
        xcenter 0.9 alpha 0
        pause 0.6
        linear 0.8 alpha 1
    show un normal pioneer close with dissolve_fast
    un "Да, Ольга Дмитриевна."
    mt "Я вижу, ты книги любишь. Поэтому даю тебе пионерское поручение!"
    show un scared pioneer close with dspr
    show d_mz surprise glasses pioneer far with dspr
    un "К-какое, Ольга Дмитриевна?"
    mt "Заведовать библиотекой!"
    show d_mz amazed glasses pioneer far with dspr
    show un shocked pioneer close with dspr
    un "…"
    $ renpy.pause (2)
    show un scared pioneer close:
        linear 1 xcenter -0.2
    show d_mz amazed glasses pioneer far:
        linear 1.4 xcenter 1.16
    pause 0.3
    th "Я что-то не то сказала? Лена книги любит, и место там тихое — как раз по ней."
    mt "Тихонова! Не делай вид, что не слышишь!"
    mt "Елена!"
    stop music fadeout 1
    stop ambience
    
    scene ext_library_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "…"
    stop ambience
    
    scene int_library_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day
    mt "Лена!"
    stop ambience
    
    scene d2_micu_lib with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day
    mt "Женя?"
    mt "…"
    stop ambience
    
    scene ext_library_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["awakening_power"]
    $ renpy.pause (1)
    th "Какая я злая сейчас!"
    show sl normal pioneer with dspr
    sl "Ольга Дмитриевна, что-то случилось?"
    th "Так. Надо успокоиться. Незачем кричать на Славю."
    mt "Славя. Ты не знаешь? Что Женя делает в библиотеке?"
    show sl surprise pioneer with dspr
    sl "Но, Ольга Дмитриевна, вы спросили на линейке: есть ли добровольцы? Вот Женя и вызвалась, а вы её сами и назначили."
    th "То есть как — сама? А как же Лена?"
    mt "А Лена тогда где сейчас?" 
    show sl normal pioneer with dspr
    sl "Лена? Не знаю. Или в домике, или на площади. Вы же ничего ей не поручали, так что она, наверное, где-то с книгой устроилась."
    play sound sfx_dinner_jingle_normal
    sl "Да вы не переживайте, Ольга Дмитриевна. Сейчас она на обед придёт."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Или я схожу с ума, или надо мной изощрённо издеваются. И пожалуй, второе."
    th "Уже обед. Не хочется, но надо."
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show sl smile pioneer with dspr
    sl "Ольга Дмитриевна, а вы на обед разве не идёте? Давайте я вас подожду."
    show un normal pioneer far behind sl at right with moveinright
    show mz glasses normal pioneer far behind sl at cright with moveinright
    hide un with dspr
    hide mz with dspr
    mt "Иду-иду, Славя. Сейчас дождусь всех опоздавших и подойду. Не жди меня."
    sl "Хорошо, Ольга Дмитриевна."
    hide sl with dspr
    stop ambience
    
    scene ext_dining_hall_near_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "И лучше бы Лена с Женей уселись где-нибудь подальше. А то я могу накричать на них прямо в столовой."
    th "А пионеры, конечно, только этого и ждут."
    stop ambience
    
    scene dct_int_dining_hall_day_siluette with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    play music something_beautiful
    $ renpy. pause (1)
    th "Как-то тихо для обеда."
    show sl doll pioneer at center with dissolve
    th "Славя?"
    hide sl
    show dv doll pioneer at center 
    with dissolve
    th "Алиса? Что с ними?"
    hide dv
    show mi doll pioneer at center
    with dissolve
    th "Мику? Да все они!"
    play sound sfx_hell_crickets_1
    hide mi with dissolve
    dreamgirl "И вот тогда Ольге стало по-настоящему страшно."
    dreamgirl "Страшно от синхронного движения ложек, подносящих очередную порцию ко рту, от синхронного движения механически жующих челюстей, от остановившихся взглядов."
    dreamgirl "Надо было или идти в зал, или уходить. А Ольга, вдруг ослабев, стояла, прислонившись к дверному косяку, и переводила взгляд с пионера на пионера."
    show sl doll pioneer at center with dissolve
    dreamgirl "Вот пионеры покончили с первым; разом, одинаковыми движениями отодвинули тарелки и принялись за второе, запивая его чаем."
    play sound sfx_hell_crickets_2
    hide sl
    show mz doll pioneer at center
    with dissolve
    dreamgirl "Вот они пообедали, встали из-за столов и спокойно, без суеты и лишних движений, построились в очередь к мойке."
    stop music fadeout 1
    stop ambience
    
    scene int_dining_hall_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    th "Как муравьи какие-то или пчёлы."
    dreamgirl "А пионеры, поставив в окно мойки грязную посуду, разворачивались и вереницей шли к выходу."
    th "Сейчас они увидят меня и поймут, что я разгадала их тайну. Надо убегать, а сил нет даже закрыть глаза."
    play sound sfx_hell_crickets_3
    show el doll pioneer at center with dissolve
    dreamgirl "И вот головной пионер встретился взглядом с Ольгой."
    play sound dct_sfx_scare
    th "Вот и всё."
    show blink
    dreamgirl "Ольга начала медленно оседать на пол. А коллективный организм, состоящий из пионеров, вдруг сломался, рассыпавшись на автономные единицы."
    # визг
    $ renpy.pause (1)
    hide el
    show sl scared pioneer close
    hide blink
    show unblink
    sl "Ольга Дмитриевна, Ольга Дмитриевна. Что с вами?"
    sl "Семён, Серёжа, помогите мне."
    stop ambience
    
    scene dct_ext_dining_bench_day
    show mt sad pioneer panama:
        zoom 0.85 xcenter 0.6 ycenter 0.74
    with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    dreamgirl "Расталкивая всех, к Ольге подбежала Славя, подхватила, не дав упасть."
    dreamgirl "С помощью мальчиков из старшего отряда помогла сесть на лавку, принесла стакан холодного компота."
    show sl serious pioneer close at fright with dspr
    sl "Ольга Дмитриевна, вставайте. Я помогу вам дойти до доктора."
    stop ambience

    scene int_aidpost_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_day
    play music music_list["silhouette_in_sunset"]
    show d_cs normal with dspr
    d_cs "Акклиматизация. Сидите в домике до вечера, пейте холодный компот и не вздумайте бегать по лагерю и командовать пионерами. Славяна и без вас справится."
    d_mt2 "А…"
    d_cs "Что-то ещё?"
    d_mt2 "Нет-нет. Ничего."
    th "Не стоит говорить доктору о том, что я увидела в столовой. Доктор тоже из НИХ."
    d_cs "Вот и хорошо. Дойдёте сами, или вас проводить? А может, у меня в изоляторе полежите?"
    th "НЕТ!"
    d_mt2 "Нет, спасибо, доктор. Мне уже легче. Лучше я у себя…"
    stop music fadeout 1
    stop ambience

    scene ext_house_of_mt_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play music music_list["no_tresspassing"] fadein 1
    dreamgirl "Ольга так и просидела в шезлонге перед домиком до самого вечера."
    show sl sad pioneer with dspr
    sl "Ольга Дмитриевна, вы так на ужин и не пошли. Как вы себя чувствуете?"
    mt "Спасибо, Славя, уже лучше."
    play sound sfx_hell_crickets_1 fadein 0.7
    th "Ложь!"
    mt "Но ужинать пока не хочется. Я вот сижу, галеты грызу."
    stop sound fadeout 1
    show sl tender pioneer with dspr
    sl "Ой, я вам сейчас компот с кухни принесу."
    hide sl with dspr
    th "Страшно. Пойдёшь в столовую, а там эти!"
    play sound sfx_hell_crickets_2 fadein 0.7
    show sl doll pioneer at center with dspr:
        alpha 0.5
    $ renpy.pause (1)
    hide sl with dspr
    stop sound fadeout 1
    dreamgirl "Ольга грызла горькие сухари и с благодарностью думала о вчерашних военных."
    th "Надо только дождаться автобуса. Спасибо тебе, незнакомый капитан."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with slideright
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    dreamgirl "Весь следующий день Ольга ходила, поминутно оглядываясь."
    scene ext_houses_day
    show dct_lineup_mt_mi_not_us:
        align (0.5, 0.5)
        pause 2.5
        linear 1 xcenter -0.5
    with squares
    "Через силу заставила себя провести линейку, но в столовую не пошла — не смогла себя пересилить, и прожила день на одних сухарях."
    dreamgirl "Но не только в столовой, везде было страшно. Всё время казалось, что стоит отвести взгляд, как пионеры за её спиной превращаются в бездушные механизмы."
    stop ambience

    scene int_house_of_mt_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    play music music_list["just_think"]
    #play sound dct_sfx_horn_rebound_tape
    th "Отбой. Пора собирать вещи. И зачем только разбирала?"
    th "Пара книг, журнал «Костёр», так и не начатый дневник практики."
    th "Зачем я здесь вообще? Какая практика? Какой дневник? Что мне туда писать?"
    th "А ведь я тогда, на первой линейке, готова была их полюбить. Как они смотрели на меня..."
    th "И как Славя обрадовалась мне вчера утром!"
    th "Всё не то, чем кажется. Всё ложь."
    th "Платья? В чемодан!"
    th "Вожатская форма? Да какая я вожатая?{w} Какие пионеры, такая и вожатая!" 
    th "В стройотрядовской форме поеду."
    th "А то мало ли. Вдруг и на самом деле убегать и прятаться придётся?"
    th "Я думала, что после того, как всё прошлое лето проездила на поездах, будет проще. И тот чудак из посёлка говорил, что справлюсь."
    th "Ведь умела договориться и с цыганами, и с дембелями, и с уголовниками."
    th "Пионерская мафия — надо же мне было такое вчера придумать. С мафией тоже можно договориться. У меня даже со старухами получалось."
    th "Кому пригрозить, кого уговорить, кому объяснить правила. И всегда у меня в вагоне был порядок и никаких ЧП. А тут… Как договариваться вот с этим?"
    th "Всё. Пора выбираться на остановку."
    stop ambience
    
    scene dct_mt_mirror with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    th "Всё ложь."
    th "Прощайте все. Зря я сюда приехала."
    th "Записку для Слави написать? Зачем?"
    th "Прощайте."
    stop music fadeout 1
    stop ambience
    
    scene ext_house_of_mt_night_without_light with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    th "Не пойду через площадь. Чемоданом ещё этим светить."
    stop ambience
    
    scene dct_ext_house_of_un_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound dct_sfx_steps3
    th "Свет не горит. Интересно, где Лена? В домике спит или…"
    stop ambience
    
    scene dct_ext_musclub_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_day
    play sound dct_sfx_steps3
    th "Пусто, нет никого."
    th "Пионеры спят."
    th "Нет, это пионеры спят. А вот спят ли «пионеры» — я не знаю."
    stop ambience
    
    scene dct_ext_houses_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    th "Чемодан тяжёлый."
    th "Но я почти дошла."
    th "Сейчас к клубам, и дальше — на остановку."
    $ renpy.sound.set_volume(0.3, delay=0)
    play sound dct_sfx_cry_short
    $ renpy.pause (1)
    th "Что это? Кто-то плачет?"
    stop sound
    $ renpy.sound.set_volume(1.0, delay=0)
    
    scene dct_ext_houses_night with dissolve:
        zoom 1.5 
        subpixel True
        xalign 0.0 yalign 0.75
        ease 5.0 xalign 1.0
    play ambience ambience_camp_center_night
    $ renpy.pause (3)
    th "Нет никого. Показалось."
    stop ambience

    scene dct_ext_clubs_night_cham with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    th "Последние пятьдесят метров до ворот. Автобус уже ждёт. И можно будет забыть, как о кошмарном сне, об этом лагере, которого нет, и о его неживых пионерах."
    th "Надо кассету забрать."
    th "Жаль, что всё так сложилось."
    stop ambience
    
    scene dct_ext_clubs_night_cham with dissolve:
        zoom 1.5 anchor (400, 300)
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_day
    dreamgirl "Лампочка над крыльцом светила безжалостно-ярко, освещая цветок ромашки. Осторожно, так, чтобы не помять стебель, зажатый между створками дверей."
    th "Я не хочу об этом думать!"
    th "Нет!"
    dreamgirl "Не хотела думать, запрещала себе, но не смогла не представить, как без пяти десять в помещение заходит Славя, выгоняет оттуда Сыроежкина…"
    stop ambience
    
    scene int_clubs_male_sunset with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "sunset"
    show el doll pioneer at left with dspr
    $ renpy.pause (1)
    show sl doll pioneer at right with moveinright
    play ambience ambience_clubs_inside_day
    sl "Сергей, отбой через пять минут. Освободи помещение кружков."
    el "Да, Славя."
    hide el with dspr
    stop ambience
    
    scene dct_int_radioroom_nolight with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_clubs_inside_day
    show sl doll pioneer with dspr
    queue sound [sfx_click_2 , sfx_click_1 , sfx_click_3 , dct_sfx_horn_rebound_tape]
    $ renpy.pause (5)
    sl "Двадцать два ноль-ноль. Отбой."
    stop ambience
    
    scene ext_clubs_night with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show sl doll pioneer with dspr
    $ renpy.pause (3)
    show sl scared pioneer with dissolve
    $ renpy.pause (1)
    show sl doll pioneer with dissolve
    $ renpy.pause (2)
    stop sound
    stop ambience
    
    scene dct_ext_clubs_night_cham with dissolve:
        zoom 1.5 anchor (400, 300)
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_day
    th "Славя вышла из клубов, сорвала цветок, пристроила его так, чтобы я заметила, и ушла."
    th "И всё это с мёртвым лицом и размеренными механическими движениями."
    show sl scared pioneer close with dspr:
        alpha 0.5
    th "Как будто у них заморозили души."
    play music music_list["i_dont_blame_you"]
    play sound sfx_bus_honk
    hide sl with dspr
    th "Надо идти: неизвестно, сколько времени автобус будет ждать."
    play sound sfx_bus_honk
    th "А у Слави блестели дорожки от слёз на мёртвом лице."
    play sound sfx_bus_honk
    th "Никуда я отсюда не уеду. {w} Хотя бы ради этого цветка и этих дорожек от слёз — никуда не уеду."
    play sound dct_sfx_bus_departure
    th "Надо бы перемотать кассету на начало. Завтра народ будить."
    mt "Славя! Хватит прятаться, выходи, поможешь мне чемодан до домика донести."
    show sl tender pioneer close with fade
    $ renpy.pause (1)
    stop music fadeout 1
    stop sound
    stop ambience
    
    scene int_house_of_mt_night2 with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    th "Они живые! Пусть им нельзя что-то делать и они не могут о чём-то говорить, но они — живые."
    show blink
    th "А я — дура! И целых два дня потеряла. И вот как я после этого с ними сходиться должна?"
    stop ambience

#########
#Часть 4#
#########

label dct_olga_p4:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 4."
    $ day_time()
    show headline_text2 u"Часть IV" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_briefing_room with dissolve
    $ prolog_time ()
    $ persistent.sprite_time ="day"
    play ambience ambience_int_cabin_day
    show d_bg normal suit at right with dspr
    show d_to normal casual at fleft with moveinleft
    d_to "Доброе утро, Глафира Денисовна."
    d_gd "Садитесь. Рассказывайте, как там ваша протеже."
    play sound dct_sfx_chair
    pause 0.2
    show d_to normal casual at left with move
    pause 0.4
    show d_to normal casual with move:
        ypos 0.18
    d_to "По мне, так адаптировалась больше, чем следует. Когда новый цикл начнётся — больно ей будет."
    d_gd "Анатолий, я не о том."
    d_to "А я так именно что о том. Эмоциональную матрицу с неё сняли, параметры микса разработаны. Осталось подготовить посредника, и можно начинать процедуру."
    d_to "Цикл на первичный организм и по циклу на клонирование каждого микса. К концу пятилетки закроем все узлы и отчитаемся об автоматизации."
    d_to "Ещё Персунов предлагает запрограммировать биполярную модель поведения микса: ментор — сестрёнка. Такую модель проще с личностью оригинала совместить."
    d_gd "Хорошо. Приглашайте её в конце цикла сюда и действуйте. Объясняться с ней вам и, по технической части, Персунову. Что и как говорить — вы оба лучше меня знаете."
    stop ambience

    scene int_house_of_mt_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    dreamgirl "Вожатая проснулась задолго до горна и даже до звонка будильника. Несмотря на то, что поздно легла, спать совершенно не хотелось."
    th "Это сейчас не хочется, а днём буду носом клевать — неудобно будет перед пионерами. Интересно, Славя тоже будет сонная ходить?"
    play music music_list["i_want_to_play"]
    "И сразу же вспомнился вчерашний то ли поздний-поздний вечер, то ли ранняя-ранняя ночь. И появившаяся неизвестно откуда Славя, молча взявшая чемодан и нёсшая его до Ольгиного домика без видимых усилий."
    th "Что там у них в голове происходит? Неважно. Будем разбираться по ходу."
    th "До конца смены осталось одиннадцать дней, как бы и их не потерять."
    th "А мне ещё же отчёт о практике писать. А до отчёта ещё и план мероприятий."
    th "Видимо, придётся сочинять. А ещё придётся учитывать «особенности» каждого пионера, чтобы не было таких проколов, как с Леной."
    dreamgirl "Ольга, откинув простыню, присела на кровати, спустив ноги. Потянулась через проход к чемодану на соседней кровати и не дотянулась — пришлось привстать."
    th "Полный чемодан платьев, а одеть нечего. И кто в этом виноват, Оля? Сама же и виновата!"
    th "Убежать тебе захотелось. Так захотелось, что чемодан чуть не ногами утаптывала. А в итоге у нас безобразно скомканная вожатская форма."
    th "Спасибо, Славя. Кажется, ты не дала мне сделать чудовищную глупость, теперь-то я никуда не уеду."
    th "Но остаётся вопрос: что сегодня надеть? Стройотрядовскую форму или спортивный костюм? Всё остальное как минимум нуждается в утюге."
    th "И пусть это будет…{w=0.7} форма!{w=0.5} А я властью вожатой объявлю сегодня день генеральной уборки."
    th "Вот и первый пункт для отчёта."
    stop music fadeout 1
    stop ambience
    
    scene ext_house_of_mt_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound sfx_slavya_run
    $ renpy.pause (3)
    sl "Доброе утро, Ольга Дмитриевна, вы тоже бегать?"
    show sl smile sport with moveinright
    mt "Доброе утро, Славя. А ты, значит, бегаешь по утрам?"
    th "Ну да, в первый же день она была в спортивном костюме, а я так волновалась, что не обратила на это внимания. А вчера мне было не до того."
    mt "Славюшка, давай в другой раз. Мне очень хочется поговорить с тобой, а во время бега не стоит разговаривать."
    th "Почему я вчера их боялась? Ещё раз спасибо тебе, Славя."
    show sl smile2 sport with dspr
    sl "Я включу трансляцию."
    hide sl with moveoutright
    play sound sfx_slavya_run
    th "Идеальная помощница, может, слишком идеальная, в ущерб самой себе."
    $ renpy.pause (2)
    stop ambience

    scene ext_square_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Девять утра. Начинаем!"
    show 3500_mt rage uniform at center with dspr:
        ypos -0.13
    mt "Лагерь, по отрядам. Становись!"
    show 3500_mt smile uniform with dspr
    mt "Вольно."
    play music music_list["timid_girl"]
    dreamgirl "Сегодня линейка началась легко и свободно."
    mt "Пионеры, последняя информация на сегодня. Сегодня по лагерю объявляется субботник!"
    hide 3500_mt with moveoutleft
    show mi upset pioneer with moveinright
    mi "Но, Олечка Дмитриевна, ведь субботник — он же от слова суббота, а сегодня среда. Я, конечно, не хочу сказать, что я…"
    hide mi with moveoutright
    show 3500_mt smile uniform at center with moveinleft:
        ypos -0.13
    show 3500_mt grin uniform with dspr
    mt "Мику, властью вожатой объявляю сегодняшний день субботой!"
    mt "Кто хочет поработать?"
    hide 3500_mt with moveoutleft
    show dv smile pioneer with moveinright
    dv "Огласите весь список, пожалуйста."
    hide dv with moveoutright
    show 3500_mt smile uniform at center with moveinleft:
        ypos -0.13
    th "И даже пошутить получилось. А отклик от Алисы — это просто как подарок."
    mt "Славя, сядешь со мной за завтраком."
    th "Порешаем, кому что поручить."
    hide 3500_mt with moveoutleft
    show sl normal pioneer with moveinright
    sl "Хорошо, Ольга Дмитриевна."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_pages
    $ set_mode_nvl ()
    "{b}Дневник практики.{/b}"
    "…"
    "{i}День первый.{/i}\n\nРазмещение пионеров по домикам с учётом пола, возраста, характеров и пожеланий пионеров…\n"
    th "Переписать! Какие характеры, какие пожелания? В институте будут долго смеяться."
    "\n{i}День второй.{/i}\n\nЗнакомство с пионерами (возраст, состав семьи, склонности, характер). Знакомство пионеров с лагерем (правила внутреннего распорядка, кружки, места отдыха, персонал).\n"
    th "Примеры, Оль, где примеры?! Съедят же."
    "\n{i}День третий.{/i}\n\nДень чистоты — генеральная уборка лагеря. Вечером — награждение отличившихся и дискотека…"
    stop sound_loop
    stop ambience

    scene black with dissolve
    $ renpy.pause (3, hard=True)
    scene ext_square_day with squares
    $ set_mode_adv ()
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["trapped_in_dreams"]
    #dreamgirl "Ольга закрыла ежедневник."
    th "Вот я и прожила тут уже десять дней, и до конца смены осталось всего ничего — четыре дня. Надо им что-то придумать, чтобы запомнили."
    th "Говорят, что они всё забудут, а я в это не верю."
    th "Вот эти их непонятные приступы, как их назвать-то…"
    th "«Коллективного превращения в роботов»."
    th "Они повторялись ещё всего два раза, а на этой неделе и вовсе их не было."
    th "Они всё больше и больше становятся людьми."
    play sound_loop dct_ambience_beach
    stop music
    show d_sz normal pioneer at center:
        yalign 0.27
    show d_oz normal pioneer at right:
        yalign 0.27
    with easeinleft
    d_oz "И-и-и…"
    hide d_sz
    hide d_oz
    with easeoutright
    th "Так! Опять эти вампирчики в красных галстуках пьют кровь из бедной задёрганной  вожатой! Ненавижу этих противных мелких кровососов! И кровососок тоже ненавижу!"
    th "Сейчас пойду наказывать кого попало!"
    stop sound_loop
    mt "Эй вы, трое! Оба ко мне!"
    show d_sz normal pioneer at left:
        zoom 1.25 ypos -0.3
    show d_oz normal pioneer at right:
        zoom 1.25 ypos -0.3
    with easeinright
    mt "Что это за школа фехтования на мётлах? Так, Оксанка, дай метлу на минутку!"
    play music littleidea
    mt "Спасибо. А теперь оба — защищайтесь!"
    stop ambience
    dreamgirl "Ольга подхватила метлу, закрутила двумя руками, как пропеллер, вокруг центра тяжести, остановила вращение, перекинула за спиной из правой руки в левую, опять закрутила и пошла в атаку на пионеров, угрожая древковым оружием."
    
    scene dct_mt_with_broom with dspr
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Господи, хорошо-то как! И можно дурачиться, и тебя никто не осудит."
    d_sz "Эй! Тётя Оля, так нечестно! Ты большая, а мы маленькие!"
    th "Только бы не расхохотаться, только бы не расхохотаться."
    mt "Ну что, мушкетёры? Сдулись? Тогда подметайте."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_broom
    show sl normal pioneer with moveinleft
    sl "Ольга Дмитриевна, всё в по…"
    mt "Всё хорошо, Славя, не беспокойся."
    stop sound_loop fadeout 3
    show sl smile pioneer with dspr
    sl "А я и не беспокоюсь вовсе, Ольга Дмитриевна."
    hide sl with moveoutleft
    th "А хорошо!"
    th "Славя сейчас возьмёт метлу и пойдёт подметать остановку. Всё сама. Если хочешь сделать что-то хорошо — сделай это сам."
    dreamgirl "Ольга улыбнулась, вспомнив, как позавчера чуть не насильно вытащила Славю за ворота."
    stop ambience
    
    scene ext_camp_entrance_day with squares
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    show sl scared pioneer with dspr
    sl "Ольга Дмитриевна. Но ведь пионеру запрещается покидать территорию лагеря!"
    stop ambience
    
    scene ext_square_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["dance_of_fireflies"]
    dreamgirl "Ночью к северу от лагеря прокатилась гроза. Удушающая жара, прижимавшая «Совёнок» к земле последние четыре дня, отпустила, и жить стало очень даже приятно."
    th "Я тут совсем обленилась. Дневник практики заполнять не хочется, руководить субботником не хочется."
    show d_sz normal pioneer at left:
        zoom .8
    show d_oz normal pioneer at cleft:
        zoom .8
    with dspr
    th "Мелким вон тоже надоело подметать площадь, мётлы побросали, о чём-то совещаются."
    th "Шугануть их, чтоб работали? Лень."
    hide d_sz
    hide d_oz
    with dspr
    dreamgirl "Лёгкий ветерок, тянувший с реки, продувал насквозь жидкую рощу, отделявшую береговую линию от площади, и приятно шевелил волосы и гладил лицо."
    show blink
    th "Сейчас вытянусь на скамейке во весь рост. Куртку под голову, панамку на лицо, и так подремаю до обеда."
    th "Лена возражать не станет. А Славя разбудит потом."
    th "Или уйти на пляж, объявить, что контролирую купание, окунуться самой пару раз и подремать уже там, в тени грибка?."
    hide blink
    show unblink
    th "Стоило прикрыть глаза, как пионеры уже куда-то удрали по своим делам."
    th "Лена? Как читала, так и читает."
    show un surprise pioneer with dspr
    un "Ч-что?"
    mt "Всё в порядке, Лен."
    hide un with dspr
    th "Всё в порядке. Всё идёт по плану."
    th "Раз дневник практики не пишется, попробую написать про пионеров."
    stop music fadeout 1
    $ set_mode_nvl ()
    th "Младший отряд — дети как дети…"
    th "…"
    th "…"
    th "Что же написать-то?"
    $ set_mode_adv ()
    dv "Ольга Дмитриевна, Ольга Дмитриевна…"
    play music music_list["you_lost_me"]
    show dv scared pioneer with easeinleft
    dv "Ольга Дмитриевна…"
    dv "…Там… К вам пришли."
    mt "Алиса. Кто пришёл, и где это «там»?"
    show dv shocked pioneer with dspr
    dv "Там… Там… Они вас ждут. Пойдёмте, пожалуйста, я провожу."
    th "Что случилось? И вообще, и с ершистой Алисой?"
    mt "Ну, веди меня. И успокойся. Мы с вами лагерь в обиду не дадим."
    stop music fadeout 1
    stop ambience
    
    scene ext_clubs_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_to normal casual at fleft:
        ypos 0.05
    show d_ss normal shirt at left
    with dspr
    th "Анатолий и… Семён Семёнович, кажется."
    th "Этим-то что здесь нужно?"
    th "Но сначала — дети!"
    stop ambience
    
    scene ext_houses_day with slideright
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["awakening_power"]
    show el scared pioneer:
        xcenter 0.22
    show un shocked pioneer:
        xcenter 0.76
    show mi scared pioneer:
        xcenter 0.11
    show d_mz surprise pioneer at center
    show dv scared pioneer:
        xcenter 0.37
    show sl scared pioneer at cright
    show d_sm surprise pioneer:
        xcenter 0.92
    with dspr
    th "Что те двое с ними сделали?!"
    th "Сейчас падут на колени и начнут поклоняться, или побегут исполнять поручения, как Алиса."
    th "А тут уже и средний отряд на подходе. Вон они, за кустами мелькают."
    th "И все опять в роботов превратятся!"
    th "Я половину смены угробила на то, чтобы они ожили, а они… И даже Славя!" 
    th "Кто-то должен за это ответить!"
    stop ambience
    
    scene ext_clubs_day with slideleft
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_to normal casual at fleft:
        ypos 0.05
    show d_ss normal shirt at left
    with dspr
    mt "Вы, двое! Стойте, где стоите!"
    stop music fadeout 1
    stop ambience
    
    scene ext_houses_day with slideright
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show el scared pioneer:
        xcenter 0.22
    show un shocked pioneer:
        xcenter 0.76
    show mi scared pioneer:
        xcenter 0.11
    show d_mz surprise pioneer at center
    show dv scared pioneer:
        xcenter 0.37
    show sl scared pioneer at cright
    show d_sm surprise pioneer:
        xcenter 0.92
    with dspr
    mt "Теперь вы!"
    stop ambience
    
    scene ext_clubs_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["doomed_to_be_defeated"]
    show d_to normal casual at fleft:
        ypos 0.05
    show d_ss normal shirt at left
    with dspr
    show 3500_mt rage uniform at center with dspr:
        ypos -0.13
    mt "Сюда цирк приехал? Вы прибежали на клоунов посмотреть? У вас других дел нет? Вы уже всю территорию убрали? В домиках порядок?"
    mt "Зубными щётками площадь подмели?"
    mt "Не слышу!"
    stop ambience
    
    scene ext_houses_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show el scared pioneer:
        xcenter 0.22
    show un shocked pioneer:
        xcenter 0.77
    show mi scared pioneer:
        xcenter 0.11
    show d_mz surprise pioneer at center
    show dv scared pioneer:
        xcenter 0.37
    show sl scared pioneer at cright
    show d_sm surprise pioneer:
        xcenter 0.92
    with dspr
    $ renpy.pause (0.5)
    show dv angry pioneer
    show d_mz angry pioneer
    with dissolve
    $ renpy.pause (0.5)
    show el shocked pioneer
    show sl serious pioneer
    show un serious pioneer
    show d_sm serious pioneer
    with dissolve
    sl "Ольга Дмитриевна, мы…"
    show mi surprise pioneer
    with dissolve
    mt "Молча-ать!"
    mt "Сергей, Семён, Алиса — взять грабли на складе и бегом на пляж, весь песок пройтись с граблями. Старшая — Двачевская!"
    hide d_sm
    hide el
    hide dv
    with dspr
    mt "Хатсуне, почему эстрада облезлая?"
    show mi dontlike pioneer
    with dspr
    mt "Славяна, Елена, Мику и Евгения — взять краску, кисти, шпатели и на концертную площадку."
    mt "Старую краску ободрать и по новой эстраду покрасить. Старшая — Славяна! И средний отряд вам в помощь: все, кого поймаете!"
    mt "Не вижу реакции! Кру-гом! Бегом марш!"
    hide sl
    hide un
    hide mi
    hide d_mz
    with dspr
    d_to "Какой замкомвзвода пропадает."
    th "Ах, да. Тут ещё и эти двое."
    dreamgirl "Запал уже проходил, но его ещё хватило бы для взбучки гостям."
    stop music fadeout 1
    stop ambience
    
    scene ext_clubs_day with slideleft
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_to normal casual at fleft:
        ypos 0.05
    show d_ss normal shirt at left
    with dspr
    dreamgirl "Вот только гости оказались крепче нервами и сильнее тёртыми жизнью, чем Ольгины пионеры, поэтому на них грозный вид вожатой не подействовал."
    d_to "Вот так оно и работает, Ольга Дмитриевна. Вот так здешние обитатели на обычных людей и реагируют."
    d_to "И когда вы проведёте здесь какое-то время, на вас такая же реакция будет."
    d_to "Но вы с пионерами неплохо поработали, совсем неплохо: видите, они не остались здесь, а послушались вас и убежали."
    d_ss "А вы, наверное, гадали: почему мы бросили пионеров на произвол судьбы? Не бросили."
    d_ss "Вот, отправили сюда вас, а сейчас хотим сделать вам предложение. И снова вы сможете от него отказаться."
    show d_ss smile shirt
    d_ss "Надеюсь, что не откажетесь."
    show d_ss normal shirt
    d_ss "Похоже, что помочь им можете только вы и только так."
    stop ambience

#########
#Часть 5#
#########

label dct_olga_p5:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 5."
    $ day_time()
    show headline_text2 u"Часть V" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_briefing_room with dissolve
    $ prolog_time ()
    $ persistent.sprite_time ="day"
    play ambience ambience_int_cabin_day
    play music music_list["heather"]
    show d_bg angry suit at right
    play sound sfx_knock_door2
    d_gd "Входите!"
    show adl_sh glasses dontlike at left with moveinleft:
        xzoom -1.0
    adl_sh3 "Глафира Денисовна, избавьте меня, пожалуйста, от контактов с вашим Персуновым."
    adl_sh3 "Сначала совершенно невменяемо-пьяный позвонил мне ночью, говорил про какие-то похороны, потом требовал ключи от моей лаборатории."
    d_gd "Александр, вы дали ему ключи?"
    adl_sh3 "Ещё чего!"
    d_gd "Вот и хорошо. Просто, бывает, срывается человек. Это так редко, и даже не каждый год происходит, что можно его простить."
    adl_sh3 "Не понимаю вас, Глафира Денисовна. Здесь ответственная работа, а вы держите на ней человека, склонного к выпивке. А если это начнёт повторяться каждую пятницу?"
    d_gd "Во-первых, не склонного, а во-вторых, не начнёт. Я, Александр, знаю причину и повод, а вы — нет. Если у вас всё по этой теме, то давайте перейдём к делам вашей лаборатории."
    stop music fadeout 1
    stop ambience

    scene white with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play sound_loop dct_sfx_typewriter
    show promo_text u"Приказ №114\nО предоставлении отпуска"  with dissolve:
        pos (0.25, 0.1)
    stop sound_loop
    pause
    hide promo_text with dspr
    play sound_loop dct_sfx_typewriter
    show promo_text u"1) Предоставить Персунову С. С., заведующему Лабораторией моделирования нейтринно-белковых систем, по его заявлению отпуск продолжительностью семь календарных дней с зачётом в счёт ежегодного отпуска.\n2) На период отпуска, предоставленного согласно п. 1 настоящего Приказа, запретить доступ Персунову С. С. в служебные помещения на территории Филиала\n3) Приказ вступает в силу немедленно.\n\nИ. О. руководителя филиала Института *** АН СССР: Андрейко Глафира Денисовна\nОтветственный: Заместитель руководителя филиала по кадрам и режиму: Г*в Анатолий Васильевич."  with dissolve:
        pos (0.01, 0.1)
    pause
    stop sound_loop
 
    scene dct_int_laboratory with squares:
        zoom 0.5
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_clubs_inside_day
    play music music_list["heather"]
    show d_to normal casual at fleft
    show d_ss normal shirt at center
    with dspr
    d_to "Прочитал, расписался?"
    d_ss "Не сомневайся."
    d_to "Семён, сдавай мне ключи и пропуск, садись на поезд и катись в будку стрелочника, и чтоб до следующего понедельника духу твоего в посёлке не было."
    d_to "Или мне тебя сопроводить?"
    d_ss "Нет, сам доеду. Плохо получилось."
    d_to "Плохо. И Трофимов — урод."
    d_to "Но как получилось — так получилось. До понедельника."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    dreamgirl "Ольга шла по посёлку, невольно сравнивая его с лагерем."
    th "А похоже на мой лагерь."
    stop ambience
    
    scene dct_ext_module_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Это уродство трёхэтажное убрать, и совсем похоже будет."
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Площадь вообще точно такая же, даже Генда на месте."
    th "Не забыть узнать, как приеду домой, кто это такой, а то все либо отмахиваются, либо шутят, либо пожимают плечами." 
    th "Стоп, Оленька, а «домой» — это куда? Скучаешь ведь по лагерю? Беспокоишься, как там ребятишки?"
    stop ambience
    
    scene ext_square_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Как там ребятишки? Славя прибежала меня проводить, думала, что я не вижу её, выглядывающую из ворот."
    th "А я неплохо поработала. Те пионеры, которых я испугалась в первый день и от которых хотела сбежать, и те, которых я оставила вчера в лагере — это разные люди."
    th "Вот только говорят, что завтра они всё забудут."
    stop ambience
    
    scene ext_square_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Это что, завтра мне опять начинать всё сначала? Неужели в них ничего не останется? А что будет через месяц, когда я уеду?"
    th "Ах да, мой двойник — такой же, как пионеры, но с моей эмоциональной матрицей, которая добавит ему устойчивости, а через него и всем пионерам. Как-то так."
    th "Что-то ещё Семён Семёнович объяснял."
    stop ambience
    
    scene ext_clubs_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_to normal casual at fleft
    show d_ss normal shirt at left
    with dspr
    d_ss "Там всё сложнее, Оля, но это уже объяснять надо с формулами и графиками. Этого даже мои аспиранты не понимают, а Анатолий даже и не пытается."
    d_to "Я «сапог», мне не положено."
    show d_ss smile shirt
    d_ss "Ты не сапог, ты — ботинок."
    show d_ss normal shirt
    d_ss "В общем, Оля, остаться после практики здесь у вас нет возможности, но помочь обитателям «Совёнка» у вас получится."
    stop ambience
    
    scene ext_square_day with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["my_daily_life"] fadein 3
    th "Семён Семёнович утверждал, что сегодня они просто спят весь день, и лучше мне там не появляться. Я ему верю, но всё же…"
    th "Ничего, сегодня ночью еду обратно." 
    th "Вот только… подарки им купить? Зря, что ли, аванс получала?"
    th "Куплю им конфет. Всё равно деньги тратить не на что."
    stop ambience
    
    scene ext_square_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Полный коммунизм: за жильё не плачу, за свет не плачу, питание бесплатное, даже спецодежду можно на складе подобрать импортную, такую, что никто и никогда не поймет, что это спецодежда, и тоже бесплатно."
    th "Мне ведь положена спецодежда? Субботники в лагере проводить?"
    th "А потом я её \"потеряю\"."
    stop ambience
    
    scene dct_int_residential_block_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    th "До обеда ещё масса времени. Комнату убрала ещё до завтрака, в бухгалтерии побывала, что там у меня дальше?"
    th "«Доклад о проделанной работе, библиотека, 12-00»."
    th "Сорок минут осталось. Сейчас на пляж идти — это только расстраиваться."
    stop music fadeout 1
    stop ambience
    
    scene ext_library_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Как будто никуда не уезжала."

    scene int_library_day with dissolve
    pause 0.2
    show d_libr normal at cright with dspr
    
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day
    th "Вот только местная \"Женя\" гораздо симпатичнее."
    show d_libr surprise with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_libr "Здравствуйте, что-то я вас не помню. Или вы — Ольга?"
    show d_libr happy with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_libr "Тогда вас сам бог послал. Сейчас ваш доклад будет, помогите мне, пожалуйста, стулья расставить."
    stop ambience
    
    scene int_library_day with slideright
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day
    play music music_list["reflection_on_water"]
    show d_libr smile with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_libr "Вот и всё. А вы нервничали. Пришло пять человек, вежливо выслушали, вежливо задали вопросы, вежливо поблагодарили и разошлись."
    d_mt2 "А я и сейчас нервничаю. Все страшные, занятые и строгие. Начиная с директора."
    d_libr "Глафира? Не бойтесь её, она только с виду строгая."
    d_mt2 "А я боюсь. Как будто она ведьма какая-то, которой уже двести лет."
    show d_libr normal with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_libr "Да, она тут самая старая будет, ей уже шестьдесят четыре. Сидит здесь безвылазно лет десять уже, не меньше. Только в отпуск на материк выбирается, да ещё зимой студентам лекции читает." 
    dreamgirl "И на бедную Ольгу посыпались биографии всех более-менее заметных обитателей посёлка."
    stop ambience
    
    scene int_library_day with fade
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day
    th "Кажется, пора бежать."
    show d_libr normal with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_mt2 "Ой. Извините, пожалуйста. У меня после обеда ещё дела в лабораторном корпусе. Я загляну к вам в следующий приезд."
    show d_libr smile with dspr #Библиотекарь, спрайт заглушка из какого-то мода
    d_libr "Что вы, что вы, Оля, это я вас заболтала, простите меня."
    stop music fadeout 1
    stop ambience
    
    scene ext_library_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Это же ходячий справочник \"Кто есть кто\", а не женщина."
    th "Но вот зачем мне знать, что Семён Семёнович тоже долгожитель, как бабушка? Что Анатолий воевал, был ранен и сейчас здесь уже семь лет?"
    th "Кажется, и я попала в местный справочник."
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    voice "Оля, подожди!"
    show d_ol normal pen1 far at cright with dissolve #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Оля, здравствуй. Меня зовут Олеся, я из лаборатории Семёна Семёновича."
    d_mt2 "Здравствуй, Олеся. А где он сам?"
    show d_ol surprise pen1 far as d_ol2 at cright with dspr: #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        alpha 1
        pause 0.8
        linear 0.2 alpha 0
    show d_ol shy pen1 far #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Он{w=0.8}… он занят. Его срочно на материк вызвали."
    show d_ol normal pen1 far with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Но это неважно. Потому что это я занимаюсь твоим проектом."
    d_ol "Приходи после обеда в лабораторный корпус, я тебе расскажу и покажу всё, что есть."
    show d_ol smile pen1 far with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Потом мы уточним параметры твоей личности. Ну то есть не твоей, или не совсем твоей, или, в общем, той, что мы будем создавать."
    d_ol "Я выслушаю твои пожелания, и мы внесем изменения, если понадобится. И, собственно, всё."
    show d_ol grin pen1 far with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Ты сможешь считать себя соавтором нового организма."
    stop ambience
    
    #ЦГ Олеси перед терминалом
    scene dct_int_laboratory_mt:
        zoom 0.85 xcenter 0.2 ycenter 0.54
    show d_ol_sit_in_laboratory
    with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_clubs_inside_day
    play music music_list["i_want_to_play"]
    dreamgirl "Больше всего Ольге понравилось моделировать будущую личность своего будущего двойника."
    d_ol "Оль, не стесняйся, заказывай что хочешь."
    d_mt2 "Ну-у-у… значит так: возраст — чуть постарше, лет на пять, а то несолидно, когда вожатая почти ровесница своим пионерам."
    d_mt2 "Рост побольше, сантиметров на пять. А то пигалица, а не вожатая."
    d_ol "Рост, возраст. Что-то ещё? Ты не стесняйся, Оль, мне самой это нравится. Глаза, волосы?"
    d_mt2 "Нет, глаза и волосы — нормально. Вот только грудь…"
    th "Хорошо, что здесь Олеся, а не Семён Семёнович."
    d_ol "Понятно, Оль. Сделаем.{w} А что по характеру? Что-то добавить хочешь?"
    d_mt2 "Добавить?{w=0.5} Добавить.{w=0.5} Сейчас, подожди."
    th "Может, смелости и агрессии добавить? Чтобы вожатая не тряслась так перед линейками?"
    d_mt2 "Знаешь, ничего не трогай, наверное."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_laboratory_mt with dissolve:
        zoom 0.6 anchor (384, 116)
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_clubs_inside_day
    show d_ol smile pen2 close with dissolve:  #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0 xcenter 0.22
    d_ol "Ну вот и всё. Самая любимая часть моей работы."
    d_ol "Но знаешь, Оль. Всё равно то, что мы сейчас вводим — это всего лишь рекомендации для Системы. А что получится — то и получится."
    d_mt2 "А мне Семён Семёнович говорил, что это будет мой двойник."
    show d_ol normal pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Не совсем двойник, Оль. У неё будет твоя внешность с поправками. Она будет считать, что приехала вожатой в пионерский лагерь. У неё будут способности к педагогике. И у неё будут твои воспоминания, но не все."
    d_ol "А ещё у неё будут воспоминания: мои, бабы Глаши, шефа — вообще всех людей, которые были здесь. И она свяжет эти воспоминания своим воображением. И будет считать этот… это лоскутное одеяло своим прошлым."
    show d_ol shy pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "«Лоскутное одеяло чужих воспоминаний» — правда, красиво? Это нам шеф на семинаре сказал. Иногда на него находит, и он начинает говорить, как артист со сцены."
    d_mt2 "Семён Семёнович? А когда он вернётся?"
    show d_ol surprise pen2 close as d_ol2: #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0 xcenter 0.22 alpha 1
        pause 1
        linear 0.35 alpha 0
    show d_ol normal pen2 close
    with dspr
    d_ol "Он{w=1}… через неделю. Ну, пойдём в виварий."
    stop ambience
    
    scene dct_int_vivariy with dissolve #Виварий
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience dct_ambience_vivero
    dreamgirl "В виварии Ольге не понравилось. Пахло зверинцем, было темно и тесно. Обеспокоенные обезьяны бегали в своих клетках, кричали, и лишь одна, похоже, что уже накачанная успокоительными, безучастно сидела в углу около поилки."
    #Шлем и жилет, каждый со свисающей косой проводов, уже надетые на животное, делали её похожей на персонаж фильма про покорение космоса.
    show d_ol normal pen2 at cleft with dissolve:  #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0
    d_ol "Вот, Оль, это твой посредник. Все данные уже или в нём, или готовы к трансляции. Осталось дождаться ночи."
    d_mt2 "А зачем так сложно? Напрямую с меня нельзя было параметры передать?"
    show d_ol serious pen2 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Понимаешь, Оль. Если передавать напрямую информацию от человека в Систему, то он или погибает, или вынужден жить здесь всю оставшуюся жизнь."
    show d_ol grin pen2 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Но, правда, стареет гораздо медленнее. И вот, когда мне исполнится двадцать пять…"
    show d_ol serious pen2 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "А, обезьянки... Их, конечно, жалко, но нам их теперь удаётся спасти."
    stop ambience
    
    scene dct_int_laboratory_mt with dissolve:
        zoom 0.5
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_clubs_inside_day
    show d_ol normal pen1 at right with dissolve #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_mt2 "Олеся, вы же сегодня опыт ставить будете?"
    d_mt2 "А можно я посмотрю?"
    d_ol "Вообще-то нет. Там для этого нужно в куче журналов расписаться, а они у шефа в столе заперты."
    show d_ol smile pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    extend " Но шеф уехал, так что ты приходи к восточным воротам к девяти вечера. Заодно и поможешь мне."
    stop ambience
    
    scene dct_ext_backroad_light_7 with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night
    play music music_list["smooth_machine"]
    show d_ol normal pen1 at right with dissolve #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Оборудование установлено, животное зафиксировано. Через час совсем стемнеет, и появится туман. Возвращаемся на территорию."
    stop ambience
    
    scene dct_ext_kpp3 with squares:
        zoom 1.5 anchor (300, 400)
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show d_ol normal pen2 at left with dissolve:  #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0
    d_ol "Ты, главное, за ворота не выглядывай, а то развернёшь Систему на себя. А как я тебе скомандую, сразу бери верёвку и тащи за неё тележку с клеткой сюда. А приборы техники утром заберут."
    dreamgirl "Ольга кивала, слушая путаный инструктаж Олеси. Потом, когда инструктаж кончился, а больше ничего не происходило, заскучала. И от скуки стала вслушиваться в трёп сидящих в курилке техников-лаборантов."
    stop ambience
    
    scene dct_ext_kpp3 with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    d_vo_2 "А куда шеф пропал?"
    d_vo_1 "Ты не знаешь? Набрал спирта в лаборатории и пьёт. Копия у него активировалась."
    d_vo_2 "И что? Радоваться должен."
    d_vo_1 "А чему радоваться? На неделе её обнулят. Ты приказ не читал? Всех активированных, начиная с первого апреля, сбрасывать на нуль."
    d_vo_1 "Помнишь, Толян выключатели по лабораториям выдавал? В том числе шефу. Только шеф не взял."
    d_vo_1 "Сказал, что причины понимает, со всем согласен, и протокол совещания подписал, но у него на детей рука не подымется… А уж за свою-то копию он всяко переживает."
    stop music fadeout 1
    d_vo_2 "Понятно. А своих детей у него…"
    play sound dct_sfx_monkey_cry
    $ renpy.pause (1)
    d_vo_2 "Началось!"
    stop ambience
    stop sound fadeout 1
    "Но дальше Ольге не удалось дослушать, потому что за воротами вдруг закричала от боли накачанная седативными обезьянка."

#########
#Часть 6#
#########

label dct_olga_p6:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 6."
    $ day_time()
    show headline_text2 u"Часть VI" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_ext_kpp3 with hpunch:
        zoom 1.5 anchor (300, 400)
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound dct_sfx_monkey_cry
    play music badstory
    #Олеся
    d_mt2 "Обезьянка!"
    show d_ol angry pen2 close with dissolve:  #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0
    d_ol "Ты куда? Забыла, что я говорила? Сиди и терпи."
    d_mt2 "Но жалко же, Олеся."
    show d_ol serious pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Мне тоже жалко. Но я сижу и терплю."
    show d_ol normal pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "А ты вообще хотела сама пойти вместо обезьянки. Не бойся, всё идёт как надо, я в первый раз тоже дёргалась."
    d_ol "Это когда Электроника делали. Трофимов захотел себе универсального помощника-лаборанта, чтоб на все руки. А у шефа как раз проект готовый был."
    d_ol "Получилось изумительно. Такой умнейший парень вышел, жаль, что туповатый."
    hide d_ol with dspr
    dreamgirl "Как можно одновременно быть умнейшим и туповатым — Олеся не расшифровала, да Ольга и не спрашивала, больше прислушиваясь к обезьянке по ту сторону ворот." 
    play sound dct_sfx_monkey_cry
    show d_ol serious pen2 close with dissolve:  #Олеся, спрайт заглушка из "По ту сторону Совёнка"
        xzoom -1.0
    d_ol "Так, а сейчас начнётся моя работа. Помни: по команде хватай верёвку и тащи."
    show d_ol normal pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Знала бы ты, какое старьё пользуем."
    show d_ol shy pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    extend " Шеф такой умница, а ему финансирование всё режут и режут. Как он результатов добивается — ума не приложу."
    show d_ol normal pen2 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Хорошо, что Трофимов в благодарность за Электроника шефу помог с оборудованием. Без него бы один только персонал для узлов штамповали."
    d_ol "Три."
    d_ol "Два."
    d_ol "Один."
    d_ol "Тянем!"
    stop music fadeout 1
    stop sound fadeout 1.5    
    stop ambience
    
    #ЦГ с обезьянкой в тележке
    show dct_mt_monkey with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    th "Бедная."
    #Олеся
    d_ol "Кажется, всё в порядке. Всё, Оль, больше ничего интересного не будет, можно идти по домам. Остальное всё техники сделают."
    d_tech_2 "Сделаем, сделаем, девочки. Сейчас скотинку коновалу сдадим, а утром за приборами вернёмся."
    stop ambience
    
    scene ext_square_night with dissolve:
        walking
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play sound_loop dct_sfx_steps2
    dreamgirl "До площади всем было по пути. Техники продолжили свой разговор, но как Ольга ни вслушивалась — больше ничего интересного не услышала: говорили о футболе, о рыбалке и о политике."
    show d_ol normal pen1 at cright with dissolve #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Оль, вот ты среди {b}них{/b} почти две недели жила. Это на две недели больше, чем любой из нас. Скажи, пожалуйста, они — люди?"
    d_mt2 "Да.{w=0.8} Да."
    th "А ведь и правда — да. Даже такие, какие они были в первые дни, когда я хотела сбежать — они где-то там, глубоко внутри, хранили человечность. Я же видела следы от слёз на щеках у «механической» Слави."
    show d_ol serious pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Оль, я тоже думаю, что да. То есть хочу так думать, но…"
    show d_ol surprise pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Ты только никому не говори, потому что это секрет. Но у нас тут живёт девочка из них."
    show d_ol shy pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Очень хорошая девочка, первый удачный микс. Девочка как девочка. Умная, красивая. Поёт замечательно, танцует, играет на всех инструментах. Мы все её очень любим."
    show d_ol serious pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Вот только каждый цикл она забывает всё, что узнала, и каждый цикл для неё начинается с того, что её папа привозит её сюда отдохнуть и чуть поработать, по четыре часа в день. Ну это она считает так…"
    d_ol "Вот посмотришь на неё, и кажется, что она — человек, ну пусть с проблемами с памятью. Но я же знаю, как они создаются. Мы сами с тобой сегодня одного создали. Людей так не делают."
    stop sound_loop
    show d_ol normal pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Ой, мы уже пришли. Тебе налево, а мне направо. А тебе же ещё собираться."
    show d_ol smile pen1 with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Ну ты как приедешь в конце цикла — обязательно заходи, а то все разъехались по отпускам, и мне даже поболтать не с кем."
    stop ambience
    
    scene dct_ext_residential_block_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play music brush_marks
    th "Этот разговор с Олесей… Чем определяется человек — происхождением или тем, что внутри него: мыслями, чувствами, эмоциями?"
    scene dct_ext_residential_block_night with fade
    th "А ведь можно сказать, что эта несчастная обезьянка кричала при родах. А раз человек намного крупнее обезьяны, то ей очень больно было. Вот она и кричала."
    scene dct_ext_residential_block_night with fade
    th "Олеся, конечно, шутила, что собирается пройти через это, чтобы не стареть. Но ведь кто-то же прошёл, откуда-то это уже известно."
    scene dct_ext_residential_block_night with fade
    th "Боль, наверное, была жуткая. Если обезьянка бедная так кричала. А кто-то и погиб — Олеся говорила, что человек или погибает, или вынужден жить здесь."
    scene dct_ext_residential_block_night with fade
    th "Я этот крик на всю жизнь запомню. Этот крик, и как мы обезьянку из тумана вытаскивали."
    stop ambience
    
    scene dct_ext_backroad_light_7
    show fog_face_mask
    with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    th "Я вру сама себе. Там ещё что-то было — что-то, что гораздо главнее, чем бедная обезьянка. И вот это \"что-то\" я тоже запомню."
    th "Тот туман. Кажется, это не просто туман. Кажется, он смотрел на меня. И кажется, я встретилась с ним взглядом."
    th "Ощущение внимательного, но совершенно безэмоционального взгляда. А я чувствовала себя букашкой под микроскопом."
    th "И если бы не Олеся."
    show d_ol angry pen1 close with dspr #Олеся, спрайт заглушка из "По ту сторону Совёнка"
    d_ol "Оля, что встала? Помогай!"
    stop ambience
    
    scene dct_int_residential_block_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    th "А сейчас это ощущение вернулось."
    scene dct_int_residential_block_night with fade
    th "Жуть какая! И на этаже, кроме меня, никого."
    scene dct_int_residential_block_night with fade
    th "А чернота за окном смо-о-отрит. Я же не усну!"
    scene dct_int_residential_block_night with fade
    th "Пойду к воротам ждать автобуса. Там хоть солдатик дежурит. Всё не одна. Ещё час — не так и много, можно потерпеть."
    stop music fadeout 1
    stop ambience

    scene ext_no_bus_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_entrance_night
    th "А прохладно, оказывается. Скоро там этот несчастный автобус?"
    play sound sfx_broom_sweep
    th "Всё равно. Хорошо, что у себя ждать не стала. Солдатик, правда, робкий какой-то. Только подметает вокруг меня да на пакет с конфетами смотрит. Как дворняга на колбасу." 
    th "Хватит с тебя одной конфеты, у меня и без тебя есть с кем поделиться."
    dreamgirl "Солдатик никак не решался подойти поближе и заговорить с девушкой. А Ольга не знала, радоваться этому или сожалеть, потому что говорить не хотелось, но разговор отвлек бы её от длящегося неприятного ощущения чужого и чуждого взгляда из темноты."
    th "Интересно, это нервы или это от того, что я смотрела туда — на клетку и туман за ней? Как там сказала Олеся: «обратила внимание системы на себя». И что теперь будет? Нет, Олеся сказала \"Система\" с большой буквы. Что бы это ни значило, но Система с большой буквы интересуется мной."
    play sound sfx_ikarus_arrive
    th "Ой, кажется, автобус едет. Всё, в лагерь! Наконец-то."
    $ renpy.pause (3)
    stop ambience
    
    scene ext_bus_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play sound sfx_intro_bus_engine_start
    th "Ну, поехали."
    
    scene int_bus_night with fade
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience sfx_bus_interior_moving
    th "А я пока подремлю по дороге."
    
    scene dct_olga_road with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    th "Как там меня встретят?"
    $ renpy.pause (1)
    show blink
    $ renpy.pause (4)
    stop ambience
    
    scene int_bus with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play sound sfx_ikarus_open_doors
    $ renpy.pause (2)
    th "Уже? Приехали? А я чуть не проспала!"
    th "Ольга Дмитриевна, на выход!"
    stop ambience
    
    play sound dct_sfx_jump
    pause 0.3
    scene ext_camp_entrance_day with vpunch
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    th "Здравствуйте, милые!"
    stop ambience
    
    scene ext_clubs_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play sound dct_sfx_horn_rise_tape
    play ambience ambience_camp_center_day
    th "Славя! Где тебя носит?"
    $ renpy.pause (3)
    stop sound fadeout 1
    th "Ну наконец-то!"
    #play sound  sfx_slavya_run
    show sl normal sport with moveinright
    play music music_list["timid_girl"]
    sl "Привет, ты, наверное, только что приехала?"
    mt "Здравствуй, Славя. Двадцать минут назад. Только знаешь, давай на вы — я всё-таки ваша вожатая. А ещё меня Ольга Дмитриевна зовут."
    show sl laugh sport with dspr
    sl "Вожатая? Вот здорово! А то мы вчера поздно вечером приехали, а нас никто не встречает."
    show sl surprise sport with dspr
    sl "А откуда вы знаете, что меня Славя зовут?"
    mt "А тебя просто по другому и назвать было нельзя. Только Славей. Ну, беги по своим делам, а я пока к себе в домик. Только предупреди всех, что линейка в девять на площади."
    hide sl with moveoutright
    play sound sfx_slavya_run
    sl "Обязательно, Ольга Дмитриевна!"
    th "Ничего не помнит. Жаль, но остальные, наверное, так же."
    th "Но наплевать, что они ничего не помнят — это те же самые девочки и мальчики."
    mt "Господи, как будто домой приехала! Главное, сегодня на линейке не улыбаться рот до ушей. Я же строгая!"
    stop music fadeout 1
    stop ambience


#########
#Часть 7#
#########

label dct_olga_p7:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 7."
    $ day_time()
    show headline_text2 u"Часть VII" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene ext_house_of_mt_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play music music_list["door_to_nightmare"]
    show d_sm normal pioneer at right with dspr
    me "Простите, вас Ольга Дмитриевна зовут?"
    th "Неужели не забыл ничего? Но они же всё забывают. И начальство говорило, и Олеся подтвердила."
    th "Да я и сама убедилась: Славя ничего не помнит и встречала меня почти теми же словами, что и в прошлый раз. А может, всё проще?"
    mt "Да, это я. Тебе Славя сказала?"
    show d_sm scared pioneer with dspr
    me "Славя? Да, Славя сказала."
    hide d_sm with moveoutright
    th "И что он хотел сказать?"
    th "Потом разберусь. А сейчас — линейка."
    stop music fadeout 1
    stop ambience
    
    scene ext_square_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound_loop ambience_medium_crowd_outdoors
    th "Три секунды"
    extend ", две"
    extend ", одна."
    th "Пора!"
    show mt rage panama pioneer with dspr
    play music music_list["doomed_to_be_defeated"]
    mt "Лагерь, по отрядам. Становись!"
    stop sound_loop fadeout 1
    dreamgirl "Началась новая смена, новое знакомство со старыми знакомыми."
    #show mt normal panama pioneer with dspr
    mt "Здравствуйте, пионеры!"
    voices "Здрав…"
    stop music fadeout 3
    show blink
    dreamgirl "А дальше работали только рефлексы, а рассудок у Ольги Дмитриевны вновь включился лишь на финальной реплике."
    hide blink
    show mt grin panama pioneer
    show unblink
    mt "Линейка закончена. Через десять минут завтрак, кто не хочет — может не ходить. Разойтись!"
    hide mt with dspr
    stop ambience
    
    scene int_dining_hall_people_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full
    th "Ура! Олька, неужели у меня получилось?"
    th "Обычная столовая. Обычные дети. И никаких \"кукол\" из прошлого цикла."
    th "Смеются, дурачатся…"
    mt "Младший отряд! Хотите поиграть — уходите из столовой!"
    th "Уже нашли себе друзей и разбились на компании."
    th "Почему в детстве достаточно пяти минут знакомства, и ровесник уже твой лучший друг? Почему в двадцать лет так не выходит?"
    show d_cs normal at center with dspr
    d_cs "Ольга Дмитриевна, если я нужна — я у себя."
    mt "Хорошо."
    hide d_cs with moveoutleft
    th "Я и про персонал теперь знаю. Интересно, что у них в головах творится? Вот эта доктор, если её разговорить, пожалуется, наверное, на мужа-пьяницу, а повариха — на сына-оболтуса, которого армия только и исправит."
    show mi normal pioneer with moveinleft
    mi "Приятного аппетита, Олечка Дмитриевна. Сегодня на завтрак каша, вы же знаете, я…"
    mt "Приятного аппетита, Мику."
    hide mi with dspr
    th "Девочки: Алиса, Лена, Мику и Женя почти не изменились, ну может совсем чуть-чуть."
    show sl serious pioneer with dspr
    sl "Ольга Дмитриевна, всё в порядке? Я тут малышей отдельно посадила."
    mt "А как же иначе, Славя — конечно, в порядке." 
    hide sl with dspr
    th "Славя стала самостоятельной и действует без команды. Взяла сейчас и усадила всех младших в один угол, чтобы их не затоптали."
    th "Правда, она и в прошлую смену уже начинала действовать без команды. Самая развитая из них."
    sl "Семён, садись с нами!"
    th "А Семён ей явно нравится. Что там про путь к сердцу через желудок? Вот и Славя скармливает Семёну свою булочку."
    me "Славя, ну как ты не понимаешь!" 
    th "А Семён что-то говорит Славе, я бы даже сказала — горячо доказывает, и оба поглядывают на меня. Нет, жаль, что они далеко сидят."
    show mz normal pioneer at left with moveinright
    show el normal pioneer at right with moveinright
    el "Женя, ты же в библиотеку?"
    th "Сыроежкин — я узнала о его происхождении! Ну и что?"
    th "Изменилось ли моё к нему отношение — ничуть. Расскажу ли я ему правду про него — никогда."
    hide mz with moveoutleft
    th "Но то, что он \"умница и туповатый\" одновременно — да. Олеся хорошо сказала; может, только не туповатый, а простоватый."
    hide el with moveoutleft
    th "Но теперь понятно, что Сыроежкин делает в помещении кружков: все эти приборы и инструменты — они для него родные; и, кажется, понятно, почему он ничего не делает в помещении кружков — ждёт команды."
    th "Надо бы этим заняться, но я же ничего не понимаю в технике! Может, хотя бы мелкий ремонт ему поручить?"
    show mi normal pioneer with dspr
    mi "… а каша, Олечка Дмитриевна, она…"
    th "Я и о происхождении Мику узнала, ведь это о ней Олеся сказала: \"Первый удачный микс\"."
    th "Вот только эта Мику — здесь, а та, о которой говорила Олеся — там."
    th "Значит, их больше одной? Значит, и мой двойник будет не один? Надо будет спросить об этом."
    mi "Но, Олечка Дмитриевна, каша всё равно вкусная. А вы стоите здесь уже полчаса и не садитесь за стол. Так же нельзя, вот мне мама говорит…"
    mt "Уже сажусь, спасибо за заботу, Мику."
    hide mi with moveoutleft
    th "Сейчас позавтракаю и пойду в библиотеку: там была печатная машинка. Нужно напечатать \"План мероприятий\" и вывесить его на стенд. С прошлой смены собираюсь."
    stop ambience
    
    scene ext_dining_hall_away_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    me "Ольга Дмитриевна!"
    show d_sm normal pioneer at right with moveinright
    mt "Да, Семён. У тебя ко мне дело? Давай побыстрее тогда. Мне ещё \"План мероприятий\" нужно напечатать и вывесить."
    mt "А может, ты мне поможешь в этом? На машинке печатать умеешь?"
    me "Но ведь это же неправильно, Ольга Дмитриевна."
    play music music_list["awakening_power"] fadein 2
    mt "Ну-ка, ну-ка. Что именно неправильно?"
    show d_sm serious pioneer with dspr
    me "Всё! Вы не должны печатать этот План, вы не должны его вывешивать. Мы должны были сегодня утром уехать по домам на автобусах."
    show d_sm scared pioneer with dspr
    me "А вместо этого остались ещё на смену! И все, все уверяют меня, что мы только сюда приехали! Даже Славя ведёт себя так, будто только познакомилась со мной! Скажите мне, что это сон, пожалуйста!"
    mt "Семён, Семён, успокойся. Сейчас во всём разберёмся."
    th "Что же делать? Что там на инструктаже говорили?"
    stop music fadeout 2
    stop ambience
    
    scene int_aidpost_day with pixellate
    $ prolog_time ()
    $ persistent. sprite_time = "day"
    play ambience ambience_medstation_inside_day
    show cs normal with dspr
    cs "А ещё ни в коем случае не рассказывай пионерам о реальном положении вещей, во избежание разбалансировки их психики."
    stop ambience
    
    scene ext_dining_hall_away_day with hpunch
    $ day_time ()
    $ persistent.sprite_time = "day"
    show d_sm normal pioneer at right
    play ambience ambience_camp_center_day
    d_to "Нет, Семён, это не сон, поздравляю тебя."
    show d_to normal casual at left with moveinleft
    d_to "Пойдёмте на остановку, а то сейчас сюда толпа сбежится. Чувствуют они нас, пока без памяти."
    stop ambience

    scene ext_bus with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    show d_sm normal pioneer at cleft
    show d_to normal casual at fleft
    with dspr
    d_to "Чтобы у вас не было сомнений, Ольга Дмитриевна, вот предписание. Распишитесь, пожалуйста, что ознакомлены."
    d_to "А вас, Семён, я забираю. Что тут вам делать, раз к вам память вернулась? Всё, санаторный курс закончен."
    show d_sm smile pioneer with dspr
    me "Правда? Значит, всё так и есть, и я не сумасшедший?"
    d_to "Правда, правда. Ты разумнее всех нас, вместе взятых."
    show d_sm normal pioneer with dspr
    me "А вещи?"
    d_to "У тебя есть что-то, чего не жалко бросить? Дуй в автобус! А то передумаю."
    hide d_sm with dspr
    mt "С ним точно всё будет в порядке?"
    show d_to smile casual
    d_to "Абсолютно. Подкормим, проверим, подкорректируем и вернем вам лучше чем был."
    show d_to normal casual
    d_to "С ними бывает такое: старые воспоминания не стираются до конца и наслаиваются на новые. И возможны последствия, вплоть до… неприятных."
    d_to "Да, неприятных для всех. И для него самого, и для вас. Например, он может объявить вас куклами-марионетками, а себя — единственным настоящим человеком, и начать уничтожать вас, или он может убить себя."
    d_to "Так что приходится забрать его у вас временно. Не беспокойтесь, никто вашему подопечному вреда не причинит."
    hide d_to with dspr
    stop ambience
    
    scene ext_no_bus with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    sl "Семён, прощай!"
    stop ambience
    
    scene ext_camp_entrance_day with slideright
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day
    play music music_list["door_to_nightmare"]
    show sl angry pioneer with dspr
    sl "Зачем! Зачем вы его отпустили? С этим."
    show sl scared pioneer with dspr
    mt "Ну что ты, Славя, ведь он же вернётся."
    show sl scared pioneer close with dspr
    sl "Да, вернётся. Вы знаете, кто это? Это же… Это…"
    show sl surprise pioneer close with dspr 
    sl "Он точно вернётся, Ольга Дмитриевна?"
    mt "Да, через несколько дней."
    show sl normal pioneer close with dspr
    sl "Хорошо."
    hide sl with fade
    dreamgirl "Больше на эту тему Славя не говорила, а пионеры — те вообще к ужину почти забыли о Семёне."
    stop music fadeout 2
    dreamgirl "Ольге тоже хватало хлопот, и за пару дней беспокойство сменилось просто галочкой в памяти, что вот есть такой пионер по имени Семён, который подъедет чуть позже."
    stop ambience
    
    scene int_house_of_mt_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    dreamgirl "Ольге Дмитриевне хватало и своих забот. И главной заботой было продолжающееся ощущение постороннего взгляда."
    stop ambience
    
    scene int_house_of_mt_night2 with vpunch
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_day
    play music music_list["orchid"]
    th "И так каждую ночь. Хоть подселяй к себе кого-то из пионеров."
    th "Я отсюда неврастеничкой уеду. Кто-то изучает и анализирует меня. Чувства, мысли, мотивы поступков."
    th "Хочется запереться в шкафу. И заперлась бы, но это не поможет."
    th "Я опять не высплюсь. Опять сорвусь на пионерах. Как вчера на Сыроежкине."
    stop music fadeout 3
    stop ambience

    scene ext_playground_day with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_soccer_play_background
    mt "Что у тебя стряслось, Серёжа?"
    show d_sz normal pioneer at center with dspr:
        yalign 0.27
    d_sz "Вот, тётя Оля. Змей не летает."
    mt "Ну, со змеем я помочь тебе не смогу, но я знаю, кто тебе поможет. Пойдём."
    stop ambience
    
    scene ext_houses_day with slideleft:
        walking
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    play sound_loop dct_sfx_steps2
    show d_sz normal pioneer at left:
        yalign 0.27
    d_sz "Тётя Оля, а мы куда идём?"
    mt "Так. К одному изобретателю в гости."
    stop sound_loop
    stop ambience

    scene ext_clubs_day with squares
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_sz normal pioneer at center:
        yalign 0.27
    mt "Видишь, кружки открыты. Дуй к Сыроежкину и попроси его помочь. Только про то, что это я тебя привела, не говори."
    hide d_sz with dspr
    th "А я подожду."
    show blinking
    $ renpy.pause (1.5)
    th "Десять секунд."
    show blinking
    $ renpy.pause (1.5)
    th "Двадцать."
    show blinking
    $ renpy.pause (1.5)
    th "Тридцать."
    show d_sz normal pioneer at center with dspr:
        yalign 0.27
    d_sz "Тётя Оля, он говорит, что ему некогда."
    mt "Некогда… А что он делает?"
    d_sz "Я не знаю, тётя Оля. Просто сидит и приборы трогает. Я попросил его змея мне сделать, а он говорит, что некогда."
    mt "Ну пойдём, попробуем ещё раз."
    stop ambience
    
    scene int_clubs_male_day with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_clubs_inside_day
    dreamgirl "Сыроежкин и правда сидел и трогал приборы, а иногда вставал и трогал инструменты. Вид он при этом имел очень задумчивый."
    show el normal pioneer at right with moveinbottom
    el "Ольга Дмитриевна?"
    show d_sz normal pioneer at left with dspr:
        yalign 0.27
    show el angry pioneer with dspr
    el "Ольга Дмитриевна, я же уже объяснил Зайцу… то есть Сергею, что мне некогда."
    mt "Серёжа, я хотела попросить тебя сделать твоему тёзке змея. Но вижу, что ты очень занят. Поэтому я тебя попрошу о другом."
    show el surprise pioneer with dspr
    el "Да, Ольга Дмитриевна?"
    mt "Научи мальчиков делать воздушных змеев так, чтобы змеи не падали на землю, а мальчики тебя больше не отвлекали от важных дел."
    show el shocked pioneer with dspr
    el "Но, Ольга Дмитриевна. У меня же занятия, у меня же расписания, у меня же…"
    mt "Собственно, Серёжа, у тебя есть выбор. Соглашаешься?"
    el "Я? Ну. Да."
    mt "Или ты учишь мальчиков делать воздушных змеев. Или{w=2}… Или ты прямо сейчас пойдешь и скажешь Жене, что она тебе очень нравится."
    show el scared pioneer with dspr
    el "Но она{w=1}… Но я не{w=1}… Давай сюда эти обломки, Серёга. Посмотрим, что ты сделал не так."
    play sound dct_sfx_horn_rise_tape
    th "Ну и дурак!"
    show blink
    stop ambience
    
    scene int_house_of_mt_day with hpunch
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    th "Ну и дурак."
    th "А я всё-таки уснула и, кажется, выспалась."
    stop sound
    stop ambience
    
    scene ext_house_of_mt_day with dissolve
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    th "Оп-па. С возвращением."
    show d_sm normal pioneer at center with dissolve
    mt "Ну что стоишь как неродной?"
    me "Здравствуйте, Ольга Дмитриевна."
    mt "Ну как ты?"
    me "Я не понял. Привезли в какой-то академгородок, побеседовали со мной, извинились, сказали, что ошибка вышла, и вернули назад. Лучше расскажите, что тут без меня было. Я же столько дней потерял. Как в первый день после приезда уехал с этим, так только сейчас и вернулся. А скоро уже и смена закончится."
    stop ambience
    
    scene dct_int_briefing_room with pixellate
    $ prolog_time ()
    $ persistent.sprite_time ="day"
    play ambience ambience_int_cabin_day
    play music music_list["door_to_nightmare"]
    show d_ss normal sweater at left
    show d_bg angry suit at right
    d_gd "Явился? Забирай ключи и иди работай."
    d_ss "Добрая Глафира Денисовна. Тогда я пошёл. Работать. Увидимся…"
    d_gd "Подожди. Ты в Подвале давно был?"
    d_ss "В Центре управления? Да вот, когда его замуровывали. Это, получается, три года назад."
    d_gd "А Толя спустился вниз через памятник на этой неделе и не смог дальше первого уровня дорогу найти — всё время ходил кругами. Потом до него дошло, что это первый виток спирального коридора, только замкнутый в кольцо."
    d_gd "Эта тварь научилась играть с пространством, Семён, и создавать локальные вакуоли. А скоро научится пробивать проходы наружу."
    d_ss "Не надо меня успокаивать. Я и так всё понимаю."
    d_gd "А я не успокаиваю, Семён. Я просто очень не хочу проснуться однажды одной из ячеек коллективного разума. И то, что мы делаем с пионерами, всё равно лучше для пионеров, чем такая участь."
    d_gd "Можешь следующего активированного пионера взять в свою лабораторию и сам убедиться. Один-то пионер погоды не сделает. Только с одним условием: ты всё ему расскажешь."
    stop music fadeout 1
    stop ambience
    
    scene dct_int_chief_corridor_day with squares
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_ss normal sweater at cleft
    show d_to normal casual at cright
    d_to "Ты как, Семён Семёныч?"
    d_ss "Переживу. Бывало и больнее."
    d_to "Чтобы между нами было честно: обнулял его лично я. Минимальным импульсом. Так что есть большой шанс, что он очнётся циклов через пять. И тогда забирай его, как договорился с бабулей. Но это всё, что я могу для тебя сделать."
    d_ss "Расстрелял, но понарошку. Я не знаю, как к тебе относиться: спасибо сказать или по морде дать. Давай мы просто на глаза попадаться друг другу не будем."
    stop ambience
    
    scene ext_square_day with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    $ set_mode_nvl ()
    window show
    "И опять потекла смена, перевалив через экватор и неотвратимо двигаясь к своему окончанию."
    "Вот только... Семён больше не улыбался своей редкой и странно знакомой Ольге улыбкой."
    show sl scared pioneer with moveinright
    "И со Славей у него ничего не вышло. Или это у Слави с ним ничего не вышло? Неизвестно."
    $ set_mode_adv ()
    mt "Славя, ты плачешь?"
    show sl sad pioneer with dspr
    window auto
    sl "Нет, нет. Всё хорошо, Ольга Дмитриевна."
    hide sl with easeoutleft
    stop ambience
    
    scene int_dining_hall_day with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    th "Ну что — всё чисто, все столы протёрты, пол в зале вымыт и стулья расставлены. Осталось только похвалить."
    mt "Семён, молодец…"
    show d_sm scared pioneer at center with dissolve
    mt "Что-то случилось, Сём?"
    me "Понимаете, Ольга Дмитриевна. Такое чувство, что я потерял или забыл что-то очень важное. А не могу вспомнить — что."
    stop ambience

#########
#Часть 8#
#########

label dct_olga_p8:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 8."
    $ day_time()
    show headline_text2 u"Часть VIII" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_briefing_room with squares
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    show d_bg normal suit at right with dspr
    show d_to normal casual with dspr:
        ypos 0.05
    d_gd "Анатолий, что вы скажете о нашей вожатой? А то мне вон под отзыв целую страницу выделили. Надо что-то написать."
    d_to "Только хорошее пишите, плохое не пишите. Она за шесть недель превратила свой узел в настоящий лагерь с настоящими пионерами. Кто не знает, тот ничего и не поймёт. Приятно посмотреть на хорошую работу."
    show d_bg smile suit with dspr
    d_gd "А то, что она с вами поругалась?"
    d_to "Ну поругалась. Так ведь по делу поругалась, какие претензии? Хорошо, молодая она ещё. Я её где припугнул, где обманул, где убедил. А лет через десять она о таких, как мы, ноги вытирать будет."
    show d_bg angry suit with dspr
    d_gd "Не то. Спрошу по-другому: вы бы доверили ей своих детей?"
    d_to "Своих?! {w=1}Издеваетесь. Но{w=1}… да. Не задумываясь."
    show d_bg smile suit with dspr
    d_gd "Во-о-от."
    show d_bg normal suit with dspr
    d_gd "Значит, так и запишем — максимальный балл и ещё, сверх того, приказ на премию — заслужила; и запрет на работу у нас — бессрочный и на любой должности. В бухгалтерию я сама позвоню, а запрет — по вашей части."
    stop ambience

    scene ext_square_sunset with squares
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening
    play music a_v_to_the_crows
    th "Вот и всё. Завтрашний день ребятишки проведут без меня. Потом — пересменка, а дальше уже будет новая вожатая. Кто она, как она? Я ничего не знаю. Пусть мне и сказали, что это мой двойник, но верить обитателям посёлка я теперь не могу."
    show sl sad pioneer close at left with dspr
    sl "Ольга Дмитриевна, вы сейчас уедете и не вернётесь."
    show sl sad pioneer close at cleft with move
    mt "С чего ты взяла?"
    show sl serious pioneer close with dspr
    sl "Я чувствую."
    show sl smile pioneer close with dspr
    th "Мне совсем не хочется обманывать Славю."
    mt "Ты права. Но говорить всем об этом совсем не обязательно. Завтрашний день проживёте без меня — будешь за старшую. А послезавтра рано утром и смена закончится. Всё будет как всегда."
    stop ambience

    scene dct_ext_playground_sunset with dissolve
    $ sunset_time ()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_soccer_play_background
    show sl normal pioneer at left with dspr
    th "А мне осталось только обойти лагерь, подать из радиорубки сигнал отбоя, и можно идти к себе и собирать чемодан, чтобы в одиннадцать вечера оказаться на остановке."
    show sl smile pioneer with dspr
    sl "Ольга Дмитриевна, смотрите — мячик баскетбольный! Давайте…"
    hide sl with dspr
    dreamgirl "Девушки подобрали мяч на баскетбольной площадке, забытый кем-то из пионеров, забросили, каждая по разу, его в корзину."
    th "Славя могла бы стать моей лучшей подругой, но в нашем мире её не существует."
    mt "Ты только провожать меня не ходи, хорошо?"
    show sl sad pioneer at left with dspr
    sl "Если вы просите, то не буду, Ольга Дмитриевна."
    stop music fadeout 1
    stop ambience
    
    scene dct_ext_library_night_with_light with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_evening
    th "Свет горит, надо выключить."
    stop ambience
    
    scene dct_ext_library_night_with_light with dissolve:
        zoom 1.5 anchor (400,300)
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_evening
    show sl normal pioneer with dissolve
    sl "Не ходите, Ольга Дмитриевна. Там Женя. Всё ждет, что Серёжа решится."
    th "А Серёжа не решится. Он и в прошлую смену не решился, и в позапрошлую. Так и будет вечно вздыхать. А я уже ничего не смогу сделать."
    stop ambience
    
    scene dct_ext_houses_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_evening
    show d_sz normal pioneer at right with easeinright:
        yalign 0.27
    d_sz "Здравствуйте, тётя Оля."
    show d_oz normal pioneer at fright with easeinright:
        yalign 0.27
    d_oz "Привет, Славя."
    d_oz "Спокойной ночи."
    play sound sfx_slavya_run
    hide d_sz
    hide d_oz
    with easeoutleft
    th "Змея запускали."
    th "Что-то я смогла. В эту смену Электроник сам выловил своего тёзку, отвёл в кружок и заставил сделать нормально летающий аппарат."
    th "Хоть что-то останется после меня."
    stop ambience

    scene ext_square_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    show d_sm sad pioneer at left with dspr:
        zoom 0.8 ypos 0.1
    show sl normal pioneer close at fright with dspr
    sl "Семён! Хватит на площади околачиваться! Отбой через полчаса."
    me "Хорошо."
    hide d_sm with dissolve
    th "Вот моя неудача. Не могу себе простить. Пусть Анатолий и уверяет меня, что всё в порядке. А я тогда ещё надеялась здесь остаться и боялась давить на Анатолия. И теперь по лагерю ходит не Семён, а тень Семёна. Послушная, никогда не улыбающаяся, молчаливая тень."
    th "И между Семёном Семёновичем и Анатолием кошка пробежала. Как мне Семён Семёнович, как всегда непонятно, сказал:"
    stop ambience
    
    scene dct_ext_module_smoking_place with pixellate:
        zoom 1.3 anchor (400, 300)
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day
    show d_ss normal sweater at left with dspr
    d_ss "Я вот тоже сдался. Но мы оба ещё поднимемся. Я обещаю."
    stop ambience
    
    scene ext_square_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    th "Тоже сдался — это как я, что ли? Непонятно."
    mt "Лена, не засиживайся долго."
    show un surprise pioneer far with dissolve
    un "Да, Ольга Дмитриевна."
    hide un with dissolve
    th "Этим двоим, Лене с Алисой, я уделяла слишком мало внимания — это тоже запишем мне в пассив. И теперь одна прячется ото всех в книги, а вторая демонстративно ниспровергает мой авторитет."
    stop ambience
    
    scene dct_ext_musclub_night_lantern_light with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    play music music_list["dance_of_fireflies"]
    show mi surprise pioneer with dspr
    mi "Спокойной ночи, Славечка, Ольга Дмитриевна."
    show mi shy pioneer with dspr
    mi "Или, может, вы хотите музыку послушать?"
    show mi grin pioneer with dspr
    mi "Я с удовольствием вам поиграю, вот только, Олечкадмитриевна, вы же всегда так за распорядком следите…"
    mt "Поздно уже, Мику. А ты так здорово играешь, что если мы будем тебя слушать, то не сможем тебя остановить и просидим до утра."
    mt "А я же так слежу за распорядком. Спокойной ночи."
    show mi laugh pioneer with dspr
    $ renpy.pause (1)
    show mi smile pioneer with dspr
    mi "Спокойной ночи.{w=2} Ой, подождите, Олечкадмитриевна."
    hide mi with dspr
    show blinking
    $ renpy.pause (1)
    show mi shy pioneer behind blinking with dspr
    mi "Вот, возьмите, это для вас."
    show dct_cassete with dspr
    $ renpy.pause (1)
    hide mi with dspr
    hide dct_cassete with dspr
    dreamgirl "Ни Ольга, ни Славя не спросили, что там. Обе и так знали."
    mt "А хорошо вчера Мику спела."
    show sl normal pioneer close at fleft with dspr
    sl "Да, хорошо. Жаль, что раньше молчала."
    mt "Жаль, что раньше не собирались."
    stop music fadeout 1
    stop ambience

    scene dct_ext_musclub_night_light with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night
    dreamgirl "С Мику действительно получилось хорошо…"
    dreamgirl "Вчера, уже после отбоя, Ольга Дмитриевна обходила лагерь."
    th "Что за посиделки? Пионеры, сделайте так, чтобы мне не пришлось ругаться. Пожалуйста."
    stop ambience
    
    scene dct_int_musclub_night_light with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_music_club_night
    show sl normal pioneer with dspr
    sl "Здравствуйте, Ольга Дмитриевна. Не шумите, пожалуйста."
    hide sl
    show un normal pioneer at left
    with dspr
    th "Да здесь весь старший отряд! И ещё несколько малышей почему-то."
    hide un
    show d_sz normal pioneer at right:
        yalign 0.27
    with dspr
    th "Но никто не кричит: «Вожатка!», никто не дёргается к выходу."
    hide d_sz
    show mi smile pioneer
    with dspr
    mi "Заходите, Олечкадмитриевна, я так рада, что вы тоже пришли."
    th "Ладно старшие. В конце-концов, ничем предосудительным они не занимаются, но малышам-то давно спать пора!"
    hide mi with dspr
    th "Но мне совсем не хочется ругаться."
    stop ambience

    scene dct_int_musclub_night_light with fade
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_music_club_night
    dreamgirl "Это был не концерт, а разговор, беседа. Участвовали все, просто Мику, в отличие от остальных, не только разговаривала, а ещё и играла и пела. Но беседа закончилась, исчерпав себя, а Мику после финальной песни просто сказала:"
    show mi shy pioneer far with dspr
    mi "Ребята, спасибо, что пришли ко мне."
    show dv shy pioneer at fleft with dspr
    dv "Всегда пожалуйста. Ты только предупреждай заранее в следующий раз. Я тоже поиграть хочу."
    hide dv with dspr
    hide mi with dspr
    mt "Спасибо, Мику."
    mt "Пионеры, спокойной ночи. Мы с Мику сами кружок закроем."
    show un normal pioneer at fright with dspr
    un "Ольга Дмитриевна, а может, я помогу?"
    mt "Ничего, Лена. Мы справимся."
    th "Иди-иди. Ничего с твоей подружкой не случится, не собираюсь я её ругать."
    stop ambience

    scene dct_int_musclub_night_light with fade
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_music_club_night
    show mi normal pioneer with dspr
    mi "Понимаете, Олечкадмитиевна, у меня день рождения будет только через два месяца, когда мы все уже давно разъедемся, а я так хотела увидеть на нём ребят, что пригласила их сейчас."
    mt "Мику. Я никогда не слышала, как ты играешь. Почему? Только гаммы и распевки. И никто никогда не слышал. Я же вижу, что тебе нравится музыка, но когда я заходила к тебе в кружок, ты начинала очень много говорить и переставала играть даже гаммы."
    show mi shocked pioneer with dspr
    mi "Олечкадмитриевна, я не…"
    mi "Я не…"
    mi "Я…"
    $ renpy.pause (3)
    th "Кажется, я поломала девушку."
    show mi scared pioneer with dspr
    th "Кажется, я залезла туда, куда не надо."
    show mi scared pioneer close with dspr
    mt "Мику, если не хочешь — не отвечай. Я не настаиваю. Пошли уже спать, время за полночь."
    th "Эти девочки, старший отряд, всего-то на три года младше меня, а я вынуждена играть в наставницу."
    mi "Нет, Ольга Дмитриевна, я отвечу."
    mi "Я отвечу."
    mi "Я… Я очень люблю музыку, но я не могла…"
    mi "Понимаете, я хочу играть для тех, кто меня услышит, а пионеры — они бы не услышали, для них это были бы просто красивые звуки."
    mi "А для меня очень важно быть услышанной."
    mt "А теперь — услышали?"
    show mi happy pioneer close with dspr
    mi "А теперь — да. Да вы же сами всё видели."
    stop ambience

    scene ext_clubs_night with pixellate
    $ night_time ()
    $ persistent.sprite_time = "night"
    show sl sad pioneer close at fright with dspr
    play ambience ambience_camp_center_night
    sl "Серёжа уже ушёл, Ольга Дмитриевна. Вы сами откроете?"
    mt "Нет, Славя, открывай ты."
    stop ambience
    
    scene dct_int_radioroom_light with squares
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_night
    show sl sad pioneer close at center with dspr
    sl "Отбой, Ольга Дмитриевна?"
    mt "Да, отбой."
    play sound dct_sfx_horn_rebound_tape
    $ renpy.pause (3)
    mt "Кассету с сигналами оставляю тебе, Славя. И пошли уже домой."
    stop sound fadeout 3
    stop ambience

    scene ext_house_of_mt_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    show sl sad pioneer close at cright with dspr
    play ambience ambience_camp_center_night
    play music higekitekina
    sl "Вы знаете, что ту песню на кассете Мику сама перевела?"
    th "И это я тоже себе в заслугу поставлю. Ни в прошлую, ни в позапрошлую смену такого не было."
    mt "Нет. Но я догадалась. Я рада, что была у неё вожатой."
    mt "Нет, не так: я рада, что была у вас вожатой. Мне повезло с пионерами, спасибо вам за это."
    show sl tender pioneer close with dspr
    sl "Ольга Дмитриевна. Мы тоже рады, что вы были у нас вожатой, вы самая замечательная вожатая. Вот, возьмите: это от всех нас."
    sl "Мы хотели вам при отъезде подарить, но раз вы сейчас уезжаете — возьмите сейчас."
    hide sl with moveoutright
    play sound sfx_slavya_run
    dreamgirl "Славя вложила в руку вожатой маленький свёрток, неловко чмокнула ту в щеку и убежала к себе в домик."
    $ renpy.pause (3)
    stop music fadeout 1
    stop ambience
    stop sound
    
    scene int_house_of_mt_night with dissolve
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night
    th "Уложить чемодан, и можно ехать. Практика закончилась."
    th "Вот только…"
    show dct_mt_with_cassette_and_tie with squares
    extend " Всё, что у меня останется от этого лета — пионерский галстук с автографами мальчиков и девочек из лагеря, которого нет; и кассета с голосом девочки, которая никогда не рождалась."
    stop ambience
    play ambience ambience_int_cabin_night
    th "Кокоро но негаи, цутеки но мираи…"
    play sound_loop "<from 25.0 loop 0.0>mods/dublicate_completed/sounds/sfx/dct_sfx_mirabilis_futurum.ogg" fadein 0.5
    dreamgirl "В голове пронеслись знакомые слова на незнакомом языке.{w} Голос Мику звучал как наяву."
    dreamgirl "Вожатая не смогла сдержать слёз."
    hide dct_mt_with_cassette_and_tie with squares
    extend " Да, пока ещё вожатая."
    play sound sfx_clench2  #выключатель
    show int_house_of_mt_night2:
        alpha 0
        pause 0.2
        linear 0.2 alpha 1
    dreamgirl "Ольга последний раз щёлкнула выключателем, закрыла дверь, и отправилась на остановку."
    stop sound_loop fadeout 3
    show black with dissolve2
    $ renpy.pause (3)
    stop ambience

#########
#Часть 9#
#########

label dct_olga_p9:
    scene black with dissolve
    $ save_name = u"Дубликат. О — значит Ольга\nЧасть 9."
    $ day_time()
    show headline_text2 u"Часть IX" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene dct_int_bus_rain with squares
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_light_rain
    show d_to normal casual at center with dspr
    d_to "Уважаемые отъезжающие, просьба приготовить документы для проверки. Чтобы мне побыстрее разобраться, прошу документы подавать в раскрытом виде. Вам ехать, а мне ещё под дождём в модуль бежать."
    hide d_to with dspr
    dreamgirl "Заскрипели ворота. Оле было видно, как их закрывают двое солдат. Как водитель автобуса, не обращая внимания на погоду, торопливо курит, выскочив на улицу."
    dreamgirl "Как дежурный по КПП бежит в караулку, пряча от дождя список пассажиров с разрешающей визой Анатолия. Голубой с белыми ромашками зонт совершенно по-дурацки смотрелся в сочетании с военной формой, но дежурному было всё равно."
    dreamgirl "Дежурному важно было донести документ сухим и подшить его в папку, записав дату и номер списка к себе в журнал. Чтобы потом, когда-нибудь, если возникнет такая необходимость, любой проверяющий мог убедиться, что в дежурство этого прапорщика ни одна копия или микс не покидали посёлок через восточные ворота."
    dreamgirl "Разумеется, никого, кроме оригиналов, в этой вакуоли и не было, но порядок есть порядок."
    stop ambience
    
    scene dct_int_bus_rain with fade
    $ prolog_time ()
    $ persistent.sprite_time = "night"
    play ambience dct_ambience_light_rain
    play music music_list["a_promise_from_distant_days_v2"]
    show d_to normal casual at center with dspr
    d_to "Всё в порядке, проверка закончена. До свидания и счастливого пути."
    show d_to smile casual with dspr
    $ renpy.pause (1)
    show d_to normal casual with dspr
    $ renpy.pause (1)
    hide d_to with dspr
    queue sound [sfx_intro_bus_engine_start, sfx_intro_bus_transition, sfx_intro_bus_engine_loop]
    th "Кажется, Анатолий собирался что-то сказать, но промолчал. И это правильно, потому что говорить совершенно не о чем."
    th "Потому что я навсегда уезжаю из бесконечного лета."
    voice "Хорошо, что дождь — значит, в салоне пыли не будет."
    th "Сосед всё пытается завязать беседу. Лучше бы детектив свой читал."
    voice "Редко здесь такие дожди бывают. Всё либо жара, либо бури."
    th "Говорить не хочется совершенно."
    th "Грустно."
    th "А дождь редкий для этих мест. Мелкий, холодный и затяжной — совершенно осенний. Под стать настроению."
    voice "Вы слышали? Собрались НБО организовывать в пионерские лагеря. Как двадцать лет назад. Зачем?"
    th "Как там мои? В их тонких рубашечках."
    dreamgirl "Ольга не хотела думать о пионерах, но не получалось."
    show un shocked pioneer at center with pixellate:
        alpha 0.45
    th "Лена сейчас испуганно выглядывает из домика и вздрагивает от каждой попадающей на неё капли."
    hide un
    show mi normal pioneer at center with pixellate:
        alpha 0.45
    th "А ей в спину несётся бесконечный монолог Мику о том, как та любит дождь, но, конечно, не такой холодный."
    hide mi
    show dv normal pioneer2 at center with pixellate:
        alpha 0.45
    th "Алиса валяется на кровати, дымит сигаретой, кашляет при каждой затяжке и перебирает струны на гитаре."
    hide dv
    show el normal pioneer at center with pixellate:
        alpha 0.45
    th "Серёжа или у себя в кружке, или в библиотеке."
    hide el
    show d_sm scared pioneer at center with pixellate:
        alpha 0.45
    th "Семён… Семён безучастно уставился в стену. Что же с ним здесь сделали? А я себе не прощу теперь, что струсила и отдала его этим."
    hide d_sm
    show d_sz normal pioneer at cleft:
        alpha 0.45 yalign 0.27
    show d_oz normal pioneer at cright:
        alpha 0.45 yalign 0.27
    with pixellate
    th "Средние и младшие у себя в домиках дисциплинированно ждут сигнала на завтрак."
    hide d_sz
    hide d_oz
    show sl smile pioneer at center with pixellate:
        alpha 0.45
    th "И только Славя, наплевав на дождь, бегает из домика в домик и всем объявляет, что вожатую срочно вызвали в город, что сегодня Славя за старшую, что завтрак будет в девять ноль-ноль."
    th "Что сегодня из-за дождя вся программа отменяется. Что смена закончилась и сегодня последний день, а завтра утром на автобусе приедет вожатая и увезёт всех в райцентр."
    hide sl
    th "Вот только завтра для них начнётся просто новый цикл с новой вожатой. Остается только утешать себя, что я сделала всё, что могла; что завтрашняя, искусственная «Ольга Дмитриевна» сможет защитить их и чуть-чуть, но скрасит их жизнь."
    stop music fadeout 1
    stop ambience
    
    scene dct_olga_road with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience sfx_bus_loop fadein 2
    dreamgirl "В окне последний раз мелькнули ворота."
    dreamgirl "Асфальт сменился бетонкой, автобус наконец смог разогнаться и сейчас, чуть вздрагивая на стыках плит, катился по степи, подбираясь к границам вакуоли."
    dreamgirl "Как обычно, при приближении к зоне перехода начало темнеть, а пассажиров автобуса потянуло в сон. Человеческое сознание протестовало таким образом против невозможных, с его точки зрения, вещей."
    show blink
    dreamgirl "Пять, десять, пятнадцать минут, и в автобусе не осталось ни одного бодрствующего человека."
    dreamgirl "Уснул и надоедливый сосед, уснула и Ольга. Последним уснул водитель в своей экранированной кабине."
    stop ambience fadeout 1
    dreamgirl "Повинуясь автоматике, автобус плавно затормозил и остановился, тихо ворча двигателем, работающем на холостом ходу."
    
    scene int_dining_hall_day with pixellate
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_empty
    play music music_list["orchid"]
    show dct_dream_veil:
        shiver
    me "Ольга Дмитриевна."
    show d_sm normal pioneer behind dct_dream_veil with dissolve2:
        xcenter 0.33
    th "Это сон, да? Я же в автобусе сейчас?"
    mt "Семён?"
    hide d_sm
    show d_ss normal sweater at left behind dct_dream_veil
    with dissolve2
    th "А ведь в них есть что-то общее."
    th "Даже не в облике, а в характере."
    hide d_ss with dissolve2
    th "Почему я раньше о таком не подумала?"
    stop ambience
    
    scene int_house_of_mt_day
    show mt normal pioneer behind dct_dream_veil
    show dct_dream_veil:
        shiver
    with dissolve2
    $ day_time ()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day
    th "Это точно сон."
    mt "…"
    th "Сон."
    mt "…"
    th "Сон."
    hide mt with pixellate
    show blink
    $ renpy.pause (2)
    scene int_bus with dissolve2
    show mt smile pioneer at center with dspr:
        alpha 0.3
    mt "Когда маленькая девочка Оля проснётся в автобусе перед воротами, пусть она не рассчитывает на особые отношения с вожатой."
    stop music fadeout 1
    stop ambience
        
    scene dct_olga_road with pixellate
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience sfx_bus_loop fadein 2
    dreamgirl "Водитель проснулся минут через пятнадцать. Поёрзал на сиденье, включил передачу, и автобус опять покатил по шоссе как ни в чём не бывало."
    
    scene dct_ext_road_day_city with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    dreamgirl "Ещё через десять минут впереди замаячила промышленная окраина города. По одному начали просыпаться пассажиры."
    
    scene int_bus with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    th "Когда-нибудь маленькая девочка Оля проснётся в автобусе."
    th "Когда-нибудь… А сейчас надо просто жить: заполнить наконец дневник практики, получить полагающуюся зарплату. Надо просто жить до момента этого «когда-нибудь»."
    voice "А вы стихи любите?"
    th "Стихи."
    dreamgirl "Ольга Дмитриевна Миронова повернулась к соседу и, глядя ему в глаза, прочитала:"
    stop ambience
    
    scene black with dspr
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play music a_v_to_the_crows
    show poem_text u"Когда ты сам по себе,\nА вместо сердца — свинец." with dspr:
        pos (500, 200)
    pause
    show poem_text u"И вместо шелка — сума.\nИ та — изрядная рвань." as poem_text_2 with dspr:
        pos (500, 350)
    pause
    show poem_text u"Когда в труде и борьбе\nСгорело всё наконец." as poem_text_3 with dspr:
        pos (500, 500)
    pause
    show poem_text u"Надежда сводит с ума." as poem_text_4 with dspr:
        pos (500, 650)
    pause
    show poem_text u"Прекрасноглазая дрянь!" as poem_text_5 with dspr:
        pos (500, 725)
    pause
    
    scene int_bus with dissolve
    $ prolog_time ()
    $ persistent.sprite_time = "day"
    play ambience sfx_bus_loop fadein 1.5
    "И больше не раскрывала уже рта до самой остановки."
    window hide
    show black with dissolve
    stop music fadeout 1
    stop ambience fadeout 1
    
    pause 2

    
    $ night_time ()
    $ persistent.sprite_time = "night"
    play ambience ambience_int_cabin_night fadein 1
    $ set_mode_nvl ()
    window show
    scene int_house_of_mt_night with squares
    "Ольга Дмитриевна завершает вечерний обход лагеря, заходит к себе в домик, смотрит на спящего Семёна."
    "С облегчением улыбается: вот и ещё один день прошёл без происшествий."
    "Достаёт из шкафа запертую шкатулку, в которой среди барахла хранится старый засаленный ежедневник."
    "Раскрывает его и прочитывает несколько страниц."
    "Хочет дописать в конце пару строк, но вместо этого открывает первую страницу — ту, где обычно пишут дарственные надписи, и читает:"
    nvl clear
    window auto
    
    scene white with dissolve
    play music music_list["everlasting_summer"]
    $ set_mode_adv ()
    show wish_text u"Полюби их! О." at truecenter with dissolve2
    pause
    
    scene int_house_of_mt_night with squares
    $ night_time ()
    $ persistent.sprite_time = "night"
    $ set_mode_nvl ()
    "Сначала её лицо трогает слабая улыбка, а потом оно совершенно преображается, и перед нами оказывается не вздорная и ленивая «вожатка», а веселая, заводная и добрая двадцатилетняя девушка, которая сама недалеко ушла от своих пионеров."
    "Потом двадцатилетняя девушка исчезает, и опять возвращается двадцатипятилетняя Ольга Дмитриевна. Только добавилась россыпь морщинок у неё вокруг глаз, и улыбается она теперь понимающе, с сочувствием и чуть с иронией."
    "Вожатая дописывает нужные строчки, прячет ежедневник и укладывается спать."
    $ renpy.pause (1)
    nvl clear
    $ set_mode_adv ()
    stop music fadeout 3
    stop ambience
    
    scene black with blinds
    if dct_ending_var == True:
        return
    else:
        $ persistent.d_olga = d_olga + 1
        menu:
            "Конец восьмой части"
            "Продолжить":
                jump dct_coin
            "В меню":
                jump dct_mnu2    
