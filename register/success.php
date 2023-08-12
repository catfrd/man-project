<!DOCTYPE html>
<html>
<head>
    <title>Registration Successful</title>
</head>
<body>
    <h2>Registration Successful</h2>
    <?php if (!empty($success_message)): ?>
        <p style="color: green;"><?php echo "Successfully Registered" ?></p>
        <p style="color: black ;"><?php echo "Hoping to meet you in person. " ?></p>
    <?php endif; ?>
</body>
</html>