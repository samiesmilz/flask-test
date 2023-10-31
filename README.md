# Simple Flask Calculator

This is a simple Flask application that provides basic mathematical operations through various API endpoints. It's designed to perform addition, subtraction, multiplication, and division operations. The app also includes a route that allows you to specify the operation as part of the URL.

## Usage

### Installation

Before using this application, make sure you have Flask installed in your Python environment. If Flask is not installed, you can install it using pip:

```bash
pip install Flask
```

### Running the Application

To run the Flask application, execute the following code:

```python
python app.py
```

The application will start, and you can access it through a web browser or by making HTTP requests to the provided routes.

### API Endpoints

- `/add`: Adds two numbers. You can use this endpoint by providing the `a` and `b` query parameters.

- `/sub`: Subtracts one number from another. Use the `a` and `b` query parameters to specify the numbers.

- `/mult`: Multiplies two numbers. Provide the `a` and `b` query parameters.

- `/div`: Divides one number by another. Use the `a` and `b` query parameters.

- `/math/<operation>`: This dynamic route allows you to specify the operation directly in the URL. Use the `a` and `b` query parameters to provide the numbers. Available operations include `add`, `sub`, `mult`, and `div`.

### Example Usage

To add two numbers (e.g., 5 and 3), you can make a request to:

```
http://localhost:5000/add?a=5&b=3
```

Replace `add` with other operation names for different mathematical operations.

## Note

This is a simple Flask calculator and does not include error handling or input validation. It's intended for demonstration and educational purposes. In a production application, you should implement proper input validation and error handling to ensure the reliability and security of the API.
