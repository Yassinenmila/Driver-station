from .explore import df 

char= [
    'fuel',
    'seller_type',
    'transmission',
    'owner'
]

for c in char :
    df[c]=df[c].fillna(df[c].mode()[0])

num = [
    'year',
    'selling_price',
    'km_driven'
]

for n in num:
    df[n]=df[n].fillna(df[n].median())



df = df.drop_duplicates()

# print('year = ', (df["year"]<1900).sum())
# print('km = ', (df['km_driven']<0).sum())
# print('prix = ',(df['selling_price']<0).sum())

for c in char :
    print(df[c].value_counts())
