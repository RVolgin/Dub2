init:

    $ dct_sprav_page = []    # Номер стараницы, открытой в Справочнике
    
    image dct_bg_delo_spravochnik = ConditionSwitch(True, im.Composite((1920, 1080), (0, 0), 'mods/dublicate/Images/gui/spravochnik/dct_bg_table.jpg', (0, 0), 'mods/dublicate/Images/gui/spravochnik/dct_bg_delo.png', (0, 0), 'mods/dublicate/Images/gui/spravochnik/dct_bg_title.png'))


    #sfx
      
    $ dct_paper_sprav = [       # Набор звуков листания из разных частей одного файла
        "<from 0.27 to 1.73>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 2.64 to 4.17>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 5.20 to 6.15>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 7.13 to 8.06>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 8.43 to 8.98>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 9.67 to 10.96>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        "<from 11.46 to 12.05>mods/dublicate/Sounds/sfx/dct_sfx_pages.ogg",
        ]

    
    #music
        
    $ dct_playlist_sprav = [    # Плейлист из нескольких композиций
        "mods/dublicate/Sounds/coin/music/Sommarfagel[Exclusive_Mix](by_Wintergatan).ogg",
        "mods/dublicate/Sounds/coin/music/Marble_Machine(by_Wintergatan).ogg",
        "mods/dublicate/Sounds/coin/music/Starmachine2000(by_Wintergatan).ogg",
        "mods/dublicate/Sounds/coin/music/Valentine(by_Wintergatan).ogg",
        "mods/dublicate/Sounds/coin/music/Telescope(by_Wintergatan).ogg"
        ]
    
    
    # Установка фона и запуск музыки
    

label dct_spravochnik:

    $ day_time()
    $ dct_sprav_page = []
    show dct_bg_delo_spravochnik
    window auto
    stop sound
    stop sound_loop
    stop ambience
    $ renpy.music.set_volume(0.3)
    if renpy.seen_label("dct_spravochnik_ukaz"):
        $ renpy.random.shuffle(dct_playlist_sprav)  # Рандомизация порядка композиций в плейлисте. Начинает срабатывать только после того, как Справочник хотябы раз запускали: осуществляется проверка на открытие лейбла dct_spravochnik_ukaz
    queue music dct_playlist_sprav

    
    
    # Алфавитный указатель
    
label dct_spravochnik_ukaz:

        
    $ renpy.block_rollback()    # Запрет отката истории (чтоб колёсиком случайно не накрутили)

    
    call screen dct_spravochnik_ukaz
    screen dct_spravochnik_ukaz:
        tag imagemap_ukaz
        modal True
        
        imagemap:
            ground "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_0a_ground.png"
            auto "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_0a_%s.png"
            alpha True  # Прозрачные области изображения исключаются из активных зон
            
            hotspot(330,230,275,130) action [SetVariable("dct_sprav_page", 1), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # АБ
            hotspot(340,380,550,280) action [SetVariable("dct_sprav_page", 3), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # ГДЖЗИ
            hotspot(460,670,300,290) action [SetVariable("dct_sprav_page", 4), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # КЛМ
            hotspot(760,830,125,135) action [SetVariable("dct_sprav_page", 6), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # О
            hotspot(1345,220,130,145) action [SetVariable("dct_sprav_page", 8), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]  # С
            hotspot(1345,375,270,300) action [SetVariable("dct_sprav_page", 10), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")] # ФЦ
            
        imagemap:   # Некоторые зоны со ссылками переплетаются, поэтому пришлось добавить второй imagemap
            ground "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_0b_ground.png"
            auto "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_0b_%s.png"
            alpha True  # Прозрачные области изображения исключаются из активных зон
            
            hotspot(605,235,145,140) action [SetVariable("dct_sprav_page", 2), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # В
            hotspot(615,825,140,135) action [SetVariable("dct_sprav_page", 5), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]   # Н
            hotspot(1060,215,285,150) action [SetVariable("dct_sprav_page", 7), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]  # ПР
            hotspot(1210,365,250,150) action [SetVariable("dct_sprav_page", 9), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")]  # ТУ
            hotspot(1215,680,280,285) action [SetVariable("dct_sprav_page", 11), Play("sound", renpy.random.choice(dct_paper_sprav)), Jump("dct_spravochnik_pages")] # ШЭЮ
            hotspot(800,125,100,135) action Jump("dct_spravochnik_menu")    # Меню
                
            
            
            
    # Общая конва для всех страниц
            
label dct_spravochnik_pages:
    pause 0.3
    
    $ renpy.block_rollback()    # Запрет отката истории (чтоб колёсиком случайно не накрутили)
    
    call screen dct_spravochnik_page
    screen dct_spravochnik_page:
        tag imagemap_pages
        modal True
        
        imagemap:
            ground "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_[dct_sprav_page]_ground.png"
            idle "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_[dct_sprav_page]_idle.png"
            hover "mods/dublicate/Images/gui/spravochnik/dct_spravochnik_page_[dct_sprav_page]_hover.png"
            alpha True  # Прозрачные области изображения исключаются из активных зон
            
            hotspot(330,125,130,100):                                       # Предыдущая страница
                action [
                    If(dct_sprav_page > 1, true=SetVariable("dct_sprav_page", dct_sprav_page - 1), false=SetVariable("dct_sprav_page", dct_sprav_page + 10)),
                    Play("sound", renpy.random.choice(dct_paper_sprav)),    # Выбирается рандомный звук из списка внутри переменной
                    Jump("dct_spravochnik_pages")
                    ]
                
            hotspot(460,125,130,100):                                       # Следующая страница
                action [
                    If(dct_sprav_page < 11, true=SetVariable("dct_sprav_page", dct_sprav_page + 1), false=SetVariable("dct_sprav_page", dct_sprav_page - 10)),
                    Play("sound", renpy.random.choice(dct_paper_sprav)),    # Выбирается рандомный звук из списка внутри переменной
                    Jump("dct_spravochnik_pages")
                    ]
                
            hotspot(680,125,100,100):                                       # Алфавитный указатель
                action [
                    Play("sound", renpy.random.choice(dct_paper_sprav)),
                    Jump("dct_spravochnik_ukaz_pause")
                    ]
            
            hotspot(800,125,100,100) action Jump("dct_spravochnik_menu")    # Меню
            
            

    # Пауза перед алфавитным указателем (нужна при перелистывании)
    
label dct_spravochnik_ukaz_pause:
    pause 0.3
    jump dct_spravochnik_ukaz


    # Выход в меню
    
label dct_spravochnik_menu:
    stop music
    $ renpy.music.set_volume(1.0)
    jump dct_mnu2


