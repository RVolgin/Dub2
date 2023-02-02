
# Монетка в фонтане - динамичная. Оптимизирована по лекалам остальных частей мода. Выкинуты описательные моменты, которые и без того переданы визуалом, а так же мелкие, не влияющие на сюжет подробности, тормозящие повествование чуть ли не на треть. Мы постарались адаптировать текст под формат мода, так же, как это делал Тангейзер.

label dct_coin_dyn:
    scene black
    stop ambience
    play music music_list['reminiscences']
    show headline_text u"Монетка в фонтане" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
    
    call dct_sixhour_dyn
    
    call dct_transitions_dyn
    
    call dct_fluctuation_dyn
    
    call dct_disposition_dyn
    
    call dct_debut_dyn
    
    call dct_d7_d5_dyn
    
    call dct_foreign_land_dyn
    
    call dct_replacement_dyn
    
    call dct_system_errors_dyn
    
    call dct_dreamreality_dyn
    
    call dct_horizontal_transport_dyn
    
    call dct_coin_final_dyn
    
return