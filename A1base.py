from tkinter import *
#caracteristicas: 
#- Perda de memoria 
#- Mudança de humor/personalidade 
#- Dificuldade em tarefas básicas
#- AVC/Derrame
#- Doenças Crônicas
#- Histórico 
#- Saúde e rotina
#- Idade

#comparativo de chances para avaliação
def sint_chance(chance):
    if chance <= 3:
        print("\nBaixa chance de Alzheimer, Monitoramento é recomendado.\n")
    elif 4 <= chance <= 5:
        print("\nModerada chance de Alzheimer, Consulta com especialista para melhor avaliação é recomendada.\n")
    else: 
        print("\nAlta chance de Alzheimer, Consulta com especialista para melhor avaliação/tratamento é altamente recomendada.\n")
    return chance

#- Perda de memória 
def sint_memloss(memloss, chance):
    if memloss == "sim" or memloss == "s":
        chance += 1
    return chance

#- Mudança de humor/personalidade 
def sint_mood(mood, chance):
    if mood == "sim" or mood == "s":
        chance += 1
    return chance

#- Dificuldade em tarefas básicas
def sint_tasks(tasks, chance):
    if tasks == "sim" or tasks == "s":
        chance += 1
    return chance

#- AVC/Derrame
def sint_AVC(AVC, chance): 
    if AVC == "sim" or AVC == "s":
        #AVC/derrame aumentam em 80% o desenvolvimento de demências
        chance += 2
    return chance

#- Doenças crônicas
def sint_illness(illness, chance): 
    if illness == "sim" or illness == "s":
        chance += 1
    return chance

#- Histórico familiar
def sint_famhist(famhist, chance): 
    if famhist == "sim" or famhist == "s":
        #histórico familiar de alzheimer aumenta as chances
        chance += 2
    return chance

#- Saúde e rotina
def sint_health(health, chance):
    if health == "nao" or health == "não" or health == "n":
        chance += 1
    return chance

#- Idade
def sint_age(age, chance):
    if age >= 65:
        chance += 1
    return chance

def main():
    chance = 0
    # Pergunta para cada característica
    print("\nSintomas: \n")
    memloss = input("A pessoa apresenta perda de memória? (sim/não): ").lower()
    mood = input("A pessoa apresenta mudanças de humor ou personalidade? (sim/não): ").lower()
    tasks = input("A pessoa tem dificuldade em realizar tarefas básicas? (sim/não): ").lower()
    
    print("\nVida/Saúde: \n")
    AVC = input("A pessoa já teve caso de AVC/Derrame? (sim/não): ").lower()
    illness = input("A pessoa possui algum tipo de doença crônica (diabetes, hipertensão, colesterol elevado)? (sim/não): ").lower()
    famhist = input("Há histórico de Alzheimer em parentes próximos da pessoa? (sim/não): ").lower()
    health = input("A pessoa mantém hábitos saudáveis? (sim/não): ").lower()
    age = int(input("Informe a idade da pessoa: \n"))
    
    # Atualiza chance com cada função de sintoma
    chance = sint_memloss(memloss, chance)
    chance = sint_mood(mood, chance)
    chance = sint_tasks(tasks, chance)
    chance = sint_AVC(AVC, chance)
    chance = sint_illness(illness, chance)
    chance = sint_famhist(famhist, chance)
    chance = sint_health(health, chance)
    chance = sint_age(age, chance)
    
    # Imprime os resultados de acordo com o Comparativo
    print("\nChance =", sint_chance(chance))

main()
