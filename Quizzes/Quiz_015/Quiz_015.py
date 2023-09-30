def open_doors(num_students: int) -> int:
    vars = []
    count = 0
    for x in range(num_students):
        vars.append(0)
    for students in range(num_students):
        for d in range(students, num_students, students + 1):
            vars[d] = not vars[d]
    for n in vars:
        if n:
            count += 1
    return count

z = open_doors(num_students=5678)
print(z)