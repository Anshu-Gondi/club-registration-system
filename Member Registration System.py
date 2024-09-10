from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

class Registration:

    def __init__(self, root):
        self.root = root
        self.root.title("Club Member Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="#2c3e50")

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Ref = StringVar()

        Membership = StringVar()
        Membership.set("0")

        #===========================Functions====================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Club Member Registration System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Club Member Registration System", "Confirm if you want to add a new record")
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0", END)
                return

        def Ref_No():
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END, "\t" + Ref.get() + "\t\t" + Firstname.get() + "\t\t" + Surname.get() +
                                   "\t\t" + Address.get() + "\t\t" + DateofOrder.get() + "\t\t" + Telephone.get()
                                   + "\t\t" + Membership.get() + "\n")

        def Membership_Fees():
            if (var4.get() == 1):
                self.txtMembership.configure(state=NORMAL)
                item = float(50)
                Membership.set("$" + str(item))
            elif (var4.get() == 0):
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")

        #===========================Frame====================================
        MainFrame = Frame(self.root, bg="#2c3e50")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=26, relief=RIDGE, bg="#34495e")
        TitleFrame.pack(side=TOP)

        self.IblTitle = Label(TitleFrame, font=('arial', 68, 'bold'), text=" Member Registration System ", padx=2, bg="#34495e", fg="white")
        self.IblTitle.grid()

        #===========================LowerFrame===============================
        MemberDetailsFrame = LabelFrame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE, bg="#34495e", fg="white")
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=880, height=400, relief=RIDGE, bg="#2c3e50", fg="white")
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=400, font=('arial', 12, 'bold'), text='Customer Name',
                                   relief=RIDGE, bg="#2c3e50", fg="white")
        MembersName_F.grid(row=0, column=0)

        Recipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=400, relief=RIDGE, bg="#2c3e50", fg="white")
        Recipt_ButtonFrame.pack(side=RIGHT)

        #===================================================================
        self.IblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference No", bd=7, bg="#2c3e50", fg="white")
        self.IblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Ref, bd=7, state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.IblFirstname = Label(MembersName_F, font=('arial', 14, 'bold'), text="First Name", bd=7, bg="#2c3e50", fg="white")
        self.IblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.IblSurname = Label(MembersName_F, font=('arial', 14, 'bold'), text="Surname", bd=7, bg="#2c3e50", fg="white")
        self.IblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2)
        self.txtSurname.grid(row=2, column=1)

        self.IblAddress = Label(MembersName_F, font=('arial', 14, 'bold'), text="Address", bd=7, bg="#2c3e50", fg="white")
        self.IblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Address, bd=7, insertwidth=2)
        self.txtAddress.grid(row=3, column=1)

        self.IblPostCode = Label(MembersName_F, font=('arial', 14, 'bold'), text="Post Code", bd=7, bg="#2c3e50", fg="white")
        self.IblPostCode.grid(row=4, column=0, sticky=W)
        self.txtPostCode = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Postcode, bd=7, insertwidth=2)
        self.txtPostCode.grid(row=4, column=1)

        self.IblTelephone = Label(MembersName_F, font=('arial', 14, 'bold'), text="Telephone", bd=7, bg="#2c3e50", fg="white")
        self.IblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Telephone, bd=7, insertwidth=2)
        self.txtTelephone.grid(row=5, column=1)

        self.IblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7, bg="#2c3e50", fg="white")
        self.IblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=DateofOrder, bd=7, insertwidth=2)
        self.txtDate.grid(row=6, column=1)

        #===========================Member Information========================================
        self.IblProve_of_ID = Label(MembersName_F, font=('arial', 14, 'bold'), text="Prove of ID", bd=7, bg="#2c3e50", fg="white")
        self.IblProve_of_ID.grid(row=7, column=0, sticky=W)

        self.cboProve_of_ID = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly', font=('arial', 14, 'bold'), width=19)
        self.cboProve_of_ID['value'] = ('', 'Pilot Licence', 'Driving Licence', 'Passport', 'Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.IblType_of_Member = Label(MembersName_F, font=('arial', 14, 'bold'), text="Type of Member", bd=7, bg="#2c3e50", fg="white")
        self.IblType_of_Member.grid(row=8, column=0, sticky=W)

        self.cboType_of_Member = ttk.Combobox(MembersName_F, textvariable=var2, state='readonly', font=('arial', 14, 'bold'), width=19)
        self.cboType_of_Member['value'] = ('', 'Full Member', 'Annual membership', 'Pay As You Go', 'Honary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8, column=1)

        self.IblMethod_of_Payment = Label(MembersName_F, font=('arial', 14, 'bold'), text="Method of Payment", bd=7, bg="#2c3e50", fg="white")
        self.IblMethod_of_Payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F, textvariable=var3, state='readonly', font=('arial', 14, 'bold'), width=19)
        self.cboMethod_of_Payment['value'] = ('', 'Visa Card', 'Master card', 'Debit Card', 'Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        #===========================Check button========================================
        self.chkMembership = Checkbutton(MembersName_F, text="Membership Fees", variable=var4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                                         command=Membership_Fees, bg="#2c3e50", fg="white")
        self.chkMembership.grid(row=10, column=0, sticky=W)

        self.txtMembership = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Membership, bd=7, insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10, column=1)

        #=============================Receipt=================================
        self.IblLabel = Label(Recipt_ButtonFrame, font=('arial', 10, 'bold'), pady=10, text="Member Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\t Member Paid", bd=7,
                              bg="#2c3e50", fg="white")
        self.IblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Recipt_ButtonFrame, font=('arial', 10, 'bold'), width=112, height=22, bg="#ecf0f1", fg="black")
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        #===========================Button========================================
        self.btnReceipt = Button(Recipt_ButtonFrame, padx=18, bd=7, font=('arial', 10, 'bold'), width=25, text="Receipt", command=Receipt, bg="#3498db", fg="white")
        self.btnReceipt.grid(row=2, column=0)
        self.btnReset = Button(Recipt_ButtonFrame, padx=18, bd=7, font=('arial', 10, 'bold'), width=25, text="Reset", command=iResetRecord, bg="#e74c3c", fg="white")
        self.btnReset.grid(row=2, column=1)
        self.btnExit = Button(Recipt_ButtonFrame, padx=18, bd=7, font=('arial', 10, 'bold'), width=25, text="Exit", command=iExit, bg="#2ecc71", fg="white")
        self.btnExit.grid(row=2, column=2)

if __name__ == '__main__':
    root = Tk()
    application = Registration(root)
    root.mainloop()
