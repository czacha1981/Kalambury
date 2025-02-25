import random
import os
import time

HIGHSCORE_FILE = "highscore.txt"
MAX_HIGHSCORES = 5  # Liczba przechowywanych najlepszych wyników

# Lista zagadek (dla uproszczenia skrócona)
zagadki = [

  

    ("""
      (__)    
      (oo)    
 /------\/  
/ |    ||   
*  /---\   
   ~~   ~~  
    """, "Krowa", ["Pies", "Krowa", "Owca", "Koza"]),
     ("""
     (o.o)  
     <(   )>  
      (   )   
     """, "Sowa", ["Sowa", "Krowa", "Koń", "Kangur"]),
  

    # 3
    ("""
     (\_/)
     (o.o)
     (> <)
    """, "Królik", ["Królik", "Mysz", "Chomik", "Żaba"]),

    # 4
    ("""
     (\__/)
     (='.'=)
     (")_(")
    """, "Kot", ["Kot", "Zając", "Mysz", "Lis"]),

    
    # 6
    ("""
     /\_/\\
    ( o.o ) 
     >  ~  <  
    """, "Kot", ["Kot", "Szczur", "Wiewiórka", "Sowa"]),

    # 7
    ("""
     (o_o) 
    --(  )--
      (  )
    """, "Robot", ["Robot", "Kosmita", "Lampa", "Dinozaur"]),

    # 8
    ("""
      (o_o)
     --( )--  
       ( )  
    """, "Kosmita", ["Kosmita", "Robot", "Duch", "Goryl"]),

    # 9
    ("""
      ^____^
     /      \\
    |  ~  ~  |
    |  0  0  |
     \______/
    """, "Misiu", ["Misiu", "Koń", "Wilk", "Kaczka"]),

    # 10
    ("""
      (o_o)
     (  -  )
      (   )  
    """, "Zombie", ["Zombie", "Duch", "Człowiek", "Mumia"]),

    
    
    # 13
    ("""
      @@@@@@  
     @ O  O @  
     @  --  @  
      @@@@@@  
    """, "Buźka", ["Buźka", "Piłka", "Księżyc", "Balon"]),

    # 14
    ("""
     \_(*_*)_/
    """, "Duszek", ["Duszek", "Koń", "Smok", "Kot"]),

    # 15
    ("""
     |￣￣￣￣|
     |  POMOC!  |
     |＿＿＿＿|
        ( o_o)
        /  |  
    """, "Człowiek", ["Człowiek", "Duch", "Kosmita", "Robot"]),

  

    # 30 - Pies
    ("""
      / \\__
     (    @\\____
     /         O
    /   (_____/
  /_____/   U
    """, "Pies", ["Pies", "Wilk", "Lis", "Królik"]),

# 31 - Kot
    ("""
      /\_/\  
     ( o.o ) 
      > ^ <
    """, "Kot", ["Kot", "Tygrys", "Rys", "Puma"]),

# 32 - Słoń
    ("""
       /  \\~~~/  \\
     (    o  o    )
      \\    --    /
       \\______/
      /        \\
    """, "Słoń", ["Słoń", "Hipopotam", "Nosorożec", "Koń"]),

# 33 - Żyrafa
    ("""
       /^ ^\\
      / 0 0 \\
      V\ Y /V
       / - \\
      /    |
      V__) ||
    """, "Żyrafa", ["Żyrafa", "Koń", "Krowa", "Lama"]),

# 34 - Kaczka
    ("""
      __
     <(o )___
      (  ._> /
       `----'
    """, "Kaczka", ["Kaczka", "Gęś", "Łabędź", "Pingwin"]),

# 35 - Rekin
    ("""
               , _
       _.-''` `'-.
      ( ooo      O)
       '-.,_______,.-'
    """, "Rekin", ["Rekin", "Delfin", "Wieloryb", "Ryba"]),

# 36 - Kaktus
    ("""
       _  _
      | || |
    -| || |-
      | || |
      | || |
      | || |
      |_||_|
    """, "Kaktus", ["Kaktus", "Drzewo", "Trawa", "Grzyb"]),

# 37 - Smutna chmura
    ("""
        .--.
     .-(    ).   
    (___.__)__)   
      ‘ ‘ ‘ ‘  
    """, "Chmura", ["Chmura", "Deszcz", "Bałwan", "Duch"]),

# 38 - Rower
    ("""
        O
      -|-
      / \\
    """, "Rower", ["Rower", "Człowiek", "Robot", "Kwiat"]),

# 39 - Gitara
    ("""
       _____
      |     |
      |     |
     /-------\\
    (         )
     \_______/
       || ||
       || ||
    """, "Gitara", ["Gitara", "Skrzypce", "Flet", "Trąbka"]),

# 40 - Drzewo
    ("""
       &&& &&  & &&
    && &\\/&\\|& ()|/ @, &&
    &\\/(/&/&||/& /_/)_&
       &&/&|/ /& &/ &/
        |/  |/
        |  |
        |  |
    """, "Drzewo", ["Drzewo", "Kaktus", "Trawa", "Góra"]),

# 41 - Rybka
    ("""
        ><(((('>
    """, "Rybka", ["Rybka", "Rekin", "Delfin", "Ośmiornica"]),

# 42 - Świnka
    ("""
      ^--^
     ( 'oo' )
     ( ---- )
    """, "Świnka", ["Świnka", "Hipopotam", "Pies", "Żółw"]),

# 43 - Ośmiornica
    ("""
      ((  ))
      ( O O )
      (  -  )
     /| | | |\\
    """, "Ośmiornica", ["Ośmiornica", "Meduza", "Delfin", "Rybka"]),

# 44 - Pingwin
    ("""
      (o_o)
      <(   )>
      (   )
    """, "Pingwin", ["Pingwin", "Kaczka", "Łabędź", "Gęś"]),

# 45 - Samochód
    ("""
      ______
     /|_||_\\`.__
    (   _    _ _\\
    =`-(_)--(_)-'
    """, "Samochód", ["Samochód", "Pociąg", "Motor", "Traktor"]),

# 46 - Samolot
    ("""
        __|__
--@--@--(_)--@--@--
    """, "Samolot", ["Samolot", "Rakieta", "Ptak", "Motyl"]),

# 47 - Balon
    ("""
      ,--.
     (    )
      `--'
      |  |
      |  |
      '--'
    """, "Balon", ["Balon", "Lampa", "Bałwan", "Beczka"]),

# 48 - Pszczoła
    ("""
      _     _
     ( o\\~~~/o )
      \\______/
      /      \\
    """, "Pszczoła", ["Pszczoła", "Motyl", "Komar", "Mucha"]),

# 49 - Nietoperz
    ("""
       _    _
      (o\\~~~/o)
       \\____/
    """, "Nietoperz", ["Nietoperz", "Sowa", "Orzeł", "Mysz"]),

# 50 - Księżyc
    ("""
        _..._
      .'     '.
     /  o   o  \\
    |    (_)    |
     \\  ~~~  /
      '.....'
    """, "Księżyc", ["Księżyc", "Słońce", "Gwiazda", "Chmura"]),

# 51 - Duch
    ("""
      .-"      "-.
     /            \\
    |              |
    |,  .-.  .-.  ,|
    | )(_o/  \\o_)( |
    |/     /\     \\|
    (_     ^^     _)
     \\__|IIIIII|__/
      | \\IIIIII/ |
      \\          /
       `--------`
    """, "Duch", ["Duch", "Kosmita", "Robot", "Płaszcz"]),

# 52 - Królik
    ("""
      (\(\  
      ( -.-) 
      o_(")(")  
    """, "Królik", ["Królik", "Mysz", "Chomik", "Żaba"]),

# 53 - Telefon
    ("""
     .----------------.
    |  .------------.  |
    | |  123456789  | |
    | |  *  0  #   | |
    |  '------------'  |
     '----------------'
    """, "Telefon", ["Telefon", "Kalkulator", "Zegarek", "Radio"]),

# 54 - Klucz
    ("""
        .--.
       /.-. '----------.
       \\ '-._______.-'
        '--'
    """, "Klucz", ["Klucz", "Miecz", "Śrubokręt", "Długopis"]),

# 55 - Zegar
    ("""
       ,--.
     _|__|_
    ( o o )
     |  | 
     |__|
    """, "Zegar", ["Zegar", "Robot", "Telefon", "Lampa"]),

    # 56 - Smok
    ("""
                 __
                (o )    ==<
                 ||      
    """, "Smok", ["Smok", "Dinozaur", "Wąż", "Krokodyl"]),



# 58 - Mumia
    ("""
      ||||||||
     ||      ||
     ||  0 0 ||
     ||  --- ||
      ||||||||
    """, "Mumia", ["Mumia", "Duch", "Zombie", "Robot"]),



# 60 - Pajęczyna
    ("""
       .     .
    '  |  |  '
    .--:--:--.
    '  |  |  '
       '  '
    """, "Pajęczyna", ["Pajęczyna", "Gwiazda", "Śnieżynka", "Słońce"]),

# 61 - Pirat
    ("""
     (⚆_⚆)
      (∩∩)
     /   |   
    """, "Pirat", ["Pirat", "Ninja", "Rycerz", "Złodziej"]),

# 62 - Zombiak
    ("""
       (o_o)
      --(  )--
        (  )
    """, "Zombie", ["Zombie", "Duch", "Mumia", "Kosmita"]),

# 63 - Rakieta
    ("""
       /^\\
      |---|
      | O |
     /|   |\\
    """, "Rakieta", ["Rakieta", "Samolot", "Lampa", "Kometa"]),

# 64 - Pistolet na wodę
    ("""
       ______
      |______|
       |  |
      |----|
    """, "Pistolet na wodę", ["Pistolet na wodę", "Mikrofon", "Latarka", "Drukarka"]),



# 66 - Pająk
    ("""
     (o.o)
     /(  )\\
    // || \\\\
    """, "Pająk", ["Pająk", "Krab", "Duch", "Ośmiornica"]),

# 67 - Pac-Man
    ("""
       ( ^>
    """, "Pac-Man", ["Pac-Man", "Buźka", "Pies", "Księżyc"]),

# 68 - Sokowirówka
    ("""
       _______
      |       |
      | O O O |
      |_______|
    """, "Sokowirówka", ["Sokowirówka", "Toaster", "Komputer", "Lodówka"]),






# 72 - Robot
    ("""
      [o_o]
     <(   )>
      ( | | )
    """, "Robot", ["Robot", "Kosmita", "Astronauta", "Zombiak"]),

# 73 - Kapelusz czarodzieja
    ("""
        /\\
       /  \\
      /____\\
    """, "Kapelusz czarodzieja", ["Kapelusz czarodzieja", "Trójkąt", "Góra", "Lampa"]),

# 74 - Piracki statek
    ("""
         ~ ~ ~
       ~ ~ ~ ~ ~
      |   ⚓   |
      |_______|
    """, "Piracki statek", ["Piracki statek", "Łódź podwodna", "Jacht", "Kajak"]),

# 75 - Duch w prześcieradle
    ("""
      .-"-.
     |     |
     | o o |
     |  ~  |
     '-----'
    """, "Duch", ["Duch", "Mumia", "Dinozaur", "Krab"]),

# 76 - Zegar kieszonkowy
    ("""
        .-'""'-.
       /   12   \\
      |    o    |
      | 9  o  3 |
      |    o    |
       \\__6__/
    """, "Zegar kieszonkowy", ["Zegar kieszonkowy", "Kompas", "Medal", "Moneta"]),

# 77 - Latający dywan
    ("""
       _____
      |     |
     (       )
      \\_____/
    """, "Latający dywan", ["Latający dywan", "Statek", "Łóżko", "Chleb"]),

# 78 - Kosmita z antenkami
    ("""
      (o_o)
     <(   )>
    --(   )--
    """, "Kosmita", ["Kosmita", "Robot", "Duch", "Lampa"]),



# 80 - Miecz świetlny
    ("""
       ||
       ||
       ||
      ||||
    """, "Miecz świetlny", ["Miecz świetlny", "Latarka", "Flara", "Pałka"]),



# 82 - Wielki nosorożec
    ("""
      (    )
     (  o  o  )
     (   ~    )
      \\_____/
    """, "Nosorożec", ["Nosorożec", "Słoń", "Hipopotam", "Krowa"]),



( """
          |    |    |
      |    |    |    |    |
  |  |  |  |  |  |  |  |  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" , "Piracki statek", ["Piracki statek", "Łódź", "Kajak", "Titanic"])

    
]

# Funkcja czyszcząca ekran
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Funkcja do centrowania tekstu
def center_text(text):
    terminal_width = os.get_terminal_size().columns
    centered_lines = [line.center(terminal_width) for line in text.split("\n")]
    return "\n".join(centered_lines)

# Wczytaj highscore'y
def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            lines = file.readlines()
            highscores = [line.strip().split(" - ") for line in lines]
            return [(name, int(score)) for name, score in highscores]
    return []

# Zapisz highscore'y
def save_highscores(highscores):
    with open(HIGHSCORE_FILE, "w") as file:
        for name, score in highscores[:MAX_HIGHSCORES]:
            file.write(f"{name} - {score}\n")

# Funkcja gry
def play_game():
    score = 0
    lives = 3
    used_questions = set()
    
    while lives > 0:
        clear_screen()
        print(center_text(f"⭐ WYNIK: {score}  ❤️ Życia: {lives}"))

        # Wybierz losową niepowtórzoną zagadkę
        available_questions = [i for i in range(len(zagadki)) if i not in used_questions]
        if not available_questions:
            print(center_text("\n🎉 BRAWO! Rozwiązałeś wszystkie zagadki!"))
            break
        q_index = random.choice(available_questions)
        used_questions.add(q_index)

        zagadka, poprawna, opcje = zagadki[q_index]

        # Wyświetl zagadkę
        print(center_text("\n" + zagadka + "\n"))
        random.shuffle(opcje)

        # Wyświetl odpowiedzi
        for i, opcja in enumerate(opcje):
            print(center_text(f"{i+1}. {opcja}"))

        # Pobierz odpowiedź gracza
        try:
            wybor = int(input("\n👉 Wybierz numer odpowiedzi: "))
            if opcje[wybor - 1] == poprawna:
                print(center_text("\n✅ DOBRZE! +10 pkt!"))
                score += 10
            else:
                print(center_text("\n❌ ZŁA ODPOWIEDŹ!"))
                lives -= 1
                print(center_text(f"Poprawna odpowiedź to: {poprawna}"))
        except (ValueError, IndexError):
            print(center_text("\n⚠️ Nieprawidłowy wybór! Straciłeś życie!"))
            lives -= 1

        time.sleep(2)

    # Game Over
    clear_screen()
    print(center_text("\n💀 GAME OVER! 💀"))
    print(center_text(f"Twój wynik: {score}"))

    # Sprawdź highscore
    highscores = load_highscores()
    if len(highscores) < MAX_HIGHSCORES or score > highscores[-1][1]:
        print(center_text("\n🎉 NOWY HIGHSCORE!"))
        name = input(center_text("\n📝 Wpisz swoje imię: "))
        highscores.append((name, score))
        highscores.sort(key=lambda x: x[1], reverse=True)  # Sortuj malejąco
        save_highscores(highscores)

    # Wyświetl highscore'y
    print(center_text("\n🏆 HIGHSCORES:"))
    for i, (name, highscore) in enumerate(highscores[:MAX_HIGHSCORES], 1):
        print(center_text(f"{i}. {name} - {highscore}"))

    input(center_text("\n🔁 Naciśnij ENTER, aby wrócić do menu..."))

# Menu gry
while True:
    clear_screen()
    print(center_text("""
  ██████╗ ███████╗███████╗███████╗ ██████╗ ███████╗
  ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝
    ██████╔╝█████╗  █████╗  █████╗   ██████╔╝███████╗
  ██╔══██╗██╔══╝  ██╔══╝  ██╔══╝   █╔══██╗╚════██╗
  ██████╔╝███████╗███████╗███████╗██║  ██║██████╔╝
  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝
        and Chips KALAMBURY w ASCII :))))   by Adam Kami
"""))
    print(center_text("\n1. 🎮 Start Gry"))
    print(center_text("2. 🏆 Highscore"))
    print(center_text("3. ❌ Wyjście"))

    choice = input("\n👉 Wybierz opcję: ")

    if choice == "1":
        play_game()
    elif choice == "2":
        highscores = load_highscores()
        print(center_text("\n🏆 NAJLEPSZE WYNIKI:"))
        for i, (name, highscore) in enumerate(highscores, 1):
            print(center_text(f"{i}. {name} - {highscore}"))
        input(center_text("\n🔁 Naciśnij ENTER, aby wrócić..."))
    elif choice == "3":
        break
    else:
        print(center_text("\n⚠️ Nieprawidłowy wybór!"))
        time.sleep(1)
