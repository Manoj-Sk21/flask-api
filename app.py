from flask import Flask, jsonify
app=Flask(__name__)
fake_jobs_db = [
    {
        "id": 1,
        "title": "Python Developer Intern",
        "company": "Tech Startup Inc.",
        "location": "Bangalore"
    },
    {
        "id": 2,
        "title": "Data Analyst Trainee",
        "company": "Data Insights",
        "location": "Bangalore"
    },
    {
        "id": 3,
        "title": "Backend Intern (Python)",
        "company": "Future Systems",
        "location": "Bangalore"
    }
]
@app.route('/api/jobs')
def get_job():
    return jsonify(fake_jobs_db)
if __name__ == '__main__':
    app.run(debug=True,port=5001)