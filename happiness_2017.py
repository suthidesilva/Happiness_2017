# -*- coding: utf-8 -*-
"""happiness_2017.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y5UKJlfvTC_6KeXHNT2K2NrXz_jGAUAw
"""

import io
import pandas as pd
df = pd.read_csv('/content/happiness_2017.csv').dropna(axis=1, how='all')

df.shape

column_names = df.columns.tolist()
print(column_names)
column_names[5]

"""Q-5: Calculating the average happiness score. You should include three digits to the right of the decimal point."""

average_happiness_score = df['HappinessScore'].mean()
print(average_happiness_score)

"""Q-6: What is the standard deviation of the happiness score?"""

sd_happiness_score  = df['HappinessScore'].std()
print(sd)

"""Q-7: The mean value for healthy life expectancy is"""

average_healthy_life_expectancy = df['Healthy life expectancy at birth'].mean()
print(average_healthy_life_expectancy)

"""and the standard deviation is"""

sd_healthy_life_expectancy = df['Healthy life expectancy at birth'].std()
print(sd_healthy_life_expectancy)

"""Histogram for happiness score"""

df['HappinessScore'].hist()

"""Q-8: What is the maximum value in the generosity column?"""

max_generosity = df['Generosity'].max()
print(max_generosity)

"""Q-9: The index of the row containing the maximum value is"""

max_generosity_index = df['Generosity'].idxmax()
print(max_generosity_index)

"""Q-10: The name of the country that is most generous is"""

macountry = df.loc[max_generosity_index, 'Country']
print(macountry)

"""Q-11: The country with the lowest generosity score is"""

min_generosity_index = df['Generosity'].idxmin()
min_country = df.loc[min_generosity_index, 'Country']
print(min_country)

"""Q-12: What is the name of the country that has the highest confidence in their national government?"""

highest_confidence_index = df['Confidence in national government'].idxmax()
highest_confidence_country = df.loc[highest_confidence_index, 'Country']
print(highest_confidence_country)

"""Q-13: What is the name and happiness score of the country with the lowest confidence in their national government?"""

lowest_confidence_index = df['Confidence in national government'].idxmin()
lowest_confidence_country = df.loc[lowest_confidence_index, 'Country']
lowest_confidence_happiness = df.loc[lowest_confidence_index, 'HappinessScore']
print(lowest_confidence_country)
print(lowest_confidence_happiness)