# Projekt gry "Snake"
Jakub Siwy

## 1. Opis programu

Aplikacja jest implementacją popularnej gry w węża (ang. Snake) przeznaczona do rozgrywki typu single-player.

Gra oferuje kilka różnych map z przeszkodami oraz najbardziej klasyczną bez ograniczeń. Zadaniem użytkownika jest tak kierować działaniami węża aby ten zjadając jabłka na swojej drodze urósł do jak największych rozmiarów. Dodatkowo co 3 minuty użytkownik może nakarmić swojego przyjaciela złotą wersją jabłka przez co otrzyma on dwukrotny bonus do zdobywanych punktów.

Gra oferuje również możliwość zapauzowania rozgrywki w trakcie, bogaty soundtrack oraz efekty zarówno wizualne jak i dźwiękowe.

## 2. Sterowanie

Cały interfejs aplikacji przysowany jest do sterowania wyłącznie za pomocą klawiatury:

W menu:

* Strzałka w górę - zmiana opcji o pozycję w górę
* Strzałka w dół - zmiana opcji o pozycję w dół

W menu wyboru planszy:

* Strzałka w prawo - wybór następnej mapy
* Strzałka w lewo - wybór poprzedniej mapy
* Esc - powrót do menu głównego
* Enter - zatwierdzenie wyboru i rozpoczęcie rozgrywki

Podczas rogrywki:

* Strzałka w prawo - zmiana kierunku poruszania w prawo
* Strzałka w lewo - zmiana kierunku poruszania w lewo
* Strzałka w dół - zmiana kierunku poruszania w dół
* Strzałka w górę - zmiana kierunku poruszania w górę
* Esc - uruchomienie menu pauzy

UWAGA: Nie ma możliwości zmiany raz ustalonego kierunku do momentu poruszenia się węża. Dodatkowo zablokowana jest możliwość obrotu głowy węża o 180 stopni.

Po rozgrywce - sterowanie takie jak w menu głównym

## 3. Sposób uruchomienia

Program uruchamiany z linii komend w folderze z plikiem Snake.py za pomocą komendy

`python3 Snake.py`

dalsze kroki wykonywać zgodnie z zasadami sterowania określonymi powyżej.

## 4. Assety wykorzystane w programie:

* https://opengameart.org/content/snake-tilemap - ciało węża (kolory zmienione)
* https://tallbeard.itch.io/music-loop-bundle - muzyka w tle (gra, menu śmierci, menu pauzy, wzmocnienia)
* https://opengameart.org/content/technological-menace - muzyka w tle (menu główne)
* https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZzn6Eo_GvFYloO5bxb3vmCSI9KlMMtH-rKrZODh8_qnO9NR7j5Y7lWxldqE07ZnkNaN0&usqp=CAU - obrazek śpiącego węża (kolory zmienione)
* https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk9eaN8hbtBWYJV3Bbjhxc3vPy0HQLNlgrkBzCYP5oVi_MkTVlWMUBdg4yFTJ50LQ8Bts&usqp=CAU - obrazek przygnębionego węża (kolory zmienione)
* https://static7.depositphotos.com/1036149/677/i/450/depositphotos_6771731-stock-photo-fun-snake-with-glasses.jpg - obrazek węża w okularach przeciwsłonecznych (kolory zmienione)

UWAGA: Wykorzystane obrazy oraz muzyka należą do ich prawnych autorów, a w aplikacji zostały wykorzystane wyłącznie do celów demonstracyjnych. Aplikacja nie została stworzona do celów komercyjnych.

## 5. Wymagania wstępne:

Aplikacja stworzona i przetestowana za pomocą następujących programów i bibliotek:

Python - wersja 3.8.10
Biblioteka pygame - wersja 2.1.2
Biblioteka SDL - wersja 2.0.16

Autor nie gwarantuje działania tego programu na innych wersjach niż wymienione wyżej, co nie oznacza braku takiej możliwości.