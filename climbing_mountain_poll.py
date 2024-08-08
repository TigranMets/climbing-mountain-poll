print('Welcome to the Mountain Climbing Poll!')

responses = {}

while True:
    full_name = input('\nPlease enter your full name: ')
    responses[full_name] = input('Which mountain would you like to climb one day? ')
    new_respondent_prompt = 'Would you like to let another person respond (yes/no)? '
    new_respondent = input(new_respondent_prompt)
    while new_respondent not in ('yes', 'no'):
        new_respondent = input(f'Please enter yes or no. \n{new_respondent_prompt}')
    if new_respondent == 'no': break
    
print("\n--- Poll Results ---")
for name, response in responses.items(): print(f'{name} would like to climb {response}')