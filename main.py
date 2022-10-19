
import theclass
import makequint
msk=""
while True:
    print("Program TBO minimalisasi\n1.input machine dfa\n2.mimaliseDFA\n3.tulis file\n4.exit\ninput:",end="")
    pilihan=input()
    if pilihan=="1":
        try :
            msk=theclass.DFAmachine(input("masukan route file quintaple:"))
            msk.printDfa()
        except:
            print("kesalahan terjadi")
    elif pilihan=="2":
        if msk!="":
            msk.minimalize()
            msk.printDfa()
        else:
            print("masukan belum ada")
    elif pilihan=="3":
        print("tulis nama mesin")
        makequint.make(input())
    elif pilihan=="4":
        break

