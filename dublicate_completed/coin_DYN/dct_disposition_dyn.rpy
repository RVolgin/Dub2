    ######################
    #Глава 4. Расстановка#
    ######################


label dct_disposition_dyn:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Расстановка\n(dynamic)"
    $ day_time()
    $ persistent.sprite_time = "day"
    scene black
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
        zoom 1.2 align (0.0, 0.9)   # Зум, чтобы не показывать дверцу шкафа с чертежом авиамодели
    show sh normal pioneer at right:
        ycenter 0.53                # Чуть приспущенный Шурик, чтобы вписываться в интерьер
    show dct_dream_veil at shiver
    with dissolve
    "Помочь Шурику в разработке принципиальной схемы. Помочь - значит в основном не мешать и слушать рассуждения Шурика, но пару раз тот похвалил Сергея за дельные мысли."
    scene bg int_musclub_day
    show mi normal pioneer
    show dct_dream_veil at shiver
    with dissolve
    "Выпросить в музыкальном кружке вращающийся стул."
    show mi shocked pioneer with dissolve_fast
    mi "Серёженька, а вам зачем? Как интересно!{nw}"    # Обрываем реплику тегом {nw}, чтобы сменить спрайт Мику
    show mi smile pioneer as mi2 at center behind dct_dream_veil:
        alpha 0
        linear 0.5 alpha 1
    show mi shocked pioneer:
        linear 0.5 alpha 0
    mi "{cps=0}Серёженька, а вам зачем? Как интересно! {/cps}Сереженька, только обязательно позовите меня на испытания! Я хочу стать подопытным кроликом! Слышишь? Ты обещал!"  # Вставляем дубль предыдущей реплики внутри тега {cps=0} {/cps}, чтобы она появлялась мгновенно. Тем самым создаётся впечатление, что это единая плавно текущая реплика, а спрайт меняется посреди неё.
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
    window hide

    # Рандомные лагерные места сменяют друг друга
    show dct_camp_hustle_to_the_left1 behind dct_dream_veil
    $ renpy.pause(1.45,hard=True)
    show dct_camp_hustle_to_the_left2 behind dct_dream_veil
    $ renpy.pause(1.45,hard=True)
    show dct_camp_hustle_to_the_left3 behind dct_dream_veil
    $ renpy.pause(1.45,hard=True)
    show dct_camp_hustle_to_the_left4 behind dct_dream_veil
    window auto
    "До самого обеда Электроник с поражающей окружающих энергией носился по лагерю в поисках материалов; пилил, клепал, паял; прессовал из мела и сухих белил, а сначала надо было придумать, как и чем прессовать, а потом обжигал керамические таблетки излучателя."
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
    "Очень хотелось подойти, отодвинуть эту проклятую книгу и заглянуть заведующей библиотекой в глаза.{w} Спросить: «Женька, ты что творишь? Со мной и с собой? С нами».{w} Но не хватало смелости."
    th "А вдруг она не врёт?"
    extend " Вдруг я действительно неинтересен?"
    "Сергей вздыхал и возвращался к своим журналам."
    pause 0.3
    show d_mz smile pioneer glasses far with dspr
    pause 0.3
    show d_mz normal pioneer glasses far with dissolve_fast
    "Женя выныривала из-за книги и опять начинала гипнотизировать Сыроежкину спину, пока тот не убегал в кружок с очередной порцией знаний."
    
    scene bg int_clubs_male_day with dissolve:
        zoom 1.2 align (0.0, 0.5)
    stop music fadeout 8
    play ambience ambience_clubs_inside_day fadein 4
    "Наконец ближе к обеду сегодняшняя порция работы закончилась. Печатные платы травились в растворе, и оставаться им там следовало до вечера; двадцать керамических излучателей остывали вместе с муфельной печью — нужно четыре штуки, но хорошо если каждый третий заработает как надо."
    #show el normal pioneer close at fleft with dissolve
    "Принципиальная схема на листе оранжевой миллиметровки была пришпилена к дверце шкафа поверх чертежа авиамодели; горка деталей, извлечённых из ящика и выпаянных из некондиционных плат, лежала на втором листе миллиметровки, и сейчас Шурик, прозванивая, раскладывал их по кучкам: резисторы отдельно, транзисторы отдельно и так далее."
    scene dct_int_clubs_male2_night_zoom
    show sh normal pioneer close at right
    with dissolve
    sh "Сергей, на сегодня, наверное, всё. Вечером я приду, платы из раствора достану и промою."
    show sh normal_smile pioneer close with dissolve_fast
    "Шурик покачал рукой каркас установки, похожий на сегмент Шуховской башни, одобрительно кивнул и, подтверждая собственные слова, повторил:"
    sh "На сегодня всё. Ты свободен, а я детали рассортирую до конца и тоже пойду."
    scene bg int_clubs_male_day:
        zoom 1.2 align (0.0, 0.5)
    show d_el think2 pioneer close as el at fleft
    with dissolve
    th "И правда, по плану сегодня действительно делать больше нечего."
    show el smile pioneer close at fleft with dspr
    el "Шурик, а может, я сам деталями займусь?"
    sh "Нет, иди-иди, а то мне ещё подумать надо."
    show el grin pioneer close with dspr
    el "Хорошо. Я на обед зайду за тобой."
    sh "Да, спасибо.{w=0.4} Пока."
    show el smile pioneer close with dspr:
        pause 1
        linear 0.8 alpha 0
    th "Подумать — это святое. Нельзя никого отвлекать, когда он думает."
    stop ambience fadeout 1
    play sound_loop ambience_camp_center_day fadein 1
    play sound [ "<silence 0.4>", sfx_close_door_1 ]
    scene ext_clubs_day:
    show 3500_el normal pioneer:
        zoom .17 anchor (.5, 1.0) pos (.48, .71)
    with slideawayup
    th "В библиотеку?{w} Сейчас, когда голова на время освободилась от забот, очень захотелось увидеть Женю."
    hide 3500_el with dissolve
    th "Я только возьму что-нибудь почитать." 
    scene bg ext_library_day
    show el surprise pioneer far at cright
    with pushleft
    show el scared pioneer far with dspr
    th "А вдруг она о чём-нибудь меня спросит?"
    show el laugh pioneer far with dissolve_fast
    extend " Придумаю что-нибудь."
    stop sound_loop fadeout 1
    
    
    play ambience ambience_library_day
    play sound sfx_open_door_clubs_2
    scene bg int_library_day with slidedown
    "Не спросила."
    show d_ma normal pioneer:
        zoom 0.75 xcenter 0.25 yalign 1.01 alpha 0
        pause 2.5
        linear 1 alpha 1
    show un normal pioneer close:
        xcenter 0.7
    with dissolve
    "Вместо Жени за столом-конторкой сидела Лена, а в кресле у журнального столика пристроился Максим. И похоже, Электроник прервал их беседу."
    el "П-привет. А где Женя?"
    un "Попросила подменить её до обеда."
    show un smile pioneer close
    un "Ты что-то хотел взять? Возьми, я запишу."
    th "Раз уж пришёл, придётся что-нибудь взять."
    show un normal pioneer close
    "Лена записала книгу в формуляр и спросила:"
    un "Сергей. Правда, что вы у себя машину для чтения памяти собираете?"
    show un shy pioneer close
    un "Я бы хотела попробовать."
    el "Если доктор решит, что это безопасно, то почему нет?"
    show un serious pioneer close
    un "Сергей. Я хочу попробовать, что бы там доктор ни решила. Вы же сами на себе попробуете?"
    show d_ma surprise pioneer with dspr:
        pause 0.5
        easeout 1.1 xcenter 1.2
    play sound [ "<silence 1.1>", sfx_open_door_kick ]
    d_ma "Ё-моё! На обед же надо сигналить, а я тут сижу!"
    "Неожиданное бегство Максима спасло Электроника от необходимости отвечать."
    play sound [ "<silence 0.4>", sfx_close_door_campus_1 ]
    show black with dissolve2
    stop ambience fadeout 1
    "Сергей пробормотал что-то невнятное и выскочил вслед за горнистом."
    window hide
    
    pause 2

    play music peritune_gentle_theme_piano fadein 1
    play ambience ambience_library_day fadein 1
    scene bg int_library_day:
        matrixcolor BrightnessMatrix(value=-0.25)
    show dct_int_library_rain:
        alpha 0.3
    show dct_int_library_rain_lamp
    with dissolve
    show d_mz sad pioneer glasses far with dissolve:
        xcenter 0.8
    window auto
    "Лена утром зашла в библиотеку без всякой глобальной цели, просто поменять книжку, но зацепилась взглядом за Женю. Та грустила в углу зала за своим столом-конторкой, чем-то напоминая нахохленную птицу под дождём."
    th "Зря мы в автобусе тогда пошутили. Сейчас бы Женя вовсю Сергея гоняла."
    extend " Или нет, не сейчас. После обеда. Отсюда и до самого кружка. Тоже ничего хорошего, но не сидела бы с таким мутным взглядом."
    extend " И Сергей не прятался бы от всех в работе."
    "А потом ещё в разговоре, пока Женя записывала в формуляр книгу, выяснилось, что она со вчерашнего дня сидит безвылазно в библиотеке с перерывами только на еду и сон."
    "И понадобились всё искусство убеждения и умение выдавать свои мысли за чужие желания, которыми обладала Лена, чтобы уговорить Женю просто сходить прогуляться по лагерю."
    show d_mz sad pioneer at right with dissolve_fast
    mz "Лена, а если кто-то придёт..."
    un "Тогда я выдам ему нужное издание и заполню формуляр не хуже тебя."
    mz "Я только..."
    un "Хорошо-хорошо. Я подежурю. Только ты недолго."
    window hide
    stop music fadeout 2.5
    play sound ["<silence 0.7>", sfx_close_door_1]
    hide d_mz sad pioneer with MoveTransition(1.0, leave=_moveright, leave_time_warp=_ease_time_warp)
    window auto
    "До обеда оставалось ещё около часа."

    show int_library_day as int_library_day2:
        alpha 0
        pause 0.5
        linear 0.5 alpha 1
    
    "Лена погасила настольную лампу, отодвинула тяжёлую портьеру у себя за спиной и впустила в библиотеку солнечные лучи.{w} Взвесила в руке выбранную книжку: на пару дней чтения хватит. Бросила взгляд на библиотечные стеллажи."
    th "А ведь рано или поздно книги кончатся. Всё, что было здесь хорошего, я уже прочитала. Сейчас читаю средненькое. А потом?"
    extend " Может, Семён что-то принесёт?"
    "Семён с Ульяной ушли сегодня утром и клятвенно обещали вернуться завтра часам к десяти; оставалось надеяться, что они вернутся не с пустыми руками."
    "По крайней мере, та пьеса, что они принесли в прошлый раз, была проглочена Леной за сутки, потом ещё три раза перечитывалась и породила массу карандашных рисунков-иллюстраций, самый доведённый до ума из которых сейчас ехал обратно как подарок автору пьесы. Та, другая Мику — автор пьесы, обладала ещё и литературным талантом."
    "А ещё интересно было осознавать, что где-то есть очень похожие на тебя Лены, встретиться с которыми, по словам того же Семёна, почти невозможно."
    show dct_int_coaching_room2
    show dct_dream_veil at shiver
    with dissolve_fast
    "Как там он сказал?"
    show d_sf serious sport at center behind dct_dream_veil with dissolve_fast:
        ypos 0.0
    me "Останется только один!"
    hide dct_int_coaching_room2
    hide d_sf
    hide dct_dream_veil
    with dissolve_fast
    "{cps=0}А ещё, интересно было осознавать, что где-то есть очень похожие на тебя Лены, встретиться с которыми, по словам того же Семёна, почти невозможно.{/cps} Можно, только во сне."
    "Лена вспомнила обрывки сна, которым завершилась их с Алисой спасательная экспедиция.{w} Сколько там Алис в одном месте оказалось? Три минимум.{w} Сон сном, но волдыри на ладонях потом сходили до самого конца цикла.{w} И это ощущение тепла от поддерживающих тебя дружеских рук на твоих плечах."
    th "Кажется, мальчики какую-то машину для чтения памяти придумывают, надо будет с ними поговорить."
    scene dct_int_library_standing_desk_back
    show dct_int_library_standing_desk_front
    with squares
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
    stop ambience fadeout 1.5
    $ renpy.music.set_volume(0.5, delay=0, channel='sound_loop')
    play sound_loop dct_ambience_rattle_in_library fadein 1.5    # Пока так, но лучше бы найти что-то более подходящее
    "И, не дожидаясь ответа, пошёл шарить по стеллажам."
    "Лена несколько раз порывалась вскочить и посмотреть на происходящую катастрофу, но всякий раз удерживала себя на месте."
    th "Женя меня съест."
    stop sound_loop fadeout 1.5
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
    "Была бы тут Женя — не остался бы, конечно, но общество Лены было гораздо приятнее."
    scene bg int_library_day
    show un normal pioneer:
        xcenter 0.75
    show d_ma normal pioneer:
        zoom 0.75 xcenter 0.25 yalign 1.01
    with squares
    "Лена против общества Максима тоже не возражала, поэтому скоро тишину в библиотеке прерывало только шуршание страниц и шмыгающий нос нелегально искупавшегося вчера Максима."
    pause 1
    "Максим решился начать разговор."
    show d_ma serious pioneer with dissolve_fast
    d_ma "Лен, а можно спросить?"
    stop ambience
    $ renpy.music.set_volume (0.5)
    play music anewbeginning fadein 3
    show un shy pioneer with dspr
    d_ma "Скажи, вы нашего физрука давно знаете? Ты и Алиса."
    show un normal pioneer with dspr
    un "Давно. Не очень, но давно."
    show d_ma surprise pioneer with dissolve_fast
    show un smile pioneer with dspr
    un "С рождения, наверное."
    #"Книжка была так себе, и разговаривать было интереснее."
    show d_un hope pioneer as un
    show d_ma normal pioneer 
    with dissolve_fast
    un "А почему ты спросил?"
    d_ma "Тогда понятно.{w=0.5} Да просто даже Алиса никогда не будет взрослого, пусть и хорошо знакомого человека, Сенькой называть.{w} И она всегда так заботится о Семёне, а Ульяна видит это и только улыбается."
    show un serious pioneer with dspr
    un "Ты наблюдательный..."
    show d_ma grin2 pioneer with dissolve_fast
    "Лена думала, как закруглить разговор. В конце концов, Максим пока ещё только непроснувшийся кандидат в старший отряд, и разъяснять тонкости взаимоотношений Рыжих с Семёном постороннему человеку не хотелось."
    "Но, кажется, Максим понял слова «с рождения» буквально и сделал свои собственные выводы."
    show d_ma smile pioneer with dissolve_fast
    d_ma "То есть ему было лет восемь.{w=0.5} Ну да, если так, то он для вас не заместитель начальника лагеря, а просто как старший брат. Понятно."
    show un smile pioneer with dissolve
    stop music fadeout 2.5
    "Все было не так, но Лена не стала поправлять."
    show un normal pioneer with dspr
    play sound sfx_open_door_1
    show el laugh pioneer close with dissolve
    "Скрипнула дверь, и на пороге показался Сыроежкин."
    show d_ma normal pioneer
    show el normal pioneer close:
        alpha 1
        pause 1.2
        linear 1 alpha 0
    with dissolve_fast
    "Поздоровался — Лене показалось, что разочарованно — и пошёл выбирать себе книжку."
    "Лена вспомнила про «машину для чтения памяти» и, решив застолбить себе место среди подопытных, стала ждать, когда Сергей вернётся к конторке."
    window hide
    stop ambience fadeout 1
    scene black with dissolve
    $ renpy.music.set_volume (1.0)

    pause 2


    play ambience ambience_clubs_inside_day fadein 1
    window show
    scene bg int_clubs_male_day with dissolve:
        zoom 1.2 align (0.0, 0.5)
    "Шурик, отпустив Сыроежкина, закончил отбирать нужные детали, высыпал их в жестяную коробку из-под леденцов и убрал в ящик стола. Посмотрел, как травятся платы, поболтал кюветой, чтобы перемешать раствор."
    th "Ладно азотная кислота, но хлорное железо шефы могли бы лагерю для кружка подарить. Сейчас бы полдня не теряли."
    extend " Нет, потеряли бы — керамике всё равно остывать до утра вместе с печью."
    stop ambience fadeout 1
    play sound sfx_unlock_medpunkt_door
    play sound_loop ambience_camp_center_day fadein 1
    scene ext_clubs_day with dissolve
    "Шурик запер клуб и, огибая здание, пошёл на своё вчерашнее место."
    stop sound_loop fadeout 1
    play ambience ambience_forest_day fadein 1
    play music the_day_when_i_die fadein 2
    scene dct_ext_glade_behind_clubs_day
    show dct_ext_glade_behind_clubs_day_barberry
    with dissolve
    "Прежде чем начинать зондировать собственный мозг, Шурику предстояло разобраться, что ему известно об этих своих сновидениях и голосе в голове, и записать данные самонаблюдения и самоанализа в рабочую тетрадь, чтобы иметь точку отсчёта."
    "Сыроежкин уже согласился быть вторым — контрольным экземпляром. Неплохо было бы для статистики набрать ещё добровольцев, но Шурик опасался возможного риска. В любом случае, как настоящий учёный из любимых книг, он твёрдо знал, что начнёт с себя."
    "Шурик открыл личную рабочую тетрадь и на первой чистой странице написал:{w}\n{i}Дневник самонаблюдения. Начат в четвёртый день смены. Данные по предыдущим дням восстановлены по памяти{/i}."
    "Перечитал. Получилось неплохо. Потом дописал в конце:\n{i}… по памяти и опросам очевидцев{/i}."
    "Дальше следовал подзаголовок:\n{i}Необычные сны и мысли. Галлюцинации и явления.{/i}"
    "Далее следовало описать события первого дня.{w} Шурик порылся в памяти:\n{i}Событие первое — сон в автобусе. Приснилось, что мне сорок лет и я еду в лагерь с пионерами. Почему-то называю пионеров {b}миксами{/b} и {b}копиями{/b}.{/i}"
    "{i}Событие второе — провал в памяти. Поздно вечером обнаружил себя стоящим на площади, спиной к лаборатории.\nЧто делал в лаборатории — не помню, и восстановить свои действия не удалось{/i}."
    "{cps=0}{i}Событие второе — провал в памяти. Поздно вечером обнаружил себя стоящим на площади, спиной к {s}лаборатории{/s} кружку.\nЧто делал в {s}лаборатории{/s} кружке — не помню, и восстановить свои действия не удалось{/i}.{/cps}\nЗачеркнул «лабораторию» и написал «кружок». Вроде бы всё."
    
    stop music
    mip "Привет. А ты Сергея не видел?" with hpunch ### у Оксаны имя голубого цвета. Стоит ли вводить отдельный тег?
    show d_oz n pioneer behind dct_ext_glade_behind_clubs_day_barberry with dissolve:
        zoom 0.75 xcenter 0.77 yalign 0.1
    "Шурик вздрогнул и уронил карандаш."
    th "Сергея? А! Это Сыроежкина, что ли?"
    sh "Нет, занятия закончились, и он ушёл. Поищи его в библиотеке."
    mip "Понятно. Если увидишь, то передай, пожалуйста, что его Оксана Зайцева искала."
    hide d_oz with MoveTransition(1.2, leave=_moveright, leave_time_warp=_ease_time_warp)
    "И, не дожидаясь ответа, девочка исчезла, нырнув куда-то в кусты."
    "Шурик повертел в руках карандаш. Синий «Картограф» сломался после контакта с бетоном отмостки, и теперь, чтобы его очинить для продолжения записей, нужно было возвращаться в клуб."
    play sound dct_sfx_horn_dinner_through_loudspeaker
    "Кстати прозвучавший горн напомнил об обеде. Пришлось отклеивать спину от стены клуба, подниматься, отряхивать форму."
    th "Здесь удивительно чисто. Ни копоти, ни глины, ни мазута. Отряхнулся, и форма как новая. А чтобы найти грязь, нужно специально постараться."
    stop ambience fadeout 1
    window hide
    scene black with dissolve
    stop sound_loop fadeout 1

    pause 2


    play ambience ambience_camp_center_day fadein 1
    window auto
    scene bg ext_houses_day at walking with dissolve
    th "Почему Алиса куксилась, что всё из цикла в цикл одно и то же? Может, она просто видеть не умеет? Не знаю. И пионеры, и природа каждый цикл хоть чуть-чуть, но разные."
    th "Вон куст подсыхает — прошлый цикл зелёный стоял, а в этом листья теряет. А здесь за четыре дня новую тропинку протоптали — интересно, приживётся или нет? А уж люди как меняются... Это просто надо увидеть."
    "Лена шла из столовой к себе в домик и размышляла."
    scene bg ext_house_of_un_day with dissolve
    th "Я, наверное, порисую сейчас. Портрет Саши начну, а то сколько времени живём в одном домике, а так Саши у меня и нету."
    stop ambience fadeout 1
    play sound_loop ambience_int_cabin_day fadein 1
    play sound sfx_open_door_1
    scene bg int_house_of_un_day with slidedown
    "Саши дома не оказалось."
    th "Или возится с мелкими, или ещё где-то — хоть у Мику в кружке, в этом цикле они сблизились раньше обычного."
    "Купальный сезон официально открывался в четверг, а в следовании инструкциям Саша была похожа на Серёжу Сыроежкина, так что на пляже её точно не было."
    th "В следующий раз."
    "Лене пришлось снова отложить мысль о Сашином портрете."
    th "Взять этюдник и уплыть на остров? Причём на малопосещаемый остров Длинный."
    extend " Или уйти с этюдником на остановку и в очередной раз нарисовать дорогу, убегающую в поля?"
    "Лена взвесила в руках этюдник и поморщилась — тяжёлый. Да и не очень-то и хотелось."
    th "Может, остаться в домике и изобразить ту сценку приручения стрекозы двумя маленькими девочками?"
    extend " И подарить Алисе?{w=0.4} Алиске понравится."
    "Лицо маленькой Алисы встало перед глазами как живое.{w} Так, одна идея есть, и ладошка зачесалась — хороший признак. Значит, результат будет удачный."
    "А потом, без перехода, Лена вспомнила, как в столовой Женя и Электроник постоянно бросали взгляды друг на друга и как они вздрагивали, отводили глаза и зажимались, если этим взглядам случалось встретиться.{w} Да, это оно."
    #"Лена быстро набросала сцену приручения стрекозы, чтобы поработать над ней после, когда время будет, а сама взяла карандаши, папку с бумагой и направилась к Жене в библиотеку."
    stop sound_loop fadeout 2
    play ambience ambience_library_day fadein 2
    scene bg int_library_day
    show mz normal pioneer glasses at right
    with dissolve
    mz "А, это ты. Заходи."
    "Женя постепенно отходила от вчерашнего приступа чёрной меланхолии и встретила Лену почти приветливо."
    un "Я почитаю тут?"
    show d_mz bukal pioneer glasses as mz with dspr
    mz "Библиотека публичная."
    show d_mz fun pioneer glasses as mz with dspr
    "Женя фыркнула на слове «публичная» и пожала плечами."
    show mz normal pioneer glasses with dspr
    mz "Читай."
    
    $ renpy.music.set_volume (0.5, delay=1.5)
    stop ambience fadeout 1
    play music fm_freemusic_chillout_music fadein 3
    hide mz with dissolve
    "Лена так и сделала — ну почти так. Выбрала книгу побольше форматом, устроилась за одним из читательских столов так, чтобы Женя оказалась в нужном ракурсе, и, спрятав в раскрытой книге лист бумаги, начала делать зарисовки, стараясь поймать эмоции." #цг-шку бы сюда
    "Женя читала что-то своё, время от времени бросая взгляды за окно и на входную дверь, хмурилась, коротко поджимала губы и переворачивала страницу.{w} А после очередной страницы проскрипела, не глядя на Лену:"
    show d_mz shyangry pioneer glasses far as mz at right with dissolve
    mz "Между прочим, можешь не прятаться. А если бы спросила разрешения — то и совсем хорошо было бы."
    un "Ой!"
    "Лена покраснела."
    show d_mz confused pioneer glasses far as mz with dissolve_fast
    mz "Рисуй, если хочешь. Но я не понимаю..."
    "Женя не договорила и, всё так же не глядя на Лену, пожала плечами."
    show mz smile pioneer glasses with dissolve_fast
    mz "И спасибо, что посидела тут вместо меня."
    show d_mz confused pioneer glasses far at right:
        alpha 0
        pause 1.5
        linear 1 alpha 1
    #play ambience ambience_library_day fadein 2.5
    "Ещё на полчаса девочки погрузились в молчание, прерываемое шелестом бумаги и редкими вздохами. Да иногда снаружи доносились голоса пионеров: по Плану мероприятий у среднего отряда было сейчас свободное время, чем они и пользовались, устроив беготню по всему лагерю."
    th "А ведь она ждёт, что Сергей заглянет, а тот боится и где-то прячется."
    extend " Зря девочки посадили Сергея на моё место, и зря я на это согласилась. Нужно бы сейчас всё рассказать, но Женя не поверит — решит, что я Сергея выгораживаю. С её-то точки зрения всё было так, как она увидела."
    hide mz
    show d_mz sceptic pioneer glasses far with dissolve_fast:
        alpha 1
    mz "Лена. А что за рукопись ты вчера у меня забыла?"
    "Скрип Жениного голоса вывел Лену из раздумий."
    un "Это..."
    "Лена задумалась, как не соврать так, чтобы Женя не стала потом крутить пальцем у виска."
    un "Это девочка одна, знакомая нашего физрука, сказку написала. И Семён попросил, чтобы я к ней иллюстрации сделала."
    show d_mz hope pioneer glasses far with dspr
    "И, отвечая на висящий в воздухе вопрос, добавила:"
    un "Можешь взять почитать. Заходи вечером. Я Саше скажу, если меня не будет."
    stop ambience fadeout 1
    scene black with dissolve
    window hide

    pause 0.5


    #play music music_list['your_bright_side'] fadein 1
    $ renpy.music.set_volume (1.0, delay=1)
    window auto
    scene bg int_library_day
    show d_mz sad pioneer glasses close:
        zoom 1.25 align (-0.5, 0.5)
    with dissolve
    show dct_cg_mz_dreams_of_el: # Псевдокартинка, со сменяющимися артами Электроника
        alpha 0
        linear 2 alpha 0.45
        pause 2
        linear 2 alpha 0.6
        pause 3.5
        linear 2 alpha 0.75
        pause 5
        linear 2 alpha 0.9
    "Женя действительно ждала Сыроежкина. Даже самой себе не сознавалась в этом, но ждала."
    "Провожала взглядом пробегающих за окнами пионеров;{w} прислушивалась, когда казалось, что кто-то топчется на крыльце;"
    play sound ["<silence 1.2>", "<to 1.0>sound/sfx/open_door_clubs.ogg"]
    show int_library_day as int_library_day2:
        alpha 0
        pause 1.3
        linear 1 alpha 1
    show d_mz amazed pioneer glasses close as mz:
        zoom 1.25 align (-0.5, 0.5) alpha 0
        pause 1.3
        linear 1 alpha 1
    #stop music fadeout 2
    extend " вздрогнула, когда вдруг повернулась дверная ручка.\n«Он!» — ёкнуло внутри."
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
    $ renpy.music.set_volume (0.5, delay=1.5)
    
    "Лену Женя уже отнесла к числу безопасных, подвоха от неё не ждала, поэтому выгонять из библиотеки не стала, а разрешила остаться и посидеть-почитать. В общем-то, каждый любитель посидеть-почитать был понятен Жене и не вызывал у неё ни агрессии, ни испуга."
    "И даже то, что Лена вместо чтения занялась рисованием, Женю особо не раздражало."
    show un surprise pioneer with dissolve_fast
    extend " Так только, дала понять, что заметила, и всё.{w} Только поначалу неприятно немного было оказаться в фокусе чужого внимания."
    show un grin pioneer with dissolve_fast
    extend " Под конец даже разговорились немного, обсуждая разное."
    stop music fadeout 3
    play ambience ambience_library_day fadein 2
    show d_un hope pioneer as un with dspr
    un "Женя, в субботу сбор отряда будет."
    mz "Я не приду."
    un "Я, может, тоже. Я не об этом. Будем решать, принимать новенького или нет. В..."
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
    th "Ну значит, не больно-то и хотелось, значит, мне и не нужно это видеть."
    "После ухода Лены Женя ещё раз обвела глазами библиотеку, увидела журналы на полке с прочитанной и возвращённой литературой."
    th "Интересно, кто брал?"
    "Глянула в ящик с читательскими формулярами. Сверху, на коротенькой шеренге формуляров, стоящих в ящике друг за другом в алфавитном порядке, лежал свежий."
    "«Родионов Максим, 14 лет, {s}средний{/s} отряд». Над зачёркнутым словом «средний» рукой Лены было написано «старший»."
    scene bg int_library_day
    show d_mz smile2 pioneer glasses close
    with squares
    mz "Любит ли читать — я ещё не знаю, но умеет — это точно."
    show d_mz normal pioneer glasses close with dissolve_fast
    "Теперь осталось только вернуть журналы на место, и можно запирать библиотеку на перерыв. Или не запирать — идти всё равно некуда."
    "Женя взяла журналы, подержала их в руках и положила обратно на полку."
    show d_mz sceptic pioneer glasses close with dspr
    
    $ renpy.music.set_volume (1.0)
    play music music_list['just_think'] fadein 3
    "Потом взяла самый верхний и быстро пролистала его. Нет, всё верно, вон и библиотечный штамп на месте. Но всё же."
    show d_mz surprise pioneer glasses close with dspr
    "Женя подошла к каталогу, выдвинула несколько ящичков и умело пробежалась по картотеке, потом проделала это ещё раз, читая каждую карточку, вынимая карточки из ящичков и проверяя, не завалилась ли какая-нибудь карточка, выпав из общего ряда."
    show d_mz amazed pioneer glasses close with dspr
    "Потом проделала то же самое уже с каждым ящичком, а не только с теми, где была периодика и издания на букву З. Ничего нового, никаких поступлений, но в фондах библиотеки «Совёнка» не числилось ни одного номера журнала «Знание-сила». Несмотря на библиотечный штамп на этих самых журналах."
    hide d_mz with dissolve_fast
    pause 0.5
    show d_mz normal pioneer glasses close with dissolve_fast
    "Женя вернулась к журналам, взяла с полки самый верхний, посмотрела на первую страницу обложки, потом перевернула и посмотрела на типографские данные.{w}\n{i}«Сдано в набор 06.09.1991.»{/i}"
    show d_mz smile2 pioneer glasses close with dissolve_fast
    "Женя глянула на календарик, притаившийся под оргстеклом, покрывающим её стол. Согласно календарику, на дворе стоял июнь 1987 года."
    show d_mz sceptic pioneer glasses close with dissolve_fast
    th "Кажется, придётся прийти на сбор отряда."
    th "Кажется, придётся спросить у новенького, где он берёт журналы. Может, он и книг хороших оттуда же натаскает?"
    window hide
    stop ambience fadeout 1
    stop music fadeout 1
    scene black with dissolve

    pause 2


    play ambience ambience_int_cabin_day fadein 1
    window show
    scene bg int_house_of_un_day with dissolve
    "Саша, чуть-чуть разминувшаяся с Леной, сейчас сидела у себя в домике и с огромным удовольствием читала ту самую пионерскую сказку. Читала, возвращалась к началу, закрывала глаза и как живых представляла себе героинь: Анфису, Ларису, Жанну, Машу. Тем более что и представлять особо не нужно."
    th "Вон же они — как живые. Ясно, с кого их списывали. Нет, разница, конечно есть, так на то и сказка."
    "Вот ни Святославы, ни Янки, ни Степана здесь не было. Святослава чуть походила на саму Сашу, но совсем-совсем чуть-чуть."
    th "Янка... Может быть, если бы Ульяна была помоложе лет на пять, то так она себя бы и вела. Степан? Не могу себе представить — неужели Семён был таким?"
    th "Нет, в нём, конечно, живёт семнадцатилетний пионер, это невооружённым глазом видно, но и двадцатипятилетний заместитель начальника лагеря — тоже в нём."
    #"Саша опять вернулась к началу и посмотрела на первую страницу."
    th "Как, когда Мику успела всё это сочинить? Она же сама говорила в день приезда, когда знакомились, что она впервые в СССР, а её папа с мамой сейчас едут на поезде из Владивостока в Москву с остановками в крупных городах."
    th "Но вот же автор: Мику Хацуне, а вот посвящение: „Сенечке, которому… и Ульянке…“, и подпись японскими закорючками. То есть Мику знала Семёна, когда тому было семнадцать? А самой Мику, получается, восемь-девять? Ничего не понимаю, надо будет спросить для начала у Лены."
    "Саша посмотрела на стену над Лениной кроватью, всю увешанную картинами. Портреты и пейзажи. «И когда успела?» Три портрета особенно притягивали взгляд."
    "Женщина, похожая на Лену как родная мама, протягивает руки открытыми ладонями к зрителю; губы плотно сжаты, глаза чуть прищурены, как будто какую-то работу делает или спорит с кем-то; а если присмотреться — то такая бездна боли в этих прищуренных глазах..."
    "Второй портрет: парень, похожий на Семёна — наверное, таким он и был в семнадцать лет; только глаза не семнадцатилетние, а взрослые и какие-то уставшие, что ли; но понимаешь, что он сейчас улыбнётся этими уставшими глазами и скажет: «Все ерунда, прорвёмся!»."
    "Третий портрет — тот очень позитивный: на нём Семён и Ульяна, сидящие рядышком, рука в руке, на крыльце этого самого домика — оба улыбаются, оба счастливы; как раз и видно, что подросток из заместителя начальника лагеря никуда не делся."
    play sound sfx_knock_door7_polite
    "В дверь постучали."
    play sound sfx_open_door_1 
    show d_ma normal pioneer with dissolve2:
        xcenter 0.5 yalign 0.02   
    d_ma "Привет."
    "Hа пороге нарисовался Максим."
    sa "Здравствуй!"
    "Саша улыбнулась хорошему человеку."
    show d_ma smile2 pioneer with dspr
    "Очень заразительно улыбнулась — так, что Максим сразу разулыбался в ответ."
    "И как-то даже и не пришлось, как всегда, маскировать смущение нахальством, а захотелось просто взять сразу и обратиться к так приветливо улыбающейся девочке со своей, такой деликатной просьбой."
    show d_ma smile pioneer with dissolve_fast
    d_ma "Саш, ты не могла бы чуть поучить меня танцевать? К следующей дискотеке?"
    sa "Хочешь Алису удивить..."
    show d_ma shy pioneer with dissolve_fast
    "Саша не спрашивала, а просто констатировала факт."
    sa "Приходи в музыкальный кружок после ужина. С Мику я договорюсь."
    window hide
    stop ambience fadeout 1
    scene black with dissolve

    pause 2

    play ambience ambience_lake_shore_day fadein 1    
    play music music_list['she_is_kind'] fadein 1
    window auto
    scene dct_ext_between_beach_and_boathouse_day
    show el smile pioneer at cleft
    show d_oz smile pioneer at cright:
        yalign 0.27
    with dissolve
    "Вторую половину дня Сыроежкин провёл в компании милой девушки Оксаны."
    hide el
    hide d_oz
    with dissolve
    "Показывал ей, как правильно держать нож; объяснял, когда режут от себя, а когда — к себе; ругался на нож, который она принесла, а потом объяснял, почему острый нож безопаснее тупого."
    show el normal pioneer at cleft with dissolve
    el "Ты когда острым ножом режешь, рука просто идёт за ножом и всё, и не надо лишних усилий делать. Просто следи, чтобы пальцы на пути у лезвия не оказались."
    show el serious pioneer with dissolve_fast
    extend " А когда режешь тупым, то ты напрягаешься, и у тебя нож обязательно сорвётся и попадёт по пальцам, как бы ты их ни берегла."
    hide el with dissolve    
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
    "Потом искали вдвоём подходящий кусок коры, и Оксана пыталась выстругать хоть что-то, похожее на кораблик."
    show el grin pioneer at cleft with dissolve
    el "Не надоело? Ну тогда пошли в клуб."
    stop ambience fadeout 1
    
    play sound_loop ambience_clubs_inside_day fadein 1
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
    "Пошли в клуб, извинились перед Шуриком за то, что помешали, и заточили нож Оксане."
    stop sound_loop fadeout 1
    window hide
    show black with dissolve_fast

    
    $ set_mode_nvl()
    scene dct_ext_between_beach_and_boathouse_day with dissolve_fast
    window show
    "Потом опять искали кусок коры."
    el "Стой. А теперь, прежде чем за нож браться, нарисуй, что ты хочешь. Да вот, хоть на мокром песке палочкой и нарисуй."
    d_oz_nvl "Вот так, да?"
    el "Нет, смотри, как надо."
    "Потом разбирали проект Оксаны по косточкам."
    el "А ты хочешь, чтобы он просто на полке стоял или чтобы его ещё и на воду спустить можно было?"
    "..."
    el "Знаешь, напиши ему письмо, небольшое, чтобы упаковать можно было.{w} В клубе была папиросная бумага, вот на ней завтра и напиши. Потом в полиэтилен запаяем и внутри корабля спрячем.{w} Если всё так, как ты говоришь — он обязательно полезет разбирать твой подарок. Там письмо и найдёт. Может, это сработает."
    "И снова взялись за ножи."
    el "А почему ты всё своими руками должна делать?"
    "..."
    el "Что значит — иначе цикл не переживёт?"
    "А потом долгие разговоры."
    el "Не знаю, Оксана, права ты или нет, но может, это мы уходим куда-то дальше, а вы здесь задерживаетесь."
    show dct_ext_between_beach_and_boathouse_sunset:
        alpha 0
        linear 1 alpha 1
    nvl hide dissolve
    window hide

    $ set_mode_adv()
    
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_lake_shore_evening fadein 1
    show d_oz d pioneer at center:
        yalign 0.27
    with dissolve
    window show
    "И расстались уже перед самым ужином, договорившись о завтрашней встрече."
    d_oz "Знаешь, Серёжа..."
    show d_oz smile pioneer with dspr
    extend " Нет, потом, в конце смены. До завтра!"
    hide d_oz with dissolve_fast
    "И убежала, прихватив с собой недоделанный кораблик."
    "А Электроник ещё посидел на берегу, улыбаясь и думая о том, какая это славная девочка, и о её словах, что он Жене нравится."
    play sound dct_sfx_horn_dinner_through_loudspeaker
    $ sunset_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    "Дождался горна и уже тогда встал, отряхнулся и пошёл — сперва в кружок за Шуриком, а оттуда на ужин."
    stop music fadeout 1.5
    stop ambience fadeout 1
    window hide
    stop sound fadeout 1.5
    scene black with dissolve
    
    
    pause 0.5


    $ night_time()
    $ persistent.sprite_time = "day"

    play ambience ambience_int_cabin_night fadein 1
    scene bg int_house_of_dv_night
    show 3500_dv sad night2 0pt at right:
        ycenter 0.83
    with dissolve
    window auto
    "Алиса была помощницей вожатой в этом лагере исключительно из-за отсутствия альтернатив, и помощница вожатой из неё вышла плохая, но какие-то привычки въелись, и их уже не вытравить. Вот и сейчас она перебирала в памяти прожитый день, анализировала свои ошибки, делала выводы и строила планы на завтра."
    show 3500_dv normal night2 0pt with dissolve_fast
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Что там со мной и лагерем происходило сегодня?"
    window hide
    stop ambience fadeout 1
    
    $ day_time()
    play music music_list['raindrops'] fadein 1
    scene bg ext_path_day
    show ext_path_sunset:
        alpha 0.6
    show d_sf normal sport at right
    show d_us normal sport at center:
        ypos -0.05
    show dct_dream_veil at shiver
    with dissolve
    window auto
    "Прощание с Персуновыми в пять утра. Алиса не утерпела и вскочила в такую рань, чтобы проводить своих самых близких людей, уходящих в утреннюю хмарь."
    dv "Вы туда же, на то же место?"
    me "Да, Алис. Точка стабильная и ещё долго продержится. Да не кисни, Рыжая. Завтра же придём назад!"
    show bg ext_playground_day
    hide ext_path_sunset
    hide d_sf
    hide d_us
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
    play sound "<from 2>sound/sfx/slavya_run.ogg" fadein 1
    $ renpy.pause (0.2)
    hide sl with MoveTransition(1.2, leave=_moveleft, leave_time_warp=_ease_time_warp)
    $ renpy.pause (0.4)
    stop sound fadeout 1.3
    "И убежала, только лёгкие шлепки подошв о покрытие беговой дорожки были слышны за спиной."
    show bg ext_square_day behind dct_dream_veil
    show d_ma normal pioneer behind dct_dream_veil:
        zoom 1.25 xcenter 0.5 yalign 0.08
    with dissolve
    "Чуть позже — Максим, который хотел спросить о чём-то, но так и не решился."
    show dct_lineup_mi_not_us behind dct_dream_veil with dissolve
    "Еще чуть позже — линейка, слава богу, в этом цикле не военизированная."
    hide d_ma
    show mt normal panama pioneer behind dct_lineup_mi_not_us
    hide dct_lineup_mi_not_us with dissolve
    mt "Алиса, а ты не в курсе, где наши физруки? Они предупредили, что появятся завтра после завтрака, но о подробностях умолчали."
    dv "Ольга Дмитриевна, помните — в первый день сестрёнка Ульянина отметилась, которая отдыхает тут недалеко? Вот, кажется, её навестить."
    show mt surprise panama pioneer with dspr
    mt "Недалеко? Странно. До ближайших людей здесь километров триста."
    show mt normal panama pioneer with dspr
    extend " Ну ладно, Алиса, на субботу какие мероприятия запланировала?"
    hide mt
    show bg ext_clubs_day
    show el smile pioneer at cright behind dct_dream_veil
    show sh laugh pioneer at cleft behind dct_dream_veil
    with dissolve
    "Кибернетики затеяли что-то новое в своей берлоге."
    show d_el smile2 pioneer as el
    show sh smile pioneer
    with dspr
    $ day_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Надо будет убедиться, что это безопасно для окружающих."
    window hide
    stop music fadeout 2.5
    
    $ night_time()
    scene bg int_house_of_dv_night
    show 3500_dv normal night2 0pt at left:
        ycenter 0.83
    with dissolve
    play ambience ambience_int_cabin_night fadein 1
    window auto
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
    th "Привыкаю постепенно — вот уже и её кровать своими вещами занимаю, и бельё на эту кровать брать на складе не стала. Но всё равно вечерами тоскливо. Хорошо хоть Ульянка каждый вечер специально поболтать заходит."
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
    th "Уговорить бы её здесь остаться — так в её лагере своя Алиса есть, той тогда совсем плохо будет. Хуже, чем мне в прошлом цикле."
    show 3500_dv normal night2 0pt with dissolve_fast
    th "А у меня уже какие-то просветы появились. Вроде Макса того же."
    show 3500_dv laugh night2 0pt with dspr
    extend " Правильно Мику про него сказала, что он тычется всюду с любопытством и дружелюбием, как молодой пёс."
    show 3500_dv smile night2 0pt with dspr
    th "Было бы ему хоть на пару лет побольше."
    show 3500_dv normal night2 0pt with dspr
    "Алиса посмотрела на гитару, но нет — настроения не было."
    th "Ну значит спать."
    play sound sfx_click_1
    pause 0.2
    show d_int_house_of_dv_night_without_light
    show 3500_dv normal night2 0pt as dv at left:
        ycenter 0.83 alpha 1 matrixcolor TintMatrix("#A1C9D0")  # Перекраска спрайта через преобразование matrixcolor. Свойство TintMatrix с цветом "#A1C9D0" даёт результат почти идентичный ночным спрайтам
        pause 0.8
        linear 1 alpha 0
    with dspr
    "Погасила свет и завернулась в простыню."
    $ night_time()                       # Прописано, чтобы при обратной перемотке цвета не сбивались.
    extend " Она уже знала, что ей приснится."
    window hide
    
    #
    #   Сон Алисы
    #
    
    $ day_time()
    $ renpy.music.set_volume(0.3, delay=0)
    stop ambience fadeout 3
    play music music_list['tried_to_bring_it_back'] fadein 3
    ###################################################################################
    
    #  Вариант с "camera:" не подходит, потому что после этого перестаёт работать класс переходов MoveTransition(). Все эти move, moveinright, easeoutleft и т.п.
    
    ###################################################################################
    # show d_int_house_of_dv_night_without_light as d_int_house_of_dv2 at shiver with Dissolve(0.0)
    
    # scene dct_cg_christmas_balls_back:
        # zoom 1.0 anchor (0.35, 0.5) pos (0.5, 0.5)
    # show dct_ball_to_world01:
        # zoom 1.23 xcenter 0.5 ycenter 0.5 matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.6, 0.05)) * TintMatrix("#be6012")
    # show dct_dv_in_christmas_ball:
        # zoom 0.82 anchor (0.521, 0.328) pos (0.5, 0.5) matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.8, 0.05)) * TintMatrix("#be8012")
    # show dct_christmas_ball:
        # anchor (0.5, 0.5) pos (0.5, 0.5)
    # camera:
        # perspective True
        # xpos 1536
    # with Dissolve(3.0)
    # window auto
    # "Каждую ночь, с середины прошлого цикла, Алисе обязательно снился один и тот же сон. Очень спокойный, никуда не зовущий, не оставляющий после себя никаких эмоций, он просто снился."
    # $ renpy.music.set_volume(1.0, delay=3)
    # camera:
        # perspective True
        # linear 1 zpos 400 xpos 1150
        # linear 0.55 zpos 600 xpos 925
        # linear 0.43 zpos 750 xpos 750
        # linear 0.3 zpos 800 xpos 625
        # linear 0.3 zpos 800 xpos 500
        # linear 0.25 zpos 750 xpos 400
        # linear 0.34 zpos 550 xpos 260
        # linear 0.34 zpos 300 xpos 125
        # linear 0.33 zpos 0 xpos 0
    # "Начинался сон с того, что Алиса оказывалась заперта внутри латунно-желтого зеркального шара — елочной игрушки."
    # camera:
        # perspective True
        # zpos 0 xpos 0
    
    # show dct_cg_christmas_balls_back:
        # linear 2 zoom 1.22 blur 80
    
    # show dct_ball_to_world as dct_ball_to_world01 behind dct_dv_in_christmas_ball:
        # linear 2 zoom 1.5
    # show dct_ball_to_world behind dct_dv_in_christmas_ball:
        # zoom 1.23 xcenter 0.5 ycenter 0.5 alpha 0
        # linear 2 zoom 1.5 alpha 1
    
    # show dct_dv_in_christmas_ball:
        # linear 2 zoom 1
    # show 3500_dv normal pioneer2:
        # zoom 0.82 anchor (0.521, 0.328) pos (0.5, 0.5) alpha 0
        # linear 2 zoom 1 alpha 1
    
    # show dct_christmas_ball:
        # linear 1 zoom 1.11 alpha 0
    ###################################################################################
    
    
    show d_int_house_of_dv_night_without_light as d_int_house_of_dv2 at shiver with Dissolve(0.0)
    
    scene dct_cg_christmas_balls_back:
        zoom 1.0 anchor (0.35, 0.5) pos (-0.3, 0.5)
    show dct_ball_to_world01:
        zoom 1.23 xcenter -0.3 ycenter 0.5 matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.6, 0.05)) * TintMatrix("#be6012")
    show dct_dv_in_christmas_ball:
        zoom 0.82 anchor (0.521, 0.328) pos (-0.3, 0.5) matrixcolor SaturationMatrix(0.75, desat=(0.9, 0.8, 0.05)) * TintMatrix("#be8012")
    show dct_christmas_ball:
        zoom 1.0 anchor (0.5, 0.5) pos (-0.3, 0.5)

    with Dissolve(3.0)
    window auto
    "Каждую ночь с середины прошлого цикла Алисе обязательно снился один и тот же сон. Очень спокойный, никуда не зовущий, не оставляющий после себя никаких эмоций — он просто снился."
    $ renpy.music.set_volume(1.0, delay=3)

    show dct_cg_christmas_balls_back:
        easeout 1.35 zoom 0.7 pos (0.15, 0.5)
        linear 0.4 zoom 0.6 pos (0.31, 0.5)
        linear 0.3 pos (0.36, 0.5)
        linear 0.4 zoom 0.7 pos (0.4, 0.5)
        easein 1.35 zoom 1 pos (0.5, 0.5)
    show dct_ball_to_world01:
        easeout 1.35 zoom 0.861 xcenter 0.15
        linear 0.4 zoom 0.738 xcenter 0.31
        linear 0.3 xcenter 0.36
        linear 0.4 zoom 0.861 xcenter 0.4
        easein 1.35 zoom 1.23 xcenter 0.5
    show dct_dv_in_christmas_ball:
        easeout 1.35 zoom 0.574 pos (0.15, 0.5)
        linear 0.4 zoom 0.492 pos (0.31, 0.5)
        linear 0.3 pos (0.36, 0.5)
        linear 0.4 zoom 0.574 pos (0.4, 0.5)
        easein 1.35 zoom 0.82 pos (0.5, 0.5)
    show dct_christmas_ball:
        easeout 1.35 zoom 0.7 pos (0.15, 0.5)
        linear 0.4 zoom 0.6 pos (0.31, 0.5)
        linear 0.3 pos (0.36, 0.5)
        linear 0.4 zoom 0.7 pos (0.4, 0.5)
        easein 1.35 zoom 1 pos (0.5, 0.5)
    "Начинался сон с того, что Алиса оказывалась заперта внутри латунно-жёлтого зеркального шара — ёлочной игрушки."
    show dct_cg_christmas_balls_back:
        zoom 1 pos (0.5, 0.5)
    show dct_ball_to_world01:
        zoom 1.23 xcenter 0.5
    show dct_dv_in_christmas_ball:
        zoom 0.82 pos (0.5, 0.5)
    show dct_christmas_ball:
        zoom 1 pos (0.5, 0.5)


    show dct_cg_christmas_balls_back:
        linear 2 zoom 1.22 blur 80
    
    show dct_ball_to_world as dct_ball_to_world01 behind dct_dv_in_christmas_ball:
        linear 2 zoom 1.5
    show dct_ball_to_world behind dct_dv_in_christmas_ball:
        zoom 1.23 xcenter 0.5 ycenter 0.5 alpha 0
        linear 2 zoom 1.5 alpha 1
    
    show dct_dv_in_christmas_ball:
        linear 2 zoom 1
    show 3500_dv normal pioneer2:
        zoom 0.82 anchor (0.521, 0.328) pos (0.5, 0.5) alpha 0
        linear 2 zoom 1 alpha 1
    
    show dct_christmas_ball:
        linear 1 zoom 1.11 alpha 0
    "Постепенно размеры игрушки росли, стенки отдалялись, теряли чёткость, горизонт становился всё дальше, и вдруг Алиса понимала, что она уже не внутри зеркального шара, а снаружи."
    scene dct_ext_square_extended_day:
        zoom 1.5 xcenter 0.5 ycenter 0.5
        easeout_cubic 4 zoom 0.65
    show 3500_dv normal pioneer2:
        zoom 1 anchor (0.521, 0.328) pos (0.5, 0.5)
        easeout 4 zoom 0.36
    show white:
        alpha 0
        pause 2.5
        linear 1.5 alpha 1
    "А потом этот шар начинал уменьшаться в размерах, горизонт опять приближался, и оказывалось, что вокруг Алисы плавают, иногда соприкасаясь, а иногда слипаясь в устойчивые гроздья, множество таких шаров."
    show dct_cg_clusters_of_worlds behind white:
        xalign 0.0
    show dct_cg_clusters_of_worlds behind white:
        ease 6 xalign 1.0
        pause 0.2
        ease 6 xalign 0.0
        pause 0.2
        repeat
    show white:
        alpha 1
        linear 1.5 alpha 0
    extend " И внутри каждого спрятана своя Алиса: в чём-то абсолютно такая же, а в чём-то похожая только на саму себя."

    "И можно перепрыгнуть со своего шара на соседний и проснуться уже там, внутри, рядом с двойником. И с двойником при таком проникновении ничего не случится. Вот только надо решиться прыгнуть."
    th "Интересно, Ленке то же самое снится?"
    # "Ещё успела подумать Алиса перед тем, как уснуть окончательно."  # Опускаем
    stop music fadeout 3
    show black:
        alpha 0
        linear 3 alpha 1
    th "Она ведь та ещё партизанка — будет молчать, пока совсем плохо не станет."



    stop sound fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
