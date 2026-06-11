# ============================================================
#  Capa de acceso a datos (DAL).
#  Todas las operaciones SQL del proyecto pasan por aquí.
#  La GUI y el exporter solo llaman funciones de este módulo.
# ============================================================

import sqlite3
from typing import Optional
from models.models import (
    Pais,
    Figurita,
    FiguritaJugador,
    FiguritaEspecial,
    ItemColeccion,
    ResumenColeccion,
    ResumenPais,
)
from database.database import get_connection

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 1 — CONSULTAS DE CATÁLOGO 
# ══════════════════════════════════════════════════════════════

def obtener_todos_los_paises() -> list[Pais]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT codPais, nombre
            FROM PAIS
            WHERE codPais != 'FWC' AND codPais != 'CCL'
            ORDER BY nombre
        """).fetchall()
    return [Pais(cod_pais=r["codPais"], nombre=r["nombre"]) for r in rows]

def obtener_pais(cod_pais: str) -> Optional[Pais]:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT codPais, nombre FROM PAIS WHERE codPais = ?
        """, (cod_pais,)).fetchone()
    if row is None:
        return None
    return Pais(cod_pais=row["codPais"], nombre=row["nombre"])

def obtener_figuritas_de_pais(cod_pais: str) -> list[Figurita]:
    figuritas: list[Figurita] = []
    with get_connection() as conn:
        rows_base = conn.execute("""
            SELECT f.numFigura, f.codPais, f.numPagina
            FROM FIGURITA f
            WHERE f.codPais = ?
            ORDER BY f.numFigura
        """, (cod_pais,)).fetchall()
        for row in rows_base:
            num = row["numFigura"]
            pais = row["codPais"]
            pagina = row["numPagina"]
            jugador = conn.execute("""
                SELECT nombre, apellido, pesoKg, alturaM, anioNacimiento
                FROM FJUGADOR
                WHERE numFigura = ? AND codPais = ?
            """, (num, pais)).fetchone()
            if jugador:
                figuritas.append(FiguritaJugador(
                    num_figura=num,
                    cod_pais=pais,
                    num_pagina=pagina,
                    nombre=jugador["nombre"],
                    apellido=jugador["apellido"],
                    peso_kg=jugador["pesoKg"],
                    altura_m=jugador["alturaM"],
                    anio_nacimiento=jugador["anioNacimiento"],
                ))
                continue
            especial = conn.execute("""
                SELECT tipoEspecial
                FROM FESPECIAL
                WHERE numFigura = ? AND codPais = ?
            """, (num, pais)).fetchone()
            if especial:
                figuritas.append(FiguritaEspecial(
                    num_figura=num,
                    cod_pais=pais,
                    num_pagina=pagina,
                    tipo_especial=especial["tipoEspecial"],
                ))
                continue
            figuritas.append(Figurita(
                num_figura=num,
                cod_pais=pais,
                num_pagina=pagina,
            ))
    return figuritas

