# Problems in work

Dziennik problemów napotkanych podczas pracy nad kodem (osobny od `error_codes.md`, który
jest ściągą kodów błędów XPlanar — tu chodzi o problemy projektowe/implementacyjne).

## Format wpisu

```
### [status] Krótki tytuł

Kontekst / co się dzieje.

**Rozwiązanie:** (dopisywane po rozwiązaniu)
```

Statusy: `OTWARTE`, `CZĘŚCIOWO ROZWIĄZANE`, `ROZWIĄZANE`.

---

### [ROZWIĄZANE] `ST_PartTrackingData` był pustym placeholderem

Struktura istniała tylko po to, żeby projekt się kompilował (property `P_PartTracking` ją
referencowała, ale sam typ nie miał żadnych pól).

**Rozwiązanie:** wypełniono polami podanymi przez użytkownika: `OK_ToProcess, NOK_ToProcess,
bInitRun, WellplateStatus, WellplateNOK_Reason, nDestinationProcess, nPriority, nSerial,
PuncherProcessResults[1..96], PipeteProcesResults[1..96], DoseProcesResult[1..12]`
(`ARRAY OF ST_ProcessResult`). Usunięto duplikat `PipeteProcesResults`, który pojawił się
dwukrotnie na przesłanej liście.

**Uwaga do sprawdzenia:** to jest niemal identyczne z istniejącym `ST_ProductData`
(`DMMS_PLC\Mover\DUTs\ST_ProductData.TcDUT`) — różnica to tylko dodane `DoseProcesResult[1..12]`.
`ST_ProductData` jest już osobnym polem `ProcessData` w `ST_Com_ExportMover`. Jeśli
`ST_PartTrackingData` ma reprezentować dokładnie to samo co `ProcessData`, mamy teraz
dwa niemal identyczne pola w tej samej strukturze komunikacyjnej movera — warto zdecydować,
czy to celowe (osobne koncepty) czy duplikacja do posprzątania.

### [CZĘŚCIOWO ROZWIĄZANE] Brak schematu numeracji stacji dla `P_CurrentStation`

`P_CurrentStation` (property na `FB_ApplicationMover`, typ `UINT`) miało gotowe Get/Set,
ale nic nigdzie nie ustawiało do niej wartości — w projekcie nie było żadnego istniejącego
schematu numerowania stacji.

**Rozwiązanie (częściowe):** dodano `ST_EStationName` (`DMMS_PLC\DUTs\Communiction\Station\ST_EStationName.TcDUT`)
z wartościami `ST01`=1 (puncher) ... `ST06`=6 (user station), wg legendy dostarczonej przez użytkownika.
Wciąż brakuje: podpięcia w każdym FB stacji (`FB_PuncherStation`, `FB_PuncherSeparateStation`,
`FB_PuncherBufferStation`) w miejscu, gdzie stacja przejmuje/zwalnia movera — trzeba znaleźć
dokładny punkt w kodzie i dopisać `GVL.g_Movers[nMoverIndex].P_CurrentStation := ST_EStationName.STxx;`.

### [OTWARTE] Brak źródła danych dla `P_TrackPos`

`P_TrackPos` (LREAL) ma gotowe Get/Set, ale nie znaleziono w interfejsie `std`
(`I_XPlanarMoverStandard`) żadnego gotowego pola/metody zwracającej pozycję na tracku
(w odróżnieniu od `P_ActPosition`, które jest pozycją w globalnym układzie X/Y/C).
Trzeba sprawdzić w IntelliSense / manualu Beckhoffa, czy taka wartość jest w ogóle
udostępniana przez bibliotekę, zanim napisze się logikę ją liczącą.

### [OTWARTE] Błędy grupowe nie są przypisywane do konkretnego movera

