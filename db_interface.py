import pymysql



conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="mysql", autocommit= True) 
conn.autocommit(True)
cursor = conn.cursor()

#hämta nyheter; antigen specifikt id eller alla
def get_news(id):
    if id is not None:

        sql = "SELECT * FROM mtgn18.news WHERE id = %s" 
        cursor.execute(sql, id)
        result = cursor.fetchone()
        j_dict = {"id":result[0], "author":result[1], "headline":result[2], "text":result[3], "tags":result[4]}
            
        return j_dict
    else:
        sql = "SELECT * FROM mtgn18.news WHERE 'id' IS NOT NULL ORDER BY id DESC"
        cursor.execute(sql, id)
        result = cursor.fetchall()


        news_list = []
        for row in result:
            j_dict = {"id":row[0], "author":row[1], "headline":row[2], "text":row[3], "tags":row[4]}
            news_list.append(j_dict)
            
        return news_list

#spara ny nyhet i DB
def add_news(dict):
        sql = "INSERT INTO mtgn18.news (author, headline, text, tags) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (dict["author"], dict["headline"], dict["text"], dict["tags"]))
        

#radera entry från DB (försvinner för alltid!)
def delete_news(id):
    sql = "DELETE from mtgn18.news WHERE id = %s"
    cursor.execute(sql, id)

#uppdatera entry i databas (edit)
def edit_news(id, dict):
    sql = "UPDATE mtgn18.news SET (author, headline, text, tags) = (%s, %s, %s, %s) WHERE id = %s "
    cursor.execute(sql, (dict["author"], dict["headline"], dict["text"], dict["tags"], id))