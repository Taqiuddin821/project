import datetime
import time
import winsound
import json
import os
from collections import Counter

DATA_FILE = "alarm_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        alarm_history = json.load(f)
else:
    alarm_history = []

sounds = {
    "1": ("Loud Beep", "alarm1.wav"),
    "2": ("Soft Alarm", "alarm2.wav"),
    "3": ("Digital Beep", "alarm3.wav")
}

print("Select Alarm Sound:")
for key, value in sounds.items():
    print(f"{key}. {value[0]}")

sound_choice = input("Enter choice (1/2/3): ")
while sound_choice not in sounds:
    print("Invalid choice.")
    sound_choice = input("Enter choice (1/2/3): ")

sound_name, sound_file = sounds[sound_choice]

if alarm_history:
    most_common_time = Counter(alarm_history).most_common(1)[0][0]
    print(f"\nAI Suggestion: You often set alarm at {most_common_time}")

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"\nAlarm set for {alarm_time} using {sound_name}")

alarm_history.append(alarm_time)
with open(DATA_FILE, "w") as f:
    json.dump(alarm_history, f)

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    if current_time == alarm_time:
        print("\nAlarm ringing! Wake up!")

        try:
            for i in range(5):
                winsound.PlaySound(sound_file, winsound.SND_FILENAME)
                time.sleep(1)
        except:
            print("Sound file error!")

        snooze = input("Snooze? (yes/no): ").lower()
        if snooze == "yes":
            snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
            alarm_time = snooze_time.strftime("%H:%M:%S")
            print(f"Snoozed to {alarm_time}")
        else:
            print("Alarm stopped.")
            break

    time.sleep(1)
