// Importation des modules nécessaires (Remplacé par des fonctions JavaScript équivalentes)
import * as math from 'mathjs';

// Fonction pour afficher un message de bienvenue avec un cadre de texte
function rectangleBienvenueComplexe() {
    let phrase = " BIENVENUE ";
    let largeur = phrase.length + 6;
    let hauteur = 5;

    console.log('*'.repeat(largeur));
    console.log('*' + ' '.repeat(largeur - 2) + '*');
    console.log('* *' + phrase.padStart((largeur - 6) / 2 + phrase.length).padEnd(largeur - 4) + '* *');
    console.log('*' + ' '.repeat(largeur - 2) + '*');
    console.log('*'.repeat(largeur));
}

// Fonction permettant de choisir la méthode de résolution parmi plusieurs options
function methodeResolution() {
    console.log("*******************Choisissez la méthode de résolution *******************\n");
    console.log("                     1. La méthode de Dichotomie");
    console.log("                     2. La méthode de la Sécante");  
    console.log("                     3. La méthode de Newton-Raphson");
    console.log("                     4. La méthode du Point Fixe\n");
}

// Fonction générique pour permettre à l'utilisateur de saisir une fonction mathématique
function saisirFonction() {
    const typesFonction = {
        "1": "Polynôme (ex: x**2 + 3*x - 8)",
        "2": "Trigonométrique (ex: sin(x), cos(x) + x)",
        "3": "Logarithmique (ex: ln(x), log(x) + x**2)",
        "4": "Racine carrée (ex: sqrt(x) + x/2)",
        "5": "Rationnelle (ex: (x + 1) / (x - 2))",
        "6": "Fonction générale (ex: x**3 - sin(x) + log(x))"
    };

    while (true) {
        console.log("*******************Menus de choix de fonction *******************\n");
        console.log("Choisissez le type de fonction que vous souhaitez entrer :\n");
        Object.keys(typesFonction).forEach(key => {
            console.log(`     ${key}. ${typesFonction[key]}`);
        });
        console.log("\n");

        let typeFonction = prompt("Entrez le numéro du type de fonction : ").trim();

        if (!typesFonction[typeFonction]) {
            console.log("Choix invalide. Veuillez entrer un nombre entre 1 et 6.\n");
            continue;
        }

        while (true) {
            let fonction = prompt("Entrez votre fonction mathématique : ").replace(/\s+/g, "").toLowerCase();
            let pattern = /^([-+]?[0-9]*\.?[0-9]+(?:\*?\*?[xX](?:\^?[0-9]+)?)?|[a-zA-Z]+\([^\)]*\))(?:[+\-*/^]([-+]?[0-9]*\.?[0-9]+(?:\*?\*?[xX](?:\^?[0-9]+)?)?|[a-zA-Z]+\([^\)]*\)))*$/;

            if (pattern.test(fonction)) {
                try {
                    let fonctionMathJS = math.compile(fonction);
                    console.log(`Votre fonction saisie '${fonction}' est correcte.\n`);
                    return fonctionMathJS;
                } catch (e) {
                    console.log("Erreur : Impossible de parser la fonction. Veuillez vérifier votre saisie.\n");
                }
            } else {
                console.log("Erreur : La fonction saisie n'est pas valide. Essayez à nouveau.\n");
            }
        }
    }
}

// Fonction pour demander la tolérance et le nombre maximal d'itérations
function saisirToleranceEtIterations() {
    while (true) {
        try {
            // Demander la tolérance avec prise en charge des notations scientifiques
            let toleranceInput = prompt("Entrez la tolérance souhaitée (ex: 0.0001, 1.0e-5, 1e-6) : \n");
            // Convertir l'entrée en nombre flottant
            let tolerance = parseFloat(toleranceInput);

            // Demander le nombre maximal d'itérations
            let nombreMaxIterations = parseInt(prompt("Entrez le nombre maximal d'itérations (ex: 100) : \n"));

            // Vérifier que la tolérance et le nombre d'itérations sont valides (supérieurs à zéro)
            if (tolerance > 0 && nombreMaxIterations > 0) {
                console.log(`Votre tolérance est : ${tolerance}`);
                console.log(`Votre nombre maximal d'itérations est : ${nombreMaxIterations}\n`);
                return { tolerance, nombreMaxIterations };
            } else {
                console.log("Erreur : la tolérance et le nombre d'itérations doivent être supérieurs à zéro.");
            }
        } catch (error) {
            console.log("Erreur : veuillez entrer des valeurs numériques valides pour la tolérance (flottant) et un entier pour le nombre d'itérations.");
        }
    }
}

// Importation des modules nécessaires
const mathjs = require('mathjs');

