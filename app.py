from flask import Flask, render_template, request
import ai_service
import history

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/learning")
def learning():
    return render_template("learning.html")


@app.route("/summarize-notes", methods=["GET", "POST"])
def summarize_notes():

    summary = None

    if request.method == "POST":

        notes = request.form.get("notes", "").strip()

        if notes:

            prompt = (
                "Summarize the following study notes in simple bullet points. "
                "Keep the summary short, clear and easy to understand. "
                "Highlight the most important points.\n\n"
                + notes
            )

            summary = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Summary ===\n"
                "Notes:\n"
                + notes
                + "\n\nSummary:\n"
                + summary
            )

    return render_template(
        "summarize.html",
        summary=summary
    )

@app.route("/generate-quiz", methods=["GET", "POST"])
def generate_quiz():

    quiz = None

    if request.method == "POST":

        topic = request.form.get("topic", "").strip()

        if topic:

            prompt = (
                "Create a quiz for the following study topic.\n\n"
                "Generate 5 multiple-choice questions.\n"
                "Each question must have 4 options: A, B, C and D.\n"
                "Clearly mention the correct answer after each question.\n"
                "Keep the questions educational and suitable for students.\n"
                "Topic: "
                + topic
            )

            quiz = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Quiz ===\n"
                "Topic:\n"
                + topic
                + "\n\nQuiz:\n"
                + quiz
            )

        else:
            quiz = "Please enter a topic."

    return render_template(
        "quiz.html",
        quiz=quiz
    )
    
@app.route("/explain-topic", methods=["GET", "POST"])
def explain_topic():

    explanation = None

    if request.method == "POST":

        topic = request.form.get("topic", "").strip()

        if topic:

            prompt = (
                "Explain the following study topic in very simple language "
                "so that a student can understand it easily.\n\n"
                "Use clear headings and numbered points.\n"
                "Include simple examples wherever useful.\n"
                "Avoid unnecessary technical words.\n"
                "Keep the explanation concise and well organized.\n\n"
                "Topic: "
                + topic
            )

            explanation = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Explain Topic ===\n"
                "Topic:\n"
                + topic
                + "\n\nExplanation:\n"
                + explanation
            )

        else:
            explanation = "Please enter a topic."

    return render_template(
        "explain.html",
        explanation=explanation
    )
    
@app.route("/history")
def history_page():

    data = history.get_history()

    return render_template(
        "history.html",
        history=data
    )
@app.route("/clear-history", methods=["POST"])
def clear_history():

    history.clear_history()

    return render_template(
        "history.html",
        history=""
    )
       
    
                    
@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/hr-interview", methods=["GET", "POST"])
def hr_interview():

    interview = None

    if request.method == "POST":

        role = request.form.get("role", "").strip()
        number = request.form.get("number", "").strip()

        if role and number:

            prompt = (
                "Generate "
                + number
                + " HR interview questions for the job role of "
                + role
                + ".\n\n"
                "For each question, provide a sample answer.\n"
                "Keep the answers simple, short and professional.\n"
                "Keep each answer under 100 words."
            )

            interview = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== HR Interview ===\n"
                "Job Role:\n"
                + role
                + "\n\nQuestions and Answers:\n"
                + interview
            )

        else:
            interview = "Please enter the job role and number of questions."

    return render_template(
        "hr_interview.html",
        interview=interview
    )
    
@app.route("/technical-interview", methods=["GET", "POST"])
def technical_interview():

    interview = None

    if request.method == "POST":

        topic = request.form.get("topic", "").strip()
        number = request.form.get("number", "").strip()

        if topic and number:

            prompt = (
                "Generate "
                + number
                + " technical interview questions on "
                + topic
                + ".\n\n"
                "Provide a short and correct answer after each question.\n"
                "Keep the answers simple and suitable for students.\n"
                "Focus on important concepts that are commonly asked in interviews."
            )

            interview = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Technical Interview ===\n"
                "Subject/Technology:\n"
                + topic
                + "\n\nQuestions and Answers:\n"
                + interview
            )

        else:
            interview = "Please enter the subject/technology and number of questions."

    return render_template(
        "technical_interview.html",
        interview=interview
    )
    
@app.route("/resume-review", methods=["GET", "POST"])
def resume_review():

    feedback = None

    if request.method == "POST":

        resume = request.form.get("resume", "").strip()

        if resume:

            prompt = (
                "Review the following resume carefully.\n\n"
                "Identify important mistakes or areas that can be improved.\n"
                "Give 8 to 10 clear and practical suggestions.\n"
                "Focus on skills, education, projects, experience, formatting "
                "and overall presentation.\n"
                "Keep the feedback simple and easy for a student to understand.\n\n"
                "Resume:\n"
                + resume
            )

            feedback = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Resume Review ===\n"
                "Resume:\n"
                + resume
                + "\n\nFeedback:\n"
                + feedback
            )

        else:
            feedback = "Please enter your resume."

    return render_template(
        "resume_review.html",
        feedback=feedback
    )
    
@app.route("/career-guidance", methods=["GET", "POST"])
def career_guidance():

    guidance = None

    if request.method == "POST":

        interest = request.form.get("interest", "").strip()
        education = request.form.get("education", "").strip()

        if interest and education:

            prompt = (
                "Suggest suitable career options based on the following student details.\n\n"
                "Interests: "
                + interest
                + "\n"
                "Education: "
                + education
                + "\n\n"
                "Recommend 5 suitable career options.\n"
                "For each option, provide a short explanation of why it may be suitable.\n"
                "Also mention important skills that the student should learn for each career.\n"
                "Keep the language simple, practical and easy to understand."
            )

            guidance = ai_service.get_ai_response(prompt)

            history.save_history(
                "=== Career Guidance ===\n"
                "Interests:\n"
                + interest
                + "\n\nEducation:\n"
                + education
                + "\n\nCareer Suggestions:\n"
                + guidance
            )

        else:
            guidance = "Please enter your interests and education."

    return render_template(
        "career_guidance.html",
        guidance=guidance
    )
    
                                                            
@app.route("/ask-ai", methods=["GET", "POST"])
def ask_ai():

    answer = None

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if question:

            answer = ai_service.get_ai_response(question)

            history.save_history(
                "=== Ask AI ===\n"
                "Question:\n"
                + question
                + "\n\nAnswer:\n"
                + answer
            )

        else:
            answer = "Please enter a question."

    return render_template(
        "ask_ai.html",
        answer=answer
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)