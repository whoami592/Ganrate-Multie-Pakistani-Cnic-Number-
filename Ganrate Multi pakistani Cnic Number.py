import random

def generate_cnic():
    # Generate a random CNIC number
    cnic_number = str(random.randint(1000000000000, 9999999999999))
    return cnic_number

def get_details(cnic):
    # Get the details of the CNIC number
    # (This is a placeholder for a real API call to get the details)
    details = {
        "name": "This tools created byMR Sabaz Ali khan",
        "location": "pakistan khyber pakhtunkhwa",
        "cnic": cnic
    }
    return details

def main():
    # Generate a random CNIC number
    cnic = generate_cnic()
    
    # Get the details of the CNIC number
    details = get_details(cnic)
    
    # Print the details
    print("Name:", details["name"])
    print("Location:", details["location"])
    print("CNIC:", details["cnic"])

# Run the main function
main()