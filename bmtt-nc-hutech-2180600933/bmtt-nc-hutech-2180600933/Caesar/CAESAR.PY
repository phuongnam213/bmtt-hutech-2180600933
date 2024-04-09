def encrypt(chuoi, khoa):
    mahoa=''
    for i in chuoi:
      if i.isalpha():
            ord_k=ord(i)+khoa
            if ord_k>ord('z'):
                ord_k =26
            k=chr(ord_k)
            mahoa+=k
      else:
        mahoa+=i
    return mahoa
def decrypt(chuoi,khoa):
  mahoa=''
  for i in chuoi:
    if i.isalpha():
      ord_k=ord(i)-khoa
      if ord_k<ord('a'):
        ord_k=26
      k=chr(ord_k)
      mahoa+=k
    else:
      mahoa+=i
  return mahoa


chuoi=input('Nhập chuỗi cần mã hóa:')
khoa=int(input('Nhập số khoá:'))

print(encrypt(chuoi,khoa))

chuoix=input('Nhập vào chuỗi cần giải mã:')
khoax=int(input('Nhập số khoá:'))

print(decrypt(chuoix,khoax))
