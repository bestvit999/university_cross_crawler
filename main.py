import crawler

if __name__ == "__main__":
    for i in range(1, 44):
        url = 'file:///Users/zhe/Documents/vscode/crawler/html/nsysu_{no}.html'.format(no=i)
        df = crawler.get_table_element(url)