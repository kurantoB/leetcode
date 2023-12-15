class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # visited
        inventory = []
        
        progress = 0
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if walkthru(board, word, r, c, progress, inventory):
                    return True
        
        return False
    
def walkthru(board, word, r, c, progress, inventory):
    if board[r][c] != word[progress]:
        return False
    inventory.append([r, c])
    progress += 1
    if progress == len(word):
        return True
    nextCells = getNextCells(board, inventory, progress)
    for nextCell in nextCells:
        if walkthru(board, word, nextCell[0], nextCell[1], progress, inventory):
            return True
    inventory.pop()
    return False

def getNextCells(board, inventory, progress):
    nextCells = []
    latest = inventory[progress - 1]
    
    #up
    if latest[0] > 0 and not [latest[0] - 1, latest[1]] in inventory:
        nextCells.append([latest[0] - 1, latest[1]])
    
    #down
    if latest[0] < len(board) - 1 and not [latest[0] + 1, latest[1]] in inventory:
        nextCells.append([latest[0] + 1, latest[1]])
    
    #left
    if latest[1] > 0 and not [latest[0], latest[1] - 1] in inventory:
        nextCells.append([latest[0], latest[1] - 1])
    
    #right
    if latest[1] < len(board[0]) - 1 and not [latest[0], latest[1] + 1] in inventory:
        nextCells.append([latest[0], latest[1] + 1])
    
    return nextCells