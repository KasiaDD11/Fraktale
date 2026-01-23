# Projekt: Fraktale
### Demonstracja algorytmiki rekurencyjnej w języku Python

---

## 1. Płatek Śniegu Kocha (`fraktal.snieg.py`)
Klasyczny przykład fraktala o nieskończonej linii brzegowej.
* **Logika:** Każdy bok trójkąta równobocznego jest dzielony na 4 części w każdym kroku rekurencyjnym.
* **Zastosowanie:** Modelowanie płatków śniegu.
<img width="224" height="201" alt="Screenshot 2026-01-23 at 16 22 59" src="https://github.com/user-attachments/assets/23b236d2-3639-4b49-8454-71327716b772" />

## 2. Drzewo Fraktalne (`fraktal.drzewo.py`)
Bardziej organiczny model fraktala wykorzystujący rekurencję rozgałęzioną.
* **Logika:** Funkcja rysuje pień, a następnie wywołuje samą siebie dwukrotnie (dla lewej i prawej gałęzi) pod określonym kątem i ze zmniejszoną długością.
* **Zastosowanie:** Symulacja systemów wzrostu roślin.
<img width="395" height="306" alt="Screenshot 2026-01-23 at 16 21 58" src="https://github.com/user-attachments/assets/241afd7b-a442-4fd7-81be-5c2181e31f7a" />
Złożoność wizualna rośnie wykładniczo wraz ze wzrostem stopnia rekurencji.

