from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import tkinter.font as tkfont
import random
import math
import functools
from typing import Tuple, cast


windown = Tk()
windown.geometry('630x550')
windown.title('CrypTool - RSA')

myFont = tkfont.Font(family='Time New Roman', size=10)
myFont1 = tkfont.Font(family='Time New Roman', size=11)


"""-------------------------------------------------------------------------------------------"""

#################### DECLARE FUNCTION #######################

# function check Prime


def check_Prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

# function to validate mark entry


def only_numbers(char):
    return char.isdigit()

# Function check_Prime entry


def checkPrime_entry(entry, buttonCheck):
    if check_Prime(int(entry.get())) == True:
        buttonCheck.config(bg="#00FF66")
    else:
        buttonCheck.config(bg="#FF3333")


# Function checkPrime_random


def randomPrime(entry):
    flag = False
    while (flag == False):
        val = random.randint(17, 701)
        if(check_Prime(val) == True):
            flag = True
    if (flag == True):
        entry.delete(0, tk.END)
        val_random = str(val)
        entry.insert(0, val_random)


def message_info_p():
    mb0 = messagebox.showinfo("showinfo", "p is prime and must be different from q ")

def message_info_q():
    mb0 = messagebox.showinfo("showinfo", "q is prime and must be different from p ")

def message_info_e():
    mb0 = messagebox.showinfo("showinfo", "e is a prime number and is in the range from 0 to phi(n) ")

def message_info_input():
    mb0 = messagebox.showinfo("showinfo", "1.Character: enter as letters without numbers. 2.Number: Must enter number and must be in the correct format 1 # 2 # 3... with a space between the number and '#' ")

# function calc n


def show_calcn(p_entry, q_entry, frame):
    if (check_Prime(int(p_entry.get())) == True) and (check_Prime(int(q_entry.get())) == True and (int(p_entry.get()) != int(q_entry.get()))):
        val = int(p_entry.get())*int(q_entry.get())
        val_str = str(val)
        myLabel = Label(frame, text=val_str,
                        width=40, background='white', relief="sunken")
        myLabel.grid(row=2, column=1, ipady=2)


def show_calcpn(p_entry, q_entry, frame):
    if (check_Prime(int(p_entry.get())) == True) and (check_Prime(int(q_entry.get())) == True and (int(p_entry.get()) != int(q_entry.get()))):
        val = (int(p_entry.get())-1)*(int(q_entry.get())-1)
        val_str = str(val)
        myLabel = Label(frame, text=val_str,
                        width=40, background='white', relief="sunken")
        myLabel.grid(row=3, column=1, ipady=2)

# Function Random_e


def egcd(e, r):
    while(r != 0):
        e, r = r, e % r
    return e


def randomPrime_e(e_entry, p_entry, q_entry):
    flag = False
    while (flag == False):
        temp = (int(p_entry.get())-1)*(int(q_entry.get())-1)
        val_random = random.randint(17, temp-1)
        if(check_Prime(val_random) == True and egcd(val_random, temp)):
            flag = True
    if (flag == True):
        e_entry.delete(0, tk.END)
        val = str(val_random)
        e_entry.insert(0, val)

# function calc_d and show


def check_prime_number(n):
    flag = True
    if (math.ceil(n) != math.floor(n)):
        flag = False
    return flag


def calc_d(e, p, q):
    x = 0
    d = 0
    r = (int(p.get())-1)*(int(q.get())-1)
    while check_prime_number((x*r + 1) / (int(e.get()))) == False:
        d = ((x+1)*r + 1)/(int(e.get()))
        x += 1
    return int(d)


def show_d(p, q, e, frame):
    d = calc_d(e, p, q)
    val_str = str(d)
    myLabel = Label(frame, text=val_str,
                    width=40, background='white', relief="sunken")
    myLabel.grid(row=5, column=1, ipady=2)


def delete(frame1):
    scrollbar = tk.Scrollbar(frame1, orient=HORIZONTAL)
    scrollbar.grid(row=3, column=1, ipadx=200)
    ascii_listbox = tk.Listbox(frame1, height=2, width=74, border=4,
                               xscrollcommand=scrollbar.set, highlightcolor="black", selectmode=EXTENDED)
    ascii_listbox.grid(row=2, column=1, sticky=NE, padx=8)
    ascii_listbox.config(state=tk.NORMAL)
    ascii_listbox.config(fg="black")
    ascii_listbox.configure(background="white")
    scrollbar.config(command=ascii_listbox.xview)