W `FB_MotionSystem.TcPOU` (linie ~1120–1370) błędy komend systemowych
(`fbXPlanarSystem.P_EnableMovers.Error`, `P_EnableGroup.Error`, `P_EnableTracks.Error`,
`P_AddTracksToGroup.Error`, `P_AddMoversToGroup.Error`, `P_AddEnviromentToGroup.Error`)
dotyczą całej grupy/systemu naraz, nie pojedynczego movera — nie ma tam pętli po `index`,
więc nie da się ich bezpośrednio podpiąć pod `P_Error`/`P_ErrorID` jednego konkretnego movera
bez dodatkowej decyzji projektowej (np. rozgłoszenie błędu do wszystkich movers w grupie?).

### [OTWARTE] `P_Error` nigdy nie wraca na `FALSE`

`P_Error` jest ustawiane na `TRUE` w miejscach, gdzie łapiemy błąd konkretnego movera
(`FB_MotionSystem`, `nMoverToCorrect`/`nMoverToTurn`), ale nigdzie nie ma logiki, która by
je resetowała z powrotem na `FALSE`. To ten sam wzorzec problemu co w `readme.md`
(sekwencje state machine, które nie mają jawnego kroku recovery) — restart/reset musi być
zrobiony kodem (np. przy `ResetMovers()`/wejściu w `Starting`), nie ręcznym wpisaniem zera.

### [ROZWIĄZANE] `I_MoverApplication` nie deklarował nowych property — kod z `FB_MotionSystem` by się nie skompilował

`GVL.g_Movers` jest typu `ARRAY[...] OF I_MoverApplication` (interfejs, nie konkretny FB).
Dopisane wcześniej `GVL.g_Movers[...].P_ErrorID := ...` / `.P_Error := ...` w `FB_MotionSystem`
odwoływały się do property, których **interfejs `I_MoverApplication` w ogóle nie deklarował**
— przez interfejs widać tylko to, co w nim jawnie zadeklarowane, więc to by nie przeszło kompilacji.

**Rozwiązanie:** dodano deklaracje `P_CurrentStation`, `P_Enable`, `P_Error`, `P_ErrorID`,
`P_TrackPos`, `P_PartTracking` do `Mover\I_MoverApplication.TcIO` (same sygnatury Get/Set,
bez ciała — interfejsy tylko deklarują). Teraz `FB_ApplicationMover` faktycznie spełnia
kontrakt interfejsu z tymi property.

### [ZROBIONE — infrastruktura] Komunikacja stacji (analogicznie do moverów)

Na podstawie nowej specyfikacji Excel dla stacji:

- Przebudowano `ST_ComOut_ExportStation.TcDUT` / `ST_ComIn_ExportStation.TcDUT` (pola:
  `Enable, ProcessComplete, OK, NOK, Error, StatusWord, StationName, Error_ID, ProcesedMover,
  MoversList[1..10]` / `Enable, StationName, ControlWord`) — **usunięto stare pola**
  (`MoverInStation, InProcess, CmdToPC, ID_Mover, CMD_status`), które nigdzie w kodzie nie były
  używane (sprawdzone grepem przed usunięciem).
- Dodano `{attribute 'pack_mode' := '1'}` do obu struktur stacji (wcześniej go nie było —
  niespójne z konwencją pyads używaną wszędzie indziej).
- Nowy plik `ST_ManMov_Station.TcDUT` (`CMD, CMD_Confirm, CMD_done`) + dopięty jako
  `ManualMovement` w `ST_Com_ExportStation.TcDUT`.
- Dodano 10 nowych property (Enable, ProcessComplete, OK, NOK, ComError, StatusWord,
  ComErrorID, ProcesedMover, MoversList, ControlWord) do `FB_StationBase.TcPOU` — proste
  magazyny, jak przy moverach.
- **Uzupełniono `FB_StationBase.Cycle()`** (wcześniej było kompletnie puste — sam średnik!) —
  teraz mapuje `THIS^` property do `Communication.g_Com_Stations[nStationIndex]`, dopasowując
  slot przez **już istniejące** `nStationIndex` (ustawiane na sztywno 1/2/3 w
  `FB_PuncherStation`/`FB_PuncherSeparateStation`/`FB_PuncherBufferStation` — nie wymyślałem
  nowego mechanizmu identyfikacji, użyłem tego co już było).
