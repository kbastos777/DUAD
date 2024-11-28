class Head :
    def __init__(self) -> None:
        pass

class Torso:
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Arm:
    def __init__(self,hand):
        self.hand = hand


class Hand:
    def __init__(self) -> None:
        pass


class Leg:
    def __init__(self,foot):
        self.foot = foot


class Foot:
    def __init__(self) -> None:
        pass


class Human:
    def __init__(self,head,torso,right_arm,left_arm,right_hand,left_hand,right_leg,left_leg,right_foot,left_foot):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.right_leg = right_leg
        self.left_leg= left_leg
        self.right_foot = right_foot
        self.left_foot = left_foot

head = Head()

right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_foot = Foot()
left_foot = Foot()
right_leg = Leg(right_foot)
left_leg = Leg(left_foot)

torso = Torso(head,right_arm,left_arm,right_leg,left_leg)

human = Human(head,torso,right_arm,left_arm,right_hand,left_hand,right_leg,left_leg,right_foot,left_foot)

print(human)