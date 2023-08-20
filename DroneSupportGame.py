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
            self.take_casualties(2)
            print('WE HAVE TAKEN 2 CASUALTIES')
        elif suppr_cas_chance >= 0.49:
            self.take_casualties(1)
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
        print('TAKING SUPRESSIVE FIRE!')
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
            self.take_casualties(2)
            print('THEY HAVE TAKEN 2 CASUALTIES')
        elif suppr_cas_chance >= 0.49:
            self.take_casualties(1)
            print('THEY HAVE TAKEN 1 CASUALTY')
        else:
            print('0 CASUALTIES REPORTED FOR THEM')
        
    def attack(self):
        attack_success_rate = random.random()
        attack_cas_rate = random.random()
        attack_cas = 0
        print('ATTACK!')
        
        if attack_cas_rate >= 0.90:
            self.take_casualties(10)
            print('THEY HAVE TAKEN 10 CASUALTIES')
        elif attack_cas_rate >= 0.75:
            self.take_casualties(5)
            print('THEY HAVE TAKEN 5 CASUALTIES')
        elif attack_cas_rate >= 0.49:
            self.take_casualties(4)
            print('THEY HAVE TAKEN 4 CASUALTIES')
        elif attack_cas_rate >= 0.24:
            self.take_casualties(3)
            print('THEY HAVE TAKEN 3 CASUALTIES')
        elif attack_cas_rate > 0:
            self.take_casualties(2)
            print('THEY HAVE TAKEN 2 CASUALTIES')
        else:
            print('NO ENEMY CASUALTIES REPORTED')
###########
        if attack_success_rate >= 0.80:
            attack_cas = 4
            print('WE HAVE TAKEN 4 CASUALTIES')
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
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        if target == str(1) and self.battery != 0:
            attack_cas = 0
            self.battery -= 10
            print('BATTERY LEVEL {battery} percent.'.format(battery=self.battery))
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
        elif target == str(2) and self.battery != 0:
            ammo_destroyed = int(attack_success_rate * 1000)
            print('{ammo_destroyed} AMMO DESTROYED!'.format(ammo_destroyed=ammo_destroyed))
            return ammo_destroyed

        else:
            print('INVALID TARGET!')


    def change_battery(self):
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        self.battery = 100
        print('BATTERY 100%')
    
    def fire_mission(self):
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('ROUNDS AWAY, ETA 1 MIKE')
        print('.......................')
        print('SPLASH! GOOD EFFECT ON TARGET. ENEMY IS SUPRESSED!')
        self.battery -= 10
        print('BATTERY LEVEL {battery} percent.'.format(battery=self.battery))

#############################################################################################
drone1 = Drone('Drone 1')
enemy = EnemyPlatoon('Chechen Brigade')
friendlies = FriendlySquad('Slayer 3')


while enemy.manpower > 0 and friendlies.manpower > 0:
    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print(drone1.__repr__())
    print(enemy.__repr__())
    print(friendlies.__repr__())
    print('The enemy and friendly platoons are preparing!')
    enemy_choice = random.random()
    friendly_choice = random.random()
    if (enemy_choice >= 0.80 or enemy.ammo < 1000) and enemy.supressed == False:
        enemy.resupply()
        print('The enemy resupplies.')

    elif enemy_choice >= 0.30 and enemy.supressed == False:
        attack = enemy.attack()
        friendlies.manpower -= attack

    elif enemy.supressed == False:
        enemy.supressive_fire()
        friendlies.is_supressed()
    else:
        enemy.supressed = False

##############
    if (friendly_choice >= 0.80 or friendlies.ammo < 500) and friendlies.supressed == False:
        friendlies.resupply()
        print('The friendlies resupply.')

    elif friendly_choice >= 0.30 and friendlies.supressed == False:
        print('The friendlies prepares their defenses and wait...')

    elif friendlies.supressed == False:
        friendlies.supressive_fire()
        enemy.is_supressed()
    
    else:
        friendlies.supressed = False

    print("Your turn!")
    your_choice = input("1 = Attack enemy positions, 2 = Change Battery, 3 = Call artillery: ")
    if your_choice == str(1) and drone1.battery > 0:

        attack_type = input("1 = Attack enemy trenches, 2 = Attack enemy ammo depots: ")
        if attack_type == str(1):

            print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
            enemy.manpower -= drone1.attack(attack_type)
            

        else:

            print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
            enemy.ammo -= drone1.attack(attack_type)
            

    elif your_choice == str(2) or drone1.battery <= 0:
        drone1.change_battery()
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    elif your_choice == str(3):
        drone1.fire_mission()
        enemy.is_supressed()
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    else:
        print('INVALID MISSION')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')



if enemy.manpower <= 0:

    print('VICTORY! PUSH THE ENEMY TRENCHES!')

elif friendlies.manpower <= 0:

    print('Friendly platoon decimated! Fall back!')

