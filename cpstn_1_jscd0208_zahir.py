import os

# Data dummy perpustakaan
list_buku = [{
                'No ID' : '120', 'Judul' : 'Vagabond', 'Genre' : 'Historical Fiction', 'Penulis' : 'Takehiko Inoe', 'Stok' : '25'
        },
        {
                'No ID' : '121', 'Judul' : 'Rich Dad Poor Dad', 'Genre' : 'Financial', 'Penulis' : 'Robert Kiyosaki', 'Stok' : '20'
        },
        {
                'No ID' : '122', 'Judul' : 'Bumi Manusia', 'Genre' : 'Drama History', 'Penulis' : 'Pramoedya C Ananta Toer', 'Stok' : '63'
        },
        {
                'No ID' : '123', 'Judul' : 'A Song Of Ice And Fire', 'Genre' : 'Epic Fantasy', 'Penulis' : 'George R. R. Martin','Stok' : '24'
        },
        {
                'No ID' : '124', 'Judul' : 'Why The Rich Are Getting Richer', 'Genre' : 'Financial', 'Penulis' : 'Robert Kiyosaki', 'Stok' : '15'
        },
        {
                'No ID' : '125', 'Judul' : 'Haikyu!!', 'Genre' : 'Sports', 'Penulis' : 'Haruichi Furudate', 'Stok' : '30'
        },
        {
                'No ID' : '126', 'Judul' : 'Monster', 'Genre' : 'Mysteri', 'Penulis' : 'Naoki Urasawa', 'Stok' : '25'
        },
        {
                'No ID' : '127', 'Judul' : '20th Century Boys', 'Genre' : 'Action, Mysteri', 'Penulis' : 'Naoki Urasawa', 'Stok' : '30'
        },
        {
                'No ID' : '128', 'Judul' : 'Kingdom', 'Genre' : 'History', 'Penulis' : 'Yasuhisa Hara', 'Stok' : '16'
        },
        {
                'No ID' : '129', 'Judul' : 'The 7 Habits Of Highly Effective People', 'Genre' : 'Self Improvement', 'Penulis' : 'Stephen Covey', 'Stok' : '25'
        },
        {
                'No ID' : '130', 'Judul' : 'The Way Of Walking Alone', 'Genre' : 'Self Improvement', 'Penulis' : 'Miyamoto Musashi', 'Stok' : '5'
        }]

# Data dummy peminjam buku
list_peminjam = [{'Nama Peminjam' : 'Zahir Ilham', 'Alamat Peminjam' : 'Jl. Asia Afrika No.99', 'No Telp' : '081324664645', 'Judul' : 'Vagabond'}]


# fungsi untuk menampilkan tabel daftar peminjam buku
def tabel2(listPeminjam):
        print("=================================================== List Buku =================================================== \n".center(121))
        print(f"| {'Nama Peminjam':^25} | {'Alamat Peminjam':^40} | {'No Telp':^12} | {'Judul':^30} |")
        print("-"*120)
        for peminjam in listPeminjam:
                Nama = peminjam['Nama Peminjam']
                Alamat = peminjam['Alamat Peminjam']
                NoTelp= peminjam['No Telp']
                judul_Buku_Pinjam = peminjam['Judul']
                print(f'| {Nama:<26}|{Alamat:<42}|{NoTelp:<14}|{judul_Buku_Pinjam:<32}|')

# fungsi untuk menampilkan tabel daftar buku
def tabel(booklist):
        print("=================================================== Data Peminjam =================================================== \n".center(121))
        print(f"| {'No ID':3^} | {'Judul':^40} | {'Genre':^28} | {'Penulis':^28} | {'Stok':^5}|")
        print("-"*121)
        for buku in booklist:
                noID = buku['No ID']
                Judul = buku['Judul']
                Genre = buku['Genre']
                Penulis = buku['Penulis']
                Stok = buku['Stok']
                print(f'| {noID:^6}|{Judul:<42}|{Genre:<30}|{Penulis:<30}|{Stok:^6}|')

# fungsi filter 
def filter_ID(id_buku):
    list_ID = [ buku['No ID'] for buku in list_buku]
    if id_buku in list_ID:
            tabel([buku for buku in list_buku if buku['No ID'] == id_buku])
    else:
            print('No ID Tidak Tersedia')
    return id_buku
