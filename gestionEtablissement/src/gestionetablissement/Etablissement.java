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
public class Etablissement {
    private List<Parcours> parcours; 
    private String nomEtablissement;
    private String dateCreation;
    private int nombreParcours;
    
    //constructeur
    public Etablissement(String _nomEtablissement, String _dateCreation){
        this.nomEtablissement = _nomEtablissement;
        this.dateCreation = _dateCreation;
        this.parcours = new ArrayList<>();
    }
    
    //Les accesseurs
    public List<Parcours> getParcours() {
        return parcours;
    }
    
    public void setParcours(List<Parcours> _parcours) {
        this.parcours = _parcours;
    }
    
    public String getNomEtablissement() {
        return nomEtablissement;
    }
    
    public void setNomEtablissement(String _nomEtablissement) {
        this.nomEtablissement = _nomEtablissement;
    }

    public String getDateCreation() {
        return dateCreation;
    }
    
     public void setDateCreation(String _dateCreation) {
        this.dateCreation = _dateCreation;
    }
     
    public void setNombreParcours(int nombreParcours) {
        this.nombreParcours = nombreParcours;
    }

    public int getNombreParcours() {
        return nombreParcours;
    }
    
    public void AjouterParcours(Parcours _parcours){
       parcours.add(_parcours);
        if(parcours.add(_parcours)){
            this.nombreParcours += 1; 
        }else{
            System.out.println("Aucun parcours n'existe dans cet etablissements.");
        }
    }
    
    //Methode d'affichage de L'établissement
    public void afficherEtablissement(){
        System.out.println("*********** Détails du Parcours ***********");
        System.out.println("Nom de L'établissement      : " + this.nomEtablissement);
        System.out.println("Date de création    : " + this.dateCreation);
        System.out.println("Nombre de parcours   : " + this.nombreParcours);
        System.out.println("");
    }
    
}
