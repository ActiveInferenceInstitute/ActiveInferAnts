import os
import csv
import random
from datetime import datetime, timezone

# Ensure the output folder exists
OUTPUT_FOLDER = "LegalData"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Define the 3R examples with sub-domains
EXAMPLES = [
    # Physical Security
    {"Setting": "Parking lot", "Sub-domain": "Public", "Recognize": "Key", "Remember": "Lock", "Respond": "Correct key opens lock"},
    {"Setting": "Factory/office", "Sub-domain": "Corporate", "Recognize": "Key card", "Remember": "Employee ID registry", "Respond": "Unlock door"},
    {"Setting": "Warehouse", "Sub-domain": "Logistics", "Recognize": "RFID tag", "Remember": "Inventory system", "Respond": "Track item"},
    {"Setting": "Gym access", "Sub-domain": "Recreational", "Recognize": "Membership card", "Remember": "Member database", "Respond": "Grant entry"},
    {"Setting": "Event entry", "Sub-domain": "Entertainment", "Recognize": "Ticket", "Remember": "Event attendee list", "Respond": "Allow entry"},
    {"Setting": "Voting booth", "Sub-domain": "Government", "Recognize": "Voter ID", "Remember": "Voter registry", "Respond": "Allow voting"},
    {"Setting": "University exam", "Sub-domain": "Education", "Recognize": "Student ID", "Remember": "Enrollment records", "Respond": "Permit exam participation"},
    {"Setting": "Hotel check-in", "Sub-domain": "Hospitality", "Recognize": "Reservation number", "Remember": "Booking system", "Respond": "Assign room"},
    {"Setting": "Public transportation", "Sub-domain": "Transport", "Recognize": "Transit card", "Remember": "Travel history", "Respond": "Allow ride"},
    {"Setting": "HOV tolling", "Sub-domain": "Transport", "Recognize": "License plate", "Remember": "DMV registry", "Respond": "Send toll bill to driver"},
    {"Setting": "Library", "Sub-domain": "Public", "Recognize": "Library card", "Remember": "Borrower records", "Respond": "Lend book"},
    {"Setting": "Smart home", "Sub-domain": "Residential", "Recognize": "Voice command", "Remember": "Device settings", "Respond": "Execute command"},
    {"Setting": "Smart lighting", "Sub-domain": "Residential", "Recognize": "Motion sensor", "Remember": "Lighting preferences", "Respond": "Adjust lighting"},
    {"Setting": "Smart thermostat", "Sub-domain": "Residential", "Recognize": "Temperature preference", "Remember": "Usage patterns", "Respond": "Adjust temperature"},
    {"Setting": "Smart fridge", "Sub-domain": "Residential", "Recognize": "Barcode", "Remember": "Inventory", "Respond": "Suggest recipes"},
    {"Setting": "Smart agriculture", "Sub-domain": "Agriculture", "Recognize": "Soil moisture level", "Remember": "Crop type", "Respond": "Adjust irrigation"},
    {"Setting": "Autonomous vehicle", "Sub-domain": "Transport", "Recognize": "Traffic signal", "Remember": "Route map", "Respond": "Adjust speed"},
    {"Setting": "Smart manufacturing", "Sub-domain": "Industrial", "Recognize": "Machine status", "Remember": "Maintenance schedule", "Respond": "Schedule repair"},
    {"Setting": "Smart energy", "Sub-domain": "Utilities", "Recognize": "Energy consumption", "Remember": "Usage patterns", "Respond": "Optimize energy distribution"},
    {"Setting": "Smart city", "Sub-domain": "Urban", "Recognize": "Sensor data", "Remember": "City management system", "Respond": "Optimize resources"},
    {"Setting": "Smart tourism", "Sub-domain": "Tourism", "Recognize": "Visitor preferences", "Remember": "Tour history", "Respond": "Customized tour suggestions"},
    {"Setting": "Smart logistics", "Sub-domain": "Logistics", "Recognize": "Package ID", "Remember": "Delivery route", "Respond": "Optimize delivery schedule"},
    {"Setting": "Smart retail", "Sub-domain": "Retail", "Recognize": "Customer face", "Remember": "Purchase history", "Respond": "Personalized offers"},
    {"Setting": "Smart healthcare", "Sub-domain": "Healthcare", "Recognize": "Wearable device data", "Remember": "Patient history", "Respond": "Health alerts"},
    
    # Digital Security
    {"Setting": "Computer login", "Sub-domain": "Corporate", "Recognize": "Password/biometric", "Remember": "Authorization registry", "Respond": "Grant access to system"},
    {"Setting": "Online interactions", "Sub-domain": "Social", "Recognize": "Username", "Remember": "Cookies", "Respond": "Custom content/ads"},
    {"Setting": "Online banking", "Sub-domain": "Finance", "Recognize": "OTP", "Remember": "Transaction history", "Respond": "Authorize transaction"},
    {"Setting": "Social media login", "Sub-domain": "Social", "Recognize": "Email/phone", "Remember": "User profile", "Respond": "Access account"},
    {"Setting": "E-commerce checkout", "Sub-domain": "Retail", "Recognize": "Payment method", "Remember": "Order history", "Respond": "Process payment"},
    {"Setting": "Online subscription", "Sub-domain": "Entertainment", "Recognize": "Subscription ID", "Remember": "Subscription records", "Respond": "Grant access to content"},
    {"Setting": "Online forum", "Sub-domain": "Social", "Recognize": "Username", "Remember": "Post history", "Respond": "Allow posting"},
    {"Setting": "Online gaming", "Sub-domain": "Entertainment", "Recognize": "Gamer tag", "Remember": "Game profile", "Respond": "Access game features"},
    {"Setting": "Online auction", "Sub-domain": "Retail", "Recognize": "Bidder ID", "Remember": "Bid history", "Respond": "Place bid"},
    {"Setting": "Online dating", "Sub-domain": "Social", "Recognize": "Profile", "Remember": "Match history", "Respond": "Suggest matches"},
    {"Setting": "Streaming service", "Sub-domain": "Entertainment", "Recognize": "Account login", "Remember": "Watch history", "Respond": "Recommend content"},
    {"Setting": "Online marketplace", "Sub-domain": "Retail", "Recognize": "Seller ID", "Remember": "Sales history", "Respond": "Process sale"},
    {"Setting": "E-learning platform", "Sub-domain": "Education", "Recognize": "Student login", "Remember": "Course records", "Respond": "Access course materials"},
    {"Setting": "Virtual assistant", "Sub-domain": "Residential", "Recognize": "Voice", "Remember": "User preferences", "Respond": "Perform tasks"},
    {"Setting": "Customer support", "Sub-domain": "Corporate", "Recognize": "Ticket number", "Remember": "Support history", "Respond": "Resolve issue"},
    {"Setting": "Corporate network", "Sub-domain": "Corporate", "Recognize": "VPN credentials", "Remember": "Access logs", "Respond": "Grant network access"},
    {"Setting": "Cognitive security - Email", "Sub-domain": "Corporate", "Recognize": "Suspicious email", "Remember": "Known phishing patterns", "Respond": "Block email"},
    {"Setting": "Cognitive security - Web browsing", "Sub-domain": "Corporate", "Recognize": "Malicious URL", "Remember": "Blacklist", "Respond": "Block access"},
    {"Setting": "Cognitive security - Network", "Sub-domain": "Corporate", "Recognize": "Unusual traffic", "Remember": "Baseline behavior", "Respond": "Alert admin"},
    
    # Financial Transactions
    {"Setting": "Retail store", "Sub-domain": "Retail", "Recognize": "Credit card", "Remember": "Bank record", "Respond": "Access to credit given"},
    {"Setting": "Banking withdrawal", "Sub-domain": "Finance", "Recognize": "Debit card PIN", "Remember": "ATM/bank records", "Respond": "Dispense cash"},
    {"Setting": "Loan security", "Sub-domain": "Finance", "Recognize": "UCC-1", "Remember": "Central filing location", "Respond": "Perfect security interest"},
    {"Setting": "Smart finance", "Sub-domain": "Finance", "Recognize": "Transaction pattern", "Remember": "Account history", "Respond": "Fraud detection"},
    
    # Legal and Professional
    {"Setting": "Law office", "Sub-domain": "Legal", "Recognize": "Law school diploma", "Remember": "Law school records", "Respond": "Admission to practice"},
    {"Setting": "Work for hire", "Sub-domain": "Corporate", "Recognize": "Role-based access", "Remember": "Permission structure", "Respond": "Adopt employee output"},
    {"Setting": "USCIS Form I-9", "Sub-domain": "Government", "Recognize": "Passport", "Remember": "Archive form I-9", "Respond": "Hire"},
    {"Setting": "Job application", "Sub-domain": "Corporate", "Recognize": "Resume", "Remember": "Applicant tracking system", "Respond": "Schedule interview"},
    
    # Healthcare
    {"Setting": "Medical appointment", "Sub-domain": "Healthcare", "Recognize": "Insurance card", "Remember": "Patient records", "Respond": "Provide treatment"},
    {"Setting": "Healthcare system", "Sub-domain": "Healthcare", "Recognize": "Medical ID", "Remember": "Health records", "Respond": "Provide care"},
    {"Setting": "Telemedicine", "Sub-domain": "Healthcare", "Recognize": "Patient ID", "Remember": "Medical history", "Respond": "Conduct consultation"},
    {"Setting": "Health security - Hospital", "Sub-domain": "Healthcare", "Recognize": "Patient wristband", "Remember": "Patient records", "Respond": "Provide treatment"},
    {"Setting": "Health security - Pharmacy", "Sub-domain": "Healthcare", "Recognize": "Prescription", "Remember": "Doctor's orders", "Respond": "Dispense medication"},
    {"Setting": "Health security - Telehealth", "Sub-domain": "Healthcare", "Recognize": "Patient login", "Remember": "Medical history", "Respond": "Start consultation"},
    {"Setting": "Health security - Emergency", "Sub-domain": "Healthcare", "Recognize": "Emergency ID", "Remember": "Emergency contact info", "Respond": "Notify contacts"},
    {"Setting": "Health security - Fitness app", "Sub-domain": "Healthcare", "Recognize": "User profile", "Remember": "Health data", "Respond": "Provide workout plan"},
    
    # Miscellaneous
    {"Setting": "Fitness tracker", "Sub-domain": "Healthcare", "Recognize": "User profile", "Remember": "Activity data", "Respond": "Provide feedback"},
    {"Setting": "Ride-sharing", "Sub-domain": "Transport", "Recognize": "Driver ID", "Remember": "Ride history", "Respond": "Assign ride"},
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
    fieldnames = ["Setting", "Sub-domain", "Recognize", "Remember", "Respond", "UTC Timestamp", "Recognizing Party", "Remembering Party", "Responding Party", "Risk Score"]
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
