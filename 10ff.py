# Necessary Imports
import json
import keyboard
import time
import os


def prograssbar(p, max):
    barsize = 50
    print('\r' + "prograss : " + '\33[5m' +
          " " + str(int(p / max * 100)) + "% |" +

          '\33[107m' +
          " " * int(p / max * barsize) +
          '\33[0m' +
          " " * int(barsize - p / max * barsize) +

          "|" + str(p) + "/" + str(max), end=""
          )


try:
    f = open("words.txt", "r")
    filedata = f.read()

    data: list = json.loads(filedata)
    print('place the pointer in input area')
    time.sleep(2)
    print('exicuting.....')

    W_delay = 0.1
    C_delay = 0.07
    i = 1
    for word in data:
        prograssbar(i, len(data))
        for l in word:
            keyboard.write(l)
            time.sleep(C_delay)
        keyboard.write(' ')
        time.sleep(W_delay)
        i += 1

    f.close()

    os.remove("words.txt")

except Exception as e:
    print(e)
    pass

print('\ndone')
