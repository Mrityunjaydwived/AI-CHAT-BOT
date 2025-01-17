import pyautogui
import time
import pyperclip  # For clipboard access
import google.generativeai as genai

genai.configure(api_key="AIzaSyBAUP2S02i_aqJ9dJyqvGT1QJzu_XTu0nw")
  

def is_last_message_from_sender(chat_log, sender_name="Mahesh Patidar Room Mate"):
   messages = chat_log.strip().split("/2025")[-1]
   if sender_name in messages:
      return True
   return False
  
pyautogui.click(1240,1051)
time.sleep(5) 


while True:
  

   # Step 1: Click on an chrome icon at (1203, 1042)
 
    # Wait for any UI changes

   # Step 2: Drag to select text
   pyautogui.moveTo(548,196)
   pyautogui.dragTo(643,1017, duration=1, button='left')

   # Step 3: Copy the selected text to the clipboard
   pyautogui.hotkey('ctrl', 'c')
   pyautogui.click(548,196)
   time.sleep(0.5)  # Allow clipboard operation to complete

   # Step 4: Get the text from the clipboard
   chat_history = pyperclip.paste()

# Print the text to verify
   print("chat_history")

   if is_last_message_from_sender(chat_history):

# Use the variable `text` as needed
      model = genai.GenerativeModel("gemini-1.5-flash")
      response = model.generate_content(f"you are a person named harry. you are from India.also your response within ten word. you analyze chat history and respond like harry. {chat_history} ")

      res = response.text
      pyperclip.copy(res)

      pyautogui.click(762,1039)
      time.sleep(1)

      pyautogui.hotkey('ctrl','v')
      time.sleep(1)

      pyautogui.press('enter')
