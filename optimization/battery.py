import pyomo.environ as pyo
import numpy as np


def pnl(model):
    return pyo.summation(model.c, model.p)




model = pyo.AbstractModel()
model.n = pyo.Param(within=pyo.NonNegativeIntegers)
model.max_power = pyo.Param(within=pyo.NonNegativeReals)
model.init_energy = pyo.Param(within=pyo.NonNegativeReals)
model.capacity = pyo.Param(within=pyo.NonNegativeReals)
model.I = pyo.RangeSet(1, model.n)
model.c = pyo.Param(model.I)
model.p = pyo.Var(model.I, domain=pyo.Reals)

def charge_power_constraint(model, i) -> bool:
    return model.p[i] <= model.max_power

def discharge_power_constraint(model, i) -> bool:
    return model.p[i] >= -model.max_power

def max_charge_constraint(model, k):
    s = sum(model.p[i] for i in range(1,k+1) )
    return model.capacity >= s

def max_discharge_constraint(model, k):
    s = sum(model.p[i] for i in range(1,k+1) )
    return s >= model.init_energy

model.OBJ = pyo.Objective(rule=pnl)
model.charge_power_constraint = pyo.Constraint(model.I, rule=charge_power_constraint)
model.discharge_power_constraint = pyo.Constraint(model.I, rule=discharge_power_constraint)

model.max_charge_constraint = pyo.Constraint(model.I, rule=max_charge_constraint)
model.max_discharge_constraint = pyo.Constraint(model.I, rule=max_discharge_constraint)


data = {
    None: {
        'n': {None: 10},
        'max_power': {None: 100},
        'capacity': {None: 500},
        'init_energy': {None: 0},
        'c': {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}
    }
}
instance = model.create_instance(data)

solver = pyo.SolverFactory('glpk')  # for nonlinear, or 'glpk' for linear
solver.solve(instance)
instance.display()
