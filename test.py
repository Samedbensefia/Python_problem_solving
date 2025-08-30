import pandas as pd
import datetime as Dt
import random

start_date = Dt.date.today()
end_date = start_date + Dt.timedelta(days=5)
Tindex = pd.date_range(start=start_date, end= end_date, freq="h" )

temps = []
for hour in Tindex:
    temp = random.randint(20,40)
    temps.append(temp)
    
df = pd.DataFrame({
    "DateTime" : Tindex,
    "Temperature" : temps
})

df = df.groupby(df['DateTime'].dt.date)['Temperature'].mean()





