**Link HEROKUAPP**<br />
https://django-tugas2.herokuapp.com/katalog/
![image](https://user-images.githubusercontent.com/112569195/190311527-4247b0fa-a576-479b-8aea-b5d3f32a53ed.png)
Penjelasan: Workflow dimulai dari Client melakukan HTTP Request dan diterima oleh urls.py. Lalu, urls.py akan melanjutkan request menuju views.py untuk diproses lebih
lanjut. Setelah itu, views.py akan meminta tampilan dari models.py yang dimana models.py akan mengambil data dari database. setelah views.py meminta tampilan dari
models.py, views.py akan melanjutkan workflow menuju katalog.html yang nantinya akan dilakukan formatting untuk menampilkan tampilan. Selanjutnya, katalog.html akan
membuat respon dan mengirim hasilnya menuju client.
**Virtual Environment**<br />
Virtual environment diperlukan untuk mengisolasi seluruh modul dan library yang diperlukan agar modul dan library yang kita butuhkan tidak terganggu oleh modul dan
library yang ada pada sistem operasi atau global.
<br />**Implementasi**<br />
Hal pertama yang saya lakukan adalah dengan melakukan clone repository template yang sudah diberikan ke dalam folder local. Setelah itu, saya membuat virtual environment
pada folder local tersebut dan menjalankannya untuk instalasi seluruh modul dan library yang diperlukan. Setelah selesai instalasi, saya membuat fungsi dan parameter
views.py dan urls.py serta katalog.html agar program dapat dijalankan. Lalu, saya melakukan migrasi untuk memuat data-data pada template repository ke dalam folder local. Setelah seluruh data dan file telah diubah dan siap untuk dijalankan, file dan data tersebut di push menuju github agar bisa dijalankan pada HEROKUAPP. Setelah melakukan push, saya menambahkan HEROKU_API_KEY dan HEROKU_APP_NAME pada github repository secret yang terdapat pada repository settings. Terakhir, program akan di deploy pada HEROKUAPP.
