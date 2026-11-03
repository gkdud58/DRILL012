# 객체로 구성된 게임월드
world = [[],[]] # 게임월드에 존재하는 모든 객체를 담는 리스트

# 게임월드에 객체를 담는 함수
def add_object(o, depth): # depth : 0(배경) 1(캐릭터)
    world[depth].append(o)


# 게임월드에서 객체를 제거하는 함수
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return


# 게임로직
def update():
    for layer in world:
        for o in layer[:]:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()