# Minecraft Mob Spawner Simulator (MMSS)
This Minecraft Mob Spawner Simulator replicates Minecraft: Java Edition's Mob Spawner spawn logic. This is useful for server-based gamemodes such as Factions.

This program can be used to calculate the number of spawners needed relative to a player's mob kill rate to create an equilibrium to maximized mob drops and xp gain.

# Spawn Logic
In Minecraft: Java Edition, a mob spawner only functions in client light levels below 12.

The game generates a random number of seconds to wait; the value is between 10 and 39.95 seconds. When done waiting, the spawner will spawn 1 to 4 mobs (given there is space for that mob to exist).

This program counts the total number of mobs spawned, and with some algebra, calculates the number of spawns per minute. However, for an accurate reading rate of mob spawners per minute, it is recommended to run this simulation
for a long time. This program will always wait at least ten seconds until a mob spawns due to the spawn logic of minecraft. By running a simulation for a long time, the effect of the initial 10 seconds isn't as profound.