def delete1(frame2):
    scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
    scrollbar1.grid(row=2, column=1, ipadx=200)

    output_label = Label(frame2, text="Output : ",
                         font=('Time New Roman', 11))
    output_label.grid(row=1, column=0, ipadx=4)
    output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                highlightcolor="black", selectmode=MULTIPLE)
    output_listbox.grid(row=1, column=1, ipadx=5)
    output_listbox.config(state=tk.NORMAL)
    output_listbox.configure(xscrollcommand=scrollbar1.set)
    scrollbar1.config(command=output_listbox.xview)


""" -----------------------------Encrypt and Decrypt ----------------------------------"""


def convert_text(text_input, frame1, frame2):
    name = text_input.get()

    if any(ch.isdigit() for ch in name):
        delete(frame1)
        delete1(frame2)
        messagebox.showerror('message', 'Name can\'t have numbers')

    else:
        l1 = [ord(c) for c in name]
        l2 = []

        for i in range(len(l1)):
            l2 += [l1[i]] + [' '] + ['#'] + [' ']
        l2 = l2[:-3]

        mystring = "".join(map(str, l2))

        scrollbar = tk.Scrollbar(frame1, orient=HORIZONTAL)
        scrollbar.grid(row=3, column=1, ipadx=200)
        ascii_listbox = tk.Listbox(frame1, height=2, width=74, border=4,
                                   xscrollcommand=scrollbar.set, highlightcolor="black", selectmode=MULTIPLE)
        ascii_listbox.grid(row=2, column=1, sticky=NE, padx=8)
        ascii_listbox.config(state=tk.NORMAL)
        ascii_listbox.insert(END, mystring)
        ascii_listbox.config(fg="black")
        ascii_listbox.configure(background="white")
        scrollbar.config(command=ascii_listbox.xview)


def num_char(text_input, var):
    check = 0
    name = text_input.get()
    choice = var.get()

    if choice == 0:
        check = 0
    if choice == 1:
        check = 1
    return check


def cacl_en_char(text_input, e, p, q, frame2):
    name = text_input.get()

    if any(ch.isdigit() for ch in name):
        delete1(frame2)
    else:
        r = (int(p.get()))*(int(q.get()))

        l1 = [ord(c) for c in name]
        l2 = [pow(number, int(e.get())) % r for number in l1]
        l3 = []

        for i in range(len(l2)):
            l3 += [l2[i]] + [' '] + ['#'] + [' ']

        l3 = l3[:-3]

        mystring = "".join(map(str, l3))

        scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
        scrollbar1.grid(row=2, column=1, ipadx=200)

        output_label = Label(frame2, text="Output : ",
                             font=('Time New Roman', 11))
        output_label.grid(row=1, column=0, ipadx=4)
        output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                    highlightcolor="black", selectmode=MULTIPLE)
        output_listbox.grid(row=1, column=1, ipadx=5)
        output_listbox.config(state=tk.NORMAL)
        output_listbox.insert(END, mystring)
        output_listbox.configure(xscrollcommand=scrollbar1.set)
        scrollbar1.config(command=output_listbox.xview)


def cacl_de_char(text_input, e, p, q, frame2):
    name = text_input.get()
    if any(ch.isdigit() for ch in name):
        delete1(frame2)
    else:
        r = (int(p.get()))*(int(q.get()))

        l1 = [ord(c) for c in name]
        l2 = [pow(number, calc_d(e, p, q)) % r for number in l1]
        l3 = []

        for i in range(len(l2)):
            l3 += [l2[i]] + [' '] + ['#'] + [' ']

        l3 = l3[:-3]

        mystring = "".join(map(str, l3))

        scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
        scrollbar1.grid(row=2, column=1, ipadx=200)

        output_label = Label(frame2, text="Output : ",
                             font=('Time New Roman', 11))
        output_label.grid(row=1, column=0, ipadx=4)
        output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                    highlightcolor="black", selectmode=MULTIPLE)
        output_listbox.grid(row=1, column=1, ipadx=5)
        output_listbox.config(state=tk.NORMAL)
        output_listbox.insert(END, mystring)
        output_listbox.configure(xscrollcommand=scrollbar1.set)
        scrollbar1.config(command=output_listbox.xview)


