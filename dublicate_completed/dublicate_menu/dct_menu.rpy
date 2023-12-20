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
    
    $ style.dct_menu_button_dynamic = Style(style.dct_menu_button)
    $ style.dct_menu_button_dynamic.color = "#046622"
    
    $ style.dct_menu_button_pedantic = Style(style.dct_menu_button)
    $ style.dct_menu_button_pedantic.color = "#710547"

    $ style.dct_menu_button_exit = Style(style.dct_menu_button)
    $ style.dct_menu_button_exit.size = 38
    
    $ dct_dynped = True
    
    
    
    
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
    
screen dct_menu_coin_help:
    add Solid("#a9863c") xzoom 0.135 yzoom 0.085 pos (0.73, 0.665) alpha 0.2
    if dct_dynped == True:
        text 'Темп сюжета как\nв предыдущих\nчастях':
            xpos 0.74
            ypos 0.68
            style "dct_menu_button"
            size 25
    else:
        text 'Оригинальное\nлитературное\nповествование':
            xpos 0.74
            ypos 0.68
            style "dct_menu_button"
            size 25
        
        
        
        
screen dct_menu_breaker:        # Экран сброса прогресса мода
    zorder 2
    
    imagemap:                           # Полностью пустая картинка. Сделана, чтобы пустые зоны вокруг диалогового окна отключали экран dct_menu_breaker
        ground im.Crop("mods/dublicate/Images/gui/reset/dct_menu_reset_empty.png",0,0,2,2)
        idle "mods/dublicate/Images/gui/reset/dct_menu_reset_empty.png"
        hover "mods/dublicate/Images/gui/reset/dct_menu_reset_empty.png"
        alpha False  # Прозрачные области изображения НЕ исключаются из активных зон
        hotspot(0,0,1920,1080) action Hide("dct_menu_breaker", transition=Dissolve(0.2))   # Возврат к оглавлению

    imagemap:                           # Тетрадный лист с текстом. Вынесен в отдельный imagemap, чтобы нажатие на него ни к чему не приводило
        ground im.Crop("mods/dublicate/Images/gui/reset/dct_menu_reset_empty.png",0,0,2,2)
        idle "mods/dublicate/Images/gui/reset/dct_menu_reset_ground.png"
        hover "mods/dublicate/Images/gui/reset/dct_menu_reset_ground.png"
        alpha True  # Прозрачные области изображения исключаются из активных зон
        hotspot(0,0,1920,1080) action Show("dct_menu_flower")   # Просто ссылаемся на веточку (которая и так есть на экране), чтобы ничего не происходило

    imagemap:                           # Диалоговое окно
        ground im.Crop("mods/dublicate/Images/gui/reset/dct_menu_reset_empty.png",0,0,2,2)
        auto "mods/dublicate/Images/gui/reset/dct_menu_reset_%s.png"
        alpha True  # Прозрачные области изображения исключаются из активных зон
        hotspot(552,645,360,198) action [                    # СБРОС ПРОГРЕССА МОДА!!!
            SetVariable("persistent.d_olga", 0),
            SetVariable("persistent.d_sim", 0),
            SetVariable("persistent.d_miuki", 0),
            SetVariable("persistent.d_prolog", 0),
            SetVariable("persistent.d_ana", 0),
            SetVariable("persistent.d_lin", 0),
            SetVariable("persistent.d_dra", 0),
            SetVariable("persistent.d_nam", 0),
            SetVariable("persistent.d_shif", 0),
            SetVariable("persistent.d_eff", 0),
            SetVariable("persistent.d_sim", 0),
            SetVariable("persistent.d_coin", 0),
            Hide("dct_menu_breaker", transition=Dissolve(0.2))
            ]
        hotspot(954,540,426,318) action Hide("dct_menu_breaker", transition=Dissolve(0.2))   # Возврат к оглавлению

    
    
