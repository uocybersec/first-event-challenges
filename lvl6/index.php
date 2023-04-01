<?php
    $flag = "CSC{fake_flag}";
    
    function hashing_function($password) {
        return hash('md5', hash('md5', $password));
    }

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username != null && $password != null) {
        if ($username == "admin" && hashing_function($password) == "0e910057037170584158391016456192") {
            echo "<h3 style='color: lime;'>ACCESS GRANTED!</h3><pre>" . $flag . "</pre>";
        } else {
            echo "<h3 style='color: darkred;'>ACCESS DENIED.</h3>";
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
</head>
<body style="background-color: grey; font-family: arial; padding: 25px;">
    <h2 style="width: 500px">Administrator Login</h2>
    <form method='POST' action=''>
        <input name='username' type='text' placeholder='Username'/><br>
        <input name='password' type='password' placeholder='Password'/><br>
        <input type='submit' value='Login'/>
    </form>
</body>
</html>