// Fonction pour la méthode de dichotomie avec affichage des intervalles
function methodeDeDichotomie(fonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations) {
    let valeurBorneInferieure = fonction(borneInferieure);

    if (Math.abs(valeurBorneInferieure) <= tolerance) {
        return borneInferieure;
    }

    let valeurBorneSuperieure = fonction(borneSuperieure);

    if (Math.abs(valeurBorneSuperieure) <= tolerance) {
        return borneSuperieure;
    }

    if (valeurBorneInferieure * valeurBorneSuperieure > 0.0) {
        console.log("La racine n'est pas encadrée entre [", borneInferieure, ";", borneSuperieure, "]");
        return null;
    }

    let nombreIterations = Math.ceil(Math.log(Math.abs(borneSuperieure - borneInferieure) / tolerance) / Math.log(2.0));

    for (let i = 0; i < Math.min(nombreIterations + 1, nombreMaxIterations); i++) {
        let pointMilieu = (borneInferieure + borneSuperieure) * 0.5;
        let valeurPointMilieu = fonction(pointMilieu);

        console.log(`Iteration ${i + 1}: Intervalle actuel = [${borneInferieure}, ${borneSuperieure}]`);

        if (valeurPointMilieu == 0.0 || (borneSuperieure - borneInferieure) < tolerance) {
            console.log(`Solution trouvée : x = ${pointMilieu} après ${i + 1} itérations`);
            return pointMilieu;
        }

        if (valeurPointMilieu * valeurBorneSuperieure < 0.0) {
            borneInferieure = pointMilieu;
            valeurBorneInferieure = valeurPointMilieu;
        } else {
            borneSuperieure = pointMilieu;
            valeurBorneSuperieure = valeurPointMilieu;
        }
    }

    return (borneInferieure + borneSuperieure) * 0.5;
}

// Fonction pour la méthode de la sécante
function methodeDeLaSecante(fonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations) {
    let valeurBorneInferieure = fonction(borneInferieure);

    if (Math.abs(valeurBorneInferieure) <= tolerance) {
        return borneInferieure;
    }

    let valeurBorneSuperieure = fonction(borneSuperieure);

    if (Math.abs(valeurBorneSuperieure) <= tolerance) {
        return borneSuperieure;
    }

    if (valeurBorneInferieure * valeurBorneSuperieure > 0.0) {
        console.log("La racine n'est pas encadrée entre [", borneInferieure, ";", borneSuperieure, "]");
        return null;
    }

    let compteurIterations = 0;
    while ((Math.abs(borneSuperieure - borneInferieure) > tolerance || Math.abs(valeurBorneSuperieure) > tolerance) && (compteurIterations < nombreMaxIterations)) {
        compteurIterations += 1;
        let estimation = borneInferieure - valeurBorneInferieure * (borneSuperieure - borneInferieure) / (valeurBorneSuperieure - valeurBorneInferieure);
        let valeurEstimation = fonction(estimation);

        if (Math.abs(valeurEstimation) <= tolerance) {
            return estimation;
        }

        if (valeurEstimation * valeurBorneSuperieure < 0.0) {
            borneInferieure = estimation;
            valeurBorneInferieure = valeurEstimation;
        } else {
            borneSuperieure = estimation;
            valeurBorneSuperieure = valeurEstimation;
        }
    }

    return (borneInferieure - valeurBorneInferieure * (borneSuperieure - borneInferieure) / (valeurBorneSuperieure - valeurBorneInferieure));
}

// Fonction pour la méthode de Newton-Raphson
function methodeDeNewtonRaphson(fonction, deriveeFonction, xInitiale, tolerance, nombreMaxIterations) {
    let compteurIterations = 0;
    let x = xInitiale;
    let valeurX = fonction(x);

    while ((Math.abs(valeurX) > tolerance) && (compteurIterations < nombreMaxIterations)) {
        let valeurDeriveeX = deriveeFonction(x);

        if (valeurDeriveeX === 0) {
            console.log("La dérivée est nulle. L'implémentation de la Méthode de Newton échoue.");
            return null;
        }

        x = x - valeurX / valeurDeriveeX;
        valeurX = fonction(x);
        compteurIterations += 1;
    }

    if (compteurIterations === nombreMaxIterations) {
        console.log("Pas de convergence avec la méthode de Newton.");
        return null;
    } else {
        return x;
    }
}

// Fonction pour la méthode du point fixe
function methodeDuPointFixe(phi, xInitiale, tolerance, nombreMaxIterations) {
    let compteurIterations = 0;
    let x = xInitiale;

    while ((Math.abs(phi(x) - x) > tolerance) && (compteurIterations < nombreMaxIterations)) {
        x = phi(x);
        compteurIterations += 1;
    }

    if (compteurIterations === nombreMaxIterations) {
        console.log("Pas de convergence avec la méthode du point fixe.\n");
        return null;
    } else {
        return x;
    }
}

// Amélioration: méthode de balayage pour la méthode de Newton
function balayageNewton(fonction, deriveeFonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations) {
    let valeursInitiales = [borneInferieure, (borneInferieure + borneSuperieure) / 2, borneSuperieure];
    for (let valInit of valeursInitiales) {
        console.log(`Essai de la méthode de Newton avec x_initiale = ${valInit}`);
        let solution = methodeDeNewtonRaphson(fonction, deriveeFonction, valInit, tolerance, nombreMaxIterations);
        if (solution !== null) {
            return solution;
        }
    }
    return null;
}

