import datetime

aktualnie=datetime.datetime.now()
doKolokwium=datetime.datetime(2024, 2, 12)
ostatnieZajecia=datetime.datetime(2024, 1, 15)
print("Od ostatnich zajęć upłynęło: ", (aktualnie-ostatnieZajecia).days, "dni")
print("Do kolokwium zostało: ", (doKolokwium-aktualnie).days, "dni")
