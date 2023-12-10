from flask import Flask, render_template, url_for


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        current_user = {
            "firstname": "John",
            "lastname": "Doe",
            "avatar_url": url_for("static", filename="profiles/john.png"),
            "is_current_user": True,
            "age": 53,
            "favourite holiday": "Beach",
            "favourite season": "Autumn",
            "favourite food": "Pasta",
        }

        matched_user = {
            "firstname": "Mary",
            "lastname": "Jane",
            "avatar_url": url_for("static", filename="profiles/mary.png"),
            "is_current_user": False,
            "age": 56,
            "favourite holiday": "Beach",
            "favourite season": "Spring",
            "favourite food": "Pizza",
        }

        displayed_fields = [
            "age",
            "favourite holiday",
            "favourite season",
            "favourite food",
        ]

        return render_template(
            "index.html",
            current_user=current_user,
            matched_user=matched_user,
            fields=displayed_fields,
        )

    return app
