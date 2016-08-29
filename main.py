import os
import shutil
import time
#----------
print("="*26)
print("Dev.Corp приветствует вас!")
print("="*26)
print("    Автор:vk.com/mcg76")
#----------
def exit():
 print("《《Выход на рабочий стол...》》")
 time.sleep(2)
def drs():
 while True:
  print("Выбран ярлык 《установка дериктории》")
  folder = input("Укажите путь в формате bin/system: ")
  print("☆ Путь сохранен")
  exit()
  break
##Ядро##
comdb = {"#3": drs,"3": drs}
##Не трогать##
while True:
 folder = os.system("find / -iname PocketMine-MP.phar")
 if folder=="not found":
  print("")
 else:
  print("Не удалось найти ядро,поиск папки src..")
  folder = os.system("find / -iname start.sh")
  if folder=="Not Found":
   print("Ок файл найден")
  else:
   print("Не удалось найти папку вашего сервера,вы можете самостоятельно выбрать дерикторию")
 print(folder)
 break
 #folder = input("Доброго времени суток,укажите путь к файлу вашего сервера: ")
while True:
 command = str(input("Выберите цифру действия:\n#1 Быстрая-очистка папки players\n#2 Быстрая очистка папки на выбор\n#3 Выбрать папку сервера\n#4 Закрыть программу\n Команда: "))
###################
 if command in comdb:
  comdb[command]()
 else:
  print("Нет такого ярлыка с номером: ",command,"\n》》Выход на рабочий стол...《《")
  time.sleep(2)
 continue
