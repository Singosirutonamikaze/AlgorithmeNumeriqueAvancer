/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package gestionetablissement;
/**
 *
 * @author DELL LATITUDE
 */
public class GestionEtablissement {

    public static void main(String[] args){
        // TODO code application logic here
        //Nouveau etablissement
        Etablissement etablissement1 = new Etablissement("Ecole Polytechnique de Lomé", "26/09/1970");
        Etablissement etablissement2 = new Etablissement("Ecole superieure des Affaires","20/10/2005");
        
        //Nouveau Parcours
        Parcours parcours1 = new Parcours("Genie Mécanique", "3ans");
        Parcours parcours2 = new Parcours("Genie Civile", "3ans");
        Parcours parcours3 = new Parcours("Genie Informatique", "3ans");
        Parcours parcours4 = new Parcours("Logisique et Transport", "3ans");
        Parcours parcours5 = new Parcours("Intelligence Artificielle et Big Data", "3ans");
        
        //Création des UEs
        UniteEnseignement uniteEnseignement1 = new UniteEnseignement("INF1241", "POO", 5);
        UniteEnseignement uniteEnseignement2 = new UniteEnseignement("MTH1213", "Algèbre linéaire de base", 4);
        UniteEnseignement uniteEnseignement3 = new UniteEnseignement("INF1423", "Algorithme", 4);
        UniteEnseignement uniteEnseignement4 = new UniteEnseignement("INF1345", "Developpement Dynamique", 4);
        
        //Ajout des ordinateur
        Ordinateur ordinateur0 = new Ordinateur(1, "Dell", "Latitude");
        Ordinateur ordinateur1 = new Ordinateur(2, "HP", "Pavilion");
        Ordinateur ordinateur2 = new Ordinateur(3, "Lenovo", "ThinkPad");
        Ordinateur ordinateur3 = new Ordinateur(4, "Apple", "MacBook Pro");
        Ordinateur ordinateur4 = new Ordinateur(5, "Asus", "ZenBook");
        Ordinateur ordinateur5 = new Ordinateur(6, "Acer", "Aspire");
        Ordinateur ordinateur6 = new Ordinateur(7, "Microsoft", "Surface Laptop");
        Ordinateur ordinateur7 = new Ordinateur(8, "Razer", "Blade");
        Ordinateur ordinateur8 = new Ordinateur(9, "Samsung", "Galaxy Book");
        Ordinateur ordinateur9 = new Ordinateur(10, "Toshiba", "Satellite");

        //creation d'un nouveau etudiant
        Etudiant etudiant1 = new Etudiant(1234, "KPONOU", "Ephraïm", "07/10/2005", "ephraim@gmail.com", 90575846);
        Etudiant etudiant2 = new Etudiant(1235, "MESSAN", "Elom Raïssa", "05/01/2007", "elom@gmail.com", 90575846);
        Etudiant etudiant3 = new Etudiant(1236, "ASSOUN", "Rodrigue", "06/07/2004", "rodrigue@gmail.com", 90575845);
        Etudiant etudiant4 = new Etudiant(1237, "TCHAMIE", "jephte", "07/06/2005", "jephte@gmail.com", 90575846);
        Etudiant etudiant5 = new Etudiant(1238, "SINGO","Yao Dieu Donné", "05/01/2006", "yaodieudonne@gmail.com", 90575846);
        Etudiant etudiant6 = new Etudiant(1239, "AKAM-YIKPO", "Eyram","02/01/2006", "eyram@gmail.com",90575846);
        Etudiant etudiant7 = new Etudiant(1240, "AKAM-YIKPO", "Etiam","02/01/2006", "etiam@gmail.com", 90575846);
        Etudiant etudiant8 = new Etudiant(1241, "DOBOU", "felix", "07/04/2005", "felix@gmail.com", 90575846);
        Etudiant etudiant9 = new Etudiant(1242, "GOMADO", "fritz", "07/03/2006","fritz@gmail.com", 90575846);
        Etudiant etudiant10 = new Etudiant(1243, "GEORGE", "Whashigton", "07/10/2003", "whashington@gmail.com", 90575846);
        
        //Affectation de l'ordinateur à l'étudiant
        etudiant1.setOrdinateur(ordinateur0);
        etudiant2.setOrdinateur(ordinateur1);
        etudiant3.setOrdinateur(ordinateur2);
        etudiant4.setOrdinateur(ordinateur3);
        etudiant5.setOrdinateur(ordinateur4);
        etudiant6.setOrdinateur(ordinateur5);
        etudiant7.setOrdinateur(ordinateur6);
        etudiant8.setOrdinateur(ordinateur7);
        etudiant9.setOrdinateur(ordinateur8);
        etudiant10.setOrdinateur(ordinateur9);
        
        //Inscrire les etudiant a l'UE
        InscriptionUE inscription1 = new InscriptionUE(etudiant1, uniteEnseignement1, 15.5);
        InscriptionUE inscription2 = new InscriptionUE(etudiant1, uniteEnseignement2, 16.5);
        InscriptionUE inscription3 = new InscriptionUE(etudiant1, uniteEnseignement3, 17.5);
        InscriptionUE inscription4 = new InscriptionUE(etudiant1, uniteEnseignement4, 19.5);
        
        //Inscrire les etudiant a l'UE
        InscriptionUE inscription5 = new InscriptionUE(etudiant2, uniteEnseignement1, 18.5);
        InscriptionUE inscription6 = new InscriptionUE(etudiant2, uniteEnseignement2, 11.5);
        InscriptionUE inscription7 = new InscriptionUE(etudiant2, uniteEnseignement3, 13.5);
        InscriptionUE inscription8 = new InscriptionUE(etudiant2, uniteEnseignement4, 17.5);
         // Inscrire les autres étudiants à des UEs
        InscriptionUE inscription9 = new InscriptionUE(etudiant3, uniteEnseignement1, 14.0);
        InscriptionUE inscription10 = new InscriptionUE(etudiant3, uniteEnseignement2, 12.5);
        InscriptionUE inscription11 = new InscriptionUE(etudiant3, uniteEnseignement3, 15.5);
        InscriptionUE inscription12 = new InscriptionUE(etudiant3, uniteEnseignement4, 16.0);

        InscriptionUE inscription13 = new InscriptionUE(etudiant4, uniteEnseignement1, 10.5);
        InscriptionUE inscription14 = new InscriptionUE(etudiant4, uniteEnseignement2, 13.5);
        InscriptionUE inscription15 = new InscriptionUE(etudiant4, uniteEnseignement3, 14.5);
        InscriptionUE inscription16 = new InscriptionUE(etudiant4, uniteEnseignement4, 15.5);

        InscriptionUE inscription17 = new InscriptionUE(etudiant5, uniteEnseignement1, 16.0);
        InscriptionUE inscription18 = new InscriptionUE(etudiant5, uniteEnseignement2, 17.0);
        InscriptionUE inscription19 = new InscriptionUE(etudiant5, uniteEnseignement3, 18.5);
        InscriptionUE inscription20 = new InscriptionUE(etudiant5, uniteEnseignement4, 19.0);

        InscriptionUE inscription21 = new InscriptionUE(etudiant6, uniteEnseignement1, 15.0);
        InscriptionUE inscription22 = new InscriptionUE(etudiant6, uniteEnseignement2, 14.5);
        InscriptionUE inscription23 = new InscriptionUE(etudiant6, uniteEnseignement3, 13.5);
        InscriptionUE inscription24 = new InscriptionUE(etudiant6, uniteEnseignement4, 12.0);

        InscriptionUE inscription25 = new InscriptionUE(etudiant7, uniteEnseignement1, 11.5);
        InscriptionUE inscription26 = new InscriptionUE(etudiant7, uniteEnseignement2, 14.0);
        InscriptionUE inscription27 = new InscriptionUE(etudiant7, uniteEnseignement3, 13.0);
        InscriptionUE inscription28 = new InscriptionUE(etudiant7, uniteEnseignement4, 10.5);

        InscriptionUE inscription29 = new InscriptionUE(etudiant8, uniteEnseignement1, 17.5);
        InscriptionUE inscription30 = new InscriptionUE(etudiant8, uniteEnseignement2, 16.0);
        InscriptionUE inscription31 = new InscriptionUE(etudiant8, uniteEnseignement3, 18.0);
        InscriptionUE inscription32 = new InscriptionUE(etudiant8, uniteEnseignement4, 19.0);

        InscriptionUE inscription33 = new InscriptionUE(etudiant9, uniteEnseignement1, 14.5);
        InscriptionUE inscription34 = new InscriptionUE(etudiant9, uniteEnseignement2, 15.0);
        InscriptionUE inscription35 = new InscriptionUE(etudiant9, uniteEnseignement3, 13.0);
        InscriptionUE inscription36 = new InscriptionUE(etudiant9, uniteEnseignement4, 12.5);

        InscriptionUE inscription37 = new InscriptionUE(etudiant10, uniteEnseignement1, 10.0);
        InscriptionUE inscription38 = new InscriptionUE(etudiant10, uniteEnseignement2, 11.0);
        InscriptionUE inscription39 = new InscriptionUE(etudiant10, uniteEnseignement3, 12.0);
        InscriptionUE inscription40 = new InscriptionUE(etudiant10, uniteEnseignement4, 13.5);

        
        //Ajouter les parcours au établissements 
        etablissement1.AjouterParcours(parcours1);
        etablissement1.AjouterParcours(parcours2);
        etablissement1.AjouterParcours(parcours3);
        
        etablissement2.AjouterParcours(parcours3);
        etablissement2.AjouterParcours(parcours4);
        etablissement2.AjouterParcours(parcours5);
        
        //Ajouter les étudiants au parcours
        parcours1.ajouterEtudiant(etudiant9);
        parcours1.ajouterEtudiant(etudiant8);
        
        parcours2.ajouterEtudiant(etudiant7);
        parcours2.ajouterEtudiant(etudiant6);
        
        parcours3.ajouterEtudiant(etudiant5);
        parcours3.ajouterEtudiant(etudiant4);
        
        parcours4.ajouterEtudiant(etudiant3);
        parcours4.ajouterEtudiant(etudiant2);
        
        parcours5.ajouterEtudiant(etudiant1);
        parcours5.ajouterEtudiant(etudiant10);
        
        //Afficher Les Etablissements
        etablissement1.afficherEtablissement();
        etablissement2.afficherEtablissement();
        
        //Afficher les parcours et les etudiants dans les parcours
        parcours1.afficherParcours();
        parcours2.afficherParcours();
        parcours3.afficherParcours();
        parcours4.afficherParcours();
        parcours5.afficherParcours();
        
        //Afficher les UES
        uniteEnseignement1.afficheUE();
        uniteEnseignement2.afficheUE();
        uniteEnseignement3.afficheUE();
        uniteEnseignement4.afficheUE();     
        
        //Afficher les étudiant
        etudiant1.afficherEtudiant();
        etudiant2.afficherEtudiant();
        etudiant3.afficherEtudiant();
        etudiant4.afficherEtudiant();
        etudiant5.afficherEtudiant();
        etudiant6.afficherEtudiant();
        etudiant7.afficherEtudiant();
        etudiant8.afficherEtudiant();
        etudiant9.afficherEtudiant();
        etudiant10.afficherEtudiant();
        
        //Afficher les UEs et les Etudiants incrits dans UES
        inscription1.afficherInscription();
        inscription2.afficherInscription();
        inscription3.afficherInscription();
        inscription4.afficherInscription();
        inscription5.afficherInscription();
        inscription6.afficherInscription();
        inscription7.afficherInscription();
        inscription8.afficherInscription();
        inscription9.afficherInscription();
        inscription10.afficherInscription();
        inscription11.afficherInscription();
        inscription12.afficherInscription();
        inscription13.afficherInscription();
        inscription14.afficherInscription();
        inscription15.afficherInscription();
        inscription16.afficherInscription();
        inscription17.afficherInscription();
        inscription18.afficherInscription();
        inscription19.afficherInscription();
        inscription20.afficherInscription();
        inscription21.afficherInscription();
        inscription22.afficherInscription();
        inscription23.afficherInscription();
        inscription24.afficherInscription();
        inscription25.afficherInscription();
        inscription26.afficherInscription();
        inscription27.afficherInscription();
        inscription28.afficherInscription();
        inscription29.afficherInscription();
        inscription30.afficherInscription();
        inscription31.afficherInscription();
        inscription32.afficherInscription();
        inscription33.afficherInscription();
        inscription34.afficherInscription();
        inscription35.afficherInscription();
        inscription36.afficherInscription();
        inscription37.afficherInscription();
        inscription38.afficherInscription();
        inscription39.afficherInscription();
        inscription40.afficherInscription();
        
        //Afficher les étudiant et leur moyenne
        // Liste des étudiants
        Etudiant[] etudiants = {etudiant1, etudiant2, etudiant3, etudiant4, etudiant5, 
                                etudiant6, etudiant7, etudiant8, etudiant9, etudiant10};

        // Afficher la moyenne générale de chaque étudiant
        for (Etudiant etudiant : etudiants) {
            etudiant.afficherEtudiantEtMoyenne();
        }
        
        /*/ Afficher les parcours et les étudiants dans les parcours
        Parcours[] parcoursArray = {parcours1, parcours2, parcours3, parcours4, parcours5};
        for (Parcours parcours : parcoursArray) {
            parcours.afficherParcours();
        }

        // Afficher les UEs
        UniteEnseignement[] ueArray = {uniteEnseignement1, uniteEnseignement2, uniteEnseignement3, uniteEnseignement4};
        for (UniteEnseignement ue : ueArray) {
            ue.afficheUE();
        }

        // Afficher les étudiants
        Etudiant[] etudiantsArray = {
            etudiant1, etudiant2, etudiant3, etudiant4, etudiant5, 
            etudiant6, etudiant7, etudiant8, etudiant9, etudiant10
        };
        for (Etudiant etudiant : etudiantsArray) {
            etudiant.afficherEtudiant();
        }*/

        /*/ Afficher les inscriptions aux UEs
        InscriptionUE[] inscriptionsArray = {
            inscription1, inscription2, inscription3, inscription4, inscription5, 
            inscription6, inscription7, inscription8, inscription9, inscription10, 
            inscription11, inscription12, inscription13, inscription14, inscription15, 
            inscription16, inscription17, inscription18, inscription19, inscription20, 
            inscription21, inscription22, inscription23, inscription24, inscription25, 
            inscription26, inscription27, inscription28, inscription29, inscription30, 
            inscription31, inscription32, inscription33, inscription34, inscription35, 
            inscription36, inscription37, inscription38, inscription39, inscription40
        };*/
        // for (InscriptionUE inscription : inscriptionsArray) {
           //  inscription.afficherInscription();
        // }

        // Afficher les étudiants et leur moyenne
        // for (Etudiant etudiant : etudiantsArray) {
        //     etudiant.afficherEtudiantEtMoyenne();
        // }

    }
    
}
