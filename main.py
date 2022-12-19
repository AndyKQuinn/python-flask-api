#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os
import app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    my_app = app.create_app()
    my_app.run(host="0.0.0.0", port=port)
