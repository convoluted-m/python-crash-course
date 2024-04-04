# 
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# the loop will run forever unless it reaches a break statement
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to visit  {city.title()}!")
    
