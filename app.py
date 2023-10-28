pip install Flask
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
    return render_template('todo.html', tasks=tasks)

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('todo_list'))

if __name__ == '__main__':
    app.run(debug=True)
project_folder/
    app.py
    templates/
        todo.html
<!DOCTYPE html>
<html>
<head>
    <title>Todo List</title>
</head>
<body>
    <h1>Todo List</h1>
    <form method="POST">
        <input type="text" name="task" placeholder="Enter a new task">
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for index, task in enumerate(tasks) %}
            <li>{{ task }} <a href="/delete/{{ index }}">[Delete]</a></li>
        {% endfor %}
    </ul>
</body>
</html>
