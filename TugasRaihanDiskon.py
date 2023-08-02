print("## program python diskon potongan harga")
print("---------------------------------------")
print("")

total = int(input('Total Belanja: Rp.'))

if (total >= 100000) and (total < 500000):
  bayar = total - (0.1 * total)
  print('Selamat, anda mendapat diskon 10%')
elif (total >= 500000) and (total < 1000000):
  bayar = total - (0.2 * total)
  print('Selamat, anda mendapat diskon 20%')
elif (total >= 1000000):
  bayar = total - (0.3*total)
  print('Selamat, anda mendapat diskon 30%')
else:
  bayar = total

#output
print('Total bayar: Rp.',round(bayar))