
import os
import shutil
import time
from tkinter import *
import webbrowser
from fpdf import FPDF
from tkinter import filedialog
from tkinter import messagebox
from fpdf import FPDF
from PIL import Image
# print(len("The entry widget can be linked to the horizontal scrollbar if we want the user to enter more text then the actual width of the widget. the widget is holded"))
submitted = False
photo = ""
photoname = ""
os.mkdir("temp")
def destroy():
  shutil.rmtree("./temp")
  exit()
  

def startagenda():
  
  titleAgenda.destroy()
  # submitted = False
  # photo = ""
  # photoname = ""
  # TODO, FIX EMOJI UNICODE ERROR
  

  def makepdf(name: str):
    global photo
    global photoname
    TABLE_COL_NAMES = ("Plan", "Check")
    TABLE_COL_NAMES2 = ("What Happended", "Fixes")
    pdf = FPDF()
    pdf.set_margin(10)
    pdf.add_font("THSarabunNew", "", "./fonts/THSarabunNew/THSarabunNew.ttf")
    pdf.add_font("THSarabunNew", "B", "./fonts/THSarabunNew/THSarabunNew Bold.ttf")
    pdf.add_font("THSarabunNew", "BI", "./fonts/THSarabunNew/THSarabunNew BoldItalic.ttf")
    pdf.add_font("THSarabunNew", "I", "./fonts/THSarabunNew/THSarabunNew Italic.ttf")
    pdf.add_page()

    pdf.set_font("THSarabunNew", "BU", size=16)
    line_height = pdf.font_size * 3.8
    line_height_header = pdf.font_size * 2
    col_width = pdf.epw / 2  # distribute content evenly

    def render_table_header(data):

        pdf.set_font(style="BU")  # enabling bold text
        for col_name in data:
            pdf.cell(col_width, line_height_header, col_name, border=1)
            
        pdf.ln(line_height_header)
        pdf.set_font(style="")



    pdf.ln()
    pdf.cell(40, 10, f"Name: {yourName.get()}, Date: {Date.get()}")
    pdf.ln()
    render_table_header(TABLE_COL_NAMES)



    for row in ((PlanEntry.get()[0:155], CheckEntry.get()[0:155]),
      (PlanEntry2.get()[0:155], CheckEntry2.get()[0:155]),
      (PlanEntry3.get()[0:155], CheckEntry3.get()[0:155]),
      (PlanEntry4.get()[0:155], CheckEntry4.get()[0:155])):
            if pdf.will_page_break(line_height):
                render_table_header(TABLE_COL_NAMES)
            for datum in row:
                pdf.multi_cell(col_width, line_height, datum, border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size*1.25)
                
            pdf.ln(line_height)
    pdf.ln(5)
    render_table_header(TABLE_COL_NAMES2)
    
    for row in (
    (WhatHappendedEntry.get()[0:155], FixEntry.get()[0:155]),
    (WhatHappendedEntry2.get()[0:155], FixEntry2.get()[0:155]),
    (WhatHappendedEntry3.get()[0:155], FixEntry3.get()[0:155]),
    (WhatHappendedEntry4.get()[0:155], FixEntry4.get()[0:155]),
):
            if pdf.will_page_break(line_height):
                render_table_header(TABLE_COL_NAMES2)
            for datum in row:
                pdf.multi_cell(col_width, line_height, datum, border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            pdf.ln(line_height)
    pdf.ln()
    if photoname == "":
      print("")
    else:
      pdf.image(photo, x=90)
      if photobutton.cget("text") == "Add Photo":
        os.remove("./temp")
    pdf.output(f"{name}")

  def openagenda():
    global submitted
    try:
      a = filedialog.askopenfilename(initialdir="./", filetypes=(("Text Document", "*.txt"),("All Files", "*.txt")))
      f = open(a, "r")
    except Exception:
      f = open("AGENDA.txt", "r")
    if submitted == False:
      Check.config(state=NORMAL)
      CheckEntry.config(state=NORMAL)
      CheckEntryNum.config(state=NORMAL)
      CheckEntry2.config(state=NORMAL)
      CheckEntryNum2.config(state=NORMAL)
      CheckEntry3.config(state=NORMAL)
      CheckEntryNum3.config(state=NORMAL)
      CheckEntry4.config(state=NORMAL)
      CheckEntryNum4.config(state=NORMAL)

      WhatHappended.config(state=NORMAL)
      WhatHappendedEntry.config(state=NORMAL)
      WhatHappendedEntryNum.config(state=NORMAL)
      WhatHappendedEntry2.config(state=NORMAL)
      WhatHappendedEntryNum2.config(state=NORMAL)
      WhatHappendedEntry3.config(state=NORMAL)
      WhatHappendedEntryNum3.config(state=NORMAL)
      WhatHappendedEntry4.config(state=NORMAL)
      WhatHappendedEntryNum4.config(state=NORMAL)

      Fix.config(state=NORMAL)
      FixEntry.config(state=NORMAL)
      FixEntryNum.config(state=NORMAL)
      FixEntry2.config(state=NORMAL)
      FixEntryNum2.config(state=NORMAL)
      FixEntry3.config(state=NORMAL)
      FixEntryNum3.config(state=NORMAL)
      FixEntry4.config(state=NORMAL)
      FixEntryNum4.config(state=NORMAL)
    else:
      Plan.config(state=NORMAL)
      PlanEntry.config(state=NORMAL)
      PlanEntry2.config(state=NORMAL)
      PlanEntry3.config(state=NORMAL)
      PlanEntry4.config(state=NORMAL)
    f.readline()
    PlanEntry.delete(0, END)
    PlanEntry.insert(0, f.readline()[2:-1])
    PlanEntry2.delete(0, END)
    PlanEntry2.insert(0, f.readline()[2:-1])
    PlanEntry3.delete(0, END)
    PlanEntry3.insert(0, f.readline()[2:-1])
    PlanEntry4.delete(0, END)
    PlanEntry4.insert(0, f.readline()[2:-1])
    f.readline()
    CheckEntry.delete(0, END)
    CheckEntry.insert(0, f.readline()[2:-1])
    CheckEntry2.delete(0, END)
    CheckEntry2.insert(0, f.readline()[2:-1])
    CheckEntry3.delete(0, END)
    CheckEntry3.insert(0, f.readline()[2:-1])
    CheckEntry4.delete(0, END)
    CheckEntry4.insert(0, f.readline()[2:-1])
    f.readline()
    WhatHappendedEntry.delete(0, END)
    WhatHappendedEntry.insert(0, f.readline()[2:-1])
    WhatHappendedEntry2.delete(0, END)
    WhatHappendedEntry2.insert(0, f.readline()[2:-1])
    WhatHappendedEntry3.delete(0, END)
    WhatHappendedEntry3.insert(0, f.readline()[2:-1])
    WhatHappendedEntry4.delete(0, END)
    WhatHappendedEntry4.insert(0, f.readline()[2:-1])
    f.readline()
    FixEntry.delete(0, END)
    FixEntry.insert(0, f.readline()[2:-1])
    FixEntry2.delete(0, END)
    FixEntry2.insert(0, f.readline()[2:-1])
    FixEntry3.delete(0, END)
    FixEntry3.insert(0, f.readline()[2:-1])
    FixEntry4.delete(0, END)
    FixEntry4.insert(0, f.readline()[2:-1])
    yourName.delete(0, END)
    yourName.insert(0, f.readline()[6:-1])
    Date.delete(0, END)
    Date.insert(0, f.readline()[14:-1])
    if submitted == False:
      Check.config(state=DISABLED)
      CheckEntry.config(state=DISABLED)
      CheckEntryNum.config(state=DISABLED)
      CheckEntry2.config(state=DISABLED)
      CheckEntryNum2.config(state=DISABLED)
      CheckEntry3.config(state=DISABLED)
      CheckEntryNum3.config(state=DISABLED)
      CheckEntry4.config(state=DISABLED)
      CheckEntryNum4.config(state=DISABLED)

      WhatHappended.config(state=DISABLED)
      WhatHappendedEntry.config(state=DISABLED)
      WhatHappendedEntryNum.config(state=DISABLED)
      WhatHappendedEntry2.config(state=DISABLED)
      WhatHappendedEntryNum2.config(state=DISABLED)
      WhatHappendedEntry3.config(state=DISABLED)
      WhatHappendedEntryNum3.config(state=DISABLED)
      WhatHappendedEntry4.config(state=DISABLED)
      WhatHappendedEntryNum4.config(state=DISABLED)

      Fix.config(state=DISABLED)
      FixEntry.config(state=DISABLED)
      FixEntryNum.config(state=DISABLED)
      FixEntry2.config(state=DISABLED)
      FixEntryNum2.config(state=DISABLED)
      FixEntry3.config(state=DISABLED)
      FixEntryNum3.config(state=DISABLED)
      FixEntry4.config(state=DISABLED)
      FixEntryNum4.config(state=DISABLED)
    else:
      Plan.config(state=DISABLED)
      PlanEntry.config(state=DISABLED)
      PlanEntry2.config(state=DISABLED)
      PlanEntry3.config(state=DISABLED)
      PlanEntry4.config(state=DISABLED)

  def save():
    try:
      a = filedialog.asksaveasfilename(filetypes=(("Text Document", "*.txt"),("All Files", "*.txt")))
      f = open(a, "w")
      f.write("Plan: \n")
      f.write(f"1.{PlanEntry.get()}\n")
      f.write(f"2.{PlanEntry2.get()}\n")
      f.write(f"3.{PlanEntry3.get()}\n")
      f.write(f"4.{PlanEntry4.get()}\n")
      f.write("Check: \n")
      f.write(f"1.{CheckEntry.get()}\n")
      f.write(f"2.{CheckEntry2.get()}\n")
      f.write(f"3.{CheckEntry3.get()}\n")
      f.write(f"4.{CheckEntry4.get()}\n")
      f.write("What Happended: \n")
      f.write(f"1.{WhatHappendedEntry.get()}\n")
      f.write(f"2.{WhatHappendedEntry2.get()}\n")
      f.write(f"3.{WhatHappendedEntry3.get()}\n")
      f.write(f"4.{WhatHappendedEntry4.get()}\n")
      f.write("Fixes: \n")
      f.write(f"1.{FixEntry.get()}\n")
      f.write(f"2.{FixEntry2.get()}\n")
      f.write(f"3.{FixEntry3.get()}\n")
      f.write(f"4.{FixEntry4.get()}\n")
      f.write(f"Name: {yourName.get()}\n")
      f.write(f"Date Created: {Date.get()}\n")
    except Exception:
      print("")

  # ADD PHOTO
  def add_photo():
    global photo
    global photoname

    photo = filedialog.askopenfilename(filetypes=(("JPEG images", "*.jpg"), ("PNG images", "*.png"), ("Other Image Types", "*.*")))

    if photo != "":
      filename, file_extension = os.path.splitext(photo)
      photoname = f"./temp/TempPic{file_extension}"
      photofile = os.path.split(photo)
      photobutton.config(text=f"{photofile[1]}, Change")
      image = Image.open(photo)
      photo = image.resize((100, 100))
      photo.save(photoname)
    # else:
    #   print("")

  def export():
    
    def maketablepdf(name: str, date: str, planAndCheck: tuple, whatAndFixes: tuple):

        def choosefexport():
          # global chosen
          chosen = chooseEntry.get()
          nameChooserTK.destroy()
          location = filedialog.askdirectory(title="Choose a file location")
          name = ""
          
          if ".pdf" in chosen:
            # pdf.output(f"{location}/{chosen}")
            name = f"{location}/{chosen}"
          elif ".pdf" not in chosen:
            # pdf.output(f"{location}/{chosen}.pdf")
            name = f"{location}/{chosen}.pdf"
          messagebox.showinfo("Agenda App Message", "Created your pdf file. Do whatever you want with it!")
          makepdf(name)



       
 
        nameChooserTK = Toplevel()
        # TODO need to check if toplevel exists
        nameChooserTK.title("Agenda App Export Filename Chooser")
        choose = Label(nameChooserTK, text="Enter a name for the pdf export file.", font=("Consolas", 20))
        chooseEntry = Entry(nameChooserTK, font=("Consolas", 20))
        chooseButton = Button(nameChooserTK, text="Select!", font=("Consolas", 20), command=choosefexport)
        
        choose.pack()
        chooseEntry.pack()
        chooseButton.pack()
        nameChooserTK.grab_set()



    table1 = (
        (PlanEntry.get(), CheckEntry.get()),
        (PlanEntry2.get(), CheckEntry2.get()),
        (PlanEntry3.get(), CheckEntry3.get()),
        (PlanEntry4.get(), CheckEntry4.get()),
    )
    table2 = (
        (WhatHappendedEntry.get(), FixEntry.get()),
        (WhatHappendedEntry2.get(), FixEntry2.get()),
        (WhatHappendedEntry3.get(), FixEntry3.get()),
        (WhatHappendedEntry4.get(), FixEntry4.get()),
    )
    
    maketablepdf(yourName.get(), Date.get(), table1, table2)

  def previewpdf():

        makepdf("./temp/temp.pdf")

        
        fullpath = os.path.abspath("./temp/temp.pdf")
        webbrowser.open(f"file:///{fullpath}")
        time.sleep(3)
        os.remove("./temp/temp.pdf")


  

  def submit():
    global submitted
    submitted = True
    Plan.config(state=DISABLED)
    PlanEntry.config(state=DISABLED)
    PlanEntryNum.config(state=DISABLED)
    PlanEntry2.config(state=DISABLED)
    PlanEntryNum2.config(state=DISABLED)
    PlanEntry3.config(state=DISABLED)
    PlanEntryNum3.config(state=DISABLED)
    PlanEntry4.config(state=DISABLED)
    PlanEntryNum4.config(state=DISABLED)

    Check.config(state=NORMAL)
    CheckEntry.config(state=NORMAL)
    CheckEntryNum.config(state=NORMAL)
    CheckEntry2.config(state=NORMAL)
    CheckEntryNum2.config(state=NORMAL)
    CheckEntry3.config(state=NORMAL)
    CheckEntryNum3.config(state=NORMAL)
    CheckEntry4.config(state=NORMAL)
    CheckEntryNum4.config(state=NORMAL)

    WhatHappended.config(state=NORMAL)
    WhatHappendedEntry.config(state=NORMAL)
    WhatHappendedEntryNum.config(state=NORMAL)
    WhatHappendedEntry2.config(state=NORMAL)
    WhatHappendedEntryNum2.config(state=NORMAL)
    WhatHappendedEntry3.config(state=NORMAL)
    WhatHappendedEntryNum3.config(state=NORMAL)
    WhatHappendedEntry4.config(state=NORMAL)
    WhatHappendedEntryNum4.config(state=NORMAL)

    Fix.config(state=NORMAL)
    FixEntry.config(state=NORMAL)
    FixEntryNum.config(state=NORMAL)
    FixEntry2.config(state=NORMAL)
    FixEntryNum2.config(state=NORMAL)
    FixEntry3.config(state=NORMAL)
    FixEntryNum3.config(state=NORMAL)
    FixEntry4.config(state=NORMAL)
    FixEntryNum4.config(state=NORMAL)

    Submit.config(state=DISABLED)

  def new():
    global submitted
    global photo
    global photoname
    if messagebox.askyesno("Agenda Confirmation", "Do you want to save changes in this agenda?"):
      a = filedialog.asksaveasfilename()
      
      f = open(a, "w")
      f.write("Plan: \n")
      f.write(f"1.{PlanEntry.get()}\n")
      f.write(f"2.{PlanEntry2.get()}\n")
      f.write(f"3.{PlanEntry3.get()}\n")
      f.write(f"4.{PlanEntry4.get()}\n")
      f.write("Check: \n")
      f.write(f"1.{CheckEntry.get()}\n")
      f.write(f"2.{CheckEntry2.get()}\n")
      f.write(f"3.{CheckEntry3.get()}\n")
      f.write(f"4.{CheckEntry4.get()}\n")
      f.write("What Happended: \n")
      f.write(f"1.{WhatHappendedEntry.get()}\n")
      f.write(f"2.{WhatHappendedEntry2.get()}\n")
      f.write(f"3.{WhatHappendedEntry3.get()}\n")
      f.write(f"4.{WhatHappendedEntry4.get()}\n")
      f.write("Fixes: \n")
      f.write(f"1.{FixEntry.get()}\n")
      f.write(f"2.{FixEntry2.get()}\n")
      f.write(f"3.{FixEntry3.get()}\n")
      f.write(f"4.{FixEntry4.get()}\n")
      photobutton.config(text="Add Photo")
      photo = ""
      photoname = ""
      shutil.rmtree("./temp")
      os.mkdir("./temp")
      PlanEntry.delete(0, END)
      PlanEntry2.delete(0, END)
      PlanEntry3.delete(0, END)
      PlanEntry4.delete(0, END)
      CheckEntry.delete(0, END)
      CheckEntry2.delete(0, END)
      CheckEntry3.delete(0, END)
      CheckEntry4.delete(0, END)
      WhatHappendedEntry.delete(0, END)
      WhatHappendedEntry2.delete(0, END)
      WhatHappendedEntry3.delete(0, END)
      WhatHappendedEntry4.delete(0, END)
      FixEntry.delete(0, END)
      FixEntry2.delete(0, END)
      FixEntry3.delete(0, END)
      FixEntry4.delete(0, END)
      yourName.delete(0, END)
      Date.delete(0, END)
    else:
      photobutton.config(text="Add Photo")
      photo = ""
      photoname = ""
      shutil.rmtree("./temp")
      os.mkdir("./temp")
      submitted = False
      if submitted == False:
        Check.config(state=NORMAL)
        CheckEntry.config(state=NORMAL)
        CheckEntryNum.config(state=NORMAL)
        CheckEntry2.config(state=NORMAL)
        CheckEntryNum2.config(state=NORMAL)
        CheckEntry3.config(state=NORMAL)
        CheckEntryNum3.config(state=NORMAL)
        CheckEntry4.config(state=NORMAL)
        CheckEntryNum4.config(state=NORMAL)

        WhatHappended.config(state=NORMAL)
        WhatHappendedEntry.config(state=NORMAL)
        WhatHappendedEntryNum.config(state=NORMAL)
        WhatHappendedEntry2.config(state=NORMAL)
        WhatHappendedEntryNum2.config(state=NORMAL)
        WhatHappendedEntry3.config(state=NORMAL)
        WhatHappendedEntryNum3.config(state=NORMAL)
        WhatHappendedEntry4.config(state=NORMAL)
        WhatHappendedEntryNum4.config(state=NORMAL)

        Fix.config(state=NORMAL)
        FixEntry.config(state=NORMAL)
        FixEntryNum.config(state=NORMAL)
        FixEntry2.config(state=NORMAL)
        FixEntryNum2.config(state=NORMAL)
        FixEntry3.config(state=NORMAL)
        FixEntryNum3.config(state=NORMAL)
        FixEntry4.config(state=NORMAL)
        FixEntryNum4.config(state=NORMAL)

        Plan.config(state=NORMAL)
        PlanEntry.config(state=NORMAL)
        PlanEntryNum.config(state=NORMAL)
        PlanEntry2.config(state=NORMAL)
        PlanEntryNum2.config(state=NORMAL)
        PlanEntry3.config(state=NORMAL)
        PlanEntryNum3.config(state=NORMAL)
        PlanEntry4.config(state=NORMAL)
        PlanEntryNum4.config(state=NORMAL)
        Submit.config(state=NORMAL)

      else:
        Plan.config(state=NORMAL)
        PlanEntry.config(state=NORMAL)
        PlanEntry2.config(state=NORMAL)
        PlanEntry3.config(state=NORMAL)
        PlanEntry4.config(state=NORMAL)
      PlanEntry.delete(0, END)
      PlanEntry2.delete(0, END)
      PlanEntry3.delete(0, END)
      PlanEntry4.delete(0, END)
      CheckEntry.delete(0, END)
      CheckEntry2.delete(0, END)
      CheckEntry3.delete(0, END)
      CheckEntry4.delete(0, END)
      WhatHappendedEntry.delete(0, END)
      WhatHappendedEntry2.delete(0, END)
      WhatHappendedEntry3.delete(0, END)
      WhatHappendedEntry4.delete(0, END)
      FixEntry.delete(0, END)
      FixEntry2.delete(0, END)
      FixEntry3.delete(0, END)
      FixEntry4.delete(0, END)
      yourName.delete(0, END)
      Date.delete(0, END)
      if submitted == False:
        Check.config(state=DISABLED)
        CheckEntry.config(state=DISABLED)
        CheckEntryNum.config(state=DISABLED)
        CheckEntry2.config(state=DISABLED)
        CheckEntryNum2.config(state=DISABLED)
        CheckEntry3.config(state=DISABLED)
        CheckEntryNum3.config(state=DISABLED)
        CheckEntry4.config(state=DISABLED)
        CheckEntryNum4.config(state=DISABLED)

        WhatHappended.config(state=DISABLED)
        WhatHappendedEntry.config(state=DISABLED)
        WhatHappendedEntryNum.config(state=DISABLED)
        WhatHappendedEntry2.config(state=DISABLED)
        WhatHappendedEntryNum2.config(state=DISABLED)
        WhatHappendedEntry3.config(state=DISABLED)
        WhatHappendedEntryNum3.config(state=DISABLED)
        WhatHappendedEntry4.config(state=DISABLED)
        WhatHappendedEntryNum4.config(state=DISABLED)

        Fix.config(state=DISABLED)
        FixEntry.config(state=DISABLED)
        FixEntryNum.config(state=DISABLED)
        FixEntry2.config(state=DISABLED)
        FixEntryNum2.config(state=DISABLED)
        FixEntry3.config(state=DISABLED)
        FixEntryNum3.config(state=DISABLED)
        FixEntry4.config(state=DISABLED)
        FixEntryNum4.config(state=DISABLED)
      else:
        Plan.config(state=DISABLED)
        PlanEntry.config(state=DISABLED)
        PlanEntry2.config(state=DISABLED)
        PlanEntry3.config(state=DISABLED)
        PlanEntry4.config(state=DISABLED)

  def check(inputtext, WidgetNumber):
    counted = len(inputtext)

    if counted > 155:
      if int(WidgetNumber) == 1:
        countingPlanEntry1.config(fg="red")
        PlanEntry.config(fg="darkred")
      if int(WidgetNumber) == 2:
        countingPlanEntry2.config(fg="red")
        PlanEntry2.config(fg="darkred")
      if int(WidgetNumber) == 3:
        countingPlanEntry3.config(fg="red")
        PlanEntry3.config(fg="darkred")
      if int(WidgetNumber) == 4:
        countingPlanEntry4.config(fg="red")
        PlanEntry4.config(fg="darkred")
      if int(WidgetNumber) == 5:
        countingCheckEntry1.config(fg="red")
        CheckEntry.config(fg="darkred")
      if int(WidgetNumber) == 6:
        countingCheckEntry2.config(fg="red")
        CheckEntry2.config(fg="darkred")
      if int(WidgetNumber) == 7:
        countingCheckEntry3.config(fg="red")
        CheckEntry3.config(fg="darkred")
      if int(WidgetNumber) == 8:
        countingCheckEntry4.config(fg="red")
        CheckEntry4.config(fg="darkred")
      if int(WidgetNumber) == 9:
        countingWhatHappendedEntry1.config(fg="red")
        WhatHappendedEntry.config(fg="darkred")
      if int(WidgetNumber) == 10:
        countingWhatHappendedEntry2.config(fg="red")
        WhatHappendedEntry2.config(fg="darkred")
      if int(WidgetNumber) == 11:
        countingWhatHappendedEntry3.config(fg="red")
        WhatHappendedEntry3.config(fg="darkred")
      if int(WidgetNumber) == 12:
        countingWhatHappendedEntry4.config(fg="red")
        WhatHappendedEntry4.config(fg="darkred")
      if int(WidgetNumber) == 13:
        countingFixEntry1.config(fg="red")
        FixEntry.config(fg="darkred")
      if int(WidgetNumber) == 14:
        countingFixEntry2.config(fg="red")
        FixEntry2.config(fg="darkred")
      if int(WidgetNumber) == 15:
        countingFixEntry3.config(fg="red")
        FixEntry3.config(fg="darkred")
      if int(WidgetNumber) == 16:
        countingFixEntry4.config(fg="red")
        FixEntry4.config(fg="darkred")
      
    else:
      if int(WidgetNumber) == 1:
        countingPlanEntry1.config(fg="black")
        PlanEntry.config(fg="black")
      if int(WidgetNumber) == 2:
        countingPlanEntry2.config(fg="black")
        PlanEntry2.config(fg="black")
      if int(WidgetNumber) == 3:
        countingPlanEntry3.config(fg="black")
        PlanEntry3.config(fg="black")
      if int(WidgetNumber) == 4:
        countingPlanEntry4.config(fg="black")
        PlanEntry4.config(fg="black")
      if int(WidgetNumber) == 5:
        countingCheckEntry1.config(fg="black")
        CheckEntry.config(fg="black")
      if int(WidgetNumber) == 6:
        countingCheckEntry2.config(fg="black")
        CheckEntry2.config(fg="black")
      if int(WidgetNumber) == 7:
        countingCheckEntry3.config(fg="black")
        CheckEntry3.config(fg="black")
      if int(WidgetNumber) == 8:
        countingCheckEntry4.config(fg="black")
        CheckEntry4.config(fg="black")
      if int(WidgetNumber) == 9:
        countingWhatHappendedEntry1.config(fg="black")
        WhatHappendedEntry.config(fg="black")
      if int(WidgetNumber) == 10:
        countingWhatHappendedEntry2.config(fg="black")
        WhatHappendedEntry2.config(fg="black")
      if int(WidgetNumber) == 11:
        countingWhatHappendedEntry3.config(fg="black")
        WhatHappendedEntry3.config(fg="black")
      if int(WidgetNumber) == 12:
        countingWhatHappendedEntry4.config(fg="black")
        WhatHappendedEntry4.config(fg="black")
      if int(WidgetNumber) == 13:
        countingFixEntry1.config(fg="black")
        FixEntry.config(fg="black")
      if int(WidgetNumber) == 14:
        countingFixEntry2.config(fg="black")
        FixEntry2.config(fg="black")
      if int(WidgetNumber) == 15:
        countingFixEntry3.config(fg="black")
        FixEntry3.config(fg="black")
      if int(WidgetNumber) == 16:
        countingFixEntry4.config(fg="black")
        FixEntry4.config(fg="black")
    if int(WidgetNumber) == 1:
      PlanCount1.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 2:
      PlanCount2.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 3:
      PlanCount3.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 4:
      PlanCount4.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 5:
      CheckCount1.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 6:
      CheckCount2.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 7:
      CheckCount3.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 8:
      CheckCount4.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 9:
      WhatHappendedCount1.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 10:
      WhatHappendedCount2.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 11:
      WhatHappendedCount3.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 12:
      WhatHappendedCount4.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 13:
      FixCount1.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 14:
      FixCount2.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 15:
      FixCount3.set(str(counted) + f"/{CountLimit}")
    if int(WidgetNumber) == 16:
      FixCount4.set(str(counted) + f"/{CountLimit}")
    return True

  CountLimit = 155


  window = Tk()
  menubar = Menu(window)
  window.config(menu=menubar)
  window.iconphoto(False, PhotoImage(file="./images/AgendaIcon.png"))
  filemenu = Menu(menubar, tearoff=0)
  filemenu.add_command(label="New", command=new)
  filemenu.add_command(label="Save", command=save)
  filemenu.add_command(label="Open", command=open)
  filemenu.add_command(label="Export PDF", command=export)
  filemenu.add_command(label="Preview PDF", command=previewpdf)
  filemenu.add_command(label="Add Photo", command=add_photo)
  filemenu.add_separator()
  filemenu.add_command(label="Quit", command=destroy)

  menubar.add_cascade(label="File", menu=filemenu, underline=0)

  aboutmenu = Menu(menubar, tearoff=0)
  def AboutButton():
    messagebox.showinfo("About", "This is an Agenda Application, By Thawin Chalermdit, Pachara Chaiwiwatworakul, Chutchanun Manmoh, \n My inspiration to create this is that in G.4 in DSIL School,\n me and my friends have Agenda every Monday, and I wanted to make it easier,\n so that the user can save it into the computer.")
  aboutmenu.add_command(label="About", command=AboutButton)
  menubar.add_cascade(label="About", menu=aboutmenu, underline=0)

  # TODO Add functions cut copy paste

  count = window.register(check)
  PlanCount1 = StringVar()
  PlanCount1.set(str(0) + f"/{CountLimit}")
  PlanCount2 = StringVar()
  PlanCount2.set(str(0) + f"/{CountLimit}")
  PlanCount3 = StringVar()
  PlanCount3.set(str(0) + f"/{CountLimit}")
  PlanCount4 = StringVar()
  PlanCount4.set(str(0) + f"/{CountLimit}")
  CheckCount1 = StringVar()
  CheckCount1.set(str(0) + f"/{CountLimit}")
  CheckCount2 = StringVar()
  CheckCount2.set(str(0) + f"/{CountLimit}")
  CheckCount3 = StringVar()
  CheckCount3.set(str(0) + f"/{CountLimit}")
  CheckCount4 = StringVar()
  CheckCount4.set(str(0) + f"/{CountLimit}")
  WhatHappendedCount1 = StringVar()
  WhatHappendedCount1.set(str(0) + f"/{CountLimit}")
  WhatHappendedCount2 = StringVar()
  WhatHappendedCount2.set(str(0) + f"/{CountLimit}")
  WhatHappendedCount3 = StringVar()
  WhatHappendedCount3.set(str(0) + f"/{CountLimit}")
  WhatHappendedCount4 = StringVar()
  WhatHappendedCount4.set(str(0) + f"/{CountLimit}")
  FixCount1 = StringVar()
  FixCount1.set(str(0) + f"/{CountLimit}")
  FixCount2 = StringVar()
  FixCount2.set(str(0) + f"/{CountLimit}")
  FixCount3 = StringVar()
  FixCount3.set(str(0) + f"/{CountLimit}")
  FixCount4 = StringVar()
  FixCount4.set(str(0) + f"/{CountLimit}")

  window.geometry("1530x900")
  window.config(bg="black")
  window.title("Agenda Application")
  titleframe = Frame(window, bg="black")
  Title = Label(titleframe, text="Agenda Application", font=("Consolas", 50), bg="black", fg="white")
  Description = Label(titleframe, text="Helps with agenda.", font=("Consolas", 20), bg="black", fg="white")
  titleframe.place(x=0, y=0)
  Plan = Label(window, text="Plan: ", font=("Consolas", 30), bg="black", fg="white")

  PlanEntryNum = Label(window, text="1. ", font=("Consolas", 30), bg="black", fg="white")
  PlanEntry = Entry(window, font=("Consolas", 30))
  countingPlanEntry1 = Label(window, font=("Consolas", 30), textvariable=PlanCount1)
  PlanEntry.config(validate="key", validatecommand=(count, "%P", 1))  

  PlanEntryNum2 = Label(window, text="2. ", font=("Consolas", 30), bg="black", fg="white")
  PlanEntry2 = Entry(window, font=("Consolas", 30))
  countingPlanEntry2 = Label(window, font=("Consolas", 30), textvariable=PlanCount2)
  PlanEntry2.config(validate="key", validatecommand=(count, "%P", 2))  

  PlanEntryNum3 = Label(window, text="3. ", font=("Consolas", 30), bg="black", fg="white")
  PlanEntry3 = Entry(window, font=("Consolas", 30))
  countingPlanEntry3 = Label(window, font=("Consolas", 30), textvariable=PlanCount3)
  PlanEntry3.config(validate="key", validatecommand=(count, "%P", 3))  

  PlanEntryNum4 = Label(window, text="4. ", font=("Consolas", 30), bg="black", fg="white")
  PlanEntry4 = Entry(window, font=("Consolas", 30))
  countingPlanEntry4 = Label(window, font=("Consolas", 30), textvariable=PlanCount4)
  PlanEntry4.config(validate="key", validatecommand=(count, "%P", 4))  

  Check = Label(window, text="Check: ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)

  CheckEntryNum = Label(window, text="1. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingCheckEntry1 = Label(window, font=("Consolas", 30), textvariable=CheckCount1)
  CheckEntry = Entry(window, font=("Consolas", 30), state=DISABLED)
  CheckEntry.config(validate="key", validatecommand=(count, "%P", 5))

  CheckEntryNum2 = Label(window, text="2. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingCheckEntry2 = Label(window, font=("Consolas", 30), textvariable=CheckCount2)
  CheckEntry2 = Entry(window, font=("Consolas", 30), state=DISABLED)
  CheckEntry2.config(validate="key", validatecommand=(count, "%P", 6))

  CheckEntryNum3 = Label(window, text="3. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingCheckEntry3 = Label(window, font=("Consolas", 30), textvariable=CheckCount3)
  CheckEntry3 = Entry(window, font=("Consolas", 30), state=DISABLED)
  CheckEntry3.config(validate="key", validatecommand=(count, "%P", 7))

  CheckEntryNum4 = Label(window, text="4. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingCheckEntry4 = Label(window, font=("Consolas", 30), textvariable=CheckCount4)
  CheckEntry4 = Entry(window, font=("Consolas", 30), state=DISABLED)
  CheckEntry4.config(validate="key", validatecommand=(count, "%P", 8))

  WhatHappended = Label(window, text="What Happended: ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)

  WhatHappendedEntryNum = Label(window, text="1. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingWhatHappendedEntry1 = Label(window, font=("Consolas", 30), textvariable=WhatHappendedCount1)
  WhatHappendedEntry = Entry(window, font=("Consolas", 30), state=DISABLED)
  WhatHappendedEntry.config(validate="key", validatecommand=(count, "%P", 9))

  WhatHappendedEntryNum2 = Label(window, text="2. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingWhatHappendedEntry2 = Label(window, font=("Consolas", 30), textvariable=WhatHappendedCount2)
  WhatHappendedEntry2 = Entry(window, font=("Consolas", 30), state=DISABLED)
  WhatHappendedEntry2.config(validate="key", validatecommand=(count, "%P", 10))

  WhatHappendedEntryNum3 = Label(window, text="3. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingWhatHappendedEntry3 = Label(window, font=("Consolas", 30), textvariable=WhatHappendedCount3)
  WhatHappendedEntry3 = Entry(window, font=("Consolas", 30), state=DISABLED)
  WhatHappendedEntry3.config(validate="key", validatecommand=(count, "%P", 11))

  WhatHappendedEntryNum4 = Label(window, text="4. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingWhatHappendedEntry4 = Label(window, font=("Consolas", 30), textvariable=WhatHappendedCount4)
  WhatHappendedEntry4 = Entry(window, font=("Consolas", 30), state=DISABLED)
  WhatHappendedEntry4.config(validate="key", validatecommand=(count, "%P", 12))

  Fix = Label(window, text="Fixes: ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)

  FixEntryNum = Label(window, text="1. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingFixEntry1 = Label(window, font=("Consolas", 30), textvariable=FixCount1)
  FixEntry = Entry(window, font=("Consolas", 30), state=DISABLED)
  FixEntry.config(validate="key", validatecommand=(count, "%P", 13))

  FixEntryNum2 = Label(window, text="2. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingFixEntry2 = Label(window, font=("Consolas", 30), textvariable=FixCount2)
  FixEntry2 = Entry(window, font=("Consolas", 30), state=DISABLED)
  FixEntry2.config(validate="key", validatecommand=(count, "%P", 14))

  FixEntryNum3 = Label(window, text="3. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingFixEntry3 = Label(window, font=("Consolas", 30), textvariable=FixCount3)
  FixEntry3 = Entry(window, font=("Consolas", 30), state=DISABLED)
  FixEntry3.config(validate="key", validatecommand=(count, "%P", 15))

  FixEntryNum4 = Label(window, text="4. ", font=("Consolas", 30), bg="black", fg="white", state=DISABLED)
  countingFixEntry4 = Label(window, font=("Consolas", 30), textvariable=FixCount4)
  FixEntry4 = Entry(window, font=("Consolas", 30), state=DISABLED)
  FixEntry4.config(validate="key", validatecommand=(count, "%P", 16))

  Submit = Button(window, text="Submit", font=("Consolas", 20), command=submit, width=20, relief=RAISED)
  Export = Button(window, text="Export PDF", font=("Consolas", 20), command=export)
  openAGENDA = Button(window, text="Open", font=("Consolas", 20), command=openagenda)
  savebutton = Button(window, text="Save", font=("Consolas", 20), command=save)
  newButton = Button(window, text="New", font=("Consolas", 20), command=new)
  previewbutton = Button(window, text="Preview PDF", font=("Consolas", 20), command=previewpdf)
  photobutton = Button(window, text="Add Photo", font=("Consolas", 20), command=add_photo)
  yourName = Entry(window, font=("Consolas", 30), width=10)
  yourNameLabel = Label(window, text="Name: ", font=("Consolas", 30), bg="black", fg="white")
  Date = Entry(window, font=("Consolas", 30), width=10)
  DateLabel = Label(window, text="Date: ", font=("Consolas", 30), bg="black", fg="white")
  Title.pack()
  Description.pack()
  Plan.place(x=0, y=150)

  PlanEntry.place(x=50, y=200)
  countingPlanEntry1.place(x=500, y=200)
  PlanEntryNum.place(x=0, y=200)

  PlanEntry2.place(x=50, y=250)
  countingPlanEntry2.place(x=500, y=250)
  PlanEntryNum2.place(x=0, y=250)

  PlanEntry3.place(x=50, y=300)
  countingPlanEntry3.place(x=500, y=300)
  PlanEntryNum3.place(x=0, y=300)

  PlanEntry4.place(x=50, y=350)
  countingPlanEntry4.place(x=500, y=350)
  PlanEntryNum4.place(x=0, y=350)

  Check.place(x=700, y=150)

  CheckEntry.place(x=750, y=200)
  countingCheckEntry1.place(x=1200, y=200)
  CheckEntryNum.place(x=700, y=200)

  CheckEntry2.place(x=750, y=250)
  countingCheckEntry2.place(x=1200, y=250)
  CheckEntryNum2.place(x=700, y=250)

  CheckEntry3.place(x=750, y=300)
  countingCheckEntry3.place(x=1200, y=300)
  CheckEntryNum3.place(x=700, y=300)

  
  CheckEntry4.place(x=750, y=350)
  countingCheckEntry4.place(x=1200, y=350)
  CheckEntryNum4.place(x=700, y=350)

  WhatHappended.place(x=0, y=450)

  WhatHappendedEntry.place(x=50, y=500)
  countingWhatHappendedEntry1.place(x=500, y=500)
  WhatHappendedEntryNum.place(x=0, y=500)

  WhatHappendedEntry2.place(x=50, y=550)
  countingWhatHappendedEntry2.place(x=500, y=550)
  WhatHappendedEntryNum2.place(x=0, y=550)

  WhatHappendedEntry3.place(x=50, y=600)
  countingWhatHappendedEntry3.place(x=500, y=600)
  WhatHappendedEntryNum3.place(x=0, y=600)

  WhatHappendedEntry4.place(x=50, y=650)
  countingWhatHappendedEntry4.place(x=500, y=650)
  WhatHappendedEntryNum4.place(x=0, y=650)

  Fix.place(x=700, y=450)

  FixEntry.place(x=750, y=500)
  countingFixEntry1.place(x=1200, y=500)
  FixEntryNum.place(x=700, y=500)

  FixEntry2.place(x=750, y=550)
  countingFixEntry2.place(x=1200, y=550)
  FixEntryNum2.place(x=700, y=550)

  FixEntry3.place(x=750, y=600)
  countingFixEntry3.place(x=1200, y=600)
  FixEntryNum3.place(x=700, y=600)

  FixEntry4.place(x=750, y=650)
  countingFixEntry4.place(x=1200, y=650)
  FixEntryNum4.place(x=700, y=650)

  previewbutton.place(x=200, y=710)
  savebutton.place(x=430, y=710)
  Submit.place(x=120, y=405)
  Export.place(x=540, y=710)
  openAGENDA.place(x=720, y=710)
  newButton.place(x=810, y=710)
  photobutton.place(x=900, y=710)
  yourName.place(x=950, y=70)
  yourNameLabel.place(x=800, y=70)
  Date.place(x=950, y=0)
  DateLabel.place(x=800, y=0)

  window.mainloop()



titleAgenda = Tk()

titleAgenda.geometry("1530x900")
titleAgenda.iconphoto(False, PhotoImage(file="./images/AgendaIcon.png"))
titleAgenda.title("Start Your Agenda!")
titleAgenda.resizable(False, False)
titleAgenda.config(bg="black")
bg = PhotoImage(file = "./images/bg.png")
bgPic = Label(titleAgenda, image=bg).place(x=0, y=0)
photo = PhotoImage(file="./images/dsil_logo.png")
Agenda = Label(titleAgenda, font=("Consolas", 100), text="Agenda Application", bg="#222034", fg="white").pack()

sentence1 = Label(titleAgenda,text="Agenda is a great way to plan your works.", font=("Consolas", 30), bg="#222034", fg="white").pack()
sentence2 = Label(titleAgenda,text="You should use this Agenda App, It works and it's great!", font=("Consolas", 30), bg="#222034", fg="white").pack()
StartAgendaButton = Button(titleAgenda, font=("Consolas", 50), text="Start", command=startagenda).pack()
picture = Label(titleAgenda, image=photo).pack()
titleAgenda.mainloop()
shutil.rmtree("./temp")