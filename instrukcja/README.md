# Instrukcja laboratoryjna — XPlanar / TwinCAT 3

Szkielet dokumentu LaTeX dla instrukcji laboratoryjnej. Zawiera tylko
strukturę (nagłówki sekcji + placeholdery) — treść merytoryczną każdego
kroku uzupełnia prowadzący na podstawie oficjalnych manuali Beckhoff
z folderu [`../dokumentacja`](../dokumentacja).

## Struktura

- `main.tex` — główny plik dokumentu, 6 sekcji (jedna na krok laboratorium):
  1. Inicjalizacja aplikacji — projekt i biblioteki
  2. Inicjalizacja moverów — free move, obroty
  3. Inicjalizacja ścieżek i stacji
  4. Ruch po ścieżkach — tłumaczenie i konfiguracja parametrów
  5. Przechyły
  6. Oś Z (odwołuje się do mechanizmów z kroków 2 i 4 — patrz notatka w sekcji)
- `zdjęcia/` — folder na zrzuty ekranu.

## Jak dodać zrzut ekranu

1. Wgraj plik obrazu (PNG/JPG) do folderu `zdjęcia/`.
2. W `main.tex` w odpowiedniej sekcji jest już wywołanie makra, np.:

   ```latex
   \zrzutEkranu{krok1-nowy-projekt.png}{Podpis pod zrzutem}
   ```

   Wystarczy, że plik w `zdjęcia/` nazywa się dokładnie tak samo jak w
   wywołaniu makra (`krok1-nowy-projekt.png`) — obrazek pojawi się w
   dokumencie automatycznie przy następnej kompilacji. Dopóki pliku nie ma,
   w tym miejscu wyświetla się szara ramka-placeholder z nazwą brakującego
   pliku, więc dokument kompiluje się poprawnie od razu, bez żadnych zdjęć.
3. Aby dodać kolejny zrzut w danej sekcji lub zmienić nazwę pliku — po
   prostu dodaj/zmień wywołanie `\zrzutEkranu{...}{...}` w `main.tex`.
4. W nazwach plików używaj myślników (`-`), nie podkreśleń (`_`) — podkreślenie
   jest w LaTeX-u znakiem specjalnym i wymagałoby escapowania (`\_`).

## Kompilacja

Standardowo, dowolnym silnikiem obsługującym pakiet `babel` z opcją
`polish` (pdfLaTeX/XeLaTeX/LuaLaTeX), np.:

```bash
pdflatex main.tex
```

(Dwa przebiegi, jeśli potrzebny aktualny spis treści.)

## Styl pisania
Zasady stylu instrukcji: [STYL.md](STYL.md).
