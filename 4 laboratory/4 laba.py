import numpy as np

# Дані для задачі
zckp = [0.16, 0.16, 0.2, 0.25, 0.25, 0.1, 0.1, 0.08, 0.07, 0.15, 0.15]
ztransport = [0.15, 0.12, 0.15, 0.1, 0.11, 0.18, 0.18, 0.15, 0.1, 0.11, 0.18]
rohani = [40, 37, 35, 40, 35, 60, 40, 35, 33, 35, 60]

# 1. Обчислення середньої очікуваної норми прибутку та ризику
def expected_return_and_risk(returns):
    expected_return = np.mean(returns)
    risk = np.std(returns)
    return expected_return, risk

expected_zckp, risk_zckp = expected_return_and_risk(zckp)
expected_ztransport, risk_ztransport = expected_return_and_risk(ztransport)
expected_rohani, risk_rohani = expected_return_and_risk(rohani)

print("Середня очікувана норма прибутку та ризик:")
print(f"Жидачівський ЦПК: {expected_zckp:.2f}, {risk_zckp:.2f}")
print(f"Запоріжтранспорт: {expected_ztransport:.2f}, {risk_ztransport:.2f}")
print(f"Рогани: {expected_rohani:.2f}, {risk_rohani:.2f}")

# 2. Обчислення коваріаційної та кореляційної матриць
returns_matrix = np.array([zckp, ztransport, rohani])
cov_matrix = np.cov(returns_matrix)
corr_matrix = np.corrcoef(returns_matrix)

print("\nКоваріаційна матриця:")
print(cov_matrix)
print("\nКореляційна матриця:")
print(corr_matrix)

# 3. Формування портфеля для мінімізації ризику
# Використання ваг для кожної акції
def portfolio_risk(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Припустимо, що сума ваг = 1 (x1 + x2 + x3 = 1)
from scipy.optimize import minimize

def minimize_risk(weights):
    return portfolio_risk(weights, cov_matrix)

# Початкові ваги для мінімізації ризику
initial_weights = [1/3, 1/3, 1/3]
bounds = [(0, 1), (0, 1), (0, 1)]
constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}

# Оптимізація
result = minimize(minimize_risk, initial_weights, bounds=bounds, constraints=constraints)
min_risk_weights = result.x

print("\nВаги портфеля для мінімізації ризику:")
print(min_risk_weights)

# 4. Формування портфеля для бажаного прибутку (mp = 5%)
target_return = 0.05

def portfolio_return(weights, expected_returns):
    return np.dot(weights, expected_returns)

expected_returns = np.array([expected_zckp, expected_ztransport, expected_rohani])

def target_return_constraint(weights):
    return portfolio_return(weights, expected_returns) - target_return

constraints = [{'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
               {'type': 'eq', 'fun': target_return_constraint}]

# Оптимізація для досягнення бажаного прибутку
result = minimize(minimize_risk, initial_weights, bounds=bounds, constraints=constraints)
target_return_weights = result.x

print("\nВаги портфеля для бажаного прибутку (5%):")
print(target_return_weights)
