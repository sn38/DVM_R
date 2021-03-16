<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../index.html">
    
</head>
<body>
     <!-- Header -->
    <div class="accueilhaut">
        <table class="header">          
            <thead>
                <tr>
                    <div class="hm1">
                        <h1> DVMath-R </h1>
                    </div>
            
                </tr>
            </thead>   
            <tbody>
                <tr>
                    <div class="descriptionh1">
                        <p> La calculatrice a cellules braille pour des  déficients visuels..</p>
                    </div>
                </tr>   
            </tbody>
        </table>
    </div>
    
     
     <div class="connexion">  

        <a class="button" href="../index.html"><h4> Déconnexion</h4></a>
    </div>

    <div class="textexo">
        <h2>Créer des exercices</h2>
        
    
        <?php
        
       
		$mysqli = new mysqli("localhost", "root", "", "historisation");
		$mysqli -> set_charset("utf8");
		$requete = "SELECT * FROM bilan";
		$resultat = $mysqli -> query($requete);
        
        
        echo'<table><tr><td>Nom</td><td>Niveau</td>  <td>Calcul_donne</td>  <td>Caclcul_pose</td>  <td>resultat</td>  <td> resultat_attendu </td></tr>';
	
		while ($ligne = $resultat -> fetch_assoc()) {
            
			echo '<tr><td>'.$ligne['nom'] . '</td><td>' . $ligne['niveau'] .'</td><td>'. $ligne['calcul_donne'] . '</td><td>' . $ligne['calcul_pose']. '</td><td>' . $ligne['resultat']. '</td><td>' . $ligne['resultat_attendu']. '</td></tr>';
			
		}
        echo'</table>';
    
		$mysqli->close();
    	?>
    </div>
 </body>          

     