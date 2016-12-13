#bestrouteapp.py
#version 1.0
###Author Austin Kelly
####this module provides a GUI interface for the bestroute application


from tkinter import *

window=Tk()##create main window object
window.title('Best Route program Augustine Kelly D16124897')##add title to window
window.configure(bg='wheat')
imgplane=PhotoImage(file='imgplane.gif')##GUI will have pic of plane

label0=Label(window,image=imgplane)#to display image of plane
label0.pack(padx=10,pady=5)


frame0=Frame(window)#container for 2 elements below
frame1=Frame()#container elements to assist layout and pack them into frame 4
frame2=Frame()
frame3=Frame()
frame4=Frame()
frame5=Frame()
frame6=Frame()
frame7=Frame()
frame8=Frame()
framea=Frame(pady=5)
frame0.pack()
framea.pack()
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
frame7.pack(pady=3)
frame8.pack()




# portvar1=StringVar()#create the data objects
# portvar2=StringVar()
# portvar3=StringVar()
# portvar4=StringVar()
# portvar5=StringVar()
# craftvar6=StringVar()


portentry1=Entry(frame1)#create the entry/input boxes
portentry2=Entry(frame2)
portentry3=Entry(frame3)
portentry4=Entry(frame4)
portentry5=Entry(frame5)
craftentry6=Entry(frame6)
portentry1.pack(side=RIGHT)
portentry2.pack(side=RIGHT)
portentry3.pack(side=RIGHT)
portentry4.pack(side=RIGHT)
portentry5.pack(side=RIGHT)
craftentry6.pack(side=RIGHT)

imgplane_label=Label(window,image=imgplane)

label0=Label(framea,relief='groove',text='ENTER THE AIRPORTS AND AIRCRAFT BELOW')
label1=Label(frame1,relief='groove',text='                         Aiport1')
label2=Label(frame2,relief='groove',text='                         Aiport2')
label3=Label(frame3,relief='groove',text='                         Aiport3')
label4=Label(frame4,relief='groove',text='                         Aiport4')
label5=Label(frame5,relief='groove',text='                         Aiport5')
label6=Label(frame6,relief='groove',text='                        Aircraft')
label7=Label(frame7,relief='groove',text='          THE RESULTS WILL APPEAR HERE          ')
label0.pack(side=TOP)
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)
label5.pack(side=LEFT)
label6.pack(side=LEFT)
label7.pack()

# label11=Label(frame1,relief='groove',text='results will appear here')
# label21=Label(frame2,relief='groove',text='results will appear here')
# label31=Label(frame3,relief='groove',text='results will appear here')
# label41=Label(frame4,relief='groove',text='results will appear here')
# label51=Label(frame5,relief='groove',text='results will appear here')
# label61=Label(frame6,relief='groove',text='results will appear here')
# label11.pack(pady=10)
# label21.pack(pady=10)
# label31.pack(pady=10)
# label41.pack(pady=10)
# label51.pack(pady=10)
# label61.pack(pady=10)



button_run=Button(frame8,text='       RUN       ')
button_exit=Button(frame8,text='       CLEAR       ')
button_run.pack(side=LEFT,padx=20,pady=5)
button_exit.pack(side=RIGHT,padx=20,pady=5)



window.mainloop()










