import pandas as pd
import numpy as np

from google.colab import files
uploaded = files.upload()

!ls -F

df = pd.read_csv(data)

"""### Calculate Relative Humidity (RH) from Temperature and Dew Point
### Standard August-Roche-Magnus approximation
"""

def calculate_rh(temp, dewp):
    return 100 * (np.exp((17.625 * dewp) / (243.04 + dewp)) / np.exp((17.625 * temp) / (243.04 + temp)))

df['HUMIDITY'] = calculate_rh(df['TEMP'], df['DEWP'])

"""###Select columns relevant to your ESP32 sensors"""

features = ['PM2.5', 'CO', 'TEMP', 'HUMIDITY']
df_clean = df[features].copy()

df_clean

df_clean = df_clean.dropna()

"""### Create the "Comfort Index" Target Label
### 0 = Good/Comfortable, 1 = Poor/Uncomfortable
### Logic: If PM2.5 > 35 or CO > 1000, it's marked as 'Poor'
"""

def define_comfort(row):
    if row['PM2.5'] <= 35 and row['CO'] <= 1000:
        return 0
    else:
        return 1

df_clean['Comfort_Index'] = df_clean.apply(define_comfort, axis=1)

df_clean.to_csv('cleaned_air_quality.csv', index=False)
