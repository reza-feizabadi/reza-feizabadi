import random
def gambler_ruin_simulation_single_run(initial_balance, bet_amount):
    """
    Simulates a single run of the gambler's ruin problem with variable betting amount,
    showing balance at each step.

    Parameters:
    - initial_balance: Starting amount of money the gambler has.
    - bet_amount: Fixed amount the gambler bets in each round.

    Returns:
    - balance_history: A list of balances at each step of the simulation.
    """
    balance = initial_balance
    balance_history = [balance]  # To store the balance after each round
    
    # Run until the gambler goes broke or decides to stop
    while balance > 0:
        # Adjust the bet if it exceeds the current balance
        current_bet = min(bet_amount, balance)
        
        # Simulate a fair coin toss
        if random.random() < 0.5:
            balance += current_bet  # Win, increase balance
        else:
            balance -= current_bet  # Lose, decrease balance
        
        # Append the current balance to history for step-by-step tracking
        balance_history.append(balance)
        
        # Print the balance at each step for real-time output
        print(f"Current Balance: {balance}")
        
        # Stop if balance is zero (bankruptcy)
        if balance == 0:
            print("The gambler has gone bankrupt.")
            break

    return balance_history

# Run a single simulation with step-by-step output
initial_balance = 10  # Starting balance of the gambler
bet_amount = 10        # Fixed betting amount per game

balance_history = gambler_ruin_simulation_single_run(initial_balance, bet_amount)
balance_history