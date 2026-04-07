import random

def main():
    # Menanyakan nama pengguna
    nama = input("Masukkan nama Anda: ")

    # Daftar template kalimat random
    templates = [
        f"{nama} sedang belajar pemrograman Python dengan sangat antusias!",
        f"Wah, {nama} terlihat sangat hebat hari ini!",
        f"Apakah {nama} tahu bahwa Python adalah bahasa yang sangat populer?",
        f"Hari ini adalah hari yang cerah untuk {nama} memulai proyek baru.",
        f"{nama} baru saja memenangkan penghargaan 'Programmer Paling Kreatif'!",
        f"Kopi hangat di pagi hari sangat cocok menemani {nama} coding.",
        f"Jangan menyerah, {nama}! Setiap baris kode membawamu lebih dekat ke tujuan."
    ]

    # Memilih kalimat secara acak
    kalimat_random = random.choice(templates)

    # Menampilkan hasil
    print("\n" + "="*30)
    print(kalimat_random)
    print("="*30)

if __name__ == "__main__":
    main()
