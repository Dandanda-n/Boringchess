from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello Form</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
    {% if name %}
        <h2>Hello, {{ name }}!</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def hello_form():
    name = None
    if request.method == 'POST':
        # Get the name from the form
        name = request.form.get('name')
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(debug=True)
