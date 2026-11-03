import pandas as pd
from model.predict import make_prediction

sample_input_data = pd.read_csv("C:\Users\Ramigo Garay\Downloads\_a0c6c427a3254322807983d067958cdb_taller5_archivos\taller5_files/bankchurn_test.csv")
result = make_prediction(input_data=sample_input_data)
print(result)