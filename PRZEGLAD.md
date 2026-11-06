# Przegląd repozytorium: struktura, rozdziały, literatura, dokumentacja

Stan na 2026-10-13. Temat pracy: *Opracowanie zestawu ćwiczeń laboratoryjnych i instrukcji dydaktycznych dla stanowiska transportowego Beckhoff XPlanar*.

Dokument opisuje, co jest w repozytorium, do czego służy każda część, jak bardzo przyda się w pracy i jak czytelny jest obecny układ. Oceny są moją opinią po przejrzeniu plików (nie czytałem wszystkich 174 PDF-ów w całości).

---

## 1. Mapa w jednym rzucie

```
Xplanar_inzynierka/
├── README.md, TODO.md          ← README zbiorcze (częściowo nieaktualne) + plan 5 laboratoriów
├── 26.08.10_StarterkitBase.tnzip   ← archiwum starter kitu Beckhoffa
├── thesis/                     ← PRACA PISEMNA
│   ├── outline.md, README.md   ← plan pracy i układ folderów
│   ├── guidelines/             ← wytyczne WETI 2026, ZR PG 45/2024, streszczenie
│   ├── template-pl/, template-en/  ← szablony LaTeX (LuaLaTeX)
│   ├── comparison/competitors.md   ← konkurencja XPlanara
│   └── materials/              ← LITERATURA (174 PDF, ok. 570 MB), po rozdziałach
├── instrukcja/                 ← instrukcja laboratoryjna (LaTeX → main.pdf), przyszły załącznik
├── topics/                     ← kody do zadań (start/ i solution/) dla 5 laboratoriów
└── kontekst/                   ← materiał roboczy z poprzedniej pracy: 2 branche projektu PLC,
                                   dokumentacja Beckhoffa, notatki handoff
```

---

## 2. Rozdziały pracy i materiały do nich

Plan z `thesis/outline.md`: 1 Wstęp, 2 Teoria, 3 Istniejące rozwiązania, 4 Możliwości XPlanara, 5 Ćwiczenia, 6 *(puste)*, 7 Podsumowanie, Załączniki.

| Rozdz. | Folder `thesis/materials/` | Zawartość | Liczba PDF | Opis źródeł |
|---|---|---|---|---|
| 1 | `1-introduction/` | Industry 4.0, elastyczna produkcja, rynek pracy (Barometr zawodów 2026), laboratoria Przemysłu 4.0, zastosowania (mikromontaż, farmacja) | 9 | brak |
| 2 | `2-theory/planar-motor-physics/` | Fizyka silników planarnych: komutacja, pola Halbacha, czujniki Halla, sterowanie lewitacją, prace doktorskie (Jansen, van Lierop), patenty klasyczne (Sawyer 1968, Trumper) | 28 | brak |
| 2 | `2-theory/xplanar/` | Patenty Beckhoff (stojan, mover, czujniki, kolizje), baza UBC, artykuły (Janning, Hartmann, SOLEIL, Lund) | 34 | **`sources.md` (39 KB, pełny opis każdej pozycji)** |
| 3 | `3-existing-solutions/direct-2d/` | Konkurenci planarni: Bosch Rexroth ctrlX FLOW6D, Planar Motor, patenty, Waterloo | 13 | brak |
| 3 | `3-existing-solutions/indirect-linear/` | Systemy liniowe: ATS SuperTrak, Rockwell iTRAK/MagneMover/QuickStick, XTS, MCS, patenty | 27 | brak |
| 4.1 | `4-xplanar-capabilities/trajectories/` | Planowanie tras: MAPF/CBS, MPC, minimum-jerk, Ruckig, CBF, manual TF5430, prace z Lund i Gandawy | 24 | brak |
| 4.2 | `4-xplanar-capabilities/communication/` | OPC UA, MQTT, PROFINET, TSN, czas cyklu | 6 | brak |
| 5 | `5-lab-exercises/` | Dydaktyka: Kolb, Biggs (constructive alignment), CDIO, ECTS, KRK/PRK, laboratoria wirtualne, PBL, karty przedmiotów PUT | 25 | brak |
| 7 | `7-summary/` | tylko README-szkielet | 0 | n/d |
| zał. | `appendices-lab-instructions/` | wskazuje na `instrukcja/` | 0 | n/d |

