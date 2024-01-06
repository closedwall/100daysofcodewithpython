from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon List",["pikachu","Bulbasore","charmender"])
table.add_column("Type",["electric","plant","fire"])
table.align='l'
print(table)