import xarray as xr
import h5py
import numpy

# netCDF
nc_path = r'D:\PhD_Workspace\FY4_H8_WS\20230427\FY4A-_AGRI--_N_DISK_1047E_20210101024500.NC'
ds = xr.open_dataset(nc_path)
b1_dn = ds['Channel01'].values
b1_array = numpy.array(b1_dn)
print(b1_array.max())

# # HDF
# hdf_path = r'D:\PhD_Workspace\FY4_H8_WS\20230427\FY4A-_AGRI--_N_DISK_1047E_L1-_FDI-_MULT_NOM_20220624000000_20220624001459_1000M_V0001.HDF'
# hdf_path = r'D:\PhD_Workspace\FY4_H8_WS\20230427\FY4A-_AGRI--_N_DISK_1047E_L1-_FDI-_MULT_NOM_20220624061500_20220624062959_1000M_V0001.HDF'
# f = h5py.File(hdf_path, 'r')
# # print(f.keys())
# dset = f['NOMChannel01']
# d_array = numpy.array(dset)
# n_array = d_array[d_array<65534]
# print(n_array.max())