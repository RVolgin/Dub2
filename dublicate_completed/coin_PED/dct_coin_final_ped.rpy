    #############################
    #Глава 12. Монетка в фонтане#
    #############################


label dct_coin_final_ped:
    $ save_name = u"Дубликат.\nМонетка в фонтане -- Финал\n(pedantic)"
    $ day_time()
    $ persistent.sprite_time = "day"
    scene black
    stop ambience
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


    #pause 18
    $ renpy.pause(18,hard=True)
    show dct_uv_coin_bus_asked at center with dissolve2     # Юля задаёт вопрос
    #pause 2
    $ renpy.pause(2,hard=True)

    #show  dct_d1_uv with dissolve
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
    # show uv guilty with dspr
    show uv smile with dissolve_fast
    uv "Знаю."
    show uv laugh with dissolve_fast
    "Юля подумала, не сделать ли вид, что обижена, но потом улыбнулась."
    show uv grin with dspr
    pause 0.25
    show uv laugh with dspr
    uv "Это всё потому, что я не материализовавшееся подсознание и не ходячий портал, а всего-лишь кошка-мутант."
    my "Ага. Была бы ты на самом деле кошкой — ты бы об этом не задумывалась."
    $ renpy.music.set_volume(0.15)
    play music music_list['mystery_girl_v2'] fadein 2
    show uv smile close with dissolve
    my "Животным, знаешь, по барабану. Так что смирись с тем, что ты — человек."
    $ renpy.music.set_volume(0.25, delay=2)
    show dct_uv_coin_bus_asked as uv with dissolve
    # "Наклонилась надо мной, загораживая весь обзор и глядя мне прямо в глаза. Зрачки расширились, сейчас гипнотизировать будет. А я делаю рывок и целую Юлю в нос."   # По канону
    "Наклонилась надо мной, загораживая весь обзор и глядя мне прямо в глаза. Зрачки расширились, готовится все свои чары выпустить. А я делаю рывок и целую Юлю в нос."
    stop music fadeout 1
    show uv sad close with dissolve_fast
    extend " Хотел в губы, но она дёрнулась и получилось в нос. Ну тоже неплохо."
    $ renpy.music.set_volume(1.0, delay=2)
    show uv smile close with dspr
    uv "Ну вот, всю таинственность момента нарушил. Ладно, пойду."
    show uv smile with dspr
    uv "Скоро Славя придёт — не люблю, когда меня видят. Я, в конце-концов, как там у тебя: «кошкодевочка, легенда лагеря», и должна являться избранным и в критические минуты."
    show uv smile far with dspr
    uv "Ещё увидимся, пока."
    my "Мяу!"
    show uv laugh far with dissolve_fast
    uv "Не дразнись!"
    hide uv with dissolve
    "И убежала."
    
    
    $ renpy.music.set_volume(0.3)
    play music fm_freemusic_chillout_music fadein 4
    "А я выхожу в проход между сиденьями, подбираю пакет и свитер. Пальто, кажется, нужно оставить, а вот телефон не забыть."
    "Или смартфон?{w=0.5} Или МР3-плеер?{w=0.5} Под моим взглядом старенькая кнопочная Нокия начинает увеличиваться в размерах, экран у неё наползает на кнопки…"
    "Кручу головой: «Отставить!». Телефон возвращается к привычному облику. М-да, и вот пошёл бы я такой за Юлей — я бы натворил там дел, в лагере-то."
    "А так…"
    scene dct_int_bus_rightwindow_day with pushleft
    "Пригибая шею, смотрю в окна автобуса — снаружи всё как положено: приоткрытые ворота с прорезанной звездой, надпись «Пионерлагерь Совёнок», два гипсовых пионера, кирпичный забор, лес по обе стороны забора, автобусная остановка."
    window hide
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
    window auto
    "Оглядываюсь назад: дорога, убегающая в холмы, ЛЭП, то ли поля, то ли луга, непонятно."
    
    
    play ambience ambience_camp_entrance_day fadein 2
    scene bg ext_camp_entrance_day with slideawayleft
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
    th "Рад бы, но нет. Внутрь мне нельзя — я сам себе такое правило установил, и поэтому я его выполню."
    "Вспоминаю трансформацию телефона."
    th "Здесь я ещё сдерживаюсь, а внутри — боюсь, что не смогу. И дело не только в пионерлагере, но и, по закону отдачи, во мне самом."
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
    sl "Или нет — костровую поляну знаешь? Подходи туда через час!"
    hide d_sl with dissolve
    "И бегом, в темпе, приличном Ульянке-маленькой, а не помощнице вожатой, скрывается за воротами."
    th "Конечно, знаю; конечно, подойду — затем я тут и оказался."
    

    scene dct_ext_bus_road
    show dct_ext_bus_road_wheat_Maya
    with pushright
    "Присаживаюсь на лавочку: до поляны двадцать минут хода, так что полчаса свободного времени у меня ещё есть."
    "Или я лучше даже прилягу. Устраиваюсь у ног правого пионера в удивительно непыльной и мягкой здешней траве, закидываю руки за голову и лежу, разглядывая облака."
    "Как их называют? Цирусы, если я правильно вспомнил. Когда я ещё здешнее небо увижу?"
    $ renpy.music.set_volume(1.0)
    play music badstory fadein 3
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
    stop music fadeout 6
    th "Интересно, в какой материнский мир из всего пакета его тогда выкинуло вместе с лодкой? Ну это так, праздный интерес, оставим эту тему в покое."
    "Перевожу взгляд с облаков на средний план. На кусте барбариса сидит птичка — не разбираюсь я в них. Мелкая, чуть побольше воробья, очень аккуратное тельце, небольшой тонкий клюв, по серо-коричневому тельцу жёлто-коричневые продолговатые пятнышки."
    "Птиц косит на меня правым глазом, потом я перестаю его интересовать. Вдруг он вспархивает с места, подлетает метра на полтора и возвращается на свою ветку с каким-то насекомым в клюве. Значит, назовем этого птица мухоловкой."


    play music littleidea fadein 5
    "Трещит ветка, вспугнутая мухоловка улетает, бросив добычу. Кто-то кидает в меня сосновой шишкой."
    show us smile sport at right with moveinright
    us "Его все уже ждут, а он тут разлёгся!"
    my "Имею право, Рыжая белка."
    th "Я знаю, она не обидится."
    "Поднимаюсь со скамейки, оглядываюсь. Вон там — начало тропинки к озеру и дальше к Старому лагерю. Туда мне можно, но время поджимает. Поэтому я протягиваю Ульянке руку."
    my "Пошли?"
    play ambience ambience_forest_day
    scene bg ext_path_day
    show dct_uv_ears_bush:       # Уши спрятаны за кустом
        zoom 0.354 anchor(0.54, 0.445)
    show dct_uv_dress_bush:      # Платье спратано за кустом
        zoom 0.354 anchor(0.56, 0.5)
    show dct_ext_path_day_bush  # Куст слева от дороги
    show us smile sport at right
    with squares
    "И мы идём на костровую поляну, не заходя в лагерь. Мне же в лагерь нельзя — я помню."
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
    us "Тогда давай так: я кусаю с одной стороны, а ты — с другой."
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
    "Куча мелких деталей вроде муравейнка у самой тропы, или лесных цветов, или заросшей просеки, уходящей неизвестно куда. И всё это раньше не замечалось или проскакивало мимо сознания."
    
    
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
    th "Кто-то ещё крадётся возле нас вдоль тропинки — я это чувствую."
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
    stop music fadeout 4
    

    scene bg ext_path2_day
    show us normal sport at right
    with irisout
    "Мы идём к костровой поляне, оставляя забор лагеря по правую руку. Слева мелькает прогал: в той стороне озеро, где купается Славя."
    us "Расскажи, как ты живёшь?"
    my "Нормально живу, Уля. Всё вроде бы нормально, и проблем не много и не мало — так, среднее количество. И близкие люди есть, которые меня понимают и которых понимаю я. Но вот узнал о вас и захотел познакомиться."
    show us smile sport with dspr
    us "И напридумывал всякого."
    my "Нет. Всё, что можно придумать, где-то уже существует. В моём мире придуманные вы, в вашем мире — я. Где-то — ещё кто-то третий."
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
    
    ######################################################################
    # Наверное, это всё же, лишнее.
    ######################################################################
    
    # $ ggname = renpy.input("Моё имя:", length=12, default="Тангейзер", allow="йцукенгшщзхъфывапролджэячсмитьбюё-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ").strip()
                        # # Ввод имени главного героя в переменную ggname. Длина - максимум 12 символов. Значение по умолчанию - Тангейзер. Знаки - только кириллические буквы и дефис. strip() - убирает пробелы перед первым и за последним непробельными символами, т.е. перед словом и после слова. В данном случае это избыточно, т.к. пробел исключён из вводимых симоволов, но просто на будущее, чтобы не забыть.
    # if ggname == "":
        # $ ggname = "Тангейзер"      # Если оставить поле пустым, то вставится значение "Тангейзер".
    
    # "Хотя... Не стоит так уж сразу терять ореол таинственности.{w} Называю ей сетевой ник. Рыжик недовольно морщит носик."
    
    ######################################################################
    
    "Называю ей сетевой ник. Рыжик недовольно морщит носик."
    show us dontlike sport with dissolve_fast
    us "Нет, не то! Как зовут по-настоящему? Как мама с папой назвали. Не бойся, я умею хранить тайны."
    show us normal sport with dissolve_fast
    th "Да я, собственно, и не боюсь, я просто не хочу. Но Ульянка настаивает, и, кажется, ей действительно это надо."
    my "Рыжая белка, зачем тебе моё имя?"
    show us smile sport with dspr
    us "Надо!"
    my "Ну хорошо, скажу перед уходом."
    stop ambience fadeout 2
    
    
    $ renpy.music.set_volume(0.6)
    play music rustic_ballad fadein 2
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    play ambience ambience_medium_crowd_outdoors fadein 2
    scene bg ext_polyana_day
    # show dct_bonfire_day
    show dct_bonfire_day_anim:
        xcenter 0.5 yanchor 0.0 ypos 0.55
    with irisout
    "А мы, собственно, уже вышли на костровую поляну."
    show d_sl shy pioneer close at left with dissolve
    sl "Ну наконец-то!"
    "Оглядываю поляну. Знакомые все лица, и все улыбаются."
    show d_sl smile2 pioneer close with dspr
    sl "Здесь все. Кто смог и кто захотел."
    "Да, действительно — все, кто смог и кто захотел."
    show d_sl smile pioneer close with dissolve_fast
    sl "Узнаёшь тех двоих?"

    show d_cs m at fright:
        alpha 0.0
        pause 1
        linear 2.0 alpha 1.0
    show d_to m smile:
        xcenter 0.63 ycenter 0.55 alpha 0.0
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
    "Алисы — вот они, обе. Здороваются со мной по-мужски, за руку, улыбаются."
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
    ### "Спрашиваю, и, дождавшись утвердительного кивка, продолжаю."
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
    "Ну это уже не моя забота, я просто полюбопытствовал."
    show dv normal pioneer far at cright:
        xzoom -1.0
    show dv_4_guitar_standing far at cright:
        xzoom -1.0 yalign 0.0
    show dv_4_badge_mirror far at cright:
        xzoom -1.0
    show 3500_dv normal pioneer2 guitar standing:
        zoom 0.75 yalign 0.0
    with dissolve
    "Алисы встают, обе с гитарами, обе — нет, не одинаковые, но очень похожие."
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
    "Скорее угадываю, чем улавливаю — настолько он слаб, запах грейпфрута. Поворачиваю голову и тону в зелёных глазищах. Ко мне подсела Лена."
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
    my "Ну к вам-то заглядывал не я один. Так что имена я уже знал. Так, несколько имён добавил в копилку и всё."
    show un smile3 pioneer close with dspr
    un "Ну вот, а мы со здешней Мику вдвоём заглянули к тебе. Не бойся — обещаю тебе, что все подумают, что это выдуманное нами имя."
    show un serious pioneer close with dspr
    un "Скажи, как ты думаешь, когда мой Семён проснётся?"
    my "Скоро, Лен. Не в этом цикле, но очень скоро."
    show un surprise pioneer close with dissolve_fast
    my "Он зайдёт в лагерь, повернёт голову к клубам, увидит тебя и скажет одними губами: «Ленка! Я прорвался!», но ты его прекрасно услышишь и бросишься к нему на шею, завизжав так, что перепуганные кибернетики выскочат на крыльцо."
    show un cry_smile pioneer close with dspr
    my "Тебя спасать, между прочим, выскочат. Вот только ты к концу этого цикла забудешь всё, а вспомнишь уже потом, когда всё произойдет."
    th "Что я там говорил Ульянке, что не выдумывал их мир? Что я только наблюдатель и регистратор? Но это правда, просто наблюдатель всегда влияет на наблюдаемый объект, и я пользуюсь этой возможностью."
    show un smile pioneer close with dissolve_fast
    th "И, кажется, Лена это знает, если задала такой вопрос. А если ещё не знает, то догадается."
    show un smile pioneer close:
        linear 6 alpha 0.0
    th "И они тоже наблюдатели, это правило распространяется и на них. Но я не жду ничего плохого ни от Лены, ни от Мику — пусть они заглядывают ко мне. Мне будет приятно."
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
    th "Но уже скоро — чувствую, что от хорошего пинка она проснется прямо сейчас, и проснётся безболезненно. Обойдёмся без пинков, всё должно быть естественно."
    "Поэтому я улыбаюсь этим троим девочкам, машу им рукой: «Я узнал вас, кто вы и откуда, и очень рад вас видеть» — Мику в ответ энергично машет мне рукой"
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
    "Пока все ресурсы системы заняты на то, чтобы выкинуть меня из здешнего мира, любые двойники могут сосуществовать в одном узле и не аннигилировать, но сколько мне здесь ещё находиться? Час-два, вряд ли больше."
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
    th "Но за вами тоже подглядывать буду — тут я наврал Семёну, и мы оба это понимаем, и не только мы."
    show d_sf serious pioneer with dspr
    show d_us hurt dress with dspr
    us_old "Врёшь ты всё."
    show us grin sport
    show d_us shy dress
    with dspr
    us_old "Не будет он… Ты уже отравился «Совёнком». Подглядывай, тебе можно."
    show d_us normal dress with dspr
    us_old "Слышишь, Сёмк — ему можно!"
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
    
    $ renpy.music.set_volume(0.15)
    play music adaytoremember fadein 4
    # $ renpy.music.set_volume(0.3)
    # play music Everlasting_Summer_guitar_cover fadein 4
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
        zoom 0.8 xcenter 0.92 ycenter 0.60 alpha 0.0
        pause 1
        linear 1.5 alpha 1.0
    show d_mt2 calm sport far:
        zoom 0.8 xcenter 0.69 ycenter 0.60 alpha 0.0
        pause 1
        linear 1.5 alpha 1.0
    sh "А… ты имеешь в виду…{w=0.4} Я как Ольга — стал целым, и знаешь, я больше Шурик.{w} Александр, он…{w=0.3} Он растворился во мне."
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
    my "А скажи, я понимаю — робот. Могу догадаться, почему робот-девочка. Но кошка тут при чём?"
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
    stop music fadeout 5
    

    "Вот, собственно, и всё."
    "Есть ещё несколько человек, с которыми я бы пообщался, но и время поджимает, и столько общения уже тяжело для меня."
    "Пора уходить. Пионеры тоже это чувствуют."
    hide d_mt with moveoutright
    pause 0.2
    show mt angry panama pioneer far
    show d_mt2 angry sport far
    with dissolve_fast
    show d_mt2:
        ease 1.5 xcenter 0.28
    show mt:
        pause 0.5
        ease 0.6 xcenter 0.65
    "Ольги поднимаются, одна сразу уходит куда-то вбок, по тропинке, а две других начинают строить каждая своих подопечных."
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
    
    
    stop ambience fadeout 5
    $ renpy.music.set_volume(1.0)
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
            # "Фелициоид краснеет, но делает вид, что ничего не произошло." # Так написано в оригинале, но я не нашёл что это за слово — Фелициоид. Зато есть слово Фелиноид, использующееся для обозначения антропоморфных разумных кошачих.
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
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    play ambience ambience_forest_day fadein 0.5
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
    "Ульянка думает о чём-то своем, я опять верчу головой, чтобы запомнить детали."
    show us sad sport with dissolve_fast
    "Вон уже и остановка, вон уже и Икарус. Никуда он не уехал, родимый."
    
    
    scene bg ext_bus
    show us sad sport at cleft
    with wiperight
    play ambience ambience_camp_entrance_day
    us "Мы ещё увидимся? По-настоящему?"
    my "Каким образом, Рыжая белка? У вас я могу существовать только несколько часов и в чужом теле — вот как сейчас; у нас ты — только в виде картинки на мониторе."
    my "Разве что в следующей жизни. Либо ты к нам, либо я к вам — как получится."
    my "Так что если в лагерь приедет новенький, высокий, сутулый и худой, по характеру и любви к книгам и технике — что-то среднее между Электроником и Женей, присмотрись к нему, прежде чем подбрасывать членистоногих в пюре."
    show us calml sport with dissolve_fast
    us "Вот далось вам всем это пюре!"
    show us shy sport with dissolve_fast
    us "А скажи, мы здесь сильно отличаемся от того, что ты и другие про нас написали?"
    my "И да, и нет. В основном деталями."
    my "Например, вот скажи, Рыжик — у тебя же веснушки с шеи переходят на плечи и дальше на грудь? По моему, очень мило."
    show us surp3 sport with dspr
    pause 0.7
    show us fear sport with dissolve_fast
    us "Ты! Ты! Ты подглядывал!"
    stop music fadeout 6
    show us shy2 sport with dissolve_fast
    my "Нет, Рыжик, я догадался. Эти веснушки — обычное для рыжих дело, а у нас про них никто не вспомнил. Ладно, прощай."
    show us normal sport with dissolve_fast
    us "Прощай.{w=0.5} Нет, подожди, время ещё есть. Побежали, я тебя с Майей познакомлю!"
    
    
    scene bg ext_road_day:
        running
    show dct_ext_road_day_wheat_Maya:
        running
    with irisout
    play music anewbeginning fadein 2
    play ambience ambience_ext_road_day
    "«Что ещё за Майя такая?» — бурчу про себя, но послушно бегу за Улькой по шоссе."
    "Двести метров,{w=0.3} пятьсот,{w=0.3} восемьсот…"
    "Ульянка останавливается в одном ей ведомом месте и ждёт меня. Догоняю, оглядываюсь."
    scene dct_ext_outside_field
    show dct_ext_outside_field_Maya
    show us normal sport far at cleft
    with irisout
    "Когда-то здесь был свёрток с шоссе на Старый лагерь. Потом лагерь закрыли, а дорожную насыпь срыли бульдозерами."
    "О том, что здесь была дорога, можно догадаться только по чуть отличающемуся оттенку пшеницы и по заросшей уже просеке, просматривающейся там, где насыпь упиралась в лес."
    "И ещё есть она: девочка, пионерка, как будто из моего старого-старого отряда. Футболка, шорты, галстук на голой шее, стрижка, закрывающая уши. Лет ей двенадцать или тринадцать, не больше."
    "Шла вдоль дороги из Старого лагеря, дошла до шоссе, присела на гранитный валун, сняла сандалию, подтянула правую ногу ступней к себе и что-то там рассматривает: то ли камешек, то ли занозу."
    "То есть рассматривала только что, а сейчас услышала шум мотора, подняла голову и так и превратилась в бронзовую скульптуру. И теперь вечно со спокойным любопытством смотрит на шоссе: кого там везут в лагерь во внеурочный день? Хорошее такое лицо."
    th "Может, у скульптора бронза осталась после отливки Генды, и он постарался уже не для халтуры, а для души — я не знаю. И не важно на самом деле."
    us "Вот, это Майя."
    "Но я и сам догадался. Подхожу, сажусь напротив Майи на корточки, чтобы не смотреть на неё сверху вниз."
    show us sad sport far with dspr
    my "Здравствуй, Майя."
    "Протягиваю правую руку и осторожно трогаю её бронзовое запястье."
    "Кажется, что взгляд у Майи на мгновение сфокусировался на мне."
    show us laugh2 sport far with dspr
    extend " Краем глаза вижу, как расцветает в улыбке Ульянка, а до того стояла, замерев в непонятно-тревожном ожидании."
    show us grin sport far at cleft with dspr
    us "Врёшь ты всё, что никогда здесь не был! Ты же всё сделал правильно!"
    us "А теперь побежали обратно."
    th "И действительно пора, а то Семён проснётся не в автобусе, а непонятно где."
    
    
    scene dct_ext_bus_road
    show dct_ext_bus_road_wheat_Maya
    show us sad sport close at cright
    with irisin
    play ambience ambience_camp_entrance_day
    "Мы стоим у автобуса; я, прежде чем залезть внутрь, пытаюсь отдышаться. Вот теперь уже совсем пора."
    "А Ульянка всё не хочет меня отпускать."
    us "Послушай, вот ты наблюдал за нами. А можно я тоже буду наблюдать, как там ты живёшь?"
    my "Конечно, можно. Мне будет очень приятно, что ты обо мне беспокоишься."
    show us shy sport close with dspr
    show dct_uv_newdressedging_close at cleft:
        alpha 0.0
        pause 1
        linear 1 alpha 1.0
    "Обнимаюсь с Ульянкой, целую её в щёку,{w=0.8} обнимаюсь с прибежавшей Юлей, она целует меня в нос и хохочет — отомстила, и лезу в автобус."
    stop ambience
    scene bg int_bus with slideright
    "Всё на месте: и пальто, и пакет. Сейчас я усну, а проснется уже Семён, и через положенное время выйдет из автобуса и пойдет к воротам «Совёнка» навстречу Славе."
    "А я уже, наверное, не стану узнавать, что его там ждёт."
    "Надо бы сделать для него что-то хорошее, но что?"
    "Делаю последнее усилие и заряжаю аккумулятор в его телефоне по самую крышку. Потом заполняю карту памяти музыкой со своей автомагнитолы — пусть разбирается, может что и пригодится. Вот удивится-то."
    $ renpy.music.set_volume(0.1, delay=4)
    
    $ day_time()                            # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "Всё, спать! Посчитаю-ка я для разнообразия автобусы: «Первый четырестадесятый подъехал к остановке, второй четырестадесятый подъехал к остановке, третий...»"

    
    
    show blink
    pause 1
    window hide
    pause 1.5
    $ prolog_time()
    window show
    scene black
    voice "Зая хренов, я думала, он работает, а он беспардонно дрыхнет! Ужин готов! Кушать подано, садитесь жрать, пожалуйста!"
    scene dct_author_room behind blink
    show unblink
    my "Повинуюсь, мой злобный хомячок!"
    window auto
    voice "Всё написал?"
    my "Возможно…"
    voice "Мистер загадочность…"
    $ renpy.music.set_volume(1.0, delay=7)
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
    show black:
        alpha 0.0
        linear 2.5 alpha 1.0
    "Всё хорошо, сестрёнка.{w=1} Я сейчас бросил монетку, и надеюсь, что она останется стоять на ребре."
    stop music fadeout 2.5
    
    $ renpy.pause(2.5)

    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound_loop')
    
    $ persistent.d_coin = d_coin + 1
    menu:
        "Конец книги «Монетка в фонтане»"
        "В меню":
            jump dct_mnu2
