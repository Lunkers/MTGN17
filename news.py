import app.db_interface as interface

    

def get_news(id):
    try:
        news = interface.get_news(id)
        return news
    except:
        return "Problem"


def save_to_db(news_dict):
    try:
        interface.add_news(news_dict)
    except:
        return "Problem"

def delete_news(id):
    try:
        interface.delete_news(id)
        return True
    except:
        return False

def edit_news(id, dict):
    try:
        interface.edit_news(id, dict)
        return True
    except:
        return False