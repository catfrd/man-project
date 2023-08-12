<?php
$errors = array();
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','regdb');
// get the post records
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = test_input($_POST["name"]);
    $institution = test_input($_POST["institution"]);
    $department = test_input($_POST["Department"]);
    $event = test_input($_POST["event"]);
    $email = test_input($_POST["email"]);
    $mobile_number = test_input($_POST["mobile_number"]);

    // Basic validation
    if (empty($name)) {
        $errors["name"] = "Name is required";
    }

    if (empty($institution)) {
        $errors["institution"] = "Institution name is required";
    }

    if (empty($department)) {
        $errors["department"] = "Department name is required";
    }

    if ($event === "select") {
        $errors["event"] = "Please select an event";
    }

    if (empty($email)) {
        $errors["email"] = "Email is required";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors["email"] = "Invalid email format";
    }

    if (empty($mobile_number)) {
        $errors["mobile_number"] = "Mobile number is required";
    }

    // If there are no errors, you can proceed to save the data or perform other actions
    if (empty($errors)) {
        // database insert SQL code
        $sql = "INSERT INTO `registration_details` ( `Name`, `Institution`, `Department`,`event`,`Email`,) VALUES ( '$Name', '$Email', '$pass')";
        // insert in database 
        $rs = mysqli_query($con, $sql);
        if($rs)
            {
                include('success.html');
            }

        // Perform registration process here (e.g., save to database)
        // Redirect to a success page or perform other actions
       
        // header("Location: success.php");
        exit();
    }
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>
    <h2>Registration Form</h2>
    <?php if (!empty($success_message)): ?>
        <p style="color: green;"><?php echo $success_message; ?></p>
    <?php endif; ?>
    <form action="register_logic.php" method="post">
        <<label for="name">Name</label>
        <input type="text" id="name" name="name"> <br>
        <span style="color: red;"><?php echo $errors["name"]; ?> </span> <br>
        
        <label for="institution">Name of the institution </label>
        <input type="text" id="institution" name="institution">
        <span style="color: red;"><?php echo $errors["institution"]; ?></span> <br>

        <label for="Department">Department</label>
        <input type="text" id="Department" name="Department">
        <span style="color: red;"><?php echo $errors["department"]; ?></span> <br>

        <label for="event">Choose an Event</label>
        <select name="event" id="event">
          <option value="select">Select </option>
          <option value="master_of_masters">Master of Masters</option>
          <option value="auction play">Auction Play</option>
          <option value="haccer_mimica">Haccer Mimica</option>
          <option value="Guessing_guns">Guessing Guns</option>
          <option value="the_alpinist">The Alpinsit</option>
          <option value="Sorting_the_choas">Sorting the Choas</option>
          <option value="ted_talks">Ted Talks</option>
          <option value="extremepore">Extremepore</option>
          <option value="tuzel_strut">Tuzel Strut</option>
          <option value="hr_mind_maze">HR Mind Maze</option>
        </select>
        <span style="color: red;"><?php echo $errors["event"]; ?></span> <br>

        <label for="email">Email</label>
        <input type="email" id="email" name="email">
        <span style="color: red;"><?php echo $errors["email"]; ?></span> <br>

        <label for="mobile_number">Mobile Number</label>
        <input type="tel" id="mobile_number" name="mobile_number">
        <span style="color: red;"><?php echo $errors["mobile_number"]; ?></span> <br>
        <input type="submit" value="Register" class="btn btn-base-color sm-btn-medium btn-large">
    </form>
</body>
</html>











 