init 1:
    $ style.dct_menu_button = Style(style.default)
    $ style.dct_menu_button.font  = "mods/dublicate_completed/fonts/bezpr.ttf"
    $ style.dct_menu_button.color = "#000000"
    $ style.dct_menu_button.size = 30
    $ style.dct_menu_button.kerning = 0.3

    $ style.dct_menu_button_unavailable = Style(style.dct_menu_button)
    $ style.dct_menu_button_unavailable.color = "#0835b3"

    $ style.dct_menu_button_exit = Style(style.dct_menu_button)
    $ style.dct_menu_button_exit.size = 38
    
    
screen dct_menu_flower:
    zorder 1
    add "mods/dublicate_completed/images/gui/dct_menu_flower.png"
screen dct_menu_simon_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_simon_sep.png"
screen dct_menu_prologue_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_prologue_sep.png"
screen dct_menu_anabasis_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_anabasis_sep.png"
screen dct_menu_dragon_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_dragon_sep.png"
screen dct_menu_clouds_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_clouds_sep.png"
screen dct_menu_4th_shift_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_4th_shift_sep.png"
screen dct_menu_life_line_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_life_line_sep.png"
screen dct_menu_cat_house_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_cat_house_sep.png"
screen dct_menu_effector_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_effector_sep.png"
screen dct_menu_olga_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_olga_sep.png"
screen dct_menu_coin_sep:
    add "mods/dublicate_completed/images/gui/dct_menu_coin_sep.png"
screen dct_menu:
    add "mods/dublicate_completed/images/gui/dct_menu_bg.png"
    if renpy.seen_label("dct_simon"):
        add "mods/dublicate_completed/images/gui/dct_menu_simon_v.png"
    if renpy.seen_label("dct_prologue"):
        add "mods/dublicate_completed/images/gui/dct_menu_prologue_v.png"
    if renpy.seen_label("dct_anabasis"):
        add "mods/dublicate_completed/images/gui/dct_menu_anabasis_v.png"
    if renpy.seen_label("dct_dragon"):
        add "mods/dublicate_completed/images/gui/dct_menu_dragon_v.png"
    if renpy.seen_label("dct_clouds"):
        add "mods/dublicate_completed/images/gui/dct_menu_clouds_v.png"
    if renpy.seen_label("dct_4th_shift"):
        add "mods/dublicate_completed/images/gui/dct_menu_4th_shift_v.png"
    if renpy.seen_label("dct_life_line"):
        add "mods/dublicate_completed/images/gui/dct_menu_life_line_v.png"
    if renpy.seen_label("dct_cat_house"):
        add "mods/dublicate_completed/images/gui/dct_menu_cat_house_v.png"
    if renpy.seen_label("dct_effector"):
        add "mods/dublicate_completed/images/gui/dct_menu_effector_v.png"
    if renpy.seen_label("dct_olga"):
        add "mods/dublicate_completed/images/gui/dct_menu_olga_v.png"
    if renpy.seen_label("dct_coin"):
        add "mods/dublicate_completed/images/gui/dct_menu_coin_v.png"
    timer 0.01 action ShowTransient("dct_menu_flower")
    textbutton "Сёмка, Сёмка, Сёмочка...":
        xpos 0.59
        ypos 0.164
        if persistent.d_eff > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_simon")]
            hovered ShowTransient("dct_menu_simon_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_simon_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Пролог":
        xpos 0.59
        ypos 0.227
        style "dct_menu_button"
        text_style "dct_menu_button"
        action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_prologue")]
        hovered ShowTransient("dct_menu_prologue_sep", transition=Dissolve(0.2))
        unhovered Hide("dct_menu_prologue_sep", transition=Dissolve(0.2))
    textbutton "Анабасис":
        xpos 0.59
        ypos 0.29
        if persistent.d_prolog > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_anabasis")]
            hovered ShowTransient("dct_menu_anabasis_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_anabasis_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Год дракона":
        xpos 0.59
        ypos 0.353
        if persistent.d_ana > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_dragon")]
            hovered ShowTransient("dct_menu_dragon_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_dragon_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Имена в облаках":
        xpos 0.59
        ypos 0.416
        if persistent.d_ana > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_clouds")]
            hovered ShowTransient("dct_menu_clouds_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_clouds_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Четвёртая смена":
        xpos 0.59
        ypos 0.479
        if persistent.d_lin > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_4th_shift")]
            hovered ShowTransient("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_4th_shift_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Линия жизни":
        xpos 0.59
        ypos 0.542
        if (persistent.d_nam > 0) and (persistent.d_dra > 0):
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_life_line")]
            hovered ShowTransient("dct_menu_life_line_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_life_line_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Кошкин дом":
        xpos 0.59
        ypos 0.605
        if persistent.d_sim > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_cat_house")]#
            hovered ShowTransient("dct_menu_cat_house_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_cat_house_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Эффектор":
        xpos 0.59
        ypos 0.668
        if persistent.d_shif > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_effector")]
            hovered ShowTransient("dct_menu_effector_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_effector_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "О - значит Ольга":
        xpos 0.59
        ypos 0.731
        if (persistent.d_nam > 0) and (persistent.d_sim > 0) and (persistent.d_prolog > 0) and (persistent.d_ana > 0) and (persistent.d_dra > 0) and (persistent.d_shif > 0) and (persistent.d_lin > 0) and (persistent.d_miuki > 0) and (persistent.d_eff > 0):
            style "dct_menu_button"
            text_style "dct_menu_button"
            #action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_olga")]
            #action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_exit")]
            action [Hide("dct_menu", transition=Dissolve(0.2)), Call("dct_olga")]
            hovered ShowTransient("dct_menu_olga_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_olga_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    textbutton "Монетка в фонтане":
        xpos 0.59
        ypos 0.794
        # if persistent.d_miuki > 0:  # Почему-то в техническом меню (dct_mnu.rpy) Монетка завязана на завершение книги Эффектор, а здесь на Кошкин дом. Но ни там, ни там, не на Ольгу, хотя казалось бы, Монетку надо в последнюю очередь читать. Странно. Переделываю на ссылку на Ольгу.
        if persistent.d_olga > 0:
            style "dct_menu_button"
            text_style "dct_menu_button"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_coin")]
            hovered ShowTransient("dct_menu_coin_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_coin_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"
    if (persistent.d_nam > 0) and (persistent.d_sim > 0) and (persistent.d_prolog > 0) and (persistent.d_ana > 0) and (persistent.d_dra > 0) and (persistent.d_shif > 0) and (persistent.d_lin > 0) and (persistent.d_miuki > 0) and (persistent.d_eff > 0) and (persistent.d_olga > 0) and (persistent.d_coin > 0):
        textbutton "Справочник":         # Кнопка СПРАВОЧНИК (должна быть скрыта, пока не прочитан весь мод)
            xpos 0.565
            ypos 0.85
            style "dct_menu_button_exit"
            text_style "dct_menu_button_exit"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_spravochnik")]
    textbutton "Выход":
        xpos 0.78
        ypos 0.85
        style "dct_menu_button_exit"
        text_style "dct_menu_button_exit"
        action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_exit")]