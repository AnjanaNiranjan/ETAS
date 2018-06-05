import numpy

import tflearn
import RPi.GPIO as GPIO
import time
import ldr2

RedPin = 11         # pin11
YellowPin = 12
GreenPin = 13
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(RedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(YellowPin, GPIO.OUT)
GPIO.setup(GreenPin, GPIO.OUT)


def getinput():
    '''a = input("Cars: ")
    b = input("Pedestrians: ")
    return (a, b)'''
    a = ldr2()
    b = ldr2()
    return(a,b)
def learn():
    net = tflearn.input_data(shape=[None, 2])
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 3, activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net, tensorboard_verbose=3)
    d = model.load('./my_model.tflearn')

    return model
def prediction(x, y, m):
    m1 = [x, y]

    pred = m.predict([m1])

    lst = []
    lst.append(pred[0][0])
    lst.append(pred[0][1])
    lst.append(pred[0][2])

    a = max(lst)
    b = lst.index(a)
    return b

def blink(a,b,c):
    i = 0
    while (i < 5):
        GPIO.output(RedPin, GPIO.HIGH)  # led on
        time.sleep(a)
        GPIO.output(RedPin, GPIO.LOW) # led off
        GPIO.output(YellowPin, GPIO.HIGH)  # led on
        time.sleep(b)
        GPIO.output(YellowPin, GPIO.LOW) # led off
        GPIO.output(GreenPin, GPIO.HIGH)  # led on
        time.sleep(c)
        GPIO.output(GreenPin, GPIO.LOW) # led off
        i += 1

    
def destroy():
    GPIO.output(RedPin, GPIO.LOW)   # led off
    GPIO.output(YellowPin, GPIO.LOW)
    GPIO.output(GreenPin, GPIO.LOW)
    GPIO.cleanup()                  # Release resource

def trafficLights(data):
    if data == 0:
        blink(10, 2, 15)

    elif data == 1:
        blink(5, 2, 20)

    elif data == 2:
        blink(15, 2, 10)

if __name__ == "__main__":
    
    
    m = learn()
    while True:
        try:
            (a1, b1) = getinput()
            data = prediction(a1, b1, m)
            trafficLights(data)
            
        except KeyboardInterrupt:
            destroy()
            
                


                

    
