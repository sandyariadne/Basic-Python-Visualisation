import pandas as pd

df = pd.DataFrame(
[
    ["surabaya", 120, 60],
    ["surabaya", 200, 20],
    ["surabaya", 220, 40],
    ["jakarta", 290, 30],
    ["jogja", 290, 30],
    ["solo", 190, 20],
    ["padang", 170, 40],
    ["lampung", 230, 78],
], columns = ["kota", "angka1", "angka2"]
)

# Pandas Veez
df.plot.scatter(x='angka1', y='angka2', title='scatter_plot')

df.plot.line(title='line chart')

df.drop(['angka2'], axis=1).plot.line(title='line chart')

df.plot.bar(title='bar chart', x="kota", y=["angka1","angka2"])

df['angka1'].value_counts().sort_index().plot.bar()

df['angka2'].value_counts().sort_index().plot.barh()

df.groupby("kota").angka1.mean().sort_values(ascending=False).plot.bar()


# Seaborn Visualization
import seaborn as sns
sns.scatterplot(x='angka1', y='angka2', data=df)

sns.scatterplot(x='angka1', y='angka2', hue='kota', data=df)

sns.lineplot(data=df.drop(['kota'], axis=1))

sns.barplot(x="kota", y="angka2", data=df)

sns.barplot(x="kota", y="angka1", data=df)


# Matplotlib Veez
import matplotlib.pyplot as plt
# create a figure and axis
fig, ax = plt.subplots()

# scatter the angka1 against the angka2
ax.scatter(df['angka1'], df['angka2'])
# set a title and labels
ax.set_title('Scatter Matplotlib')
ax.set_xlabel('angka1')
ax.set_ylabel('angka2')




# create color dictionary
colors = {'jakarta':'red', 
          'surabaya':'green', 
          'padang':'blue',
          'lampung':'yellow',
          'jogja':'black',
          'bandung':'purple',
          'denpasar':'orange',
         }
# create a figure and axis
fig, ax = plt.subplots()

# scatter the angka1 against the angka2
#ax.scatter(df['angka1'], df['angka2'])

# plot each data-point
for i in range(len(df['angka1'])):
    ax.scatter(df['angka1'][i], 
               df['angka2'][i],
               color=colors[df['kota'][i]])
# set a title and labels
ax.set_title('Colored Scatter plot')
ax.set_xlabel('angka1')
ax.set_ylabel('angka2')



# get columns to plot
columns = df.columns.drop(['kota'])
# create x data
x_data = range(0, df.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df[column])
# set title and legend
ax.set_title('Line chart')
ax.legend(["angka1", "angka2"])


# get columns to plot
columns = df.columns.drop(['kota'])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(df["kota"], df[column])
# set title and legend
ax.set_title('Line chart')
ax.legend(["angka1", "angka2"])


# create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = df['kota'].value_counts() 
# get x and y data 
points = data.index 
frequency = data.values 
# create bar chart 
ax.bar(points, frequency) 
# set title and labels 
ax.set_title('Bar chart') 
ax.set_xlabel('kota') 
ax.set_ylabel('Frequency')



# Statistical Veez
df.angka1.plot.hist()

df.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)

df.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=100)