def obtener_figurita(num_figura: int, cod_pais: str) -> Optional[Figurita]:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT f.numFigura, f.codPais, f.numPagina,
                   j.nombre, j.apellido, j.pesoKg, j.alturaM, j.anioNacimiento,
                   e.tipoEspecial
            FROM FIGURITA f
            LEFT JOIN FJUGADOR  j ON (f.numFigura = j.numFigura AND f.codPais = j.codPais)
            LEFT JOIN FESPECIAL e ON (f.numFigura = e.numFigura AND f.codPais = e.codPais)
            WHERE f.numFigura = ? AND f.codPais = ?
        """, (num_figura, cod_pais)).fetchone()
    if row is None:
        return None
    if row["nombre"] or row["apellido"]:
        return FiguritaJugador(
            num_figura=row["numFigura"], cod_pais=row["codPais"],
            num_pagina=row["numPagina"], nombre=row["nombre"],
            apellido=row["apellido"], peso_kg=row["pesoKg"],
            altura_m=row["alturaM"], anio_nacimiento=row["anioNacimiento"],
        )
    if row["tipoEspecial"]:
        return FiguritaEspecial(
            num_figura=row["numFigura"], cod_pais=row["codPais"],
            num_pagina=row["numPagina"], tipo_especial=row["tipoEspecial"],
        )
    return Figurita(num_figura=row["numFigura"], cod_pais=row["codPais"],
                    num_pagina=row["numPagina"])

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 2 — GESTIÓN DE LA COLECCIÓN DEL USUARIO
# ══════════════════════════════════════════════════════════════

def agregar_figurita(num_figura: int, cod_pais: str, cantidad: int = 1) -> bool:
    if cantidad < 1:
        raise ValueError("La cantidad debe ser al menos 1.")
    with get_connection() as conn:
        existe = conn.execute("""
            SELECT 1 FROM FIGURITA WHERE numFigura = ? AND codPais = ?
        """, (num_figura, cod_pais)).fetchone()
        if existe is None:
            return False
        conn.execute("""
            INSERT OR IGNORE INTO COLECCION (numFigura, codPais, cantidad, pegada)
            VALUES (?, ?, 0, 0)
        """, (num_figura, cod_pais))
        conn.execute("""
            UPDATE COLECCION
            SET cantidad = cantidad + ?
            WHERE numFigura = ? AND codPais = ?
        """, (cantidad, num_figura, cod_pais))
    return True

def quitar_figurita(num_figura: int, cod_pais: str, cantidad: int = 1) -> bool:
    if cantidad < 1:
        raise ValueError("La cantidad debe ser al menos 1.")
    with get_connection() as conn:
        existe = conn.execute("""
            SELECT cantidad FROM COLECCION
            WHERE numFigura = ? AND codPais = ?
        """, (num_figura, cod_pais)).fetchone()
        if existe is None:
            return False
        nueva_cantidad = max(0, existe["cantidad"] - cantidad)
        conn.execute("""
            UPDATE COLECCION
            SET cantidad = ?,
                pegada   = CASE WHEN ? = 0 THEN 0 ELSE pegada END
            WHERE numFigura = ? AND codPais = ?
        """, (nueva_cantidad, nueva_cantidad, num_figura, cod_pais))
    return True

def marcar_pegada(num_figura: int, cod_pais: str, pegada: bool = True) -> bool:
    with get_connection() as conn:
        item = conn.execute("""
            SELECT cantidad FROM COLECCION
            WHERE numFigura = ? AND codPais = ?
        """, (num_figura, cod_pais)).fetchone()
        if item is None or item["cantidad"] == 0:
            return False
        conn.execute("""
            UPDATE COLECCION
            SET pegada = ?
            WHERE numFigura = ? AND codPais = ?
        """, (1 if pegada else 0, num_figura, cod_pais))
    return True

def obtener_item_coleccion(num_figura: int, cod_pais: str) -> ItemColeccion:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT cantidad, pegada FROM COLECCION
            WHERE numFigura = ? AND codPais = ?
        """, (num_figura, cod_pais)).fetchone()
    if row is None:
        return ItemColeccion(num_figura=num_figura, cod_pais=cod_pais, cantidad=0, pegada=False)
    return ItemColeccion(
        num_figura=num_figura,
        cod_pais=cod_pais,
        cantidad=row["cantidad"],
        pegada=bool(row["pegada"]),
    )

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 3 — CONSULTAS PRINCIPALES DE LA APP
# ══════════════════════════════════════════════════════════════

def obtener_faltantes(cod_pais: Optional[str] = None) -> list[dict]:
    filtro_pais = "AND f.codPais = :pais" if cod_pais else ""
    params: dict = {"pais": cod_pais} if cod_pais else {}
    query = f"""
        SELECT
            f.numFigura      AS num_figura,
            f.codPais        AS cod_pais,
            p.nombre         AS nombre_pais,
            j.nombre         AS nombre_jugador,
            j.apellido       AS apellido_jugador,
            e.tipoEspecial   AS tipo_especial,
            f.numPagina      AS num_pagina
        FROM FIGURITA f
        JOIN PAIS p ON f.codPais = p.codPais
        LEFT JOIN FJUGADOR  j ON (f.numFigura = j.numFigura AND f.codPais = j.codPais)
        LEFT JOIN FESPECIAL e ON (f.numFigura = e.numFigura AND f.codPais = e.codPais)
        LEFT JOIN COLECCION c ON (f.numFigura = c.numFigura AND f.codPais = c.codPais)
        WHERE (c.numFigura IS NULL OR c.cantidad = 0)
        {filtro_pais}
        ORDER BY p.nombre, f.numFigura
    """
    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()
    return [dict(row) for row in rows]

