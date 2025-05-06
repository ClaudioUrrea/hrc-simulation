#!/usr/bin/env python3
import numpy as np
import pandas as pd

# Parámetros del paper
num_episodes = 10000
fatigue_levels = ['low', 'medium', 'high']
skill_levels = ['novice', 'intermediate', 'expert']
task_completion_time_mean = 10  # segundos
task_completion_time_std = 2    # segundos

# Generar datos
data = {
    'episode': range(num_episodes),
    'fatigue': np.random.choice([0, 0.5, 1], size=num_episodes, p=[0.3, 0.4, 0.3]),  # 0: low, 0.5: medium, 1: high
    'skill_level': np.random.choice([0, 1, 2], size=num_episodes, p=[0.3, 0.4, 0.3]),  # 0: novice, 1: intermediate, 2: expert
    'task_completion_time': np.random.normal(task_completion_time_mean, task_completion_time_std, num_episodes),
    'task_complexity': np.random.choice(['low', 'medium', 'high'], size=num_episodes, p=[0.3, 0.4, 0.3]),
    'task_type': np.random.choice(['human-only', 'robot-only', 'collaborative'], size=num_episodes, p=[0.3, 0.3, 0.4])
}

# Crear DataFrame y guardar
df = pd.DataFrame(data)
df.to_csv('synthetic_hrc_data.csv', index=False)
print("Datos sintéticos generados y guardados en synthetic_hrc_data.csv")
