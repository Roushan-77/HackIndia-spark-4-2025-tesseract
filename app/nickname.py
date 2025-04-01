def get_nickname():
    try:
        with open("nickname.txt", "r") as file:
            nick_name = file.read().strip()
            if nick_name:
                return nick_name
    except FileNotFoundError:
        pass

    nick_name = input("Bot: What's your nickname? \nYou: ")
    
    with open("nickname.txt", "w") as file:
        file.write(nick_name)
    
    print(f"Bot: Nice to meet you, {nick_name}!\n")
    return nick_name

call_name = get_nickname()

