# requirments
- Pillow
- tesseract
- lxml
- pandas

1. download python3 : https://www.python.org/downloads/
2. open terminal, and install manually
    ```
    $ pip install Pillow
    $ pip install tesseract
    $ pip install lxml
    $ pip install pandas
    ```
    or install from requrements.txt
    ```
    $ pip install -r requirements.txt
    ```

# how to run
1. you need to manual collect the html file -> save to "./html" folder -> named as "nsysu_{i}.html"
    ```
    ./html
    |_  nsysu_1.html
    |_  nsysu_2.html
    |_  nsysu_3.html
    |_       ...
    ```
2. excute main.py by command line
    ```
    # open the terminal
    $ python main.py
    ```

3. The decoder in it will take more time to extract IMAGE to TEXT (for full identifications)

# result
1. crawled dataframe will be saved to "./csv/{department_name_#ofpeople}.csv"
    ```
    ./csv
    |_  人文暨科技跨領域學士學位學程41人.html
    |_  中國文學系58人.html
    |_  化學系58人.html
    |_       ...
    ```