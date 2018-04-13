import tkinter as tk

class A:
    pass

class B:
    pass

class C:
    pass

class Demo(A, B):
    pass

class CDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("繼承")

        self.button1 = tk.Button(self)
        self.button1["text"] = "A的子類別"
        self.button1["command"] = self.show1
        self.button1.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.button2 = tk.Button(self)
        self.button2["text"] = "C的子類別"
        self.button2["command"] = self.show2
        self.button2.grid(row=0, column=1, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "..."
        self.result.grid(row=1, column=0, columnspan=2, sticky=tk.N+tk.W)

    def show1(self):
        self.result["text"] = issubclass(Demo, A)

    def show2(self):
        self.result["text"] = issubclass(Demo, C)

if __name__ == '__main__':
   root = tk.Tk()
   app = CDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：cdemo5.py
# 功能：示範類別定義
# 作者：張凱慶
