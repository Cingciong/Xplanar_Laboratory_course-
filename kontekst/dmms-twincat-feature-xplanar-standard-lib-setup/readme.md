# DMMS XPlanar — nauka i odtworzenie dokumentacji

## O co chodzi w tym branchu

Ten branch **nie jest branchem deweloperskim**. Jego celem jest **odtworzenie dokumentacji** i przejście krok po kroku przez budowę prototypowego kodu na XPlanara, w oparciu o dostępną dokumentację Beckhoffa — na potrzeby edukacyjne: moje i każdego, kto będzie musiał ruszyć ten system od zera.

Pomysł jest prosty: zamiast trzymać wiedzę w głowie, spisuję **całą drogę** — od pustego projektu do jeżdżących moverów. Każdy problem, na który wpadłem po drodze, jest tu opisany razem z tym, **jak go obeszliśmy**. Dzięki temu następna osoba nie będzie się męczyć tydzień z rzeczami, które da się rozwiązać w pięć minut, jak się wie gdzie kliknąć.

Wszystkie napotkane problemy są opisywane tutaj w markdownie na bieżąco.

---

## Materiały źródłowe

Cała ta praca opiera się na dwóch manualach Beckhoffa (wersje robocze / DRAFT):

- **Tc3_XPlanarStandard Operating Manual** — główna biblioteka aplikacyjna. To praktycznie tutorial krok po kroku (rozdział „Quick Start"): FB_MotionSystem, sekwencje Startup / Starting / Execute, wzorzec komenda→Cycle→feedback, Collision Avoidance, tracki.
- **Tc3_XPlanarUtility Operating Manual** — warstwa niskopoziomowa (TcIo): odczyt konfiguracji sprzętu, diagnostyka kafelków (CoE), detekcja i identyfikacja moverów, movement areas.

Do tego diagram przepływu aplikacji DMMS (`DMMS_Unified_Flowchart`) jako mapa tego, jak docelowy system jest poukładany.

Wszystkie te materiały (oba manuale PDF, flowchart, dodatkowe notatki) leżą w folderze **[`dokumentacja/`](dokumentacja/)** w repozytorium.

---

## Setup środowiska

Pełna instrukcja konfiguracji TwinCAT + XPlanar jest w osobnym pliku:

**[setup_env/setup.md](setup_env/setup.md)**

W skrócie, co trzeba (szczegóły w linku wyżej):

1. **Visual Studio 2017 Community** + **TwinCAT Package Manager** (nakładka na VS).
2. **Instalacja pakietów przez skrypt** — `setup_env/install_packages.py` czyta `CurrentConfig.config` i instaluje biblioteki przez `tcpkg` (obejście zawieszającego się „Load Config" w GUI).
3. **Biblioteka `Tc3_XPlanarStandard`** — nie ma jej w globalnych repozytoriach, leży w `setup_env/Tc3_XPlanarStandard/`. Trzeba ją ręcznie skopiować do `Managed Libraries` i przeładować. **Bez tej biblioteki projekt się nie uruchomi.**
4. **Sieć + AMS NetID + route do IPC** — konfiguracja połączenia ze sterownikiem (statyczne IP `192.168.2.x`, route do urządzenia XPlanar).

> **Uwaga:** komputer musi mieć wyłączoną wirtualizację / Hyper-V / Docker — inaczej runtime TwinCAT nie wystartuje.

---

## Krok po kroku: od zera do jeżdżących moverów

Poniżej cała droga w kolejności, w jakiej się przez nią przechodziło. Format: **objaw → przyczyna → rozwiązanie**. To jest sedno tego dokumentu — realna lista pułapek.

### Faza 1 — Projekt PLC i biblioteka

Zgodnie z manualem (Quick Start): nowy projekt PLC, dodanie bibliotek `Tc3_XPlanarStandard` + `Tc3_Physics`, stworzenie `FB_MotionSystem` z metodą `Cycle()` wołaną co cykl.

**Problem: 20 moverów zamiast 2**
- *Objaw:* po Buildzie w PLC Instance pojawiło się 20 pozycji `fbXPlanarMover[1..20]`.
- *Przyczyna:* tablica jest wymiarowana parametrem biblioteki `maxNumMover`, którego wartość domyślna to 20.
- *Rozwiązanie:* Library Manager → zaznacz `Tc3_XPlanarStandard` → zakładka **Library Parameters** → `Params_XPlanar` → ustaw `maxNumMover = 2` i `moverCount = 2` w kolumnie **Value (editable)** → **Rebuild**.
- *Pułapka:* dolny panel „Documentation" pokazuje zawsze fabryczne wartości (read-only) — to myli. Liczy się górny panel „Library Parameters". I **bez Rebuildu nic się nie zmieni** w Instance.

### Faza 2 — Obiekty MOTION i aktywacja konfiguracji

Movery, grupa Collision Avoidance i Environment muszą istnieć jako obiekty NC w sekcji **MOTION** (MC Project). Tu poszła seria błędów przy aktywacji — każdy odsłaniał kolejny.

**Problem: „Initialization of mover detection failed, no movers configured" (0x33171000)**
- *Przyczyna:* w Configuratorze przy dodawaniu/usuwaniu moverów ostatni eksport poszedł bez żadnego movera.
- *Rozwiązanie:* Configurator → połóż movery na kafelkach → Export/Apply → Activate.

**Problem: „CPU setting mismatch — 2/6 configured, 12/0 found on target"**
- *Przyczyna:* konfiguracja Real-Time z innej maszyny (inna liczba rdzeni).
- *Rozwiązanie:* SYSTEM → Real-Time → Settings → **Read from Target** → przydziel rdzenie → zapisz. Sprawdzić, że taski (PlcTask + taski XPlanara) wskazują na istniejące rdzenie.

**Problem: „The same BTN is configured for more than one tile" (0x33170010)**
- *Przyczyna:* dwa kafelki miały ten sam numer seryjny (BTN) — pozostałość po ręcznym dłubaniu w konfiguracji (kopiowanie kafelka kopiuje też BTN).
- *Rozwiązanie na sprzęcie:* Configurator (połączony z maszyną, Config Mode) → **Scan BTNs** → przypisz każdemu kafelkowi realny numer z jego naklejki (**Assign BTN**). Każdy kafelek = inny BTN.
- *Uwaga:* BTN-y kafelków ustawia się też ręcznie na obiekcie kafelka w TcCOM Objects (dwuklik → Parameter (Init) → pole BTN).

**Problem: „DynamicConstraint_PathXY / _Coordinates / _Container was assigned, this is forbidden" (0x98110700)**
- *Przyczyna:* rozspójniona parametryzacja moverów po wielokrotnym ręcznym modyfikowaniu konfiguracji. Limity dynamiki mają być **dziedziczone** z `XPlanarMoverParametrizationSet`, a nie wpisane bezpośrednio na moverze.
- *Rozwiązanie:* **przywrócenie działającego backupu konfiguracji** (`.tsproj.bak` / migawka `.tnzip`). To ważna lekcja: modyfikowanie działającej konfiguracji sprzętu metodą prób i błędów prowadzi do narastającego uszkodzenia — szybciej jest wrócić do spójnego stanu niż łatać kolejne objawy.

### Faza 3 — Linkowanie PLC ↔ MOTION (najważniejszy etap)

To był największy blocker. Obiekt movera w PLC (`fbXPlanarMover`) i obiekt movera w MOTION to **dwa osobne światy**, które trzeba spiąć przez process image (mapping).

**Model do zapamiętania — mover w MOTION ma cztery „końcówki":**
- `PlcToMc` — komendy z PLC do movera (enable, jedź) — **linkujesz TY**
- `McToPlc` — statusy z movera do PLC (stan, pozycja, Done) — **linkujesz TY**
- `IoToMc` — feedback ze sprzętu (XPU) do movera — linkuje się z XPU (zwykle auto)
- `McToIo` — setpointy z movera do XPU — jw.

**Problem: błąd `33093` (0x8145) „Cyclic interface mapping missing between NC and PLC" przy EnableMovers**
- *Przyczyna:* strona PLC movera nie była zlinkowana. Zmiana rozmiaru tablicy (20→2) i przerobienie FB zerwały istniejące linki.
- *Rozwiązanie:* w MOTION → Axes prawy przycisk na moverze → **Change Axis PLC Links...** → wskaż `fbXPlanarMover[1]` (dla drugiego movera → `fbXPlanarMover[2]`). Ta opcja spina wszystkie podstruktury (STD/SET/ACT/COORDMODE/SETONTRACK) naraz — nie trzeba klikać pin-po-pinie.
- Dodatkowo: zlinkować grupę i environment: `Groups → Planar Group → STD` do `fbXPlanarSystem.group.MCTOPLC_STD`, `Environment → STD` do `fbXPlanarSystem.environment.MCTOPLC_STD`. To komendy **systemowe** (EnableMovers idzie przez `fbXPlanarSystem`), więc bez nich enable padnie mimo zlinkowanych moverów.
- *Weryfikacja:* prawy na końcówce → **Goto Link Variable** (musi przeskoczyć na drugą stronę); w Online wartości mają się zmieniać.
- *Uwaga:* w oknie Change Link odznaczyć **„Only Unused"** i zaznaczyć **„All Types"**, inaczej lista bywa pusta.

### Faza 4 — Kod: typowe błędy składniowe

**`:=` zamiast `:` w deklaracji**
- *Objaw:* `C0006: ',, AT or ':' expected instead of ':='` + kaskada „not defined".
- *Przyczyna:* w deklaracji zmiennych typ podaje się dwukropkiem (`x : FB_XPlanarSystem;`), a `:=` to przypisanie wartości. (Literówka przepisana wprost z PDF-a.)

**`i not defined` w metodach**
- Zmienna pętli `i` musi być zadeklarowana w `VAR` **danej metody** (Cycle/Startup/Execute).

**`nExecutingSequence not defined`**
- *Przyczyna:* liczniki maszyn stanów (`nStartupSequence`, `nStartingSequence`, `nExecutingSequence`) muszą być w `VAR` **samego FB**, nie w metodzie — bo muszą pamiętać stan między cyklami. Zmienne lokalne metody giną po każdym wywołaniu.

### Faza 5 — Włączanie moverów (enable)

**Problem: enable działa po świeżym downloadzie, ale nie po ręcznym restarcie — błąd `33105` (0x8151) „Command not allowed in current axis state"**
- *Przyczyna:* PLC i NC to **dwa niezależne stany**. Ręczne wyzerowanie liczników w online resetuje tylko PLC — a movery w NC zostają włączone z poprzedniego przebiegu. `EnableMovers` na już-włączonym moverze jest zabroniony.
- *Rozwiązanie:* przed enable sprowadzić movery do znanego stanu — **najpierw `ResetMovers()` (poczekać na `.Done`), potem `EnableMovers()`**. Alternatywnie sprawdzić `P_State` i pominąć enable, jeśli mover już `Enabled`.
- *Lekcja:* nie restartuje się przez ręczne wpisywanie zer w liczniki. Restart robi się kodem, który resetuje też stan moverów (w docelowym systemie DMMS służy do tego osobna sekwencja `Resetting`). Warto zrobić jeden „przycisk restartu": stan 0 w MAIN woła `Starting(bReset:=TRUE)` i `Execute(bReset:=TRUE)`.

### Faza 6 — Ruch (movery się podnoszą, ale nie jadą)

**Problem: Execute wpada w nieistniejący krok 15 — `MoveToPosition` zwraca Error**
- *Przyczyna:* współrzędne docelowe z przykładu w manualu (120/360/600) pasują do układu 2×3 z PDF, ale **leżą poza naszą powierzchnią** (mamy inny układ kafelków).
- *Rozwiązanie:* nie wpisywać sztywnych współrzędnych. Odczytać realną pozycję movera (`P_ActPosition`) jako punkt wyjścia i robić **ruch względny** (np. +50 mm w Y od pozycji startowej, potem powrót). Pozycja movera to na pewno punkt na powierzchni, więc mały ruch względny nie wyjedzie poza kafelki.
- *Diagnostyka:* dodać realne kroki błędu (15/25) przechwytujące `P_MoveToPosition.ErrorID` zamiast ślepego zaułka.
- *Pamiętać:* pozycja to **środek movera** — musi zmieścić się z zapasem od krawędzi (mover ~155 mm, środek nie bliżej niż ~80 mm od brzegu). Rotacja C tylko na przecięciach 4 kafelków (co 120 mm).

---

## Wskazówki do debugowania (watch list)

Do podglądu w trybie online — te zmienne mówią, gdzie stoi każda maszyna stanów:

| Zmienna | Co mówi |
|---|---|
| `MAIN.nState` | faza główna (0 init / 1 Startup / 30 Starting / 40 Execute) |
| `fbXMotionUnit.nStartupSequence` | krok Startup (30 = gotowe) |
| `fbXMotionUnit.nStartingSequence` | krok Starting (80 = gotowe; 55 = błąd enable) |
| `fbXMotionUnit.nExecutingSequence` | krok Execute |
| `fbXPlanarMover[1].P_ActPosition` | realna pozycja movera (odświeża się = mapping żyje) |
| `fbXPlanarMover[1].P_State` | stan movera (Disabled / Enabled / Error) |
| `nErrorID` | ostatni kod błędu — przełączyć watch na HEX i szukać w InfoSys |

**Złota zasada:** jak coś „wisi", pierwsze pytanie brzmi — czy `Cycle()` tego obiektu jest wołany co cykl? Bez cyklicznego `Cycle()` komendy nie wychodzą i feedback się nie odświeża.

---

## Linki zewnętrzne

- Opis zmiennych → https://docs.google.com/spreadsheets/d/1pWvlZZPiQmnRhIk3CjhZyXXYygv8_nX20cS1mLHevxo/edit?usp=sharing
- ClickUp → https://app.clickup.com/2568436/v/o/f/90120774939
- Biblioteka pyads → https://pyads.readthedocs.io/en/latest/documentation/index.html

## Oprogramowanie

Wymagany komputer z Windowsem, TwinCAT jako nakładka na Visual Studio. **NIE MOŻNA MIEĆ zainstalowanej wirtualizacji / Dockera.** Instrukcja setupu: [setup_env/setup.md](setup_env/setup.md).

## Użytkowanie

Uruchomić solucję `.sln`. Górną zakładką edytora wybrać target, uruchomić „run in runtime mode" i wgrać program na urządzenie.

## Wkład

Michał · Aneta · Rafał · Artur · Igor

## Licencja

_(do uzupełnienia)_

---

_Dokumentację odtworzył i spisał — Igor._
