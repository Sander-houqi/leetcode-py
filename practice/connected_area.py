
import cv2
import numpy as np


# seed filting 求连通域算法，只需要遍历一次图像时间复杂度O(n)；而常规算法两次遍历图像的时间复杂度O(n^2)
#参考
#http://harrymei.github.io/2019/01/14/%E6%B1%82%E8%BF%9E%E9%80%9A%E5%9F%9F%E7%AE%97%E6%B3%95/

def get_4_neb(img,stack,i,j):
    """
        遍历4邻域,注意边界条件
    """

    if i-1>=0 and img[i-1,j]>0:
        img[i-1][j]=0
        stack.append([i-1,j])

    if i+1<img.shape[0] and img[i+1,j]>0:
        img[i+1][j]=0
        stack.append([i+1,j])

    if j-1>=0 and img[i,j-1]>0:
        img[i,j-1]=0
        stack.append([i,j-1])
    
    if j+1<img.shape[1] and img[i,j+1]>0:
        img[i,j+1]=0
        stack.append([i,j+1])

    return stack


def connected_area(ori_img):
    """[summary]
        img : numpy array 
    Args:
        img ([type]): [description]
    """
    img = ori_img.copy()
    rows,cols = img.shape

    con_areas=[]
    for i in range(rows):
        for j in range(cols):
            if img[i][j]>0:
                area = []
                img[i][j]=0
                stack = [[i,j]]
                while len(stack)!=0:
                    s_i,s_j = stack.pop()
                    area.append([s_i,s_j])
                    stack = get_4_neb(img,stack,s_i,s_j)
                    
                print(area)
                if len(area)>0:
                    con_areas.append(area)
    print(len(con_areas))
    return con_areas



if __name__ == "__main__":
    binary_img = np.zeros((4, 7), dtype=np.int16)
    index = [[0, 2], [0, 5],
            [1, 0], [1, 1], [1, 2], [1, 4], [1, 5], [1, 6],
            [2, 2], [2, 5],
            [3, 1], [3, 2], [3, 4], [3, 6]]
    for i in index:
        binary_img[i[0], i[1]] = np.int16(255)

    print("原始二值图像")
    print(binary_img)

    print(connected_area(binary_img))