# -*- coding=utf-8 -*-
import numpy as np
from math import ceil
import tensorflow as tf 




def conv2d(feature_map, weights, strides=(1,1), pading='same'):
    """[summary]

    Arguments:
        feature_map {[type]} -- [description]
        weights {[type]} -- [description]

    Keyword Arguments:
        stride {int} -- [description] (default: {1})
        pading {str} -- [description] (default: {'same'})
    """

    height, width, channel = feature_map.shape
    k_h, k_w,k_c= weights.shape

    # output
    if pading == 'same':
        output_shape = ceil(height/strides[0]),ceil(width/strides[1])
    elif pading=='valid':
        output_shape = ceil((height-k_h+1)/strides[0]), ceil((height-k_w+1)/strides[1])
    else:
        print('padding params is invalid')

    # padding
    if pading == 'same':
        if (height % strides[0] == 0):
            pad_along_height = max(k_h - strides[0], 0)
        else:
            pad_along_height = max(k_h - (height % strides[0]), 0)
        if (width % strides[1] == 0):
            pad_along_width = max(k_w - strides[1], 0)
        else:
            pad_along_width = max(k_w - (height % strides[1]), 0)

        # 因为pad是在上下、左右四侧pad。所以当pi不为偶数时要分配下
        # 这里是当pi为奇数时，下侧比上侧多一，右侧比左侧多一。
        pad_top = pad_along_height // 2
        pad_bottom = pad_along_height - pad_top
        pad_left = pad_along_width // 2
        pad_right = pad_along_width - pad_left
    elif pading=='valid':
        pad_top = pad_bottom = pad_left = pad_right = 0
    else:
        print('padding params is invalid')
    
    out_res = np.zeros(output_shape,dtype=np.float32)

    for i in range(channel):

        fm = feature_map[:,:,i]
        wei = weights[:,:,i]
        pad_fm = np.pad(fm,((pad_top,pad_bottom),(pad_left,pad_right)),'constant', constant_values=(0,0))
        
        tmp_res = np.zeros(output_shape,dtype=np.float32)
        for i in range(output_shape[0]):
            for j in range(output_shape[1]):
                kk =  pad_fm[i*strides[0]:i*strides[0]+k_h,j*strides[1]:j*strides[1]+k_w]
                tmp_res[i][j]= np.sum(kk*wei)

        out_res = out_res+tmp_res

    return out_res
    
def tensorflow_test(img,weights):

    img = np.expand_dims(img,0)
    weights = np.expand_dims(weights,-1)
    input = tf.placeholder(tf.float32,[1,5,5,3])
    filter = tf.placeholder(tf.float32,[3,3,3,1])
    op1 = tf.nn.conv2d(input, filter, strides=[1,2,2,1], padding='SAME')

    init = tf.initialize_all_variables() 
    with tf.Session() as sess:
        sess.run(init)
        res = sess.run(op1,feed_dict={input:img,filter:weights})
        # print(res)

        return res


if __name__ == "__main__":
    # 5*5*3
    img_data = [[[1, 1, 1],
                 [1, 5, 1],
                 [1, 6, 1],
                 [4, 1, 1],
                 [1, 3, 1]],

                [[1, 1, 1],
                 [1, 100, 1],
                 [1, 1, 1],
                 [20, 1, 1],
                 [20, 20, 1]],

                [[1, 1, 1],
                 [1, 1, 1],
                 [1, 17, 1],
                 [1, 1, 1],
                 [1, 1, 20]],

                [[1, 1, 178],
                 [1, 15, 1],
                 [1, 1, 1],
                 [1, 121, 1],
                 [1, 1, 1]],

                [[1, 1, 21],
                 [1, 53, 1],
                 [87, 41, 1],
                 [1, 1, 1],
                 [1, 1, 71]]]

    weights_data = [
        [[1, 0, 1],
         [-1, 1, 0],
         [0, -1, 0]],
        [[-1, 0, 1],
         [0, 0, 1],
         [1, 1, 1]],
        [[-1, 0, 1],
         [0, 0, 1],
         [1, 1, 1]]

    ]
    img_data=np.array(img_data,dtype=np.float32)
    weights_data=np.array(weights_data)
    print(img_data.shape,weights_data.shape)

    np_res = conv2d(img_data,weights_data,strides=(2,2),pading='same')
    print(np_res)

    tf_res=tensorflow_test(img_data,weights_data)
    print(tf_res[0,:,:,0])