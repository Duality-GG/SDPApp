# this is for the user to manually type what they want to look at
# in our links code, we can have user automatically copy and paste their link

# as a reminder, this is can integrated into presets and constellations.

def get_constellation_coordinates():
    right_ascension = float(input("Enter the Right Ascension of the constellation (in hours): "))
    declination = float(input("Enter the Declination of the constellation (in degrees): "))
    return right_ascension, declination

def get_exposure_details():
    number_of_exposures = int(input("Enter the number of exposures: "))
    exposure_length = float(input("Enter the length of each exposure (in seconds): "))
    return number_of_exposures, exposure_length

def main():
    print("Enter the details for the astrophotography session:")
    ra, dec = get_constellation_coordinates() # right ascension , declination
    num_exposures, exp_length = get_exposure_details()

    print(f"\nAstrophotography Session Details:")
    print(f"Constellation Coordinates: Right Ascension = {ra} hours, Declination = {dec} degrees")
    print(f"Number of Exposures: {num_exposures}")
    print(f"Exposure Length: {exp_length} seconds")

if __name__ == "__main__":
    main()
