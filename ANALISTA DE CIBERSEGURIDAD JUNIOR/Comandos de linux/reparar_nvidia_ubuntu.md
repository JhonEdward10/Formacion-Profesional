# 🔧 Reparación del Driver NVIDIA en Ubuntu

## Diagnóstico y solución — GTX 1060 Mobile
### Acer Nitro AN515-52

---

## 🔍 PASO 1 — Verificar si el driver funciona

```bash
nvidia-smi
```

Si sale error "NVIDIA-SMI has failed", el driver no está activo.

---

## 🔍 PASO 2 — Ver qué driver recomienda el sistema

```bash
ubuntu-drivers devices
```

Busca el que dice "recommended" (normalmente nvidia-driver-535).

---

## 🔍 PASO 3 — Ver si el módulo está cargado

```bash
lsmod | grep nvidia
```

Si no sale nada, el módulo no está cargado.

---

## 🔍 PASO 4 — Ver el estado de DKMS

```bash
dkms status
```

Debe decir "installed" para tu kernel actual.

---

## 🔍 PASO 5 — Buscar qué bloquea el driver (¡LA CLAVE!)

```bash
grep -rn "nvidia" /etc/modprobe.d/ /lib/modprobe.d/ 2>/dev/null | grep -i off
```

Si aparece "alias nvidia off" el driver está desactivado por nvidia-prime.

---

## 🔧 PASO 6 — Reconstruir el módulo (si es necesario)

```bash
sudo dpkg-reconfigure nvidia-dkms-535
```

---

## ✅ SOLUCIÓN PRINCIPAL — Activar la GPU NVIDIA

```bash
sudo prime-select nvidia
sudo reboot
```

Después del reinicio verificar:

```bash
nvidia-smi
```

---

## 📋 COMANDOS ÚTILES EXTRA

Ver qué modo de GPU está activo:
```bash
sudo prime-select query
```

Cambiar entre modos:
```bash
sudo prime-select nvidia      # GPU dedicada
sudo prime-select on-demand   # Híbrido
sudo prime-select intel       # Solo gráficos integrados
```

Ver tipo de sesión (X11 o Wayland):
```bash
echo $XDG_SESSION_TYPE
```

---

## 💡 LECCIÓN APRENDIDA

El problema ocurrió después de cambios en el kernel. El archivo
`/lib/modprobe.d/blacklist-nvidia.conf` tenía el driver en modo "off"
(puesto por nvidia-prime).

El comando `sudo prime-select nvidia` lo reactivó correctamente.

**Resultado:** Driver 535.309.01 activo, GTX 1060 funcionando,
parpadeo de pantalla resuelto.

---

*Pitalito, Huila — 2026 · Jhon Edward Méndez*
