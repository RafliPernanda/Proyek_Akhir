# Import modul tambahan
from prettytable import PrettyTable
import pwinput
import sys

# Data pengguna dan pendaftaran
pengguna = [] #List berisi [username, password] Pengguna
pendaftaran = {}
pengguna_login = None
credit = ("Muhammad Rafli Pernanda", "Fariz Muwaffaq", "Elfin Sinaga")

akunAdmin = [["admin", "admin"]]  # List berisi [username, password] admin

# Daftar Lomba
DaftarLomba = ["Beumbaan Vol. 1", "Belarian Hambat"] 

# Registrasi pengguna baru
def registrasi_pengguna():
    global pengguna
    print("=== Registrasi Pengguna Baru ===")
    while True:
        try:
            nama_pengguna = str(input("Masukkan nama pengguna: "))

        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            return registrasi_pengguna
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            return registrasi_pengguna

        if not all(char.isalpha() or char.isspace() for char in nama_pengguna):
            print("Nama pengguna hanya boleh terdiri dari huruf dan spasi.")
            continue
        if len(nama_pengguna.strip()) < 3:  # Strip untuk menghindari spasi kosong
            print("Nama pengguna harus terdiri dari minimal 3 huruf.")
            continue

        # Memastikan username belum digunakan
        for user in pengguna:
            if user["username"] == nama_pengguna:
                print("Nama pengguna sudah terdaftar, silakan gunakan nama lain.")
                return
        try:
            kata_sandi = pwinput.pwinput("Masukkan kata sandi: ")

        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            return registrasi_pengguna
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            return registrasi_pengguna
        
        # Menambahkan pengguna baru ke dalam list
        pengguna.append({"username": nama_pengguna, "kata_sandi": kata_sandi, "role": "pengguna"})
        
        print(f"Registrasi pengguna dengan username {nama_pengguna} berhasil! Silahkan Login.")
        return menu_utama
    
def logout():
    print("Terima kasih telah menggunakan program ini.")
    print(f"Program ini dibuat oleh {credit[0]}, {credit[1]}, dan {credit[2]}.")
    sys.exit()

def login_pengguna():
    global pengguna_login
    Kesempatan = 0
    while True:
        if len(pengguna) == 0:
            print("Belum ada pengguna yang terdaftar. Silakan registrasi terlebih dahulu.")
            return False
        Kesempatan += 1
        if Kesempatan > 3:
            print("Anda Telah Melakukan Kesalahan Sebanyak 3 Kali, Silahkan Mengulang Dari Menu Utama")
            menu_utama()
        else:
            try:
                input_username = input("Masukkan nama pengguna: ")
                input_pw = pwinput.pwinput("Masukkan kata sandi: ")
            except KeyboardInterrupt:
                print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
                logout()
            except EOFError:
                print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
                logout()
            except TypeError:
                print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
                return login_pengguna
            except ValueError:
                print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
                return login_pengguna
            

        for user in pengguna:
            if user["username"] == input_username and user["kata_sandi"] == input_pw:
                pengguna_login = user
                print(f"Login Berhasil, Selamat datang {input_username}!")
                return True
            else:
                print("Nama pengguna atau kata sandi salah, silahkan coba lagi.")

def login_admin():
    global pengguna_login
    try:
        input_username = input("Masukkan username admin: ")
        input_pw = pwinput.pwinput("Masukkan kata sandi admin: ")

    except KeyboardInterrupt:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except EOFError:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except TypeError:
        print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
        return login_admin
    except ValueError:
        print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
        return login_admin

    for admin in akunAdmin:
        if admin[0] == input_username and admin[1] == input_pw:
            pengguna_login = {"username": admin[0], "role": "admin"}
            print("Login Berhasil, Selamat Datang Admin!")
            menu_admin()
        else:
            print("Username atau kata sandi admin salah.")
    return False

    
#Menampilkan List Perlombaan
def Perlombaan():
    for ListLomba in DaftarLomba:
        print(f"- {ListLomba}")

