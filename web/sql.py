    @app.route('/api/login' )
    def login():
    
        login = request.args.get("l")
        with connect(host=host,user=user,password=pa,database=db) as connection:
                select_movies_query = "SELECT * FROM user WHERE login = '" + login + "'"
    
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    result = cursor.fetchall()
                    for row in result:
                         print(row)
