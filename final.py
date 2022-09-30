from pickle import TRUE

def practica1():
  print("Introduce valor")
  X = int(input())
  lst = list(range(1, X+1))
  print(lst)
  def f(n):
    return all([not n%x==0 for x in range (2,n)])
  for i in range(1,X+1):
    i,f(i)
    primos = []
    for lNum in range(1, X+1):
        if (f(lNum)):
          primos.append(lNum)

  print(primos)
  
