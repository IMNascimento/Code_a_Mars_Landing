
from components import UltrasonicSensor, LED, Button, LightSensor
from components import Buttonfrom components import Buzzer
from time import sleep, time

ultrasonic = UltrasonicSensor("D1")

while True:
    distance = ultrasonic.distance
    print(distance)
    sleep(0.1)

red_led = LED("D2")
yellow_led = LED("D3")
green_led = LED("D4")

if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()


buzzer = Buzzer("D5")
if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
    buzzer.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()



light = LightSensor("D6")
while True:
    lightlevel = (light.reading)
    print lightlevel

plt.ion()
fig = plt.figure()
x_data = []
y_data = []
start_time = time()

x_data.append(elapsed_time)
y_data.append(lightlevel)

plt.title("Light Sensor input over time")
plt.ylabel("Light Level")
plt.xlabel("Time in seconds")

plt.plot(x_data, y_data)
plt.draw()
plt.pause(0.01)


button = Button("D7")

while True:
    if button.is_pressed:
        buzzer.on()
    else:
        buzzer.off()

Morse_Dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def encrypt(message):
    convert = ' '
    for letter in message:
        if letter != ' ':
            convert += Morse_Dict[letter] + ' '
        else:
            convert += ' '
    return convert

def decrypt(message):
    message += ' '
    decode = ''
    text = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            text += letter
        else:
            i += 1
            if i == 2:
                decode += ' '
            else:
                decode += list(Morse_Dict.keys())[list(Morse_Dict.values()).index(text)]
                text = ''
    return decode

def main():
    text = input("Enter Message: ")
    output = encrypt(text.upper())
    print(output)
if __name__ == '__main__':
    main()

#fizar alterações para correção de bugs