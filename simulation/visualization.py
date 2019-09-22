from model import Model


class Visualization():
    def __init__(self, model):
        self.model = model
        self.render()

    def step(self):
        self.model.step()
        self.render()

    def render(self):
        text = ""
        for y in range(self.model.grid.height):
            for x in range(self.model.grid.width):
                c = self.model.grid[y][x]
                if c is None:
                    text += ' '
                elif c.type == 0:
                    text += 'X'
                elif c.type == 1:
                    text += '0'
                # else:
                #     text += '+'
            text += '\n'
        print(text)


if __name__ == '__main__':
    model_params = {
        "height": 10,
        "width": 10,
        # Agent density, from 0.8 to 1.0
        "density": 0.8,
        # Homophily, from 3 to 8
        "homophily": 2
    }

    model = Model(**model_params)
    viz = Visualization(model)

    for i in range(100):
        if model.running:
            print("Step:", i)
            viz.step()
            print('----')