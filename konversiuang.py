#Konversi Uang Sederhana Ikmal Ali Azhari NIM 2309116087 
print('=' * 100)
print('Jasa Konversi Uang')
print('\t [1. Rupiah ke USD]')
print('\t [2. Rupiah ke Yen]')
print('\t [3. Rupiah ke Ringgit Malaysia]')

print('=' * 100)
#ini sebagai display

operasi = input('Pilih Mata Uang (1,2,3): ')
bilangan_1 = eval(input('Masukkan Nominal Uang Anda : '))
#ini sebagai input

print('=' * 100)


if operasi == '1':
  hasil = bilangan_1 * 0.00008
  print(f'Hasil Dari Nominal Rp.{bilangan_1} ke Dollar adalah {hasil}')
elif operasi == '2':
  hasil = bilangan_1 * 0.00876
  print(f'Hasil Dari Nominal Rp.{bilangan_1} ke Yen adalah {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * 0.00032
  print(f'Hasil Dari Nominal Rp.{bilangan_1} ke Ringgit Malaysia adalah {hasil}')

  print(f'Silahkan Input Ulang')
  #ini sebagai output
