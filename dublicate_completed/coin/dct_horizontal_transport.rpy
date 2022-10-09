    ####################################
    #Глава 11. Горизонтальный транспорт#
    ####################################


label dct_horizontal_transport:
    $ save_name = u"Дубликат. Монетка в фонтане -- Горизонтальный транспорт"
    $ night_time()
    $ persistent.sprite_time = "night"
    scene black
    stop sound
    stop sound_loop
    stop ambience
    play music twinkling
    show headline_text2 u"Глава XI. Горизонтальный транспорт" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve

    scene bg ext_square_night
    show un normal pioneer at left:
        ycenter 0.65
    show d_sf normal hike at right:
        xzoom -1 ypos 0.12
    with dissolve
    un "Семен, значит, ты думаешь что мы не настоящие?"
    "Лена передернула плечами от своих слов."
    show d_sf sad hike with dspr
    me "Я не знаю, Лен..."
    "Перед ужином поговорить не получилось, а вот сейчас, когда Ульяна убежала к Алисе, а Семен, от нечего делать, слонялся по лагерю и вышел на площадь, и случился этот разговор."
    show d_sf normal hike with dspr
    me "Я не знаю, Лен.{w} Для самих себя мы, конечно, настоящие. И мир вокруг нас тоже.{w} Но вот то, как этот мир устроен. И как мы устроены. И физически и духовно."
    show un serious pioneer with dissolve_fast
    un "Продолжай, я поняла."
    show un normal pioneer with dissolve_fast
    "Лена принялась что-то рисовать, поглядывая на Семена."
    show d_sf laugh hike with dspr
    me "Мне красивую позу принять? Я могу."
    hide d_sf with dissolve
    "Семен вскочил со скамейки и встал напротив Лены, копируя Генду."
    show un smile pioneer with dspr
    un "Ну, если ты именно таким хочешь остаться в памяти потомков."
    show un normal pioneer with dspr
    un "Но ты говорил про наш мир."
    show d_sf normal hike at right with dissolve:
        xzoom -1 ypos 0.12
    "Семен тоскливо огляделся. Сел рядом. Вздохнул."
    show un normal pioneer with dspr
    "Говорить о догадках, интуиции и непроверенных гипотезах вдруг расхотелось."
    "Захотелось просто сидеть, наблюдая, как Лена работает.{w} Да-да, та самая, третья из тех вещей, за которыми можно бесконечно наблюдать."
    "Или дойти до Алисы, постучаться к ней в домик, и секретничать с Алисой и Ульяной уже втроем?"
    me "\~ Вот ведь. Алиса относится ко мне лучше, чем я к ней, а я на Лену нашел время, на Алису не смог. \~"
    me "\~ Прости меня, Вредина, я обязательно исправлюсь. \~"
    "Но надо было отвечать."
    me "Видишь, Лена. Сначала я думал, что все мы, всего лишь модель, которую обсчитывает какой-то супер-пупер компьютер. Но потом…{w} Слишком у нас все нерационально. Люди ладно, но даже лагеря не во всем одинаковые."
    me "Будь я компьютером, здесь бы все было по одному образцу. И пионеры говорили бы одинаковыми наборами фраз. Исключительно для экономии ресурсов."
    me "А мы в каждом лагере, хоть чуть, но разные. А уж когда просыпаемся.{w} Те же две Алисы, это два абсолютно разных человека. Похожих очень, но перепутать можно, только если не знаешь обеих.{w} Про Ульян вообще молчу."
    "Лена закончила рисовать и повернула альбом к Семену."
    show un smile pioneer with dspr
    "Получился «Семен доказывающий теорему». Стоит у едва намеченной классной доски, мел в правой руке, а сам обернулся к классу и смотрит на зрителя чуть ехидно.{w} Вот только…"
    show d_sf laugh hike with dspr
    me "Ты меня семнадцатилетним сделала."
    show un smile2 pioneer with dspr
    un "Терпи, я тебя таким вижу."
    show d_sf smile hike with dspr
    me "А можно посмотреть?"
    show un shy pioneer with dspr
    "Лена долго решалась, но разрешила и протянул альбом."
    un "Смотри."
    show d_sf normal hike
    show un normal pioneer
    with dspr
    "Семен начал листать:{w} Женя с разными выражениями лица;{w} Шурик, поправляющий очки;{w} Максим с горном, сидящий на скамье;{w} тот же Максим, спящий в тени березы;{w} две Ульяны, большая и маленькая, хлопающие друг-друга пятернями;{w} Ольга Дмитриевна, читающая нотацию среднему отряду."
    show d_sf serious hike with dspr
    me "Когда успела, Лен?"
    show un smile pioneer with dspr
    un "Ну, книги в библиотеке кончились…"
    show d_sf normal hike with dspr
    me "Понятно."
    show un normal pioneer with dspr
    
    "А альбом был очень интересный и каждому обитателю лагеря было посвящено несколько листов."
    "Семен, прохаживающийся перед строем футболистов.{w} Семен держащий за руку Ульяну.{w} Уже виденный Семен у школьной доски.{w} Саша, танцующая с Максимом.{w} Саша на площади что-то доказывающая Сыроежкину.{w} Саша в спортивной форме на беговой дорожке.{w} Мику за роялем и Мику на собрании отряда грустная, грустная."
    show d_sf serious hike with dspr
    me "Ты знаешь, что Мику и Шурик проснулись?"
    show un sad pioneer with dissolve_fast
    un "Знаю. И радости им это не доставило."
    show d_sf sad hike with dspr
    un "Помнишь, давно-давно, я говорила тебе про занозы в душе. Вот, похоже они не были готовы к тому, чтобы проснуться, но проснулись из-за машины Шурика, а теперь им очень больно."
    me "Особенно Мику. Ты права."
    show un serious pioneer with dissolve_fast
    un "Но мы же не бросим их?"
    show d_sf normal hike with dspr
    "Семен только кивнул, как само собой разумеющемуся, перелистывая страницы дальше."
    show un normal pioneer with dissolve_fast
    "Вот Славя, подметающая площадь…"
    me "\~ Стоп!{w=0.3} Славя? \~"
    show d_sf serious hike with dspr
    "Он поднял глаза на Лену."
    show un shy pioneer with dspr
    un "Ну, ты рассказывал о девочке похожей на Сашу. Помощнице вожатой в других лагерях. Вот я и представила себе ее."
    "Звучало неубедительно, но…{w=0.5} пусть."
    show d_sf normal hike
    show un normal pioneer
    with dspr
    "А дальше... Дальше были две Алисы, одна здешняя, а другая из лагеря Виолы, тут ошибиться было невозможно."
    "Они о чем-то спорили яростно, схватив друг-друга за пионерские галстуки. Почти на грани драки.{w} Почти, потому что уже ясно, сейчас они еще поорут друг на друга, выпустят пар, потом одна из Алис хлопнет другую по плечу и обе рассмеются."
    "А дальше шли уже совсем незнакомые люди. Мальчики, девочки, мужчины, женщины, — все набросаны достаточно схематично, но все же узнаваемо. Под некоторыми подписаны имена, некоторые безымянные."
    me "Лена?"
    show un cry_smile pioneer with dissolve_fast
    "Лена посмотрела на Семена неожиданно доверчиво. И, как когда-то рассказала ему о себе и Семене-втором, начала свой рассказ."
    show anim prolog_1:
        alpha 0
        linear 0.5 alpha 1
    $ set_mode_nvl()
    "Все это началось в прошлом цикле, после той спасательной экспедиции, которую Лена с Алисой предприняли в поисках Семена и Ульяны."
    un "Я тогда тоже, как ты, решила, что наш мир не может существовать.{w} Только я решила, что наш мир не компьютерная модель, а чья то фантазия."
    "А потом Лену заинтересовал человек, придумавший их мир.{w} Какое-то время Лена отбрасывала от себя эту мысль, но снова и снова к ней возвращалась.{w} А дальше приехал Второй и Лене стало не до того."
    un "В конце цикла, когда мы ехали в автобусе, и мой Семен уже уснул, я подумала, что, может, если я пойму этого человека, то я тогда пойму и то, как мне разбудить моего Семена, ведь он такой же придуманный, как и мы все."
    "И Лена попыталась на основе того, что она знает о мире, представить себе придумавшего этот мир автора.{w} Так появился первый «портрет неизвестного» в ее альбоме."
    un "А потом я поняла, что не может один человек столько выдумать и в голове держать."
    "И появились еще портреты других людей.{w} Портретов оказалось мало, возникла необходимость в словах."
    un "И я пошла к Алиске."
    "И оказалось, что Алиса тоже думала об этом, да так, что за неполный цикл исписала уже полторы тетради.{w} Вдвоем дело пошло веселее, у некоторых «неизвестных» появились имена или хотя бы прозвища."
    un "Алиса еще сказала, что эти прозвища называются «ники»."
    
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    
    "А потом Семен унес Ленину иллюстрацию в лагерь Виолы, а через два часа перед Леной появилась недовольная, тем что ее оторвали от каких-то своих дел, Ульяна-маленькая и передала новую работу Мику из того лагеря, и ее просьбу: «Что-нибудь с этим сделать»."
    "Мику написала сказку про маленькую планету. Астероид, прямо как в «Маленьком принце».{w} Маленькую планету, на которой только и есть, что один единственный пионерский лагерь.{w} На Земле мало кто знает про эту планету, только несколько человек."
    "И вот, пока хоть один человек помнит и думает о той планете, на ней и в лагере все хорошо.{w} А иначе, каждую смену что-то в том мире теряется навсегда.{w} Уменьшается радиус планеты, исчезают пионеры и никто не вспоминает о них, сокращается территория лагеря, становятся короче смены.{w} И так, пока не останется каменная глыба астероида, лишенного атмосферы."
    "Но и пионеры в том лагере тоже знают о Земле.{w} Не все, конечно.{w} И тоже, пока они помнят о ней, то все на Земле хорошо."
    un "Ну, не хорошо, конечно, Земля она вон какая большая, а пионеров вон как мало, но хоть чуточку, но лучше."
    un "И вот у нас все встало на свои места.{w} Никакая мы не модель. Никто нас не придумывал. Есть наши лагеря, Сеть, как вы с Ульяной их называете, есть Материнские миры и есть Земля."
    un "И все это связано, через людей.{w} И там, и там, и здесь."
    un "И вот мы сейчас переписываем рассказик.{w} То есть переписывают Мику из того лагеря, с нашей Алиской, а я так, на подхвате, почитать, покритиковать, иллюстрации сделать.{w} И Ульянка-маленькая, она — наш почтальон."
    show un serious pioneer
    show anim prolog_1:
        alpha 1
        linear 0.5 alpha 0
    $ set_mode_adv()
    
    un "И еще, в рассказе Мику, те пионеры, что знают о Земле, рано или поздно, но уходят туда."
    show un angry2 pioneer with dspr
    extend " Понятно?"
    # Лена смотрела очень строго. # Опускаем
    show d_sf serious hike with dspr
    me "Да, Лен. Понятно."
    show d_sf smile hike
    show un serious pioneer
    with dspr
    me "Девочки, вы умницы.{w} Это лучше моего компьютера.{w} Я горд тем, что дружу с вами."
    show un shy pioneer with dissolve_fast
    me "И, если все это правда, я не хочу, чтобы вы, то есть мы, там потерялись."
    "Семен махнул рукой куда-то за горизонт"
    show un normal pioneer
    show d_sf normal hike
    with dspr
    un "Если все это правда, то не потеряемся."
    # Лена улыбнулась.  # Опускаем
    show un smile pioneer with dspr
    un "Говорят, беженцы из Атлантиды всегда узнавали друг-друга."
    show d_sf smile hike with dspr
    un "Ну, спокойной ночи. Вон и Ульяна идет."
    # Подошла Ульяна, села рядом с Семеном, уместив свою голову ему на груди.   # Опускаем
    pause 0.5
    show d_us normal sport_windbreaker with dissolve:
        xcenter 0.54 ycenter 1.04 rotate 15.5
    us "Это хорошо, что ты здесь, Лен. Мне чтобы два раза не рассказывать. Знаете, какой завтра день?"
    show d_sf serious hike with dspr
    me "Воскресенье. Восьмой день цикла."
    show un shy pioneer with dspr
    un "Завтра приезжает мой Семен."
    show d_sf normal hike with dspr
    us "Ты, Лена, почти правильно ответила. Завтра приезжают автобусы во все лагеря."
    show un normal pioneer
    show d_us serious sport_windbreaker
    with dspr
    us "И барьеры между мирами будут проницаемыми. Одним словом, я еще подумаю, что тут можно сделать."
    show d_us normal sport_windbreaker with dspr
    extend " И сестренка подумает. И Алиса подумает."
    show d_us smile sport_windbreaker with dspr
    extend " А сейчас, пошли спать, Сёмк."
    stop music fadeout 1.5
    scene black with dissolve
    
    pause 1.2
    

    play sound_loop ambience_int_cabin_night fadein 1
    pause 0.3
    d_jn "Па, а зачем я?"
    window hide
    scene dct_int_house_of_el_night:
        blur 25
    show d_jn:
        xalign 0.5 yalign 0.3 blur 50
    show unblink
    pause
    show blink
    pause 1.3
    window auto
    d_jn "Па, а зачем я?"
    hide blink
    show unblink
    show dct_int_house_of_el_night:
        pause 1
        linear 1 blur 0
    show d_jn:
        pause 1
        linear 1 blur 0
    "Шурик проснулся настолько, чтобы найти на стуле очки. Постепенно возвращалось сознание и забывался сон. Чей сон и что в нем снилось забылось сразу же, какое-то время держались еще в памяти отдельные кадры, но постепенно ушли и они."
    "Перед Шуриком стояла Яна, трогала его за руку и терпеливо спрашивала: «Па, а зачем я?»."
    "Шурик глянул на фосфоресцирующие стрелки часов, «вчера» уже закончилось, а «сегодня» потихоньку вступало в свои права."
    "Шепотом, чтобы не разбудить соседа Шурик сказал:"
    sh "Ян, давай днем."
    d_jn "Нет, сейчас."
    "Яна тоже догадалась прикрутить громкость."
    "Пришлось вылезать из под одеяла, натягивать шорты и идти на крыльцо."
    sh "Счастье твое, Яна, что сегодня воскресение и можно спать до девяти утра."
    stop sound_loop fadeout 1
    play ambience ambience_camp_center_night fadein 1
    scene dct_ext_house_of_el_night with slideawayup
    "Шурик прислушался к своим ощущениям.{w} Нет, признаков присутствия Александра в голове не наблюдалось, хотя часть его привычек, черт характера и ключевые воспоминания перешли к дубликату."
    th "Покоя тебе, где бы ты не был"
    show d_jn with dissolve_fast:
        xalign 0.5 yalign 0.3
    d_jn "Па, а зачем я?"
    "Нужно было отвечать."
    th "Я не должен чувствовать вину, но мне стыдно."
    th "Все проделано Александром. Пусть руками старого Шурика, но Александром."
    th "Старый Шурик был такой же технической личностью, как и Яна, но мне все равно стыдно."
    sh "Яна, ты для того, чтобы исчезнуть, умереть.{w} Ты должна была собрать рассеянную в системе информацию…"
    "Шурик говорил долго, рассказывая то, что он вытащил из памяти Александра."
    sh "… а потом, лишенный памяти робот бестолково ходил бы по Шлюзу, пока у него не кончился бы заряд. Не удерживаемое ничем нейтринное кольцо вылетело бы из ловушки, а связь с Системой оборвалась. И всё. Для тебя всё."
    "Про то, что для Шурика это тоже было бы всё, он умолчал."
    th "Вот теперь я Яне ничего не должен."
    # Шурик присел на ступеньки     # Опускаем
    th "Теперь я ей должен только то, что хочу дать."
    extend " Надо бы ей ухо поправить и полировку восстановить."
    "В ожидании реакции робота мысли Шурика лениво перекатывались."
    th "И повоспитывать чуть-чуть, чтобы не будила в пять утра."
    "А Яна замерла неподвижно, только повернув голову так, чтобы держать Шурика в поле зрения обоих оптических датчиков."
    th "Интересно, о чем она думает? Надо бы ей сказать, чтобы не замирала надолго, что неприятно так с ней разговаривать."
    th "Яна, ты когда замираешь, шевели чуть-чуть какой-нибудь частью тела, чтобы понятно было, что ты не статуя, а живая."
    extend " Живая?"
    extend " Да, живая!"
    d_jn "Па, это не то. Это я и сама знала. Твоя старшая личность не зашифровала программу."
    th "Вот, значит как. Моя старшая личность."
    sh "И ты спокойно об этом говоришь?"
    d_jn "Это было мое предназначение."
    "Шурик не удержался и притянул Яну к себе."
    show d_jn with dissolve_fast:
        zoom 1.25 yalign 0.33
    extend " Удивительно, но металлический корпус не холодил руку и тело. Удивительно, но Яна приняла это как должное, переступив поближе к Шурику и опустившись рядом с ним на крашенные доски."
    d_jn "Па, я решила, что это предназначение — ложное. И теперь я ищу — зачем я."
    th "Дожили, робот спрашивает о смысле жизни."
    "Если бы кто-то, хорошо знающий Шурика, хоть тот же Семен, сейчас наблюдал за ним, он очень бы удивился — Шурик смеялся."
    sh "Дочка..."
    "Cлово было произнесено неожиданно, легко, и неожиданно легко."
    sh "Дочка, ты задаешь такой вопрос, на который отвечает, даже для самих себя, едва ли десятая часть всех людей.{w} И то, многие только в конце жизни. А большинство живет не думая, просто как трава растет."
    d_jn "Я поняла, па. Тогда я буду думать над этим."
    d_jn "Я бы поцеловала тебя сейчас, но не могу. Конструкция не позволяет."
    show d_jn:
        pause 0.6
        linear 1 alpha 0
    extend " Над конструкцией я тоже буду думать."
    stop ambience fadeout 1
    play sound_loop ambience_int_cabin_night fadein 1
    scene dct_int_house_of_el_night with slidedown
    "Яна убежала, а неожиданно развеселившийся Шурик вернулся в домик, покосился на спящего Сыроежкина, подмигнул своему отражению и прошептал:"
    $ night_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "night"
    sh "Не надо оваций. Если пионера и руководителя кружка кибернетики из меня не выйдет, я всегда могу переквалифицироваться в пожилые электрики."
    stop sound_loop fadeout 1
    show black with dissolve
    window hide
    
    pause 0.5
    

    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day fadein 1   # Тут специально амбиенс не от спортплощадки, потому что на ней никто не играет.
    scene bg ext_playground_day
    with dissolve
    window auto
    "Сашка закончила нарезать круги по стадиону."
    play sound "<from 2.6>sound/sfx/slavya_run.ogg" fadein 1.5
    $ renpy.pause (2.2)
    show sl sad sport far with easeinleft:
        xanchor 0.0 xpos 0.15
    th "А пионеры спят."
    extend " Пользуются тем, что сегодня нет линейки и можно спать до завтрака, и спят."
    show d_us hurt sport at fright:
        ypos 0.09 alpha 0
        linear 1 alpha 1
    th "Вот и Ульяна зря сидит и ждет желающих провести зарядку."
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
    "Ульяна удалилась куда-то в сторону хозяйственных ворот.{w} Саша вздохнула. Чувствовалось, что Ульяна всеми силами старается поддерживать от нее дистанцию, а причина была не понятна."
    show sl normal sport far with dissolve_fast
    "Но насильно мил не будешь и, поскольку Ульяна никогда не показывала своего недовольства, Саша тоже не лезла выяснять отношения. Потому что всего через неделю смена закончится, и кто знает, удастся ли приехать в этот лагерь на следующий год?"
    hide sl with dissolve
    "Поэтому Саша проводила Ульяну взглядом, быстро, пока Семен еще не вышел из тренерской, ополоснулась в душе и побежала к себе."
    stop ambience fadeout 1
    play sound_loop ambience_camp_center_day fadein 1
    scene bg ext_dining_hall_away_day with pushright
    pause 0.3
    scene bg ext_square_day with pushright
    "Спорткомплекс, столовая, площадь… Нигде ни души, и только на площади случилась остановка."
    "Около флагштоков имел место быть Максим, он увидел Сашку и несколько растерянно помахал ей рукой."
    scene dct_ext_square_profile_view_day
    show d_ma shy pioneer:
        zoom 0.75 xcenter 0.9 yalign 1.01
    with dissolve
    show 3500_sl smile3 sport as sl:
       zoom 0.75 xcenter -0.1
       easein 1.8 xcenter 0.66
    pause 0.5
    d_ma "Привет. Я уже привык, оказывается, в семь утра трубить подъем. И сбор в восемь утра. А сегодня не надо, надо только в девять — на завтрак."
    show 3500_sl smile3 sport as sl:
       zoom 0.75 xcenter 0.66
    show d_ma serious pioneer
    with dissolve_fast
    d_ma "А я вскочил и прибежал, еще думал, что проспал. И только здесь опомнился. Так глупо. Сосед смеяться будет."
    show sl happy sport far at cright with dissolve_fast:
        zoom 1.0
    sa "Ничего, Максимка. Зато я теперь стала лучше думать о пионерах, не все из них, оказывается, спят до завтрака."
    show sl smile sport far with dissolve_fast
    sa "Пошли умываться, раз уж не спишь."
    scene bg ext_musclub_day with pushright
    "Неизвестно, зачем, проходя мимо музыкального кружка, они решили заглянуть в окно.{w} Неизвестно, зачем, увидев Мику за роялем, они решили заглянуть на минутку и поздороваться.{w} Потому что даже то, что в открытое окно изнутри не доносилось ни звука, их не насторожило."
    scene dct_ext_music_club_verandah_opendoor_day
    show d_ma smile pioneer at right:
        yalign 0.02
    with dissolve
    "Максим чуть отстал от проскользнувшей вперед Сашки и, может быть, даже так бы и прождал ту на веранде, не заходя в помещение, если бы не..."
    show d_ma surprise pioneer with dspr
    sa "Максииим!"
    stop sound_loop
    scene bg int_musclub_day with slidedown
    "Мику играла.{w} Руки бегали по клавишам, голова чуть покачивалась в такт музыке, спина наклонялась то вправо, то влево. Губы ее шевелились, а на щеках блестели влажные следы слез.{w} Но рояль не издавал ни звука, пальцы проваливались сквозь неподвижные клавиши, а сквозь тело Мику начинал просвечивать интерьер кружка."
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
    "А белая как мел, отчаянно трусящая Сашка, не думала ни о каких привидениях, а бросилась к Мику, обнимая ее."
    show mi cry pioneer close:
        linear 2 alpha 0.5
    show d_ma surprise pioneer at cleft with dissolve_fast:
        zoom 1.0 yalign 0.02
    "Неизвестно, что сработало: инстинкт, или Сашина скрытая память о том, как она сама начала похоже растворяться, после контакта с Пионером."
    show d_ma surprise pioneer with dissolve_fast:
        zoom 1.25 yalign 0.08
    show mi cry pioneer close:
        linear 2 alpha 0.4
    "Но дальше Сашка уже пронзительно кричала:"
    sa "Мику, останься!"
    play music music_list['memories_piano_outdoors'] fadein 4
    show mi scared pioneer close with dspr:
        linear 8 alpha 1.0
    show sl tender sport close as sl2 at cright behind mi:
        alpha 0
        pause 3
        linear 1 alpha 1
    show d_ma shy pioneer as d_ma2 at cleft behind mi:
        zoom 1.25 yalign 0.08 alpha 0
        pause 3
        linear 1 alpha 1
    "Пока вместе с Максимом они обнимали с двух сторон поролоново-мягкие, но уже постепенно твердеющие и набирающие плотность плечи руководителя музыкального кружка."
    stop music fadeout 1.5
    show black with dissolve
    
    pause 0.5
    

    play sound_loop ambience_camp_center_day fadein 1
    scene bg ext_dining_hall_near_day with dissolve
    stop sound_loop fadeout 5
    play ambience ambience_dining_hall_full fadein 5
    show dct_ext_dining_door_day:
        anchor(0.52, 0.51) pos(0.5, 0.5) alpha 0
        pause 1.5
        linear 1 alpha 1
    show int_dining_hall_people_day:
        alpha 0
        pause 4
        linear 1 alpha 1
    "Женя обогнула стайку пионеров из среднего отряда, изучающих график посещения бани, и зашла в столовую. Помахала рукой Сереже, стоящему в очереди к раздаче, и пошла отвоевывать столик на двоих."
    scene dct_int_dining_hall_table_day_back_people
    show dct_int_dining_hall_table_day_chairs
    show mz normal pioneer close:
        xcenter 0.39 ycenter 0.4
    show dct_int_dining_hall_table_day_front
    with dissolve
    show el laugh pioneer close behind dct_int_dining_hall_table_day_front:
        xcenter 1.25 ycenter 0.22
        linear 0.9 xcenter 0.76
        pause 0.15
        linear 0.5 ycenter 0.47
    "Через минуту Сережа опустил на стол поднос с двумя порциями завтрака."
    el "Вот и я, с добычей." 
    show mz smile pioneer close with dissolve_fast:
        xcenter 0.4
    mz "Приятного аппетита."
    show d_mz sceptic pioneer close as mz:
        xcenter 0.39
    show d_el shy3 pioneer close as el
    with dissolve_fast
    "Можно было оглядеться."
    show int_dining_hall_people_day with dissolve
    pause 0.4
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
    "Вот Семен с Ульяной и Алиса с ними, за одним столиком."
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
    "Вот Мику, Саша, Максим и Лена."
    "Мику необычно осунувшаяся и бледная, но улыбается и ест с аппетитом, больше всего она сейчас похожа на выздоравливающую после тяжелой болезни. Куда-то она уходила из домика этим утром, но дело ее."
    show mz normal pioneer close
    show el smile pioneer close
    show d_cs smile glasses far:
        zoom 0.8 anchor (0.5, 0.9) pos (1.1, 0.975) rotate 0.0 transform_anchor True
        linear 0.6 pos (1.035, 0.975) rotate -17.5 transform_anchor True
    "Доктор, кстати, поглядывает на Мику с легким профессиональным интересом."
    hide mi
    hide sl
    hide d_ma
    hide un
    hide d_cs
    hide int_dining_hall_people_day
    with dissolve
    mz "Что нового, Сережа?"
    show el normal pioneer close with dspr
    el "Нового? Шурик что-то затеял, но пока меня в секреты не посвящал.{w} Вставал ни свет ни заря, и сейчас позавтракал вперед всех и куда-то убежал."
    show d_mz sceptic pioneer close as mz with dspr
    mz "Будешь ему помогать?"
    show el sad pioneer close with dissolve_fast
    el "Ох, Женька."
    # Сережа вздохнул.  # Опускаем
    show d_mz hope pioneer close as mz with dspr
    mz "Если позовет — помогай. Я знаю, для тебя это важно."
    show int_dining_hall_people_day with dissolve
    "Поток пионеров от входных дверей к раздаче постепенно иссякал."
    show mt normal pioneer:
        xcenter 0.65 alpha 0
        linear 1 alpha 1
        pause 0.7
        ease 1.3 xcenter 0.14
        pause 1.1
        linear 0.5 ycenter 0.7
    show d_sf normal sport:
        xcenter 0.55 ypos 0.2 alpha 0
        pause 3.1
        linear 1 alpha 1
    show d_us normal sport:
        xcenter 0.75 ypos 0.09 alpha 0
        pause 3.4
        linear 1 alpha 1
    show dv normal pioneer at cleft:
        ycenter 0.66 alpha 0
        pause 3.1
        linear 1 alpha 1
    "Последней зашла Ольга Дмитриевна, взяла на раздаче кусок хлеба, положила на него вчерашнюю холодную котлету, накрыла вторым куском и с этаким гамбургером в одной руке, и стаканом какао в другой прошла за столик к Семену."
    hide mt
    hide d_sf
    hide d_us
    hide dv
    with dissolve
    "Какое-то время было тихо, только иногда брякали вилки о тарелки, да стоял равномерный шум, обычный для столовых в час пик."
    show el grin pioneer close
    show mz normal pioneer close
    hide int_dining_hall_people_day with dissolve
    el "Жень, давай ты библиотеку сегодня не будешь открывать."
    show d_mz fun pioneer close as mz with dspr
    mz "Я и не собиралась."
    show el smile pioneer close with dspr
    extend " Все равно никого не будет. Воскресенье же, уборка, стирка, баня и так далее."
    show d_mz excitement pioneer close as mz with dissolve_fast:
        xcenter 0.4
    "Скажи, а ты умеешь грести?"
    window hide
    show d_el shy pioneer close as el with dspr
    pause 0.2
    stop ambience fadeout 1
    show black with dissolve
    
    pause 1.5
    

    play music music_list['my_daily_life'] fadein 1
    play sound_loop ambience_int_cabin_day fadein 2
    scene dct_dv_mirror
    show black:
        alpha 1
        pause 1.5
        linear 1 alpha 0
    window auto
    "Перетаскивающая вещи Алиса старательно делала злобное лицо, но, на самом деле, была страшно довольна."
    th "Что тут у нас осталось?"
    extend " Полный шкаф платьев?"
    scene dct_closet_with_dresses with dissolve:
        yalign 0.0
        pause 1
        ease 2 yalign 1.0
    th "Интересно, для чего человеку столько платьев, если их ни разу не надевали?"
    "Взять эти платья, постараться сложить их покомпактнее и закинуть охапку на плечо. В руки, дополнительно, взять картонную коробку с чайными чашками, сахаром, печеньем и мелким барахлом."
    # В дверях столкнуться с Максимом.  # По канону
    stop sound_loop fadeout 1
    play ambience ambience_camp_center_day fadein 1
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
    dv "Свое таскай."
    "Ну, Максим и таскал свое.{w} А что свое? Походный рюкзак, с которым он приехал и пару удочек."
    show dv guilty pioneer with dspr
    dv "Ты что, на рыбалку ходишь?"
    show d_ma smile pioneer with dissolve_fast
    d_ma "Если получается."
    show dv grin pioneer with dissolve_fast:
        xcenter 0.16
    dv "Пойдешь — меня позови."
    scene black with squares
    "Вожатая хитрая!"
    show mt smile pioneer close with dissolve:
        xcenter 0.38
    mt "Я, между прочим, в твоих интересах все решила."
    show mt grin pioneer close with dissolve_fast
    extend " Так что, Алиса, таскать тебе."
    hide mt with dissolve
    "Вот Алиса и таскала."
    scene bg ext_houses_day with squares
    th "Сразу с крыльца повернуть направо, через два домика налево, еще раз налево и опять через два домика направо."
    th "Прочь с дороги, иду по приборам, а то из-за этих чертовых платьев ничего не видно."
    "Максим скинул на новом месте свое барахло, догнал и все таки забрал себе половину платьев, пошел рядом.{w} Кивнуть ему."
    scene dct_ext_сentral_alley_from_dining_hall_to_west
    show d_sf normal pioneer at cleft
    with dissolve
    th "А вот и Сенька. Тоже сегодня в роли грузчика."
    th "Тяжелое ему Ульяна таскать запретила, поэтому у него ходок больше выйдет."
    show d_sf serious pioneer
    extend " Но ему таскать проще, все по главной аллее."
    th "Ну Ольга, ну реформатор."
    extend " А сама сейчас на пляже."
    scene bg ext_houses_day with squares:
        xzoom -1
    show dv normal pioneer at right:
    show d_ma normal pioneer at cleft:
        yalign 0.02
    with dissolve
    dv "Сенька, не хватайся за коробку, она легкая. Лучше дверь открой."
    show dv smile pioneer with dspr
    extend " Как там наша Рыжая?"
    me "Обещала к двенадцати."
    dv "Значит один час у нас еще есть."
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
    th "Но Ольга все равно молодец, я ей даже дерзить до конца цикла не буду."
    show mt sad pioneer close as mt2:
        xcenter 0.38 alpha 0
        pause 0.25
        linear 0.25 alpha 1
    extend " Наверное."
    stop music fadeout 2.5
    stop ambience fadeout 1
    play sound_loop ambience_dining_hall_full fadein 1
    scene dct_int_dining_hall_table_day_back_people
    show mt normal pioneer close:
        xcenter 0.38
    show dct_int_dining_hall_table_day_front
    with blinds
    "На завтраке Ольга, подсев к Алисе за столик, спросила:"
    mt "Ну как, готова к переезду?"
    dv "Нет."
    "Ответила Алиса честно и откровенно."
    show mt smile pioneer close with dspr
    mt "А придется."
    # show mt smile pioneer close with Dissolve(0.0):
    show mt smile pioneer close:
        linear 0.55 ycenter 0.23
    scene int_dining_hall_people_day
    show mt normal pioneer:
        xcenter 0.5 ycenter 0.7
        linear 0.5 ycenter 0.5
    with dissolve_fast
    "Вожатая поднялась и, перекрывая шум столовой, сделала объявление:"
    mt "Пионеры и к ним примкнувшие, минутку внимания."
    mt "Во-первых, с сегодняшнего дня, наш горнист уже официально переводится в старший отряд."
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
    extend " А Алиса улыбается невольно."
    show mt normal pioneer with dspr
    mt "Но это еще не все."
    "Ольга выждала, пока не стихнет шум, и продолжила."
    mt "Я решила навести порядок с проживанием персонала."
    show mt smile pioneer with dspr
    extend " И отдельных пионеров тоже."
    stop sound_loop fadeout 1
    play ambience ambience_int_cabin_day fadein 1
    show dct_int_chief_corridor_day with squares
    "И вот, командирским решением, Ольга, две поварихи из трех и Персуновы сейчас переселяются в административный корпус."
    stop ambience fadeout 1
    play sound_loop ambience_dining_hall_full fadein 1
    hide dct_int_chief_corridor_day with squares
    mt "Физруки, хватит жить в тренерской, когда в корпусе есть спальни для персонала."
    stop sound_loop fadeout 1
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_house_of_mt_day with dissolve    
    "Максим и Семен-второй, который, кстати, еще не приехал, поселяются в бывшем домике Ольги."
    show dv grin pioneer at right:
        alpha 0
        pause 1
        linear 1 alpha 1
    "Но таскать Ольгины вещи приходится Алисе, не великая цена за то, чтобы остаться жить в своем домике."
    show dv normal pioneer with dissolve_fast
    th "А ведь есть и минусы. Теперь вот так, запросто, к Сеньке с Рыжей не забежишь, всегда есть шанс нарваться на вожатку."
    show dv laugh pioneer with dspr
    extend " Ну ничего, у меня будем собираться."
    stop ambience fadeout 1
    play sound_loop ambience_int_cabin_day fadein 1
    show dct_int_chief_corridor_day with blinds
    "Все, последняя ходка была, дальше уж пусть сама вожатая разбирается, чего и куда повесить."
    scene dct_int_residential_block_day with dissolve
    "Алиса и Максим скинули охапку платьев на незастеленный матрац и огляделись."
    th "А ведь неплохо можно устроиться."
    "Две кровати, шифоньер, книжный шкаф, стол обеденный и стол письменный. Какое-то подобие прихожей, кухонная ниша, с плиткой и раковиной, и, напротив, Алиса толкнула дверь, умывальник, унитаз и даже душ за прозрачной занавеской."
    "Все очень маленькое, но своё. Хочешь питайся и мойся отдельно, хочешь — ходи в столовую и в баню."
    "Будильник, извлеченный из коробки показывал без пятнадцати двенадцать. Пора, наверное."
    show dct_int_chief_corridor_day with dissolve
    "Алиса вышла в коридор и просунула голову в дверь Семеновой комнаты.{w} Тот сидел на кровати, утирая лоб, и тоже оглядывал помещение, прикидывая явно, как и куда сдвинуть вместе обе кровати."
    
    $ renpy.music.set_volume(1.0, delay=2)
    play music dreamers_of_the_day fadein 2

    dv "Ну что, идем?"
    me "Идем, Алиса."

 
    stop sound_loop fadeout 1
    scene bg ext_path2_day with fade
    show un smile pioneer far:
        xcenter 0.41
    show sl smile dress far:
        xcenter 0.59
    with dissolve
    "Осведомленные или приглашенные пионеры и к ним примкнувшие из двух лагерей, поодиночке, парами и тройками, старясь не привлекать внимания, исчезали за забором и тянулись к костровым полянам."
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
    "Не все, в основном старший отряд и чуть-чуть мелких, оставляя на часок лагеря на произвол судьбы."
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
    "А все потому, что вчера вечером Семен изрек:"
    play ambience ambience_camp_center_night fadein 1.5
    $ renpy.music.set_volume(0.4, delay=2)
    
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
    extend " Есть еще несколько мест, но поляна симпатичнее всего, не в пещеру же спускаться."
    show un shy pioneer with dspr
    "За что был вознагражден приглушенным, но восторженным воплем Ульяны и ее репликой:"
    show d_us laugh sport_windbreaker
    show d_sf smile hike
    with dspr
    us "Гениально, Сёмка."
    show d_us smile sport_windbreaker
    show un smile pioneer
    with dspr
    extend " Хоть ты конечно тормоз."
    show d_us serious sport_windbreaker
    show d_sf normal hike
    with dspr
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
    "Все когда-нибудь бывает впервые."
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
    "И никто из заинтересованных лиц не услышал, как на остановке зафырчал приехавший, на три часа раньше положенного срока, Икарус."
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