from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
import serial.tools.list_ports
import io
import time
from datetime import datetime
import threading
now = datetime.now()

connected = 0

# state_FL =''
# state_FR =''
# state_RL =''
# state_RR =''


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
root.geometry('710x550')
root.resizable(width=False, height=False)
root.title("Pyro Manager v5")
defaultbg = root.cget('bg')

fontStyle_header = tkFont.Font(family="Lucida Grande", size=25)
fontStyle_header_2 = tkFont.Font(family="Lucida Grande", size=22)
fontStyle_normal = tkFont.Font(family="Arial", size=15)
fontStyle_normal_small = tkFont.Font(family="Arial", size=10)
fontStyle_normal_small_button = tkFont.Font(family="TkDefaultFont", size=9)
fontStyle_tab = tkFont.Font(family="Arial", size=10)
fontStyle_tab_search = tkFont.Font(family="Arial", size=14)

my_notebook = ttk.Notebook(root)
my_notebook.place(x = 0, y = 45)

Control_frame= Frame(my_notebook, width = 450, height = 600)
Config_frame= Frame(my_notebook, width = 450, height = 600)



def on_close():
    global status
    global is_alive
    is_alive = 0
    status = 0
    # threading.Thread(target=con).kill()
    root.destroy()


def Trig_Blink():
    print('Triggered')
    for _ in range(20):
        Label_Trigger_in.config(bg = '#FFFF00')
        time.sleep(0.1)
        Label_Trigger_in.config(bg = defaultbg)
        time.sleep(0.1)

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

def Telemetry_sync(state_FL, state_FR, state_RL, state_RR):
    print('reached')
    if(state_FL == 'HIGH'):
        Button_FL_ARMED.config(text= 'FL-ARMED', bg='blue', padx=10)
        Button_FL_DISARMED.config(text = 'FL-DISARM', bg=defaultbg, padx= 17-9)
    if(state_FL == 'LOW'):
        print('enables')
        Button_FL_ARMED.config(text= 'FL-ARM', bg=defaultbg, padx=17)
        Button_FL_DISARMED.config(text = 'FL-DISARMED', bg='blue', padx= 10-9)
    if(state_FR == 'HIGH'):
        Button_FR_ARMED.config(text= 'FR-ARMED', bg='blue', padx=10)
        Button_FR_DISARMED.config(text = 'FR-DISARM', bg=defaultbg, padx= 17-9)
    if(state_FR == 'LOW'):
        Button_FR_ARMED.config(text= 'FR-ARM', bg=defaultbg, padx=17)
        Button_FR_DISARMED.config(text = 'FR-DISARMED', bg='blue', padx= 10-9)
    if(state_RL == 'HIGH'):
        Button_RL_ARMED.config(text= 'RL-ARMED', bg='blue', padx=10)
        Button_RL_DISARMED.config(text = 'RL-DISARM', bg=defaultbg, padx= 17-9)
    if(state_RL == 'LOW'):
        Button_RL_ARMED.config(text= 'RL-ARM', bg=defaultbg, padx=17)
        Button_RL_DISARMED.config(text = 'RL-DISARMED', bg='blue', padx= 10-9)
    if(state_RR == 'HIGH'):
        Button_RR_ARMED.config(text= 'RR-ARMED', bg='blue', padx=10)
        Button_RR_DISARMED.config(text = 'RR-DISARM', bg=defaultbg, padx= 17-9)
    if(state_RR == 'LOW'):
        Button_RR_ARMED.config(text= 'RR-ARM', bg=defaultbg, padx=17)
        Button_RR_DISARMED.config(text = 'RR-DISARMED', bg='blue', padx= 10-9)

