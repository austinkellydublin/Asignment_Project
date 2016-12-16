#bestrouteapp.py
#version 1.0
###Author Austin Kelly
'''this module provides a GUI interface for the bestroute application and leverages  tkinter which is a wrapper around tlc'''



from tkinter import *
from logerrors import *
from cheapest2 import *

def runapp():##this is the main function that calls the route module to calculate the best route
    try:
        port1 = str(portvar1.get())
        port2 = str(portvar2.get())
        port3 = str(portvar3.get())
        port4 = str(portvar4.get())
        port5 = str(portvar5.get())
        aircraft = str(craftvar6.get())
        try:
            candidates = Permroutes(port1, port2, port3, port4, port5).candidates
            craft_range = Aircraft(aircraft).range
            bestroute= Cheapest(candidates, craft_range).cheapest_route
        except:
            Logerrors('An error occured in GUIapp whilst calling Route constructor with parameters supplied ')
        texta=''
        for x in bestroute:
            texta= str(x) + ' , '
        textb= texta

        label7.configure(text=  textb)
    except:
        label7.configure(fg='red')
        label7.configure(text='check your input and clear the fields and try again')


def clearfields():#this function will clear the fields
    label7.configure(fg='blue')
    portvar1.set('')
    portvar2.set('')
    portvar3.set('')
    portvar4.set('')
    portvar5.set('')
    craftvar6.set('')
    label7.configure(text='              THE RESULTS WILL APPEAR HERE             ')





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




portvar1=StringVar()#create the data objects
portvar2=StringVar()
portvar3=StringVar()
portvar4=StringVar()
portvar5=StringVar()
craftvar6=StringVar()


portentry1=Entry(frame1,textvariable=portvar1)#create the entry/input boxes todo use portentry1.get() to retrieve value in function and v.set to reset it to clear''
portentry2=Entry(frame2,textvariable=portvar2)
portentry3=Entry(frame3,textvariable=portvar3)
portentry4=Entry(frame4,textvariable=portvar4)###
portentry5=Entry(frame5,textvariable=portvar5)
craftentry6=Entry(frame6,textvariable=craftvar6)
portentry1.pack(side=RIGHT)
portentry2.pack(side=RIGHT)
portentry3.pack(side=RIGHT)
portentry4.pack(side=RIGHT)
portentry5.pack(side=RIGHT)
craftentry6.pack(side=RIGHT)

imgplane_label=Label(window,image=imgplane)

label0=Label(framea,relief='groove',text='ENTER THE AIRPORTS AND AIRCRAFT BELOW')
label1=Label(frame1,relief='groove',text='                         Airport1')
label2=Label(frame2,relief='groove',text='                         Airport2')
label3=Label(frame3,relief='groove',text='                         Ariport3')
label4=Label(frame4,relief='groove',text='                         Airport4')
label5=Label(frame5,relief='groove',text='                         Airport5')
label6=Label(frame6,relief='groove',text='                        Aircraft')
label7=Label(frame7,relief='groove',text='                       THE RESULTS WILL APPEAR HERE                        ')
label0.pack(side=TOP)
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)
label5.pack(side=LEFT)
label6.pack(side=LEFT)
label7.pack()
label7.configure(fg='blue')



button_run=Button(frame8,text='       RUN       ')
button_clear=Button(frame8,text='       CLEAR       ')
button_run.pack(side=LEFT,padx=20,pady=5)
button_clear.pack(side=RIGHT,padx=20,pady=5)
button_run.configure(command=runapp)
button_clear.configure(command=clearfields)

window.resizable()##
window.mainloop()










