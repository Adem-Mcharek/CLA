from flask import Blueprint, render_template, request, flash, jsonify, send_file
from flask_login import login_required, current_user
from .models import Job
from . import db
import json
import os 
import time
import subprocess
from io import StringIO , BytesIO




views = Blueprint('views', __name__)


# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST': 
#         note = request.form.get('note')#Gets the note from the HTML 

#         if len(note) < 1:
#             flash('Note is too short!', category='error') 
#         else:
#             new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
#             db.session.add(new_note) #adding the note to the database 
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)


#---------------------------------------------------------------
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    # all_jobs = Job.query.order_by(Job.Ratings.desc()).limit(15).all()
    all_jobs = Job.query.order_by(Job.id.desc()).all()
    return render_template('home.html', jobs=all_jobs, user=current_user)

 

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/download/<id>')
def download(id):
    download = Job.query.filter_by(id=id).first()
    return send_file(BytesIO(download.CL), download_name=f"{download.Company}.pdf", as_attachment=True )




# Configure temporary directory (replace with a secure location)
TEMP_DIR = "/tmp/latex_conversion"  # Adjust as needed
os.makedirs(TEMP_DIR, exist_ok=True)  # Create directory if it doesn't exist
 
# @views.route("/convert-to-pdf", methods=["POST"])
# def convert_to_pdf():
#     try:
#         # Receive LaTeX code from the client
#         latex_code = request.data.decode("utf-8")

#         # Generate a unique filename for the LaTeX source and PDF
#         filename_prefix = f"{TEMP_DIR}/{request.remote_addr}_{int(time.time())}"
#         tex_filename = f"{filename_prefix}.tex"
#         pdf_filename = f"{filename_prefix}.pdf"

#         # Write the LaTeX code to a temporary file
#         with open(tex_filename, "w") as f:
#             f.write(latex_code)

#         # Execute the PDF conversion process using a secure subprocess call
#         subprocess.run(["pdflatex", "-halt-on-error", tex_filename], check=True)

#         # Check if the PDF was generated successfully
#         if not os.path.exists(pdf_filename):
#             raise Exception("PDF generation failed")

#         return_type = request.args.get("return_type", "download")  # Handle download or embed request
#         if return_type == "download":
#             return send_file(pdf_filename, mimetype="application/pdf", as_attachment=True)
#         elif return_type == "embed":
#             # Provide the PDF URL for embedding using an iframe tag (consider accessibility and performance)
#             pdf_url = f"/static/{pdf_filename}"
#             return f"<iframe src='{pdf_url}' width='800' height='600'></iframe>"
#         else:
#             return "Invalid return type", 400

#     except Exception as e:
#         # Handle errors gracefully, e.g., log the error and return a user-friendly message
#         print(f"Error during conversion: {e}")
#         return "PDF generation failed. Please try again later.", 500
    


