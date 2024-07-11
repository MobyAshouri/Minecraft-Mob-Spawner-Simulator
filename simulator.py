import asyncio
from spawner import Spawner

NUM_OF_SPAWNERS = 100
SIMULATION_LENGTH_IN_SECONDS = 60

async def timer(length: int, tasks: list[asyncio.Task]):
    for i in range(length):
        await asyncio.sleep(1)
        length-=1
        print(f"TIME REMAINING: {length}")
    
    for task in tasks:
        task.cancel()
    

async def simulation(spawners: list):
    allTasks: list[asyncio.Task] = []
    
    for spawner in spawners:
        allTasks.append(asyncio.create_task(spawner.spawn()))
        
    await timer(SIMULATION_LENGTH_IN_SECONDS, tasks=allTasks)
    
    spawnsAccumulator:int = 0
    for spawner in spawners:
        spawnsAccumulator+=spawner.totalMobsSpawned
        
    print("-----------------------------------")
    print(f"TOTAL SPAWNS: {spawnsAccumulator}")
    spm = (spawnsAccumulator * 60)/SIMULATION_LENGTH_IN_SECONDS
    print(f"SPAWNS PER MINUTE: {spm}")
    

async def main():
    spawners:list = []
    
    for i in range(NUM_OF_SPAWNERS):
        spawners.append(Spawner(spawnerID=i))
        
    await simulation(spawners=spawners)
        
        
asyncio.run(main())