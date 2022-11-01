
import theclass
import makequint
msk=""
while True:
    #initialilze program agar program berulang-ulang hingga memilih pilihan keluar.
    print("Program TBO minimalisasi\n1.input machine dfa\n2.mimaliseDFA\n3.tulis file\n4.exit\ninput:",end="")
    pilihan=input()
    #menerima pilihan input.
    if pilihan=="1":
        #pilihan ini memintak nama file dari bahasa seperti L1 dan mengubahnya menjadi object DFAmachine
        try :
            msk=theclass.DFAmachine(input("masukan route file quintaple:"))
            msk.printDfa()
        except:
            print("kesalahan terjadi")
    elif pilihan=="2":
        #mengminimalizazi object DFAmachine menjadi object DFAmachine yang lebih sederhana 
        if msk!="":
            msk.minimalize()
            msk.printDfa()
        else:
            print("masukan belum ada")
    elif pilihan=="3":
        #membuat file yang menyimpan bahasa DFA nantinya.
        print("tulis nama mesin")
        makequint.make(input())
    elif pilihan=="4":
        break

