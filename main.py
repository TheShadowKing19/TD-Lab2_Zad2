import numpy as np
import matplotlib.pyplot as plt


# Zestaw funkcji numer 7


# Parametr f - częstość próbkowania
f = 2

T = 1 / f

# Częstotliwość próbkowania
fs = 8000

# Okres próbkowania
Ts = 1/fs

# Czas trwania sygnału
Tc = 1

# Liczba próbek przypadających na cały sygnał
N = Tc * fs

# Wartość fi
fi = 2 * np.pi

t = np.arange(0, (N - 1) / fs, Ts)

# Funkcje
x = (1 - t) * np.sin(2 * np.pi * f * t + fi) * np.cos(4 * np.pi * t)
y = np.sin(np.pi * t) * np.sin(2 * x * np.pi * t)
z = np.sqrt(np.abs(y)) - (3 * x)
v = x * (y ** 2) - (z * np.cos(x))

fig, (ay, az, av) = plt.subplots(3)  # Kolejno:
# fig -> nazwa okna
# ay, az, av -> deklaracja wykresów, które będą częścia okna. Deklaracja w sposób jak wyżej powoduję, że wykresy będą
# wyświetlone jeden na drugim. Jeśli byśmy napisali to w sposób "((ay, az), ay)", wykres ay i az były obok siebie, a ay
# pod nimi
# plt.subplots() -> Jak argument bierze układ wykresów. Argument (3, 2) stworzyłby układ 3x2 wykresów
ay.plot(t, y)
ay.set_title("y(t)")
az.plot(t, z)
az.set_title("z(t)")
av.plot(t, v)
av.set_title("v(t)")
fig.tight_layout()  # Wyrównuje położenie wykresów
plt.savefig('TD-Lab2_Zad2.png')
plt.show()



