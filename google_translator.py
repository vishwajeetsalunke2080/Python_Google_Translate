#necessary Imports 
from gtts import gTTS
import tkinter as tk
from scipy.io.wavfile import write 
import json
from google_trans_new import google_translator
import wavio as wv
from tkinter import messagebox
from tkinter import ttk
import sounddevice as sd
from tkinter import *
import os
import speech_recognition as sr
from tkinter.messagebox import *
from tkinter.filedialog import *
import requests


#root initialization
root=tk.Tk()
root.title("Google Translator")
root.geometry('1000x240')


#arrays for language selection

gtts = ['af', 'ar', 'bn', 'bs', 'ca', 'cs', 'cy', 'da',
'de', 'el', 'en', 'eo', 'es', 'et', 'fi', 'fr', 'gu', 'hi',
'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'km', 'kn',
'ko', 'la', 'lv', 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pl',
'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv', 'sw',
'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi']


#functions of program
def Translation_Function():
    try:
        translator_input = user_input_textbox.get("1.0","end")
        translation_output = answer_textbox.get("1.0","end")
        translator = google_translator()
        source = translator.detect(translator_input)
        source_lang.set(source[1])
        dst=dest_lang.current()
        destination = gtts[dst]
        translation = translator.translate(translator_input,lang_src=source[0],lang_tgt=destination)
        answer_textbox.delete('1.0',END)
        answer_textbox.insert("1.0",translation)    
    except:
        messagebox.showerror("Error!","Please check your internet connection and check if text is entered or not")
def info():
    messagebox.showinfo("Version","Version 1.1"+"\n"+"Google Translator (2021-22)"+"\n"+"help & support : vishwajeetsalunke42@outlook.com")    

def open_file():
    try:
        file = askopenfilename(defaultextension=".txt", 
                                  filetypes=[("Text Documents",".txt")])  
        if file == "":   
            file = None
        else: 
            root.title("Google Translate - "+os.path.basename(file)) 
            user_input_textbox.delete(1.0,END)   
            file = open(file,"r") 
            user_input_textbox.insert(1.0,file.read())   
            file.close()
    except UnicodeDecodeError:
        messagebox.showerror("Error!","Only English Language Supported")


def exchange_command():
    t1 = user_input_textbox.get("1.0",END) 
    t2 = answer_textbox.get("1.0",END)
    answer_textbox.delete("1.0",END)
    user_input_textbox.delete("1.0",END)
    user_input_textbox.insert("1.0",t2) 

def speaker_output_source():
    translator_input = user_input_textbox.get("1.0","end")
    translator = google_translator()
    source = translator.detect(translator_input)
    source_lang.set(source[1])
    dst=dest_lang.current()
    destination = gtts[dst]
    translation = translator.translate(translator_input,lang_src=source[0],lang_tgt=destination)
    myobj = gTTS(text=translation, lang=destination, slow=False) 
    myobj.save(r"C:\AppData\Translation.mp3")
    os.system(r"C:\AppData\Translation.mp3")

def clicked():
    from pytesseract import pytesseract
    from tkinter import Tk
    from tkinter import messagebox
    import os
    from PIL import Image

    #root initialization
    root= Tk()
    root.geometry('1100x550')
    root.title("Tesseract OCR")

    #function definitions
    def helpinfo():
        messagebox.showinfo("About","Tesseract OCR"+"\n"+"Powered by © Tesseract"+"\n"+"Help & Support: vishwajeetsalunke42@outlook.com")

    def browse_file():   
        try:
            file = askopenfilename(defaultextension=".png", 
                                    filetypes=[("Portable Network Graphics File",".png")])  
            if file == "":  
                file = None
            else: 
                root.title("Tesseract OCR -"+os.path.basename(file)) 
                file = open(file,"r") 
                image=file.name
            
            text1.delete('1.0',END)
            text1.insert("1.0",image)
            file.close()
        except UnicodeDecodeError:
            messagebox.showerror("Error!","Image not Supported")
        image_path = image
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"	
        img = Image.open(image_path) 
        pytesseract.tesseract_cmd = path_to_tesseract 
        text = pytesseract.image_to_string(img) 
        textbox.delete('1.0',END)    
        textbox.insert("1.0",text[:-1])

    #input components [textbox,labels]
    textbox = Text(root,width=100,height=25,font=('Calbri',12))
    textbox.pack()
    text1 = Text(root,width=100,height=1,font=('Calbri',12))
    text1.pack()
    label = Label(root,text="Image Path :")
    label.place(x=10,y=450)

    #menu Components
    my_menu=Menu(root)
    root.config(menu=my_menu)
    file_menu= Menu(my_menu)
    my_menu.add_cascade(label="Help", menu=file_menu)
    file_menu.add_command(label="About",command=helpinfo)

    #button components
    button1 = Button(root,text="Browse",command=browse_file)
    button1.place(x=470,y=500)
    root.mainloop()

#image objects
rootlabel = PhotoImage(file=r"C:\AppData\gt.png")

speak = PhotoImage(file=r"C:\AppData\speaker.png")

#root objects
root.iconphoto(False,rootlabel)

#menu objects
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)
tools_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
my_menu.add_cascade(label="Tools", menu=tools_menu)
file_menu.add_command(label="Open File",command=open_file)
tools_menu.add_command(label="Grab Image Text",command=clicked)
file_menu.add_command(label="Exit",command=root.quit)
about_menu= Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Version",command=info)

#input objects
user_input_textbox = Text(root,width=50,height=5,font=('calbri',11))
user_input_textbox.place(x=50,y=60)
answer_textbox = Text(root,width=50,height=5,font=('calbri',11))
answer_textbox.place(x=550,y=60)

#choice objects
n = tk.StringVar()
source_lang = ttk.Combobox(root,width=10,text=n)
source_lang['values']=("Auto-Detect")
source_lang.grid(column=5,row=5)
source_lang.place(x=165,y=20)
source_lang.set("Auto-Detect")
n1 = tk.StringVar()
dest_lang = ttk.Combobox(root,width=10,text=n1)
dest_lang['values']=('Afrikaans', 'Arabic', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh',
'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French',
'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian',
'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam',
'Marathi', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala',
'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai',
'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese')
dest_lang.grid(column=1,row=5)
dest_lang.place(x=695,y=20)
dest_lang.set("Hindi")


#button objects
Translate_button = Button(root,text='Translate',width=10,height=1,command=Translation_Function)
Translate_button.place(x=430,y=170)
exc = PhotoImage(file=r"C:\AppData\lte.png")
exchange = Button(root,image=exc,command=exchange_command)
exchange.place(x=490,y=90)
speak_btn = Button(root,image=speak,command=speaker_output_source)
speak_btn.place(x=930,y=150)

#label objects
label_1 = Label(root,text="Source Language :")
label_1.place(x=48,y=20)
label_2 = Label(root,text="Destination Language :")
label_2.place(x=550,y=20)

#root
root.mainloop()
