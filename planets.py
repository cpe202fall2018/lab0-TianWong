def weight_on_planets():
   # write your code here
   weight = float(input("What do you weigh on earth? "))

   print("On Mars you would weigh " + str(weight * 0.38) + " pounds.\nOn Jupiter you would weigh " + str(weight * 2.34) + " pounds.")

if __name__ == '__main__':
   weight_on_planets()