def obtener_repetidas(cod_pais: Optional[str] = None) -> list[dict]:
    filtro_pais = "AND f.codPais = :pais" if cod_pais else ""
    params: dict = {"pais": cod_pais} if cod_pais else {}
    query = f"""
        SELECT
            c.numFigura              AS num_figura,
            c.codPais                AS cod_pais,
            p.nombre                 AS nombre_pais,
            j.nombre                 AS nombre_jugador,
            j.apellido               AS apellido_jugador,
            e.tipoEspecial           AS tipo_especial,
            c.cantidad               AS cantidad,
            (c.cantidad - 1)         AS disponibles
        FROM COLECCION c
        JOIN FIGURITA f ON (c.numFigura = f.numFigura AND c.codPais = f.codPais)
        JOIN PAIS     p ON f.codPais = p.codPais
        LEFT JOIN FJUGADOR  j ON (c.numFigura = j.numFigura AND c.codPais = j.codPais)
        LEFT JOIN FESPECIAL e ON (c.numFigura = e.numFigura AND c.codPais = e.codPais)
        WHERE c.cantidad > 1
        {filtro_pais}
        ORDER BY p.nombre, c.numFigura
    """
    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()
    return [dict(row) for row in rows]

def obtener_coleccion_completa(cod_pais: Optional[str] = None) -> list[dict]:
    filtro_pais = "WHERE f.codPais = :pais" if cod_pais else ""
    params: dict = {"pais": cod_pais} if cod_pais else {}
    query = f"""
        SELECT
            f.numFigura              AS num_figura,
            f.codPais                AS cod_pais,
            p.nombre                 AS nombre_pais,
            j.nombre                 AS nombre_jugador,
            j.apellido               AS apellido_jugador,
            e.tipoEspecial           AS tipo_especial,
            f.numPagina              AS num_pagina,
            COALESCE(c.cantidad, 0)  AS cantidad,
            COALESCE(c.pegada,   0)  AS pegada
        FROM FIGURITA f
        JOIN PAIS p ON f.codPais = p.codPais
        LEFT JOIN FJUGADOR  j ON (f.numFigura = j.numFigura AND f.codPais = j.codPais)
        LEFT JOIN FESPECIAL e ON (f.numFigura = e.numFigura AND f.codPais = e.codPais)
        LEFT JOIN COLECCION c ON (f.numFigura = c.numFigura AND f.codPais = c.codPais)
        {filtro_pais}
        ORDER BY p.nombre, f.numFigura
    """
    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()
    return [dict(row) for row in rows]

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 4 — ESTADÍSTICAS Y RESÚMENES
# ══════════════════════════════════════════════════════════════

def obtener_resumen_global() -> ResumenColeccion:
    with get_connection() as conn:
        total = conn.execute("SELECT COUNT(*) AS n FROM FIGURITA").fetchone()["n"]
        stats = conn.execute("""
            SELECT
                COUNT(CASE WHEN pegada   = 1               THEN 1 END) AS pegadas,
                COUNT(CASE WHEN cantidad > 0               THEN 1 END) AS tengo,
                SUM (CASE WHEN cantidad > 1 THEN cantidad - 1 ELSE 0 END) AS repetidas
            FROM COLECCION
        """).fetchone()
    pegadas   = stats["pegadas"]   or 0
    tengo     = stats["tengo"]     or 0
    repetidas = stats["repetidas"] or 0
    faltan    = total - tengo
    return ResumenColeccion(
        total_figuritas=total,
        total_pegadas=pegadas,
        total_tengo=tengo,
        total_faltan=faltan,
        total_repetidas=repetidas,
    )

