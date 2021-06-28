from typing import Any, List, Optional

def printTop(maxChar: int) -> str:
    spacer = maxChar + 2
    top = "┌"+"─"*spacer+"┐"
    print(top)
    return top

def printRow(row: List, maxChar: int) -> str:
    vert = "│"
    fmtRow = ""
    for item in row:
        fmtItem = f"{vert} {item} {vert:>{maxChar-len(item)+1}}"
        fmtRow += fmtItem
    print(fmtRow)
    return fmtRow 

def printBottom(maxChar: int) -> str:
    spacer = maxChar + 2
    bottom = "└"+"─"*spacer+"┘"
    print(bottom)
    return bottom

def getLongestRow(rows: List[List[Any]]) -> int:
    longestRow = 0
    for row in rows:
        rowLen = 0
        for item in row:
            itemLen = len(str(item))
            rowLen += itemLen
        #print(rowLen)
        if rowLen > longestRow:
            longestRow = rowLen
    return longestRow

def table(rows: List[List[Any]]):
    maxChars = getLongestRow(rows)
    printTop(maxChars)
    for row in rows:
        printRow(row, maxChars)
    printBottom(maxChars)

rows1=[
        ["Lemon"],
        ["Sebastiaan"],
        ["KutieKatj9"],
        ["Jake"],
        ["Not Joe"]
    ]

#table(rows1)


rows2 = [
    ["joe", "ben", "mo"],
    ["joannie", "britt", "joey"],
    ["maria", "erin", "sam"],
    ["eve", "marley", "delly"]
]


table(rows2)

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    