def filter_Judul(judulBuku):
    list_judul = [ buku['Judul'] for buku in list_buku]
    if judulBuku in list_judul:
            os.system("cls")
            tabel([buku for buku in list_buku if buku['Judul'] == judulBuku])
    else:
            print('Judul Tidak Tersedia')
    return judulBuku
def filter_Penulis(penulisBuku):
    list_Penulis = [ buku['Penulis'] for buku in list_buku]
    if penulisBuku in list_Penulis:
            os.system("cls")
            tabel([buku for buku in list_buku if buku['Penulis'] == penulisBuku])
    else:
            print('Penulis Tidak Tersedia')
    return penulisBuku
def filter_Genre(genreBuku):
    list_Genre = [ buku['Genre'] for buku in list_buku]
    if genreBuku in list_Genre:
            os.system("cls")
            tabel([buku for buku in list_buku if buku['Genre'] == genreBuku])
    else:
            print('Genre Tidak Tersedia')
    return genreBuku

# fungsi ubah stok buku
def ubah_stok(judul_buku_stok):
    for buku in list_buku:
        if buku['Judul']==judul_buku_stok:
            os.system("cls")
            filter_Judul(judul_buku_stok)
            editStok= input('Edit Stok : ')
            if editStok.isdigit():
                    os.system("cls")
                    buku['Stok']=editStok
                    filter_Judul(judul_buku_stok)
            else:
                    os.system("cls")
                    print('Stok harus berupa angka')
    return judul_buku_stok 

# fungsi untuk menginput data peminjam buku
def data_peminjam():
        namaPeminjam = input('Masukkan Nama anda : ').title()
        Alamat = input('Masukkan Alamat anda : ').title()
        NoTelp= input('Masukkan No Telp anda : ')
        if NoTelp.isdigit() and len(NoTelp) >= 10 and len(NoTelp) <=12 and NoTelp[0]=='0' and NoTelp[1]== '8':
                judul_Buku_Pinjam = input("Masukkan Judul Buku yang dipinjam: ").title()
                filter_Judul(judul_Buku_Pinjam)
                checkout= input("Apakah Anda Yakin Ingin meminjam Buku Tersebut (Y/N) : ").lower()
                if checkout == 'y':
                        os.system("cls")
                        for buku in list_buku:
                                if buku['Judul']==judul_Buku_Pinjam :
                                        buku['Stok']=str(int(buku['Stok'])-1)
                                        filter_Judul(judul_Buku_Pinjam )
                                        peminjam= [{'Nama Peminjam' : namaPeminjam, 'Alamat Peminjam' : Alamat, 'No Telp' : NoTelp, 'Judul' : judul_Buku_Pinjam}]
                                        list_peminjam.extend(peminjam)
                                        tabel2(peminjam)

                elif checkout == 'n':
                        os.system("cls")
                        print('Anda akan dialihkan ke Menu Sebelumnya')
                else:
                        os.system("cls")
                        print('Menu yang anda pilih salah')
        else:
                os.system("cls")
                print('Nomor telepon harus terdiri dari 10-12 digit angka dan berisi 08 pada 2 digit pertama')

# fungsi untuk mencari buku
def cari():
        while True:
                pilihan_menu_cari = input("""\n Silakan Pilih Menu\n\n
                        1. Cari Berdasarkan No ID\n
                        2. Cari Berdasarkan Judul\n
                        3. Cari Berdasarkan Genre\n
                        4. Cari Berdasarkan Penulis\n    
                        5. Kembali Ke Menu Sebelumnya\n                         
                        Pilihan Menu : """)
                if pilihan_menu_cari == '1':
                        os.system("cls")
                        input_ID = input("Masukkan ID Buku: ")
                        filter_ID(input_ID )
                elif pilihan_menu_cari == '2':
                        os.system("cls")
                        inputJudul = input("Masukkan Judul Buku: ").title()
                        filter_Judul(inputJudul)
                elif pilihan_menu_cari == '3':
                        os.system("cls")
                        genreBuku = input("Masukkan Genre Buku: ").title()
                        filter_Genre(genreBuku)
                elif pilihan_menu_cari == '4':
                        os.system("cls")
                        inputPenulis= input("Masukkan Penulis Buku: ").title()
                        filter_Penulis(inputPenulis)
                elif pilihan_menu_cari == '5':
                        os.system("cls")
                        break
                else:
                        os.system("cls")
                        print('Pilihan Menu Tidak Tersedia')

