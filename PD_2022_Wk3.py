import pandas as pd

def readCSV(CSVfile):
    df = pd.read_csv(CSVfile)
    return(df)

input1 = readCSV("/Users/kt/Desktop/prep/week3_2022/PD_2022_Wk3_Input1.csv")
input2 = readCSV("/Users/kt/Desktop/prep/week3_2022/PD_2022_Wk3_input2.csv")

input1 = input1[['id','gender']]
input2 = input2.rename(columns={"Student ID": "id"})

#for col in input2.columns:
    #print(col)

#merge input1 and input2 with the id column
df = pd.merge(input1, input2, on='id',how="inner")

#melt the dataframe 
df = pd.melt(df,id_vars=["id","gender"],var_name="subject",value_name='score')
df['pass']= df.score >= 75

#df['average']= df.groupby(['id','gender']).mean()

#create a new df with id,gender, average score, and number of passes)
df_1 = df.groupby(['id','gender'])['pass'].sum().reset_index(name='number of passed subject')
df= df.groupby(['id']).mean().round(1)
df_final = pd.merge(df, df_1, on='id',how='inner').drop(['pass'],axis=1)

df_final.to_csv('/Users/kt/Desktop/prep/week3_2022/PD_2022_Wk3_output.csv',index=False)
#newdf = df[(df.id == 1)]
#print(newdf)