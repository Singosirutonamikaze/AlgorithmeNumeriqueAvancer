/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package gestionetablissement;

/**
 *
 * @author DELL LATITUDE
 */
public class UniteEnseignement {
    private String codeUE;
    private String intituleUE;
    private int coefficient;
    
    //constructeur
    public UniteEnseignement(String _codeUE, String _intituleUE, int _coefficient){
        this.codeUE = _codeUE;
        this.intituleUE = _intituleUE;
        this.coefficient = _coefficient;
    }

    //Les accesseurs en lecture et en ecriture
    public String getCodeUE() {
        return codeUE;
    }

    public void setCodeUE(String _codeUE) {
        this.codeUE = _codeUE;
    }

    public String getIntituleUE() {
        return intituleUE;
    }

    public void setIntituleUE(String _intituleUE) {
        this.intituleUE = _intituleUE;
    }
    
    public int getCoefficient() {
        return coefficient;
    }

    public void setCoeficient(int _coefficient) {
        this.coefficient = _coefficient;
    }
    
    public void afficheUE(){
        System.out.println("*********** Détails de L'unité d'enseignement ***********");
        System.out.println("Code de l'UE     : " + this.codeUE);
        System.out.println("Intitulé de l'UE    : " + this.intituleUE);
        System.out.println("Nombre de crédit de l'UE    : " + this.coefficient);
        System.out.println(" ");
    }

}