# fungsi untuk menu create
def create_():
        while True:
                print('\n')
                print('MY LIBRARY'.center(85))
                print('-'*85)
                print("\n\nSilakan Pilih Menu\n".center(85))
                pilihan_menu_create = input("""
                1. Menambah Data Buku Baru
                2. Kembali ke Menu Utama
                Pilihan Menu : """)
                list_ID = [ buku['No ID'] for buku in list_buku]
                list_judul = [ buku['Judul'] for buku in list_buku]
                if pilihan_menu_create == '1':
                        os.system("cls")
                        id_baru=input("Masukkan ID Baru : ")
                        if id_baru.isdigit():
                                while id_baru in list_ID:
                                        print('ID Sudah tersedia, Silakan masukkan ID Lain')
                                        id_baru=input("Masukkan ID Baru : ")
                                        os.system("cls")
                                if id_baru not in list_ID:
                                        judul_buku=input("Masukkan Judul : ").title()
                                        if judul_buku in list_judul:
                                                konfirmasi_judul=input('Buku sudah terdaftar, ingin tambah stok(Y/N)? ')
                                                if konfirmasi_judul=='y':
                                                        os.system("cls")
                                                        ubah_stok(judul_buku)
                                                else:
                                                        print('Anda akan dialihkan ke menu sebelumnya')
                                                        break
                                        else:        
                                                genre=input("Masukkan Genre : ").title()
                                                penulis=input("Masukkan Penulis : ").title()
                                                stok=input("Masukkan Stok : ")
                                                if stok.isdigit():
                                                        data_buku_baru = [{'No ID' : id_baru, 
                                                                'Judul' : judul_buku, 
                                                                'Genre' : genre, 
                                                                'Penulis' : penulis,
                                                                'Stok' : stok}]
                                                        tabel(data_buku_baru)
                                                        Is_Done = input("Simpan data ini (Y/N) :").lower()
                                                        if Is_Done == 'y':
                                                                os.system("cls")
                                                                list_buku.extend(data_buku_baru)
                                                                print("Data Berhasil disimpan")
                                                                tabel(list_buku)
                                                        elif Is_Done == 'n':
                                                                print("Anda akan dialihkan ke Menu Create")
                                                        else:
                                                                os.system("cls")
                                                                print("Inputan yang anda masukkan tidak sesuai, Data Otomatis Tersimpan")
                                                                list_buku.extend(data_buku_baru)
                                                                tabel(list_buku)
                                                else:
                                                        print('Stok harus berupa angka')
                        else:
                                print('ID harus berupa angka')
                elif pilihan_menu_create == '2':
                        os.system("cls")
                        break
                else:
                        print("Pilih menu yang tersedia !!!!")

# fungsi untuk menu ubah data berdasarkan id                        
def ubah_data():
        idBuku = input("Masukkan ID Buku untuk merubah data: ")
        list_ID = [buku['No ID'] for buku in list_buku]
        if idBuku in list_ID:
                filter_ID(idBuku)
                Ubah_Data= input("Apakah Anda Yakin Ingin Merubah Data Buku Tersebut (Y/N) : ").lower()
                if Ubah_Data == 'y':
                        os.system("cls")
                        for buku in list_buku:
                                if buku['No ID']==idBuku:
                                        filter_ID(idBuku)
                                        GantiJudul=input('Ingin Mengubah Judul (Y/N)? ').lower()
                                        if GantiJudul == 'y':
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Judul']= input('Edit Judul : ').title()
                                        else :
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Judul']= buku['Judul']
                                        GantiGenre=input('Ingin Mengubah Genre (Y/N)? ').lower()
                                        if GantiGenre == 'y':
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Genre']= input('Edit Genre : ').title()
                                        else :
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Genre']= buku['Genre']
                                        GantiPenulis=input('Ingin Mengubah Penulis (Y/N)? ').lower()
                                        if GantiPenulis == 'y':
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Penulis']= input('Edit Penulis : ').title()
                                        else :
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Penulis']= buku['Penulis']
                                        GantiStok=input('Ingin Mengubah Stok (Y/N)? ').lower()
                                        if GantiStok == 'y':
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                ubahStok= input('Edit Stok : ')
                                                if ubahStok.isdigit():
                                                        os.system("cls")
                                                        buku['Stok']=ubahStok
                                                        filter_ID(idBuku)
                                                else:
                                                        print('Stok harus berupa angka')
                                        else :
                                                os.system("cls")
                                                filter_ID(idBuku)
                                                buku['Stok']= buku['Stok']      
                elif Ubah_Data == 'n':
                        os.system("cls")
                        print('Anda akan dialihkan ke Menu Update')
                else:
                        os.system("cls")
                        print('Menu yang anda pilih salah')                       
        elif idBuku not in list_ID:
                os.system("cls")
                print('ID tidak tersedia !!!')

