import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

# create the main window
root = tk.Tk()
root.title("Plagiarism Checker")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# create the UI elements for the file selection buttons
file1_label = tk.Label(root, text="Select File 1")
file1_btn = tk.Button(root, text="Browse", width=10)
file2_label = tk.Label(root, text="Select File 2")
file2_btn = tk.Button(root, text="Browse", width=10)

# create the UI elements for the plagiarism check button
check_btn = tk.Button(root, text="Check for Plagiarism", width=20)

# create the UI elements for displaying the similarity percentage
result_label = tk.Label(root, text="Similarity Percentage:")
result = tk.Label(root, text="0%")

# position the UI elements for the file selection buttons
file1_label.place(x=50, y=50)
file1_btn.place(x=250, y=50)
file2_label.place(x=50, y=100)
file2_btn.place(x=250, y=100)

# position the UI elements for the plagiarism check button
check_btn.place(x=100, y=150)

# position the UI elements for displaying the similarity percentage
result_label.place(x=50, y=200)
result.place(x=200, y=200)

# function to browse and select the file
def select_file():
    filename = filedialog.askopenfilename()
    return filename

# function to calculate the similarity percentage
def check_similarity():
    file1 = open(select_file(), 'r').read()
    file2 = open(select_file(), 'r').read()
    similarity_ratio = SequenceMatcher(None, file1, file2).ratio()
    similarity_percentage = str(round(similarity_ratio*100, 2)) + "%"
    result.config(text=similarity_percentage)

# bind the browse buttons to the select_file function
file1_btn.config(command=select_file)
file2_btn.config(command=select_file)

# bind the check for plagiarism button to the check_similarity function
check_btn.config(command=check_similarity)

# start the main loop
root.mainloop()
