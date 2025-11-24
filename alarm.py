import datetime
import time
import winsound

sounds = {
    "1": ("Loud Beep", "alarm1.wav"),
    "2": ("Soft Alarm", "alarm2.wav"),
    "3": ("Digital Clock Beep", "alarm3.wav")
}

print("Select Alarm Sound:")
for key, value in sounds.items():
    print(f"{key}. {value[0]}")

sound_choice = input("Enter your choice (1/2/3): ")

while sound_choice not in sounds:
    print("Invalid choice. Try again.")
    sound_choice = input("Enter your choice (1/2/3): ")

sound_name, sound_file = sounds[sound_choice]

alarm_time = input("Enter alarm time in HH:MM:SS (24-hour format): ")

print(f"\nAlarm set for {alarm_time} using sound: {sound_name}\n")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    if current_time == alarm_time:
        print("⏰ Alarm ringing! Wake up!")
        try:
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
        except:
            print("Error: Sound file missing or unsupported.")
        break
    
    time.sleep(1)
