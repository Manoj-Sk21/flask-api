import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location=db.Column(db.string(100),nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location':self.location
        }
with app.app_context():
    db.create_all()
    if not Job.query.first():
        starter_job1= Job(title='Software Engineer', company='Tech Corp',location='Remote')
        starter_job2= Job(title='Data Scientist', company='Data Inc',location='New York')
        db.session.add(starter_job1)
        db.session.add(starter_job2)
        db.session.commit()
@app.route('/api/jobs')
def get_job():
    all_jobs = Job.query.all()
    jobs_list = [job.to_dict() for job in all_jobs]
    return jsonify(jobs_list)
if __name__ == '__main__':
    app.run(debug=True,port=5001)