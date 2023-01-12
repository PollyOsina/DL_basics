# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 03:08:56 2022

@author: Polly
"""

# Датафрейм находится на гугл диске

import pandas as pd
import numpy as np


data = pd.read_csv('https://drive.google.com/uc?id=1JY8l5nSu9O4GtMDpaOfH2Oowlpza3U-c')

# Задание 1
# Какой ответ на вопрос по [homework]pandas:

# 0) Сколько всего возрастных категорий?

data.Age.nunique()

# 1) Сколько мужчин из города категории A? (не уникальных ID, а количество строк)
data[(data.City_Category == 'A') & (data.Gender == 'M')].shape[0]

# 2) Сколько женщин от 46 до 50, потративших (столбец Purchase) больше 20000 
#   (условных единиц, в данном случае)? (не уникальных ID, а количество строк)
data[(data["Gender"] == 'F') & (data["Age"] == '46-50') & (data["Purchase"] > 20000)].shape


# 3) Сколько NaN'ов в столбце Product_Category_3?
data['Product_Category_3'].isnull().sum()

# 4). Какую долю (вещественное число от 0 до 1, округлить до 4-го знака) от всех 
#     покупателей составляют ВМЕСТЕ мужчины от 26 до 35 лет и женщины старше 36 
#     лет (то есть нужно учесть несколько возрастных категорий)? (вещественное 
#     число, округлённое до 4-го знака) (считать не по уникальным ID пользователей,
#     а по суммарному количеству строк)

round(data.query(" (Gender == 'M' and Age == '26-35') or (Gender == 'F' and \
    (Age == '36-45' or Age == '46-50' or Age == '51-55' or Age == '55+')) ").shape[0] / data.shape[0], 4)