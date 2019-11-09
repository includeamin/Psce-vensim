import pcse
from pcse.fileinput import CABOFileReader, cabo_weather, CABOWeatherDataProvider


def load_data():
   weather_data = CABOWeatherDataProvider('NL2', fpath="./Data/METEO/CABOWE")
   #file = cabo_weather.CABOWeatherDataProvider("./Data/METEO/CABOWE")
   print(weather_data.export())

   for item in weather_data.export():
       print(item)


if __name__ == '__main__':
    load_data()