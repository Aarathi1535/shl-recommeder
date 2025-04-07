# Approach for Solving the SHL Recommender API Problem

## Objective:
Create an API that receives a query in the form of text and returns a list of relevant assessments based on matching tags or descriptions.

## 1. Setting Up the Environment:
- **Flask**: Chose **Flask** to quickly set up a web API due to its simplicity and lightweight nature.
- **Python**: Used **Python 3.13** as specified in the project.

## 2. Data Model:
- **Assessments**: A list of assessments, each containing:
  - `id`: Unique identifier for the assessment.
  - `name`: Name of the assessment.
  - `description`: Brief explanation of the assessment.
  - `tags`: Tags associated with the assessment (used for matching queries).

## 3. API Endpoint:
- **Endpoint**: `/recommend`
- **Method**: `GET`
- **Query Parameter**: Accepts a query string via `?query=<text>` in the URL.
- The endpoint matches the query against tags or descriptions and returns the matching assessments in JSON format.

## 4. Recommendation Logic:
- The query is compared to the tags and descriptions of each assessment. If any tag matches or if the query is part of the description, that assessment is recommended.

## 5. Error Handling:
- If no query is provided, a `400 Bad Request` error is returned.
- If no assessments match the query, a message indicating no results is returned.

## 6. Testing:
- The endpoint is tested using **Postman**, **curl**, and a browser.
- Example query: `http://127.0.0.1:5000/recommend?query=leadership`

## 7. Conclusion:
- This solution efficiently matches queries to assessments and returns them in a JSON format.
