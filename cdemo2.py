import tkinter as tk

class Demo:
    """類別的文件字串"""

    #類別屬性
    a = "類別屬性a"

    def __init__(self):
        #實體屬性
        self.a = "實體屬性a"

    def __str__(self):
        return "Demo物件的字串"

    @classmethod
    def getA(cls):
        return cls.a

class CDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.demo = Demo()

        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("顯示類別的各種資訊")

        self.button1 = tk.Button(self)
        self.button1["text"] = "文件字串"
        self.button1["command"] = self.show1
        self.button1.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.button2 = tk.Button(self)
        self.button2["text"] = "物件字串"
        self.button2["command"] = self.show2
        self.button2.grid(row=0, column=1, sticky=tk.N+tk.W)

        self.button3 = tk.Button(self)
        self.button3["text"] = "類別屬性"
        self.button3["command"] = self.show3
        self.button3.grid(row=0, column=2, sticky=tk.N+tk.W)

        self.button4 = tk.Button(self)
        self.button4["text"] = "實體屬性"
        self.button4["command"] = self.show4
        self.button4.grid(row=0, column=3, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "..."
        self.result.grid(row=1, column=0, columnspan=4, sticky=tk.N+tk.W)

    def show1(self):
        self.result["text"] = self.demo.__doc__

    def show2(self):
        self.result["text"] = str(self.demo)

    def show3(self):
        self.result["text"] = Demo.getA()

    def show4(self):
        self.result["text"] = self.demo.a

if __name__ == '__main__':
   root = tk.Tk()
   app = CDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：cdemo2.py
# 功能：示範類別定義
# 作者：張凱慶
