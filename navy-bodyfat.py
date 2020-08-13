import tkinter as tk
import sys

def formula(event=None):

    from math import log10

    H = float(entry_H.get())
    N = float(entry_N.get())
    A = float(entry_A.get())

    bf = 86.1*log10(A - N) - 70.041*log10(H) + 36.76

    entry_H.delete(0, tk.END)
    entry_N.delete(0, tk.END)
    entry_A.delete(0, tk.END)

    label5.config(text="your estimated body fat is {bf:0.1f}%".format(bf=bf))

def quit():
    sys.exit()


app = tk.Tk()

thefont=("Calibri Light", 14)

label1 = tk.Label(
    text="this calculator will estimate your body fat using a formula developed \nby the U.S. Navy for body composition assessment.",
    font=thefont)

label2 = tk.Label(
    text="(this calculation only applies to males)",
    font=thefont)

label3 = tk.Label(
    text="measure your neck circumference just under the larynx. \nmeasure your abdominal circumference over the navel.",
    font=thefont,
    justify=tk.LEFT)

label4 = tk.Label(
    text="all measurements should be in inches.",
    font=thefont)

labelH = tk.Label(
    text="height:",
    font=thefont,
    justify=tk.RIGHT)

entry_H = tk.Entry(
    font=thefont,
    justify=tk.CENTER)

labelN = tk.Label(
    text="neck:",
    font=thefont,
    justify=tk.RIGHT)

entry_N = tk.Entry(
    font=thefont,
    justify=tk.CENTER)

labelA = tk.Label(
    text="abdomen:",
    font=thefont,
    justify=tk.RIGHT)

entry_A = tk.Entry(
    font=thefont,
    justify=tk.CENTER)

calculate = tk.Button(
    text="calculate",
    font=thefont,
    height=2,
    width=10,
    command=formula)

label5 = tk.Label(
    text="",
    font=thefont)

close = tk.Button(
    text="close",
    font=thefont,
    height=2,
    width=10,
    command=quit)

label1.grid(row=0, columnspan=2, pady=(40,10), padx=20)
label2.grid(row=1, columnspan=2, pady=10)
label3.grid(row=2, columnspan=2, pady=10)
label4.grid(row=3, columnspan=2, pady=10)

labelH.grid(row=4, sticky="E", pady=5)
entry_H.grid(row=4, column=1, sticky="W", pady=5)

labelN.grid(row=5, sticky="E", pady=5)
entry_N.grid(row=5, column=1, sticky="W", pady=5)

labelA.grid(row=6, sticky="E", pady=5)
entry_A.grid(row=6, column=1, sticky="W", pady=5)

calculate.grid(row=7, columnspan=2, pady=10)
label5.grid(row=8, columnspan=2, pady=(10, 30))
close.grid(row=9, columnspan=2, pady=(30,20))



app.title("U.S. Navy body fat")
app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
app.iconbitmap("navy_logo.ico")
app.mainloop()
