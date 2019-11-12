from pcse.fileinput import CABOWeatherDataProvider
import csv


class MeteoExtractor:
    def __init__(self, path: str, f_name: str, coefficients: dict):
        self.Path: str = path
        self.FName: str = f_name
        self.Coefficients: dict = coefficients

    def writer(self):
        weather_data = CABOWeatherDataProvider(self.FName, fpath=self.Path)
        keys = weather_data.export()[0].keys()
        with open(f'{self.FName}.csv', 'w') as f:
            file = csv.DictWriter(f, keys)
            file.writeheader()
            file.writerows(weather_data.export())

    def loader(self):
        with open(f'{self.FName}.csv', 'w') as f:
            file = csv.reader(f)
            return file

    def load_general_lookup(self):
        csv_weather_file = self.loader()
        et0s = [item["ET0"] for item in csv_weather_file]
        final_result = {}

        for i in range(len(self.Coefficients.keys())):
            temp = [item * self.Coefficients[i] for item in et0s]
            final_result[i] = temp

        return final_result


if __name__ == '__main__':
    obj = MeteoExtractor('../Data/METEO/CABOWE', "NL2", {"Apple": 1, "Apple2": 3, "Apple4": 4, "Apple5": 5,
                                                         "Orange1": 1, "Orange2": 2, "Orange3": 4, "Orange4": 5})
    obj.writer()

    pass
