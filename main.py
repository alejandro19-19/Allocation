"""
Elaborado por: Alejandro Escobar Tafurt
Codigo: 201941378
Sistemas operativos
Practice No. 4: Allocation

Nota: El codigo recibe un archivo de texto con el formato establecido en la practica y retorna el resultado esperado en la consola
"""
#lectura del archivo
file = open("input.txt","r")
arrayInput = file.readlines()
file.close()

processes = []
memory = []
method = int(arrayInput[0])
nPartitions = int(arrayInput[1])
aux = 2

#eliminar el salto de linea
characters = "\n"
for z in range(len(arrayInput)):
  for x in range(len(characters)):
      arrayInput[z] = arrayInput[z].replace(characters[x],"")

#asignacion memoria
for i in range(nPartitions):
  memory.append(int(arrayInput[aux]))
  aux = aux + 1

#procesos
nProcesses = int(arrayInput[aux])
aux = aux+1
for k in range(nProcesses):
  processes.append(int(arrayInput[aux]))
  aux = aux + 1
  
#funciones auxiliares para retornar el resultado obtenido con el formato esperado
def printAnswer(output):
  for i in range(len(output)):
    print(output[i])

def answer(result,memory,processes):
  output = []
  for i in range(len(result)):
    aux = result[i]
    if aux[1] == None:
      output.append("P"+ str(aux[0])+" --> "+ str(processes[aux[0]])+ " Not allocated")
    else:
      output.append("P"+ str(aux[0])+" --> "+ str(processes[aux[0]])+ " is put in "+ str(aux[2])+", "+ str(aux[1]+1)+" partition.")
  
  return output
    
#funcion principal 
def allocation(method, nPartitions, memory, nProcesses, processes):
  if method == 1:
    result = firstFit(nPartitions, memory, nProcesses, processes)
    output = answer(result,memory,processes)
    printAnswer(output)
  elif method == 2:
    result = bestFit(nPartitions, memory, nProcesses, processes)
    output = answer(result,memory,processes)
    printAnswer(output)
    
  elif method == 3:
    result = worstFit(nPartitions, memory, nProcesses, processes)
    output = answer(result,memory,processes)
    printAnswer(output)
    
  else:
    print("ingrese un metodo válido (1=FirstFit, 2=BestFit, 3=WorstFit)")
    
def firstFit(nPartitions, memory, nProcesses, processes):
  result = []
  
  for i in range(nProcesses):
    for j in range(len(memory)):
      if processes[i] <= memory[j]:
        memoryCapacity = memory[j]
        memory[j] = memory[j] - processes[i]
        result.append([i,j,memoryCapacity])
        break
      elif j == len(memory)-1:
        result.append([i, None])
  return result

def bestFit(nPartitions, memory, nProcesses, processes):
  result = []
  for i in range(nProcesses):
    for j in range(len(memory)):
      auxBestFit = bestWorstFitArray(memory,processes[i])
      if processes[i] <= memory[j] and min(auxBestFit) == memory[j]:
        memoryCapacity = memory[j]
        memory[j] = memory[j] - processes[i]
        result.append([i,j,memoryCapacity])
        break
      elif j == len(memory)-1:
        result.append([i, None])
  return result

def worstFit(nPartitions, memory, nProcesses, processes):
  result = []
  for i in range(nProcesses):
    for j in range(len(memory)):
      auxBestFit = bestWorstFitArray(memory,processes[i])
      if processes[i] <= memory[j] and max(auxBestFit) == memory[j]:
        memoryCapacity = memory[j]
        memory[j] = memory[j] - processes[i]
        result.append([i,j,memoryCapacity])
        break
      elif j == len(memory)-1:
        result.append([i, None])
  return result
  
#funcion auxiliar para la implementacion del worst y best fit
def bestWorstFitArray(memory,process):
  array = []
  for i in range(len(memory)):
    if memory[i]>= process:
      array.append(memory[i])
  return array
#funcion auxiliar para retornar el resultado obtenido con el formato esperado

#invocacion de la funcion principal
allocation(method, nPartitions, memory, nProcesses, processes)  

"""
ejemplo 1

1
5
100
500
200
300
600
4
212
417
112
426

ejemplo 2

1
5
100
500
300
400
800
4
500
300
400
800

"""
