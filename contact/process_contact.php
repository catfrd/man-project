<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    require 'PHPMailer/PHPMailerAutoload.php';

    $mail = new PHPMailer;
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->Port = 587;
    $mail->SMTPAuth = true;
    $mail->SMTPSecure = 'tls';
    $mail->Username = 'frdofmoon@gmail.com'; // Your Gmail email address
    $mail->Password = 'Rofl6060'; // Your Gmail password
    $mail->setFrom('your@gmail.com', 'Your Name');
    $mail->addAddress('recipient@example.com'); // Recipient's email address
    $mail->Subject = 'Contact Form Submission';
    $mail->Body = "Name: $name\nEmail: $email\nMessage: $message";

    if ($mail->send()) {
        echo "Message sent successfully.";
    } else {
        echo "Error sending message: " . $mail->ErrorInfo;
    }
}
?>
