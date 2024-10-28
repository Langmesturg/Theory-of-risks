import math

projects = {
    "A.Ink": {
        "price": 3400000,
        "periods": [3 * 12, 3 * 12 + 3, 3 * 12 + 6], 
        "probabilities": [0.5, 0.3, 0.2]
    },
    "B.Ltd": {
        "price": 2930000,
        "periods": [3 * 12 + 2, 4 * 12, 4 * 12 + 5],
        "probabilities": [0.3, 0.5, 0.2]
    },
    "ATС": {
        "price": 2500000,
        "periods": [4 * 12, 4 * 12 + 6, 5 * 12],
        "probabilities": [0.1, 0.4, 0.5]
    }
}

monthly_loss = 40000

def calculate_stats(project):
    expected_risk = 0
    risks = []
    
    for period, probability in zip(project["periods"], project["probabilities"]):
        delay_months = period - 36
        if delay_months > 0:
            risk = delay_months * monthly_loss
        else:
            risk = 0
        expected_risk += risk * probability
        risks.append(risk)
    
    mean = expected_risk
    
    variance = sum([prob * (risk - mean)**2 for risk, prob in zip(risks, project["probabilities"])])
    
    std_dev = math.sqrt(variance)
    
    return expected_risk, variance, std_dev

project_stats = {name: calculate_stats(project) for name, project in projects.items()}

for name, stats in project_stats.items():
    expected_risk, variance, std_dev = stats
    print(f"Project {name}:")
    print(f"  Expected risk: ${expected_risk:.2f}")
    print(f"  Variance: {variance:.2f}")
    print(f"  Standard deviation: {std_dev:.2f}\n")

optimal_project = min(project_stats, key=lambda name: project_stats[name][0])
print(f"Optimal project: {optimal_project} with expected risk = ${project_stats[optimal_project][0]:.2f}")
