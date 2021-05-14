def option():
        option_is_invalid = True
        while option_is_invalid:
            try:
                option = int(input("Please input your option: "))
                option_is_invalid = False
                return option
            except:
                return -1