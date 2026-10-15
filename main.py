import modelos.Empleado as emp
import modelos.Departamento as dep

empleado1 = emp.Empleado("dan", "11111111-7", "dnemp@comp.cl", 1)
empleado2 = emp.Empleado("carl", "22222222-8", "caremp@comp.cl", 2)

ventas = dep.Departamento("ventas", 1)

ventas.empleados.append(empleado1)
ventas.empleados.append(empleado2)

print(ventas)
