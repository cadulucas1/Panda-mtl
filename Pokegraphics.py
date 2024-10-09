import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon11.csv')

df.set_index('Generation', inplace=True)

lendario = df.query('Legendary == True')
data = lendario.loc[:, ['Name', 'Total']]
exp = [0.1 if i != 0 else 0.3 for i in range (len(data))]

plt.pie(data.iloc[:, 1], labels=data.iloc[:, 0], autopct='%.2f%%', startangle=85)
plt.tight_layout()
plt.show()

plt.bar(data.iloc[:, 0], data.iloc[:, 1], color='#8232d7')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#numero 2
fogo = df.query('Type_1 == "Fire" & Type_2 != ""')
#print(fogo[:])
data1 = fogo.loc[:, ['Name', 'Speed','Sp. Atk']]
exp1 = [0.1 if i != 0 else 0.3 for i in range (len(data1))]
#print(data1[:])

plt.pie(data1.iloc[:, 1], labels=data1.iloc[:, 0], autopct='%.2f%%', startangle=85)
plt.tight_layout()
plt.show()
bar_width = 0.35
ind1 = [i for i in range(len(data1))] 
ind2 = [i+bar_width for i in range(len(data1))] 
ind3 = [i+bar_width/2 for i in range(len(data1))] 

x=data1.iloc[:, 0]
y1=data1.iloc[:, 1]
y2=data1.iloc[:, 2]
plt.bar(ind1, y1, width=bar_width, color='#8232d7', label='Speed')
plt.bar(ind2 , y2, width=bar_width, color='#3235d7', label='Sp. Atk')
plt.xticks(ind3, x)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#nuemro3
numero = df.query('HP <=30 ')
data2 = numero.loc[:, ['Name', 'HP']]
exp2 = [0.1 if i != 0 else 0.3 for i in range (len(data))]

plt.bar(data2.iloc[:, 0], data2.iloc[:, 1], color='#8232d7')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#nuemro4
numero = df.query('Defense >60 & Type_1 == "Bug"')
data3 = numero.loc[:, ['Name', 'Defense','HP','Sp. Def','Total' ]]
exp3 = [0.1 if i != 0 else 0.3 for i in range (len(data))]

bar = 0.35
indc1 = [i for i in range(0,len(data3)*3,3)] 
indc2 = [i+bar for i in range(0,len(data3)*3,3)]
indc21 = [i+bar*2 for i in range(0,len(data3)*3,3)] 
indc22 = [i+bar*3 for i in range(0,len(data3)*3,3)] 
indc3 = [i+bar/2 for i in range(0,len(data3)*3,3)] 

x1=data3.iloc[:, 0]
y3=data3.iloc[:, 1]
y4=data3.iloc[:, 2]
y5=data3.iloc[:, 3]
y6=data3.iloc[:, 4]

plt.bar(indc1, y3, width=bar, color='#3235d7', label='Defense')
plt.bar(indc2 , y4, width=bar, color='#35d732', label='HP')
plt.bar(indc21 , y5, width=bar, color='#32d7d4', label='Sp. Def')
plt.bar(indc22 , y6, width=bar, color='#d73235', label='Total')

plt.xticks(indc3, x1)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#nuemro5
legendary = df.query('Legendary == True')
data4 = legendary.loc[:, ['Name','Attack','Defense','HP','Sp. Def','Sp. Atk','Speed','Total' ]]
exp4 = [0.1 if i != 0 else 0.3 for i in range (len(data4))]

bar = 0.35
inc1 = [i for i in range(0,len(data4)*5,5)] 
inc2 = [i+bar for i in range(0,len(data4)*5,5)]
inc21 = [i+bar*2 for i in range(0,len(data4)*5,5)] 
inc22 = [i+bar*3 for i in range(0,len(data4)*5,5)]
inc23 = [i+bar*4 for i in range(0,len(data4)*5,5)] 
inc24 = [i+bar*5 for i in range(0,len(data4)*5,5)] 
inc25 = [i+bar*6 for i in range(0,len(data4)*5,5)] 
inc3 = [i+bar/2 for i in range(0,len(data4)*5,5)] 

x2=data4.iloc[:, 0]
y7=data4.iloc[:, 1]
y8=data4.iloc[:, 2]
y9=data4.iloc[:, 3]
y10=data4.iloc[:, 4]
y11=data4.iloc[:, 5]
y12=data4.iloc[:, 6]
y13=data4.iloc[:, 7]

plt.bar(inc1, y7, width=bar, color='#ff0000', label='Attack')
plt.bar(inc2 , y8, width=bar, color='#0000ff', label='Defense')
plt.bar(inc21 , y9, width=bar, color='#3cb371', label='HP')
plt.bar(inc22 , y10, width=bar, color='#ee82ee', label='Sp. Def')
plt.bar(inc23 , y11, width=bar, color='#32d7d4', label='Sp. Atk')
plt.bar(inc24 , y12, width=bar, color='#e3a972', label='Speed')
plt.bar(inc25 , y13, width=bar, color='#ffa500', label='Total')


plt.xticks(inc3, x2)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()