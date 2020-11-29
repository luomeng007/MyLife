import os
import time
import speech


class Meditation:
    def __init__(self):
        self.start_time = time.time()

        self.minutes = 20

        self.timestamp = np.arange(self.minutes) + 1

    def main_program(self):
        print("开始冥想！")
        speech.say("los geht's")

        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    print(f"已经过去了{i + 1}分钟")
                    break

        speech.say("Fertig!")
        print("冥想结束!")

        MainGame.attribute_list[2] += 1


if __name__ == "__main__":
    # ML: My Life
    m = Meditation()
    m.main_program()