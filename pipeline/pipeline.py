#!/usr/bin/env python3
"""Pipeline V1 de BeatGaler Marketing: seis modulos unidos por identificadores.

Solo biblioteca estandar. No inventa datos: valida enlaces, muestra arboles y
arma la parte numerica de un informe; la interpretacion la escribe una persona
o un agente, nunca este script.

    python pipeline/pipeline.py comprobar
    python pipeline/pipeline.py estado
    python pipeline/pipeline.py arbol M-001
    python pipeline/pipeline.py aprender X-001 [--escribir]

`--raiz` apunta a otra copia de la estructura (la de pruebas/circuito).
"""
import argparse
import csv
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
M1, M2, M3, M4, M5, M6 = ('1-investigacion', '2-razonamiento', '3-hipotesis-guiones',
                          '4-produccion', '5-medicion', '6-aprendizaje')
TABLAS = {
    'evidencia': (M1, 'evidencia.csv', 'EV'),
    'preguntas': (M1, 'preguntas.csv', 'Q'),
    'mecanismos': (M2, 'mecanismos.csv', 'M'),
    'nodos': (M2, 'nodos.csv', 'N'),
    'hipotesis': (M3, 'hipotesis.csv', 'H'),
    'guiones': (M3, 'guiones.csv', 'G'),
    'experimentos': (M3, 'experimentos.csv', 'X'),
    'piezas': (M4, 'piezas.csv', 'P'),
    'informes': (M6, 'informes.csv', 'A'),
}
TIPOS_EVIDENCIA = {'observacion', 'testimonio', 'fuente', 'resultado'}
RAMAS = {'mecanismo', 'audiencia', 'fallo', 'alternativas', 'camino'}
CIERRES_ANCLADOS = {'dato', 'fuente', 'testimonio'}
CIERRES_ABIERTOS = {'supuesto', 'no_sabemos'}
ROLES = {'prueba', 'contraste'}
PLATAFORMAS = {'instagram', 'tiktok'}
NUMERICOS = ['horas_desde_publicacion', 'vistas', 'retencion_3s_pct', 'skip_rate_pct', 'tiempo_medio_s',
             'completo_pct', 'likes', 'comentarios', 'comentarios_galer', 'guardados', 'envios', 'visitas_perfil']
# Con unas 100 vistas por pieza, una diferencia de retencion menor a ~20 puntos no se distingue del ruido.
VISTAS_MINIMAS_AVISO = 400


def leer(raiz, modulo, archivo):
    ruta = raiz / modulo / archivo
    if not ruta.exists():
        raise ValueError(f'Falta {ruta}')
    with ruta.open(encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))


def cargar(raiz):
    datos = {nombre: leer(raiz, mod, arch) for nombre, (mod, arch, _) in TABLAS.items()}
    datos['resultados'] = leer(raiz, M5, 'resultados.csv')
    return datos


def lista(valor):
    return [v for v in re.split(r'[;\s]+', valor or '') if v]