def cacl_out_num(text_input, e, p, q, frame2):
    mystring = text_input.get()
    r = (int(p.get()))*(int(q.get()))
    l1 = mystring.split(' ')
    l1 = [int(i) for i in l1 if i != '#']
    l2 = [pow(number, int(e.get())) % r for number in l1]

    l2 = [chr(value) for value in l2]

    l3 = []

    for i in range(len(l2)):
        l3 += [l2[i]] + [' '] + ['#'] + [' ']

    l3 = l3[:-3]

    mystring = "".join(map(str, l3))

    scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
    scrollbar1.grid(row=2, column=1, ipadx=200)

    output_label = Label(frame2, text="Output : ", font=('Time New Roman', 11))
    output_label.grid(row=1, column=0, ipadx=4)
    output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                highlightcolor="black", selectmode=MULTIPLE)
    output_listbox.grid(row=1, column=1, ipadx=5)
    output_listbox.config(state=tk.NORMAL)
    output_listbox.insert(END, mystring)
    output_listbox.configure(xscrollcommand=scrollbar1.set)
    scrollbar1.config(command=output_listbox.xview)


def cacl_out1_num1(text_input, e, p, q, frame2):
    mystring = text_input.get()
    r = (int(p.get()))*(int(q.get()))
    l1 = mystring.split(' ')
    l1 = [int(i) for i in l1 if i != '#']
    l2 = [pow(number, calc_d(e, p, q)) % r for number in l1]

    l2 = [chr(value) for value in l2]

    l3 = []

    for i in range(len(l2)):
        l3 += [l2[i]] + [' '] + ['#'] + [' ']

    l3 = l3[:-3]

    mystring1 = "".join(map(str, l3))

    scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
    scrollbar1.grid(row=2, column=1, ipadx=200)

    output_label = Label(frame2, text="Output : ", font=('Time New Roman', 11))
    output_label.grid(row=1, column=0, ipadx=4)
    output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                highlightcolor="black", selectmode=MULTIPLE)
    output_listbox.grid(row=1, column=1, ipadx=5)
    output_listbox.config(state=tk.NORMAL)
    output_listbox.insert(END, mystring1)
    output_listbox.configure(xscrollcommand=scrollbar1.set)
    scrollbar1.config(command=output_listbox.xview)


def calc_en_num(text_input, e, p, q, frame1, frame2):
    mystring = text_input.get()
    if any(ch.isdigit() for ch in mystring) and '#' and ' ':
        r = (int(p.get()))*(int(q.get()))
        l1 = mystring.split(' ')
        l1 = [int(i) for i in l1 if i != '#']

        l2 = [pow(number, int(e.get())) % r for number in l1]
        l3 = []

        for i in range(len(l2)):
            l3 += [l2[i]] + [' '] + ['#'] + [' ']

        l3 = l3[:-3]

        mystring1 = "".join(map(str, l3))

        scrollbar = tk.Scrollbar(frame1, orient=HORIZONTAL)
        scrollbar.grid(row=3, column=1, ipadx=200)
        ascii_listbox = tk.Listbox(frame1, height=2, width=74, border=4,
                                   xscrollcommand=scrollbar.set, highlightcolor="black", selectmode=MULTIPLE)
        ascii_listbox.grid(row=2, column=1, sticky=NE, padx=8)
        ascii_listbox.config(state=tk.NORMAL)
        ascii_listbox.insert(END, mystring1)
        ascii_listbox.config(fg="black")
        ascii_listbox.configure(background="white")
        scrollbar.config(command=ascii_listbox.xview)

        n = True
        for i in range(len(l2)):
            if l2[i] < 0 or l2[i] > 127:
                n = False
                break
        if n == True:
            cacl_out_num(text_input, e, p, q, frame2)
        else:
            delete1(frame2)
            messagebox.showerror(
                'message', 'The encrypted message could not be decoded into a text message!')
    else:
        delete(frame1)
        delete1(frame2)
        messagebox.showerror('message', 'Name can\'t have characters')


