import matplotlib.pyplot as plt
import pandas as pd



if __name__ == "__main__":

     df = pd.read_csv(r'49945.csv',sep=';')
     df_homi = df.loc[df['Causas (lista reducida)'] == "099  Agresiones (Homicidio)"]
     df_homi_total = df_homi.loc[df_homi['Sexo'] == "Ambos sexos" ]
     df_homi_total_final = df_homi_total.loc[df_homi_total['Provincia de residencia'] != "Total"]
     df_final = df_homi_total_final[["Provincia de residencia", "Total"]]


     df_final.plot.bar(x='Provincia de residencia',y='Total',figsize=(30,10))
     plt.savefig('homicidios.pdf')

