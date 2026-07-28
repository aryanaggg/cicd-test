from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "Hello, We are LIVE!"}


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # raise RuntimeError("simulated production failure")