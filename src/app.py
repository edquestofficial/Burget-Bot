import google.generativeai as ai
import gradio as gr
import util as ut
import os
from dotenv import load_dotenv


# Configure api_key
ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the AI model based on the provided prompt
def get_response(prompt):
    response = chat.send_message(prompt)
    return response.text

# Define Model Instance
model = ai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


# Set the initial context for the chatbot, including instructions and the menu for the Burger Spot Restaurant
context =  ut.content() 

# create welcome message
context.append("")
response = get_response(context)

# Chatbot function to handle incoming messages and generate responses based on the context
def chatbot(message, history):
  prompt = message
  context.append(prompt)
  response = get_response(context)
  context.append(response)
  return response

# create gradio instance  & launch it
gr.ChatInterface(fn=chatbot, examples=["🍔🍟🥤", "classic burger", "fries", "Toppings: lettuce", "Drinks: coke/sprite/bottled water/juice"], title=response).launch(debug=True, share=True)