def calc_de_num(text_input, e, p, q, frame1, frame2):
    mystring = text_input.get()
    if any(ch.isdigit() for ch in mystring) and '#' and ' ':
        r = (int(p.get()))*(int(q.get()))
        l1 = mystring.split(' ')
        l1 = [int(i) for i in l1 if i != '#']

        l2 = [pow(number, calc_d(e, p, q)) % r for number in l1]
        l3 = []

        for i in range(len(l2)):
            l3 += [l2[i]] + [' '] + ['#'] + [' ']

        l3 = l3[:-3]

        mystring1 = "".join(map(str, l3))

        scrollbar = tk.Scrollbar(frame1, orient=HORIZONTAL)
        scrollbar.grid(row=3, column=1, ipadx=200)
        ascii_listbox = tk.Listbox(frame1, height=2, width=74, border=4,
                                   xscrollcommand=scrollbar.set, highlightcolor="black", selectmode=MULTIPLE)
        ascii_listbox.grid(row=2, column=1, sticky=NE, padx=8)
        ascii_listbox.config(state=tk.NORMAL)
        ascii_listbox.insert(END, mystring1)
        ascii_listbox.config(fg="black")
        ascii_listbox.configure(background="white")
        scrollbar.config(command=ascii_listbox.xview)

        n = True
        for i in range(len(l2)):
            if l2[i] < 0 or l2[i] > 127:
                n = False
                break
        if n == True:
            cacl_out1_num1(text_input, e, p, q, frame2)
        else:
            delete1(frame2)
            messagebox.showerror(
                'message', 'The encrypted message could not be decoded into a text message!')
    else:
        delete(frame1)
        delete1(frame2)
        messagebox.showerror('message', 'Name can\'t have characters')


def En(text_input, frame1, frame2, e, p, q, var):
    if num_char(text_input, var) == 0:
        convert_text(text_input, frame1, frame2)
        cacl_en_char(text_input, e, p, q, frame2)
    else:
        calc_en_num(text_input, e, p, q, frame1, frame2)


def De(text_input, frame1, frame2, e, p, q, var):
    if num_char(text_input, var) == 0:
        convert_text(text_input, frame1, frame2)
        cacl_de_char(text_input, e, p, q, frame2)
    else:
        calc_de_num(text_input, e, p, q, frame1, frame2)


""" -------------------------------------------------------------------- """


def Clear_all(p, q, e, text_input, frame, frame1, frame2):
    p.delete(0, tk.END)
    q.delete(0, tk.END)
    e.delete(0, tk.END)
    n = Label(frame, width=40,
              background='white', relief="sunken")
    n.grid(row=2, column=1, ipady=2)
    pn = Label(frame, width=40,
               background='white', relief="sunken")
    pn.grid(row=3, column=1, ipady=2)
    d = Label(frame, width=40, background='white', relief="sunken")
    d.grid(row=5, column=1, ipady=2)

    text_input.delete(0, tk.END)

    delete(frame1)
    delete1(frame2)

    ####################### MAIN FUNTION ########################