- **Krytyczne odkrycie:** `GVL.g_Stations[index].Cycle()` **nigdzie nie było wcześniej wołane**
  (w przeciwieństwie do moverów, gdzie `GVL.g_Movers[index].Cycle()` już istniało w
  `FB_MotionSystem.Cycle()`) — cała ta logika byłaby martwym kodem. Dopisano pętlę
  `FOR index := 1 TO GVL.gc_NumberStations DO GVL.g_Stations[index].Cycle(); END_FOR`
  w `FB_MotionSystem.Cycle()`, tuż po pętli po trackach.

### [OTWARTE] Manual movement stacji — tylko struktura, brak logiki wykonawczej

`ST_ManMov_Station` (`CMD, CMD_Confirm, CMD_done`) istnieje jako typ i pole w
`ST_Com_ExportStation`, ale **nic go nie czyta ani nie zapisuje** — nie ma odpowiednika
metody `ManualMovement` (jak przy moverze) dla stacji. Nie wiadomo, jakie kody `CMD` mają
jakie znaczenie (nie było tego w specyfikacji), więc nie zgadywałem logiki wykonawczej.

### [OTWARTE] `ProcesedMover` / `MoversList` nigdy nie są wypełniane

Property `P_ProcesedMover` i `P_MoversList` na `FB_StationBase` są gotowe (Get/Set działa,
`Cycle()` je eksportuje), ale nic w projekcie nie ustawia, który mover jest aktualnie
obsługiwany ani kto czeka w kolejce — ta logika musi powstać w konkretnych FB stacji
(`FB_PuncherStation` itd.), tam gdzie już zarządzają listami moverów (`fbList_Station` itd.).

### [OTWARTE] Rozjazd numeracji stacji: `nStationIndex`/`GVL.PuncherStation` (1/2/3) vs legenda `ST01..ST06`

To jest ważne i **świadomie nierozwiązane**. W projekcie już istnieje numeracja stacji:
`GVL.PuncherStation:=1, GVL.PuncherSeparateStation:=2, GVL.PuncherBufferStation:=3`
(3 stacje, dokładnie tyle ile `gc_NumberStations`). Twoja nowa legenda dla `StationName` mówi:
`ST01=puncher, ST02=gripper, ST03=puncher buffer, ST04=dose station, ST05=shacking station,
ST06=user station` (6 typów).

**Te dwie numeracje się NIE pokrywają:** `ST01`(1)=puncher pasuje do istniejącego indeksu 1,
`ST03`(3)="puncher buffer" pasuje do indeksu 3 — ale `ST02`(2)=gripper **nie pasuje** do
`PuncherSeparateStation` (indeks 2, to nie jest gripper). W `Cycle()` na razie eksportuję
**surowy `nStationIndex`** jako `OUT.StationName` (czyli 1/2/3), **nie** przepuszczam go przez
`ST_EStationName` (ST01..ST06) — bo nie wiem, czy chcesz mapować 1→ST01, 3→ST03, a co z
indeksem 2 (gripper wg legendy, ale w kodzie to PuncherSeparateStation)? To wymaga Twojej
decyzji, nie zgadywania.

### [ROZWIĄZANE] Niespójność typu `StationName` między istniejącą strukturą a nową specyfikacją

Istniejące `ST_ComOut_ExportStation.TcDUT` / `ST_ComIn_ExportStation.TcDUT` miały
`StationName: STRING(30)`, nowa specyfikacja chciała `INT`.

**Rozwiązanie:** przebudowano obie struktury zgodnie z nową specyfikacją (`StationName: INT`
+ reszta pól z Excela) — patrz wpis „Komunikacja stacji" wyżej. Świadomie **nie** przepuszczono
wartości przez `ST_EStationName` w `Cycle()` — patrz osobny wpis o rozjeździe numeracji ST01..ST06
vs `nStationIndex` 1/2/3, to wciąż otwarte.
