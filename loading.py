from time import sleep

text = "█"
for i in range(0, 101, 10):
    print(f"{i}%\t{text*(i//10)}", end="\r")
    sleep(0.5)
print()
