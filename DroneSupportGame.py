import random

class FriendlySquad:

    def __init__(self, input_name):
        self.name = input_name
        self.manpower = 10
        self.ammo = 2000
        self.supressed = False

    def __repr__(self):

        return 'Our friendly Squad are named the {name}, their manpower is {manpower} men and are down to {ammo} rounds.'.format(name=self.name, manpower=self.manpower, ammo=self.ammo)

    def take_casualties(self, casualties):
        self.manpower -= casualties

    def resupply(self):
        self.ammo += 1000

    def supressive_fire(self):
        print('SUPRESSIVE FIRE!')
        supression = self.manpower * 30
        if self.ammo - supression <= 0:
            self.ammo = 0
            print('OUT OF AMMO! NEED RESUPPLY!')
        else:
            self.ammo -= supression

    def is_supressed(self):
        print('GET DOWN! TAKING SUPRESSIVE FIRE!')
        self.supressed = True
        suppr_cas_chance = random.random()
        if suppr_cas_chance >= 0.75:
            take_casualties(2)
            print('WE HAVE TAKEN 2 CASUALTIES')
        elif suppr_cas_chance >= 0.49:
            take_casualties(1)
            print('WE HAVE TAKEN 1 CASUALTY')
        else:
            print('NO CASUALTIES REPORTED')
    
###########################################################

class EnemyPlatoon:

    def __init__(self, input_name):
        self.name = input_name
        self.manpower = 30
        self.ammo = 6000
        self.supressed = False

    def __repr__(self):

        return 'The enemy platoon are named the {name}, their manpower is {manpower} men and are down to {ammo} rounds.'.format(name=self.name, manpower=self.manpower, ammo=self.ammo)

    def take_casualties(self, casualties):
        self.manpower -= casualties

    def resupply(self):
        self.ammo += 3000

    def supressive_fire(self):
        print('SUPRESSIVE FIRE!')
        supression = self.manpower * 30
        if self.ammo - supression <= 0:
            self.ammo = 0
            print('THE ENEMY IS OUT OF AMMO!')
        else:
            self.ammo -= supression

    def is_supressed(self):
        print('SUPRESSIVE FIRE! KEEP THEIR HEADS DOWN!')
        self.supressed = True
        suppr_cas_chance = random.random()
        if suppr_cas_chance >= 0.75:
            take_casualties(2)
            print('THEY HAVE TAKEN 2 CASUALTIES')
        elif suppr_cas_chance >= 0.49:
            take_casualties(1)
            print('THEY HAVE TAKEN 1 CASUALTY')
        else:
            print(' CASUALTIES REPORTED')
        
    def attack(self):
        attack_success_rate = random.random()
        attack_cas_rate = random.random()
        attack_cas = 0
        print('ATTACK!')
        if attack_cas_rate >= 0.75:
            take_casualties(5)
            print('THEY HAVE TAKEN 5 CASUALTIES')
        elif attack_cas_rate >= 0.49:
            take_casualties(3)
            print('THEY HAVE TAKEN 3 CASUALTIES')
        elif attack_cas_rate >= 0.24:
            take_casualties(2)
            print('THEY HAVE TAKEN 2 CASUALTIES')
        elif attack_cas_rate > 0:
            take_casualties(1)
            print('THEY HAVE TAKEN 1 CASUALTY')
        else:
            print('NO ENEMY CASUALTIES REPORTED')
###########
        if attack_success_rate >= 0.75:
            attack_cas = 5
            print('WE HAVE TAKEN 5 CASUALTIES')
            return attack_cas
        elif attack_success_rate >= 0.49:
            attack_cas = 5
            print('WE HAVE TAKEN 3 CASUALTIES')
            return attack_cas
        elif attack_success_rate >= 0.24:
            attack_cas = 5
            print('WE HAVE TAKEN 2 CASUALTIES')
            return attack_cas
        elif attack_success_rate > 0:
            attack_cas = 5
            print('WE HAVE TAKEN 1 CASUALTY')
            return attack_cas
        else:
            print('NO CASUALTIES REPORTED ON OUR SIDE')
            return attack_cas
        

###########################################################

class Drone:

    def __init__(self, input_name):
        self.name = input_name
        self.battery = 100
        self.ammo = 30

    def __repr__(self):

        return 'Our drone is nicknamed {name}, has {battery} percent battery and has {ammo} ammo left.'.format(name=self.name, battery=self.battery, ammo=self.ammo)

    def attack(self, target):
        attack_success_rate = random.random()
        if target == 'trench' and self.battery != 0:
            attack_cas = 0
            if attack_success_rate >= 0.75:
                attack_cas = 5
                print('THEY HAVE TAKEN 5 CASUALTIES')
                return attack_cas
            elif attack_success_rate >= 0.49:
                attack_cas = 3
                print('THEY HAVE TAKEN 3 CASUALTIES')
                return attack_cas
            elif attack_success_rate >= 0.24:
                attack_cas = 2
                print('THEY HAVE TAKEN 2 CASUALTIES')
                return attack_cas
            elif attack_success_rate > 0:
                attack_cas = 1
                print('THEY HAVE TAKEN 1 CASUALTY')
                return attack_cas
            else:
                print('NO CASUALTIES REPORTED')
                return attack_cas
        elif target == 'ammo dump' and self.battery != 0:
            ammo_destroyed = int(attack_success_rate * 1000)
            print('{ammo_destroyed} AMMO DESTROYED!'.format(ammo_destroyed=ammo_destroyed))
            return ammo_destroyed

        else:
            print('INVALID TARGET!')

        self.battery -= 10
        print('BATTERY LEVEL {battery} percent.'.format(battery=self.battery))

    def change_battery(self):
        self.battery = 100
        print('BATTERY 100%')
    
    def fire_mission(self):
        print('ROUNDS AWAY, ETA 1 MIKE')
        print('.......................')
        print('SPLASH! GOOD EFFECT ON TARGET. ENEMY IS SUPRESSED!')

#############################################################################################
drone1 = Drone('Drone 1')
enemy = EnemyPlatoon('Chechen Cunts')
friendlies = FriendlySquad('Slayer 3')

##while enemy.manpower != 0: