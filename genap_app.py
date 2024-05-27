
def CheckGenap(n): 
    #Fungsi untuk mengecek angka genap dengan output boolean (benar/salah)
    if n % 2 == 0: # habis dibagi 2
        return f'Ini bilangan genap.'
    return f'Ini bilangan ganjil.'

# main idiom
if __name__ == "__main__":
    userInput = input('Masukkan angka: ')
    userInputNum = int(userInput)
    print(CheckGenap(userInputNum))



import unittest
from genap_app import CheckGenap # from <module name> import <function name>

class TestCheckGenap(unittest.TestCase):
    def test_CheckGenap_success1(self):
        #input
        num = 2
        #proses
        result = CheckGenap(num)
        #output
        self.assertEqual(result, 'Ini bilangan genap.')

        # ini versi penulisan 1 line
        # self.assertEqual(CheckGenap(10), 'Ini bilangan genap.')

    def test_CheckGenap_success2(self):
        self.assertEqual(CheckGenap(3), 'Ini bilangan ganjil.')

# idiom unittest
if __name__ == '__main__':
    unittest.main(verbosity=1)


