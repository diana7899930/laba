rom utf8_decorator import utf8_converter      

@utf8_converter                                
def show_message(text1, text2):
    print("Аргумент 1:", text1)
    print("Аргумент 2:", text2)

show_message("Привіт", "Світ")
