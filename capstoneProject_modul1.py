dataPegawai = [
    {'idPegawai' : '17001', 'Nama Pegawai' : 'Bobi Ratubi',
      'Divisi' : 'Marketing', 'Jabatan' : 'Staff', 
      'Domisili' : 'Jakarta', 'Tempat Lahir' : 'Semarang', 'Usia' : '25 Tahun', 'Pendidikan Terakhir' : 'S1'},
       {'idPegawai' : '17002', 'Nama Pegawai' : 'Andi Putra',
      'Divisi' : 'Sales', 'Jabatan' : 'Manajer', 
      'Domisili' : 'Bogor', 'Tempat Lahir' : 'Surabaya', 'Usia' : '35 Tahun', 'Pendidikan Terakhir' : 'S2'},
       {'idPegawai' : '17003', 'Nama Pegawai' : 'Indra Harnanto',
      'Divisi' : 'Finance', 'Jabatan' : 'Senior Analyst', 
      'Domisili' : 'Bekasi', 'Tempat Lahir' : 'Jambi', 'Usia' : '29 Tahun', 'Pendidikan Terakhir' : 'S1'},
       {'idPegawai' : '17004', 'Nama Pegawai' : 'Rudi Hermawan',
      'Divisi' : 'Sales', 'Jabatan' : 'Staff', 
      'Domisili' : 'Tangerang', 'Tempat Lahir' : 'Jakarta', 'Usia' : '27 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17005', 'Nama Pegawai' : 'Helmy Susanto',
      'Divisi' : 'Marketing', 'Jabatan' : 'Staff', 
      'Domisili' : 'Bogor', 'Tempat Lahir' : 'Bogor', 'Usia' : '24 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17006', 'Nama Pegawai' : 'Adit Kharisma',
      'Divisi' : 'Finance', 'Jabatan' : 'Junior Analyst', 
      'Domisili' : 'Jakarta', 'Tempat Lahir' : 'Solo', 'Usia' : '22 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17007', 'Nama Pegawai' : 'Sintiya Halifa',
      'Divisi' : 'Sales', 'Jabatan' : 'Staff', 
      'Domisili' : 'Bekasi', 'Tempat Lahir' : 'Makasar', 'Usia' : '23 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17008', 'Nama Pegawai' : 'Nadiya Putri',
      'Divisi' : 'Marketing', 'Jabatan' : 'Staff', 
      'Domisili' : 'Bekasi', 'Tempat Lahir' : 'Bekasi', 'Usia' : '23 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17009', 'Nama Pegawai' : 'Fery Feryandi',
      'Divisi' : 'Sales', 'Jabatan' : 'Staff', 
      'Domisili' : 'Bekasi', 'Tempat Lahir' : 'Bandung', 'Usia' : '23 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17010', 'Nama Pegawai' : 'Samantha Grace',
      'Divisi' : 'Finance', 'Jabatan' : 'Manajer', 
      'Domisili' : 'Jakarta', 'Tempat Lahir' : 'Surabaya', 'Usia' : '34 Tahun', 'Pendidikan Terakhir' : 'S2'},
      {'idPegawai' : '17011', 'Nama Pegawai' : 'Hardi Haryanto',
      'Divisi' : 'Marketing', 'Jabatan' : 'Manajer', 
      'Domisili' : 'Tangerang', 'Tempat Lahir' : 'Bandung', 'Usia' : '33 Tahun', 'Pendidikan Terakhir' : 'S2'},
      {'idPegawai' : '17012', 'Nama Pegawai' : 'Gretha Gracia',
      'Divisi' : 'Finance', 'Jabatan' : 'Senior Analyst', 
      'Domisili' : 'Bogor', 'Tempat Lahir' : 'Bogor', 'Usia' : '29 Tahun', 'Pendidikan Terakhir' : 'S1'},
      {'idPegawai' : '17013', 'Nama Pegawai' : 'Bima Subekti',
      'Divisi' : 'Marketing', 'Jabatan' : 'Intern', 
      'Domisili' : 'Jakarta', 'Tempat Lahir' : 'Jakarta', 'Usia' : '21 Tahun', 'Pendidikan Terakhir' : 'SMA'},
      {'idPegawai' : '17014', 'Nama Pegawai' : 'Nindya Putri',
      'Divisi' : 'Sales', 'Jabatan' : 'Intern', 
      'Domisili' : 'Jakarta', 'Tempat Lahir' : 'Jakarta', 'Usia' : '21 Tahun', 'Pendidikan Terakhir' : 'SMA'},
      {'idPegawai' : '17015', 'Nama Pegawai' : 'Dania Mutiara',
      'Divisi' : 'Finance', 'Jabatan' : 'Intern', 
      'Domisili' : 'Depok', 'Tempat Lahir' : 'Makasar', 'Usia' : '22 Tahun', 'Pendidikan Terakhir' : 'S1'},
]

