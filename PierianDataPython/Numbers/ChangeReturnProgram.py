#The user enters a cost and then the amount of money given. The program
# will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
cost_total = 132.2
bani_user = 200.0


bancnote_global = [500, 200, 100, 50, 10, 5, 1]
monede_global = [0.50, 0.10, 0.05, 0.01]


buzunar_final = {}

# Calculează restul
rest = bani_user - cost_total
if rest < 0:
    print("Prea puțini bani, womp womp")
elif rest == 0:
    print("Ai dat bani exacti!")
else:
    print(f"Restul de primit este: {round(rest, 2)} lei")

    for bancnota in bancnote_global:
        numar_bancnote = int(rest // bancnota)
        rest = round(rest - numar_bancnote * bancnota, 2)
        if numar_bancnote > 0:
            buzunar_final[bancnota] = numar_bancnote

    for moneda in monede_global:
        numar_monede = int(rest // moneda)
        rest = round(rest - numar_monede * moneda, 2)
        if numar_monede > 0:
            buzunar_final[moneda] = numar_monede

    print("Numărul de bancnote și monede necesare pentru rest:")
    for valoare, numar in buzunar_final.items():
        if valoare >= 1:
            print(f"{numar} bancnote de {int(valoare)} lei")
        else:
            print(f"{numar} monede de {int(valoare * 100)} bani")
