# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47' 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24' 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42' 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12' 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15' 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names():
    for star in targets:
        print(star)
print_star_names()

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_names_and_spectral_types():
    for star in targets:
        print(f"{star}: {targets[star]['Spectral Type']}")
print_star_names_and_spectral_types()

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_bright_stars():
    for star in targets:
        if targets[star]['Magnitude'] > 0.1:
            print(star)
find_bright_stars()

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Lucy"] = {
    "RA": "08h 13m 35.4s",
    "Dec": "+24° 01' 19″",
    "Magnitude": 2.4,
    "Spectral Type": "G2V"
}
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest_star_near_20_declination():
    closest_star = None
    min_diff = float('inf')
    for star in targets:
        declination = targets[star]['Dec']
        # Convert Dec to a numeric value for comparison (simplified)
        declination_value = float(declination.split('°')[0])
        diff = abs(declination_value - 20)
        if diff < min_diff:
            min_diff = diff
            closest_star = star
    return closest_star
print(find_brightest_star_near_20_declination())


# 6) What is your favorite constellation?
# My favorite constellation is Lyra.