# funsgi untuk menu hapus
def hapus():
        id_Buku = input("Masukkan ID Buku untuk menghapus data: ")
        list_ID = [buku['No ID'] for buku in list_buku]
        if id_Buku not in list_ID:
                os.system("cls")
                print('Data buku tidak tersedia !!!')
        elif id_Buku in list_ID:
                os.system("cls")
                filter_ID(id_Buku)
                hapus_Data= input("Apakah Anda Yakin Ingin Menghapus Data Buku Tersebut (Y/N) : ").lower()
                if hapus_Data == 'y':
                        os.system("cls")
                        indexToDelete = None
                        for index,buku in enumerate (list_buku):
                                if buku['No ID'] == id_Buku:
                                    indexToDelete = index
                                    del list_buku[indexToDelete]
                                    tabel(list_buku)
                                    break       
                elif hapus_Data == 'n':
                        os.system("cls")
                        print('Data tidak jadi dihapus')
                else :
                        print('Masukkan inputan yang sesuai')                             

# funsgi untuk menu read
def Read_():
        while True:
                print('\n')
                print('MY LIBRARY'.center(85))
                print('-'*85)
                print("\n\nSilakan Pilih Menu\n".center(85))
                pilihan_menu_read = input("""
                1. Melihat semua data buku yang tersedia
                2. Cari Buku
                3. Kembali ke Menu Utama
                Pilihan Menu : """)
                if pilihan_menu_read == '1':
                        if len(list_buku)!=0:
                                os.system("cls")
                                tabel(list_buku)
                        else:
                                os.system("cls")
                                print('Data tidak tersedia')
                elif pilihan_menu_read == '2':
                        os.system("cls")
                        cari()
                elif pilihan_menu_read == '3':
                        os.system("cls")
                        break
                else:
                        print("Pilih menu yang tersedia !!!!")

# fungsi untuk menu update
def Update_():
        while True:
                print('\n')
                print('MY LIBRARY'.center(85))
                print('-'*85)
                print("\nSilakan Pilih Menu\n".center(85))
                pilihan_menu_update = input("""
                1. Update Data
                2. Kembali ke Menu Utama
                Pilihan Menu : """)
                if pilihan_menu_update == '1':
                        os.system("cls")
                        ubah_data()                     
                elif pilihan_menu_update == '2':
                        os.system("cls")
                        break
                else:
                        os.system("cls")
                        print("Pilih menu yang tersedia !!!!")  

# fungsi untuk menu delete
def Delete_():
        while True:
                print('\n')
                print('MY LIBRARY'.center(85))
                print('-'*85)
                print("\nSilakan Pilih Menu".center(85))
                pilihan_menu_Delete = input("""
                1. Delete Data Menurut No ID
                2. Hapus Seluruh Data
                3. Kembali ke Menu Utama
                Pilihan Menu : """)
                if pilihan_menu_Delete == '1':
                        os.system("cls")
                        hapus()                     
                elif pilihan_menu_Delete == '2':
                        os.system("cls")
                        confirmasi_hapus = input("Apakah anda yakin ingin menghapus seluruh data(Y/N)? ").lower()
                        if confirmasi_hapus == 'y':
                                os.system("cls")
                                password = input("Masukkan Password : ")
                                list_password = ["admin1", "admin2", "admin3"]
                                if password not in list_password:
                                        os.system("cls")
                                        print("Password yang anda masukkan salah !!!")
                                elif password in list_password:
                                        os.system("cls")
                                        list_buku.clear()
                                        tabel(list_buku)
                        elif confirmasi_hapus == 'n':
                                os.system("cls")
                        else:
                                print("Masukkan perintah yang benar")
                elif pilihan_menu_Delete == '3':
                        os.system("cls")
                        break      
                else:
                        print("Pilih menu yang tersedia !!!!")     

