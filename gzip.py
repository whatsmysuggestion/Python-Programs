import gzip
data="hello welcome"
with gzip.open('demo.txt.gz','wb') as f:
    f.write(data)
    f.close()