def comprobar(raiz):
    """Devuelve la lista de errores de trazabilidad; vacia si todo enlaza."""
    d, err = cargar(raiz), []
    es_prueba = (raiz / 'ES-PRUEBA').exists()
    ids = {}
    for nombre, (_, archivo, prefijo) in TABLAS.items():
        vistos = set()
        for fila in d[nombre]:
            i = fila.get('id', '')
            if not re.fullmatch(rf'(PRUEBA-)?{prefijo}-\d{{3,4}}(-\d{{2}})?', i):
                err.append(f'{archivo}: id invalido «{i}»')
            if i in vistos:
                err.append(f'{archivo}: id repetido {i}')
            vistos.add(i)
        ids[nombre] = vistos

    def existe(tabla, valor, donde):
        if valor not in ids[tabla]:
            err.append(f'{donde}: no existe {tabla} «{valor}»')

    for e in d['evidencia']:
        if e['tipo'] not in TIPOS_EVIDENCIA:
            err.append(f"evidencia {e['id']}: tipo «{e['tipo']}»")
        if not e['referencia'].strip() or not e['contenido'].strip():
            err.append(f"evidencia {e['id']}: falta referencia o contenido")
    hijos = {}
    for n in d['nodos']:
        hijos.setdefault(n['padre'], []).append(n['id'])
    for n in d['nodos']:
        donde = f"nodo {n['id']}"
        existe('mecanismos', n['mecanismo'], donde)
        if n['padre']:
            existe('nodos', n['padre'], donde)
        if n['rama'] not in RAMAS:
            err.append(f"{donde}: rama «{n['rama']}»")
        hoja = n['id'] not in hijos
        cierre = n['cierre']
        if hoja and cierre not in CIERRES_ANCLADOS | CIERRES_ABIERTOS:
            err.append(f'{donde}: es hoja y no declara en que termina')
        if not hoja and cierre:
            err.append(f'{donde}: tiene hijos y aun asi declara cierre')
        for ev in lista(n['evidencia']):
            existe('evidencia', ev, donde)
        for q in lista(n['pregunta_abierta']):
            existe('preguntas', q, donde)
        if cierre in CIERRES_ANCLADOS and not lista(n['evidencia']):
            err.append(f'{donde}: cierre «{cierre}» sin evidencia citada')
        if cierre in CIERRES_ABIERTOS and not lista(n['pregunta_abierta']):
            err.append(f'{donde}: cierre «{cierre}» sin pregunta abierta')
    for m in d['mecanismos']:
        ramas = {n['rama'] for n in d['nodos'] if n['mecanismo'] == m['id']}
        for falta in sorted(RAMAS - ramas):
            err.append(f"mecanismo {m['id']}: falta la rama «{falta}»")
    for h in d['hipotesis']:
        existe('mecanismos', h['mecanismo'], f"hipotesis {h['id']}")
        for n in lista(h['nodos']):
            existe('nodos', n, f"hipotesis {h['id']}")
        if not h['prediccion'].strip() or not h['refutacion'].strip():
            err.append(f"hipotesis {h['id']}: falta prediccion o refutacion")
    for g in d['guiones']:
        existe('hipotesis', g['hipotesis'], f"guion {g['id']}")
        if not (raiz / M3 / g['archivo']).exists():
            err.append(f"guion {g['id']}: no existe el archivo {g['archivo']}")
    for x in d['experimentos']:
        existe('hipotesis', x['hipotesis'], f"experimento {x['id']}")
    for p in d['piezas']:
        donde = f"pieza {p['id']}"
        existe('guiones', p['guion'], donde)
        existe('experimentos', p['experimento'], donde)
        if p['rol'] not in ROLES:
            err.append(f"{donde}: rol «{p['rol']}»")
    for i, r in enumerate(d['resultados'], start=2):
        donde = f'resultados.csv linea {i}'
        existe('piezas', r['pieza'], donde)
        if r['plataforma'] not in PLATAFORMAS:
            err.append(f"{donde}: plataforma «{r['plataforma']}»")
        esperado = 'PRUEBA' if es_prueba else 'real'
        if r['origen'] != esperado:
            err.append(f"{donde}: origen «{r['origen']}», aqui solo se admite «{esperado}»")
        if not r['fuente_dato'].strip():
            err.append(f'{donde}: falta de donde se leyo el dato')
        for campo in NUMERICOS:
            if r[campo].strip():
                try:
                    float(r[campo])
                except ValueError:
                    err.append(f'{donde}: {campo} no es un numero')
    for a in d['informes']:
        existe('experimentos', a['experimento'], f"informe {a['id']}")
        if not (raiz / M6 / a['archivo']).exists():
            err.append(f"informe {a['id']}: no existe el archivo {a['archivo']}")
    return err


def resumen_arbol(d, mecanismo):
    nodos = [n for n in d['nodos'] if n['mecanismo'] == mecanismo]
    padres = {n['padre'] for n in nodos}
    hojas = [n for n in nodos if n['id'] not in padres]
    cuenta = {}
    for h in hojas:
        cuenta[h['cierre']] = cuenta.get(h['cierre'], 0) + 1
    ancladas = sum(v for k, v in cuenta.items() if k in CIERRES_ANCLADOS)
    solidez = {e['id']: e['solidez'] for e in d['evidencia']}
    debiles = [h['id'] for h in hojas if h['cierre'] in CIERRES_ANCLADOS
               and all(solidez.get(ev) == 'texto_historico' for ev in lista(h['evidencia']))]
    return nodos, hojas, cuenta, ancladas, debiles


