<?php
include_once 'dbh.php';
$id=$_POST['id'];
$delete = "DELETE FROM orders_notification WHERE id=$id";
$result=mysqli_query($conn,$delete);
?>