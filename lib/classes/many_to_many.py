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
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = []

        for magazine in self.magazines():
            topic_areas.append(magazine.category)
            
        if topic_areas == []:
            return None
        
        return topic_areas

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
        all_contributors = []
        for article in self.articles():
            all_contributors.append(article.author)
        return list(set(all_contributors))

    def article_titles(self):
        article_titles = []

        for article in self.articles():
            article_titles.append(article.title)
        
        if article_titles == []:
            return None

        return article_titles

    def total_contributing_authors(self):
        authors_for_all_articles = []
        for article in self.articles():
            authors_for_all_articles.append(article.author)
        authors_count = { author:authors_for_all_articles.count(author) for author in authors_for_all_articles }
        return authors_count

    
    def contributing_authors(self):
        top_contributors = []
        for author, count in self.total_contributing_authors().items():
            if count > 2:
                top_contributors.append(author)
        if len(top_contributors) == 0:
            return None
            
        return top_contributors



    def __repr__(self):
        return f"Magazine: {self.name} | Category: {self.category}"