from utils.loader import configData
from pymongo import MongoClient
from pytz import timezone
from datetime import datetime
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey']);db = cluster['HYG'];points = db['points']
#-----------------------------------------------------------------------------------------------------#
async def addp(membro, pontos):

    points.update_one(
        {"_id": membro.id},
        {"$inc": {"pontos": pontos}},
        upsert = True
    )

async def addp2(membro, ctx, up):

    dt = datetime.now(timezone('America/Sao_Paulo'))
    
    points.update_one(
        {"_id": membro.id},
        {"$set": {f"ponto{up}": f"adicionado {dt.strftime('%d/%m/%Y')} por {ctx.name}"}},
        upsert = True
    )
#-----------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------#
async def rmvp(membro, pontos):
    
    points.update_one(
        {"_id": membro.id},
        {"$inc": {"pontos": pontos}},
        upsert = True
    )

async def rmvp2(membro, up,rs):

    points.update_one(
        {"_id": membro.id},
        {"$unset":{f"ponto{up}": rs}},
        upsert = True
    )
#-----------------------------------------------------------------------------------------------------#