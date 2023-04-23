# Entity extraction for Chinese News

## Objective

Build an API that can extract entities (person, location, organization) from Online Chinese news paragraphs

## API contract

- **GET /home**
Returns string "Hello World!"
    - Input: None
    - Output: "Hello World!"

- **POST /predict_entity**
Given text input, extracts all entities including entity type and confidence score
    - Input: {"text": <input_string>}
    - Output: {"entities": [[<entity_text>, <entity_type>, <confidence_score>]]}
    - Example:
        ```
        Input: {"text": "陈俊勇本月底将到印度尼西亚旅游，加上从未确诊，因此决定继续戴口罩"}
        Output: {"entities": [["本月","DATE","0.5319928"],["陈俊勇","PERSON","0.9998766"]]}
        ```
## Exposed API

The API is accessible via https://chinese-news-ner.onrender.com at the various endpoints mentioned in the API contract above

## Running the API on your local

1. Clone this repository

	`git clone https://github.com/quissuiven/ner-chinese-news.git`


2. Build and run Docker Image

	```
	cd ner-chinese-news
	docker build -f Dockerfile -t qui-app .
	docker run --name flask1 -d --publish 5000:5000 qui-app
	```

3. Test the API by making a call to http://localhost:5000/ at the various endpoints mentioned in the API contract above

