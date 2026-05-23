# Système de prospection serruriers — Implémentation détaillée

## Le problème précis

Le créateur a un agent vocal IA qui peut capter les urgences serrurerie 24/7. Il ne sait pas encore :

- **Où** trouver les bons serruriers (pas sur LinkedIn, peu sur les réseaux)
- **Quoi leur dire** (ils parlent chantier et urgence, pas SaaS)
- **Comment démontrer** la valeur sans une longue présentation

---

## Comprendre la cible

Un serrurier urgentiste solo c'est :
- CA 36 000–72 000 €/an, revenu net ~40 000 €/an
- 25–45 interventions/mois, prix moyen 130 € (jusqu'à 500 € nuit/WE)
- Son téléphone = son outil de travail et son talon d'Achille
- Il perd 40–60 % de ses appels quand il est sous une porte
- Il déteste les centrales (Depanneo, HomeServe) qui lui volent ses leads et dégradent la réputation du métier
- Il ne lit pas ses emails pro, répond aux SMS

**Sa douleur n°1 :** Sortir d'un chantier et voir 2 appels manqués — sachant qu'ils sont partis chez une centrale.

---

## La stack du système

### Étape 1 — Trouver les serruriers cibles (scraping)

**Sources prioritaires :**

- **Pages Jaunes** — catégorie "serrurier", filtrer par ville/département
- **Google Maps API** — "serrurier dépannage + ville" → fiches complètes avec téléphone
- **Societe.com / INSEE** — code NAF **43.32B** (serrurerie, menuiserie métallique) → filtre TPE < 5 salariés

**Signaux de qualification (les meilleurs prospects) :**
- Pas de service de rappel automatique sur leur fiche Google → ils perdent des appels maintenant
- Présence web minimale (pas de site ou site vitrine basique) → ils n'ont pas encore de solution
- 10–50 avis Google, note entre 3,8 et 4,4 → établis mais pas encore saturés de clients
- Pas d'avis récents sur les 30 derniers jours → flux entrant insuffisant

**Exclure :**
- Réseaux et franchises (HomeServe, Eco Serrurier, Depanneo affiliés)
- Serruriers avec site pro avancé + formulaire de devis en ligne (déjà équipés)
- Structures > 5 salariés (cycle de vente plus long, décision pas solo)

Volume cible : 300–500 contacts qualifiés par département en 1 nuit de scraping.

---

### Étape 2 — Le message qui ouvre la conversation

Les serruriers reçoivent beaucoup de démarchage. Le message doit être court, personnel, et toucher la douleur exacte.

**SMS — template :**

> "Bonjour [Prénom], serrurier à [Ville] — cette nuit pendant que vous étiez sur un chantier, combien d'urgences sont allées chez la centrale d'à côté ? J'ai un système qui les récupère à votre place. 2 min pour voir ? [Lien Cal.com]"

**Personnalisation minimale requise :**
- Prénom (récupéré sur la fiche)
- Ville exacte (pas la région)
- Heure d'envoi : mardi ou mercredi, 11h–13h (pause chantier)

**Ne pas envoyer :**
- Le lundi (surchargé post-WE)
- Le vendredi après-midi et le week-end (sur le terrain ou récupération)
- Après 19h (hors du cadre professionnel)

---

### Étape 3 — La démo qui vend (le samedi soir)

Quand un serrurier répond positivement au SMS, on ne planifie pas une "réunion Teams". On planifie une démo le samedi soir entre 20h et 22h.

**Déroulé :**
1. À l'heure convenue, l'agent Vapi appelle le numéro du serrurier
2. L'agent simule un client en urgence : "Bonsoir, j'ai ma clé cassée dans la serrure, je suis bloqué dehors..."
3. L'agent qualifie, rassure, promet un délai réaliste, propose de le mettre en contact
4. Appel dure 60–90 secondes

Le serrurier vient de recevoir exactement ce que ses clients reçoivent — au moment où il comprend le mieux le problème (samedi soir, il pense aux urgences manquées).

**Juste après la démo**, tu le rappelles en vocal (toi, pas l'agent) :
> "Vous venez de voir ce que vos clients entendront à 23h quand vous serez indisponible. On branche ça sur votre numéro cette semaine ?"

---

### Étape 4 — Onboarding en 48h

L'artisan doit voir un résultat avant la fin de la première semaine. Sans résultat visible = churn assuré.

**Process d'onboarding :**
1. Redirection d'appel configurée (après 3 sonneries sans réponse → agent Vapi)
2. Test live avec le serrurier : il appelle son propre numéro depuis un autre téléphone
3. Il entend l'agent répondre → c'est son moment "waouh"
4. Rapport automatique configuré : SMS hebdo avec le résumé des appels traités

**Ce que l'agent dit (script serrurier) :**
> "Bonjour, vous avez joint l'équipe de [Nom du serrurier] à [Ville]. Il est actuellement en intervention. Pouvez-vous me décrire votre problème ? Je lui transmets immédiatement et il vous rappelle dans les [X] minutes."

L'agent :
- Détecte les mots-clés urgence ("bloqué", "clé cassée", "porte claquée", "cambriolage")
- Note le nom, le numéro, l'adresse, la nature du problème
- Envoie un SMS récap au serrurier avec toutes les infos
- Promet un délai précis (pas "le plus vite possible")

---

### Étape 5 — Rétention par la preuve mensuelle

Le rapport mensuel est le seul argument anti-churn qui fonctionne sur ce segment.

**Format SMS mensuel automatique :**

> "Bilan mai — Agent [Prénom] : 23 appels pris en charge, 8 urgences qualifiées, 3 chantiers confirmés (640 € générés). Votre agent a tourné."

Ce SMS transforme l'abonnement de "dépense" en "investissement avec retour mesurable". Le serrurier ne peut plus résilier sans perdre quelque chose de concret.

---

## Ce que ça donne en chiffres réels

| Volume                         | Taux | Résultat              |
|--------------------------------|------|-----------------------|
| 300 serruriers scrapés         | —    | base qualifiée        |
| 200 avec numéro SMS valide     | —    | —                     |
| Taux de réponse SMS            | ~15% | 30 réponses           |
| Acceptent une démo             | ~40% | 12 démos              |
| Closing après démo samedi soir | ~35% | **4 clients payants** |

4 clients sur 300 contacts = 1,3 % de conversion globale.
À 120 €/mois : **480 €/mois récurrents** sur un cycle de prospection de 2 semaines.

Avec 2 cycles/mois : 8 clients/mois. À mois 6 : 48 clients = ~5 750 €/mois.

---

## Ce qui se construit en premier

Dans l'ordre strict :

1. **Script Vapi serrurier** — le cœur du produit, tester avec 5 vrais appels
2. **50 contacts manuels** Pages Jaunes Paris — valider le SMS et le taux de réponse
3. **1 démo samedi soir** — fermer le 1er client payant
4. **Automatisation n8n** — seulement après le 1er client, pas avant
