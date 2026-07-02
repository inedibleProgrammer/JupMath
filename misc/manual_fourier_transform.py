import numpy as np

def manual_fourier_transform(t, x, target_freqs):
    """
    Numerically integrates the Fourier Transform: 
    Integral of x(t) * exp(-j * 2 * pi * f * t) dt
    """
    N = len(t)
    dt = t[1] - t[0] # The 'dt' from our integral
    X_f = []

    for f in target_freqs:
        # Create the complex exponential 'e^(-j*2*pi*f*t)'
        # Using Euler's Formula: e^(-j*theta) = cos(theta) - j*sin(theta)
        exponent = -2j * np.pi * f * t
        basis_function = np.exp(exponent)
        
        # Multiply signal by basis and sum (This is the numerical integration)
        integral_sum = np.sum(x * basis_function) * dt
        X_f.append(integral_sum)
        
    return np.array(X_f)

# --- Example Usage ---
fs = 1000
t = np.linspace(0, 1.0, fs, endpoint=False)
# 60Hz noise signal (common in your embedded work)
x = np.sin(2 * np.pi * 60 * t) 

# Define the frequencies we want to check
frequencies_to_check = np.arange(0, 150, 1) # Check 0Hz to 150Hz

# Run our manual integral
spectrum = manual_fourier_transform(t, x, frequencies_to_check)
magnitude = np.abs(spectrum)

print(magnitude)
