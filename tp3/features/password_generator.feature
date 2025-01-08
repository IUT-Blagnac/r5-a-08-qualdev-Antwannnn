# language: fr
Fonctionnalité: Générateur de mot de passe
  En tant qu'utilisateur
  Je veux pouvoir générer différents types de mots de passe
  Afin de sécuriser mes comptes avec des mots de passe robustes

  Scénario: Génération d'un mot de passe par défaut
    Quand je génère un mot de passe par défaut
    Alors je dois obtenir un mot de passe de 16 caractères
    Et le mot de passe doit contenir au moins 2 caractères spéciaux
    Et le mot de passe doit contenir au moins 2 chiffres
    Et le mot de passe doit contenir au moins 2 lettres majuscules

  Plan du Scénario: Génération d'un mot de passe personnalisé
    Quand je génère un mot de passe avec les exigences suivantes:
      | longueur_min | caracteres_speciaux_min | chiffres_min | majuscules_min | exclure_similaires | exclure_ambigus |
      | <longueur>   | <spec_chars>            | <numbers>     | <uppercase>    | <sim>             | <amb>           |
    Alors je dois obtenir un mot de passe de <longueur> caractères
    Et le mot de passe doit contenir au moins <spec_chars> caractères spéciaux
    Et le mot de passe doit contenir au moins <numbers> chiffres
    Et le mot de passe doit contenir au moins <uppercase> lettres majuscules

    Exemples:
      | longueur | spec_chars | numbers | uppercase | sim   | amb   |
      | 12       | 1          | 1       | 1         | false | false |
      | 20       | 3          | 3       | 3         | true  | true  |
      | 8        | 0          | 1       | 1         | false | false |

  Scénario: Génération d'un mot de passe mémorable
    Quand je génère un mot de passe mémorable
    Alors je dois obtenir un mot de passe contenant 4 mots
    Et les mots doivent être séparés par des caractères spéciaux
    Et certains caractères doivent être remplacés par des chiffres

  Scénario: Vérification des exigences du mot de passe
    Étant donné un mot de passe "Test123456!@#"
    Quand je vérifie les exigences suivantes:
      | longueur_min | caracteres_speciaux_min | chiffres_min | majuscules_min |
      | 10           | 3                       | 3            | 1              |
    Alors la vérification doit retourner vrai