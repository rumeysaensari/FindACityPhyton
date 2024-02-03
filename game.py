import turtle
import pandas
from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def game():
    screen = turtle.Screen()
    screen.title("Turkey's Cities Find Game")
    image = "C:/Users/ahmet/Desktop/Programming with python midterm project/files/unnamed_turkey_map.gif"
    screen.addshape(image)
    turtle.shape(image)
    screen.setup(1400, 820)

    u = turtle.Turtle()
    u.hideturtle()
    u.penup()
    u.goto(310, 370)
    u.write(username.get(), font=("Verdana", 10))

    data = pandas.read_csv("C:/Users/ahmet/Desktop/Programming with python midterm "
                           "project/files/81_cities_coordinate.csv")
    all_cities = data.city.to_list()
    guessed_cities = []
    counter = 0

    while counter < 81:
        answer_city = screen.textinput(title=f"{counter}/81 Cities Correct", prompt="Let's write a city name!").title()

        if answer_city not in all_cities:
            messagebox.showinfo("Alert!", "The city you entered is not in Turkey!")

        elif answer_city in guessed_cities:
            messagebox.showinfo("showinfo", "You entered the same city again. Please enter another city name.")

        elif answer_city in all_cities:
            guessed_cities.append(answer_city)
            u.clear()  # Clear the previous username display
            u.write(username.get(), font=("Verdana", 10))

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            city_data = data[data.city == answer_city]
            t.goto(int(city_data.x), int(city_data.y))
            counter += 1
            t.write(answer_city, font=("Verdana", 10))

        if counter == 81:
            messagebox.showinfo("Congratulations!", "You have guessed all 81 cities!")


def validateLogin(username):
    print("username entered:", username.get())
    return


welcome_window = tk.Tk()
welcome_window.title("Welcome to the Turkey's Cities Find Game!")
welcome_window.geometry('500x300')
usernameLabel = Label(welcome_window, text="User Name")
usernameLabel.pack()
usernameLabel.place(x=120, y=100)
username = StringVar()
usernameEntry = Entry(welcome_window, textvariable=username)
usernameEntry.pack()
usernameEntry.place(x=190, y=100)
validateLogin = partial(validateLogin, username)
loginButton = Button(welcome_window, text="Login", command=validateLogin)
loginButton.pack()
loginButton.place(x=230, y=130)
info2 = tk.Label(welcome_window,
                 text="Hello, welcome to the game. You will win the game when you enter 81 provinces of Turkey.")
info2.pack()
info3 = tk.Label(welcome_window,
                 text="Enter your username and save with the login button. Then click the start game button.")
info3.pack()
start_button = tk.Button(text="Start the game", command=game)
start_button.place(x=210, y=200)
close_button = tk.Button(text="Exit the game", command=welcome_window.destroy)
close_button.place(x=212, y=230)
welcome_window.mainloop()
