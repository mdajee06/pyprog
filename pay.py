hours = float(input("hours worked?"))
if hours > 40:
    overtime_hours = hours - 40
else:
    overtime_hours = 0
base_hours = hours - overtime_hours
wages = base_hours * 12 + overtime_hours * 12 * 1.5
print(f"wages = {wages} ")
