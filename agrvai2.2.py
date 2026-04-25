import random
import time

emojis = ["🐷", "🐷", "🐭", "🐅", "7️⃣", "🐯"]

valores = {
    "🐷": 2,
    "🐭": 3,
    "🐅": 4,
    "7️⃣": 6,
    "🐯": 10
}

def girar_slot(emojis):
    s1 = s2 = s3 = "" 
    
    for i in range(15):
        if i <10:
            s1 = random.choice(emojis)
        if i <12:
            s2 = random.choice(emojis)
        if i <15:
            s3 = random.choice(emojis)
        
        print(f"\r | {s1} | {s2} | {s3} | ", end="")
        time.sleep(0.15)
    
    return s1, s2, s3

print("=== 🎰 CASSINO DO TIGRIN 🎰 ===")

saldo = int(input("Quanto de saldo deseja depositar na plataforma?: R$"))

while saldo > 0:
    print(f"\nSeu saldo é: R${saldo}")
    aposta = int(input("Digite o valor da aposta: R$"))

    if aposta > saldo:
        print("SALDO INSUFICIENTE")
        continue

    print("Girando....", end="")
    time.sleep(1)

    slot1, slot2, slot3 = girar_slot(emojis)
    print("\n Resultado final!: ")

    if slot1 == slot2 == slot3:
        premio = valores[slot1] * aposta
        print(f"\n🎰 JACKPOT! 🎰\nVocê ganhou R${premio}")
        saldo += premio

    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        if slot1 == slot2 or slot1 == slot3:
            emoji_ganhos = slot1
        else:
            emoji_ganhos = slot2


        premio = (valores[emoji_ganhos] * aposta) // 2
        print(f"\n🎰 PAR! 🎰\nVocê ganhou R${premio}")
        saldo += premio

    else:
        print("😪 Poxa não foi dessa vez")
        saldo -= aposta

    continuar = input("deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

print(f"\nVocê saiu com R${saldo}")
print("Obrigado por jogar!")
     


                




