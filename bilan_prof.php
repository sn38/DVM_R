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
    <link rel="stylesheet" href="index.php">
</head>
<body>
    <!----Header---->
    <div class="container-fluid bandeau_haut">
        <h1>DV-MATH</h1>
        <p>La calculatrice à cellules braille pour deficients visuels...</p>
    </div>
    <!----Fin header---->


    <!----Menu---->
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

    <!----Début historique------>
    <div class="textexo cold-sm-1">
        <h2>Bilan professeur</h2>
        
    
        <?php
        
       
		$mysqli = new mysqli("localhost", "root", "", "historisation_eleves");
		$mysqli -> set_charset("utf8");
		$requete = "SELECT * FROM bilan";
		$resultat = $mysqli -> query($requete);
        ?>
        
    <table>
        
        <tr class="ligne1">
            <td>Nom</td>
            <td>Niveau</td>  
            <td>Calcul_donne</td>  
            <td>Caclcul_pose</td>  
            <td>resultat</td> 
             <td> resultat_attendu </td>
        </tr>
            <?php
                while ($ligne = $resultat -> fetch_assoc()) {
                        
                        echo '<tr><td>'.$ligne['nom'] . '</td><td>' . $ligne['niveau'] .'</td><td>'. $ligne['calcul_donne'] . '</td><td>'
                         . $ligne['calcul_pose']. '</td><td>' . $ligne['resultat']. '</td><td>' . $ligne['resultat_attendu']. '</td></tr>';
                        
                    }
                    echo'</table>';
                
                    $mysqli->close();
                    ?>
    </div>
     <!----Fin historique------>
</body>
</html>