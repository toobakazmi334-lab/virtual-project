from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Virtual Learning Management System")

# ---------------- DUMMY DATA ----------------
courses = {
    "python": {
        "title": "Python Programming",
        "teacher": "Sir Ali",
        "lessons": ["Variables", "Loops", "Functions", "OOP"]
    },
    "web": {
        "title": "Web Development",
        "teacher": "Miss Sara",
        "lessons": ["HTML", "CSS", "JavaScript", "FastAPI"]
    },
    "ai": {
        "title": "Artificial Intelligence",
        "teacher": "Dr Ahmed",
        "lessons": ["Intro AI", "Machine Learning", "Neural Networks"]
    }
}

students = ["Ayesha", "Ali", "Hamza", "Fatima"]

# ---------------- HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    course_cards = ""
    for key, course in courses.items():
        lessons = "".join(f"<li>{l}</li>" for l in course["lessons"])
        course_cards += f"""
        <div class="card">
            <h2>{course['title']}</h2>
            <p><b>Teacher:</b> {course['teacher']}</p>
            <ul>{lessons}</ul>
        </div>
        """

    students_list = "".join(f"<li>{s}</li>" for s in students)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Virtual LMS</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f6f8;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            .container {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
                justify-content: center;
            }}
            .card {{
                background: white;
                padding: 20px;
                width: 280px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.15);
            }}
            ul {{
                padding-left: 20px;
            }}
            .students {{
                margin-top: 40px;
                background: white;
                padding: 20px;
                border-radius: 10px;
                max-width: 400px;
                margin-left: auto;
                margin-right: auto;
            }}
        </style>
    </head>
    <body>
        <h1>🎓 Virtual Learning Management System</h1>

        <h2 style="text-align:center;">📚 Courses</h2>
        <div class="container">
            {course_cards}
        </div>

        <div class="students">
            <h2>🧑‍🎓 Students</h2>
            <ul>
                {students_list}
            </ul>
        </div>
    </body>
    </html>
    """

# ---------------- API ENDPOINT ----------------
@app.get("/api/courses")
def api_courses():
    return courses
