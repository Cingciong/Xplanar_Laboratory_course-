# XPlanar — ściąga kodów błędów

Kompletny katalog kodów błędów XPlanara. Trzy źródła:

1. **Sekcja A** — błędy NC / komend biblioteki (napotkane realnie w tym projekcie),
2. **Sekcja B** — pełny katalog zdarzeń drivera `TcIoXPlanar` (88 pozycji, wyciągnięte
   z definicji zdarzeń w `DMMS_XPlanar.tsproj`),
3. **Sekcja C** — jak samemu odczytać kod i gdzie szukać.

> **Jak czytać kod:** przełącz watch zmiennej `nErrorID` / `ErrorID` na **HEX**
> (prawy przycisk na zmiennej → Display → Hexadecimal). Kody z zakresu `0x33xxxxxx`
> to zdarzenia drivera XPlanar (sekcja B). Kody `0x4xxx` / `33xxx` (dec) to błędy
> rdzenia NC (sekcja A).

---

## Sekcja A — błędy NC / komend (najczęstsze w praktyce)

Te kody zwracają metody biblioteki `Tc3_XPlanarStandard` (`P_EnableMovers.ErrorID`,
`P_MoveToPosition.ErrorID`, `P_BuildTrackExt.ErrorID` itd.). Zakres „Further Error Codes"
rdzenia NC — opisane w InfoSys pod *TC3 Motion → NC Error Codes*.

| Dec | Hex | Znaczenie | Typowa przyczyna w tym projekcie |
|---|---|---|---|
| **18000** | 0x4650 | Drive hardware not ready | brak zasilania mocy / E-stop wciśnięty / napęd w rozruchu / mover w błędzie. Sprawdź DC-link kafelka (CoE-Online, `DcLinkVoltage` > 6 V) i pulpit bezpieczeństwa |
| **33093** | 0x8145 | Missing cyclic interface NC ↔ PLC | zerwany link obiektu (mover / grupa / environment / track). **Po dodaniu/usunięciu zmiennych PLC zawsze `Activate Configuration`** — sam Login nie przelicza mappingu |
| **33105** | 0x8151 | Command not allowed in current axis state | `EnableMovers` na już włączonym moverze; `MoveToPosition` gdy mover w trybie `OnTrack` (trzeba `MoveOnTrack`); ręczne zerowanie liczników nie resetuje stanu NC → użyj `ResetMovers` |
| **33158** | 0x8186 | Collision Avoidance odrzuciło ruch | cel poza powierzchnią (Environment) albo kolizja z innym moverem. `stInfo.nObjectType`/`nObjectID` mówią, co zablokowało |
| **33160** | 0x8188 | Build track — geometria odrzucona | segmenty tracka nie łączą się / wychodzą poza powierzchnię / obiekt NC ma parametry innej sieci tracków. **Czytaj `P_BuildTrackExtInfoText`** — driver opisuje słownie, co jest nie tak |

> Kody `33xxx` w tej tabeli to wartości **dziesiętne** (tak pokazuje je zmienna UDINT).
> Ten sam błąd w HEX bywa łatwiejszy do znalezienia w InfoSys.

### stInfo — kto zawinił przy błędzie ruchu/enable

Przy `MoveToPosition`, `EnableMovers`, `AddMoversToGroup` struktura `stInfo` wskazuje obiekt:

- `stInfo.nObjectType` — typ obiektu (np. 304 = Environment)
- `stInfo.nObjectID` — konkretny obiekt (np. `0x05120020` = Environment, `0x0512xxxx` = grupa/track)

Oba movery wskazujące **ten sam** `nObjectID` typu Environment = ruch wyprowadza poza kafelki.

---

## Sekcja B — katalog zdarzeń drivera TcIoXPlanar (0x33xx xxxx)

Pełna lista z konfiguracji. Grupy wg 3–4 cyfry hex.

### 0x3317_00xx — komunikacja / identyfikacja moverów (Coordinated Mover Communication)

