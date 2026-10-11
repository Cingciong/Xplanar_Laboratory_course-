# Styl instrukcji (`main.tex`)

Wzorzec: podrozdziały „Środowisko TwinCAT XAE Shell” i „Kod demo SK12” (Wstęp). Nowe i poprawiane fragmenty piszemy tak samo.

## Zasady ogólne
- Język polski, zwięzły, rzeczowy. Krótkie zdania. Bez wykładów, o które autor nie prosił (np. nie tłumaczyć, czym jest czas rzeczywisty, jeśli autor chce tylko wskazać, do czego służy zakładka).
- **Nie dopisujemy treści merytorycznej z własnej inicjatywy.** Autor dyktuje, co ma być napisane. Brakujące miejsca: `\opisDoUzupelnienia{}`.
- Niepewne twierdzenia oznaczamy kursywą: *(do sprawdzenia: …)* albo *(do potwierdzenia: …)*. Źródła niepotwierdzone w dokumentacji Beckhoffa opisujemy w `\uwaga{}`.
- Rozdziały tylko per zagadnienie (5). Bez własnych, numerowanych podtematów typu 2.1.

## Struktura rozdziałów i nagłówków
- `\chapter` = zagadnienie, `\section` = główne bloki, dalej nienumerowane: `\podrozdzial{…}` (trafia do spisu treści) i `\podpodrozdzial{…}` (też do spisu, niższy poziom).
- Kolejność w bloku: **krótkie wprowadzenie → zrzut ekranu → opis tego, co widać** (lista). Zrzut stoi od razu po ogólnym opisie.
- Części Solution Explorera opisujemy po kolei: SYSTEM, MOTION, I/O, PLC; każda ma własny nagłówek.
- W opisie ogólnym najpierw zasady/kontekst, na samym dole dobre praktyki (np. nazewnictwo).
- Na końcu rozdziału: `\subsection*{Dokumentacja Beckhoff (Infosys)}` z listą klikalnych nazw (`\href`), po jednej dla każdego zagadnienia.

## Listy i zdania
- Wypunktowania po przecinku, bez zagnieżdżonych nawiasów; zamiast „(…)” pisać osobnym zdaniem lub po myślniku.
- Definicje w formie: `\textbf{Nazwa} --- krótki opis.` Opis jednym zdaniem; długie opisy skracamy.
- Wyjaśnienia dotyczące bieżącego stanu piszemy z „(aktualnie: …)”, żeby było wiadomo, o który element chodzi (np. aktywny projekt `StarterkitBase`, target `<Local>`).
- Nazwy elementów programu/TwinCAT w `\texttt{}`; pojęcia przy pierwszym użyciu kursywą z tłumaczeniem w nawiasie.

## Zrzuty ekranu
- Makro `\zrzutEkranu[szerokość]{ścieżka względem zdjęcia/}{podpis}`.
- Podpis krótki: `Solution Explorer --- SYSTEM`, `Edytor TcXaeShell --- pasek menu i pasek narzędzi`.
- Nazwa pliku: małe litery, myślniki, bez polskich znaków i spacji, wg schematu elementu, np. `solution-explorer-plc-kod.png`.
- Folder: `zdjęcia/<NN-rozdzial>/<podrozdzial>/`, np. `zdjęcia/01-wstep/czesci-projektu/`.
- Figury ustawiamy na stałe (`[H]`), żeby stały przy swoim opisie.

## Technikalia
- Budowanie: `pdflatex` dwa razy (spis treści). W VS Code: LaTeX Workshop, kompilacja przy zapisie (`.vscode/settings.json`).
- Autor edytuje plik ręcznie (autozapis). Zmiany robimy punktowo, po dopasowaniu linii, bez nadpisywania całych bloków, które mógł zmienić.
- Znaki w generowanych skryptach: backslash i `\t` łatwo uszkodzić, używać surowych ciągów.