def obtener_resumen_por_pais() -> list[ResumenPais]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT
                p.codPais                                                       AS cod_pais,
                p.nombre                                                        AS nombre_pais,
                COUNT(f.numFigura)                                              AS total,
                COUNT(CASE WHEN c.pegada   = 1               THEN 1 END)       AS pegadas,
                COUNT(CASE WHEN c.cantidad > 0               THEN 1 END)       AS tengo,
                SUM (CASE WHEN c.cantidad > 1 THEN c.cantidad - 1 ELSE 0 END)  AS repetidas
            FROM PAIS p
            JOIN FIGURITA f ON p.codPais = f.codPais
            LEFT JOIN COLECCION c ON (f.numFigura = c.numFigura AND f.codPais = c.codPais)
            WHERE p.codPais != 'FWC' AND p.codPais != 'CCL'
            GROUP BY p.codPais, p.nombre
            ORDER BY pegadas DESC, p.nombre
        """).fetchall()
    resultado = []
    for r in rows:
        total     = r["total"]
        pegadas   = r["pegadas"]   or 0
        tengo     = r["tengo"]     or 0
        repetidas = r["repetidas"] or 0
        faltan    = total - tengo
        resultado.append(ResumenPais(
            cod_pais=r["cod_pais"],
            nombre_pais=r["nombre_pais"],
            total=total,
            pegadas=pegadas,
            tengo=tengo,
            faltan=faltan,
            repetidas=repetidas,
        ))
    return resultado

def obtener_resumen_pais(cod_pais: str) -> Optional[ResumenPais]:
    todos = obtener_resumen_por_pais()
    for rp in todos:
        if rp.cod_pais == cod_pais:
            return rp
    return None

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 5 — OPERACIONES EN LOTE (BULK)
#  Para la carga inicial de figuritas desde la UI.
# ══════════════════════════════════════════════════════════════

def agregar_figuritas_bulk(items: list[tuple[int, str, int]]) -> dict:
    exitosos = 0
    fallidos: list[tuple[int, str]] = []
    with get_connection() as conn:
        for num_figura, cod_pais, cantidad in items:
            existe = conn.execute("""
                SELECT 1 FROM FIGURITA WHERE numFigura = ? AND codPais = ?
            """, (num_figura, cod_pais)).fetchone()
            if existe is None:
                fallidos.append((num_figura, cod_pais))
                continue
            conn.execute("""
                INSERT OR IGNORE INTO COLECCION (numFigura, codPais, cantidad, pegada)
                VALUES (?, ?, 0, 0)
            """, (num_figura, cod_pais))
            conn.execute("""
                UPDATE COLECCION
                SET cantidad = cantidad + ?
                WHERE numFigura = ? AND codPais = ?
            """, (cantidad, num_figura, cod_pais))
            exitosos += 1
    return {"exitosos": exitosos, "fallidos": fallidos}

def marcar_pegadas_bulk(items: list[tuple[int, str]]) -> int:
    marcadas = 0
    with get_connection() as conn:
        for num_figura, cod_pais in items:
            cursor = conn.execute("""
                UPDATE COLECCION
                SET pegada = 1
                WHERE numFigura = ? AND codPais = ? AND cantidad > 0
            """, (num_figura, cod_pais))
            marcadas += cursor.rowcount
    return marcadas

def resetear_coleccion() -> None:
    with get_connection() as conn:
        conn.execute("DELETE FROM COLECCION")

# ══════════════════════════════════════════════════════════════
#  SECCIÓN 6 — BÚSQUEDA
# ══════════════════════════════════════════════════════════════

def buscar_figuritas(termino: str) -> list[dict]:
    if len(termino.strip()) < 2:
        return []
    patron = f"%{termino.strip()}%"
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT
                f.numFigura              AS num_figura,
                f.codPais                AS cod_pais,
                p.nombre                 AS nombre_pais,
                j.nombre                 AS nombre_jugador,
                j.apellido               AS apellido_jugador,
                e.tipoEspecial           AS tipo_especial,
                f.numPagina              AS num_pagina,
                COALESCE(c.cantidad, 0)  AS cantidad,
                COALESCE(c.pegada,   0)  AS pegada
            FROM FIGURITA f
            JOIN PAIS p ON f.codPais = p.codPais
            LEFT JOIN FJUGADOR  j ON (f.numFigura = j.numFigura AND f.codPais = j.codPais)
            LEFT JOIN FESPECIAL e ON (f.numFigura = e.numFigura AND f.codPais = e.codPais)
            LEFT JOIN COLECCION c ON (f.numFigura = c.numFigura AND f.codPais = c.codPais)
            WHERE
                j.nombre       LIKE :p OR
                j.apellido     LIKE :p OR
                p.nombre       LIKE :p OR
                e.tipoEspecial LIKE :p OR
                CAST(f.numFigura AS TEXT) = :exacto
            ORDER BY p.nombre, f.numFigura
            LIMIT 100
        """, {"p": patron, "exacto": termino.strip()}).fetchall()
    return [dict(row) for row in rows]