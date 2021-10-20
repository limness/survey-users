# Survey API

## Request & Response

### API Resources

  - [GET /api/active_polls/](#get-magazines)
  - [GET /api/answers_polls/](#get-magazinesid)
  - [POST /add_answer/](#post-magazinesidarticles)

### GET /api/active_polls/

    curl -G "http://localhost:8000/api/active_polls/"
    
Response body:

    [
      {
          "id": 1,
          "poll_name": "SpaceX и BlueOrigin",
          "description": "Выбираем лучшую космическую корпорацию",
          "questions": [
              {
                  "id": 31,
                  "question_type": "own_asnwer",
                  "question_text": "В каком году был запущен SN10?",
                  "poll": 1
              },
              {
                  "id": 32,
                  "question_type": "own_asnwer",
                  "question_text": "Starlink это...",
                  "poll": 1
              }
          ],
          "data_begin": "2021-10-19",
          "data_end": "2021-10-29"
      },
      {
          "id": 2,
          "poll_name": "Что такое ИИ",
          "description": "sfs",
          "questions": [
              {
                  "id": 36,
                  "question_type": "own_asnwer",
                  "question_text": "Перцептрон это...",
                  "poll": 2
              },
              {
                  "id": 37,
                  "question_type": "own_asnwer",
                  "question_text": "Для чего служит тензор?",
                  "poll": 2
              }
          ],
          "data_begin": "2021-10-19",
          "data_end": "2021-10-29"
      }
    ]

### GET /api/answers_polls/

    curl -G "http://localhost:8000/api/active_polls/" -d "user_id=347"
    
Response body:

    [
        {
            "id": 40,
            "user_id": 347,
            "answer_id": "1",
            "answer_text": "Спутниковая система интернета",
            "question_detail": {
                "id": 32,
                "question_type": "own_asnwer",
                "question_text": "Starlink это...",
                "poll": 1
            },
            "question_poll": 32
        },
        {
            "id": 41,
            "user_id": 347,
            "answer_id": "1",
            "answer_text": "Что-то иное..",
            "question_detail": {
                "id": 32,
                "question_type": "own_asnwer",
                "question_text": "Starlink это...",
                "poll": 1
            },
            "question_poll": 32
        }
     ]



### POST /add_answer/

    curl "http://localhost:8000/api/add_answer/" -d "user_id=347&question_id=32&answer_id=1&answer_text='pananie'"

Request body:

    [
        {
            "id": 45,
            "user_id": 347,
            "answer_id": "1",
            "answer_text": "2020",
            "question_detail": {
                "id": 31,
                "question_type": "own_asnwer",
                "question_text": "В каком году был запущен SN10?",
                "poll": 1
            },
            "question_poll": 32
        }
    ]



## Error handling

Error responses

    {
      "status" : "error",
      "data": "An error occurred during serialization of current polls"
    }

    {
      "status" : "error",
      "data" : "No answers were found for this ID"
    }
    
    {
      "status" : "error",
      "data" : "No answers were found for this ID"
    }
    
    {
      "status" : "error",
      "data" : "Invalid Question ID"
    }

* 200 - OK
* 201 - HTTP_201_CREATED
* 400 - Bad Request
