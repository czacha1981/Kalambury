import streamlit as st
import random

# Talia kart (symbol, wartość)
deck = [
    ("♥", i) for i in range(2, 15)
] + [("♦", i) for i in range(2, 15)] + [("♣", i) for i in range(2, 15)] + [("♠", i) for i in range(2, 15)]

# Funkcja do losowania karty
def draw_card():
    return random.choice(deck)

st.title("Gra karciana: Wojna")

if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0

# Przycisk do losowania kart
if st.button("Dobierz kartę"):
    player_card = draw_card()
    computer_card = draw_card()

    st.write(f"**Twoja karta:** {player_card[0]} {player_card[1]}")
    st.write(f"**Karta komputera:** {computer_card[0]} {computer_card[1]}")

    if player_card[1] > computer_card[1]:
        st.success("Wygrałeś rundę!")
        st.session_state.player_score += 1
    elif player_card[1] < computer_card[1]:
        st.error("Przegrałeś rundę!")
        st.session_state.computer_score += 1
    else:
        st.warning("Remis!")

st.write(f"**Twój wynik:** {st.session_state.player_score}")
st.write(f"**Wynik komputera:** {st.session_state.computer_score}")

# Przycisk resetowania gry
if st.button("Resetuj grę"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.write("Gra zresetowana!")