menuList = [
    '1. Report Data Pegawai',
    '2. Mengubah Data Pegawai',
    '3. Menambah Data Pegawai',
    '4. Menghapus Data Pegawai',
    '5. Keluar'
]

def dataError():
     print('Data Yang Anda Masukan Tidak Dapat Ditemukan!')
def dataNormal():
      jumlahPegawai = len(dataPegawai)
      print(f'Jumlah Data Pegawai: {jumlahPegawai}')
      for pegawai in (dataPegawai):
            print(f'ID Pegawai : {pegawai['idPegawai']}, Nama Pegawai : {pegawai['Nama Pegawai']}, Divisi : {pegawai['Divisi']}, Jabatan : {pegawai['Jabatan']}, Domisili : {pegawai['Domisili']}')      
def dataLengkap():
      idPegawaiInput = input('Masukan ID Pegawai: ')
      for pegawai in (dataPegawai):
            if pegawai ['idPegawai'] == idPegawaiInput:
                 print(f'\n== {pegawai['Nama Pegawai']} ==\n'
                    f'Divisi : {pegawai['Divisi']}\n'
                    f'Jabatan : {pegawai["Jabatan"]}\n'
                    f'Domisili : {pegawai['Domisili']}\n'
                    f'Tempat Lahir : {pegawai['Tempat Lahir']}\n'
                    f'Usia : {pegawai['Usia']}\n'
                    f'Pendidikan Terakhir : {pegawai['Pendidikan Terakhir']}\n')

def divisi(dataPegawai):
     divisiPegawai1 = input('Sort Data Berdasarkan Divisi :  ')
     divisi1 = [pegawai for pegawai in (dataPegawai) if pegawai ['Divisi'] == divisiPegawai1]
     if divisi1:          
        print(f'\n====== {divisiPegawai1} ======\n')
        for pegawai in divisi1:
             print(f'ID Pegawai : {pegawai['idPegawai']}, Nama Pegawai : {pegawai['Nama Pegawai']}, Jabatan : {pegawai['Jabatan']}')
def jabatan(dataPegawai):
     jabatanPegawai1 = input('Sort Data Berdasarkan Jabatan :  ')
     jabatan1 = [pegawai for pegawai in (dataPegawai) if pegawai ['Jabatan'] == jabatanPegawai1]
     if jabatan1:          
        print(f'\n====== {jabatanPegawai1} ======\n')
        for pegawai in jabatan1:
             print(f'ID Pegawai : {pegawai['idPegawai']}, Nama Pegawai : {pegawai['Nama Pegawai']}, Divisi : {pegawai['Divisi']}')
def domisili(dataPegawai):
     domisiliPegawai1 = input('Sort Data Berdasarkan Domisili :  ')
     domisili1 = [pegawai for pegawai in (dataPegawai) if pegawai ['Domisili'] == domisiliPegawai1]
     if domisili1:
        print(f'\n====== {domisiliPegawai1} ======\n')
        for pegawai in domisili1:
             print(f'ID Pegawai : {pegawai['idPegawai']}, Nama Pegawai : {pegawai['Nama Pegawai']}')

def UpdateDivisi(dataPegawai):
     divisiBaru = input(f'Divisi Saat Ini ({idPegawaiInput}): ')
     for pegawai in dataPegawai:
           if pegawai ['idPegawai'] == idPegawaiInput:
            pegawai['Divisi'] = divisiBaru
            print('Data Pegawai Updated: ')
            dataNormal()
def UpdateJabatan(dataPegawai):
    jabatanBaru = input(f'Jabatan Saat Ini ({idPegawaiInput}): ')
    for pegawai in dataPegawai:
          if pegawai ['idPegawai'] == idPegawaiInput:
            pegawai['Jabatan'] = jabatanBaru
            print('Data Pegawai Updated: ')
            dataNormal()
def UpdateDomisili(dataPegawai):
    domsiliBaru = input(f'Domisili saat ini ({idPegawaiInput}): ')
    for pegawai in dataPegawai:
          if pegawai ['idPegawai'] == idPegawaiInput:
            pegawai['Domisili'] = domsiliBaru
            print('Data Pegawai Updated: ')
            dataNormal()

