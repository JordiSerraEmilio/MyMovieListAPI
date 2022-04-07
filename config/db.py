import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:admin@cluster0.xfs7y.mongodb.net/admin?retryWrites=true&w=majority")
db = client.mymovielistdb
