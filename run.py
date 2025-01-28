from app import create_app

# Create Flask App
app = create_app()

# Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)  # Starts the server