screen dct_menu:
    add "mods/dublicate/images/gui/dct_bg_table.jpg"

    if (persistent.d_nam > 0) or (persistent.d_sim > 0) or (persistent.d_ana > 0) or (persistent.d_dra > 0) or (persistent.d_shif > 0) or (persistent.d_lin > 0) or (persistent.d_miuki > 0) or (persistent.d_eff > 0) or (persistent.d_olga > 0) or (persistent.d_coin > 0):
        imagemap:               # Кнопка "Выключатель"
            ground "mods/dublicate/images/gui/reset/dct_menu_breaker_idle.png"
            auto "mods/dublicate/images/gui/reset/dct_menu_breaker_%s.png"
            hotspot(0,0,1920,1080) action Show("dct_menu_breaker", transition=Dissolve(0.2))
    
    add "mods/dublicate/images/gui/dct_bg_menu.png"
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
    

    textbutton "Дубликат":   # Это просто заголовок. Функции кнопки у него нет
        xpos 0.648
        ypos 0.102
        style "dct_menu_button_exit"
        text_style "dct_menu_button_exit"
    
    textbutton "О - значит Ольга":
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
    
    textbutton "Сёмка, Сёмка, Сёмочка...":
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
    textbutton "Кошкин дом":
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
    
    textbutton "Пролог":
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
    textbutton "Анабасис":
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
    textbutton "Линия жизни":
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
    textbutton "Год дракона":
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
    textbutton "Имена в облаках":
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
    textbutton "Четвёртая смена":
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
    textbutton "Эффектор":
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
            

    # textbutton "Монетка в фонтане":
        # xpos 0.59
        # ypos 0.773
        # if (persistent.d_olga > 0) and (persistent.d_dra > 0):
            # if renpy.seen_label("dct_coin"):
                # style "dct_menu_button"
                # text_style "dct_menu_button"
            # else:
                # style "dct_menu_button_increase"
                # text_style "dct_menu_button_increase"
            # action [Hide("dct_menu", transition=Dissolve(0.2)), If(dct_dynped == True, true=Jump("dct_coin_dyn"), false=Jump("dct_coin_ped"))]
            # hovered ShowTransient("dct_menu_coin_sep", transition=Dissolve(0.2))
            # unhovered Hide("dct_menu_coin_sep", transition=Dissolve(0.2))
        # else:
            # style "dct_menu_button_unavailable"
            # text_style "dct_menu_button_unavailable"

    
    # if (persistent.d_olga > 0) and (persistent.d_dra > 0):  # Кнопка Динамичная/Педантичная (скрыта, до тех пора, пока не станет доступна Монетка в фонтане)
        # if dct_dynped == True:
            # textbutton "Динамичная\n{size=15}{k=-2.9}--------------------------------{/k}{/size}":         # Кнопка "Динамичная" (проявляется, когда значение переменной "dct_dynped" = True)
                # xpos 0.75
                # ypos 0.773
                # style "dct_menu_button_dynamic"
                # text_style "dct_menu_button_dynamic"
                # action [SetVariable("dct_dynped", False)]
                # hovered ShowTransient("dct_menu_coin_help", transition=Dissolve(0.2))
                # unhovered Hide("dct_menu_coin_help", transition=Dissolve(0.2))
        # else:
            # textbutton "Педантичная\n{size=15}{k=-2.7}----------------------------------{/k}{/size}":         # Кнопка "Педантичная" (проявляется, когда значение переменной "dct_dynped" = False)
                # xpos 0.75
                # ypos 0.773
                # style "dct_menu_button_pedantic"
                # text_style "dct_menu_button_pedantic"
                # action [SetVariable("dct_dynped", True)]
                # hovered ShowTransient("dct_menu_coin_help", transition=Dissolve(0.2))
                # unhovered Hide("dct_menu_coin_help", transition=Dissolve(0.2))
                
                
    textbutton "Монетка в фонтане":
        xpos 0.59
        ypos 0.773
        if (persistent.d_olga > 0) and (persistent.d_dra > 0):
            if renpy.seen_label("dct_coin"):
                style "dct_menu_button"
                text_style "dct_menu_button"
            else:
                style "dct_menu_button_increase"
                text_style "dct_menu_button_increase"
            action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_coin")]
            hovered ShowTransient("dct_menu_coin_sep", transition=Dissolve(0.2))
            unhovered Hide("dct_menu_coin_sep", transition=Dissolve(0.2))
        else:
            style "dct_menu_button_unavailable"
            text_style "dct_menu_button_unavailable"

        
    textbutton "Титры":
        xpos 0.565
        ypos 0.85
        style "dct_menu_button_exit"
        text_style "dct_menu_button_exit"
        action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_credits")]


    if (persistent.d_nam > 0) and (persistent.d_sim > 0) and (persistent.d_prolog > 0) and (persistent.d_ana > 0) and (persistent.d_dra > 0) and (persistent.d_shif > 0) and (persistent.d_lin > 0) and (persistent.d_miuki > 0) and (persistent.d_eff > 0) and (persistent.d_olga > 0) and (persistent.d_coin > 0):
        textbutton "Справочник":         # Кнопка СПРАВОЧНИК (скрыта, пока не прочитан весь мод)
            xpos 0.645
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
        
        
  
    imagebutton:            # Кнопка-штамп "Об авторе"
        pos (0.14, 0.82)
        auto "mods/dublicate/images/gui/dct_stamp_author_%s.png"
        action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_epitaph")]




##
##
##  Технические кнопки, нужны для тестирования. В рабочем билде должны быть отключены
##
##

    # textbutton "{space=65}Титры\n(финальные)":
        # xpos 0.37
        # ypos 0.85
        # style "dct_menu_button_exit"
        # text_style "dct_menu_button_exit"
        # action [Hide("dct_menu", transition=Dissolve(0.2)), Jump("dct_titles")]
        

    # if (persistent.d_ana == 0):
        # imagebutton:            # Кнопка "Проснуться" (несколько красных точек в левом верхнем углу папки). Делает мод полностью прочитанным
            # pos (0.19, 0.2)
            # idle "mods/dublicate/images/sprites/oth/red_stars.png"
            # hover "mods/dublicate/images/sprites/oth/red_stars.png"
            # action [
                # SetVariable("persistent.d_olga", 1),
                # SetVariable("persistent.d_sim", 1),
                # SetVariable("persistent.d_miuki", 1),
                # SetVariable("persistent.d_prolog", 1),
                # SetVariable("persistent.d_ana", 1),
                # SetVariable("persistent.d_lin", 1),
                # SetVariable("persistent.d_dra", 1),
                # SetVariable("persistent.d_nam", 1),
                # SetVariable("persistent.d_shif", 1),
                # SetVariable("persistent.d_eff", 1),
                # SetVariable("persistent.d_sim", 1),
                # SetVariable("persistent.d_coin", 1),
                # ]