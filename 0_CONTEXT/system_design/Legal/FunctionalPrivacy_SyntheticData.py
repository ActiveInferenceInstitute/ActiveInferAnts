import os
import csv
import random
from datetime import datetime, timezone

# Ensure the output folder exists
OUTPUT_FOLDER = "LegalData"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Define the 3R examples
EXAMPLES = [
    {"Setting": "Parking lot", "Recognize": "Key", "Remember": "Lock", "Respond": "Correct key opens lock"},
    {"Setting": "Retail store", "Recognize": "Credit card", "Remember": "Bank record", "Respond": "Access to credit given"},
    {"Setting": "Factory/office", "Recognize": "Key card", "Remember": "Employee ID registry", "Respond": "Unlock door"},
    {"Setting": "Computer login", "Recognize": "Password/biometric", "Remember": "Authorization registry", "Respond": "Grant access to system"},
    {"Setting": "Law office", "Recognize": "Law school diploma", "Remember": "Law school records", "Respond": "Admission to practice"},
    {"Setting": "Banking withdrawal", "Recognize": "Debit card PIN", "Remember": "ATM/bank records", "Respond": "Dispense cash"},
    {"Setting": "Loan security", "Recognize": "UCC-1", "Remember": "Central filing location", "Respond": "Perfect security interest"},
    {"Setting": "Online interactions", "Recognize": "Username", "Remember": "Cookies", "Respond": "Custom content/ads"},
    {"Setting": "HOV tolling", "Recognize": "License plate", "Remember": "DMV registry", "Respond": "Send toll bill to driver"},
    {"Setting": "Grocery store", "Recognize": "Trademark", "Remember": "Consumer recalls ads", "Respond": "Purchase trusted brand"},
    {"Setting": "Work for hire", "Recognize": "Role-based access", "Remember": "Permission structure", "Respond": "Adopt employee output"},
    {"Setting": "USCIS Form I-9", "Recognize": "Passport", "Remember": "Archive form I-9", "Respond": "Hire"},
    {"Setting": "Library", "Recognize": "Library card", "Remember": "Borrower records", "Respond": "Lend book"},
    {"Setting": "Hotel check-in", "Recognize": "Reservation number", "Remember": "Booking system", "Respond": "Assign room"},
    {"Setting": "Medical appointment", "Recognize": "Insurance card", "Remember": "Patient records", "Respond": "Provide treatment"},
    {"Setting": "Online banking", "Recognize": "OTP", "Remember": "Transaction history", "Respond": "Authorize transaction"},
    {"Setting": "Social media login", "Recognize": "Email/phone", "Remember": "User profile", "Respond": "Access account"},
    {"Setting": "E-commerce checkout", "Recognize": "Payment method", "Remember": "Order history", "Respond": "Process payment"},
    {"Setting": "Gym access", "Recognize": "Membership card", "Remember": "Member database", "Respond": "Grant entry"},
    {"Setting": "Public transportation", "Recognize": "Transit card", "Remember": "Travel history", "Respond": "Allow ride"},
    {"Setting": "University exam", "Recognize": "Student ID", "Remember": "Enrollment records", "Respond": "Permit exam participation"},
    {"Setting": "Voting booth", "Recognize": "Voter ID", "Remember": "Voter registry", "Respond": "Allow voting"},
    {"Setting": "Online subscription", "Recognize": "Subscription ID", "Remember": "Subscription records", "Respond": "Grant access to content"},
    {"Setting": "Event entry", "Recognize": "Ticket", "Remember": "Event attendee list", "Respond": "Allow entry"},
    {"Setting": "Warehouse", "Recognize": "RFID tag", "Remember": "Inventory system", "Respond": "Track item"},
    {"Setting": "Smart home", "Recognize": "Voice command", "Remember": "Device settings", "Respond": "Execute command"},
    {"Setting": "Online gaming", "Recognize": "Gamer tag", "Remember": "Game profile", "Respond": "Access game features"},
    {"Setting": "Healthcare system", "Recognize": "Medical ID", "Remember": "Health records", "Respond": "Provide care"},
    {"Setting": "Corporate network", "Recognize": "VPN credentials", "Remember": "Access logs", "Respond": "Grant network access"},
    {"Setting": "E-learning platform", "Recognize": "Student login", "Remember": "Course records", "Respond": "Access course materials"},
    {"Setting": "Smart city", "Recognize": "Sensor data", "Remember": "City management system", "Respond": "Optimize resources"},
    {"Setting": "Online forum", "Recognize": "Username", "Remember": "Post history", "Respond": "Allow posting"},
    {"Setting": "Fitness tracker", "Recognize": "User profile", "Remember": "Activity data", "Respond": "Provide feedback"},
    {"Setting": "Virtual assistant", "Recognize": "Voice", "Remember": "User preferences", "Respond": "Perform tasks"},
    {"Setting": "Job application", "Recognize": "Resume", "Remember": "Applicant tracking system", "Respond": "Schedule interview"},
    {"Setting": "Customer support", "Recognize": "Ticket number", "Remember": "Support history", "Respond": "Resolve issue"},
    {"Setting": "Online auction", "Recognize": "Bidder ID", "Remember": "Bid history", "Respond": "Place bid"},
    {"Setting": "Smart thermostat", "Recognize": "Temperature preference", "Remember": "Usage patterns", "Respond": "Adjust temperature"},
    {"Setting": "Online dating", "Recognize": "Profile", "Remember": "Match history", "Respond": "Suggest matches"},
    {"Setting": "Ride-sharing", "Recognize": "Driver ID", "Remember": "Ride history", "Respond": "Assign ride"},
    {"Setting": "Streaming service", "Recognize": "Account login", "Remember": "Watch history", "Respond": "Recommend content"},
    {"Setting": "Online marketplace", "Recognize": "Seller ID", "Remember": "Sales history", "Respond": "Process sale"},
    {"Setting": "Smart fridge", "Recognize": "Barcode", "Remember": "Inventory", "Respond": "Suggest recipes"},
    {"Setting": "Online education", "Recognize": "Student ID", "Remember": "Grades", "Respond": "Provide feedback"},
    {"Setting": "Telemedicine", "Recognize": "Patient ID", "Remember": "Medical history", "Respond": "Conduct consultation"},
    {"Setting": "Smart lighting", "Recognize": "Motion sensor", "Remember": "Lighting preferences", "Respond": "Adjust lighting"},
    {"Setting": "Cognitive security - Email", "Recognize": "Suspicious email", "Remember": "Known phishing patterns", "Respond": "Block email"},
    {"Setting": "Cognitive security - Web browsing", "Recognize": "Malicious URL", "Remember": "Blacklist", "Respond": "Block access"},
    {"Setting": "Cognitive security - Network", "Recognize": "Unusual traffic", "Remember": "Baseline behavior", "Respond": "Alert admin"},
    {"Setting": "Health security - Hospital", "Recognize": "Patient wristband", "Remember": "Patient records", "Respond": "Provide treatment"},
    {"Setting": "Health security - Pharmacy", "Recognize": "Prescription", "Remember": "Doctor's orders", "Respond": "Dispense medication"},
    {"Setting": "Health security - Telehealth", "Recognize": "Patient login", "Remember": "Medical history", "Respond": "Start consultation"},
    {"Setting": "Health security - Emergency", "Recognize": "Emergency ID", "Remember": "Emergency contact info", "Respond": "Notify contacts"},
    {"Setting": "Health security - Fitness app", "Recognize": "User profile", "Remember": "Health data", "Respond": "Provide workout plan"},
    {"Setting": "Smart agriculture", "Recognize": "Soil moisture level", "Remember": "Crop type", "Respond": "Adjust irrigation"},
    {"Setting": "Autonomous vehicle", "Recognize": "Traffic signal", "Remember": "Route map", "Respond": "Adjust speed"},
    {"Setting": "Smart retail", "Recognize": "Customer face", "Remember": "Purchase history", "Respond": "Personalized offers"},
    {"Setting": "Smart healthcare", "Recognize": "Wearable device data", "Remember": "Patient history", "Respond": "Health alerts"},
    {"Setting": "Smart manufacturing", "Recognize": "Machine status", "Remember": "Maintenance schedule", "Respond": "Schedule repair"},
    {"Setting": "Smart energy", "Recognize": "Energy consumption", "Remember": "Usage patterns", "Respond": "Optimize energy distribution"},
    {"Setting": "Smart education", "Recognize": "Student engagement", "Remember": "Learning progress", "Respond": "Adaptive learning content"},
    {"Setting": "Smart tourism", "Recognize": "Visitor preferences", "Remember": "Tour history", "Respond": "Customized tour suggestions"},
    {"Setting": "Smart logistics", "Recognize": "Package ID", "Remember": "Delivery route", "Respond": "Optimize delivery schedule"},
    {"Setting": "Smart finance", "Recognize": "Transaction pattern", "Remember": "Account history", "Respond": "Fraud detection"},
]

