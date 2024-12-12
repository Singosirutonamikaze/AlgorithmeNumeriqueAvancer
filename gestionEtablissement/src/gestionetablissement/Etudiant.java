/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gestionetablissement;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author DELL LATITUDE
 */
public class Etudiant {
    private Ordinateur ordinateur;
    private Parcours parcourChoisi;
    private int numeroDeCarte;
    private String nomEtudiant;
    private String prenomEtudiant;
    private String dateDeNaissance;
    private String emailEtudiant; 
    private long telephoneEtudiant; 
    private float moyenneUE;
    private UniteEnseignement UniteEns;
    private List<InscriptionUE> inscriptions = new ArrayList<>();

    //constructeur
    public Etudiant(int _numeroDeCarte, String _nomEtudiant, String _prenomEtudiant, String _dateDeNaissance, String _emailEtudiant, long _telephoneEtudiant){
        this.numeroDeCarte = _numeroDeCarte;
        this.nomEtudiant = _nomEtudiant;
        this.prenomEtudiant = _prenomEtudiant;
        this.dateDeNaissance = _dateDeNaissance;
        this.emailEtudiant = _emailEtudiant;
        this.telephoneEtudiant = _telephoneEtudiant;
        this.inscriptions = new ArrayList<>();
    }
    
    //Les accesseurs en lecture et en ecriture
    //Ordinateur
    public Ordinateur getOdinateur(){
        return ordinateur;
    }
    
    public void setOrdinateur(Ordinateur _ordinateur){
        this.ordinateur = _ordinateur;
    }
    //Parcours
    public Parcours getParcourChoisi(){
        return parcourChoisi;
    }
    public void setParcourChoisi(Parcours _parcourChoisi) {
        this.parcourChoisi = _parcourChoisi;
    }
    //Numero de telephone
    public int getNumeroDeCarte() {
        return numeroDeCarte;
    }
    
    public void setNumeroDeCarte(int _numeroDeCarte) {
        this.numeroDeCarte = _numeroDeCarte;
    }
    //Nom Etudiant
    public String getNomEtudiant() {
        return nomEtudiant;
    }
    
    public void setNomEtudiant(String _nomEtudiant) {
        this.nomEtudiant = _nomEtudiant;
    }
    //prenom
    public String getPrenomEtudiant() {
        return prenomEtudiant;
    }

    public void setPrenomEtudiant(String _prenomEtudiant) {
        this.prenomEtudiant = _prenomEtudiant;
    }
    //Date  de Naissance
    public String getDateDeNaissance() {
        return dateDeNaissance;
    }

    public void setDateDeNaissance(String _dateDeNaissance) {
        this.dateDeNaissance = _dateDeNaissance;
    }
    //Email
    public String getEmailEtudiant() {
        return emailEtudiant;
    }

    public void setEmailEtudiant(String _emailEtudiant) {
        this.emailEtudiant = _emailEtudiant;
    }
    //Numero de telephone 
    public long getTelephoneEtudiant() {
        return telephoneEtudiant;
    }

    public void setTelephoneEtudiant(long _telephoneEtudiant) {
        this.telephoneEtudiant = _telephoneEtudiant;
    }
    //Moyenne de chaque Etudiant  dans l'UE
    public void setMoyenneUE(float _moyenneUE) {
        this.moyenneUE = _moyenneUE;
    }

    public float getMoyenneUE() {
        return moyenneUE;
    }
    
    public void setUniteEns(UniteEnseignement _UniteEns) {
        this.UniteEns = _UniteEns;
    }

    public Ordinateur getOrdinateur() {
        return ordinateur;
    }

    public UniteEnseignement getUniteEns() {
        return UniteEns;
    }
    
    
    // Méthode afficherEtudiant
    public void afficherEtudiant() {
        System.out.println("************** Informations de l'Étudiant *************** ");
        System.out.println("Nom : " + this.nomEtudiant);
        System.out.println("Prénom : " + this.prenomEtudiant);
        System.out.println("Date de naissance : " + this.dateDeNaissance);
        System.out.println("Email : " + this.emailEtudiant);
        System.out.println("Téléphone : " + this.telephoneEtudiant);
        System.out.println("Numéro de carte : " + this.numeroDeCarte);
        System.out.println("Parcours choisi : " + getParcourChoisi());
        System.out.println("Ordinateur attribué : ");
        if (ordinateur != null) {
            // Affichage des informations de l'ordinateur
            System.out.println("Marque : " + ordinateur.getMarque());
            System.out.println("Modèle : " + ordinateur.getModele());
            System.out.println("Numéro de série : " + ordinateur.getNumeroDeSerie());
        } else {
            System.out.println("Aucun ordinateur attribué.");
        }
        System.out.println(" ");
    }
    // Ajouter une inscription à l'étudiant
    public void ajouterInscription(InscriptionUE inscription) {
        inscriptions.add(inscription);
    }
    
    // Calculer la moyenne générale
    public float calculerMoyenneGenerale() {
        float sommeNotesPonderees = 0;
        int sommeCoefficients = 0;

        for (InscriptionUE inscription : inscriptions) {
            UniteEnseignement ue = inscription.getUniteEnseignement();
            float moyenne = inscription.getMoyenne();
            int coefficient = ue.getCoefficient();

            sommeNotesPonderees += moyenne * coefficient;
            sommeCoefficients += coefficient;
        }

        if (sommeCoefficients == 0){
            return 0;
        } // Éviter la division par zéro
        
        return sommeNotesPonderees / sommeCoefficients;
    }

    // Afficher les détails de l'étudiant
    public void afficherEtudiantEtMoyenne() {
        System.out.println("Numero de carte : " + this.numeroDeCarte + " | Nom : " + this.nomEtudiant + " | Prénom : " + this.prenomEtudiant);
        System.out.println("Moyenne Générale : " + calculerMoyenneGenerale() + "/20");
        System.out.println(" ");
    }
    
}
