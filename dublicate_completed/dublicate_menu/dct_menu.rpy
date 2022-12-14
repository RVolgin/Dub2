init 1:
    $ style.dct_menu_button = Style(style.default)
    $ style.dct_menu_button.font  = "mods/dublicate/fonts/bezpr.ttf"
    $ style.dct_menu_button.color = "#000000"
    $ style.dct_menu_button.size = 30
    $ style.dct_menu_button.kerning = 0.3

    $ style.dct_menu_button_unavailable = Style(style.dct_menu_button)
    $ style.dct_menu_button_unavailable.color = "#909090"
    
    $ style.dct_menu_button_increase = Style(style.dct_menu_button)
    $ style.dct_menu_button_increase.color = "#0835b3"

    $ style.dct_menu_button_exit = Style(style.dct_menu_button)
    $ style.dct_menu_button_exit.size = 38
    
    
screen dct_menu_flower:
    zorder 1
    add "mods/dublicate/images/gui/dct_menu_flower.png"
screen dct_menu_olga_sep:
    add "mods/dublicate/images/gui/dct_menu_olga_sep.png"
screen dct_menu_simon_sep:
    add "mods/dublicate/images/gui/dct_menu_simon_sep.png"
screen dct_menu_cat_house_sep:
    add "mods/dublicate/images/gui/dct_menu_cat_house_sep.png"
screen dct_menu_prologue_sep:
    add "mods/dublicate/images/gui/dct_menu_prologue_sep.png"
screen dct_menu_anabasis_sep:
    add "mods/dublicate/images/gui/dct_menu_anabasis_sep.png"
screen dct_menu_life_line_sep:
    add "mods/dublicate/images/gui/dct_menu_life_line_sep.png"
screen dct_menu_dragon_sep:
    add "mods/dublicate/images/gui/dct_menu_dragon_sep.png"
screen dct_menu_clouds_sep:
    add "mods/dublicate/images/gui/dct_menu_clouds_sep.png"
screen dct_menu_4th_shift_sep:
    add "mods/dublicate/images/gui/dct_menu_4th_shift_sep.png"
screen dct_menu_effector_sep:
    add "mods/dublicate/images/gui/dct_menu_effector_sep.png"

screen dct_menu_coin_sep:
    add "mods/dublicate/images/gui/dct_menu_coin_sep.png"
