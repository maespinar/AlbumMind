# ============================================================
#  Clases de datos que representan cada tabla de la BD.
#  Almacén de datos.
# ============================================================

from dataclasses import dataclass, field
from typing import Optional

# ─────────────────────────────────────────────────────────────
#  PAIS
# ─────────────────────────────────────────────────────────────
@dataclass
class Pais:
    cod_pais: str
    nombre: str
    def __str__(self) -> str:
        return f"[{self.cod_pais}] {self.nombre}"

# ─────────────────────────────────────────────────────────────
#  PAGINA
# ─────────────────────────────────────────────────────────────
@dataclass
class Pagina:
    num_pagina: int
    def __str__(self) -> str:
        return f"Página {self.num_pagina}"

# ─────────────────────────────────────────────────────────────
#  PEQUIPO — página de un equipo
# ─────────────────────────────────────────────────────────────
@dataclass
class PaginaEquipo(Pagina):
    cod_pais: str = ""
    def __str__(self) -> str:
        return f"Página {self.num_pagina} — Equipo {self.cod_pais}"

# ─────────────────────────────────────────────────────────────
#  PEXTRA — página especial
# ─────────────────────────────────────────────────────────────
@dataclass
class PaginaExtra(Pagina):
    seccion: str = ""
    def __str__(self) -> str:
        return f"Página {self.num_pagina} — {self.seccion}"

# ─────────────────────────────────────────────────────────────
#  FIGURITA
# ─────────────────────────────────────────────────────────────
@dataclass
class Figurita:
    num_figura: int
    cod_pais: str
    num_pagina: int
    def __str__(self) -> str:
        return f"Figurita #{self.num_figura} ({self.cod_pais}) — Pág. {self.num_pagina}"

    def es_escudo(self) -> bool:
        if self.cod_pais == 'FWC':
            return False
        offset = (self.num_figura - 10) % 20
        return offset == 0

    def es_foto_equipo(self) -> bool:
        if self.cod_pais == 'FWC':
            return False
        offset = (self.num_figura - 10) % 20
        return offset == 12

# ─────────────────────────────────────────────────────────────
#  FJUGADOR — figurita de jugador
# ─────────────────────────────────────────────────────────────
@dataclass
class FiguritaJugador(Figurita):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    peso_kg: Optional[float] = None
    altura_m: Optional[float] = None
    anio_nacimiento: Optional[int] = None
    @property
    def nombre_completo(self) -> str:
        partes = [p for p in (self.nombre, self.apellido) if p]
        return " ".join(partes) if partes else "(sin nombre)"

    def __str__(self) -> str:
        return (
            f"Figurita #{self.num_figura} — {self.nombre_completo} "
            f"[{self.cod_pais}] Pág. {self.num_pagina}"
        )

# ─────────────────────────────────────────────────────────────
#  FESPECIAL — figurita especial
# ─────────────────────────────────────────────────────────────
@dataclass
class FiguritaEspecial(Figurita):
    tipo_especial: Optional[str] = None
    def __str__(self) -> str:
        tipo = self.tipo_especial or "Especial"
        return f"Figurita #{self.num_figura} — {tipo} [{self.cod_pais}] Pág. {self.num_pagina}"

# ─────────────────────────────────────────────────────────────
#  COLECCION — estado de la colección del usuario
# ─────────────────────────────────────────────────────────────
@dataclass
class ItemColeccion:
    num_figura: int
    cod_pais: str
    cantidad: int = 0
    pegada: bool = False
    @property
    def tiene(self) -> bool:
        return self.cantidad > 0

    @property
    def repetidas(self) -> int:
        return max(0, self.cantidad - 1)

    @property
    def estado(self) -> str:
        if self.cantidad == 0:
            return "❌ Falta"
        if self.pegada and self.cantidad == 1:
            return "✅ Pegada"
        if self.pegada and self.cantidad > 1:
            return f"✅ Pegada (+{self.repetidas} repetida{'s' if self.repetidas > 1 else ''})"
        if not self.pegada and self.cantidad == 1:
            return "📦 Tengo (sin pegar)"
        return f"📦 Tengo x{self.cantidad} ({self.repetidas} para intercambio)"

    def __str__(self) -> str:
        return f"#{self.num_figura} [{self.cod_pais}] — {self.estado}"

# ─────────────────────────────────────────────────────────────
#  RESUMEN DE COLECCION — agregado para mostrar en la UI
# ─────────────────────────────────────────────────────────────
@dataclass
class ResumenColeccion:
    total_figuritas: int = 980
    total_pegadas: int = 0
    total_tengo: int = 0
    total_faltan: int = 980
    total_repetidas: int = 0
    @property
    def porcentaje(self) -> float:
        if self.total_figuritas == 0:
            return 0.0
        return round((self.total_pegadas / self.total_figuritas) * 100, 1)

    def __str__(self) -> str:
        return (
            f"Álbum: {self.total_pegadas}/{self.total_figuritas} pegadas "
            f"({self.porcentaje}%) | "
            f"Tengo: {self.total_tengo} | "
            f"Faltan: {self.total_faltan} | "
            f"Repetidas: {self.total_repetidas}"
        )

# ─────────────────────────────────────────────────────────────
#  RESUMEN POR PAIS — para la vista de equipo en la UI
# ─────────────────────────────────────────────────────────────
@dataclass
class ResumenPais:
    cod_pais: str
    nombre_pais: str
    total: int = 20
    pegadas: int = 0
    tengo: int = 0
    faltan: int = 20
    repetidas: int = 0
    @property
    def porcentaje(self) -> float:
        if self.total == 0:
            return 0.0
        return round((self.pegadas / self.total) * 100, 1)

    @property
    def completo(self) -> bool:
        return self.pegadas == self.total

    def __str__(self) -> str:
        return (
            f"{self.nombre_pais} [{self.cod_pais}]: "
            f"{self.pegadas}/{self.total} ({self.porcentaje}%) | "
            f"Faltan: {self.faltan} | Repetidas: {self.repetidas}"
        )