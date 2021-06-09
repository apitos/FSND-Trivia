import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  # Implement pagination
  def paginate_questions(request,selection):

    page = request.args.get('page',1,type=int)

    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_questions = [question.format() for question in selection]
    current_questions = formatted_questions[start:end]

    return current_questions, start, end

  # --- endpoint to handle GET requests for categories  
  @app.route('/categories')
  def get_categories():

    categories = Category.query.order_by(Category.id).all()

    if len(categories)==0:
      abort(404)

    return jsonify({
      'success': True,
      'categories': {category.id: category.type for category in categories},
      'total_categories':len(Category.query.all())
      })

  
 # --- endpoint for getting all available questions displaying by 10 questions per page
  @app.route('/questions')
  def get_questions():

    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request,questions)

    if len(current_questions[0])==0:
      abort(404)

    try:
      begin = current_questions[1] + 1 # Start
    
      if (current_questions[2] > len(questions)):
        last = len(questions) 
      else:
        last = current_questions[2]

      # retrieve all categories  
      categories = Category.query.order_by(Category.type).all()

      return jsonify({
        'success': True,
        'categories': {category.id: category.type for category in categories},
        'questions':current_questions[0],
        'total_questions':len(Question.query.all()),
        'showing':"from " + str(begin) + " to " + str(last) + " of " + str(len(Question.query.all())) + " questions"
        })

    except Exception as e:
      print(e)
      abort(422)    

  # --- endpoint to DELETE question using a question ID.
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):

    question = Question.query.filter(Question.id == question_id).one_or_none()

    if question is None:
      abort(404)
    
    try:
      question.delete()
  
      return jsonify({
        'success': True,
        'deleted': question_id,
        'message': 'Question successfuly deleted',
      })

    except Exception as e:
      print(e)
      abort(422)


  # --- endpoint to POST a new question 
  @app.route('/questions', methods=['POST'])
  def create_questions():

    body = request.get_json()

    new_question = body.get('question')
    new_answer = body.get('answer')
    new_category = body.get('category')
    new_difficulty = body.get('difficulty')

    if not new_question or not new_answer or not new_category or not new_difficulty:
      abort(400)

    try:
      question = Question(question=new_question, answer=new_answer, category=new_category,difficulty=new_difficulty)
      question.insert()

      return jsonify({
        'success': True,
        'question': new_question,
        'answer':new_answer,
        'category': new_category,
        'difficulty': new_difficulty,
        'questions': question.format(),
        'message': 'Question successfully created!'
        }), 201

    except Exception as e:
      print(e)
      abort(422)

  # --- search question
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search_term = body.get('searchTerm')
    print("This " + search_term)
    if search_term == '':
      abort(422)  
    try:
      questions_list = Question.query.order_by(Question.id).filter(Question.question.ilike(f'%{search_term}%')).all()
      current_questions = paginate_questions(request, questions_list)
      questions = [question.format() for question in questions_list]

      if len(questions) == 0:
        abort(404)
      
      return jsonify({
        'success': True,
        'questions': current_questions[0],
        'total_questions': len(questions),
        'current_category': None
        }), 200
    except Exception as e:
      print(e)
      abort(404)

  # --- GET endpoint to get questions based on category. 
  @app.route('/categories/<int:id>/questions', methods=['GET'])
  def retrieve_questions_by_category(id):

    # get the category by id
    category = Category.query.filter_by(id=id).one_or_none()

    # abort 400 for bad request if category isn't found
    if (category is None):
      abort(400)

    try:

      questions = Question.query.filter(Question.category == id).all()

      # if available questions in this category
      if (len(questions) == 0):
        abort(404)
      else:
        # --- pagination
        current_questions = paginate_questions(request, questions)

        return jsonify({
          'success': True,
          #'questions': [question.format() for question in questions],
          'questions': current_questions,
          'total_questions': len(questions),
          'current_category': category.type
          })

    except Exception as e:
      print(e)
      abort(422)

 
  """
  test play_quizzes
  """

  @app.route('/quizzes', methods=['POST'])
  def play_quiz():

    try:
      body = request.get_json()

      if not ('quiz_category' in body and 'previous_questions' in body):

        abort(404)

      quiz_category = body.get('quiz_category')

      previousQuestion = body.get('previous_questions')

      if quiz_category['type'] == 'click':
        questions = Question.query.filter(Question.id.notin_(previousQuestion)).all()

      else:
        questions = Question.query.filter_by(
                    category=quiz_category['id']).filter(Question.id.notin_(previousQuestion)).all()

      if len(questions) == 0 :
        abort(404)

      available_questions = []

      format_questions = [question.format() for question in questions]

      for qn in format_questions:
        if qn['id'] not in previousQuestion:
          available_questions.append(qn)

        if len(available_questions) > 0:
          selected_question = random.choice(available_questions)

      return jsonify({
        'success' : True,
        'question' : selected_question
        })

    except Exception as e:
      print(e)
      abort(404)


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  return app