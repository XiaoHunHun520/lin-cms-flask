from lin import Duplicated, NotFound


class KamiNotFound(NotFound):
    message = "卡密不存在"
    _config = False


class KamiActivation(Duplicated):
    code = 24
    message = "卡密未激活"
    _config = False

class KamiActivationok(NotFound):
    message = "卡密激活成功"
    _config = False