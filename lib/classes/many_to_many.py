class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, '_title'):
            print('title has already been set')
            return
        if not isinstance(new_title, str):
            print('title must be str')
        if not len(new_title) >= 5 and len(new_title) <= 50:
            print('name must be between 5 and 50 characters')
        self._title = new_title
    
    def __repr__(self):
        return f"{self.title} by {self.author} in {self.magazine}"
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            print('name has already been set')
            return 
        if not isinstance(new_name, str):
            print('name must be str')
            return 
        if len(new_name) < 1:
            print('name must be greater than 0 characters')
            return 
        
        self._name = new_name

    def articles(self):
        total_articles = []
        for article in Article.all:
            if article.author is self:
                total_articles.append(article)
        return total_articles
            
    def magazines(self):
        magazine_contributions = []
        for article in self.articles():
            magazine_contributions.append(article.magazine)
        return list(set(magazine_contributions))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

    def __repr__(self):
        return f"{self.name}"

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (len(new_name) >= 2 and len(new_name) <= 16):
            self._name = new_name
        else:
            print('name error')
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and (len(new_category) > 0):
            self._category = new_category
        else:
            print('category error')

    def articles(self):
        total_articles = []
        for article in Article.all:
            if article.magazine is self:
                total_articles.append(article)
        return total_articles

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

    def __repr__(self):
        return f"Magazine: {self.name} | Category: {self.category}"

eliza = Author('Eliza Cohen')
vanity_fair = Magazine('Vanity Fair', 'Lifestyle')
a1 = Article(eliza, vanity_fair, 'How to care for a chi')
time = Magazine('Time', 'Events')
a2 = Article(eliza, time, 'A Chis Rise to Fame')

pistachio = Author('Pistachio')
a3 = Article(pistachio, vanity_fair, 'Y2K Fashion from a Chis Perspective')
a4 = Article(pistachio, time, 'Chi: Dog of the Century')

print(time.articles())