def main():
    """----------------------------------------FRAME 0---------------------------------------------------"""

    validation = windown.register(only_numbers)

    frame = tk.LabelFrame(windown, text="Parameters")
    frame.grid(row=0, column=0, padx=8, pady=10, ipadx=4)

    """ BEGIN: Create p, stringvar, button, message box """

    p_label = Label(frame, text="p : ", font=('Time New Roman ', 11))
    p_label.grid(row=0, column=0)

    p_entry = tk.Entry(frame, validate="key",
                       validatecommand=(validation, '%S'), width=40)
    p_entry.grid(row=0, column=1, ipady=2)
    p_entry.focus()

    p_buttonCheck = tk.Button(frame, text="Check", width=8,
                              command=lambda: checkPrime_entry(p_entry, p_buttonCheck))
    p_buttonCheck['font'] = myFont
    p_buttonCheck.grid(row=0, column=2, padx=10)

    p_buttonRandom = tk.Button(
        frame, text="Random", width=8, command=lambda: randomPrime(p_entry))
    p_buttonRandom['font'] = myFont
    p_buttonRandom.grid(row=0, column=3, padx=10, ipady=2)

    p_buttonInfo = tk.Button(frame, text="?", width=8,
                             command=lambda: message_info())
    p_buttonInfo['font'] = myFont
    p_buttonInfo.grid(row=0, column=4, padx=10, ipady=2)

    """ END: Create p """

    """ BEGIN: Create q """

    q_label = Label(frame, text="q : ", font=('Time New Roman ', 11))
    q_label.grid(row=1, column=0)
    q_entry = Entry(frame, validate="key",
                    validatecommand=(validation, '%S'), width=40)
    q_entry.grid(row=1, column=1, padx=10, pady=5, ipady=2)

    q_buttonCheck = tk.Button(frame, text="Check", width=8,
                              command=lambda: checkPrime_entry(q_entry, q_buttonCheck))
    q_buttonCheck['font'] = myFont
    q_buttonCheck.grid(row=1, column=2)

    q_buttonRandom = tk.Button(
        frame, text="Random", width=8, command=lambda: randomPrime(q_entry))
    q_buttonRandom['font'] = myFont
    q_buttonRandom.grid(row=1, column=3, ipady=2)
    q_buttonInfo = tk.Button(frame, text="?", width=8, command=message_info)
    q_buttonInfo['font'] = myFont
    q_buttonInfo.grid(row=1, column=4, ipady=2)

    """ END: Create q """

    """ BEGIN: Create n """

    n_label = Label(frame, text="n: ", font=('Arial ', 11))
    n_label.grid(row=2, column=0)
    n_myLable = Label(frame, width=40,
                      background='white', relief="sunken")
    n_myLable.grid(row=2, column=1, ipady=2)
    n_buttonShow = tk.Button(frame, text="Show", width=8,
                             command=lambda: show_calcn(p_entry, q_entry, frame))
    n_buttonShow['font'] = myFont
    n_buttonShow.grid(row=2, column=2, ipady=2)

    """ END: Create n """

    """ BEGIN: Create Phi(n)"""

    pn_label = Label(frame, text="Phi(n) : ", font=('Time New Roman ', 11))
    pn_label.grid(row=3, column=0)
    pn_myLable = Label(frame, width=40,
                       background='white', relief="sunken")
    pn_myLable.grid(row=3, column=1, ipady=2)
    pn_buttonShow = tk.Button(frame, text="Show", width=8,
                              command=lambda: show_calcpn(p_entry, q_entry, frame))
    pn_buttonShow['font'] = myFont
    pn_buttonShow.grid(row=3, column=2, ipady=2)

    """ BEGIN: Create e"""

    e_label = Label(frame, text="e : ", font=('Time New Roman ', 11))
    e_label.grid(row=4, column=0)
    e_entry = Entry(frame, validate="key",
                    validatecommand=(validation, '%S'), width=40)
    e_entry.grid(row=4, column=1, padx=10, pady=5, ipady=2)

    e_buttonCheck = tk.Button(
        frame, text="Check", width=8, command=lambda: checkPrime_entry(e_entry, e_buttonCheck))
    e_buttonCheck['font'] = myFont
    e_buttonCheck.grid(row=4, column=2, ipady=2)

    e_buttonRandom = tk.Button(
        frame, text="Random", width=8, command=lambda: randomPrime_e(e_entry, p_entry, q_entry))
    e_buttonRandom['font'] = myFont
    e_buttonRandom.grid(row=4, column=3, ipady=2)

    e_buttonInfo = tk.Button(frame, text="?", width=8, command=message_info)
    e_buttonInfo['font'] = myFont
    e_buttonInfo.grid(row=4, column=4, ipady=2)

    """ END: Create e"""

    """BEGIN: Create d"""

    d_label = Label(frame, text="d : ", font=('Time New Roman ', 11))
    d_label.grid(row=5, column=0)
    d_myLabel = Label(frame, width=40, background='white', relief="sunken")
    d_myLabel.grid(row=5, column=1, ipady=2)

    d_buttonShow = tk.Button(frame, text="Show", width=8, command=lambda: show_d(
        p_entry, q_entry, e_entry, frame))
    d_buttonShow['font'] = myFont
    d_buttonShow.grid(row=5, column=2, ipady=2)

    """END: Create d"""

    """--------------------------------------------------------------------------------------------------"""

    """------------------------------------FRAME 1-------------------------------------------------------"""

    frame1 = tk.LabelFrame(windown, text="Input")
    frame1.grid(row=1, column=0, ipadx=10)

    var = tk.IntVar()

    """ Radio Button """

    radio_box1 = Radiobutton(
        frame1, text="Characters", variable=var, value=0)
    radio_box1.grid(row=0, column=0, columnspan=2)
    radio_box2 = Radiobutton(
        frame1, text="Numbers", variable=var, value=1)
    radio_box2.grid(row=0, column=1, sticky=W)

    """ Text Input """

    text_import = StringVar()
    text_label = Label(frame1, text="Text : ", font=('Time New Roman', 11))
    text_label.grid(row=1, column=0, ipadx=6)
    text_input = Entry(frame1, width=74, textvariable=text_import)
    text_input.grid(row=1, column=1, ipady=3, padx=10, sticky=NE)

    text_buttonInfo = tk.Button(
        frame1, text="?", width=4, command=message_info)
    text_buttonInfo['font'] = myFont
    text_buttonInfo.grid(row=1, column=2, ipady=3, padx=10)

    """ ASCII input """

    scrollbar = tk.Scrollbar(frame1, orient=HORIZONTAL)
    scrollbar.grid(row=3, column=1, ipadx=200)

    ascii_label = Label(frame1, text="Input : ", font=('Time New Roman', 11))
    ascii_label.grid(row=2, column=0, ipadx=3, ipady=15)
    ascii_listbox = tk.Listbox(frame1, width=74, height=2, border=4,
                               xscrollcommand=scrollbar.set, highlightcolor="black")
    ascii_listbox.grid(row=2, column=1, sticky=NE, padx=8)
    scrollbar.config(command=ascii_listbox.xview)

    """ -------------------------------------------------------------------------------------------------------------- """

    """ -------------------------------------------FRAME 2 ----------------------------------------------------------- """

    frame2 = tk.LabelFrame(windown, text="Output")
    frame2.grid(row=2, column=0, ipadx=45)

    scrollbar1 = tk.Scrollbar(frame2, orient=HORIZONTAL)
    scrollbar1.grid(row=2, column=1, ipadx=200)

    output_label = Label(frame2, text="Output : ", font=('Time New Roman', 11))
    output_label.grid(row=1, column=0, ipadx=4)
    output_listbox = tk.Listbox(frame2, width=72, height=2, border=4,
                                highlightcolor="black")
    output_listbox.grid(row=1, column=1, ipadx=5)
    output_listbox.configure(xscrollcommand=scrollbar1.set)
    scrollbar.config(command=output_listbox.xview)

    """ --------------------------------------------------------------------------------------------------------------------- """

    """ ----------------------------------------FRAME 3 --------------------------------------------------------------------- """

    frame3 = tk.LabelFrame(windown, relief=FLAT)
    frame3.grid(row=3, column=0, padx=10, pady=10, ipadx=180)

    Encrypt = tk.Button(frame3, text="Encrypt", width=8,
                        command=lambda: En(text_input, frame1, frame2, e_entry, p_entry, q_entry, var))
    Encrypt['font'] = myFont
    Encrypt.configure(background="#CFCFCF")
    Encrypt.pack(side=LEFT, fill=BOTH, padx=1, ipady=1)

    Decrypt = tk.Button(frame3, text="Decrypt", width=8, command=lambda: De(
        text_input, frame1, frame2, e_entry, p_entry, q_entry, var))
    Decrypt['font'] = myFont
    Decrypt.configure(background="#CFCFCF")
    Decrypt.pack(side=LEFT, fill=BOTH, ipady=1, padx=5)

    Clearall = tk.Button(frame3, text="Clear all", width=8,
                         command=lambda: Clear_all(p_entry, q_entry, e_entry, text_input, frame, frame1, frame2))
    Clearall.configure(background="#CFCFCF")
    Clearall['font'] = myFont
    Clearall.pack(side=RIGHT, fill=BOTH, ipady=1)

    """--------------------------------------------------------------------------------------------------"""


if __name__ == '__main__':
    main()
    windown.mainloop()
