#!/usr/bin/env python3
import os
import random
from time import sleep
import termcolor


def main():
    size = str(TERM_SIZE).split(",")
    colm = int(size[0].split("=")[1])                       # sutun
    line = int(size[1].split("=")[1].removesuffix(")"))     # satır
    print('\033[?25l', end="")                              # hide cursor on bash
    sayac = 0
    while sayac <= 50:
        colm0 = random.randint(1, colm)
        line0 = random.randint(1, line-17)
        for i in range(1, 16):
            pozisyon(colm0, line0+i)
            sleep(0.02)
        sayac += 1


def pozisyon(cc, ll):
    # link = https://en.m.wikipedia.org/wiki/ANSI_escape_code
    print("\033[%d;%dH" % (ll, cc), end='')  # set cursor position
    text = chr(random.randint(65, 128))
    termcolor.cprint(text, "green")


TERM_SIZE = os.get_terminal_size()

if __name__ == "__main__":
    main()
