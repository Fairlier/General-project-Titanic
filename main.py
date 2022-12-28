import pandas as pd


test = pd.read_csv('./test.csv')


# print(test.head())


print(test.info())


'''
    Заметим, что у Age, Fare, Cabin отсутствуют некоторые значения
    Если таких строк мало, которые содержат пустые значения, то их можно удалить
    Или вставить пропущенные значения, например, средним значением, медианой или модой 
'''


# Вывод уникальных значений по каждому столбцу
# test_columns = test.columns
# for i in range(len(test_columns)):
#     print(f'\n{test_columns[i]} : ', test[f'{test_columns[i]}'].unique())


# Проверка на наличие пропущенных значений
print(test.isnull().sum())


# Вставляем вместо пропущенных значений наиболее часто встречающиеся значения
female_age = test[test.Sex == 'female'].Age.mean()
male_age = test[test.Sex == 'male'].Age.mean()

test.loc[test.Sex == 'female', 'Age'] = test.Age.fillna(female_age)
test.loc[test.Sex == 'male', 'Age'] = test.Age.fillna(male_age)


# Проверка на наличие пропущенных значений
print(test.isnull().sum())

# Вставляем вместо пропущенных значений наиболее часто встречающиеся значения
pclass_value = test.Pclass.unique()
for i in pclass_value:
    temp_mean = test[test.Pclass == i].Fare.mean()
    test.loc[test.Pclass == i, 'Fare'] = test.Fare.fillna(temp_mean)


# Проверка на наличие пропущенных значений
print(test.isnull().sum())


# Удалим столбец Cabin
test.drop(['Cabin'], axis='columns', inplace=True)


# Проверка на наличие пропущенных значений
print(test.isnull().sum())


# Заменим значения столбца Sex female на 0, male на 1
test.loc[test.Sex == 'female', 'Sex'] = 0
test.loc[test.Sex == 'male', 'Sex'] = 1

test = test.astype({'Sex': 'int'})


# Проверка на измения значения и типа столбца Sex
print(test.Sex.value_counts())


# Проверка на наличие дубликатов
print(test.duplicated().sum())