def generate_synthetic_data(num_records: int) -> list:
    # Generates a synthetic dataset based on predefined examples.
    #
    # Parameters:
    # - num_records (int): The number of synthetic records to generate.
    #
    # Returns:
    # - list: A list of dictionaries representing the synthetic dataset.
    synthetic_data = []
    for _ in range(num_records):
        example = random.choice(EXAMPLES)
        example["UTC Timestamp"] = datetime.now(timezone.utc).isoformat()
        example["Recognizing Party"] = f"Party_{random.randint(1, 100)}"
        example["Remembering Party"] = f"Party_{random.randint(1, 100)}"
        example["Responding Party"] = f"Party_{random.randint(1, 100)}"
        example["Risk Score"] = random.randint(1, 100)
        synthetic_data.append(example)
    return synthetic_data

def save_synthetic_data_to_csv(data: list, file_path: str) -> None:
    # Saves the synthetic dataset to a CSV file.
    #
    # Parameters:
    # - data (list): The synthetic dataset to save.
    # - file_path (str): The path to the CSV file.
    fieldnames = ["Setting", "Recognize", "Remember", "Respond", "UTC Timestamp", "Recognizing Party", "Remembering Party", "Responding Party", "Risk Score"]
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Synthetic dataset saved to {file_path}")

def main():
    # Main function to generate and save the synthetic dataset.
    num_records = 50  # Number of synthetic examples to generate
    synthetic_dataset = generate_synthetic_data(num_records)
    
    # Print the synthetic dataset to terminal
    for data in synthetic_dataset:
        print(data)
    
    # Save the synthetic dataset to a CSV file
    csv_file_path = os.path.join(OUTPUT_FOLDER, "synthetic_3R_data.csv")
    save_synthetic_data_to_csv(synthetic_dataset, csv_file_path)

if __name__ == "__main__":
    main()
