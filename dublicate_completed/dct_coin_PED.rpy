
# Монетка в фонтане - педантичная. Тождественна версии из фанфика. Неторопливое литературное повествование со всеми, даже незначительными подробностями.

label dct_coin_ped:
    scene black
    stop ambience
    play music music_list['reminiscences']
    show headline_text u"Монетка в фонтане" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
    
    call dct_sixhour_ped
    
    call dct_transitions_ped
    
    call dct_fluctuation_ped
    
    call dct_disposition_ped
    
    call dct_debut_ped
    
    call dct_d7_d5_ped
    
    call dct_foreign_land_ped
    
    call dct_replacement_ped
    
    call dct_system_errors_ped
    
    call dct_dreamreality_ped
    
    call dct_horizontal_transport_ped
    
    call dct_coin_final_ped
    
return