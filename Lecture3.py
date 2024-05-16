# %%
#exercise 1

rows = 9 

for i in range(rows):
    variable = i + 1

    
    for a in range(i + 1):
        print(variable, end = "")  
    print()  

# %%
#ungraded

def number_of_words:
    tryWords = input(number_of_words)



# %%
var2 = 20

var1 = int(input("masukan angka untuk var1: "))


if var1 == var2:
    #whats going to happen
    print("var1 is equal to var2")
elif var1 > var2:
    print("var1 is more than var2")
elif var1 < var2:
    print("var1 is less than var2")
else:
    print("var1 is not equal to var2")



# %%
if 1 == 1:
    print("sama")
else:
    print("eda")

print ("sama") if 1 == 1 else print("beda")
#ternary is only for if-else, does not work with elif, or if else.
#statement/coding that has at least 2 statements (for the 2 conditions)




# %%
var1 = int(input("masukkan angka 1-5:"))

while var1 <= 5:
    #maka jalankan kode beriku
    print("kondisi sesuai")
    var1 = int(input("msukkan angka 1-5: "))

print("kondisi tidak sesuai")

    






# %%
#tipe data list dan tuple itu bisa digunakan untuk 
listAngka = [5,2,3,4,5]

range(13) #function untuk membuat kumpulan angka 

var1 = 1
while var1 <= 5:
    for varAngka in range(13):
        print(varAngka)

        if varAngka > 3:
            break
    var1 = int(input("angka"))

    






# %%
[print(varAngka) for varAngka in range(4)]
#ternary

# %%
#use of keys and dictionaries

dictionary = {'foo': 1, 'bar': 2, 'baz': 3}

for key in dictionary:
    print(dictionary[key])

# %%


def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

password = input("enter your pass")
if check_password(password):
    print("valid")
else:
    print("invalid")




# %%
print() # untuk menampilkan text
type() # untuk mengetahui tipe data dari seuah value/variabel
len() # untuk mengetahui jumlah karakter dari string/banyaknya data dari list atau tuple
int() # untuk mengubah tipe data dari string ke integer
input() # untuk menerima input dari user


# %%
# penjumlahan

def addNumber(v, y): 
    var1 = v
    var2 = y

    return var1 + var2

def sayHello():
    print("hello World")

iniGlobal = "ini global"

#sayHello()
result = addNumber(30, 60) 
#print(result)

#if result > 50:
   # print("pass")
#else:
  #  print("no pass")

print(result)
print(iniGlobal)






# %%
#function untuk memuat profile user yang akan mengenerate nama lengkap 
#yang terdiri dari firstname + lastname

def generateProfile(firstname,lastname):
    fullName = firstname + " " + lastname

    return fullName

def sayHello(userName = "World"):
    print("Hello " + userName)

#sayHello()
#sayHello("Ryan")

# - variable-length parameter
# - ada tanda bintang (* atau **)
'''
def generateClass(className, *studentNames):
    print("Nama kelas: " + className)
    print("List nama student:")


    for std in studentNames:
       print (std)


    print("List nama student: " + studentNames)

generateClass("HCK-17", "sasa", "gracia", "vincent", "Ryan", "Dani", "Fiqih", "Rio")
'''
# contoh **

#variable length parameter (* and **)

def generateNilaiKelas(className, **studentGrades):
    nilai = 0

    print("Nama kelas: " + className)
    print("List nama student:")
    #for std in studentNames:
        #print (std)


    for key in studentGrades:
        print(key, studentGrades[key])
        nilai = nilai + studentGrades[key]

    nilaiRataRata = nilai / len(studentGrades)

    print("Nilai Rata-Rata Kelas: ", nilaiRataRata)

generateNilaiKelas("HCK-17", sasa=77, vincen=88, Ryan = 88)


#sifat parameter function:
# - ergantung pada posisi
# - waji diisi, jika ada

#variasi parameter:
# - default/optional parameter

#result = generateProfile("Rey", "Mysterio") #output: "Rey Mysterio"
#result1 = generateProfile(lastname="Cena", firstname="John") #output: "John Cena"

#print(result)
#print(result1) 




# %%
#normal function
def sayHello():
    print("Hello world!")

#call normal function
sayHello()

#anon function
bilangHello = lambda userName: print("hello " + userName)

#call anon function
bilangHello("boi")




# %%
def sayHello(name):
    print("Hello" + name)

def generateProfile(firstName, lastName):
    print()


