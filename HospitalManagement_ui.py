from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import Tk_backend

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueAvailabilityError(Error):
   """Raised when the Invalid Availability is given"""
   pass

class ValueSpecializeError(Error):
   """Raised when the Invalid Availability is given"""
   pass

class ValueAgeError(Error):
   """Raised when the Invalid Age is given"""
   pass

class Hospital:
	def __init__(self,root):
		self.root = root
		self.root.title("Hospital Management System")
		self.root.iconbitmap("My_icon.ico")
		self.root.geometry("850x550+0+0")
		self.root.config(bg = "cadet blue")

		DoctorId = StringVar()
		Doctorfirstname = StringVar()
		Doctorsecondname = StringVar()
		DoctorSpecialization = StringVar()
		DoctorAvailability = StringVar()
		DoctorAge = StringVar()
		AvailabilityOption = ["\t\t\t\t\t\t\t\tNone\t\t\t\t\t\t\t\t\t","Morning","Evening","Night",]
		SpecializationOption = ["\t\t\t\t\t\t\t\tNone\t\t\t\t\t\t\t\t\t","Pediatrician","Gynecologist","Surgeon","Psychiatrist","Cardiologist","Dermatologist"]


		def clearAll():
			self.EntryLabelId.delete(0,END)
			self.EntryFirstName.delete(0,END)
			self.EntrySecondName.delete(0,END)
			DoctorSpecialization.set(SpecializationOption[0])
			DoctorAvailability.set(AvailabilityOption[0])
			self.EntryAge.delete(0,END)




		def addTolist():
				if (Doctorfirstname.get().isdigit() == True) and (Doctorsecondname.get().isdigit() == True):
					messagebox.showinfo("Error","Invalid Data Entry!!Please Enter valid Data")
				else:
					try:
						if DoctorAvailability.get() == AvailabilityOption[0]:
							raise ValueAvailabilityError
						elif DoctorSpecialization.get() == SpecializationOption[0]:
							raise ValueSpecializeError
						elif DoctorAge.get().isdigit() != True:
							raise ValueAgeError
						elif int(DoctorAge.get()) < 23:
							raise ValueAgeError
						elif int(DoctorAge.get()) > 65:
							raise ValueAgeError

						checkId = int(DoctorId.get())
						Tk_backend.AddDoctorDetails(DoctorId.get(),Doctorfirstname.get(),Doctorsecondname.get(), \
							DoctorSpecialization.get(),DoctorAvailability.get(),DoctorAge.get())
						RightList.delete(0,END)
						RightList.insert(END,(DoctorId.get(),Doctorfirstname.get(),Doctorsecondname.get(), \
							DoctorSpecialization.get(),DoctorAvailability.get(),DoctorAge.get()))
						clearAll()
					except sql.IntegrityError:
						messagebox.showinfo("Error","Already the ID exist!Please give another ID")
					except ValueError:
						messagebox.showinfo("Error","Invalid ID!!Please enter a valid ID")
					except ValueAvailabilityError:
						messagebox.showinfo("Error","Invalid Data!!Please enter a valid Availability")
					except ValueSpecializeError:
						messagebox.showinfo("Error","Invalid Data!!Please enter a valid Specialization")
					except ValueAgeError:
						messagebox.showinfo("Error","Invalid Data!!Please enter a valid Age")


		def DisplayList():
			RightList.delete(0,END)
			DocListdata = Tk_backend.DisplayingDoctorDetails()
			for record in DocListdata:
				RightList.insert(END,record)

		def LoadListInfo(event):
			global sd
			searchList = RightList.curselection()[0]
			sd = RightList.get(searchList)
			self.EntryLabelId.delete(0,END)
			self.EntryLabelId.insert(END,sd[0])
			self.EntryFirstName.delete(0,END)
			self.EntryFirstName.insert(END,sd[1])
			self.EntrySecondName.delete(0,END)
			self.EntrySecondName.insert(END,sd[2])
			for Option in SpecializationOption:
				if Option == sd[3]:
					DoctorSpecialization.set(Option)
					break
			for Option in AvailabilityOption:
				if Option == sd[4]:
					DoctorAvailability.set(Option)
					break
			self.EntryAge.delete(0,END)
			self.EntryAge.insert(END,sd[5])


		def UpdatetoList():
			if sd[0] != DoctorId.get():
				messagebox.showinfo("Error","You can't edit the Doctor ID Number!! Please check Remove the Old ID and Re-enter")
			else:
				Tk_backend.UpdateDoctorDetails(DoctorId.get(),Doctorfirstname.get(),Doctorsecondname.get(), \
					DoctorSpecialization.get(),DoctorAvailability.get(),DoctorAge.get())
				RightList.delete(0,END)
				RightList.insert(END,(DoctorId.get(),Doctorfirstname.get(),Doctorsecondname.get(), \
					DoctorSpecialization.get(),DoctorAvailability.get(),DoctorAge.get()))
				clearAll()
				messagebox.showinfo("Confirmation","Successfully Updated")

		def deleteList():
			Tk_backend.DeleteDoctorDetails(sd[0])
			RightList.delete(0,END)
			clearAll()
			DisplayList()

		def doExist():
			answer = messagebox.askyesnocancel("Exist","Do you want to cancel")
			if (answer):
				self.root.quit()


		#def _show_value(v, *pargs):
		#	print(type(v.get()))


		###############################Frame###################################################
		MainFrame = Frame(self.root, bg = "cadet blue")
		MainFrame.grid()

		Headerframe = Frame(MainFrame, bd = 2, padx = 54, pady = 8, bg = "Ghost White" ,relief = RIDGE)
		Headerframe.pack(side = TOP)

		self.Heading = Label(Headerframe, font = ("Times", "44", "bold italic") , text = "Hospital Management System",bg = "Ghost White")
		self.Heading.grid()

		ButtonFrame = Frame(MainFrame,bd = 5, width = 1150 , height = 70 ,bg = "Ghost White", padx = 18, pady = 10)
		ButtonFrame.pack(side =BOTTOM)


		DataFrame = Frame(MainFrame,width = 1000, height = 500, padx = 5, pady = 5,bg = "cadet blue",relief = RIDGE) 
		DataFrame.pack(side = BOTTOM)

		EntryLeftFrame = LabelFrame(DataFrame,font = ("Helvetica", "20", "bold"), text = "Doctor Entry",bd = 10,width = 700, height = 650, padx = 2,pady = 5)
		EntryLeftFrame.pack(side = LEFT)
		#self.LeftHeading = Label(EntryLeftFrame,font = ("Times", "20", "bold italic"), text = "Data Entry",pady = 5)
		#self.LeftHeading.grid()

		EntryRightFrame = LabelFrame(DataFrame,font = ("Serif", "15", "bold"), text = "Details",width = 600, height = 550,bd = 5, padx = 2, pady = 5,bg = "Ghost White",)
		EntryRightFrame.pack(side = RIGHT)

		###################################Entry Widgets & Labels#######################################

		self.LabelId = Label(EntryLeftFrame,font = ("arial", "15"),text = "ID", padx = 5, pady = 5)
		self.LabelId.grid(row = 0, column = 0, sticky = W)
		self.EntryLabelId = Entry(EntryLeftFrame,textvariable = DoctorId, width = 50)
		self.EntryLabelId.grid(row = 0, column = 1)

		self.LabelfirstName = Label(EntryLeftFrame,font = ("arial", "15"),text = "First Name", padx = 5, pady = 5)
		self.LabelfirstName.grid(row = 1, column = 0, sticky = W)
		self.EntryFirstName = Entry(EntryLeftFrame,textvariable = Doctorfirstname, width = 50)
		self.EntryFirstName.grid(row = 1, column = 1)

		self.LabelSecondName = Label(EntryLeftFrame,font = ("arial", "15"),text = "Second Name", padx = 5, pady = 5)
		self.LabelSecondName.grid(row = 2, column = 0, sticky = W)
		self.EntrySecondName = Entry(EntryLeftFrame,textvariable = Doctorsecondname, width = 50)
		self.EntrySecondName.grid(row = 2, column = 1)

		self.LabelSpecialization = Label(EntryLeftFrame,font = ("arial", "15"),text = "Specialization", padx = 5, pady = 5)
		self.LabelSpecialization.grid(row = 3, column = 0, sticky = W)
		DoctorSpecialization.set(SpecializationOption[0])
		self.DropSpecialization = OptionMenu(EntryLeftFrame,DoctorSpecialization,*SpecializationOption)
		self.DropSpecialization.config(width = 44,padx = 5, pady = 5)
		self.DropSpecialization.grid(row = 3, column = 1)

		self.LabelAvailability = Label(EntryLeftFrame,font = ("arial", "15"),text = "Availability", padx = 5, pady = 5)
		self.LabelAvailability.grid(row = 4, column = 0, sticky = W)
		DoctorAvailability.set(AvailabilityOption[0])
		self.DropAvailability = OptionMenu(EntryLeftFrame,DoctorAvailability, *AvailabilityOption)
		self.DropAvailability.config(width = 44,padx = 5, pady = 5)
		self.DropAvailability.grid(row = 4, column = 1)

		self.LabelAge = Label(EntryLeftFrame,font = ("arial", "15"),text = "Age", padx = 5, pady = 5)
		self.LabelAge.grid(row = 5, column = 0, sticky = W)

		self.EntryAge = Entry(EntryLeftFrame,textvariable = DoctorAge, width = 50)
		self.EntryAge.grid(row = 5, column = 1)

		##################################Side Bar and Display box#########################################
		
		RightScroll = Scrollbar(EntryRightFrame)
		RightScroll.grid(row = 0, column = 1, sticky = "ns") 

		RightList = Listbox(EntryRightFrame, font = ("arial", "11", "bold italic"),height = 15,width = 40,yscrollcommand = RightScroll.set)
		RightList.grid(row = 0, column = 0)
		RightList.bind('<<ListboxSelect>>',LoadListInfo)
		RightScroll.config(command = RightList.yview)

		##############################Button Widget#########################################################

		AddButton = Button(ButtonFrame, text = "Add", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2,command = addTolist)
		AddButton.grid(row = 0,column = 0)

		deleteButton = Button(ButtonFrame, text = "Delete", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2, command = clearAll)
		deleteButton.grid(row = 0,column = 1)

		updateButton = Button(ButtonFrame, text = "Update", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2, command = UpdatetoList)
		updateButton.grid(row = 0,column = 2)

		displayButton = Button(ButtonFrame, text = "Display", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2, command = DisplayList)
		displayButton.grid(row = 0,column = 3)

		exitButton = Button(ButtonFrame, text = "Exit", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2, command = doExist)
		exitButton.grid(row = 0,column = 4)

		deletePerButton = Button(ButtonFrame, text = "Remove", height = 2, font = ("arial", "10","bold"), width = 10, padx = 10, pady = 2, command = deleteList)
		deletePerButton.grid(row = 0,column = 5)


		


if __name__ =="__main__":
	root = Tk()
	Application = Hospital(root)
	root.mainloop()