| Hex | Symbol | Opis |
|---|---|---|
| 0x33170029 | CouldNotProcessAllCommands | Nie przetworzono wszystkich odpowiedzi ({1} z {2}) |
| 0x3317002B | MoverNotAbleToIdentify | Mover nie potrafi się zidentyfikować / brak poprawnego BTN |
| 0x3317002C | MoverError | {1} mover(ów) ma błąd — komunikacja przerwana |
| 0x3317002D | ConfiguredBtnNotIdentified | Skonfigurowany BTN '{1}' nie znaleziony na systemie |
| 0x3317002E | Failed | Komunikacja koordynowana nie powiodła się |
| 0x33170035 | WrongMoverType | Zły typ movera — nie potrafi komunikować |
| 0x3317003C | BtnIdentifiedMultipleTimes | BTN '{1}' zidentyfikowany wielokrotnie |
| 0x3317003D | InvalidTileFirmware | Firmware kafelka za stary (wymagana ≥ 4) |
| 0x3317003E | TileDcLinkVoltageNotOk | Napięcie DC-link kafelka nie OK |
| 0x3317003F | PartHasAnError | Part ma błąd, {2} kafelków w błędzie |
| 0x33170040 | MoverIsActivated | Mover jest aktywny — komunikacja wymaga wyłączonych moverów |
| 0x33170044 | IdentifiedBtnNotConfigured | Zidentyfikowany BTN '{1}' nie jest skonfigurowany |
| 0x3317004B | NoMovers | Nie znaleziono moverów na systemie |
| 0x3317004C | OrientationWrongMoverType | Zły typ movera — nie da się określić orientacji |
| 0x3317004D | FailedPreparation | Przygotowanie komunikacji movera nie powiodło się |
| 0x3317004E | FailedCommunication | Komunikacja movera nie powiodła się |
| 0x3317004F | UncertainOrientation | Określona orientacja movera jest niepewna |

### 0x33172000 — multicomputing

| Hex | Symbol | Opis |
|---|---|---|
| 0x33172000 | SameTargetButDifferentTasks | Peers z tym samym targetem muszą być w tym samym tasku |

### 0x3317_50xx — enable / stan / feedback movera (najważniejsza grupa)

