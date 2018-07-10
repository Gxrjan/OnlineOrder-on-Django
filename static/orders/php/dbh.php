<?php

	$dbServername = "127.0.0.1";
	$dbUsername = "root";
	$dbPassword = "";
	$dbName = "onlineorder";

	$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

	if (!$conn) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}
?>