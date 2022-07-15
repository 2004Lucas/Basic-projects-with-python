#building a bot that can be used to display the time

#importing the time module
import time

#defining the function that will be used to display the time
def display_time():
    #getting the current time
    current_time = time.strftime("%H:%M:%S")
    #displaying the current time
    print(current_time)
    #calling the function again after 1 second
    time.sleep(1)
    display_time()
#calling the function
display_time()

# end of file botclock.py 
# Learning to code by building a bot that can be used to display the time
# https://github.com/2004Lucas/Basic-projects-with-python
# Have a nice day!