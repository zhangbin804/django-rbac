# from multiprocessing import Process
# import time
# import random
#
# def piao(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randint(1, 3))
#     print('--------',name)
#     time.sleep(random.randint(1, 3))
#
# if __name__ =='__main__':
#     p1 = Process(target=piao,kwargs={'name':'1'})
#     p2 = Process(target=piao,kwargs={'name':'2'})
#     p3 = Process(target=piao,kwargs={'name':'3'})
#     p1.start()
#     p2.start()
#     p3.start()
#     print('主进程')


# from multiprocessing import Process
# import time
# import random
# import os
# class Piao(Process):
#     def __init__(self,name):
#         super().__init__() #必须继承父类的一些属性
#         self.name = name
#     def run(self):  #必须得实现一个run方法
#         print(os.getppid(),os.getpid())
#         print('%s is piaoing'%self.name)
#         time.sleep(random.randint(1,3))
#         print('%s is piao end'%self.name)
# if __name__ =='__main__':
#     p1 = Piao('alex')
#     p2 = Piao('wupeiqi')
#     p3 = Piao('yuanhao')
#     p1.start()
#     p2.start()
#     p3.start()
#     print('主进程',os.getpid())
#

















