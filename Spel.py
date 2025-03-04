import math
import random
from random import randint

# Funktion för att hantera inmatning av heltal.
def input_value_int(fråga, feltext, min = 0, max = math.inf):
    while True:
        try:
            value = int(input(fråga))
            if min <= value <=max:
                return value
            else:
                print(feltext)
            
        except ValueError:
            print(feltext)

# Funktion för att hantera inmatning av strängar.
def input_valid_str(fråga, feltext, möjliga_svar):
    svar = input(fråga)
    while svar not in möjliga_svar:
        svar = input(f'{feltext}\n{fråga}')

    return svar

# Funktion för att utföra de matematiska beräkningarna. 
def korrekt_svar_beräkning(operand_1, operand_2, räknesätt):
    if räknesätt == "*":
        return operand_1*operand_2
    elif räknesätt == "//":
        return operand_1 // operand_2
    elif räknesätt == "%":
        return operand_1 % operand_2

# Funktion som frågar spelaren om hen vill spela igen.
def spela_igen(svar_spela_igen):
    if svar_spela_igen == "j":
        return True
    else: 
        return False

# Funktion som ser till att samma fråga inte frågas flera gånger än tillåtet. 
def slump_check(max_count, operand, ställda_frågor):
    while True:
        antal_frågade = ställda_frågor.count(operand)
        if antal_frågade < max_count:
            return operand
        operand = randint(0, 12)
        
    
    

 #Huvudkoden som kör spelet.
def main():
    spela = True

    # Variabeln inställningar ser till att de inledande frågorna inte upprepas om en spelare förlorar.
    inställningar = False

    while spela:
        while not inställningar:

            # Inledande frågor till spelaren som skickas till funktionen som kollar om svaren är giltiga.  
            fråga_antal_frågor = ("Välj antal frågor 12-39: ")
            totalt_antal_frågor = input_value_int(fråga_antal_frågor, "Ange ett giltigt svar!", 12, 39)
            
            
            
            fråga_räknesätt = "Vilket matematiskt räknesätt vill du spela med?: *, //, eller %? "
            svar_räknesätt = input_valid_str(fråga_räknesätt, "Ange giltigt svar!",["*", "//", "%"])

            # Anger variablerna operand_1 och operand_2 värden baserat på vad spelaren väljer för räknesätt.
            if svar_räknesätt == "*":
                fråga_tabell = "Vilken tabell vill du spela med? 2-12: "
                operand_1 = input_value_int(fråga_tabell, "Ange giltigt svar!", 2, 12 )
                
                
            else:
                fråga_divisor = "Vilken divisor vill du spela med? 2-5: "
                operand_2 = input_value_int(fråga_divisor, "Ange giltigt svar!", 2, 5)

            # Efter nedan rad körs inte längre denna kod om spelaren förlorar, utan endast om hen vinner och börjar om.
            inställningar = True
       
        # Räknar antal återstående frågor 
        återstående_frågor = totalt_antal_frågor

        # Skapar en lista och anger värden till max_count som används i funktionen som säkerställer att frågor inte                 upprepas för ofta.
        if totalt_antal_frågor <= 13:
            max_count = 1
        elif totalt_antal_frågor <= 26:
            max_count = 2
        else:
            max_count = 3
        ställda_frågor = []
        
        # Självaste frågesporten/zombie-letandet börjar här.
        while återstående_frågor > 0:

            # Genererar slumpmässiga operander för mattefrågorna och säkerställer att de inte upprepas för ofta.
            if svar_räknesätt == "*":
                operand_2 = slump_check(max_count, randint(0, 12), ställda_frågor)
                ställda_frågor.append(operand_2)
            else:
                operand_1 = slump_check(max_count, randint(0, 12), ställda_frågor)
                ställda_frågor.append(operand_1)
                
            # Ställer mattefrågor och beräknar svaret.
            fråga_matte = (f"Fråga {totalt_antal_frågor - återstående_frågor + 1}/{totalt_antal_frågor}: Vad är {operand_1} {svar_räknesätt} {operand_2}? Svar: ")
            len_fråga_matte = len(fråga_matte)
            line = "-" * len_fråga_matte
            print(line)
            korrekt_svar = korrekt_svar_beräkning(operand_1, operand_2, svar_räknesätt)
            svar_matte = input_value_int(fråga_matte, "Ange giltigt svar!", 0, math.inf)
            
            # Kollar så att svaret är korrekt, om det är korrekt går spelaren vidare till zombiefrågan.  
            if svar_matte == korrekt_svar:
                print("Korrekt svar!")
                
    
            else: 
                print(f"Felaktigt svar! Det rätta svaret är: {korrekt_svar}") 
                break
            # Här är zombie-frågorna, den sista utelämnas. 
            if återstående_frågor > 1:
                zombie = randint(1, återstående_frågor)
                fråga_zombie = (
                    f"Bakom vilken dörr finns det en zombie? 1-{återstående_frågor}: ")
                svar_zombie = input_value_int(fråga_zombie, "Ange ett giltigt svar!", 1, återstående_frågor)
                    
                if svar_zombie == zombie:
                    print("Det fanns en zombie bakom dörren, du förlorade! 🧟")
                    break                
                else:
                    print(f"Korrekt! Zombien var bakom dörr {zombie}.\n")
                    återstående_frågor -= 1
            else:
                
                återstående_frågor -= 1
        # Här vinner spelaren om hen har svaret rätt på alla frågor. 
        if återstående_frågor == 0:
            print("Grattis, du svarade rätt på alla frågor, undvek zombiesarna och har därmed vunnit spelet!")
            fråga_spela_igen = ("Vill du spela igen? j/n: ")
            svar_spela_igen = input_valid_str(fråga_spela_igen, "Ange giltigt svar!", (["j", "n"]))

            if spela_igen(svar_spela_igen):
                # Raden nedan säkerställer att de ursprungliga frågorna gällande inställningar upprepas. 
                inställningar = False
            else:
                print("Tack! Hejdå!")
                break
        # Om spelaren förlorar kan hen spela igen.
        else: 
            fråga_spela_igen = ("Vill du spela igen? j/n: ")
            svar_spela_igen = input_valid_str(fråga_spela_igen, "Ange giltigt svar!", (["j", "n"]))
            if spela_igen(svar_spela_igen):
                print(f"Spelet börjar nu om på fråga {totalt_antal_frågor}.")
                continue
            else:
                print("Tack för att du spelade!")
                break
                
    


        
main()