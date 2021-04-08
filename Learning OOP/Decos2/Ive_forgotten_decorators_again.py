# DECORATORS DO NOT CALL THE FUNCTION THEY WRAP!
# THEY ARE SIMPLE A MODIFIED COPY OF THE FUNCTION YOU WISH TO RUN

def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Before the function runs")
        a_function_to_decorate()
        print("After the function runs")
    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED. IMPORTANT!
    return the_wrapper_around_the_original_function

####################################################################################################################################

def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()

# THESE TWO ARE THE SAME AS EACHOTHER, LITERALLY! 

@my_shiny_new_decorator
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

#OUTPUT FOR BOTH:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the fucntion runs