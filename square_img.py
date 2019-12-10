import cv2
import glob
import matplotlib.pyplot as plt
import numpy as np
import os

# アスペクト比固定で指定サイズ内に収まるようリサイズ
def scale_box(img, width, height):
    scale = min(width / img.shape[1], height / img.shape[0])
    return cv2.resize(img, dsize=None, fx=scale, fy=scale)

# 余白部分を黒で埋める
def add_margin(img,size):
    pad_list = np.array([0 for i in range(size)])
    height = img.shape[0]
    width = img.shape[1]
    diff_height = size - height
    diff_width = size - width

    # 画像の縦幅を変更
    if diff_height <0:
        pass
    elif diff_height == 0:
        pass
    elif diff_height >0:
        while img.shape[0] <size:
            img = np.insert(img, img.shape[0], 0, axis=0)

    # 画像の横幅を変更
    if diff_width <0:
        pass
    elif diff_width == 0:
        pass
    elif diff_width >0:
        while img.shape[1] <size:
            img = np.insert(img, img.shape[1], 0, axis=1)
    return img

# 実行
def do(size = 500,input_path ="./input_example/*",output_path = "./output_example/"):
    path_list = glob.glob(input_path)
    for i in range(len(path_list)):
        filename = os.path.basename(path_list[i])
        print(filename)
        img = cv2.imread(path_list[i])
        dst = scale_box(img,size,size)
        dst = add_margin(dst,size)
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        plt.imsave(output_path+filename,dst)
        print(f"{img.shape} -> {dst.shape}")
