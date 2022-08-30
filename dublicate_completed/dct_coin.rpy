label dct_coin:       #вступительный лейбл
    scene black
    stop ambience
    play music music_list['reminiscences']
    show headline_text u"Монетка в фонтане" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
    
    call dct_sixhour
    
    call dct_transitions
    
    #call dct_fluctuation
    
    #call dct_disposition
    
    #call dct_debut
    
    call dct_d7_d5
    
    call dct_foreign_land
    
    call dct_replacement
    
    #call dct_system_errors
    
    call dct_dreamreality
    
    #call dct_horizontal_transport
    
    call dct_coin_final
    
return
