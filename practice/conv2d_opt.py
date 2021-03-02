# -*- coding=utf-8 -*-
import numpy as np
from math import ceil
import tensorflow as tf 


# 参考https://blog.csdn.net/Daycym/article/details/83826222?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control
# https://zhuanlan.zhihu.com/p/63974249
def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    """
    Parameters
    ----------
    input_data : 由(数据量, 通道, 高, 长)的4维数组构成的输入数据
    filter_h : 卷积核的高
    filter_w : 卷积核的长
    stride : 步幅
    pad : 填充

    Returns
    -------
    col : 2维数组
    """
    # 输入数据的形状
    # N：批数目，C：通道数，H：输入数据高，W：输入数据长
    N, C, H, W = input_data.shape  
    out_h = (H + 2*pad - filter_h)//stride + 1  # 输出数据的高
    out_w = (W + 2*pad - filter_w)//stride + 1  # 输出数据的长
    # 填充 H,W
    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    # (N, C, filter_h, filter_w, out_h, out_w)的0矩阵
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
    
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            #y:y_max:stride 从小到大间隔stride
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]
    # 按(0, 4, 5, 1, 2, 3)顺序，交换col的列，然后改变形状
    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col

#反向传播的时候需要
def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
    N, C, H, W = input_shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]

class Convolution:
	# 初始化权重（卷积核4维）、偏置、步幅、填充
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
        
        # 中间数据（backward时使用）
        self.x = None   
        self.col = None
        self.col_W = None
        
        # 权重和偏置参数的梯度
        self.dW = None
        self.db = None

    def forward(self, x):
        # 卷积核大小，FN就是实际就是输出的Channel，C是输入的channel
        FN, C, FH, FW = self.W.shape
        # 数据数据大小
        N, C, H, W = x.shape
        # 计算输出数据大小
        out_h = 1 + int((H + 2*self.pad - FH) / self.stride)
        out_w = 1 + int((W + 2*self.pad - FW) / self.stride)
        # 利用im2col转换为行
        col = im2col(x, FH, FW, self.stride, self.pad)
        # 卷积核转换为列，展开为2维数组 
        col_W = self.W.reshape(FN, -1).T
        # 计算正向传播，矩阵相乘(N*out_h*out_w,C*filter_h*filter_w) * (C*filter_h*filter_w,FN) = N*out_h*out_w*FN
        out = np.dot(col, col_W) + self.b
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        self.x = x
        self.col = col
        self.col_W = col_W

        return out

    def backward(self, dout):
        # 卷积核大小
        FN, C, FH, FW = self.W.shape
        dout = dout.transpose(0,2,3,1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)
        # 逆转换
        dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

        return dx


# 白板默写版本

def img2col(input,filter_h,filter_w,out_h,out_w,stride=1,pad=0):

	#input 大小
	N, C, H, W = input.shape

	# pad
	img = np.pad(input,[(0,0),(0,0),(pad,pad),(pad,pad)], 'constant')

	# 生成col矩阵 N*C_in*filter_h*filter_w*out_h*out_w的矩阵
	col = np.zeros((N,C,filter_h,filter_w,out_h,out_w))

	#填充col向量
	for y in range(filter_h):
		y_max = y + stride*out_h
		for x  in range(filter_w):
			x_max = x + stride*out_w
			col[:,:,y,x,:,:] = img[:,:,y:y_max:stride,x:x_max:stride]

	#交换col的位置并且reshape到(N*out_h*out_w,C*filter_h*filter_w)
	col = col.transpose(0,4,5,1,2,3).reshape(N*out_h*out_w,-1)
	return col


# caffe 的卷积实现
def conv2d(input,weight,stride=1,pad=0):

	#卷积核大小,FN就是实际就是输出的Channel，C是输入的channel
	FN, C, FH, FW = weight.shape

	#input 大小
	N , C, H , W = input.shape

	#输出大小
	out_h = (H - FH + 2 * pad) // stride + 1
	out_w = (W - FW + 2 * pad) // stride + 1

	#img2col 图像转向量
	col = img2col(input,FH,FW,out_h,out_w)

	#卷积核转换为列,即变为（FN,C*f_h*f_w）,需要转置
	col_w = weight.reshape(FN,-1).T

	#矩阵相乘(N*out_h*out_w,C*filter_h*filter_w) * (C*filter_h*filter_w,FN) = (N*out_h*out_w)*FN
	out = np.dot(col,col_w)	

	#reshape+transpose
	out = out.reshape(N,out_h,out_w,-1).transpose(0,3,1,2)

	return out