| Hex | Symbol | Opis |
|---|---|---|
| 0x33175001 | CouldNotReachStartHeight | Nie osiągnięto zdefiniowanej wysokości startowej (lewitacja) |
| 0x33175002 | BtnNotFound | BTN ({1}) nie znaleziony — mover/kafelek bez dopasowania kalibracji |
| 0x33175003 | FeedbackVersionNotAvailable | Wybrana wersja feedbacku niedostępna |
| 0x33175007 | InitOfMoverFailed | Inicjalizacja movera nie powiodła się |
| 0x33175008 | MoverPositionOutsideOfMovementArea | Pozycja poza obszarem ruchu — zatrzymanie movera |
| 0x33175009 | NcMappingError | Błąd mappingu NC |
| 0x3317500A | FeedbackError | Błąd feedbacku |
| 0x3317500B | NcCycleTimeCouldNotBeDetermined | Nie ustalono czasu cyklu NC |
| 0x3317500C | UnreachablePositionSetpoints | Setpointy pozycji nieosiągalne (oś/setpoint/pozycja aktualna) |
| 0x3317500F | CouldNotEnterMovementArea | Nie udało się wejść w obszar ruchu |
| 0x33175010 | ObserverError | Błąd obserwatora — złe parametry |
| 0x33175011 | RotatedMoverError | Mover obrócony — enable niemożliwy |
| 0x33175012–18 | ForceLimits… | Parametry limitów siły poza zakresem (min>max, poniżej zera, zero w DOF) |
| 0x3317501A | NoRotationAtThisPosition | Setpoint C nieosiągalny w tej pozycji |
| 0x3317501D | NoMovementAreaAssigned | Mover nie przypisany do obszaru ruchu — enable niemożliwy |
| 0x3317501F | NotAllowedToLeaveMovementAreaWhenFlying | Mover nie może opuścić obszaru gdy aktywny — najpierw disable |
| 0x33175022 | NcPartNotFound | Part OID z NC nie znaleziony |
| 0x33175023 | IsOnPartWithError | Mover na parcie z błędem → stan błędu |
| 0x33175024 | UsesDeactivatedPart | Mover używa dezaktywowanego partu |
| 0x33175026 | SystemCouldNotBeEnabled | Mover nie może enable — part i kafelki się nie włączyły |
| 0x33175027 | MoverHasError | Mover ma błąd — próba komunikacji przerwana |
| 0x33175028 | InvalidTileFw | Zła firmware kafelka (wymagana ≥ 4) |
| 0x33175029 | TileDCLinkVoltageTooLow | Napięcie DC-link kafelka za niskie |
| 0x3317502A | CouldNotSwitchSystemOn | Nie udało się załączyć systemu |
| 0x3317502B | CommunicationFailed | Komunikacja movera nie powiodła się |
| 0x3317502C | FileTransferFailed | Transfer pliku do movera nie powiódł się |
| 0x3317502E | MoverCannotBeReset | Mover nie może się zresetować — part się nie resetuje |
| 0x33175030 | OrientationDeterminationNotAllowed | Określanie orientacji niedozwolone dla tego typu movera |
| 0x33175031 | PartHasAnError | Part używany przez movera ma błąd |
| 0x33175032 | MoverNotAbleToCommunicate | Brak bumpera ID — komunikacja niemożliwa |
| 0x33175033 | MoverIsActivated | Mover aktywny — komunikacja przerwana |
| 0x33175034 | OrientationUncertain | Orientacja movera niepewna |
| 0x33175035 | MoverCannotBeReenabled | Nie można ponownie enable — setpointy NC poza zakresem |
| 0x33175036 | CouldNotCancelMoverTransfer | Nie anulowano transferu movera |
| 0x33175038 | CouldNotFinishMoverAdoption | Nie zakończono adopcji movera |
| **0x33175039** | RemovedFromMaDueToLostEtherCat | **Mover usunięty z obszaru — utrata EtherCAT jednego z kafelków** |
| 0x3317503A | ExternalFeedbackDeviationTooLarge | Zbyt duże odchylenie feedbacku zewnętrznego |
| 0x3317503C | ActivateMoverTransferFailed | Aktywacja transferu movera nie powiodła się |
| 0x33175041 | MoverTransferNotActivated | Mover między dwoma systemami, transfer nieaktywowany |
| 0x33175042 | OrientationBumperOutsideTile | Bumper movera poza obszarem kafelka |
| 0x33175043 | OrientationWrongMoverFirmware | Zła firmware movera (wymagana > 3) |
| 0x33175044 | TransmissionFailed | Transmisja wiadomości do movera nie powiodła się |
| 0x33175045 | ReceptionFailed | Poziom sygnału odpowiedzi movera za niski |
| 0x33175046 | DecodingFailed | Wiadomość od movera nieprawidłowa |
| 0x33175047 | OrientingMoverFailed | Mover obrócony, nie da się zorientować |
| 0x33175048 | MoverPositionChanged | Pozycja movera zmieniła się podczas komunikacji |
| 0x33175049 | CouldNotEstablishCommunication | Nie nawiązano komunikacji z moverem |

### 0x3317_60xx — sprzęt / zasilanie / temperatura (system shutdown)

| Hex | Symbol | Opis |
|---|---|---|
| 0x33176002 | EtherCatCommunicationLost | Utrata EtherCAT — system wyłączany |
| 0x33176004 | PowerSupplyTemperatureTooHigh | Temperatura zasilacza przekroczona — shutdown |
| 0x33176005 | TileTemperatureTooHigh | Temperatura kafelka przekroczona — shutdown |
| 0x33176007 | HardwareError | Błąd sprzętowy |
| 0x3317600B | CouldNotResetTile | Nie udało się zresetować kafelka |

### 0x3317_80xx / 90xx — part detection / software coupling (submovery)

