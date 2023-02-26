init 1:


    $ style.dct_titles_button = Style(style.default)
    $ style.dct_titles_button.font  = "mods/dublicate/fonts/bezpr.ttf"
    $ style.dct_titles_button.color = "#ffda7d"
    $ style.dct_titles_button.size = 50
    $ style.dct_titles_button.kerning = 0.3
    $ style.dct_titles_button.outlines = [(2, '#000', 0, 0)]
    
    
        ###  С гиперссылками ничего не выходит
    
    $ style.dct_hyperlink_button = Style(style.dct_titles_button)
    $ style.dct_hyperlink_button.font  = "mods/primerchik_navskidku_4/OpenSans-Bold.ttf"
    $ style.dct_hyperlink_button.size = 30
    $ style.dct_hyperlink_button.color = "#54afff"
    $ style.dct_hyperlink_button.hover_color = "#abd8ff"
    $ style.dct_hyperlink_button.underline = True
    $ style.dct_hyperlink_button.outlines = [(2, '#000', 0, 0)]
    
    
    # $ style.dct_hyperlink = Style(style.dct_titles_button)
    # $ style.dct_hyperlink.font  = "mods/primerchik_navskidku_4/OpenSans-Bold.ttf"
    # $ style.dct_hyperlink.size = 30
    # # $ style.dct_hyperlink.bold = True
    # $ style.dct_hyperlink.color = "#aaaaff"
    # $ style.dct_hyperlink.hover_color = "#ffffff"
    # $ style.dct_hyperlink.underline = True
    # $ style.dct_hyperlink.outlines = [(2, '#000', 0, 0)]
    
    # $ style.hyperlink_text = style.dct_hyperlink
    
    
    ### Музыка в меню
    
    $ dct_Moments = "<to 124.685>mods/dublicate/sounds/coin/music/Moments_(by_Shane_Ivers).ogg"
    
    $ Ya_vasha_tayna = "<from 1.5>mods/dublicate/sounds/coin/music/Ya_vasha_tayna[instrumental](by_Rock_ostrova).ogg"
    
    
    ### Фоны в меню
    
    image dct_ext_train_day_not_train = "mods/dublicate/images/gui/titles/dct_ext_train_day_not_train.jpg"     # Перрон без поезда
    
    image dct_ext_train_day = "mods/dublicate/images/bg/dct_ext_train_day.jpg" # Перрон с поездом
    
    image dct_titles_view_outside = im.Composite((2736,720), (0,0), "mods/dublicate/images/gui/titles/dct_titles_view_outside.jpg", (1368,0), "mods/dublicate/images/gui/titles/dct_titles_view_outside.jpg")
    
    
    image dct_titles_bg:
        contains:                           # Слой с изображением движущегося фона за окном
            "dct_titles_view_outside"
            anchor (0.75, 0.5) pos (0.5, 0.58)
            linear 7 anchor (0.25, 0.5)
            repeat
        contains:                           # Слой с изображением купе
            "mods/dublicate/images/gui/titles/dct_titles_coupe.png"
            anchor (0.5, 0.5) xpos 0.5 ypos 0.5
            pause 2
            ease 0.1 ypos 0.5015
            ease 0.1 ypos 0.5
            pause 0.2
            ease 0.1 ypos 0.5015
            ease 0.1 ypos 0.5
            repeat



    ###########  —  Страницы меню

    screen dct_titles_authors:

        text 'Модификация «Дубликат» для визуальной новеллы «Бесконечное лето»':
            xalign 0.5
            yalign 0.05
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_fanfic:
    
        text 'На основе фанфика «Дубликат»':
            xalign 0.5
            yalign 0.14
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
            

    screen dct_titles_authors_list: 
            
        text 'СЮЖЕТ, СЦЕНАРИЙ, КОД\n{vspace=15}Двадцатьвторой (Тангейзер Вагнеров)\n\n{vspace=15}МЕНЮ\n{vspace=15}Лисёндра, Salo Tor, Павел Грошев\n\n{vspace=15}СЦЕНАРИЙ, КОД ("Монетка в фонтане")\n{vspace=15}Павел Грошев, Роман Волгин, Endless Sunset\n\n{vspace=15}ВЫЧИТКА, КОРРЕКЦИЯ\n{vspace=15}Андрей Серебрянников, Endless Sunset.\n\n{vspace=15}ГРАФИКА\n{vspace=15}Андрей Серебрянников, Павел Грошев':
            xalign 0.5
            ypos 0.25
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
                    
    
    screen dct_titles_thanks:
    
        text 'Благодарности':
            xalign 0.5
            yalign 0.02
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 100
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_artists:
    
        text 'Художники':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_artists_list1:
        
        text 'AnBro\n{vspace=15}ArseniXC\n{vspace=15}Bomj Jack Letovich Tucker\n{vspace=15}burbur\n{vspace=15}Dream Maker (PapaKarlo)\n{vspace=15}Eru\n{vspace=15}Kef34\n{vspace=15}KokkaMokka\n{vspace=15}MarkTailor\n{vspace=15}miku_xikka\n{vspace=15}Mo~\n{vspace=15}Naraii\n{vspace=15}Orika\n{vspace=15}polinaowl\n{vspace=15}Quandial':
            xalign 0.5
            ypos 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
                    

    screen dct_titles_artists_list2:
    
        text 'SHONI AGITA\n{vspace=15}Tocakyca\n{vspace=15}UntitledExpression\n{vspace=15}VAR\n{vspace=15}Weeping Cat (Four MdSd)\n{vspace=15}Wrath Art\n{vspace=15}Алексей Ручковский\n{vspace=15}Вдохновение vs. Лень\n{vspace=15}Ив Нарвал\n{vspace=15}Лаборатория фотошопа\n{vspace=15}Максим Смолев\n{vspace=15}Персональный Арт Советова\n{vspace=15}Стасек\n{vspace=15}Художник-кун':
            xalign 0.5
            ypos 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_artists_list3:
    
        text 'Фон коридора административного корпуса\nпредоставлен Дмитрием Зотовым\n{vspace=30}За замечательную Юлю спасибо\nДине Ким и Lana Lupine\n{vspace=30}Авторы двух фонов железной дороги,\nк сожалению, пока не опознаны\n{vspace=90}Отдельная благодарность команде\nБесконечное лето 3D (Summer\'s Builders)':
            xalign 0.5
            ypos 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
              
           
    screen dct_titles_mods:
        
        text 'Моды':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
        
        
    screen dct_titles_mods_list1:
    
        text '7 дней лета: Lost Alpha\n{vspace=15}Second Chance\n{vspace=15}Sprites and CG by Orika\n{vspace=15}Бесконечное Лето [[Русская озвучка]\n{vspace=15}Булки, кефир и рок-н-ролл \n{vspace=15}Вспомнить всё\n{vspace=15}Гости из будущего\n{vspace=15}Другая история\n{vspace=15}История одного пионера\n{vspace=15}Лето в библиотеке\n{vspace=15}Настоящий лагерь...':
            xalign 0.5
            ypos 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
                
    
    screen dct_titles_mods_list2:
    
        text 'Они пьют не только кровь\n{vspace=15}Орден Совёнка 2\n{vspace=15}Падшая пионерка\n{vspace=15}По ту сторону Совёнка\n{vspace=15}Поездка Лены\n{vspace=15}Последний пионер\n{vspace=15}Продолжение истории\n{vspace=15}СБОРНИК ЦГ, БГ И СПРАЙТОВ\n(+архивы разработки)\n{vspace=15}Смотритель\n{vspace=15}Эти безумные деньки':
            xalign 0.5
            ypos 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
        
    
    screen dct_titles_novels_anime:
    
        text 'Новеллы':
            xalign 0.5
            yalign 0.2
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
            
        text 'Аниме':
            xalign 0.5
            yalign 0.56
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_novels_anime_list:
    
        text 'Конгломерат\n{vspace=15}Морозный поцелуй\n{vspace=15}Травница':
            xalign 0.5
            ypos 0.26
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
            
        text 'Ветер крепчает\n{vspace=15}Повседневная жизнь старшеклассников':
            xalign 0.5
            ypos 0.6
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_sounds:

        text 'Музыка и звуки':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]


    screen dct_titles_sounds_list:
    
        text 'Стихи (а вообще-то песня) «Демон Дороги» - с разрешения автора: Светланы Никифоровой (Алькор)\n{vspace=15}Зелёный гитарист — Everlasting Summer [[guitar cover]\n{vspace=15}Wintergatan — Marble Machine, Sommarfågel, Starmachine2000, Telescope, Valentine\n{vspace=15}Инструментальная версия песни «Я ваша тайна» предоставлена автором: Владимиром Захаровым (Рок-Острова)\n{vspace=30}Дополнительные звуки и музыка:\nnoisefx.ru , freesound.org , vk.com/madiax, freemusicarchive.org , audeeyah.com , bensound.com':
            xalign 0.5
            ypos 0.2
            text_align 0.5            
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
        

    screen dct_titles_sovenok:
    
        text 'Посвящается памяти Тангейзера Вагнерова.\n\n{vspace=15}От тех, кому не всё равно. Для тех, кто ждал и верил.\n\n{vspace=15}...Где-то в мире бесконечного лета в лагерь приехал новенький: высокий, сутулый и худой, по характеру и любви к книгам и технике — что-то среднее между Электроником и Женей. Скоро он проснётся, через положенное время выйдет из автобуса и пойдёт к воротам Совёнка навстречу Славе.\n\n{vspace=15}А подброшенная вверх монетка навсегда останется стоять на ребре.':
            xpos 210
            yalign 0.9
            xmaximum 1500
            justify True
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]

    ###########  —  Страницы финальных титров закончились
    


    
    
    #################################
    #################################
    #################################
    #################################
    #################################
    #
    #
    #        Титры меню
    #
    #
    #################################
    #################################
    #################################
    #################################
    #################################






    
    screen dct_credits_authors:
    
        text 'Модификация «Дубликат» для визуальной новеллы «Бесконечное лето»':
            xalign 0.5
            yalign 0.05
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
    
        text 'На основе фанфика «Дубликат»':
            xalign 0.5
            yalign 0.14
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
            
        text 'СЮЖЕТ, СЦЕНАРИЙ, КОД\n{vspace=15}Двадцатьвторой (Тангейзер Вагнеров)\n\n{vspace=15}МЕНЮ\n{vspace=15}Лисёндра, Salo Tor, Павел Грошев\n\n{vspace=15}СЦЕНАРИЙ, КОД ("Монетка в фонтане")\n{vspace=15}Павел Грошев, Роман Волгин, Endless Sunset\n\n{vspace=15}ВЫЧИТКА, КОРРЕКЦИЯ\n{vspace=15}Андрей Серебрянников, Endless Sunset.\n\n{vspace=15}ГРАФИКА\n{vspace=15}Андрей Серебрянников, Павел Грошев':
            xalign 0.5
            ypos 0.22
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
        
        textbutton 'Меню':
            xalign 0.4
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_authors", transition=Dissolve(0.4)), Jump("dct_credits_closed")]
            
        textbutton 'Далее':
            xalign 0.6
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_titles_credits1", transition=Dissolve(0.4)), Return()]
            
    screen dct_credits_artists:
    
        text 'Благодарности':
            xalign 0.5
            yalign 0.02
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 100
            outlines [(2, '#000', 0, 0)]

        text 'Художники':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]

    ##
    ##      Вариант с гиперссылками в самом тексте (пока отключён, т.к. не понятно, как нужно прописать стиль для гиперссылок)
    ##

        # text '{a=https://vk.com/anbro_s}AnBro{/a}\n{vspace=15}{a=https://vk.com/arsenixc}ArseniXC{/a}\n{vspace=15}{a=https://vk.com/bomjjack}Bomj Jack Letovich Tucker{/a}\n{vspace=15}{a=https://vk.com/bur_2}burbur{/a}\n{vspace=15}{a=https://vk.com/dreamofmaker}Dream Maker (PapaKarlo){/a}\n{vspace=15}{a=https://vk.com/eru_chan}Eru{/a}\n{vspace=15}{a=https://vk.com/kef34art}Kef34{/a}\n{vspace=15}{a=https://vk.com/kokkamokka}KokkaMokka{/a}\n{vspace=15}{a=https://vk.com/shwwma}MarkTailor{/a}\n{vspace=15}{a=https://vk.com/kunz_digital}miku_xikka{/a}\n{vspace=15}{a=https://vk.com/mo_shy_arts}Mo~{/a}\n{vspace=15}{a=https://vk.com/naraii03}Naraii{/a}\n{vspace=15}{a=https://vk.com/orika_art}Orika{/a}\n{vspace=15}{a=https://vk.com/owlpolina}polinaowl{/a}\n{vspace=15}{a=https://vk.com/quandyarts}Quandial{/a}':
            # xalign 0.25
            # ypos 0.19
            # text_align 0.5
            # color "#fff"
            # font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            # size 30
            # outlines [(2, '#000', 0, 0)]
        
        # text '{a=https://vk.com/shoniagita}SHONI AGITA{/a}\n{vspace=15}{a=https://vn.reactor.cc/user/Tocakyca}Tocakyca{/a}\n{vspace=15}{a=https://vk.com/untitledexpression}UntitledExpression{/a}\n{vspace=15}{a=https://vk.com/art_by_var}VAR{/a}\n{vspace=15}{a=https://vk.com/weepingcat}Weeping Cat (Four MdSd){/a}\n{vspace=15}{a=https://www.instagram.com/wrath.art/}Wrath Art{/a}\n{vspace=15}{a=https://vk.com/id185406057}Алексей Ручковский{/a}\n{vspace=15}{a=https://vk.com/vd_vs_ln}Вдохновение vs. Лень{/a}\n{vspace=15}{a=https://vk.com/public61508685}Ив Нарвал{/a}\n{vspace=15}{a=https://vk.com/public184889068}Лаборатория фотошопа{/a}\n{vspace=15}{a=https://vk.com/smolevn}Максим Смолев{/a}\n{vspace=15}{a=https://vk.com/sovietov_art}Персональный Арт Советова{/a}\n{vspace=15}{a=https://vk.com/stasekpivasek}Стасек{/a}\n{vspace=15}{a=https://vk.com/ikskey}Художник-кун{/a}':
            # xalign 0.75
            # ypos 0.19
            # text_align 0.5
            # color "#fff"
            # font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            # size 30
            # outlines [(2, '#000', 0, 0)]
            
        ################################################    
            
        ### Гиперссылки через textbutton
        
        textbutton "AnBro" xcenter 0.32 ypos 0.19 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/anbro_s")
        textbutton "ArseniXC" xcenter 0.32 ypos 0.24 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/arsenixc")
        textbutton "Bomj Jack Letovich Tucker" xcenter 0.32 ypos 0.29 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/bomjjack")
        textbutton "burbur" xcenter 0.32 ypos 0.34 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/bur_2")
        textbutton "Dream Maker (PapaKarlo)" xcenter 0.32 ypos 0.39 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/dreamofmaker")
        textbutton "Eru" xcenter 0.32 ypos 0.44 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/eru_chan")
        textbutton "Kef34" xcenter 0.32 ypos 0.49 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/kef34art")
        textbutton "KokkaMokka" xcenter 0.32 ypos 0.54 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/kokkamokka")
        textbutton "MarkTailor" xcenter 0.32 ypos 0.59 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/shwwma")
        textbutton "miku xikka" xcenter 0.32 ypos 0.64 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/kunz_digital")
        textbutton "Mo~" xcenter 0.32 ypos 0.69 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/mo_shy_arts")
        textbutton "Narai" xcenter 0.32 ypos 0.74 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/naraii03")
        textbutton "Orika" xcenter 0.32 ypos 0.79 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/orika_art")
        textbutton "polinaowl" xcenter 0.32 ypos 0.84 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/owlpolina")
        textbutton "Quandial" xcenter 0.32 ypos 0.89 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/quandyarts")
        
        textbutton "SHONI AGITA" xcenter 0.68 ypos 0.19 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/shoniagita")
        textbutton "Tocakyca" xcenter 0.68 ypos 0.24 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vn.reactor.cc/user/Tocakyca")
        textbutton "UntitledExpression" xcenter 0.68 ypos 0.29 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/untitledexpression")
        textbutton "VAR" xcenter 0.68 ypos 0.34 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/art_by_var")
        textbutton "Weeping Cat (Four MdSd)" xcenter 0.68 ypos 0.39 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/weepingcat")
        textbutton "Wrath Art" xcenter 0.68 ypos 0.44 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://www.instagram.com/wrath.art/")
        textbutton "Алексей Ручковский" xcenter 0.68 ypos 0.49 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/id185406057")
        textbutton "Вдохновение vs. Лень" xcenter 0.68 ypos 0.54 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/vd_vs_ln")
        textbutton "Ив Нарвал" xcenter 0.68 ypos 0.59 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/public61508685")
        textbutton "Лаборатория фотошопа" xcenter 0.68 ypos 0.64 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/public184889068")
        textbutton "Максим Смолев" xcenter 0.68 ypos 0.69 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/smolevn")
        textbutton "Персональный Арт Советова" xcenter 0.68 ypos 0.74 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/sovietov_art")
        textbutton "Стасек" xcenter 0.68 ypos 0.79 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/stasekpivasek")
        textbutton "Художник-кун" xcenter 0.68 ypos 0.84 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/ikskey")

            
        ################################################ 

        textbutton 'Меню':
            xalign 0.4
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_artists", transition=Dissolve(0.4)), Jump("dct_credits_closed")]
            
        textbutton 'Далее':
            xalign 0.6
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_artists", transition=Dissolve(0.4)), Return()]


    screen dct_credits_artists_other:
    
        text 'Благодарности':
            xalign 0.5
            yalign 0.02
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 100
            outlines [(2, '#000', 0, 0)]

        text 'Художники':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
    
    
    ##
    ##      Вариант с гиперссылками в самом тексте (пока отключён, т.к. не понятно, как нужно прописать стиль для гиперссылок)
    ##
    
        # text "Фон коридора административного корпуса\nпредоставлен Дмитрием Зотовым\n{vspace=30}За замечательную Юлю спасибо\n{a=https://vk.com/shopolak}Дине Ким{/a} и Lana Lupine\n{vspace=30}Авторы двух фонов железной дороги,\nк сожалению, пока не опознаны\n{vspace=90}Отдельная благодарность команде\n{a=https://vk.com/everlastingsummer3d}Бесконечное лето 3D (Summer's Builders){/a}":
            # xalign 0.5
            # ypos 0.22
            # text_align 0.5
            # color "#fff"
            # font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            # size 30
            # outlines [(2, '#000', 0, 0)]
            
        ################################################    
            
        ### Гиперссылки через textbutton
        
        text "Фон коридора административного корпуса\nпредоставлен Дмитрием Зотовым\n{vspace=30}За замечательную Юлю спасибо\n{space=160} и Lana Lupine\n{vspace=30}Авторы двух фонов железной дороги,\nк сожалению, пока не опознаны\n{vspace=90}Отдельная благодарность команде":
            xalign 0.5
            ypos 0.22
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
            
            
        textbutton "Дине Ким" xcenter 0.444 ypos 0.365 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/shopolak")
        textbutton "Бесконечное лето 3D (Summer's Builders)" xcenter 0.5 ypos 0.63 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/everlastingsummer3d")
        
        ################################################

        textbutton 'Меню':
            xalign 0.4
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_artists_other", transition=Dissolve(0.4)), Jump("dct_credits_closed")]
            
        textbutton 'Далее':
            xalign 0.6
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_artists_other", transition=Dissolve(0.4)), Return()]


    screen dct_credits_mods:
        
        text 'Благодарности':
            xalign 0.5
            yalign 0.02
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 100
            outlines [(2, '#000', 0, 0)]

        text 'Моды':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]

        text '7 дней лета: Lost Alpha\n{vspace=15}Second Chance\n{vspace=15}Sprites and CG by Orika\n{vspace=15}Бесконечное Лето [[Русская озвучка]\n{vspace=15}Булки, кефир и рок-н-ролл \n{vspace=15}Вспомнить всё\n{vspace=15}Гости из будущего\n{vspace=15}Другая история\n{vspace=15}История одного пионера\n{vspace=15}Лето в библиотеке\n{vspace=15}Настоящий лагерь...':
            xalign 0.25
            ypos 0.22
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]

        text 'Они пьют не только кровь\n{vspace=15}Орден Совёнка 2\n{vspace=15}Падшая пионерка\n{vspace=15}По ту сторону Совёнка\n{vspace=15}Поездка Лены\n{vspace=15}Последний пионер\n{vspace=15}Продолжение истории\n{vspace=15}СБОРНИК ЦГ, БГ И СПРАЙТОВ\n(+архивы разработки)\n{vspace=30}Смотритель\n{vspace=15}Эти безумные деньки':
            xalign 0.75
            ypos 0.22
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]

        textbutton 'Меню':
            xalign 0.4
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_mods1", transition=Dissolve(0.4)), Jump("dct_credits_closed")]
            
        textbutton 'Далее':
            xalign 0.6
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_mods1", transition=Dissolve(0.4)), Return()]


    screen dct_credits_sounds_novel_anime:

        text 'Благодарности':
            xalign 0.5
            yalign 0.02
            color "#14ab14"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 100
            outlines [(2, '#000', 0, 0)]

        text 'Музыка и звуки':
            xalign 0.5
            yalign 0.14
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]

    ##
    ##      Вариант с гиперссылками в самом тексте (пока отключён, т.к. не понятно, как нужно прописать стиль для гиперссылок)
    ##

        # text 'Стихи (а вообще-то песня) «Демон Дороги» с разрешения автора: {a=https://www.allkorr.ru/}Светланы Никифоровой (Алькор){/a}\n{vspace=15}{a=https://vk.com/zgitarist}Зелёный гитарист{/a} — {a=https://www.youtube.com/watch?v=z6sTDBAUTfg}Everlasting Summer [[guitar cover]{/a}\n{vspace=15}{a=http://www.wintergatan.net}Wintergatan{/a} — Marble Machine, Sommarfågel, Starmachine2000, Telescope, Valentine\n{vspace=15}Инструментальная версия песни «Я ваша тайна» предоставлена автором: {a=https://vk.com/vladirzah}Владимиром Захаровым{/a} ({a=http://www.rok-ostrova.ru}Рок-острова{/a})\n{vspace=30}Дополнительные звуки и музыка:\n{a=https://noisefx.ru/}noisefx.ru{/a} , {a=https://freesound.org/}freesound.org{/a} , {a=https://vk.com/madiax/}vk.com/madiax{/a} , {a=http://freemusicarchive.org/}freemusicarchive.org{/a} , {a=https://audeeyah.com/}audeeyah.com{/a} , {a=https://www.bensound.com/}bensound.com{/a}':
            # xalign 0.5
            # ypos 0.22
            # text_align 0.5            
            # color "#fff"
            # font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            # size 30
            # outlines [(2, '#000', 0, 0)]
            
            
        ################################################    
            
        ### Гиперссылки через textbutton

        text "Стихи (а вообще-то песня) «Демон Дороги» с разрешения автора: " xanchor 1.0 xpos 0.635 ypos 0.22 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        textbutton "Светланы Никифоровой (Алькор)" xanchor 0.0 xpos 0.632 ypos 0.22 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://www.allkorr.ru/")
        
        textbutton "Зелёный гитарист" xanchor 1.0 xpos 0.434 ypos 0.273 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/zgitarist")
        text " — " xanchor 0.0 xpos 0.432 ypos 0.273 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        textbutton "Everlasting Summer [[guitar cover]" xanchor 0.0 xpos 0.456 ypos 0.273 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://www.youtube.com/watch?v=z6sTDBAUTfg")
        
        textbutton "Wintergatan" xanchor 1.0 xpos 0.267 ypos 0.325 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("http://www.wintergatan.net")
        text " — Marble Machine, Sommarfågel, Starmachine2000, Telescope, Valentine" xanchor 0.0 xpos 0.264 ypos 0.325 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        
        text "Инструментальная версия песни «Я ваша тайна» предоставлена автором: " xanchor 1.0 xpos 0.649 ypos 0.378 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        textbutton "Владимиром Захаровым" xanchor 0.0 xpos 0.646 ypos 0.378 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/vladirzah")
        text " (" xanchor 1.0 xpos 0.867 ypos 0.378 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        textbutton "Рок-острова" xanchor 0.0 xpos 0.865 ypos 0.378 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("http://www.rok-ostrova.ru")
        text ")" xanchor 1.0 xpos 0.972 ypos 0.378 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        
        text "Дополнительные звуки и музыка:" xcenter 0.5 ypos 0.445 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]

        text ",{space=225},{space=245},{space=333},{space=229}," xanchor 0.0 xpos 0.2 ypos 0.484 color "#fff" font "mods/dublicate/fonts/OpenSans-Bold.ttf" size 30 outlines [(2, '#000', 0, 0)]
        textbutton "noisefx.ru" xanchor 1.0 xpos 0.198 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://noisefx.ru/")
        textbutton "freesound.org" xanchor 1.0 xpos 0.32 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://freesound.org/")
        textbutton "vk.com/madiax" xanchor 1.0 xpos 0.453 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://vk.com/madiax/")
        textbutton "freemusicarchive.org" xanchor 0.0 xpos 0.463 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("http://freemusicarchive.org")
        textbutton "audeeyah.com" xanchor 0.0 xpos 0.641 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://audeeyah.com/")
        textbutton "bensound.com" xanchor 0.0 xpos 0.765 ypos 0.484 style "dct_hyperlink_button" text_style "dct_hyperlink_button" action OpenURL("https://www.bensound.com/")
        
        ################################################  

        text 'Новеллы':
            xcenter 0.25
            yalign 0.6
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]
            
        text 'Конгломерат\n{vspace=15}Морозный поцелуй\n{vspace=15}Травница':
            xcenter 0.25
            ypos 0.63
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]
            
        text 'Аниме':
            xcenter 0.7
            yalign 0.6
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/TrixieProHeavy_Regular.otf"
            size 50
            outlines [(2, '#000', 0, 0)]

        text 'Ветер крепчает\n{vspace=15}Повседневная жизнь старшеклассников':
            xcenter 0.7
            ypos 0.63
            text_align 0.5
            color "#fff"
            font "mods/dublicate/fonts/OpenSans-Bold.ttf"
            size 30
            outlines [(2, '#000', 0, 0)]

        textbutton 'Меню':
            xalign 0.5
            yalign 0.98
            style "dct_titles_button"
            text_style "dct_titles_button"
            action [Hide("dct_credits_sounds", transition=Dissolve(0.4)), Jump("dct_credits_closed")]
            

    ###########  —  Страницы менюшных титров закончились
    
    


