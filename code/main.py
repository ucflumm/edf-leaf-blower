# importing the required libraries
from machine import Pin
from machine import PWM
import time



# initial varibale declaratins
frequency = 0
duty_cycle = 0



# pin declarations
# This is GPIO15 not pin 15
pwmPin = Pin(15) # declare the pin for PWM output
pwmOutput = PWM(pwmPin) # define a PWM object



# ask user for frequency
while True:
    frequency = float(input("Enter pwm frequency in Hz : "))

    # set the PWM frequency only once at the beginning
    if frequency >= 0:
        pwmOutput.freq(int(frequency))
        break

    else:
        print("frequency cannot be negative. Enter again ")
        continue




# function for asking duty_cycle input
# Need to fix duty cycle scaling as 10% duty cycle already provides full power
# Assuming that 5% equals mid throttle (0 throttle)
# Working with the knowledge that 1ms pulse = 0% and 2ms = 100% throttle range.
# Reminder that we are working with 3v3 logic not 5v Arduino logic
def duty():
    duty_cycle = float(input("Enter duty_cycle in percentage : "))
    # crash when character is input
    # convert duty cycle % to micropython range 0 - 65025
    duty_cycle = int( duty_cycle * 65025 / 100  )
    print("duty_cycle = ", duty_cycle)
    return duty_cycle # returns the duty cycle (in integer)





# define function for PWM generation
def pwmGenerate(duty_cycle):
    duty_cycle = duty_cycle
    pwmOutput.duty_u16(duty_cycle)




# generate the PWM signal with variable duty cycle
while True:
    duty_cycle = duty() # duty cycle in integer
    # check user input for discrepancy
    if duty_cycle >= 0 and duty_cycle <= 65025:
        pwmGenerate(duty_cycle)

    else:
        print("Unsuitable range, please enter again")
        continue
