import tkinter as tk
from tkinter import ttk
DENSITY=7850
F={"Meter (m)":1,"Millimeter (mm)":.001,"Feet (ft)":.3048,"Inch (in)":.0254}
def calc(*a):
    try:
        kg=float(L.get() or 0)*F[LU.get()]*float(W.get() or 0)*F[WU.get()]*float(T.get() or 0)*F[TU.get()]*DENSITY
        result.config(text=f"{kg:,.6f} KG")
    except ValueError: result.config(text="请输入数字")
def reset():
    L.set("1");W.set("1");T.set("1");LU.set("Meter (m)");WU.set("Meter (m)");TU.set("Millimeter (mm)");calc()
root=tk.Tk();root.title("Metal Plate Weight");root.geometry("430x500");root.minsize(390,450)
frm=ttk.Frame(root,padding=22);frm.pack(fill="both",expand=True)
ttk.Label(frm,text="Metal Plate Weight",font=("Segoe UI",18,"bold")).pack(anchor="w")
ttk.Label(frm,text="铁板重量计算器").pack(anchor="w",pady=(0,18))
L=W=T=tk.StringVar()
LU=WU=TU=tk.StringVar()
def field(name,var,unitvar,default,unit):
    ttk.Label(frm,text=name).pack(anchor="w")
    row=ttk.Frame(frm);row.pack(fill="x",pady=(3,12))
    var.set(default);unitvar.set(unit)
    ttk.Entry(row,textvariable=var).pack(side="left",fill="x",expand=True,padx=(0,8))
    ttk.Combobox(row,textvariable=unitvar,values=list(F),state="readonly",width=18).pack(side="right")
field("Length / 长度",L,LU,"1","Meter (m)")
field("Width / 宽度",W,WU,"1","Meter (m)")
field("Thickness / 厚度",T,TU,"1","Millimeter (mm)")
ttk.Button(frm,text="计算 Calculate",command=calc).pack(fill="x",pady=(4,8))
ttk.Button(frm,text="清除 Reset",command=reset).pack(fill="x")
result=ttk.Label(frm,text="0.007850 KG",font=("Segoe UI",24,"bold"),anchor="center")
result.pack(fill="x",pady=25)
ttk.Label(frm,text="钢材密度：7,850 kg/m³").pack()
for v in (L,W,T,LU,WU,TU): v.trace_add("write",calc)
root.after(50,calc);root.mainloop()
