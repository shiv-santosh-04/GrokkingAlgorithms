voted = {}
def check_voter(name):
    if name in voted:
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")
print(check_voter("Luca"))
print(check_voter("Luca"))
print(check_voter("Micheal"))