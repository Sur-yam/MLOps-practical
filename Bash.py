from pathlib import Path

stages = [
    "Data collection", "Data validation", "Preprocessing",
    "Feature engineering", "Model training", "Model evaluation",
    "Deployment", "Monitoring", "Feedback and retraining"
]
print("MLOps workflow")
print(" -> ".join(stages))
output = Path(__file__).with_name("workflow_output.txt")
output.write_text(" -> ".join(stages) + "\n", encoding="utf-8")
print("Saved:", output)
