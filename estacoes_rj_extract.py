import pandas as pd
import netCDF_extract as ext
from netCDF4 import Dataset
#
path = '/home/rafael/WRF/Build_WRF/WRFV3/run/wrfout_d03_2017-12-16_00:00:00'
nc = Dataset(path)

df = pd.read_csv('../../dados_informacoes/estacoes.csv')

estacoes = df.Estacoes
lat = df.LAT.values
lon = df.LON.values
t2 = {}

for i in range(len(estacoes)):
    x , y = ext.getXYcoordinate(lat[i],lon[i],nc)
    vlr = ext.extractpoint(x,y,nc)
    t2[estacoes[i]] = vlr


dataframe = pd.DataFrame.from_dict(t2)
index = pd.DatetimeIndex(start = '2017-12-15 21:00:00', freq = 'H',periods =67)
dataframe.index = index


dataframe.to_json('wrf4.json')



print("concluido")
