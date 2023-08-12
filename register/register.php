<?php

// Validate the user input.
$name = $_POST['name'];
$institution=$_POST['institution'];
$department=$_POST['Department'];
$event=$_POST['event'];
$email = $_POST['email'];
$mobile_number= $_POST['mobile_number'];


if (empty($name)) {
  echo "Name is required";
} else {
  $name = test_input($name);
  if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
    echo "Only letters and white space allowed";
  }
}

if (empty($institution)) {
    echo "Institution is required";
  } else {
    $institution = test_input($institution);
    if (strlen($institution) < 8) {
      echo "Invalid";
    }
  }
  
if (empty($department)) {
    echo "Department is required";
  } 

  
if ($event == "") {
echo "Please select an event.";
} else {
echo "You have selected $event.";
}
  

if (empty($email)) {
  echo "Email is required";
} else {
  $email = test_input($email);
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "Invalid email format";
  }
}


if (empty($mobile_number)) {
  echo "Contact number is required";
} else {
  $mobile_number = test_input($mobile_number);
  if (strlen($mobile_number)!=10) {
    echo "Invalid Contact number";
  } 
}

// Collect the validated data.
$name = $_POST['name'];
$institution=$_POST['institution'];
$department=$_POST['Department'];
$event=$_POST['event'];
$email = $_POST['email'];
$mobile_number= $_POST['mobile_number'];

// Store the data in an SQL database.
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "regdb";

// Create connection
$conn = new mysqli_connect('localhost', 'root', '','regdb');
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO registration Details ()
VALUES ('John', 'Doe', 'john@example.com')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}