from tkinter import *
from tkinter import messagebox
import serial.tools.list_ports
import io
import time
from datetime import datetime
import threading
now = datetime.now()


available_ports =[
" "
]
running = 0
is_alive = 0
is_reading_serial = False
status = 0
l = 0
port_sel = ""
ser = "null"
m=0

root = Tk()
root.geometry("710x550")
root.resizable(width=False, height=False)
root.title("Pyro Manager_v4")
defaultbg = root.cget('bg')

def on_close():
    global status
    global is_alive
    is_alive = 0
    status = 0
    # threading.Thread(target=con).kill()
    root.destroy()

def S_B_Blink():
    for _ in range(3):
        Button_Search.config(bg='#FF0000')
        time.sleep(0.3)
        Button_Search.config(bg=defaultbg)
        time.sleep(0.3)
def FL_ARMED_B_Blink():
    for _ in range(3):
        Button_FL_ARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_FL_ARMED.config(bg=defaultbg)
        time.sleep(0.3)
def FL_DISARMED_B_Blink():
    for _ in range(3):
        Button_FL_DISARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_FL_DISARMED.config(bg=defaultbg)
        time.sleep(0.3)
def FR_ARMED_B_Blink():
    for _ in range(3):
        Button_FR_ARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_FR_ARMED.config(bg=defaultbg)
        time.sleep(0.3)
def FR_DISARMED_B_Blink():
    for _ in range(3):
        Button_FR_DISARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_FR_DISARMED.config(bg=defaultbg)
        time.sleep(0.3)
def RL_ARMED_B_Blink():
    for _ in range(3):
        Button_RL_ARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_RL_ARMED.config(bg=defaultbg)
        time.sleep(0.3)
def RL_DISARMED_B_Blink():
    for _ in range(3):
        Button_RL_DISARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_RL_DISARMED.config(bg=defaultbg)
        time.sleep(0.3)
def RR_ARMED_B_Blink():
    for _ in range(3):
        Button_RR_ARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_RR_ARMED.config(bg=defaultbg)
        time.sleep(0.3)
def RR_DISARMED_B_Blink():
    for _ in range(3):
        Button_RR_DISARMED.config(bg='#FF0000')
        time.sleep(0.3)
        Button_RR_DISARMED.config(bg=defaultbg)
        time.sleep(0.3)

def Test_B_Blink(result):
    if(result==1):
        for _ in range(3):
            Button_test.config(bg='#00FF00')
            time.sleep(0.3)
            Button_test.config(bg=defaultbg)
            time.sleep(0.3)
    elif(result==0):
        for _ in range(3):
            Button_test.config(bg='#FF0000')
            time.sleep(0.3)
            Button_test.config(bg=defaultbg)
            time.sleep(0.3)

def Open_B_Blink():
    for _ in range(3):
        Button_Open.config(bg='#FF0000')
        time.sleep(0.3)
        Button_Open.config(bg=defaultbg)
        time.sleep(0.3)

def con(m = 0):
    global is_reading_serial
    while(is_alive == 1):
        if (status == 1):
            try:
                is_reading_serial = True
                # time.sleep(2)
                # m = m+1
                # print_term(str(m))
                # print(m)
                line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
                # print("Recieved: " + line)
                if (line == '' ):
                    time.sleep(0.1)
                    line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
                if (line != ''):
                    pr = "Alert: " + line
                    print_term(str(pr))
                    if(line == '60'):
                        messagebox.showwarning('Warning', 'Malfunction Warning!!!!')
                term="READ <-" + line
                print(term)
            except:
                print("Port Closed")
        else:
            time.sleep(0.2)
        is_reading_serial = False
        time.sleep(0.1)

def COM_init():
    try:
        ports = serial.tools.list_ports.comports()
        global available_ports
        available_ports =[
        ""
        ]
        for p in ports:
            if p.device in available_ports:
                pass
            else:
                available_ports.append(p.device)
    except:
        print('Exception occured')
    if(len(available_ports)<=1):
        threading.Thread(target=S_B_Blink).start()
