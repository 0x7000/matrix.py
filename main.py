#!/usr/bin/env python3
import os
import random
from time import sleep
import termcolor


def main():
    os.system("clear")
    size = str(TERM_SIZE).split(",")
    colm = int(size[0].split("=")[1])                       # sutun
    line = int(size[1].split("=")[1].removesuffix(")"))     # satır
    print('\033[?25l', end="")                              # hide cursor on bash
    sayac = 0
    while 1:
        sayac += 1
        colm0 = random.randint(1, colm)
        line0 = random.randint(1, line-17)
        for i in range(1, 16):
            pozisyon(line0+i, colm0, "m")
            #sleep(0.01)
            for x in range(1, 9):
                pozisyon(line0+x, colm0+x, "x")
                #sleep(0.001)
        if sayac == 2000:
            break


def pozisyon(ll, cc, w):
    if w == "m":
        # link = https://en.m.wikipedia.org/wiki/ANSI_escape_code
        print("\033[%d;%dH" % (ll, cc), end='')  # set cursor position
        text = chr(random.randint(65, 128))
        termcolor.cprint(text, "green")
    else:
        print("\033[%d;%dH" % (ll, cc), end='')  # set cursor position
        termcolor.cprint(" ", "green")


TERM_SIZE = os.get_terminal_size()

if __name__ == "__main__":
    main()
