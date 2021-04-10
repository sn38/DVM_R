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
    <div class="container">
        <div class="btn-group btn-group-toggle groupe_de_boutons" data-toggle="buttons">
            <label class="btn btn-secondary bouton_1">
                <a class="bouton_index" href="index.php"><p>Déconnexion</p></a>
            </label>
            <label class="btn btn-secondary bouton_2">
                <a class="bouton_index" href="new_exo.php"><p>Ajouter un exercice</p></a>
            </label>
            <label class="btn btn-secondary bouton_3 ">
                <a class="bouton_index" href="bilan_prof.php"><p>Bilan professeurs</p></a>
            </label>
        </div>
    <!----Fin menu---->
    
    <?php
	$db_servername  = "localhost";
	$db_username = "root";
	$db_password = "";
    
	$dbh = new PDO("mysql:host=$db_servername;dbname=historisation_eleves", $db_username, $db_password);
    

    if(isset($_POST['submit'])){ // si le bouton a été enclenché

        if(isset($_POST['Calcul'], $_POST['Resultat'], $_POST['Niveau'])){           
            if($_POST['Calcul'] !== ""  && $_POST['Resultat'] !== "" && $_POST['Niveau'] !==""){
                //Enregistrement bdd
                $Calcul= $_POST['Calcul'];
                $Resultat = $_POST['Resultat'];
                $Niveau = $_POST['Niveau'];
                $insert = "INSERT INTO creat_exo (exercice, resultat, niveau) VALUES('$Calcul', '$Resultat', '$Niveau')";   
                $execute = $dbh->query($insert); 

                if($execute == true){
                    
                    $msgSuccess = "L'exercice à été enregistré avec succès";

                }else{
                    $msgError = "L'enregistrement n'a pas pu être effectué";
                }
            }
        }
    }
    ?>
  

    <!----Debut formulaire et tableau---->
    <div class="col-md-9 container champs1">
        <div class="container">
            <h2 class="titre_H2">Ajouter un exercice</h2>
            <div class="row grid-divider">
                <div class="col-sm-3">
                    <div class="col-padding">
                        <form  action="" method="POST">
                            <div class="simple-login-container2 ">
                                <div class="row">
                                    <div class="col-md-12 form-group">
                                        <input type="text" name="Calcul" class="form-control" placeholder="Calcul" >
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-12 form-group">
                                        <input type="text" name="Resultat" class="form-control" placeholder="Resultat" >
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-12 form-group">
                                        <input type="text" placeholder="Niveau" class="form-control" name="Niveau">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-12 form-group3">
                                        <button type="submit" name="submit"class="btn btn-block btn-login2" placeholder="Enter your Password"> Enregistrer </button>
                                    </div>
                                </div>
                                <div class="row">      
                            </div>
                             </div>   
                                                  
                        </form>
                    </div>
                </div>
                <div class="col-sm-3">
                    <div class="col-padding">
                    <!--- du texte -->
                    </div>
                </div>
                <div class="col-sm-3">
                    <div class="col-padding">
                    <!--- du texte -->
                    </div>
                </div>
                <div class="col-sm-3">
                    <div class="col-padding">
                    <!--- du texte -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="cordon">
        <?php
            if(isset($msgError)){ echo $msgError; }elseif(isset($msgSuccess)){
                echo $msgSuccess;
            }

        ?>
    </div>
    
    
        <table class="tableauxajouterexo">
            
            <tr class="ligne1">
                <td>Numéro exercice</td>
                <td>Calcul</td>
                <td>Résultat</td>
                <td>Niveau</td>
            </tr>
               
            <?php
            $db_servername  = "localhost";
            $db_username = "root";
            $db_password = "";
                $requete = "SELECT * FROM creat_exo";
                $resultat = $dbh -> query($requete);

                while ($ligne=$resultat->fetch(PDO::FETCH_ASSOC)){
                        
                        echo '<tr><td>'.$ligne['numero']. '</td><td>'.$ligne['exercice'] . '</td><td>' . $ligne['resultat'] .'</td><td>'. $ligne['niveau'] . '</td></tr>';
                        
                    }
                    echo'</table>';
                
                    
                    ?>
        </table>
   </div>
</div>
<!----fin formulaire et tableau-->



</body>
</html>