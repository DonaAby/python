# from time import sleep
# def task():
#     #block for a moment
#     sleep(2)
#     #display a message
#     print("this is from another thread")
# # task()
#
# from threading import Thread
# #create a thread
# thread=Thread(target=task)
# #Next,we can create an instance of the threading.Thread class and specify
# #our function name as the "target" arguement in the constructor.
# #run the thread
# # thread.start()
#
# """passing arguements"""
# def task(sleep_time,message):
#     #block for a moment
#     sleep(sleep_time)
#     #display a message
#     print(message)
#
# #create a thread
# thread=Thread(target=task,args=(1.5,"New message from another thread"))
# #run the thread
# thread.start()
## wait for the thread to finish
# print("waiting for the thread...")
# thread.join()

"""MULTITHREADING without threads"""
# import time#import time module
# import threading
# def cal_square(num):
#     print("calculate the square of the no")
#     for n in num:
#         time.sleep(0.3)  #at each iteration it waits for 0.3 sec
#         print("square is ",n*n)
# def cal_cube(num):
#     print("calculate the cube of the no ")
#     for n in num:
#         time.sleep(0.3)
#         print("cube is ",n*n*n)
# arr=[4,5,6,7,2]
# t1=time.time() # to get total time to execute the functions
# cal_square(arr)
# cal_cube(arr)
# print("total time taken by threads is ",time.time()-t1)

"""MULTITHREADING USING THREADS"""

import time#import time module
import threading
def cal_square(num):
    print("calculate the square of the no")
    for n in num:
        time.sleep(0.3)  #at each iteration it waits for 0.3 sec
        print("square is ",n*n)
def cal_cube(num):
    print("calculate the cube of the no ")
    for n in num:
        time.sleep(0.3)
        print("cube is ",n*n*n)
arr=[4,5,6,7,2]
t1=time.time() # to get total time to execute the functions
th1=threading.Thread(target=cal_square,args=(arr,))
th2=threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by threads is ",time.time()-t1)