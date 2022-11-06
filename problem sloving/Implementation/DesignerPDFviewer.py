problem Link:

https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

def designerPdfViewer(h, word):
    height=0
    for letter in word:
        height=max(height,h[ord(letter)-ord("a")])
        
    return height*len(word)     