from functools import partial
from msilib import Table
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
import conexiune
import tkinter as tk
from tkinter import ttk, END


class interfata():

    def __init__(self,root):
        self.connect = conexiune.c
        self.root = root
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title('Prison Management')
        self.login_window.geometry('1000x800')
        self.bg = ImageTk.PhotoImage(file="C:\\poze\\img.jpg")

        # Create a canvas
        self.canvas = tk.Canvas(self.login_window, width=400, height=300)
        self.canvas.pack(fill=tk.X)

        # Display image
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        # self.login_window.config(background='black')
        self.usernameLabel= tk.Label(self.login_window, text="User Name").pack(fill=tk.X, padx=5, pady=5)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self.login_window, textvariable=username).pack(fill=tk.X, padx=5, pady=5)

        # password label and password entry box
        passwordLabel = tk.Label(self.login_window, text="Password").pack(fill=tk.X, padx=5, pady=5)
        password = tk.StringVar()
        passwordEntry = tk.Entry(self.login_window, textvariable=password, show='*').pack(fill=tk.X, padx=5, pady=5)

        validateLogin = partial(self.validateLogin, username, password)

        # login button
        loginButton = tk.Button(self.login_window, text="Login", command=validateLogin).pack(fill=tk.X, padx=5, pady=5)



    def validateLogin(self, username, password):
        if( username.get()=='admin' and password.get()=='admin'):
            self.combo_optiuni()
        else:
            showinfo(
                title='Eroare',
                message=f'Parola sau username gresite'
            )

        print("username entered :", username.get())
        print("password entered :", password.get())
        return

    def optiune2(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title('Prison Management')
        self.login_window.geometry('600x500')

    def combo_inchisoare(self):
        self.label = ttk.Label(self.login_window,text="Selectati inchisoarea:")
        self.label.pack(fill=tk.X, padx=5, pady=5)
        self.inchisoare = tk.StringVar()
        self.inchisoare_cb = ttk.Combobox(self.login_window, textvariable=self.inchisoare)
        self.query = "SELECT denumire_inchisoare FROM inchisoare"
        self.connect.execute(self.query)
        self.result = self.connect.fetchall()
        self.inchisoare_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
        self.inchisoare_cb['state'] = 'readonly'
        self.inchisoare_cb.pack(fill=tk.X, padx=5, pady=5)
        self.inchisoare_cb.bind('<<ComboboxSelected>>', self.inchisoare_changed)

    def inchisoare_changed(self,event):
        showinfo(
                title='Result',
                message=f'You selected {self.inchisoare.get()}!'
            )
        self.login_window.destroy()
        self.root.deiconify()
        self.tabele()

        self.bg = ImageTk.PhotoImage(file="C:\\poze\\img.jpg")

        # Create a canvas
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack(fill="both", expand=True)

        # Display image
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas.create_text(500,400, text="MENIU",
                           font=("Times New Roman", 30))

    def optiune_changed(self,event):
        if (self.optiune.get() == 'Operatiuni pe inchisori existente'):
            self.combo_inchisoare()
        else:
            self.adaugareInchisoare()
    #          self.denumireLabel = tk.Label(self.login_window, text="Denumire inchisoare").pack(fill=tk.X, padx=5, pady=5)
    #         denumire = tk.StringVar()
    #         denumireEntry = tk.Entry(self.login_window, textvariable=denumire).pack(fill=tk.X, padx=5, pady=5)
    #
    #
    #         self.adresaLabel = tk.Label(self.login_window, text="Adresa").pack(fill=tk.X, padx=5, pady=5)
    #         adresa = tk.StringVar()
    #         adresaEntry = tk.Entry(self.login_window, textvariable=adresa).pack(fill=tk.X, padx=5, pady=5)
    #
    #         self.capacitateFLabel = tk.Label(self.login_window, text="Capacitate_F").pack(fill=tk.X, padx=5, pady=5)
    #         capacitate_F = tk.StringVar()
    #         capacitateFEntry = tk.Entry(self.login_window, textvariable=capacitate_F).pack(fill=tk.X, padx=5, pady=5)
    #
    #         self.capacitateMLabel = tk.Label(self.login_window, text="Capacitate_M").pack(fill=tk.X, padx=5, pady=5)
    #         capacitate_M = tk.StringVar()
    #         capacitateFEntry = tk.Entry(self.login_window, textvariable=capacitate_M).pack(fill=tk.X, padx=5, pady=5)
    #
    #         self.judetLabel = tk.Label(self.login_window, text="Judet").pack(fill=tk.X, padx=5, pady=5)
    #         self.judet = tk.StringVar()
    #         self.judet_cb = ttk.Combobox(self.login_window, textvariable=self.judet)
    #         self.result = ['Alba', 'Arad', 'Arges', 'Bacau', 'Bihor', 'Bistrita-Nasaud', 'Botosani', 'Brailla', 'Brasov', 'Bucuresti',
    # 'Buzau', 'Calarasi', 'Caras-Severin', 'Cluj', 'Constanta', 'Covasna', 'Dambovita', 'Dolj', 'Galati', 'Giurgiu', 'Gorj', 'Harghita',
    # 'Hunedoara', 'Ialomita', 'Iasi', 'Ilfov', 'Maramures', 'Mehedinti', 'Mures', 'Neamt', 'Olt', 'Prahova', 'Salaj', 'Satu Mare', 'Sibiu',
    # 'Suceava', 'Teleorman', 'Timis', 'Tulcea', 'Valcea', 'Vaslui', 'Vrancea']
    #         self.judet_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
    #         self.judet_cb['state'] = 'readonly'
    #         self.judet_cb.pack(fill=tk.X, padx=5, pady=5)

    def run_interface(self):
        self.root.mainloop()

    def combo_optiuni(self):
        self.label = ttk.Label(self.login_window,text="Selectati optiunea:")
        self.label.pack(fill=tk.X, padx=5, pady=5)
        self.optiune = tk.StringVar()
        self.optiune_cb = ttk.Combobox(self.login_window, textvariable=self.optiune)
        self.result=['Operatiuni pe inchisori existente', 'Adaugare inchisoare la baza de date']
        self.optiune_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
        self.optiune_cb['state'] = 'readonly'
        self.optiune_cb.pack(fill=tk.X, padx=5, pady=5)
        self.optiune_cb.bind('<<ComboboxSelected>>', self.optiune_changed)


    def tabele(self):
        self.root.title(f' {self.inchisoare.get()}')
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.sentinte_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.sentinte_menu = tk.Menu(self.menubar)
        self.sentinte_menu.add_command(label='Vizualizare', command=self.vizualizareSentinte)
        self.sentinte_menu.add_command(label='Adaugare', command=self.adaugareSentinte)
        self.sentinte_menu.add_command(label='Stergere', command=self.stergereSentinte)

        self.menubar.add_cascade(
            label="Sentinte",
            menu=self.sentinte_menu
        )

        self.prizonieri_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.prizonieri_menu = tk.Menu(self.menubar)
        self.prizonieri_menu.add_command(label='Vizualizare', command=self.vizualizarePrizonieri)
        self.prizonieri_menu.add_command(label='Adaugare', command=self.adaugarePrizonieri)
        self.prizonieri_menu.add_command(label='Stergere', command=self.stergerePrizonieri)

        self.menubar.add_cascade(
            label="Prizonieri",
            menu=self.prizonieri_menu
        )

        self.infractiuni_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )

        self.infractiuni_menu = tk.Menu(self.menubar)
        self.infractiuni_menu.add_command(label='Vizualizare', command=self.vizualizareInfractiuni)

        self.menubar.add_cascade(
            label="Infractiuni",
            menu=self.infractiuni_menu
        )

        self.inchisori_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.inchisori_menu = tk.Menu(self.menubar)
        self.inchisori_menu.add_command(label='Vizualizare', command=self.vizualizareInchisori)


        self.menubar.add_cascade(
            label="Inchisori",
            menu=self.inchisori_menu
        )

        self.paznici_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.paznici_menu = tk.Menu(self.menubar)
        self.paznici_menu.add_command(label='Vizualizare', command=self.vizualizarePaznici)


        self.menubar.add_cascade(
            label="Paznici",
            menu=self.paznici_menu
        )

        self.tura_paznici_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.tura_paznici_menu = tk.Menu(self.menubar)
        self.tura_paznici_menu.add_command(label='Vizualizare', command=self.vizualizareTureP)

        self.menubar.add_cascade(
            label="Tura Paznici",
            menu=self.tura_paznici_menu
        )

        self.celule_menu = tk.Menu(
            self.menubar,
            tearoff=0
        )
        self.celule_menu = tk.Menu(self.menubar)
        self.celule_menu.add_command(label='Vizualizare', command=self.vizualizareCelule)

        self.menubar.add_cascade(
            label="Celule",
            menu=self.celule_menu
        )
    def stergerePrizonieri(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Sterge prizonieri")
        self.filewin.geometry('1000x600')

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)

        self.Label1 = tk.Label(self.filewin, text="Introduceti numele pentru care doriti sa stergeti ").pack(fill='both', padx=0, pady=0)
        nume = tk.StringVar()
        # Entry1 = tk.Entry(self.filewin, textvariable=nume).pack(fill=tk.X, padx=5, pady=5)
        self.nume_cb = ttk.Combobox(self.filewin, textvariable=nume)
        self.querry="SELECT nume from prizonier"
        self.connect.execute(self.querry)
        self.result = self.connect.fetchall()
        self.nume_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
        self.nume_cb['state'] = 'readonly'
        self.nume_cb.pack(fill=tk.X, padx=5, pady=5)

        delete_prizonier = partial(self.delete_prizonier, nume)
        self.button = tk.Button(self.filewin, text="Sterge prizonier", command=delete_prizonier)
        self.button.pack(fill=tk.X, padx=0, pady=0)

    def delete_prizonier(self, nume):
        self.querry ="DELETE FROM prizonier WHERE nume='%s' " % (
            nume.get())
        self.connect.execute(self.querry)
        self.connect.execute('commit')
        showinfo(
            title='',
            message=f'Prizonier sters cu succes!'
        )
    def stergereSentinte(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Sterge sentinta")
        self.filewin.geometry('1000x600')

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)

        self.Label1 = tk.Label(self.filewin, text="Alegeti sentinta pe care doriti sa o stergeti ").pack(fill='both', padx=0, pady=0)
        id_sentinta = tk.StringVar()
        self.id_sentinta_cb = ttk.Combobox(self.filewin, textvariable=id_sentinta)
        self.query = "SELECT id_sentinta FROM sentinte"
        self.connect.execute(self.query)
        self.result = self.connect.fetchall()
        self.id_sentinta_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
        self.id_sentinta_cb['state'] = 'readonly'
        self.id_sentinta_cb.pack(fill=tk.X, padx=5, pady=5)

        delete_sentinta = partial(self.delete_sentinta, id_sentinta)
        self.button = tk.Button(self.filewin, text="Sterge sentinta", command=delete_sentinta)
        self.button.pack(fill=tk.X, padx=0, pady=0)

    def delete_sentinta(self, id_sentinta):
        self.querry ="DELETE FROM sentinte WHERE id_sentinta='%s' " % (
            id_sentinta.get())
        self.connect.execute(self.querry)
        self.connect.execute('commit')
        showinfo(
            title='',
            message=f'Sentinta stearsa cu succes!'
        )

    def adaugarePrizonieri(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Adauga prizonieri")
        self.filewin.geometry('1000x600')

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.frame = tk.Frame(self.filewin, width=800, height=2000)
        self.frame.pack(expand=True, fill='both')
        self.canvas = tk.Canvas(self.frame,  width=800, height=2000, scrollregion=(0, 0, 800, 2000))
        self.canvas.config(width=300, height=2000)
        self.canvas.pack(side='left', fill='both')



        self.Label1 = tk.Label(self.frame, text="ID Prizonier").pack( fill=tk.X,padx=0, pady=0)
        id_prizonier = tk.StringVar()
        Entry1 = tk.Entry(self.frame, textvariable=id_prizonier).pack( fill=tk.X,padx=5, pady=5)

        self.Label2 = tk.Label(self.frame, text="Sex").pack( fill=tk.X,padx=5, pady=5)
        sex = tk.StringVar()
        Entry2 = tk.Entry(self.frame, textvariable=sex).pack( fill=tk.X,padx=5, pady=5)

        self.Label3 = tk.Label(self.frame, text="nume").pack(fill=tk.X, padx=5, pady=5)
        nume = tk.StringVar()
        Entry3 = tk.Entry(self.frame, textvariable=nume).pack(fill=tk.X, padx=5, pady=5)

        self.Label4 = tk.Label(self.frame, text="prenume").pack(fill=tk.X, padx=5, pady=5)
        prenume= tk.StringVar()
        Entry4 = tk.Entry(self.frame, textvariable=prenume).pack(fill=tk.X, padx=5, pady=5)

        self.Label5 = tk.Label(self.frame, text="cnp").pack(fill=tk.X, padx=5, pady=5)
        cnp = tk.StringVar()
        Entry5 = tk.Entry(self.frame, textvariable=cnp).pack(fill=tk.X, padx=5, pady=5)

        self.Label6 = tk.Label(self.frame, text="adresa").pack(fill=tk.X, padx=5, pady=5)
        adresa = tk.StringVar()
        Entry6 = tk.Entry(self.frame, textvariable=adresa).pack(fill=tk.X, padx=5, pady=5)

        self.Label7 = tk.Label(self.frame, text="data_admitere").pack(fill=tk.X, padx=5, pady=5)
        data_admitere = tk.StringVar()
        Entry7 = tk.Entry(self.frame, textvariable=data_admitere).pack(fill=tk.X, padx=5, pady=5)

        self.Label8 = tk.Label(self.frame, text="data eliberarii initiale").pack(fill=tk.X, padx=5, pady=5)
        data_eliberarii_in = tk.StringVar()
        Entry8 = tk.Entry(self.frame, textvariable=data_eliberarii_in).pack(fill=tk.X, padx=5, pady=5)

        self.Label9 = tk.Label(self.canvas, text="data eliberarii finale").pack(fill=tk.X, padx=5, pady=5)
        data_eliberarii_fin = tk.StringVar()
        Entry9 = tk.Entry(self.canvas, textvariable=data_eliberarii_fin).pack(fill=tk.X, padx=5, pady=5)

        self.Label10 = tk.Label(self.canvas, text="eliberat").pack(fill=tk.X, padx=5, pady=5)
        eliberat = tk.StringVar()
        Entry10 = tk.Entry(self.canvas, textvariable=eliberat).pack(fill=tk.X, padx=5, pady=5)

        self.Label11 = tk.Label(self.canvas, text="scris_carte").pack(fill=tk.X, padx=5, pady=5)
        scris_carte = tk.StringVar()
        Entry11 = tk.Entry(self.canvas, textvariable=scris_carte).pack(fill=tk.X, padx=5, pady=5)

        self.Label12 = tk.Label(self.canvas, text="scris_carte").pack(fill=tk.X, padx=5, pady=5)
        munca_comunitate = tk.StringVar()
        Entry12 = tk.Entry(self.canvas, textvariable=scris_carte).pack(fill=tk.X, padx=5, pady=5)

        self.Label13 = tk.Label(self.canvas, text="violenta").pack(fill=tk.X, padx=5, pady=5)
        violenta = tk.StringVar()
        Entry13 = tk.Entry(self.canvas, textvariable=violenta).pack(fill=tk.X, padx=5, pady=5)

        self.Label14 = tk.Label(self.canvas, text="denumire_inchisoare").pack(fill=tk.X, padx=5, pady=5)
        denumire_inchisoare = tk.StringVar()
        Entry14 = tk.Entry(self.canvas, textvariable=denumire_inchisoare).pack(fill=tk.X, padx=5, pady=5)

        self.Label15 = tk.Label(self.canvas, text="id_celula").pack(fill=tk.X, padx=5, pady=5)
        id_celula = tk.StringVar()
        Entry15 = tk.Entry(self.canvas, textvariable=id_celula).pack(fill=tk.X, padx=5, pady=5)

        self.Label16 = tk.Label(self.canvas, text="id_sentinta").pack(fill=tk.X, padx=5, pady=5)
        id_sentinta = tk.StringVar()
        Entry16 = tk.Entry(self.canvas, textvariable=id_sentinta).pack(fill=tk.X, padx=5, pady=5)

        insert_prizonier = partial(self.insert_prizonier, id_prizonier, sex, nume, prenume, cnp, adresa, data_admitere, data_eliberarii_in, data_eliberarii_fin, eliberat, scris_carte, munca_comunitate, violenta, denumire_inchisoare, id_celula, id_sentinta)
        self.button = tk.Button(self.filewin, text="Adauga prizonier", command=insert_prizonier)
        self.button.pack(fill=tk.X, padx=0, pady=0)


    def insert_prizonier(self, id_prizonier, sex, nume, prenume, cnp, adresa, data_admitere, data_eliberarii_in, data_eliberarii_fin, eliberat, scris_carte, munca_comunitate, violenta, denumire_inchisoare, id_celula, id_sentinta):
        self.querry= "INSERT INTO prizonier(id_prizonier, sex, nume, prenume, cnp, adresa, data_admitere, data_eliberarii_in, data_eliberarii_fin, eliberat, scris_carte, munca_comunitate, violenta, inchisoare_denumire_inchisoare, celula_id_celula, sentinte_id_sentinta) VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s', '%s')" % (
            id_prizonier.get(), sex.get(), nume.get(), prenume.get(), cnp.get(), adresa.get(), data_admitere.get(), data_eliberarii_in.get(), data_eliberarii_fin.get(), eliberat.get(), scris_carte.get(), munca_comunitate.get(), violenta.get(), denumire_inchisoare.get(), id_celula.get(), id_sentinta.get())
        self.connect.execute(self.querry)
        self.connect.execute('commit')
        showinfo(
            title='',
            message=f'Prizonier adaugat cu succes!'
        )

    def adaugareSentinte(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Adauga sentinta")
        self.filewin.geometry('1000x600')
        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy,bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)

        self.Label1 = tk.Label(self.filewin, text="ID Sentinta").pack(fill=tk.X, padx=5, pady=5)
        id_sentinta = tk.StringVar()
        Entry1 = tk.Entry(self.filewin, textvariable=id_sentinta).pack(fill=tk.X, padx=5, pady=5)

        self.Label2 = tk.Label(self.filewin, text="Data_comitere").pack(fill=tk.X, padx=5, pady=5)
        data_comitere = tk.StringVar()
        Entry2 = tk.Entry(self.filewin, textvariable=data_comitere).pack(fill=tk.X, padx=5, pady=5)

        self.Label3 = tk.Label(self.filewin, text="Sentinta_initiala").pack(fill=tk.X, padx=5, pady=5)
        sentinta_initiala = tk.StringVar()
        Entry3 = tk.Entry(self.filewin, textvariable=sentinta_initiala).pack(fill=tk.X, padx=5, pady=5)

        self.Label4 = tk.Label(self.filewin, text="Minimizare sentinta:").pack(fill=tk.X, padx=5, pady=5)
        minimizare_sentinta= tk.StringVar()
        Entry4 = tk.Entry(self.filewin, textvariable=minimizare_sentinta).pack(fill=tk.X, padx=5, pady=5)

        self.Label5 = tk.Label(self.filewin, text="Sentinta finala").pack(fill=tk.X, padx=5, pady=5)
        sentinta_finala = tk.StringVar()
        Entry5 = tk.Entry(self.filewin, textvariable=sentinta_finala).pack(fill=tk.X, padx=5, pady=5)

        self.Label6 = tk.Label(self.filewin, text="Dovada incriminatoare").pack(fill=tk.X, padx=5, pady=5)
        dovada_incriminatoare = tk.StringVar()
        Entry6 = tk.Entry(self.filewin, textvariable=dovada_incriminatoare).pack(fill=tk.X, padx=5, pady=5)

        self.Label7 = tk.Label(self.filewin, text="Id_infractiune").pack(fill=tk.X, padx=5, pady=5)
        id_infractiune = tk.StringVar()
        Entry7 = tk.Entry(self.filewin, textvariable=id_infractiune).pack(fill=tk.X, padx=5, pady=5)

        self.Label8 = tk.Label(self.filewin, text="Cod gravitate").pack(fill=tk.X, padx=5, pady=5)
        cod_gravitate = tk.StringVar()
        Entry8 = tk.Entry(self.filewin, textvariable=cod_gravitate).pack(fill=tk.X, padx=5, pady=5)

        self.Label9 = tk.Label(self.filewin, text="CNP Prizonier").pack(fill=tk.X, padx=5, pady=5)
        cnp_prizonier = tk.StringVar()
        Entry9 = tk.Entry(self.filewin, textvariable=cnp_prizonier).pack(fill=tk.X, padx=5, pady=5)

        insert_sentinta = partial(self.insert_sentinta, id_sentinta, data_comitere, sentinta_initiala, minimizare_sentinta, sentinta_finala, dovada_incriminatoare, id_infractiune, cod_gravitate, cnp_prizonier)
        self.button = tk.Button(self.filewin, text="Adauga sentinta", command=insert_sentinta)
        self.button.pack(fill=tk.X, padx=0, pady=0)

    def insert_sentinta(self, id_sentinta, data_comitere, sentinta_initiala, minimizare_sentinta, sentinta_finala, dovada_incriminatoare, id_infractiune, cod_gravitate, cnp_prizonier):
        self.querry= "INSERT INTO sentinte(id_sentinta, data_comitere, sentinta_initiala, minimizare_sentinta, sentinta_finala, dovada_incriminatorie, infractiuni_id_infractiune, infractiuni_cod_gravitate, prizonier_cnp) VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            id_sentinta.get(), data_comitere.get(),  sentinta_initiala.get(), minimizare_sentinta.get(), sentinta_finala.get(), dovada_incriminatoare.get(), id_infractiune.get(), cod_gravitate.get(), cnp_prizonier.get())
        self.connect.execute(self.querry)
        self.connect.execute('commit')
        showinfo(
            title='',
            message=f'Sentinta adaugata cu succes!'
        )


    def adaugareInchisoare(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Adauga inchisoare")
        self.filewin.geometry('1000x600')
        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)

        self.denumireLabel = tk.Label(self.filewin, text="Denumire inchisoare").pack(fill=tk.X, padx=5, pady=5)
        denumire = tk.StringVar()
        denumireEntry = tk.Entry(self.filewin, textvariable=denumire).pack(fill=tk.X, padx=5, pady=5)

        self.adresaLabel = tk.Label(self.filewin, text="Adresa").pack(fill=tk.X, padx=5, pady=5)
        adresa = tk.StringVar()
        adresaEntry = tk.Entry(self.filewin, textvariable=adresa).pack(fill=tk.X, padx=5, pady=5)

        self.capacitateFLabel = tk.Label(self.filewin, text="Capacitate_F").pack(fill=tk.X, padx=5, pady=5)
        capacitate_F = tk.StringVar()
        capacitateFEntry = tk.Entry(self.filewin, textvariable=capacitate_F).pack(fill=tk.X, padx=5, pady=5)

        self.capacitateMLabel = tk.Label(self.filewin, text="Capacitate_M").pack(fill=tk.X, padx=5, pady=5)
        capacitate_M = tk.StringVar()
        capacitateFEntry = tk.Entry(self.filewin, textvariable=capacitate_M).pack(fill=tk.X, padx=5, pady=5)

        self.judetLabel = tk.Label(self.filewin, text="Judet").pack(fill=tk.X, padx=5, pady=5)
        judet = tk.StringVar()
        self.judet_cb = ttk.Combobox(self.filewin, textvariable=judet)
        self.result = ['Alba', 'Arad', 'Arges', 'Bacau', 'Bihor', 'Bistrita-Nasaud', 'Botosani', 'Brailla', 'Brasov',
                       'Bucuresti',
                       'Buzau', 'Calarasi', 'Caras-Severin', 'Cluj', 'Constanta', 'Covasna', 'Dambovita', 'Dolj',
                       'Galati', 'Giurgiu', 'Gorj', 'Harghita',
                       'Hunedoara', 'Ialomita', 'Iasi', 'Ilfov', 'Maramures', 'Mehedinti', 'Mures', 'Neamt', 'Olt',
                       'Prahova', 'Salaj', 'Satu Mare', 'Sibiu',
                       'Suceava', 'Teleorman', 'Timis', 'Tulcea', 'Valcea', 'Vaslui', 'Vrancea']
        self.judet_cb['values'] = [self.result[m] for m in range(0, len(self.result))]
        self.judet_cb['state'] = 'readonly'
        self.judet_cb.pack(fill=tk.X, padx=5, pady=5)


        insert = partial(self.insert_inchisoare,denumire, judet, adresa, capacitate_F, capacitate_M )
        self.button = tk.Button(self.filewin, text="Adauga inchisoare", command=insert)
        self.button.pack(fill=tk.X, padx=0, pady=0)


        # login button


    def insert_inchisoare(self, denumire, judet, adresa, capacitate_F, capacitate_M):
        self.querry= "INSERT INTO inchisoare(DENUMIRE_INCHISOARE, JUDET, ADRESA, CAPACITATE_F, CAPACITATE_M) VALUES('%s','%s', '%s', '%s', '%s')" % (
            denumire.get(), judet.get(),  adresa.get(), capacitate_F.get(), capacitate_M.get())
        self.connect.execute(self.querry)
        self.connect.execute('commit')
        showinfo(
            title='',
            message=f'Inchisoare adaugata cu succes!'
        )



    def vizualizareCelule(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Celule")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM celula"
        self.connect2 = self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()

        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("1", "2", "3", "4", "5")
        self.trv.column("1", width=30, anchor='c')
        self.trv.column("2", width=80, anchor='c')
        self.trv.column("3", width=30, anchor='c')
        self.trv.column("4", width=30, anchor='c')
        self.trv.column("5", width=30, anchor='c')
        self.trv.heading("1", text="ID_CELULA")
        self.trv.heading("2", text="F")
        self.trv.heading("3", text="M")
        self.trv.heading("4", text="CAPACITATE_CELULA")
        self.trv.heading("5", text="OCUPAT")

        for dt in self.result2:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

    def vizualizareTureP(self):
            self.filewin = tk.Toplevel(self.root)
            self.filewin.title("Ture Paznici")
            self.filewin.geometry('1000x600')
            self.query2 = "SELECT * FROM tura_paznic"
            self.connect2 = self.connect.execute(self.query2)
            self.result2 = self.connect.fetchall()

            self.total_rows = len(self.result2)
            self.total_columns = len(self.result2[0])


            self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
            self.exit_button.pack(fill=tk.X, padx=0, pady=0)
            self.trv = ttk.Treeview(self.filewin, selectmode='browse')
            self.trv.pack(fill='x')
            self.trv["columns"] = ("1", "2", "3", "4")
            self.trv.column("1", width=30, anchor='c')
            self.trv.column("2", width=80, anchor='c')
            self.trv.column("3", width=30, anchor='c')
            self.trv.column("4", width=30, anchor='c')
            self.trv.heading("1", text="ID_TURA")
            self.trv.heading("2", text="DATA_ORA_INCEPUT")
            self.trv.heading("3", text="DATA_ORA_FINAL")
            self.trv.heading("4", text="PAZNIC_ID_PAZNIC")

            for dt in self.result2:
                self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                                values=(dt[0], dt[1], dt[2], dt[3]))
    def vizualizarePaznici(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Paznici")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM paznic"
        self.connect2 = self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()

        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        self.trv.column("1", width=30, anchor='c')
        self.trv.column("2", width=80, anchor='c')
        self.trv.column("3", width=80, anchor='c')
        self.trv.column("4", width=80, anchor='c')

        self.trv.heading("1", text="ID_PAZNIC")
        self.trv.heading("2", text="RANG")
        self.trv.heading("3", text="NUME")
        self.trv.heading("4", text="PRENUME")
        self.trv.heading("5", text="DATA_ANG")
        self.trv.heading("6", text="DATA_NASTE")
        self.trv.heading("7", text="PENSIONAT")
        self.trv.heading("8", text="INCHISOARE_DENUMIRE_INCHISOARE")


        for dt in self.result2:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7]))

    def vizualizareInchisori(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Inchisori")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM inchisoare"
        self.connect2 = self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()

        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)

        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("0", "1", "2", "3", "4")
        self.trv.column("0", width=30, anchor='c')
        self.trv.column("1", width=80, anchor='c')
        self.trv.column("2", width=80, anchor='c')
        self.trv.column("3", width=80, anchor='c')
        self.trv.column("4", width=80, anchor='c')
        self.trv.heading("0", text="DENUMIRE_INCHISOARE")
        self.trv.heading("1", text="JUDET")
        self.trv.heading("2", text="ADRESA")
        self.trv.heading("3", text="CAPACITATE_F")
        self.trv.heading("4", text="CAPACITATE_M")

        for dt in self.result2:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

    def vizualizarePrizonieri(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Prizonieri")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM prizonier WHERE inchisoare_denumire_inchisoare = " + str(self.inchisoare.get()).replace('{','\'').replace('}','\'')
        
        self.connect2 = self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()

        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy, bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16")
        self.trv.column("1", width=30, anchor='c')
        self.trv.column("2", width=30, anchor='c')
        self.trv.column("3", width=30, anchor='c')
        self.trv.column("4", width=30, anchor='c')
        self.trv.column("5", width=30, anchor='c')
        self.trv.column("6", width=30, anchor='c')
        self.trv.column("7", width=30, anchor='c')
        self.trv.column("8", width=30, anchor='c')
        self.trv.column("9", width=30, anchor='c')
        self.trv.column("10", width=30, anchor='c')
        self.trv.column("11", width=30, anchor='c')
        self.trv.column("12", width=30, anchor='c')
        self.trv.column("13", width=30, anchor='c')
        self.trv.column("14", width=30, anchor='c')
        self.trv.column("15", width=30, anchor='c')
        self.trv.heading("1", text="ID_PRIZONIER")
        self.trv.heading("2", text="S")
        self.trv.heading("3", text="NUME")
        self.trv.heading("4", text="PRENUME")
        self.trv.heading("5", text="CNP")
        self.trv.heading("6", text="ADRESA")
        self.trv.heading("7", text="DATA_ADMITERE")
        self.trv.heading("8", text="DATA_ELIBERARE")
        self.trv.heading("9", text="DATA_ELIBERARII_FIN")
        self.trv.heading("10", text="ELIBERAT")
        self.trv.heading("11", text="SCRIS_CARTE")
        self.trv.heading("12", text="MUNCA_COMUNITATE")
        self.trv.heading("13", text="VIOLENTA")
        self.trv.heading("14", text="INCHISOARE_DENUMIRE_INCHISOARE")
        self.trv.heading("15", text="CELULA_ID_CELULA")
        self.trv.heading("16", text="SENTINTE_ID_SENTINTA")

        for dt in self.result2:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11], dt[12], dt[13], dt[14], dt[15]))

    def vizualizareInfractiuni(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Infractiuni")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM infractiuni"
        self.connect2 = self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()

        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit", command=self.filewin.destroy,bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("", "", "")
        self.trv.column("", width=30, anchor='c')
        self.trv.column("", width=80, anchor='c')
        self.trv.column("", width=80, anchor='c')

        self.trv.heading("", text="ID_INFRACTIUNE")
        self.trv.heading("", text="NUME_INFRACTIUNE")
        self.trv.heading("", text="COD_GRAVITATE")
        for dt in self.result2:
            self.trv.insert("", 'end', iid=dt[0], text=dt[0],
                       values=(dt[0], dt[1], dt[2]))

    def vizualizareSentinte(self):
        self.filewin = tk.Toplevel(self.root)
        self.filewin.title("Sentinte")
        self.filewin.geometry('1000x600')
        self.query2 = "SELECT * FROM sentinte"
        self.connect2=self.connect.execute(self.query2)
        self.result2 = self.connect.fetchall()


        self.total_rows = len(self.result2)
        self.total_columns = len(self.result2[0])

        self.exit_button = tk.Button(self.filewin, text="Exit",command=self.filewin.destroy,bg='red')
        self.exit_button.pack(fill=tk.X, padx=0, pady=0)
        self.trv = ttk.Treeview(self.filewin, selectmode='browse')
        self.trv.pack(fill='x')
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.trv.column("1", width=30, anchor='c')
        self.trv.column("2", width=80, anchor='c')
        self.trv.column("3", width=80, anchor='c')
        self.trv.column("4", width=80, anchor='c')
        self.trv.column("5", width=80, anchor='c')
        self.trv.heading("1", text="ID_SENTINTA")
        self.trv.heading("2", text="DATA_COMITERE")
        self.trv.heading("3", text="SENTINTA_INITIALA")
        self.trv.heading("4", text="MINIMIZARE_SENTINTA")
        self.trv.heading("5", text="SENTINTA_FINALA")
        self.trv.heading("6", text="DOVADA_INCRIMINATORIE")
        self.trv.heading("7", text="INFRACTIUNI_ID_INFRACTIUNE")
        self.trv.heading("8", text="INFRACTIUNI_COD_GRAVITATE")
        self.trv.heading("9", text="PRIZONIER_CNP")
        for dt in self.result2:
            self.trv.insert("", 'end',
                       values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6],dt[7], dt[8]))


















