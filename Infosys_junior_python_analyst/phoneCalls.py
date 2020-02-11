import pandas as pd
import dateutil

# Load data from csv file
data = pd.read_csv('./phone_data.csv', index_col='index', header=0)
# Convert date from string to date times
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

#1
print("How many rows does the data variable have?")
print(data['item'].count())

#2
print("What was the duration of the longest call?")
print(data['duration'].max())

#3
print("How long did the outgoing calls last? ('item' = 'call')?")
print(data[data["item"] == 'call'].sum()["duration"])

#4
print("Group the data by month, output the total duration of calls of each month.")
print(data.groupby('month')['duration'].sum())

#5
print("What is the total of durations of the calls to each network?")
print(data[data["item"] == 'call'].groupby('network').sum()['duration'])

#6
print("How many calls (call), SMSs (sms) and records (data) there were each month?")
print(data.groupby(['month', 'item'])['item'].count())

#7
print("Divide all records that have 'item' = 'call' and output data describing:")
print(data[data['item'] == 'call'].groupby('month').agg(

#8 Total duration of the calls
    total_duration=('duration', sum),
#9 Average duration of the calls
    mean_duration=('duration', lambda x: (sum(x)/len(x))),
#10 Number of connections
    sum_calls=('item', len),
#11 Min. and max. dates in a month and their range.
    max_date=('date', max),
    min_date=('date', min),
    range_in_days=("date", lambda x: (max(x) - min(x)).days)
))
