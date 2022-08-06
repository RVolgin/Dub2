label dct_intro:
    $ prolog_time()
    $ persistent.sprite_time = "day"
    play music music_list["sunny_day"]#Уточнять!
    $ renpy.pause (1)
    scene ext_square_day with blinds
    $ renpy.pause (2)
    show d_jn with pixellate:
        xalign 0.5
        yalign 0.3
    $ renpy.pause (3)
    d_rb "Эта история о людях."
    d_rb "О разных людях, живших и живущих неизвестно где и неизвестно когда."
    d_rb "О людях настоящих и не совсем настоящих."
    d_rb "Но все равно...{w} О людях."
    hide d_jn with pixellate
    $ renpy.pause (1)
    stop music fadeout 1.0
    jump dct_mnu2