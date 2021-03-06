from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./swagger/')

# Read the swagger.yml file to configure the endpoints
app.add_api('app.yaml')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)