def con(m = 0):
    global is_reading_serial
    global connected
    telem_reading = False
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
                if(line == '60'):
                    pr = "Alert: " + line
                    print_term(str(pr))
                    messagebox.showwarning('Warning', 'Malfunction Warning!!!!')
                elif(line == '124'):
                    pr = "Alert: " + line
                    print_term(str(pr))
                    print_term('Detonated!!!')
                    threading.Thread(target = Trig_Blink).start()
                    messagebox.showwarning('Detonation', 'Pyro Triggered')
                while(line != ''):
                    telem_reading = True
                    print(ser.readline())
                    line = str(ser.readline()).replace('r','').replace('\\n','').replace('b','').replace('\'','').replace('\\','')
                    print("Recieved_rd: " + line)
                    identifiers = line.split(':')
                    print(identifiers)
                    if(identifiers[0] == 'T'):
                        Telemetry_data=["FL","FR","RL", "RR"]
                        print('Telemetry Received. ')
                        Telemetry_data[0] = str(identifiers[1]).strip(' ')
                        Telemetry_data[1] = str(identifiers[2]).strip(' ')
                        Telemetry_data[2] = str(identifiers[3]).strip(' ')
                        Telemetry_data[3] = str(identifiers[4]).strip(' ')
                        print("Telemetry_data for temp::")
                        print(Telemetry_data)
                        time.sleep(0.001)
                        threading.Thread(target=Telemetry_sync, args=(Telemetry_data[0], Telemetry_data[1], Telemetry_data[2], Telemetry_data[3],)).start()

                        # print(str(identifiers[1]).split(':'))
                        # state_FL = str(identifiers[1]).strip(' ')
                        # state_FR = str(identifiers[2]).strip(' ')
                        # state_RL = str(identifiers[3]).strip(' ')
                        # state_RR = str(identifiers[4]).strip(' ')
                        # print('FL: ' + state_FL)
                        # print('FR: ' + state_FR)
                        # print('RL: ' + state_RL)
                        # print('RR: ' + state_RR)
                        # Telemetry_data_temp = str(identifiers[1]).split(':')
                        # Telemetry_data[0] = Telemetry_data_temp[0]
                        # Telemetry_data[1] = Telemetry_data_temp[1]
                        # Telemetry_data[2] = Telemetry_data_temp[2]
                        # Telemetry_data[3] = Telemetry_data_temp[3]
                        # Telemetry_data[0] = state_FL
                        # Telemetry_data[1] = state_FR
                        # Telemetry_data[2] = state_RL
                        # Telemetry_data[3] = state_RR
                        # threading.Thread(target=Telemetry_sync, args=(Telemetry_data[0], Telemetry_data[1], Telemetry_data[2], Telemetry_data[2],)).start()
                        # print(state_FL)
                telem_reading = False
                # if (line != ''):
                #     pr = "Alert: " + line
                #     print_term(str(pr))
                #     if(line == '60'):
                #         messagebox.showwarning('Warning', 'Malfunction Warning!!!!')
                #     elif(line == '100'):
                #         messagebox.showwarning('Detonation', 'Pyro Triggered')
                #     elif(line == '6'):
                #         # .messagebox.showinfo(title=None, message=None, **options)
                #         if (connected == 0 ):
                #             connected = 1
                #             is_reading_serial = False
                #             # time.sleep(0.1)
                #             print("GOT IT")
                #             send_data(6)
                #             # time.sleep(0.5)
                #             # messagebox.showinfo('Connection', 'Remonte Connected')
                #             is_reading_serial = True
                term="READ <-" + line
                print(term)
            except:
                print("Port Closed")
        else:
            time.sleep(0.001)
        is_reading_serial = False
        if (telem_reading == False):
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

    try:
        time.sleep(1)
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
        time.sleep(0.1)
        ser.write(bytes(f, 'utf-8'))
        print(bytes(f, 'utf-8'))
        print_term(term)
        # time.sleep(2)
        line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
        if (line == '' ):
            time.sleep(0.1)
            line = str(ser.readline()).replace('r','').replace('n','').replace('\\','').replace('b','').replace('\'','')
        term="READ <-" + line
        print("Recieved_sd: " + line)
        print_term(term)
        status = 1
        # threading.Thread(target=tx_off).start()
        # print(line)
        return line
    except:
        print("Port Closed")


