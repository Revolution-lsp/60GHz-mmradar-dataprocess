import serial
import struct

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parse_data(x,y):
    # 解析數據
##    distance = struct.unpack('>H', bytes(data[0:2]))[0]
##    if distance > 32767: # 將大於32767的數據轉換為負數
##        distance -= 65536
##    x = struct.unpack('>H', bytes(data[2:4]))[0]
##    if x > 32767: # 將大於32767的數據轉換為負數
##        x -= 65536
##    y = struct.unpack('>H', bytes(data[4:6]))[0]
##    if y > 32767: # 將大於32767的數據轉換為負數
##        y -= 65536
##    return distance, x, y
    z=float(((x<<8|y)&0x7FFF)/100.00000)
    if (((x << 8 | y) & 0x8000) == 0x8000):
        z=-z
    return z

##xpoint=[]
##ypoint=[]
##zpoint=[]

##fig = plt.figure(figsize=(10, 7))
##ax = plt.axes(projection="3d")

def check_sum(data):
    # 计算并检查校验和
    #print("check_sum",data[:-1])
    checksum = sum(data[:-1]) % 256
    #print("Ans",checksum)

    return checksum 

##def plot_point3D(x,y,z):
##    # Creating figure
## 
##    # Creating plot
##    ax.scatter3D(xpoint, ypoint, zpoint, color="green")
##    plt.title("3D point clouds")
##    ax.set_xlabel('x')
##    ax.set_ylabel('y')
##    ax.set_zlabel('z')
##    # show plot
##    #plt.show()

##def update(frame):
##    read_from_port('COM9')
##    ax.clear()
##    fig.canvas.draw()
    

def read_from_port(port):
    with serial.Serial(port, baudrate=115200, timeout=1) as ser:
        data = []
        while True:
            byte = ser.read(1)
            if byte == b'\x53':
                next_byte = ser.read(1)
                if next_byte == b'\x59':
                    print("Start frame detected")
                    data = [0x53, 0x63]
                    continue
                    
            data.append(ord(byte))
            #print(f"Received byte: {ord(byte):02x}")
            #print("data",data)
            #print("data:", [hex(d) for d in data])
            if len(data) == 15:
                #if data[-2:] == [0x53, 0x43] and check_sum(data[:-2]):
                if data[-2:] == [84,67] and data[3]==5 and check_sum(data[:-2])==data[-3]:
                    print("End frame detected, checksum passed")
                    #print(data[5:11])
                    print("data:", [hex(d) for d in data])
                    x = parse_data(data[6],data[7])
                    y = parse_data(data[8],data[9])
                    z = parse_data(data[10],data[11])
                    xpoint.append(x)
                    ypoint.append(y)
                    zpoint.append(z)
                    print(f' X: {x} cm, Y: {y} cm, Z: {z} cm')
                    #plot_point3D(x,y,z)
                    return x,y,z
                else:
                    #print(data[-2:])
                    print("End frame detected, checksum failed")
                data = []

if __name__ == "__main__":
    # 用您的串口替換'/dev/cu.usbserial-1442210'
##    anim=FuncAnimation(fig,update)
##    plt.show()
    read_from_port('COM9')
