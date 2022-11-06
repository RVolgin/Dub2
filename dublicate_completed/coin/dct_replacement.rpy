    #################
    #Глава 8. Замена#
    #################


label dct_replacement:
    $ save_name = u"Дубликат. Монетка в фонтане -- Замена"
    $ day_time()
    $ persistent.sprite_time = "day"
    scene black
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
    th "В носу свербит, а скоро потечет."
    us "Вот зачем под дождем бегал? Алиска бы одна справилась прекрасно."
    th "Вот-вот, и я о том же."
    th "Зачем я бегал под дождем?"
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
    "Сейчас сижу на длинной скамье в спортзале, смотрю, как половина мелких перекидывает мячик через сетку, играя в игру, которую они считают волейболом."
    "А вторая половина окружила Ульяну и о чем-то серьезно с ней беседует.{w} Я даже ревную чуть."
    "На улицу не выйти — дождь. Средний отряд оккупировал столовую, с ними там Ольга и Алиса, младший, весь целиком, а не только футбольная команда, здесь у меня. Ну а старшие, те старшие, те сами по себе."
    "Но вот через час у старших собрание, где Максим главный герой."
    me "Рыжик, ты не в курсе, где собрание будет?"
    "Тут доступных мест-то…"
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
    th "Я уже давно потерял право на участие в отрядной жизни, наверное с тех пор, как заявил свои права на Ульяну."
    extend " Или с тех пор, как Рыжик заявила свои права на меня."
    show d_sf sad sport with dspr
    th "Вот так, сохранил прекрасные отношения со всеми, даже со спящими еще Мику и  Сашкой, даже с Женей, даже с кибернетиками. А из отряда, из компании, которая, пусть изредка, но выделяет себя из общей лагерной массы, выпал."
    th "Понятно, что двадцатипятилетний заместитель руководителя лагеря по физическому воспитанию не может быть в пионерском отряде, наравне с пионерами, но обидно."
    show d_sf normal sport with dspr
    th "Даже мелкие больше меня за октябренка держат, чем старшие — за пионера. Даже волейбол и посиделки наши с девочками теперь от случая к случаю проходят, а не каждый вечер, как раньше."
    th "У всех свои дела."
    extend " Вот могли бы собрание и здесь провести, но предпочли чаепитие у Алисы на складе."
    show d_sf serious sport with dspr
    "Дальше посидеть и посокрушаться у меня не получается."
    stop ambience fadeout 2.5
    play sound dct_sveta_falls_in_gym
    show d_sf serious sport:
        pause 0.5
        linear 0.5 alpha 0
    "Одна из девочек бросается за мячом, неловко наступает, подворачивает ногу и падает, пытается встать, вскрикивает и снова падает."
    
    play music music_list['afterword'] fadein 2.5
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
        zoom 0.88 xcenter 0.65 yalign 1.01

    with pixellate
    "Ну что, подскакиваю с места и уношу Светку с площадки к себе на скамью."
    me "Больно? Давай гляну."
    "Эта мелочь развернулась в мою сторону, и протягивает правую ногу, положив лодыжку мне на колени."
    d_sv "На, глянь."
    "А вот не нравится мне эта лодыжка. Растяжение, даже доктором быть для этого не обязательно, чтобы понять."
    show d_sv upset with dspr
    "Знаю, что завтра отроковица будет в полном здравии, но сейчас ей больно и она еле сдерживается, чтоб не заплакать, только тихо поскуливает, когда я очень осторожно проверяю подвижность сустава."
    show d_sf serious sport:
        pause 0.6
        linear 1 alpha 0
    me "Больно. Вижу. Посиди здесь, я сейчас."
    show d_sf sad sport with dissolve:
        alpha 1
    "Приношу из тренерской эластичный бинт и обматываю Светкину щиколотку."
    show d_sv sad with dspr
    "В принципе, можно больше ничего не делать до завтра, все равно у пионеров все повреждения восстанавливаются за несколько часов."
    "Но пионеры же об этом не знают, девочке же страшно и больно. Надо ее в медпункт."
    show d_sf normal sport with dspr
    me "Ходить ты, конечно, не в состоянии."
    show d_sf smile sport
    show d_sv surprise
    with dspr
    # me "Ну, цепляйся за шею, понесу тебя к доктору."    # По канону
    
    me "Ну, хватайся крепче, понесу тебя к доктору."
    
    show d_sf smile sport:
        anchor (0.5, 0.0) pos (0.3, 0.2)
        linear 1 anchor (0.5, 0.0) pos (0.51, 0.0) knot (0.5, 0.2)
    show d_sf_grabs_d_sv:                                      # Подхватывание Светы (спрайт становится видимым через 0.55 секунды)
        anchor (0.5, 0.0) pos (0.3, 0.2)
        linear 1 anchor (0.5, 0.0) pos (0.51, 0.0) knot (0.5, 0.2)
    show d_sv surprise:
        pause 0.55
        alpha 0

    show d_ge:
        pause 0.5
        easeout 0.8 xcenter 1.15
    pause 1
    show d_sf sad sport
    show d_oz n pioneer
    with dspr
    th "Ох, спина ты моя молодая!"
    # "Оксана бежит, открывает передо мной двери спортзала. Ульяна смотрит на меня."  # По канону
    show d_sf_carrying_d_sv smile:
        xcenter 0.51
    hide d_sf_grabs_d_sv
    "Геля бежит, открывать нам двери спортзала. Ульяна смотрит на меня."
    show d_us hurt sport with dspr
    us "Донесешь, Сёмк?"
    show d_sf smile sport with dspr
    
    $ persistent.sprite_time = "day"        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    me "Куда я денусь, тут живого весу то…"
    
    show black with dissolve_fast
    $ persistent.sprite_time = "night"
    
    scene dct_ext_сentral_alley_from_dining_hall_to_west_after_rain
    show d_sf normal sport at left
    show d_sf_carrying_d_sv sad at left
    with dissolve_fast
    "Пока играли, пока лодыжку щупали, дождь унесло куда-то на север и он поливает в районе той поляны, где есть переход в лагерь Виолы."
    "Осторожно несу калеку в обход столовой и через площадь к медпункту, лавируя между лужами."
    "Со спортплощадки есть прямая дорожка, по задам столовой и склада, но ну ее, она сейчас раскисла, и тащить по ней груз, даже такой легкий, как вот эта второклассница, занятие архинеприятное."
    
    # "Вот и солнце показалось, сейчас все быстро высохнет."  # По канону
    "Вот и тучи начали расступаться, сейчас все быстро высохнет."
    
    scene dct_ext_dining_hall_away_after_rain
    show d_sf normal sport at center
    show d_sf_carrying_d_sv sad at center
    with dissolve
    d_sv "Тебе не тяжело меня нести?"
    show d_sf serious sport with dspr
    "А я прямо сейчас понял — почему я так привязался к мелким. Все дело в их безоговорочном ко мне доверии, всего-навсего."
    "Я еще держу в голове остатки фантомных воспоминаний, внушенных Системой мне — спящему дубликату."
    show d_sf sad sport with dspr
    "Так вот, в той своей фантомной биографии, я не доверял никому, вовсе."
    "И сам вот так, как они, не смог бы, просто не хватило бы сил."
    show d_sf normal sport with dspr
    "И поэтому вот такое доверие, оно в моем представлении что-то настолько ценное, что просто не может существовать."
    "Почти столь же ценное, как Ульянкина любовь ко мне.{w} Которая тоже не должна была случиться."
    scene dct_ext_square_after_rain
    show d_sf smile sport at right
    show d_sf_carrying_d_sv sad at right
    with dissolve
    me "Уж, как-нибудь, мелочь, я тебя донесу."
    show d_sf_carrying_d_sv shy with dspr
    "Мелочь благодарно прижимается, насколько это возможно, в ее положении и состоянии."
    show d_sf sad sport with dspr
    "А вот моя спина благодарности не высказывает, моя спина высказывает свои претензии."
    show d_sf normal sport
    show d_sf_carrying_d_sv smile
    with dspr
    "Я все таки тормоз, Рыжик права. Надо было посадить девочку на раму, и мы прекрасно бы с ней доехали на велосипеде. Зря что ли мы их со склада забирали?"
    show d_sf sad sport with dspr
    "А сейчас спина будет болеть, а Ульяна ворчать."
    # "Вот и медпункт. Осторожно сгружаю Светку на крыльцо, а сам толкаю дверь."  # По канону
    scene dct_ext_aidpost_after_rain with dissolve

    $ persistent.sprite_time = "night"        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Вот и медпункт.{w} Осторожно толкаю дверь."
    
    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day
    show dct_int_aidpost_day_curtain
    show d_cs normal far
    show d_sf normal sport at left
    show d_sv sad:
        zoom 0.97 xcenter 0.65 yalign 0.21
    with slidedown
    me "Доктор, я к вам пациента принес."
    show d_cs normal stethoscope far:
        xcenter 0.8
    show d_sv sad:
        zoom 0.73 xcenter 0.93 ycenter 0.69
    show d_sf sad sport:
        xcenter 0.12 ypos 0.2
    with fade
    "Семен помог Светлане допрыгать до кушетки, а сам уселся на стул и стал ждать заключения доктора."
    th "С прошлого цикла ничего здесь не поменялось."
    show d_sf serious sport with dspr
    th "А что и кто здесь может поменяться?{w=0.4} Докторица?"
    show d_cs smile stethoscope far
    show d_sv shock
    with dspr
    th "Вот интересно, я сам в конце-концов в подобного «физрука» превращусь?"
    extend " Или скачусь назад, в пионеры?"
    show d_sf sad sport with dspr
    extend " И каково девчонкам это видеть будет?"
    "Занавеска, вокруг второй кушетки была задернута, и кто-то иногда тихонько всхлипывал за ней, скрытый от посторонних глаз."
    show d_sf normal sport with dspr
    th "Надо ли мне знать, кто там?"
    show d_cs normal stethoscope far with dspr
    "Семен поймал взгляд доктора и кивнул головой в сторону занавески."
    show d_sv upset with dspr
    d_cs "Растяжение.{w=0.4} Семен, дальше уже моя забота."
    "Доктор сделала вид, что не поняла вопроса."
    show d_sv sad with dspr
    me "Свет, обед тебе сюда принесут, я распоряжусь. И сам зайду перед обедом."
    me "Попросить кого, чтобы сейчас пришли?"
    show d_sv smile with dspr
    d_sv "Да, пусть Геля придет."
    show d_sf sad sport:
        linear 0.5 ypos 0.0
    pause 0.5
    "Семен поставил стул на место, попрощался и уже взялся за ручку, когда из-за занавески донеслось:"
    show dct_int_aidpost_day_mi_behind_curtain
    show dct_int_aidpost_day_curtain ajar
    with dissolve_fast
    mi "Се… Сен-нечка, подожди меня."
    hide dct_int_aidpost_day_mi_behind_curtain
    show d_sf serious sport
    with dissolve_fast
    me "Я буду на крыльце, Мику."
    hide  d_sf with dissolve
    
    
    stop music fadeout 1.5
    play ambience ambience_camp_center_day fadein 1.5
    scene bg ext_aidpost_day:
        zoom 2 xcenter 0.45 ycenter 0.4
    show d_sf normal sport:
        xcenter 0.3
    with slideawayup
    pause 0.4
    show d_cs normal stethoscope with dissolve:
        xcenter 0.67
    me "Что с нею, доктор?"
    d_cs "Ничего заразного."
    show d_sf serious sport with dspr
    d_cs "Сами же понимаете, что я не скажу."
    d_cs "Привела ее эта блондинка с косами, можете у нее спросить."
    
    
    "Они еще постояли на крыльце, глядя на быстро высыхающий под солнцем лагерь."
    d_cs "Редко здесь такие дожди бывают."
    "Семен хотел ответить что-нибудь столь же нейтральное, но не успел."
    show mi sad pioneer far behind d_sf with dissolve
    window show
    mi "Простите за задержку. Я еще с девочкой поговорила, успокоила её."
    mi "А то вы её бросили одну на кушетке, а она же маленькая."
    show mi dontlike pioneer far with dissolve_fast
    extend " Стыдно!"
    window hide
    
    
    scene dct_ext_square_profile_view_day
    show d_sf normal sport at center:
        xzoom -1.0
    show mi sad pioneer at right
    with fade
    window auto
    "Семен и Мику шли к складу длинной дорогой, опять мимо Генды, через площадь и налево по главной аллее, в сторону хозворот."
    "Солнце активно сушило лагерь после помывки, асфальт уже, почти везде, из черного становился серым, и обвисшие мокрые флаги уже начинали расправляться на флагштоках, обсыхая на солнце и ветерке."
    "Воробьи вылезли из укрытий и массово принимали водные процедуры в оставшихся лужах."
    scene bg ext_square_day
    show mi upset pioneer at fright
    show d_sf normal sport at cright:
        xcenter 0.65
    with dissolve
    mi "Вот представь себе, Сенечка, лабораторию, а в ней, за стеклянной перегородкой клетки с обезьянками, глупыми и шумными обезьянками.{w} Виварий."
    mi "Сотрудники ходят, разговаривают между собой, свои проблемы обсуждают. Иногда детей своих приводят, «на обезьянок посмотреть»."
    show mi sad pioneer with dissolve_fast
    mi "А всем командует там высокий, слегка сутулый дядька с серыми глазами. Лет ему за тридцать, у него каштановые волосы и борода."
    mi "И зовут этого дядьку..."
    show mi upset pioneer with dissolve_fast
    "Мику замолчала и начала заново."
    stop ambience fadeout 1.3
    window hide
    
    

    play music forgotten_summer fadein 2
    scene black with dissolve
    show promo_text_un u"{color=#00b4cf}Рассказ Мику{/color}" at truecenter with dspr
    $ renpy.pause(3.0)

    $ set_mode_nvl()
    window show

    scene black
    show dct_ext_сentral_alley_from_dining_hall_to_west:
        alpha 0.6
    with dissolve
    "А знаешь, как делали миксов в вашей лаборатории?"
    "Нет-нет, Сенечка, не отвечай, я знаю, что такое миксы, я знаю, что это не твоя лаборатория, что ты не оригинал и не подлинник, я многое теперь знаю.{w} И про тебя и вообще. Про тебя, может даже в чем-то больше, чем ты сам про себя.{w} Машина у Шурика работает{w=0.4}, работала.{w=0.4} Он обещал ее сломать, и я ему верю."
    
    "\nВ общем, взяли такую обезьянку, посадили ее в клетку, клетку обвешали какими-то приборами и вынесли в туман. А из тумана потом к клетке шагнуло…{w} Существо?{w=0.5} Да, пусть будет существо: глупое, пустое, беспамятное и бесполое существо. Первичный организм. Оно вцепилось в клетку и хотело дотянуться до обезьянки, но не могло.{w} А его били током.{w} Как это называется?{w=0.3} Ударили неотпускающим током через прутья клетки, и начали это существо «наполнять информацией», так кажется. Вот только, когда оно, это существо, нет, уже она — девочка, осознала себя и впервые посмотрела на мир осмысленно, первое, что она увидела, это вцепившаяся с той стороны в прутья решетки мертвая обезьянка.{w} И табличка на клетке: пол, возраст, вес, инвентарный номер и кличка: «Мику»."
    
    "\nВот у вас у всех, Сенечка, были мама и папа. Пусть у ваших оригиналов, но все равно были. А у таких как я, только обезьянка.{w} Я не обижаюсь на твоего оригинала, это ведь была его лаборатория, если бы не он, меня бы не было на свете. Так что я считаю его своим папой. А мой оригинал — обезьянка по кличке Мику. А твой оригинал, он, действительно, хотел нам только добра и относился к нам, как к собственным детям. И у него все получилось. Но обезьянку жалко.{w} А может, Сенечка, она не умерла? Может она во мне теперь живет? Потому что я помню теперь все, что она видела и слышала. Все разговоры, и всех людей, которые проходили мимо. Она слышала разговоры, запоминала, но не понимала.{w} А я поняла только то что смогла, ведь я, всего лишь шестнадцатилетняя пионерка, подвинутая на музыке, а не технарь, как Сережа. И помню, как обезьянке было страшно, одной в том тумане."
    
    "\nСенечка, я сегодня чуть с ума не сошла. Сижу в кружке у себя, пытаюсь играть, под дождь так хорошо играется, а вижу себя обезьянкой в клетке.{w} У меня истерика случилась, а Сашенька с доктором меня валерьянкой и еще каким-то таблетками отпаивали. Поэтому я замороженная сейчас, не обращай внимания, это пройдет.{w} А знаешь, почему я с ума не сошла? Из-за той сказки, что ты принес. Я подумала, что если моя сестра способна творить, то, значит, и я сумею.{w} А обезьянка — нет, обезьянки творить не умеют. А еще я за твою историю с Микусей уцепилась. Я и эту историю тоже теперь помню. Да, Микуся там, в мире наших снов, и здесь она не появится никогда, но свою память она нам подарила.{w} Сенечка, ведь если она была счастлива, пусть даже так коротко и такой ценой, значит и для меня где-то запасен в мире кусочек счастья?!"

    stop music fadeout 1.5
    window hide


    $ set_mode_adv()

    play ambience ambience_camp_center_day fadein 1.3

    scene bg ext_dining_hall_away_day
    with blinds
    
    window auto
    "Где-то, напротив столовой, мимо них проскользнули Женя с Сергеем."
    show d_el shy_think pioneer far:
        xcenter -0.3
        linear 4.5 xcenter 1.19
    show d_mz happy glasses pioneer far:
        xcenter -0.19
        linear 4.5 xcenter 1.3
    "Женя, расправившая плечи и гордая, и Электроник, с несколько обалдевшим видом."
    mi "Какая Женечка красивая..."
    "Мику отметила это мимоходом, ни капельки не сбившись с общего повествования."
    show dct_ext_storage_day
    show d_sf normal sport:
        xcenter 0.2
    show mi sad pioneer at cright
    with blinds
    "Так за разговором, хотя, говорила почти одна Мику, а Семен больше молчал, дошли до ворот склада."
    mi "Сенечка, я еще хочу сказать, что я, может быть, забуду всё между циклами. Но прежней Мику, какой вы ее знали, в этом узле, уже не будет."
    me "Мику.{w=0.5} Куда ты денешься?{w} Ты и сейчас прежняя, только еще не поняла этого."
    stop ambience fadeout 1
    
    play sound_loop ambience_int_cabin_day fadein 1
    scene dct_int_warehouse_day with slidedown
    "Семен, наконец, потянул за ручку, и, пропустив Мику на склад, зашел сам."
    "Восемь пар глаз смотрели на них. Пахло пылью, свежим постельным бельем, крепкозаваренным чаем и Сашкиной выпечкой."
    show dv angry pioneer2 far at left with dissolve
    dv "Ну, наконец-то."
    show dv grin pioneer2 far with dissolve_fast
    extend " Наливайте себе чай и начинаем."
    stop sound_loop fadeout 1
    show black with dissolve
    
    pause 0.5
    
    
    play music music_list['confession_oboe'] fadein 1
    scene dct_ext_clubs_rain with dissolve
    "Делать Шурику было совершенно нечего.{w} Может быть, впервые, за все бесчисленные циклы."
    scene bg int_clubs_male_day
    show dct_int_clubs_male_rain
    with squares
    "Он сидел в кружке, листал подшивку «Радио», не вникая в суть текста, смотрел как компьютер пытается расшифровать абракадабру, записанную на ленте видеомагнитофона."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.95
    "Всего-то и нужно было, что поменять местами две платы, благо они внешне были совершенно одинаковые."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.9
    "Александр помалкивал. Шурик чувствовал его присутствие у себя в голове, но и только.{w} Как будто находишься в комнате, где за твоей спиной есть кто-то еще.{w} Этот кто-то молчит, и вообще, старается никак не проявлять себя, но ты его чувствуешь."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.85
    th "Значит, прибор работает, то есть работал."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.8
    th "Сам сделал, сам и сломал."
    "Легко можно было все исправить, но Шурик точно знал, что он этого делать не будет."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.75
    th "Если каждый из обитателей вспомнит что-то подобное тому, что вспомнил я…"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.7
    extend " Эта штука, в масштабах Сети, будет посильнее атомной бомбы."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.65
    extend " А для большинства людей, которые все вспомнят, это просто катастрофа."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.6
    th "Александр, он бы обязательно сделал что-то подобное. Просто, чтобы посмотреть что получится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.55
    extend " Семен верно сказал в день приезда: «Какая великолепная физика!»"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.5
    th "Прежний Шурик, тот бы проделал всё ради торжества прогресса, а вот нынешний я, без сожаления взял и все уничтожил, свою Нобелевскую премию, которой тут нет."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.45
    "В голове что-то поворочалось и опять затихло."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.4
    th "Интересно, что я себя с Александром не отождествляю — просто посторонний человек, делящий со мной моё тело и подаривший мне свою память."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.35
    "Шурик выглянул в окно: дождь заканчивался, он еще сеял россыпью мелких капель по лужам, но небо на юго-западе уже голубело, тучу явно утягивало в сторону леса."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.3
    "Делать было решительно нечего, а начинать новый проект не хотелось. Пока объяснишь Сыроежкину, почему бросаем старый, пока сам поставишь себе задачу, пока, пока, пока… Так и цикл закончится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.25
    extend " Тем более, в условиях Сети, ничего глобального, что имело бы перспективы, создать не получится."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.2
    "Проще дождаться нового цикла, когда сбросится память, и начать с чистого листа, когда будешь верить, что ты — Шурик Трофимов, перспективный выпускник, за которого бьются пять ведущих вузов СССР, а не копия давно умершего человека, живущая двухнедельными циклами внутри пространственной вакуоли."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.15
    "А сейчас, нужно подчистить следы своих манипуляций с установкой."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.1
    "Сыроежкин, конечно, сейчас видит только Женю, но парень он умный и наблюдательный.{w} «Микс», — мелькнуло в голове, «Человек!» — упрямо подумал Шурик."
    show dct_int_clubs_male_rain:
        linear 1 alpha 0.05
    th "На собрание сходить?"
    show dct_int_clubs_male_rain:
        linear 1 alpha 0
    th "Можно и сходить, но, сначала, еще одно дело. Кое-кому я сильно задолжал."
    stop music fadeout 1
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_clubs_day
    show 3500_sh normal_smile pioneer:
        zoom .17 anchor (.5, 1.0) pos (.48, .72)
    with slideawayup
    "Шурик вышел на крыльцо. Дождь окончательно прекратился, лужа, разливавшаяся на всю ширину главной аллеи, уже стекла ручьем в реку и сейчас асфальт быстро сох под летним солнцем."
    show 3500_sh smile pioneer with dissolve_fast
    th "Должна она появиться, должна."
    show 3500_sh normal pioneer with dissolve_fast
    th "Ограничители в моей голове сняты, сейчас здесь только я и Вселенная. И никаких дополнительных фильтров восприятия, кроме своих личных, тех, что у всех людей присутствуют."
    scene dct_ext_another_clubhouse_day with dissolve
    # "Шурик вынес на улицу табурет и присел под навесом, внимательно глядя на крыльцо заколоченного здания напротив."    # По канону
    "Шурик вынес на улицу табурет и присел под навесом, внимательно глядя на крыльцо заброшенного здания напротив."
    th "Нужно только один раз увидеть, а дальше пойдет само."
    show d_jn:
       xzoom 1.8 yzoom 0.35 anchor (0.5, 1.0) pos (0.46, 0.795) blur 70 alpha 0
       easein 3 xzoom 0.21 yzoom 0.21 blur 10 alpha 1
       linear 1 blur 0
    "Воздух над крыльцом начал дрожать, а пожарный щит, закрывавший входную дверь, замерцал, затмеваемый металлическим блеском. Область металлического блеска все сокращалась, делаясь все более непрозрачной, пока не собралась в небольшую, ростом с пяти-шестилетнего ребенка, металлическую фигурку."
    "Потускневшая полировка панциря, исцарапанный лицевой щиток, прикрывающий фотоэлементы, кончик левого уха чуть загнут назад. Серая от микротрещин, а когда-то была черной, резиновая гофра на суставах."
    "Положив правую руку на перила фигурка стояла абсолютно неподвижно, как умеют стоять только памятники и механизмы.{w} И, в то же время, Шурик ясно чувствовал, что оттуда, из-за зеркального лицевого щитка, за ним внимательно наблюдают."
    "Шурик встал с табурета, сделал несколько шагов, спустившись с крыльца на асфальт аллеи, и, присев на корточки, протянул руки навстречу механоиду. Почти как когда-то, множество циклов тому назад."
    "Что-то толкалось в груди, что-то не давало говорить ровно."
    sh "Ну здравствуй, Яна."
    scene dct_ext_camp_entrance_day
    show d_jn:
        zoom 0.17 anchor (0.5, 1.0) pos (0.265, 0.75)
    show 3500_sh normal pioneer:
        zoom 0.17 anchor (0.5, 1.0) pos (0.3, 0.75)
    with dissolve
    "Зажужжали приводы, застучали каучуковые подошвы по доскам крыльца и асфальту."
    "Подхваченный двумя руками кошкоробот взлетел к небу и плавно опустился на землю."
    "Корпус робота изредка подрагивал и на эти единичные импульсы накладывалась еще и низкочастотная вибрация."
    "Резиновые ладони обхватили ладони белковые, бывший алюминиевый бидон прижался к человеческим ногам, голова, когда-то выколоченная Сыроежкиным из металлического листа вокруг деревянной болванки, сначала уткнулась лбом в пряжку ремня, а через минуту задралась, так, что в лицевом щитке отразились очки и мокрые глаза за ними."
    d_jn "Здравствуй, па!"
    stop ambience fadeout 1
    show black with dissolve
    
    pause 0.5
    
    
    play music music_list['farewell_to_the_past_full'] fadein 1
    scene dct_int_warehouse_day
    show dv smile pioneer2 far at fleft

    show black
    show d_ma normal pioneer:
        xcenter 0.5 yalign 0.02
    with dissolve
    "Не смотря на вчерашние слова Саши, что все проголосуют за него, Максим волновался."
    show d_ma serious pioneer with dissolve_fast
    "Он уже привык относить себя к старшему отряду, и если вдруг большинство проголосует против…{w} Он, конечно, переживет, но будет обидно."
    show d_ma rage pioneer with dspr
    "А уж в среднем отряде как обрадуются. И найдутся желающие поднять свой авторитет за счет «выскочки», обязательно найдутся."
    show d_ma angry pioneer with dspr
    extend " Разберется, конечно, но отдых будет испорчен."
    show d_ma normal pioneer with dissolve_fast
    hide black with dissolve2
    "Сразу после завтрака Максим увязался за Алисой и почти три часа помогал ей наводить порядок на складе."
    show d_ma normal pioneer:
        easeout 1 xcenter 0.75 alpha 0
    "Во-первых, чтобы не трястись от волнения."
    hide dv with dissolve
    "Во-вторых, от Витьки — соседа по домику, все равно никакой поддержки ждать не приходится."
    "Витька, вообще, последнее время, изменился. Дерганный какой-то стал, как-будто Максим ему чем-то не нравится."
    show d_ma angry pioneer with dissolve:
        zoom .75 xcenter 0.36 yalign 1.01 alpha 1

    "Вчера, поздно вечером, вообще чуть не подрались по непонятному поводу: Катерину Максим у Витьки уводит."
    show d_ma serious pioneer with dspr
    "Максим пожал плечами.{w} То что лагерь маленький и Катя все время на глаза попадается, разве Максим в этом виноват."
    show d_ma normal pioneer with dissolve_fast
    "Кто этих влюбленных поймет?"
    show dv grin pioneer2 close at fright:
        alpha 0
        linear 1.5 alpha 1
    show d_ma shy pioneer with dspr
    "В-третьих, из-за самой Алисы, конечно."
    show dv grin pioneer2 close at fright:
        linear 1.5 alpha 0
    extend " Особенно, когда разглядел за насмешками и подколками живую девушку."
    hide d_ma with dissolve
    "И Максим три часа таскал по складу тюки с грязным бельем, пересчитывал и переписывал лампочки и банки с краской на стеллажах, раскладывал по размерам комплекты пионерской формы."
    "Ну и разговаривал с Алисой, уже без взаимных подколок, а просто, с интересом слушая девушку и рассказывая о своем."
    show dv grin pioneer2 far at cright:
        alpha 1
    show d_ma normal pioneer:
        zoom .75 xcenter 0.45 yalign 1.01
    with dissolve
    "Вот только однажды случился неловкий момент. Когда после одного не очень приличного, но ужасно смешного анекдота Алиса, отсмеявшись, прокомментировала, старушечьим голосом: «Ох и молодежь нонеча пошла…»"
    show dv laugh pioneer2 far
    show d_ma grin pioneer
    with dissolve_fast
    d_ma_dv "Алиса, ты еще скажи: «Вот я, в твои годы!»\nВот я, помню, в твои годы…"
    show dv sad pioneer2 far with dissolve_fast
    "Алиса неожиданно погрустнела, будто действительно что-то вспомнила, и оборвала реплику."
    show d_ma serious pioneer with dspr
    d_ma "Алиса, что-то не так?"
    show 3500_dv sadness pioneer2 as dv with dissolve_fast:
        zoom 0.75 xoffset 20
    window show
    dv "Все так Максим. Не обращай внимания."
    show 3500_dv normal pioneer2 as dv with dspr
    extend " Так, вспомнила одну вещь неприятную."
    hide dv with dissolve
    "А Максим сделал вывод: не провоцировать Алису на воспоминания."
    window auto
    stop music fadeout 1.5
    show black with dissolve
    hide d_ma
    
    pause 0.5

    play ambience ambience_int_cabin_day fadein 1
    show sl smile2 pioneer at cright behind black
    hide black with dissolve
    "Первой на склад прибежала Сашка, положила на стол пахнущий корицей пакет, тепло улыбнулась Максиму, и поздоровалась с ним."
    show dv scared pioneer2 close behind sl:
        xcenter 0.14
    show sl scared pioneer close:
        xcenter 0.36
    with dissolve
    "А следом начала что-то на ухо говорить Алисе, Максим уловил только имя Мику."
    show dv guilty pioneer2 close with dissolve_fast
    dv "Может, к ней вернешься, Саш?"
    show sl normal pioneer close with dissolve_fast
    sa "Нет-нет, она сама меня сюда отправила, а то Максимке тут, говорит, совсем страшно будет."
    show dv shy pioneer2 close
    show sl smile pioneer close
    with dspr
    sa "И сама она может быть еще подойдет."
    hide sl
    show dv sad pioneer2 close:
        pause 2
        linear 1 alpha 0
    with dissolve
    "Деятельная Сашка сразу кинулась наводить порядок на рабочем месте Алисы, превращая его в стол для чаепития и не обращая внимания на ворчание хозяйки."
    "Складывалось впечатление, что Алису здесь, внутри отряда, не особо то и боятся."
    "Все журналы и пачка бланков накладных были убраны на подоконник, стол застелен миллиметровкой, отмотанной от неизвестно откуда появившегося рулона, на столе появилась тарелка, а в тарелку была высыпана из пакета горка печенья."
    hide dv
    show sl smile2 pioneer with dissolve
    sa "Вот, состряпала на скорую руку."
    hide sl with dissolve
    "Тут же рядом был водружен чайник, и выставлена батарея разномастных чашек."
    show sl smile pioneer with dissolve
    sa "Раз, два, три, четыре… девять, десять."
    show sl happy pioneer with dissolve_fast
    sa "Все, на всех хватит и никто не уйдет обиженным!"
    hide sl with dissolve
    pause 0.7
    show un normal pioneer far at left with dissolve
    "Второй пришла Лена.{w} Тихо, на грани шепота поздоровалась, на мгновение показала свои зеленые глаза и опять спрятала их под ресницами."
    hide un with dissolve
    "Села около окна и принялась что-то то ли записывать, то ли зарисовывать в блокноте, потаскивая потихоньку печенье."
    show d_us smile sport at cright with dissolve:
        ypos -0.05
    "Прибежала Ульяна, принесла охапку малышовых дождевиков."
    show d_ma surprise pioneer:
        zoom 0.75 xcenter 1.15 ypos 0.06
        easein 0.5 xcenter 1.0 ypos 0.05 rotate -25.0
    th "Это что, уже и дождь кончился, пока я тут пылью дышал?"
    show d_ma surprise pioneer:
        xcenter 1.0 ypos 0.05 rotate -25.0
        easein 0.5 xcenter 1.15 ypos 0.06 rotate 0.0
    show d_us normal sport with dspr
    us "Сёмка чуть задержится. Светка ногу подвернула, он ее в медпункт потащил."
    hide d_us
    hide d_ma
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
    "Следом пришел Шурик, и, почти сразу за ним, Сыроежкин и Женя."
    hide sh with dissolve
    "Шурик сел в углу, обвел взглядом помещение и снял очки. Казалось, что он не очень понимает где находится и зачем он здесь."
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
    "Последними зашли Семен и Мику."
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
    "Мику обменялась взглядами с Сашкой, Сашка встревоженным, Мику успокаивающим, взглянула на Шурика, дождалась его еле заметного кивка, так же еле заметно кивнула в ответ, и взялась за чайник."
    window show
    "Семен устроился рядом с Ульяной, откинувшись спиной на стеллаж, как обычно с непроницаемым выражением лица."
    scene dct_int_warehouse_day
    window auto
    "Минуту все молчали, спрятавшись за чашками с чаем. Только девочки переглядывались и нервно пересмеивались. Все стеснялись начать."
    "Наконец, Мику не выдержала:"
    show mi dontlike pioneer close at fleft with dissolve
    mi "Ну давайте же, ребята. В первый раз для чего-то важного собрались и все стесняемся."
    show mi shy pioneer close with dspr
    extend " Сенечка, может ты начнешь?"
    show d_sf sad sport at fright with dissolve:
        xzoom -1.0
    me "Мику, но я же, вроде как, уже не…"
    show mi scared pioneer close
    show dv angry pioneer2 far:
        xcenter 0.55
    with dissolve_fast
    dv "Что ты?"
    show d_sf serious sport
    show 3500_dv dontlike pioneer2 as dv:
        zoom 0.75 xoffset 20
    with dissolve_fast
    dv "Сенька, ты все равно свой.{w} Пока хоть один из нас здесь присутствует, ты свой!"
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
    me "Ну хорошо, опять все свалилось на бедного меня."
    show d_sf normal sport
    hide mi smile pioneer close
    with dissolve
    "Семен отхлебнул чай."
    me "Начинаю опрос."
    show d_sf smile sport with dspr
    show sl happy pioneer close at left:
        alpha 0
        pause 0.5
        linear 1 alpha 1
    me "Ляксандра?{w=0.8} Есть что сказать?"
    "Все заулыбались, вспомнив Сашкино прозвище."
    show sl shy pioneer close with dspr
    "Саша покачала головой, благодарно улыбаясь Семену."
    hide sl with dissolve
    "Что там было в памяти у этой девушки, появившейся на свет, в результате сбоя, вместо здешней Слави, знали только система и она сама."
    stop ambience fadeout 1
    show black with dissolve
    hide d_sf
    
    pause 0.5

    play ambience ambience_int_cabin_day fadein 1
    hide black with dissolve
    "Все, как и обещала Сашка, проголосовали за."
    show el grin pioneer at left with dissolve
    "Сыроежкин только попытался затащить Максима в кружок кибернетики"
    show d_ma surprise pioneer with dissolve:
        zoom 0.75 xcenter 0.55 yalign 1.01
    show d_mz facepalm glasses pioneer with dissolve:
        xcenter 0.14
    extend ", но был остановлен, к  удивлению большинства присутствующих, самим Шуриком:"
    show 3500_sh normal2 noglasses pioneer glasses at fright with dissolve:
        ycenter 0.856
    sh "Сергей, мы здесь не за этим собрались, ты не находишь?"
    show el normal pioneer
    show d_mz smile2 glasses pioneer
    show d_ma normal pioneer
    with dissolve_fast
    extend " И еще, зачем нам участник, которого пришлось уговаривать?"
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
    "И пионер хотел сказать, что согласен, но вдруг прервал себя, еще не издав ни звука."
    stop ambience fadeout 1
    
    play music "<from 32.5 loop 0.0>sound/music/farewell_to_the_past.ogg" fadein 1.5
    show black behind d_ma with squares
    "Вспомнились вдруг вчерашние слова Лены, в пересказе Саши, и сегодняшние — Алисы: «Ты думаешь, что в старшем отряде вся жизнь повидлом намазана? Ну-ну»."
    show d_ma normal pioneer with dissolve_fast
    "Что-то Алиса хотела до него донести, сегодня, пока вместе наводили порядок на складе, о чем-то предупредить."
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
    sa "Может дать ему время подумать?"
    show 3500_sh normal2 noglasses pioneer glasses at fright with dissolve:
        ycenter 0.856
    show sl surprise pioneer close:
        pause 1.2
        linear 1 alpha 0
    sh "Нет.{w=0.6} Решать он должен сейчас.{w=1.0} Пока мы все здесь рядом."
    show 3500_sh angry_serious noglasses pioneer glasses
    show d_ma surprise pioneer
    with dissolve_fast
    sh "Мы сейчас в роли экрана, понимаете?{w} И то, что он сейчас решит, это решит он сам, а не…"
    show 3500_sh normal noglasses pioneer glasses with dissolve_fast
    "Шурик споткнулся на полуслове, и только ткнул рукой с зажатыми в них очками, куда-то вниз, себе под ноги."
    sh "Одним словом, Максим, посмотри на нас и скажи, хочешь ли ты перейти в наш отряд?"
    hide sl
    hide 3500_sh with dissolve
    stop ambience fadeout 3
    
    $ renpy.music.set_volume(1.0, delay=3)
    "Впервые у пионера из среднего отряда спрашивали его желание."
    show d_ma normal pioneer with dissolve_fast
    window show
    "Максим оглядел собравшихся."
    show sl smile2 pioneer close with dissolve:
        xcenter 0.1
    "Сашка, улыбается радостно и чуть кивает головой, она-то в ответе не сомневается и только ждет подтверждения."
    hide sl
    show 3500_sh normal2 noglasses pioneer glasses behind d_ma:
        zoom 0.75 xcenter 0.71
    with dissolve
    "Шурик, сидит и протирает очки с отсутствующим видом, мыслями у себя в кружке.{w} Но те два замечания, что он подал, говорят о его внимании к происходящему."
    hide 3500_sh
    show un serious pioneer far behind d_ma:
        xcenter 0.37
    with dissolve
    "Лена, подняла ресницы, кажется изучила всего, пока Макс барахтался в ее зеленых глазищах, и отпустила. Сделав какие-то свои выводы."
    hide un
    show mi cry_smile pioneer close:
        xcenter 0.9
    with dissolve
    "Мику, копирует Сашку, только улыбается чуть печально. Будто провожает во взрослую жизнь, которая будет далеко не мёдом."
    hide mi
    show el smile pioneer:
        xcenter 0.22
    show mz shy glasses pioneer:
        xcenter 0.15
    with dissolve
    "Сыроежкин и Женя, так и сидят не отпуская рук, им, кажется, нет особого дела до Максима, они заняты сами собой"
    show mz smile glasses pioneer with dspr
    pause 0.1
    show d_mz excitement pioneer as mz with dissolve_fast
    extend ", но вот Женя бросила на Максима быстрый взгляд, сняла свои круглые очки, и чуть улыбнулась."
    "И оказалось, что зря он ее побаивался, что это она сама всех боится, но готова подпустить Максима чуть поближе, переведя в круг доверенных лиц.{w} Чего ей бояться, когда Сергей рядом?"
    hide el
    hide mz
    show dv grin pioneer2 far behind d_ma:
        xcenter 0.6
    with dissolve
    "Алиса, смотрит насмешливо, но и с надеждой, почему-то."
    hide dv
    show d_sf normal sport:
        xzoom -1.0 xcenter 0.88
    with dissolve
    "Семен...{w} По лицу Семена ничего не разобрать.{w} Вообще, непонятно, в каком он тут качестве, но что-то связывает его с отрядом, почему-то Алиса сказала про то, что он свой здесь и остальные приняли это как должное."
    hide d_sf
    show d_us serious sport:
        xcenter 0.77 ypos -0.05
    
    with dissolve
    "Ульяна, очень серьезно ждет ответа. И тоже смотрит оценивающе и почему-то чуть-чуть ревниво."
    hide d_us with dissolve
    show d_ma grin2 pioneer with dissolve_fast
    th "Да что я маюсь? Не смогу я теперь в детские игры играть, хватит."
    $ renpy.music.set_volume(0.25, delay=1.0)
    play ambience ambience_int_cabin_day fadein 1
    
    d_ma "Да, я хочу перейти в старший отряд!"
    show d_sf laugh sport with dspr:
        xzoom -1.0 xcenter 0.88
    me "Быть по сему!"
    
    # "Семен на мгновение улыбнулся совершенно по детски, рот до ушей."
    stop ambience fadeout 3
    
    $ renpy.music.set_volume(1.0, delay=3)
    show dv grin pioneer2 far behind d_ma:
        xcenter 0.6 alpha 0
        linear 1 alpha 1
    show un smile pioneer far behind d_ma:
        xcenter 0.37 alpha 0
        linear 1 alpha 1
    show 3500_sh smile noglasses pioneer glasses behind d_ma:
        zoom 0.75 xcenter 0.71 alpha 0
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
       
    
    "Впервые пионер из среднего отряда перешел в старший по собственной воле."
    scene black

    show dct_int_warehouse_day:
        xalign 0.5 yalign 1.2
    with dissolve
    show dct_int_warehouse_day:
        yalign 0.7
        easeout 0.8 yzoom 5.0 yalign 1.5 blur 20 alpha 0
    
    show dct_int_corridor2:
        yzoom 3.0 xalign 0.5 yalign 0.0 blur 20 alpha 0
        pause 0.9
        linear 0.3 yalign 0.5 alpha 0.4
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
    "Глубоко в шахте под поселком Шлюз что-то щелкнуло и погасли лампочки на одном блоке, тут же вспыхнув на другом."
    stop music fadeout 5
    show dct_int_datacenter:
        pause 1
        linear 2.5 alpha 0
        
    $ day_time()                        # Прописано, чтобы при обратной перемотке цвета не сбивались.
    $ persistent.sprite_time = "day"
    "И мир Сети еще чуть изменился." with vpunch
    window auto



    
    stop sound fadeout 2
    stop music
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene black with dissolve2

    $ renpy.pause(3)
    
    $ renpy.sound.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')