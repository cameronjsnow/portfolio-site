from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
        
            
    return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data.decode('utf-8'))
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@views.route('/portfolio')
@login_required
def portfolio():
    projects = [
        {
            "title": "Stock Data Visualization Tool",
            "description": "A web-based tool using Python, Flask, and Pygal for visualizing stock data.",
            "technologies": ["Python", "Flask", "HTML", "Docker"],
            "link": "https://github.com/yourusername/stock-visualizer"
        },
        # Add more projects as needed
    ]
    return render_template("portfolio.html", user=current_user, projects=projects)

@views.route('/game')
@login_required
def game():
    return render_template("game.html", user=current_user)

@views.route('/writing')
@login_required
def writing():
    return render_template("writing.html", user=current_user)