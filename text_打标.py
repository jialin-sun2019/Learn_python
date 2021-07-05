from tkinter import *
import pandas as pd
from tkinter import messagebox
import os

class LabelSelect:
    def __init__(self, master):
        self.master = master
        self.master.title("LabelSelect")
        self.w, self.h = self.master.maxsize()#设置大小

        self.master.state('zoomed')          #直接全屏显示
        self.frame = Frame(self.master)
        self.frame.pack(fill=BOTH, expand=1)

        self.label0 = Label(self.master, text='文本内容', bg='Pink')
        self.label0.place(x=700, y=0, width=200, height=60)
        self.button0 = Button(self.master, text='确定', command=self.yes_ture)
        self.button0.place(x=600, y=600, width=200, height=120)

        self.button1 = Button(self.master, text='取消', command=self.no_false)
        self.button1.place(x=800, y=600, width=200, height=120)

        self.button2 = Button(self.master, text='反转', command=self.other_reversa)
        self.button2.place(x=700, y=720, width=200, height=120)

        self.button3 = Button(self.master, text='保存', command=self.save_csv)
        self.button3.place(x=1200, y=600, width=50, height=60)

        self.canvas_w = self.w-50
        self.canvas_h = self.h-360
        self.mainPanel = Canvas(self.master, bg='LightBlue')
        self.mainPanel.place(x=25, y=60, width=self.canvas_w, height=self.canvas_h)
        self.textpanel = self.mainPanel.create_text(800, 330, text='', font=('宋体', 14, 'bold'))

        self.mainPane2 = Canvas(self.master, bg='Wheat')
        self.mainPane2.place(x=400, y=0, width=200, height=60)
        self.textpane2 = self.mainPane2.create_text(100, 30, text='', font=('宋体', 20, 'bold'))

        self.text_list,self.label_list = self.read_data()
        self.text_OK = list()
        self.label_OK = list()
        self.now_text = ''
        self.now_label = 0
        self.show_text()
    def read_data(self):
        df = pd.read_csv('舆情情感文本.csv', encoding='gb18030')
        text_list = list(df['text'])
        label_list = list(df['label'])
        print("->->->->->->->->->->->->数据读取完成->->->->->->->->->")
        return text_list,label_list
    def compute_len(self,text):
        text = re.sub("[a-zA-Z0-9\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", str(text))
        text = list(text)
        for i in range(int(len(text) / 70) + 1):
            text.insert((i + 1) * 70+i, '\n')
        return ''.join(text)
    def yes_ture(self):
        self.text_OK.append(self.now_text)
        self.label_OK.append(self.now_label)
        del self.text_list[0]
        del self.label_list[0]
        self.show_text()
    def no_false(self):
        del self.text_list[0]
        del self.label_list[0]
        self.show_text()
    def other_reversa(self):
        self.text_OK.append(self.now_text)
        if self.now_label==1:
            self.label_OK.append(int(0))
        if self.now_label==0:
            self.label_OK.append(int(1))
        del self.text_list[0]
        del self.label_list[0]
        self.show_text()
    def show_text(self):
        try:
            self.now_text = self.text_list[0]
            self.now_label = self.label_list[0]
        except:
            messagebox.showinfo('您的表格为空，将无法为您显示，程序即将保存之后结束')
            self.save_csv()
        self.mainPane2.itemconfig(self.textpane2, text=str(self.now_label))
        self.mainPanel.itemconfig(self.textpanel, text=self.compute_len(self.now_text))
    def save_csv(self):
        if os.path.exists('情感文本OK.csv'):
            enen_df = pd.read_csv('舆情情感文本.csv', encoding='gb18030')
            ok_data = pd.DataFrame({'text': self.text_OK, 'label': self.label_OK})
            enen_df.append(ok_data)
            enen_df.to_csv('情感文本OK.csv', encoding='gb18030', index=False)
        else:
            ok_data = pd.DataFrame({'text': self.text_OK, 'label': self.label_OK})
            ok_data.to_csv('情感文本OK.csv', encoding='gb18030', index=False)
        origi_data = pd.DataFrame({'text': self.text_list, 'label': self.label_list})
        origi_data.to_csv('舆情情感文本.csv', encoding='gb18030', index=False)
        exit()

if __name__ == '__main__':
    root = Tk()
    select = LabelSelect(root)
    root.mainloop()
