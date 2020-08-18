optimal = int(input())
H = int(input())
M = int(input())

output_hours = ((optimal + M) // 60 + H) % 24
output_minutes = (optimal + M) % 60

print(output_hours)
print(output_minutes)