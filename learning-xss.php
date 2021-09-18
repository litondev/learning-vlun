<?php 
// allow a
// delete javascript: and onclick= dari tag

// echo str_replace('javascript:','',str_replace("onclick=", "",strip_tags($_GET['name'],'<a>'))) ?? 'testing';
echo $_GET['name'];
?>

<form method="get">
	<input type="text" name="name">
	<button>Kirim</button>
</form>