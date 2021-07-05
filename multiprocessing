from tqdm import tqdm
import pandas as pd
import re
import jieba
import time
import multiprocessing
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
    data_list = data_list_1
    pool = multiprocessing.Pool(processes=8)
    for i in range(1,9):
        pool.apply_async(My_jieba,(i,))
    pool.close()
    pool.join()
    for i in range(2,9):
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
