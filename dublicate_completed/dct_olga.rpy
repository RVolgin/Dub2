label dct_olga:       #вступительный лейбл
    scene black
    stop ambience
    play music music_list['reflection_on_water']
    show headline_text u"О — значит Ольга" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    show text(u"{size=48}{color=#ffdd7d}{i}Здесь должна быть история про Ольгу.\n \n \n {/i}{/color}{/size}") at cright with dspr
    $ renpy.pause(1.5)
    show text(u"{size=48}{color=#ffdd7d}{i}\nНо её пока не подвезли.\n \n {/i}{/color}{/size}") as text2 at cright with dspr
    $ renpy.pause(1.5)
    show text(u"{size=48}{color=#ffdd7d}{i}\n \nВ смысле, автобус ещё не подошёл.\n {/i}{/color}{/size}") as text3 at cright with dspr
    $ renpy.pause(1.5)
    show text(u"{size=48}{color=#ffdd7d}{i}\n \n \nПоэтому, давайте посмотрим, что там дальше.{/i}{/color}{/size}") as text4 at cright with dspr
    $ renpy.pause(3.0)
    show black as black2 with dissolve
    stop music fadeout 1
    $ renpy.pause(1.0)
    
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
