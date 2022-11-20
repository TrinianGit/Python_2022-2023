class Bug:
    """Klasa Bug reprezentująca robaki i zliczająca ich obecną ilość"""
    licznik = 0
    def __init__(self):
        Bug.licznik += 1
        self.licznik = Bug.licznik
    def __str__(self):
        return f"Bug.licznik = {Bug.licznik}, self.licznik = {self.licznik}"
    def __del__(self):
        Bug.licznik -= 1
        print('Koniec', 'Bug.licznik = ', Bug.licznik, 'self.licznik = ', self.licznik)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])