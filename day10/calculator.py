import os
#calculator
#add
def add(n1, n2):
    return round((n1 + n2)*100)/100

#substract
def substract(n1, n2):
    return round((n1 - n2)*100)/100

#multiply
def multiply(n1, n2):
    return round((n1 * n2)*100)/100

#division
def division(n1, n2):
    return round((n1 / n2) * 100) / 100

calculator = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division,
}

def calculation():
    dicision = True
    execute_once = True
    answer = 0
    while dicision:
        os.system('cls')
        print("choose symbol to perform operation")
        if execute_once:
            answer = float(input("whats your first number: "))
            execute_once = False
        for key in calculator:
            print(key)
        symbol = input("pick an operation: ")
        n2 = float(input("whats your second number: "))

        function = calculator[symbol]
        final_answer = function(answer, n2)
        print(f"{answer} {symbol} {n2} = {final_answer}")
        answer = final_answer
        choose = input(
            "do you want to continue calculation or start new calculation: y/n "
        )
        if choose == 'n':
            dicision = False
            calculation()
          
calculation()