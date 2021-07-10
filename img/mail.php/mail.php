<?php
//get data from form  
$name = $_POST['name'];
$phone = $_POST['phone'];
$email= $_POST['email'];
$message= $_POST['message'];
$to = "ayush.negi082004@gmail.com";
$subject = "Mail From HSGA";
$txt ="Name = ". $name . "\r\n  Email = " . $email . "\r\n Message =" . $message;."\r\n Phone =" . $phone;
$headers = "From: noreply@HSGA.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:thankyou.html");
?>