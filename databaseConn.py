import string
import random

# generate uuid
def generate_unique_alphanumeric(length=8):
    characters = string.ascii_letters + string.digits  # Alphanumeric characters (both lowercase and uppercase)
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id

# check if key is in db
def check_key_in_db(key_value, table_name, supabase, column_name):
    print("checking long in DB")
    response = supabase.from_(table_name).select(column_name).eq(column_name, key_value).execute()
    return len(response.get('data')) > 0

# get short key for given url
def get_short_url_from_db(long_url, table_name, supabase, column_name):
    response = supabase.from_(table_name).select('id').eq(column_name, long_url).execute()
    data = response.get('data')
    return data[0]['id']

# get long url from db for given short url
def get_long_url_from_db(data_value, table_name, supabase, column_name):
    response = supabase.from_(table_name).select(column_name).eq('id', data_value).execute()
    return response.get('data')[0]['long_url']

# add url to db
def addUrl(long_url, supabase, table_name):
    shortUrl = None
    # check if long url is already there
    check_url = check_key_in_db(long_url, table_name, supabase, 'long_url')
    print(check_url)
    if check_url:
        # return existing short url
        print("already exit return same shorted url")
        return get_short_url_from_db(long_url, table_name, supabase, 'long_url')

    # create key and map it with long url
    while True:
        key = generate_unique_alphanumeric()
        key_check = check_key_in_db(key, table_name, supabase, 'id')
        if not key_check:
            # insert in db
            data = [{'id': key, 'long_url': long_url}]
            supabase.table(table_name).insert(data).execute()
            break
    return key

# get long url for given short url
def get_long_url(short_url, supabase):
    # check if short url is present
    value = check_key_in_db(key_value=short_url, supabase=supabase, table_name='chota_url', column_name='id')
    # print(value)
    if value:
        # get long url
        long_url = get_long_url_from_db(data_value=short_url, table_name='chota_url', supabase=supabase, column_name='long_url')
        # print(long_url)
        return long_url
    return False