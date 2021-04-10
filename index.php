<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DV-Maths</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="index.html">
</head>
<body>
    <!----Header---->
    <div class="container-fluid bandeau_haut">
        <h1>DV-MATH</h1>
        <p>La calculatrice à cellules braille pour deficients visuels...</p>
    </div>
    <!----Fin header---->
  
    <!----Debut Connexion----->
    <div class="simple-login-container">
        <h2>Connexion à une session professeur</h2>
        <form action="verification.php" method="POST">
            <div class="row">
                <div class="col-md-12 form-group">
                    <input type="text" class="form-control" placeholder="Nom de compte" name="username" required>
                 </div>
            </div>
            <div class="row">
                <div class="col-md-12 form-group">
                    <input type="password"  placeholder="Mot de passe" class="form-control " name="password" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                    <input type="submit" id='submit' class='btnn_connexion' value='Connexion' >
                </div>
            </div>   
        </form>

          <?php
                if(isset($_GET['erreur'])){
                    $err = $_GET['erreur'];
                    if($err==1 || $err==2)
                        echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
                }
                ?>
    </div>
    
              

    <!----Fin Connexion----->
    
    <?php include("pied_page.php"); ?> 

</body>
</html>