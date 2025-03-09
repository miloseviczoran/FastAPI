# 📝 FastAPI Todo App

A full-stack **Todo App** built using **FastAPI**, **JavaScript**, **Python**, and **PostgreSQL**. The application is deployed on **Render** and managed using **GitHub**.

🚀 Features

- ✅ Create, update, delete tasks
- 📌 Mark tasks as completed
- 🔍 Fetch tasks using API endpoints
- 🗄️ PostgreSQL database for persistent storage
- 🌐 FastAPI backend with an interactive API
- 💻 JavaScript frontend for a smooth user experience

🏗️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** JavaScript (Vanilla/Framework)
- **Database:** PostgreSQL
- **Deployment:** Render
- **Version Control:** GitHub

📂 Project Structure
FastAPI-TodoApp/ 
│── .git/ # Git version control
│── alembic/ # Database migrations
│── routers/ # API route handlers
│── static/ # Static files (CSS, JS)
│── templates/ # HTML templates
│── test/ # Unit tests
│── database.py # Database connection setup
│── main.py # Main FastAPI application
│── models.py # Database models
│── requirements.txt # Dependencies
│── README.md # Documentation
│── .gitignore # Ignored files for Git
│── todosapp.db # Database file (if using SQLite locally)


## 🛠️ Installation & Setup
Follow these steps to set up and run the project locally:

1️⃣ Clone the Repository  
  bash
  git clone https://github.com/your-username/todo-app.git
  cd todo-app

2️⃣ Create & Activate a Virtual Environment
  # On Windows
  python -m venv venv
  venv\Scripts\activate
  
  # On macOS & Linux
  python3 -m venv venv
  source venv/bin/activate

3️⃣ Install Dependencies
  pip install -r requirements.txt

4️⃣ Set Up Environment Variables
  DATABASE_URL=postgresql://user:password@host:port/dbname

5️⃣ Run Database Migrations
  alembic upgrade head

6️⃣ Start the Application
  uvicorn main:app --reload

7️⃣ Access the API Documentation
Once the server is running, open your browser and go to:
  🔹 Swagger UI: http://127.0.0.1:8000/docs
  🔹 ReDoc: http://127.0.0.1:8000/redoc


🌍 Live Demo
🚀 Check out the live version of the app:
🔗 Todo App on Render: https://zoran-deployment-fastapi.onrender.com/

📜 API Endpoints
Method	Endpoint	Description
  GET	/tasks	            Get all tasks
  POST	/tasks	          Create a new task
  GET	/tasks/{id}	        Get a single task
  PUT	/tasks/{id}	        Update a task
  DELETE	/tasks/{id}	    Delete a task

🧪 Running Tests
pytest

📜 License
This project is licensed under the MIT License.
