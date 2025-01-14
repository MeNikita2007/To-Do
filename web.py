import requests

class Weather:
    def __init__(self):
        self.exit = True
        self.weather_parameters = {
        # 'format': 4,
        '0': '',
        # 'T': '',
        'M': '',
        'lang': 'ru'
    }
    
    def start(self):
        while self.exit:
            print('Weather servise')
            city = input("Enter city`s name or `EXIT` for exit: ")
            language = input("Enter en or ru for choose language: ")
            self.weather_parameters.update({'lang':language})
            if city == 'EXIT':
                self.exit = False
            else:
                response = self.get_weather(city)
                if response.status_code == 200:
                    print(response.text)
                else:
                    print(f'ERROR: programm ended with error {response.status_code }')
        
    def get_weather(self, city):
        url = f'http://wttr.in/{city}'
        response = requests.get(url, params=self.weather_parameters)
        return response
    
if __name__ == "__main__":
    weather_app = Weather()
    weather_app.start()
# url = 'http://wttr.in/Жуковский'
# weather_paramaters = {
#     'format': 4,
#     '0': '',
#     'T': '',
#     'M': '',
#     'lang': 'ru'
# }
# response = requests.get(url, params=weather_paramaters)
# print(response.text)