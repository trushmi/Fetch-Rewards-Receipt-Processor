# Fetch Rewards Receipt Processor

Fetch Rewards is a popular consumer-engagement platform in the United States with over 17 million active users. The platform allows users to submit digital or scan printed receipts to earn points, which can later be redeemed for free gift cards or other prizes and rewards.

This project aims to develop a web service in alignment with the 'Receipt Processor' task outlined by Fetch Rewards. The service is designed to meet the requirements of the provided API documentation, facilitating the processing of receipts and the calculation of reward points. The original repository for the task can be found
[here](https://github.com/fetch-rewards/receipt-processor-challenge)

## API Specification

Endpoint: Process Receipts

- Path: /receipts/process
- Method: POST
- Payload: Receipt JSON
- Response: JSON containing an id for the receipt.

Example Response:
```
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

Endpoint: Get Points

- Path: /receipts/{id}/points
- Method: GET
- Response: A JSON object containing the number of points awarded.


Example Response:
```
{ "points": 32 }
```

## Rules for getting points

The points are calculated based on the following rules:

1. One point for every alphanumeric character in the retailer name.
1. 50 points if the total is a round dollar amount with no cents.
1. 25 points if the total is a multiple of 0.25.
1. 5 points for every two items on the receipt.
1. If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
1. 6 points if the day in the purchase date is odd.
1. 10 points if the time of purchase is after 2:00pm and before 4:00pm.

## Example
```
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
```

```
Expected result: 28 points
```

## Tech Stack

- **Backend**: Python, Flask
- **Containerization**: Docker

## Structure

- **requirements.txt**: lists all the necessary Python packages and their versions required to run the Flask application.

- **Dockerfile**: defines the setup for a Docker container to host the Flask application.

- **src folder**:

  **server.py**: establishes a Flask web server and defines two routes to process receipts and retrieve points associated with a receipt. It imports necessary functions from utils.py and validations.py to calculate points based on receipt data and validate receipt structures, respectively. The file contains main functionality to receive POST requests at /receipts/process to process new receipts, and GET requests at /receipts/{id}/points to retrieve points associated with a given receipt ID.

  **validations.py** : contains functions to validate the receipt structure and its content, ensuring that the data provided adheres to specified conditions. For example, it checks the type and format of the retailer name, purchase date and time, total amount, and item structure in the receipt. It also defines a ValidationResult class to encapsulate the result of a validation check.

  **utils.py**: contains a collection of functions to calculate points based on different criteria provided in a receipt. Each function takes a receipt dictionary as input and returns points based on certain conditions like the retailer's name, purchase date and time, total amount, and item descriptions among others. The file also contains a main function get_total_receipt_points which aggregates points from all the criteria.

  **test_utils.py**: includes unit tests for the functions defined in utils.py. It uses the unittest framework to define test cases ensuring that the point calculation functions work as expected.

## Setup and Running Instructions

1. Prerequisites:

- Ensure that you have [Docker](https://www.docker.com/) installed on your machine.

2.Build Docker Image:

- Navigate to the project directory where the Dockerfile and requirements.txt are located.
- Run the following command to build the Docker image:

```
docker build -t my-receipts-app .
```

3. Run Docker Container:

- Once the image is built, run the following command to start the container:

```
docker run -d -p 8080:5000 my-receipts-app
```

4. Accessing the Application:

- The application will now be running in a Docker container and is accessible at http://localhost:8080.

- You can now use the defined routes to process receipts and retrieve points.

5. Stop and Remove Docker Container:

- To stop the running container, first find the container ID with the following command:

```
docker ps
```

Then stop the container with:

```
docker stop <container-id>
```

6. Viewing Logs:

- To view the logs for the running container, use the following command:

```
docker logs <container-id>
```

7. Run the tests

- To run the tests within Docker, ensure you have built your Docker image and have a running Docker container.
  You can find the container ID using the following command:

```
docker ps
```

- Use the docker exec command to run the tests in the specified container:

```
docker exec -it <container-id> python -m unittest test_utils.py
```
## Demo
You can use [Postman](https://www.postman.com/) to check and try how endpoints work. Postman is a popular API testing and development tool that allows you to send HTTP requests to endpoints and receive responses.

Example of Endpoints: Get Points and Process Receipts with Postman:

![github](https://github.com/trushmi/Fetch-Rewards-Receipt-Processor/assets/88466266/c0e5e6e1-ec58-4d51-896e-610ed5692c02)

## About Author

My name is Iryna. I am a software engineer with a background in the media industry, leadership, and communications. I recently graduated from the Software Engineering Program at Hackbright Academy, where I honed my skills in full-stack development and fundamental computer science concepts.

My technical expertise lies in object-oriented programming languages, particularly in Python. Additionally, I am well-versed in JavaScript, HTML, CSS, and the React framework, enabling me to create responsive and client-oriented user interfaces. My [LinkedIn](https://www.linkedin.com/in/trushmi/)
