import os, time 

to_do_list = []

def print_func():
  print()
  for item in to_do_list:
    print(item)
  print()

while True:
  option = input("Do you want to view, add or edit your To_Do List?  ")
  print()
  
  if option == "view":
    print_func()
  elif option == "add":
    item = input("What would you like to add to your To-Do List?  ")
    to_do_list.append(item)
  elif option == "remove":
    item = input("What would you like to remove from your To-Do List?  ")
    if item in to_do_list:
      to_do_list.remove(item)
    else:
      print(f"{item} is not in To_Do List")

  print_func()
  time.sleep(3)
  os.system("clear")
  time.sleep(1)