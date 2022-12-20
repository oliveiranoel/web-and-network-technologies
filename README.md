# Web- und Netzwerktechnologie - Temperaturmessgerät
### Florian Fa, Julius Oswald und Noel Oliveira

Am 31.08.2022 haben sich die Bundesräte entschieden, eine Energiesparkampagne zu lancieren.

Da wir bereits im Winter angekommen und die Tage somit grundsätzlich kälter sind, wird uns klar, wie stark wir auf Heizungen angewiesen sind.
Die aktuelle Energiekrise bekräftigt dieses Gefühl. Das Team hat sich daher entschieden, mit Hilfe des erlenten Wissens im Modul Web- und Netzwerktechnologie
sowie der micro:bit-Software ein Programm zur Temperaturüberwachung zu erstellen.

Mit Hilfe dieses Programms ist es möglich, die im Raum aktuelle Temperatur zu messen und anzuzeigen. Durch Drücken des A-Knopfs wird die aktuelle Temperatur gemessen.
Werden in einem Raum an verschiedenen Orten unterschiedliche Temperaturen gemessen, wird automatisch der Durchschnitt der durchgeführten Messungen berechnet.
Durch Drücken des B-Knopfs wird ein neuer Raum "geöffnet" und gleichzeitig der Durchschnitt für diesen kalkuliert. Durch schütteln des micro:bits werden die Räume gelöscht und eine neue Messung kann gestartet werden.

## Vorbereitung
### Python
Um dieses Programm laufen zu lassen, wird **python3** benötigt.

### micro:bit
Laden sie die client.py software auf den eingesteckten micro:bit hoch. Dies können sie auf [dieser Website](https://python.microbit.org/v/3) durchführen. Benutzer sie dafür den Chrome browser, da Safari erfahrungsgemäss Schwierigkeiten bereitet.

### Serieller Port (Windows)
Wenn sie auf dem Windows PC sind, dann gemäss [dieser Beschreibung](https://fhnw365.sharepoint.com/teams/webnt122_M365/Freigegebene%20Dokumente/Forms/AllItems.aspx?id=%2Fteams%2Fwebnt122%5FM365%2FFreigegebene%20Dokumente%2Fhs22%2F03%2FAB3%2E1%2Epdf&parent=%2Fteams%2Fwebnt122%5FM365%2FFreigegebene%20Dokumente%2Fhs22%2F03) den USB-Serial-Port auslesen. Bei macos/linux ist dies nicht nötig, der Port wird automatisch ausgelesen. Stellen Sie sicher, dass nur ein USB Port mit dem micro:bit belegt ist. 

### Librarys
Die Library welche benötigt werden, sind im requirements.txt enthalten. Diese können mit folgendem Befehl installiert werden:`pip3 install -r requirements.txt`

### Argumente
Sie können nachfolgende Argumente der gateway.py Applikation übergeben:

#### --server
Die Adresse des Server, auf welchem die webserver.py Applikation läuft.

#### --serial
Die Serielle Schnittstelle des USB-Ports, wo der micro:bit eingesteckt ist. Nur bei Windows notwendig!