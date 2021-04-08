import tkinter as tk
import webbrowser

root = tk.Tk()
root.title('Web Browser')
root.geometry("400x150")
x = tk.StringVar()


def fb():
    webbrowser.open_new('https://www.facebook.com/')


def utube():
    webbrowser.open_new('https://www.youtube.com/')
    


def insta():
    webbrowser.open_new('https://www.instagram.com/')


def twitter():
    webbrowser.open_new('https://www.twitter.com/')


def wiki():
    webbrowser.open_new('https://www.wikipedia.org/')


def search():
    word = x.get()
    webbrowser.open_new('http://www.google.com/search?q=' + word)


x = tk.StringVar()
button1 = tk.Button(root, text="Facebook", fg="white", bg="blue", command=fb)
button2 = tk.Button(root, text="YouTube", fg="white", bg="red", command=utube)
button3 = tk.Button(root, text="Instagram", fg="white", bg="pink", command=insta)
button4 = tk.Button(root, text="Twitter", fg="white", bg="skyBlue", command=twitter)
button5 = tk.Button(root, text="Wikipedia", fg="white", bg="black", command=wiki)

button1.place(x=10, y=70, width=80, height=30)
button2.place(x=100, y=70, width=80, height=30)
button3.place(x=190, y=70, width=80, height=30)
button4.place(x=10, y=105, width=135, height=30)
button5.place(x=155, y=105, width=135, height=30)

button6 = tk.Button(root, text="Search", fg="white", bg="#202020", command=search)
button6.place(x=320, y=10, width=70, height=50)

entry = tk.Entry(root, textvariable=x)
entry.place(x=10, y=10, width=300, height=50)

root.mainloop()
