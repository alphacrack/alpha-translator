from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Set up AWS credentials
session = boto3.Session(
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='eu-west-1'  # Replace with your desired region
)

# Create an AWS Translate client
translate = session.client('translate')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    source_language_code = request.form['source_language']
    target_language_code = request.form['target_language']
    
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
    )
    
    translated_text = response['TranslatedText']
    
    return render_template('result.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
