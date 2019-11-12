from pcse.fileinput import CABOWeatherDataProvider
import csv


class MeteoExtractor:
    def __init__(self, path: str, f_name: str, coefficients: dict):
        self.Path: str = path
        self.FName: str = f_name
        self.Coefficients: dict = coefficients

    def get_weather_et0(self):
        weather_data = CABOWeatherDataProvider(self.FName, fpath=self.Path)
        data = weather_data.export()
        et0s = [item["ET0"] for item in data]
        return et0s

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
            print(file)
            return file

    def load_general_lookup(self):
        et0s = self.get_weather_et0()
        final_result = {}
        keys = self.Coefficients.keys()
        for item in keys:
            temp = [float(self.Coefficients[item]) * float(i) for i in et0s]
            final_result[item] = temp

        return final_result
    def save_lookups(self):
        # obj = MeteoExtractor('../Data/METEO/CABOWE', "NL2", {"Apple": 1, "Apple2": 3, "Apple4": 4, "Apple5": 5,
        #                                                      "Orange1": 1, "Orange2": 2, "Orange3": 4, "Orange4": 5})
        result = self.load_general_lookup()
        for item in result.keys():
            with open(f'./{item}.txt', 'w') as f:
                temp_str = ''
                for i in result[item]:
                    temp_str += f",({result[item].index(i)},{i})"
                f.write(f"{item} ([(1,{min(result[item])}),({len(result[item])},{max(result[item])})]{temp_str})\n")


if __name__ == '__main__':
    obj = MeteoExtractor('../Data/METEO/CABOWE', "NL2", {"Apple": 1, "Apple2": 3, "Apple4": 4, "Apple5": 5,
                                                         "Orange1": 1, "Orange2": 2, "Orange3": 4, "Orange4": 5})
    result = obj.save_lookups()

    # for item in result.keys():
    #     with open(f'./{item}.txt', 'w') as f:
    #         temp_str = ''
    #         for i in result[item]:
    #             temp_str += f",({result[item].index(i)},{i})"
    #         f.write(f"{item} ([(1,{min(result[item])}),({len(result[item])},{max(result[item])})]{temp_str})\n")
