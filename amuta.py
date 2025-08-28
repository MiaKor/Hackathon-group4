import consts

from screen import draw_message


def amuta(name, my_data):
    my_amuta_data = my_data[name]

    location = (0, 100)

    for i in my_amuta_data:

        location = (0, location[1])

        for k in i:

            draw_message(k, 40, "white", location)

            location = (location[0] + 200, location[1])

            if i.index(k) == len(i) - 1:
                location = (location[0], location[1] +60)


my_name = "hello"

my_data = [["ori", "058", "rishon"],

           ["dana", "069", "nes"]

           ]