label dct_titles:
    play sound Ya_vasha_tayna fadein 1  # Для версии-концовки, чтоб музыка не зацикливалась
    show dct_titles_bg
    show image(Solid("#000000")):
        alpha 1
        linear 2 alpha 0.15

    $ renpy.pause(2,hard=True)

    $ renpy.block_rollback()    # Запрет отката истории (чтоб колёсиком случайно не накрутили)
    
    # Страница первая, авторы
    show screen dct_titles_authors
    show screen dct_titles_fanfic
    show screen dct_titles_authors_list 
    with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_authors
    hide screen dct_titles_fanfic
    hide screen dct_titles_authors_list 
    with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница вторая, художники раз
    show screen dct_titles_thanks
    show screen dct_titles_artists
    show screen dct_titles_artists_list1
    with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_artists_list1 with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница третья, художники два
    show screen dct_titles_artists_list2 with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_artists_list2 with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница четвертая, художники три
    show screen dct_titles_artists_list3 with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_artists
    hide screen dct_titles_artists_list3
    with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница пятая, моды раз
    show screen dct_titles_mods
    show screen dct_titles_mods_list1
    with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_mods_list1 with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница шестая, моды два
    show screen dct_titles_mods_list2 with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_mods
    hide screen dct_titles_mods_list2
    with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница седьмая, новеллы и аниме
    show screen dct_titles_novels_anime
    show screen dct_titles_novels_anime_list
    with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_novels_anime
    hide screen dct_titles_novels_anime_list
    with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница восьмая, музыка
    show screen dct_titles_sounds
    show screen dct_titles_sounds_list
    with dissolve
    $ renpy.pause(9,hard=True)
    hide screen dct_titles_thanks
    hide screen dct_titles_sounds
    hide screen dct_titles_sounds_list
    with dissolve
    $ renpy.pause(1,hard=True)
    
    # Страница девятая, посвящение
    show screen dct_titles_sovenok with dissolve
    $ renpy.pause(15,hard=True)
    show image(Solid("#000000")): # Плавный переход в черный экран
        linear 6 alpha 1.0
    $ renpy.pause(8,hard=True)  # Ждем, пока погаснет экран. 2 секунды музыка играет в темноте, так задумано
    hide screen dct_titles_sovenok with Dissolve(2.0)
    stop sound fadeout 2

    $ renpy.pause(1.5,hard=True)
    jump dct_mnu2
    
    
    
    #################################
    #################################
    #################################
    #################################
    #################################
    #
    #
    #        Титры меню
    #
    #
    #################################
    #################################
    #################################
    #################################
    #################################





label dct_credits:

    play music dct_Moments fadein 2
    
    if persistent.d_coin > 0: # Если Монетка прочитана, что приравниваем к прочитанному целиком моду, выводится фон с прибывшим поездом
        show dct_ext_train_day
    else:
        show dct_ext_train_day_not_train # Если Монетка не прочитана, выводится пустой перрон, поезд еще в пути 
        
    show image(Solid("#000000")):
        alpha 1
        linear 2 alpha 0.15
    $ renpy.pause(2,hard=True)

    $ renpy.block_rollback()    # Запрет отката истории (чтоб колёсиком случайно не накрутили)
   
    call screen dct_credits_authors with dissolve
    call screen dct_credits_artists
    call screen dct_credits_artists_other
    call screen dct_credits_mods
    call screen dct_credits_sounds_novel_anime

label dct_credits_closed:
    stop music fadeout 2
    show image(Solid("#000000")):
        linear 2 alpha 1

    pause 2.5
    jump dct_mnu2