# Pilih lomba dan kategori
def MenuLomba():
    print("==================================")
    print("Pilih Lomba yang Ingin Diikuti:")
    LihatLomba()  #Menampilkan Lomba Yang Tersedia
    print("==================================")
    
    try:
        PilihLomba = int(input("Masukkan nomor lomba yang ingin diikuti: "))
        if 1 <= PilihLomba <= len(DaftarLomba):
            Lomba = DaftarLomba[PilihLomba - 1]  #Memilih Lomba
        else:
            print("Pilihan Yang Anda Masukkan Salah! Silahkan Coba Lagi.")
            return MenuLomba()
    except KeyboardInterrupt:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except EOFError:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except TypeError:
        print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
        MenuLomba()
    except ValueError:
        print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
        MenuLomba()

    kategoriLari()
    try:
        PilihKategori = input("Pilih Kategori Lomba : ")
    except KeyboardInterrupt:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except EOFError:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except TypeError:
        print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
        kategoriLari()
    except ValueError:
        print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
        kategoriLari()
    if PilihKategori == "1":
        Kategori = "5km"
    elif PilihKategori == "2":
        Kategori = "10km"
    elif PilihKategori == "3":
        Kategori = "Full Marathon"
    else:
        print("Pilihan Yang Anda Masukkan Salah! Silahkan Coba Lagi")
        MenuLomba()
    
    return Lomba, Kategori

def kategoriLari():
    tkategori = PrettyTable()
    tkategori.field_names = ["No.", "Kategori Lari"]
    tkategori.add_row(["1.", "5K"])
    tkategori.add_row(["2.", "10K"])
    tkategori.add_row(["3.", "Full Marathon"])
    print(tkategori)

#Mendaftar Lomba
def MendaftarLomba(username):
    global pendaftaran
    if len(DaftarLomba) == 0:
        print("Belum Ada Pendaftaran Yang Dibuka Pada Saat Ini")
    else:
        if cek_pendaftaran(username):
            print("Anda Hanya Dapat Mendaftar 1 Lomba Pada 1 Waktu!")
        else:
            Lomba, Kategori = MenuLomba()
            pendaftaran[username] = {"Lomba": Lomba, "Kategori": Kategori}
            print(f"Anda Telah Berhasil Mendaftar Lomba {pendaftaran[username]['Lomba']} Dengan Kategori {pendaftaran[username]['Kategori']}.")

# Mengecek apakah pengguna sudah mendaftar lomba 
def cek_pendaftaran(username):
    global pendaftaran
    return username in pendaftaran

#Mengedit Pendaftaran
def EditPendaftaran(username):
    global pendaftaran
    if cek_pendaftaran(username):
        Lomba, Kategori = MenuLomba()
        pendaftaran[username] = {"Lomba": Lomba, "Kategori": Kategori}
        print(f"Berhasil Mengubah Lomba Menjadi {Lomba} Dengan Kategori {Kategori}.")
    else:
        print("Anda Belum Mendaftar Perlombaan.")
        
#Membatalkan Pendaftaran
def BatalPendaftaran(username):
    global pendaftaran
    if cek_pendaftaran(username):
        del pendaftaran[username]
        print("Pendaftaran Berhasil Dibatalkan.")
    else:
        print("Anda Belum Mendaftar Perlombaan")

#Menambahkan Lomba
def TambahLomba():
    try:
        LombaBaru = str(input("Masukkan Nama Lomba Baru : "))
    except KeyboardInterrupt:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except EOFError:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except TypeError:
        print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
        TambahLomba()
    except ValueError:
        print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
        TambahLomba()
    
    if LombaBaru in DaftarLomba:
        print("Lomba Sudah Ada, Silahkan Memasukkan Lomba Baru")
        return TambahLomba()
    else:
        DaftarLomba.append(LombaBaru)
        print("Lomba Berhasil Ditambahkan")
        LihatLomba()

#Melihat Perlombaan Untuk Admin
def LihatLomba():
    if len(DaftarLomba) == 0:
        print("Belum Ada Lomba Yang Ditambahkan")
    else:
        TabelLomba = PrettyTable()
        TabelLomba.field_names = ["No.", "Nama Lomba"]
        for i, lomba in enumerate(DaftarLomba, 1):
            TabelLomba.add_row([i, lomba])
        print(TabelLomba)
        

def tampilkan_akun():
    print("\n--- Akun yang Terdaftar ---")
    TabelAkun = PrettyTable()
    TabelAkun.field_names = ["No.", "Nama Pengguna"]
    
    if pengguna:
        for i, user in enumerate(pengguna, 1):
            TabelAkun.add_row([i, user['username']])
        print(TabelAkun)
    else:
        print("Belum ada akun yang terdaftar.")

