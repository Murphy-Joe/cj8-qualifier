import copy
rows = [
    ["joe", "ben", "mo"],
    ["joannie", "britt", "joey"],
    ["maria", "erin", "sam"],
    ["eve", "marley", "delly"]
]
labels = []
labels = ['First', 'Second', 'Third']
centered = True
#centered = False

#asciis = "│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘"
ul = '┌'
um = '┬'
ur = '┐'
ml = '├'
mm = '┼'
mr = '┤'
ll = '└'
lm = '┴'
lr = '┘'
horiz = '─'
vert = '│'

labelTop = ""
labelRow = ""

topBuilder = ""
rowBuilder = ""
botBuilder = ""
lastRow = len(rows)-1


for i, row in enumerate(rows):
    if i == 0:

        botBuilder += ll
        if labels: 
            labelTop += ul

    lastItem = len(row)-1

    for n, item in enumerate(row):
        lenCheck = copy.deepcopy(rows)
        if labels:
            lenCheck.insert(0,labels)
        column = [row[n] for row in lenCheck]
        longestItem = max(column,key=len)
        colMaxChars = len(longestItem)
        spacing = colMaxChars + 2

        padding =  colMaxChars - len(item) + 1
        if labels:
            lblPadding = colMaxChars - len(labels[n]) + 1
        # first item
        if n == 0:
            if not centered:
                # | item     |
                rowBuilder += f"{vert} {item} {vert:>{padding}}"
            else:
                rowBuilder += f"{vert} {item:^{colMaxChars}} {vert}"
            if i == 0:
                botBuilder += f"{horiz*spacing}"
                if labels: 
                    labelTop += f"{horiz*spacing}"
                    if not centered:
                        labelRow += f"{vert} {labels[n]} {vert:>{lblPadding}}"
                    else: 
                        labelRow += f"{vert} {labels[n]:^{colMaxChars}} {vert}"
                        # ├───────────
                    topBuilder += f"{ml}{horiz*(spacing)}"
                else:
                    # ┌───────────
                    topBuilder += f"{ul}{horiz*(spacing)}"

        
        # last item  
        elif n == lastItem:
            if not centered:
                # item       |
                rowBuilder += f" {item} {vert:>{padding}}\n"
            else:
                rowBuilder += f" {item:^{colMaxChars}} {vert}\n"
            if i == 0:
                # ────────────
                botBuilder += f"{horiz*spacing}"
                if labels:
                    labelTop += f"{horiz*spacing}"
                    if not centered:
                        labelRow += f" {labels[n]} {vert:>{lblPadding}}\n"
                    else: 
                        labelRow += f" {labels[n]:^{colMaxChars}} {vert}\n"
                    # ───────────┤
                    topBuilder += f"{horiz*(spacing)}{mr}"
                else:
                    # ───────────┐
                    topBuilder += f"{horiz*spacing}{ur}"

        # middle item
        else:
            if not centered:
                # item       |
                rowBuilder += f" {item} {vert:>{padding}}"
            else:
                rowBuilder += f" {item:^{colMaxChars}} {vert}"
            if i == 0:
                if labels:
                    labelTop += f"{um}{horiz*spacing}{um}"
                    if not centered:
                        labelRow += f" {labels[n]} {vert:>{lblPadding}}"
                    else:
                        labelRow += f" {labels[n]:^{colMaxChars}} {vert}"
                    # ┼────────────┼
                    topBuilder += f"{mm}{horiz*spacing}{mm}"
                else:
                    # ┬────────────┬
                    topBuilder += f"{um}{horiz*spacing}{um}"
                # ┴────────────┴
                botBuilder += f"{lm}{horiz*spacing}{lm}"

    if i == 0:
        botBuilder += lr
        if labels:
            labelTop += ur
    result = f"{labelTop}\n{labelRow}{topBuilder}\n{rowBuilder}{botBuilder}"
print(result)



