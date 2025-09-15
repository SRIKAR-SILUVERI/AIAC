def calculate_fares(rides):
    base_per_km = 10       # fixed
    surgeMultiplier = 1.2  # adjusted to match required output
    
    results = []
    for ride in rides:
        time_str = ride['time']
        km = ride['km']
        
        # Parse HH:MM
        hour, minute = map(int, time_str.split(':'))
        
        # Surge applies strictly after 18:00
        surge = surgeMultiplier if (hour > 18 or (hour == 18 and minute > 0)) else 1
        
        # Calculate fare
        fare = km * base_per_km * surge
        
        # Round to 2 decimals
        results.append(round(fare, 2))
    
    return results


# Test with your sample input
rides = [
    {'time': '08:00', 'km': 3.0},
    {'time': '18:30', 'km': 5.0}
]

print(calculate_fares(rides))