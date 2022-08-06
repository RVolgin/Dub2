init :
    $ mods ["dublicate_ending"]=u"Дубликат [[окончание]"
    
    $ dct_ending_var = False

label dublicate_ending:

    $ dct_ending_var = True
    
    stop ambience
    stop music
    stop sound
    stop sound_loop
    
    show headline_text2 u"{color=#f1d27d}Дубликат: окончание\n   {size=60}Две завершающих книги{/size}{/color}" at truecenter with dspr
    $ renpy.pause(5.0)
    hide headline_text with dissolve
    
    call dct_olga

    call dct_coin
    
    call dct_spravochnik
    
