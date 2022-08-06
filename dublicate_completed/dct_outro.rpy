label dct_exit:
    if (persistent.d_sim > 0 and persistent.d_prolog > 0 and persistent.d_ana > 0 and persistent.d_dra > 0 and persistent.d_nam > 0 and persistent.d_shif > 0 and persistent.d_lin > 0 and persistent.d_miuki > 0 and persistent.d_eff > 0 and persistent.d_coin > 0 ):
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
        d_rb "О людях настоящих и не совсем настоящих."
        d_rb "Но все равно...{w} О людях."
        d_rb "О людях{w} и человечности."
        hide d_jn with pixellate
        $ renpy.pause (1)
        stop music fadeout 1.0
    
    scene black
    show credits dct_credits:
        xalign 0.5
        ypos 1.3
        linear 52.0 ypos -4.0
    $ renpy.pause(15)

return