| Hex | Symbol | Opis |
|---|---|---|
| 0x33178006 | TileHardwareError | Jeden kafelek partu ma błąd — part i movery wyłączane |
| 0x33178009 | PartDetectionNotPossible | Redetekcja partu niemożliwa |
| 0x33179008 | SubMoversInDifferentMovementArea | Submovery w różnych obszarach ruchu |
| 0x3317900E | SubMoverPositionsMismatch | Niezgodność pozycji submoverów |
| 0x33179100 | SoftwareCouplingInitializationCheckFail | Sprzężenie programowe — zła inicjalizacja |
| 0x33179101 | SoftwareCouplingSubmoverError | Submover ma błąd w sprzężeniu |
| 0x33179102 | SoftwareCouplingNoAvailableMemory | Brak pamięci na sprzężenie |
| 0x33179103 | NumberOfSubmoversNotSupported | Nieobsługiwana liczba submoverów |
| 0x33179104 | SoftwareCouplingSubmoverControlOff | Sterowanie submovera wyłączone |
| 0x33179105 | SoftwareCouplingInvalidSetpoints | Nieprawidłowe setpointy sprzężenia |
| 0x33179106 | SoftwareCouplingSubmoverTouchPowerLimit | Submover dotknął limitu mocy — sprzężenie wyłączone |
| 0x33179108 | SoftwareCouplingActiveIndexNotValid | Aktywny indeks niedostępny |

### 0x3317_00xx — konfiguracja kafelków / BTN (z zakresu setup)

| Hex | Symbol | Opis |
|---|---|---|
| 0x33170010 | (tile BTN) | Ten sam BTN skonfigurowany dla więcej niż jednego kafelka |
| 0x33171000 | (mover detection) | Inicjalizacja detekcji moverów nie powiodła się (brak moverów) |
| 0x33175002 | BtnNotFound | BTN nie znaleziony (patrz wyżej) |

---

## Sekcja C — jak diagnozować

### Odczyt kodu
1. Watch na `nErrorID` (lub `.ErrorID` danej komendy) → prawy → Display → **Hexadecimal**
2. Kod `0x33xxxxxx` → znajdź w Sekcji B tego pliku
3. Kod `0x4xxx` lub `33xxx` (dec) → Sekcja A / InfoSys NC Error Codes

### Gdzie szukać przyczyny — hierarchia
Zawsze od dołu łańcucha w górę:

```
Sprzęt (EtherCAT OP? DC-link?) → Driver XPU (DetectedAPMxxxx?) → Oś NC → PLC
```

- **grupa 60xx / 18000 / 33175039** → problem sprzętowy (moc, EtherCAT, temperatura). Nie szukaj w kodzie
- **33093 / 5009 NcMappingError** → linki NC↔PLC. Po zmianie process image: `Activate Configuration`
- **grupa 00xx (komunikacja)** → identyfikacja BTN, wymaga bumperów ID + zasilania
- **33158** → Collision Avoidance, czytaj `stInfo`
- **33160** → geometria tracka, czytaj `P_BuildTrackExtInfoText`

### Tekstowe pola diagnostyczne (czytaj je zamiast zgadywać!)
| Pole | Kiedy | Co mówi |
|---|---|---|
| `P_BuildTrackExtInfoText` | błąd budowy tracka | słowny opis, co z geometrią |
| `P_InfoText` (TrackTable) | walidacja tracka | zawartość geometrii |
| `stInfo.nObjectType/ID` | błąd ruchu/enable | który obiekt zablokował |
| **TwinCAT Logged Events** | zawsze | driver opisuje zdarzenia słownie (View → Other Windows → TwinCAT Logged Events) |

### Diagnostyka w kodzie — wzorzec
Każdy krok błędu w maszynie stanów łapie surowe dane, zamiast być ślepym zaułkiem:
```
nErrorID  := fbXPlanarSystem.P_Xxx.ErrorID;      // kod
nErrObjID := fbXPlanarSystem.P_Xxx.stInfo.nObjectID;  // co zawiniło
```
Manual ma dziury w numeracji kroków (15/25/55) — trzeba je dopisać, inaczej sekwencja
zamiera bez śladu.

---

_Źródło kodów: katalog zdarzeń z `DMMS_XPlanar.tsproj` (definicje `TcIoXPlanar`) +
manuale `Tc3_XPlanarStandard` / `Tc3_XPlanarUtility` (DRAFT) + błędy napotkane w projekcie.
Pełne opisy z parametrami: InfoSys Beckhoff, TC3 Motion NC Error Codes._
