from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for attendance records
attendance_records = {}


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    session_id = request.form['session_id']
    student_name = request.form['student_name']

    if session_id not in attendance_records:
        attendance_records[session_id] = set()

    attendance_records[session_id].add(student_name)

    return redirect(url_for('index'))


@app.route('/view_attendance')
def view_attendance():
    return render_template('attendance.html', attendance_records=attendance_records)


if __name__ == '__main__':
    app.run(debug=True)
