# Selamat datang di BikinHTML

BikinHTML adalah sebuah kerangka kerja yang dapat menghasilkan sebuah file HTML dengan sintaks bahasa Indonesia. Berikut adalah cara penggunaan BikinHTML.

# Cara Penggunaan
1. Line pertama. Line pertama dalam sebuah BikinHTML harus diawali dengan `Saya ingin buat halaman web`

2. Pemisah sintaks. Pemisah sintaks dalam BikinHTML adalah titik yang diikuti oleh spasi. Contoh: `Saya ingin buat halaman web. `

3. Memberi judul pada file HTML. Untuk memberi judul pada file HTML yang dihasilkan, cukup dengan memasukkan sintaks

```
Judul halaman adalah "<judul>".

```

Dengan `<judul>` diganti dengan judul dari halaman.

4. Membuat elemen dan text. Untuk membuat elemen dan text, gunakan kata "berisikan" atau "terdapat" pada kalimat dan diikuti oleh konten dalam tanda petik dobel. Contoh:

```
Di dalam halaman terdapat sebuah "div". Div tersebut berisikan "<text>"

```

Beberapa elemen seperti div, span, header, footer, section, dapat dibuat dengan memasukkan ke dalam tanda petik dobel. Beberapa Elemen digantikan dengan keyword tertentu.

5. Membuat gambar. Seperti membuat elemen tetapi menggunakan kata "gambar"

```

Terdapat "gambar".

```

6. Memberi atribut. Memberi atribut kepada sebuah elemen dapat dilakukan dengan memberikan kata "dengan atribut" yang diikuti oleh namaatribut=isiatribut. Contoh:

```

Terdapat "gambar" dengan atribut src=image.png, width=300px, class=gambar.

```

7. Kembali satu level ke root HTML. Untuk kembali naik satu level dari dalam sebuah div, span, paragraf, dapat menggunakan keyword "selanjutnya," atau "kemudian,". Contoh:

```
Halaman berisikan "div". Dalam div terdapat kata "Halo".

Kemudian, setelah div terdapat sebuah gambar dengan src=halo.jpg

```

8. Import. Gunakan keyword "memakai". Contoh: `Website ini memakai "bootstrap".`
