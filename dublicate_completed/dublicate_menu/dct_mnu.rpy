label dct_mnu2:
    $ prolog_time()
    scene black
    call screen dct_menu
#Техническое меню
#Пока так, но однозначно в переделку.
menu:
    "Оглавление"
    "Сёмка, Сёмка, Сёмочка..." if persistent.d_nam > 0:
        jump dct_simon
    "Пролог":
        jump dct_prologue
    "Анабасис" if persistent.d_prolog > 0:
        jump dct_anabasis
    "Год дракона" if persistent.d_ana > 0:
        jump dct_dragon
    "Имена в облаках" if persistent.d_ana > 0:
        jump dct_clouds
    "Четвертая смена" if persistent.d_nam > 0:
        jump dct_4th_shift
    "Линия жизни" if (persistent.d_shif > 0 and persistent.d_dra > 0):
        jump dct_life_line
    "Кошкин дом" if (persistent.d_shif > 0 and persistent.d_sim > 0):
        jump dct_cat_house
    "Эффектор" if persistent.d_shif > 0:
        jump dct_effector
    "О — значит Ольга" if (persistent.d_nam > 0 and persistent.d_sim > 0 and persistent.d_prolog > 0 and persistent.d_ana > 0 and persistent.d_dra > 0 and persistent.d_shif > 0 and persistent.d_lin > 0 and persistent.d_miuki > 0 and persistent.d_eff > 0):
        jump dct_olga
    "Монетка в фонтане" if persistent.d_eff > 0:
        jump dct_coin
    "Выход":
        jump dct_exit