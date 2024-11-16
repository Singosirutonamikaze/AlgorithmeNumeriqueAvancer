import React, { useState } from "react";
import math from "mathjs";

const App = () => {
  // États pour les différentes étapes et valeurs
  const [message, setMessage] = useState("Bienvenue!");
  const [fonction, setFonction] = useState("");
  const [tolerance, setTolerance] = useState("");
  const [iterations, setIterations] = useState("");
  const [choix, setChoix] = useState(null);
  const [bornes, setBornes] = useState({ inf: 0, sup: 0 });
  const [racine, setRacine] = useState(null);
  const [recommencer, setRecommencer] = useState(false);

  // Fonction pour afficher le message de bienvenue
  const rectangleBienvenueComplexe = () => {
    const phrase = " BIENVENUE ";
    const largeur = phrase.length + 6;
    const hauteur = 5;
    return (
      <div>
        <pre>{'*'.repeat(largeur)}</pre>
        <pre>{'*' + ' '.repeat(largeur - 2) + '*'}</pre>
        <pre>{'* *' + phrase.padStart((largeur - 6) / 2 + phrase.length).padEnd(largeur - 4) + '* *'}</pre>
        <pre>{'*' + ' '.repeat(largeur - 2) + '*'}</pre>
        <pre>{'*'.repeat(largeur)}</pre>
      </div>
    );
  };

  // Fonction pour saisir une fonction mathématique
  const saisirFonction = (type) => {
    const typesFonction = {
      "1": "Polynôme (ex: x**2 + 3*x - 8)",
      "2": "Trigonométrique (ex: sin(x), cos(x) + x)",
      "3": "Logarithmique (ex: ln(x), log(x) + x**2)",
      "4": "Racine carrée (ex: sqrt(x) + x/2)",
      "5": "Rationnelle (ex: (x + 1) / (x - 2))",
      "6": "Fonction générale (ex: x**3 - sin(x) + log(x))"
    };
    return typesFonction[type];
  };

  // Fonction pour la méthode de Dichotomie
  const methodeDeDichotomie = (fonction, borneInferieure, borneSuperieure, tolerance, nombreMaxIterations) => {
    let valeurBorneInferieure = math.evaluate(fonction, { x: borneInferieure });

    if (Math.abs(valeurBorneInferieure) <= tolerance) {
      return borneInferieure;
    }

    let valeurBorneSuperieure = math.evaluate(fonction, { x: borneSuperieure });

    if (Math.abs(valeurBorneSuperieure) <= tolerance) {
      return borneSuperieure;
    }

    if (valeurBorneInferieure * valeurBorneSuperieure > 0.0) {
      return "La racine n'est pas encadrée entre les bornes.";
    }

    let nombreIterations = Math.ceil(Math.log(Math.abs(borneSuperieure - borneInferieure) / tolerance) / Math.log(2.0));

    for (let i = 0; i < Math.min(nombreIterations + 1, nombreMaxIterations); i++) {
      let pointMilieu = (borneInferieure + borneSuperieure) * 0.5;
      let valeurPointMilieu = math.evaluate(fonction, { x: pointMilieu });

      if (valeurPointMilieu === 0.0 || (borneSuperieure - borneInferieure) < tolerance) {
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
  };

  // Fonction pour gérer le calcul de la racine
  const calculerRacine = (choix, fonction, tolerance, iterations, bornes) => {
    const { inf, sup } = bornes;

    if (choix === 1) {
      setRacine(methodeDeDichotomie(fonction, inf, sup, tolerance, iterations));
    } else if (choix === 2) {
      // Implémentation de la méthode de la secante ici
      setRacine("Méthode de la sécante en cours...");
    } else if (choix === 3) {
      // Implémentation de la méthode de Newton-Raphson ici
      setRacine("Méthode de Newton-Raphson en cours...");
    } else if (choix === 4) {
      // Implémentation de la méthode du point fixe ici
      setRacine("Méthode du point fixe en cours...");
    }
  };

  // Fonction pour gérer la réinitialisation du calcul
  const resetCalculation = () => {
    setRacine(null);
    setRecommencer(true);
  };

  return (
    <div>
      {rectangleBienvenueComplexe()}

      {recommencer && (
        <div>
          <h2>Choisissez une méthode de résolution</h2>
          <div>
            <button onClick={() => setChoix(1)}>Méthode de Dichotomie</button>
            <button onClick={() => setChoix(2)}>Méthode de la Sécante</button>
            <button onClick={() => setChoix(3)}>Méthode de Newton-Raphson</button>
            <button onClick={() => setChoix(4)}>Méthode du Point Fixe</button>
          </div>

          <div>
            <label>
              Fonction à résoudre:
              <input
                type="text"
                value={fonction}
                onChange={(e) => setFonction(e.target.value)}
                placeholder="Entrez la fonction (ex: x^2 - 3)"
              />
            </label>
          </div>

          <div>
            <label>
              Tolérance:
              <input
                type="number"
                value={tolerance}
                onChange={(e) => setTolerance(e.target.value)}
                placeholder="Entrez la tolérance"
              />
            </label>
          </div>

          <div>
            <label>
              Nombre maximal d'itérations:
              <input
                type="number"
                value={iterations}
                onChange={(e) => setIterations(e.target.value)}
                placeholder="Entrez le nombre d'itérations"
              />
            </label>
          </div>

          <div>
            <label>
              Borne inférieure:
              <input
                type="number"
                value={bornes.inf}
                onChange={(e) => setBornes({ ...bornes, inf: parseFloat(e.target.value) })}
                placeholder="Entrez la borne inférieure"
              />
            </label>
          </div>

          <div>
            <label>
              Borne supérieure:
              <input
                type="number"
                value={bornes.sup}
                onChange={(e) => setBornes({ ...bornes, sup: parseFloat(e.target.value) })}
                placeholder="Entrez la borne supérieure"
              />
            </label>
          </div>

          <button onClick={() => calculerRacine(choix, fonction, parseFloat(tolerance), parseInt(iterations), bornes)}>
            Calculer la racine
          </button>

          <div>
            <h3>Racine trouvée: {racine}</h3>
          </div>

          <button onClick={resetCalculation}>Recommencer</button>
        </div>
      )}
    </div>
  );
};

export default App;
