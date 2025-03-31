def cap_rate(net_operating_income, property_value):
    return (net_operating_income / property_value) * 100


# Example inputs
net_operating_income = 500000  # Annual NOI in dollars
property_value = 8000000  # Property value in dollars

cap_rate_value = cap_rate(net_operating_income, property_value)
print(f"Cap Rate: {cap_rate_value:.2f}%")


