
from flask import Flask, request, send_file, jsonify
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_request():
    data = request.get_json()
    if not data or "type" not in data:
        return jsonify({"error": "Missing 'type' field"}), 400

    if data["type"] == 1:
        # Створюємо простий PDF-файл у памʼяті
        from reportlab.pdfgen import canvas
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 750, "Це PDF-файл, сформований для type = 1")
        p.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="generated.pdf", mimetype='application/pdf')

    elif data["type"] == 2:
        return jsonify({"type": 2})

    else:
        return jsonify({"error": "Unsupported type"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
