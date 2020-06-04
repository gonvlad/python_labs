import pandas
import matplotlib.pyplot as plt

data_frame = pandas.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ["Belarus"]
country_data = data_frame[data_frame["Country"].isin(countries)]

diff_df = country_data
diff_df["All_cases"] = country_data[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
diff_df["Difference"] = country_data['All_cases'].diff()

country_data.plot(x = "Date", y = ["Confirmed", "Recovered", "Deaths"], kind='line')
plt.show()

diff_df.plot(x = "Date", y = "Difference", kind="line")
plt.show()
