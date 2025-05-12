# Cinema Ticket Reservation – Mini Project

# Task:
# Create a simple script where the user reserves cinema tickets.

#Program features:
# - Ask the user for:
#     - their name
#     - number of tickets
#     - whether they want 3D (yes/no)
#
# - Ticket prices:
#     - Regular: 6 €
#     - 3D: 8 €
#
# - Print the final price and a thank-you message.
#
# - If the number of tickets is negative or invalid, show a warning.

# Bonus features:
# - If the user orders more than 5 tickets, apply a 10% discount.
# - Handle user input carefully (use int(), .lower(), data checks)


print("Welcome to the cinema, here you can choose your ticket!")

#input user's
print("Please enter your name.")
name = input()

print(f"Hello {name} please, how many tickets do you want?")
sum_tickets = int(input())

if sum_tickets <= 0:
    print("Invalid number of tickets. Please enter a number greater than 0.")
else: 

    type_ticket = input("Okay, so what type of movie do you want to go to? 2D or 3D? 2D costs 6 Euros and 3D costs 8 Euros.\n").strip().lower()
    

    if type_ticket == "2d":
        price_ticket = 6
        
    elif type_ticket == "3d":
        price_ticket = 8
    else:
        print("Invalid ticket type. Please choose 2D or 3D.")
        price_ticket = 0

# Price calculation
    total_price = sum_tickets * price_ticket

 # Bonus: 10% discount for more than 5 tickets
    if sum_tickets > 5:
        discount = total_price * 0.10
        total_price -= discount
        print(f"You got a 10% discount of {discount:.2f} €!")

    # Final output
    print(f"You reserved {sum_tickets} tickets for a {type_ticket.upper()} movie.")
    print(f"Final price: {total_price:.2f} €")
    print("Thank you and enjoy your movie!")


