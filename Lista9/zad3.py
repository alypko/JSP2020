import matplotlib.pyplot as plt
import numpy as np

g = 9.81

v0 = float(input("Podaj predkosc poczatkowa: "))
alfa = np.radians(int(input("Podaj kat rzutu: ")))

v0x = v0 * np.cos(alfa)
v0y = v0 * np.sin(alfa)

H_max = (v0y**2)/(2*g)
T = 2*v0y/g
zasieg = v0**2/g * np.sin(2*alfa)

print("\nMaks. wysokosc:", H_max,"\nZasieg ruchu: ", zasieg,"\nCzas calk: ", T)

czas = np.arange(0, T, 0.01)

vx = [v0x for t in czas]
vy =[v0y - g*t for t in czas]
x = [v0x*t for t in czas]
y = [v0y*t-0.5*g*(t**2) for t in czas]
tor = [x*np.tan(alfa)-g*x**2/(2*v0x**2) for x in x]

fig = plt.figure()

ax_1 = fig.add_subplot(3, 1, 1)
ax_1.set(title = 'Predkosc chwilowa w kierunku pionowym i poziomym po czasie t',
        xlabel = 'x[m]',
        ylabel = 't[s]')
ax_1.plot(czas, vx, czas, vy)

ax_2 = fig.add_subplot(3, 1, 2)
ax_2.set(title = 'Polozenie w funckcji czasu',
        xlabel = 'x[m]',
        ylabel = 't[s]')
ax_2.plot(x, czas)

ax_3 = fig.add_subplot(3, 1, 3)
ax_3.set(title = 'Wykres toru rzutu',
        xlabel = 'x[m]',
        ylabel = 'y[m]')
ax_3.plot(czas, tor)

plt.tight_layout()
plt.show()