// Définition du symbole 'x' qui sera utilisé dans les fonctions mathématiques
const x = math.symbol('x');

// Fonction pour demander les bornes à l'utilisateur
function demanderBornes() {
    // Boucle infinie pour répéter la demande tant que les valeurs sont invalides
    while (true) {
        try {
            // Demander les bornes de l'intervalle
            let borneInferieure = parseFloat(prompt("Entrez la borne inférieure de l'intervalle : "));
            let borneSuperieure = parseFloat(prompt("Entrez la borne supérieure de l'intervalle : "));

            // Vérifier que la borne inférieure est bien inférieure à la borne supérieure
            if (borneInferieure < borneSuperieure) {
                return [borneInferieure, borneSuperieure];  // Retourner les bornes si elles sont valides
            } else {
                console.log("Erreur : la borne inférieure doit être inférieure à la borne supérieure.");
            }
        } catch (error) {
            console.log("Erreur : veuillez entrer des valeurs numériques valides pour les bornes.");
        }
    }
}

// Fonction principale pour exécuter le programme
function main() {
    let action = true;  // Variable pour contrôler si l'utilisateur veut recommencer ou quitter

    // Afficher un message de bienvenue
    rectangleBienvenueComplexe();

    // Boucle principale pour permettre à l'utilisateur de recommencer ou quitter
    while (action) {
        // Affichage du menu pour choisir la méthode de résolution
        methodeResolution();

        // Boucle pour s'assurer que l'utilisateur saisit un choix valide entre 1 et 4
        while (true) {
            try {
                let choix = parseInt(prompt("Entrez le numéro de la méthode (1-4) : "), 10);
                if (choix >= 1 && choix <= 4) {
                    break;  // Si le choix est valide, sortir de la boucle
                } else {
                    console.log("Erreur : le numéro doit être un entier entre 1 et 4.");
                }
            } catch (error) {
                console.log("Erreur : veuillez entrer un nombre entier.");
            }
        }

        // Affichage de la méthode choisie
        if (choix === 1) {
            console.log("*************** METHODE DE DICHOTOMIE ***************");
        } else if (choix === 2) {
            console.log("*************** METHODE DE LA SECANTE ***************");
        } else if (choix === 3) {
            console.log("*************** METHODE DE NEWTON-RAPHSON ***************");
        } else if (choix === 4) {
            console.log("*************** METHODE DU POINT FIXE ***************");
        }

        // Demander à l'utilisateur de saisir la fonction à résoudre
        let fonctionStr = saisirFonction();
        try {
            // Convertir la fonction en une expression mathématique utilisable par mathjs
            let fonctionExpr = math.parse(fonctionStr);
            let fonction = math.compile(fonctionExpr);
            console.log("Fonction interprétée : f(x) =", fonctionExpr.toString());
        } catch (error) {
            console.log("Erreur lors de l'interprétation de la fonction :", error);
            continue;  // Si la fonction est invalide, demander à nouveau la fonction
        }

        // Si la méthode choisie nécessite des bornes (Dichotomie ou Sécante)
        if (choix === 1 || choix === 2) {
            let [borneInferieure, borneSuperieure] = demanderBornes();
            console.log(`Votre intervalle est : [${borneInferieure}, ${borneSuperieure}]`);
        }

        // Demander à l'utilisateur la tolérance et le nombre maximal d'itérations
        let { tolerance, nombreMaxIterations } = saisirToleranceEtIterations();

        // Variable pour stocker la racine trouvée
        let racine = null;

        // Exécution de la méthode choisie par l'utilisateur
        if (choix === 1) {
            racine = methodeDeDichotomie(fonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations);
        } else if (choix === 2) {
            racine = methodeDeLaSecante(fonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations);
        } else if (choix === 3) {
            // Calcul de la dérivée de la fonction
            let deriveeFonction = math.compile(fonctionExpr.derivative(x));
            let xInitiale = parseFloat(prompt("Entrez une estimation initiale de la racine (exemple: 2) : "));
            racine = methodeDeNewtonRaphson(fonction, deriveeFonction, xInitiale, tolerance, nombreMaxIterations);
        } else if (choix === 4) {
            let xInitiale = parseFloat(prompt("Entrez une estimation initiale de la racine (exemple: 2) : "));
            racine = methodeDuPointFixe(fonction, xInitiale, tolerance, nombreMaxIterations);
        }

        // Affichage de la racine trouvée
        if (racine !== null) {
            console.log(`La racine trouvée est : ${racine}`);
        } else {
            console.log("Aucune racine n'a été trouvée.");
        }

        // Demander à l'utilisateur s'il souhaite recommencer ou quitter
        let choixRecommencer = prompt("Souhaitez-vous recommencer ? (oui/non) : ").toLowerCase();
        if (choixRecommencer === "oui") {
            action = true;  // Continuer si l'utilisateur souhaite recommencer
        } else {
            action = false;  // Quitter si l'utilisateur ne veut pas recommencer
        }
    }
}

// Appeler la fonction principale pour démarrer le programme
main();
