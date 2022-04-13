import random
from time import sleep
from random import choice
for i in range(0, 10):
    simon_says = ["Hands on head", "Hands on ears",
                  "Right hand up", "Left hand up",
                  "Hands on shoulders"]
    intros = ["Simon says...", ""]
    index = random.randint(0, 4)
    instruction = simon_says[index]
    intro = choice(intros)
    print("{} {}".format(intro, instruction))
    sleep(4)
