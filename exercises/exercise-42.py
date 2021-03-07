# Show even numbers

# bad method
#for c in range(0, 50):
#    if c % 2 == 0:
#        print(c, end=" ")
#print("End program..")

# good method
for c in range(2, 51, 2):
    print(c, end = " ")
print("End program...")
