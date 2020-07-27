import requests
from bs4 import BeautifulSoup

def spider(page=3):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
    }
    num = 0
    # 创建书籍详情List
    DataBase = []   # 总表
    Books= []   # 每一页的分表
    book = []   # 书籍详情
    for i in  range(page+1)[1:]:
        url = 'https://www.qidian.com/rank/yuepiao?style=1&page=' + str(i)
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text,'lxml')
        block = soup.find(class_='book-img-text')
        items = block.find_all('li')
        for item in items:
            # 排序
            num += 1
            book.append(num)
            # 书籍名称
            bookname = item.h4.string
            book.append(bookname)
            author_block = item.find(class_='author').find(class_='name')
            # 作者
            author = author_block.string
            book.append(author)
            # 书籍类型
            Type = ''
            for types in author_block.next_siblings:
                Type += types.string
            book.append(Type)
            # 书籍简介
            introduction = item.find(class_='intro').string
                # 删除简介中的空格
            introduction = ''.join(introduction.split())
            book.append(introduction)
            # 书籍URL
            url = item.h4.a['href']
            book.append(url)
            # 添加正在爬取的页码
            book.append(i+10)

            Books.append(book)
            book = [] # 注意每次都要初始化!

        DataBase.append(Books)
        Books = []   

    return DataBase