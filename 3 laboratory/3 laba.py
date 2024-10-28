import sympy as sp

# Визначаємо функцію корисності
x = sp.Symbol('x', real=True, positive=True)
U = 0.1 * x**2

L1_outcomes = [0, 5, 20]
L1_probabilities = [0.5, 0.5, 0]

L2_outcomes = [10, 5, 30]
L2_probabilities = [0, 0.5, 0.5]

def expected_utility(outcomes, probabilities, utility_function):
    return sum(p * utility_function.subs(x, outcome) for outcome, p in zip(outcomes, probabilities))

M_U_L1 = expected_utility(L1_outcomes, L1_probabilities, U)
M_U_L2 = expected_utility(L2_outcomes, L2_probabilities, U)

E_L1 = sum(p * outcome for outcome, p in zip(L1_outcomes, L1_probabilities))
E_L2 = sum(p * outcome for outcome, p in zip(L2_outcomes, L2_probabilities))

X = sp.Symbol('X', real=True, positive=True)

certainty_equivalent_L1_solution = sp.solve(U - M_U_L1, x)
certainty_equivalent_L1 = certainty_equivalent_L1_solution[0] if certainty_equivalent_L1_solution else None

certainty_equivalent_L2_solution = sp.solve(U - M_U_L2, x)
certainty_equivalent_L2 = certainty_equivalent_L2_solution[0] if certainty_equivalent_L2_solution else None

if certainty_equivalent_L1 is None or certainty_equivalent_L2 is None:
    print("Не вдалося знайти детермінований еквівалент для однієї з лотерей. Перевірте коректність функції корисності або значень.")
else:
    risk_premium_L1 = E_L1 - certainty_equivalent_L1
    risk_premium_L2 = E_L2 - certainty_equivalent_L2

    preferred_lottery = "L1" if certainty_equivalent_L1 > certainty_equivalent_L2 else "L2"

    # Виведення результатів
    print("Очікувана корисність для L1:", M_U_L1)
    print("Очікувана корисність для L2:", M_U_L2)
    print("Очікуваний виграш для L1:", E_L1)
    print("Очікуваний виграш для L2:", E_L2)
    print("Детермінований еквівалент для L1:", certainty_equivalent_L1)
    print("Детермінований еквівалент для L2:", certainty_equivalent_L2)
    print("Премія за ризик для L1:", risk_premium_L1)
    print("Премія за ризик для L2:", risk_premium_L2)
    print("Вибрана лотерея:", preferred_lottery)
