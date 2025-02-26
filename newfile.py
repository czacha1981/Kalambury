import streamlit as st
import random

# Inicjalizacja zmiennych
achievements = []
endings = {
    "lost": "Zginąłeś w lesie, twoja podróż się skończyła. Może następnym razem będziesz mądrzejszy?",
    "found_treasure": "Znalazłeś skarb! Twoja podróż zakończyła się sukcesem. Zostałeś bohaterem w swojej wiosce!",
    "escaped": "Udało ci się uciec z lasu, ale nie znalazłeś żadnego skarbu. Twoja podróż była tylko częściowo udana.",
    "mysterious_disappearance": "Zniknąłeś bez śladu w lesie. Coś dziwnego się stało..."
}

# Funkcja do dodawania osiągnięć
def add_achievement(achievement):
    if achievement not in achievements:
        achievements.append(achievement)

# Funkcja do wyświetlania fabuły
def intro():
    st.title("Tajemniczy Las")
    st.write("Jest 6:00 rano, a ty stoisz na skraju tajemniczego lasu. Decyzja należy do ciebie. Co chcesz zrobić?")
    st.write("1. Wejść do lasu.")
    st.write("2. Zostać w wiosce i poczekać na lepsze warunki.")

def forest_entrance():
    st.write("Decydujesz się wejść do lasu. Otacza cię mrok, a ścieżki zdają się prowadzić w różnych kierunkach.")
    st.write("Nagle pojawia się przed tobą wybór:")
    st.write("1. Pójść w lewo, w stronę rzeki.")
    st.write("2. Pójść w prawo, w stronę gęstych drzew.")
    st.write("3. Zawrócić i wrócić do wioski.")

def forest_choice(choice):
    if choice == 1:
        river_path()
    elif choice == 2:
        dense_forest()
    elif choice == 3:
        st.write("Wracasz do wioski. Gra zakończona.")
        add_achievement("escape")
        show_achievements()

def river_path():
    st.write("Idziesz w stronę rzeki, gdzie widzisz zamek na wzgórzu.")
    st.write("1. Zbliżyć się do zamku.")
    st.write("2. Odpocząć nad brzegiem rzeki.")
    choice = st.radio("Wybór", ["Zamek", "Odpoczynek"])
    if choice == "Zamek":
        treasure_found()
    else:
        rest_and_escape()

def dense_forest():
    st.write("Wchodzisz w gęsty las. Dziwne dźwięki otaczają cię z każdej strony.")
    st.write("1. Podążać za dźwiękami.")
    st.write("2. Spróbować znaleźć ścieżkę powrotną.")
    choice = st.radio("Wybór", ["Ścieżka", "Dźwięki"])
    if choice == "Ścieżka":
        escaped()
    else:
        mysterious_disappearance()

def treasure_found():
    st.write("Docierasz do zamku, gdzie znajdujesz ukryty skarb!")
    st.write("Gratulacje, twoja podróż zakończyła się sukcesem!")
    add_achievement("found_treasure")
    show_achievements()

def rest_and_escape():
    st.write("Po chwili odpoczynku czujesz się zmęczony i decydujesz się wrócić do wioski.")
    add_achievement("escape")
    show_achievements()

def escaped():
    st.write("Po długiej wędrówce udaje ci się znaleźć wyjście z lasu, ale nie udało ci się znaleźć żadnego skarbu.")
    add_achievement("escaped")
    show_achievements()

def mysterious_disappearance():
    st.write("Dźwięki prowadzą cię w głąb lasu, ale tracisz orientację i znikaś bez śladu.")
    add_achievement("mysterious_disappearance")
    show_achievements()

def show_achievements():
    st.write("Twoje osiągnięcia:")
    for achievement in achievements:
        st.write(f"- {achievement}")

def game():
    intro()
    choice = st.radio("Wybór", ["Wejść do lasu", "Zostać w wiosce"])
    if choice == "Wejść do lasu":
        forest_entrance()
        choice = st.radio("Wybór", ["W lewo", "W prawo", "Zawrócić"])
        forest_choice(choice)
    else:
        st.write("Decydujesz się nie ryzykować i czekać na lepsze warunki w wiosce.")

if __name__ == "__main__":
    game()
    
