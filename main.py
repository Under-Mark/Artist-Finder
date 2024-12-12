from tkinter import *
from PIL import Image, ImageTk  
import requests
import json
# Create main window


def search():
    song = SEARCH_ENTRY.get()
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={song}")
    song = response.json()
    

    if song['resultCount'] == 0:
        SHOW_ARTIST.config(text=f"No result found")
    for _ in song['results']:
        SHOW_ARTIST.config(text=f"Artist Name: {_['artistName']}")

WINDOW = Tk()
WINDOW.geometry('250x150')

# Title label
BOX_TITLE = Label(WINDOW, text='Artist Searcher')
BOX_TITLE.pack()

# Create a frame for the entry label and search entry
ENTRY_FRAME = Frame(WINDOW,pady=10)
ENTRY_FRAME.pack()  # Add some padding for better layout

# Entry label and input field inside the frame
ENTRY_LBL = Label(ENTRY_FRAME, text='Enter Song name: ')
ENTRY_LBL.grid(row=0, column=0, padx=5)  # Use grid to arrange inside the frame
SEARCH_ENTRY = Entry(ENTRY_FRAME,)
SEARCH_ENTRY.grid(row=0, column=1)


# Submit button outside the frame
SUBMIT_BUTTON = Button(WINDOW, text='Search Artist',command= search)
SUBMIT_BUTTON.pack(pady=10)


SHOW_ARTIST = Label(WINDOW,text='')
SHOW_ARTIST.pack()
# Run the application
WINDOW.mainloop()
