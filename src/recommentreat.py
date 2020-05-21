import pandas as pd
from scipy.spatial.distance import pdist, squareform

def recommend(sex, diab, age, trauma, myopia, col, diag):

    newpatient = {"Patient ID": "New patient",
              "Sex": sex, 
              "Diabetes": diab, 
              "Ageing": age,
              "Eye Trauma": trauma,
              "Myopia": myopia,
              "Cholesterol": col}

    df = pd.read_csv("INPUT/treatments.csv")
    df_rec = df[df["Diagnostic"]==diag]
    df_rec.drop(columns=["Diagnostic", "Treatment"], inplace = True)
    df_rec = df_rec.append(pd.Series(newpatient), ignore_index=True)
    df_rec = df_rec.set_index("Patient ID")
    df_rec = df_rec.T

    distances = pd.DataFrame(1/(1 + squareform(pdist(df_rec.T, 'euclidean'))), 
                         index=df_rec.columns, columns=df_rec.columns)

    similarities_new = distances['New patient'].sort_values(ascending=False)[1:]
    sim_pac = similarities_new[0:3]
    pat_ID = list(sim_pac.index)

    result = df[(df["Patient ID"] == pat_ID[0]) | (df["Patient ID"] == pat_ID[1]) | (df["Patient ID"] == pat_ID[2])]
    return result