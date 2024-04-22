from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from App.models import db
from App.models import Internship
from App.controllers import create_user
from App.controllers import create_project
from App.controllers import initialize_internship

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# @index_views.route('/', methods=['GET'])
@index_views.route('/home', methods=['GET'])
def index_page():
  search_query = request.args.get('search_query')
  page = request.args.get('page', 1, type=int)
  if search_query:
    internships = Internship.query.filter(Internship.internship_title.like("%" + search_query + "%") | Internship.company_name.like("%" + search_query + "%"))
  else:
    internships = Internship.query  # Get all internships if no search term
  paged_internship = internships.paginate(page=page, per_page=10)
  return render_template('index.html', paged_internship=paged_internship, page=page, search_query=search_query)


@index_views.route('/init', methods=['GET'])
def init():
  db.drop_all()
  db.create_all()
  create_user('bob', 'bobpass')
  initialize_internship()
  return jsonify(message='db initialized!')

@index_views.route('/company', methods=['GET'])
def company_page():
  return render_template('company.html', title="Companies Application")


# @index_views.route('/company', methods=['POST'])
# def create_project_action():
#     data = request.form
#     flash(f"Project {data['internship_title']} created!")
#     create_project(data['internship_title'], data['company_name'],
#     data['location'] ,data['start_date'], data['duration'], data['stipend'])
#     return redirect(url_for('index_views.company_page'))



@index_views.route('/', methods=['GET'])
def home_page():
  return render_template('homey.html', title="Home Page")



# @index_views.route('/search', methods=['GET'])
# def search_internships():
#   page = request.args.get('page', 1, type=int)
#   search_query = request.args.get('search_query')
#   search_term = request.args.get('search')
#   if search_term:
#     internships = Internship.query.filter(
#       Internship.internship_title.like(f'%{search_term}%') |
#       Internship.company_name.like(f'%{search_term}%')
#     )
#   else:
#     internships = Internship.query  # Get all internships if no search term
#     paged_internship = internships.paginate(page=page, per_page=10)
#     return render_template('index.html', paged_internship=paged_internship, page=page)
#   paged_internship = internships.paginate(page=page, per_page=10)
#
#   return render_template('search.html', internships=internships.all(), paged_internship=paged_internship, page=page, search_query=search_query)
