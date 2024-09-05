import tkinter as tk
import tkinter.ttk as ttk
import sv_ttk

class Taschenrechner:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Taschenrechner")
        self.root.geometry("300x400")
        self.center_window()
        self.create_widgets()

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=10)

    def create_widgets(self):
        self.setup_frame()
        self.setup_topBar()
        self.setup_bottombar()

    def setup_frame(self):
        self.frameAnzeige = ttk.Frame(self.root)
        self.frameAnzeige.grid(column=0, row=0, sticky="nsew")
        self.frameButtons = ttk.Frame(self.root)
        self.frameButtons.grid(column=0, row=1, sticky="nsew")

        self.frameAnzeige.rowconfigure(0, weight=1)
        self.frameAnzeige.columnconfigure(0, weight=1)
    
    def setup_topBar(self):
        # register()-Methode ist Tkinter Funktion, die eine Python Funktion(self.validate_input() in ein
        # Form verwandelt, die Tkinter intern verwenden kann
        vcmd = (self.root.register(self.validate_input), '%P')

        # Entry - Wann validieren, nach jedem Tastendruck 
        self.entryResult = ttk.Entry(self.frameAnzeige , validate='key', validatecommand=vcmd, justify=tk.RIGHT, font=("Helvetica", 24), state="enabled")
        self.entryResult.grid(row=0, column=0, pady=(10,5), padx=5, sticky="nsew")
        self.entryResult.focus()

        # Alternativ über Label, falls keine Eingabe erlaubt
        # self.labelResult = ttk.Label(self.frameAnzeige, text="Warte auf Eingabe", font=("Helvetica", 20), anchor="center")
        # self.labelResult.grid(row=0, column=0, sticky="nsew")

    def setup_bottombar(self):
        self.buttonsRechnen = {
            # Zahlen
            "EinsButton": ttk.Button(self.frameButtons, text="1", width=2, command=lambda:self.button_click("1")),
            "ZweiButton": ttk.Button(self.frameButtons, text="2", width=2, command=lambda:self.button_click("2")),
            "DreiButton": ttk.Button(self.frameButtons, text="3", width=2, command=lambda:self.button_click("3")),
            "VierButton": ttk.Button(self.frameButtons, text="4", width=2, command=lambda:self.button_click("4")),
            "FünfButton": ttk.Button(self.frameButtons, text="5", width=2, command=lambda:self.button_click("5")),
            "SechsButton": ttk.Button(self.frameButtons, text="6", width=2, command=lambda:self.button_click("6")),
            "SiebenButton": ttk.Button(self.frameButtons, text="7", width=2, command=lambda:self.button_click("7")),
            "AchtButton": ttk.Button(self.frameButtons, text="8", width=2, command=lambda:self.button_click("8")),
            "NeunButton": ttk.Button(self.frameButtons, text="9", width=2, command=lambda:self.button_click("9")),
            "NullButton": ttk.Button(self.frameButtons, text="0", width=2, command=lambda:self.button_click("0")),
            # Standardoperationen
            "PlusButton": ttk.Button(self.frameButtons, text="+", width=2, command=lambda:self.button_click("+")),
            "KommaButton": ttk.Button(self.frameButtons, text=".", width=2, command=lambda:self.button_click(".")),
            "MinusButton": ttk.Button(self.frameButtons, text="-", width=2, command=lambda:self.button_click("-")),
            "MalButton": ttk.Button(self.frameButtons, text="*", width=2, command=lambda:self.button_click("*")),
            "GeteiltButton": ttk.Button(self.frameButtons, text="/", width=2, command=lambda:self.button_click("/")),
            "ProzentButton": ttk.Button(self.frameButtons, text="%", width=2, command=lambda:self.button_click("%")),
            "ErgebnisButton": ttk.Button(self.frameButtons, text="=", width=2, command=lambda: self.ergebnis_berechnen()),
            # Zusätzliche mathematische Operationen
            "SinusButton": ttk.Button(self.frameButtons, text="sin", width=2),
            "CosinusButton": ttk.Button(self.frameButtons, text="cos", width=2),
            "TangensButton": ttk.Button(self.frameButtons, text="tan", width=2),
            "LogarithmusButton": ttk.Button(self.frameButtons, text="log", width=2),
            "PiButton": ttk.Button(self.frameButtons, text="pi", width=2),
            "WurzelButton": ttk.Button(self.frameButtons, text="sqrt", width=2),
            "PowerButton": ttk.Button(self.frameButtons, text="pow", width=2),
            "ModuloButton": ttk.Button(self.frameButtons, text="mod", width=2),
            # Spezielle Funktionen
            "KlammerAufButton": ttk.Button(self.frameButtons, text="(", width=2),
            "KlammerZuButton": ttk.Button(self.frameButtons, text=")", width=2),
            "DeleteButton": ttk.Button(self.frameButtons, text="DEL", width=2, command=lambda: self.delete_entry()),
            "DeleteAllButton": ttk.Button(self.frameButtons, text="AC", width=2, command=lambda: self.delete_all_entry())
        }
        # 1. Reihe
        self.buttonsRechnen["DeleteAllButton"].grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["DeleteButton"].grid(row=0, column=1, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["ProzentButton"].grid(row=0, column=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["GeteiltButton"].grid(row=0, column=3, sticky="nsew", pady=5, padx=5)
        # 2. Reihe
        self.buttonsRechnen["SiebenButton"].grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["AchtButton"].grid(row=1, column=1, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["NeunButton"].grid(row=1, column=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["MalButton"].grid(row=1, column=3, sticky="nsew", pady=5, padx=5)
        # 3. Reihe
        self.buttonsRechnen["VierButton"].grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["FünfButton"].grid(row=2, column=1, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["SechsButton"].grid(row=2, column=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["MinusButton"].grid(row=2, column=3, sticky="nsew", pady=5, padx=5)
        # 4. Reihe
        self.buttonsRechnen["EinsButton"].grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["ZweiButton"].grid(row=3, column=1, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["DreiButton"].grid(row=3, column=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["PlusButton"].grid(row=3, column=3, sticky="nsew", pady=5, padx=5)
        # 5. Reihe
        self.buttonsRechnen["NullButton"].grid(row=4, column=0, columnspan=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["KommaButton"].grid(row=4, column=2, sticky="nsew", pady=5, padx=5)
        self.buttonsRechnen["ErgebnisButton"].grid(row=4, column=3, sticky="nsew", pady=5, padx=5)

        for row in range(5):
            self.frameButtons.rowconfigure(row, weight=1)
        for col in range(4):
            self.frameButtons.columnconfigure(col, weight=1)

    def validate_input(self, new_value):
        if new_value == "":
            return True
        if len(new_value) > 14:
            return False
    
        allowedChars = "0123456789.+-*/()%"
        for char in new_value:
            if char not in allowedChars:
                return False
        return True

    def ergebnis_berechnen(self):
        try:
            entryText = self.entryResult.get()
            print(eval(entryText))
            result = eval(entryText)

            self.entryResult.delete(0, tk.END)
            self.entryResult.insert(0, str(result))
        except Exception as e:
            self.entryResult.delete(0, tk.END)
            self.entryResult.insert(0, e)
        
    def delete_entry(self):
        entryText = self.entryResult.get()
        self.entryResult.delete(len(entryText)-1,tk.END)

    def delete_all_entry(self):
        entryText = self.entryResult.get()
        self.entryResult.delete(0, tk.END)

    def button_click(self,text):    
        self.entryResult.insert(tk.END, text) #tk.END Konstante und Ende eines Widgets
        self.entryResult.focus()

    def center_window(self):
        #Erzwingt die Aktualisierung aller ausstehenden Ereignisse
        self.root.update_idletasks()

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        windowWidth = self.root.winfo_width()
        windowHeight = self.root.winfo_height()

        x_cordinate = int((screenWidth//2) - (windowWidth/2))
        y_cordinate = int((screenHeight/2) - (windowHeight/2))

        self.root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_cordinate, y_cordinate))

if __name__ == "__main__":
    root = tk.Tk()
    rechner = Taschenrechner(root)
    sv_ttk.set_theme("dark")
    root.mainloop()