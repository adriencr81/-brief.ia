# WORKFLOW — Futures publications TEST (après Paperclip)

Vous pouvez adapter ce workflow pour chaque nouvel outil testé.

---

## STRUCTURE: 1 TEST = 1 SEMAINE COMPLÈTE

```
Lundi 20h      → Story: "Je teste [OUTIL] ce matin..."
Mardi 09h      → Story: setup/résultats
Mardi 18h      → Story: observation live
Jeudi 07h–09h  → CARROUSEL CANVA (7 slides)
Jeudi 09h30    → Publier + Caption
Vendredi 18h   → REEL CapCut (30–40s)
Jeudi 20h      → Story: relais carrousel
```

**Total temps:** 2h30–3h (setup + création)

---

## TEMPLATE — Contenu à créer AVANT le test

Créez ces fichiers dans `contenu/` AVANT de lancer le test:

### 1. **carrousel-[OUTIL]-v3.md**

Modèle de structure (7 slides):

```markdown
# Carrousel Instagram — [OUTIL] v3
**Compte :** brief.ia
**Format :** 7 slides
**Angle :** [Votre hypothèse principale]

---

## SLIDE 1 — Hook
**Visuel :** Fond noir uni. Texte centré.
**Texte :**
> [Accroche percutante avec chiffre concret]
> 
> [Résultat absurde ou surprise]
> 
> *Voilà ce que les démos ne montrent jamais.*

---

## SLIDE 2 — Le test
**Visuel :** Screenshot [NOM] à droite.
**Texte :**
> **Ce que j'ai voulu [FAIRE]**
> 
> [Description courte du test setup]
> 
> Temps estimé : [X]h.
> Spoiler : [twist/surprise].

---

## SLIDE 3 — Vérité #1
**Visuel :** Screenshot [NOM] en fond.
**Texte :**
> **Vérité #1**
> [Affirmation courte]
> 
> [Details de ce qui s'est passé]
> 
> Réalité : [chiffre ou découverte clé]

---

## SLIDE 4 — Vérité #2
[Même structure — incluez screenshot + découverte]

---

## SLIDE 5 — Vérité #3
[Même structure — incluez screenshot + découverte]

---

## SLIDE 6 — Les chiffres
**Visuel :** Fond sombre uni.
**Texte :** (Texte seul, pas screenshot)
> **Ce que ça donne vraiment**
> 
> ⏱ Setup : [Xh]
> ⏱ Premier cycle : [+Y min]
> 📄 Résultat : [oui/non/partial]
> 🔧 Interventions manuelles : [combien]
> 💸 Coût : [montant]
> 
> Utilisable ? **[Verdict court]**

---

## SLIDE 7 — Verdict + CTA
**Visuel :** Fond noir. Logo brief.ia coin haut-gauche.
**Texte :**
> **Verdict brief.ia**
> 
> [Affirmation #1 sur ce qui fonctionne]
> [Affirmation #2 sur la friction]
> 
> ✅ Pour toi si : [Use case]
> ❌ Pas pour toi si : [Limites claires]
> 
> **Score : [X] / 5**
> 
> 💬 Commente [KEYWORD]
> et je t'envoie le test complet en DM.
```

### 2. **reel-[OUTIL]-v3.md**

Modèle script reel (30–40s):

```markdown
# Reel Instagram — [OUTIL] v3
**Format :** Texte animé — 28–35 secondes

## Script

> **[1]** — 3 sec
> [Accroche forte avec chiffre]
>
> **[2]** — 2 sec
> [Situation initiale]
>
> **[3]** — 2 sec
> [Setup description]
>
> **[4]** — 3 sec
> [Découverte #1]
>
> **[5]** — 3 sec
> [Découverte #2]
>
> **[6]** — 2 sec
> [Résultat intermédiaire]
>
> **[7]** — 3 sec
> [Découverte clé]
>
> **[8]** — 2 sec
> [Tension/question]
>
> **[9]** — 3 sec — PAUSE
> [Conclusion forte en 1 phrase]
>
> **[10]** — 3 sec
> **Score : [X] / 5**
> Commente [KEYWORD] → test complet.
```

### 3. **stories-[OUTIL].md**

