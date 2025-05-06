complete=" bob's your uncle"
complete=complete.split("")
first_part=complete[1].split("")
result=f"{first_part[2]}'{first_part[0]} {first_part[1]} {complete[0]}"

print(result)