from tkinter import *
from login import *

def main():
    root = Tk()
    root.title("学生成绩管理系统")
    LoginPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()