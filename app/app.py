import os
from flask import Flask, render_template_string, request

app = Flask(__name__)
FILE_PATH = "counter.txt"

# Ensure the file exists right when the app starts
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        f.write("0")

def read_counter():
    with open(FILE_PATH, "r") as f:
        return int(f.read().strip())

def write_counter(count):
    with open(FILE_PATH, "w") as f:
        f.write(str(count))

@app.route("/", methods=["GET", "POST"])
def index():
    # 1. Check for the click event (POST request)
    if request.method == "POST":
        current_count = read_counter()
        # 2. Update the variable
        new_count = current_count + 1
        write_counter(new_count)
    else:
        new_count = read_counter()

    # 3. Send the updated count back to the browser
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Click Counter</title></head>
    <body style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1>Click Counter: {{ count }}</h1>
        <form method="post">
            <button type="submit" style="font-size: 20px; padding: 10px 20px; cursor: pointer;">Click Me!</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(html, count=new_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
