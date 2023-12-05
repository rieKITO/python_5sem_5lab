def action_choice():
    is_correct = False
    while is_correct is False:
        try:
            number = int(input("-> "))
            if number < 1 or number:
                pass
        except:
            pass