def arbol(raiz, mecanismo):
    d = cargar(raiz)
    m = next((m for m in d['mecanismos'] if m['id'] == mecanismo), None)
    if not m:
        raise ValueError(f'No existe el mecanismo {mecanismo}')
    nodos, hojas, cuenta, ancladas, debiles = resumen_arbol(d, mecanismo)
    lineas = [f"{m['id']} · {m['nombre']} ({m['estado']})", m['resumen'], '']

    def pinta(padre, nivel):
        for n in [n for n in nodos if n['padre'] == padre]:
            marca = f" [{n['cierre']}]" if n['cierre'] else ''
            refs = ' '.join(lista(n['evidencia']) + lista(n['pregunta_abierta']))
            lineas.append(f"{'  ' * nivel}- {n['id']} ({n['rama']}) {n['pregunta']}")
            lineas.append(f"{'  ' * nivel}  → {n['respuesta']}{marca}{' ' + refs if refs else ''}")
            pinta(n['id'], nivel + 1)

    pinta('', 0)
    total = len(hojas)
    pct = round(ancladas / total * 100, 1) if total else 0.0
    lineas += ['', f'Hojas: {total} | ancladas: {ancladas} ({pct}%) | ' +
               ', '.join(f'{k}: {v}' for k, v in sorted(cuenta.items()))]
    if debiles:
        lineas.append('Ancladas solo en texto historico (modelo, no evidencia empirica): ' + ', '.join(debiles))
    return '\n'.join(lineas)


def estado(raiz):
    d = cargar(raiz)
    err = comprobar(raiz)
    lineas = ['COMPROBACION: ' + ('sin errores' if not err else f'{len(err)} errores')]
    lineas.append(f"1 Investigacion: {len(d['evidencia'])} evidencias, "
                  f"{sum(1 for q in d['preguntas'] if q['estado'] == 'abierta')} preguntas abiertas")
    for m in d['mecanismos']:
        _, hojas, _, ancladas, _ = resumen_arbol(d, m['id'])
        lineas.append(f"2 Razonamiento: {m['id']} {m['nombre']}: {len(hojas)} hojas, {ancladas} ancladas")
    lineas.append(f"3 Hipotesis y guiones: {len(d['hipotesis'])} hipotesis, {len(d['guiones'])} guiones, "
                  f"{len(d['experimentos'])} experimentos")
    por_estado = {}
    for p in d['piezas']:
        por_estado[p['estado']] = por_estado.get(p['estado'], 0) + 1
    lineas.append('4 Produccion: ' + (', '.join(f'{v} {k}' for k, v in sorted(por_estado.items())) or 'sin piezas'))
    lineas.append(f"5 Medicion: {len(d['resultados'])} lecturas")
    lineas.append(f"6 Aprendizaje: {len(d['informes'])} informes")
    return '\n'.join(lineas), err


def num(fila, campo):
    valor = fila.get(campo, '').strip()
    return float(valor) if valor else None


