
def make_d_d_eta(ro_sham_bo):

    def d_d_eta(eta, x0):
        return (ro_sham_bo(eta + 0.01, x0) - ro_sham_bo(eta, x0)) / 0.01

    return d_d_eta


def make_d_d_x0(ro_sham_bo):

    def d_d_x0(eta, x0):
        return (ro_sham_bo(eta, x0 + 0.01) - ro_sham_bo(eta, x0)) / 0.01

    return d_d_x0


def make_d2_d_eta2(ro_sham_bo):

    return make_d_d_eta(make_d_d_eta(ro_sham_bo))


def make_d2_d_x02(ro_sham_bo):

    return make_d_d_x0(make_d_d_x0(ro_sham_bo))


def make_d2_d_eta_d_x0(ro_sham_bo):

    return make_d_d_eta(make_d_d_x0(ro_sham_bo))
