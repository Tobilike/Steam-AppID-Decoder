# Steam AppID Decoder 🎮

Ein kleines, schnelles Python-Skript, um das Krypto-Zahlen-Chaos im `steamapps`-Ordner zu entschlüsseln. Es liest die Steam-Manifestdateien aus und ordnet die numerischen Ordner-IDs (AppIDs) automatisch den echten Spielnamen zu.

## 📋 Das Problem
Steam speichert Spieldaten, Shader-Caches (`shadercache`), Kompatibilitätsdaten (`compatdata`) oder Workshop-Mods oft ausschließlich unter der reinen Steam-Identifikationsnummer (z. B. `620`). Ohne Onlinesuche ist es schwer zu erkennen, welcher Ordner zu welchem Spiel gehört. 

Dieses Skript scannt den Ordner und erstellt im Handumdrehen ein übersichtliches, lokal ausgelesenes Inhaltsverzeichnis.

## ✨ Features
- 🚀 **Keine externen Abhängigkeiten:** Nutzt ausschließlich Module der Python-Standardbibliothek (`pathlib`, `argparse`, `os`). Keine Installation via `pip` nötig!
- 🧹 **Saubere Formatierung:** Sorgt für perfekte Lesbarkeit.
- 🛠️ **Maximale Flexibilität:** Kann entweder direkt im Zielordner ausgeführt oder von überall aus mit einem Pfad-Argument gefüttert werden.
- 🛡️ **Fehlertolerant:** Beschädigte oder leere `.acf`-Dateien werden automatisch erkannt und sicher übersprungen, ohne dass das Skript abstürzt.

## 🚀 Verwendung

### Voraussetzungen
* Python 3.x muss auf deinem System installiert sein.

### Installation & Start
1. Lade die Skript-Datei herunter (z. B. als `steam_decoder.py`).
2. Verschiebe die Datei in deinen Steam-Ordner (idealerweise direkt in den Ordner `steamapps`).
3. Öffne ein Terminal in diesem Ordner und starte das Skript:

```bash
python steam_decoder.py
```

### Alternativer Pfad
Falls du das Skript von einem anderen Ort aus ausführen möchtest, kannst du den Pfad zum steamapps-Ordner einfach als Argument hinten anhängen:
```bash
python steam_decoder.py /pfad/zu/deinem/steam/steamapps
```

## 📊 Beispiel-Ausgabe

```
--- DEINE STEAM SPIELE-LISTE ---
ORDNER-NUMMER   |   SPIELNAME
--------------------------------------------------
        400       ->    Portal
        620       ->    Portal 2
        730       ->    Counter-Strike 2
        377160    ->    Fallout 4
--------------------------------------------------
Erfolgreich 4 Spiele zugeordnet.
```


### 📜 Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Das bedeutet, du darfst damit machen, was du willst – teilen, verändern und verbessern!
