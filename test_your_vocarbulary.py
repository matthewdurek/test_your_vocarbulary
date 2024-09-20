#Bread ideas : 
#Pun ideas : 'leaven the playing field'

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing from Pillow for PNG support
import random
import os

# Bread types list
BREADS = [
    'Arepa Bread', 'Babka Bread', 'Bagel', 'Baguette', 'Banana Bread', 'Bao Buns', 'Beer Bread',
    'Biscuits', 'Bread Pudding', 'Brioche Bread', 'Brown Bread', 'Challah Bread', 'Ciabatta Bread',
    'Cloud Bread', 'Corn Bread', 'Crumpets', 'English Muffin', 'Flatbread', 'Focaccia Bread', 
    'Garlic Bread', 'Gluten-Free Bread', 'Hokkaido Bread', 'Irish Soda Bread', 'Italian Bread', 
    'Monkey Bread','Multigrain Bread', 'Naan Bread', 'Paratha Flatbread', 'Pita Bread', 'Potato Bread',
    'Pumpernickel Bread', 'Quick Bread', 'Rye Bread', 'Sourdough Bread', 'Sprouted Grain Bread', 
    'White Bread', 'Whole Wheat Bread'
]

breads = BREADS.copy() #bread is in fact bread.

# Initialize the root Tkinter window
root = tk.Tk()
root.title("Test Your Vocarbulary")
root.geometry("800x600")

# Global variables to track score and current question
current_question = 0
score = 0
selected_bread = None
answer_buttons = []
question_frame = None #Store the current question frame

# Function to check the selected answer
def check_answer(answer):
    global score, current_question
    if answer == selected_bread:
        score += 1
    current_question += 1
    if current_question < len(BREADS): #MUST BE ADJUSTED when adding new breads 
        display_question()
    else:
        end_quiz()

# Function to end the quiz and show the final score with appropriate message
def end_quiz():
    global score
    total_questions = len(BREADS)
    percentage = (score / total_questions) * 100
    # Determine message based on percentage of total correct
    if percentage <= 15:
        message = "You're toast!"
    elif percentage <= 30:
        message = "Your knowledge is kinda crusty..."
    elif percentage <= 50:
        message = "Kneads improvement."
    elif percentage <= 70:
        message = "More proofing required."
    elif percentage <= 85:
        message = "Bread is the yeast of your worries!"
    elif percentage < 100:
        message = "You sliced right through it!"
    else:
        message = "You got all that bread!"

    # Show the final score and message
    messagebox.showinfo("Quiz Complete", f"Your score: {score}/{total_questions} ({percentage:.2f}%)\n{message}")
    root.quit()

# Function to display a random question with bread image and 4 options
def display_question():
    global selected_bread, answer_buttons, image_label, question_frame
    
    # Destroy the previous question frame if it exists
    if question_frame is not None:
        question_frame.destroy()

    # Clear previous buttons
    for btn in answer_buttons:
        btn.destroy()

    # Create a frame to hold the image and buttons and center it
    question_frame = tk.Frame(root)
    question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 
    # Choose a random bread for the current question
    selected_bread = random.choice(breads) 
    breads.remove(selected_bread)
    
    # Load the bread image
    bread_image_path = os.path.join("images", f"{selected_bread}.png")  # Adjust the path to the 'images' folder

    # Log the path to see if its correct
    print(f"Loading image from {bread_image_path}")
    print(os.getcwd())
    
    if os.path.exists(bread_image_path):
        try:
            # Use PIL to open and resize the image, then convert to Tkinter format
            image = Image.open(bread_image_path)
            width, height = image.size #Grabs x & y values
            maxvalue = 300
            ratio = maxvalue/image.height
            image = image.resize((int(width*ratio), int(height*ratio))) #Aspect ratio adjustment
            bread_image = ImageTk.PhotoImage(image)
            image_label = tk.Label(question_frame, image=bread_image)
            #image_label.config(image=bread_image)
            image_label.image = bread_image  # Keep reference to avoid garbage collection
            image_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading image: {e}")
            # Show a grey box as a placeholder in case of error
            bread_image = ImageTk.PhotoImage(Image.new("RGB", (300, 300), color="grey"))
            image_label.config(image=bread_image)
            image_label.image = bread_image  # Keep reference to avoid garbage collection
            image_label.pack(pady=20)
    else:
        print(f"Image not found at: {bread_image_path}")
        # Placeholder if image is not found
        bread_image = ImageTk.PhotoImage(Image.new("RGB", (300, 300), color="gray"))
        image_label = tk.Label(question_frame, image=bread_image)
        #image_label.config(image=bread_image)
        image_label.image = bread_image  # Keep reference to avoid garbage collection
        image_label.pack(pady=20)
    
    # Generate 3 random wrong answers
    wrong_answers = random.sample([bread for bread in BREADS if bread != selected_bread], 3)
    
    # Combine correct and wrong answers
    options = wrong_answers + [selected_bread]
    random.shuffle(options)
    
    # Display answer buttons
    answer_buttons = []
    for i, option in enumerate(options):
        btn = tk.Button(question_frame, text=option, command=lambda opt=option: check_answer(opt), font=("Times New Roman", 14))
        btn.pack(pady=5)
        answer_buttons.append(btn)

# Function to display the menu screen
def display_menu():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to hold all the widgets and center it
    menu_frame = tk.Frame(root)
    menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Display the question
    question_label = tk.Label(menu_frame, text="Will you rise to the occasion?", font=("Times New Roman", 18))
    question_label.pack(pady=20)

    # Display the buttons
    bready_button = tk.Button(menu_frame, text="I'm bready!", font=("Times New Roman", 14), command=start_quiz)
    bready_button.pack(pady=10)

    gluten_free_button = tk.Button(menu_frame, text="Gluten-Free Option", font=("Times New Roman", 14), command=root.quit)
    gluten_free_button.pack(pady=10)

# Function to start the quiz
def start_quiz():
    # Clear the menu
    for widget in root.winfo_children():
        widget.destroy()

    # Display the first question
    global image_label
    image_label = tk.Label(root, text="Image will appear here", width=1000, height=300)
    image_label.pack(pady=20)
    display_question()

# Display the initial menu
display_menu()

# Run the Tkinter main loop
root.mainloop()