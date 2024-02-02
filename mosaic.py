# =====================================================================
# Mosaic example : 2 variables
# =====================================================================
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Preference': ['Tea', 'Coffee', 'Tea', 'Coffee', 'Coffee']
}

df = pd.DataFrame(data)

# Convert DataFrame to a format suitable for mosaic plot
# Here, we count occurrences of each Gender-Preference combination
plot_data = df.groupby(['Gender', 'Preference']).size()

# Create a mosaic plot
mosaic(plot_data, title='Gender vs. Preference Mosaic Plot')

# Display the plot
plt.show()
# =====================================================================
# Mosaic example : 3 variables
# =====================================================================
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# Sample data
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Preference': ['Tea', 'Coffee', 'Tea', 'Coffee', 'Coffee', 'Tea', 'Coffee'],
    'Age Group': ['Young', 'Old', 'Young', 'Old', 'Young', 'Young', 'Old']
}

df = pd.DataFrame(data)

# Group by all variables and count the occurrences
counts = df.groupby(['Gender', 'Preference', 'Age Group']).size()

# Convert the groupby object to a pandas Series with a MultiIndex
counts_series = counts.reset_index(name='size').set_index(['Gender', 'Preference', 'Age Group'])['size']

# Create a mosaic plot with the counts
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
mosaic(counts_series, title='Gender, Preference, and Age Group Mosaic Plot')
plt.show()
