PROJEKT: AUTOMATYZACJA TESTÓW APLIKACJI WEBOWEJ W PYTHONIE


Celem projektu jest przetestowanie obszaru udanego logowania istniejącego użytkownika oraz dodawania pierwszego adresu, 
z wyszczególnieniem walidacji poszczególnych pól formularza, dla strony https://automationpractice.techwithjatin.com/


Testy są napisane w: Python + Selenium.

Wzorzec projektowy: Page Object Model.

Technika testowania: Data Driven Testing (czytanie z pliku .csv)


---

Wymagania wstępne:
- [Python 3.12.3+](https://www.python.org/downloads/)
- [Selenium WebDriver](https://www.selenium.dev/downloads/)

Requirements:
```bash
pip install -r requirements.txt
```

Uruchomienie wszystkiech testów:
run_tests.py

W wyniku przeprowadzonych testów tworzony jest raport: HTMLTestRunner

---
Opis przypadków testowych:

101 - pozytywne logowanie istniejącego użytkownika.

201 - dodawanie pierwszego adresu bez wymaganego pola „City”.

202-204 - Dodawanie pierwszego adresu używając nieprawidłowych danych w polach „Home Phone” lub „Mobile Phone”.

205 - Dodawanie pierwszego adresu bez pola „State”.

206-208 - Dodawanie pierwszego adresu używając nieprawidłowych danych w polu „Zip/Postal Code”.

209-210 - Dodawanie pierwszego adresu bez podania prawidłowego pola „First Name”.

211-212 - Dodawanie pierwszego adresu bez podania prawidłowego pola „Last Name”.

213 - Dodawanie pierwszego adresu zakończone powodzeniem.
