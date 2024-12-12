/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gestionetablissement;

/**
 *
 * @author DELL LATITUDE
 */
public class Ordinateur {
    private Etudiant proprietaire;
    private int numeroDeSerie;
    private String marque;
    private String modele;
    
    //Constructeur
    public Ordinateur(int _numeroDeSerie, String _marque, String _modele) {
        this.numeroDeSerie = _numeroDeSerie;
        this.marque = _marque;
        this.modele = _modele;
    }    
    
    // Les accesseurs
    public Etudiant getProprietaire() {
        return proprietaire;
    }

    public void setProprietaire(Etudiant _etudiant) {
        this.proprietaire = _etudiant;
        _etudiant.setOrdinateur(this);
    }

    public int getNumeroDeSerie() {
        return numeroDeSerie;
    }

    public void setNumeroDeSerie(int _numeroDeSerie) {
        this.numeroDeSerie = _numeroDeSerie;
    }

    public String getMarque() {
        return marque;
    }
    
    public void setMarque(String _marque) {
        this.marque = _marque;
    }

    public String getModele() {
        return modele;
    }

    public void setModele(String _modele) {
        this.modele = _modele;
    }
   
}
