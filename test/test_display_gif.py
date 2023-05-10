import imageio


def create_gif(image_list, gif_name, duration=1):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


if __name__ == "__main__":
    figure_folder = r'E:\PhD_Workspace\FY4_H8_WS\20230510'
    time_list = ['20210619010000', '20210619020000', '20210619024500', '20210619030000', '20210619031500', '20210619040000', '20210619050000', '20210619054500', '20210619060000', '20210619061500', '20210619070000']
    gif_imgs = []
    for time_str in time_list:
        figure_path = figure_folder + '/geolocation_FY4A_AGRI_' + time_str + '.png'
        gif_imgs.append(figure_path)
    gif_path = figure_folder + '/FY4A_GeoNEX_20210619.gif'
    create_gif(gif_imgs, gif_path)
