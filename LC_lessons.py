dictgaji = {
    "manager": 10000000,
    "staff": 5000000,
    "kasir": 4000000
}

dictgaji["manager"]

def hitunggaji(jabatan, jamKerja): #output: uang gaji + lembur
    if jamKerja > 40:
        uangLembur = 20000 # per jam
        extraJam = jamKerja - 40
        gaji = dictgaji[jabatan]
        #dapat lembur
        total = gaji + (uangLembur * extraJam)
        return total
    
    else:
        #ga dapet lembur
        gaji = dictgaji[jabatan]
        return gaji
    
def totalGaji(**dataKaryawan):
    total = 0
    for key in dataKaryawan:
        #hitung gaji setiap karyawan
        gaji = hitunggaji(key, dataKaryawan[key])

        #increment total dengan gaji
        total = total + gaji

    return total


#totalGaji(manager=45, staff=30, kasir=40)

print(hitunggaji("manager", 45))
print(hitunggaji("staff", 60))
print(hitunggaji("kasir", 75))