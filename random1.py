import random
print(random.random())
random.seed(50)
print(random.randint(10, 20))
random.seed(19)
print(random.randint(10, 20))
print(random.randint(10, 20))

print(random.choice(["salam", "necesen", "sagol"]))
