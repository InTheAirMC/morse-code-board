import board
#Write your code here
def turn_all(leds):
    leds[0].toggle()
    leds[1].toggle()
    leds[2].toggle()
    leds[3].toggle()
import time
def morse_code_translator(word):
    output = ''
    morse_to_eng = {'h': '....', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '.': '.-.-.-', '?': '..--..', ',': '--..--', ' ': '/'}

    for char in word:
        if char.lower() in morse_to_eng:
            print(char,end='')
            for char1 in morse_to_eng[char.lower()]:
                if char1 == ".":
                    turn_all(board.leds)
                    time.sleep(.125)
                    turn_all(board.leds)
                    time.sleep(.125)
                elif char1 == "-":
                    turn_all(board.leds)
                    time.sleep(.5)
                    turn_all(board.leds)
                    time.sleep(.5)
    
#     for x in range(len(word)):
#         if word[keys[x]] 
morse_code_translator("Among Us[c] is a 2018 online multiplayer social deduction game developed and published by American game studio Innersloth. The game was inspired by the party game Mafia and the science fiction horror film The Thing. It allows for cross-platform play, first being released on iOS and Android devices in June 2018 and on Windows later that year in November. The game was then ported to the Nintendo Switch in December 2020, and will release on PlayStation 4, PlayStation 5, Xbox One and Xbox Series X/S in December 2021. While the game was initially released in 2018, to little mainstream attention, it received a massive influx of popularity in 2020 due to many well-known Twitch streamers and YouTubers playing it. The timing of the COVID-19 pandemic has also been credited with boosting the game\'s popularity.")

