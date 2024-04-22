from App.models import Internship
from App.database import db
import csv 


def initialize_internship():  
  with open('App/static/internship.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 
    for row in csv_reader:
      new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
      db.session.add(new_internship)

  try:
    db.session.commit()
  except Exception as e:
    print("An error occurred during commit:", e)

if __name__ == "__main__":
  initialize_database()


def create_project(internship_title,company_name,location,start_date,duration,stiped):
  newproject=Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,duration=duration,stipend=stiped)
  db.session.add(newproject)
  db.session.commit()
  return newproject


