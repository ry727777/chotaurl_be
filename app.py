from flask import Flask, request, jsonify, redirect
from supabase_py import create_client
from flask_cors import CORS
from generate_url import short_url, redirect_url

app = Flask(__name__)
CORS(app)

# Initialize Supabase client
supabase_url = 'https://lzekqhtqskrehxglbpmm.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWtxaHRxc2tyZWh4Z2xicG1tIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwODE5NzI4MywiZXhwIjoyMDIzNzczMjgzfQ.TZbUdk8SCGGaoH0T3Lk5-hPpNTDwePhg4jIuTiooyKw'
supabase = create_client(supabase_url, supabase_key)

@app.route('/')
def welcome_to_short_url():
    return "SHORT URL"

@app.route('/shorten', methods=['POST'])
def url_shortening():
    return short_url(request, supabase)

# Route to redirect short URL to original URL
@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
    value = redirect_url(short_url, supabase=supabase)
    if not value:
        return jsonify({'error': 'invalid url'}), 400
    return redirect(value, 301)

if __name__ == '__main__':
    app.run(debug=True)