def Search_ports():
    COM_init()
    variable = StringVar(root)
    variable.set(available_ports[0])
    COM_options = OptionMenu(root, variable, *available_ports, command=portss)
    COM_options.place(x=440-84, y=32)
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
        print("Test Successfully----")
        print_term("Test Successfully")
        threading.Thread(target=Test_B_Blink, args=(1,)).start()
        # state_FL = str(Telemetry_data[0])
        # state_FR = str(Telemetry_data[1])
        # state_RL = str(Telemetry_data[2])
        # state_RR = str(Telemetry_data[3])
        # print(state_FL)
        # print(state_FR)
        # print(state_RL)
        # print(state_RR)
        # threading.Thread(target=Telemetry_sync, args=("LOW", "HIGH", "HIGH", "HIGH",)).start()
        # Telemetry_sync(state_FL, state_FR, state_RL, state_RR)
    else:
        print("Test Failed!!!")
        print_term("Test Failed!!!")
        # messagebox.showwarning("FAILED","CONNECTION FAILED!!!")
        threading.Thread(target=Test_B_Blink, args=(0,)).start()

def Coms_end():
    global status
    global connected
    connected = 0
    status = 0
    ser.close()
    Button_Open.config(text='open Port', bg=defaultbg)
    # Button_FL_ARMED.config(bg=defaultbg)
    # Button_FL_DISARMED.config(bg=defaultbg)

def FL_ARMED():
    FL_ARMED_Test = send_data("a")
    if (FL_ARMED_Test == "49"):
        # messagebox.showinfo("INFO","msg")
        print_term("FL_ARMED")
        Button_FL_ARMED.config(text= 'FL-ARMED', bg='blue', padx=10)
        Button_FL_DISARMED.config(text = 'FL-DISARM', bg=defaultbg, padx= 17-9)
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
        Button_FL_DISARMED.config(text = 'FL-DISARMED', bg='blue', padx= 10-9)
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
            Button_FR_DISARMED.config(text = 'FR-DISARM', bg=defaultbg, padx= 17-9)
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
        Button_FR_DISARMED.config(text = 'FR-DISARMED', bg='blue', padx= 10-9)
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
        Button_RL_DISARMED.config(text = 'RL-DISARM', bg=defaultbg, padx= 17-9)
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
        Button_RL_DISARMED.config(text = 'RL-DISARMED', bg='blue', padx= 10-9)
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
        Button_RR_DISARMED.config(text = 'RR-DISARM', bg=defaultbg, padx= 17-9)
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
        Button_RR_DISARMED.config(text = 'RR-DISARMED', bg='blue', padx= 10-9)
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

def RPG7_FIRE():
    # Button_ALL_FIRE_SIM.config(bg='#F5BA11')
    RPG7_FIRE_Test = send_data("m")
    if (RPG7_FIRE_Test == '61'):
        print_term("RPG7_FIRE")
        print("RPG7_FIRE")
        # Button_ALL_FIRE_SIM.config(bg = '#F5F9D2')
    else:
        print_term("RPG7_FIRE_FAILED")
        print("Failed")

def GPMG_FIRE():
    # Button_ALL_FIRE_SEQ.config(bg='#F5BA11')
    GPMG_FIRE_Test = send_data("n")
    if (GPMG_FIRE_Test == '62'):
        print_term("GPMG_FIRE")
        print("GPMG_FIRE")
        # Button_ALL_FIRE_SEQ.config(bg = '#F5F9D2')
    else:
        print_term("GPMG_FIRE_FAILED")
        print("Failed")



Label_Pyro_Header = Label(root, text="The Dirty Solution v5", font =fontStyle_header_2)
# Label_selectport = Label(root, text="Select COM Port")

Button_Search = Button(root, text="Search Device", command = Search_ports, pady = 1)
Button_test = Button(root, text= "Test/Sync", command = Test_Coms, padx = 10, pady =1)
Button_Open = Button(root, text= "Open Port", command = Connect)
Button_Close = Button(root, text= "Close Port", command = Coms_end, padx = 10)

term_listbox = Listbox(root, width=40, height=30)



Button_Search.place(x=350-80, y=35)
Button_Open.place(x=455, y =35)
Button_test.place(x = 525, y = 35)
Button_Close.place(x = 610, y = 35)

Label_Pyro_Header.place(x=0, y=0)

# Label_Pyro_RL.place(x=30, y=75+175)

term_listbox.place(x= 455, y = 66)
# Label_selectport.place(x=350-90, y=15)




Control_frame.pack(fill="both", expand =1)
Config_frame.pack(fill="both", expand =1)

my_notebook.add(Control_frame, text = 'Controls')
my_notebook.add(Config_frame, text = 'Configure')

Canvas = Canvas(Control_frame, width=450, height=150)