Dodatkowo:

- **`thesis/comparison/competitors.md`** (5 KB): zestawienie konkurencji (ACOPOS 6D, Planar Motor, Siemens, Rockwell, Rexroth; potem systemy liniowe). Zawiera ważną obserwację, że kilka marek korzysta z technologii Planar Motor Inc. Uczciwie oznacza „brak danych”.
- **`thesis/guidelines/guidelines-summary.md`** (2,7 KB): zwięzłe streszczenie wymogów formalnych (Arial 10 pt, interlinia 1,5, PN-ISO 690, oświadczenie o GenAI, układ rozdziałów).

---

## 3. Laboratoria: instrukcja, kody, plan

### `TODO.md`: plan dydaktyczny
Najbardziej wartościowy dokument koncepcyjny. Opisuje 5 laboratoriów i ich kolejność:

1. **Wstęp** (pokaz na maszynie, demo SK12, symulacja `BasicSimulation` na laptopie)
2. **Konfiguracja i włączenie** (backup, pakiety, EtherCAT, lewitacja)
3. **Ruch wysterowany** (6 DoF: `MoveToPosition`, `MoveZ`, `MoveA/B/C`)
4. **Tracki i omijanie kolizji** (Group, błąd 33158, 2 zadania)
5. **Dynamiczne trasowanie** (stacje, zwrotnice)

Ma uzasadnienia dydaktyczne, konkretne parametry (zakresy osi, współrzędne startowe) i szczere uwagi o ograniczeniach.

### `instrukcja/`
Dokument LaTeX (636 linii, ma `main.pdf`), 6 kroków, makro `\zrzutEkranu` z placeholderami, plik `STYL.md` z zasadami pisania, zrzuty ekranu rozdziałów 1 i 2 (TcXaeShell, Configurator, skanowanie IO). To przyszły **załącznik pracy**. Zaawansowanie: rozdziały 1–2 mają zrzuty, dalsze to głównie szkielet.

### `topics/`
Kody do zadań w układzie `start/` + `solution/` dla każdego laboratorium. Stan: rzeczywisty kod jest tylko w `01-introduction/demo/` (StarterkitBase) i pustym projekcie w `02-configuration/start`. Pozostałe `README.md` mają status „kod do uzupełnienia”.

---

## 4. Dokumentacja techniczna (`kontekst/`)

| Element | Co to jest | Wartość |
|---|---|---|
| `kontekst/dokumentacja/*.pdf` | Oficjalne manuale Beckhoff DRAFT: `Tc3_XPlanarStandard` i `Tc3_XPlanarUtility` | Kluczowe: źródło prawdy dla ćwiczeń |
| `kontekst/dokumentacja/error_codes.md` | Ściąga kodów błędów XPlanar (13 KB) | Bardzo praktyczna dla studentów |
| `kontekst/dokumentacja/readme.md` | Droga „od zera do jeżdżących moverów” w formacie objaw → przyczyna → rozwiązanie (12 KB) | Bardzo dobra baza do instrukcji i rozdz. 5 |
| `kontekst/dokumentacja/latex/` | 9 rozdziałów LaTeX: system, PLC, środowisko, diagnostyka, problemy, dziennik (110 KB), wykrywanie moverów, strefa wspólna, BTN | Gotowa wiedza do wykorzystania, ale nieuporządkowana |
| `kontekst/dokumentacja/html/DMMS_architecture.html` | Diagram architektury aplikacji | Pomocny wizualnie |
| `kontekst/dokumentacja/setup_env/` | Skrypt instalacji pakietów, `setup.md`, biblioteka `Tc3_XPlanarStandard` (3.3.2411.0 i 3.3.2505.0) | Niezbędne do odtworzenia środowiska |
| `kontekst/dmms-...-communication-updates/`, `...-xplanar-standard-lib-setup/` | Dwa kompletne projekty TwinCAT z poprzedniej pracy (z archiwami `.tnzip` i plikami PLC) | Wzorzec architektury, **nie** materiał do bezpośredniego użycia w ćwiczeniach |
| `kontekst/.claude/handoffs/` | Notatki z analiz kodu (architektura, bugi, zależność od zewnętrznego PC) | Oszczędza tygodnie czytania kodu |

