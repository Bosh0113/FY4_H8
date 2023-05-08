import numpy as np

# loc_raw_size = 10992
# LUT_path = '/disk2/workspace/20230505/FullMask_Grid_1000/FullMask_Grid_1000.raw'
# lon_npy_path = '/disk2/workspace/20230505/FullMask_Grid_1000/FullMask_Grid_1000_lon.npy'
# lat_npy_path = '/disk2/workspace/20230505/FullMask_Grid_1000/FullMask_Grid_1000_lat.npy'

loc_raw_size = 21984
LUT_path = '/disk2/workspace/20230505/FullMask_Grid_500/FullMask_Grid_500.raw'
lon_npy_path = '/disk2/workspace/20230505/FullMask_Grid_500/FullMask_Grid_500_lon.npy'
lat_npy_path = '/disk2/workspace/20230505/FullMask_Grid_500/FullMask_Grid_500_lat.npy'

if __name__ == "__main__":
    # 打开文件并读取所有数据
    with open(LUT_path, 'rb') as f:
        data = f.read()

    # 将数据解析为一个 Numpy 数组
    # '<' 表示使用小端字节序，'d' 表示使用 double 类型
    arr = np.frombuffer(data, dtype='<d')

    # 将数据按照经度和纬度分开，并且每个网格用一个元组表示
    grid_size = 16  # 每个网格占用 16 字节
    grid_count = len(arr) // (grid_size // 8)   # 计算网格的数量
    lat_arr = arr[0:grid_count*2:2]
    lon_arr = arr[1:grid_count*2:2]

    # grid_arr = np.array(list(zip(lon_arr, lat_arr)))
    # print(grid_arr.shape)
    lon_2d = lon_arr.reshape((loc_raw_size, loc_raw_size))
    lat_2d = lat_arr.reshape((loc_raw_size, loc_raw_size))
    np.save(lon_npy_path, lon_2d)
    np.save(lat_npy_path, lat_2d)