def aprender(raiz, experimento):
    """Arma la parte numerica del informe. No concluye nada."""
    d = cargar(raiz)
    x = next((x for x in d['experimentos'] if x['id'] == experimento), None)
    if not x:
        raise ValueError(f'No existe el experimento {experimento}')
    h = next(h for h in d['hipotesis'] if h['id'] == x['hipotesis'])
    m = next(m for m in d['mecanismos'] if m['id'] == h['mecanismo'])
    piezas = {p['id']: p for p in d['piezas'] if p['experimento'] == experimento}
    lecturas = [r for r in d['resultados'] if r['pieza'] in piezas]
    es_prueba = (raiz / 'ES-PRUEBA').exists()
    out = [f'# Informe de aprendizaje — {experimento}', '']
    if es_prueba:
        out += ['**DATOS DE PRUEBA. Nada de este informe describe videos ni audiencia reales.**', '']
    out += [f"Hipotesis {h['id']} · mecanismo {m['id']} ({m['nombre']}) · contraste: {x['contraste']}", '']
    out += ['## 1. Que predijimos', '', h['prediccion'], '', f"Se refutaria si: {h['refutacion']}", '']
    out += ['## 2. Que ocurrio', '']
    avisos = []
    if not lecturas:
        out += ['Todavia no hay lecturas registradas para este experimento.', '']
    excluidas = [p['id'] for p in piezas.values() if p['ejecucion'].strip().lower().startswith('mal')]
    if excluidas:
        avisos.append('Piezas excluidas por mala ejecucion (no cuentan ni a favor ni en contra): ' + ', '.join(excluidas))
    for plataforma in sorted({r['plataforma'] for r in lecturas}):
        filas = [r for r in lecturas if r['plataforma'] == plataforma and r['pieza'] not in excluidas]
        ultima = {}
        for r in filas:  # la lectura mas tardia de cada pieza
            if r['pieza'] not in ultima or (num(r, 'horas_desde_publicacion') or 0) >= (num(ultima[r['pieza']], 'horas_desde_publicacion') or 0):
                ultima[r['pieza']] = r
        out += [f'### {plataforma}', '', '| Pieza | Rol | Cuerpo | Horas | Vistas | Retencion 3 s | Tiempo medio (s) | Comentarios GALER |',
                '| --- | --- | --- | --- | --- | --- | --- | --- |']
        for pid in sorted(ultima):
            r, p = ultima[pid], piezas[pid]
            out.append(f"| {pid} | {p['rol']} | {p['cuerpo']} | {r['horas_desde_publicacion']} | {r['vistas']} | "
                       f"{r['retencion_3s_pct']} | {r['tiempo_medio_s']} | {r['comentarios_galer']} |")
        out.append('')
        for cuerpo in sorted({piezas[pid]['cuerpo'] for pid in ultima}):
            grupo = {rol: [ultima[pid] for pid in ultima if piezas[pid]['cuerpo'] == cuerpo and piezas[pid]['rol'] == rol]
                     for rol in ROLES}
            if not grupo['prueba'] or not grupo['contraste']:
                avisos.append(f'{plataforma}/{cuerpo}: no hay prueba y contraste sobre el mismo cuerpo; no se comparan')
                continue
            for campo, etiqueta in (('retencion_3s_pct', 'retencion a 3 s (puntos)'), ('tiempo_medio_s', 'tiempo medio (s)')):
                a = [num(r, campo) for r in grupo['prueba'] if num(r, campo) is not None]
                b = [num(r, campo) for r in grupo['contraste'] if num(r, campo) is not None]
                if a and b:
                    dif = round(sum(a) / len(a) - sum(b) / len(b), 1)
                    out.append(f'- {cuerpo}, {etiqueta}: prueba menos contraste = {dif:+} '
                               f'({len(a)} contra {len(b)} piezas)')
            horas = [num(r, 'horas_desde_publicacion') for rol in ROLES for r in grupo[rol]
                     if num(r, 'horas_desde_publicacion') is not None]
            if horas and max(horas) - min(horas) > 12:
                avisos.append(f'{plataforma}/{cuerpo}: las lecturas se tomaron con mas de 12 horas de diferencia')
            pocas = [r['pieza'] for rol in ROLES for r in grupo[rol] if (num(r, 'vistas') or 0) < VISTAS_MINIMAS_AVISO]
            if pocas:
                avisos.append(f'{plataforma}/{cuerpo}: piezas con menos de {VISTAS_MINIMAS_AVISO} vistas '
                              f'({", ".join(sorted(pocas))}); una diferencia pequena no se distingue del ruido')
        out.append('')
    out += ['## 3. Que explicacion propusimos', '', m['resumen'], '']
    out += ['## 4. Que evidencia respalda esa explicacion', '', 'PENDIENTE de redactar. Los numeros de arriba son un resultado observado, no una explicacion.', '']
    out += ['## 5. Que otras explicaciones siguen siendo posibles', '']
    out += [f'- {a}' for a in avisos]
    out += ['- Primer cuadro, duracion, horario, audiencia a la que la plataforma lo repartio y repeticion del cuerpo: revisar una por una.', '']
    out += ['## 6. Que aprendimos realmente', '', 'PENDIENTE. «Todavia no sabemos» es una respuesta valida.', '']
    out += ['## 7. Que preguntas nuevas aparecieron', '', 'PENDIENTE. Cada una se registra en 1-investigacion/preguntas.csv.', '']
    out += ['## 8. Que deberiamos probar despues', '', 'PENDIENTE.', '']
    return '\n'.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Pipeline V1 de BeatGaler Marketing')
    ap.add_argument('--raiz', type=Path, default=RAIZ)
    sub = ap.add_subparsers(dest='orden', required=True)
    sub.add_parser('comprobar')
    sub.add_parser('estado')
    a = sub.add_parser('arbol')
    a.add_argument('mecanismo')
    l = sub.add_parser('aprender')
    l.add_argument('experimento')
    l.add_argument('--escribir', action='store_true', help='guarda el borrador en 6-aprendizaje/informes/ si no existe')
    args = ap.parse_args(argv)
    try:
        if args.orden == 'comprobar':
            err = comprobar(args.raiz)
            print('\n'.join(err) if err else 'COMPROBACION: todo enlaza, sin errores')
            return 1 if err else 0
        if args.orden == 'estado':
            texto, err = estado(args.raiz)
            print(texto)
            return 1 if err else 0
        if args.orden == 'arbol':
            print(arbol(args.raiz, args.mecanismo))
        if args.orden == 'aprender':
            texto = aprender(args.raiz, args.experimento)
            if args.escribir:
                destino = args.raiz / M6 / 'informes' / f'borrador-{args.experimento}.md'
                if destino.exists():
                    raise ValueError(f'Ya existe {destino}; no se sobrescribe')
                destino.write_text(texto + '\n', encoding='utf-8')
                print(f'Borrador guardado en {destino}')
            else:
                print(texto)
    except (ValueError, KeyError, StopIteration) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
