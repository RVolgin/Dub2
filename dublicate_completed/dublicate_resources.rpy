init :
    $ config.developer = True
    $ config.autoreload = False
    $ mods ["dublicate_completed"]=u"Дубликат COMPLETED"
    
        
        #Заголовки частей и глав.
    image headline_text = ParameterizedText(color="#14ab14", font="mods/dublicate_completed/fonts/TrixieProHeavy_Regular.otf", size=192)
    image headline_text2 = ParameterizedText(color="#14ab14", font="mods/dublicate_completed/fonts/TrixieProHeavy_Regular.otf", size=96)
    
    image poem_text = ParameterizedText(color="#ffffff", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000000", size=48)
    
    image promo_text = ParameterizedText (color="#4c4c4c", font="mods/dublicate_completed/fonts/bezpr.ttf", size=48)
    image promo_text2 = ParameterizedText (color ="#ff0000", font="mods/dublicate_completed/fonts/bezpr.ttf", size=128)
    image promo_text_un = ParameterizedText (color="#b956ff", font="mods/dublicate_completed/fonts/TrixieProHeavy_Regular.otf", size=48)
    image promo_text_dv = ParameterizedText (color="#f18816", font="mods/dublicate_completed/fonts/TrixieProHeavy_Regular.otf", size=48)
    
    #Спрайты, БГ и ЦГ: оригинальные и переобъявленные из БЛ и модов. Почему-то половина оригинальной графики отказалась работать. Пришлось переобъявлять.
    
    #bg
    
    image dct_altar = "mods/dublicate_completed/images/bg/dct_altar.jpg"
    image dct_buswindov_rain = "mods/dublicate_completed/images/bg/dct_buswindov_rain.jpg"
    image dct_ext_410bus = "mods/dublicate_completed/images/bg/dct_ext_410bus.jpg"
    image dct_ext_aidpost_night_with_light = "mods/dublicate_completed/images/bg/dct_ext_aidpost_night_with_light.jpg"
    image dct_ext_backdoor_day_7dl = "mods/dublicate_completed/images/bg/dct_ext_backdoor_day_7dl.jpg"
    image dct_ext_backdoor_day_7dl_zoom = "mods/dublicate_completed/images/bg/dct_ext_backdoor_day_7dl_zoom.jpg"
    image dct_ext_backroad_day_7 = "mods/dublicate_completed/images/bg/dct_ext_backroad_day_7.jpg"
    image dct_ext_backroad_light_7 = "mods/dublicate_completed/images/bg/dct_ext_backroad_light_7.jpg"
    image dct_ext_backroad_night_7 = "mods/dublicate_completed/images/bg/dct_ext_backroad_night_7.jpg"
    image dct_ext_backroad_sunset_7 = "mods/dublicate_completed/images/bg/dct_ext_backroad_sunset_7.jpg"
    image dct_ext_bathhouse_day = "mods/dublicate_completed/images/bg/dct_ext_bathhouse_day.jpg"
    image dct_ext_beach_day_with_pass_train = "mods/dublicate_completed/images/bg/dct_ext_beach_day_with_pass_train.jpg"
    image dct_ext_beach_night_with_pass_train = "mods/dublicate_completed/images/bg/dct_ext_beach_night_with_pass_train.jpg"
    image dct_ext_beach_sunset_not_train = "mods/dublicate_completed/images/bg/dct_ext_beach_sunset_not_train.jpg"
    image dct_ext_boathouse_day_with_pass_train = "mods/dublicate_completed/images/bg/dct_ext_boathouse_day_with_pass_train.jpg"
    image dct_ext_boathouse_night_with_pass_train = "mods/dublicate_completed/images/bg/dct_ext_boathouse_night_with_pass_train.jpg"
    image dct_ext_boathouse_sunset = "mods/dublicate_completed/images/bg/dct_ext_boathouse_sunset.jpg"
    image dct_ext_boat = "mods/dublicate_completed/images/bg/dct_ext_boat.jpg"
    image dct_ext_boathouse_alt_day_7dl = "mods/dublicate_completed/images/bg/dct_ext_boathouse_alt_day_7dl.jpg"
    image dct_ext_boathouse_alt_day_7dl_night = "mods/dublicate_completed/images/bg/dct_ext_boathouse_alt_day_7dl_night.jpg"
    image dct_ext_busstop_summer = "mods/dublicate_completed/images/bg/dct_ext_busstop_summer.jpg"
    image dct_ext_buses = "mods/dublicate_completed/images/bg/dct_ext_buses.jpg"    # Остановка с Икаркусом и ЛАЗом
    image dct_ext_bulletin_board = "mods/dublicate_completed/images/bg/dct_ext_bulletin_board.jpg"
    image dct_ext_camp_entrance_sunset = "mods/dublicate_completed/images/bg/dct_ext_camp_entrance_sunset.jpg"
    image dct_ext_city_scuare_sunset = "mods/dublicate_completed/images/bg/dct_ext_city_scuare_sunset.jpg"
    image dct_ext_clubs_sunset = "mods/dublicate_completed/images/bg/dct_ext_clubs_sunset.jpg"
    image dct_ext_cliff_day = "mods/dublicate_completed/images/bg/dct_ext_cliff_day.jpg"
    image dct_ext_cliff_day_zoom = "mods/dublicate_completed/images/bg/dct_ext_cliff_day_zoom.jpg"
    image dct_ext_cliff_day_cloudy = "mods/dublicate_completed/images/bg/dct_ext_cliff_day_cloudy.jpg"
    image dct_ext_cliff_night = "mods/dublicate_completed/images/bg/dct_ext_cliff_night.jpg"
    image dct_ext_cliff_sunset = "mods/dublicate_completed/images/bg/dct_ext_cliff_sunset.jpg"
    image dct_ext_dining_hall_near_sunset = "mods/dublicate_completed/images/bg/dct_ext_dining_hall_near_sunset.jpg"
    image dct_ext_dinning_hall_rain_night = "mods/dublicate_completed/images/bg/dct_ext_dinning_hall_rain_night.jpg"
    image d_ext_dv_hideout_day_7 = "mods/dublicate_completed/images/bg/d_ext_dv_hideout_day_7.jpg"
    image d_ext_dv_hideout_sunset = "mods/dublicate_completed/images/bg/d_ext_dv_hideout_sunset.jpg"
    image dct_ext_gate_entrance_sunset = "mods/dublicate_completed/images/bg/dct_ext_gate_entrance_sunset.jpg"
    image dct_ext_gate_entrance_day = "mods/dublicate_completed/images/bg/dct_ext_gate_entrance_day.jpg"
    image dct_ext_gate_entrance_sim = "mods/dublicate_completed/images/bg/dct_ext_gate_entrance_sim.jpg"
    image dct_ext_hangar_day = "mods/dublicate_completed/images/bg/dct_ext_hangar_day.jpg"
    image dct_ext_hangar_night = "mods/dublicate_completed/images/bg/dct_ext_hangar_night.jpg"
    image dct_ext_hangar_sunset = "mods/dublicate_completed/images/bg/dct_ext_hangar_sunset.jpg"
    image dct_ext_house_of_dv_sunset = "mods/dublicate_completed/images/bg/dct_ext_house_of_dv_sunset.jpg"
    image dct_ext_house_of_kids_day = "mods/dublicate_completed/images/bg/dct_ext_house_of_kids_day.jpg"
    image dct_ext_house_of_sl_night = "mods/dublicate_completed/images/bg/dct_ext_house_of_sl_night.jpg"
    image dct_ext_house_of_un_night = "mods/dublicate_completed/images/bg/dct_ext_house_of_un_night.jpg"
    image dct_ext_house_of_un_sunset = "mods/dublicate_completed/images/bg/dct_ext_house_of_un_sunset.jpg"
    image dct_ext_houses_night = "mods/dublicate_completed/images/bg/dct_ext_houses_night.jpg"
    image dct_ext_island_reverse_day = "mods/dublicate_completed/images/bg/dct_ext_island_reverse_day.jpg"
    image dct_ext_island_reverse_night = "mods/dublicate_completed/images/bg/dct_ext_island_reverse_night.jpg"
    image dct_ext_island_reverse_sunset = "mods/dublicate_completed/images/bg/dct_ext_island_reverse_sunset.jpg"
    image dct_ext_island_sunset = "mods/dublicate_completed/images/bg/dct_ext_island_sunset.jpg"
    image dct_ext_kpp2 = "mods/dublicate_completed/images/bg/dct_ext_kpp2.jpg"
    image dct_ext_kpp3 = "mods/dublicate_completed/images/bg/dct_ext_kpp3.jpg"
    image dct_ext_kpp5 = "mods/dublicate_completed/images/bg/dct_ext_kpp5.jpg"
    image dct_ext_lake_day = "mods/dublicate_completed/images/bg/dct_ext_lake_day.jpg"
    image dct_ext_lake_night = "mods/dublicate_completed/images/bg/dct_ext_lake_night.jpg"
    image dct_ext_lake_sunset = "mods/dublicate_completed/images/bg/dct_ext_lake_sunset.jpg"
    image dct_ext_library_night_with_light = "mods/dublicate_completed/images/bg/dct_ext_library_night_with_light.jpg"
    image dct_ext_module_day = "mods/dublicate_completed/images/bg/dct_ext_module_day.jpg"
    image dct_ext_module_night = "mods/dublicate_completed/images/bg/dct_ext_module_night.jpg"
    image dct_ext_module_smoking_place = "mods/dublicate_completed/images/bg/dct_ext_module_smoking_place.jpg"
    image dct_ext_module_smoking_place2 = "mods/dublicate_completed/images/bg/dct_ext_module_smoking_place2.jpg"
    image dct_ext_module_smoking_place2_sunset = "mods/dublicate_completed/images/bg/dct_ext_module_smoking_place2_sunset.jpg"
    image dct_ext_musclub_night = "mods/dublicate_completed/images/bg/dct_ext_musclub_night.jpg"
    image dct_ext_no_bus_night = "mods/dublicate_completed/images/bg/dct_ext_no_bus_night.jpg"
    image dct_ext_no_bus_white_fog_night = "mods/dublicate_completed/images/bg/dct_ext_no_bus_white_fog_night.jpg"
    image dct_ext_no_bus_pink_fog_night = "mods/dublicate_completed/images/bg/dct_ext_no_bus_pink_fog_night.jpg"
    image dct_ext_old_building_day = "mods/dublicate_completed/images/bg/dct_ext_old_building_day.jpg"
    image dct_ext_old_building_sunset = "mods/dublicate_completed/images/bg/dct_ext_old_building_sunset.jpg"
    image dct_ext_path2_sunset = "mods/dublicate_completed/images/bg/dct_ext_path2_sunset.jpg"
    image dct_ext_playground_sunset = "mods/dublicate_completed/images/bg/dct_ext_playground_sunset.jpg"
    image dct_ext_pyramid = "mods/dublicate_completed/images/bg/dct_ext_pyramid.jpg"
    image dct_ext_pass_train_zoom = "mods/dublicate_completed/images/bg/dct_ext_pass_train_zoom.jpg"
    image dct_ext_railway = "mods/dublicate_completed/images/bg/dct_ext_railway.jpg"
    image dct_ext_railway_night = "mods/dublicate_completed/images/bg/dct_ext_railway_night.jpg"
    image dct_ext_railway_gr_bl = "mods/dublicate_completed/images/bg/dct_ext_railway_gr_bl.jpg"
    image dct_ext_railway_without_rail = "mods/dublicate_completed/images/bg/dct_ext_railway_without_rail.jpg"
    image dct_ext_residential_block_day = "mods/dublicate_completed/images/bg/dct_ext_residential_block_day.jpg"
    image dct_ext_residential_block_night = "mods/dublicate_completed/images/bg/dct_ext_residential_block_night.jpg"
    image dct_ext_residential_block_sunset = "mods/dublicate_completed/images/bg/dct_ext_residential_block_sunset.jpg"
    image dct_ext_square_day = "mods/dublicate_completed/images/bg/dct_ext_square_day.jpg" #Площадь в 4й смене
    image dct_ext_warehouse2_day_7 = "mods/dublicate_completed/images/bg/dct_ext_warehouse2_day_7.jpg"
    image dct_ext_washstand_sunset = "mods/dublicate_completed/images/bg/dct_ext_washstand_sunset.jpg"
    image dct_ext_washstand_night = "mods/dublicate_completed/images/bg/dct_ext_washstand_night.jpg"
    image dct_ext_washstand2_night = "mods/dublicate_completed/images/bg/dct_ext_washstand2_night.jpg" #питьевой фонтанчик
    image dct_int_sporthall = "mods/dublicate_completed/images/bg/dct_int_sporthall.jpg" #спортзал из 7ДЛ
    image dct_ext_square_day_gate = "mods/dublicate_completed/images/bg/dct_ext_square_day_gate.jpg" #Поселок Шлюз - площадь. Заказать, а пока так.
    image dct_ext_stage_big_day = "mods/dublicate_completed/images/bg/dct_ext_stage_big_day.jpg"
    image dct_ext_stage_big_sunset = "mods/dublicate_completed/images/bg/dct_ext_stage_big_sunset.jpg"
    image dct_ext_storage_day = "mods/dublicate_completed/images/bg/dct_ext_storage_day.png"
    image dct_ext_switchman_house_day = "mods/dublicate_completed/images/bg/dct_ext_switchman_house_day.jpg" #Домик стрелочника
    image dct_ext_switchman_house_night = "mods/dublicate_completed/images/bg/dct_ext_switchman_house_night.jpg" #Домик стрелочника
    image dct_ext_switchman_house_sunset = "mods/dublicate_completed/images/bg/dct_ext_switchman_house_sunset.jpg"
    image dct_ext_train_day = "mods/dublicate_completed/images/bg/dct_ext_train_day.jpg"
    image dct_ext_train_day_overcast = "mods/dublicate_completed/images/bg/dct_ext_train_day_overcast.jpg"
    image dct_ext_train_day_overcast_not_train = "mods/dublicate_completed/images/bg/dct_ext_train_day_overcast_not_train.jpg"
    image dct_ext_water_day = "mods/dublicate_completed/images/bg/dct_ext_water_day.jpg"
    image dct_ext_well_sunset = "mods/dublicate_completed/images/bg/dct_ext_well_sunset.jpg"
    image dct_int_410bus_night = "mods/dublicate_completed/images/bg/dct_int_410bus_night.jpg" #410 зима салон
    image dct_int_access_7 = "mods/dublicate_completed/images/bg/dct_int_access_7.jpg"
    image dct_int_aidpost_sunset = "mods/dublicate_completed/images/bg/dct_int_aidpost_sunset.jpg"
    image dct_int_barracks_night = "mods/dublicate_completed/images/bg/dct_int_barracks_night.jpg"
    image dct_int_briefing_room = "mods/dublicate_completed/images/bg/dct_int_briefing_room.jpg"
    image dct_int_bus_sunset1 = "mods/dublicate_completed/images/bg/dct_int_bus_sunset1.jpg"
    image dct_int_bus_rain = "mods/dublicate_completed/images/bg/dct_int_bus_rain.jpg"
    image dct_int_bus_people_day = "mods/dublicate_completed/images/bg/dct_int_bus_people_day.jpg"
    image dct_int_cabin = "mods/dublicate_completed/images/bg/dct_int_cabin.jpg"
    image dct_int_cabinet_day = "mods/dublicate_completed/images/bg/dct_int_cabinet_day.jpg"
    image dct_int_cafe = "mods/dublicate_completed/images/bg/dct_int_cafe.jpg"
    image dct_int_cafe_sunset_rain = "mods/dublicate_completed/images/bg/dct_int_cafe_sunset_rain.jpg"
    image dct_int_chief_corridor_day = "mods/dublicate_completed/images/bg/dct_int_chief_corridor_day.jpg"
    image dct_int_chief_office_night = "mods/dublicate_completed/images/bg/dct_int_chief_office_night.jpg"
    image dct_int_coaching_room = "mods/dublicate_completed/images/bg/dct_int_coaching_room.jpg" #тренерская
    image dct_int_coaching_room2 = "mods/dublicate_completed/images/bg/dct_int_coaching_room2.jpg"
    image dct_int_coaching_room3 = "mods/dublicate_completed/images/bg/dct_int_coaching_room3.jpg"
    image dct_int_coaching_room2_night = "mods/dublicate_completed/images/bg/dct_int_coaching_room2_night.jpg"
    image dct_int_coaching_room3_night = "mods/dublicate_completed/images/bg/dct_int_coaching_room3_night.jpg"
    image dct_int_clubs_male_day_wrecked = "mods/dublicate_completed/images/bg/dct_int_clubs_male_day_wrecked.jpg"
    image dct_int_corridor2 = "mods/dublicate_completed/images/bg/dct_int_corridor2.jpg" #корридор к кассам.
    image dct_int_datacenter = "mods/dublicate_completed/images/bg/dct_int_datacenter.jpg"
    image dct_int_dining_hall_day_siluette = "mods/dublicate_completed/images/bg/dct_int_dining_hall_day_siluette.jpg"
    image dct_int_house_of_kids_fog = "mods/dublicate_completed/images/bg/dct_int_house_of_kids_fog.jpg"
    image dct_int_house_of_kids = "mods/dublicate_completed/images/bg/dct_int_house_of_kids.jpg"
    image d_int_house_of_dv_night_without_light = "mods/dublicate_completed/images/bg/d_int_house_of_dv_night_without_light.jpg"
    image dct_int_house_of_sl_night = "mods/dublicate_completed/images/bg/dct_int_house_of_sl_night.jpg"
    image dct_int_house_of_sl_sunset = "mods/dublicate_completed/images/bg/dct_int_house_of_sl_sunset.jpg"
    image dct_int_house_of_un_sunset = "mods/dublicate_completed/images/bg/dct_int_house_of_un_sunset.jpg"
    image dct_int_mine_coalface_dark = "mods/dublicate_completed/images/bg/dct_int_mine_coalface_dark.jpg"
    image dct_int_residential_block_day = "mods/dublicate_completed/images/bg/dct_int_residential_block_day.jpg"
    image dct_int_residential_block_night = "mods/dublicate_completed/images/bg/dct_int_residential_block_night.jpg"
    image dct_int_residential_block2_sunset = "mods/dublicate_completed/images/bg/dct_int_residential_block2_sunset.jpg"
    image dct_int_room_of_us_day = "mods/dublicate_completed/images/bg/dct_int_room_of_us_day.jpg"
    image dct_int_room_of_us_day_2 = "mods/dublicate_completed/images/bg/dct_int_room_of_us_day_2.jpg"
    image dct_int_shop = "mods/dublicate_completed/images/bg/dct_int_shop.jpg"
    image dct_int_shop_entrance = "mods/dublicate_completed/images/bg/dct_int_shop_entrance.jpg"
    image dct_int_shower = "mods/dublicate_completed/images/bg/dct_int_shower.jpg"
    image dct_int_switchman_house_day = "mods/dublicate_completed/images/bg/dct_int_switchman_house_day.jpg"
    image dct_int_switchman_house_day_bed = "mods/dublicate_completed/images/bg/dct_int_switchman_house_day_bed.jpg"
    image dct_int_switchman_house_night_bed = "mods/dublicate_completed/images/bg/dct_int_switchman_house_night_bed.jpg"
    image dct_int_switchman_house_night_candle = "mods/dublicate_completed/images/bg/dct_int_switchman_house_night_candle.jpg"
    image dct_int_switchman_house_night_candle_bed = "mods/dublicate_completed/images/bg/dct_int_switchman_house_night_candle_bed.jpg"
    image dct_int_switchman_house_sunset = "mods/dublicate_completed/images/bg/dct_int_switchman_house_sunset.jpg"
    image dct_intro_xx = "mods/dublicate_completed/images/bg/dct_intro_xx.jpg"
    image dct_int_chief_corridor_night = "mods/dublicate_completed/images/bg/dct_int_chief_corridor_night.jpg"
    image dct_int_library_cellar = "mods/dublicate_completed/images/bg/dct_int_library_cellar.jpg"
    image dct_int_liaz_day_rain = "mods/dublicate_completed/images/bg/dct_int_liaz_day_rain.jpg"
    image dct_int_loft_day = "mods/dublicate_completed/images/bg/dct_int_loft_day.jpg"
    image dct_int_mine_room = "mods/dublicate_completed/images/bg/dct_int_mine_room.jpg"
    image dct_int_mine_exit_day = "mods/dublicate_completed/images/bg/dct_int_mine_exit_day.jpg"
    image dct_int_mp_room = "mods/dublicate_completed/images/bg/dct_int_mp_room.jpg"
    image dct_int_old_building_day = "mods/dublicate_completed/images/bg/dct_int_old_building_day.jpg"
    image dct_int_old_building_sunset = "mods/dublicate_completed/images/bg/dct_int_old_building_sunset.jpg"
    image dct_int_train_day = "mods/dublicate_completed/images/bg/dct_int_train_day.jpg"
    image dct_int_train_day_dark = "mods/dublicate_completed/images/bg/dct_int_train_day_dark.jpg"
    image dct_int_tonnel = "mods/dublicate_completed/images/bg/dct_int_tonnel.jpg"
    image dct_semen_room = "mods/dublicate_completed/images/bg/dct_semen_room.jpg"
    image dct_storeroom_day = "mods/dublicate_completed/images/bg/dct_storeroom_day.jpg"
    image dct_storeroom_night = "mods/dublicate_completed/images/bg/dct_storeroom_night.jpg"
    image dct_storeroom_night2 = "mods/dublicate_completed/images/bg/dct_storeroom_night2.jpg"
    image dct_int_warehouse_day = "mods/dublicate_completed/images/bg/dct_int_warehouse_day.jpg"
    image dct_int_hospital_transparent = "mods/dublicate_completed/images/bg/dct_int_hospital_transparent.png"
    image dct_int_hospital_transparent2 = "mods/dublicate_completed/images/bg/dct_int_hospital_transparent2.png"
    image dct_landscape_city1 = "mods/dublicate_completed/images/bg/dct_landscape_city1.jpg"
    image dct_landscape_city1_day = "mods/dublicate_completed/images/bg/dct_landscape_city1_day.jpg"
    image dct_landscape_forest1 = "mods/dublicate_completed/images/bg/dct_landscape_forest1.jpg"
    image dct_landscape_forest3 = "mods/dublicate_completed/images/bg/dct_landscape_forest3.jpg"
    image dct_landscape_forest3_overcast_1 = "mods/dublicate_completed/images/bg/dct_landscape_forest3_overcast_1.jpg"
    image dct_landscape_forest3_overcast_2 = "mods/dublicate_completed/images/bg/dct_landscape_forest3_overcast_2.jpg"
    
    
    image dct_bank_from_water_side = "mods/dublicate_completed/images/bg/dct_bank_from_water_side.jpg"    # Вид на лодочную станцию и берег со стороны воды
    image dct_railway_embankment_day = "mods/dublicate_completed/images/bg/dct_railway_embankment_day.jpg"  # Берег возле железнодорожной насыпи ДЕНЬ
    image dct_railway_embankment_overcast = "mods/dublicate_completed/images/bg/dct_railway_embankment_overcast.jpg"    # Берег возле железнодорожной насыпи ПАСМУРНО
    
        
    ##### bg (coin)
    
    image dct_clubs_male_comp_day = "mods/dublicate_completed/images/bg/coin01/dct_clubs_male_comp_day.jpg"     # Рабочий стол с компом в клубе кибертнетиков
    image dct_clubs_male_comp_night = "mods/dublicate_completed/images/bg/coin01/dct_clubs_male_comp_night.jpg"
    image dct_clubs_male_comp_night_light_mon = "mods/dublicate_completed/images/bg/coin01/dct_clubs_male_comp_night_light_mon.jpg"
    image dct_clubs_male_comp_sunset = "mods/dublicate_completed/images/bg/coin01/dct_clubs_male_comp_sunset.jpg"
    image dct_ext_clubs_night_light_inside = "mods/dublicate_completed/images/bg/coin01/dct_ext_clubs_night_light_inside.jpg" # Здание клуба кибернетиков ночью со светящимися окнами
    image dct_ext_buses_filled = "mods/dublicate_completed/images/bg/coin01/dct_ext_buses_filled.jpg"       # Икарус и ЛАЗ на стоянке, в Икарусе сидят люди
    image dct_ext_house_of_el_day = "mods/dublicate_completed/images/bg/coin01/dct_ext_house_of_el_day.jpg"     # Домик кибернетиков ЭКСТЕРЬЕР
    image dct_ext_house_of_el_night = "mods/dublicate_completed/images/bg/coin01/dct_ext_house_of_el_night.jpg"
    image dct_ext_house_of_el_sunset = "mods/dublicate_completed/images/bg/coin01/dct_ext_house_of_el_sunset.jpg"
    image dct_ext_library_sunset = "mods/dublicate_completed/images/bg/coin01/dct_ext_library_sunset.jpg"
    image dct_int_bus_middle = "mods/dublicate_completed/images/bg/coin01/dct_int_bus_middle.jpg"   # Салон автобуса, левый борт
    image dct_int_bus_another_middle = "mods/dublicate_completed/images/bg/coin01/dct_int_bus_another_middle.jpg"   # Салон автобуса, правый борт
    image dct_int_bus_people = "mods/dublicate_completed/images/bg/coin01/dct_int_bus_people.jpg"   # Салон автобуса, видоизменённая передняя площадка
    image dct_int_bus_stern = "mods/dublicate_completed/images/bg/coin01/dct_int_bus_stern.jpg"     # Салон автобуса, задняя площадка
    image dct_ext_camp_entrance_night = "mods/dublicate_completed/images/bg/coin01/dct_ext_camp_entrance_night.jpg" # Вид на клуб и на ворота лагеря ночью
    image dct_int_clubs_male_night = "mods/dublicate_completed/images/bg/coin01/dct_int_clubs_male_night.jpg"   # Внутри клуба ночью
    image dct_int_clubs_male_night_light = "mods/dublicate_completed/images/bg/coin01/dct_int_clubs_male_night_light.jpg"
    image dct_int_clubs_male_night_light_mon = "mods/dublicate_completed/images/bg/coin01/dct_int_clubs_male_night_light_mon.jpg"
    image dct_int_house_of_el_day = "mods/dublicate_completed/images/bg/coin01/dct_int_house_of_el_day.jpg"     # Домик кибернетиков ИНТЕРЬЕР
    image dct_int_house_of_el_night = "mods/dublicate_completed/images/bg/coin01/dct_int_house_of_el_night.jpg"
    image dct_int_house_of_el_night_light = "mods/dublicate_completed/images/bg/coin01/dct_int_house_of_el_night_light.jpg"
    image dct_int_house_of_el_sunset = "mods/dublicate_completed/images/bg/coin01/dct_int_house_of_el_sunset.jpg"
    
    
    
    image dct_dream_sh_first_disert = "mods/dublicate_completed/images/bg/coin02/dct_dream_sh_first_disert.jpg"
    image dct_int_library_standing_desk_back = "mods/dublicate_completed/images/bg/coin02/dct_int_library_standing_desk_back.jpg"   # Бибилотека, вид из-за Жениного стола
    image dct_int_library_standing_desk_front = "mods/dublicate_completed/images/bg/coin02/dct_int_library_standing_desk_front.png"
    image dct_ext_musclub_backside_night = "mods/dublicate_completed/images/bg/coin02/dct_ext_musclub_backside_night.jpg"   # Музыкальный клуб с тыльной стороны ночью
    image dct_ext_musclub_backside_night_brightwindows = "mods/dublicate_completed/images/bg/coin02/dct_ext_musclub_backside_night_brightwindows.jpg"   # Музыкальный клуб с тыльной стороны ночью со светящимися окнами
    image dct_ext_dining_bench_day = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_bench_day.png"       # Скамейка у входа в столовую, ДЕНЬ
    image dct_ext_dining_bench_day_front = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_bench_day_front.png"   # Скамейка у входа в столовую (только скамейка, столб и угол здания)
    image dct_ext_dining_bench_sunset = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_bench_sunset.png" # Скамейка у входа в столовую, ЗАКАТ
    image dct_ext_dining_door_day = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_door_day.jpg"         # Двери столовой, ДЕНЬ
    image dct_ext_dining_door_day_front = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_door_day_front.png" # Двери столовой (только лавка и ограждение)
    image dct_ext_dining_door_sunset = "mods/dublicate_completed/images/bg/coin02/dct_ext_dining_door_sunset.jpg"   # Двери столовой, ЗАКАТ
    image dct_int_dining_hall_table_day_back = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_day_back.jpg"   # Обеденный стол, ДЕНЬ
    image dct_int_dining_hall_table_day_back_people = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_day_back_people.jpg"
    image dct_int_dining_hall_table_day_chairs = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_day_chairs.png"
    image dct_int_dining_hall_table_day_front = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_day_front.png"
    image dct_int_dining_hall_table_sunset_back = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_sunset_back.jpg" # Обеденный стол, ЗАКАТ
    image dct_int_dining_hall_table_sunset_back_people = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_sunset_back_people.jpg"
    image dct_int_dining_hall_table_sunset_chairs = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_sunset_chairs.png"
    image dct_int_dining_hall_table_sunset_front = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_table_sunset_front.png"
    image dct_ext_сentral_alley_from_dining_hall_to_west = "mods/dublicate_completed/images/bg/coin02/dct_ext_сentral_alley_from_dining_hall_to_west.jpg" # Главная аллея лагеря от столовой с видом на западные ворота
    image dct_ext_playground_opposite_gate_day = "mods/dublicate_completed/images/bg/coin02/dct_ext_playground_opposite_gate_day.jpg"
    image dct_int_dining_hall_people_sunset = "mods/dublicate_completed/images/bg/coin02/dct_int_dining_hall_people_sunset.jpg"
    image dct_ext_music_club_sunset = "mods/dublicate_completed/images/bg/coin02/dct_ext_music_club_sunset.jpg"
    
    
    
    image dct_ext_beach_night_view_from_gym = "mods/dublicate_completed/images/bg/coin06/dct_ext_beach_night_view_from_gym.jpg" # Пляж ночью, вид с крыльца спортзала
    image dct_ext_stage_close_day = "mods/dublicate_completed/images/bg/coin06/dct_ext_stage_close_day.jpg" # Сцена днём, приближенная
    image dct_ext_stage_edge_day = "mods/dublicate_completed/images/bg/coin06/dct_ext_stage_edge_day.jpg" # Сцена, самый край возле колонки
    image dct_ext_square_profile_view_day = "mods/dublicate_completed/images/bg/coin06/dct_ext_square_profile_view_day.jpg" # Площадь с боку днём, вид на Генду и админ. корпус
    image dct_ext_alley_from_library_to_square = "mods/dublicate_completed/images/bg/coin06/dct_ext_alley_from_library_to_square.jpg" # Аллея от бибилиотеки к площади
    image dct_int_clubs_male2_night_zoom = "mods/dublicate_completed/images/bg/coin06/dct_int_clubs_male2_night_zoom.jpg" # Кладовка кибернетиков (левая половина) в двукратном зуме
    image dct_ext_beach_barhan = "mods/dublicate_completed/images/bg/coin06/dct_ext_beach_barhan.jpg" # Пляж с тентом-зонтиком днём
    image dct_ext_beach_day_lifesaving_shield = "mods/dublicate_completed/images/bg/coin06/dct_ext_beach_day_lifesaving_shield.jpg" # Пляж со щитом средств для спасения утопающих
    
    
    
    image dct_ext_forest_dark_night = "mods/dublicate_completed/images/bg/coin07/dct_ext_forest_dark_night.jpg" # "Дремучий лес" (Шурик пробирается по лагерю)
    image dct_int_musclub_night_light = "mods/dublicate_completed/images/bg/coin07/dct_int_musclub_night_light.jpg" # Музклуб внутри (ночь, свет включён)
    image dct_int_musclub_night_nolight = "mods/dublicate_completed/images/bg/coin07/dct_int_musclub_night_nolight.jpg" # Музклуб внутри (ночь, свет выключён)
    image dct_ext_music_club_verandah_night = "mods/dublicate_completed/images/bg/coin07/dct_ext_music_club_verandah_night.jpg" # Музклуб, веранда (ночь, свет не горит)
    
    
    
    image dct_ext_aidpost_after_rain = "mods/dublicate_completed/images/bg/coin08/dct_ext_aidpost_after_rain.jpg" # Медпункт после дождя
    image dct_ext_dining_hall_away_after_rain = "mods/dublicate_completed/images/bg/coin08/dct_ext_dining_hall_away_after_rain.jpg" # Столовая вдали после дождя
    image dct_ext_square_after_rain = "mods/dublicate_completed/images/bg/coin08/dct_ext_square_after_rain.jpg" # Площадь после дождя
    image dct_ext_сentral_alley_from_dining_hall_to_west_after_rain = "mods/dublicate_completed/images/bg/coin08/dct_ext_сentral_alley_from_dining_hall_to_west_after_rain.jpg" # Аллея от столовой до западных ворот после дождя
    image dct_ext_clubs_rain = "mods/dublicate_completed/images/bg/coin08/dct_ext_clubs_rain.jpg" # Клуб кибернетиков (снаружи) во время дождя дождя
    image dct_int_clubs_male_rain = "mods/dublicate_completed/images/bg/coin08/dct_int_clubs_male_rain.jpg" # Клуб кибернетиков (внутри) во время дождя дождя
    image dct_ext_another_clubhouse_day = "mods/dublicate_completed/images/bg/coin08/dct_ext_another_clubhouse_day.jpg" # Второе здание клубов (заброшенное)
    image dct_ext_camp_entrance_day = "mods/dublicate_completed/images/bg/coin08/dct_ext_camp_entrance_day.jpg" #  # Вид на клуб и на ворота лагеря днём

    

    image dct_bank_from_water_side_zoom = "mods/dublicate_completed/images/bg/coin10/dct_bank_from_water_side_zoom.jpg"
    image dct_ext_square_night_darker = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_darker.jpg"
    image dct_ext_square_night_darkest = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_darkest.jpg"
    image dct_ext_square_night_crop = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_crop.jpg"
    image dct_ext_square_night_purple = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_purple.jpg"
    image dct_ext_square_night_purple_blur = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_purple_blur.jpg"
    image dct_ext_square_night_purple_blur_HD = im.Scale("mods/dublicate_completed/images/bg/coin10/dct_ext_square_night_purple_blur_HD.jpg",1920,1080)
    image dct_ext_square_profile_view_night = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_profile_view_night.jpg" # Площадь с боку ночью, вид на Генду и админ. корпус
    image dct_ext_square_profile_view_night_darker = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_profile_view_night_darker.jpg"
    image dct_ext_square_profile_view_night_darkest = "mods/dublicate_completed/images/bg/coin10/dct_ext_square_profile_view_night_darkest.jpg"
    image dct_ext_stage_close_night = "mods/dublicate_completed/images/bg/coin10/dct_ext_stage_close_night.jpg"
    image dct_ext_stage_close_night_darker = "mods/dublicate_completed/images/bg/coin10/dct_ext_stage_close_night_darker.jpg"
    image dct_ext_stage_normal_night_darker = "mods/dublicate_completed/images/bg/coin10/dct_ext_stage_normal_night_darker.jpg"
        
        
    
    image dct_int_bus_rightwindow_day = "mods/dublicate_completed/images/bg/coin12/dct_int_bus_rightwindow_day.jpg"
    image dct_int_bus_leftwindow_day = "mods/dublicate_completed/images/bg/coin12/dct_int_bus_leftwindow_day.jpg"
    image dct_ext_bus_road = "mods/dublicate_completed/images/bg/coin12/dct_ext_bus_road.jpg"
    image dct_ext_outside_field = "mods/dublicate_completed/images/bg/coin12/dct_ext_outside_field.jpg"
    image dct_author_room = "mods/dublicate_completed/images/bg/coin12/dct_author_room.jpg"
    
    
    
    #cg
    
    image d_us_and_uv_close = "mods/dublicate_completed/images/cg/d_us_and_uv_close.jpg"
    image d_us_and_uv_far = "mods/dublicate_completed/images/cg/d_us_and_uv_far.jpg"
    image d_to_and_uv_close = "mods/dublicate_completed/images/cg/d_to_and_uv_close.jpg"
    image d_to_and_uv_far = "mods/dublicate_completed/images/cg/d_to_and_uv_far.jpg"
    image d_us_cry_far = "mods/dublicate_completed/images/cg/d_us_cry_far.jpg"
    image d_us_cry_close = "mods/dublicate_completed/images/cg/d_us_cry_close.jpg"
    image dct_alice_effector_part3 = "mods/dublicate_completed/images/cg/dct_alice_effector_part3.jpg"
    image dct_anabasis_fin = "mods/dublicate_completed/images/cg/dct_anabasis_fin.jpg"
    image dct_binocular_view = "mods/dublicate_completed/images/cg/dct_binocular_view.png"
    image dct_boat_solo = "mods/dublicate_completed/images/cg/dct_boat_solo.jpg"
    image dct_boat_solo_day = "mods/dublicate_completed/images/cg/dct_boat_solo_day.jpg" # Один на лодке днём
    image dct_boathouse_semen = "mods/dublicate_completed/images/cg/dct_boathouse_semen.png"
    image dct_bonfire = "mods/dublicate_completed/images/cg/dct_bonfire.jpg"
    image dct_cat_house_part2 = "mods/dublicate_completed/images/cg/dct_cat_house_part2.jpg"
    image dct_cat_house_part3_footprint = "mods/dublicate_completed/images/cg/dct_cat_house_part3_footprint.jpg"
    image dct_cof = "mods/dublicate_completed/images/cg/dct_cof.jpg"
    image dct_d1_gate = "mods/dublicate_completed/images/cg/dct_d1_gate.jpg"
    image dct_concert = "mods/dublicate_completed/images/cg/dct_concert.jpg"
    image dct_d2_lineup = "mods/dublicate_completed/images/cg/dct_d2_lineup.jpg"
    image dct_d2_mirror = "mods/dublicate_completed/images/cg/dct_d2_mirror.jpg"
    image dct_d3_disco = "mods/dublicate_completed/images/cg/dct_d3_disco.jpg"
    image dct_d3_revelation = "mods/dublicate_completed/images/cg/dct_d3_revelation.jpg" #Семен, Лена, вечер, скамейка
    image dct_d3_sl_dance = "mods/dublicate_completed/images/cg/dct_d3_sl_dance.jpg"
    image dct_d5_sl_square_me_lead_7dl = "mods/dublicate_completed/images/cg/dct_d5_sl_square_me_lead_7dl.jpg"
    image dct_dragonfly = "mods/dublicate_completed/images/cg/dct_dragonfly.jpg"
    image dct_dv_dance_7 = "mods/dublicate_completed/images/cg/dct_dv_dance_7.jpg"
    image dct_dream_veil = "mods/dublicate_completed/images/cg/dct_dream_veil.png" #вуаль сна
    image dct_floor hatch = "mods/dublicate_completed/images/cg/dct_floor hatch.jpg"
    image dct_day_sky = "mods/dublicate_completed/images/cg/dct_day_sky.jpg"
    image dct_night_sky = "mods/dublicate_completed/images/cg/dct_night_sky.jpg"
    image dct_ext_sim_ul_train = "mods/dublicate_completed/images/cg/dct_ext_sim_ul_train.jpg"
    image dct_forest_sky_day = "mods/dublicate_completed/images/cg/dct_forest_sky_day.jpg"
    image dct_prolog_4 = "mods/dublicate_completed/images/cg/dct_prolog_4.jpg"
    image dct_prologue_keyboard_monitor_3 = "mods/dublicate_completed/images/cg/dct_prologue_keyboard_monitor_3.jpg"
    image dct_prologue_monitor_1 = "mods/dublicate_completed/images/cg/dct_prologue_monitor_1.jpg"
    image dct_prologue_monitor_2 = "mods/dublicate_completed/images/cg/dct_prologue_monitor_2.jpg"
    image dct_prologue_monitor_3 = "mods/dublicate_completed/images/cg/dct_prologue_monitor_3.jpg"
    image dct_prologue_monitor_4 = "mods/dublicate_completed/images/cg/dct_prologue_monitor_4.jpg"
    image dct_intro_3 = "mods/dublicate_completed/images/cg/dct_intro_3.jpg"
    image dct_intro_7 = "mods/dublicate_completed/images/cg/dct_intro_7.jpg"
    image dct_intro_8 = "mods/dublicate_completed/images/cg/dct_intro_8.jpg"
    image dct_intro_9 = "mods/dublicate_completed/images/cg/dct_intro_9.jpg"
    image dct_intro_11 = "mods/dublicate_completed/images/cg/dct_intro_11.jpg"
    image dct_intro_13 = "mods/dublicate_completed/images/cg/dct_intro_13.jpg"
    image dct_story_one_pioneer = "mods/dublicate_completed/images/cg/dct_story_one_pioneer.jpg"
    image dct_story_one_pioneer2 = "mods/dublicate_completed/images/cg/dct_story_one_pioneer2.jpg"
    image dct_story_one_pioneer3 = "mods/dublicate_completed/images/cg/dct_story_one_pioneer3.jpg"
    image dct_d1_un_book = "mods/dublicate_completed/images/cg/dct_d1_un_book.jpg"
    #image dct_sht = "mods/dublicate_completed/images/cg/dct_sht.jpg" #СХТ40 - переделано в прозрачный спрайт
    image dct_un_effector_1 = "mods/dublicate_completed/images/cg/dct_un_effector_1.jpg"
    image dct_un_effector_2 = "mods/dublicate_completed/images/cg/dct_un_effector_2.jpg"
    image dct_neptunesday = "mods/dublicate_completed/images/cg/dct_neptunesday.jpg" #День Нептуна
    image dct_mi_and_dsl_in_shop = "mods/dublicate_completed/images/cg/dct_mi_and_dsl_in_shop.jpg"
    image dct_names_in_clouds_fin = "mods/dublicate_completed/images/cg/dct_names_in_clouds_fin.jpg"
    image dct_mi_boat_7d = "mods/dublicate_completed/images/cg/dct_mi_boat_7d.jpg"
    image dct_life_line_fin = "mods/dublicate_completed/images/cg/dct_life_line_fin.jpg"
    image dct_life_line_road = "mods/dublicate_completed/images/cg/dct_life_line_road.jpg"
    image slide_rule = "mods/dublicate_completed/images/cg/slide_rule.jpg" # Логарифмическая линейка заманена на нарисованную
    image dct_us_old = "mods/dublicate_completed/images/cg/dct_us_old.jpg"
    image dct_4th_shift_fin = "mods/dublicate_completed/images/cg/dct_4th_shift_fin.jpg"
    image dct_cat_house_part3_lenin_v_razlive = "mods/dublicate_completed/images/cg/dct_cat_house_part3_lenin_v_razlive.jpg"
    image dct_cs_and_uv_meeting_1 = "mods/dublicate_completed/images/cg/dct_cs_and_uv_meeting_1.jpg"
    image dct_cs_and_uv_meeting_2 = "mods/dublicate_completed/images/cg/dct_cs_and_uv_meeting_2.jpg"
    image dct_cs_and_uv_mirror_finger = "mods/dublicate_completed/images/cg/dct_cs_and_uv_mirror_finger.jpg"
    image dct_cs_and_uv_mirror = "mods/dublicate_completed/images/cg/dct_cs_and_uv_mirror.jpg"
    image dct_uv_behind_tree = "mods/dublicate_completed/images/cg/dct_uv_behind_tree.jpg"
    image dct_uv_wilde_laugh = "mods/dublicate_completed/images/cg/dct_uv_wilde_laugh.jpg"
    image dct_to_hunter = "mods/dublicate_completed/images/cg/dct_to_hunter.jpg"
    image dct_to_in_bog = "mods/dublicate_completed/images/cg/dct_to_in_bog.jpg"
    image dct_to_in_bog_2 = "mods/dublicate_completed/images/cg/dct_to_in_bog_2.jpg"
    image dct_dancing_uv = "mods/dublicate_completed/images/cg/dct_dancing_uv.jpg"
    image dct_olga_road = "mods/dublicate_completed/images/cg/dct_olga_road.jpg" #Просто, вырезаная дорога из Аним_16
    image dct_lineup = "mods/dublicate_completed/images/cg/dct_lineup.jpg"
    image dct_lineup_mi_not_us = "mods/dublicate_completed/images/cg/dct_lineup_mi_not_us.jpg"
    image dct_lineup_mt_mi_not_us = "mods/dublicate_completed/images/cg/dct_lineup_mt_mi_not_us.jpg"
    image dct_lineup_sh_not_dv = "mods/dublicate_completed/images/cg/dct_lineup_sh_not_dv.jpg"
    image dct_lineup_us_sport = "mods/dublicate_completed/images/cg/dct_lineup_us_sport.jpg"
    image dct_lineup_two_lines = "mods/dublicate_completed/images/cg/dct_lineup_two_lines.jpg"
    
    ##### cg (coin)
    
    image dct_int_bus_window_view = "mods/dublicate_completed/images/cg/coin01/dct_int_bus_window_view.jpg"
    
    image dct_int_mirror_in_library = im.Composite((1920, 1080), (0, 0), 'mods/dublicate_completed/images/cg/coin02/dct_mirror_wall_library.jpg', (0, 0), 'mods/dublicate_completed/images/cg/coin02/dct_mirror_with_shadow.png', (0, 0), 'mods/dublicate_completed/images/cg/coin02/dct_mirror_bookshelves.png', (0, 0), 'mods/dublicate_completed/images/cg/coin02/dct_mirror_frame.png')
    image dct_disassembled_catrobot = "mods/dublicate_completed/images/cg/coin02/dct_disassembled_catrobot.jpg"
    image dct_cg_foots_and_ball = "mods/dublicate_completed/images/cg/coin02/dct_cg_foots_and_ball.jpg"
    image dct_cg_el_kick_ball = "mods/dublicate_completed/images/cg/coin02/dct_cg_el_kick_ball.jpg"
    
    image dct_mi_piano1 = "mods/dublicate_completed/images/cg/coin06/dct_mi_piano1.jpg" # Мику играет на пианино
    image dct_sh_in_cage = "mods/dublicate_completed/images/cg/coin06/dct_sh_in_cage.jpg" # Шурик тестит машину для чтения воспоминаний
    image dct_sky_over_flowerbed_behind_library = "mods/dublicate_completed/images/cg/coin06/dct_sky_over_flowerbed_behind_library.jpg" # Небо над головой в обраблении крон
    image dct_mz_and_el_sitting_on_bench_near_flowerbed = "mods/dublicate_completed/images/cg/coin06/dct_mz_and_el_sitting_on_bench_near_flowerbed.jpg" # Эл и Женя сидят на лавочке
    
    image dct_mz_and_el_sitting_on_grass = "mods/dublicate_completed/images/cg/coin07/dct_mz_and_el_sitting_on_grass.jpg" # Эл и Женя сидят на траве под деревьями
        
    image dct_dv_two_pieces_bg_dark = "mods/dublicate_completed/images/cg/coin10/dct_dv_two_pieces_bg_dark.jpg"
    image dct_dv_two_pieces_bg_square = "mods/dublicate_completed/images/cg/coin10/dct_dv_two_pieces_bg_square.jpg"
    image dct_dv_two_pieces_casual = im.Scale("mods/dublicate_completed/images/cg/coin10/dct_dv_two_pieces_casual.png",1536,1620)
    image dct_dv_two_pieces_pioneer = im.Scale("mods/dublicate_completed/images/cg/coin10/dct_dv_two_pieces_pioneer.png",1536,1620)
    image dct_dv_argue = "mods/dublicate_completed/images/cg/coin10/dct_dv_argue.jpg"
    image dct_dv_argue sternsmile = "mods/dublicate_completed/images/cg/coin10/dct_dv_argue_sternsmile.jpg"
    image dct_sl_clean_square_1 = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_1.jpg",0.7)
    image dct_sl_clean_square_2 = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_2.jpg",0.7)
    image dct_sl_clean_square_3 = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_3.jpg",0.7)
    image dct_sl_clean_square_4 = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_4.jpg",0.7)
    image dct_sl_clean_square_5 = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_5.jpg",0.7)
    image dct_sl_clean_square_6 = "mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_6.jpg"
    image dct_sl_clean_square_7 = "mods/dublicate_completed/images/cg/coin10/dct_sl_clean_square_7.jpg"
    image dct_dsl_in_shop = im.Alpha("mods/dublicate_completed/images/cg/coin10/dct_dsl_in_shop.jpg",0.7)
    image arseniy_chebynkin_izbad = im.Scale("mods/dublicate_completed/images/cg/coin10/arseniy_chebynkin_izbad.jpg",1920,1080) #Изба из Травницы (https://arsenixc.artstation.com/projects/PeEE1)
    
    image dct_int_bus_blue = "mods/dublicate_completed/images/cg/coin12/dct_int_bus_blue.jpg"
    image dct_int_bus_pink = "mods/dublicate_completed/images/cg/coin12/dct_int_bus_pink.jpg"
    image dct_int_bus_purple = "mods/dublicate_completed/images/cg/coin12/dct_int_bus_purple.jpg"
    image dct_d1_uv = "mods/dublicate_completed/images/cg/coin12/dct_d1_uv.jpg"
    image dct_d1_uv_2 = "mods/dublicate_completed/images/cg/coin12/dct_d1_uv_2.jpg"
    


    
    
    ##### Трансформации (coin)
    
    transform dct_zoom_sparkle:         # Вспышка блёсток
        zoom 0 alpha 0 anchor(0.5, 0.5)
        linear 0.2 zoom 0.8 alpha 1.0
        linear 0.05 zoom 1.0 alpha 0
        



    #############################
    #преобразованные изображения#
    #############################
    
    image dct_int_bus_people_day_grayscale_small = "mods/dublicate_completed/images/bg/dct_int_bus_people_day_grayscale_small.jpg"
    image dct_d2_lineup_grayscale_small = "mods/dublicate_completed/images/cg/dct_d2_lineup_grayscale_small.jpg"
    image dct_d2_mirror_grayscale_small = "mods/dublicate_completed/images/cg/dct_d2_mirror_grayscale_small.jpg"
    image dct_d3_disco_grayscale_small = "mods/dublicate_completed/images/cg/dct_d3_disco_grayscale_small.jpg"
    image dct_int_dining_hall_people_day_grayscale_small = "mods/dublicate_completed/images/bg/dct_int_dining_hall_people_day_grayscale_small.jpg"
    image dct_intro_xx_grayscale_small = "mods/dublicate_completed/images/bg/dct_intro_xx_grayscale_small.jpg"
    image dct_semen_room_grayscale_small = "mods/dublicate_completed/images/bg/dct_semen_room_grayscale_small.jpg"
    image dct_prolog_4_grayscale_small = "mods/dublicate_completed/images/cg/dct_prolog_4_grayscale_small.jpg"
    image dct_prologue_keyboard_monitor_3_grayscale_small = "mods/dublicate_completed/images/cg/dct_prologue_keyboard_monitor_3_grayscale_small.jpg"
    image dct_intro_8_grayscale_small = "mods/dublicate_completed/images/cg/dct_intro_8_grayscale_small.jpg"
    image dct_intro_13_grayscale_small = "mods/dublicate_completed/images/cg/dct_intro_13_grayscale_small"
    
    ##########
    #анимация#
    ##########
    
    #image recoil = Animation("mods/dublicate_completed/images/anim/anim02.png", 1,"mods/dublicate_completed/images/anim/anim01.png", 1,"mods/dublicate_completed/images/anim/anim00.png", 1,"mods/dublicate_completed/images/anim/anim10.png", 1)
    image dct_anim02 = "mods/dublicate_completed/images/anim/dct_anim02.png"
    image dct_anim01 = "mods/dublicate_completed/images/anim/dct_anim01.png"
    image dct_anim00 = "mods/dublicate_completed/images/anim/dct_anim00.png"
    image dct_anim10 = "mods/dublicate_completed/images/anim/dct_anim10.png"
    image dct_smartphone = "mods/dublicate_completed/images/anim/dct_smartphone.png"
    image dct_smartphone1 = "mods/dublicate_completed/images/anim/dct_smartphone1.png"
    image dct_smartphone4 = "mods/dublicate_completed/images/anim/dct_smartphone4.png"
    image dct_smartphone6 = "mods/dublicate_completed/images/anim/dct_smartphone6.png"
    image dct_smartphone8 = "mods/dublicate_completed/images/anim/dct_smartphone8.png"
    image dct_smartphone10 = "mods/dublicate_completed/images/anim/dct_smartphone10.png"
    image dct_smartphone12 = "mods/dublicate_completed/images/anim/dct_smartphone12.png"
    image dct_smartphone14 = "mods/dublicate_completed/images/anim/dct_smartphone14.png"
    image dct_smartphone16 = "mods/dublicate_completed/images/anim/dct_smartphone16.png"
    
    
    
    ##### Анимация (coin)
    
    image dct_road_anim:                  # Дорога (автобус едет в лагерь)
        "mods/dublicate_completed/images/anim/coin01/dct_road_6.jpg"
        pause 0.6
        "mods/dublicate_completed/images/anim/coin01/dct_road_5.jpg" with dissolve_fast
        pause 0.6
        "mods/dublicate_completed/images/anim/coin01/dct_road_4.jpg" with dissolve_fast
        pause 0.6
        "mods/dublicate_completed/images/anim/coin01/dct_road_3.jpg" with dissolve_fast
        pause 0.6
        "mods/dublicate_completed/images/anim/coin01/dct_road_2.jpg" with dissolve_fast
        pause 0.6
        "mods/dublicate_completed/images/anim/coin01/dct_road_1.jpg" with dissolve_fast
        pause 1
        


    image dct_camp_stroll_to_the_right:                  # Смена локаций лагеря
        "bg ext_musclub_day" with pushleft
        pause 2.5
        "bg ext_washstand_day" with pushleft
        pause 2.5
        "dct_ext_stage_big_sunset" with pushleft
        pause 2.5
        "bg ext_library_day" with pushleft
        pause 2.5
        "bg ext_aidpost_day" with pushleft
        pause 2.5
        "dct_ext_bathhouse_day" with pushleft
        pause 2.5
        "dct_ext_beach_sunset_not_train" with pushleft
        pause 2.5
        "dct_ext_boathouse_sunset" with pushleft
        pause 2.5
        "d_ext_dv_hideout_sunset" with pushleft
        pause 2.5
        repeat
        
        
        
    # image dct_camp_stroll_to_the_right:                  # То же самое, но крутится без перерыва
        # "bg ext_musclub_day" with pushleft
        # pause 1
        # "bg ext_washstand_day" with pushleft
        # pause 1
        # "dct_ext_stage_big_sunset" with pushleft
        # pause 1
        # "bg ext_library_day" with pushleft
        # pause 1
        # "bg ext_aidpost_day" with pushleft
        # pause 1
        # "dct_ext_bathhouse_day" with pushleft
        # pause 1
        # "dct_ext_beach_sunset_not_train" with pushleft
        # pause 1
        # "dct_ext_boathouse_sunset" with pushleft
        # pause 1
        # "d_ext_dv_hideout_sunset" with pushleft
        # pause 1
        # repeat
        
        
        
    image dct_el_shuttles_back_and_forth:                  # Электроник курсирует туда-сюда (мимо бибилиотеки)
        "el normal pioneer far"
        xcenter 0.14 alpha 0
        linear 1 xcenter 0.38  alpha 1
        linear 1 xcenter 0.62
        linear 1 xcenter 0.86 alpha 0
        pause 0.5
        "el serious pioneer far"
        xcenter 0.86 alpha 0
        linear 1 xcenter 0.62  alpha 1
        linear 1 xcenter 0.38
        linear 1 xcenter 0.14 alpha 0
        pause 0.5
        repeat
        
        
    image dct_el_running_back_and_forth:                  # Электроник бегает туда-сюда (на спортплощадке)
        "d_el laugh shorts"
        xcenter 0.86 alpha 0
        linear 0.6 xcenter 0.62  alpha 1
        linear 0.6 xcenter 0.38
        linear 0.6 xcenter 0.14 alpha 0
        pause 0.2
        "d_el smile shorts"
        xcenter 0.14 alpha 0
        linear 0.6 xcenter 0.38  alpha 1
        linear 0.6 xcenter 0.62
        linear 0.6 xcenter 0.86 alpha 0
        pause 0.2
        repeat
    
    
    
    image dct_clubs_male_comp_sh_crumble:                  # Шурик фрагментируется на экране монитора (выводить на экран в позиции xcenter 0.5 ycenter 0.45)
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh2.png"
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh3.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh4.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh5.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh6.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh7.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh8.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "mods/dublicate_completed/images/anim/coin01/dct_clubs_male_comp_sh9.png" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        pause 1
        "dct_clubs_male_comp_clear" with dissolve_fast
        xcenter 0.5 ycenter 0.45
        
        
        
    
    image d_sf_grabs_d_sv:          # Проявление Светы в руках Семёна, когда тот её подхватывает
        "d_sf_carrying_d_sv smile"
        alpha 0
        pause 0.55
        alpha 1
    
    
    
    
                                # Последовательность переходов "с шара на шар" на площади в 10 главе
        
    image dct_ball_to_ball_1 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_1.jpg"
    image dct_ball_to_ball_2 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_2.jpg"
    image dct_ball_to_ball_3 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_3.jpg"
    image dct_ball_to_ball_4 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_4.jpg"
    image dct_ball_to_ball_5 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_5.jpg"
    image dct_ball_to_ball_6 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_6.jpg"
    image dct_ball_to_ball_7 = "mods/dublicate_completed/images/anim/coin10/dct_ball_to_ball_7.jpg"

            

    
    
    image dct_int_bus_shimmer:                  # Цветные переливы в автобусе
        "bg int_bus" with dissolve_fast
        pause 0.5
        "dct_int_bus_pink" with dissolve_fast
        pause 0.5
        "dct_int_bus_purple" with dissolve_fast
        pause 0.5
        "dct_int_bus_blue" with dissolve_fast
        pause 0.5
        repeat
        

        
    image dct_uv_coin_bus:                  # Юля появляется в автобусе
        "dct_uv_coin_bus_farfar"
        alpha 0.0
        pause 1.0
        linear 0.5 alpha 1.0
        pause 0.5
        linear 0.5 alpha 0.0
        pause 2.0
        "dct_uv_coin_bus_far"
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 0.5
        linear 0.5 alpha 0.0
        pause 2.0
        "dct_uv_coin_bus_medium"
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 0.5
        linear 0.5 alpha 0.0
        pause 2.0
        "dct_uv_coin_bus_close"
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 0.5
        linear 0.5 alpha 0.0
        pause 2.0
        "dct_uv_coin_bus_closeclose"
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 0.5
        linear 0.5 alpha 0.0
        
                                    ################
        
    image dct_uv_coin_bus_shocked_1:          # Юля шокирована в автобусе (в трёх актах)
        pause 1.0
        "bg int_bus"
        
    image dct_uv_coin_bus_shocked_2:
        pause 1.0
        "uv shocked"
        
    image dct_uv_coin_bus_shocked_3:
        pause 0.5
        "dct_d1_uv_2"
        alpha 0
        linear 0.5 alpha 1.0
        linear 1.0 alpha 0.0
        
                                    ################
        
        
        
    ######### Сверкания в последней главе последней книги #########
    
    image dct_coin_bus_sparkle:         # Случайное сверкания для включения в состав группы
        choice:
            "dct_coin_bus_sparkle1"
        choice:
            "dct_coin_bus_sparkle2"
        choice:
            "dct_coin_bus_sparkle3"
        choice:
            "dct_coin_bus_sparkle4"
        choice:
            "dct_coin_bus_sparkle5"
        choice:
            "dct_coin_bus_sparkle6"
        choice:
            "dct_coin_bus_sparkle7"
        choice:
            "dct_coin_bus_sparkle8"
        choice:
            "dct_coin_bus_sparkle9"
        choice:
            "dct_coin_bus_sparkle10"
            
            
    image dct_coin_bus_sparkle_a:           # Группа сверканий A
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.85 ycenter 0.2
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.42 ycenter 0.73
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.2 ycenter 0.4
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.52 ycenter 0.1
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.27 ycenter 0.69
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.67 ycenter 0.31
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.55 ycenter 0.8
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.45 ycenter 0.75
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.72 ycenter 0.44
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.6 ycenter 0.5
        dct_zoom_sparkle
        pause 0.25
        repeat
        
        
        
    image dct_coin_bus_sparkle_b-:           # Группа сверканий B
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.34 ycenter 0.25
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.64 ycenter 0.1
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.8 ycenter 0.8
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.27 ycenter 0.65
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.94 ycenter 0.13
        dct_zoom_sparkle
        pause 0.25
        repeat
        
        
        
    image dct_coin_bus_sparkle_c-:           # Группа сверканий C
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.17 ycenter 0.28
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.5 ycenter 0.94
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.35 ycenter 0.12
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.72 ycenter 0.5
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.25 ycenter 0.9
        dct_zoom_sparkle
        pause 0.25
        repeat
        
        
        
    image dct_coin_bus_sparkle_d-:           # Группа сверканий D
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.45 ycenter 0.4
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.7 ycenter 0.15
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.38 ycenter 0.55
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.65 ycenter 0.8
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.58 ycenter 0.25
        dct_zoom_sparkle
        pause 0.25
        repeat
        
        
        
    image dct_coin_bus_sparkle_e-:           # Группа сверканий E
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.4 ycenter 0.1
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.65 ycenter 0.45
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.75 ycenter 0.35
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.48 ycenter 0.8
        dct_zoom_sparkle
        pause 0.25
        "dct_coin_bus_sparkle"
        zoom 0 alpha 0 anchor(0.5, 0.5) xcenter 0.68 ycenter 0.88
        dct_zoom_sparkle
        pause 0.25
        repeat
        
        

                    # Отложенные запуски
                    
    image dct_coin_bus_sparkle_b:
        pause 5
        "dct_coin_bus_sparkle_b-"
        
    image dct_coin_bus_sparkle_c:
        pause 10
        "dct_coin_bus_sparkle_c-"
        
    image dct_coin_bus_sparkle_d:
        pause 15
        "dct_coin_bus_sparkle_d-"
        
    image dct_coin_bus_sparkle_e:
        pause 15
        "dct_coin_bus_sparkle_d-"




                  # Юля в лесу за кустом
                  
    image dct_uv_ears_bush:     # Уши
        "uv shocked far"
        anchor(0.5, 0.5) xcenter 0.145 ycenter 0.647 rotate 33.8
        pause 0.5
        "uv sad far"
        anchor(0.5, 0.5) xcenter 0.145 ycenter 0.647 rotate 33.8
        pause 0.15
        "uv guilty far"
        anchor(0.5, 0.5) xcenter 0.148 ycenter 0.657 rotate 12.2
        pause 0.5
        "uv sad far"
        anchor(0.5, 0.5) xcenter 0.145 ycenter 0.647 rotate 33.8
        pause 0.15
        "uv shocked far"
        repeat
        


    image dct_uv_dress_bush:     # Платье
        pause 0.2
        "images/sprites/far/uv/uv_2_pioneer.png"
        anchor(0.5, 0.5) xcenter 0.147 ycenter 0.615 rotate -32.3
        pause 0.4
        "images/sprites/far/uv/uv_3_pioneer.png"
        anchor(0.5, 0.5) xcenter 0.147 ycenter 0.615 rotate -32.3
        pause 0.3
        "images/sprites/far/uv/uv_1_pioneer.png"
        anchor(0.5, 0.5) xcenter 0.151 ycenter 0.618 rotate -36.0
        pause 0.3
        
        
                  
    ###############################################################
        
    
    
    
    #####################
    #шумы, звуки, музыка#
    #####################
    
    #ambience
    
    $ dct_ambience_boat = "mods/dublicate_completed/sounds/ambience/dct_ambience_boat.ogg"
    $ dct_ambience_conf = "mods/dublicate_completed/sounds/ambience/dct_ambience_conf.ogg" #совещание
    $ dct_ambience_fire = "mods/dublicate_completed/sounds/ambience/dct_ambience_fire.ogg"
    $ dct_ambience_morning_birds = "mods/dublicate_completed/sounds/ambience/dct_ambience_morning_birds.ogg" #ночные птицы и ветер
    $ dct_ambience_oars = "mods/dublicate_completed/sounds/ambience/dct_ambience_oars.ogg" #плеск весел
    $ dct_ambience_oars2 = "mods/dublicate_completed/sounds/ambience/dct_ambience_oars2.ogg" #плеск весел чуть быстрее
    $ dct_ambience_run = "mods/dublicate_completed/sounds/ambience/dct_ambience_run.ogg" #бег по траве
    $ dct_ambience_train = "mods/dublicate_completed/sounds/ambience/dct_ambience_train.ogg" #поезд в движении
    $ dct_ambience_train_slow = "mods/dublicate_completed/sounds/ambience/dct_ambience_train_slow.ogg" #поезд в движении
    $ dct_ambience_wind = "mods/dublicate_completed/sounds/ambience/dct_ambience_wind.ogg" #легкий ветер
    $ dct_ambience_bonfire = "mods/dublicate_completed/sounds/ambience/dct_ambience_bonfire.ogg" #ночной костер в лесу
    $ dct_ambience_candle = "mods/dublicate_completed/sounds/ambience/dct_ambience_candle.ogg" #свеча
    $ dct_ambience_old_house_wind = "mods/dublicate_completed/sounds/ambience/dct_ambience_old_house_wind.ogg" #ветер в старом корпусе
    $ dct_ambience_creaking_floor = "mods/dublicate_completed/sounds/ambience/dct_ambience_creaking_floor.ogg" #пол скрипит
    $ dct_ambience_drips_in_mine = "mods/dublicate_completed/sounds/ambience/dct_ambience_drips_in_mine.ogg" #вода капает в заброшенной шахте
    $ dct_ambience_vent = "mods/dublicate_completed/sounds/ambience/dct_ambience_vent.ogg" #шум вытяжной вентиляции
    $ dct_ambience_river1 = "mods/dublicate_completed/sounds/ambience/dct_ambience_river1.ogg" #шум реки
    $ dct_ambience_beach = "mods/dublicate_completed/sounds/ambience/dct_ambience_beach.ogg" #пляж
    $ dct_ambience_light_rain = "mods/dublicate_completed/sounds/ambience/dct_ambience_light_rain.ogg"
    $ dct_ambience_heavy_rain = "mods/dublicate_completed/sounds/ambience/dct_ambience_heavy_rain.ogg" #ливень
    $ dct_ambience_room = "mods/dublicate_completed/sounds/ambience/dct_ambience_room.ogg" #комната
    $ dct_ambience_storm = "mods/dublicate_completed/sounds/ambience/dct_ambience_storm.ogg" 
    $ dct_ambience_street1 = "mods/dublicate_completed/sounds/ambience/dct_ambience_street1.ogg" # городская улица
    $ dct_ambience_street2 = "mods/dublicate_completed/sounds/ambience/dct_ambience_street2.ogg"
    $ dct_ambience_supermarket = "mods/dublicate_completed/sounds/ambience/dct_ambience_supermarket.ogg"
    $ dct_ambience_eskalator = "mods/dublicate_completed/sounds/ambience/dct_ambience_eskalator.ogg"
    $ dct_ambience_fobos_daemos = "mods/dublicate_completed/sounds/ambience/dct_ambience_fobos_daemos.ogg"
    $ dct_ambience_living_room = "mods/dublicate_completed/sounds/ambience/dct_ambience_living_room.ogg"
    $ dct_ambience_cafe = "mods/dublicate_completed/sounds/ambience/dct_ambience_cafe.ogg"
    $ dct_ambience_swamp = "mods/dublicate_completed/sounds/ambience/dct_ambience_swamp.ogg"
    $ dct_ambience_swamp_night = "mods/dublicate_completed/sounds/ambience/dct_ambience_swamp_night.ogg"
    
    ##### ambience (coin)
    
    $ dct_ambience_volley_in_gym = "mods/dublicate_completed/sounds/coin/ambience/dct_ambience_volley_in_gym.ogg"   # Игра в волейбол в зале
    
    
    #music

    $ higekitekina = "mods/dublicate_completed/sounds/music/higekitekina.ogg"
    $ anewbeginning = "mods/dublicate_completed/sounds/music/anewbeginning.ogg"
    $ twinkling = "mods/dublicate_completed/sounds/music/twinkling.ogg"
    $ adaytoremember = "mods/dublicate_completed/sounds/music/adaytoremember.ogg"
    $ forgotten_summer = "mods/dublicate_completed/sounds/music/forgotten_summer.ogg"
    $ feeling_good = "mods/dublicate_completed/sounds/music/feeling_good.ogg"
    $ i_tried_to_bring_it_back = "mods/dublicate_completed/sounds/music/i_tried_to_bring_it_back.ogg"
    $ my_2nd_summer = "mods/dublicate_completed/sounds/music/my_2nd_summer.ogg"
    $ littleidea = "mods/dublicate_completed/sounds/music/littleidea.ogg"
    $ buddy = "mods/dublicate_completed/sounds/music/buddy.ogg"
    $ tenderness = "mods/dublicate_completed/sounds/music/tenderness.ogg"
    $ crush = "mods/dublicate_completed/sounds/music/crush.ogg"
    $ homeworldcollapse = "mods/dublicate_completed/sounds/music/homeworldcollapse.ogg"
    $ badstory = "mods/dublicate_completed/sounds/music/badstory.ogg"
    $ dreamers_of_the_day = "mods/dublicate_completed/sounds/music/dreamers_of_the_day.ogg"
    $ cambo_coffee = "mods/dublicate_completed/sounds/music/cambo_coffee.ogg"
    $ peritune_gentle_theme_piano = "mods/dublicate_completed/sounds/music/peritune_gentle_theme_piano.ogg"
    $ fm_freemusic_chillout_music = "mods/dublicate_completed/sounds/music/fm_freemusic_chillout_music.ogg"
    $ twisterium_eternal_love = "mods/dublicate_completed/sounds/music/twisterium_eternal_love.ogg"
    $ its_in_the_fog = "mods/dublicate_completed/sounds/music/its_in_the_fog.ogg"
    $ inossi_imaginary_love = "mods/dublicate_completed/sounds/music/inossi_imaginary_love.ogg"
    $ rustic_ballad = "mods/dublicate_completed/sounds/music/rustic_ballad.ogg"
    $ a_v_to_the_crows = "mods/dublicate_completed/sounds/music/a_v_to_the_crows.ogg"
    $ supernova = "mods/dublicate_completed/sounds/music/supernova.ogg"
    $ brush_marks = "mods/dublicate_completed/sounds/music/brush_marks.ogg"
    $ mr_wick = "mods/dublicate_completed/sounds/music/mr_wick.ogg"
    $ the_day_when_i_die = "mods/dublicate_completed/sounds/music/the_day_when_i_die.ogg"
    $ osc_two = "mods/dublicate_completed/sounds/music/osc_two.ogg"
    $ something_beautiful = "mods/dublicate_completed/sounds/music/something_beautiful.ogg"
    
    ##### music (coin)
    
    $ Everlasting_Summer_guitar_cover = "mods/dublicate_completed/sounds/coin/music/Everlasting_Summer[guitar_cover](youtu.be_z6sTDBAUTfg).ogg"
    $ Everlasting_Summer_electric_guitar_cover = "mods/dublicate_completed/sounds/coin/music/Everlasting_Summer_Main_Theme_[electric_guitar_cover](youtu.be_hVT9O5yVYU4).ogg"
    
    
    #sfx
    
    $ dct_sfx_alice_sneezing = "mods/dublicate_completed/sounds/sfx/dct_sfx_alice_sneezing.ogg"#алиса чихает
    $ dct_sfx_teapot = "mods/dublicate_completed/sounds/sfx/dct_sfx_teapot.ogg" #чайник
    $ dct_sfx_teapot1 = "mods/dublicate_completed/sounds/sfx/dct_sfx_teapot1.ogg"
    $ dct_sfx_well1 = "mods/dublicate_completed/sounds/sfx/dct_sfx_well1.ogg"#колодец
    $ dct_sfx_well2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_well2.ogg"#колодец
    $ dct_sfx_well3 = "mods/dublicate_completed/sounds/sfx/dct_sfx_well3.ogg"#колодец
    $ dct_sfx_whistle = "mods/dublicate_completed/sounds/sfx/dct_sfx_whistle.ogg" #свисток судьи
    $ dct_sfx_broom = "mods/dublicate_completed/sounds/sfx/dct_sfx_broom.ogg" #метла
    $ dct_sfx_bus_arrival = "mods/dublicate_completed/sounds/sfx/dct_sfx_bus_arrival.ogg" #прибытие автобуса
    $ dct_sfx_bus_departure = "mods/dublicate_completed/sounds/sfx/dct_sfx_bus_departure.ogg" #отбытие автобуса
    $ dct_sfx_bus_departure2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_bus_departure2.ogg" #отбытие автобуса кратко
    $ dct_sfx_dart ="mods/dublicate_completed/sounds/sfx/dct_sfx_dart.ogg" #стрела попадает в цель
    $ dct_sfx_forest_day2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_forest_day2.ogg"
    $ dct_sfx_jump = "mods/dublicate_completed/sounds/sfx/dct_sfx_jump.ogg" #прыг из автобуса
    $ dct_sfx_grass_steps = "mods/dublicate_completed/sounds/sfx/dct_sfx_grass_steps.ogg" #убыстряющиеся шаги по траве
    $ dct_sfx_bus_door = "mods/dublicate_completed/sounds/sfx/dct_sfx_bus_door.ogg"
    $ dct_sfx_chair = "mods/dublicate_completed/sounds/sfx/dct_sfx_chair.ogg" #двигающийся стул
    $ dct_sfx_crow = "mods/dublicate_completed/sounds/sfx/dct_sfx_crow.ogg" #сонная ворона
    $ dct_sfx_short_beeps = "mods/dublicate_completed/sounds/sfx/dct_sfx_short_beeps.ogg" #короткие гудки
    $ dct_sfx_solo_card = "mods/dublicate_completed/sounds/sfx/dct_sfx_solo_card.ogg" #одиночная брошенная карта
    $ dct_sfx_train_arrival = "mods/dublicate_completed/sounds/sfx/dct_sfx_train_arrival.ogg" #прибытие поезда
    $ dct_sfx_train_arrival_with_horn_far = "mods/dublicate_completed/sounds/sfx/dct_sfx_train_arrival_with_horn_far.ogg"
    $ dct_sfx_train_arrival_with_horn = "mods/dublicate_completed/sounds/sfx/dct_sfx_train_arrival_with_horn.ogg"
    $ dct_sfx_badger = "mods/dublicate_completed/sounds/sfx/dct_sfx_badger.ogg" #барсук недоволен
    $ dct_sfx_radio = "mods/dublicate_completed/sounds/sfx/dct_sfx_radio.ogg" #рация шипит
    $ dct_sfx_robot_run_away = "mods/dublicate_completed/sounds/sfx/dct_sfx_robot_run_away.ogg"
    $ dct_sfx_horn_rise = "mods/dublicate_completed/sounds/sfx/dct_sfx_horn_rise.ogg" #горн-подъём
    $ dct_sfx_alarm = "mods/dublicate_completed/sounds/sfx/dct_sfx_alarm.ogg" #будильник
    $ dct_sfx_slammed_book = "mods/dublicate_completed/sounds/sfx/dct_sfx_slammed_book.ogg"
    $ dct_sfx_match = "mods/dublicate_completed/sounds/sfx/dct_sfx_match.ogg" #спичка
    $ dct_sfx_teaspoon = "mods/dublicate_completed/sounds/sfx/dct_sfx_teaspoon.ogg" #чайная ложка
    $ dct_sfx_pages = "mods/dublicate_completed/sounds/sfx/dct_sfx_pages.ogg" #страницы
    $ dct_sfx_cry = "mods/dublicate_completed/sounds/sfx/dct_sfx_cry.ogg" #плач
    $ dct_sfx_cry_short = "mods/dublicate_completed/sounds/sfx/dct_sfx_cry_short.ogg"
    $ dct_us_laugh = "mods/dublicate_completed/sounds/sfx/dct_us_laugh.ogg"
    $ dct_sfx_fallen_book = "mods/dublicate_completed/sounds/sfx/dct_sfx_fallen_book.ogg"
    $ dct_sfx_open_metall_door = "mods/dublicate_completed/sounds/sfx/dct_sfx_open_metall_door.ogg"
    $ dct_sfx_scissors = "mods/dublicate_completed/sounds/sfx/dct_sfx_scissors.ogg" #ножницы, стрижка волос
    $ dct_sfx_steps2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_steps2.ogg" #шаги нескольких человек по твердому полу
    $ dct_sfx_steps3 = "mods/dublicate_completed/sounds/sfx/dct_sfx_steps3.ogg"
    $ dct_sfx_running = "mods/dublicate_completed/sounds/sfx/dct_sfx_running.ogg" #бег
    $ dct_sfx_badminton = "mods/dublicate_completed/sounds/sfx/dct_sfx_badminton.ogg"
    $ dct_sfx_discharge = "mods/dublicate_completed/sounds/sfx/dct_sfx_discharge.ogg" #гром разряд
    $ dct_sfx_facepalm = "mods/dublicate_completed/sounds/sfx/dct_sfx_facepalm.ogg"
    $ dct_sfx_ping_pong = "mods/dublicate_completed/sounds/sfx/dct_sfx_ping_pong.ogg"
    $ dct_sfx_hammering = "mods/dublicate_completed/sounds/sfx/dct_sfx_hammering.ogg" #стук молотков
    $ dct_sfx_sht40_1 = "mods/dublicate_completed/sounds/sfx/dct_sfx_sht40_1.ogg" #выстрел сигнальной ракетой
    $ dct_sfx_sht40_2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_sht40_2.ogg" #зыуковой сигнал ракеты СХТ
    $ dct_sfx_clang = "mods/dublicate_completed/sounds/sfx/dct_sfx_clang.ogg" #лязг челюстей кошкоробота
    $ dct_sfx_close_door_hard = "mods/dublicate_completed/sounds/sfx/dct_sfx_close_door_hard.ogg" #хлопок дверью
    $ dct_sfx_breaking_glass = "mods/dublicate_completed/sounds/sfx/dct_sfx_breaking_glass.ogg" #бьющееся стекло
    $ dct_sfx_applause = "mods/dublicate_completed/sounds/sfx/dct_sfx_applause.ogg" #аплодисменты
    $ dct_sfx_monitor = "mods/dublicate_completed/sounds/sfx/dct_sfx_monitor.ogg" #кардиомонитор
    $ dct_sfx_scare = "mods/dublicate_completed/sounds/sfx/dct_sfx_scare.ogg" #испуг У
    $ dct_sfx_fall = "mods/dublicate_completed/sounds/sfx/dct_sfx_fall.ogg" #падение
    $ dct_sfx_pulse = "mods/dublicate_completed/sounds/sfx/dct_sfx_pulse.ogg" #пульс
    $ dct_sfx_pulse_slow = "mods/dublicate_completed/sounds/sfx/dct_sfx_pulse_slow.ogg" #пульс
    $ dct_sfx_refrigerator = "mods/dublicate_completed/sounds/sfx/dct_sfx_refrigerator.ogg" #холодильник
    $ dct_sfx_femscreech = "mods/dublicate_completed/sounds/sfx/dct_sfx_femscreech.ogg"
    $ dct_sfx_train_horn_far = "mods/dublicate_completed/sounds/sfx/dct_sfx_train_horn_far.ogg"
    $ dct_sfx_voices_in_forest = "mods/dublicate_completed/sounds/sfx/dct_sfx_voices_in_forest.ogg"
    $ dct_sfx_wood_floor_squeak = "mods/dublicate_completed/sounds/sfx/dct_sfx_wood_floor_squeak.ogg"
    $ dct_sfx_inhale = "mods/dublicate_completed/sounds/sfx/dct_sfx_inhale.ogg"
    $ dct_sfx_apple = "mods/dublicate_completed/sounds/sfx/dct_sfx_apple.ogg"
    $ dct_sfx_typewriter = "mods/dublicate_completed/sounds/sfx/dct_sfx_typewriter.ogg" #пишущая машинка
    $ dct_sfx_soldiers_run_start = "mods/dublicate_completed/sounds/sfx/dct_sfx_soldiers_run_start.ogg" #Строевой шаг
    $ dct_sfx_soldiers_run_continue = "mods/dublicate_completed/sounds/sfx/dct_sfx_soldiers_run_continue.ogg"
    $ dct_sfx_soldiers_run_stop = "mods/dublicate_completed/sounds/sfx/dct_sfx_soldiers_run_stop.ogg"
    $ dct_sfx_rustle_alice = "mods/dublicate_completed/sounds/sfx/dct_sfx_rustle_alice.ogg"
    $ dct_sfx_lift = "mods/dublicate_completed/sounds/sfx/dct_sfx_lift.ogg"
    $ dct_sfx_5500Hz = "mods/dublicate_completed/sounds/sfx/dct_sfx_5500Hz.ogg"
    $ dct_sfx_fright = "mods/dublicate_completed/sounds/sfx/dct_sfx_fright.ogg"
    $ dct_sfx_phone_disk = "mods/dublicate_completed/sounds/sfx/dct_sfx_phone_disk.ogg"
    $ dct_sfx_knife_drop = "mods/dublicate_completed/sounds/sfx/dct_sfx_knife_drop.ogg"
    $ dct_sfx_jump_in_swamp = "mods/dublicate_completed/sounds/sfx/dct_sfx_jump_in_swamp.ogg"
    $ dct_sfx_steps_in_swamp = "mods/dublicate_completed/sounds/sfx/dct_sfx_steps_in_swamp.ogg"
    $ dct_sfx_splash_in_swamp = "mods/dublicate_completed/sounds/sfx/dct_sfx_splash_in_swamp.ogg"
    #Кошка
    $ dct_sfx_cat_hiss1 = "mods/dublicate_completed/sounds/sfx/dct_sfx_cat_hiss1.ogg"
    $ dct_sfx_meow1 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow1.ogg"
    $ dct_sfx_meow2 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow2.ogg"
    $ dct_sfx_meow3 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow3.ogg"
    $ dct_sfx_meow4 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow4.ogg"
    $ dct_sfx_meow5 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow5.ogg"
    $ dct_sfx_meow6 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow6.ogg"
    $ dct_sfx_meow7 = "mods/dublicate_completed/sounds/sfx/dct_sfx_meow7.ogg"
    $ dct_sfx_roar = "mods/dublicate_completed/sounds/sfx/dct_sfx_roar.ogg"
    
    ##### sfx (coin)
    
    $ dct_sfx_bus_braking = "<from 8.1 to 12.5>mods/dublicate_completed/sounds/sfx/dct_sfx_bus_arrival.ogg" #притормаживание автобуса
    # $ dct_sfx_loop_engine_noise_fast = "<from 1.43 to 10.8>mods/dublicate_completed/sounds/sfx/dct_sfx_bus_departure.ogg" #шум двигателя автобуса быстрый
    # $ dct_sfx_loop_engine_noise_slow = "<from 11.15 to 28.25>mods/dublicate_completed/sounds/sfx/dct_sfx_bus_arrival.ogg" #шум двигателя автобуса медленный
    # $ dct_sfx_bus_moves_between_stops = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_bus_moves_between_stops.ogg"
    $ dct_sfx_loop_bus_moves_slow = "<from 18.27 to 51.79>mods/dublicate_completed/sounds/coin/sfx/dct_sfx_bus_moves_between_stops.ogg" #звук автобуса, едущего медлено
    $ dct_sfx_UAZ_engine = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_UAZ_engine.ogg" # Заведённый УАЗ во сне Шурика
    $ dct_sfx_horn_dinner = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_horn_dinner.ogg" # Горн на обед
    $ dct_sfx_horn_dinner_through_loudspeaker = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_horn_dinner_through_loudspeaker.ogg" # Горн на обед через репродктор
    $ dct_sfx_horn_rise_through_loudspeaker = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_horn_rise_through_loudspeaker.ogg" # Горн-подъём через репродктор
    $ dct_sfx_robot_run_club_attic = "<to 2.6>mods/dublicate_completed/sounds/coin/sfx/dct_sfx_robot_run_club_attic.ogg" # Яна пробегает по чердаку клуба
    $ dct_sfx_record_crackling = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_record_crackling.ogg" # Потрескивание старой пластинки
    $ dct_sfx_sveta_falls_in_gym = "mods/dublicate_completed/sounds/coin/sfx/dct_sveta_falls_in_gym.ogg" # Света падает в спортзале и вскрикивает
    $ dct_sfx_uv_call = "mods/dublicate_completed/sounds/coin/sfx/dct_sfx_uv_call.ogg" # Ты пойдёшь со мной? Пойдёшь? Пойдёшь? Ты со мной... Пойдёшь?
    
   
    
    
    ############
    #Переменные#
    ############
    
    $ d_sim = 0 #Сёмка
    $ d_prolog = 0
    $ d_ana = 0 #Анабасис
    $ d_dra = 0 #Год дракона
    $ d_nam = 0 #Имена в облаках
    $ d_shif = 0 #4 смена
    $ d_lin = 0 #Линия жизни
    $ d_miuki = 0 #Кошкиндом
    $ d_eff = 0 #Эффектор
    $ d_olga = 0 #Ольга
    $ d_coin = 0 #Монетка
    
    ###########
    #Персонажи#
    ###########
    
    $ d_sl = Character(u"Славяна", color="#d3a900", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    #$ d_sa = Character(u"Девушка", color="#d3a900", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Саша на остановке   !!!  Не требуется, так как есть дефолтный персонаж "slg", указывающий в качестве имени "Девушка" цветом Слави
    
    $ d_sm = Character(u"Двойник", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Сёмкины клоны
    $ d_s2 = Character(u"Второй", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_s1 = Character(u"Человек", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #СС до знакомства.
    $ d_ss = Character(u"Семён Семёнович", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_s3 = Character(u"Незнакомец", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Семен-физрук до знакомства с Ульяной мл.
    
    $ d_sz = Character(u"Сергей", color="#0089e1", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Сергей Зайцев
    $ d_oz = Character(u"Оксана", color="#4de2f3", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Оксана Зайцева
    $ d_gr = Character(u"Гришка", color="#4de2e7", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Гришка
    #$ d_va = Character(u"Вася", color="#5de2e7", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Вася (переехал вниз в coin)
    $ d_ar = Character(u"Артём", color="#6ef3f8", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Артём
    $ d_ar_voice = Character(u"Второй голос", color="#6ef3f8", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Артём голос
    
    
    $ d_ck = Character(u"Повариха", color="#f3974d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Бабуля
    $ d_bg = Character(u"Баба Глаша", color="#f3974d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_gd = Character(u"Глафира Денисовна", color="#f3974d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ kids = Character(u"Малышня", color="#4de227", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ voices = Character(u"Голоса", color="#4de227", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_cs = Character(u"Доктор", color="#fcef08", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_rb = Character(u'Робот', color="#6a7ca5", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_jn = Character(u'Яна', color="#6a7ca5", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_mt2 = Character (u'Оля', color="#01df31", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Эмоциональная матрица
    
    $ d_dk = Character (u'Дядька', color="#3dc65b", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Дядька/водитель
    $ d_vl = Character (u'Дядя Валера', color="#3dc65b", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_ge = Character (u'Незнакомка', color="#01df31", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Незнакомка-ОД в городе
    
    $ d_dy = Character(u"Динамик", color="#e91b1b", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_mp = Character (u'Мария Петровна', color="#01df31", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Соседка Алисы kind = nvl
    
    $ d_to = Character (u'Анатолий', color="#3BE620", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Толик
    $ d_t1 = Character (u'Толик', color="#3BE620", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_t2 = Character (u'Незнакомец', color="#3BE620", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    $ d_t3 = Character (u'Анатолий Васильевич', color="#3BE620", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_u1 = Character (u'Рыжая девушка', color="#e91b1b", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Ульяна_взрослая
    $ us_old = Character (u'Ульяна-большая', color="#e91b1b", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ d_hel = Character (u'Елена', color="#b956ff", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Альтер-эго Лены
    
    $ d_tie = Character (u'Галстук', color="#00ff00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Замдиректора "Вакуоли"
    
    $ d_vo_2 = Character (u'Первый голос', color="#00ff00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Собеседник Артёма"
    
    $ whisper = Character(u"Шёпот", color="#4de227", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000")
    
    $ mss = Character(u"Хозяйка", color="#f000ff", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Светлана, хозяйка кошки.
    $ ms_s = Character(u"Светлана", color="#f000ff", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Светлана, хозяйка кошки.
    $ mic = Character(u"Михаил", color="#00aa00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Михаил, муж Светланы.
    
    $ uv_cst = Character(u"Богиня", color="#4eff00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Юля-Баст
    $ uv_cgl = Character(u"Девушка-кошка", color="#4eff00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Юля-нека
    
    $ adl_sh1 = Character(u"Александр Сергеевич", color="#faed25", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Шурик-оригинал
    $ adl_sh2 = Character(u"\"Шурик\"", color="#faed25", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Шурик-оригинал
    

    
    ##### Персонажи (coin)
    
    $ ggname = ""    # Переменная для выбора имени главного героя
    $ d_gg = Character("[ggname]", color="#8ffad5", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Имя главного героя в заключительной главе последней книги
    $ d_gm = Character(u"Малявка", color="#f3974d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Глафира: мелкая
    $ d_us_nvl = Character(u"Ульяна: ", kind=nvl, color="#ff3200", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Ульяна в режиме NVL
    $ d_dv_nvl = Character(u"Алиса: ", kind=nvl, color="#ffaa00", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Алиса в режиме NVL
    $ d_ma_dv = Character(u"{color=#79cdf7}Максим{/color} | {color=#ffaa00}Алиса{/color}",what_color = "#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Максим | Алиса
    $ d_ma = Character(u"Максим", color="#79cdf7", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Максим
    $ d_ka = Character(u"Катя", color="#894f91", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Катя
    $ d_va = Character(u"Вася", color="#ac613a", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Вася
    $ d_sv = Character(u"Света", color="#55a022", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Света
    $ d_civ = Character(u"Тип в штатском", color="#9e414d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Гражданский из первого сна Шурика
    $ d_guys = Character(u"Ребятня", color="#4de227", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") # Средний отряд, собирательный термин
    $ d_jn_old = Character(u"Яна-старшая", color="#1457df", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Жена Александра
    $ d_jn_young = Character(u"Яна-младшая", color="#2c8df0", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Дочь Александра
    $ d_maj = Character(u"Майор", color="#658554", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") #Майор из третьего сна Шурика
    $ d_voice_me = Character(u"Голос", color="#e1dd7d", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") # ГОЛОС цветом как у Семёна
    
    $ d_voice_color = ""    # Переменная для смены цвета персонажа "Доносящийся голос"
    $ d_vocal_noise = Character(u"{color=[d_voice_color]}Доносящийся голос{/color}", color="#ffffff", what_color="#ffdd7d", drop_shadow = [(2,2)], drop_shadow_color = "#000", what_drop_shadow = [(2,2)], what_drop_shadow_color = "#000") # Голосовой шум, обрывки фраз на переферии
    
    

    
    
    #########
    #Эффекты#
    #########
    
    transform walking:
        pos (0,0)
        linear 0.3 pos (-4,-2)
        linear 0.3 pos (0,0)
        pos (0,0)
        linear 0.3 pos (4,-2)
        linear 0.3 pos (0,0)
        repeat
        
    transform running:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (25,25)
        ease 0.20pos (0, 0)
        ease 0.20pos (-25,25)
        repeat
        
    transform shiver:
        pos (-2,0)
        linear 0.1 pos (0,0)
        linear 0.1 pos (2,0)
        linear 0.1 pos (0,0)
        linear 0.1 pos (-2,0)
        repeat

    #######
    #Титры#
    #######
    
    $ dct_credits = "Модификация Дубликат для визуальной новеллы Бесконечное лето. На основе фанфика «Дубликат».\nМузыка, звуки и компьтерная графика из оригинальной новеллы.\nДополнительные звуки и музыка: https://noisefx.ru/ , https://freesound.org/ , https://vk.com/madx1 , http://freemusicarchive.org, https://audeeyah.com/ , https://www.bensound.com\nСтихи (а вообще-то песня) \"Демон Дороги\" с разрешения автора: Светланы Никифоровой (Алькор)\nДополнительные CG, спрайты и фоны и одежда: Mo~, Ив Нарвал, Kef34, М. Смолев, KunzDigital, Quandial, MarkTailor, Eru, UntitledExpression \nФон коридора административного корпуса предоставлен Дмитрием Зотовым. Часть фонов и отдельные арты взята из модов \"История одного пионера\", \"7 Дней лета\" и \"Булки, кефир и рок-н-ролл\".\nМеню: Лисёндра и Salo Tor.\nСюжет, сценарий, код: Двадцатьвторой (Тангейзер Вагнеров).\nАвтор модификации полностью принимает и горячо поддерживает лицензию оригинальной новеллы: CC BY-NC-SA 4.0\nК сожалению, пока не нашел модификаций, из которых взяты два фона железной дороги или указаний на авторов. Надо как-то решить этот вопрос, а то неприлично получается.\nВроде бы всё сказал?\nВсех благодарю за внимание к модификации."
    $ life_line_credits = "{color=#ffda7d} {size=36} {i} Как бы мне не было плохо, я должен вернуться.\n\nК этим серым воротам и к людям за ними.\n\nКаждый раз к одним и тем же, и каждый раз к совсем другим.\n\nС их бедами и радостями, с их мыслями и чувствами, с их мечтами и потерями.\n\nК опостылевшему распорядку и к бесконечному лету.\n\nПотому что иначе однажды мне станет некуда возвращаться.\n\nПотому что иначе мне останется только нежизнь.\n\nБез снов, без слов, без надежды.\n\nБез ожидания любви."
    $ effector_letter_1_credits = "{color=#ffda7d}{i}Что же ты, Рыжик, творишь?\n\nПочему ни с кем не советовалась? Знаешь, что здесь, на периферии, из тебя получатся только девочки-октябряточки, которым расти еще и расти?\nНо, что сделала — то сделала, я подожду.\n\nМы могли хотя бы в одном лагере с тобой оказаться, а сейчас как нам найти друг друга? Я просто не успею дотянуть до твоего проявления, я же сам через пару циклов отключусь.\nВ общем так, если прочитаешь это, ищи меня в лагере у Виолы и Толяныча, а там — ориентируйся сама. И, когда найдешь, попробуй сказать мне: „Ты здесь не просто так!“ — может быть, это и сработает.\nГоворят, есть такая вещь, как самовнушение. Вот я и попробую самовнушиться. Я не знаю, как это делать, но я попробую, как могу.\n\nА если я проснусь первым, значит, мне останется только найти именно тебя (всего ничего, конечно, найду) и терпеливо ждать и надеяться.\n\nСобрал в эту папку все, что касалось нас с тобой, хоть чуть-чуть. Все отчеты по нашей работе, может быть, это поможет тебе вспомнить, или, может, это мне поможет вспомнить.\n\nЯ тебя тоже люблю. С.{/i}"
    $ effector_letter_2_1_credits = "{color=#ffda7d}{i}Привет, Сёмка. Жаль, что мы разминулись, но так, наверное, к лучшему. Потому что иначе ты будешь меня отговаривать, будешь ругаться и запрещать, мы поссоримся, а я все равно сделаю это.\nСём, сейчас ты уже конечно знаешь, что объявлена эвакуация персонала. Может быть знаешь, что я не уехала ни в первой очереди, ни во второй, — конечно уже знаешь. Из-за тебя, Сёмк, зануды и тормоза, и не уехала.\nВ общем, я остаюсь. Сразу меня не хватятся, пока не начнут последний персонал вывозить, а там мне уже будет все-равно.\n\nКое-кто, по слухам, еще остается, например, бабуля, но я не хочу как они. Я хочу быть с тобой, как ты и только как ты, понимаешь ты это?\nДелить твою жизнь и судьбу с тобой, и делиться своей жизнью и судьбой тоже с тобой!\nЯ знаю, Сём, ты сейчас ругаешься, но и рад этому, я уже слишком хорошо тебя знаю.\nЭтой ночью будет туман, тот самый, который мне нужен. Домик у тебя экранирован, а сарай — нет.\nПоэтому студентка третьего курса Ульяна пойдет вечером в сарай, а оттуда уже не выйдет. А вместо нее, через четыре цикла, появятся полсотни маленьких Ульянок: все копии, а одна — неиницированный подлинник.\nТолько инициировать его будет некому, оригинала-то не будет. Так что ты просто помни, что я — это я. Оригинал ли, подлинник ли — неважно. Все равно это я, и я тебя люблю.\n\nТвоя Ульяна.{/i}"
    $ effector_letter_2_2_credits = "{color=#ffda7d}{i}P.S. Уже темнеет, и туман на краю леса показался, пора идти в сарай, а я сижу и вспоминаю.\nКак ты демонстративно игнорировал меня, как я обиделась и пожаловалась твоему шефу. Я даже не знала тогда, что он твой оригинал.\nКак я в чистом поле попала под ливень, а ты заметил меня и прибежал спасать, и как мы укрывались потом от ливня вдвоем, под твоим огромным плащом.\nКак ты, чтобы напугать и оттолкнуть меня, рассказал все о себе. Хотел оттолкнуть, а не получилось — я не испугалась, а всего лишь подумала что ты доверяешь мне и заинтересовалась тобой. Знаешь, Сёмка, доверие и интерес — родители любви.\nКак я начала присматриваться к тебе.\nВспоминаю, как мы наперегонки бежали вверх по лестнице, той, что на обрыве, как я тайком вывозила тебя наружу по пропуску твоего оригинала (Твой шеф лежал в медпункте и я пошла к Виолетте Церновне и все ей про нас рассказала, она и отдала мне этот пропуск на три дня. Она очень хороший человек, Сём), как случайно встретили моих родителей. Я знаю, ты киваешь головой, но правда случайно, Сёмка!\nЭто наша и только наша неделя в нашем домике!\nДа, домик наш, а не твой, после всего я имею на него право. Сейчас я здесь у нас наведу порядок и пойду.\nБуду сидеть в сарае и вспоминать, пока смогу. Может быть и {s}этим{/s} {s}Ульянке-подлиннику{/s} {u}мне{/u} потом легче вспомнить всё будет.\n\nЗнаешь, Сёмк, если бы ты воевал со всем миром, то я бы стояла у тебя за спиной и подавала патроны. Да я знаю, что это сказала Ева Браун, но ведь может же и Ева Браун сказать правильные слова.\n\nНе прощаюсь. Вероятность нашей встречи целых 0,3\%, это я тебе как любимая студентка бабули говорю. А это значит, что никуда мы друг от друга не денемся!\n\nСёмка, Сёмка, Сёмочка…{/i}"
    $ effector_letter_3_credits = "{color=#ffda7d}{i}Дорогой „потомок“. Какого х ты третируешь несчастную девочку? Я знаю о твоем к нам отношении, и претензий к тебе не имею, но она-то тут причем?\nОна даже не подозревает о вашем существовании! Ты для нее просто „охамевший малолетка“!\nА делает она, между прочим, работу именно по твоей (я не виноват, что не могу твое авторство указать, сам знаешь почему) теме! Как руководитель заявляю: или ты помогаешь ей делать все измерения, пока она здесь на практике, или ты свободен!\nСам же ко мне пришел и ныл, что хочешь осмысленности, так работай! Или выметайся и „существуй и прозябай“ (твой термин, между прочим) в качестве контрольного организма!\n\nВыключать тебе сознание я не буду, этого удовольствия и доказательства твоей моральной правоты ты от меня не дождешься!\nИ не показывайся мне на глаза, пока я не остыну! Со мной же ты работаешь?! Вот и с ней работай!{/i}"
    


label dublicate_completed:

    $ dct_ending_var = False
    
    stop ambience
    stop music
    stop sound
    stop sound_loop
    
    jump dct_intro


