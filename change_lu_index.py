# substitui lu_index
from netCDF4 import Dataset 
import numpy as np

def change(new):
	lunew = np.load(new)
	nc = Dataset('geo_em.d03.nc','a')
	nc.variables['LU_INDEX'][0,:] = lunew
	nc.close
	print('Complete change!!!!!') 

new = 'lu_rj_1km.npy'


if __name__ == '__main__':
	change(new)

