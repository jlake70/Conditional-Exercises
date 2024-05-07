#Write a program that prompts user to enter a traffic light color and outputs the action to take

light_color = input("Enter the traffic light color (red, yellow, green):")

if light_color == "red":
    print("Stop the car!")
elif light_color == "green":
    print("Keep on your way!")
elif light_color  == "yellow":
    print("Slow down!")
#Could also write else instead of final elif
#else:
#   print("Slow Down!")