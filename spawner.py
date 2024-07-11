import random
import asyncio

MINIMUM_NUM_SECONDS_FOR_SPAWN = 10
MAXIMUM_NUM_SECONDS_FOR_SPAWN = 39.95

class Spawner:
    def __init__(self, spawnerID:int = 0, spawnsPerWave:int = 4, totalMobsSpawned:int = 0) -> None:
        self.spawnerID: int = spawnerID
        self.SPAWNS_PER_WAVE: int = spawnsPerWave      # set the number of spawns per second
        self.totalMobsSpawned: int = totalMobsSpawned
        self.secondsUntilSpawn: float = 0
        
    async def spawn(self):
        minSeconds = int(round((MINIMUM_NUM_SECONDS_FOR_SPAWN * 100), 0))
        maxSeconds = int(round((MAXIMUM_NUM_SECONDS_FOR_SPAWN * 100), 0))
        self.secondsUntilSpawn = random.randint(minSeconds, maxSeconds) / 100
        
        await asyncio.sleep(self.secondsUntilSpawn)
        print(f"--> SPAWNED: {self.spawnerID}")
        self.totalMobsSpawned+=random.randint(1, self.SPAWNS_PER_WAVE)
        
        
        await self.spawn()
    
    async def resetMobsSpawned(self):
        self.totalMobsSpawned = 0
        
    async def setSpawnsPerWave(self, newSpawnRate: int):
        self.SPAWNS_PER_WAVE = newSpawnRate
        
    async def __dict__(self):
        return {
            "SPAWNS_PER_SECOND": self.SPAWNS_PER_SECOND,
            "TOTAL_MOBS_SPAWNED": self.totalMobsSpawned
        }