Label_object_MainBox = Label(Control_frame, text = "MB", padx= 168, pady=110, relief=RIDGE)

Button_FL_ARMED = Button(Control_frame, text= "FL-ARM", command = FL_ARMED, padx = 17)
Button_FL_DISARMED = Button(Control_frame, text= "FL-DISARM", command = FL_DISARMED, padx = 17-9)
Button_FL_FIRE = Button(Control_frame, text= "FIRE-FL", command = FL_FIRE, padx = 5)


Button_RL_ARMED = Button(Control_frame, text= "RL-ARM", command = RL_ARMED, padx = 17)
Button_RL_DISARMED = Button(Control_frame, text= "RL-DISARM", command = RL_DISARMED, padx = 17-9)
Button_RL_FIRE = Button(Control_frame, text= "FIRE-RL", command = RL_FIRE, padx = 5)

Button_FR_ARMED = Button(Control_frame, text= "FR-ARM", command = FR_ARMED, padx = 17)
Button_FR_DISARMED = Button(Control_frame, text= "FR-DISARM", command = FR_DISARMED, padx = 17-9)
Button_FR_FIRE = Button(Control_frame, text= "FIRE-FR", command = FR_FIRE, padx = 5)

Button_RR_ARMED = Button(Control_frame, text= "RR-ARM", command = RR_ARMED, padx = 17)
Button_RR_DISARMED = Button(Control_frame, text= "RR-DISARM", command = RR_DISARMED, padx = 17-9)
Button_RR_FIRE = Button(Control_frame, text= "FIRE-RR", command = RR_FIRE, padx = 5)

Label_Trigger_in = Label(Control_frame, text= "Trig",relief = RIDGE)

Button_ALL_FIRE_SIM = Button(Control_frame, text= "FIRE RPG7", command = RPG7_FIRE, padx = 5, pady = 5, font = fontStyle_header, bg = '#F5F9D2')
Button_ALL_FIRE_SEQ = Button(Control_frame, text= "FIRE GPMG", command = GPMG_FIRE, padx = 5, pady = 5, font = fontStyle_header, bg = '#F5F9D2')

Label_object_MainBox.place(x=75-25, y=80+25)

Label_Trigger_in.place(x=380, y=350)

Button_FL_ARMED.place(x = 75+2-25, y = 80+2+25)
Button_FL_DISARMED.place(x = 75+2-25, y = 105+4+25)
Button_FL_FIRE.place(x = 25, y = 65)

# Button_FR_ARMED.place(x = 5+250, y = 75+50)
Button_RL_ARMED.place(x = 252+2-25, y = 80+2+25)
Button_RL_DISARMED.place(x = 252+2-25, y = 105+4+25)
Button_RL_FIRE.place(x = 252+2-25+15, y = 10)

# Label_Pyro_FR.place(x=30+250, y=75+25)
# Button_RL_ARMED.place(x = 188+2, y = 80+2)
Button_FR_ARMED.place(x = 163+2-25, y = 80+2+25)
Button_FR_DISARMED.place(x = 163+2-25, y = 105+4+25)
Button_FR_FIRE.place(x = 163+2-15, y = 10)

# Label_Pyro_RR.place(x=30+250, y=75+175)
Button_RR_ARMED.place(x = 340+2-25, y = 80+2+25)
Button_RR_DISARMED.place(x = 340+2-25, y = 105+4+25)
Button_RR_FIRE.place(x = 380, y = 65)
Button_RR_FIRE.place(x = 380, y = 65)

Button_ALL_FIRE_SIM.place(x = 5, y = 400)
Button_ALL_FIRE_SEQ.place(x = 225, y = 400)


Canvas.place(x=2, y=2)

Canvas.create_line(75+2-25+44,80+2+25,75+2-25+44,80,fill='RED')
Canvas.create_line(75+2-25+44,80,80,80,fill='RED')

Canvas.create_line(340+2+20,80+2+20,340+2+20,80,fill='RED')
Canvas.create_line(340+2+20,80,400,80,fill='RED')

Canvas.create_line(163+15,105+4+25,163+15,10,fill='RED')

Canvas.create_line(163+15+90,105+4+25,163+15+90,10,fill='RED')




is_alive = 1
threading.Thread(target=con).start()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
