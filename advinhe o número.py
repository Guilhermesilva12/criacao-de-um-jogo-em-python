import time
attempt = 1
secretNumber = 1578




print("Jogo Advinhe o número\n")
time.sleep(1)
print("Você terá 7 chances\n")
time.sleep(1)
print("O número secreto está entre 1000 e 2000\n")


while (attempt <= 7 or number == secretNumber):
        try:
                number = int(input("Chance [{}]\nVocê nunca advinhará o número secreto de 4 dígitos: ".format(attempt)))
        


                if (number == secretNumber and attempt == 1):
                    print ("Tá de hack?, acertou de primeira!")
                    time.sleep(2)
                    print ("Até mais!")
                    time.sleep(1)
                    print("Hacker")
                    break

                elif (number == secretNumber and attempt == 2):
                        print("Acertou, mas MEIO fraquinho ainda né!?")
                        time.sleep(2)
                        print("Meio hacker ainda eu diria")
                        time.sleep(1)
                        print("Até mais!")
                        break

                elif (number == secretNumber and attempt >= 3 and attempt < 5):
                        print ("Jogou honestamente!")
                        time.sleep(1)
                        print("Mas também, pelo tanto de chance que teve kkkkk")
                        time.sleep(2)
                        print("Até mais!")
                        break

                elif (number == secretNumber and attempt > 5 and attempt <=7):
                        print ("PELO AMOR DE DEUS!")
                        time.sleep(1)
                        print("Vai se benzer, tomar um banho de sal grosso kkkkk")
                        time.sleep(1)
                        print("Acertou\nAté mais")
                        break  

                elif (number < secretNumber):
                    print ("O número informado é menor do que o número secreto\n")

            
                elif (number > secretNumber):            
                    print ("O número informado é maior do que o número secreto\n")

                attempt += 1

        except:
                print("Opção Inválida\n")

           






        
