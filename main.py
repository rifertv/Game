from random import randint

hau = 1
grow = 1
grows =[]

while hau <=5:
  hau += 1
  ran = randint(1,6)
  man = int(input(' Введите число, от 1 до 5: '))
  num = abs (man - ran)
  


  if num == 0:
    grow = 6
    grows.append(grow)
  elif num == 1:
    grow = 5
    grows.append(grow)
  elif num == 2:
    grow = 4
    grows.append(grow)
  elif num == 3:
    grow = 3  
    grows.append(grow)
  elif num == 4:
    grow = 2
    grows.append(grow)
  elif num == 2:
    grow = 4
    grows.append(grow)
  elif num == 5:
    grow = 1
    grows.append(grow)
 
  print("Кол-во очков: ",grow)

  ball = sum(grows)
   

print ("Ваш результат ",ball," очков")
if ball <= 25:
  print(" U lose(")
else:
  print(" U Win)")