from matplotlib import rc
rc("font", family="serif", size=18)

import daft

pgm = daft.PGM([10, 6.5], origin=[-1, -3], grid_unit=1.5, node_unit=1.5)
pgm.add_node(daft.Node('phi', r'$\phi$', 0, 0, observed=True))
pgm.add_node(daft.Node('z', r'$z_i$', 2, 0))
pgm.add_node(daft.Node('x', r'$x_i$', 4, 1.125, observed=True))
pgm.add_node(daft.Node('l', r'$l_{i,j}$', 4, -1.125, observed=True))
pgm.add_node(daft.Node('u', r'$u_{j,k}$', 6.5, -1))
pgm.add_node(daft.Node('mu', r'$\mu_k$', 6.5, .875))
pgm.add_node(daft.Node('sigma', r'$\Sigma_k$', 6.5, 2.125))
pgm.add_plate(daft.Plate([1, -2.5, 4, 4.75], label=r"$N$"))
pgm.add_plate(daft.Plate([3, -2.25, 5, 2.25], label=r"$M$"))
pgm.add_plate(daft.Plate([5.25, -2, 2.5, 5], label=r"$K$"))
pgm.add_edge("phi", "z")
pgm.add_edge("z", "x")
pgm.add_edge("z", "l")
pgm.add_edge("u", "l")
pgm.add_edge("mu", "x")
pgm.add_edge("sigma", "x")
pgm.render()
pgm.figure.savefig('img/3.svg')
