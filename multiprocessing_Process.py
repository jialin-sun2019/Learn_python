from tqdm import tqdm
import pandas as pd
import re
import jieba
import time
from multiprocessing import Process

names = locals()
data_list_1 = list()
data_list_2 = list()
data_list_3 = list()
data_list_4 = list()
data_list_5 = list()
data_list_6 = list()
data_list_7 = list()
data_list_8 = list()
df = pd.read_csv('随机80万数据.csv', encoding='gb18030')
def My_jieba(num):
    global data_list_1, data_list_2, data_list_3, data_list_4
    global data_list_5, data_list_6, data_list_7, data_list_8
    for text in tqdm(df['博文内容'][(num - 1) * 10 * 10000:num * 10 * 10000 - 1]):
        try:
            text1 = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", str(text))
            cut_list = list(jieba.cut(text1))
            names['data_list_' + str(num)].append(cut_list)
        except KeyError:
            pass
    print(len(names['data_list_' + str(num)]))

def return_list():
    data_list = list()
    p1 = Process(target=My_jieba, args=(1,))
    p2 = Process(target=My_jieba, args=(2,))
    p3 = Process(target=My_jieba, args=(3,))
    p4 = Process(target=My_jieba, args=(4,))
    p5 = Process(target=My_jieba, args=(5,))
    p6 = Process(target=My_jieba, args=(6,))
    p7 = Process(target=My_jieba, args=(7,))
    p8 = Process(target=My_jieba, args=(8,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    for i in range(1,9):
        data_list.extend(names['data_list_' + str(i)])
    return data_list
def main():
    print("->->->->->->开始计时->->->->->->")
    start_time = time.time()
    Thousand_data = return_list()
    print("数据的总大小是{0}".format(len(Thousand_data)))
    end_time = time.time()
    print("->->->->->->共计使用时间为{0}s->->->->->->".format(end_time - start_time))

if __name__=='__main__':
    main()
