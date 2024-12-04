
import pandas as pd

# df = pd.read_csv('YT_data_1.csv')
df = pd.read_csv('C:/Users/HP/django_learnex_1/dLearnex/dLearnex/YT_data_1.csv')

def func_1(course_name, topic, subtopic):
    # Ensure data consistency
    df_1 = df[
        (df['organisation'].str.strip().str.lower() == course_name.strip().lower()) & 
        (df['module'].str.strip().str.lower() == topic.strip().lower()) & 
        (df['topic'].str.strip().str.lower() == subtopic.strip().lower())
    ]

    print(df_1.head())

    # print(df_1.channel.unique())
    df_unique = df_1.drop_duplicates(subset='channel')

    return df_unique

# func_1('Python', 'Functions', 'Parameters')