def tampilkan_data_pendaftaran():
    print("\n--- Data Pendaftaran Lari ---")
    TabelPendaftaran = PrettyTable()
    TabelPendaftaran.field_names = ["Nama Peserta", "Lomba", "Kategori"]
    
    if pendaftaran:
        for username, data in pendaftaran.items():
            TabelPendaftaran.add_row([username, data['Lomba'], data['Kategori']])
        print(TabelPendaftaran)
    else:
        print("Belum ada data pendaftaran.")
        
#Mengambil Data Dan Kategori Lomba 
def DataLomba(username):
    if username in pendaftaran:
        data = pendaftaran[username]
        return f"Anda Terdaftar Pada Perlombaan {data['Lomba']} Dengan Kategori {data['Kategori']}."
    else:
        return
    
# Menghapus Perlombaan
def HapusLomba():
    if len(DaftarLomba) == 0:
        print("Belum Ada Lomba Yang Ditambahkan")
    else:
        print("Daftar Perlombaan yang Tersedia:")
        for i, lomba in enumerate(DaftarLomba, 1):
            print(f"{i}. {lomba}")
        try:
            HapusData = int(input("Masukkan nomor lomba yang ingin dihapus: "))
            if 1 <= HapusData <= len(DaftarLomba):
                lomba_dihapus = DaftarLomba.pop(HapusData - 1)
                print(f"Lomba '{lomba_dihapus}' berhasil dihapus.")
                
                # Menghapus pendaftaran yang terkait dengan lomba yang dihapus
                for username in list(pendaftaran.keys()):
                    if pendaftaran[username]['Lomba'] == lomba_dihapus:
                        del pendaftaran[username]
                        print(f"Pendaftaran pengguna '{username}' untuk lomba '{lomba_dihapus}' telah dihapus.")
            else:
                print("Nomor lomba tidak valid. Silakan coba lagi.")
        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            HapusLomba()
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            HapusLomba()
        
#Melihat Pendaftaran    
def LihatPendaftaran(username):
    if cek_pendaftaran(username):
        print(DataLomba(username))
    else:
        print("Anda Belum Mendaftar Lomba.")
    
# Fungsi untuk menu admin
def menu_admin():
    while True:
        print("""\033[1;31;48m
 __    __     ______     __   __     __  __          
/\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \         
\ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \        
 \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\       
  \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/       
                                                     
 ______     _____     __    __     __     __   __    
/\  __ \   /\  __-.  /\ "-./  \   /\ \   /\ "-.\ \   
\ \  __ \  \ \ \/\ \ \ \ \-./\ \  \ \ \  \ \ \-.  \  
 \ \_\ \_\  \ \____-  \ \_\ \ \_\  \ \_\  \ \_\\"\_\ 
  \/_/\/_/   \/____/   \/_/  \/_/   \/_/   \/_/ \/_/ 
                                                     
\033[1;37;48m""")
        try:
            tmenu_admin = PrettyTable()
            tmenu_admin.field_names = ["No.", "Menu Admin"]
            tmenu_admin.add_row(["1.", "Tampilkan Akun Terdaftar"])
            tmenu_admin.add_row(["2.", "Tampilkan Data Pendaftaran"])
            tmenu_admin.add_row(["3.", "Tambahkan Lomba"])
            tmenu_admin.add_row(["4.", "Menghapus Lomba"])
            tmenu_admin.add_row(["5.", "Lihat Lomba"])
            tmenu_admin.add_row(["6.", "Kembali ke Menu Utama"])
            print(tmenu_admin)
            pilihan_admin = input("Pilih Menu: ")
        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            return menu_admin
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            return menu_admin
        if pilihan_admin == "1":
            tampilkan_akun()
        elif pilihan_admin == "2":
            tampilkan_data_pendaftaran()
        elif pilihan_admin == "3":
            TambahLomba()
        elif pilihan_admin == "4":
            HapusLomba()
        elif pilihan_admin == "5":
            LihatLomba()
        elif pilihan_admin == "6":
            menu_utama()
        else:
            print("Pilihan tidak valid, Masukkan angka 1/2/3/4/5/6")
            
