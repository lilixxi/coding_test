students = list(range(1,31))
submit = [int(input()) for _ in range(28)]
n_submitted = (list(set(students) - set(submit)))
n_submitted.sort()
for _ in n_submitted:
  print(_)