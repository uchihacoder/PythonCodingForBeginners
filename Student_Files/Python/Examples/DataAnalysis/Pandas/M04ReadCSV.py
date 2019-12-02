import numpy as np
import matplotlib as p
import pdb
from pandas import *

df = read_csv('train.csv')
men = df[df.Sex == 'male']
women = df[df.Sex =='female']
proportion_women_survived = float(sum(women.Survived))/len(women) * 100
proportion_men_survived = float(sum(men.Survived))/len(men) * 100
age = df.Age
avg_women_age = float(women.Age.sum())/len(men)
avg_men_age = float(men.Age.sum())/len(men)
print("Titantic statistics")
print("Women survived: {:>5.2f}%".format(proportion_women_survived))
print("Men survived:   {:>5.2f}%".format(proportion_men_survived))
print("Average age of women: {:>5.2f}".format(avg_women_age))
print("Average age of men:   {:>5.2f}".format(avg_men_age))
print(df.Age)
L = list(df.Age)
print(L)
print(df.columns)