```markdown
# Stories Instagram — [OUTIL]

## J0 — Tease
> Je teste [OUTIL] ce matin.
> [Promesse de l'outil en 1 ligne]
> Verdict dans 48h. 👀

## J1 — Setup + Live
Story 1:
> [Description de ce que j'ai voulu faire]
> [Temps estimé vs réel]

Story 2:
> [Observation/découverte live]
> Suite demain →

## J3 — Relais
> Vous avez vu le carrousel ?
> [Hook rapide]
> Commente [KEYWORD] pour la version complète.
```

---

## PENDANT LE TEST: Prenez les screenshots clés

**Minimum à capturer:**
1. **Homepage/présentation de l'outil** (pour context)
2. **Interface setup/configuration** (ce que vous avez dû faire)
3. **Résultats/output visible** (la preuve que ça fonctionne)
4. **Point de friction ou surprise** (la découverte clé)
5. **Résultat final** (ce que l'outil a produit)

**Nommez les screenshots:** `[nom-outil]/[type]-[numero].png`
- Ex: `paperclip/setup-1.png`, `paperclip/results.png`, etc.

---

## APRÈS LE TEST: Remplissez les templates

1. **Lisez vos notes du test**
2. **Remplissez `carrousel-[OUTIL]-v3.md`** avec les vraies données
3. **Remplissez `reel-[OUTIL]-v3.md`** avec le vrai script
4. **Remplissez `stories-[OUTIL].md`** avec les vrai quotes
5. **Testez la lisibilité:** le texte est-il compréhensible en 2 phrases ?

---

## CANVA CHECKLIST UNIVERSELLE

Pour TOUT nouveau test:

- [ ] Fond noir (#000000) pour slides texte
- [ ] Fond sombre (#1a1a1a) pour slides screenshot
- [ ] Texte blanc par défaut, cyan (#00AAFF) pour highlights
- [ ] Badge "TEST & VERDICT" slide 1
- [ ] Screenshots: opacité 30–60% si en fond, 100% si visible
- [ ] Score en TRÈS GRAND (70–80pt) slide 7
- [ ] Logo brief.ia slide 7 coin haut-gauche
- [ ] Tout texte lisible sur mobile
- [ ] Transitions: aucune (ou cut sec)

---

## CAPTION TEMPLATE (adapter)

```
[Accroche + chiffre du test]

[OUTIL] promet [PROMESSE].
J'ai cherché [ANGLE].
J'ai tout trouvé.

[Nombre] vérités que les démos ne montrent jamais → swipe

💬 Commente [KEYWORD] et je t'envoie le test complet en DM.

#IA #[OUTIL] #Automatisation #Solopreneur #Fondateur #OutilsIA #AItools #Freelance #BriefIA
```

---

## RYTHME: 1 OUTIL PAR SEMAINE MAX

| Semaine | Outil | Status |
|---------|-------|--------|
| S1 (13–17 avril) | Paperclip | ✅ Prêt |
| S2 (20–24 avril) | [À choisir] | À planifier |
| S3+ | [À choisir] | À planifier |

**Règle:** Ne testez qu'un outil par semaine. Pas 2–3 en parallèle (burnout garanti).

---

## ERREURS À NE PAS REFAIRE

❌ Plus bas de 7/10 sur l'honnêteté → pas de publication (silence > bullshit)
❌ Tester un outil juste parce qu'il buzzed → testez ce que VOUS utilisiez réellement
❌ Publier avant d'avoir le score final → attendez d'être décidé
❌ Mélanger "c'est cool" et "je l'utilise" → marquez la différence

✅ Testez = vous utilisez vraiment pour quelque chose
✅ Verdict clair = vous savez pour qui c'est, pour qui c'est pas
✅ Chiffres réels = durée, coût, résultat mesurable
✅ Screenshots = crédibilité (on voit le vrai outil)

---

## PROCHAINE ÉTAPE: SEMAINE 2

Pour tester un 2e outil (semaine du 20–24 avril):

1. **Dimanche:** Décidez quel outil (basé sur vos vrais besoins)
2. **Lundi:** Créez les fichiers `.md` templates (vides)
3. **Mardi–Mercredi:** Testez l'outil (2–3h)
4. **Jeudi:** Remplissez les fichiers `.md`
5. **Jeudi–Vendredi:** Créez Canva + Reel
6. **Samedi:** Programmez tout pour la semaine suivante

---

**Vous êtes prêt pour Paperclip ?** 🚀

Allez-y!
