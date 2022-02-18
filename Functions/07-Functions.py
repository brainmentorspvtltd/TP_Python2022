def playerHealth():
    health = 56
    return health

def enemyHealth():
    health = 45
    return health

def showHealth():
    h1 = playerHealth()
    h2 = enemyHealth()
    print("Player Health :",h1)
    print("Enemy Health :",h2)

showHealth()