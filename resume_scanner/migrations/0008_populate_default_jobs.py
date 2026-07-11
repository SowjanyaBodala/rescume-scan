from django.db import migrations

def populate_jobs(apps, schema_editor):
    Job = apps.get_model('resume_scanner', 'Job')
    default_jobs = [
        {
            "title": "Software Developer Intern",
            "description": "We are hiring a Software Developer Intern. Required skills: Python, Django, REST APIs, HTML, CSS, JavaScript, Git, and basic database knowledge."
        },
        {
            "title": "Data Analyst",
            "description": "We are looking for a Data Analyst. Required skills: SQL, Python, Excel, Pandas, Numpy, Tableau/PowerBI, statistics, and data visualization."
        },
        {
            "title": "ML Engineer",
            "description": "We are hiring a Machine Learning Engineer. Required skills: Python, Scikit-learn, TensorFlow/PyTorch, NumPy, SciPy, statistics, linear algebra, and data preprocessing."
        },
        {
            "title": "Frontend Developer",
            "description": "We are hiring a Frontend Developer. Required skills: HTML, CSS, JavaScript, React/Vue/Angular, responsive design, and UI/UX basics."
        },
        {
            "title": "Backend Engineer",
            "description": "We are looking for a Backend Engineer. Required skills: Python, Django/Flask, RESTful APIs, PostgreSQL/MySQL, system architecture, caching, and server management."
        }
    ]
    for job_data in default_jobs:
        if not Job.objects.filter(title=job_data["title"]).exists():
            Job.objects.create(title=job_data["title"], description=job_data["description"])

def remove_jobs(apps, schema_editor):
    Job = apps.get_model('resume_scanner', 'Job')
    Job.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('resume_scanner', '0007_alter_applicant_skill_gap'),
    ]

    operations = [
        migrations.RunPython(populate_jobs, reverse_code=remove_jobs),
    ]