def print_term(msg):
    global l
    l = l+1
    now = datetime.now()
    date_time = now.strftime("%H.%M.%S ")
    msg = date_time + ":- " + msg
    if (l>31):
        term_listbox.delete(0)
    term_listbox.insert(l, msg)


def send_data(ff):
    global l
    global status
    global is_reading_serial
    status = 0
    # time.sleep(1)
    f = str(ff)
    term="WRITE ->" + f
    while(is_reading_serial):
        time.sleep(0.1)
        print("Waiting for Thread to finish>>>")
    ser.write(bytes(f, 'utf-8'))
    print_term(term)
    # time.sleep(2)
    line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
    if (line == '' ):
        time.sleep(0.1)
        line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
    term="READ <-" + line
    print("Recieved: " + line)
    print_term(term)
    status = 1
    # print(line)
    return line

def Search_ports():
    COM_init()
    variable = StringVar(root)
    variable.set(available_ports[0])
    COM_options = OptionMenu(root, variable, *available_ports, command=portss)
    COM_options.place(x=90, y=23)
    print(available_ports)


def portss(port_selected):
    global port_sel
    port_sel = port_selected
    print("Port Selected: " + port_sel)


def Connect():
    global l
    global ser
    global status
    global running
    try:
        if (running == 0):
            running = 1
        print("Connecting")
        ser = serial.Serial(port = port_sel, baudrate =  9600, timeout=1)
        l = l+1
        term = "Connected to: " + str(port_sel)
        print_term(term)
        time.sleep(2)
        Connect_result = send_data(3)
        status = 1
        if Connect_result == "3":
            print("Connected Successfully")
            Button_Open.config(text ='Connected', bg='#00FF00')
        else:
            print("Connection Failed")
            threading.Thread(target=Open_B_Blink).start()
            # Button_Open.confi(bg='#FF0000')
    except:
        threading.Thread(target=Open_B_Blink).start()
        print_term("Failed to open port")


def Test_Coms():
    Test_res = send_data(4)
    if Test_res == "4":
        print("Test Successfully")
        print_term("Test Successfully")
        threading.Thread(target=Test_B_Blink, args=(1,)).start()
    else:
        print("Test Failed!!!")
        print_term("Test Failed!!!")
        messagebox.showwarning("FAILED","CONNECTION FAILED!!!")
        threading.Thread(target=Test_B_Blink, args=(0,)).start()

def Coms_end():
    global status
    status = 0
    ser.close()
    Button_Open.config(text='open Port', bg=defaultbg)
    Button_FL_ARMED.config(bg=defaultbg)
    Button_FL_DISARMED.config(bg=defaultbg)

def FL_ARMED():
    FL_ARMED_Test = send_data("a")
    if (FL_ARMED_Test == "49"):
        # messagebox.showinfo("INFO","msg")
        print_term("FL_ARMED")
        Button_FL_ARMED.config(text= 'FL-ARMED', bg='blue', padx=10)
        Button_FL_DISARMED.config(text = 'FL-DISARM', bg=defaultbg, padx= 17)
        print("FL_ARMED")
    else:
        print_term("FL_ARMED_FAILED")
        threading.Thread(target=FL_ARMED_B_Blink).start()
        print("Failed")

def FL_DISARMED():
    FL_DISARMED_Test = send_data("b")
    if (FL_DISARMED_Test == '50'):
        print_term("FL_DISARMED")
        Button_FL_ARMED.config(text= 'FL-ARM', bg=defaultbg, padx=17)
        Button_FL_DISARMED.config(text = 'FL-DISARMED', bg='blue', padx= 10)
        print("FL_DISARMED")
    else:
        print_term("FL_DISARMED_FAILED")
        threading.Thread(target=FL_DISARMED_B_Blink).start()
        print("Failed")

