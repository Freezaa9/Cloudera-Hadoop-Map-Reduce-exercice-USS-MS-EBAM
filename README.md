# Cloudera-Hadoop-Map-Reduce-exercice-USS-MS-EBAM
3 training example of Map and Reduce fonction on Cloudera platform

https://www.cloudera.com/downloads/quickstart_vms/5-13/config.html

**VMWARE Cloudera Quickstart virtual machine**
https://downloads.cloudera.com/demo_vm/vmware/cloudera-quickstart-vm-5.13.0-0-vmware.zip

**Local test MAP and REDUCE fonction:**
**MAP**
echo " A A B B C C D D D D D D " | ./mapper.py
cat ./data.csv | ./mapper.py
**MAP and REDUCE**
cat ./data.csv | ./mapper.py | ./reducer.py

**MAP and REDUCE fonction with HADOOP:**
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.13.0.jar 
-input /home/cloudera/shares/partage/data.csv 
-mapper "/home/cloudera/shares/partage/mapper.py" 
-reducer "/home/cloudera/shares/partage/reducer.py" 
-output out

**Atelier 1: Total des ventes par magasin **
L’objectif : 
	Se familiariser avec le traitement distribué
	Utilisation du langage python pour la création des fonctions Map et Reduce
	Analyse des résultats.
Emplacement du fichier : /formation/ateliers/mapreduce/
Réalisation : Vous allez copier, supprimer plusieurs fichiers de données dans HDFS
Chapitre correspondant : HadoopDistributed File System (MapReduce) 


Nous allons utiliser un fichier input sous la forme suivant:
	 date | temps | magasin| produit | cout | paiement

Un exemple du contenu du fichier input : 

15/10/2019|16:40|paris|ballon |1000|cb
15/10/2019|11:49|nice|t-shirt|3000|cash
15/10/2019|13:07|bordeaux|ballon |1500|cheque
15/10/2019|10:02|paris|soulier|1900|cash
15/10/2019|16:40|dreux|xbox|350|cb
15/10/2019|11:49|lyon|iphone|999|cash
15/10/2019|13:07|lille|montre|150|cheque
15/10/2019|10:02|nante|jus orange|2|cash
15/10/2019|16:40|rennes|eau|4|cb
15/10/2019|11:49|nancy|ballon |1000|cb



1-	Transférer le fichier data.csv dans HDFS 
2-	Écrire les deux fonctions  map et reduce qui ont pour but de  calculer le total des ventes par magasin 
a.	Tester les deux fonctions en local 
b.	Une fois le test en local est ok lancer le traitement sur hadoop 
i.	Avant de lancer assurez-vous que le répertoire out n’existe pas et si c’est le cas supprimez le ==> hadoop fs -rm -r out 
c.	Lire le résultat sur Hadoop 



**Atelier 2: Calcul du salaire Min et Max**
L’objectif :

Se familiariser avec le traitement distribué

Utilisation du langage python pour la création des fonctions Map et Reduce

Analyse des résultats.
Emplacement du fichier : /formation/ateliers/mapreduce/
Réalisation : Vous allez copier, supprimer plusieurs fichiers de données dans HDFS
Chapitre correspondant : HadoopDistributed File System (MapReduce)
Nous allons utiliser un fichier input sous la forme suivant:
ID ; Age ; Sexe ; Ville ; Salaire
Un exemple du contenu du fichier input :
1;22;homme;Lille;22000
2;22;homme;Dreux;14000
3;22;homme;Stratsbourg;22000
4;22;homme;Rennes;21500
5;22;homme;Nice;22000
6;22;homme;Nantes;24000
7;22;homme;Lyon;26000
8;22;homme;Chartres;20000
1- Transférer le fichier data.csv dans HDFS
2- Écrire les deux fonctions map et reduce qui ont pour but de calculer le salaire min et max par
tranche par Age et le nombre d’échantillon utilisé.
a. Tester les deux fonctions en local
b. Une fois le test en local est ok lancer le traitement sur hadoop
i. Avant de lancer assurez-vous que le répertoire out n’existe pas et si c’est le
cas supprimez le ==> hadoop fs -rm -r out
c. Lire le résultat sur Hadoop
3- Écrire les deux fonctions map et reduce qui ont pour but de calculer le salaire min et max par
Ville et le nombre d’échantillon utilisé.
a. Tester les deux fonctions en local
b. Une fois le test en local est ok lancer le traitement sur hadoop
i. Avant de lancer assurez-vous que le répertoire out n’existe pas et si c’est le
cas supprimez le ==> hadoop fs -rm -r out
c. Lire le résultat sur Hadoop
4- Écrire les deux fonctions map et reduce qui ont pour but de calculer le salaire moyen par ville
et par tranche d’age.
a. Tester les deux fonctions en local
b. Une fois le test en local est ok lancer le traitement sur hadoop
i. Avant de lancer assurez-vous que le répertoire out n’existe pas et si c’est le
cas supprimez le ==> hadoop fs -rm -r out
c. Lire le résultat sur Hadoop
