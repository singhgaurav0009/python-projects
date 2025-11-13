import datetime
import time
import winsound  # works on Windows

alarm = input("Enter time (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm:
        print("Wake up!")
        winsound.Beep(1000, 2000)
        break
    time.sleep(1)
