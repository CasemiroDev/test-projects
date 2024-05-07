import pandas as pd
import numpy as np

x = str(input("Type the DataBase with the weights of the any vacancies: "))
y = str(input("Type the DataBase with the knowledge of any candidacts: "))

def readatas(o):
    """

    This function read the wheights of any technologies and return the variable for can be use globally.

    o - Wants to be the archive xlsx with the weights of all technologies.

    df ::: DataFrame with the wheights.

    Is to much important the number of columns in df and df2 be equal!!!

    """
    df = pd.read_excel(o, sheet_name=0)
    return df

def normalization(df,i):
    """

    This Function do the normalization of the datas removing the zeros and removing class columns
    for the algorithm can use just the numerical datas.

    df_rm ::: Remove the columns thats have just zeros in df.
    pro_data ::: Convert the DataFrame df_rm into a list.
    df2 ::: DataFrame with the qualification of all candidacts.
    norm_df2 ::: Removing the column names of df2.
    df2_rm ::: Removing the columns thats have just zeros in df to stay equal with pro_data.
    pro_data2 ::: Convert the DataFrame df2_rm into a list.

    """
    df_rm = df.loc[:, (df != 0).any(axis=0)]
    pro_data = df_rm.values.tolist()

    df2 = pd.read_excel(i, sheet_name=0)
    norm_df2 = df2.drop('names', axis=1)
    df2_rm = norm_df2.loc[:, (df != 0.).any(axis=0)]
    pro_data2 = df2_rm.values.tolist()
    
    return pro_data, pro_data2, df2

def wheigthap(vacancy):
    """
    This function multiplicate the knowledge of any candidacts with the respective weights and after
    this do the division with them sum of the wheights, this form doing a rank with the best profesionals.

    vacancy - is the vacancy in the df, for can analisys the candidacts.

    multiplied ::: do the multiplication of the pro_data2 with the chosen vacancy in pro_data.
    wheights ::: Convert the multiplied(array of numpy) into a list.
    df3 ::: Transform the respective multiplications in wheights into a DataFrame, and are removed the zeros.
    df3_rm ::: Remove the columns thats have just zeros in df3.
    pro_data3 ::: Convert the DataFrame df3_rm into a list.
    cont ::: Is the first counter.
    cont2 ::: Is the second counter.
    listsum ::: Is the variable of results at the sum of knowledge x weights.
    list_pro ::: Is the list with the results of listsum into a list.
    cont3 ::: Is the third counter.
    cont4 ::: Is the quarter counter.
    app ::: Is the final list with the results of the knowledge at any candidacts with the weights applied.
    cache ::: Is Is the variable of results at the division of the knowledge just already applied.
    the weights and the sum at the total of weights.
    app_new ::: Transform a list app into a DataFrame and insert the column names with the respective names in
    df2.
    app_new2 ::: Convert app_new into a list
    app_new3 ::: organize the app_new2 in a decrescent form
    df_final ::: Transform the app_new3 already organizated into a DataFrame and download in the past of the
    project(archive xlsx).

    """
    multiplied = list(np.multiply(pro_data2,pro_data[vacancy - 1]))
    wheights = np.array(multiplied).tolist()

    df3 = pd.DataFrame(wheights)
    df3_rm = df3.loc[:, (df3 != 0.).any(axis=0)]
    pro_data3 = df3_rm.values.tolist()


    cont = 0
    cont2 = 0
    listsum = 0
    list_pro = []
    while cont != len(pro_data2):
        listsum += sum(pro_data3[cont2])
        cont += 1
        cont2 += 1
        list_pro.append(listsum)
        listsum = 0

    cont3 = 0
    cont4 = 0
    app = []
    while cont4 != len(list_pro):
        cache = list_pro[cont3] / sum(pro_data[vacancy-1])
        cont3 += 1
        cont4 += 1
        app.append(cache)
        cache = 0

    app_new = pd.DataFrame(app)
    app_new['names'] = df2['names']

    app_new2 = app_new.values.tolist()
    app_new3 = sorted(app_new2,reverse=True)
    df_final = pd.DataFrame(app_new3)
    df_final.to_excel("Ranking.xlsx", sheet_name='rank',index=False)
 
df = readatas(x)
pro_data, pro_data2, df2 = normalization(df,y)
readatas(x)
normalization(df,y)
wheigthap(4)

