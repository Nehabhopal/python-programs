pin="1234"
trial=1

while trial<=3:
    input_pin=input(f"trial- {trial}| pin>>")
    trial += 1
    if input_pin==pin:
        print("correct")
        break
    else:
        print("incorect")

