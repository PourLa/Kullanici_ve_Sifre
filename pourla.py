import  sys
import sqlite3
from PyQt5 import  QtWidgets,QtGui


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")


        baglanti.commit()

    def init_ui(self):

        etiket1 = QtWidgets.QLabel (self)
        etiket1.setText ("Kullanıcı Adı:")
        etiket1.move (15,5)

        etiket2 = QtWidgets.QLabel (self)
        etiket2.setText ("Şifre:")
        etiket2.move (15,60)

        self.kullanici_adi =  QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("Lütfen Kullanıcı Adı ve Şifreyi Giriniz!")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()

        v_box.addWidget(self.kullanici_adi)
        v_box.addStretch()
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addLayout(v_box)


        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)

        self.resize (270,200)

        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)


app = QtWidgets.QApplication(sys.argv)

app_icon = QtGui.QIcon("TürkHackTeam_Logo.png")
app.setWindowIcon(app_icon)
pencere = Pencere()
pencere.setWindowTitle("PourLa")


sys.exit(app.exec_())
