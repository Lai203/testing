#
#               111
#          1111 111
#         1111  111
#        1111   111
#               111
#               111
#               111
#               111
#               111
#               111
#               111
#       1111111111111111111
#

#LIST MENU 
# print ("|---------------------------------------|")
# print ("|      WELCOME LADIES & GENTLEMAN       |")
# print ("|---------------------------------------|")
# print ("|              LIST MENU                |")
# print ("|           1. (A1) AYAM GORENG         |")
# print ("|           2. (A2) AYAM BAKAR          |")
# print ("|           3. (B1) ES JERUK            |")
# print ("|           4. (B2) TEH MANIS           |")
# print ("|---------------------------------------|")

# total_harga = 0
# total_porsi = 0
# opsi = "Y"
# while opsi == "Y" :
#     kode = input ("Masukkan Kode Pesanan : ")
#     menu = kode [0:2]
#     jumlah = int (kode [2:4]) 
#     if menu == "A1" :
#         harga = 15000
#         nama_menu = "Ayam Goreng"
#     elif menu == "A2" :
#         harga = 20000
#         nama_menu = "Ayam Bakar"
#     elif menu == "B1" :
#         harga = 8000                
#         nama_menu = "Es Jeruk"
#     elif menu == "B2" :
#         harga = 5000            
#         nama_menu = "Teh Manis"
#     else :
#         harga = 0
#         nama_menu = "Tidak Tersedia"
#     total_porsi = total_porsi + jumlah
#     total_harga = total_harga + (harga*jumlah)
#     print("  Menu yang dipilih       :",nama_menu)
#     print("  Harga per porsi         : Rp. ", harga)
#     print("  Total Pembayaran        : Rp. ", total_harga)
#     print("  Total Porsi Keseluruhan : ", total_porsi)
#     opsi = input ("Apakah akan pesan lagi (Y/N) : ") 



#
#          222222       
#       2222    2222    
#      2222      2222   
#      2222       2222  
#                  2222 
#                 2222  
#              2222     
#            2222       
#          2222         
#        2222           
#      2222             
#     2222              
#     22222222222222222 
#
import random
import string
import datetime

#List Pemilihan Presiden
print (" ----------------------------------------")
print ("|         DAFTAR MOVIE YANG ADA          |")
print ("| ---------------------------------------|")
print ("|   TELAH HADIR                          |")
print ("|   1. SUZUME NO TOJIMARI                |")
print ("|   2. JUJUTSU KAISEN 0                  |")
print ("|   3. KIMETSU NO YAIBA MUGEN NO TRAIN   |")
print ("|   4. YOUR NAME                         |")
print (" ----------------------------------------")

print (" ---------------------------------------------------------")
print ("|                                                         |")
print ("|  HARGA TIKET                                            |")
print ("|  SUZUME NO TOJIMARI              : (SZNT): 100.000 IDR  |")
print ("|  JUJUTSU KAISEN 0                : (JJK0): 150.000 IDR  |")
print ("|  KIMETSU NO YAIBA MUGEN NO TRAIN : (KNYT): 200.000 IDR  |")
print ("|  YOUR NAME                       : (YUNE): 100.000 IDR  |")
print ("|                                                         |")
print ("|                                                         |")
print ("|  KURSI TERSEDIA :                                       |")
print ("|  1. VVIP   = 20.000 IDR                                 |")
print ("|  2. VIP    = 10.000 IDR                                 |")
print ("|  3. GENERAL= 5.000 IDR                                  |")
print ("|                                                         |")
print (" ---------------------------------------------------------")
Datas_Transaction = {}
input_transaction = { 'MovieChoosen' : 'AAAA',
                'ChairChoosen' : '1',
                'Ticket'       : 1,
                'GenerateCode' : "AAAAAAAA",
                'MoviePrice'   : 000000000,
                'TotalPrice'   : 000000000 
              }

while True:
    
    Transaction = dict.fromkeys(input_transaction.keys())

    Transaction['GenerateCode']= input ("Please input the Movie With Chair and Ticket Buy (e.g : SZNT2100 = Suzume No Tojimari in VIP, buy 100 Ticket) :")
    Transaction['MovieChoosen'] = Transaction['GenerateCode'][0:4]
    Transaction['ChairChoosen'] = Transaction['GenerateCode'][4]
    Transaction['Ticket'] = int (Transaction['GenerateCode'][5:])

    if Transaction['MovieChoosen']  == "SZNT" or Transaction['MovieChoosen']  == "YUNE" :
        Transaction['MoviePrice'] = 100000
    elif Transaction['MovieChoosen'] == "JJK0" :
        Transaction['MoviePrice'] = 150000
    elif Transaction['MovieChoosen']  == "KNYT" :
        Transaction['MoviePrice'] = 200000
    else :
        print("No Movie Available")

    if Transaction['ChairChoosen'] == "1" :
        Transaction['ChairChoosen'] = "VVIP"
        TicketPrice = Transaction['MoviePrice'] + 20000
    elif Transaction['ChairChoosen'] == "2" :
        Transaction['ChairChoosen'] = "VIP"
        TicketPrice = Transaction['MoviePrice'] + 10000
    elif Transaction['ChairChoosen'] == "3" :
        Transaction['ChairChoosen'] = "GENERAl"
        TicketPrice = Transaction['MoviePrice'] + 5000
    else :
        print ("NO CHAIR LMAO")

    Transaction['TotalPrice'] = TicketPrice *  Transaction['Ticket']

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))

    Datas_Transaction.update({KEY : Transaction})

    print (f"\n {'KEY':<15}{'CODE':<15} {'MOVIE':<10} {'PRICE':<10} {'CHAIR':<10} {'TICKET':<10} {'TOTAL PRICE':<10}")
    print ('-'*100)

    for Transaction in Datas_Transaction :
        KEY = Transaction
        CODE = Datas_Transaction [KEY]['GenerateCode']
        MOVIE = Datas_Transaction [KEY]['MovieChoosen']
        CHAIR = Datas_Transaction [KEY]['MovieChoosen']
        TICKET = Datas_Transaction [KEY]['Ticket']        
        PRICE = Datas_Transaction [KEY]['MoviePrice']
        TOTAL = Datas_Transaction [KEY]['TotalPrice']

        print (f"{KEY:<16}{CODE:<15}{MOVIE:<11}{PRICE:<13}{CHAIR:<11}{TICKET:<12}{TOTAL:<10}")
   
    print ("\n")
    OPTION = input ("DO YOU WANNA BUY MORE TICKET (Y/N) : ")
    if (OPTION == "N") or (OPTION == "n"):
        break

print ("THANK YOU FOR YOUR PURCHASE!! :D ")    

