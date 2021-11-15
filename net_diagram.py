import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

if __name__ == "__main__":

     df = pd.read_csv(r'49945.csv', sep=';')
     df_homi = df.loc[df['Causas (lista reducida)'] == "099  Agresiones (Homicidio)"]
     df_homi_total = df_homi.loc[df_homi['Sexo'] == "Ambos sexos"]
     df_homi_total = df_homi_total.loc[df_homi['Total'] < 2]
     df_homi_total_final = df_homi_total.loc[df_homi_total['Provincia de residencia'] != "Total"]
     df_final = df_homi_total_final[["Provincia de residencia", "Total"]]
     df_final['Total'] = df['Total'].astype('int')

     G = nx.Graph()

     start = df_final['Provincia de residencia'].tolist()
     to = [2, 4, 6, 8]  # La lista de puntos finales del lado, importe la declaración de punto final usted mismo, los elementos en la misma posición en el inicio y las listas corresponden a
     for j in range(len(start)):
          G.add_edge(start[j], df_final.loc[df_final['Provincia de residencia'] == start[j]]['Total'].values[0])

     nx.draw(G,node_color='red', edge_color='green',width=5,with_labels=True, arrowsize=1000, node_size=100)
     #plt.show()
     plt.savefig('homicidios_diagrama_red.tiff')




