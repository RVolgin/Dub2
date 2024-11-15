label dct_dragon:
    scene black
    play music music_list["raindrops"]
    show headline_text u"Год дракона" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    show text(u"{size=48}{color=#ffdd7d}{i}Дождь. Опять. Всю ночь.\nДо самого утра.{/i}{/color}{/size}") at right with dspr
    $ renpy.pause(3.0)
    hide text with dissolve
    stop music fadeout 1
    $ save_name = u"Дубликат. Год дракона"
    
    scene int_bus_people_day with hpunch
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    $ set_mode_adv ()
    "Просыпаюсь как от толчка."
    "И сразу начинаю крутить головой."
    th "Доброе утро, Алиса. Где это я?"
    th "А, это же автобус, я же в лагерь еду!"
    play music i_tried_to_bring_it_back
    "Как-то я с приключениями сюда добиралась, но не вспоминается так, спросонья. Или это всё сон мне снился? Интересно, что за компания у меня на эти две недели будет?"
    "Рядом мелкая спит, года на два-три меня помладше. Тоже рыжая, как и я." 
    "Поселить её с собой в одном домике? Домик Рыжих будет. Что-то родственное в ней чувствую, надо будет, как проснётся, познакомиться с ней поближе."
    "Поднимаюсь на ноги и выглядываю в проход. Люди как люди." 
    "Вон девочка спит, на Ленку похожа."
    th "А хорошо бы… Нет, это невероятно, чтобы Ленка из Ленинграда сюда приехала."
    "Парней всего двое, и оба явные ботаники."
    "Так, ещё одна гитаристка, кроме меня. Интересно, как она с такими длинными волосами живёт? Да ещё и в такой цвет выкрасила. Ох, наживёт она тут проблем от администрации." 
    "Кто ещё есть интересный?" 
    "И тут меня толкают локтем в бок. Несильно, но бесцеремонно."
    stop music fadeout 1
    show us grin sport close at left with moveinleft
    us "Привет, Рыжая!"
    play music music_list["eat_some_trouble"]
    th "На себя посмотри."
    th "Я, конечно, рыжая, но нельзя же так сразу."
    dv "От рыжей слышу, а меня вообще-то Алиса зовут."
    stop music fadeout 3
    "Холодно смотрю на соседку."
    show us sad sport close with dissolve
    us "Ты что, Алиса, это же я, Ульяна…" 
    show us angry sport close with dissolve
    us "Ты что, всё забыла? Семёна помнишь? Бомбоубежище помнишь? Вечер в столовой помнишь?" 
    "Я только пожимаю плечами. О чём речь вообще?"
    show us fear sport close with dissolve
    us "Ну ничего, Алиса, я тебя в покое не оставлю, я заставлю тебя всё вспомнить!" 
    th "А вот сейчас соседка точно или заплачет, или поколотит меня. Что с ней такое?"
    "Я машинально сую руку в карман куртки. «Чья куртка? Откуда она на мне?». И нащупываю там свёрнутую бумажку." 
    "Записка, почему-то чертёжным шрифтом, очень уверенным почерком, как будто человеку привычно так писать: {i}«Алиса, а сильная отдача у арбалета?»{/i}."
    "И вторая строчка: {i}«Надо тебе дать пендель, чтоб проснулась. Если ты и так всё вспомнила, то поймёшь меня. Прощения не прошу»{/i}." 
    "Соседка что-то продолжает говорить, а я замираю и не слушаю её. Я вспоминаю!"
    th "Что-то с памятью твоей стало, Алиса. Даже дом родной не могу вспомнить. Ну давай, хотя бы день отъезда вспомни!"
    stop sound_loop
    

    scene dct_YOTD_neighbor_door_closed
    show dct_dream_veil at shiver
    with pixellate
    
    $ prolog_time()
    $ persistent.sprite_time = "day"
    $ set_mode_adv ()
    play music music_list["trapped_in_dreams"]
    "Квартира номер шесть."
    "Дверь, обитая старым, дышащим на ладан дерматином, кнопка звонка на уровне чуть выше пояса, чтобы внучке было удобно.{w} Вот только внучка эта давно выросла и уехала."
    play sound sfx_door_bell
    $ renpy.pause(1)
    stop sound
    "Слышу, как подходит хозяйка и без всяких «Кто там?» отпирает мне дверь."
    play sound sfx_open_door_1
    
    show dct_YOTD_neighbor_door_open behind dct_dream_veil
    show d_mp normal behind dct_dream_veil:
        zoom 0.85 xcenter 0.53 ycenter 0.68 matrixcolor TintMatrix("#D1E6F6")*BrightnessMatrix(value=-0.1)
    with dissolve
    dv "Здрасьте, Марьпетровна. Что ж вы не спрашиваете, кто пришёл?" 
    show d_mp smile with dspr
    d_mp "А зачем, Алисочка? Только ты одна так и звонишь. Как будто точку в конце предложения ставишь. Переночевать пришла? Заходи."
    show d_mp normal with dspr
    dv "Нет, я по другому делу. Я, Марьпетровна, неожиданно в пионерский лагерь уезжаю на две недели. Пусть мои вещи у вас полежат?"
    
    scene dct_int_mp_room
    show dct_dream_veil at shiver
    with pixellate
    "Потому что не хочется мне их в квартире оставлять. Маманя разных мужиков к себе водит. Раз в полгода новый «папа», и не каждый из «пап» безобидный тихий алкаш."
    "Вот уже, наверное, год, как я стала угадывать, что сейчас произойдёт или о чём меня спросят, как будто я уже проживала эту жизнь, как будто всё уже было. Вот и сейчас Мария Петровна запахнёт халат потуже и непонимающе посмотрит на меня, а я объясню, в чём дело."
    show d_mp shocked at cright behind dct_dream_veil with dissolve:
        ycenter 0.68
    dv "Самой смешно. Семнадцать лет и пионерский лагерь. Туда, оказывается, до восемнадцати ездить можно. У завучихи дочка должна была поехать, но заболела. Шампанское холодное на выпускном оказалось. Вот чтобы не пропала путёвка, я и поехала."
    show d_mp upset with dspr
    "Отдали мне путёвку, потому что путёвка в старший отряд. Иначе не увидела бы я её — рылом не вышла. Ну не хотят старшие в пионерский лагерь ездить: тебе семнадцать лет, а тебя в шортики или юбочку наряжают и заставляют под барабан строем ходить!"
    "Лагерь-то пионерский. Вот и не хотят. А вот я — я согласилась, были на то причины. И мы ещё посмотрим, кто там будет под барабан в красном галстуке маршировать. А я как знала, что мне путёвку предложат, когда утром мимо школы пошла и на крыльце завучиху встретила."
    "Я же говорю, стала угадывать то, что должно случиться."
    show d_mp sad with dspr
    d_mp "Понятно, Алисочка. Может, тогда чаю попьём на прощание? Мама-то дома? Знает, что ты уезжаешь?"
    "Вот не надо про мать. Хотя Марии Петровне можно."
    dv "Дома она, не проспалась ещё, ничего она не знает."
    show d_mp upset with dspr
    dv "Записку на столе для неё оставила — прочитает, если захочет. И вы простите, Марьпетровна, некогда мне чай пить, правда-правда. А то на поезд опоздаю."
    "Мария Петровна хочет сказать что-то ещё, но только показывает на угол прихожей."
    show d_mp normal with dspr
    d_mp "Ставь туда своё приданое, не пропадёт. Потом в кладовку уберу."
    hide d_mp with dissolve
    "Ставлю, куда показали, пакет с «приданым»: две пластинки, кое-какие документы, тетрадка со стихами и табами, золотая цепочка, письмо от Ленки — она, когда уезжала в Ленинград семь лет назад, письмо написала, я ей ответила на новый адрес, и всё, и закончилась переписка."
    "Вот и всё моё приданое. Остальное везу с собой: спортивная сумка с вещами и гитара в чехле."
    show d_mp smile at cright behind dct_dream_veil with dissolve:
        ycenter 0.68
    d_mp "Может, всё-таки попьёшь чаю-то?"
    dv "Марьпетровна, ну поезд же ждать не будет. А как приеду, так попьём обязательно. Я обещаю."
    show d_mp normal with dspr
    "Мария Петровна обнимает меня, я обнимаю её, даже слезинка подступила."
    "Что может быть общего у семнадцатилетней пацанки и семидесятидевятилетней бабушки, всю жизнь проработавшей (она говорит: прослужившей) на должности литературного редактора?"
    "Но вот уже пять — нет, шесть лет мы общаемся. Началось с того, что она, не вынеся моих издевательств над гитарой, взяла меня за руку и затащила к себе домой, чтобы: «Хоть три аккорда тебе показать, а то уши отваливаются!»."
    "Всякое бывало: и орали друг на друга, и ночевала я у неё, и скорую к ней вызывала, и в больницу к ней бегала, и она ко мне в больницу ходила… В больнице я всем врала, что мать работает, а ко мне бабушка ходит."
    dv "Марьпетровна, вы так прощаетесь со мной, будто я не на две недели, а навсегда уезжаю."
    show d_mp sad with dspr
    d_mp "Беги на поезд, Алисочка. Для меня и две недели могут «навсегда» оказаться. И ты через две недели уже другая приедешь."
    show dct_YOTD_entrance behind dct_dream_veil with pixellate
    "Меня выпроваживают и легонько выталкивают на площадку. Слышу сзади всхлип."
    dv "Марьпетровна…"
    stop music fadeout 1
    d_mp "Беги-беги. Может, ты и вовсе не приедешь."
        
    scene int_bus_people_day
    show us fear sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    $ set_mode_adv ()
    play sound_loop sfx_intro_bus_engine_loop
    th "О, что-то начала вспоминать, нормально."
    "Рыжая орёт на меня, но мне не до неё."
    th "Отстань, Мелкая. Я тебе в домике морду набью."
    stop sound_loop
    
    # scene black with pixellate
    # $ prolog_time()
    # $ persistent.sprite_time = "day"
    # $ set_mode_nvl ()
    # play music music_list["you_lost_me"]
    
    scene dct_YOTD_entrance
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    $ persistent.sprite_time = "day"
    play music music_list["you_lost_me"]
    
    "На меня последний раз пахнуло смесью запахов лекарств, герани, книг и каких-то духов. И дверь за моей спиной мягко закрылась."
    "Ну вот, с единственным взрослым, который что-то для меня значит, я попрощалась. Но что-то было неправильное в этом прощании, не должна она была говорить про то, что я не приеду."
    "Стою спиной к двери Марьи Петровны и шагнуть к выходу не могу, а вместо этого разглядываю наш подъезд: сантиметровый слой масляной краски на стенах и лестнице, стены зелёные, деревянная лестница — коричневая."
    "Ступеньки, за пятьдесят лет вышарканные жильцами так, что на них углубления от ног остались, отполированные руками жильцов широкие перила, по которым так удобно скатываться."
    "И везде — на штукатурке стен, на перилах, на дверях в подъезд — выцарапаны надписи. Каждое поколение детей считает нужным здесь отметиться, оставляя свои имена, а ЖЭК только красит поверх выцарапанного, так что надписи остаются видны."
    "Вон и две моих: «Алиса» и «Алиса+Лена», а к последней надписи Алик дописал «=дуры», за что потом от меня по шапке получил. Один раз за меня, один раз за Ленку…"
    "Что ж мне так идти-то не хочется? Может, вернуться и попить чаю у Марьи Петровны? Нет! Встряхиваюсь, поезд действительно ждать не будет."
    # nvl clear
    
    scene dct_YOTD_yard1:
        zoom 0.5
    show dct_dream_veil at shiver
    with pixellate
    "Вот и двор. Хороший двор, что бы там ни говорили. Самое главное, что чужих здесь не бывает. Две двухэтажки и одна трёхэтажка, стоящие буквой П, огораживают его с трёх сторон, а с четвёртой он закрыт от посторонних сараями."
    "Когда-то в них дрова хранились, а в шестидесятых, ещё до моего рождения, в дома газ провели. Газ провели, а сараи остались."
    "И теперь наш двор — это такой закрытый от посторонних мир: детская площадка у первого дома, перекладины для сушки белья у третьего, и аллея с двумя десятками старых тополей, которые все называют «парк», посередине."
    "Наши должны уже собраться у крайнего сарая."
    scene dct_YOTD_yard2:
        zoom 0.5
    show dct_dream_veil at shiver
    with pixellate
    "Так и есть, вон они сидят и дымят: четверо в карты режутся, Миха с мотоциклом ковыряется, Миха-большой на турнике повис. Венька, как обычно, чуть в стороне и в книжку уткнулся."
    "Портвейн ещё не доставали — ну правильно, светло ещё, незачем народ дразнить, а то 02 звонить начнут. Сейчас спросят, куда я собралась."
    "Здороваюсь и сразу прощаюсь. Попутно вытаскиваю изо рта у Веньки сигарету — рано ему ещё — и вставляю её себе в рот."
    "По тропинке между сараями и домом направляюсь к остановке.{w} Венька увязывается со мной."
    scene dct_ext_busstop_summer
    show dct_dream_veil at shiver
    with pixellate
    "И опять то ощущение, что что-то идёт не так: я думала, мне в чувствах признаваться будут, а Венька уговаривает меня не возвращаться домой после лагеря." 
    "А на остановке произносит «Прощай» вместо «Пока»."
    # $ set_mode_adv ()
    
    
    scene dct_int_liaz_day_rain
    show dct_dream_veil at shiver
    with pixellate
    d_dy "Следующая остановка — Вокзал!"
    stop music fadeout 1
    
    scene int_bus_people_day
    show us fear sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Почему мне кажется, что всё было не так? И тогда казалось, и сейчас."
    th "Почему я ехала на вокзал?"
    th "Мне нужно было в кассу, в окошко администратора. Показать путёвку в лагерь и забрать билет."
    th "Так, дальше что было? Вспоминай, Рыжая."
    stop sound_loop
    
    scene dct_int_corridor2
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    $ persistent.sprite_time = "day"

    play music music_list["goodbye_home_shores"]
    pause 0.4
    show d_vl normal coat at center behind dct_dream_veil with dissolve
    "В коридоре, ведущем к кассам, я натыкаюсь на дядьку."
    show d_vl normal coat:
        easein 0.5 xcenter 0.62
        pause 1.2
        ease 1 xcenter 0.38
        pause 1
        easeout 0.5 xcenter 0.5
        repeat
    "Я направо, и он направо, я налево, и он налево. И так несколько раз." 
    "Я помню, что колеблюсь: или обматерить его для начала, или сразу кастет доставать. Не люблю я таких дядечек с некоторых пор, не люблю аж до кастета, седина им в бороду."
    show d_vl smile coat at right with dissolve_fast
    "Но дядька только улыбается и дорогу уступает: иди, мол. А я сразу успокоилась, даже улыбнуться в ответ захотелось."
    d_dk "Проходите, барышня, а то до утра не разойдёмся. Вот только касса-то закрыта."
    "Дяденька окает, а я анекдот про окрестности Онежского озера сразу вспомнила. Мне, правда, самой захотелось улыбнуться в ответ, но я сдержалась."
    dv "Я слишком юна для тебя, дядя."
    show d_vl normal coat with dspr
    pause 0.4
    stop music fadeout 1
    
    scene int_bus_people_day
    show us fear sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Вот, вспомнила. Тогда я тоже почувствовала, что что-то не так: почему в тоннеле ни души, что это за дядька, почему закрыта круглосуточная касса?"
    "Ульяна, ты меня уже достаёшь."
    stop sound_loop
    
    scene dct_int_corridor2
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    $ persistent.sprite_time = "day"
    play music music_list["no_tresspassing"]
    "А касса и правда закрыта. Все пять окошечек, и в предбаннике никого. Только скучающий милиционер сидит на скамье и дремлет над газетой."
    "Сначала стучусь в окошко к администратору, не дождавшись ответа, начинаю стучать во все подряд."
    voice "Деточка, ты читать умеешь?"
    "Голос из-за спины. Милиционер проснулся."
    "А на окошечке записка, которой только что не было: {i}«Кассы закрыты до 9-00. Администрация»{/i}." 
    "Я поворачиваюсь к милиционеру, чтобы отлаять его за «деточку», а того уже нету. Только пожелтевший «Советский спорт» на скамейке лежит."
    stop music fadeout 1
    
    scene int_bus_people_day
    show us angry sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Мне было не по себе от этой чертовщины, а стало просто страшно. И я бросилась бежать."
    "Не помню, как я проскочила коридор. Просто, вот я стояла перед кассами, и вот я уже в зале. Кажется, мгновенно перенеслась."
    "Нет, через зал я только проскочила, прямо в буфет. Почему в буфет? Потому что там были люди. Представляете? Зал ожидания на вокзале пустой, и только в буфете кто-то есть." 
    th "Мне и сейчас страшно, а тогда, когда бежала от кассы, сама себя не помнила."
    "Мелкая вроде успокаиваться начала. Поселю с собой, точно. Но морду всё равно набью."
    stop sound_loop
    
    scene dct_int_cafe
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    $ persistent.sprite_time = "day"
    play music music_list["you_won_t_let_me_down"]
    play ambience ambience_dining_hall_empty
    "В буфете никого, только давешний дядька. Перед ним гора пирожков на тарелке, несколько бутылок с лимонадом и минералкой и начатый стакан с чаем."
    show dct_int_cafe_sunset_rain behind dct_dream_veil:
        alpha 0
        ease 2.5 alpha 1
    "В дополнение к моим страхам ещё и темнеет — откуда-то натянуло грозовые тучи, перекрывшие свет заходящего солнца. Жёлтые лампочки накаливания не могут до конца победить темноту, и в зале устанавливается полумрак." 
    "А я поняла, что во всём вокзале просто никого нет."
    "Никого, только дядька, я и стайка цыганок, испуганно жмущихся в тамбуре и не решающихся выйти на привокзальную площадь под ливень, который вот-вот начнётся."
    
    show d_vl normal coat at right behind dct_dream_veil with dissolve:
        ypos 0.2 matrixcolor TintMatrix("#EFD0FF")   # Перекраска спрайта через преобразование matrixcolor. Свойство TintMatrix с цветом "#EFD0FF" даёт результат идентичный вечерним спрайтам
    
    d_dk "Сейчас ливанёт. Садись, перекусишь перед дорогой, я и на тебя взял."
    "Я, чтобы не показывать свой страх, начинаю наступать на дядьку."
    dv "Ты! Что всё это значит? Это ты всё устроил!"
    show d_vl smile coat with dspr
    d_dk "Что устроил?"
    "Дядька, улыбаясь, смотрит на меня снизу вверх."
    d_dk "Ты зачем к кассам попёрлась? Тебе что было сказано? «Автобус на привокзальной площади»."
    show d_vl normal coat with dspr
    d_dk "Ох уж эти …"
    "Тут дядька произносит непонятное слово."
    d_dk "Вечно всё путают и забывают. Да ты кушай." 
    "Дядя меняет тему, пододвинув ко мне тарелку с пирожками и бутылку с лимонадом."
    d_dk "Или как хочешь, девчонки съедят. Вон они, уже бегут. Славяна — та точно не откажется."
    stop ambience
    stop music fadeout 1
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Что-то тогда зашевелилось у меня в памяти в ответ на имя «Славяна», но успокоилось."
    stop sound_loop
    
    $ prolog_time()
    scene dct_int_cafe_sunset_rain
    show d_vl normal coat at right:
        ypos 0.2 matrixcolor TintMatrix("#EFD0FF")
    show dct_dream_veil at shiver
    with pixellate
    play ambience ambience_dining_hall_empty
    play sound dct_sfx_discharge
    "За окном загрохотало; тут же, как по приглашению, в буфет забегают две девушки, примерно мои ровесницы, только вот не моего круга."
    show d_mi smile casual behind dct_dream_veil:
        xcenter 0.25 matrixcolor TintMatrix("#EFD0FF")
    show d_sl smile dress behind dct_dream_veil:
        xcenter 0.45 ycenter 0.833 matrixcolor TintMatrix("#EFD0FF")
    with easeinleft
    d_dk "Не смотри на них так, Алиса."
    stop sound
    stop ambience
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Дядька тогда назвал меня по имени, но вот это меня почему-то совсем не напугало."
    "А Мелкая киснет. Да что с ней такое?"
    stop sound_loop
    

    $ prolog_time()
    scene dct_int_cafe_sunset_rain
    show d_vl normal coat at right:
        ypos 0.2 matrixcolor TintMatrix("#EFD0FF")
    show d_mi smile casual:
        xcenter 0.25 matrixcolor TintMatrix("#EFD0FF")
    show d_sl smile dress:
        xcenter 0.45 ycenter 0.833 matrixcolor TintMatrix("#EFD0FF")
    show dct_dream_veil at shiver
    with pixellate
    play music music_list["drown"]
    play ambience ambience_dining_hall_empty
    d_dk "С ЭТИМИ девушками ты не знакома. Позволь официально представить тебе моих подруг по несчастью: Мику Хатсуне и Славяну Феоктистову. Девочки, это Алиса Двачевская, которая вот-вот окончательно проснётся и покинет нас надолго, если не навсегда. Ну это вы знаете, иначе нас бы сюда не выкинуло."
    hide d_vl
    hide d_mi
    hide d_sl
    with dissolve
    pause 0.7
    show d_mi smile casual behind dct_dream_veil:
        xcenter 0.4 ycenter 0.68 matrixcolor TintMatrix("#EFD0FF")
    show d_vl normal coat behind dct_dream_veil:
        xcenter 0.62 ypos 0.2 matrixcolor TintMatrix("#EFD0FF")
    show d_sl smile dress behind dct_dream_veil:
        xcenter 0.84 ycenter 1.033 matrixcolor TintMatrix("#EFD0FF")
    with dissolve
    mi "Здравствуйте, дядя Валера."
    "Тут иностранка обращает на меня внимание."
    show d_mi grin casual
    show d_sl normal dress
    with dspr
    mi "Здравствуй, меня зовут Мику, Мику Хатсуне. Мику это имя, а Хатсуне это фамилия. Это японские имя и фамилия, потому что мама у меня…"
    show d_mi sad casual with dspr
    "И тут Мику вздрагивает, шепчет что-то вроде: «Никак не отвыкну», и внезапно замолкает, отвернувшись."
    show d_sl smile dress with dspr
    d_sl "Еле спаслись от дождя, дядя Валера!"
    stop ambience
    stop music fadeout 1
    
    scene int_bus_people_day
    show us cry sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "И опять. Мне тогда показалось, что имя «Мику» и эта манера тараторить мне знакома."
    th "Может быть, это всё-таки мне сон приснился, пока мы ехали?"
    "Ну, Мелкая, ну нельзя же так. Ну обозналась ты, ну бывает."
    stop sound_loop
    
    scene dct_int_cafe_sunset_rain
    show d_mi sad casual behind dct_dream_veil:
        xcenter 0.4 ycenter 0.68 matrixcolor TintMatrix("#EFD0FF")
    show d_vl normal coat behind dct_dream_veil:
        xcenter 0.62 ypos 0.2 matrixcolor TintMatrix("#EFD0FF")
    show d_sl smile dress behind dct_dream_veil:
        xcenter 0.84 ycenter 1.033 matrixcolor TintMatrix("#EFD0FF")
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    play music music_list["trapped_in_dreams"]
    play ambience ambience_dining_hall_empty
    pause 0.5
    show d_mi smile casual with dspr
    "Девочки делят между собой пирожки и жадно накидываются на еду, при этом иностранка не отстаёт от колхозницы." 
    "Или у них у всех стальные желудки, или они самоубийцы. Что-то брать в вокзальном буфете."
    "Пока они едят и переговариваются о чём-то своём, я пью лимонад, закусывая его своим личным печеньем из сумки (надеюсь, лимонад безопасный), и разглядываю всех троих."
    show d_mi normal casual with dissolve_fast
    mi "Дядя Валера." 
    "Я ожидала бесконечного потока слов от Мику, а она неожиданно меня обманула." 
    mi "Зачем вы так? Я понимаю, что вам нужно объяснить Алисе, почему мы трое вместе, но я себя несчастной не считаю, Славяна тоже. Да и вы тоже, не прибедняйтесь."
    "Вижу, что дядька отвлёкся от тарелки, и спрашиваю:"
    dv "И где же ваш автобус?"
    stop ambience
    stop music fadeout 1
    
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Это всё-таки был сон. В жизни я бы их всех послала, но во сне — почему бы и не поддержать разговор?"
    stop sound_loop
    
    scene dct_int_cafe_sunset_rain
    show d_mi normal casual behind dct_dream_veil:
        xcenter 0.4 ycenter 0.68 matrixcolor TintMatrix("#EFD0FF")
    show d_vl normal coat behind dct_dream_veil:
        xcenter 0.62 ypos 0.2 matrixcolor TintMatrix("#EFD0FF")
    show d_sl smile dress behind dct_dream_veil:
        xcenter 0.84 ycenter 1.033 matrixcolor TintMatrix("#EFD0FF")
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    show dct_dream_veil at shiver
    play music music_list["dance_of_fireflies"]
    play ambience ambience_dining_hall_empty
    d_dk "Как всегда, на той стороне площади."
    "Дядька пожимает плечами так, будто я у него спросила, какого цвета трава."
    show d_sl normal dress with dspr
    d_sl "Дядь Валера, она же спит ещё, она же место не может выбирать, ты ей хоть наводку дай какую. Где этот автобус, как на него сесть?"
    show d_vl smile coat with dspr
    d_dk "Не ты нОходишь четырестОдесятый Овтобус, а четырестОдесятый Овтобус нОходит тебя!"
    "Дядька окает совсем уж преувеличенно. И ещё поднимает блестящий от пирожкового жира указательный палец кверху, чем портит всё впечатление." 
    show d_vl normal coat with dspr
    "Славяна ждёт продолжения, но дядя Валера опять занялся пирожками и замолк; тогда Славяна берёт инициативу в свои руки."
    show d_sl smile dress with dspr
    d_sl "Понимаешь, Алиса. Дядя Валера и есть водитель того самого автобуса." 
    "А дядя Валера, я уже мысленно так его называю, кивает в подтверждение."
    show d_vl serious coat with dspr
    d_vl "Точно, и автобус, между прочим, уже час тебя дожидается. Какого … ты на вокзал попёрлась?"
    "И оканье его куда-то пропало."
    stop ambience
    stop music fadeout 1
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "А я совсем запуталась и потерялась между сном и воспоминаньями. И реальным кажутся только этот Икарус, соседка и пионерский лагерь, куда мы едем."
    "Хорошо хоть Мелкая реветь перестала."
    stop sound_loop
    
    scene dct_int_cafe_sunset_rain
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    play ambience ambience_dining_hall_empty
    "А эти трое расправились с пирожками, Мику относит тарелку на мойку (за все время ни буфетчица так и не появилась, ни посетителей никого не было), и мы, обогнув цыганок, выходим на привокзальную площадь."
    stop ambience
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Дальнейшие события опять вспоминаются кусками."
    stop sound_loop
    
    scene dct_ext_city_scuare_sunset
    show d_vl normal coat:
        xcenter 0.32 matrixcolor TintMatrix("#A1C9D0")  # Перекраска спрайта через преобразование matrixcolor. Свойство TintMatrix с цветом "#A1C9D0" даёт результат почти идентичный ночным спрайтам
    show d_mi smile casual at cright:
        xcenter 0.87 matrixcolor TintMatrix("#A1C9D0")
    show d_sl smile dress at right:
        xcenter 0.67 ycenter 0.833 matrixcolor TintMatrix("#A1C9D0")
    show dct_overcast_rain_1
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    play music twinkling
    "Вот девочки прячутся под зонтиками, потому что ливень хоть и закончился и небо почти очистилось, но мелкий дождик ещё идёт, а дядя Валера снимает с себя кожаную куртку и накидывает мне на плечи, оставаясь в одной рубашке."
    show d_vl normal with dissolve_fast    
    dv "Дядя Валера, не надо, сами же промокнете."
    "Я сопротивляюсь, а он только отмахивается."
    show d_vl smile with dspr    
    d_vl "Алиска, фантомы не болеют."
    show d_vl normal with dspr    
    "От куртки слабо пахнет машинным маслом, бензином и табаком." 
    show d_vl serious with dspr    
    "На мгновение мы встречаемся взглядами, и я вижу… тоску и что-то ещё, даже не могу описать, что. Я не Достоевский, чтобы описывать." 
    "Дядя Валера извлекает из кармана куртки пачку сигарет и ключи от автобуса, закуривает, и контакт теряется."
    show d_vl normal with dspr 
    "Но мне вдруг захотелось, чтобы тоски в глубине его карих глаз поубавилось. А ещё жалею, что маман в своих попытках устроить личную жизнь скатывалась всё ниже и ниже, не встретив вот такого дядю Валеру."
    "Я ещё хочу спросить про то, что за фантомы он поминал, но забываю."
    show black with dissolve_fast
    pause 0.5
    hide black with dissolve_fast
    "Вот мы идём по улице, Славяна оглядывается."
    show d_sl surprise dress with dissolve_fast
    d_sl "Идут за нами."
    show d_sl smile dress with dissolve_fast
    "Тут уже оглядываюсь я. Всё те же цыганки, что стояли в тамбуре вокзала, идут за нами метрах в пятидесяти, не отставая и не догоняя."
    show d_vl smile with dspr
    d_vl "Я же говорил, что так и таскаются за мной от сна к сну. Где я их подцепил — ума не приложу."
    stop music fadeout 1
    
    scene int_bus_people_day
    show us sad sport close at fleft
    with pixellate
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound_loop sfx_intro_bus_engine_loop
    th "Значит, это всё-таки сон."
    th "Да, я помню, тогда же и подумала, что подольше бы не просыпаться. А то проснёшься, а там беспутная маман и взрослая жизнь в общаге ткацкой фабрики."
    th "И это, Ульяна, не дуйся ты так. Я тебя даже бить передумала."
    stop sound_loop

    scene dct_ext_city_scuare_sunset
    show dct_dream_veil at shiver
    show d_vl normal:
        zoom 0.75 xcenter 0.22 yalign 1.005 matrixcolor TintMatrix("#A1C9D0")
    show d_sl normal dress at cleft:
        zoom 0.75 xcenter 0.4 matrixcolor TintMatrix("#A1C9D0")
    show dct_overcast_rain_1
    show d_mi serious casual at cright:
        zoom 1.25 xcenter 0.7 ypos -0.03 matrixcolor TintMatrix("#A1C9D0")
    with pixellate
    $ prolog_time()
    play music higekitekina
    "Вот Славяна с дядей Валерой вырвались вперёд. И мы идём плечом к плечу с Мику."
    mi "Знаешь, Алисочка. Я хотела, пока мы были под крышей, попросить у тебя подержать гитару, а то так поиграть хочется, что пальцы болят."
    "И вдруг, без перехода, Мику резко меняет тему."
    show d_mi angry casual with dissolve
    mi "Я тебя ненавижу, Алиса. За Сенечку. Ты убила его."
    "А голос спокойный и бесцветный какой-то."
    "Я ничего не понимаю и только пожимаю плечами. Кто такой Сенечка? А Мику продолжает, Мику почему-то надо выговориться."
    mi "Хорошо, что всё обошлось. Потому что иначе… Меня нельзя убить, я остаточный фантом, но случилось бы что-то нехорошее. Молчи, Алисочка. Просто молчи. Ты убила его, и теперь за тобой долг." 
    mi "Ты мне его никогда не выплатишь, а я никогда не буду с тебя его требовать. Просто помни о нём. Я не сумасшедшая, я знаю, что ты не виновата и сейчас ничего не помнишь и не понимаешь, о чём речь, и в лагере мои слова забудешь. Но я тебя ненавижу."
    th "Ну молчи так молчи. Я и молчу."
    
    show d_mi cry casual far behind d_vl with dissolve:
        zoom 0.657 xcenter 0.07 ycenter 0.65
    show d_vl serious:
    show d_sl surprise dress:
    with dissolve_fast
    "Вот Мику убежала вперёд всех, чтобы мы не видели, как она плачет."
    show d_vl serious:
        linear 0.5 alpha 0
    show d_sl surprise dress:
        linear 0.5 alpha 0
    show d_mi cry casual far:
        linear 0.5 alpha 0
    extend " Вот дядя Валера догнал её, чтобы она не плакала в одиночестве.{nw}"    # Обрываем реплику тегом {nw}, чтобы показать спрайты персонажей
    show dct_overcast_rain_1 behind d_sl
    show d_sl normal dress close:
        zoom 1.0 xcenter 0.4 ycenter 0.5
        linear 0.5 alpha 1
    "{cps=0}Вот Мику убежала вперёд всех, чтобы мы не видели, как она плачет. Вот дядя Валера догнал её, чтобы она не плакала в одиночестве. {/cps}А я оказалась вдвоём со Славяной."   # Вставляем дубль предыдущей реплики внутри тега {cps=0} {/cps}, чтобы она появлялась мгновенно. Тем самым создаётся впечатление, что это единая плавно текущая реплика, а спрайтs появляются посреди неё.
    dv "Вы тоже в лагерь?"
    show d_sl serious dress close with dspr
    d_sl "Нет! Нам нельзя. Мы всего лишь остаточные фантомы! И не спрашивай об этом больше никогда!"
    th "Ещё одна сумасшедшая."
    dv "А дядя Валера — он тоже фантом?"
    "Чтобы не беспокоить Славяну, спрашиваю я."
    show d_sl sad dress close with dissolve_fast
    d_sl "Почти. Дядя Валера — он застрял на полпути. Он говорит, что в его институте случилась авария и три человека-оригинала пострадало. Слишком поздно решились на запись подлинников, двоих успели переписать, а он умер в процессе записи. Поэтому для него у вас нет тела."
    "Произносится всё это спокойно и как-то грустно, как будто о каком-то давнем несчастье рассказывают, так что я даже не знаю, как к этому относиться. Конечно, это бред, но вдруг я что-то не знаю и не понимаю? И где это — У НАС?"
    stop music fadeout 1
    
    scene dct_ext_410bus
    show dct_overcast_rain_1
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    
    play music adaytoremember
    "Вот мы стоим на проезжей части перед автобусом. Мику вдруг обнимает меня."
    show d_mi cry casual behind dct_dream_veil with dissolve:
        zoom 1.25 xcenter 0.62 matrixcolor TintMatrix("#A1C9D0")
    mi "Прости меня, Алисочка. Забудь, что я тебе наговорила."
    hide d_mi
    show d_sl tender dress close behind dct_dream_veil:
        xcenter 0.38 matrixcolor TintMatrix("#A1C9D0")
    with dissolve
    "Следом Славяна."
    d_sl "Прощай, Алиса. Передай Семёну, что он…{w=0.5} Что его…{w=0.3} Ничего ему не передавай. Забудь."
    hide d_sl with dissolve
    show d_vl normal behind dct_overcast_rain_1 at center:
        alpha 0 matrixcolor TintMatrix("#A1C9D0")
        pause 1
        linear 1 alpha 1
    "Тут автобус заводится, хлопает водительская дверь, и из кабины выходит дядя Валера."
    d_vl "Всё, по машинам, Алиса. До встречи, девочки."
    "Славяна и Мику отходят на тротуар, я порываюсь стянуть с себя куртку, но дядя Валера меня останавливает."
    d_vl "Потом, Алиса. Всё, поехали."
    "И засовывает что-то в карман куртки."
    show d_vl smile
    show d_mi cry_smile casual behind dct_overcast_rain_1:
        xcenter 0.65 matrixcolor TintMatrix("#A1C9D0")
    show d_sl tender dress behind dct_overcast_rain_1:
        xcenter 0.35 ycenter 0.833 matrixcolor TintMatrix("#A1C9D0")
    with dissolve
    show dct_overcast_rain_2:
        alpha 0
        pause 1
        linear 1.5 alpha 1
    show d_vl smile:
        alpha 1
        pause 2
        linear 1 alpha 0
    "Я забираюсь в салон, вижу, как дядя Валера коротко обнимает девочек и бежит в кабину под снова усиливающимся дождём. Что-то скрежещет под полом, и мы трогаемся."
    
    scene dct_buswindov_rain
    show dct_dream_veil at shiver
    with pixellate
    $ prolog_time()
    "Уже стемнело, мы не торопясь едем по городу сквозь дождь, останавливаясь на редких светофорах."
    "Окна запотели, и я время от времени смахиваю лишнюю влагу со стекла ребром ладони. По ногам потянуло тёплым воздухом — заработала печка."
    "Становится очень уютно, я поплотнее заворачиваюсь в куртку, вытягиваю ноги и прижимаюсь виском к прохладному стеклу, глядя на пробегающие за окном дома." 
    "Дядя Валера включает музыку, что-то хорошее и незнакомое, и я кричу во всё горло, чтобы он отмотал на начало и сделал погромче."
    "Какое-то время ещё пытаюсь понять, почему на имя «Семён» что-то откликается внутри меня. Никого же не знаю и не помню, чтобы человека так звали."
    stop music fadeout 1

    scene int_bus_people_day
    show us sad sport close at fleft
    with hpunch
    $ day_time()
    $ persistent.sprite_time = "day"
    play music anewbeginning
    "Записка тает у меня в руках, а я вспоминаю: наконечник стрелы и спина, обтянутая пионерской рубашкой."
    "Вот я плавно тяну спуск, вот арбалет вздрагивает, и в этот момент Ульяна толкает меня. А я вижу, как стрела входит между лопатками Семёна." 
    "Семён?" 
    "Ульяна?"
    hide us
    show us sad sport close at center
    with dissolve
    dv "Улька!" 
    "Кричу так, что те в автобусе, кто ещё не проснулся, просыпаются, а те, кто уже проснулся, вздрагивают и оглядываются."
    "Я обнимаю Ульяну и начинаю плакать."


    scene black with blinds
    $ renpy.pause(3.0)
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    $ persistent.d_dra = d_dra + 1
    
menu:
    "Конец книги «Год дракона»"
    "Продолжить":
        jump dct_clouds
    "К оглавлению":
        jump dct_mnu2    
