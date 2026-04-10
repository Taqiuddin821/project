Smart AI-Based Alarm Clock (Python)

A futuristic, intelligent alarm clock built using Python that goes beyond traditional alarms by learning user behavior and providing smart suggestions.

Overview

The Smart AI Alarm Clock is a console-based application that allows users to set alarms with customizable sounds while incorporating basic AI concepts like pattern recognition and adaptive suggestions.

Unlike traditional alarm systems, this project:

Learns from user habits
Suggests frequently used alarm times
Provides snooze functionality
Stores data for future improvements
Features
Set alarm using HH:MM:SS (24-hour format)
Multiple alarm sound options
AI-based time suggestion system
Stores user history using JSON
Snooze functionality
Real-time clock monitoring
AI Concept Used

This project uses basic machine learning logic (pattern recognition):

Tracks previously set alarm times
Uses frequency analysis (Counter)
Suggests the most common alarm time
Adapts based on user behavior
Tech Stack

Language: Python

Libraries Used:

datetime → Time handling
time → Delay management
winsound → Sound playback
json → Data storage
os → File handling
collections → Pattern analysis
Project Structure
Smart-AI-Alarm
│── alarm.py
│── alarm_data.json
│── alarm1.wav
│── alarm2.wav
│── alarm3.wav
│── README.md
Installation & Setup
Clone the repository:
git clone ::https://github.com/Taqiuddin821/project
Navigate to the project folder:
cd smart-ai-alarm
Run the program:
python alarm.py
Usage
Select alarm sound
Enter alarm time (HH:MM:SS)
Wait for alarm trigger
Choose to snooze or stop
Example Output
Select Alarm Sound:
1. Loud Beep
2. Soft Alarm
3. Digital Beep

Enter choice (1/2/3): 1

AI Suggestion: You often set alarm at 07:00:00

Enter alarm time (HH:MM:SS): 07:30:00

Alarm set for 07:30:00 using Loud Beep

Alarm ringing! Wake up!

Snooze? (yes/no): no
Alarm stopped.
Limitations
Works only on Windows (uses winsound)
Requires .wav sound files
Basic AI (not full ML model)
Future Enhancements
GUI using Tkinter / PyQt
Voice assistant integration
Real ML model for prediction
Mobile app version
Smart home integration
Multi-alarm support
Learning Outcomes
Time-based automation in Python
File handling and persistent storage
Basic AI/ML concepts
Real-world problem solving
Author

Taqiuddin
Reg No: 25BAI10349
Course: CSE (AI & ML)
Year: 2025–26
