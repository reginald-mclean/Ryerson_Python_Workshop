''''
O'Reilly Data Analysis with Python Book
https://learning.oreilly.com/library/view/python-for-data/9781491957653/

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
from collections import defaultdict
import seaborn as sns
np.set_printoptions(precision=4)
pd.options.display.max_rows = 20


########################################################################################################
################################### Time Zone Example ##################################################
########################################################################################################
'''


path = 'datasets/bitly_usagov/example.txt'

line = open(path).readline()
#print(line)
#print(type(line))


records = [json.loads(line) for line in open(path)]
# print(records)


# print(records)

# time_zones = [rec['tz'] for rec in records]
# print(time_zones)

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

"""
time_zones = []
for rec in records
    if 'tz' in rec:
        time_zones.append(rec['tz'])
"""

#print(time_zones[:10])


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_counts_2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_counts(time_zones)
counts_2 = get_counts_2(time_zones)
# print(counts)
# print(counts_2)

# print(counts['America/New_York'])
# print(counts_2['America/New_York'])
# print(len(time_zones))
# print(len(counts))


def top_counts(dict, n=10):
    pairs = [(count, tz) for tz, count in dict.items()]
    pairs.sort()
    return pairs[-n:]


top_count = top_counts(counts)
#sns.barplot(y=[x[1] for x in top_count], x=[x[0] for x in top_count])
#plt.show()
#plt.close()
# print(records)
dataframe = pd.DataFrame(records)
# print(dataframe)
# print(dataframe.columns)
# print(dataframe['tz'].value_counts())

clean_frame = dataframe['tz'].fillna('Missing')
clean_frame[clean_frame == ''] = 'Unknown'

# print(clean_frame.value_counts())

# print(clean_frame.value_counts())

# print(clean_frame.index)
subset = clean_frame.value_counts()[:10]
sns.barplot(y=subset.index, x=subset.values)
# plt.show()
# plt.close()

# print(dataframe['a'])
# print(dataframe['tz'])
# print(dataframe['a'][50])
# print(dataframe['a'][51][:50])

results = pd.Series([x.split()[0] for x in dataframe.a.dropna()])
# print(results)
# print(results[:5])
# print(results.value_counts())

# cframe = dataframe[dataframe.a.notnull()]
# cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# print(cframe['os'][:5])
# print(cframe)

# by_tz_os = cframe.groupby(['tz', 'os'])
# print(by_tz_os)
# aggregate_counts = by_tz_os.size().unstack().fillna(0)
# print(aggregate_counts[:10])

########################################################################################################
################################### MovieLens Example ##################################################
########################################################################################################

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('datasets/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('datasets/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genre']
movies = pd.read_table('datasets/movielens/movies.dat', sep='::', header=None, names=mnames)

# ratings_and_users =
data = pd.merge(pd.merge(ratings, users), movies)
# print(data.columns)

# this is an aside about pivoting a table

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
print(df)
table = pd.pivot_table(df, values='D', index=['A', 'B'],
                   columns=['C'], aggfunc=np.sum)
print(table)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print(mean_ratings[:5])

ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print(active_titles)
mean_ratings = mean_ratings.rename(index={'Seven Samurai (The Magnificent Seven) (Shichinin no samurai) (1954)':
                           'Seven Samurai (Shichinin no samurai) (1954)'})

# top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print(top_female_ratings[:10])

# top_male_ratings = mean_ratings.sort_values(by='M', ascending=False)
# print(top_male_ratings[:10])

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])
rating_std_by_title = data.groupby('title')['rating'].std()
print(rating_std_by_title)
rating_std_by_title = rating_std_by_title.loc[active_titles]
print(rating_std_by_title)
rating_std_by_title = rating_std_by_title.sort_values(ascending=True)[:10]
print(rating_std_by_title)


########################################################################################################
################################### Baby Names Example #################################################
########################################################################################################

names = ['reggie', '1', '2']
names1880 = pd.read_csv('datasets/babynames/yob1880.txt', names=['name', 'sex', 'births'])
print(names1880.groupby('sex').births.sum())
print(names1880)

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in range(1880, 2011):
    path = 'datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# print(len(pieces))
# print(pieces)
names = pd.concat(pieces, ignore_index=True)
# print(names)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births.tail())
total_births.plot(title='Total births by sex and year')
plt.show()

def add_property(group):
    group['prop'] = group.births / group.births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_property).sort_values(by='prop', ascending=False)
# print(names.head(10))


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.reset_index(inplace=True, drop=True)
# print(top1000.head(10))

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
# print(total_births.info())

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
# plt.show()
'''