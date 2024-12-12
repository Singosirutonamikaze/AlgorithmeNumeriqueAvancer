/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gestionetablissement;

/**
 *
 * @author DELL LATITUDE
 */
public class InscriptionUE {
    private Etudiant etudiant;
    private UniteEnseignement uniteEnseignement;
    private float moyenne;
    
    public InscriptionUE(Etudiant etudiant1, UniteEnseignement uniteEnseignement1, double _moyenne) {
        this.etudiant = etudiant1;
        this.uniteEnseignement = uniteEnseignement1;
        this.moyenne = (float) _moyenne;
        etudiant.ajouterInscription(this);
    }
    
    //Les accesseurs 
    public Etudiant getEtudiant(){
        return etudiant;
    }
    
    public float getMoyenne(){
        return moyenne;
    }
    
    public UniteEnseignement getUniteEnseignement(){
        return uniteEnseignement;
    }   
    
    public void InscriptionUE(Etudiant _etudiant, UniteEnseignement _uniteEnseignement, float _moyenne) {
        if (moyenne >= 0 && moyenne <= 20) {
            this.etudiant = _etudiant;
            this.uniteEnseignement = _uniteEnseignement;
            this.moyenne = _moyenne;
        }else{
            System.out.println("La moyenne doit être compris entre 0 et 20");
        }    
    }
    // Setter pour mettre à jour la moyenne
    public void setMoyenne(float nouvelleMoyenne) {
        if (nouvelleMoyenne >= 0 && nouvelleMoyenne <= 20) {
            this.moyenne = nouvelleMoyenne;
        } else {
            System.out.println("La moyenne doit être comprise entre 0 et 20.");
        }
    }

    // Méthode pour afficher les informations de l'inscription
    public void afficherInscription() {
        System.out.println("Étudiant : " + this.etudiant.getNomEtudiant() + " | UE : " + this.uniteEnseignement.getCodeUE() + " | Moyenne : " + this.moyenne + "/20");
        System.out.println("");
    }
}
