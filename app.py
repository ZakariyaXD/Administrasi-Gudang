import csv
import os

csv_filename = 'Data/Barang.csv'

# clearscreen ubntuk membersihkan layar dengan key cls = clearscreen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan menu program
def show_menu():

    clear_screen()
    print("=== Aplikasi Administrasi Gudang === \n")
    print("============ Menu =============")
    print("1. Lihat Daftar Barang")
    print("2. Tambah Barang")
    print("3. Edit Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Sortir Barang")
    print("0. Keluar \n")
    print("===============================")
    selected_menu = input("Pilih menu :  ")
    
    # Percabangan untuk menentukan pilihan menu
    if(selected_menu == "1"):
        lihat_barang()
    elif(selected_menu == "2"):
        tambah_barang()
    elif(selected_menu == "3"):
        edit_barang()
    elif(selected_menu == "4"):
        hapus_barang()
    elif(selected_menu == "5"):
        cari_barang()
    elif(selected_menu == "6"):
        sorting_barang()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

# fungsi kembali ke menu isinya memanggil fungsi show menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali")
    show_menu()

# fungsi menampilkan barang 
def lihat_barang():
    clear_screen()
    Barang = []
# buka file CSV dengan mode R / Baca
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("-" * 55)
    print("\t\tDaftar Stok Barang Toko")
    print("-" * 55)

    print("KODE \t NAMA \t\t QTY")
    print("-" * 55)

    # Looping untuk mengeluarkan datanyna
    for data in Barang:
        print(f"{data['KODE']} \t {data['NAMA']} \t\t {data['QTY']}")
    print("-" * 55)
    
    back_to_menu()


#  fungsi tambah barang 
def tambah_barang():
    clear_screen()
    with open(csv_filename, mode='a',newline='') as csv_file:
        fieldnames = ['KODE', 'NAMA', 'QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("===============================")
        print("======== Tambah Barang ========")
        print("===============================\n")
        
        kode = input("kode: ")
        nama = input("Nama Barang: ")
        QTY = input("Jumlah Barang: ")

        print("===============================")


        writer.writerow({'KODE': kode, 'NAMA': nama, 'QTY': QTY})    
    
    back_to_menu()


def cari_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("Cari berdasarkan kode")
    kode = input("Masukkan kode : ")

    data_found = []

    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['KODE'] == kode):
            data_found = Barang[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"NAMA: {data_found['NAMA']}")
        print(f"QTY :{data_found['QTY']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    

def edit_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("-" * 55)
    print("\t\tDaftar Stok Barang Toko")
    print("-" * 55)

    print("KODE \t NAMA \t\t QTY")
    print("-" * 55)

    for data in Barang:
        print(f"{data['KODE']} \t {data['NAMA']} \t\t {data['QTY']}")

    print("-" * 55)
    kode = input("Pilih Kode Barang : ")
    nama = input("Nama Baru: ")
    QTY = input("Jumlah baru: ")

    # mencari Barang dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in Barang:
        if (data['KODE'] == kode):
            Barang[indeks]['NAMA'] = nama
            Barang[indeks]['QTY'] = QTY
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['KODE', 'NAMA', 'QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'KODE': new_data['KODE'], 'NAMA': new_data['NAMA'], 'QTY': new_data['QTY']}) 

    back_to_menu()


def hapus_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("KODE \t NAMA \t\t QTY")
    print("-" * 55)

    for data in Barang:
        print(f"{data['KODE']} \t {data['NAMA']} \t\t {data['QTY']}")

    print("-----------------------")
    kode = input("Hapus Barang dengan KODE : ")

    indeks = 0
    for data in Barang:
        if (data['KODE'] == kode):
            Barang.remove(Barang[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['KODE', 'NAMA', 'QTY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'KODE': new_data['KODE'], 'NAMA': new_data['NAMA'], 'QTY': new_data['QTY']}) 

    print("Data sudah terhapus")
    back_to_menu()

def sorting_barang():

    # importing pandas package
    import pandas as pandasForSortingCSV
  
    # assign dataset
    csvData = pandasForSortingCSV.read_csv("Data/Barang.csv")
                                         
    # displaying unsorted data frame
    print("\nBefore sorting:")
    print(csvData)
  
# sort data frame
    csvData.sort_values(["KODE"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)
  
    # displaying sorted data frame
    print("\nAfter sorting:")
    print(csvData)
    back_to_menu()
#def sorting_barang(arr):
    #clear_screen()
#    n = len(arr)
    # Traverse through all array elements
#    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
#        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
#            if arr[j][2] > arr[j + 1][2]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#   return arr


if __name__ == "__main__":
    while True:
        show_menu()