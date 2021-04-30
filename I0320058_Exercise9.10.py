import array

A=array.array('i', [100,200,300,400,500])
print(A)
A[1]=-700   #mengubah elemen kedua
A[4]=800    #mengubah elemen ketiga
print(A)

#nilai awal sebelum dibalik
print('nilai awal sebelum dibalik : ', A)
#membalik urutan elemen array
A.reverse()

#setelah dibalik
print(A)
