
P_e = 43  # l’unité est dBm
G_e = 15  # l’unité est dB
G_r = 0  # l’unité est dB
f = 1800  # l’unité est MHz
sens = -100  # l’unité est dBm

def affaiblissement_espace_libre(d_km, f_mhz):
  # Formule standard : 32.44 + 20*log10(f_mhz) + 20*log10(d_km)
  return 32.44 + 20 * np.log10(f_mhz) + 20 * np.log10(d_km)

def puissance_recue(d_km, f_mhz):
  affaiblissement = affaiblissement_espace_libre(d_km, f_mhz)
  return P_e + G_e + G_r - affaiblissement

print("--- Résultats pour différentes distances ---")
distances_test = [1, 2, 5, 10]
for d in distances_test:
  aff = affaiblissement_espace_libre(d, f)
  pr = puissance_recue(d, f)
  print(
      f"À {d} km -> Affaiblissement: {aff:.2f} dB | Puissance reçue:"
      f" {pr:.2f} dBm"
  )

distances = np.linspace(0.1, 20, 500)
puissances = puissance_recue(distances, f)

plt.figure(figsize=(10, 6))
plt.plot(
    distances,
    puissances,
    label="Puissance reçue (1800 MHz)",
    color="blue",
    linewidth=2,
)

plt.axhline(
    y=sens, color="red", linestyle="--", label=f"Sensibilité ({sens} dBm)"
)

plt.title("Puissance reçue en fonction de la distance", fontsize=14)
plt.xlabel("Distance (km)", fontsize=12)
plt.ylabel("Puissance reçue (dBm)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend()

plt.show()