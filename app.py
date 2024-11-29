import pandas as pd

# Эта программа считывает данные о сотрудниках из CSV файла, вычисляет среднюю зарплату
# и фильтрует сотрудников старше 30 лет.
if __name__ == '__main__':
    dataframe = pd.read_csv('data.csv')
    print(f"Всего строк в файле: {len(dataframe)}")
    average_salary = dataframe['salary'].mean()
    print(f"Средняя зарплата всех сотрудников: {average_salary}")
    print("Сотрудники, возраст которых старше 30 лет:")
    print(dataframe.loc[(dataframe['age'] > 30)])

