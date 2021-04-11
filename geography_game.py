print("Welcome to this geography game! Please read the rules.")
print()
print("RULES:")
print("In this game, you will recieve a question.")
print("All of the answers will be one word or a number")
print("If you get something wrong, YOU'RE DONE")
print("After you answer, press enter")
print("Good Luck!")
print()

print("To confirm that you can play the game...")

confo = input("Answer this question: What is 1+1? ")

if confo == str(2):
  print("Congrats! You are ready for your first question:")
  ecua = input("What is the largest city in Ecuador? ").lower()

  if ecua == "guayaquil":
    print("Correct! You may pass. Your next question is below.")
    least = input("What is the least populated state in the United States? ").lower()

    if least == "california":
      print("Oof, that's the most populated state, you're wrong")
    
    if least == "wyoming":
      print("Congrats! You're correct. Your next question is below.")

      spirit = input("What is the largest religion in the world? ").lower()

      if spirit == "christianity":
        print("Correct! Your next question is below")

        brus = input("What is the main language spoken in Brazil? ").lower()

        if brus == "portuguese":
          print("Congrats! You're correct. Your next question is below")

          cana = input("What is the capital of Canada? ").lower()

          if cana == "ottawa":
            print("You're correct! The next question is below.")

            za = input("What country is landlocked in South Africa? ").lower()

            if za == "lesotho":
              print("Yep, that's correct. Your next question is below")

              zeal = input("What is the largest city on New Zealand's South Island? ")

              if zeal == "christchurch":
                print("Ding ding ding! Good job")
                print("Your next question is below:")

                pop = input("What is the most populated country in the world? ")
              
              if zeal == "auckland":
                print("Ahh, that's the largest city on the North Island. Sorry")
              
              else:
                print("You're wrong!")
            
            else:
              print("Rip, you're done.")
          
          else:
            print("You're wrong. To restart, press the run button.")
        
        if brus == "spanish":
          print("Good guess, but you're wrong.")
        
        else:
          print("You're wrong!! Press the run button to restart.")
      
      if spirit == "islam":
        print("Well, this could be true in the future, but not yet.")

      else:
        print("You are wrong")
    
    else:
      print("Welp, you're wrong.")
  
  if ecua == "quito":
    print("Quito may be the capital, but not the largest city.")
  
  else:
    print("Rip... you are wrong")


else:
  print("Sorry, but you cannot move on to question one")
  print("Go study some basic math.")
