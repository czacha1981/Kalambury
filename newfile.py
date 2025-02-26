import streamlit as st

# Inicjalizacja zmiennych
if "achievements" not in st.session_state:
    st.session_state.achievements = []

endings = {
    "lost": "Zginąłeś w lesie, twoja podróż się skończyła. Może następnym razem będziesz mądrzejszy?",
    "found_treasure": "Znalazłeś skarb! Twoja podróż zakończyła się sukcesem. Zostałeś bohaterem w swojej wiosce!",
    "escaped": "Udało ci się uciec z lasu, ale nie znalazłeś żadnego skarbu. Twoja podróż była tylko częściowo udana.",
    "mysterious_disappearance": "Zniknąłeś bez śladu w lesie. Coś dziwnego się stało..."
}

# Funkcja do dodawania osiągnięć
def add_achievement(achievement):
    if achievement not in st.session_state.achievements:
        st.session_state.achievements.append(achievement)

# Funkcja do wyświetlania fabuły
def intro():
    st.title("Tajemniczy Las")
    st.write("Jest 6:00 rano, a ty stoisz na skraju tajemniczego lasu. Decyzja należy do ciebie. Co chcesz zrobić?")
    choice = st.radio("Wybór", ["Wejść do lasu", "Zostać w wiosce"])
    if choice == "Wejść do lasu":
        st.session_state.game_step = "forest_entrance"
    else:
        st.session_state.game_step = "village_wait"

def forest_entrance():
    st.write("Decydujesz się wejść do lasu. Otacza cię mrok, a ścieżki zdają się prowadzić w różnych kierunkach.")
    choice = st.radio("Wybór", ["W lewo, w stronę rzeki", "W prawo, w stronę gęstych drzew", "Zawrócić i wrócić do wioski"])
    if choice == "W lewo, w stronę rzeki":
        st.session_state.game_step = "river_path"
    elif choice == "W prawo, w stronę gęstych drzew":
        st.session_state.game_step = "dense_forest"
    else:
        st.session_state.game_step = "village_wait"

def river_path():
    st.write("Idziesz w stronę rzeki, gdzie widzisz zamek na wzgórzu.")
    choice = st.radio("Wybór", ["Zbliżyć się do zamku", "Odpocząć nad brzegiem rzeki"])
    if choice == "Zbliżyć się do zamku":
        st.session_state.game_step = "treasure_found"
    else:
        st.session_state.game_step = "rest_and_escape"

def dense_forest():
    st.write("Wchodzisz w gęsty las. Dziwne dźwięki otaczają cię z każdej strony.")
    choice = st.radio("Wybór", ["Podążać za dźwiękami", "Spróbować znaleźć ścieżkę powrotną"])
    if choice == "Podążać za dźwiękami":
        st.session_state.game_step = "mysterious_disappearance"
    else:
        st.session_state.game_step = "escaped"

def treasure_found():
    st.write("Docierasz do zamku, gdzie znajdujesz ukryty skarb!")
    st.write("Gratulacje, twoja podróż zakończyła się sukcesem!")
    add_achievement("found_treasure")
    st.session_state.game_step = "show_achievements"

def rest_and_escape():
    st.write("Po chwili odpoczynku czujesz się zmęczony i decydujesz się wrócić do wioski.")
    add_achievement("escaped")
    st.session_state.game_step = "show_achievements"

def escaped():
    st.write("Po długiej wędrówce udaje ci się znaleźć wyjście z lasu, ale nie udało ci się znaleźć żadnego skarbu.")
    add_achievement("escaped")
    st.session_state.game_step = "show_achievements"

def mysterious_disappearance():
    st.write("Dźwięki prowadzą cię w głąb lasu, ale tracisz orientację i znikaś bez śladu.")
    add_achievement("mysterious_disappearance")
    st.session_state.game_step = "show_achievements"

def show_achievements():
    st.write("Twoje osiągnięcia:")
    for achievement in st.session_state.achievements:
        st.write(f"- {achievement}")
    st.write("Chcesz spróbować jeszcze raz?")
    retry = st.radio("Wybór", ["Tak", "Nie"])
    if retry == "Tak":
        st.session_state.game_step = "intro"
    else:
        st.write("Dziękujemy za grę!")

# Główna funkcja gry
def game():
    if "game_step" not in st.session_state:
        st.session_state.game_step = "intro"

    if st.session_state.game_step == "intro":
        intro()
    elif st.session_state.game_step == "forest_entrance":
        forest_entrance()
    elif st.session_state.game_step == "river_path":
        river_path()
    elif st.session_state.game_step == "dense_forest":
        dense_forest()
    elif st.session_state.game_step == "treasure_found":
        treasure_found()
    elif st.session_state.game_step == "rest_and_escape":
        rest_and_escape()
    elif st.session_state.game_step == "escaped":
        escaped()
    elif st.session_state.game_step == "mysterious_disappearance":
        mysterious_disappearance()
    elif st.session_state.game_step == "show_achievements":
        show_achievements()
    elif st.session_state.game_step == "village_wait":
        st.write("Decydujesz się nie ryzykować i czekać na lepsze warunki w wiosce. Gra zakończona.")
        st.session_state.game_step = "show_achievements"

if __name__ == "__main__":
    game()
    
