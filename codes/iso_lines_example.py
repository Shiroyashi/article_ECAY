import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# 1. Настройка цветовой карты
cmap = plt.cm.get_cmap('plasma').copy()
cmap.set_under('white')

# 2. Сетка переменных
x = np.linspace(1e-4, 1, 300)
Q2 = np.linspace(0.1, 10, 300)
X, Q2_grid = np.meshgrid(x, Q2)

# 3. Модельная функция
M = 100.0
log_term = np.log(1 / X)
numerator = Q2_grid**4
denominator = (M**2 + Q2_grid)**2
f = log_term * numerator / denominator

# 4. Маска
a, b = 5.0, 4.0
mask = Q2_grid <= (a + b * X)
f[~mask] = 0

# 5. Нормировка
dx = x[1] - x[0]
dQ2 = Q2[1] - Q2[0]
f /= np.sum(f) * dx * dQ2

# 6. Highest Density Region: отсортируем значения
f_flat = f.ravel()
sorted_indices = np.argsort(f_flat)[::-1]
f_sorted = f_flat[sorted_indices]
cdf_sorted = np.cumsum(f_sorted) * dx * dQ2
threshold_idx = np.searchsorted(cdf_sorted, 0.9)
f_star = f_sorted[threshold_idx]

# 7. Построение
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# --- (1) Плотность f(x, Q2)
norm = Normalize(vmin=1e-10, vmax=np.max(f))
cf1 = axs[0].contourf(X, Q2_grid, f, levels=50, cmap=cmap, norm=norm, extend='min')
axs[0].plot(x, a + b * x, 'w--', label=r'Исключённая область: $Q^2 > a + bx$')
axs[0].set_title('Плотность $f(x, Q^2)$')
axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$Q^2$')
axs[0].legend()
fig.colorbar(cf1, ax=axs[0], extend='min')

# --- (2) Область HDR с контуром
cf2 = axs[1].contourf(X, Q2_grid, f, levels=50, cmap=cmap, norm=norm, extend='min')
c = axs[1].contour(X, Q2_grid, f, levels=[f_star], colors='red', linewidths=2)
axs[1].clabel(c, inline=True, fmt={f_star: 'HDR 90%'}, fontsize=10)
axs[1].plot(x, a + b * x, 'w--')
axs[1].set_title('Highest Density Region (90%)')
axs[1].set_xlabel(r'$x$')
axs[1].set_ylabel(r'$Q^2$')
fig.colorbar(cf2, ax=axs[1], extend='min')

plt.tight_layout()
plt.show()
