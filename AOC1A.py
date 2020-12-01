# language: Python 3.8 or higher as the new Walrus operator (:=) has been used.

expense_report = # a list
target = 2020

for i,value1 in enumerate(expense_report[:-1]):
  if (value2 := target - value1) in expense_report[i+1:]:
    print(f'Numbers found are {value1} and {value2}')
    print('Therefore solution is: ', value1*value2)
    break
else:
   print('No solution')