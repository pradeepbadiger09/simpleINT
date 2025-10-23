P = 10000  # Principal
R = 10     # Rate of Interest
T = 1.5    # Time in years

SI = (P * R * T) / 100
print(f"Simple Interest: ₹{SI}")
CI = P * ((1 + R / 100) ** T) - P
print(f"Compound Interest: ₹{round(CI, 2)}")
