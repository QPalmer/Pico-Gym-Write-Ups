def all_your_base(str, base):
    # change base input into integer
    base_val = int(base)

    # split string 
    words = str.split()

    text = [ ]

    for word in words:
        decimal = (int(word, base_val))
        text.append(chr(decimal))

    final_text = "".join(text)  
    print(final_text)

def run_program():
    while True:
        string = input(f"Enter String:\n")
        if string == "q":
            exit(0)
        else:
            base = input(f"Enter Base \n")
            all_your_base(string, base)


run_program()
