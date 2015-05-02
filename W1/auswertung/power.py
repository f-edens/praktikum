__author__ = 'fred'

from pythonUtils.data import Data
from scipy.integrate import trapz

pfile = "files/press.data"
vfile = "files/volume.data"
pvfile = "files/pv.data"

vmin = 195.
hub = 140.


def main():
    pdata = Data(pfile, ("t", "p")).p
    vdata = Data(vfile, ("t", "v")).v

    # Gemessenen Winkel in Volumen umrechnen [cm³]
    vdata *= -1
    vdata -= min(vdata)
    vdata *= hub/max(vdata)
    vdata += vmin

    with open(pvfile, "w+") as out:
        for p, v in zip(pdata, vdata):
            out.write("%f\t%f\n" % (p, v))

    energy = trapz(pdata * 1e3, vdata*1e-6)

    print(energy)


if __name__ == '__main__':
    main()