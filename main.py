import crawler
import os, argparse

year = 108
path, dirs, files = next(os.walk("./html/{year}/".format(year=year)))

if __name__ == "__main__":
    file_count = len(files)
    for i in range(1, file_count):
        url = 'file:///Users/zhe/Documents/vscode/crawler/html/{year}/nsysu_{no}.html'.format(year=year, no=i)
        title, df = crawler.get_table_element(url)
        # export to CSV ----------------------------------- #
        df.to_csv('./csv/{year}/{title}.csv'.format(year=year, title=title), index=False, encoding='utf-8-sig')