new_list = [1,2,3,4,5]
n = int(input("Enter the value of nth node to be deleted.\n"))
def removenthnode(new_list, n):
  del new_list[n]

save_list = new_list.copy()  # or save_list = new_list[:]
removenthnode(new_list, n)
print(f"New List is {new_list}")
