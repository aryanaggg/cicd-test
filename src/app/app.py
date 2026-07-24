from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Hello CI/CD!"}

@app.get("/health")
def health():
    return {"message": "Healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)