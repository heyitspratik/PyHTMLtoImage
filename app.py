from flask import Flask, Response, render_template
import imgkit

app = Flask(__name__)

@app.route('/convert_certificate')
def convert_certificate():
    context = {
        'name': 'Jack Sparrow',
        'course': 'Python Programming',
        'date': '08/08/2023 5:18PM'
    }
    
    html_content = render_template('participation_certificate.html', **context)
    image_bytes = convert_html_to_image(html_content)
    
    return Response(image_bytes, content_type='image/png')

def convert_html_to_image(html_content):
    options = {
        'quiet': '',
        'encoding': 'UTF-8'
    }
    
    return imgkit.from_string(html_content, False, options=options)

if __name__ == '__main__':
    app.run(debug=True)
