# bmi_calc_improved
# Calculates body mass index for a person's height and weight
#    input: height and weight
#    output: body mass index and corresponding description
#       ("normal", "underweight", etc.)
# As distributed, the program displays a table showing all
# the ranges and their descriptions.  You will modify it to
# display just the relevant description for the user's inputs.
#
# Known bugs:
#   1) Accepts negative values for input.

def print_intro():
    print("This program computes your body mass index (BMI)")
    print("from your height and your weight. BMI is an")
    print("approximation of your body fat percentage.\n")

def main():
    print_intro()
    height= float(input("Enter you height in inches: "))
    weight= float(input("Enter you weight in pounds: "))
    calc_display_bmi(height,weight)

def print_meaning(bmi):
    if bmi < 18.5:
        print_row('< 18.5', 'underweight')
    elif 18.5 <= bmi < 25:
        print_row('18.5—25', 'normal')
    elif 25 <= bmi < 30:
        print_row('25—30', 'overwieght')
    else:
        print_row('> 30', 'obese')

def print_row(weight_range, description):
    print(format(weight_range, ".<10"),
          description, sep='')

def calc_display_bmi(height, weight):
    bmi = (703 * weight) / (height **2)
    print("Your BMI is",format(bmi,".2f"))
    print_meaning(bmi)

main()
