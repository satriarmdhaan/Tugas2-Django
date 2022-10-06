## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS adalah kode CSS yang ditulis langsung dalam elemen `HTML`.

Kelebihan dari Inline CSS:
* Pengujian suatu perubahan dapat dilihat dan diuji dengan lebih mudah.
* Dapat digunakan untuk memperbaiki kode dengan cepat.
* Memiliki proses _request HTTP_ yang lebih kecil dan proses load website lebih cepat.

Kekurangan dari Inline CSS:
* Tidak efisien karena hanya dapat diaplikasikan pada satu elemen `HTML`.

Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan kode `HTML`.

Kelebihan dari Internal CSS:
* Tampilan hanya berubah pada satu halaman saja.
* TidaK diperlukan import file karena `HTML` dan `CSS` berada pada satu file yang sama.
* `Class` dan `ID` dapat digunakan melalui _internal stylesheet_.

Kekurangan dari Internal CSS:
* Tidak efisien apabila ingin mengaplikasikan `CSS` ke beberapa file.
* Performa website lebih lambat karena membutuhkan `load` yang besar ketika ingin berganti halaman.

External CSS adalah kode yang ditulis terpisah dari kode `HTML Eksternal`. Dengan kata lain, kode CSS ditulis dalam file khusus dengan ekstensi `.css`.

Kelebihan dari External CSS:
* Ukuran file `HTML` lebih kecil dan struktur kode `HTML` menjadi lebih rapih.
* _Load_ halaman lebih cepat.
* `File CSS` dapat digunakan ke beberapa halaman sekaligus.

Kekurangan dari External CSS:
* Halaman dapat menjadi berantakan apabila `file CSS` gagal dipanggil oleh `file HTML`.

## Jelaskan tag HTML5 yang diketahui.
* `<dl>` Berfungsi untuk mendefinisikan description list.
* `<p>` Berfungsi untuk mendefinisikan paragraf.
* `<style>` Berfungsi untuk mendefinisikan style information.
* `<li>` Berfungsi untuk mendefinisikan list item.
* `<title>` Berfungsi untuk mendefinisikan judul halaman.

## Tipe-Tipe CSS Selector yang diketahui.
* `:hover` Berfungsi untuk memilih elemen ketika mouse sedang hover pada elemen tersebut.
* `.class` Berfungsi untuk memilih seluruh elemen yang ada didalam class.

## Implementasi

* Melakukan kustomisasi pada folder templates html tugas 4 dengan `<style>` menurut ketentuan pada tugas 5. 