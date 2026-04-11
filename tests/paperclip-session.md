# Session test Paperclip — brief.ia
**Date :** 2026-04-11 (samedi matin)
**Objectif :** Pipeline veille IA → Newsletter (4 agents) — test pour Post #1 Instagram

---

## Contexte

Test réel de Paperclip (paperclip.ing) pour produire du contenu Instagram authentique.
- Pilier : Test & Verdict
- Format final : Carrousel 7 slides + Reel texte animé
- Use case testé : Pipeline veille IA → Newsletter Substack/Beehiiv

---

## Déroulé de la session

### Installation

- Commande : `npx paperclipai onboard --yes`
- Prérequis vérifiés : Node v22.17.0 / npm 10.9.2 ✅
- Aucun compte requis, open source MIT, auto-hébergé

### Question LLM — Décision clé

**Question posée :** Clé API Anthropic ou Claude Code ?

**Résultat de recherche :**
- L'adapter "Claude Local" de Paperclip utilise le CLI `claude` installé localement
- Il peut s'authentifier via **connexion d'abonnement** (pas de clé API séparée requise)
- Conclusion : l'abonnement Claude Code suffit, pas besoin de crédits Anthropic API en plus

### Configuration

- **Company name :** brief.ia
- **Mission :** Créer une newsletter hebdomadaire en français qui teste des outils IA pour fondateurs et freelances, et publie des verdicts honnêtes sur ce qui marche vraiment.
- **LLM :** Claude Local (via Claude Code, sans clé API séparée)

### Choix plateforme newsletter

Paperclip a évalué 3 options de lui-même (Ghost, Beehiiv, custom) et choisi **Beehiiv** :
- Free jusqu'à 2 500 subs
- API pour future automation
- Built-in referral/growth tools
- Zero DevOps overhead

**Décision prise :** Ne pas connecter Beehiiv maintenant. Paperclip génère la newsletter → review manuelle → publication humaine. Objectif : valider la qualité du contenu avant d'automatiser la publication.

### Employés créés (manuellement — Paperclip avait créé des issues, pas des agents)

| Employé | Description |
|---------|-------------|
| News Scout | Monitor Product Hunt, HN, Twitter/X (#AItools). Output : liste des 5 meilleurs outils IA pour fondateurs francophones |
| AI Tool Researcher | Deep-dive par outil : prix, use cases, avis, scores (setup / valeur / pertinence solopreneur) |
| Newsletter Writer | Rédige la newsletter en français 800-1000 mots, ton honnête, structure : hook / outil / verdict / pour qui / tip |
| Publisher | Formate en plain text pour review manuelle, ne publie pas, signale les sections à valider |

**Observation :** Paperclip a créé des issues (tâches planifiées), pas des employés directement. Les employés ont été créés manuellement ensuite.

### Pipeline lancé

- Les 4 agents ont été lancés
- En cours au moment de l'enregistrement

---

## Observations en live

- Paperclip a créé des issues/tâches (BRI-2 à BRI-7), pas des employés → structure d'équipe à créer entièrement à la main
- Pas de visibilité sur l'avancement des tâches en cours : impossible de savoir où en est le pipeline sans aller chercher manuellement
- Le Newsletter Writer s'est retrouvé en état "blocked" : il attendait les résultats du News Scout avant de pouvoir rédiger — les dépendances entre agents ne sont pas gérées automatiquement
- La newsletter générée porte sur **Perplexity AI** — un outil lancé en 2022, pas récent. Le News Scout n'est pas calibré pour prioriser la fraîcheur des sujets
- Newsletter bien structurée et au bon format, mais le choix du sujet décrédibilise l'outil de veille

---

## Verdict final

**Temps réel de setup :** 1h00 (installation + création manuelle des 4 agents)
**Temps d'un cycle complet :** ~20 min après lancement
**Newsletter publiable telle quelle ?** Avec retouches (structure OK, sujet trop daté)
**Blocage principal :** Pas de création automatique d'équipe + pas de visibilité sur les tâches + Scout qui sort des vieilles news
**Score global :** 2,5/5

---

## Matière pour le carrousel Instagram

**Verdict en 1-2 phrases brutes :**
Paperclip peut produire une newsletter en 20 minutes. Mais il faut 1h de setup manuel, zéro visibilité sur ce qui tourne, et le Scout t'a sorti Perplexity comme "outil récent". C'est prometteur, pas encore fiable.

**Chiffre concret :**
1h de setup + 20 min de génération = 1h20 pour une newsletter sur un outil de 2022

**Cas d'usage exact testé :**
Pipeline 4 agents : veille IA → recherche → rédaction → formatage newsletter (brief.ia, français, 800-1000 mots)

**Limite principale :**
Le News Scout ne filtre pas par fraîcheur — il peut sortir n'importe quel outil connu, pas forcément les lancements récents

**Pour qui c'est utile :**
Quelqu'un qui veut structurer une équipe IA locale, qui a du temps pour configurer, et qui valide chaque output avant de publier

**Pour qui c'est inutile :**
Quelqu'un qui veut un pipeline clé en main qui tourne tout seul sans supervision

**Angle retenu :**
- [ ] "J'ai automatisé ma veille IA avec 4 agents — 0 min de recherche par semaine"
- [x] **"Paperclip promet une entreprise sans humains. Voilà ce que personne ne dit."**

---

## Screenshots à prendre

- [ ] Screenshot 1 — Terminal onboarding (message de succès)
- [ ] Screenshot 2 — Interface vierge après login
- [ ] Screenshot 3 — Création d'un agent (le plus visuel)
- [ ] Screenshot 4 — Pipeline en cours (logs / progression)
- [ ] Screenshot 5 — Newsletter générée (résultat brut)

---

## Séquence de publication

```
J0  → Stories : "Je teste Paperclip ce matin. Verdict dans 48h."
J1  → Stories : screenshot setup + 1 observation
J2  → Carrousel publié (mardi ou jeudi 7h–9h)
J3  → Réponse commentaires + share en story
J5  → Reel publié
J6  → Story CTA newsletter Beehiiv
```
