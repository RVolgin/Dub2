    ##############################
    #Глава 7. Чужие в чужой земле#
    ##############################


label dct_foreign_land:
    $ save_name = u"Дубликат. Монетка в фонтане -- Чужие в чужой земле"
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene black
    stop sound
    stop ambience
    stop sound_loop
    play music music_list['your_bright_side'] fadein 2
    show headline_text2 u"Глава VI. Чужие в чужой земле" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    # scene dct_sky_over_flowerbed_behind_library with dissolve:
        # size (1920, 1252) align (0.5, 0.5)
        
    scene bg ext_no_bus_sunset with dissolve:
        zoom 2 pos (-0.33, -0.2)
    "Оказывается, это трудно, наладить отношения с другим человеком, даже если этот человек тебе нравится.{w} Даже если ты нравишься этому человеку."
    "За шесть часов заместитель руководителя кружка кибернетики и заведующая библиотекой успели три раза поссориться и два раза помириться. И сейчас пытались помириться в третий раз."
    "Началось всё с того, что Женя пошутила в своей обычной манере, когда окружающим непонятно, что это: или шутка, или очередной укол."
    scene black
    show d_mz smile2 glasses pioneer close at center
    with squares
    mz "Тебе не поздно ещё убежать и сделать вид, что ничего не было."
    "А Электроник понял всё буквально."
    hide d_mz
    show el serious pioneer close at center
    with pixellate
    extend " Ну, почти буквально."
    el "Если ты так говоришь, значит ты хочешь, чтобы я убежал."
    hide el
    show d_mz shyangry glasses pioneer close at center
    with pixellate
    "И Женя не нашлась, что ответить."
    "Убеждать, что её не так поняли, она не хотела, сказать в ответ: «Ну и скатертью дорога!» — не смогла. {w}Собиралась, но перехватило дыхание."
    
    scene dct_mz_and_el_sitting_on_grass with squares
    
    # "Были там ещё, конечно, и другие слова, и, в результате, парочка, собирающаяся распасться, не успев сложиться, сидела на скамье. Все там же, в конце библиотечной аллеи, спрятавшись от всех за статуей читающего пионера, каждый на своем конце, и молчали, отвернувшись друг от друга."   # По канону
    
    "Были там ещё, конечно, и другие слова, и в результате парочка, собирающаяся распасться, не успев сложиться, сидела в тени деревьев."
    "Всё там же, в конце библиотечной аллеи, спрятавшись от всех за статуей читающего пионера, и устроившись на безопасном расстоянии. Сидели и молчали, стараясь не смотреть друг на друга."
    
    "Электроник держался за ручку всё того же многострадального портфеля, всё искал и не находил в себе силы встать, попрощаться и уйти в кружок.{w} Всё-таки, Жене он не нужен…"
    "Женя же всё мучительно пыталась понять: что она сделала не так. Отчего сейчас всё рушится?"
    th "Сейчас он встанет и уйдёт."
    extend " И всё."
    "Наконец, Сергей решился."
    scene bg ext_path_sunset:
        zoom 1.5 align (1.0, 0.1)
    show 3500_el sad pioneer briefcase:
        xcenter .65 ycenter.833
    with dissolve
    "Вздохнул, как-то сгорбившись поднялся на ноги, прихватив портфель левой рукой, повернулся к Жене."
    "«Удачи тебе!» — собирался сказать Электроник, но не успел."
    scene bg ext_path_sunset:
        zoom 1.5 align (0.0, 0.1)
    show d_mz cry glasses_glare pioneer at cleft
    with dissolve
    mz "Спасибо за то, что потратил на меня время."
    "Женя тоже поднялась и стояла, наклонив голову так, чтобы в очках отражалось садящееся Солнце, и произносила такие слова, какие сумела подобрать, когда поняла, что Сергей сейчас уйдёт."
    "Что вот эта, мелькнувшая между ними сегодня не любовь, не дружба, не влюблённость, а так, тень взаимной симпатии, это всё, что она получила и получит от жизни. Вообще всё."
    stop music fadeout 3
    
    
    
    # "— Понимаешь, Женя, — признается ей Электроник неделей позже, уже в автобусе, когда они сядут рядом и Женя склонит голову на его плечо. — Я вдруг понял, что ты пускаешь солнечные зайчики очками мне в глаза не для того, чтобы дополнительно позлить меня, а чтобы спрятать от меня слезы. И тогда увидел тебя. Не умную и симпатичную девочку, которая мне понравилась с первого дня, не стервозную грымзу («Ну спасибо», — подумает Женя), а перепуганную, не знающую что ей делать, девушку, которая прячет свои испуг и растерянность под иронией. Которая еле сдерживается, чтобы не дать себе разреветься в моем присутствии. Которая действительно не умеет говорить о каких-то вещах. Я сам не умею, а та девушка — еще хуже. И я нарушил своё правило, рискнул и решил всё про нас двоих самостоятельно и в одиночку."    # По канону
    # "— А стервозная грымза вдруг увидела твою простоту, Сережа, — ответит Женя. — Не примитивность, а простоту («Как у отвертки», — пробурчит Электроник), гениальную простоту о которой говорят: «Без страха и упрека». Что бы ты о себе ни думал." # По канону
    
    scene dct_int_bus_window_view
    show dct_int_bus_window_view_el_mz
    with blinds
    "Это потом, уже в автобусе, когда они сядут рядом и Женя склонит голову на его плечо, Электроник признается:"
    play sound_loop sfx_bus_interior_moving fadein 3
    el "Понимаешь, Женя, я вдруг понял, что ты пускаешь солнечные зайчики очками мне в глаза не для того, чтобы дополнительно позлить меня, а чтобы спрятать от меня слёзы.{w} И тогда увидел тебя."
    el "Не умную и симпатичную девочку, которая мне понравилась с первого дня и не стервозную грымзу."
    mz "\~ Ну спасибо. \~"
    el "А перепуганную, не знающую что ей делать, девушку, которая прячет свои испуг и растерянность под иронией.{w} Которая еле сдерживается, чтобы не дать себе разреветься в моём присутствии.{w} Которая, действительно, не умеет говорить о каких-то вещах."
    el "Я сам не умею, а та девушка — ещё хуже. И я нарушил своё правило, рискнул и решил всё про нас двоих, самостоятельно и в одиночку."
    mz "А стервозная грымза, вдруг, увидела твою простоту, Серёжа."
    mz "Не примитивность, а простоту."
    el "\~ Как у отвёртки. \~"
    mz "Гениальную простоту, о которой говорят: «Без страха и упрека». Что бы ты о себе ни думал."
    stop sound_loop fadeout 2
    "Но случится это только неделей позже, когда смена закончится."
    
    
    play music tenderness fadein 3
    scene bg ext_path_sunset
    show el laugh pioneer far:
        xcenter 0.54
    show d_mz confused glasses pioneer far:
        xcenter 0.46
    with blinds
    # "А в тот день портфель упал на скамейку и Сергей, внезапно оказавшись напротив Жени, взял ее за запястья, и сказал, запинаясь, краснея и спотыкаясь через слово:"   # По канону
    "А в тот день портфель упал на траву, и Сергей, внезапно оказавшись напротив Жени, взял её за запястья и сказал, запинаясь, краснея и спотыкаясь через слово:"
    el "Тратить время на тебя, Женька, полезно, удивительно легко и приятно. И я собираюсь это так и продолжать."
    show el upset pioneer far:
        xcenter 0.53
    show d_mz shy_cry pioneer far:
        xcenter 0.47
    with dissolve_fast
    "А Женя вдруг уткнулась лицом в Электроника, уронив очки и, впервые в жизни, заплакала на людях."
    "Парализованный ужасом, Сергей только и смог, что, обняв Женю, дать ей спрятать мокрое лицо у себя на груди и слушать между всхлипами:"
    $ sunset_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "sunset"
    mz "Ты…{w=0.3} ты…{w=0.5} никто…{w=0.5} никогда…{w=0.3} никогда не…{w=0.2} не называл меня Женькой."
    stop music fadeout 2.5
    show black with dissolve2
    window hide

    pause 0.5

    
    $ night_time()
    $ persistent.sprite_time = "day"
    window auto
    play ambience ambience_music_club_night fadein 1
    scene dct_int_musclub_night_light
    show mi smile pioneer far
    show sl smile2 pioneer:
        xcenter 0.68
    show d_ma smile pioneer:
        xcenter 0.32 yalign 0.02
    with dissolve
    mi "Ребята, спасибо что пришли. Гораздо приятнее играть для кого-то, даже просто аккомпанировать, чем сидеть одной в кружке."
    
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
    "Мику смотрела на Сашу с Максимом, стоящих рядом и ещё разгоряченных после танца, и любовалась ими. Они так здорово смотрелись вдвоём, оба спортивные, светловолосые, голубоглазые и оба, одновременно, открытые и застенчивые.{w} Жалко даже, что они не вместе."
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
    scene dct_int_musclub_night_nolight with dissolve
    stop ambience fadeout 1
    pause 0.5
    
    
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 1
    scene dct_ext_music_club_verandah_night
    show mi normal pioneer far:
        xcenter 0.24
    show d_ma smile pioneer:
        zoom 0.75 xcenter 0.41 yalign 1.01
    show sl smile pioneer far:
        xcenter 0.56
    with slideawayup
    "Все трое вышли на веранду. Уже стемнело и жара отступила, была та самая комфортная температура, когда солнце уже не обжигает, а, в то же время, прогревшиеся за день воздух и земля отдают достаточно теплоты, не давая мёрзнуть."
    show sl smile pioneer at center with dissolve
    sa "Давайте посидим ещё. Не хочется расходиться."
    show d_ma smile pioneer at left with dissolve:
        zoom 1.0 yalign 0.02
    # show mi normal pioneer:
        # xcenter 0.05
    # show sl smile pioneer at center
    
    sa "Только свет не включайте, а то насекомые налетят."
    show sl smile pioneer:
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
    sa "Все подглядывали...{w} Ну, не все, конечно."
    show sl smile2 pioneer
    show mi normal pioneer
    show d_ma normal pioneer
    with dissolve_fast
    sa "Видишь ли, Максим, те соло — это просто для души. И как часть души."
    sa "Вот у Мику — музыка, у той девочки, которая написала сказку и подписалась «Мику Хатсуне», у той слова."
    show mi upset pioneer with dissolve_fast
    extend " Лена — рисует. А у меня вот такие танцы соло."
    sa "Я не против, если кто-то увидит кусочек моей души, но раскрывать свою душу специально для публики я не готова."

    # "Саша прикрыла глаза и кивнула сама себе, своим мыслям и замолчала. Мику же, непривычно немногословная, спросила."  # По канону
    
    show mi sad pioneer with dissolve_fast
    "Саша кивнула сама себе, каким-то своим мыслям и замолчала. Мику же, непривычно немногословная, спросила:"
    mi "Максимчик, завтра собрание отряда, ты готов?"
    show sl serious pioneer
    show d_ma serious pioneer
    with dissolve_fast
    d_ma "Нет, Мику.{w} А как я должен к нему подготовиться?{w} Клятву страшную выучить? Или подойти к каждому из вас и попросить проголосовать за меня?"
    show sl normal pioneer with dspr
    sa "Вообще-то, все и так проголосуют за тебя."
    show mi upset pioneer with dissolve_fast
    sa "Собрание не для того, чтобы тебя не принять, а для того, чтобы ты имел возможность отказаться. Потому что понять, что тебя ожидает, ты ещё не можешь. Но, если внутренний голос против, то лучше будет к нему прислушаться."
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
    mi "Но откуда-то же появилась эта папка. И подписано моим именем и моим почерком, Сашенька, Максимчик. И я чувствую, что могла бы так написать, ну пусть не так хорошо, но похоже. А Леночка и Сенечка отвечают совершенно непонятно."
    stop music fadeout 2.5
    pause 1
    show mi normal pioneer with dspr
    stop sound_loop fadeout 1.5
    "А потом кончилась пластинка."
    show sl smile pioneer:
        linear 0.5 ypos 0.0
    show sl smile2 pioneer with dissolve_fast:
        ypos 0.19
        linear 0.5 ypos 0.0
    sa "Пойду я, спать скоро, а надо ещё душ после танцев принять."
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
    "Они отправились, каждый к своему домику, за полотенцами, договорившись встретиться у столовой."
    show mi smile pioneer with dissolve_fast
    "А Мику смотрела вслед Максиму, уходящему по освещённой аллее, и думала, что пусть эти двое и не влюблены друг в друга, но кажется, у Саши вот-вот появится или уже появился хороший друг, и это здорово."
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Потому что Леночка, она замечательная девушка, но иногда её бывает так трудно понять."
    stop ambience fadeout 1
    show black with dissolve
    window hide
    $ renpy.music.set_volume(1.0)

    pause 0.5

    
    $ night_time()
    $ persistent.sprite_time = "day"
    window auto
    play ambience ambience_int_cabin_night fadein 1
    scene dct_int_house_of_el_night_light with dissolve
    "Шурик лежал, глядя в потолок, и ждал, когда угомонится Сыроежкин.{w} Очень хотелось, не дожидаясь утра, пойти и посмотреть на результаты расшифровки."
    show el smile pioneer close at left with dissolve
    show el smile pioneer at center with dissolve
    show el smile pioneer far at cright with dissolve
    hide el with dissolve
    "Потому что завтра, во-первых, будет неудобно перед напарником за то, что первое испытание провёл без него. А, во-вторых, вдруг там записалось что-то такое, за что потом перед Сергеем будет стыдно."
    show el laugh pioneer far at cright with dissolve
    show el laugh pioneer at center with dissolve
    show el laugh pioneer close at left with dissolve
    hide el with dissolve
    $ persistent.sprite_time = "day"                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "А сосед по домику всё никак не хотел затихать."
    show dct_int_house_of_el_night with dissolve
    
    $ persistent.sprite_time = "night"
    "Ходил по комнате взбудораженный, что-то фальшиво напевая."
    show d_el grin shorts at cleft with dissolve
    extend " Всё порывался рассказать Шурику, какая замечательная девушка работает в библиотеке."
    show d_el upset nude at cright with dissolve
    extend " И выяснял, не припрятан ли у Шурика в чемодане флакон с одеколоном."
    hide d_el with dissolve
    "А потом, когда уже улёгся, всё мечтательно вздыхал и ворочался с боку на бок. И уснул далеко после отбоя."
    stop ambience fadeout 5
    
    
    play music music_list['you_lost_me'] fadein 5
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
    extend " и, избегая чужого внимания, свернул направо, чтобы обогнуть тёмное здание административного корпуса с северной стороны и, через полосу молоденьких сосенок, выйти на дорожку, соединяющую музыкальный кружок с главной аллеей."
    scene dct_ext_forest_dark_night
    show sh upset pioneer close
    with fade
    "То, что он плохо ориентируется в ночном лесу, Шурик понял почти сразу."
    "Захотел повернуть назад, на свет фонарей освещавших аллею, но, услышав как хлопнула дверь в крайнем домике, передумал."
    th "Ещё не хватало, чтобы увидели, как я из кустов выбираюсь."
    "Поэтому оставалось двигаться только вперёд, используя для ориентировки исключительно внутренний компас потомственного горожанина, не бывавшего нигде, дальше городского парка с аттракционами, куда восьмилетнего Шурика водила мама."
    show sh rage pioneer close with dissolve_fast
    "Это было… нелегко."
    "Паутина липла к лицу, ноги спотыкались о невидимые кочки, ветки норовили сбить очки с лица и приходилось очки придерживать левой рукой, потому что со зрением минус шесть передвигаться без очков в ночном лесу остаётся только на ощупь."
    scene bg ext_path2_night with squares
    "Так что, когда впереди показался свет, Шурик обрадовался и зашагал энергичнее."
    th "Кажется, это фонарь, и я вышел к поперечной аллее."
    extend " Сейчас мне налево, и я окажусь на перекрестке."
    stop music fadeout 1
    scene dct_ext_musclub_night_lantern_light with irisout
    play music music_list['timid_girl']
    show mi shocked pioneer with dissolve
    mi "Ой, Сашечка, а что ты здесь делаешь? Ты ко мне пришёл? Но уже поздно. Я вот задержалась у себя в кружке, играла и думала, думала и играла, пересела в кресло и задремала. А проснулась — уже поздно. На часы посмотрела — отбой давно был, а я и не слышала. А жалко, мне так нравится Максима слушать, ведь когда живой человек играет, это гораздо лучше, чем запись."
    sh "Здравствуй, Мику. Я…{w} гулял.{w} И заблудился в лесу, и к твоему кружку вышел случайно."
    show mi upset pioneer with dissolve_fast
    th "Вот ведь, как невовремя!"
    th "Сейчас пойдут разговоры, она же не удержится. А попросить не болтать, так ещё хуже выйдет."
    show mi serious pioneer with dspr
    th "Хотя, попробую. Девочка она добрая… \~{w}\n«Микс!» мелькнуло в сознании.\n\~ …и понимающая, хоть и болтушка."
    sh "Мику, можно тебя попросить об одной вещи?"
    show mi smile pioneer close with dissolve_fast
    mi "Конечно, Сашечка."
    sh "Не рассказывай никому, что я заблудился. Неудобно."
    mi "Конечно-конечно, Сашечка. Я — могила! Но пойдём, я тебя до домика провожу. Вот тропинка. А то ты опять куда-нибудь заблудишься."
    "Приговаривая так, Мику убирала хвою, сор, мелкие веточки с одежды Шурика. Материализовав откуда-то носовой платок и поплевав на него, стёрла паутину и попыталась оттереть следы смолы с лица."
    show mi shy pioneer close with dissolve_fast
    mi "Только…{w=0.7} Сашечка, может тебе сначала к умывальникам? Мыло и полотенце у меня в кружке есть. А я подожду."
    "Вот к умывальникам идти было совершенно незачем. Еле-еле удалось доказать Мику, что до клубов идти ближе и по асфальту, что там есть раковина, что там есть и полотенце, и мыло."
    scene dct_ext_houses_night_lantern_light with pushright
    "Но отделаться от Мику не удалось, и Шурику, сопровождаемому японкой, пришлось идти по самой середине ярко освещённой аллеи, под её бесконечное чириканье, привлекая внимание всех, кто хотел и мог это увидеть."
    "Кажется, кто-то увидел, кажется, чья-то тень мелькнула от фонаря в кусты."
    show mi laugh pioneer close at fleft with dissolve_fast
    mi "Ну всё, хи-хи, Сашечка, теперь нас точно в парочку запишут."
    hide mi with dissolve_fast
    "Но Шурику было всё равно."
    "Шурик, оставив щебетанье Мику как звуковой фон, размышлял, как ему достаточно вежливо и не обижая, избавиться от общества японки, но так ничего и не успел придумать."
    stop music fadeout 1
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_clubs_night
    show mi smile pioneer close at fright
    with dissolve
    mi "Вот и пришли, Сашечка. Ой, а там же ваша машина, мне Серёжа про неё рассказывал, когда табуретку в кружке просил. А можно на неё посмотреть?"
    stop ambience fadeout 1
    
    
    play music my_2nd_summer fadein 2.5
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
    
    # "Мику посмотрела на Шурика очень серьезно, будто решая, можно ли тому доверять."    # По канону

    show sh normal pioneer with dspr
    "А вот с результатами было не ясно."
    scene dct_mi_in_cage with squares
    "Потому что, пока Мику рассматривала интерьеры кружка кибернетики, пока она хихикала, сидя внутри клетки: «Я обезьянка Мику, умею петь и играть на всех инструментах. Дорогая публика, подходите поближе, не стесняйтесь! — И, внезапно погрустнев. — Сашечка, неужели я и есть, всего лишь такая забавная учёная обезьянка?»"
    "Пока Мику крутилась, совершая один оборот за десять минут, на своем табурете, наблюдая за Шуриком так и оставшимися печальными глазами, тот сидел перед монитором и пытался понять, что же выдала ему программа расшифровки."
    scene dct_int_clubs_male_night_light_mon
    show sh serious pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    with dissolve
    "Теоретически, это должно было быть что-то вроде отдельных кадриков, сменяющих друг-друга как слайды и склеенные в тридцатисекундный ролик."
    "И эти кадрики должны были служить подсказками для самого Шурика, или любого другого испытуемого, кто там перед этим сидел на вращающемся табурете. Большего, от имеющийся у кибернетиков аппаратуры, и ждать было нельзя."
    "А сейчас, с разрешением 640 х 200, с монитора на Шурика смотрело его собственное лицо, ну, почти его собственное."
    scene dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_al:
        xcenter 0.5 ycenter 0.45
    with dissolve
    th "Кто-то меня состарил, лет на двадцать."
    th "Где-то ошибка в программе."
    scene dct_int_clubs_male_night_light_mon
    show sh normal pioneer close:
        xzoom -1.25 yzoom 1.25 anchor (0.5, 0.56) pos (0.3, 1.0)
    with dissolve
    th "Утешает одно, какой-то результат мы получили."
    show dct_clubs_male_comp_night_light_mon
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    show dct_clubs_male_comp_night:
        alpha 0
        pause 1.5
        linear 1 alpha 1
    # "Шурик запустил программу дешифровки, помог выбраться из клетки Мику, и машинально, совсем не задумываясь и не слыша себя, ответил на ее вопрос, заданный десять минут назад."  # По канону
    
    "Шурик запустил программу дешифровки, и выключил монитор."
    scene dct_int_clubs_male2_night_zoom
    show sh serious pioneer
    show mi sad pioneer at fright
    with dissolve
    "Потом помог выбраться из клетки Мику, и машинально, совсем не задумываясь и не слыша себя, ответил на её вопрос, заданный десять минут назад."
    scene dct_int_clubs_male_night_light
    show sh serious pioneer at cleft:
        xcenter 0.4
    show mi shocked pioneer at fleft
    with dissolve
    sh "Мику, если даже и так. Подумай о том, что задав себе такой вопрос, ты сделала первый шаг из клетки."
    "А потом, уже придя в себя, продолжил более впопад."
    show sh normal pioneer with dspr
    sh "Результаты будут завтра утром, но где-то я ошибся, поэтому истолковать их правильно, скорее всего, не получится…"
    show mi serious pioneer with dissolve_fast
    extend " В общем, завтра, после подъёма, встречаемся здесь."
    hide sh
    hide mi
    with dissolve
    show dct_int_clubs_male_night with dissolve
    $ persistent.sprite_time = "day"                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Они, вдвоём с притихшей Мику, прибрали всё в кружке как было, заперли здание."
    
    $ persistent.sprite_time = "night"
    scene bg ext_clubs_night with slideawayup
    "Шурик проводил девушку до перекрестка, откуда Мику убежала по боковой аллее, зацокав каблучками."
    scene dct_ext_houses_night_lantern_light
    show mi normal pioneer far at cleft
    with pushleft
    mi "Нет-нет, Сашечка, дальше провожать не надо, дальше я сама, короткой дорогой."
    scene dct_ext_house_of_el_night with fade
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    "А Шурик, вернувшись к себе в домик, проспал без сновидений до самого подъёма, даже не задумавшись о том, что уверенно добрался до него, тоже через лес, тоже самой короткой дорогой, так, как будто исходил тут всё на тысячу рядов."
    stop music fadeout 2.5
    show black with dissolve
    window hide
    
    pause 1
    
    
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day fadein 1
    scene dct_ext_house_of_el_day with dissolve
    window auto
    "Утром, однако, никто и ничего не сказал про то, что видел, как Шурик и Мику поздно вечером, вдвоём, шли к клубам, а потом возвращались обратно."
    
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
    "Сашка пробежала в сторону стадиона, счастливый Сыроежкин, с первыми звуками горна, подскочил и убежал на пост, к домику Жени."

    scene black with dissolve
    scene bg ext_house_of_mt_day
    show unblink
    "Вожатая, додрёмывая в шезлонге, наблюдала за постепенным пробуждением лагеря и думала о том, что завтра прибывает опоздавший пионер, что придётся селить Алису у себя, а опоздавшего — вместе с Максимом, в Алисином домике."
    show blinking
    th "Ох, и ругаться будет Рыжая."
    "Небо с запада постепенно затягивало тучами, да ещё и неприятный такой ветерок потянул с реки."
    stop sound fadeout 2.5
    th "Кажется, погода всё портит, кажется, весь день сегодня будем сидеть по домикам."
    play sound dct_sfx_horn_assembly_through_loudspeaker
    "Прозвучал сигнал сбора, пора и на линейку. Нет, горнист в лагере - это, действительно, здорово. Ольга поднялась и пошла на площадь, чтобы там довести до пионеров программу сегодняшнего дня."
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
    "Семён сзади чуть слышно фыркнул, он всегда фыркает при этой команде, но ничего не объясняет."
    "Средний отряд, подгоняемый Ульяной, встал на своё место."
    show d_us smile sport behind mt:
        xcenter 0.75 ypos -0.05
    with dissolve
    "Прибежали малыши, построились."
    show d_sf normal pioneer with dspr
    "Солидно выступили старшие: Мику, Лена, Саша, Алиса на правом фланге."
    show d_us normal sport with dspr
    th "Стоп, а где остальные?"
    "Но спрашивать не пришлось, со стороны домиков прибежали Женя с Сергеем Сыроежкиным, а со стороны клубов — Шурик."
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
    "Как обычно, в эти минуты, разум у Ольги отключился, а текст пошёл на полном автопилоте."
    mt "…а программу спортивного праздника, до вас доведет мой заместитель."
    show mt normal panama pioneer behind d_sf:
        xcenter 0.55
    show d_sf normal pioneer:
        zoom 1.25 xcenter 0.3 ypos -0.05
    with dissolve_fast
    me "Вот скажите, товарищи пионеры. А чего вы ждёте от сегодняшнего праздника?"
    kids "Бега!\nПлавания!\nФутбола!"
    show d_sf smile pioneer with dspr
    "На слове «Футбол» Семён заинтересованно повернул голову в сторону кричавшего, но промолчал."
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
    mt "\~ Вот клоун. Сейчас скажет, что... \~"
    
    play sound "<from 2.07 to 4.70>mods/dublicate_completed/Sounds/sfx/dct_sfx_discharge.ogg"
    stop ambience fadeout 2
    play sound_loop dct_ambience_light_rain fadein 2
    $ renpy.pause(0.8,hard=True)
    show mt surprise panama pioneer
    show d_sf normal pioneer
    show d_us hurt sport
    with dspr
    $ renpy.pause(0.9,hard=True)
    stop sound fadeout 0.9
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
    "Физрук не стал дожидаться решения вожатой и перехватил инициативу."
    scene dct_ext_сentral_alley_from_dining_hall_to_west_after_rain at running
    show dct_overcast_rain_1 at running:
        xzoom -1.0
    show dct_overcast_rain_2 at running:
        xzoom -1.0
    with squares
    "А уже, под хорошим таким ливнем, оставив Ольгу с Ульяной управляться в столовой с пионерами, побежал с Алисой к складу за плащами, прозрачными накидками из пленки: красными для малышей, жёлтыми для среднего отряда, синими для старшего и бесцветными для персонала."
    stop sound_loop fadeout 1.5
    scene black with dissolve
    
    pause 0.5
    
    
    play music music_list['get_to_know_me_better']
    scene white with dissolve
    "Женя в хорошем настроении и Женя в настроении обычном - это два разных человека."
    show ext_house_of_sl_day
    show el laugh pioneer close at right
    show int_house_of_sl_day
    show mi upset pioneer far at cright
    show mz laugh glasses pioneer close at left
    with dissolve
    "Начиная с самого утра, когда поздоровалась с куда-то торопящейся соседкой, и выбежала навстречу Сергею, нет — Серёже."
    show int_house_of_sl_day:
        linear 1 ycenter -0.5
    show mi upset pioneer far at cright:
        linear 1 ycenter -0.5
    show mz shy glasses pioneer close at left with dissolve_fast
    mz "Доброе утро, я рада тебя видеть."
    el "А как я рад, Женя."
    hide int_house_of_sl_day
    hide mi
    "И вот это: «как я рад», — ещё добавило градус счастья. Даже торчащие у Сергея из кармана шорт полотенце и зубная щётка вызвали только умиление."
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
    show int_house_of_sl_day behind el:
        xcenter 1.5
        linear 1 xcenter 0.5
    hide ext_house_of_sl_day
    pause 1
    show mi upset pioneer behind el with dissolve
    "Зашла Мику, отчего-то грустная и серьёзная, кивнула Сергею."
    mi "Женя, Серёжа, не опоздайте на линейку."
    show ext_house_of_sl_day behind int_house_of_sl_day
    hide mi with dissolve
    show int_house_of_sl_day:
        pause 1.5
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
    "Романтическая линейка, когда можно стоять рядом и поминутно оглядываться друг на друга, и касаться случайно руками. Взяться за руки ни Сергей, ни Женя пока ещё не решались."
    scene dct_ext_dining_hall_near_rain with pushleft
    $ persistent.sprite_time = "day"                          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Романтическая пробежка под дождём к столовой, когда Сергей всё норовил стащить с себя рубашку, чтобы прикрыть ею Женю."
    
    $ persistent.sprite_time = "night"
    scene black
    show dct_ext_dining_hall_near_rain
    show dct_int_dining_hall_people_rain
    with slidedown
    "В столовой Женя перехватила взгляд Шурика."
    show d_mz smile2 glasses pioneer close at left with dissolve
    mz "На тебя Шурик ворчать не будет? Если будет, ты скажи мне. Я его на место поставлю."
    show d_el smile2 pioneer close at right with dissolve
    el "Не знаю."
    "Сергей легкомысленно пожал плечами."
    show el grin pioneer close as d_el with dspr
    el "Сейчас провожу тебя до библиотеки и проверю."
    hide d_mz
    hide d_el
    with dissolve
    show dct_int_dining_hall_people_rain:
        linear 1 ycenter -0.5
    show dct_ext_dining_hall_near_rain:
        pause 1.7
        linear 1 xcenter 1.5
    show dct_ext_houses_rain:
        xcenter -0.5
        pause 1.7
        linear 1 xcenter 0.5
        pause 0.7
        linear 1 xcenter -0.5
    show dct_ext_library_rain:
        xcenter 1.5
        pause 3.4
        linear 1 xcenter 0.5
    "Они забрали у Семёна накидки и, стараясь передвигаться по поребрику, чтобы не намочить ноги, побежали под дождём в библиотеку."
    "И вот, после того как Сергей убежал наконец в свой кружок..."
    scene dct_int_library_rain
    show d_el rain mirror:
        xcenter 0.6
    show mz shy pioneer:
        xcenter 0.4
    with blinds
    el "Женя, у меня там сегодня опыт важный, я побежал!"
    hide d_el with dissolve
    "После этого Женя десять раз поправила на нём капюшон накидки, прежде чем выпустить из помещения библиотеки."
    hide mz with dissolve
    "Потом следила за ним в окно и махала рукой, пока Сергей не скрылся за поворотом аллеи."
    show dct_int_library_rain_lamp:
        alpha 0
        pause 1.5
        linear 0.25 alpha 1
    
    # ".......... — Женя включила настольную лампу и, выбрав книжку, соответствующую настроению — романтическую и теплую, устроилась в кресле, закинув ноги на журнальный столик."  # По канону
    
    "И вот, после того как Сергей убежал наконец в свой кружок, Женя включила настольную лампу и, выбрав книжку, соответствующую настроению — романтическую и тёплую, устроилась за столом, забравшись с ногами на стул."
    "Пролистала пару страниц, подняла глаза на зеркало, но под этим углом отражения своего не увидела."
    show dct_int_mirror_in_library with squares
    "Поэтому произнесла просто, обращаясь в пустоту:"
    mz "Я хочу сказать, Евгения, что вы, определенно, влюблены.{w} Это замечательно, но, если бы не ваша мнительность, вы бы не потеряли целую неделю так бездарно."
    hide dct_int_mirror_in_library with squares
    "Улыбнулась своим мыслям и продолжила чтение под шум дождя."
    $ persistent.sprite_time = "night"# Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Почти невероятно, что кто-то из пионеров собёрется в такой ливень в библиотеку."
    $ persistent.sprite_time = "day"
    show d_mz hope pioneer close at fleft with dissolve
    th "И как там Серёжа? Не промок ли, пока бежал в свой кружок?"
    show d_mz sceptic pioneer close at fleft with dspr
    th "Надо будет, чтобы он телефон сюда провёл. Из кружка в библиотеку."
    show d_mz smile pioneer close at fleft with dissolve_fast
    th "Тогда в следующий раз я буду знать, что с ним всё в порядке."
    stop music fadeout 1
    show black with dissolve
    
    pause 0.5
    
    
    play ambience ambience_int_cabin_day fadein 1
    play sound dct_sfx_horn_rise_through_loudspeaker
    scene dct_int_house_of_el_day with blinds
    pause 0.5
    show d_el laugh nude far at right with dissolve
    show d_el laugh shorts at cright with dissolve
    show el laugh pioneer close at center as d_el with dissolve
    hide d_el with dissolve
    # "Сыроежкин убежал, едва протрубили подъем и даже чуть раньше."  # По канону
    "Сыроежкин убежал, едва протрубили подъём."
    show sh normal_serious pioneer dct with dissolve
    "Шурик встал, вспомнил о договорённости с Мику."
    show sh smile pioneer close with dissolve_fast
    "Порадовался тому, что не придётся ничего говорить соседу."
    hide sh with dissolve
    "И, для начала, отправился к умывальникам."
    stop sound fadeout 1.5
    stop ambience fadeout 1
    scene black with squares
    window hide
    
    pause .5

    
    play music music_list['you_won_t_let_me_down'] fadein 1
    $ set_mode_nvl()
    $ persistent.sprite_time = "day"
    window show
    scene dct_dormitory_at_range with dissolve
    "Александр Трофимов-оригинал, заведующий лабораторией спецавтоматики, стоял у общежития, кутаясь в черное пальто от стылого, тянущего со стороны полигона, ветра, и ждал машину.{w} Хотелось закурить, но, по закону подлости, как только закуришь, машина обязательно подойдёт, а курить в кузове Александр почему-то стеснялся."
    "\nМашины всё не было, Александр уже собрался сунуть руку за сигаретами в карман, когда за углом загудело и, со стороны центральной улицы городка, выкатилась колонна из трёх Уралов и двух БТР."
    show dct_dormitory_at_range_Ural_BTR with dissolve
    extend " Знакомый уже майор узнал Александра, махнул рукой, крикнув: «В третью машину!», — и открыл планшет, чтобы поставить там ещё одну галочку.{w} Александр подхватил зажатый между ног портфель, подбежал к Уралу, кивнув прапорщику, сидящему рядом с водителем и, откинув полог тента, полез в кузов.{w} Его подхватили несколько рук, приняли портфель, помогли забраться самому, устроили на одной из поперечных лавок."
    scene dct_convoy_of_trucks with dissolve
    "Урал дёрнулся и покатил по улицам городка."
    "\nАлександр огляделся, поздоровался. Вокруг сидели более-менее знакомые люди, командировочные и гражданский персонал полигона: инженеры из почтовых ящиков, ремонтники, научные сотрудники различных номерных НИИ, пара учительниц из местной школы, в том числе классная руководительница дочери."
    "\nУрал куда-то ехал, поворачивая в несколько приёмов на узких улочках.{w} Потом — короткая остановка, полог открыли и в кузов заглянул дежурный по КПП. Пробежал глазами по пассажирам и исчез, скрытый упавшим пологом.{w} Александр услышал: «Проезжайте», — и колонна, медленно набирая скорость, покатила в сторону аэродрома."
    
    
    show black:
        alpha 0
        linear 1 alpha 1
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    

    "А потом — резкое торможение и тишина.{w} Только приглушенные голоса снаружи, в которых угадывались попытки связаться по рации.{w} Пассажиры Урала, выждав несколько минут, полезли наружу, полез и Александр."
    show dct_road_bus_BTR:
        alpha 0
        pause 1.5
        linear 1.5 alpha 1
    "\n И первое, что он увидел, был зад знакомого автобуса, торчащий из кювета.{w} Тут же стоял побитый БТР, около которого кто-то бинтовал кого-то. Но это было не важно, потому что на пассажирах автобуса не было ни царапинки, но и живых среди них тоже не было.{w} Некоторые ещё дышали, но это ненадолго."
    $ renpy.music.set_volume(0.0, delay=1)
    scene black with squares
    window hide
    
    
    $ set_mode_adv()
    
    play sound_loop sfx_water_sink_stream fadein 1
    scene bg ext_washstand2_day with dissolve_fast
    window show
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
    # play sound_loop crush fadein 2
    window hide
    scene black with squares
    
    $ renpy.music.set_volume(1.0, delay=1.5)
    $ set_mode_nvl()
    window show
    "Когда начали изучать первых двойников, когда начали изучать их оригиналов, обнаружили в мозгу, сперва у людей-копий, потом у высокоинтеллектуальных животных, а потом и всех людей некую область, отвечающую за его личное Я. Своего рода маяк-идентификатор.{w} И в недрах института Глафиры Денисовны, возникла теория, одним из пунктов которой было так называемое нейтринное кольцо.{w} Считалось, что таких колец существует бесконечно много, и каждой человеческой или не человеческой личности соответствует одно кольцо.{w} Как только личность возникала, сразу же начинал работать такой маяк, сразу же устанавливалась связь между ним и свободным на тот момент кольцом."
    "\nПессимисты утверждали, что это не более, чем математическая конструкция, мол, где вы видели  нейтрино вживую, да ещё и в составе кольца из себе подобных?{w} Мистики, всегда имеющиеся в подобных учреждениях, считали кольцо доказательством существования души, Бога, богов, переселения душ — в зависимости от исповедуемого учения.{w} А с точки зрения энтузиастов науки, такие кольца действительно существовали в некой сопряжённой с нашей вселенной с иными физическими свойствами, и связь между вселенными осуществляется через пространственные вакуоли, подобные тем, где находились пионерский лагерь «Совенок» или посёлок Шлюз, и принадлежащие одновременно обеим вселенным."
    "\nКак бы то ни было, но теория работала.{w} Находясь внутри вакуоли, можно было скопировать такое кольцо, и тогда в вакуоли появлялось несколько организмов-копий, можно было воздействовать на кольцо, изменяя характеристики организма, а можно было разорвать связь кольца и организма. Организм при этом прекращал функционировать, мгновенно и безболезненно."
    "\nТо, что создавалось в лаборатории Александра и испытывалось на полигоне, как раз и разрывало такую связь, создавая при этом временную вакуоль, прямо внутри нашего пространства.{w} Из этой штуки и выстрелили по автобусу.{w} Целились в БТР, с тем, чтобы пассажиров автобуса захватить в заложники, а попали в автобус. Просто временная вакуоль образовалась вокруг объекта с наибольшим числом организмов.{w} То, что нападавшие были уничтожены огнем из БТР, Александру было уже всё равно."
    $ renpy.music.set_volume(0.0, delay=1)
    # stop sound_loop fadeout 1
    window hide
    
    $ set_mode_adv()
    play ambience ambience_camp_center_day fadein 1
    scene dct_ext_house_of_el_day with squares
    window show
    "Холодная вода привела ненадолго Шурика в чувство. Ровно настолько, чтобы он умылся и дошёл до домика."
    stop ambience fadeout 1
    window hide
    

    $ set_mode_nvl()
    
    $ renpy.music.set_volume(1.0, delay=1)
    scene black with squares
    window show
    "Дальнейшие события дня в памяти Александра сохранились плохо, отрывками.{w} Вот он лезет внутрь автобуса, вот он берет из руки Яны-младшей бумажку с номером телефона, вот он сидит на асфальте перед автобусом, а вот он уже в салоне самолёта."
    "\nВ институте к трагедии Александра отнеслись с пониманием и не тревожили.{w} Все хлопоты по сворачиванию лаборатории и подготовке к эвакуации взял на себя его заместитель, а Александр сидел, заперевшись у себя в кабинете, и только рассматривал фотографию жены и дочери. Хотел убить себя, но никак не мог решиться."
    "\nПоэтому, когда случился пожар на маяке, Александр сознательно полез тушить, невзирая на очевидную опасность, и не ошибся. Ожоги, отравление газами, выделяемыми горящим пластиком.{w} Ему оставалось жить не более двух суток, когда Виола решилась и вот так, впервые, не считая себя самой, на практике создала настоящие организмы-подлинники: Александра и Анатолия, тоже пострадавшего при пожаре."
    $ renpy.music.set_volume(1.0, delay=0)
    stop music fadeout 1
    window hide
    
    
    $ set_mode_adv()
    play ambience ambience_int_cabin_day fadein 1
    scene dct_mi_morning_house with blinds
    window auto
    "Мику, проснувшись, сразу вспомнила об окончании вчерашнего вечера."
    "О Шурике, испачканном, взъерошенном и непонимающем, куда он попал, выпавшем на неё из кустов, когда Мику запирала здание музыкального кружка.{w} О совершенно материнском желании этого Шурика умыть и почистить.{w} О визите в кружок кибернетики и загадочной установке, стоящей в центре кладовки, и занимающей почти всё свободное место."
    stop ambience fadeout 1
    
    # "О визите в кружок кибернетики и загадочной установке, стоящей в центре помещения, прямо на столе." # По канону
    
    play sound_loop ambience_int_cabin_night fadein 1
    scene dct_empty_in_cage with dissolve
    "Установка чем-то напоминала гигантскую клетку, а Мику, оказавшись внутри клетки, почувствовала себя экспонатом какого-то вивария."
    stop sound_loop fadeout 1
    
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_sl_day
    show mi grin pioneer close
    with dissolve
    "Мику улыбнулась, услышанным два дня назад словам Серёжи: «Мы собираемся познать тайны человеческого мозга, Мику, — Сыроежкин, когда начинал говорить о науке, всегда говорил пафосно и с придыханием, — прочитать забытые воспоминания и понять механизмы мышления!»"
    
    # "А потом всплыл в памяти недавний сон: журчащая за бортом лодки вода и надвигающаяся громада моста, на фоне черной тучи, пустой общий вагон, по которому сквозняк гоняет какие-то бумажки, промороженный автобус, зимний город, где она никогда не бывала, толстая тетка буфетчица, наливающая кофе, спутник, на лицо которого нельзя смотреть." # По канону
    
    show mi upset pioneer close with dissolve_fast
    "А потом всплыл в памяти недавний сон:"
    stop ambience fadeout 1
    
    play music music_list['tried_to_bring_it_back'] fadein 1
    scene dct_ext_cliff_day_zoom
    show dct_ext_cliff_day_boat_bow
    with dissolve
    "Журчащая за бортом лодки вода"
    show dct_railway_embankment_overcast:
        alpha 0
        linear 1 alpha 1
    extend " и надвигающаяся громада дамбы, на фоне чёрной тучи"
    show dct_int_train_day:
        alpha 0
        linear 1 alpha 1
    extend ", пустой общий вагон, по которому сквозняк гоняет какие-то бумажки"
    show dct_int_410bus_night:
        alpha 0
        linear 1 alpha 1
    extend ", промороженный автобус"
    show dct_intro_xx:
        alpha 0
        linear 1 alpha 1
    extend ", зимний город, где она никогда не бывала"
    show dct_int_cafe:
        alpha 0
        linear 0.8 alpha 1
    show dct_cof:
        alpha 0
        pause 1.2
        linear 0.7 alpha 1
    extend ", уютная кофейня и чашка ароматного горячего кофе"
    show dct_life_line_fin:
        alpha 0
        linear 1 alpha 1
    extend ", спутник, на лицо которого нельзя смотреть."
    scene white
    show d_sf normal pioneer at cleft:
        zoom 1.25 ycenter 0.74
    show d_us normal dress at cright:
        zoom 1.25 ycenter 1.04
    with dissolve
    "И непонятное желание заботиться о Семёне с Ульяной, оберегать их от всего плохого."
    $ persistent.sprite_time = "day"      # Прописано, чтобы при обратной перемотке цвета не сбивались.
    th "Нет, они очень хорошие люди, но почему к той же Саше, я ничего такого не чувствую?"
    scene black with dissolve_fast
    $ persistent.sprite_time = "night"
    scene dct_ext_musclub_night_lantern_light
    show sh upset pioneer
    with dissolve_fast
    "И, как-то интуитивно почувствовав, что завтра будет поздно, уговорить Шурика на эксперимент: «Сашечка, ну пожалуйста, пожалуйста, пожалуйста, мне это очень важно, и именно сегодня, сейчас!»"
    scene dct_mi_in_cage with dissolve
    $ persistent.sprite_time = "day"
    "А потом нужно было сидеть неподвижно на вращающемся табурете, смотреть на медленно поворачивающиеся вокруг тебя стены и стараться ни о чём не думать."
    stop music fadeout 1
    

    play sound_loop ambience_camp_center_day fadein 1
    scene bg ext_clubs_day
    show mi dontlike pioneer far
    with blinds
    "И вот сейчас Мику, обогнав Шурика, стояла возле крыльца клубов, нетерпеливо притоптывая левой ногой."
    show sh normal pioneer far at right with MoveTransition(1.5, enter=_moveright, enter_time_warp=_ease_time_warp)
    "Что-то изменилось в нём за ночь, что-то появилось ещё, что иногда диссонировало с образом рассеянного учёного, а что именно — Мику пока понять не могла."
    show mi normal pioneer far with dissolve_fast
    sh "Доброе утро, Мику."
    show mi upset pioneer far with dissolve_fast
    th "Вот и опять. Вчерашний Шурик, скорее всего, забыл бы поздороваться."
    th "И взгляд его изменился: цепкий, слегка удивленный чему-то, и ещё печаль пополам с тоскою, на самом дне взгляда."
    show mi serious pioneer far
    show sh serious pioneer far
    with dspr
    mi "Доброе утро ещё раз, Сашечка. С тобой всё в порядке?"
    show sh surprise pioneer far with dspr
    sh "Что? А, да, конечно."
    show mi normal pioneer far with dspr
    th "нет, это уже прежний Шурик."
    stop sound_loop fadeout 1
    
    
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_clubs_male_day with slidedown
    "В кружке ничего не изменилось. Сразу бросились в глаза оставленные вчера Шуриком около раковины полотенце и мыло."
    # ", а потом уже Мику обратила внимание на видеомагнитофон, промотавший кассету и отключившийся мигающий курсором монитор. И торчащие отовсюду острые железки, провода, инструменты, так что приходилось перемещаться, придерживая юбку обеими руками." # По канону
    
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 1
    scene dct_clubs_male_comp_day
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with dissolve
    "Шурик скинул со стула стопку каких-то чертежей, сел перед монитором, и начал набивать на клавиатуре последовательность команд, читая появляющиеся ответы и удовлетворённо кивая или морщась, в зависимости от отклика."
    stop sound_loop fadeout 1
    
    
    scene bg int_clubs_male_day
    show sh serious pioneer close at cright:
        ycenter 0.73
    show mi normal pioneer close at left
    with dissolve
    sh "Вот, Мику. Как испытуемому, тебе предоставляется право самой нажать на кнопку и первой посмотреть результаты расшифровки твоей памяти."
    show sh serious pioneer close:
        linear 0.5 ycenter 0.5
    show mi surprise pioneer close with dissolve_fast
    sh "Ты внесла бесценный вклад в развитие науки о человеческом мышлении, в раскрытие тайн мозга."
    show sh normal pioneer close with dspr
    "А потом вдруг взгляд и интонации Шурика изменились, и он вполголоса, и с явным сочувствием, добавил."
    show mi serious pioneer close with dissolve_fast
    sh "Знаешь, посмотри это сама, одна, а потом решишь, что с этим делать."
    show sh serious pioneer close with dspr
    "Но сразу же опять возник старый Шурик и продолжил с напором."
    sh "Интересы науки, Мику, требуют отказаться от личных капризов!"
    show mi serious pioneer close:
        pause 0.5
        ease 1.2 xcenter 0.65
        linear 0.5 ycenter 0.73
    hide sh with dissolve
    "Шурик вышел, оставив Мику наедине с компьютером, а девочка, усевшись на ещё тёплый стул, занесла руку, зажмурилась и отчаянно нажала на клавишу «Ввод»."
    stop ambience fadeout 1
    window hide
    

    $ set_mode_nvl()
    
    play music homeworldcollapse fadein 1
    scene dct_ext_laboratory_of_d_sh
    show dct_d_sh_in_lab_window
    show black
    with squares
    window show
    "Александр Трофимов-подлинник, на второй цикл окреп настолько, что Виола отпустила его из медпункта."
    show black:
        linear 1 alpha 0
    extend " Он сидел в трёхэтажном модуле, в своей бывшей лаборатории и смотрел, как на площади, у ног истукана, совещается о чём-то весь оставшийся персонал института: Глафира Денисовна, Виола-подлинник, Анатолий-подлинник и Семён Персунов-дубликат.{w} Последний, официально не относился к персоналу, но, каким-то образом, сумел влиться в остатки коллектива, может быть, как активный представитель бесчисленных пассивных миксов и копий, населявших узлы Сети.{w} Александра это особо не интересовало, Александр занимался исключительно личными делами."
    "\nКогда галлюцинации — побочные эффекты переноса сознания и фантомные боли — наследство умершего старого тела прошли, когда прошёл психологический шок и Александр примирился со своим новым статусом, он вернулся мыслями к своей погибшей семье.{w} Новый же статус подсказал ему и выход. То, что считал неприемлемым для себя оригинал, казалось возможным для подлинника. Александр решил воссоздать одну из Ян."
    hide dct_d_sh_in_lab_window with dissolve
    "\nИ вот, пока остальные четверо переводили Сеть в автономный режим функционирования, пока корректировали систему циклов, пока изменяли топологию Сети, оставив непосредственный доступ к Шлюзу только из двух узлов, Александр творил.{w} Нужно было: создать компактное электронное устройство излучающие сигналы, похожие на ряд сигналов человеческого мозга;{w} разработать конструкцию робота и заучить её наизусть;{w} закинуть в первый узел сети необходимые для строительства робота материалы;"
    show black:
        pause 1
        linear 1 alpha 1
    extend " продумать и запрограммировать техническую личность-копию — Шурика Трофимова."
    $ renpy.music.set_volume(0.0, delay=1)
    window hide
    
    
    $ set_mode_adv()
    
    play ambience ambience_int_cabin_day fadein 1
    play sound_loop sfx_computer_noise fadein 1
    scene dct_clubs_male_comp_day
    show dct_clubs_male_comp_table:
        xcenter 0.5 ycenter 0.45
    with squares
    window show
    sh "Мику, садись на мое место. Сейчас я выйду, и ты нажмёшь вот эту кнопку."
    sh "Что ты увидишь, я не знаю. Какие-то подсказки для твоей памяти."
    mi "Я поняла. Спасибо, Сашечка. Ты что, куришь?"
    sh "Сегодня да, Мику."
    "Шурик, не скрываясь, открыл и закрыл тайник с сигаретами."
    sh "Так надо."
    stop sound_loop fadeout 1
    stop ambience fadeout 1
    window hide
    

    $ set_mode_nvl()
    
    $ renpy.music.set_volume(1.0, delay=1)
    scene bg int_mine_coalface
    show black
    with squares
    window show
    show black:
        linear 1 alpha 0
    "Действуя по своему плану, Александр заложил в первом узле, в пещере, это самое электронное устройство, как он его однажды назвал — «ловушка для души».{w} Вся задача этого устройства состояла в том, чтобы, имитируя человеческий мозг, привязать к себе нейтринное кольцо.{w} Практически, вероятность этого события была минимальной и ждать предстояло долго."
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
    "\n Чтобы не тратить время на ожидание, Александр потребовал заглушить своё сознание Выключателем и жил в своём узле, в виде Шурика, такого же, как и все его копии в прочих узлах."
    show int_mine_coalface behind adl_sh
    show 3500_sh serious pioneer
    with dissolve
    extend " Но, на одиннадцатый день двухнедельного цикла, сознание возвращалось к Александру и он спускался вниз, в пещеру, к своему прибору, проверяя, не сработала ли ловушка.{w} Что при этом происходило с его копиями в других узлах Александра не интересовало — эгоизм тоже является движущей силой Вселенной, наравне с любовью, страхом и ленью."
    show 3500_sh normal pioneer with dspr
    "\n И вот, в первый цикл пребывания Семёна в лагере бабы Глаши, Александр обнаружил, что ловушка сработала."
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
    extend " На одиннадцатый день второго цикла Семёна, Александр, вставив в робота сработавшую ловушку, отпустил его и стал ждать результатов."
    hide ext_clubs_day
    hide sh
    with dissolve
    show d_jn:
        linear 2 zoom 1.5 ycenter 0.6
    "\n Робот должен был уехать на автобусе в Шлюз и там остаться."
    show dct_fog:
        alpha 0
        linear 1.5 alpha 1
    extend " Опять же, на одиннадцатый день цикла, вокруг посёлка возникал туман — видимый результат взаимодействия двух вселенных. Робот должен был пройти сквозь туман, нейтринное кольцо, пойманное прибором-ловушкой, должно было клонироваться, и из тумана к роботу должен был шагнуть новый стерильный организм."
    show d_jn:
        linear 1 zoom 1.0 ycenter 0.77
    hide dct_fog
    show d_jnjn behind d_jn at center:
        ycenter 0.6
    with dissolve
    "\nНа этом, судьба робота, как временной технической личности, должна была завершиться.{w} Робот, обнимая стерильный организм, превращался в антенну, принимающую всё, что осталось от обеих Ян в инфосфере Сети, транслируя это новому организму, тем самым формируя его Я. Выполнив свою задачу, робот отключался."
    show d_jn:
        linear 1 alpha 0
    extend " Похожим образом создавались миксы, только там записывались те или иные таланты и навыки организма, а не его личность, личность возникала по принципу «как получится». Похожим образом создавались подлинники, только там личность транслировалась непосредственно от оригинала.{w} «Воскреснуть», после контакта с роботом могла только одна Яна: или жена, или дочь. Кто именно — определял случай, Александр был согласен на любой вариант."
    show d_jnjn:
        linear 1.5 alpha 0
   
    
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    

    "Но Александр был гением."
    scene dct_int_datacenter with dissolve:
        ycenter 0.5
    extend " Понимая, что маленький робот не сможет таскать на себе развитый мозг, он сумел выделить, внутри вроде бы абсолютно защищенной Системы, независимую и невидимую системой область, обсчитывающую поведение робота, чем наделил кошкоробота Яну избыточными мощностями.{w} Наличие собственного нейтринного кольца сделало из неё личность, а возможность пользоваться вычислительными ресурсами Системы подарило — интеллект."
    scene bg ext_playground_day
    show d_sf smile pioneer:
        xcenter 0.43 ypos 0.065
    show d_jn:
        xcenter 0.58 yalign 0.1
    with dissolve
    "\nИ ещё, кошкоробот Яна, по своему, но подружилась с Семёном.{w} Всё это привело к тому, что записанная в памяти робота программа действий оказалась стёртой, кошкоробот получил свободу воли и уехал обратно в родной лагерь, вместе с физруком, а Яна-человек, понятно, так и не появилась."
    scene dct_int_clubs_male_night_light_mon
    show sh cry pioneer close at left
    with dissolve
    "\nРесурсов, чтобы повторить попытку у Александра не было."
    scene dct_int_clubs_male_night with dissolve
    extend " После этого ему только и оставалось, что убивать себя каждый цикл, в надежде, что в Шурике активируется его собственная, Шурика, личность, которая навсегда сотрёт Александра."
    stop music fadeout 1


    $ set_mode_adv()
    
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_clubs_day:
        zoom 3.0 xcenter 0.5 ycenter 0.6
    show sh serious pioneer far:
        zoom 0.8 xcenter 0.75 ycenter 0.87
    with squares
    window auto
    "Шурик сидел на крыльце клубов и курил. Маловероятно, что сейчас его кто-то поймает с сигаретой, да и наплевать ему было на всё."
    "Приступы чужих воспоминаний накатывали волнами, почти полностью при этом подавляя личность Шурика."
    "\~ Вот теперь ты знаешь всё \~, — прошелестело в голове."
    show sh normal pioneer far with dspr
    th "Я надеялся, что ты активируешься, тогда бы ушёл спокойно, ты бы нашёл применение моим знаниям."
    th "А сейчас, я не уверен, что ты перейдёшь в следующий цикл, не отключившись."
    th "Но ты, читая, стёр мою память, перезаписав её себе. То, что я ещё функционирую, это инерция, это скоро пройдет, как только ты ляжешь спать."
    show sh surprise pioneer far with dspr
    th "Спроси Семёна, как это выглядит изнутри и снаружи, он видел и сам участвовал в таком, со всех трёх сторон баррикады."
    show sh scared pioneer far with dissolve_fast
    sh "Александр? Подожди!"    #— закричал Шурик, не задумываясь, что кто-то еще его может услышать.   # По канону
    show sh upset pioneer far with dspr
    "\~ Ты теперь единственный Александр, и других нет \~, — отпечаталась в голове чужая мысль. И, с каким-то щелчком, незримый собеседник исчез."
    show sh cry pioneer far with dissolve_fast
    "Болело сердце."
    play sound sfx_close_door_1
    show mi cry pioneer far with dissolve:
        zoom 0.8 xcenter 0.5 yalign 1.0
    # "Хлопнула за спиной дверь. Из клубов, придерживаясь за перила и столбы крыльца, вышла плачущая Мику."   # По канону
    "Хлопнула за спиной дверь. Из клубов, придерживаясь за ручку двери, вышла плачущая Мику."
    show sh upset pioneer far with dissolve_fast
    "Что-то она говорила самой себе, или, может, не себе."
    show sh upset pioneer far:
        linear 0.5 yalign 1.0
    "Чтобы разобрать, Шурик поднялся, шагнув ей навстречу, и услышал сквозь всхлипы:"
    show sh normal pioneer far with dissolve_fast
    mi "Ничего, цирковая обезьянка Мику, она сильная, она справится."
    show sh normal pioneer far:
        ease 1.0 xcenter 0.58
    "Мику пошатнулась и, не давая ей упасть, Шурик (Или Александр?) подхватил японку."
    show mi upset pioneer far with dissolve_fast
    sh "Ты тоже вспомнила то, что нельзя было вспоминать?"
    show sh normal pioneer far:
        linear 0.5 xcenter 0.59 ycenter 0.87
    show mi upset pioneer far:
        linear 0.5 xcenter 0.49 ycenter 0.85
    "Они осторожно присели на верхнюю ступеньку крыльца."
    mi "Сашечка, скажи. Серёжа, он уже записывал свою память на твоей машине?"
    "Мику не ответила прямо. Но и такого ответа было достаточно."
    sh "Нет. Собирались после завтрака."
    show mi sad pioneer far with dissolve_fast
    mi "Это хорошо, Сашечка. Потому что эта ваша машина, она не должна существовать."
    show sh serious pioneer far with dspr
    $ persistent.sprite_time = "day"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    sh "Да. Я всё сделаю прямо сейчас, не беспокойся."
    stop ambience fadeout 1
    window hide
    show black with dissolve
    
    pause 1.0
    

    $ persistent.sprite_time = "night"
    play music music_list['confession_oboe']
    scene dct_int_clubs_male_rain with dissolve
    pause 0.3
    show el serious pioneer close at right with dissolve
    window auto
    el "Ты готов, Шурик?"
    sh "Давно уже.{w=0.5} Включай, да начнём запись."
    show el laugh pioneer close with dspr
    el "Шурик, а ты знаешь, что Женя…"
    $ persistent.sprite_time = "night"              # Прописано, чтобы при обратной перемотке цвета не сбивались.
    sh "И что же она?"
    scene dct_int_clubs_male2_night_zoom with dissolve
    $ persistent.sprite_time = "day"
    show d_el think pioneer as el with dissolve:
        xcenter 0.5 ycenter 0.5
    "Сыроежкин был влюблен, ему было не до того, и он был ограничен системой, которая слегка корректировала приоритеты в его восприятии. Поэтому он не замечал, ни отсутствие энтузиазма в репликах Шурика, ни того, что тот откровенно тянет время, интересуясь подробностями Жениной биографии."
    show el normal pioneer with dspr
    hide el with MoveTransition(1.5, leave=_moveright, leave_time_warp=_ease_time_warp)     # Электроник плавно уходит с экрана направо
    "Поделившись с напарником, наконец, переполняющими его чувствами и эмоциями, Сергей вспомнил, зачем пришёл."
    el "Включаю. Отсчет по команде «Ноль». Три, два, один. Ноль!"
    $ persistent.sprite_time = "day"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "А в лабораторном журнале кружка добавилась запись: «10-05, начало эксперимента. Первая в истории запись памяти человека! Испытуемый — Александр Трофимов, оператор — Сергей Сыроежкин», — Очередная порция пафоса от Сыроежкина."
    
    $ persistent.sprite_time = "night"
    scene dct_int_clubs_male_rain
    show d_el think2 pioneer as el at cleft
    with dissolve
    "А пока Шурик совершал свой десятиминутный оборот, пока на экране осциллографа электронный луч рисовал, вместо окружности, диковинные кривые, символизирующие запутанность процесса мышления, Сыроежкин с тоской поглядывал то на часы, то на входную дверь и думал:"
    show el smile pioneer with dspr
    th "Как хорошо, что сейчас запишем, а программа расшифрует без нашего участия."
    th "Как хорошо, что я сразу побегу в библиотеку."
    show el normal pioneer with dspr
    th "Надо бы телефон в кружок провести, а то завтра засядем за анализ результатов, а я буду беспокоиться, как там Женя?"
    $ renpy.music.set_volume(0.0, delay=1.0)
    show black with dissolve
    
    pause 0.5
    
    $ renpy.music.set_volume(1.0, delay=1.0)
    show d_el think2 pioneer as el
    hide black with dissolve
    "Жужжал привод табуретки, дождь своими каплями колотил по стёклам, шуршал видеомагнитофон."
    "Электроник скучал, глядя в окно туда, где на противоположном конце лагеря располагалась библиотека и ждал, когда пискнет десятиминутный таймер."
    th "Ещё шесть минут"
    extend ", пять с половиной"
    extend ", пять..."
    play sound sfx_door_bell
    scene dct_sh_in_cage
    show dct_el_in_cage:
        alpha 0
        pause 4
        linear 1 alpha 1
    with squares
    "В отмеренный срок Сергей выключил установку, поменял в видеомагнитофоне кассету, помог, зацепившемуся рубашкой Шурику, выбраться из клетки, внёс новую запись в лабораторный журнал, и сам полез внутрь установки."
    scene dct_int_clubs_male_rain
    show sh cry pioneer close
    with dissolve
    sh "Сергей, ты готов?"
    $ persistent.sprite_time = "night"                # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Что-то было не так в голосе партнера."
    scene dct_int_clubs_male2_night_zoom with dissolve
    $ persistent.sprite_time = "day"
    th "Отсутствие энтузиазма?"
    extend " Нет, не может быть! Шурик же настоящий стальной фанатик науки."
    th "Он даже на отношения между Сергеем и Женей смотрел с той точки зрения, чтобы они не мешали занятиям в кружке."
    extend " И всё же, что-то было не так."
    show sh serious pioneer with dissolve
    "Эта мысль мелькнула и исчезла, Электроник принял устойчивую позу, так, чтобы голова оказалась на продолжении оси вращения табурета и ответил Шурику:"
    el "Готов!"
    show sh normal pioneer with dspr
    sh "Три, два, один. Ноль!"
    scene dct_el_in_cage with squares
    "И стена с окном медленно поползла слева направо, а шкаф начал вплывать в поле зрения."
    "Предстояло самое трудное, усидеть десять минут, не думая о Жене. Вообще ни о чём не думая, но, главное, о Жене."
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
    stop music fadeout 1
    show black with dissolve
    hide mz
    
    pause 0.5
    
    $ renpy.music.set_volume(1.0, delay=0.0)
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_door_bell
    hide black with dissolve
    "Пискнул таймер, десять минут пытки безмыслием истекли."
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
    el "Шурик, как хочешь, давай тебя. Или меня, мне всё равно."
    show sh serious pioneer close with dspr
    sh "Хорошо, тогда меня."
    show sh normal pioneer close with dspr
    sh "Сейчас одиннадцать, раньше пяти вечера ничего не будет, можешь заниматься своими делами."
    show sh serious pioneer close with dspr
    sh "А мне неохота в такой дождь лишний раз по улице бегать, я здесь поработаю."
    show el smile pioneer close with dspr:
        pause 2.5
        linear 1 alpha 0
    
    # "Сыроежкин благодарно кивнул, натянул носки, сушившиеся над плиткой (он успел промочить ноги, пока бежал в клубы), снял с вешалки накидку и, попрощавшись, вышел на крыльцо."   # По канону
    
    "Сыроежкин благодарно кивнул, натянул носки, сушившиеся над плиткой (он успел промочить ноги, пока бежал в клубы), снял с вешалки накидку, подошёл к двери, и выглянул сквозь  стекло на улицу."
    stop ambience fadeout 1
    
    
    play sound_loop dct_ambience_light_rain fadein 1
    scene dct_ext_clubs_rain
    show dct_ext_clubs_rain_el_in_window as d_el
    show dct_overcast_rain_2
    with slideawayup
    "Дождь разошёлся не на шутку: напротив крыльца, на всю ширину главной аллеи, от поребрика до поребрика, разлилась лужа, вся в жёлтых разводах пыльцы."
    "Крупные дождевые капли выбивали пузыри на её поверхности. Вода достаточно быстро текла в сторону стоянки, чтобы там уйти в кюветы и, через дренажные канавы и овраг, попасть в реку, где-то между Старым лагерем и Периметром."
    "Сыроежкин посмотрел на лужу, потом посмотрел на свои ноги в свежевысушенных носках, обутые в дырявые сандалии."
    show d_el rain behind dct_overcast_rain_2 with dissolve:
        xcenter 0.6
    "После чего разулся, снял носки, засунув их поглубже в карман шорт, открыл дверь, не забыв попрощаться с Шуриком, и, держа сандалии в одной руке, а другой придерживая накидку сбежал с крыльца прямо в лужу."
    # "Из под навеса, под сильный дождь."   # По канону
    hide d_el with MoveTransition(1.0, leave=_moveright, leave_time_warp=_ease_time_warp)
    $ day_time()                         # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    th "Женя, я уже бегу, ставь чайник!"
    

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