from app import app

if __name__ == '__main__':
    app.run(app.config['APP_HOST'], app.config['APP_PORT'], threaded=True)
