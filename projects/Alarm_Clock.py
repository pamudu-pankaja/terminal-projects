import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")

    sound_file=""
    is_running =True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            if pygame.mixer.music.get_busy():
                time.sleep(20)

            is_running = False

        time.sleep(1)

def main():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        alarm_time=input("Enter the alarm time (HH/MM/SS): ")

        if alarm_time <current_time :
            print("Invalid time")
            continue
        else:
            set_alarm(alarm_time)
            break

if __name__=="__main__":
    main()




