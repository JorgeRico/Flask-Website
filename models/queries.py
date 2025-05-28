from models.database import Database

class Query():
    def selectByIdQuery(self, id):
        db     = Database()
        query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet where id = %s;" %id
        result = db.getJsonData(query)

        return result[0]
    
    def selectListTable(self):
        db = Database()
        query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet;"
        result = db.getJsonData(query)

        return result
    
    def insertQuery(self, name, numCards):
        db     = Database()
        query  = 'INSERT INTO mtgSet (name, numCards) VALUES ("%s", %s);' %(name, numCards)
        result = db.insertData(query)

        return result
    
    def updateQuery(self, id, name, numCards):
        db    = Database()
        query = "UPDATE mtgSet SET id = %s, name = '%s', numCards = %s where id = %s;" %(id, name, numCards, id)
        db.updateData(query)


