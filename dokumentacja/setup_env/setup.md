## Instrukcja Konfiguracji Środowiska TwinCAT i XPlanar

### Etap 1: Instalacja Wymaganego Oprogramowania
1. **Zainstaluj Visual Studio 2017 Community**: Pobierz instalator z [tego linku](https://aka.ms/vs/15/release/vs_community.exe).
2. **Zainstaluj TwinCAT Package Manager**: Pobierz instalator ze [strony Beckhoff](https://www.beckhoff.com/pl-pl/download/725320261) i przeklikaj standardowy proces instalacji.

---

### Etap 2: Konfiguracja Pakietów (Obejście interfejsu)
3. **Sprawdź dostępność narzędzia**: Uruchom Wiersz polecenia (CMD) i upewnij się, że komenda `tcpkg` jest poprawnie rozpoznawana przez system.
4. **Zainstaluj pakiety za pomocą skryptu**: Przejdź do folderu `setup env`. Uruchom znajdujący się tam skrypt Python. Skrypt automatycznie odczyta plik `CurrentConfig.config` i zainstaluje biblioteki (jest to obejście problemu zawieszającego się Load Config w interfejsie). 
    * *Uwaga: W trakcie pracy skryptu może być konieczne ręczne zatwierdzanie instalacji niektórych paczek klawiszem `Y` w konsoli.*
5. **Zweryfikuj integrację z VS**: Po uruchomieniu projektu z pliku `.sln`, TwinCAT Shell powinien być już automatycznie połączony z Visual Studio 2017. Jeśli tak nie jest, należy ręcznie doinstalować pakiet `TwinCAT.Standard.XAE`.
6. **Zainstaluj brakującą bibliotekę**: Z folderu `setup_env` zainstaluj ręcznie bibliotekę `Tc3_XPlanarStandard` (nie jest ona dostępna w globalnych repozytoriach w internecie). Instalacja polega na otwarciu referencji w projekcie (`PLC` -> `[Nazwa projektu]` -> `[Nazwa projektu]` -> `References`) i sprawdzeniu w szczegółach (`Details`), gdzie zapisywane są biblioteki. Zazwyczaj jest to ścieżka `C:\ProgramData\Beckhoff\TwinCAT\PlcEngineering\Managed Libraries`. Skopiuj bibliotekę do tego folderu, a następnie zresetuj (przeładuj) system.

---

### Etap 3: Ustawienia Sieciowe PC (Lokalne)
7. **Skonfiguruj statyczny adres IP**: W ustawieniach karty sieciowej komputera (Ethernet) przypisz statyczne wartości:
    * Adres IP: `192.168.2.x` (gdzie `x` to unikalna końcówka Twojego komputera)
    * Brama domyślna (Default Gateway): `192.168.2.1`
8. **Skonfiguruj AMS NetID**: W Zasobniku systemowym (obszar ukrytych ikon) kliknij prawym przyciskiem myszy na ikonę TwinCAT -> **Router** -> **Change AMS NetID**. Zapisz zmiany.

---

### Etap 4: Konfiguracja Sterownika IPC (Zdalna)
9. **Połącz się przez Pulpit Zdalny (RDP)** ze sterownikiem Beckhoff (stan na **09.07.2026**):
    * IP: `192.168.2.44`
    * Login: `Administrator`
    * Hasło: `1`
10. **Zarejestruj swój komputer**: Na pulpicie sterownika uruchom **Beckhoff Device Manager** -> **TwinCAT** -> **Connectivity**. Dodaj do listy swój komputer. **Ważne:** Adres IP oraz AMS NetID muszą być dokładnie takie same, jak te ustawione w Krokach 7 i 8 na Twoim komputerze.

---

### Etap 5: Zestawienie Połączenia (Tworzenie Route'a)
11. **Dodaj Target w TwinCAT**:
    * Na swoim komputerze, w otwartym projekcie na górnym pasku rozwiń listę urządzeń (zamiast `Local` wybierz **Choose Target System**).
    * Kliknij **Search Ethernet**, a następnie **Broadcast Search**.
    * Znajdź i zaznacz urządzenie XPlanar na liście, po czym kliknij **Add Route**.
    * Upewnij się, że opcja **Secure ADS** jest zaznaczona (**ON**).
    * W oknie weryfikacji podaj poświadczenia zdalne urządzenia docelowego (Login: `Administrator`, Hasło: `1`).