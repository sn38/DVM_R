<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DV-Maths</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="js/bootstrap.min.js">
    <link rel="stylesheet" href="index.html">
</head>
<body>
    <!----Header---->
    <div class="container-fluid bandeau_haut">
        <h1>DV-MATH</h1>
        <p>La calculatrice à cellules braille pour deficients visuels...</p>
    </div>
    <!----Fin header---->

    <!----Menu---->
    <div class="container">
        <div class="btn-group btn-group-toggle groupe_de_boutons" data-toggle="buttons">
            <label class="btn btn-secondary bouton_1">
                <a class="bouton_index" href="index.php"><p>Déconnexion</p></a>
            </label>
            <label class="btn btn-secondary bouton_2">
                <a class="bouton_index" href="new_exo.php"><p>Ajouter un exercice</p></a>
            </label>
            <label class="btn btn-secondary bouton_3">
                <a class="bouton_index" href="bilan_prof.php"><p>Bilan professeurs</p></a>
            </label>
        </div>
    
      <!----Fin menu---->
      
    <?php
                session_start();
                if($_SESSION['username'] !== ""){
                    $user = $_SESSION['username'];
                    // afficher un message
                  ?>
                   
                <div class="message_user_connexion">
                      <?php

                    echo "Bonjour $user, vous êtes connecté !";
                }
    ?>
                </div>
    </div>           

             

    

</body>
</html>