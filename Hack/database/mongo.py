from motor.motor_asyncio import AsyncIOMotorClient


class Mongo:
    def __init__(self, url):
        self.mongo = AsyncIOMotorClient(url)
        self.db = self.mongo.HACK
        self.usersdb = self.db.usersdb

    async def get_users(self) -> list:
        if user := self.usersdb.find():
            return [int(user['user_id']) for user in await user.to_list(length=1000000000)]
        else:
            return []
        
    async def is_user(self, user_id: int) -> bool:
        user = await self.usersdb.find_one({"user_id": user_id})
        return bool(user)
    
    async def add_user(self, user_id: int):
        try:
            is_served = await self.is_user(user_id)
            if is_served:
                return
            return await self.usersdb.insert_one({"user_id": user_id})
        except:
            pass