---

## 5. Jak bardzo przyda się to do pracy

**Wysoka przydatność**
- `2-theory/xplanar/sources.md` plus patenty: gotowa podstawa rozdz. 2 i fragmentu rozdz. 3. Najlepiej opracowana część literatury.
- `5-lab-exercises/`: rzadko spotykany, ale potrzebny zestaw. Uzasadnia „dlaczego tak, a nie inaczej” z perspektywy teorii nauczania (Kolb, Biggs, CDIO) i wymogów prawnych (KRK, PRK). Wprost odpowiada na wymóg rozdz. 5 z `outline.md`.
- `TODO.md` + `instrukcja/` + `kontekst/dokumentacja/`: rdzeń praktyczny pracy, czyli właściwy wkład autorski.
- `4-xplanar-capabilities/trajectories/`: solidny, naukowy kontekst dla podrozdz. 4.1 (MAPF, MPC, CBF), co spełnia założenie „żeby podejście było trochę naukowe”.

**Średnia przydatność**
- `planar-motor-physics/` (28 pozycji, w tym kilkanaście patentów USA z lat 1968–2016): bardzo szeroko. Dla pracy inżynierskiej wystarczy kilka pozycji (Jansen, van Lierop, Kim & Trumper, Xia 2004, Mikroniek). Reszta to materiał „na wszelki wypadek”.
- `3-existing-solutions/`: dobra baza danych technicznych konkurentów, ale `competitors.md` jest na razie krótki względem 40 zebranych PDF-ów.
- `communication/` (6 pozycji): pokrywa OPC UA/MQTT/PROFINET/TSN ogólnie, ale **nie dotyka ADS/pyads**, który jest faktyczną komunikacją w Waszym projekcie.

**Niska przydatność / ryzyko**
- `kontekst/` jako całość: dwa branche kodu z poprzedniej pracy plus archiwa `.tnzip` (ok. 80 tys. plików). Cenne jako wzorzec, ale zaśmieca repozytorium.
- Wiele patentów USA skanowanych bez warstwy tekstowej, więc nie da się ich przeszukiwać ani cytować fragmentów bez ręcznego przepisywania.

---

## 6. Ocena czytelności i spójności

### Co działa dobrze
- Foldery rozdziałów 1:1 z planem pracy; nazwy angielskie, spójne, z numeracją.
- Pliki źródeł mają zrozumiałe nazwy w schemacie `autor-rok-temat.pdf`.
- `sources.md` w `2-theory/xplanar` to wzorzec: opis, link, status pobrania, klucz BibTeX, adnotacja „do którego rozdziału”.
- Wytyczne streszczone w jednym krótkim pliku z hierarchią ważności (ZR → wydział → promotor).
- `TODO.md` i `STYL.md` są konkretne i użyteczne.

