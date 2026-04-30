import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from routes.describe import describe_bp
from routes.recommend import recommend_bp

load_dotenv()

app = Flask(__name__)

# Register blueprints
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "service": "Tool-134 AI Service",
        "version": "1.0.0",
        "port": os.getenv("FLASK_PORT", "5000")
    }), 200


if __name__ == '__main__':
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_ENV", "development") == "development"
    print("")
    print("  Tool-134 AI Service starting...")
    print(f"  Running on http://localhost:{port}")
    print(f"  Health check:  http://localhost:{port}/health")
    print(f"  Describe:      http://localhost:{port}/describe")
    print(f"  Recommend:     http://localhost:{port}/recommend")
    print("")
    app.run(host='0.0.0.0', port=port, debug=debug)