<?php 
	/* TABLE 1 => test */
		/*
			id => int,autoincrement,
			nama => varchar(10),
			no => int
		*/

	/* Table 2 => test1 */
		/*
			id  => int,autoincrement,
			password => varchar(10),
			nama => varchar(10)
		*/

	$koneksi = mysqli_connect("localhost","root","","penetrasi");

	if(isset($_GET['id'])){
		$id = $_GET['id'];
		
		/* Test 1 => BREAK SQL */
			// Mengunakan (test1'--') untuk mendisabled (AND no='1')
			// $data = mysqli_query($koneksi,"SELECT * FROM test WHERE nama='$id' AND no='1'");
			// print_r(mysqli_num_rows($data));

		/* Test 2 => BREAK SQL AND SEE DATA */
			// Mengunakan ('1' OR 1=1) untuk mengambil semua data
			// Atau
			// Mengunakn ('1' or 1=1;) untuk mengambil semua data

			// Mengunakan ('1' UNION select * from test1) untuk mengambil data dari table test1 lalu menampilkan dengan kolom test

			// Mengunakan ('1' or sleep(3);) untuk mengetahui paling mudah kalau vlun

			// $data = mysqli_query($koneksi,"SELECT * FROM test WHERE no=$id");
			// print_r(mysqli_num_rows($data));	

			// if(mysqli_num_rows($data) > 0){
			// 	while($item = mysqli_fetch_array($data)){
			// 		echo "<br>";
			// 		echo "Nama : ".$item['nama'];
			// 		echo "<br>";
			// 		echo "No :".$item['no'];
			// 		echo "<br><br>";
			// 	}
			// }	

		/* Test 3 => UPDATE DATA */
			// Mengunakan (namaTest' where id=3 -- ') untuk mengupdate nama id=3

			// Mengunakan (test2',no=4 where id=3 -- ') untuk menngupdate nama dan no id=3

			// $nameTest = $_GET['nama'] ?? "Nama Test".rand(0,4);
			// $data = mysqli_query($koneksi,"UPDATE test SET nama='$nameTest' where id=$id");
			// print_r(mysqli_affected_rows($koneksi));		
	}
?>

<form method="GET">		
	<input tyep="text" name="nama">
	<input type="text" name="id">
	<button>Kirim</button>
</form>