def dataPegawaiUpdated():
     if True:
           idPegawai = input('idPegawai : ')
           try:
                 int(idPegawai)
                 namaPegawai = input('Nama Pegawai : ')
                 divisiPegawai = input('Divisi : ')
                 jabatanPegawai = input('Jabatan : ')
                 domisiliPegawai = input('Domisili : ')
                 tempatLahir = input('Tempat Lahir : ')
                 usiaPegawai = input('Usia: ')
                 pendidikanTerakhir = input('Pendidikan Terakhir : ')
                 indikatorData = {
                         'idPegawai' : idPegawai,
                         'Nama Pegawai' : namaPegawai,
                         'Divisi' : divisiPegawai,
                         'Jabatan' : jabatanPegawai,
                         'Domisili' : domisiliPegawai,
                         'Tempat Lahir' : tempatLahir,
                         'Usia' : usiaPegawai,
                         'Pendidikan Terakhir' : pendidikanTerakhir
                    }
                 dataPegawai.append(indikatorData)
                 dataNormal()
                 print(f'\n=== {namaPegawai} Telah Berhasil Dimasukan Kedalam List! ===\n')
                 
           except ValueError:
                 dataError()
def HapusDataPegawai():
     idPegawaiInput = input('Masukan ID pegawai: ')
     statusPegawai = input('Status Pegawai Saat ini: ')
     for index, pegawai in enumerate(dataPegawai):
           if pegawai['idPegawai'] == idPegawaiInput:
               indexPegawai = index
               dataPegawai.pop(indexPegawai)
               dataNormal()
               print(f'\n=== Saudara {pegawai['Nama Pegawai']} Saat ini Berstatus {statusPegawai} ===\n') 

userInput = '9'
while userInput != '5':
    print ('\n========== SISTEM INFORMASI PEGAWAI ==========\n')
    for menu in menuList:
        print(menu)
     
    userInput = input('Pilih menu yang ingin dilihat: ')
    if userInput == '1':
            print('\n========== DATA PEGAWAI PT. MAKMUR ==========\n')
            dataNormal()
            print('1. Sorting Data Pegawai')
            print('2. Data Individu Pegawai')
            print('3. Kembali ke Menu Utama')
            userMenu1 = input ('Pilih menu: ')
            if userMenu1 =='1':
                print('Sorting Berdasarkan :')
                print('1. Divisi')
                print('2. Jabatan')
                print('3. Domisili')
                print('4. Kembali ke Menu Utama')
                userSort = input('Pilih Data Sort: ')
                if userSort =='1':
                     divisi(dataPegawai)
                     
                elif userSort =='2':
                     jabatan(dataPegawai)
                     
                elif userSort == '3':
                     domisili(dataPegawai)
                     
                else:
                     dataError()
                     break
    
            elif userMenu1 == '2':
                       dataLengkap()
                          
            elif userMenu1 == '3':
                 quit
            else:
                 dataError()
                 break        
    elif userInput == '2':
            print('\n========== UBAH DATA PEGAWAI PT. MAKMUR ==========\n')
            dataNormal()
            idPegawaiInput = input('Masukan ID pegawai: ')
            for pegawai in dataPegawai:
                if pegawai ['idPegawai'] == idPegawaiInput:
                    print('\n========== PILIH DATA YANG INGIN DIUBAH ==========\n')
                    print('1. Divisi')
                    print('2. Jabatan')
                    print('3. Domisili')
                    print('4. Kembali ke Menu Utama')
                    userMenu2 = input('Pilih Data Yang Ingin Diubah: ')                
                    
                    if userMenu2 == '1':
                                UpdateDivisi(dataPegawai)
                    
                    elif userMenu2 == '2':
                                UpdateJabatan(dataPegawai)
                                
                    elif userMenu2 == '3':
                                UpdateDomisili(dataPegawai)
                    elif userMenu2 == '4':
                          print('== Selesai ==')
                    else:
                          dataError()
                          break                                               
    elif userInput == '3':
            print('\n========== INPUT DATA PEGAWAI BARU PT. MAKMUR ==========\n')
            dataPegawaiUpdated()
    elif userInput == '4':
            print('\n========== PENONAKTIFAN PEGAWAI PT. MAKMUR ==========\n')
            HapusDataPegawai()
     
    elif userInput == '5':
            print('Sampai Jumpa!')
    else:
            dataError()
            break