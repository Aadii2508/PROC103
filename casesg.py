import pandas as pd
import plotly.express as xp

covidg =pd.read_csv("COVID_data.csv")
disp =xp.scatter(covidg, title="Graph 1", x="date", y="cases", color="Country")
disp.show()