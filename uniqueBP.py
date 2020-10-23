#!/usr/local/bin/python3
import numpy as np
import pandas as pd


 
def uniqueBP(df_in):
  #controllare se esiste colonna BP
  if 'BP' in df_in.columns:
    d2 = pd.DataFrame(df_in,columns=['BP'])
    ret = d2.drop_duplicates(subset=['BP'])
  else:
    ret= pd.DataFrame( columns=['BP'])
  return(ret)
  
	
def main():
  print ("funzione di libreria python_bigdata")
  print ("estrae lista unica dalla colonna BP")
  data = pd.DataFrame([('Andrea', 12, 178),
                     ('Maria', 14, 154),
                     ('Maria', 14, 154),
                     ('Luca', 15, 175)],
                    columns=['nome', 'BP', 'indirizzo'])
                    
  data_noBP = pd.DataFrame([('Andrea', 12, 178),
                     ('Maria', 14, 154),
                     ('Maria', 14, 154),
                     ('Luca', 15, 175)],
                    columns=['nome', 'telefono', 'indirizzo'])                   
  print("data frame originale")
  print(data)
  print("dataframe con valori del campo BP univoci")
  print(uniqueBP(data))
  print("dataframe senza colonna BP")
  print(uniqueBP(data_noBP))
  
if __name__== "__main__":
  main()

  



