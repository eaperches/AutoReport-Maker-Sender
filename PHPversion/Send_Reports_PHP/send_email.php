<?php
  require 'Includes/PHPMailer/src/Exception.php';
  require 'Includes/PHPMailer/src/PHPMailer.php';
  require 'Includes/PHPMailer/src/SMTP.php';

  use PHPMailer\PHPMailer\PHPMailer;
  use PHPMailer\PHPMailer\SMTP;
  use PHPMailer\PHPMailer\Exception;

  $mail = new PHPMailer(true);

  try {
      //Server settings
      $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      // Enable verbose debug output
      $mail->isSMTP();                                            // Send using SMTP
      $mail->Host       = 'smtp.gmail.com';                    // Set the SMTP server to send through
      $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
      $mail->Username   = '';                     // SMTP username
      $mail->Password   = '';                               // SMTP password
      $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` also accepted
      $mail->Port       = 587;                                    // TCP port to connect to

      //Recipients
      $mail->setFrom('', '');
      $mail->addAddress('', '');     // Add a recipient

      // Attachments
      $mail->addAttachment('output.csv', 'report.csv');         // Add attachments

      // Content
      $mail->isHTML(true);                                  // Set email format to HTML
      $mail->Subject = '';
      $mail->Body    = '';

      $mail->send();
      echo 'Message has been sent';
  } catch (Exception $e) {
      echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
  }
 ?>
