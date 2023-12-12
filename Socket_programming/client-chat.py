# Bağlantı için socket kütüphanesinin yüklenmesi
import socket

print("mesajlaşmayı bitirmek için, Bye veya bye yazınız.")
host_ip = input("serveri açtığınız host'un İP adresini yazabilirsiniz! ")
s = socket.socket()	# socket kütüphanesinden socket fonksiyonunun s değişkenine atanması
s.connect((host_ip,12345))	# server host'un ip ve port'u ile bağlanması

# mesajlaşmanın başlanması
while True:
    str = input("zamanı öğrenmek için 't', tarihi öğrenmek için 'd' yazabilirsiniz! ")
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    print ("N:",s.recv(1024).decode())
s.close()
