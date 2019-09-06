# N-Back
*A CLI game and python module to test working memory*

### Requirements
* python 3

### Installation
```git clone https://github.com/jd-reynolds/n_back```

### Usage
```python3 n_back/n_back.py```
* Random numbers in a given range (default: 0-2) are appended to a list one at a time
* If the number appended occurred n steps back (default: n=3), enter "m" for memory
* Otherwise, enter "n" for no
* For a greater challenge, provide optional arguments for range and length respectively

```python3 n_back/n_back.py 4 5```

