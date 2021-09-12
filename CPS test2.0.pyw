import tkinter as tk
import time as t
from typing import Counter
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setup()
        

    def setup(self):
        self.i = 0
        self.inp = tk.Entry(self)
        self.inp.pack()
        self.inp.insert(0,"请输入秒数,默认为10")
        self.show = tk.Label(self,font=("宋体",20),text="测手速神器\n")
        self.show.pack()
        self.counts = tk.Button(self, text="点按第一下以开始", 
                    width=50,height=7,command=self.start)
        self.counts.pack()

        self.resets = tk.Button(self, text="重新设置时间",
                    command=self.reset)
        self.resets.pack()

        self.quit = tk.Button(self, text="退出程序", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def start(self):
        self.counts["command"] = self.count
        self.counts["text"] = "计数中"
        try:
            self.settime = float(self.inp.get())
            if self.settime < 0:
                self.inp.delete(0,"end")
                self.inp.insert(0,"默认10-只能输入数字")
                self.settime = 10
        except ValueError:
            self.inp.delete(0,"end")
            self.inp.insert(0,"默认10-只能输入数字")
            self.settime = 10
        self._timer = Timer(self.settime)
        self.count()

    def count(self):
        self._timer.start()
        if not self._timer.gettime():
            self.cps()
            if self.rest<=3:
                self.show["fg"]="red"
            self.i += 1
            self.show["text"] = f"累计: {self.i},平均速率:{self.cpss}\n\
剩余时间:{self.rest}"
        else:
            self.show["fg"]="black"
            self.show["text"] = f"时间到了!\n\
最终成绩:{self.i}\n平均速率:{self.cpss}"
            self.counts["text"] = "时间到了!"

        

    def reset(self):
        self._timer.stop()
        self.i = 0
        self.show["text"] = "测手速神器\n"
        self.show["fg"]="black"
        self.counts["command"] = self.start
        self.counts["text"] = "点按第一下以开始"

    def cps(self):
        self.cpss=round(self.i/(t.time()+0.00001-self._timer._timenow),3)
        self.rest=round(self.settime-(t.time()+0.00001-self._timer._timenow),3)
        
    

class Timer():
    def __init__(self, time):
        self._time = time
        self._timenow = 0
        self._startflag = False

    def start(self):
        
        if not self._startflag:
            self._startflag = True
            self._timenow = t.time()
           

    def gettime(self):
        return (t.time() - self._timenow) >= self._time

    def stop(self):
        self._startflag = False


root = tk.Tk()
app = Application(master=root)
root.title("测手速神器v2.0-汉化")
app.mainloop()