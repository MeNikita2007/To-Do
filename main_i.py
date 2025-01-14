import threading
import time, os

class Working_Panel:
    def __init__(self):
        self.pendulum = 0
        self.timer = 0
        self.temperature = 0
    def run_pendulum(self):
        list_num = [0,1,2,3,4,5,6,7,8,9]
        while True:
            for i in list_num:
                self.pendulum = i
                time.sleep(1)
            for i in reversed(list_num):
                 self.pendulum = i
                 time.sleep(1)
    def run_timer(self):
        while True:
            current_time = time.time()
            local_time = time.localtime(current_time)
            formatted_time = time.strftime("%H:%M:%S", local_time)
            self.timer = formatted_time 
            time.sleep(1)
            
            
    def run_temperature(self):
        list_temp = [10,12,14,16,18,20]
        while True:
            if self.pendulum >= 0 and self.pendulum <=5:
                self.temperature = list_temp[self.pendulum]        

    def print_menu(self):
        print('--------------------------------------------')
        print('|Введите 1 чтобы увидеть положение маятника|')
        print('|Введите 2 чтобы увидеть время             |')
        print('|Введите 3 чтобы увидеть температуру       |')
        print('--------------------------------------------')
    
    def menu(self):
        while True:
            print(f'Маятник на позиции: {self.pendulum}')
            print(f'Текущее время: {self.timer}')
            print(f'Текущая температура: {self.temperature}')
            time.sleep(0.5)
            os.system('cls||clear')
               
    def run(self):
        th1 = threading.Thread(target = self.run_pendulum)
        th2 = threading.Thread(target = self.run_timer)
        th3 = threading.Thread(target = self.run_temperature)
        th1.start()
        th2.start()
        th3.start()
        self.menu()
        th1.join()
        th2.join()
        th3.join()

if __name__ == '__main__':
    panel = Working_Panel()
    panel.run()