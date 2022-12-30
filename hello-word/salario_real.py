wage = int(input('wage? '))
tax = float (input ('Tax in % (ex:27.5)?'))
print ("Real value:{0}". format (wage-(tax * 0.01))) 
if tax >= 10. and tax <= 27.:  
   print("baixo")
elif tax > 27. and tax <= 27.:
   print ("Medio")
elif tax > 27. and tax < 100.:
   print("Alto")
else :
   print("Imposto invalido")         