from website import create_app
import os


app = create_app()

TEMP_DIR = "/tmp/latex_conversion"  # Adjust as needed
os.makedirs(TEMP_DIR, exist_ok=True)  # Create directory if it doesn't exist

if __name__ == '__main__':
    app.run(debug=True)
