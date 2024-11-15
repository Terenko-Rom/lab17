import pandas as pd
import json
boys_data = {
    "Ivan": "2005-06-15",
    "Petro": "2004-08-22",
    "Andriy": "2003-11-30",
    "Maksym": "2005-01-12",
    "Oleksiy": "2004-03-05"
}
with open('boys.json', 'w') as file:
    json.dump(boys_data, file, indent=4)
with open('boys.json', 'r') as file:
    data = json.load(file)
series = pd.Series(data)
series = pd.to_datetime(series)
series_dict = series.to_dict()
with open('dtm.json', 'w') as file:
    json.dump(series_dict, file, default=str)