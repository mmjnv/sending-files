from flask import Flask, request, send_from_directory

app = Flask(__name__)

# Set the directory to store the uploaded files
upload_directory = r"C:\Users\mmjnv\Desktop\final\New folder"

# Define the routes for handling file uploads
@app.route("/upload_image", methods=["POST"])
def upload_image():
    image_file = request.files["image"]
    image_file.save(f"{upload_directory}/image.jpg")
    return "Image file uploaded successfully!"

@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    csv_file = request.files["csv"]
    csv_file.save(f"{upload_directory}/data.csv")
    return "CSV file uploaded successfully!"

@app.route("/upload_json", methods=["POST"])
def upload_json():
    json_file = request.files["json"]
    json_file.save(f"{upload_directory}/data.json")
    return "JSON file uploaded successfully!"

# Define a route to serve the file
@app.route("/file/<filename>")
def serve_file(filename):
    return send_from_directory(upload_directory, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
