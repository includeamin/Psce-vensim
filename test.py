import pcse
import csv
from pcse.fileinput import CABOFileReader, cabo_weather, CABOWeatherDataProvider


def load_data():
   weather_data = CABOWeatherDataProvider('NL2', fpath="./Data/METEO/CABOWE")
   #file = cabo_weather.CABOWeatherDataProvider("./Data/METEO/CABOWE")
   keys = weather_data.export()[0].keys()
   print(keys)
   with open('amin.csv','w') as f:
       file = csv.DictWriter(f,keys)
       file.writeheader()
       file.writerows(weather_data.export())

   # import pandas
   # pandas.DataFrame.to_csv(weather_data.export())




if __name__ == '__main__':
    load_data()