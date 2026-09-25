from flask import jsonify, request

from ..data import data


def register_routes(app):
    @app.get("/students/stats")
    def get_stats():
        students = data.STUDENTS
        total = len(students)
        if total == 0:
            return jsonify({"total": 0, "averageGrade": 0, "minGrade": None, "maxGrade": None}), 200

        grades = [s["grade"] for s in students]
        return jsonify(
            {
                "total": total,
                "averageGrade": round(sum(grades) / total, 2),
                "minGrade": min(grades),
                "maxGrade": max(grades),
            }
        ), 200

    @app.get("/students/search")
    def search_students():
        q = request.args.get("q", "").strip()
        if not q:
            return jsonify({"error": "Paramètre 'q' requis"}), 400

        found = [
            s for s in data.STUDENTS
            if q.lower() in s["firstName"].lower() or q.lower() in s["lastName"].lower()
        ]
        return jsonify(found), 200

    @app.get("/students")
    def get_all_students():
        return jsonify(data.STUDENTS), 200

    @app.get("/students/<int:student_id>")
    def get_student(student_id):
        student = next((s for s in data.STUDENTS if s["id"] == student_id), None)
        if student is None:
            return jsonify({"error": "Étudiant non trouvé"}), 404
        return jsonify(student), 200

 