# fungsi menu peminjam
def menu_peminjam():
        while True:
                print('\n')
                print('MY LIBRARY'.center(125))
                print("="*125)
                print("\nSilakan Pilih Menu\n".center(85))
                pilihan_menu_peminjam = input("""
                1. Melihat semua data buku yang tersedia\n
                2. Cari Buku\n
                3. Pinjam Buku\n
                4. Keluar dari menu\n
                Pilihan Menu : """)
                if pilihan_menu_peminjam == '1':
                        os.system("cls")
                        tabel(list_buku)
                elif pilihan_menu_peminjam == '2':
                        os.system("cls")
                        cari()
                elif pilihan_menu_peminjam == '3':
                        os.system("cls")
                        data_peminjam()  
                elif pilihan_menu_peminjam == '4':
                        os.system("cls")
                        break
                else:
                        os.system("cls")
                        print("Pilih menu yang tersedia !!!!")

# fungsi menu utama                        
def Home():
        while True:
                print('\n')
                print('WELCOME TO MY LIBRARY'.center(125))
                print("="*125)
                print("""
                                                1. Lihat Daftar Buku Tersedia\n
                                                2. Lihat Daftar Peminjam Buku\n
                                                3. Menambahkan Daftar Buku\n
                                                4. Update Data Buku\n
                                                5. Menghapus Data Buku\n
                                                6. Kembali ke Menu Login
                                                                                        """)
                print("="*125)
                Pilihan_Menu_Home = input("\nSilakan pilih menu : ")
                if Pilihan_Menu_Home == '1':
                        os.system("cls")
                        Read_()
                elif Pilihan_Menu_Home == '2':
                        os.system("cls")
                        tabel2(list_peminjam)
                elif Pilihan_Menu_Home == '3':
                        os.system("cls")
                        create_()
                elif Pilihan_Menu_Home == '4':
                        os.system("cls")
                        Update_()
                elif Pilihan_Menu_Home == '5':
                        os.system("cls")
                        Delete_()    
                elif Pilihan_Menu_Home == '6':
                        os.system("cls")
                        break      
                else :
                        os.system("cls")
                        print("Inputan yang anda masukkan tidak sesuai")

# fungsi menu login
def menu_login():
        os.system("cls")
        while True:
                print('MY LIBRARY LOGIN'.center(125))
                print("="*125)
                print("""
                                                1. Masuk sebagai admin\n
                                                2. Masuk sebagai peminjam buku\n
                                                3. Keluar dari sistem
                                                                       """)
                print("="*125)
                Pilihan_Menu_Login = input("\nSilakan pilih menu :")
                list_password = ["admin1", "admin2", "admin3"]
                if Pilihan_Menu_Login == '1':
                        os.system("cls")
                        password = input("Masukkan Password : ")
                        if password not in list_password:
                                os.system("cls")
                                print("Password yang anda masukkan salah !!!")
                        elif password in list_password:
                                os.system("cls")
                                Home()
                elif Pilihan_Menu_Login == '2':
                        os.system("cls")
                        menu_peminjam()
                elif Pilihan_Menu_Login == '3':
                        logout = input("Apakah anda yakin akan keluar(Y/N) ? ").lower()
                        if logout == 'y':
                                os.system("cls")
                                password = input("Masukkan Password : ")
                                if password not in list_password:
                                        os.system("cls")
                                        print("Password yang anda masukkan salah !!!")
                                elif password in list_password:
                                        os.system("cls")
                                        print(f'{"=====================================================Keluar Dari My Library=====================================================":^50}')
                                        break
                        else :
                                os.system("cls")
                else:
                        os.system("cls")
                        print("Pilihan yang anda masukkan tidak sesuai")
menu_login()                  

