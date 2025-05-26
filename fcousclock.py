import time
import winsound

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f'{mins:02d}:{secs:02d}', end="\r")
        time.sleep(1)
        total_seconds -= 1

def start_pomodoro():
    while True:
        print("工作时间: 25分钟")
        countdown(25)  # 25分钟工作
        winsound.Beep(1000, 1000)
        
        print("休息时间: 5分钟")
        countdown(5)  # 5分钟休息
        winsound.Beep(1000, 1000)

if __name__ == "__main__":
    start_pomodoro()
