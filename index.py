import ephem
import math

# 1. Mengatur Lokasi Pengamat (Kebumen)
kebumen = ephem.Observer()
kebumen.lat = '-7.670829'      # Garis Lintang (Latitude) Kebumen
kebumen.lon = '109.660677'     # Garis Bujur (Longitude) Kebumen
kebumen.elevation = 100        # Ketinggian dari permukaan laut (meter)

# Mengatur kondisi atmosfer untuk akurasi refraksi di dekat ufuk
kebumen.temp = 28              # Suhu tropis rata-rata sore hari (Celcius)
kebumen.pressure = 1010        # Tekanan atmosfer standar (mBar)

# 2. Mengatur Tanggal Pengamatan (18 Februari 2026)
# Kita set ke siang hari UTC, agar bisa mencari sunset di sore harinya.
#yy = input("Masukan Waktu: ")
kebumen.date = '2026/03/19 05:00:00' 

# 3. Mendefinisikan Benda Langit
matahari = ephem.Sun()
bulan = ephem.Moon()

# 4. Mencari Waktu Matahari Terbenam (Sunset)
waktu_sunset = kebumen.next_setting(matahari)
kebumen.date = waktu_sunset # Geser waktu pengamat ke detik sunset

# 5. Menghitung Posisi Bulan pada Waktu Sunset Tersebut
bulan.compute(kebumen)
matahari.compute(kebumen)

# 6. Mengubah format radian ke derajat desimal agar mudah dibaca
tinggi_bulan_derajat = bulan.alt * 180 / math.pi
elongasi_derajat = ephem.separation(bulan, matahari) * 180 / math.pi

# 7. Menampilkan Hasil
print("=== SIMULASI HISAB HILAL 2026 ===")
print(f"Lokasi       : Kebumen")
print(f"Waktu Sunset : {ephem.localtime(waktu_sunset)} WIB") # Konversi ke waktu lokal PC
print(f"---------------------------------")
print(f"Tinggi Hilal : {tinggi_bulan_derajat:.2f} derajat")
print(f"Elongasi     : {elongasi_derajat:.2f} derajat")

if tinggi_bulan_derajat >= 3 and elongasi_derajat >= 6.4:
    print("Status       : Memenuhi Kriteria MABIMS (Bisa dilihat)")
elif tinggi_bulan_derajat > 0:
    print("Status       : Wujudul Hilal (Di atas ufuk, tapi belum memenuhi MABIMS)")
else:
    print("Status       : Bulan di bawah ufuk (Belum wujud)")
