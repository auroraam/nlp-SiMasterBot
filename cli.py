from engine import reply

print("SimasterBot CLI — ketik :q untuk keluar.")
while True:
    msg = input("you> ")
    if msg in [":q", "quit", "exit"]:
        break
    print("bot>", reply(msg))
