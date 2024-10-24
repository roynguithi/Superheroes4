# Superheroes4

Welcome to the Superheroes API! This API allows you to track heroes and their superpowers. It is built using Flask and SQLAlchemy, making it a great starting point for learning about RESTful APIs and database interactions in Python.

Table of Contents

- Features
- Technologies Used
- Getting Started
- API Endpoints
- Database Structure
- Running the Application
- Testing the API
- Contributing
- License

Features

- View a list of heroes and their details
- Retrieve specific hero information by ID
- List all available superpowers
- Retrieve specific superpower information by ID
- Update superpower descriptions
- Create new associations between heroes and their powers

Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- PostgreSQL: A powerful, open-source relational database.
- Marshmallow: For object serialization and deserialization.

Getting Started

To get started with this project, you'll need to clone the repository and install the required dependencies.

Prerequisites

- Python 3.x installed on your machine.
- PostgreSQL installed and running.
- pip for installing Python packages.

Clone the Repository

You can clone the repository using the following commands:

git clone git@github.com:roynguithi/Superheroes4.git
cd phase-4-superheroes4

Install Dependencies

Use pip to install the required packages:

pip install -r requirements.txt

API Endpoints

Heroes

- GET /heroes
  - Returns a list of all heroes.

- GET /heroes/:id
  - Returns detailed information about a specific hero, including their powers.

Powers

- GET /powers
  - Returns a list of all superpowers.

- GET /powers/:id
  - Returns detailed information about a specific superpower.

- PATCH /powers/:id
  - Updates the description of a specific superpower.

Hero Powers

- POST /hero_powers
  - Creates a new association between a hero and a power.

Database Structure

The application uses a relational database structure with the following models:

- Hero
  - id: Unique identifier for the hero.
  - name: Real name of the hero.
  - super_name: Superhero name of the hero.

- Power
  - id: Unique identifier for the power.
  - name: Name of the superpower.
  - description: Description of the superpower.

- HeroPower
  - id: Unique identifier for the hero-power relationship.
  - hero_id: Foreign key referencing a hero.
  - power_id: Foreign key referencing a power.
  - strength: Indicates the strength of the power for the hero (e.g., Strong, Weak, Average).

Running the Application

To run the application, make sure your PostgreSQL database is running and then execute:

python app.py

This will start the Flask development server, and you can access the API at http://127.0.0.1:5000.

Testing the API

You can test the API using Postman or cURL. Import the provided Postman collection to explore the various endpoints and see their responses.

Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

License

This project is open source and available under the MIT License.