class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #we have a dictionary for rows, a dictionary for columns, and a dictionary for boxes
        #each key in the dictionary is the row index (0-8)
        #inside each key we have a set "seen" that holds whether we have seen a number in the row/column

        import collections

        #Create a dictionary where every row/column index (0-8) gets its own "seen" set.
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)

        #Create a dictionary where every box coordinate (ex: 0,0) gets its own seen set.
        boxes = collections.defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                current_num = board[row][column]

                #print(current_num) #1, 2, ., ., ., 3, ...

                if current_num == ".":
                    continue

                if current_num in rows[row] or current_num in columns[column] or current_num in boxes[(row // 3, column // 3)]:
                    return False

                rows[row].add(current_num)
                columns[column].add(current_num)
                boxes[(row // 3, column // 3)].add(current_num)

        return True

