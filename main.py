import pandas as pd


test = pd.read_csv('./test.csv')

print(test.head())

print(test.info())
# Заметим, что у Age, Fare, Cabin отсутствуют некоторые значения
# Если таких строк мало, которые содержат пустые значения, то их можно удалить
# Или вставить пропущенные значения, например, средним значением, медианой или модой


# Вывод уникальных значений по каждому столбцу
# test_columns = test.columns
# for i in range(len(test_columns)):
#     print(f'\n{test_columns[i]} : ', test[f'{test_columns[i]}'].unique())

# Проверка на наличие пропущенных значений
print(test.isnull().sum())

# Вставляем вместо пропущенных значений наиболее часто встречающиеся значения
test['Age'].fillna(test.Age.mode()[0], inplace=True)
test['Fare'].fillna(test.Fare.mode()[0], inplace=True)

# Проверка на наличие пропущенных значений
print(test.isnull().sum())

# Дубликатов нет
print(test.duplicated().sum())