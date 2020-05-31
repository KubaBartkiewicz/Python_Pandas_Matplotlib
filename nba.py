import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('nba.csv',index_col = 'Name')
data.drop(data[data['Salary'].isnull()].index, inplace=True)
#data.drop('Name', axis = 1, inplace = True)
#data = data.reset_index(drop=True)

height_dict = dict()
for i in set(data['Height']):
    height_dict.update({i:round(int(i[0])*30.48 + int(i[2])*2.54)})
data = data.replace({'Height' : height_dict})

weight_dict = dict()
for i in set(data['Weight']):
    weight_dict.update({i:round(i*0.45359237)})
data = data.replace({'Weight' : weight_dict})    

college_dict = dict()
for n,i in enumerate(set(data['College'])):
    college_dict.update({i:n})
data = data.replace({'College' : college_dict})

for i in set(data['Position']):
    x = data.loc[data['Position'] == i].mean(axis = 0 ,skipna = True)
    print({i:round(x['Weight'])})

dict_teams_age = dict()    
for i in set(data['Team']):
    x = data.loc[data['Team'] == i]
    dict_teams_age.update({i:round(x['Age'].mean())})
print(max(dict_teams_age, key = lambda k :dict_teams_age[k] ) )

print(data.loc[data['Height'].idxmax()])
 
fig = plt.figure(figsize=(15,10))
ax = fig.subplots(2, 2)
fig.suptitle('Los Angeles Lakers')

lla = data.loc[data['Team'] == 'Los Angeles Lakers']
print(lla)
ax[0,0].plot(lla['Height'], lla['Weight'], 'bo')
ax[0,0].grid()
ax[0,0].set_xticks(range(180,226,5))
ax[0,0].set_yticks(range(70,130,5))
ax[0,0].set_xlabel('Height  [cm]')
ax[0,0].set_ylabel('Weight  [kg]')

ax[0,1].plot(data['Position'], data['Height'], 'go',
             lla['Position'], lla['Height'], 'ro')
ax[0,1].set_xticks(['PG','SG','SF','PF','C'])
ax[0,1].set_xlabel('Position')
ax[0,1].set_ylabel('Height [cm]')
ax[0,1].grid()

ax[1,0].pie(lla['Salary'], labels = lla.index, autopct = '%0.0f%%', pctdistance = 0.9, startangle=150 )

fig.show()
    
positions_dict = dict()
for n,i in enumerate(['PG','SG','SF','PF','C'], start = 1):
    positions_dict.update({i:n})
data = data.replace({'Position' : positions_dict})

teams_dict = dict()
for n,i in enumerate(set(data['Team'])):
    teams_dict.update({i:n})
data = data.replace({'Team' : teams_dict})

print(data.corr(method = 'spearman'))

