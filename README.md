# ai-requirements-analyzer
AI-Driven Requirements Analyzer &amp; Risk Predictor using Python, Flask, and OpenAI’s GPT-4 for NLP processing.


## Demonstration 

Here’s a small demo project showcasing an AI Talent Matcher using Python, Flask, and Scikit-learn. This prototype will include:

•	A basic Flask API for talent matching

•	A sample dataset (community members with skills and performance history)

•	K-means clustering to group similar talents

•	A recommendation engine to suggest the best team members for a given project


## Folder structure 

 ![image](https://github.com/user-attachments/assets/22e14e77-18b2-4dde-92bc-7276d8582c8b)



## Running the Demo
A. Install Dependencies
> pip install flask pandas scikit-learn

B. Start Flask App
> python main.py

C. Test API with a Sample Request
> curl -X POST "http://127.0.0.1:5000/match" -H "Content-Type: application/json" -d '{"skills": ["Python", "ML"]}'

D. Expected JSON Response
>
{
  "matches": [
    {"name": "Alice", "skills": "Python;ML", "performance": 4.5},
    {"name": "Dave", "skills": "Python;DataScience", "performance": 4.7}
  ]
}


E. Containerization (Dockerfile)

FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

