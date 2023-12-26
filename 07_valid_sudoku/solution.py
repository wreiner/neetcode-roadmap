class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        columns = {}
        rows = {}
        rboxid = -3
        cboxid = -1
        boxid = -3

        for ridx, row in enumerate(board):
            if not ridx in rows:
                rows[ridx] = {}

            if ridx % 3 == 0:
                rboxid += 3
            
            # # check for empty boxes
            # if rboxid >= 2:
            #     for i in range(rboxid-3, rboxid):
            #         if len(boxes[i]) <= 0:
            #             return False

            boxid += rboxid

            if not boxid in boxes:
                boxes[boxid] = {}

            for cidx, column in enumerate(row):
                if not cidx in columns:
                    columns[cidx] = {}

                if cidx == 0:
                    cboxid = rboxid - 1

                if cidx %3 == 0:
                    cboxid += 1
                    boxid = cboxid

                if not boxid in boxes:
                    boxes[boxid] = {}

                if column == '.':
                    continue

                if boxes[boxid].get(column) is not None:
                    return False
                
                boxes[boxid][column] = 1

                if rows[ridx].get(column) is not None:
                    return False
                rows[ridx][column] = 1
                
                if columns[cidx].get(column) is not None:
                    return False
                columns[cidx][column] = 1
        
        return True

