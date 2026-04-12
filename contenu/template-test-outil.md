# Template — Série TEST & VERDICT
**Compte :** brief.ia
**Usage :** Réutiliser pour chaque test d'outil (OpenClaw, Gemma, N8N, etc.)
**Méthodes :** spécificité + transformation mesurable + CTA échange + tutoiement
**Dernière mise à jour :** 2026-04-12

---

## VARIABLES À REMPLIR AVANT CHAQUE POST

```
[OUTIL]             → Nom de l'outil (ex: OpenClaw)
[PROMESSE]          → La tagline ou promesse marketing exacte
[USE_CASE]          → Ce que tu as voulu faire concrètement
[TEMPS_SETUP]       → Temps réel de setup (honnête, en minutes/heures)
[TEMPS_CYCLE]       → Temps du premier cycle complet
[NB_AGENTS]         → Nombre d'agents / étapes créés
[VÉRITÉ_1]          → Premier problème concret rencontré
[VÉRITÉ_2]          → Deuxième problème
[VÉRITÉ_3]          → Troisième problème (ou surprise positive)
[CHIFFRE_ABSURDE]   → Le détail le plus frappant du test (ex: "news de 2022")
[RÉSULTAT]          → Ce que l'outil a produit concrètement
[POUR_QUI]          → Public qui en bénéficierait vraiment
[PAS_POUR_QUI]      → Public qui serait déçu
[SCORE]             → Note /5 (honnête, pas de 5/5)
[MOT_CTA]           → Mot à commenter pour recevoir le rapport (ex: RAPPORT, VERDICT, TEST)
```

---

## HOOK — 3 formules (choisir la plus forte selon le test)

### Formule A — Échec + chiffres + twist *(la plus virale)*
> J'ai passé [TEMPS_SETUP] à [USE_CASE].
> [RÉSULTAT absurde ou inattendu].
> *Voilà ce que les démos ne montrent jamais.*

*Exemple :* "J'ai passé 2h à configurer 4 agents IA. Ils m'ont sorti une newsletter sur un outil de 2022."

### Formule B — Transformation mesurable
> [NB] semaines à chercher un outil pour [USE_CASE].
> Zéro résultat. Puis j'ai testé [OUTIL].
> [Résultat concret en chiffres].

*Exemple :* "3 semaines à chercher un outil pour automatiser ma veille. Zéro résultat. Puis j'ai testé Paperclip. Verdict : 2,5/5."

### Formule C — Contre-promesse
> [OUTIL] promet [PROMESSE].
> J'ai cherché où c'était faux.
> J'ai tout trouvé.

*Exemple :* "Paperclip promet l'entreprise sans humains. J'ai cherché où j'étais encore dans la boucle. J'ai tout trouvé."

---

## CARROUSEL — Structure 7 slides