def FL_FIRE():
    FL_FIRE_Test = send_data("c")
    if (FL_FIRE_Test == '51'):
        print_term("FL_FIRE")
        print("FL_FIRE")
    else:
        print_term("FL_FIRE_FAILED")
        print("Failed")

def FR_ARMED():
        FR_ARMED_Test = send_data("d")
        if (FR_ARMED_Test == '52'):
            print_term("FR_ARMED")
            Button_FR_ARMED.config(text= 'FR-ARMED', bg='blue', padx=10)
            Button_FR_DISARMED.config(text = 'FR-DISARM', bg=defaultbg, padx= 17)
            print("FR_ARMED")
        else:
            print_term("FR_ARMED_FAILED")
            threading.Thread(target=FR_ARMED_B_Blink).start()
            print("Failed")

def FR_DISARMED():
    FR_DISARMED_Test = send_data("e")
    if (FR_DISARMED_Test == '53'):
        print_term("FR_DISARMED")
        Button_FR_ARMED.config(text= 'FR-ARM', bg=defaultbg, padx=17)
        Button_FR_DISARMED.config(text = 'FR-DISARMED', bg='blue', padx= 10)
        print("FR_DISARMED")
    else:
        print_term("FR_DISARMED_FAILED")
        threading.Thread(target=FR_DISARMED_B_Blink).start()
        print("Failed")

def FR_FIRE():
    FR_FIRE_Test = send_data("f")
    if (FR_FIRE_Test == '54'):
        print_term("FR_FIRE")
        print("FR_FIRE")
    else:
        print_term("FR_FIRE_FAILED")
        print("Failed")

def RL_ARMED():
    RL_ARMED_Test = send_data("g")
    if (RL_ARMED_Test == '55'):
        Button_RL_ARMED.config(text= 'RL-ARMED', bg='blue', padx=10)
        Button_RL_DISARMED.config(text = 'RL-DISARM', bg=defaultbg, padx= 17)
        print_term("RL_ARMED")
        print("RL_ARMED")
    else:
        print_term("RL_ARMED_FAILED")
        threading.Thread(target=RL_ARMED_B_Blink).start()
        print("Failed")

def RL_DISARMED():
    RL_DISARMED_Test = send_data("h")
    if (RL_DISARMED_Test == '56'):
        print_term("RL_DISARMED")
        Button_RL_ARMED.config(text= 'RL-ARM', bg=defaultbg, padx=17)
        Button_RL_DISARMED.config(text = 'RL-DISARMED', bg='blue', padx= 10)
        print("RL_DISARMED")
    else:
        print_term("RL_DISARMED_FAILED")
        threading.Thread(target=RL_DISARMED_B_Blink).start()
        print("Failed")

def RL_FIRE():
    RL_FIRE_Test = send_data("i")
    if (RL_FIRE_Test == '57'):
        print_term("RL_FIRE")
        print("RL_FIRE")
    else:
        print_term("RL_FIRE_FAILED")
        print("Failed")

def RR_ARMED():
    RR_ARMED_Test = send_data("j")
    if (RR_ARMED_Test == '58'):
        print_term("RR_ARMED")
        Button_RR_ARMED.config(text= 'RR-ARMED', bg='blue', padx=10)
        Button_RR_DISARMED.config(text = 'RR-DISARM', bg=defaultbg, padx= 17)
        print("RR_ARMED")
    else:
        print_term("RR_ARMED_FAILED")
        threading.Thread(target=RR_ARMED_B_Blink).start()
        print("Failed")

def RR_DISARMED():
    RR_DISARMED_Test = send_data("k")
    if (RR_DISARMED_Test == '59'):
        print_term("RR_DISARMED")
        Button_RR_ARMED.config(text= 'RR-ARM', bg=defaultbg, padx=17)
        Button_RR_DISARMED.config(text = 'RR-DISARMED', bg='blue', padx= 10)
        print("RR_DISARMED")
    else:
        print_term("RR_DISARMED_FAILED")
        threading.Thread(target=RR_DISARMED_B_Blink).start()
        print("Failed")

