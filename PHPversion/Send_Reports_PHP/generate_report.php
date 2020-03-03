<?php
include_once 'Includes/database_connection.php';

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbDatabase);
header('Content-Type: text/csv; charser=utf-8');
header('Content-Disposition: attachment; filename=data.csv');
$output = fopen("output.csv", "w");
fputcsv($output, array('Column1', 'Column2'));
$query = "";
$result = mysqli_query($conn, $query);
while($row = mysqli_fetch_assoc($result))
{
  fputcsv($output, $row);
}
fclose($output);

include_once 'send_email.php';
