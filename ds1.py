import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Users': [120, 180, 250, 310, 400, 520]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Users'], marker='o', color='blue', linestyle='--')

# Add titles and labels
plt.title('Growth of Bus Tracking App Users Over 6 Months')
plt.xlabel('Month')
plt.ylabel('Number of Users')
plt.grid(True)
plt.tight_layout()

# Show the graph
plt.show()
