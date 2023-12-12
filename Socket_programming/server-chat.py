# işletim sistemine erişim sağlayıp gereken komutların verilmesi
import os
os.system("sudo fuser -i 12345/tcp")
os.system("sudo lsof -i :8000")

# Bağlantı için socket kütüphanesinin yüklenmesi
import socket


port = 12345


print("clientten mesaj bekleniyor, sonlandırmak için Bye veya bye")
s = socket.socket()	# socket kütüphanesinden socket fonksiyonunun s değişkenine atanması
print("socket.socket()==",s)

s.bind(('', port))	 # belirtilen port ile bağlantıya kendisini açması
s.listen(1)	# bağlantı kurulmasını beklemesi

c, addr = s.accept()	# bağlantı kuran host'un IP adresini c ve addr değişkenine atanması

print ("bağlantı kurulan host: ",addr)

# mesajlaşmanın başlanması
while True:
    rcvdData = c.recv(1024).decode()	# gelen mesajın rcvdData değişkenine atanması.
    print ("S:",rcvdData)
    
    # Client'ın zaman ve tarih isteğine otomatik cevap verilmesi için koşulların belirlenmesi
    if(rcvdData=='t'):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        c.send(current_time.encode())
    elif(rcvdData=='d'):
        from datetime import date
        today = date.today()
        #dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        c.send(d1.encode())
    else:
        sendData = input("N: ")
        c.send(sendData.encode())
        if(sendData == "Bye" or sendData == "bye"):
            break
c.close()
