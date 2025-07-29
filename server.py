from flask import Flask, request, jsonify, send_file
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_request():
    data = request.get_json()
    if not data or "type" not in data:
        return jsonify({"error": "Missing 'type' in request"}), 400

    if data["type"] == 1:
        # Створення PDF у пам'яті
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer)
        c.drawString(100, 750, "Це PDF-файл, згенерований сервером.")
        c.save()
        pdf_buffer.seek(0)
        return send_file(pdf_buffer, as_attachment=True, download_name="file.pdf", mimetype="application/pdf")

    elif data["type"] == 2:
        return jsonify({"type": 2, "message": "JSON response for type 2"})

    else:
        return jsonify({"error": "Invalid 'type' value"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
