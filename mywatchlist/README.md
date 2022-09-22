## Link HEROKUAPP

Link : [Link](https://tugas3-django.herokuapp.com/mywatchlist/)

## Perbedaan antara JSON, XML, dan HTML
- JSON : JSON (JavaScript Object Notation) adalah suatu format dari JavaScript untuk menyimpan dan mentransfer data dalam bentuk key dan value dengan format array.
- XML  : XML (eXtensible Markup Language) adalah markup language seperti HTML yang berguna untuk menyimpan dan mentransfer data dalam bentuk teks sederhana dengan tree   seperti HTML.
- HTML : HTML (HyperText Markup Language) adalah markup language yang paling umum digunakan untuk membuat suatu laman website. Dalam HTML anda bisa membuat struktur tampilan laman website anda sendiri. HTMl digunakan hanya untuk menampilkan data-data dari bahasa pemrograman menjadi suatu tampilan yang lebih dimengerti oleh orang awam dan bukan untuk mentransfer data.

## Data Delivery dalam Implementasi Platform
Data delivery diperlukan dalam implementasi platform untuk mentransfer data dari pusat data atau database menuju platform atau sebaliknya.
## Langkah - Langkah Implementasi
1. Membuat `django-app` bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`.

2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan `django-app` yang sudah dibuat.
  ```
  INSTALLED_APPS = [
    ...,
    'mywatchlist',
  ]
  ```

3. Buka 'urls.py' di folder `project_django` dan tambahkan path `mywatchlist` seperti sebagai berikut.
  ```
  urlpatterns = [
    ...,
    path('mywatchlist/', include('mywatchlist.urls')),
  ]
  ```

4. Buka file `models.py` yang ada pada folder `mywatchlist` dan menambahkan potongan kode berikut.
  ```
  from django.db import models

  class watchlist(models.Model):
      title = models.CharField(max_length=255)
      watched = models.TextField()
      rating = models.IntegerField()
      release_date = models.TextField()
      review = models.TextField()
  ```

5. Jalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam _database_ Django lokal.

6. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam _database_ Django lokal.

7. Buatlah sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `initial_mywatchlist_data.json` yang berisi data-data objek mywatchlist.

8. Jalankan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data tersebut ke dalam _database_ Django lokal.

9. Membuat function-function pada `views.py` untuk _render_ model yang telah dibuat ke dalam bentuk HTML, JSON, dan XML.

10. Membuat routing pada `urls.py` yang berada dalam folder `mywatchlist` dengan cara menambahkan `urlpatterns`.

11. Menambahkan `class` pada `test.py` dan fungsi-fungsi untuk melakukan testing pada `python manage.py test`.

12. Menambahkan isi `Procfile` agar data-data pada `initial_mywatchlist_data.json` dapat ditampilkan pada HEROKUAPP dengan potongan kode sebagai berikut.
  ```
  release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'

  web: gunicorn project_django.wsgi --log-file -
  ```

13. Melakukan `add`,`commit`, dan `push` ke dalam github.

## Postman
# HTML
![mywatchlist-html](https://user-images.githubusercontent.com/112569195/191591557-9c07f489-9013-4e14-9688-bc39b70b3a14.jpg)

# JSON
![mywatchlist-json](https://user-images.githubusercontent.com/112569195/191591672-e13a98c4-6f08-441c-8484-e33b0fa9179e.jpg)

# XML
![mywatchlist-xml](https://user-images.githubusercontent.com/112569195/191591702-574dee67-ef10-4e17-a5c9-928cff92a478.jpg)
