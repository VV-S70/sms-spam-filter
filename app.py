import os
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Loading dataset and training the model
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"
df = pd.read_csv(url, sep="\t", header=None, names=["label", "message"])

df["label_num"] = df.label.map({"ham": 0, "spam": 1})
X = df["message"]
y = df["label_num"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)

clf = MultinomialNB()
clf.fit(X_train_dtm, y_train)

from flask import send_from_directory

@app.route('/logo.png')
def logo():
    return send_from_directory(os.getcwd(), 'logo.png')
  
@app.route("/")
def home():
  return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
  if request.method == "POST":
    message = request.form["message"]
    data = [message]
    vect_data = vect.transform(data)
    my_prediction = clf.predict(vect_data)

    result = "SPAM 🚨" if my_prediction[0] == 1 else "NOT SPAM (Safe) ✅"
    return render_template(
        "index.html", prediction=result, original_text=message
    )


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