### Problemy (od najpoważniejszych)
1. **Bibliografia jest niekompletna.** Tylko jeden z ośmiu folderów ma opis źródeł (`sources.md`). Pozostałe 140 PDF-ów to same pliki bez metadanych. `thesis/praca/_bibliography.bib` zawiera tylko 4 wpisy z szablonu, więc żadne z 174 źródeł nie jest jeszcze w `.bib`. To najważniejsza luka formalna (PN-ISO 690 wymaga pełnych danych).
2. **Główny `README.md` jest nieaktualny.** Opisuje foldery `dokumentacja/`, `test_prog/`, `wzorzec_starter_kit/`, których nie ma na poziomie głównym (dokumentacja jest w `kontekst/dokumentacja/`, a dwa pozostałe nie istnieją). Dodatkowo w terminalu zapisano go w złym kodowaniu, więc część narzędzi pokazuje krzaczki. Warto sprawdzić, że plik jest w UTF-8.
3. **Numeracja rozdziałów jest niespójna.** `outline.md` ma rozdz. 6 „do ustalenia”, `7-summary/README.md` nosi tytuł „Rozdział 4 — Podsumowanie”, a szablon LaTeX ma tylko 4 pliki rozdziałów (`1_introduction` … `4_summary`). Trzeba zdecydować: 6 rozdziałów bez luki albo 7 z rzeczywistą treścią.
4. **README-ki rozdziałów są puste.** Mają po 1–2 zdania („Materiały robocze…”) i nie mówią, co jest w folderze ani co z tego wynika dla treści.
5. **Rozproszenie dokumentacji.** Ta sama wiedza występuje w `README.md`, `TODO.md`, `kontekst/dokumentacja/readme.md`, `kontekst/.claude/handoffs/` i `instrukcja/`. Nie wiadomo, który plik jest nadrzędny. Wg README kopia dokumentacji w dwóch branchach jest bajt-w-bajt identyczna, więc jest też nadmiarowa.
6. **Rozmiar.** ok. 570 MB PDF oraz ok. 80 tys. plików w `kontekst/` utrudniają synchronizację i operacje (listowanie folderu na dysku sieciowym trwa minuty). Warto przenieść PDF-y poza git (np. Git LFS lub Zotero) albo dodać do `.gitignore`.
7. **Śmieci robocze:** `instrukcja/build.log`, `main.aux/.log/.out/.toc`, `.vs/`, pliki `.broken_20260720`, `Untitled1`, `DMMS_XPlanar_0405_notwork.tnzip`. `26.08.10_StarterkitBase.tnzip` leży luzem w katalogu głównym.
8. **Granica „co jest pracą, a co kontekstem”.** `kontekst/` zawiera Wasz wcześniejszy kod, ale `thesis/` o nim nie wspomina. Czytelnik nie wie, które elementy są wkładem autorskim, a które odtworzeniem istniejącego projektu.

### Moja ogólna ocena
| Aspekt | Ocena (1–5) | Komentarz |
|---|---|---|
| Kompletność literatury | 4 | Bardzo bogata i dobrze dobrana tematycznie |
| Opis i indeksacja literatury | 2 | Tylko jeden rozdział opisany, `.bib` pusty |
| Struktura folderów | 4 | Logiczna, zgodna z planem |
| Spójność dokumentacji | 2,5 | Nieaktualny README, rozbieżna numeracja |
| Zaawansowanie części praktycznej | 3 | Dobry plan i instrukcja, kody ćwiczeń dopiero szkieletem |
| Przydatność całości do pracy | 4 | Materiału wystarczy z nawiązką, brakuje porządku |

---

## 7. Rekomendowane kolejne kroki

1. Rozstrzygnąć numerację rozdziałów (z lukiem po rozdz. 5 czy bez) i poprawić `7-summary/README.md` oraz `outline.md`.
2. Zrobić `sources.md` dla pozostałych folderów (można wygenerować z metadanych PDF) i przenieść wpisy do `_bibliography.bib`, korzystając z kluczy `xp-...`.
3. Zaktualizować główny `README.md`: właściwe ścieżki, spis folderów, odesłanie do tego pliku.
4. Wypełnić README-ki rozdziałów: „co tu jest”, „najważniejsze 3–5 źródeł”, „co jeszcze trzeba przeczytać”.
5. Wyczyścić pliki robocze i przenieść `.tnzip` do osobnego folderu (np. `archiwa/`).
6. Dla rozdz. 4.2 dodać źródła o ADS/pyads i EtherCAT, bo to rzeczywiste kanały komunikacji tego stanowiska.
7. Zdecydować, co z `kontekst/`: albo osobne repozytorium, albo wykaz w `thesis/` z opisem, co zostało przejęte.
