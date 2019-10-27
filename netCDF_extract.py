'''extract temporal series at point value in WRFoutput file to one variavel '''

from netCDF4 import Dataset
import pandas as pd


def getXYcoordinate(lat,lon,nc):
    cor_lat = pd.DataFrame(nc.variables['XLAT'][0][:])
    cor_lat2 = pd.DataFrame({'a': cor_lat.iloc[:, 0], 'b': abs(cor_lat.iloc[:, 0] - lat)})
    x = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.to_numpy()[0]

    cor_lon = pd.DataFrame(nc.variables['XLONG'][0][:])
    cor_lon2 = pd.DataFrame({'a': cor_lon.iloc[0, :], 'b': abs(cor_lon.iloc[0, :] - lon)})
    y = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.to_numpy()[0]

    return  x , y




def extractpoint(x, y, nc,  variavel = 'T2', convert = True):

    if convert==True:
        vlr = (nc.variables[variavel][:, x, y]-273.15)[:] #This change from kelvin to celsius

    else:
        vlr = (nc.variables[variavel][:, x, y])[:] #This change from kelvin to celsius

    return vlr


def extractvariavel(netCDFfile,variavel = 'T2'):
    nc = Dataset(netCDFfile)
    variavel = (nc.variables[variavel][:])[:]
    return variavel



# # open file
# path = '/home/rafael/WRF/Build_WRF/WRFV3/run/wrfout_d03_2017-12-16_00:00:00'
#
# nc = Dataset(path)
# # latbounds = -23.050334
# # lonbounds = -43.5956
# #
# # x,y = getXYcoordinate(latbounds,lonbounds)
# #
# # vlr = extract(x,y,nc,convert=False)
# #
# import matplotlib.pyplot as plt
# # plt.plot(vlr)
# # plt.show()
#
# var = extractvariavel(path,variavel='LU_INDEX')
#
#
#
# plt.imshow(var[3,:,:])
# plt.show()