import random
import tkinter as tk

fun_facts = [
    "Ants only sleep for 1.9 hours a day.",
    "The first computer weighed around 27 tons.",
    "A year on Venus is shorter than a day on that planet.",
    "Sound cannot travel through a vacuum.",
    "Cats have over 100 communication sounds, while dogs only have about 10.",
    "Flamingos' tongues are pink due to the food they eat.",
    "The average cloud weighs about as much as 100 elephants.",
    "The Sun emits more energy in one second than humans use in 20 billion years.",
    "The longest river in the world is the Nile, and the tallest mountain is Mount Everest.",
    "In space, there are cosmic strings that are millions of kilometers in diameter.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "Bananas are berries, but strawberries are not.",
    "The world's largest desert is Antarctica.",
    "A group of flamingos is called a 'flamboyance'",
    "A day on Saturn is less than 11 hours long.",
    "The fingerprints of koalas are so similar to humans' that they have been confused at crime scenes.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can grow up to 6 inches taller during the summer due to the expansion of the iron in the heat.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "Cows have best friends and can become stressed when separated from them.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes."
    "The Great Wall of China is not visible from space with the naked eye.",
    "Honeybees can recognize human faces.",
    "The world's smallest mammal is the bumblebee bat, weighing around 2 grams.",
    "A newborn kangaroo is about 1 inch in length.",
    "The average person spends about 6 months of their life waiting for red lights to turn green.",
    "The fear of the number 13 is called triskaidekaphobia.",
    "A group of owls is called a parliament.",
    "A sneeze can travel up to 100 miles per hour.",
    "Polar bears have black skin underneath their white fur.",
    "The longest recorded flight of a chicken is 13 seconds.",
    "The only letter that doesn't appear in the periodic table is the letter 'J'."
]


def generate_fact():
    random_fact = random.choice(fun_facts)
    fact_label.config(text=random_fact)


app = tk.Tk()
app.title("Fun Fact Generator")

fact_label = tk.Label(app, text="", wraplength=300, justify="center", font=("Helvetica", 12))
fact_label.pack(padx=20, pady=20)

generate_button = tk.Button(app, text="Generate Fun Fact", command=generate_fact)
generate_button.pack(padx=20, pady=10)


app.mainloop()
