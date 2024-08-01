import tkinter as tk
import json
from tkinter.messagebox import askyesno, showinfo
def Findjson():
    with open(f"{ENE.get()}.json", "r") as f:
        data = json.load(f)
    showinfo("~<Student grading system>~~~<Popup>~", f"Student is {data["student"]["name"]}, Age is {data["student"]["age"]}, Class is {data["student"]["class"]}, Grade is {data["student"]["grade"]}")
    exit_hm = askyesno("~<Student grading system>~~~<Popup>~", 'Order has been done Exit window?')
    if exit_hm:
        WIN.destroy()
        exit()
def createjson():
    dictuse = {
        "student":{
            "name":NEE.get(),
            "age":ASBSB.get(),
            "class":CEE.get(),
            "grade":GSBSB.get()
        }
    }
    f = open("{}.json".format(NEE.get()), "w")
    f.write(str(json.dumps(dictuse)))
    f.close()
WIN = tk.Tk()
WIN.title("~<Student grading system>~")
#LOAD FILE LFrame
LLF = tk.LabelFrame(WIN,text="Load .json file")
LLF.grid(row=0, column=0, padx=50, pady=25, sticky="NEWS")
#label and entry
ENL = tk.Label(LLF, text="Name of the student")
ENL.grid(row=0, column=0, padx=20, pady=20)
ENE = tk.Entry(LLF)
ENE.grid(row=2, column=0, padx=20, pady=20)
#LOAD Get file
LB = tk.Button(LLF, text="LOAD", pady=10, padx=20, command=Findjson)
LB.grid(row=1, column=1, padx=20, pady=20, sticky="NEWS")
#CREATE LFrame
CLF = tk.LabelFrame(WIN, text="Create .json file")
CLF.grid(column=1, row=0, padx=50, pady=25)
#NAME Label And Entry
NEL = tk.Label(CLF, text="Name of the student")
NEL.grid(column=0, row=0, padx=20, pady=20)
NEE = tk.Entry(CLF)
NEE.grid(column=0, row=1, padx=20, pady=20)
#CLASS Label And Entry
CEL = tk.Label(CLF, text="The class of the student")
CEL.grid(column=1, row=0, pady=20, padx=20)
CEE = tk.Entry(CLF)
CEE.grid(column=1, row=1, padx=20, pady=20)
#AGE Label And Spinbox
ASBL = tk.Label(CLF, text="The age of the student")
ASBL.grid(column=3, row=0, padx=20, pady=20)
ASBSB = tk.Spinbox(CLF, from_=18, to=25)
ASBSB.grid(column=3, row=1, padx=20, pady=20)
#Grade Label And Spinbox
GSBL = tk.Label(CLF, text="The Grade(1-100) of the student")
GSBL.grid(column=4, row=0, padx=20, pady=20)
GSBSB = tk.Spinbox(CLF, from_=1, to=100)
GSBSB.grid(column=4, row=1, padx=20, pady=20)
#Submit button
Subb = tk.Button(CLF, text="Create .json file", command=createjson)
Subb.grid(column=2, row=2, padx=20, pady=20, sticky="NEWS")
WIN.mainloop()