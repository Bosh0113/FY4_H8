import imageio


def create_gif(image_list, gif_name, duration=1):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


if __name__ == "__main__":
    gif_imgs = [
        r'E:\PhD_Workspace\FY4_H8_WS\20230509\figure\FY4_FYCenter_202106190300_NIR_s1.png',
        r'E:\PhD_Workspace\FY4_H8_WS\20230509\figure\FY4_GeoNEX_202106190300_NIR_s1.png'
    ]
    gif_path = r'E:\PhD_Workspace\FY4_H8_WS\20230509\figure\FY4A_GeoNEX-FYCenter_s1.gif'
    create_gif(gif_imgs, gif_path)
