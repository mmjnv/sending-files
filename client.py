import requests
import time

# Set the server IP address and port
server_ip = "192.168.200.163"
server_port = 8000

# Define the menu function
def display_menu():
    print("Menu:")
    print("1. Upload image")
    print("2. Upload CSV")
    print("3. Upload JSON")
    print("4. Exit")

# Send the file to the server with timeout
def upload_file(file_type, file_path):
    start_time = time.time()
    with open(file_path, "rb") as file:
        file_data = file.read()
        files = {file_type: file_data}
        endpoint = ""
        if file_type == "image":
            endpoint = "upload_image"
        elif file_type == "csv":
            endpoint = "upload_csv"
        elif file_type == "json":
            endpoint = "upload_json"
        try:
            response = requests.post(f"http://{server_ip}:{server_port}/{endpoint}", files=files, timeout=5)
            print(response.text)  # Print the response from the server
        except requests.Timeout:
            print("File upload timed out.")
            return
        end_time = time.time()
        latency = end_time - start_time
        print(f"End-to-end latency: {latency} seconds")

# Main menu loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        image_path = input("Enter the image file path: ")
        upload_file("image", image_path)
    elif choice == "2":
        csv_path = input("Enter the CSV file path: ")
        upload_file("csv", csv_path)
    elif choice == "3":
        json_path = input("Enter the JSON file path: ")
        upload_file("json", json_path)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
