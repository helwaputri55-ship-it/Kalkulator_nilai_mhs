def hitung_nilai_akhir(tugas, uts, uas):
    if tugas < 0 or uts < 0 or uas < 0:
        return 0
    if tugas > 100 or uts > 100 or uas > 100:
        return 0
    nilai = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai

def tentukan_huruf(nilai_akhir):
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 55:
        return 'C'
    else:
        return 'D'

def cek_kelulusan(huruf):
    if huruf == 'A' or huruf == 'B' or huruf == 'C':
        return "Lulus"
    else:
        return "Tidak Lulus"

# Blok ini hanya akan dieksekusi jika file dijalankan langsung (bukan di-import)
if __name__ == '__main__':
    print("\n=== DEMO 4 SKENARIO SISTEM PENILAIAN ===")
    
    # Skenario 1
    print("\n1. Skenario Hitung Nilai Valid (Input: 80, 80, 80)")
    hasil_1 = hitung_nilai_akhir(80, 80, 80)
    print(f"   Expected Output : 80.0")
    print(f"   Actual Output   : {hasil_1}")

    # Skenario 2
    print("\n2. Skenario Hitung Nilai Invalid/Minus (Input: -10, 80, 80)")
    hasil_2 = hitung_nilai_akhir(-10, 80, 80)
    print(f"   Expected Output : 0 (Error Handling)")
    print(f"   Actual Output   : {hasil_2}")

    # Skenario 3
    print("\n3. Skenario Penentuan Huruf (Input: 85)")
    hasil_3 = tentukan_huruf(85)
    print(f"   Expected Output : A")
    print(f"   Actual Output   : {hasil_3}")

    # Skenario 4
    print("\n4. Skenario Cek Kelulusan (Input: D)")
    hasil_4 = cek_kelulusan('D')
    print(f"   Expected Output : Tidak Lulus")
    print(f"   Actual Output   : {hasil_4}")
    
    print("\n========================================\n")