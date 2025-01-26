#Name with Initials Code 

full_name = input("Please enter you full name: > ")

name_parts = full_name.split()
# Verify the full name prints with splits use print(name_parts)

first_name = name_parts[0]
last_name = name_parts[-1]
# Verify print(first_name)
# Verify print(last_name)

middle_name = '' if len(name_parts) <= 2 else name_parts[1]
# Verify middle name prints print(middle_name)

middle_initials = "".join([name[0] + "." for name in middle_name.split()])
# Verify print(middle_initials)

Full_name = f"{last_name}, {first_name[0]}.{middle_initials}"
print()
print (f"Aloha {Full_name} Have an amazing day!") 