def RR_FIRE():
    RR_FIRE_Test = send_data("l")
    if (RR_FIRE_Test == '60'):
        print_term("RR_FIRE")
        print("RR_FIRE")
    else:
        print_term("RR_FIRE_FAILED")
        print("Failed")



Label_selectport = Label(root, text="Select COM Port")
Label_Pyro_FL= Label(root, text="Pyro Branch FL")
Label_Pyro_RL= Label(root, text="Pyro Branch RL")
Label_Pyro_FR= Label(root, text="Pyro Branch FR")
Label_Pyro_RR= Label(root, text="Pyro Branch RR")
Label_Terminal= Label(root, text="Terminal")

Button_Search = Button(root, text="Search Device", command = Search_ports)
Button_Open = Button(root, text= "Open Port", command = Connect)
Button_test = Button(root, text= "Test", command = Test_Coms, padx = 20)
Button_Close = Button(root, text= "Close Port", command = Coms_end, padx = 20)

Button_FL_ARMED = Button(root, text= "FL-ARM", command = FL_ARMED, padx = 17)
Button_FL_DISARMED = Button(root, text= "FL-DISARM", command = FL_DISARMED, padx = 17)
Button_FL_FIRE = Button(root, text= "FIRE-FL", command = FL_FIRE, padx = 45+30)

Button_RL_ARMED = Button(root, text= "RL-ARM", command = RL_ARMED, padx = 17)
Button_RL_DISARMED = Button(root, text= "RL-DISARM", command = RL_DISARMED, padx = 17)
Button_RL_FIRE = Button(root, text= "FIRE-RL", command = RL_FIRE, padx = 45+30)

Button_FR_ARMED = Button(root, text= "FR-ARM", command = FR_ARMED, padx = 17)
Button_FR_DISARMED = Button(root, text= "FR-DISARM", command = FR_DISARMED, padx = 17)
Button_FR_FIRE = Button(root, text= "FIRE-FR", command = FR_FIRE, padx = 45+30)

Button_RR_ARMED = Button(root, text= "RR-ARM", command = RR_ARMED, padx = 17)
Button_RR_DISARMED = Button(root, text= "RR-DISARM", command = RR_DISARMED, padx = 17)
Button_RR_FIRE = Button(root, text= "FIRE-RR", command = RR_FIRE, padx = 45+30)

term_listbox = Listbox(root, width=40, height=30)






Label_selectport.place(x=5, y=5)
Label_Pyro_FL.place(x=30, y=75+25)
Button_FL_ARMED.place(x = 5, y = 75+50)
Button_FL_DISARMED.place(x = 75+25, y = 75+50)
Button_FL_FIRE.place(x = 5, y = 105+50)

Label_Pyro_RL.place(x=30, y=75+175)
Button_RL_ARMED.place(x = 5, y = 75+200)
Button_RL_DISARMED.place(x = 75+25, y = 75+200)
Button_RL_FIRE.place(x = 5, y = 105+200)

Label_Pyro_FR.place(x=30+250, y=75+25)
Button_FR_ARMED.place(x = 5+250, y = 75+50)
Button_FR_DISARMED.place(x = 75+250+25, y = 75+50)
Button_FR_FIRE.place(x = 5+250, y = 105+50)

Label_Pyro_RR.place(x=30+250, y=75+175)
Button_RR_ARMED.place(x = 5+250, y = 75+200)
Button_RR_DISARMED.place(x = 75+250+25, y = 75+200)
Button_RR_FIRE.place(x = 5+250, y = 105+200)

Label_Terminal.place(x=455, y=30)


Button_Search.place(x=5, y=25)
Button_Open.place(x=180, y =25)
Button_test.place(x = 315-60, y = 25)
Button_Close.place(x = 390-60, y = 25)


term_listbox.place(x= 455, y = 55)

is_alive = 1
threading.Thread(target=con).start()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