def menu_pengguna():
    while True:
        print("""\033[1;31;48m
                    __    __     ______     __   __     __  __                                             
                    /\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \                                            
                    \ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \                                           
                    \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\                                          
                    \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/                                          
                                                                                        
 ______   ______     __   __     ______     ______     __  __     __   __     ______    
/\  == \ /\  ___\   /\ "-.\ \   /\  ___\   /\  ___\   /\ \/\ \   /\ "-.\ \   /\  __ \   
\ \  _-/ \ \  __\   \ \ \-.  \  \ \ \__ \  \ \ \__ \  \ \ \_\ \  \ \ \-.  \  \ \  __ \  
 \ \_\    \ \_____\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_____\  \ \_\\"\_\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_/\/_/ 
                                                                                        
\033[1;37;48m""")
        try:
            tmenu_user = PrettyTable()
            tmenu_user.field_names = ["No.", "Menu Pengguna"]
            tmenu_user.add_row(["1.", "Daftar Marathon"])
            tmenu_user.add_row(["2.", "Lihat Pendaftaran"])
            tmenu_user.add_row(["3.", "Edit Pendaftaram"])
            tmenu_user.add_row(["4.", "Batalkan Pendaftaran"])
            tmenu_user.add_row(["5.", "Keluar"])
            print(tmenu_user)

            PilihMenuPengguna = input("Pilih Menu : ")
            if PilihMenuPengguna == "1":
                MendaftarLomba(pengguna_login['username'])
            elif PilihMenuPengguna == "2":
                LihatPendaftaran(pengguna_login['username'])
            elif PilihMenuPengguna == "3":
                EditPendaftaran(pengguna_login['username'])
            elif PilihMenuPengguna == "4":
                BatalPendaftaran(pengguna_login['username'])
            elif PilihMenuPengguna == "5":
                break
            else:
                print("Pilihan tidak valid, Masukkan angka 1/2/3/4/5.")
        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            return menu_pengguna
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            return menu_pengguna

# Fungsi untuk login
def login():
    global pengguna_login
    print("Pilih jenis login:")
    print("1. Login sebagai Pengguna")
    print("2. Login sebagai Admin")
    try: 
        pilihan_login = int(input("Pilih (1/2): "))
    except KeyboardInterrupt:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except EOFError:
        print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
        logout()
    except TypeError:
        print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
        login()
    except ValueError:
        print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
        login()

    if pilihan_login == 1:
        login_pengguna()
    elif pilihan_login == 2:
        login_admin()
    else:
        print("Pilihan tidak valid, Masukkan angka 1/2")
        return login
    
def menu_utama(): 
    while True:
        print("""\033[1;31;48m
  ___ ___ _  _ ___   _   ___ _____ _   ___    _   _  _   _      _   ___ ___ 
 | _ \ __| \| |   \ /_\ | __|_   _/_\ | _ \  /_\ | \| | | |    /_\ | _ \_ _|
 |  _/ _|| .` | |) / _ \| _|  | |/ _ \|   / / _ \| .` | | |__ / _ \|   /| | 
 |_| |___|_|\_|___/_/ \_\_|   |_/_/ \_\_|_\/_/ \_\_|\_| |____/_/ \_\_|_\___|

                |  \/  | /_\ | _ \  /_\_   _| || |/ _ \| \| |                              
                | |\/| |/ _ \|   / / _ \| | | __ | (_) | .` |                              
                |_|  |_/_/ \_\_|_\/_/ \_\_| |_||_|\___/|_|\_|                              
\033[1;37;48m""")
        tmenu_utama = PrettyTable()
        tmenu_utama.field_names = ["No. ","Menu Utama"]
        tmenu_utama.add_row(["1.", "Registrasi"])
        tmenu_utama.add_row(["2.", "Login"])
        tmenu_utama.add_row(["3.", "Keluar"])
        print(tmenu_utama)

        try:
            pilihan = int(input("Pilih Menu : "))
            if pilihan == 1:
                registrasi_pengguna()
            elif pilihan == 2:
                login()
                if pengguna_login['role'] == "admin":
                        menu_admin()
                elif pengguna_login['role'] == "pengguna":    
                    menu_pengguna()
            elif pilihan == 3:
                logout()
            else:
                print("Pilihan tidak valid, silahkan masukkan angka 1/2/3.")
        except KeyboardInterrupt:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except EOFError:
            print("Terdapat Kesalahan saat Anda menginput, Anda akan keluar dari program")
            logout()
        except TypeError:
            print("Terdapat Kesalahan saat Anda menginput, silahkan coba lagi")
            continue
        except ValueError:
            print("Terdapat kesalahan saat Anda menginput, silahkan coba lagi")
            continue
        
# Program utama
# while True:
menu_utama()