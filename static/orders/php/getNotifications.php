<?php
include_once 'dbh.php';
mysqli_set_charset($conn,'utf8');

$sql = "SELECT * FROM orders_notification";
$result=mysqli_query($conn,$sql);
/*$array = array(
	'notifications' => array(),
);

$i = 0;
while ($row = mysqli_fetch_array($result)) {
	$array['notifications'][$i++] = $row;
}

$json = json_encode($array);*/
$json = json_encode($result)
echo $json;
?>