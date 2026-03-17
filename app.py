from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    summary = None
    image = None
    title = None

    if request.method == "POST":
        name = request.form["name"]
        try:
            results = wikipedia.search(name)
            if results:
                page = wikipedia.page(results[0])
                summary = page.summary
                title = page.title

                if page.images:
                    image = page.images[0]

        except:
            summary = "Person not found"

    return render_template("index.html", summary=summary, image=image, title=title)

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)


