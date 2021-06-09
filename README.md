# Trivia API
Trivia API is a web application that relies on a REST API, which facilitates a user to perform the following functions:

1) View questions - both all questions and by category. Questions should display the question, category, and difficulty level. As for the answer, it can be show / hide.
2) Delete the questions.
3) Add questions and require them to include question content and an answer.
4) Search questions based on a string or a portion of text.
5) Play the question-answer game in random choice of question, in a specific category or in all the questions available in all categories.

## Getting Started

### Installing Dependencies

#### Python 3.8
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### PIP Dependencies
navigate to the ``/backend`` directory and run:

```sh
pip install -r requirements.txt
```

This will install all of the required packages in the ``requirements.txt`` file.

#### Virtual Enviornment
Working within a virtual environment is recommended.

#### Key Dependencies
[Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

[SQLAlchemy](https://www.sqlalchemy.org/)' is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```sh
psql trivia < trivia.psql
```

## Running the server
From within the ``/backend`` directory

To run the server, execute:

For ***Mac*** :
```sh
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

For ***Windows*** :
```sh
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

## Testing
To run the tests, run :
```sh
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## Frontend Dependencies
This project uses NPM to manage software dependencies. from the frontend directory run :
```sh
npm install
```
> _**tip**_: `npm i` is shorthand for npm install

## Running the Frontend in Developement mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open `http://127.0.0.1:3000` to view it in the browser. The page will reload if you make edits.
```sh
npm start
```

## API Reference

### Getting Started

* Backend Base URL: `http://127.0.0.1:5000/`
* Frontend Base URL: `http://127.0.0.1:3000/`
* Authentication: Authentication or API keys are not used in the project yet.

## Error Handling

Errors are returned in the following json format:

```
      {
        "success": False,
        "error": 404,
        "message": "resource not found"
      }
```

The error codes currently returned are:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 – internal server error

## Endpoints

#### GET /categories

- General: Returns all the categories.
- Sample: `curl http://127.0.0.1:5000/categories`
```json
        {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "success": true
        }
```

#### GET /questions

* General:
  * Returns a list questions.
  * Results are paginated in groups of 10.
  * Also returns list of categories and total number of questions.
* Sample: `curl http://127.0.0.1:5000/questions`
```json
        {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "current_catagory": null, 
        "questions": [
            {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 1, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            }, 
            {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 2, 
            "question": "What boxer's original name is Cassius Clay?"
            }, 
            {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 3, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }, 
            {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            }, 
            {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 5, 
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            }, 
            {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 6, 
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 7, 
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }, 
            {
            "answer": "George Washington Carver", 
            "category": 4, 
            "difficulty": 2, 
            "id": 8, 
            "question": "Who invented Peanut Butter?"
            }, 
            {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 9, 
            "question": "What is the largest lake in Africa?"
            }, 
            {
            "answer": "The Palace of Versailles", 
            "category": 3, 
            "difficulty": 3, 
            "id": 10, 
            "question": "In which royal palace would you find the Hall of Mirrors?"
            }
        ], 
        "success": true, 
        "total_questions": 19
        }
```

#### POST /questions

* General:
  * Creates a new question using JSON request parameters.
  * Returns JSON object with newly created question id.
* Sample: 
    * For ***Mac*** : `curl -X POST http://127.0.0.1:5000/questions/create -H 'Content-Type: application/json' -d '{"question":"Macintosh an Operating System is a product of ?","answer":"Apple","category":1,"difficulty":1}'`
    ```json
            {
            "answer": "Apple",
            "category": "1",
            "difficulty": "1",
            "message": "Question successfully created!",
            "question": "Macintosh an Operating System is a product of ?",
            "questions": {
            "answer": "Apple",
            "category": 1,
            "difficulty": 1,
            "id": 27,
            "question": "Macintosh an Operating System is a product of ?"
            },
            "success": true
            }
    ```

    * For ***Windows*** : `curl -X POST http://127.0.0.1:5000/questions --data "{\"question\":\"Macintosh an Operating System is a product of ?\",\"answer\":\"Apple\",\"category\":\"1\",\"difficulty\":\"1\"}" -H "Content-Type: application/json"`
    ```json   
            {
            "answer": "Apple",
            "category": "1",
            "difficulty": "1",
            "message": "Question successfully created!",
            "question": "Macintosh an Operating System is a product of ?",
            "questions": {
            "answer": "Apple",
            "category": 1,
            "difficulty": 1,
            "id": 27,
            "question": "Macintosh an Operating System is a product of ?"
            },
            "success": true
            }
    ```

#### DELETE /questions/<int:id\>
  
* General:
  * Deletes a question by id using url parameters.
  * Returns id of deleted question upon success.
* Sample: `curl http://127.0.0.1:5000/questions/24`
```json        
        {
        "message": "Question successfuly deleted", 
        "question": "24",
        "success": true
        }
```

#### POST /questions/search

* General:
  * Searches for questions using search term in JSON request parameters.
  * Returns JSON object with matching questions.
* Sample: 
    * for **Mac** : `curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "africa"}'`
    ```json
            {
            "current_category": null,
            "questions": [
                    {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                    }
            ],
            "success": true,
            "total_questions": 1
            }
    ```

    * for **Windows** : `curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" --data "{\"searchTerm\": \"africa\"}"`
    ```json        
            {
            "current_category": null,
            "questions": [
                    {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                    }
            ],
            "success": true,
            "total_questions": 1
            }
    ```

#### GET /categories/<int:id\>/questions

* General:
  * Gets questions by category id using url parameters.
  * Returns JSON object with paginated matching questions.
* Sample: `curl localhost:5000/categories/6/questions`
```json  
        {
        "current_category": "Sports",
        "questions": [
            {                      
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }
            ],
        "success": true,
        "total_questions": 2
        }
```

#### POST /quizzes

* General:
  * Allows users to play the quiz game.
  * Uses JSON request parameters of category and previous questions.
  * Returns JSON object with random question not among previous questions.
* Sample: 
    * For **Mac** :
    `curl -X POST localhost:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [2, 4],"quiz_category": {"type": "Art", "id": 2}}'`
      ```json  
            {
            "question": {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
                },
            "success": true
            }  
      ```        
    * For **Windows** : `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" --data "{\"previous_questions\": [2, 4], \"quiz_category\": {\"type\": \"Art\", \"id\": \"2\"}}"`
      ```json  
            {
            "question": {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
                },
            "success": true
            }   
      ```         
    
## Authors
Amar Guessas worked on the development of the API and the performance of the tests on the frontend thereafter.

## Acknowledgements
Udacity provided the starter files for the project including the frontend.