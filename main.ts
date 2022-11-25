function giroAleatorio () {
    if (Math.randomBoolean()) {
        maqueen.motorStop(maqueen.Motors.M1)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    } else {
        maqueen.motorStop(maqueen.Motors.M2)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
    basic.pause(randint(500, 2000))
}
let distancia = 0
basic.pause(2000)
let velocidad = 180
basic.forever(function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velocidad)
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (distancia < 18 && distancia != 0) {
        giroAleatorio()
    }
})
control.inBackground(function () {
    while (true) {
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
    }
})
