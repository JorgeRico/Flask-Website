from models.database import Database

class Query():
    # select Object by id
    def selectByIdQuery(self, id):
        db     = Database()
        query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet where id = %s;" %id
        result = db.getJsonData(query)

        return result[0]
    
    # list of items
    def selectListTable(self):
        db = Database()
        query  = "SELECT id as id, name as name, numCards as numCards, deleted as deleted FROM mtgSet;"
        result = db.getJsonData(query)

        return result
    
    # insert object on DB
    def insertQuery(self, name, numCards):
        db     = Database()
        query  = 'INSERT INTO mtgSet (name, numCards) VALUES ("%s", %s);' %(name, numCards)
        result = db.insertData(query)

        return result
    
    # Update object on DB
    def updateQuery(self, id, name, numCards):
        db    = Database()
        query = "UPDATE mtgSet SET id = %s, name = '%s', numCards = %s where id = %s;" %(id, name, numCards, id)
        db.updateData(query)

    # mark as deleted on DB
    def deleteQuery(self, id):
        db    = Database()
        query = "UPDATE mtgSet SET deleted = 1 where id = %s;" %(id)
        db.updateData(query)


