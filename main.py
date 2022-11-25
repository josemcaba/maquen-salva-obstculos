def giroAleatorio():
    if Math.random_boolean():
        maqueen.motor_stop(maqueen.Motors.M1)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    else:
        maqueen.motor_stop(maqueen.Motors.M2)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    basic.pause(2000)
def medirDistancia():
    global distancia
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    basic.pause(50)
    for index in range(numDist - 1):
        distancia += maqueen.ultrasonic(PingUnit.CENTIMETERS)
        basic.pause(50)
    distancia = distancia / numDist
distancia = 0
numDist = 0
numDist = 5
basic.pause(2000)

def on_forever():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 175)
    medirDistancia()
    if distancia < 15:
        giroAleatorio()
basic.forever(on_forever)

def on_in_background():
    while True:
        basic.show_leds("""
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            """)
        basic.pause(200)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(200)
control.in_background(on_in_background)
