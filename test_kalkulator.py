import unittest
from kalkulator_nilai import hitung_nilai_akhir, tentukan_huruf, cek_kelulusan

class TestPenilaianMahasiswa(unittest.TestCase):

    # 1. Menguji fungsi hitung_nilai_akhir (Valid)
    def test_hitung_nilai_akhir_valid(self):
        # 80*0.3 + 80*0.3 + 80*0.4 = 80.0
        self.assertEqual(hitung_nilai_akhir(80, 80, 80), 80.0)

    # 2. Menguji fungsi hitung_nilai_akhir (Invalid / Error Handling)
    def test_hitung_nilai_akhir_invalid(self):
        # Jika dosen salah input nilai minus (-10), program harus mereturn 0
        self.assertEqual(hitung_nilai_akhir(-10, 80, 80), 0)

    # 3. Menguji fungsi tentukan_huruf
    def test_tentukan_huruf(self):
        self.assertEqual(tentukan_huruf(85), 'A')
        self.assertEqual(tentukan_huruf(72), 'B')

    # 4. Menguji fungsi cek_kelulusan
    def test_cek_kelulusan(self):
        self.assertEqual(cek_kelulusan('A'), "Lulus")
        self.assertEqual(cek_kelulusan('D'), "Tidak Lulus")

if __name__ == '__main__':
    unittest.main()