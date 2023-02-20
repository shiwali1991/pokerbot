import openai
import streamlit as st
import os

def get_poker_suggestions(game_type, num_players, pot_size, community_cards, position, opp_action, opp_tendency, hand_strength, stack_size, table_dynamics, bet_size):
    # Initialize OpenAI API key
    openai.api_key = os.getenv("OPEN_API_KEY")

    # Generate text using OpenAI GPT-3
    prompt = f"As an expert poker player, In a {game_type} game with {num_players} players, the pot size is {pot_size} and the community cards are {community_cards}. You are in {position} position and your opponents are playing {opp_action}. They tend to play {opp_tendency}. Your stack size is {stack_size} and your hand strength is {hand_strength}. The table dynamics are {table_dynamics} with bet of {bet_size}. What are the best actions you will take if you playing aggressive. Give top 2 actions in value 1-10 with 10 being the best?"
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    message = completions.choices[0].text.strip()
    return message

# Get user inputs from Streamlit app

game_type = st.selectbox("Select game type", ["No-Limit Hold'em", "Limit Hold'em", "Pot-Limit Omaha", "Seven-Card Stud", "Omaha Hi-Lo"])
num_players = st.selectbox("Select number of players", [2, 6, 7, 8, 9])
pot_size = st.selectbox("Select pot size", ["Small (less than 50 big blinds)", "Medium (50-100 big blinds)", "Large (more than 100 big blinds)"])
community_cards = st.selectbox("Select community cards", ["Flop (3 cards)", "Turn (4th card)", "River (5th card)"])
position = st.selectbox("Select your position", ["Early position", "Middle position", "Late position"])
opp_action = st.selectbox("Select opponents' actions", ["Tight", "Loose"])
opp_tendency = st.selectbox("Select opponents' tendencies", ["Passive", "Aggressive"])
hand_strength = st.selectbox("Select your hand strength", ["Weak", "Medium", "Strong"])
stack_size = st.selectbox("Select your stack size", ["Small stack (less than 20 big blinds)", "Medium stack (20-50 big blinds)", "Large stack (more than 50 big blinds)"])
table_dynamics = st.selectbox("Select table dynamics", ["Tight", "Loose"])
#bet_type = st.selectbox("Select type of bet", ["Raise", "Call", "Fold"])
bet_size = st.number_input("Enter bet size")

# Get poker suggestions and display them in the Streamlit app
suggestions = get_poker_suggestions(game_type, num_players, pot_size, community_cards, position, opp_action, opp_tendency, hand_strength, stack_size, table_dynamics, bet_size)
st.write(suggestions)
