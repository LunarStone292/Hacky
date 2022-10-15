import random
import os

def coin():
    input("\n Press enter to flip the coin...")
    testa_croce = random.choice(['cross', 'head'])
    print("\n " + testa_croce)

coin()