### SLIDE 1 — Hook
- Fond noir uni
- Badge "TEST & VERDICT" haut droite (cyan #00AAFF, bold 14pt)
- Hook choisi (formule A, B ou C)
- Sous-texte bas : "*Voilà ce que les démos ne montrent jamais.*"

### SLIDE 2 — Le test
- Screenshot setup ou interface
- "Ce que j'ai voulu [faire/automatiser]"
- Liste des étapes ou agents (avec "0 intervention humaine" si applicable)
- Dernière ligne : "Temps estimé : [X]. Spoiler : c'était faux." *(en gris italique)*

### SLIDE 3 — Vérité #1
- Screenshot illustrant le problème
- Titre : "Vérité #1 / [titre court]"
- [VÉRITÉ_1] en 3–4 lignes max
- Chiffre fort en grand + comparaison démo vs réalité

### SLIDE 4 — Vérité #2
- Screenshot illustrant le problème
- Titre : "Vérité #2 / [titre court]"
- [VÉRITÉ_2] en 3–4 lignes
- Dernière ligne : conséquence en italique

### SLIDE 5 — Vérité #3 (ou Surprise)
- Screenshot du résultat
- Titre : "Vérité #3" ou "Surprise :"
- [CHIFFRE_ABSURDE] mis en évidence — c'est la chute visuelle

### SLIDE 6 — Les chiffres
- Fond #1a1a1a — texte only
- ⏱ Setup : [TEMPS_SETUP]
- ⏱ Premier cycle : [TEMPS_CYCLE]
- 📄 [Résultat principal] : oui / non
- 🔧 Interventions manuelles : [nb]
- 💸 Coût : [coût réel]
- Publiable tel quel ? **Non / Oui** *(en rouge/cyan)*
- Avec retouches ? **Oui / Non**

### SLIDE 7 — Verdict + CTA
- Logo brief.ia haut gauche
- Verdict 1 ligne + "tu es encore dans la boucle" si applicable
- ✅ Pour toi si : [POUR_QUI]
- ❌ Pas pour toi si : [PAS_POUR_QUI]
- **Score : [SCORE] / 5** *(très grand, 60–70pt)*
- 💬 Commente **[MOT_CTA]** et je t'envoie le test complet en DM.

---

## REEL — Structure 10 scènes (28–35 sec)

```
[1] J'ai passé [TEMPS_SETUP] à [USE_CASE].        (3 sec)
[2] Résultat : [CHIFFRE_ABSURDE].                 (2 sec — choc, gris décalé)
[3] Voilà ce qui s'est passé.                     (2 sec — transition)
[4] Setup : [TEMPS_SETUP].                        (3 sec)
    Pour un outil censé [PROMESSE courte].
[5] [VÉRITÉ_2 en 3 lignes max]                    (3 sec)
[6] [RÉSULTAT] sort quand même.                   (2 sec — respiration)
[7] [VÉRITÉ_3 : le chiffre absurde mis en scène]  (3 sec — laisser lire)
[8] Mais "[PROMESSE]" ?                           (2 sec)
[9] C'est du marketing.                           (3 sec — PAUSE, seul sur fond noir)
[10] Score : [SCORE] / 5                          (3 sec)
     Commente [MOT_CTA] → test complet en DM.
```

**Notes fixes :**
- Slide [2] : résultat en gris, décalé — effet choc visuel
- Slide [9] : seul sur fond noir, pause 3 sec
- Typo : Inter Bold, blanc sur noir, min 45pt
- Cover : slide [9] ou [2]

---

## CAPTION — Formule

```
[Hook formule A — 2 lignes]

[PROMESSE de l'outil en 1 ligne].
[Ce que tu as cherché / trouvé — 1 ligne].

[Ce que le carrousel révèle — 1 ligne] → swipe

💬 Commente [MOT_CTA] et je t'envoie le test complet en DM.

#IA #[OUTIL] #AgentsIA #Automatisation #Solopreneur #Fondateur #OutilsIA #Freelance #BriefIA
```

---

## VIGNETTE CANVA — Specs

**Format :** 1080x1080 px
**Fond :** #000000
**Badge série :** "TEST & VERDICT" — fond cyan #00AAFF, texte noir bold, haut droite
**Éléments :**
- Logo [OUTIL] centré (ou screenshot iconique)
- Hook slide 1 en police bold 65–75pt, blanc
- Logo brief.ia haut gauche (24pt)

---

## CHECKLIST PUBLICATION

### J0 — Teaser Story
- [ ] "J'ai testé [OUTIL] ce matin. [Promesse courte]. Verdict dans 48h."
- [ ] Fond noir, texte blanc/cyan, logo brief.ia

### J2 — Carrousel (mardi ou jeudi 7h–9h)
- [ ] 7 slides créées (dupliquer template Canva)
- [ ] Badge TEST & VERDICT visible slide 1
- [ ] Chiffre absurde mis en évidence slide 5
- [ ] Score en grand slide 7
- [ ] "[MOT_CTA]" en cyan slide 7
- [ ] Caption copiée avec CTA "Commente [MOT_CTA]"
- [ ] Lien bio actif

### J5 — Reel
- [ ] Script monté, slide [9] seul sur fond noir
- [ ] Son instrumental
- [ ] Durée 28–35 sec
- [ ] Cover : slide [9]
