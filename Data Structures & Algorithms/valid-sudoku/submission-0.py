class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        blocks = {}
        for rowNum, row in enumerate(board):

            for colNum, num in enumerate(row):
                if num == ".":
                    continue
                rows[(rowNum, num)] = rows.get((rowNum, num), 0) + 1
                print(rows[(rowNum, num)])
                if rows[(rowNum, num)] > 1:
                    
                    return False

                columns[(colNum, num)] = columns.get((colNum, num), 0) + 1
            #    print(columns[(colNum, num)])
                if columns[(colNum, num)] > 1:
                    return False

                blockNum = 0 #init
                if rowNum <= 2:
                    if colNum <= 2:
                        blockNum = 1
                    elif colNum <= 5:
                        blockNum = 2
                    else:
                        blockNum = 3

                elif rowNum <= 5:
                    if colNum <= 2:
                        blockNum = 4
                    elif colNum <= 5:
                        blockNum = 5
                    else:
                        blockNum = 6

                else:
                    if colNum <= 2:
                        blockNum = 7
                    elif colNum <= 5:
                        blockNum = 8
                    else:
                        blockNum = 9

                blocks[(blockNum, num)] = blocks.get((blockNum, num), 0) + 1
                #print(blocks[(blockNum, num)])
                if blocks[(blockNum, num)] > 1:
                    return False

        return True



        