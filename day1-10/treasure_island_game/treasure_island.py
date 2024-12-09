#Treinar o inglês aqui né :p
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure or something else...")
choice1 = input("You can go explore the forest or the beach. Which one do you choose?\n        Type 'forest' or 'beach'.\n").lower()
if choice1 == "forest":
    print("""
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ 
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ 
      /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\ 
          """)

    choice2 = input("You find a cabin in the middle of the forest. Do you enter it or keep walking?\n        Type 'cabin' or 'walk'.\n").lower()
    if choice2 == "cabin":
        print(r"""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~~__~~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
            """)
        
        choice3 = input("You found a treasure map! Will you go to where the X marks the spot or head to the volcano?\n        Type 'X' or 'volcano'.\n").lower()
        if choice3 == "x":
            print(r'''
              __.-.__.-.__
            .'\ '-.__.-' /'.
           /  |    ,_    |  \
          /   |  _/| \_  |   \
          '-._/ \.-""-./ \_.-'
              | ( ^ \^ ) |
              |  \ == /  |
              |  /'--'\  |
              |          |
              '._      _.'
                 `""""`
                ''')

            print("You go to the spot where the X marked and there you find... a gift shop! At least you'll leave with a nice t-shirt!\n        THANKS FOR PLAYING!")
            #Joke ending
        elif choice3 == "volcano":
            print(r'''
         ____ /\ ____            _ _   --           - -__     -_
        /v y \/\/    \                   --  --___     _ __--__ -" _
       ____\7 \\_^_^/ \                            _ --        -_ "-_
      /    V/ \/   \ ^/\            __                          _--,_
     / \^\|/ \()^7_ \ ^|      /">^/",,\                        /"("\"\
    /\^   / \^_() 7_\        </">LX<"<,\                    _/"/"|\ )\>_
    |^    /\ ()_|  7|        / >/ >O-,\"                 _/"_." _/ / / \"\
          ^   \_\            ^" V"O^  V               /""_-" ,/"  /\  \ ) "-,_
               \_\              '  \>              _-"/ ( .-/ \ !   )  \ _\"-_"\_
 ___ ___ ______ \_\ _ _____ ___ ___ \> _ ___   _-"/_-"   / (    |  / \  | \  \_- "-_  __ _ _
       _  _ _-   \_\   --  -   - --  \">   -<_"__" /  _/|   \ \ | /! \  \  -_( _"-<_">-- -
              --  \_`>    _--    _ ___",">-____ _"> ""_" "--"--"-" "-"' "-"  '"  _
                   \__">      C"" -_O   "O-'           '">        __ -  -
         _ __()_ ___"-__"\__ __)    - O         __ - - "      - -
                ()   _">--"> _ .-- "      - """
                        """
                  ''')
            
            print("You try to climb the volcano, but it erupts immediately. You are completely incinerated by the lava.\n        GAME OVER!")
        else:
            print("You died because you couldn't make the decision.\n        GAME OVER!")
    elif choice2 == "walk":
        print(r'''
      /^\      /^\
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |  pb   | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'
              ''')
        
        choice3 = input("You encounter a huge, ferocious wolf. Do you decide to fight it or call for help?\n        type 'fight' or 'help'.\n").lower()
        if choice3 == "fight":
            print("Did you really think you could beat the wolf in a fight?\n        GAME OVER!")
        elif choice3 == "help":
            print(r"""
     ,.,
   ,((()),   Are you
  ,((/"\)),   okay?
  ,)\'-'/(,    /
  ((()'())) ---
  /')\_/('\
 / (_   _)|
 \ \)   ( |
  \       /
                  """)
            
            choice4 = input("You are saved by a native woman. You are injured. Do you decide to let her help you or try to go on alone?\n        Type 'help' or 'alone'.\n").lower()
            if choice4 == "help":
                print(r'''
      _____           _____
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  
             "8b d8"   
              `888'
                "
                      ''')
                
                print("She takes care of you, and with time you fall in love with their culture... and with her. You form a family and live together on the island for the rest of your days.\n        THANKS FOR PLAYING!")
                #Love ending
            elif choice4 == "alone":
                print("You try to continue your journey alone but end up dying from your injuries.\n        GAME OVER!")
            else:
                print("You died because you couldn't make the decision.\n        GAME OVER!")
        else:
            print("You died because you couldn't make the decision.\n        GAME OVER!")
    else:
        print("You died because you couldn't make the decision.\n        GAME OVER!")
elif choice1 == "beach":
    print(r'''
      __|__ |___| |\
      |o__| |___| | \
      |___| |___| |o \
     _|___| |___| |__o\
    /...\_____|___|____\_/
    \   o * o * * o o  /
-------------------------------
          ''')
    choice2 = input("You find a shipwreck on the beach. Do you decide to explore it or go to a nearby cave?\n        Type 'ship' or 'cave'.\n").lower()
    if choice2 == "ship":
        print(r"""
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//

              """)
        choice3 = input("While you explore the ship, pirates appear and give you an ultimatum: join them or die.\n        Type 'join' or 'die'.\n").lower()
        if choice3 == "join":
            print(r"""
                                                    .
                                                _._/|_
                      .                        (__( (_(
                     /|                   - '. \'-:)8)-.
                    ( (_..-..          .'     '.'-(_(-' 
           _~_       '-.--.. '.      .'         '  )8)  
        __(__(__     \      88 \    /            )(8(        \.    .
       (_((_((_(      8\     88 \.-'  .-.        )88 :       /\\  _X_ __ .
     \=-:--:--:--.     8)     88/__) /(e))       88.'        \#\\(__((_//\   .
    _,\_o__o__o__/,__(8(_,__,_'.'--' '--' _    _88.'..___,___,\_,,,|/_(Y(/__,__,___,___ldb
                \    '._''--..'-/88 ) 88)(8  \\  \              \w\_   /X/
                 8\ __.--''_--'( 8  ( 8/   88( )8 )              -' ' __ 
                  '8888--''     \ 8  \88   88| 88(                   /_/
                                )88  (88   ) ) 88\                  _ '
                               ( 8    )88 ( (   88\                /V
                                )8)   (8\'-8 )-. '8'.___ __
                                //     \8 '-//--'  '88-8.-'             H
                               ((     ((   ))     
                                \      \   (    X    
                                                                       Y
                                         X   __
                                            )_/  /\
                                             '  /W/
                                                \|
                  """)
            
            print("You join the pirates and immediately receive a cool hat and a parrot. You set sail with them, and your ship gets caught in a storm caused by... THE KRAKEN!")
            choice4 = input("You can try to escape by swimming or fight the creature alongside the rest of the crew.\n        Type 'swimm' or 'fight'.\n").lower()
            if choice4 == "swimm":
                print("You obviously drown.\n        GAME OVER!")
            elif choice4 == "fight":
                print("The boat is completely destroyed, and you wash ashore on... the same island as before. Time to start over.\n        THANKS FOR PLAYING!")
                #"Looping" end
            else:
                print("You died because you couldn't make the decision.\n        GAME OVER!")
        elif choice3 == "die":
            print("You already knew where this was going, right?\n        GAME OVER!")
        else:
            print("You died because you couldn't make the decision.\n        GAME OVER!")
    elif choice2 == "cave":
        print("You enter the cave and stumble upon something. When you look to see what it is... IT'S THE TREASURE CHEST! How did no one find it before? You leave, leaving the empty chest behind.\n        THANKS FOR PLAYING!")
        #Luck ending
    else:
        print("You died because you couldn't make the decision.\n        GAME OVER!")
else:
    print("You died because you couldn't make the decision.\n        GAME OVER!")