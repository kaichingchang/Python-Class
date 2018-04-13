import tkinter as tk

class CDemo(tk.Frame):
    count = 0

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("Welcome")

        self.button = tk.Button(self)
        self.button["text"] = "按我"
        self.button["command"] = self.show
        self.button.grid(row=0, column=0)

        self.result = tk.Label(self)
        self.result["text"] = "歡迎光臨"
        self.result["width"] = 20
        self.result.grid(row=1, column=0)

    def show(self):
        if CDemo.count % 2 == 0:
            self.result["text"] = "謝謝光臨"
            self.button["text"] = "再按我"
        else:
            self.result["text"] = "歡迎光臨"
            self.button["text"] = "按我"
        CDemo.count += 1

if __name__ == '__main__':
   root = tk.Tk()
   app = CDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：cdemo1.py
# 功能：示範類別定義
# 作者：張凱慶
