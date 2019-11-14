from pcse.fileinput import CABOWeatherDataProvider
import csv
import os
import pathlib


class MeteoExtractor:
    def __init__(self, path: str, f_name: str, coefficients: dict, crops, simulate_dir=''):
        self.Path: str = path
        self.FName: str = f_name
        self.Coefficients: dict = coefficients
        self.Crops: list = crops
        self.Dirs = {"Name": {"METEO": "path",
                              "CROP": "path",
                              "LookUp": "path"}}
        self.SimulateDir = simulate_dir
        self.coefficients_validation()
        self.init_dirs()

    def coefficients_validation(self):
        for item in self.Coefficients.keys():
            if len(self.Crops) != len(self.Coefficients[item].keys()):
                raise Exception("Number of Coefficients should equal to number of Crops")

    def init_dirs(self):
        for region in self.Coefficients.keys():
            if not os.path.exists(f'{self.SimulateDir}/{region}'):
                pathlib.Path(f'{self.SimulateDir}/{region}').mkdir(parents=True, exist_ok=True)
            for item in self.Crops:
                if not os.path.exists(f'{self.SimulateDir}/{region}/{item}'):
                    os.mkdir(f'{self.SimulateDir}/{region}/{item}')

                if not os.path.exists(f'{self.SimulateDir}/{region}/{item}/METEO'):
                    os.mkdir(f'{self.SimulateDir}/{region}/{item}/METEO')

                if not os.path.exists(f'{self.SimulateDir}/{region}/{item}/CROP'):
                    os.mkdir(f'{self.SimulateDir}/{region}/{item}/CROP')

                if not os.path.exists(f'{self.SimulateDir}/{region}/{item}/LOOKUP'):
                    os.mkdir(f'{self.SimulateDir}/{region}/{item}/LOOKUP')

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
    obj = MeteoExtractor('../Data/METEO/CABOWE', "NL2",
    {"Tajan": {
        "Sib": 1, "Khiar": 2, "Berenj": 3, 'Gandom': 3, "Tare": 5, "Sir": 6, "Piaz": 5, "Havij": 5
    }, "Sari": {
        "Sib": 1, "Khiar": 2, "Berenj": 3, 'Gandom': 3, "Tare": 5, "Sir": 6, "Piaz": 5, "Havij": 5

    }, "Amol": {
        "Sib": 1, "Khiar": 2, "Berenj": 3, 'Gandom': 3, "Tare": 5, "Sir": 6, "Piaz": 5, "Havij": 5

    }, "Tehran": {
        "Sib": 1, "Khiar": 2, "Berenj": 3, 'Gandom': 3, "Tare": 5, "Sir": 6, "Piaz": 5, "Havij": 5
    }
    },
                         ["Sib", "Khiar", "Berenj", 'Gandom', "Tare", "Sir", "Piaz", "Havij"],
                         simulate_dir="./SimulateData")
    # result = obj.save_lookups()

    # for item in result.keys():
    #     with open(f'./{item}.txt', 'w') as f:
    #         temp_str = ''
    #         for i in result[item]:
    #             temp_str += f",({result[item].index(i)},{i})"
    #         f.write(f"{item} ([(1,{min(result[item])}),({len(result[item])},{max(result[item])})]{temp_str})\n")
