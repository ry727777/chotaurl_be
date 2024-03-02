from databaseConn import addUrl, get_long_url
from flask import jsonify

def short_url(request, supabase):
    data = request.get_json()
    if 'longUrl' not in data:
        return jsonify({'error': 'Missing long_url parameter'}), 400
    long_url = data['longUrl']
    if 'http://' in  long_url or  'https://' in long_url:
         short_code = addUrl(long_url, supabase=supabase, table_name='chota_url')
         short_url = f'http://127.0.0.1:5000/{short_code}'
         return jsonify({'short_url': short_url}), 200
    
    return jsonify({'error': 'invalid url'}), 400  

def redirect_url(short_url, supabase):
    value = get_long_url(short_url=short_url, supabase=supabase)
    return value
    
# https://ry727777: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@github.com/ry727777/chota_url_be.git