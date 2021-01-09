import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = np.array([
      len( df.loc[ df['race'] == df['race'].unique()[0] ]),
      len( df.loc[ df['race'] == df['race'].unique()[1] ]),
      len( df.loc[ df['race'] == df['race'].unique()[2] ]),
      len( df.loc[ df['race'] == df['race'].unique()[3] ]),
      len( df.loc[ df['race'] == df['race'].unique()[4] ])
    ])

    # What is the average age of men?
    average_age_men = int(np.mean( df.loc[ df['sex'] == 'Male' ]['age'] ))

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = int( len( df.loc[ df['education'] == 'Bachelors']) / len( df.loc[ df['education'] != 'Bachelors']) )

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[ df.education.isin(['Bachelors', 'Masters', 'Doctorate']) ]
    lower_education = df.drop(higher_education.index)

    # percentage with salary >50K
    higher_education_rich = int( len(higher_education.loc[higher_education.salary.isin(['>50K'])]) / len(higher_education) * 100)
    lower_education_rich = int( len(lower_education.loc[lower_education.salary.isin(['>50K'])]) / len(lower_education) * 100)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min( df["hours-per-week"] )

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[ df["hours-per-week"] == min_work_hours ]

    rich_percentage = int( len(num_min_workers.loc[num_min_workers.salary.isin(['>50K'])]) / len(num_min_workers) * 100)

    # What country has the highest percentage of people that earn >50K?
    rich_countries = df.loc[ df.salary.isin(['>50K']) ]["native-country"]
    highest_earning_country = rich_countries.mode()[0]
    highest_earning_country_percentage = np.int( len(rich_countries.loc[ rich_countries.isin([highest_earning_country]) ]) / len(rich_countries) )

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df.loc[ df["native-country"].isin(["India"])]
    rich_india_occs = india_df.loc[ india_df.salary.isin([">50K"])]["occupation"]
    top_IN_occupation = rich_india_occs.mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
