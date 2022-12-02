    #########################
    #Глава 10. Снореальность#
    #########################


label dct_dreamreality:
    $ save_name = u"Дубликат. Монетка в фонтане -- Снореальность"
    $ night_time()
    $ persistent.sprite_time = "day"
    scene black
    show headline_text2 u"Глава X. Снореальность" at truecenter with dspr
    $ renpy.pause(3.0)
    hide headline_text2 with dissolve
    
    
    play ambience ambience_int_cabin_night fadein 1.5
    scene bg int_house_of_dv_night with dissolve
    dv "Ну, в последний раз на старом месте. Отвяжись жених от невесты!"
    show 3500_dv smile night2 0pt at center with dissolve_fast:
        ypos -0.15
    "Алиса хмыкнула и, глядя в потолок, произнесла переиначенную бабушкину поговорку."
    th "Что бы еще сказать, соответствующее моменту?"
    show 3500_dv grin night2 0pt with dissolve_fast
    th "Завтра надо будет пнуть Рыжую, пусть забирает остатки своего барахла. А то одно сплошное расстройство."
    show 3500_dv laugh night2 0pt with dissolve_fast
    th "А флаг себе оставлю и на новом месте вывешу."
    th "А если меня Ольга к себе в домик определит? Приедет Второй, спросит где вожатая, а его в домик с пиратским флагом отправят. Пионерский лагерь, ага. Дурдом «Совенок»."
    show 3500_dv guilty night2 0pt with dissolve_fast
    th "Это все Сенька виноват, до него все чинно и благородно было. Может, ночью на флагштоке пиратский флаг поднять?"
    show 3500_dv smile night2 0pt with dissolve_fast
    th "{i}Я подниму черно-белый флаг, закончится этот угар. Я уплыву и это будет знак, того что Земля есть шар.{/i}"
    show 3500_dv sad night2 0pt with dissolve_fast
    th "Только флаг тогда сразу Ольга конфискует, выцарапывай его потом"
    show 3500_dv guilty night2 0pt with dspr
    "Где-то в домике, в какой то щели, надрывался сверчок. Когда он уставал и делал перерыв становилось слышно, как звенит спираль в лампочке."
    "Спать не хотелось, давили какие-то не додуманные мысли, не сказанные слова, не совершенные поступки, которые надо было в своё время додумать, досказать, доделать, а сейчас уже поздно."
    th "Пойти погулять? Или поиграть на эстраде? Тут где-то Сенька с Рыжей шатались, пойти их поискать?"
    show 3500_dv sad night2 0pt with dspr
    th "Я, кажется, наконец-то простила себе тот выстрел из арбалета. Надо будет сказать об этом Семену, это очень важно."
    show 3500_dv normal night2 0pt with dissolve_fast
    th "Но это можно и завтра."
    show 3500_dv grin night2 0pt with dissolve
    th "Пойду поиграю"
    show 3500_dv grin night2 0pt:
        ease 1 xcenter .16
    "Уже было раздевшаяся Алиса достала из сумки черные джинсы и футболку, в которых приехала сюда."
    th "Надену. А то все в форме да в форме"
    show 3500_dv grin casual 1pt with dissolve2
    pause 1
    show 3500_dv guilty casual 1pt with dissolve_fast
    "Подержалась за кожаную куртку, висящую на гвозде."
    th "Откуда она у меня?"
    th "Я помню, что приехала в ней, в первый свой цикл активной фазы, потом, при отъезде, оставила ее здесь и с тех пор она так тут и висит."
    show 3500_dv normal casual 1pt with dissolve_fast
    th "Мужская кожаная куртка с крошками табака в кармане."
    th "Семен ничего не знает, говорит, что для него цикл всегда начинался со второй недели, повариха покойная странно на нее посмотрела, как-будто вспомнила что-то, но промолчала."
    show 3500_dv smile casual 1pt with dspr
    th "Возьму с собой, уже прохладно"
    
    $ renpy.sound.set_volume(0.5)
    play sound sfx_door_squeak_light
    pause 0.4
    play sound2 sfx_knock_door3_dull
    pause 0.5
    stop sound2 fadeout 0.3
    $ renpy.sound.set_volume(1.0)
    "Заскрипело крыльцо и в домик, коротко перед этим стукнув в дверь, заглянула вожатая."
    show 3500_dv normal casual 1pt
    show mt normal pioneer at cright
    with dissolve
    mt "Ты далеко собралась, на ночь глядя?"
    dv "Не дальше ограды, Ольга Дмитриевна."
    show mt sad pioneer with dspr
    "Ольга пошевелила губами, но не стала озвучивать ответ. Только кивнула разрешающе."
    mt "Не гуляй долго. Я все же беспокоюсь о вас, хоть по мне этого и не заметно."
    "Ну и у Алисы тоже не получилось поскандалить."
    show 3500_dv guilty casual 1pt with dissolve_fast
    dv "До отбоя еще полчаса — имею полное право."
    show mt smile pioneer with dspr
    mt "Имеешь, имеешь."
    show 3500_dv normal casual 1pt with dissolve_fast
    show mt smile pioneer:
        pause 2
        linear 1 alpha .0
    "Ольга кивнула еще раз, и прикрыв дверь пошла в сторону поперечной аллеи, чтобы там свернуть в сторону кружка кибернетики, по своему извечному маршруту вечернего обхода."
    "А Алиса стояла и думала, глядя в спину удаляющейся вожатой."
    show 3500_dv guilty casual 1pt with dissolve_fast
    th "Что это с нами?"
    th "Раньше бы уже орали друг на друга, а сейчас спокойно разошлись."
    show 3500_dv shocked casual 1pt with dissolve_fast
    th "Стареем? Если мне сорок пять, то сколько же Ольге?"
    show 3500_dv angry casual 1pt with dissolve_fast
    th "Так, стоп, Алиска! Прекрати маяться дурью — тебе семнадцать! Сем-над-цать! Правильно тебя Улька ругает!"
    show 3500_dv normal casual 1pt with dissolve_fast
    "Алиса закинула как мешок на плечо куртку."
    show 3500_dv normal casual 1pt coat guitar carried with dissolve_fast
    show d_int_house_of_dv_night_without_light:
        alpha .0
        pause 2
        linear 1 alpha 1.0
        
    $ persistent.sprite_time = "day"    # Прописано, чтобы при обратной перемотке цвета не сбивались.
    "Чтобы куртка не сваливалась с плеча подперла ее гитарой, и вышла, закрыв дверь не запирая."
    
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_house_of_dv_night
    show 3500_dv normal casual 1pt coat guitar carried at cright:
        zoom .75
    with dissolve
    th "Все-таки в удивительном мире мы живем. Никому просто не приходит в голову, что нужно запирать за собой домик, когда уходишь."
    show 3500_dv normal casual 1pt coat guitar carried at cright:
        easeout 1.3 xcenter 1.25
    "И пошла на эстраду, принимать своё обычное снотворное, кивнув по пути только что пришедшей на площадь Лене."
    window hide
    stop ambience fadeout 1
    show black with dissolve
    play ambience ambience_camp_center_night fadein 1
    hide black with dissolve
    window auto
    show d_us normal sport_windbreaker:
        zoom .75 xcenter 1.2
        easein 2  xcenter .62
    "Через десять минут после ее ухода, в домик к Алисе заглянула Ульяна."
    hide d_us with dissolve
    "Обнаружила отсутствие гитары, все поняла, но, чтобы не разминуться, не пошла на эстраду, а завалилась подремать поджидая, и так и уснула."

    
    stop ambience fadeout 1
    scene black with dissolve
    $ renpy.music.set_volume(0.6, delay=1.5, channel='ambience')
    play ambience ambience_camp_center_night fadein 1
    $ renpy.music.set_volume(0.3)
    play music Everlasting_Summer_guitar_cover fadein 1.5
    scene bg ext_stage_big_night
    show 3500_dv blink casual 1pt guitar playing:
        zoom .15 anchor (0.5, 1.0) pos (0.45, 0.75)
    with fade
    pause .2
    show dct_ext_stage_big_night_sl_sitting
    show d_ma sit_back:
        zoom .24 anchor (0.5, 0.98) pos (0.39, 0.96)
    with dissolve
    "Пять минут спустя, после прихода Алисы, на концертной площадке, на заднем ряду лавок устроились Максим и Саша."
    window hide
    show mz normal pioneer:
        anchor (0.65, 0.53) pos (1.39, 0.58)
        easein 1.5 pos (0.89, 0.58)
    show el serious pioneer:
        xcenter 1.15 ycenter 0.55
        easein 1.5 xcenter 0.65
    pause 1.5
    show el surprise pioneer with dissolve_fast
    window show
    "И почти сразу туда же сунулись Женя с Сыроежкиным."
    window hide
    show el shocked pioneer:
        easeout 0.9 xcenter 1.15
    pause 0.45
    show mz laugh pioneer:
        pause 0.2
        rotate 0.0 pos (0.89, 0.58) transform_anchor True   # Если нужно повернуть изображение не вокруг центра, а вокруг другой, произвольной точки, то обязательно надо включать transform_anchor True
        linear 0.11 rotate 6.55 pos (0.95, 0.6) transform_anchor True
        linear 0.07 rotate 6.55 pos (1.01, 0.6) transform_anchor True
        linear 0.21 rotate 0.0 pos (1.17, 0.58) transform_anchor True
        linear 0.2 xpos 1.4 transform_anchor True
    pause 0.8
    window auto
    "Но, увидев Алису, развернулись и ушли."
    "Алисе было все равно — Алиса играла."
    d_ma "Я и не думал, что на простой гитаре возможно такое."
    "Максим говорил почти шопотом, и Саша отвечала ему столь же тихо."
    sa "Это же Алиса, в чем-то она даже лучше Мику."
    sa "Мы, во второй день по приезду, у Мику в кружке собирались, и я слышала, как они дуэтом играют. Даже ради одного этого стоило в лагерь приехать."
    "Саша помолчала, а потом попрощалась с Максимом."
    sa "Я, пожалуй, пойду к себе — потанцевать хотела, но видно сегодня не судьба."
    sa "Нет, не провожай меня. Лучше подойди к Алисе, когда она в домик засобирается, только не восхищайся слишком активно. А то она засмущается и начнет ругаться."
    hide dct_ext_stage_big_night_sl_sitting with dissolve
    "Саша ушла, а Максим остался"
    window show
    show d_ma sit_back with dissolve_fast:
        zoom .22 anchor (0.5, 0.98) pos (0.37, 0.92)
    extend ", постепенно перебираясь с заднего ряда все ближе и ближе к эстраде"
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
    # extend ", прямо напротив Алисы, сидевшей свесив ноги на краю сцены."    # По канону  
    extend ", прямо напротив Алисы, балансировавшей на самом краю сцены."
    window auto
    show 3500_dv normal casual 1pt guitar playing with dspr
    pause 0.8
    show 3500_dv blink casual 1pt guitar playing with dspr
    "А Алиса только мельком глянула на Максима, как бы отметив: «Ты здесь». И опять ушла в музыку."
    "«Музыка это ритмически и мелодически организованные звуки», — вспомнилось сухое определение."
    "Так оно и было, сперва. Были просто красивые звуки."
    "Потом за звуками горнист услышал эмоции, потом… Потом показалось, что за эмоциями следом идет еще и мысль, или даже Мысль."
    stop music fadeout 5
    show 3500_dv blink casual 1pt guitar playing:
        ease 6 alpha 0
    show 3500_dv normal casual 1pt guitar standing as dv2:
        zoom .27 anchor (0.5, 1.0) pos (0.28, 0.67) alpha 0
        ease 6 alpha 1
    show ext_stage_normal_night:
        linear 40 alpha 0
    d_ma "\~ Понять бы её. Ведь вот она Алиса настоящая. Поймешь мысль — поймешь и то, над чем Алиса сейчас бьется, и саму Алису. \~"
    "А потом Максим обнаружил что музыка кончилась."
    # "Что Алиса сидит на краю эстрады отложив гитару и молча смотрит на него."   # По канону
    "Что Алиса отставив гитару будто приросла к сцене и молча смотрит на него. Что глаза ее, в свете единственной сорокаваттной лампочки, спрятавшейся высоко под куполом, кажутся бездонными и темными-темными."
    "Мальчик и девочка смотрели друг-другу в глаза и молчали."
    d_ma "\~ Сейчас она опять начнет издеваться \~"
    "Максим, поёжился то ли от прохлады, заползающей под рубашку, то ли от внимательного и серьезного взгляда Алисы."
    d_ma "\~ Что меня тянет к тебе? Злая и насмешливая помощница вожатой, которая почти на три года старше меня. \~"
    d_ma "\~ Есть же Катька, я уже понял, что Катька в меня влюбилась. Есть же Саша и Мику, в конце-концов, если уж мне так нравятся девушки постарше. \~"
    d_ma "\~ А я трачу время и силы, в надежде понравиться тебе. \~"
    $ renpy.music.set_volume(1.0)
    show black with dissolve_fast:
        alpha 0.6
    hide black with dissolve_fast
    "Лампочка под куполом мигнула. Вдруг показалось, что кроме этой эстрады ничего больше в мире не существует, что весь мир сжался до янтарно-желтого шара, в который заключена эстрада и два человека на ней."
    d_ma "\~ Как там Алиса сказала? «Вспомни свой домашний адрес», — а я не помню! Как я могу его вспомнить если его не существует, если существуют только Алиса и ее глаза? \~"
    d_ma "\~ Вот был целый мир, а лампочка мигнула, и раз и нет мира, остался только лагерь внутри желтого шара, а прочий мир перестал существовать. \~"
    stop ambience fadeout 1
    show black with dissolve_fast:
        alpha 0.6
    hide black with dissolve_fast
    d_ma "\~ А потом лампочка мигнула еще раз, и этот шар сжался вокруг эстрады, оставив все прочее снаружи, и внутри остались только мы двое: пионерка с гитарой и глупый пионер с горном, которого держат в плену эти глаза. \~"
    d_ma "\~ А потом лампочка мигнет в третий раз, шар сожмется еще и останется только Алиса, а все прочее исчезнет. \~"
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
    d_ma "\~ Может я уже исчез? Может меня уже не существует, как и всего мира?» \~"
    hide d_ma
    show dct_ext_stage_close_night_darker behind black:
        blur 20
    hide black with dissolve2
    "Показалось, что ровный горизонтальный край сцены начал терять четкость очертаний и размываться."
    "Страшно не было."
    d_ma "\~ Вот и всё. Я исчез не успев даже влюбиться в тебя. \~"
    play ambience ambience_camp_center_night fadein 2
    show dct_ext_stage_close_night_darker:
        linear 2 blur 0
    dv "Заигралась я."
    "Слова Алисы смыли навождение."
    dv "Вон, уже и фонари погасили."
    show 3500_dv smile casual 1pt guitar standing with dspr
    dv "Раз уж ты здесь, кавалер, пойдем, проводишь меня."
    "И правда, обычно на концертную площадку попадал свет от фонарей, освещавших аллею. Но не сейчас, сейчас светила только тусклая лампочка под самым куполом."
    th "Значит уже больше двенадцати."
    hide d_ma with dissolve
    show d_ma normal pioneer with dissolve:
        zoom .43 anchor (0.5, 0.99)  pos (0.5, 1.0)
    d_ma "Пойдем."
    "Максим протянул руку Алисе, помогая той спрыгнуть с эстрады."
    scene dct_ext_stage_close_night_darker
    show d_ma normal pioneer:
        zoom .43 anchor (0.5, 0.99)  pos (0.5, 1.0)
    show 3500_dv surprise casual 1pt guitar carried:
        zoom .43 xcenter .4 ycenter .85
    with wipedown
    dv "Ты ледяной как мертвец!"
    show 3500_dv grin casual 1pt guitar carried with dissolve_fast
    dv "Я думала — примерзну к твоей руке."
    "K Алисе вернулась привычная манера."
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast
    dv "Держи."
    show d_ma surprise pioneer coat with dissolve_fast
    "Откуда-то появилось кожаная куртка, неожиданно заботливо накинутая на плечи Максиму."
    show d_ma serious pioneer coat with dspr
    "Тот дернул было плечами, но Алиса удержала куртку."
    show 3500_dv laugh casual 1pt guitar carried with dspr
    show d_ma shy pioneer coat with dspr
    dv "Держи, держи. А когда я начну мерзнуть — вернешь."
    
    
    play music music_list['no_tresspassing'] fadein 3
    scene bg ext_library_night
    show d_ma normal pioneer coat at center:
        yalign 0.02
    show 3500_dv normal casual 1pt guitar carried at right:
        xcenter 0.75 ycenter 0.83
    with dissolve
    "Фонари, оказывается, светили. Но у них едва получалось осветить пятачок земли вокруг столба."
    "Светили и лампочки в окнах домиков, тех — в которых еще не спали. Но казалось, что до них так же далеко, как до звезд."
    show 3500_dv smile casual 1pt guitar carried with dspr
    dv "Тьма окутала маленький лагерь."
    "Слегка нараспев произнесла Алиса."
    show 3500_dv normal casual 1pt guitar carried with dspr
    dv "Скажи, кавалер, ты знаешь, что такое гомеостаз?"
    show d_ma grin2 pioneer coat with dspr
    d_ma "Ну да, я же, говорят, умный и начитанный мальчик.{w=0.3} Гомеостаз, это равновесие, если одним словом."
    show 3500_dv laugh casual 1pt guitar carried with dspr
    dv "Начитанный, умный. Еще и отличник поди?"
    show d_ma grin pioneer coat with dspr
    d_ma "Нет — троечник с плюсом. Я же ленивый. И есть более приятные и полезные вещи, чем школьная учеба."
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
    dv "А я вот — дура. Я, когда слово «гомеостаз» услышала, полчаса смеялась. Думала, что это что-то про отношения между двумя мужчинами."
    show 3500_dv smile casual 1pt guitar carried with dspr
    show d_ma smile2 pioneer coat with dspr
    dv "Так вот, такие как я, говорят, этот самый гомеостаз нарушают, и Лагерь пытается от них избавиться."
    show 3500_dv normal casual 1pt guitar carried with dspr
    show d_ma normal pioneer coat with dspr
    dv "Это мне Рыжая сказала и Сенька подтвердил. А они знают о чем речь, они сами такие же нарушители гомеостаза, как и я."
    dv "И еще больше, чем я. Так что это я такая же, как они."
    
    
    scene dct_ext_square_profile_view_night_darker
    show dct_ext_square_profile_view_night_darkest:
        alpha 0.0
    show 3500_dv grin casual 1pt guitar carried:
        xcenter 0.32 ycenter 0.83
    show d_ma normal pioneer coat:
        xcenter 0.61 yalign 0.02
    with dissolve
    dv "И вот, кажется что-то происходит."
    show dct_ext_square_profile_view_night_darkest:
        pause 1
        linear 3 alpha 0.2
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast:
        xcenter 0.37
    "Алиса как будто размышляла вслух, не особо интересуясь присутствием Максима, но потом протянула ладонь и сама взяла Максима за руку."
    show 3500_dv normal casual 1pt guitar carried with dissolve_fast:
        xcenter 0.42
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 0.4
    "И тот поняв, что девушке не по себе, что она нервничает, слегка сжал руку Алисы: «Я здесь, я с тобой, не бойся»."
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 0.6
    "Они уже подошли к самому сердцу лагеря, к площади утыканной фонарями, но вокруг становилось все темнее и темнее."
    show dct_ext_square_profile_view_night_darkest:
        linear 1 alpha 0.7
    d_ma "\~ Как в чернильнице \~"
    show dct_ext_square_profile_view_night_darkest:
        linear 1.5 alpha 0.8
    "И неожиданный холод пробирал до костей."
    show dct_ext_square_profile_view_night_darkest:
        linear 3 alpha 1.0
    "А когда стало совсем невыносимо холодно, Максим услышал как Алиса пробурчала:"
    dv "И надо только решиться шагнуть с шара на шар."
    window hide
    stop ambience fadeout 1
    play music music_list['sparkles'] fadein 1 # Момент перехода с шара на шар
    #play sound sfx_tree_branches #Шелест листьев
    scene dct_ball_to_ball_1
    show dct_ball_to_ball_dv_ma
    with pixellate
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
    play ambience ambience_camp_center_night fadein 2
    scene dct_ext_square_profile_view_night
    show 3500_dv normal casual 1pt guitar carried:
        xcenter 0.42 ycenter 0.83
    show d_ma normal pioneer coat:
        xcenter 0.61 yalign 0.02
    with pixellate
    window show
    "И сразу же стало светло, как и должно быть при таком количестве фонарей"
    show d_ma normal pioneer coat carried with dissolve_fast
    extend ", и сразу же стало тепло, как и должно быть в середине лета"
    $ renpy.music.set_volume(0.3, delay=0, channel='sound_loop')
    play sound_loop sfx_broom_sweep fadein 2
    extend ", и сразу же стало слышно, как кто-то подметает площадь."
    show 3500_dv shocked casual 1pt guitar carried
    show d_ma surprise pioneer coat carried
    with dissolve_fast
    "Два вопроса прозвучали одновременно."
    show 3500_dv shocked casual 1pt guitar carried:
        easeout 1.5 xcenter -0.3
    show d_ma surprise pioneer coat carried:
        easeout 1.5 xcenter -0.11
    d_ma_dv "Саша? Что ты здесь делаешь?\nСлавя...на?"
    stop sound_loop fadeout 2
    "А знакомая и в то же время незнакомая девушка подняла глаза, улыбнулась, сначала растерянно, а потом понимающе, и неожиданно звонко произнесла:"
    slp "Я — Славя!"
    window hide
    $ renpy.music.set_volume(1.0, delay=0, channel='sound_loop')
    stop ambience fadeout 1.5
    
    
    scene black with dissolve
    $ set_mode_nvl()
    play music music_list['waltz_of_doubts'] fadein 3  #Славя подметает площадь
    show anim prolog_1 with dissolve2
    window show
    th "Объясните мне, зачем я подметаю площадь каждый вечер? Я могла бы этого не делать, но я это делаю."
    hide anim prolog_1
    show dct_sl_clean_square_1
    with dissolve
    extend " Программа, заложенная в меня как в обитателя лагеря, виновата?"
    show anim prolog_1
    hide dct_sl_clean_square_1
    with dissolve
    extend " Нет конечно, я просто делаю это, потому что мне приятно видеть чистый лагерь. Потому что это мой дом. Теперь уже точно — дом."
    hide anim prolog_1
    show arseniy_chebynkin_izbad
    show d_sl_casual at left
    show black as black2:
        alpha 0.3
    with dissolve
    extend " Очень жаль что большая семья с кучей братьев и большой дом, и мама с папой, это все сон. А может и не сон, ведь если есть мои двойники в других лагерях, то может быть где-то живет и настоящая девочка Славя, у которой есть мама с папой и свой дом."
    show anim prolog_1
    hide arseniy_chebynkin_izbad
    hide d_sl_casual
    hide black2
    with dissolve
    extend " Она настоящая, а я? Я ведь тоже настоящая, только в непонятном месте."
    
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    
    th "Плохо только то, что по настоящему мало с кем можно поговорить."
    show anim prolog_1:
        linear 1 alpha 0
    show dct_sl_clean_square_2:
        alpha 0 yalign 1.0
        easein 2.5 yalign 0.5 alpha 1
    pause 1
    extend " Я была чудовищно одинока до того как проснулась и спасалась в общественной активности от одиночества, и отгораживалась от людей активностью же."
    show anim prolog_1:
        pause 1
        linear 1 alpha 1
    show dct_sl_clean_square_2:
        easeout 2.5 yalign 0.0 alpha 0
    pause 1
    extend " Но и сейчас стало не намного лучше. Эйфория первой недели прошла, и вот накатило."
    hide anim prolog_1
    show dct_sl_clean_square_3
    with dissolve
    extend " Здесь чудесные люди: мальчики и девочки, но я уже знаю все что они могут сказать."
    show anim prolog_1
    hide dct_sl_clean_square_3
    with dissolve
    extend " Нет, есть еще Алиса, Ульяна и Мику, но мы никогда не были особо близки, пока спали, и странно было бы если бы мы сблизились сейчас. Характеры, их не изменишь."
    hide anim prolog_1
    show dct_sl_clean_square_4
    with dissolve
    extend " А малыши, те что не спят, они все равно малыши, с ними интересно и забавно, но как поговорить с ними откровенно? Они просто не поймут. Бедный-бедный Семен, как он с этим со всем справлялся в одиночку?"
    show anim prolog_1
    hide dct_sl_clean_square_4
    with dissolve
    extend " Хорошо что они есть на свете, те жители другого лагеря, которые тоже не спят, хорошо, что они помнят о нас. Иначе, просто опустились бы от растерянности руки."
    
    nvl hide dissolve
    nvl clear
    nvl show dissolve
    
    th "А есть еще, как ее Ульяна-большая назвала, чужая память. Сейчас я уже понимаю, что большая часть этой памяти, это воспоминания того моего двойника — Славяны, из-за которой я обрезала косы."
    hide anim prolog_1
    show dct_dsl_in_shop
    with dissolve
    extend " И так хочется иногда, в минуту слабости, махнуть рукой и дать ей жизнь. Наверное это получится, если очень захотеть. Просто ляжет спать Славя, а проснется Славяна. Почти никто подмены и не заметит."
    show anim prolog_1
    hide dct_dsl_in_shop
    with dissolve
    extend " Но она не хочет, я не знаю, как, но я чувствую, что она этого не хочет. Да и я сама не хочу, потому что я — Славя! Такая какая есть, та помощница вожатой, которая провожала нашего Семена, стоя на берегу."
    
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
    
    extend " А чтобы никто не увидел, как она плачет, прижимала бинокль к глазам. Наверное я тогда была влюблена в него, не знаю, не помню. Или мне было очень жалко, что он убегает от нас? Может быть я думала, что мы его чем-то обидели?"

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
    
    extend " Не помню, столько времени прошло, и я спала тогда. Только и помню, что само бегство Семена: от момента, когда, возвращаясь с пробежки, встретила запыхавшуюся Женю, стучащую кулачками в дверь к Ольге Дмитриевне, и до того, как понурая, как-будто лишившаяся внутреннего стержня, вожатая даже не скомандовала, а тихо попросила: «Давайте не будем говорить об этом»."
    
    hide 3500_sl
    hide 3500_mt
    
    show dct_bank_from_water_side_zoom:
        pause 0.7
        ease 3 xalign 0.0
    show 3500_sl scared sport binoculars as sl2:
        linear 0.7 alpha 0
    show 3500_sl sad sport binoculars:
        zoom 0.75 xcenter 0.65 ypos 0.15 alpha 0
        linear 0.7 alpha 1
        ease 3 xcenter 1.65
    show 3500_mt rage pioneer panama megaphone as mt2:
        linear 0.7 alpha 0
    show 3500_mt scared pioneer panama megaphone:
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
    
    th "Так вот, это именно я, и я на своем месте."
    show anim prolog_1:
        linear 1 alpha 0
    show dct_sl_clean_square_5:
        alpha 0 yalign 0.0
        easein 2.5 yalign 0.5 alpha 1
    pause 1
    extend " Я уверена, что и Славяна это понимает и сейчас согласна со мной. Значит буду просто жить, здесь, у себя дома — в лагере «Совенок»."
    show anim prolog_1:
        pause 1
        linear 1 alpha 1
    show dct_sl_clean_square_5:
        easeout 2.5 yalign 1.0 alpha 0
    pause 1
    extend " Делать добро из зла, потому что ничего больше под руками у меня нет. Делать лагерь лучше, помогать другим его обитателям осознать себя, делать так, чтобы когда они проснутся, они проснулись в самом лучшем лагере."
    hide anim prolog_1
    show dct_sl_clean_square_6:
        alpha 0.6
    with dissolve
    extend " А еще, это мой дом и мне уплывать отсюда некуда. А когда решу что хватит, тогда и буду дальше думать."
    show dct_sl_clean_square_6 with dissolve_fast:
        alpha 1.0
    extend " А что там решат для себя другие мальчики и девочки, это им решать. Я…"
    show dct_sl_clean_square_7:
        alpha 0
        linear 1.5 alpha 1
    
    nvl hide dissolve
    pause 0.5
    window hide
    pause 0.5
    
    
    $ set_mode_adv()
    window auto
    stop music fadeout 4
    play ambience ambience_camp_center_night fadein 4
    play sound_loop sfx_broom_sweep fadein 4
    th "Кто-то идет на площадь. Двое, что за парочка? Отбой ведь уже был, придется воспитывать влюбленных."
    scene dct_ext_square_night_crop
    show 3500_dv grin casual 1pt guitar carried at cleft:
        zoom 1.25 yalign 0.15
    show d_ma normal pioneer coat carried at right:
        zoom 1.25 yalign 0.08
    with fade
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
    #scene bg ext_square_night
    show d_sl surprise pioneer broom:
        zoom 0.75 xcenter 0.37 yalign 0.0
    show 3500_dv normal casual 1pt guitar carried at fleft:
        zoom 1.0 ycenter 0.83
    show d_ma normal pioneer coat carried at cright:
        zoom 1.0 yalign 0.02
    with dissolve
    th "Но ведь им же нельзя здесь находиться, это Семен очень ясно дал понять. Или можно?"
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
    stop ambience fadeout 1.5
    play music my_2nd_summer fadein 1.5
    dv "Ну здравствуй, сестренка."
    
    
    show black with dissolve
    hide d_ma
    show d_ma serious pioneer coat carried guitar standing at center with dissolve:
        yalign 0.86
    "Потом, в следующие циклы, в этот день Максиму всегда снился один и тот же сон."
    hide d_ma with dissolve
    scene dct_ext_square_night_purple:
        xzoom 1.1 yzoom 1.16 xcenter 0.535 ycenter 0.552 rotate 1.24 blur 10
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.6 xcenter 0.84 ycenter 0.7
    show 3500_dv normal casual 1pt at fleft:
        ycenter 0.83
    show d_sl smile2 pioneer broom close at center#:
    show black:
        alpha 0.65
    with dissolve
    "Как будто он стоит на краю площади, а посередине, напротив памятника, три фигуры:"
    show black behind d_sl with dissolve
    extend " первая, которую он сначала принимает за Сашу, но это не Саша, это какая-то другая девушка, очень похожая, но не она."
    th "Славная девушка"
    show d_sl smile2 pioneer broom close:
        linear 1.3 alpha 0
    #pause .5
    show black behind dv2 with Dissolve(1.8)
    "А потом уже смотрит только на двух других участников сна, на двух Алис."
    show black:
        linear 20 alpha 0
    "Они стоят, зеркальные отражения одна другой, и жадно разглядывают друг-друга, а всей разницы между ними, что одна вся в черном, а другая в обычной пионерской форме, с хулигански повязанным на запястье красным галстуком."
    "Губы их шевелятся, но слов с того места, где стоит Максим, не слышно."
    show 3500_dv normal casual 1pt at fleft:
        zoom 0.91 xcenter 0.32 ycenter 0.8
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.66 xcenter 0.74 ycenter 0.72
    with Dissolve(1.5)
    "Потом обе Алисы одновременно, как по команде начинают медленно сходиться."
    show 3500_dv normal casual 1pt at fleft:
        zoom 0.825 xcenter 0.46 ycenter 0.78
    show 3500_dv grin pioneer3 as dv2:
        zoom 0.72 xcenter 0.64 ycenter 0.74
    with Dissolve(1.5)
    th "Как на дуэли"
    
    scene dct_ext_square_night_purple_blur_HD
    show dct_dv_two_pieces_pioneer:
        anchor(0.5,0.7) pos(0.65,0.8) rotate 2.3 transform_anchor True
    show dct_dv_two_pieces_casual:
        anchor(0.5,0.7) pos(0.35,0.8) rotate -2.3 transform_anchor True
    with fade
    "Когда девушки оказываются на расстоянии шага друг от друга они останавливаются, поднимают руки: та что в черном, та что привела его сюда — правую, а ее отражение — левую и начинают тянуться друг к другу."
    show dct_dv_two_pieces_pioneer:
        ease 2 pos(0.61,0.8)
    show dct_dv_two_pieces_casual:
        ease 2 pos(0.39,0.8)
        
    $ renpy.pause(0.2,hard=True)
    "И вот, когда между кончиками их пальцев остаются считанные сантиметры, обе Алисы оглядываются на Максима, местная Алиса что-то говорит, а та что привела Максима на площадь, ловит его взгляд, и как-будто просит разрешения."
    "Что Максиму остается? Он машет рукой, это разрешение давая."
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
    "И, в момент касания рук все вокруг накрывает тьма, и Максим просыпается."
    
    $ renpy.pause(0.5,hard=True)
    $ renpy.music.set_volume(0.3, delay=3.0)
    "А перед самым пробуждением, уже в полусне, он видит лицо той, второй Алисы, думает во сне-же, что эти Алисы, они все-таки разные, и слышит голос:"
    show dct_dv_argue with flash
    dv "Смотри, горнист. Обидишь сестренку — найду и оторву башку!"
    show dct_dv_argue sternsmile with dspr
    "Но Максим уже понимает язык Алисы, и понимает, что пусть звучит это как угроза, но еще это пожелание удачи или даже счастья."
    hide dct_dv_argue with dissolve2
    stop music fadeout 2.5
    stop sound
    stop sound2
    "«Рыж-ж-жевская!» — С оттяжкой произносит вслух Максим и просыпается окончательно."
    
    play ambience ambience_camp_center_night fadein 1.5
    dv "Что ты сейчас сказал? Повторить не боишься?"
    scene dct_ext_stage_close_night behind blink
    show 3500_dv angry casual 1pt behind blink:
        zoom 0.75 xcenter 0.4 yalign 0.0
    show unblink
    "Максим вздрогнул и открыл глаза. Прямо над ним, абсолютно готовая к рукоприкладству, нависала Алиса.{w} Злая Алиса."
    "Она протянула левую руку к галстуку Максима, а правую уже занесла, для сокрушительного щелбана."
    "Но Максим откуда-то знал правильный ответ."
    d_ma "Рыжевская, скажи. Вы успели коснуться друг-друга? Там, на площади?"
    show 3500_dv smile casual 1pt with dissolve_fast:
        xcenter 0.42
    "И случилось чудо: пальцы правой руки страшной ДваЧе распрямились, кисть развернулась в расслабленную пятерню, и пятерня эта погрузилась в шевелюру Максима, ласково потрепав."
    dv "Много будешь знать, Макс, скоро состаришься."
    show 3500_dv laugh casual 1pt with dspr
    dv "Вот, примерно, как я. Я тут играю, стараюсь, можно сказать для единственного слушателя. А единственный слушатель взял и заснул, прямо на концерте."
    show 3500_dv normal casual 1pt with dspr
    dv "Что там тебе снилось, я не знаю. И, ты как хочешь, а я всё — в домик и спать."
    scene bg ext_square_night
    show 3500_dv smile casual 1pt guitar carried at center:
        ycenter 0.83
    show d_ma smile2 pioneer coat carried at right:
        yalign 0.02
    with fade
    "И фонари светили нормально, и холода не было, и куртку Алиса сунула Максиму со словами:"
    dv "На, тащи, хоть какая то от тебя польза будет."
    show un normal pioneer far at fleft with dissolve
    "На площади, как обычно в это время, сидела Лена, молча кивнувшая им обоим."
    show un smile pioneer far with dspr
    "А горнист все думал:"
    hide un
    show d_ma normal pioneer coat carried
    with dissolve
    d_ma "\~ А ведь она впервые назвала меня Максом. \~"
    scene bg ext_house_of_dv_night
    show 3500_dv normal casual 1pt guitar carried at center:
        ycenter 0.83
    show d_ma normal pioneer coat carried at right:
        yalign 0.02
    with fade
    d_ma "\~ Не Максимом, племянником, кавалером или горнистом, а Максом. \~"
    show black:
        alpha 0
        linear 1 alpha 1
    stop ambience fadeout 3
    
    $ night_time()
    $ persistent.sprite_time = "night"          # Прописано, чтобы при обратной перемотке цвета не сбивались.
    d_ma "\~ Это должно что-то значить? \~"
    scene black with dspr
    
    
    $ renpy.pause(3)
    
    $ renpy.music.set_volume(1.0, delay=0)
    $ renpy.music.set_volume(1.0, delay=0, channel='ambience')