screen dct_menu:
    add "mods/dublicate/images/gui/dct_menu_bg.png"
    if persistent.d_olga > 0:
        add "mods/dublicate/images/gui/dct_menu_olga_v.png"
    if persistent.d_sim > 0:
        add "mods/dublicate/images/gui/dct_menu_simon_v.png"
    if persistent.d_miuki > 0:
        add "mods/dublicate/images/gui/dct_menu_cat_house_v.png"
    if persistent.d_prolog > 0:
        add "mods/dublicate/images/gui/dct_menu_prologue_v.png"
    if persistent.d_ana > 0:
        add "mods/dublicate/images/gui/dct_menu_anabasis_v.png"
    if persistent.d_lin > 0:
        add "mods/dublicate/images/gui/dct_menu_life_line_v.png"
    if persistent.d_dra > 0:
        add "mods/dublicate/images/gui/dct_menu_dragon_v.png"
    if persistent.d_nam > 0:
        add "mods/dublicate/images/gui/dct_menu_clouds_v.png"
    if persistent.d_shif > 0:
        add "mods/dublicate/images/gui/dct_menu_4th_shift_v.png"
    if persistent.d_eff > 0:
        add "mods/dublicate/images/gui/dct_menu_effector_v.png"
    if persistent.d_coin > 0:
        add "mods/dublicate/images/gui/dct_menu_coin_v.png"
    timer 0.01 action ShowTransient("dct_menu_flower")
    
    textbutton "?? - ???????????? ??????????":
        xpos 0.59
        ypos 0.171
        if persistent.d_miuki > 0:
            if renpy.seen_label("dct_olga"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_olga")]
                hovered ShowTransient("dct_menu_olga_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_olga_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_olga")]
                hovered ShowTransient("dct_menu_olga_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_olga_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    
    textbutton "??????????, ??????????, ??????????????...":
        xpos 0.59
        ypos 0.248
        if persistent.d_eff > 0:
            if renpy.seen_label("dct_simon"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_simon")]
                hovered ShowTransient("dct_menu_simon_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_simon_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_simon")]
                hovered ShowTransient("dct_menu_simon_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_simon_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "???????????? ??????":
        xpos 0.605
        ypos 0.304
        if persistent.d_sim > 0:
            if renpy.seen_label("dct_cat_house"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_cat_house")]#
                hovered ShowTransient("dct_menu_cat_house_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_cat_house_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_cat_house")]#
                hovered ShowTransient("dct_menu_cat_house_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_cat_house_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    
    textbutton "????????????":
        xpos 0.59
        ypos 0.381
        if renpy.seen_label("dct_prologue"):
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_prologue")]
            hovered ShowTransient("dct_menu_prologue_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_prologue_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_increase"
            text_style "dct_menu_button_increase"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_prologue")]
            hovered ShowTransient("dct_menu_prologue_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_prologue_sep", transition=Dissolve(0.2))
    textbutton "????????????????":
        xpos 0.59
        ypos 0.437
        if persistent.d_prolog > 0:
            if renpy.seen_label("dct_anabasis"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_anabasis")]
                hovered ShowTransient("dct_menu_anabasis_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_anabasis_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_anabasis")]
                hovered ShowTransient("dct_menu_anabasis_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_anabasis_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "?????????? ??????????":
        xpos 0.605
        ypos 0.493
        if (persistent.d_nam > 0) and (persistent.d_dra > 0):
            if renpy.seen_label("dct_life_line"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_life_line")]
                hovered ShowTransient("dct_menu_life_line_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_life_line_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_life_line")]
                hovered ShowTransient("dct_menu_life_line_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_life_line_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "?????? ??????????????":
        xpos 0.605
        ypos 0.549
        if persistent.d_ana > 0:
            if renpy.seen_label("dct_dragon"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_dragon")]
                hovered ShowTransient("dct_menu_dragon_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_dragon_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_dragon")]
                hovered ShowTransient("dct_menu_dragon_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_dragon_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "?????????? ?? ??????????????":
        xpos 0.59
        ypos 0.605
        if persistent.d_ana > 0:
            if renpy.seen_label("dct_clouds"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_clouds")]
                hovered ShowTransient("dct_menu_clouds_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_clouds_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_clouds")]
                hovered ShowTransient("dct_menu_clouds_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_clouds_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "?????????????????? ??????????":
        xpos 0.59
        ypos 0.661
        if persistent.d_lin > 0:
            if renpy.seen_label("dct_4th_shift"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_4th_shift")]
                hovered ShowTransient("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_4th_shift")]
                hovered ShowTransient("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "????????????????":
        xpos 0.605
        ypos 0.717
        if persistent.d_shif > 0:
            if renpy.seen_label("dct_effector"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_effector")]
                hovered ShowTransient("dct_menu_effector_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_effector_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_effector")]
                hovered ShowTransient("dct_menu_effector_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_effector_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "?????????????? ?? ??????????????":
        xpos 0.59
        ypos 0.773
        if (persistent.d_olga > 0) and (persistent.d_dra > 0):
            if renpy.seen_label("dct_coin"):
                style "dct_menu_button"
                text_style "dct_menu_button"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_coin")]
                hovered ShowTransient("dct_menu_coin_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_coin_sep", transition=Dissolve(0.2))
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
                action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_coin")]
                hovered ShowTransient("dct_menu_coin_sep", transition=Dissolve(0.2))
                unhovered Hide("dct_menu_coin_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    if (persistent.d_nam > 0) and (persistent.d_sim > 0) and (persistent.d_prolog > 0) and (persistent.d_ana > 0) and (persistent.d_dra > 0) and (persistent.d_shif > 0) and (persistent.d_lin > 0) and (persistent.d_miuki > 0) and (persistent.d_eff > 0) and (persistent.d_olga > 0) and (persistent.d_coin > 0):
        textbutton "????????????????????":         # ???????????? ???????????????????? (????????????, ???????? ???? ???????????????? ???????? ??????)
            xpos 0.565
            ypos 0.85
            style "dct_menu_button_exit"
            text_style "dct_menu_button_exit"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_spravochnik")]
    textbutton "??????????":
        xpos 0.78
        ypos 0.85
        style "dct_menu_button_exit"
        text_style "dct_menu_button_exit"
        action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_exit")]