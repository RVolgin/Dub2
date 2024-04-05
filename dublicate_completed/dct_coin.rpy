init 1:
    $ style.dct_coin_choosing = Style(style.default)
    $ style.dct_coin_choosing.color = "#ffdd7d"
    $ style.dct_coin_choosing.hover_color = "#fffbb4"
    $ style.dct_coin_choosing.underline = False
    $ style.dct_coin_choosing.text_align = 0.5

screen dct_coin_choosing:
    textbutton "{size=56}{i}Монетка в фонтане{/i}{/size}":
        xcenter 0.5
        ycenter 0.45
        style "dct_coin_choosing"
        text_style "dct_coin_choosing"
        action Jump("dct_coin_dyn")
    
    textbutton "{i}{size=56}Монетка в фонтане: расширенная версия{/size}\n{size=30}Содержит дословный текст исходного фанфика со всеми подробностями{/size}{/i}":
        xcenter 0.5
        ycenter 0.55
        style "dct_coin_choosing"
        text_style "dct_coin_choosing"
        action Jump("dct_coin_ped")

label dct_coin:
    if (persistent.d_coin > 0):
        scene black
        call screen dct_coin_choosing
    else:
        jump dct_coin_dyn
