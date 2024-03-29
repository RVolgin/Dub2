init:

    ### Свеча
    
    $ dct_Freiheit = "mods/dublicate/sounds/music/Freiheit(by_Schiller).ogg"


    screen dct_epitaph_screen: 
        add "mods/dublicate/images/gui/dct_bg_table.jpg"   
        add "mods/dublicate/images/gui/dct_bg_menu.png"   
        add "mods/dublicate/images/gui/epitaph/dct_ep_photo.png"
        add "mods/dublicate/images/gui/dct_menu_flower.png"
        viewport id "dct_epitaph_vp":   # Вьюпорт — это контейнер, в который помещается текстовый блок. У вьюпорта есть уникальный id, чтобы к нему можно прикрутить персональную полосу прокрутки.
            xsize 1000
            ysize 800
            xpos 0.55
            ycenter 0.5
            draggable True      # Перетаскивание текста мышью (или пальцем, если на смартфоне)
            mousewheel True     # Прокрутка текста колёсиком мыши
            
            text '{space=150}{i}«...тот же лес, тот же воздух и та же вода,{/i}\n{space=300}{i}только ты не вернулся...»{/i}\n\n{space=40}Леонид Жилеев родился летом 67 года прошлого века в семье молодых инженеров. Он, как и всё поколение людей 60-70-х годов рождения, всё же больше из прошлого века, как ни крути. Это и все формы школьных организаций тех лет: октябрята, пионерия, комсомол, разные бесплатные кружки; и беззаботное, с очень умеренным контролем родителей, детство; и свободные от машин дороги; и обязательная армия, институт; и дефициты всего, и радости от очень простых вещей; какие-то, возможно, старомодные, но очень базовые, ключевые понятия и навыки, которые стальным, неубиваемым болтом были вкручены в нас всех. Всех тех, кто успел пожить и пообщаться вживую с людьми, которые воевали в годы Великой Отечественной войны. Лёня не особо ценил и отмечал какие-то дежурные праздники, но День Победы был для него священным праздником, и это было искренне.\n\n{space=40}У него была фантастическая память и понимание всего. Человек при этом читал и поглощал информацию, можно сказать, тоннами; фильтровал, конечно, но читал и анализировал очень много. Вначале это были книги, журналы, статьи, затем благословенный интернет с его возможностями. Все цепочки и прошедших, и последующих исторических и житейских событий складывались им в совершенно логическом порядке. Конечно, он не был каким-то пророком или философом, но если нужно было его мнение о чём-то, то он мог дать очень грамотный комментарий. Лёня знал и понимал намного больше других, это не в обиду сказано кому-то, это правда. Он был очень незаурядным человеком — умным, думающим, в постоянном поиске… Даже не могу сказать, что именно он искал; наверное, ему просто было очень интересно жить каждый день, открывать что-то новое для себя или же находить подтверждения своим каким-то мыслям и предположениям. Мне всегда казалось, что с его природными возможностями при желании он мог бы добиться просто грандиозной карьерной или жизненной реализации. Но ему это просто не было нужно, на подобные вопросы он всегда улыбался и говорил: «а зачем?..». В чём-то он даже казался, а может и был, слегка пофигистом, как он сам говорил: «Я не ленюсь, я прокрастинирую..».\n\n{space=40}До него я и слов таких не знала, да и вообще до него о многих вещах не подозревала, он открывал каждый раз что-то новое для меня. Это теперь я понимаю, что Лёня был просто очень самодостаточным человеком, ему хватало собственной оценки своей значимости в этом мире, а к похвалам со стороны он относился с благодарностью и уважением, но и с иронией. Мы вообще постоянно шутили и смеялись. Не обидно, без злобы, и не над кем-то, чаще над собой, и именно весело, ещё и с какой-нибудь известной киношной фразой. Лёня был вообще человек в целом по жизни очень простой, без претензий и капризов. Но при этом с какими-то своими привычками и странностями, которым он был очень верен. Мы жили очень дружно и уединённо, общаясь с довольно небольшим количеством людей, но при этом нам никогда не было скучно. Лёня всегда любил порядок и последовательность во всём. Всё выстраивал заранее, что-то прописывал, прорисовывал, советовался, а потом воплощал. Если выстроенная им намеченная траектория дел где-то сдвигалась или менялась — не любил этого, ворчал. Спонтанность пробивалась в неожиданно, без повода подаренных цветах, в какой-нибудь незапланированной поездке с утра в выходной.\n\n{space=40}Его увлечение эпистолярным жанром, думаю, возникло от той же неуёмной жажды к познаниям всего и вся и к литературе. Но и к общению, конечно. К общению с интересными людьми, близкими ему по духу. И людей таких, как я впоследствии убедилась, было немало. Повторюсь, что в реальной жизни Лёня был человек замкнутый и малообщительный. Причём неожиданна была его направленность в стиле Фэнтези и именно на подростковую аудиторию. Он как-то очень благосклонно, одновременно и с уважением, и с юмором относился к этим ещё не взрослым ребятам, но уже имеющим свою точку зрения на всё. И очень ценил отклики на его сочинения именно от юных читателей, считал их оценку самой объективной и неподкупной.\n\n{space=40}Мне было дано судьбой прожить с Лёней целых 14 лет. И я безмерно благодарна господу, что мы встретились, подружились и полюбили друг друга. Хотя изначально он казался мне существом с другой планеты. Но потом я поняла, как мне безумно повезло быть рядом с таким человеком, пусть даже не так долго, как хотелось бы. Не знаю, получил ли он что-то от общения и жизни со мной, но я точно стала лучше.\n\n{space=40}Благодарю его за всё и очень сильно скучаю.':
                xpos 0.5
                ypos 0.1
                xmaximum 565
                justify True
                color "#001e3c"
                font "mods/dublicate/fonts/OpenSans-Regular.ttf"
                size 18
                #outlines [(1, '#000', 0, 0)]
                
        vbar value YScrollValue("dct_epitaph_vp"):      # Полоса прокрутки. Привязана к id "dct_epitaph_vp", т.е. к расположенному выше вьюпорту.
           ysize 810
           pos (1640, 135)
            
        imagebutton:
            pos (0.155, 0.86)
            auto "mods/dublicate/images/gui/epitaph/dct_stamp_menu_%s.png"
            action [Hide("dct_epitaph", transition=Dissolve(0.2)), Jump("dct_epitaph_closed")]
 

label dct_epitaph:

    play music dct_Freiheit fadein 1
    call screen dct_epitaph_screen with Dissolve(0.2)   
    $ renpy.block_rollback()    # Запрет отката истории (чтоб колёсиком случайно не накрутили)


label dct_epitaph_closed:
    stop music fadeout 0.2
    jump dct_mnu2
    
    
    
    
    
    
    