import random

print("""            ,___________________________________________/7_ 
           |-_______------. `\                             |
       _,/ | _______)     |___\____________________________|
  .__/`((  | _______      | (/))_______________=.
     `~) \ | _______)     |   /----------------_/
       `__y|______________|  /
       / ________ __________/
      / /#####\(  \  /     ))
     / /#######|\  \(     //
    / /########|.\______ad/`
   / /###(\)###||`------``
  / /##########||
 / /###########||
( (############||
 \ \####(/)####))
  \ \#########//
   \ \#######//
    `---|_|--`
       ((_))
        `-`""")
print("What are you dueling for? Welcome to the Roulette Dueler. In few minutes, one of you will not be here, RIP.")
duel = input("Let the duel begin? Y/n ").lower()


bullets = ["Empty","Empty","Empty","Empty","Empty","Kaboom"]

life = True

if duel == "y":
    life
    print("Wheeling")
else:
    print("Life is too short and mortal.")
    life = False


while life:

    first_fire = input("Are you ready? -y ").lower()
    if first_fire == "y":
        fire = random.choice(bullets)
        print(fire)
        bullets.remove(fire)
        if fire == "Kaboom":
            life = False

    else:
        print("Life is too short and mortal.")
        break




