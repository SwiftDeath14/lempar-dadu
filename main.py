'''
Generator Lemparan Dadu
-------------------------------------------------------------
Program ini mensimulasikan lemparan dadu dengan 1 atau 2 dadu.
Pengguna dapat memilih jumlah dadu dan memutuskan apakah ingin 
melempar ulang atau tidak.
'''
import random  # Mengimpor pustaka random untuk menghasilkan angka acak
import os  # Mengimpor pustaka os untuk membersihkan layar konsol

# Fungsi untuk menentukan jumlah dadu yang akan dilempar
def num_die():
    while True:
        try:
            # Meminta input dari pengguna untuk jumlah dadu
            num_dice = input('Jumlah dadu (1 atau 2): ')
            valid_responses = ['1', 'one', 'two', '2']  # Respon yang valid
            if num_dice not in valid_responses:
                raise ValueError('Hanya diperbolehkan 1 atau 2 dadu.')
            else:
                return num_dice
        except ValueError as err:
            # Menampilkan pesan error jika input tidak valid
            print(err)

# Fungsi utama untuk melempar dadu
def roll_dice():
    min_val = 1  # Nilai minimum pada dadu
    max_val = 6  # Nilai maksimum pada dadu
    roll_again = 'y'  # Variabel untuk mengecek apakah pengguna ingin melempar lagi

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        # Membersihkan layar konsol
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Meminta jumlah dadu dari pengguna
        amount = num_die()

        if amount == '2' or amount == 'two':
            print('Mengocok dadu...')
            # Menghasilkan angka acak untuk dua dadu
            dice_1 = random.randint(min_val, max_val)
            dice_2 = random.randint(min_val, max_val)

            print('Hasil dadu adalah:')
            print('Dadu Pertama: ', dice_1)
            print('Dadu Kedua: ', dice_2)
            print('Total: ', dice_1 + dice_2)

            # Menanyakan kepada pengguna apakah ingin melempar ulang
            roll_again = input('Ingin melempar lagi? (y/n) ')
        else:
            print('Mengocok dadu...')
            # Menghasilkan angka acak untuk satu dadun
            dice_1 = random.randint(min_val, max_val)
            print(f'Hasil dadu adalah: {dice_1}')

            # Menanyakan kepada pengguna apakah ingin melempar ulang
            roll_again = input('Ingin melempar lagi? (y/n) ')

# Memastikan kode hanya dijalankan jika file ini adalah program utama
if __name__ == '__main__':
    roll_dice()
