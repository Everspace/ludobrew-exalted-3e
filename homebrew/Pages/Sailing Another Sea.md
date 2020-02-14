---
content: page
name: Sailing Another Sea
---

# Basics

This is a Sail rework to hopefully make boat'ing much more interesting

It introduces 2 new resources to keep track of while in combat:

* **Bilge** (b) - Your ship is taking on water! Or a city is getting weary from your assault. It makes it harder to perform actions as the battle draws on, and this resource represents wear and tear on the ship as a whole. When a charm or effect has a cost involving bilge, you gain that much instead of losing it.
* **Tempo** (t) - The resource for a captain to spend to perform decisive actions as a man with a boat below him.

Every ship must have a captain, and optionally a specific battlegroup that operates as the crew.

## Combat

At the start of Combat, all participants Join Battle like normal. Generally ships will start at Extreme range away from one another, and must take actions to close the distance.

In addition at the beginning of the captain's turn:

* Gain (Crew Size + Crew Might + Drill - Weight) Tempo
* Take Bilge which accumulates at (Weight + hl lost + bilge penalty)
* Lose 1HL for every 5 bilge you have over (Weight * 5)

While on a boat:

* You take a general die penalty of (Bilge /5) while on your ship of origin.
* If you do not have at least a dot of sail, you take a further -3 to all actions while you try not to be in the flurry of activity.

A boat with no empty health levels is not "sunk" or destroyed immediately, it is simply stalled, and the captain is unable to spend Tempo, and the only ship-specific action able to be taken is **Remove Bilge**. Further action must be taken to actually sink the ship, or repairs must be made lest the boat go under and you make it back to port.

## Weight

How barge and in charge are you? Weight is the measure of one's boat-attude.

| Size | Weight | Max size
|:-:|:-:|:-:|
| Rowboat | 0 | 1
| Small | 1 | 3
| Medium | 3 | 5
| Large | 5 | 7
| City | 7 | lots

* A boat can only hold up to a total of "Max Size" people. (This does not usually include the heroes and their pet Tyrant Lizard)
* Size across different types is added together, for example: A size 1 battlegroup of sailors and a size 2 of soldiers is size 3 and fits inside a small boat.
* **Vast Wealth** or **An Incredible Treasure** is worth 1 size.
* At rowboat size, you are considered to be Tiny Creature.
* Medium boat and larger has Legendary Size
* Use your best judgement on what boats are what Weight.

# Action

## Captain Action

* Roll Wits + Sail for most actions.
* Roll Int + Sail to identify a ship
* Roll Perception + Sail to get information on their Bilge, or other qualities of the ship.

A caption may perform (in addition to the default actions) any of the following actions:

* Spend Tempo
* Make Tempo with (Wits + Sail)

In addition once per turn you get a **Nautical Action**, which can be used to do

* Spend Tempo
* A Command action to specifically your crew using (Sail or War)

You may only spend Tempo at one thing at a time.

### Tempo

| Cost | Effect
|:----:|:--
| 3t | Fire weapons
| 3t | Ready Weapons
| 6t | Board
| 6t 1hl | Ram (inflict 10b or 3hl, or Prone passengers)
| 6t | Swerve (prone non-crewmembers)
| 10t | Cause an environmental hazard
| 3t | Move a rangeband
| 10t | Move 2 rangebands
| 3t | Withdraw
| xt | Add x Initative
| xt | Prevent next x bilge <!--Up to a max?-->
| x*2t | Remove x bilge

* Firing weapons behaves like Seige Weapons, but can be directed with Sail (if they are on a boat). When you do, make a Withering attack to add Bilge (vs 0 soak), or a decisive attack using Initative as usual.
* Firing a weapon always hits, unless magic makes it a contest.
* A Ram allows you inflict the opposing ship with your choice of ONE OF the following:
  * 10 bilge
  * 3hl
  * A roll to Remain Upright for EVERYONE
* Swerve causes all unwanted passengers on your ship to roll to Remain Upright.

## Everybody Actions

| Action | Does | Roll |
|:-|:-|:-:
| Reduce Bilge | <- | (??? + ???)
| Be a Crewmember | Make Tempo | (Wits + Bureau or War - 3) or (Wits + Sail)
| Ready the Weapons | <- | (Dex + Sail) or (??? + War/Archery)
| Take Aim | Gain Ship Initiative | (Perception + Combat Ability or Sail)
| Fire | <- | (Perception + Sail)
|Patch Job| Basic project to remove HLs from bilge per turn | (Attribute + Craft)
| Stay Upright | Prevent prone due to sudden movement | (Dex + Dodge or Athletics) or (Stamina + Resistance)

### Reduce Bilge

* Roll (Something + Something) to reduce bilge.

Any hero can attempt to stunt something reasonable to reduce bilge, the power relies on people helping out! For example:

* Int + Bureaucracy to increase efficiency by organization
* Strength or Stamina + Athletics to yeet water out of the ship
* Wits + Sail to perform your boatly duties
* Wits + Craft to quickly plug small leaks as they appear,
* Int + Craft to make better makeshift tools as a basic project.
* Appearance + Performance to bolster spirits
* Int + Medicine to give people a little... pick-me-up you made earlier.

### Be a Crewmember

Craftier folk can generate Tempo for the captain to spend.

They may roll (Wits + Bureaucracy or War - 3) or (Wits + Sail) to create Tempo for the captain to spend.

### Ready the Weapons

A character can roll some combination of stuff to beat difficulty 2 to ready a barrage. This is usually Dexterity + Sail, or (Something + War/Archery)

### Take Aim

A character can steady the weapons to add (Perception + Combat Ability) initiative to the ship.

### Fire

A character can launch the weapons themselves with the captain's permission. This can be the usual pool for attacking with a Siege weapon, or (Perception + Sail)

### Patch Job

A crafter can do a Basic Project to reduce the number of ship HLs that count for incoming bilge. This does not repair the ship itself, it just makes it hurt less.

### Stay Upright

Sometimes the boat is rocked by another boat, or terrible seas happen or you're being picked up by a behemoth. People on the boat must beat the difficulty presented or be knocked prone. They may nimbly regain their footing with (Dex + Dodge or Athletics) or "just take it" with (Stamina + Resistance).
