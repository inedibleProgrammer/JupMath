import math

def freq_from_db(db_target, gbw_hz=1_000_000):
    """
    Calculates the frequency for a specific dB value assuming a -20dB/decade slope.
    Standard LM358 GBW is approximately 1 MHz.
    """
    # Convert dB to a raw voltage gain ratio: Gain = 10^(dB/20)
    ratio = 10 ** (db_target / 20)
    
    # Frequency = GBW / Gain_Ratio
    freq = gbw_hz / ratio
    return freq

def log_interpolate(f_start, f_end, physical_percent):
    """
    Calculates the exact frequency of a point based on its physical position 
    between two markings on a log-scale axis.
    physical_percent: 0.5 for halfway, 0.3 for 30% across, etc.
    """
    log_start = math.log10(f_start)
    log_end = math.log10(f_end)
    
    # Find the log-value at that physical percentage
    log_target = log_start + (physical_percent * (log_end - log_start))
    
    # Convert back from log to frequency
    return 10 ** log_target

# --- EXECUTION ---
gbw_lm358 = 1_000_000  # 1MHz

# 1. Theoretical: Find frequency at 40dB
freq_at_40db = freq_from_db(40, gbw_lm358)
print(f"Frequency at 40dB (Theoretical): {freq_at_40db / 1000:.1f} kHz")

# 2. Visual: Find frequency physically "halfway" between 10k and 20k
freq_mid_10k_20k = log_interpolate(10000, 20000, 0.5)
print(f"Frequency at visual midpoint of 10k-20k: {freq_mid_10k_20k / 1000:.1f} kHz")
