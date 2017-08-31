#'''
#from microbit import *

arrayTime = []
analog_0 = 0
BPM = 0
reset = 0
threshold = 900
pastTime = running_time()

# If the array length is 5 or greater, pop the entry out
while True:

    analog_0 = pin0.read_analog()

    if reset == 0:  # Pulse has crossed a hump
        if (analog_0 >= threshold):  # Or whatever number it has to exceed to be considered as a beat
            arrayTime.append(running_time() - pastTime)
            pastTime = running_time()
            display.show(Image.Heart)
            reset = 1

    if reset == 1:  # Pulse is on a hump
        if (analog_0 < threshold):
            reset = 0

    if len(arrayTime) >= 6:
        arrayTime.pop(0)
        BPM = averageArray(arrayTime)
        # BPM = int(averageArray(arrayTime))     #If BPM cannot have decimals
        display.scroll("%d bpm" % (BPM), delay=100,)


#'''


def averageArray(arrayTime):
    total = 0
    for item in arrayTime:
        total = total + item
    averageDuration = total / len(arrayTime)
    BPM = 60 / averageDuration
    return BPM


'''
arrayTime = [2, 2, 2]
BPM = averageArray(arrayTime)
print(BPM)
'''
