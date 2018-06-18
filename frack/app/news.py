import app.db_interface

    

def get_news(id):
    return app.db_interface.get_news(id)


def save_to_db(news_dict):
    succ = app.db_interface.add_news(news_dict)
    if succ:
        return True 
    else:
         return False