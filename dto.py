from typing import NamedTuple


class i_in_controller(NamedTuple):

    # get,post,update,delete
    method: str
    # http body
    data: str
    # type of content
    content: str
    # named user
    user: str

    def __init__(self, request):
        method = request.method
        data = request.data
        content = request.content_type
        user = request.user


class controller(i_in_controller):

    def __init__(self, request):
        super().__init__(request)

    def parse():
        # Parse JSON into an object with attributes corresponding to dict keys.
        i_in = json.loads(data, object_hook=lambda d: namedtuple(
            'X', d.keys())(*d.values()))

        return i_input_interactor(self.method, self.user, i_in.get("cmd"),
                                  i_in.get("deveui"), i_in.get("data"))


class i_input_interactor(NamedTuple):
    # save data, get data, remove data
    method: str
    # user name and passw
    user: str
    # api vega info
    cmd: str
    # device Eui
    dev: str
    # data info packet
    data: str

    def __init__(self, method, user, cmd, dev, data):
        self.method = method
        self.user = user
        self.cmd = cmd
        self.dev = dev
        self.data = data
